"""
Monte Carlo path model: probability that Dale reaches £750k invested by end-2034 (age 40)
under each route, given his constraints (floor never touched, PG exposure ≤ risk pot, energy limits).

All numbers live in params.json (each leaf: value/low/high/src/confidence). This file is mechanics only.

Routes (kind):
  contract_only   (contract)  one ~13-week pre-sales block per year (the SOT one-block rule), surplus to index
  contract_heavy  (contract)  three blocks per year (~150 billed days) - the "labour" comparator, health cost flagged
  buy_*           (buy)       search from 2027, buy with vendor note + bank/GGS debt, manager in place, Dale sells
  build_*         (build)     start from zero (ecommerce / B2B services / AWS-AI consultancy)
  build_ai_app    (venture)   AI app or vertical SaaS with a second person; stage-gated, heavy-tailed exit
  hybrid_plan     (hybrid)    SOT plan: one block Feb-Apr 2027, then buy a distributor-type business
  hybrid_plan_app (hybrid)    hybrid_plan plus the "product from inside owned customers" option (app_option)

Timeline: t=0 is calendar 2027 ... t=7 is 2034. Start state is end-2026.
Backstop (all non-contract routes): if year-end liquid falls below floor + buffer, Dale does one SC contracting
block that year if one lands (the SOT's "26 days covers a year's burn" backstop). This is what keeps a failure
a bad year rather than a restart, and it is counted in hours.
"""
from __future__ import annotations
import json, os, copy
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load_params(path=os.path.join(HERE, "params.json")):
    with open(path) as f:
        return json.load(f)


def v(node, key):
    for k in key.split("."):
        node = node[k]
    return node["value"] if isinstance(node, dict) and "value" in node else node


def set_override(p, dotted, val):
    node = p
    parts = dotted.split(".")
    for part in parts[:-1]:
        node = node[part]
    leaf = node[parts[-1]]
    if isinstance(leaf, dict) and "value" in leaf:
        leaf["value"] = val
    else:
        node[parts[-1]] = val


def lognormal(rng, median, p90, size):
    mu = np.log(np.maximum(median, 1e-9))
    sigma = np.maximum((np.log(np.maximum(p90, 2e-9)) - mu) / 1.2816, 0.02)
    return np.exp(rng.normal(mu, sigma, size))


def annuity(principal, rate, term):
    if term <= 0:
        return principal
    if rate <= 0:
        return principal / term
    return principal * rate / (1 - (1 + rate) ** -term)


