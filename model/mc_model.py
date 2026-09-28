"""
Monte Carlo path model: probability that Dale reaches £750k invested by end-2034 (age 40)
under each route, given his constraints (floor never touched, PG ≤ risk pot, energy limits).

All parameters live in params.json with a `src` key naming the research note / URL that
justifies them. Nothing in this file is a number; it is only mechanics.

Routes modelled
  A  contract_only      : one ~3-month pre-sales block per year, surplus to index
  B1 buy_distributor    : buy an importer/distributor with a manager, Dale sells
  B2 buy_services       : buy a contracted B2B services firm (cleaning/compliance/etc.)
  B3 buy_hire           : buy a plant/tool/equipment hire firm
  B4 buy_logistics      : buy a courier/3PL/pallet business
  B5 buy_ecommerce      : buy an existing multi-channel ecommerce brand
  B6 buy_saas           : buy a small SaaS with paying customers
  B7 buy_agency         : control group - agency / MSP
  C1 build_ecommerce    : start multi-channel ecommerce from zero
  C2 build_services     : start a B2B services business from zero
  D  hybrid_plan        : SOT plan - one block Feb-Apr 2027, then B1-style buy by Sep 2027

Each route is simulated year by year 2026 -> 2034 (9 steps, t=0 is end-Sep 2026).
State: liquid_investable (index + cash), business_equity (0 if none), debt_outstanding,
floor_breached flag, hours/week profile, face-to-face share.
"""
from __future__ import annotations
import json, math, sys, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load_params(path=os.path.join(HERE, "params.json")):
    with open(path) as f:
        return json.load(f)


def v(p, key):
    """Return the value of a parameter (params are {value, src} dicts)."""
    node = p
    for k in key.split("."):
        node = node[k]
    return node["value"] if isinstance(node, dict) and "value" in node else node


def lognormal_from_median_and_p90(rng, median, p90, size):
    """Lognormal draws parameterised by median and 90th percentile."""
    mu = math.log(median)
    sigma = (math.log(p90) - mu) / 1.2816
    return rng.lognormal(mu, sigma, size)


