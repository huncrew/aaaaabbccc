import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
lead = {R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3,
        R+"blocks_while_operating":[3,2,1,0], R+"seller_finance_share":0.5, R+"bank_term_years":10, R+"exit_multiple_median":3.0,
        R+"ebitda_growth_median":0.08, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"p_manager_stays":0.85,
        R+"p_severe_decline_yr1":0.06, "general.floor":60000, "general.crypto_sleeve_share":0.10}
def run(name, ov, route=B):
    r = M.simulate(route, p, n=N, overrides=ov); c = r["conditional"]
    print(f"{name:70s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} P750|deal={(c['p_target_given_acquired'] or 0):5.1%} NW50={r['nw_percentiles_2034']['50']/1000:4.0f}k")
print("Origination case, listing-scan multiples (SE contracted servicing, 29 Sep 2026 scan)")
run("as before: pay 2.0x, EV 400k median", {**lead, R+"multiple_median":2.0, R+"ev_median":400000, R+"ev_p90":600000})
run("scan median: pay 2.6x (p90 3.3x), EV 300k/450k", {**lead, R+"multiple_median":2.6, R+"multiple_p90":3.3, R+"ev_median":300000, R+"ev_p90":450000})
run("scan best SE deal: 3.1x on 96k NP (Surrey HVAC), EV 295k", {**lead, R+"multiple_median":3.1, R+"multiple_p90":3.4, R+"ev_median":295000, R+"ev_p90":400000})
run("London EICR firm: 3.0x on 167k EBITDA, EV ~500k, 90% recurring", {**lead, R+"multiple_median":3.0, R+"multiple_p90":3.3, R+"ev_median":500000, R+"ev_p90":600000, R+"p_severe_decline_yr1":0.04})
run("  + 25% crypto sleeve", {**lead, R+"multiple_median":3.0, R+"multiple_p90":3.3, R+"ev_median":500000, R+"ev_p90":600000, R+"p_severe_decline_yr1":0.04, "general.crypto_sleeve_share":0.25})
run("negotiated to 2.3x on the same EBITDA (50% VN), EV 385k", {**lead, R+"multiple_median":2.3, R+"multiple_p90":2.8, R+"ev_median":385000, R+"ev_p90":500000, R+"p_severe_decline_yr1":0.04})
