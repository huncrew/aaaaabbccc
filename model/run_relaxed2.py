import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
best = {R+"blocks_per_year":4, "general.floor":60000, R+"seller_finance_share":0.5, R+"bank_term_years":10, R+"multiple_median":2.3, R+"exit_multiple_median":3.5, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.08, R+"blocks_while_operating":1}
def run(name, ov, route=B):
    r = M.simulate(route, p, n=N, overrides=ov); c = r["conditional"]
    print(f"{name:66s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} P750|deal={(c['p_target_given_acquired'] or 0):5.1%} EV={((c['median_ev_closed'] or 0)/1000):4.0f}k NW50={r['nw_percentiles_2034']['50']/1000:4.0f}k days={r['mean_employed_days_total']:4.0f} floor={r['p_floor_breached']:4.0%}")
run("BEST (4 blocks x2, floor 60k, 50% VN, 10y, 2.3x, £400k, 8% growth, 1 blk/yr)", best)
run("  same, blocks land 90% of the time (reliable £12k/month)", {**best, R+"p_block_lands":0.9, "general.backstop_p_block_lands":0.9})
run("  same, horizon 2036 (42)", {**best, "horizon.years":10})
run("  same, horizon 2038 (44)", {**best, "horizon.years":12})
run("  health version: 3 blocks x2 instead of 4", {**best, R+"blocks_per_year":3})
run("  health version: 3 blocks x2, no blocks while running", {**best, R+"blocks_per_year":3, R+"blocks_while_operating":0})
run("  without the 8% growth (3% base)", {**best, R+"ebitda_growth_median":0.03})
run("  without the 2.3x (2.8x distributor pricing)", {**best, R+"multiple_median":2.8, R+"exit_multiple_median":3.5})
run("  keep the £120k floor", {**best, "general.floor":120000})
run("  pessimistic fit (0.8) and yr-1 severe decline 25%", {**best, R+"fit_multiplier":0.8, R+"p_severe_decline_yr1":0.25})