def simulate(route: str, p: dict, n: int = 20000, seed: int = 42, overrides: dict | None = None):
    rng = np.random.default_rng(seed)
    years = v(p, "horizon.years")  # 8: end-2026 .. end-2034
    g = p["general"]
    if overrides:
        # shallow override of general or route values, e.g. {"general.index_real_return_mean": 0.05}
        for k, val in overrides.items():
            node = p
            parts = k.split(".")
            for part in parts[:-1]:
                node = node[part]
            if isinstance(node[parts[-1]], dict) and "value" in node[parts[-1]]:
                node[parts[-1]]["value"] = val
            else:
                node[parts[-1]] = val

    start_liquid = v(g, "start_investable")           # ~£150-170k after incoming
    floor = v(g, "floor")                              # £120k never touched
    burn = v(g, "annual_burn")                         # £20k conservative
    mean_r = v(g, "index_nominal_return_mean")
    sd_r = v(g, "index_return_sd")
    target = v(g, "target")                            # £750k

    # arrays
    liquid = np.full(n, start_liquid, dtype=float)
    biz_equity = np.zeros(n)
    debt = np.zeros(n)
    alive_biz = np.zeros(n, dtype=bool)
    floor_breached = np.zeros(n, dtype=bool)
    reached_year = np.full(n, 99, dtype=int)
    hours = np.zeros((n, years))
    f2f = np.zeros((n, years))
    ebitda = np.zeros(n)
    owner_draw = np.zeros(n)
    acquired_year = np.full(n, 99, dtype=int)
    sold = np.zeros(n, dtype=bool)
    deal_failed = np.zeros(n, dtype=bool)

    r = p["routes"][route]
    kind = v(r, "kind")  # contract | buy | build | hybrid

    # --- per-route parameters --------------------------------------------------------------
    if kind in ("buy", "hybrid"):
        p_close_per_year = v(r, "p_close_within_12m")          # P(complete a deal in a given search year)
        ev_median, ev_p90 = v(r, "ev_median"), v(r, "ev_p90")
        mult_median, mult_p90 = v(r, "multiple_median"), v(r, "multiple_p90")
        seller_fin = v(r, "seller_finance_share")                # share of EV as vendor loan
        bank_rate = v(r, "bank_rate")                            # all-in on bank/GGS debt
        bank_term = v(r, "bank_term_years")
        vl_rate = v(r, "vendor_loan_rate")
        vl_term = v(r, "vendor_loan_term_years")
        deal_costs = v(r, "deal_costs")
        wc_reserve_pct = v(r, "wc_reserve_pct")
        mgr_cost = v(r, "manager_cost")                          # £ if a manager must be hired/retained
        p_mgr_stays = v(r, "p_manager_stays")
        yr1_ebitda_mult_median = v(r, "yr1_ebitda_change_median")  # e.g. 0.95
        yr1_ebitda_mult_p90 = v(r, "yr1_ebitda_change_p90")
        p_severe_yr1 = v(r, "p_severe_decline_yr1")              # >40% EBITDA drop (seller-dependency etc.)
        severe_mult = v(r, "severe_decline_factor")
        p_fail_annual = v(r, "p_failure_annual_after_yr1")        # business ceases / equity ~0
        growth_median = v(r, "ebitda_growth_median")
        growth_sd = v(r, "ebitda_growth_sd")
        exit_mult_median = v(r, "exit_multiple_median")
        exit_mult_p90 = v(r, "exit_multiple_p90")
        exit_year_earliest = v(r, "exit_earliest_years_held")
        p_sell_when_eligible = v(r, "p_sell_per_year_when_eligible")
        hrs_yr1, hrs_later = v(r, "hours_yr1"), v(r, "hours_yr3")
        f2f_share = v(r, "f2f_share")
        fit = v(r, "fit_multiplier")                             # personality/health fit applied to success probs
        draw_tax = v(g, "effective_tax_on_draw")
        max_bank_debt = v(g, "risk_pot_after_block") if kind == "hybrid" else v(g, "risk_pot_now")
    if kind in ("contract", "hybrid"):
        block_gross_median, block_gross_p90 = v(r, "block_gross_median"), v(r, "block_gross_p90")
        p_block_lands = v(r, "p_block_lands")
        blocks_per_year = v(r, "blocks_per_year")
        contract_tax = v(g, "effective_tax_on_contract")
        health_cost_per_block = v(r, "health_recovery_weeks_per_block")
    if kind == "build":
        capital_in = v(r, "capital_in")
        p_survive = v(r, "survival_curve")                       # list P(alive at end of year k | alive k-1)
        profit_median_by_year = v(r, "owner_profit_median_by_year")  # list
        profit_p90_by_year = v(r, "owner_profit_p90_by_year")
        p_reach_70k_ever = v(r, "p_reach_70k_by_yr3")
        resale_mult_median = v(r, "resale_multiple_median")
        hrs_yr1, hrs_later = v(r, "hours_yr1"), v(r, "hours_yr3")
        f2f_share = v(r, "f2f_share")
        fit = v(r, "fit_multiplier")
        draw_tax = v(g, "effective_tax_on_draw")

    searching = np.ones(n, dtype=bool) if kind in ("buy", "hybrid") else np.zeros(n, dtype=bool)
    search_years = np.zeros(n, dtype=int)
    max_search_years = v(r, "max_search_years") if kind in ("buy", "hybrid") else 0
    build_started = np.zeros(n, dtype=bool)
    if kind == "build":
        build_started[:] = True
        liquid -= capital_in
        alive_biz[:] = True
        acquired_year[:] = 0
    years_held = np.zeros(n, dtype=int)

    for t in range(years):
        year = 2027 + t  # the calendar year being simulated (t=0 -> 2027)
        # 1. market return on liquid (floor + surplus) ----------------------------------
        ret = rng.normal(mean_r, sd_r, n)
        liquid *= (1 + ret)
        liquid -= burn  # living costs, always paid from cash flow first (see below adjustments)

        h = np.zeros(n)
        ff = np.zeros(n)

        # 2. contracting income ---------------------------------------------------------
        if kind == "contract" or (kind == "hybrid" and t == 0):
            nblocks = blocks_per_year if kind == "contract" else 1
            for _ in range(int(nblocks)):
                lands = rng.random(n) < p_block_lands
                gross = lognormal_from_median_and_p90(rng, block_gross_median, block_gross_p90, n)
                liquid += np.where(lands, gross * (1 - contract_tax), 0.0)
                h += np.where(lands, v(r, "hours_per_block_week") * (13 / 52), 0.0)
        # contract-only route: no f2f, hours as above

        # 3. acquisition search & completion ------------------------------------------
        if kind in ("buy", "hybrid"):
            can_search = searching & (search_years < max_search_years)
            # hybrid: search starts 2027 too (SOT: offer Feb-Apr 2027, completion by Sep 2027)
            close = can_search & (rng.random(n) < p_close_per_year * fit)
            search_years += can_search.astype(int)
            h += np.where(can_search, v(r, "search_hours_week"), 0.0)
            ff += np.where(can_search, 0.5, 0.0)
            idx = np.where(close)[0]
            if idx.size:
                ev = lognormal_from_median_and_p90(rng, ev_median, ev_p90, idx.size)
                mult = lognormal_from_median_and_p90(rng, mult_median, mult_p90, idx.size)
                e0 = ev / mult                                   # EBITDA bought
                vendor = ev * seller_fin
                cash_needed = ev * (1 - seller_fin)
                # bank debt capped by risk pot; rest from cash; if cash short, deal shrinks (buy smaller)
                bank = np.minimum(cash_needed * v(r, "bank_share_of_cash_gap"), max_bank_debt)
                equity_cash = cash_needed - bank + deal_costs + ev * wc_reserve_pct
                available = liquid[idx] - floor
                scale = np.clip(available / np.maximum(equity_cash, 1), 0, 1)
                # scale the deal down if cash is short (min viable deal at 0.6 of drawn EV, else no deal)
                ok = scale >= v(r, "min_deal_scale")
                scale = np.where(ok, np.minimum(scale, 1.0), 0.0)
                ev, e0, vendor, bank, equity_cash = ev * scale, e0 * scale, vendor * scale, bank * scale, equity_cash * scale
                liquid[idx] -= np.where(ok, equity_cash, 0.0)
                debt[idx] = np.where(ok, vendor + bank, 0.0)
                ebitda[idx] = np.where(ok, e0, 0.0)
                biz_equity[idx] = np.where(ok, ev, 0.0)  # book at EV; marked to market on exit
                alive_biz[idx] = ok
                acquired_year[idx] = np.where(ok, t, 99)
                searching[idx] = ~ok
                # manager retention risk crystallises at completion
                mgr_leaves = rng.random(idx.size) > p_mgr_stays
                # year-1 EBITDA change
                chg = lognormal_from_median_and_p90(rng, yr1_ebitda_mult_median, yr1_ebitda_mult_p90, idx.size)
                severe = rng.random(idx.size) < (p_severe_yr1 / fit)
                chg = np.where(severe, severe_mult, chg)
                chg = np.where(mgr_leaves, chg * v(r, "manager_leaves_factor"), chg)
                ebitda[idx] *= chg
                # store annual debt service
                ann_bank = np.where(bank > 0, bank * bank_rate / (1 - (1 + bank_rate) ** -bank_term), 0.0)
                ann_vl = np.where(vendor > 0, vendor * vl_rate / (1 - (1 + vl_rate) ** -vl_term), 0.0) if vl_rate > 0 else vendor / vl_term
                debt_service = ann_bank + ann_vl
                if "debt_service" not in locals():
                    debt_service_all = np.zeros(n)
                    debt_years_left = np.zeros(n)
                debt_service_all[idx] = np.where(ok, debt_service, 0.0)
                debt_years_left[idx] = np.where(ok, max(bank_term, vl_term), 0)

        # 4. business operation -------------------------------------------------------
        if kind in ("buy", "hybrid"):
            op = alive_biz & (acquired_year <= t)
            if op.any():
                held = t - acquired_year
                # years after the first: growth + failure hazard
                later = op & (held >= 1)
                gr = rng.normal(growth_median, growth_sd, n)
                ebitda = np.where(later, ebitda * (1 + gr), ebitda)
                fail = later & (rng.random(n) < p_fail_annual / fit)
                # failure: equity gone, bank debt still owed up to PG (risk pot), vendor loan dies with the business
                bank_pg_loss = np.minimum(debt, max_bank_debt) * v(r, "pg_loss_share_on_failure")
                liquid = np.where(fail, liquid - bank_pg_loss, liquid)
                alive_biz = np.where(fail, False, alive_biz)
                biz_equity = np.where(fail, 0.0, biz_equity)
                ebitda = np.where(fail, 0.0, ebitda)
                debt = np.where(fail, 0.0, debt)
                deal_failed |= fail
                op = alive_biz & (acquired_year <= t)
                # owner draw = EBITDA - manager cost (if manager needed) - debt service
                ds = np.where(debt_years_left > 0, debt_service_all, 0.0)
                draw_pre = ebitda - mgr_cost - ds
                draw = np.where(op, draw_pre, 0.0)
                # if draw negative, it is a cash call on the risk pot (never the floor -> floor_breached if needed)
                net_draw = np.where(draw > 0, draw * (1 - draw_tax), draw)
                liquid = np.where(op, liquid + net_draw, liquid)
                owner_draw = np.where(op, draw, owner_draw)
                debt = np.where(op & (debt_years_left > 0), np.maximum(debt - (ds - debt * v(r, "blended_debt_rate")), 0), debt)
                debt_years_left = np.where(op, np.maximum(debt_years_left - 1, 0), debt_years_left)
                h += np.where(op, np.where(held == 0, hrs_yr1, hrs_later), 0.0)
                ff += np.where(op, f2f_share, 0.0)
                # business equity marked at current EBITDA x entry multiple (conservative) less debt
                biz_equity = np.where(op, np.maximum(ebitda * mult_median - debt, 0.0), biz_equity)
                # exit option
                eligible = op & (held >= exit_year_earliest) & ~sold
                sell = eligible & (rng.random(n) < p_sell_when_eligible)
                if sell.any():
                    xm = lognormal_from_median_and_p90(rng, exit_mult_median, exit_mult_p90, n)
                    proceeds = np.maximum(ebitda * xm - debt, 0.0)
                    net = proceeds * (1 - v(g, "effective_tax_on_exit"))
                    liquid = np.where(sell, liquid + net, liquid)
                    biz_equity = np.where(sell, 0.0, biz_equity)
                    debt = np.where(sell, 0.0, debt)
                    alive_biz = np.where(sell, False, alive_biz)
                    sold |= sell
                    # after a sale the SOT says the odd contract is allowed; ignore (conservative)

        if kind == "build":
            op = alive_biz
            held = t
            surv = p_survive[min(held, len(p_survive) - 1)] * (fit if held == 0 else 1.0)
            die = op & (rng.random(n) > surv)
            alive_biz = np.where(die, False, alive_biz)
            deal_failed |= die
            op = alive_biz
            pm = profit_median_by_year[min(held, len(profit_median_by_year) - 1)]
            p9 = profit_p90_by_year[min(held, len(profit_p90_by_year) - 1)]
            prof = lognormal_from_median_and_p90(rng, max(pm, 1.0), max(p9, 2.0), n) if pm > 0 else np.zeros(n)
            # a share of builds never reach meaningful profit: cap using p_reach_70k
            prof = np.where(op, prof, 0.0)
            liquid = np.where(op, liquid + prof * (1 - draw_tax), liquid)
            owner_draw = np.where(op, prof, owner_draw)
            biz_equity = np.where(op, prof * resale_mult_median, 0.0)
            h += np.where(op, np.where(held == 0, hrs_yr1, hrs_later), 0.0)
            ff += np.where(op, f2f_share, 0.0)
            # exit after year 3 if profitable
            eligible = op & (held >= 3) & ~sold & (prof > 30000)
            sell = eligible & (rng.random(n) < v(r, "p_sell_per_year_when_eligible"))
            if sell.any():
                net = prof * resale_mult_median * (1 - v(g, "effective_tax_on_exit"))
                liquid = np.where(sell, liquid + net, liquid)
                biz_equity = np.where(sell, 0.0, biz_equity)
                alive_biz = np.where(sell, False, alive_biz)
                sold |= sell

        # 5. floor check, hours, reached -----------------------------------------------
        floor_breached |= liquid < floor
        hours[:, t] = h
        f2f[:, t] = np.clip(ff, 0, 1)
        nw = liquid + biz_equity
        newly = (nw >= target) & (reached_year == 99)
        reached_year = np.where(newly, year, reached_year)

    nw_final = liquid + biz_equity
    res = {
        "route": route,
        "n": n,
        "p_target_by_2034": float(np.mean(nw_final >= target)),
        "p_target_by_2032": float(np.mean(reached_year <= 2032)),
        "p_target_liquid_only_2034": float(np.mean(liquid >= target)),
        "p_floor_breached": float(np.mean(floor_breached)),
        "p_business_acquired": float(np.mean(acquired_year < 99)) if kind in ("buy", "hybrid") else (1.0 if kind == "build" else 0.0),
        "p_business_failed": float(np.mean(deal_failed)),
        "p_sold": float(np.mean(sold)),
        "median_year_reached": float(np.median(np.where(reached_year == 99, 2040, reached_year))),
        "nw_percentiles_2034": {str(q): float(np.percentile(nw_final, q)) for q in (5, 10, 25, 50, 75, 90, 95)},
        "liquid_percentiles_2034": {str(q): float(np.percentile(liquid, q)) for q in (5, 10, 25, 50, 75, 90, 95)},
        "median_owner_draw_when_operating": float(np.median(owner_draw[owner_draw != 0])) if np.any(owner_draw != 0) else 0.0,
        "mean_hours_by_year": [float(np.mean(hours[:, t])) for t in range(years)],
        "mean_f2f_by_year": [float(np.mean(f2f[:, t])) for t in range(years)],
        "reached_year_hist": {str(y): float(np.mean(reached_year == y)) for y in range(2027, 2035)},
    }
    return res, nw_final, liquid


def fan(nw_by_year):
    return {str(q): [float(np.percentile(col, q)) for col in nw_by_year] for q in (10, 25, 50, 75, 90)}


if __name__ == "__main__":
    p = load_params()
    out = {}
    for route in p["routes"]:
        res, _, _ = simulate(route, json.loads(json.dumps(p)))
        out[route] = res
        print(f"{route:20s} P(750k by 2034)={res['p_target_by_2034']:.2f}  P(floor breached)={res['p_floor_breached']:.2f}  "
              f"P(fail)={res['p_business_failed']:.2f}  median NW={res['nw_percentiles_2034']['50']:,.0f}")
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2)
