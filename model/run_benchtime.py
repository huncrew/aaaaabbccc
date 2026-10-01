import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
lead = {R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3,
        R+"blocks_while_operating":[3,2,1,0], R+"seller_finance_share":0.5, R+"bank_term_years":10, R+"multiple_median":2.3, R+"exit_multiple_median":3.0,
        R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.08, R+"contract_years_before_search":2, "general.floor":60000, "general.crypto_sleeve_share":0.10}
def run(name, ov, route=B):
    r = M.simulate(route, p, n=N, overrides=ov); c = r["conditional"]
    print(f"{name:64s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} yr={c['median_acquisition_year'] or 0:.0f} P750|deal={(c['p_target_given_acquired'] or 0):5.1%} NW50={r['nw_percentiles_2034']['50']/1000:4.0f}k")
print("Lead plan (3 days/wk, buy 2029, 10% crypto sleeve) = baseline")
run("baseline: search opens 2029, P(close)/yr 30%, pay 2.3x", lead)
print("--- bench time spent on deal origination (off-market, retiring owners, lunches, trade shows)")
run("search opens 2028 (a year of origination while banking)", {**lead, R+"contract_years_before_search":1})
run("  + P(close)/yr 50% (more approaches, better pipeline)", {**lead, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5})
run("  + pay 2.0x (proprietary deal, no broker auction)", {**lead, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"multiple_median":2.0})
run("  + manager stays 85% (you chose the business for its manager)", {**lead, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"multiple_median":2.0, R+"p_manager_stays":0.85})
run("  + severe yr-1 decline 6% (real DD, seller retained 12 months)", {**lead, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"multiple_median":2.0, R+"p_manager_stays":0.85, R+"p_severe_decline_yr1":0.06})
print("--- bench time spent on the app instead (cold build, second person, from 2027)")
run("AI app from 2027 + 3 days/wk contracting, no business", {"general.crypto_sleeve_share":0.10, "general.blocks_fallback_per_year":3, "routes.build_ai_app.fit_multiplier":1.0}, "build_ai_app")
run("AWS consultancy from 2027 (as modelled)", {"general.crypto_sleeve_share":0.10, "general.blocks_fallback_per_year":3}, "build_aws_partner")
print("--- bench time spent on the crypto sleeve (only the allocation can change; hours do not change returns)")
run("baseline with 25% sleeve instead of 10%", {**lead, "general.crypto_sleeve_share":0.25})
run("origination case (all of the above) with 25% sleeve", {**lead, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"multiple_median":2.0, R+"p_manager_stays":0.85, R+"p_severe_decline_yr1":0.06, "general.crypto_sleeve_share":0.25})