def simulate(route, p, n=20000, seed=42, overrides=None):
    p = copy.deepcopy(p)
    if overrides:
        for k, val in overrides.items():
            set_override(p, k, val)
    rng = np.random.default_rng(seed)
    years = int(v(p, "horizon.years"))
    g = p["general"]
    r = p["routes"][route]
    kind = v(r, "kind")

    floor = v(g, "floor")
    burn = v(g, "annual_burn")
    mean_r, sd_r = v(g, "index_nominal_return_mean"), v(g, "index_return_sd")
    target = v(g, "target")
    draw_tax = v(g, "effective_tax_on_draw")
    exit_tax = v(g, "effective_tax_on_exit")
    tax_sole = v(g, "effective_tax_on_contract_sole")
    tax_stacked = v(g, "effective_tax_on_contract_stacked")
    bs_on = bool(v(g, "backstop_enabled")) and kind != "contract"
    bs_buffer = v(g, "backstop_trigger_buffer")
    bs_gross_med, bs_gross_p90, bs_p = v(g, "backstop_block_gross_median"), v(g, "backstop_block_gross_p90"), v(g, "backstop_p_block_lands")
    bs_hours = v(g, "backstop_hours_week_equiv")
    pg_share = v(g, "pg_share_of_facility")
    max_debt_x = v(g, "senior_debt_max_ebitda_multiple")

    # ---------------- state ----------------
    liquid = np.full(n, float(v(g, "start_investable")))
    biz_equity = np.zeros(n)
    debt = np.zeros(n)
    bank_service = np.zeros(n)
    vendor_service = np.zeros(n)
    bank_years_left = np.zeros(n)
    vendor_years_left = np.zeros(n)
    ebitda = np.zeros(n)
    alive_biz = np.zeros(n, dtype=bool)
    acquired_year = np.full(n, 99)
    searching = np.zeros(n, dtype=bool)
    search_years = np.zeros(n)
    entry_mult = np.zeros(n)
    sold = np.zeros(n, dtype=bool)
    failed = np.zeros(n, dtype=bool)
    floor_breached = np.zeros(n, dtype=bool)
    reached_year = np.full(n, 99)
    owner_draw_hist = np.zeros((n, years))
    hours = np.zeros((n, years))
    f2f = np.zeros((n, years))
    backstop_used = np.zeros((n, years), dtype=bool)
    blocks_done = np.zeros(n)
    nw_path = np.zeros((n, years))
    stage = np.zeros(n, dtype=int)
    ev_closed = np.zeros(n)
    ebitda_closed = np.zeros(n)
    cash_in_deal = np.zeros(n)
    venture_alive = np.zeros(n, dtype=bool)
    app_started = np.zeros(n, dtype=bool)

    # ---------------- route params ----------------
    if kind in ("buy", "hybrid"):
        p_close = v(r, "p_close_within_12m") * v(r, "fit_multiplier")
        max_search = v(r, "max_search_years")
        fit = v(r, "fit_multiplier")
        mgr_cost = v(r, "manager_cost")
        search_start = int(v(r, "contract_years_before_search")) if "contract_years_before_search" in r else 0
        blocks_pre = int(v(r, "blocks_per_year")) if "blocks_per_year" in r else 0
        blocks_search = int(v(r, "blocks_during_search")) if "blocks_during_search" in r else 0
        blocks_fallback = int(v(g, "blocks_fallback_per_year"))
        blocks_operating = int(v(r, "blocks_while_operating")) if "blocks_while_operating" in r else 0
        p_land = v(r, "p_block_lands") if "p_block_lands" in r else v(g, "backstop_p_block_lands")
        c_tax_one = tax_sole
        c_tax_multi = v(r, "effective_tax_on_contract") if "effective_tax_on_contract" in r else v(g, "effective_tax_on_contract_multi")
        bank_debt = np.zeros(n)
        searching[:] = True
    if kind == "contract":
        blocks = int(v(r, "blocks_per_year"))
        p_land = v(r, "p_block_lands")
        c_tax = v(r, "effective_tax_on_contract") if "effective_tax_on_contract" in r else tax_sole
    if kind == "build":
        fit = v(r, "fit_multiplier")
        liquid -= v(r, "capital_in")
        alive_biz[:] = True
        acquired_year[:] = 0
        surv = v(r, "survival_curve")
        pm_by, p9_by = v(r, "owner_profit_median_by_year"), v(r, "owner_profit_p90_by_year")
    if kind == "venture":
        fit = v(r, "fit_multiplier")
        venture_alive[:] = True
        acquired_year[:] = 0
    app = r.get("app_option") if kind == "hybrid" else None

    for t in range(years):
        year = 2027 + t
        liquid *= (1 + rng.normal(mean_r, sd_r, n))
        liquid -= burn
        h = np.zeros(n)
        ff = np.zeros(n)
        income_this_year = np.zeros(n, dtype=bool)

        # ---- contracting blocks (planned) ----
        if kind == "contract":
            for _ in range(blocks):
                lands = rng.random(n) < p_land
                gross = lognormal(rng, v(r, "block_gross_median"), v(r, "block_gross_p90"), n)
                liquid += np.where(lands, gross * (1 - c_tax), 0.0)
                h += np.where(lands, v(r, "hours_per_block_week") * 13 / 52, 0.0)
                blocks_done += lands
                income_this_year |= lands
        if kind in ("buy", "hybrid"):
            # planned blocks: blocks_pre per year before the search opens, blocks_search per year while searching
            idle = (~searching | (search_years >= max_search)) & ~alive_biz & (t >= search_start)
            operating = alive_biz & (acquired_year < t)   # from the second year of ownership (SOT: not before 100 days / three paid months)
            nb = np.where(t < search_start, blocks_pre, np.where(searching & (search_years < max_search) & (acquired_year == 99), blocks_search, np.where(idle, blocks_fallback, np.where(operating, blocks_operating, 0))))
            for b in range(int(nb.max()) if nb.size else 0):
                do = nb > b
                lands = do & (rng.random(n) < p_land)
                gross = lognormal(rng, v(g, "backstop_block_gross_median"), v(g, "backstop_block_gross_p90"), n)
                tax = c_tax_one if b == 0 else c_tax_multi
                liquid += np.where(lands, gross * (1 - tax), 0.0)
                h += np.where(lands, v(g, "backstop_hours_week_equiv"), 0.0)
                blocks_done += lands
                income_this_year |= lands

        # ---- search & completion ----
        if kind in ("buy", "hybrid"):
            can = searching & (search_years < max_search) & (t >= search_start)
            close = can & (rng.random(n) < p_close)
            search_years += can
            h += np.where(can, v(r, "search_hours_week"), 0.0)
            ff += np.where(can, 0.5, 0.0)
            idx = np.where(close)[0]
            if idx.size:
                m = idx.size
                ev = lognormal(rng, v(r, "ev_median"), v(r, "ev_p90"), m)
                mult = lognormal(rng, v(r, "multiple_median"), v(r, "multiple_p90"), m)
                e0 = ev / mult
                vendor = ev * v(r, "seller_finance_share")
                gap = ev - vendor
                avail = np.maximum(liquid[idx] - floor, 0.0)          # the risk pot = cash above the floor at completion
                bank = np.minimum.reduce([gap * v(r, "bank_share_of_cash_gap"), avail / pg_share, e0 * max_debt_x])
                # lender DSCR gate: (EBITDA - manager) / (bank + vendor service) >= dscr_min -> shrink bank debt to fit
                vs = annuity(vendor, v(r, "vendor_loan_rate"), v(r, "vendor_loan_term_years"))
                bank_af = annuity(1.0, v(r, "bank_rate"), v(r, "bank_term_years"))
                bank_cap = np.maximum(((e0 - mgr_cost) / v(g, "dscr_min") - vs) / bank_af, 0.0)
                bank = np.minimum(bank, bank_cap)
                equity_cash = gap - bank + v(r, "deal_costs") + ev * v(r, "wc_reserve_pct")
                scale = np.clip(avail / np.maximum(equity_cash, 1.0), 0.0, 1.0)
                ok = scale >= v(r, "min_deal_scale")
                scale = np.where(ok, scale, 0.0)
                ev, e0, vendor, bank, equity_cash = ev * scale, e0 * scale, vendor * scale, bank * scale, equity_cash * scale
                liquid[idx] -= equity_cash
                ev_closed[idx] = ev
                ebitda_closed[idx] = e0
                cash_in_deal[idx] = equity_cash
                debt[idx] = vendor + bank
                bank_debt[idx] = bank
                ebitda[idx] = e0
                entry_mult[idx] = mult
                alive_biz[idx] = ok
                acquired_year[idx] = np.where(ok, t, 99)
                searching[idx] = ~ok
                # year-1 shock: manager leaves, seller-dependency, severe decline
                chg = lognormal(rng, v(r, "yr1_ebitda_change_median"), v(r, "yr1_ebitda_change_p90"), m)
                severe = rng.random(m) < v(r, "p_severe_decline_yr1") / fit
                chg = np.where(severe, v(r, "severe_decline_factor"), chg)
                mgr_leaves = rng.random(m) > v(r, "p_manager_stays")
                chg = np.where(mgr_leaves, chg * v(r, "manager_leaves_factor"), chg)
                ebitda[idx] *= chg
                bank_service[idx] = np.where(ok, annuity(bank, v(r, "bank_rate"), v(r, "bank_term_years")), 0.0)
                vendor_service[idx] = np.where(ok, annuity(vendor, v(r, "vendor_loan_rate"), v(r, "vendor_loan_term_years")), 0.0)
                bank_years_left[idx] = np.where(ok, v(r, "bank_term_years"), 0)
                vendor_years_left[idx] = np.where(ok, v(r, "vendor_loan_term_years"), 0)

        # ---- operating an acquired business ----
        if kind in ("buy", "hybrid"):
            op = alive_biz & (acquired_year <= t)
            held = t - acquired_year
            later = op & (held >= 1)
            ebitda = np.where(later, ebitda * (1 + rng.normal(v(r, "ebitda_growth_median"), v(r, "ebitda_growth_sd"), n)), ebitda)
            fail = later & (rng.random(n) < v(r, "p_failure_annual_after_yr1") / fit)
            pg_loss = bank_debt * (debt / np.maximum(debt + 1e-9, 1e-9)) * pg_share * v(r, "pg_loss_share_on_failure")  # PG called on remaining bank debt
            liquid = np.where(fail, liquid - pg_loss, liquid)
            alive_biz &= ~fail
            failed |= fail
            ebitda = np.where(fail, 0.0, ebitda)
            debt = np.where(fail, 0.0, debt)
            bank_debt = np.where(fail, 0.0, bank_debt)
            op = alive_biz & (acquired_year <= t)
            ds = np.where(bank_years_left > 0, bank_service, 0.0) + np.where(vendor_years_left > 0, vendor_service, 0.0)
            draw = np.where(op, ebitda - mgr_cost - ds, 0.0)
            liquid += np.where(draw > 0, draw * (1 - draw_tax), draw)   # negative draw = cash call
            owner_draw_hist[:, t] = draw
            income_this_year |= op & (draw > 0)
            interest = debt * v(r, "blended_debt_rate")
            new_debt = np.where(op & (ds > 0), np.maximum(debt - (ds - interest), 0.0), debt)
            bank_debt = np.where(debt > 0, bank_debt * new_debt / np.maximum(debt, 1e-9), 0.0)
            debt = new_debt
            bank_years_left = np.where(op, np.maximum(bank_years_left - 1, 0), bank_years_left)
            vendor_years_left = np.where(op, np.maximum(vendor_years_left - 1, 0), vendor_years_left)
            h += np.where(op, np.where(held == 0, v(r, "hours_yr1"), v(r, "hours_yr3")), 0.0)
            ff += np.where(op, v(r, "f2f_share"), 0.0)
            biz_equity = np.where(op, np.maximum(ebitda * entry_mult - debt, 0.0), np.where(alive_biz, biz_equity, 0.0))
            eligible = op & (held >= v(r, "exit_earliest_years_held")) & ~sold
            sell = eligible & (rng.random(n) < v(r, "p_sell_per_year_when_eligible"))
            if sell.any():
                xm = lognormal(rng, v(r, "exit_multiple_median"), v(r, "exit_multiple_p90"), n)
                net = np.maximum(ebitda * xm - debt, 0.0) * (1 - exit_tax)
                liquid = np.where(sell, liquid + net, liquid)
                biz_equity = np.where(sell, 0.0, biz_equity)
                debt = np.where(sell, 0.0, debt)
                bank_debt = np.where(sell, 0.0, bank_debt)
                alive_biz &= ~sell
                sold |= sell

        # ---- app option from inside owned customers (hybrid_plan_app) ----
        if app is not None:
            start = alive_biz & (acquired_year <= t - v(app, "years_after_completion")) & ~app_started & ((liquid - floor) > v(app, "capital"))
            liquid = np.where(start, liquid - v(app, "capital"), liquid)
            app_started |= start
            stage = np.where(start, 1, stage)
            trying = app_started & (stage == 1) & alive_biz
            succ = trying & (rng.random(n) < v(app, "p_success_per_year"))
            dead = trying & ~succ & (rng.random(n) < v(app, "p_kill_per_year"))
            stage = np.where(succ, 2, np.where(dead, 9, stage))
            paying = app_started & (stage == 2) & alive_biz
            extra = lognormal(rng, v(app, "profit_median"), v(app, "profit_p90"), n)
            liquid = np.where(paying, liquid + extra * (1 - draw_tax), liquid)
            ebitda = np.where(paying, ebitda + extra * v(app, "ebitda_uplift_share"), ebitda)
            h += np.where(app_started & (stage < 9) & alive_biz, v(app, "hours_week"), 0.0)

        # ---- build from zero ----
        if kind == "build":
            op = alive_biz
            s = surv[min(t, len(surv) - 1)] * (fit if t == 0 else 1.0)
            die = op & (rng.random(n) > s)
            alive_biz &= ~die
            failed |= die
            op = alive_biz
            pm, p9 = pm_by[min(t, len(pm_by) - 1)], p9_by[min(t, len(p9_by) - 1)]
            prof = np.where(op, lognormal(rng, pm, p9, n), 0.0)
            liquid += prof * (1 - draw_tax)
            owner_draw_hist[:, t] = prof
            income_this_year |= op & (prof > burn)
            biz_equity = np.where(op, prof * v(r, "resale_multiple_median"), 0.0)
            h += np.where(op, np.where(t == 0, v(r, "hours_yr1"), v(r, "hours_yr3")), 0.0)
            ff += np.where(op, v(r, "f2f_share"), 0.0)
            eligible = op & (t >= 3) & ~sold & (prof > 30000)
            sell = eligible & (rng.random(n) < v(r, "p_sell_per_year_when_eligible"))
            if sell.any():
                net = prof * v(r, "resale_multiple_median") * (1 - exit_tax)
                liquid = np.where(sell, liquid + net, liquid)
                biz_equity = np.where(sell, 0.0, biz_equity)
                alive_biz &= ~sell
                sold |= sell

        # ---- venture (AI app) ----
        if kind == "venture":
            op = venture_alive
            liquid = np.where(op & (t < 2), liquid - v(r, "capital_per_year"), liquid)
            pa, pk = v(r, "p_advance_stage"), v(r, "p_kill_per_year")
            adv_p = np.array([pa[min(s, len(pa) - 1)] for s in stage]) * fit
            kill_p = np.array([pk[min(s, len(pk) - 1)] for s in stage]) / fit
            adv = op & (rng.random(n) < adv_p) & (stage < 3)
            kill = op & ~adv & (rng.random(n) < kill_p)
            stage = np.where(adv, stage + 1, stage)
            venture_alive &= ~kill
            failed |= kill
            op = venture_alive
            pm_s, p9_s = v(r, "owner_profit_by_stage"), v(r, "owner_profit_p90_by_stage")
            pm = np.array([pm_s[min(s, len(pm_s) - 1)] for s in stage], dtype=float)
            p9 = np.array([p9_s[min(s, len(p9_s) - 1)] for s in stage], dtype=float)
            prof = np.where(op & (pm > 0), lognormal(rng, np.maximum(pm, 1), np.maximum(p9, 2), n), 0.0)
            liquid += prof * (1 - draw_tax)
            owner_draw_hist[:, t] = prof
            income_this_year |= op & (prof > burn)
            pe, em_s, e9_s = v(r, "p_exit_per_year_by_stage"), v(r, "exit_value_median_by_stage"), v(r, "exit_value_p90_by_stage")
            ex_p = np.array([pe[min(s, len(pe) - 1)] for s in stage])
            em = np.array([em_s[min(s, len(em_s) - 1)] for s in stage], dtype=float)
            e9 = np.array([e9_s[min(s, len(e9_s) - 1)] for s in stage], dtype=float)
            sell = op & (rng.random(n) < ex_p) & ~sold & (em > 0)
            if sell.any():
                val = lognormal(rng, np.maximum(em, 1), np.maximum(e9, 2), n)
                liquid = np.where(sell, liquid + val * (1 - exit_tax), liquid)
                venture_alive &= ~sell
                sold |= sell
            op = venture_alive
            biz_equity = np.where(op, em * v(r, "unsold_equity_haircut"), 0.0)
            h += np.where(op, np.where(t < 2, v(r, "hours_yr1"), v(r, "hours_yr3")), 0.0)
            ff += np.where(op, v(r, "f2f_share"), 0.0)

        if kind in ("build", "venture"):
            gone = ~(alive_biz | venture_alive)
            for b in range(int(v(g, "blocks_fallback_per_year"))):
                lands = gone & (rng.random(n) < v(g, "backstop_p_block_lands"))
                gross = lognormal(rng, v(g, "backstop_block_gross_median"), v(g, "backstop_block_gross_p90"), n)
                liquid += np.where(lands, gross * (1 - (tax_sole if b == 0 else v(g, "effective_tax_on_contract_multi"))), 0.0)
                h += np.where(lands, v(g, "backstop_hours_week_equiv"), 0.0)
                blocks_done += lands
                income_this_year |= lands

        # ---- backstop: one SC contracting block if cash is threatening the floor ----
        if bs_on:
            need = liquid < floor + bs_buffer
            lands = need & (rng.random(n) < bs_p)
            gross = lognormal(rng, bs_gross_med, bs_gross_p90, n)
            tax = np.where(income_this_year, tax_stacked, tax_sole)
            liquid += np.where(lands, gross * (1 - tax), 0.0)
            h += np.where(lands, bs_hours, 0.0)
            blocks_done += lands
            backstop_used[:, t] = lands

        floor_breached |= liquid < floor
        hours[:, t] = h
        f2f[:, t] = np.clip(ff, 0, 1)
        nw = liquid + biz_equity
        nw_path[:, t] = nw
        reached_year = np.where((nw >= target) & (reached_year == 99), year, reached_year)

    nw_final = liquid + biz_equity
    pct = lambda a: {str(q): float(np.percentile(a, q)) for q in (5, 10, 25, 50, 75, 90, 95)}
    acq = acquired_year < 99
    draw_by_held = []
    if kind in ("buy", "hybrid") and acq.any():
        for k in range(years):
            vals = []
            for t in range(years):
                sel = acq & (acquired_year == t - k) & (owner_draw_hist[:, t] != 0)
                if sel.any():
                    vals.append(owner_draw_hist[sel, t])
            draw_by_held.append(float(np.median(np.concatenate(vals))) if vals else None)
    cond = {
        "p_target_given_acquired": float(np.mean(nw_final[acq] >= target)) if acq.any() else None,
        "p_500k_given_acquired": float(np.mean(nw_final[acq] >= 500000)) if acq.any() else None,
        "nw_percentiles_given_acquired": pct(nw_final[acq]) if acq.any() else None,
        "p_target_given_not_acquired": float(np.mean(nw_final[~acq] >= target)) if (~acq).any() else None,
        "median_draw_by_year_held": draw_by_held,
        "median_acquisition_year": float(np.median(2027 + acquired_year[acq])) if acq.any() else None,
        "median_ev_closed": float(np.median(ev_closed[acq])) if acq.any() else None,
        "median_ebitda_at_close": float(np.median(ebitda_closed[acq])) if acq.any() else None,
        "median_cash_in_deal": float(np.median(cash_in_deal[acq])) if acq.any() else None,
        "ev_closed_p10_p90": [float(np.percentile(ev_closed[acq], 10)), float(np.percentile(ev_closed[acq], 90))] if acq.any() else None,
    }
    od = owner_draw_hist[owner_draw_hist != 0]
    res = {
        "route": route, "kind": kind, "n": n,
        "p_target_by_2034": float(np.mean(nw_final >= target)),
        "p_target_by_2032": float(np.mean(reached_year <= 2032)),
        "p_500k_by_2034": float(np.mean(nw_final >= 500000)),
        "p_target_liquid_only_2034": float(np.mean(liquid >= target)),
        "p_floor_breached": float(np.mean(floor_breached)),
        "p_business_acquired": float(np.mean(acquired_year < 99)),
        "p_business_failed": float(np.mean(failed)),
        "p_sold": float(np.mean(sold)),
        "p_backstop_ever": float(np.mean(backstop_used.any(axis=1))),
        "mean_backstop_years": float(backstop_used.sum(axis=1).mean()),
        "mean_blocks_total": float(blocks_done.mean()),
        "mean_employed_days_total": float(blocks_done.mean() * 45),
        "median_year_reached": float(np.median(np.where(reached_year == 99, 2040, reached_year))),
        "nw_percentiles_2034": pct(nw_final),
        "liquid_percentiles_2034": pct(liquid),
        "median_owner_draw_when_operating": float(np.median(od)) if od.size else 0.0,
        "owner_draw_p25_p75": [float(np.percentile(od, 25)), float(np.percentile(od, 75))] if od.size else [0, 0],
        "mean_hours_by_year": [float(hours[:, t].mean()) for t in range(years)],
        "mean_f2f_by_year": [float(f2f[:, t].mean()) for t in range(years)],
        "reached_year_hist": {str(y): float(np.mean(reached_year == y)) for y in range(2027, 2035)},
        "fan": {str(q): [float(np.percentile(nw_path[:, t], q)) for t in range(years)] for q in (10, 25, 50, 75, 90)},
        "years": [2027 + t for t in range(years)],
        "conditional": cond,
    }
    return res


if __name__ == "__main__":
    p = load_params()
    out = {}
    for route in p["routes"]:
        res = simulate(route, p)
        out[route] = res
        print(f"{route:18s} P750k={res['p_target_by_2034']:.2f} P500k={res['p_500k_by_2034']:.2f} floor={res['p_floor_breached']:.2f} "
              f"acq={res['p_business_acquired']:.2f} fail={res['p_business_failed']:.2f} sold={res['p_sold']:.2f} "
              f"backstop={res['p_backstop_ever']:.2f} draw={res['median_owner_draw_when_operating']:>8,.0f} "
              f"NW p10/50/90={res['nw_percentiles_2034']['10']:>8,.0f}/{res['nw_percentiles_2034']['50']:>8,.0f}/{res['nw_percentiles_2034']['90']:>9,.0f}")
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
