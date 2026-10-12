"""Runs the base model (raw fit=1 and fit-adjusted), the labour sweep, and tornado sensitivities. Writes results.json."""
import json, copy, os
import numpy as np
import mc_model as M
HERE = os.path.dirname(os.path.abspath(__file__))
p = M.load_params()
N = 20000
out = {"routes_raw": {}, "routes_fit": {}, "sweep_labour": [], "tornado": {}, "scenarios": {}}
for route in p["routes"]:
    out["routes_fit"][route] = M.simulate(route, p, n=N)
    out["routes_raw"][route] = M.simulate(route, p, n=N, overrides={f"routes.{route}.fit_multiplier": 1.0})
    r = out["routes_fit"][route]
    print(f"{route:18s} fit P750k={r['p_target_by_2034']:.2f} raw={out['routes_raw'][route]['p_target_by_2034']:.2f} P500k={r['p_500k_by_2034']:.2f} acq={r['p_business_acquired']:.2f} "
          f"P750k|acq={r['conditional']['p_target_given_acquired']} days={r['mean_employed_days_total']:.0f} NW50={r['nw_percentiles_2034']['50']:,.0f}")
# labour sweep on the SOT hybrid plan: years of contracting before the search x blocks per year
base = "hybrid_2blocks_2y"
for yrs in (0, 1, 2, 3):
    for bpy in (1, 2, 3):
        ov = {f"routes.{base}.contract_years_before_search": yrs, f"routes.{base}.blocks_per_year": bpy, f"routes.{base}.blocks_during_search": 1}
        r = M.simulate(base, p, n=10000, overrides=ov)
        out["sweep_labour"].append({"years": yrs, "blocks_per_year": bpy, "p750": r["p_target_by_2034"], "p500": r["p_500k_by_2034"], "p_acq": r["p_business_acquired"],
                                    "days": r["mean_employed_days_total"], "p_floor": r["p_floor_breached"], "nw50": r["nw_percentiles_2034"]["50"], "nw90": r["nw_percentiles_2034"]["90"],
                                    "acq_year": r["conditional"]["median_acquisition_year"]})
        print("sweep", yrs, bpy, round(r["p_target_by_2034"], 3), round(r["p_business_acquired"], 2), round(r["mean_employed_days_total"]))
# tornado on the base hybrid route
tor = {
 "general.start_investable": (150000, 200000), "routes.%s.seller_finance_share" % base: (0.2, 0.5), "routes.%s.multiple_median" % base: (2.0, 3.6),
 "routes.%s.manager_cost" % base: (0, 45000), "routes.%s.p_close_within_12m" % base: (0.15, 0.5), "general.index_nominal_return_mean": (0.03, 0.07),
 "routes.%s.ebitda_growth_median" % base: (-0.02, 0.08), "routes.%s.exit_multiple_median" % base: (2.2, 3.8), "routes.%s.bank_term_years" % base: (5, 10),
 "general.pg_share_of_facility": (0.2, 1.0), "routes.%s.max_search_years" % base: (1, 3), "routes.%s.p_severe_decline_yr1" % base: (0.06, 0.25),
 "routes.%s.p_failure_annual_after_yr1" % base: (0.02, 0.10), "general.annual_burn": (16800, 24000), "general.dscr_min": (1.2, 1.5),
 "routes.%s.fit_multiplier" % base: (0.8, 1.3), "general.backstop_p_block_lands": (0.55, 0.9), "routes.%s.ev_median" % base: (220000, 400000),
}
for k, (lo, hi) in tor.items():
    rl = M.simulate(base, p, n=10000, overrides={k: lo}); rh = M.simulate(base, p, n=10000, overrides={k: hi})
    out["tornado"][k] = {"low": lo, "high": hi, "p750_low": rl["p_target_by_2034"], "p750_high": rh["p_target_by_2034"], "p500_low": rl["p_500k_by_2034"], "p500_high": rh["p_500k_by_2034"], "base_value": M.v(p, k)}
    print("tornado", k, round(rl["p_target_by_2034"], 3), round(rh["p_target_by_2034"], 3))
# scenarios: what has to be true
scen = {
 "SOT plan as written": {},
 "Negotiated deal (50% vendor note, 10-yr GGS)": {f"routes.{base}.seller_finance_share": 0.5, f"routes.{base}.bank_term_years": 10},
 "+ second line grows EBITDA 8%/yr": {f"routes.{base}.seller_finance_share": 0.5, f"routes.{base}.bank_term_years": 10, f"routes.{base}.ebitda_growth_median": 0.08},
 "+ buy at 2.3x (services/logistics pricing)": {f"routes.{base}.seller_finance_share": 0.5, f"routes.{base}.bank_term_years": 10, f"routes.{base}.ebitda_growth_median": 0.08, f"routes.{base}.multiple_median": 2.3, f"routes.{base}.exit_multiple_median": 2.8},
 "+ £200k start cash": {f"routes.{base}.seller_finance_share": 0.5, f"routes.{base}.bank_term_years": 10, f"routes.{base}.ebitda_growth_median": 0.08, f"routes.{base}.multiple_median": 2.3, f"routes.{base}.exit_multiple_median": 2.8, "general.start_investable": 200000},
 "All of the above, no contracting (SOT one-block)": {f"routes.{base}.seller_finance_share": 0.5, f"routes.{base}.bank_term_years": 10, f"routes.{base}.ebitda_growth_median": 0.08, f"routes.{base}.multiple_median": 2.3, f"routes.{base}.exit_multiple_median": 2.8, "general.start_investable": 200000, f"routes.{base}.contract_years_before_search": 0, f"routes.{base}.blocks_per_year": 1},
}
for name, ov in scen.items():
    r = M.simulate(base, p, n=10000, overrides=ov)
    out["scenarios"][name] = {"overrides": ov, "p750": r["p_target_by_2034"], "p500": r["p_500k_by_2034"], "p_acq": r["p_business_acquired"], "nw50": r["nw_percentiles_2034"]["50"], "nw90": r["nw_percentiles_2034"]["90"], "p_floor": r["p_floor_breached"], "days": r["mean_employed_days_total"], "p750_given_acq": r["conditional"]["p_target_given_acquired"], "draw_by_held": r["conditional"]["median_draw_by_year_held"]}
    print("scenario", name, round(r["p_target_by_2034"], 3), round(r["p_business_acquired"], 2), r["conditional"]["p_target_given_acquired"])
json.dump(out, open(os.path.join(HERE, "results.json"), "w"))
print("written")
