# Browser research brief: real sales data for line selection (for the Cowork / browser models)

Goal: pick the product lines to sell on Amazon UK and eBay UK on what is actually selling, not on search-term proxies. Category-agnostic: if socks win, socks win. Fill `candidates_template.csv` (one row per product line) and save it as `browser_findings.csv` in this folder (or drop it in the Drive folder "Path to 750k - Trade line (lane B)"). The scoring script `score_lines.py` merges it with the supply-side data.

Use the seller's own logged-in tools first. They are first-party sales data, free, and allowed:

## 1. eBay: Terapeak Product Research (Seller Hub > Research > Product Research)
Real SOLD data, up to 3 years. For each candidate keyword set marketplace = eBay UK, last 90 days, condition New, format Fixed price. Record:
- `ebay_sold_90d` (total sold), `ebay_avg_sold_price_gbp`, `ebay_sell_through_pct`, `ebay_sellers` (number of sellers), `ebay_top_seller_share_pct` (top seller's units / total), `ebay_listings_active`
- Also run the Sourcing Insights / category view for the parent category and note any category flagged as high-demand, low-supply.

## 2. Amazon: Product Opportunity Explorer (Seller Central > Growth > Product Opportunity Explorer), marketplace UK
Amazon's own niche data. For each niche that matches a candidate record:
- `amz_search_volume_90d`, `amz_search_growth_90d_pct`, `amz_units_sold_90d` (niche units), `amz_avg_price_gbp`, `amz_products_in_niche`, `amz_top5_click_share_pct`, `amz_avg_review_count_top` (average reviews of top products), `amz_new_products_launched_180d`, `amz_successful_launches_180d`, `amz_return_rate_note`
- Also browse the Explorer by category for niches with: search volume growing, top-5 click share under 50%, average review count under 500, price £12–60. Add any such niche as a NEW row even if it is not on the candidate list. This is where unexpected winners come from.

## 3. Amazon listing pages (ordinary browsing)
For the top 5 products per niche: `amz_bsr_top` (best seller rank and category), "X bought in past month" badge value (`amz_bought_past_month_top`), number of sellers on the listing, FBA or merchant-fulfilled, whether Amazon itself is a seller (`amz_amazon_is_seller` yes/no). Amazon as a seller or a brand-gated listing = skip.

## 4. Fees (Amazon Revenue Calculator, eBay fee page)
`amz_referral_pct`, `amz_fba_fee_gbp` for the typical size/weight; `ebay_fvf_pct` for the category.

## 5. Sanity checks to note in `notes`
Brand dominance (one brand on page 1), restricted/gated category, hazmat (batteries, aerosols, liquids), certification needed, seasonality visible in Terapeak's 12-month chart, returns complaints in reviews, counterfeit/IP risk (never copy a branded product).

## Rules
- Human pace, logged-in seller tools, no bulk scraping, no automation against pages that block it.
- Numbers exactly as shown, with the date and the search term used (`search_term`, `date_seen`).
- If a tool does not show a field, leave it blank; do not estimate.
- 30–60 rows is plenty for round one: the 15 trade survivors already in the template, plus whatever the Opportunity Explorer browse turns up.
