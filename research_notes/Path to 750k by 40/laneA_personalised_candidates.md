# Lane A — Personalised / made-to-order product lines for the US market (candidate scan)

Date: 2026-10-23. Companion file: `laneA_personalised_candidates.csv` (64 candidate lines, one row each, every number with a source URL or a stated estimation method). Budget used: 105 of ~120 searches/fetches; stopped at 105 and wrote up.

## 1. What this is

A scored list of 64 personalised / made-to-order product LINES that two established US-facing Etsy shops (designers in the Philippines, US print-on-demand partners, channels Etsy + Amazon Custom + Walmart + eBay + Faire, no paid ads above 5% of revenue) could add. Each line is scored 0–100, filtered to 15 survivors, and the survivors carry unit economics per channel.

## 2. Method and data sources (what worked, what was blocked)

| Source (tried in the order asked) | Result | Used for |
|---|---|---|
| Google Trends via pytrends (5-y weekly, US) | **BLOCKED — HTTP 429 TooManyRequests** on both attempts (first batch of 5 terms; retry after a 45 s pause with 2 terms). Not circumvented. | Nothing. Seasonality index taken instead from RankHero's 12-month Google-type monthly series (see below). |
| Etsy search pages and autocomplete (`etsy.com/search?q=`, `suggestions_ajax.php`) | **BLOCKED — HTTP 403** on both endpoints, with and without a browser UA. | Nothing directly. |
| Etsy fee help page (help.etsy.com) | **403.** Fees taken from three third-party fee guides that agree (craftybase, checkoutpage, gelato); figures match the brief. | Fees. |
| eRank public blogs | OK. Rank lists for Sep-2026 and full-year 2025; "personalized gift" #4 in 2025 (up from #21); "personalized gifts" #97 (down from #13); "mugs" #73 (down from #14); "wall art" #3 (down from #1). No per-keyword volumes in text. | Trend direction, candidate generation. |
| **RankHero keyword pages** (`rankhero.com/keywords/<term>`) — found via the Alura/EverBee/Marmalead search | **Primary source.** Public per-keyword pages with: global monthly searches (source not named on page; CPC and country split indicate Google Ads data), USA searches, Etsy listing count (global and USA), keyword difficulty, a 12-month monthly series, and a price distribution with median. 55 pages fetched. | Demand, competition, seasonality, market price. |
| Amazon.com best-seller pages | **BLOCKED — HTTP 503.** | — |
| AsinSight public Amazon reports (`asinsight.com/report/US/<term>`) | OK — estimated monthly unit sales for the top ASINs per keyword and Amazon weekly search volume. Used for 4 proxies. | Amazon sold-velocity evidence. |
| Walmart.com search | **BLOCKED — bot-verification challenge ("hold the button").** | — |
| Faire category pages and Faire support article on commission | **403 on both.** Commission figures from Faire-citing third parties (craftybase, eightx). | Faire fees. |
| Pinterest Trends | Page returned only a title (JS app); no data. | — |
| Reddit r/EtsySellers, r/Etsy | **Fetch not permitted by the tool for reddit.com**; two web searches with site filters returned no Reddit threads. Substituted with seller-tool blogs (insightagent, listifyai, printify) for the evergreen-vs-seasonal view. | Qualitative only. |
| Etsy Seller Handbook trend reports | Not reachable directly; secondary coverage says Etsy reports >25% of Nov–Dec sales carry a personalisation request. | Context. |
| POD price lists | Printful and Prodigi catalogue pages render client-side (no prices in HTML); Printify product pages show "Loading…". Prices taken from (a) Printify category pages as indexed by search ("From USD x"), (b) podvector.ai's May-2026 Printful/Printify price tables, (c) Printify's custom-puzzle page. | COGS. |
| Market size | Arizton: US personalised gifts USD 9.69bn (2024) → 14.56bn (2030), 7.03% CAGR (https://www.arizton.com/market-reports/united-states-personalized-gifts-market). Technavio: +USD 5.27bn 2024–29 at 9.9% CAGR. No Statista page surfaced. | Context. |

### Scoring rubric (0–100)
- **Demand (25)** on *effective* US monthly searches = RankHero USA searches × a relevance factor (1.0 for product-specific terms; 0.1–0.5 for broad gift terms such as "anniversary gift" where printed keepsakes are a minority of results — the factor and reason are in the CSV). Bands: ≥50k 25 · ≥20k 22 · ≥10k 19 · ≥5k 15 · ≥2k 11 · ≥1k 8 · ≥500 5 · else 2. **Survivor threshold: ≥2,000 effective (score ≥11).**
- **Competition (15)** = USA Etsy listings ÷ USA monthly searches (listings per monthly search). <1 → 15 · <3 → 12 · <8 → 9 · <20 → 6 · <50 → 3 · else 1.
- **Gross margin (20)** on Etsy at the stated price after POD base + partner US shipping + design labour + Etsy fees (6.5% + 3% + $0.25 + $0.20). ≥60% 20 · ≥50% 16 · ≥40% 12 · ≥30% 6 · else 0. **Survivor threshold 40%.**
- **Evergreen (15)** seasonality index = peak month ÷ 12-month mean of the RankHero monthly series (Sep-2025→Aug-2026 or Oct-2025→Sep-2026 depending on page). <1.2 → 15 · <1.35 → 12 · <1.5 → 9 · <2 → 5 · <3 → 2 · else 0. Threshold 1.5 is reported as a warning, not a gate (per brief, survivors = demand + margin + chain fit).
- **Chain fit (10)**: 10 = designers + existing print partners (poster/canvas/framed); 7 = POD catalogue item the chain does not yet use (ornament, blanket, pillow, mug, puzzle, acrylic); 4 = needs an engraving / outdoor-sign partner not in the chain. **Survivor threshold ≥7.**
- **Repeat / gifting recurrence (10)**: judgement — annual occasions and multi-recipient families score high.
- **Ticket (5)**: ≥$40 5 · ≥$30 4 · ≥$20 2 · else 1.

### Cost assumptions (all in the CSV per row)
- POD base + partner US shipping, listed with free shipping to the buyer. Poster 18×24 $15.50 (Printify enhanced matte $10.50 + est. $5 ship; Printful premium luster equivalent $24.94). Canvas 16×20 $38.44 (Printful $29.95 + $8.49). Framed 16×20 $56.98 (Printful $46.49 + $10.49). Sources: https://podvector.ai/articles/printful/costs-and-charges/printful-poster-pricing-full-breakdown-for-pod-sellers ; https://podvector.ai/articles/printful/reviews/printful-custom-home-decor-review-honest-breakdown-for-pod-sellers ; Printify framed vertical poster "From USD 35.89" (11×14) at https://printify.com/app/products/home-and-living/posters.
- Design labour: **assumption** of a $6/hour fully-loaded Philippines designer → $1.00 (10-min name/date drop-in), $2.00 (20-min star map / map / soundwave render), $9.00 (90-min illustrated portrait), $15.00 (150-min multi-figure or building illustration). Replace with actuals.
- Format price floors applied so margin reflects the format, not an arbitrary price: canvas $89.95, framed $119, blanket $79.95, pillow $39.95, acrylic $129. The market median for the anchor keyword sits beside it in the CSV; where our price is well above the median (e.g. framed retirement print at $119 vs $23 median), treat conversion as the risk, not margin.
- Etsy Offsite Ads: 12% (shops over $10k/yr) shown as a separate per-order case; Amazon and Walmart 15% referral (Home & Kitchen / Home, Kitchen, Decor & Garden); Faire 15% on reorders, 25% on a new retailer's first order (third-party figures; Faire's page was 403), on a wholesale price of 50% of retail.

