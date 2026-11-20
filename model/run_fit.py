import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
lead = {R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3,
        R+"blocks_while_operating":[3,2,1,0], R+"seller_finance_share":0.5, R+"bank_term_years":10, R+"exit_multiple_median":3.0,
        R+"ebitda_growth_median":0.08, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"p_manager_stays":0.85,
        R+"p_severe_decline_yr1":0.04, R+"multiple_median":2.3, R+"multiple_p90":2.8, R+"ev_median":385000, R+"ev_p90":500000,
        "general.floor":60000, "general.crypto_sleeve_share":0.10}
print("Lead plan (2.3x, EV 385k, origination) with fit multiplier varied. Fit scales P(close) and divides failure/decline hazards.")
for name, f in [("poor fit 0.80 (e.g. people-heavy firm you dislike running)",0.80),("neutral 1.00",1.0),("services baseline 1.05",1.05),("distributor baseline 1.10",1.10),("strong fit 1.20 (systematic, data-led, manager-run)",1.20)]:
    r = M.simulate(B, p, n=N, overrides={**lead, R+"fit_multiplier":f}); c = r["conditional"]
    print(f"{name:62s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} P750|deal={(c['p_target_given_acquired'] or 0):5.1%}")
print("--- same, but fit also changes what you do with hours: poor fit = you take 1 fewer contracting block/yr while operating (burnout), strong fit = growth 10% not 8%")
r = M.simulate(B, p, n=N, overrides={**lead, R+"fit_multiplier":0.8, R+"blocks_while_operating":[2,1,0,0]}); print(f"{'poor fit + fewer blocks':62s} P750={r['p_target_by_2034']:5.1%}")
r = M.simulate(B, p, n=N, overrides={**lead, R+"fit_multiplier":1.2, R+"ebitda_growth_median":0.10}); print(f"{'strong fit + 10% growth':62s} P750={r['p_target_by_2034']:5.1%}")
