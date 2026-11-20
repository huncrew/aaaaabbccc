import mc_model as M
p = M.load_params(); N=10000; E="routes.build_ecommerce."
base={"general.blocks_fallback_per_year":3,"general.backstop_p_block_lands":0.8,"general.crypto_sleeve_share":0.10,"general.floor":60000}
def run(name, ov, route="build_ecommerce"):
    r=M.simulate(route,p,n=N,overrides={**base,**ov}); 
    print(f"  {name:78s} P750={r['p_target_by_2034']:5.1%} P500={r['p_500k_by_2034']:5.1%} NW50={r['nw_percentiles_2034']['50']/1e3:4.0f}k")
print("Build ecommerce 'strategically', 3-day contracting alongside until profit > £60k, 10% sleeve. Owner profit = after a VA/ops hire, before tax.")
print("Dale's own record (≈$500k rev over 3 yrs full-time ≈ £130k/yr rev; 20-30% net) ≈ £25-40k/yr -> this is the population median curve already modelled.")
run("population median (as modelled): profit 5/15/25/30/35k, resale 1.7x", {})
top1={E+"owner_profit_median_by_year":[15000,60000,125000,160000,190000], E+"owner_profit_p90_by_year":[40000,120000,250000,320000,380000],
      E+"survival_curve":[0.95,0.9,0.9,0.92,0.95], E+"resale_multiple_median":3.0, E+"fit_multiplier":1.0, E+"p_sell_per_year_when_eligible":0.35}
run("top-1% operator: profit 15/60/125/160/190k, survival 90-95%/yr, sells at 3.0x SDE", top1)
run("  same but profit ramps a year slower (15/40/90/140/170k)", {**top1, E+"owner_profit_median_by_year":[15000,40000,90000,140000,170000]})
run("  same as top-1% but survival 80%/yr (one bad platform/ad-cost year)", {**top1, E+"survival_curve":[0.9,0.8,0.8,0.85,0.9]})
run("  top-1% + 25% crypto sleeve", {**top1, "general.crypto_sleeve_share":0.25})
run("  top-1% but no contracting fallback (full time on it from 2027)", {**top1, "general.blocks_fallback_per_year":0})
print("\nFor comparison, same engine:")
R="routes.hybrid_2blocks_2y."
lead={R+"blocks_per_year":3,R+"blocks_during_search":3,R+"p_block_lands":0.8,R+"bank_term_years":10,R+"ebitda_growth_median":0.08,R+"contract_years_before_search":1,R+"p_close_within_12m":0.5,R+"p_manager_stays":0.85,R+"p_severe_decline_yr1":0.04,R+"multiple_median":2.3,R+"multiple_p90":2.8,R+"ev_median":250000,R+"ev_p90":350000,R+"seller_finance_share":0.65,R+"blocks_while_operating":[2,2,2,2,2,2],R+"fit_multiplier":1.10}
run("buy electrical servicing (lead plan)", lead, "hybrid_2blocks_2y")
run("buy an ecommerce brand at 2.3x and add your skill (15% growth)", {**lead,R+"fit_multiplier":1.2,R+"exit_multiple_median":2.7,R+"p_severe_decline_yr1":0.12,R+"p_manager_stays":0.6,R+"ebitda_growth_median":0.15}, "hybrid_2blocks_2y")
run("AI app (as modelled, for the comparison you raised)", {"routes.build_ai_app.fit_multiplier":1.0}, "build_ai_app")