## 3. Top 15 survivors (pass demand ≥2,000 effective US searches, Etsy GM ≥40%, chain fit ≥7), ranked by total score

| # | Line | Score | Eff. US searches/mo | US listings per search | SI | Etsy GM | Why (one line) |
|---|---|---|---|---|---|---|---|
| 1 | Birth-flower family bouquet print | 88 | 22,625 | 1.4 | 1.14 | 50.6% | largest flat-demand term in the set (90.5k US/mo, SI 1.14), only 1.4 listings per search, pure design work on an existing poster SKU; family/grandparent gifting recurs with every new child. |
| 2 | Custom star map print (night sky by date/place) | 85 | 18,100 | 1.0 | 1.22 | 50.6% | 18.1k US/mo, difficulty 31 ('easy'), ~1 listing per search, SI 1.22; a render template the designers can run in minutes; feeds anniversary, wedding and birth occasions all year. |
| 3 | Custom city/coordinates map print | 68 | 18,100 | 5.4 | 2.19 | 50.6% | 18.1k US/mo on 97k US listings; same render workflow as star maps; Nov–Dec spikes (SI 2.19) but a 27k+ floor in every month. |
| 4 | Small-business logo sign (acrylic/canvas, B2B) | 67 | 12,100 | 5.8 | 1.45 | 42.1% | 12.1k US/mo, SI 1.45, $129 ticket on a Printify acrylic product; B2B buyers reorder for new locations/events and it is a natural Faire / Walmart line — needs the acrylic SKU priced before launch. |
| 5 | Housewarming print (house sketch + address + date) | 61 | 6,050 | 26.4 | 1.8 | 50.6% | 60.5k US/mo on the broad term (10% relevance applied); the house-sketch-plus-address format is a 20-minute designer job and sells year-round (floor 165k global). |
| 6 | Watercolour portrait from photo (people/pets) | 61 | 3,600 | 43.4 | 1.03 | 48.9% | flattest series in the set (SI 1.03), 3.6k US/mo, $59.95 poster at 49% margin; reuses the shop's portrait skill with a lower design minute count than full illustrations. |
| 7 | Pet portrait (photo-to-art, non-memorial) | 60 | 12,100 | 41.1 | 1.64 | 40.6% | the shop's own faded line still has 12.1k US/mo and Amazon proof (AsinSight top-10 avg 570 units/mo); margin is the thin one at 40.6% because of 90-min design time — raise price or template the style. |
| 8 | Nursery name + birth-stats print | 60 | 2,400 | 602.2 | 1.03 | 48.1% | demand steady (SI 1.03) and Amazon personalised baby gifts move 4–7k units/mo per top ASIN, but 1.45M US listings make it the most saturated survivor — launch only as a bundle/variant of birth-flower or star-map. |
| 9 | Retirement print (years of service / 'the legend') | 60 | 4,065 | 9.3 | 1.33 | 40.6% | 27.1k US/mo, SI 1.33 (May–Jun peak), framed $119 at 40.6%; recurrence is low (one per retiree) but the buyer is often an office — route to corporate/B2B listings too. |
| 10 | Baptism / christening print | 57 | 2,960 | 15.7 | 1.41 | 48.1% | 14.8k US/mo (20% relevance), SI 1.41, 48% margin on a $39.95 poster; faith-occasion gifting from godparents/grandparents gives repeat buyers. |
| 11 | Golf course map / scorecard print | 56 | 2,710 | 6.5 | 4.24 | 50.6% | 27.1k US/mo on 'golf gift' (10% relevance) and only 6.5 listings per search; custom-map engine reused; **SI 4.24 — Christmas/Father's Day line, not evergreen.** |
| 12 | Anniversary 'our story' print (star map/map/dates) | 55 | 4,950 | 41.4 | 1.8 | 45.0% | 49.5k US/mo broad term, canvas $89.95 at 45%; Feb peak (SI 1.8) but annual recurrence per couple is the best in the set. |
| 13 | Human memorial print (in loving memory, photo+poem) | 53 | 6,600 | 90.8 | 1.84 | 45.0% | 6.6k US/mo, canvas $89.95 at 45%; 599k US listings so it needs a distinct art style; pairs with the pet-memorial sub-lines that failed on margin only because of illustration time. |
| 14 | Wedding gift print (names/date/venue) | 51 | 3,310 | 92.3 | 1.8 | 40.6% | 33.1k US/mo broad term (10% relevance), framed $119 at 40.6%; Feb–Mar peak; same render workflow as star map/map. |
| 15 | Established family-name sign (canvas) | 51 | 2,400 | 34.9 | 1.78 | 46.2% | 2.4k US/mo, median market price $48 supports a $79.95 canvas at 46%; Nov–Dec lift (SI 1.78) but a 2.4k floor; a template line the designers can run unattended. |

