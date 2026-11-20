import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
lead = {R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3,
        R+"blocks_while_operating":[3,2,1,0], R+"seller_finance_share":0.5, R+"bank_term_years":10, R+"multiple_median":2.3, R+"exit_multiple_median":3.0,
        R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.08, R+"contract_years_before_search":2, "general.floor":60000}
def run(name, ov, route=B):
    r = M.simulate(route, p, n=N, overrides=ov)
    print(f"{name:58s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} NW p10/50/90={r['nw_percentiles_2034']['10']/1000:4.0f}k/{r['nw_percentiles_2034']['50']/1000:4.0f}k/{r['nw_percentiles_2034']['90']/1000:5.0f}k floor-breach={r['p_floor_breached']:4.0%}")
print("lead 3-day plan (buy a traditional business), crypto sleeve rebalanced yearly:")
run("no crypto", lead)
run("10% sleeve, +25%/yr mean, 80% vol", {**lead, "general.crypto_sleeve_share":0.10})
run("25% sleeve, +25%/yr, 80% vol", {**lead, "general.crypto_sleeve_share":0.25})
run("25% sleeve, +40%/yr, 80% vol", {**lead, "general.crypto_sleeve_share":0.25, "general.crypto_mean":0.40})
run("40% sleeve, +40%/yr, 80% vol", {**lead, "general.crypto_sleeve_share":0.40, "general.crypto_mean":0.40})
run("25% sleeve, +60%/yr, 100% vol (very bullish)", {**lead, "general.crypto_sleeve_share":0.25, "general.crypto_mean":0.60, "general.crypto_sd":1.0})
print("3 days/week contracting only + crypto, no business:")
c = {"routes.contract_heavy.blocks_per_year":3, "routes.contract_heavy.p_block_lands":0.8}
run("no crypto", c, "contract_heavy")
run("25% sleeve, +25%/yr", {**c, "general.crypto_sleeve_share":0.25}, "contract_heavy")
run("25% sleeve, +40%/yr", {**c, "general.crypto_sleeve_share":0.25, "general.crypto_mean":0.40}, "contract_heavy")
run("40% sleeve, +40%/yr", {**c, "general.crypto_sleeve_share":0.40, "general.crypto_mean":0.40}, "contract_heavy")
print("build routes with the 3-day contracting behind them + 25% sleeve at +25%:")
run("build AWS/AI consultancy", {"general.crypto_sleeve_share":0.25, "general.blocks_fallback_per_year":3}, "build_aws_partner")
run("build AI app w/ 2nd person (fit 1.0)", {"general.crypto_sleeve_share":0.25, "general.blocks_fallback_per_year":3, "routes.build_ai_app.fit_multiplier":1.0}, "build_ai_app")
run("build B2B services", {"general.crypto_sleeve_share":0.25, "general.blocks_fallback_per_year":3}, "build_services")
