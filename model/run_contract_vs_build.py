import mc_model as M, numpy as np
p=M.load_params(); N=10000; B="hybrid_2blocks_2y"; R=f"routes.{B}."
def buy(name, blocks_before, years_before, blocks_while, fit=1.10, ev=250000, vn=0.65, sleeve=0.10, p_close=0.5, mult=2.3, extra={}):
    ov={R+"blocks_per_year":blocks_before, R+"blocks_during_search":blocks_before, R+"p_block_lands":0.8, "general.backstop_p_block_lands":0.8, "general.blocks_fallback_per_year":blocks_before,
        R+"bank_term_years":10, R+"ebitda_growth_median":0.08, R+"contract_years_before_search":years_before, R+"p_close_within_12m":p_close, R+"p_manager_stays":0.85,
        R+"p_severe_decline_yr1":0.04, R+"multiple_median":mult, R+"multiple_p90":mult+0.5, R+"ev_median":ev, R+"ev_p90":ev*1.4, R+"seller_finance_share":vn,
        R+"blocks_while_operating":blocks_while, R+"fit_multiplier":fit, "general.floor":60000, "general.crypto_sleeve_share":sleeve, **extra}
    r=M.simulate(B,p,n=N,overrides=ov); c=r["conditional"]
    print(f"  {name:76s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} deal={r['p_business_acquired']:4.0%} buy-yr={c['median_acquisition_year'] or 0:.0f} days≈{r['mean_employed_days_total']:4.0f} NW50={r['nw_percentiles_2034']['50']/1e3:4.0f}k")
print("A. CONTRACT TO GET CASH, THEN BUY (no ecommerce lanes)")
buy("A1 4 blocks/yr (full time) for 2 yrs, buy 2029, then 2 blocks/yr while owning", 4, 2, [2,2,1,0])
buy("A2 3 blocks/yr for 2 yrs, buy 2029, then 2/yr", 3, 2, [2,2,1,0])
buy("A3 3 blocks/yr, origination from yr 1, buy 2028, then 2/yr", 3, 1, [2,2,1,0])
buy("A4 as A3 but bigger firm (EV 385k, 50% VN) and taper 3-2-1-0", 3, 1, [3,2,1,0], ev=385000, vn=0.5)
buy("A5 as A3 but fit 0.95 (you dislike running it) ", 3, 1, [2,2,1,0], fit=0.95)
print("\nC. HYBRID: lanes + contracting + buy (lanes modelled as the side_option/probe overlay: £5k test, trade capital £25k if 5 buyers)")
so={"test_cost":5000,"p_five_buyers":0.5,"trade_capital":25000,"profit_median":25000,"profit_p90":60000,"p_fail_per_year":0.2,"hours_week":8}
so2={**so,"p_five_buyers":0.65,"profit_median":40000,"profit_p90":90000}
buy("C1 A3 + lanes at calibrated odds (profit med £25k)", 3, 1, [2,2,1,0], extra={R+"side_option":so})
buy("C2 A3 + lanes at Dale-record odds (profit med £40k, p 0.65)", 3, 1, [2,2,1,0], extra={R+"side_option":so2})
buy("C3 C2 with 25% sleeve", 3, 1, [2,2,1,0], sleeve=0.25, extra={R+"side_option":so2})