Also passed all three gates but ranked 16th (not in the top 15): Dog memorial framed print (score 49). Near-misses that failed only margin at the stated format: Family portrait illustration (30.6%, 150-min design time), Pet memorial portrait canvas (37.3%), Sympathy blanket (30%), Personalised baby blanket (30%), Custom puzzle (27.7% at $44.95 vs $20 market median), Personalised mug (33%). Failed on chain fit despite strong demand: Engraved cutting board (14.8k US/mo, 3.0 listings per search — no POD engraving price found) and Address sign (outdoor partner).

## 4. Unit economics per survivor

Price is the free-shipping retail price. COGS = POD base + partner US shipping. Design = per-order designer minutes at the $6/h assumption. Etsy fees = 6.5% transaction + 3% + $0.25 processing + $0.20 listing renewal. 'Etsy+OSA' adds the 12% Offsite Ads fee on an attributed order. Amazon/Walmart = 15% referral (Amazon Custom also needs the $39.99/mo Professional plan — fixed, not per order). Faire = wholesale at 50% of retail, 15% commission on reorders (25% on a retailer's first order). Orders/month = orders needed for $2,500 gross profit on Etsy at the base fee case.

| Line | Format | Price | COGS | Design | Etsy fees | Etsy GP | Etsy GM | Etsy+OSA GM | Amazon GM | Walmart GM | Faire reorder GM (on wholesale) | Orders/mo for $2.5k GP | POD price source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Birth-flower family bouquet print | poster18x24 | $44.95 | $15.50 | $2.00 | $4.72 | $22.73 | 50.6% | 38.6% | 46.1% | 46.1% | 7.1% ($1.60) | 110 | Printify enhanced-matte poster 18x24 $10.50 |
| Custom star map print (night sky by date/place) | poster18x24 | $44.95 | $15.50 | $2.00 | $4.72 | $22.73 | 50.6% | 38.6% | 46.1% | 46.1% | 7.1% ($1.60) | 110 | Printify enhanced-matte poster 18x24 $10.50 |
| Custom city/coordinates map print | poster18x24 | $44.95 | $15.50 | $2.00 | $4.72 | $22.73 | 50.6% | 38.6% | 46.1% | 46.1% | 7.1% ($1.60) | 110 | Printify enhanced-matte poster 18x24 $10.50 |
| Small-business logo sign (acrylic/canvas, B2B) | acrylic | $129.00 | $60.00 | $2.00 | $12.70 | $54.30 | 42.1% | 30.1% | 36.9% | 36.9% | -11.1% ($-7.17) | 47 | Printify provider Acrylic Idea Factory acrylic print 'From EUR 46.72' |
| Housewarming print (house sketch + address + date) | poster18x24 | $44.95 | $15.50 | $2.00 | $4.72 | $22.73 | 50.6% | 38.6% | 46.1% | 46.1% | 7.1% ($1.60) | 110 | Printify enhanced-matte poster 18x24 $10.50 |
| Watercolour portrait from photo (people/pets) | poster18x24 | $59.95 | $15.50 | $9.00 | $6.15 | $29.30 | 48.9% | 36.9% | 44.1% | 44.1% | 3.3% ($0.98) | 86 | Printify enhanced-matte poster 18x24 $10.50 |
| Pet portrait (photo-to-art, non-memorial) | poster18x24 | $49.95 | $15.50 | $9.00 | $5.20 | $20.25 | 40.6% | 28.6% | 36.0% | 36.0% | -13.1% ($-3.27) | 124 | Printify enhanced-matte poster 18x24 $10.50 |
| Nursery name + birth-stats print | poster18x24 | $39.95 | $15.50 | $1.00 | $4.25 | $19.20 | 48.1% | 36.1% | 43.7% | 43.7% | 2.4% ($0.48) | 131 | Printify enhanced-matte poster 18x24 $10.50 |
| Retirement print (years of service / 'the legend') | framed16x20 | $119.00 | $56.98 | $2.00 | $11.75 | $48.27 | 40.6% | 28.6% | 35.4% | 35.4% | -14.1% ($-8.40) | 52 | Printful framed poster 16x20 black/white $46.49 + $10.49 US ship |
| Baptism / christening print | poster18x24 | $39.95 | $15.50 | $1.00 | $4.25 | $19.20 | 48.1% | 36.1% | 43.7% | 43.7% | 2.4% ($0.48) | 131 | Printify enhanced-matte poster 18x24 $10.50 |
| Golf course map / scorecard print | poster18x24 | $44.95 | $15.50 | $2.00 | $4.72 | $22.73 | 50.6% | 38.6% | 46.1% | 46.1% | 7.1% ($1.60) | 110 | Printify enhanced-matte poster 18x24 $10.50 |
| Anniversary 'our story' print (star map/map/dates) | canvas16x20 | $89.95 | $38.44 | $2.00 | $9.00 | $40.51 | 45.0% | 33.0% | 40.0% | 40.0% | -4.9% ($-2.21) | 62 | Printful canvas 16x20 1.25in $29.95 + $8.49 US ship |
| Human memorial print (in loving memory, photo+poem) | canvas16x20 | $89.95 | $38.44 | $2.00 | $9.00 | $40.51 | 45.0% | 33.0% | 40.0% | 40.0% | -4.9% ($-2.21) | 62 | Printful canvas 16x20 1.25in $29.95 + $8.49 US ship |
| Wedding gift print (names/date/venue) | framed16x20 | $119.00 | $56.98 | $2.00 | $11.75 | $48.27 | 40.6% | 28.6% | 35.4% | 35.4% | -14.1% ($-8.40) | 52 | Printful framed poster 16x20 black/white $46.49 + $10.49 US ship |
| Established family-name sign (canvas) | canvas16x20 | $89.95 | $38.44 | $1.00 | $9.00 | $41.51 | 46.2% | 34.2% | 41.2% | 41.2% | -2.7% ($-1.21) | 61 | Printful canvas 16x20 1.25in $29.95 + $8.49 US ship |

Reading the table: a $44.95 poster line clears $2,500/month at ~110 orders (about 4 a day); the $89.95 canvas and $119 framed lines need 52–62 orders. Faire wholesale only works on the poster formats (positive but thin) — canvas/framed go negative at a 50% wholesale price with Printful's base costs, so Faire lines should be unframed prints or a cheaper partner. Etsy's base take (9.5% + $0.45) is lower than Amazon's and Walmart's 15% for any ticket above ~$8, so Etsy base margins are the best in the table; an Offsite-Ads-attributed Etsy order (21.5% + $0.45) is the most expensive case of all.

Fee example (star map poster $44.95): transaction 0.065×44.95 = $2.92; processing 0.03×44.95+0.25 = $1.60; listing $0.20; total $4.72 (10.5%). COGS $15.50 + design $2.00 → GP $22.73, GM 50.6%. With Offsite Ads: +$5.39 → GP $17.34 (38.6%).

## 5. Three lines to launch first inside an established shop, and why

1. **Custom star map print (poster, with canvas/framed upsell).** Best demand-to-competition ratio in the whole set (18.1k US searches vs 17.3k US listings, difficulty 31), flat all year (SI 1.22), 50.6% margin at $44.95, and the render is a template the Philippines team can run in 20 minutes. An established Star Seller shop with 1,000+ reviews ranks for a mid-competition term faster than a new shop. Occasion coverage (anniversary, wedding, birth, memorial dates) means the same SKU answers several gift searches.
2. **Birth-flower family bouquet print.** Largest flat demand in the set (90.5k US/mo, SI 1.14, 1.4 listings per search even after discounting 75% of the intent to jewellery). Pure illustration-library work: draw the 12 flowers once, then every order is a 20-minute assembly. Recurs with each new grandchild and is the strongest Mother's Day / grandparent line that is not seasonal. Natural Faire line as an unpersonalised zodiac/birth-month print series.
3. **Custom city / coordinates map print, with the housewarming house-sketch variant as the same listing family.** Same render engine and partner SKUs as the star map, so the second and third lines cost almost nothing extra to launch. 18.1k US/mo with Nov–Dec spikes (SI 2.19) complements the star map's flat profile, and the housewarming variant (effective 6k US/mo, year-round) converts the map into a $44.95–$89.95 new-home gift.

Why not pet portraits first: the shop's own data shows the line faded, demand is still real (12.1k US/mo) but 90-minute design time leaves 40.6% at $49.95 and 41 listings per search. Re-enter it later via the watercolour style (SI 1.03, 49% margin) and the memorial variants once the three template lines are running.

## 6. Which survivors also suit Amazon Custom, Walmart, Faire

| Line | Amazon Custom (seller-fulfilled personalised) | Walmart Marketplace | Faire (wholesale to boutiques) |
|---|---|---|---|
| Star map print | Yes — text/date inputs map to Amazon Custom fields; GM 60% at $44.95 after 15% referral. | Yes (printed wall art, 15%). | Only as an unpersonalised "night sky over [city]" print series. |
| Birth-flower bouquet | Yes — name + month inputs. AsinSight shows Amazon personalised-baby gifts moving 4–7k units/mo per top ASIN, so the category has Amazon demand. | Yes. | **Best Faire line** — zodiac/birth-month print sets, no personalisation needed. |
| Custom map / housewarming | Yes — address/coordinates inputs. | Yes. | Partial (city series). |
| Small-business logo sign | Marginal — logo upload is supported but Amazon buyers skew consumer. | Yes, but acrylic SKU must be priced first. | Yes — boutiques buy "open/hours" and brand signs; Faire GM positive only if the acrylic COGS is below ~$45. |
| Watercolour / pet portrait | Yes — photo upload; Amazon pet-portrait top-10 average 570 units/mo at $18 (price pressure is severe on Amazon). | Weak (low-price competition). | No. |
| Nursery / baptism / anniversary / wedding / established-name / memorial prints | Yes — all are name/date inputs. | Yes (wall art). | Only the unpersonalised versions. |
| Retirement / golf | Yes. | Yes. | Golf: yes as a course-map print series for pro-shop boutiques. |

## 7. Seasonality warnings (index = peak month ÷ 12-month mean, RankHero series)

- **Extreme (index >3): plan stock-free, launch 8 weeks before the peak, expect near-zero sales otherwise.** Custom stocking 5.95, Personalised ornament 5.14, Memorial ornament 4.78, Golf gift 4.24 (Dec = 201k vs 18k Jan), Grandma gift 3.99 (Dec = 49.5k vs 5.4k Jun), Fishing gift 3.34, Custom puzzle 3.17, Personalised blanket 3.03.
- **Strong (2–3):** Graduation 2.81 (May), Christian gift 2.82 (Dec), Teacher gift 2.34 (Dec and Jun–Jul), Family tree gift ~2.4 (Dec), Custom map 2.19 (Nov–Dec), Nurse gift 2.17 (Dec, May), Military gift 2.15.
- **Moderate (1.5–2):** Housewarming 1.80 (Feb–Mar), Anniversary 1.80 (Feb), Wedding 1.80 (Feb–Mar), Corporate gift 1.88 (Sep–Oct), Memorial gift 1.84 (Nov–Dec), New-home gift 1.52, Pet portrait 1.64, Established family-name sign 1.78.
- **Evergreen (<1.5):** Watercolour portrait 1.03, Nursery wall art 1.03, Handwritten recipe 1.04, Line-art portrait 1.06, Sympathy gift 1.13, Address sign 1.13, Birth flower 1.14, Baby stats 1.20, Star map 1.22, Pet memorial 1.24, Song lyrics 1.31, Retirement 1.33, Established sign 1.35, Baptism 1.41, Soundwave 1.41, Business sign 1.45.
- Caveat: the index uses one 12-month Google-type series, not five years of Google Trends (blocked). A single year can overstate or understate a peak; the brief's 5-year weekly view remains to be done when Trends access is available.

## 8. Five gaps I could not fill, and why

1. **Etsy-native search volume and sold-velocity.** Etsy search, autocomplete and the fee page all returned 403; eRank/Printify blogs publish ranks but not volumes. The demand column is therefore Google-type monthly search volume with an Etsy listing count, not Etsy searches or Etsy sales per listing. Marketplace Insights (15 free searches/week inside the seller account) would close this in an afternoon for the 15 survivors.
2. **Five-year seasonality and trend direction.** Google Trends returned 429 on both attempts, so the evergreen score rests on one 12-month series per keyword. Year-on-year change is only available where RankHero states it (memorial gift −18%, soundwave −34%).
3. **Engraved and outdoor-sign base costs.** No POD partner price was found for engraved cutting boards, engraved keepsakes or outdoor address signs within budget, so the highest-demand engraved line (personalised cutting board, 14.8k US/mo, 3 listings per search) is scored but cannot be a survivor until a partner quote exists. Printify lists acrylic signs and wooden ornaments but the pages render client-side.
4. **Amazon and Walmart category evidence.** Amazon best-seller pages (503) and Walmart search (bot challenge) were blocked; the only Amazon evidence is AsinSight's estimates for four keywords (pet portrait, personalised wall art, personalised signs, baby blankets/gifts). No evidence at all for Walmart demand on these lines.
5. **Actual partner costs and the design-labour rate.** The shop's own framed-print and canvas costs are not in the brief, so public Printful/Printify prices were used (Printful's framed poster is the expensive case). The $6/hour designer assumption drives the pet/family portrait margins; at $4/hour the family-portrait canvas line passes 40%, at $10/hour the watercolour line falls below it. Both inputs should be replaced with actuals before any ranking between the illustrated lines is trusted.

