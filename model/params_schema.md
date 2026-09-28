# params.json schema for mc_model.py

Every leaf is an object: `{"value": <number|list>, "low": <number>, "high": <number>, "src": "<note file> — <one-line evidence + URL>", "confidence": "measured|derived|inferred"}`.
`low`/`high` are a plausible range for sensitivity sliders. Lists (survival curves, profit-by-year) use the same wrapper with list values.

Conventions
- Money in GBP nominal. Years: t=0 is calendar 2027, horizon 8 steps to end-2034 (Dale turns 40 in 2034).
- Lognormal parameters are given as `median` and `p90` pairs.
- Probabilities are annual unless the key says otherwise.
- "fit_multiplier" is applied to success probabilities (P(close), and divides failure probabilities). 1.0 = no adjustment. Leave at 1.0 with a `src` note describing the evidence for/against fit; the coordinator sets final fit values.

```
{
  "horizon": {"years": ...},                        // 8
  "general": {
    "start_investable",        // liquid investable at end-2026 after incoming £50k (SOT: ~£150–170k)
    "floor",                   // £120k never touched (SOT)
    "annual_burn",             // £20k conservative (SOT)
    "index_nominal_return_mean", "index_return_sd",   // from investment_returns_and_tax.md
    "target",                  // 750000
    "effective_tax_on_draw",   // blended tax on £70–100k owner draw via salary+dividends (investment_returns_and_tax.md)
    "effective_tax_on_contract", // marginal retention on a contracting block stacked on other income
    "effective_tax_on_exit",   // BADR 18% + CGT 24% blend on a £0.75–1.2m sale
    "risk_pot_now", "risk_pot_after_block"   // SOT: £50–70k now, £80–110k after one block — max personally-guaranteed bank debt
  },
  "routes": {
    "contract_only": {"kind": "contract", "block_gross_median", "block_gross_p90", "p_block_lands", "blocks_per_year", "hours_per_block_week", "health_recovery_weeks_per_block"},
    "buy_distributor": {"kind": "buy",
       "p_close_within_12m",      // P(a searching buyer completes a deal in a given year of search)
       "max_search_years",
       "ev_median", "ev_p90",     // EV distribution of in-envelope deals actually available (from listings + multiples notes)
       "multiple_median", "multiple_p90",   // entry multiple of adjusted EBITDA/SDE at this size & sector
       "seller_finance_share",    // share of EV as vendor loan
       "bank_share_of_cash_gap",  // share of (EV − vendor loan) funded by bank/GGS debt rather than cash
       "bank_rate", "bank_term_years", "vendor_loan_rate", "vendor_loan_term_years", "blended_debt_rate",
       "deal_costs", "wc_reserve_pct", "min_deal_scale",
       "manager_cost",            // £/yr fully loaded for the GM/ops manager the owner needs (0 if EBITDA already after a manager — state which)
       "p_manager_stays", "manager_leaves_factor",
       "yr1_ebitda_change_median", "yr1_ebitda_change_p90",   // EBITDA yr1 post-close ÷ EBITDA at purchase
       "p_severe_decline_yr1", "severe_decline_factor",       // P(>40% drop) and the factor
       "p_failure_annual_after_yr1", "pg_loss_share_on_failure",
       "ebitda_growth_median", "ebitda_growth_sd",
       "exit_multiple_median", "exit_multiple_p90", "exit_earliest_years_held", "p_sell_per_year_when_eligible",
       "hours_yr1", "hours_yr3", "f2f_share", "search_hours_week", "fit_multiplier"},
    "buy_services": {... same keys ...},
    "buy_hire": {...}, "buy_logistics": {...}, "buy_ecommerce": {...}, "buy_saas": {...}, "buy_agency": {...},
    "build_ecommerce": {"kind": "build", "capital_in", "survival_curve" (list of 5 annual conditional survival probs), "owner_profit_median_by_year" (list 5), "owner_profit_p90_by_year" (list 5), "p_reach_70k_by_yr3", "resale_multiple_median", "hours_yr1", "hours_yr3", "f2f_share", "fit_multiplier", "p_sell_per_year_when_eligible"},
    "build_services": {... same ...},
    "hybrid_plan": {"kind": "hybrid", ...all contract keys with blocks_per_year=1..., ...all buy_distributor keys...}
  }
}
```
