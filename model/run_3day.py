import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
def run(name, ov, route=B):
    r = M.simulate(route, p, n=N, overrides=ov); c = r["conditional"]
    print(f"{name:62s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} yr={c['median_acquisition_year'] or 0:.0f} EV={((c['median_ev_closed'] or 0)/1000):4.0f}k P750|deal={(c['p_target_given_acquired'] or 0):5.1%} NW50={r['nw_percentiles_2034']['50']/1000:4.0f}k days={r['mean_employed_days_total']:4.0f} hrs={[round(h) for h in r['mean_hours_by_year']]}")
# 3 days/week continuous ≈ 3 blocks/yr (135–140 billed days); a block lands 80% (continuous 3-day roles are the common shape)
three = {R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3}
taper = {R+"blocks_while_operating":[3,2,1,0]}      # business replaces contracting over 3 years after purchase
keep  = {R+"blocks_while_operating":[3,3,3,3]}      # 3 days a week throughout, business on top
deal  = {R+"seller_finance_share":0.5, R+"bank_term_years":10, R+"multiple_median":2.3, R+"exit_multiple_median":3.0, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.08}
print("--- 3 days/week from 2027, floor £120k kept")
run("search from 2027, deal when cash allows, taper 3-2-1-0", {**three, **taper, R+"contract_years_before_search":0})
run("1 year banked first, then search, taper 3-2-1-0", {**three, **taper, R+"contract_years_before_search":1})
run("2 years banked first, then search, taper 3-2-1-0", {**three, **taper, R+"contract_years_before_search":2})
run("2 years banked, negotiated deal (2.3x, £400k, 50% VN, 10y, 8% gr)", {**three, **taper, **deal, R+"contract_years_before_search":2})
run("1 year banked, negotiated deal", {**three, **taper, **deal, R+"contract_years_before_search":1})
print("--- floor usable to £60k")
run("2 years banked, negotiated deal, floor £60k", {**three, **taper, **deal, R+"contract_years_before_search":2, "general.floor":60000})
run("1 year banked, negotiated deal, floor £60k", {**three, **taper, **deal, R+"contract_years_before_search":1, "general.floor":60000})
print("--- keep 3 days/week throughout (business on top, not replacing)")
run("2 years banked, negotiated deal, keep 3 days/wk", {**three, **keep, **deal, R+"contract_years_before_search":2})
print("--- horizon")
run("2 yrs banked, negotiated, taper, floor 60k -> by 2036", {**three, **taper, **deal, R+"contract_years_before_search":2, "general.floor":60000, "horizon.years":10})
run("2 yrs banked, negotiated, taper, floor 60k -> by 2038", {**three, **taper, **deal, R+"contract_years_before_search":2, "general.floor":60000, "horizon.years":12})
print("--- no business at all: 3 days/week for 8 years")
run("3 days/wk contracting only, 8 years", {"routes.contract_heavy.blocks_per_year":3, "routes.contract_heavy.p_block_lands":0.8}, "contract_heavy")
run("3 days/wk contracting only, by 2036", {"routes.contract_heavy.blocks_per_year":3, "routes.contract_heavy.p_block_lands":0.8, "horizon.years":10}, "contract_heavy")
print("--- pessimistic checks on the lead case")
run("lead case, fit 0.8, severe yr-1 decline 25%", {**three, **taper, **deal, R+"contract_years_before_search":2, "general.floor":60000, R+"fit_multiplier":0.8, R+"p_severe_decline_yr1":0.25})
run("lead case, blocks land only 65%", {**three, **taper, **deal, R+"contract_years_before_search":2, "general.floor":60000, R+"p_block_lands":0.65, "general.backstop_p_block_lands":0.65})
run("lead case, 3% growth not 8%", {**three, **taper, **deal, R+"contract_years_before_search":2, "general.floor":60000, R+"ebitda_growth_median":0.03})