## 9. Source index (every URL used)

- https://www.rankhero.com/keywords/address-sign
- https://www.rankhero.com/keywords/anniversary-gift
- https://www.rankhero.com/keywords/baby-stats
- https://www.rankhero.com/keywords/baptism-gift
- https://www.rankhero.com/keywords/birth-flower
- https://www.rankhero.com/keywords/business-sign
- https://www.rankhero.com/keywords/christian-gift
- https://www.rankhero.com/keywords/coach-gift
- https://www.rankhero.com/keywords/corporate-gift
- https://www.rankhero.com/keywords/couples-portrait
- https://www.rankhero.com/keywords/custom-car-portrait
- https://www.rankhero.com/keywords/custom-caricature
- https://www.rankhero.com/keywords/custom-map
- https://www.rankhero.com/keywords/custom-pet-portrait
- https://www.rankhero.com/keywords/custom-portrait
- https://www.rankhero.com/keywords/custom-puzzle
- https://www.rankhero.com/keywords/custom-star-map
- https://www.rankhero.com/keywords/custom-stocking
- https://www.rankhero.com/keywords/dog-memorial-gift
- https://www.rankhero.com/keywords/engraved-gift
- https://www.rankhero.com/keywords/established-sign
- https://www.rankhero.com/keywords/family-name-sign
- https://www.rankhero.com/keywords/family-portrait
- https://www.rankhero.com/keywords/family-tree-gift
- https://www.rankhero.com/keywords/fishing-gift
- https://www.rankhero.com/keywords/godmother-gift
- https://www.rankhero.com/keywords/golf-gift
- https://www.rankhero.com/keywords/graduation-gift
- https://www.rankhero.com/keywords/grandma-gift
- https://www.rankhero.com/keywords/handwritten-recipe
- https://www.rankhero.com/keywords/house-portrait
- https://www.rankhero.com/keywords/housewarming-gift
- https://www.rankhero.com/keywords/line-art-portrait
- https://www.rankhero.com/keywords/memorial-gift
- https://www.rankhero.com/keywords/memorial-ornament
- https://www.rankhero.com/keywords/military-gift
- https://www.rankhero.com/keywords/new-home-gift
- https://www.rankhero.com/keywords/nurse-gift
- https://www.rankhero.com/keywords/nursery-wall-art
- https://www.rankhero.com/keywords/personalized-blanket
- https://www.rankhero.com/keywords/personalized-cutting-board
- https://www.rankhero.com/keywords/personalized-doormat
- https://www.rankhero.com/keywords/personalized-ornament
- https://www.rankhero.com/keywords/pet-memorial
- https://www.rankhero.com/keywords/pet-portrait
- https://www.rankhero.com/keywords/push-pin-map
- https://www.rankhero.com/keywords/retirement-gift
- https://www.rankhero.com/keywords/song-lyrics-print
- https://www.rankhero.com/keywords/soundwave-art
- https://www.rankhero.com/keywords/star-map
- https://www.rankhero.com/keywords/sympathy-gift
- https://www.rankhero.com/keywords/teacher-gift
- https://www.rankhero.com/keywords/watercolor-portrait
- https://www.rankhero.com/keywords/wedding-gift
- https://help.erank.com/blog/most-searched-keywords-on-etsy/ (Sep-2026 top searches)
- https://help.erank.com/blog/top-etsy-searches-in-2025/ (2025 annual ranks)
- https://help.erank.com/blog/etsy-mothers-day-gift-trends-2026/
- https://printify.com/blog/top-etsy-searches/ (seasonal keyword calendar; market-size quote)
- https://podvector.ai/articles/printful/costs-and-charges/printful-poster-pricing-full-breakdown-for-pod-sellers (Printful poster/framed/canvas table, May-2026)
- https://podvector.ai/articles/printful/reviews/printful-custom-home-decor-review-honest-breakdown-for-pod-sellers (Printful vs Printify home-decor table, May-2026)
- https://printify.com/app/products/home-and-living/posters ; https://printify.com/app/products/home-and-living/kitchen-accessories ; https://printify.com/custom-puzzles/ ; https://printify.com/app/print-provider/104/acrylic-idea-factory ; https://printify.com/custom-acrylic-signs/
- https://www.asinsight.com/report/US/custom-pet-portrait ; https://www.asinsight.com/report/US/personalized-wall-art ; https://www.asinsight.com/report/US/personalized-signs ; https://www.asinsight.com/report/US/personalized-baby-gifts-girl ; https://www.asinsight.com/report/US/personalized-baby-blankets-for-girls
- Fees: https://app.craftybase.com/blog/the-complete-guide-to-etsy-fees ; https://checkoutpage.com/blog/etsy-fees ; https://www.repricer.com/?p=1593 (Amazon 15% Home & Kitchen) ; https://ecomcircles.com/blog/walmart-marketplace-fees/ ; https://craftybase.com/blog/how-much-does-faire-charge ; https://faire.com/support/articles/360040446591 (403)
- Market size: https://www.arizton.com/market-reports/united-states-personalized-gifts-market ; https://www.technavio.com/report/personalized-gifts-market-in-us-industry-analysis
- Blocked: https://www.etsy.com/search?q=... (403) ; https://www.etsy.com/suggestions_ajax.php (403) ; https://help.etsy.com/hc/en-us/articles/360000344908 (403) ; https://www.amazon.com/Best-Sellers-Home-Kitchen-Personalized-Gifts/zgbs/home-garden/ (503) ; https://www.walmart.com/search?q=personalized+gifts (bot challenge) ; https://www.faire.com/category/home-decor/wall-art (403) ; https://trends.pinterest.com/ (no server-rendered data) ; old.reddit.com (fetch not permitted) ; Google Trends API via pytrends (429 ×2)
