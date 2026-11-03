import mc_model as M, copy
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
base = {"general.crypto_sleeve_share":0.10, "general.floor":60000, R+"bank_term_years":10, R+"exit_multiple_median":3.0}
lead = {**base, R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3, R+"blocks_while_operating":[3,2,1,0], R+"seller_finance_share":0.5, R+"multiple_median":2.0, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.08, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"p_manager_stays":0.85, R+"p_severe_decline_yr1":0.06}
full = {**base, R+"blocks_per_year":0, R+"blocks_during_search":1, R+"blocks_while_operating":[0], "general.blocks_fallback_per_year":0, R+"contract_years_before_search":0, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.8, R+"vendor_loan_term_years":5, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.12}
def run(name, ov, side=True):
    pp = copy.deepcopy(p)
    if not side: del pp["routes"][B]["side_option"]
    r = M.simulate(B, pp, n=N, overrides=ov); c = r["conditional"]
    print(f"{name:58s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} NW50={r['nw_percentiles_2034']['50']/1000:4.0f}k p90={r['nw_percentiles_2034']['90']/1000:5.0f}k floor={r['p_floor_breached']:3.0%} hrs={[round(h) for h in r['mean_hours_by_year']]}")
print("3-day contracting + origination + buy 2028 (L):")
run("  without the side line", lead, side=False)
run("  with the one-line import probe from 2027", lead)
run("  probe, but 5-buyer test passes 50% (warm trade network)", {**lead, R+"side_option.p_pass_five_buyer_test":0.5})
run("  probe, pessimistic: passes 20%, fails 30%/yr", {**lead, R+"side_option.p_pass_five_buyer_test":0.2, R+"side_option.p_fail_per_year":0.3})
print("Business full time, seller-funded deal, 1 block/yr while searching (L4):")
run("  without the side line", full, side=False)
run("  with the one-line import probe from 2027", full)
run("  probe passes 50%", {**full, R+"side_option.p_pass_five_buyer_test":0.5})
print("Side line only, no acquisition search, 3 days/wk contracting (what if the probe is the business):")
run("  probe + contracting, never buy", {**lead, R+"p_close_within_12m":0.0})
run("  probe + contracting, never buy, probe p90 £200k (the JCB tail)", {**lead, R+"p_close_within_12m":0.0, R+"side_option.profit_p90":200000})
