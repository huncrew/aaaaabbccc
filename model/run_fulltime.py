import mc_model as M
p = M.load_params(); N = 10000; B = "hybrid_2blocks_2y"; R = f"routes.{B}."
base = {"general.crypto_sleeve_share":0.10, "general.floor":60000, R+"bank_term_years":10, R+"exit_multiple_median":3.0}
noc = {R+"blocks_per_year":0, R+"blocks_during_search":0, R+"blocks_while_operating":[0], "general.blocks_fallback_per_year":0, R+"contract_years_before_search":0}
def run(name, ov, route=B):
    r = M.simulate(route, p, n=N, overrides=ov); c = r["conditional"]
    print(f"{name:70s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} yr={c['median_acquisition_year'] or 0:.0f} EV={((c['median_ev_closed'] or 0)/1000):4.0f}k draw1-4={[round((d or 0)/1000) for d in (c['median_draw_by_year_held'] or [])[:4]]}k NW50={r['nw_percentiles_2034']['50']/1000:4.0f}k days={r['mean_employed_days_total']:4.0f} floor={r['p_floor_breached']:3.0%}")
print("=== BUSINESS FULL TIME FROM 2027, NO PLANNED CONTRACTING (SC backstop only if cash hits the floor)")
run("A1 full-time search (close 50%/yr), buy what cash allows, 35% VN, 2.3x", {**base, **noc, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3})
run("A2  + 60% vendor note (retiring owner paid from profits over 5 yrs)", {**base, **noc, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.6, R+"vendor_loan_term_years":5})
run("A3  + 80% vendor note / earn-in (seller keeps skin for 5 yrs)", {**base, **noc, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.8, R+"vendor_loan_term_years":5})
run("A4  A3 + target EV £400k (bigger business, seller-funded)", {**base, **noc, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.8, R+"vendor_loan_term_years":5, R+"ev_median":400000, R+"ev_p90":600000})
run("A5  A4 + buy-and-build: EBITDA +12%/yr from cash-flow bolt-ons", {**base, **noc, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.8, R+"vendor_loan_term_years":5, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.12})
run("A6  A5 + 25% crypto sleeve", {**base, **noc, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.8, R+"vendor_loan_term_years":5, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.12, "general.crypto_sleeve_share":0.25})
print("=== the realistic version of A: vendor note 50%, close 40%/yr, 8% growth")
run("A7 full-time, 50% VN, close 40%, EV £300k, 8% growth", {**base, **noc, R+"p_close_within_12m":0.4, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.5, R+"vendor_loan_term_years":5, R+"ebitda_growth_median":0.08})
run("A8  same with ONE block a year only while searching (the SOT coast)", {**base, **noc, R+"blocks_during_search":1, R+"p_close_within_12m":0.4, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.5, R+"vendor_loan_term_years":5, R+"ebitda_growth_median":0.08})
run("A9  same, one block/yr while searching AND in years 1-2 of ownership", {**base, **noc, R+"blocks_during_search":1, R+"blocks_while_operating":[1,1,0], R+"p_close_within_12m":0.4, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.5, R+"vendor_loan_term_years":5, R+"ebitda_growth_median":0.08})
print("=== for comparison: the 3-day plan with origination work (from last run)")
lead = {**base, R+"blocks_per_year":3, R+"blocks_during_search":3, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":3, R+"blocks_while_operating":[3,2,1,0], R+"seller_finance_share":0.5, R+"multiple_median":2.0, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.08, R+"contract_years_before_search":1, R+"p_close_within_12m":0.5, R+"p_manager_stays":0.85, R+"p_severe_decline_yr1":0.06}
run("L  3 days/wk 2027-28, origination, buy 2028, taper", lead)
run("L2 same but 2 days/wk (2 blocks/yr) and taper 2-1-0", {**lead, R+"blocks_per_year":2, R+"blocks_during_search":2, "general.blocks_fallback_per_year":2, R+"blocks_while_operating":[2,1,0]})
run("L3 same but 1 block/yr only (SOT one-block) with origination", {**lead, R+"blocks_per_year":1, R+"blocks_during_search":1, "general.blocks_fallback_per_year":1, R+"blocks_while_operating":[1,0]})
run("L4 A5-style seller-funded deal (80% VN, 12% growth) + 1 block/yr while searching", {**base, **noc, R+"blocks_during_search":1, R+"p_close_within_12m":0.5, R+"multiple_median":2.3, R+"max_search_years":3, R+"seller_finance_share":0.8, R+"vendor_loan_term_years":5, R+"ev_median":400000, R+"ev_p90":600000, R+"ebitda_growth_median":0.12})
