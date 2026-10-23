# Product plan v1: what to sell, how demand is proved, how it reaches the money

*Built from two research passes (23 Oct 2026): `laneA_personalised_candidates.csv/.md` (64 lines scored, 15 survivors) and `laneB_trade_candidates.csv/.md` (66 lines scored, 27 pass, final 15). Method as in `Ecom-dist system design v1.md`. Every figure traces to a URL in the CSVs. Where a source was bot-blocked the agents recorded it and used a proxy, flagged in the `is_estimate` / `flags` columns.*

## 1. Targets this plan has to hit

| | Lane A (US personalised, made-to-order) | Lane B (UK trade consumables and spares) |
|---|---|---|
| Revenue | £150k/yr ≈ $16k/month | £200k/yr ≈ £16.7k/month |
| Gross profit needed | ≈ £70k (45%) | ≈ £64k (32%) ≈ £5.3k/month |
| What that is in lines | 3 lines at ~110 orders/month each, or 5–6 lines at half that | 2–3 SKUs at the £2,500/month gross-profit rate, or 8–10 at a third of it |
| Capital | None (made to order) | ≈ £23k average stock at 6 turns; under the £40k cap |

## 2. Lane A: the survivors

| Rank | Line | Effective US searches/mo | Listings per search | Seasonality (peak ÷ mean) | Price | Etsy gross margin | Amazon margin | Orders/mo for $2,500 GP |
|---|---|---|---|---|---|---|---|---|
| 1 | Birth-flower family bouquet print | 22,600 | 1.4 | 1.14 | $44.95 | 51% | 46% | 110 |
| 2 | Custom star map print | 18,100 | 1.0 | 1.22 | $44.95 | 51% | 46% | 110 |
| 3 | Custom city / coordinates map (housewarming variant) | 18,100 | 5.4 | 2.19 | $44.95 | 51% | 46% | 110 |
| 4 | Small-business logo sign (acrylic/canvas), B2B | 12,100 | 5.8 | 1.45 | $129 | 42% | 37% | 47 |
| 5 | Housewarming house-sketch + address print | 6,050 | 26 | 1.80 | $44.95 | 51% | 46% | 110 |
| 6 | Watercolour portrait from photo | 3,600 | 43 | 1.03 | $59.95 | 49% | 44% | 86 |
| 7 | Pet portrait (photo-to-art) | 12,100 | 41 | 1.64 | $49.95 | 41% | 36% | 124 |
| 8 | Nursery name + birth-stats print | 2,400 | 602 | 1.03 | $39.95 | 48% | 44% | 131 |
| 9 | Retirement print | 4,065 | 9 | 1.33 | $119 | 41% | 35% | 52 |
| 10 | Baptism / christening print | 2,960 | 16 | 1.41 | $39.95 | 48% | 44% | 131 |
| 11 | Golf course map / scorecard | 2,710 | 6.5 | **4.24** | $44.95 | 51% | 46% | 110 |
| 12 | Anniversary "our story" print | 4,950 | 41 | 1.80 | $89.95 | 45% | 40% | 62 |
| 13 | Human memorial print | 6,600 | 91 | 1.84 | $89.95 | 45% | 40% | 62 |
| 14 | Wedding gift print | 3,310 | 92 | 1.80 | $119 | 41% | 35% | 52 |
| 15 | Established family-name sign (canvas) | 2,400 | 35 | 1.78 | $89.95 | 46% | 41% | 61 |

**Launch first:** star map, birth-flower bouquet, custom map with the housewarming variant. All three are template renders on the poster SKU already produced, design time per order is minutes, margins 51% on Etsy, and the three together at 110 orders a month each are the whole £150k lane target. Canvas ($89.95) and framed ($119) are upsell tiers needing 52–62 orders/month each.

**Channel notes (from the CSV):** Etsy's take (9.5% + $0.45) beats Amazon Custom and Walmart (15%); an Etsy order attributed to Offsite Ads loses ~12 points of margin. Faire works only for unframed poster sets at 50% wholesale (canvas and framed go negative); birth-flower and zodiac print sets are the Faire line. Golf is seasonal (index 4.2): run it as a spring campaign, not a core line.

**What failed and why it matters:** engraved cutting boards had demand (14.8k/mo, 3 listings per search) but no partner price could be found; family-portrait illustration and pet-memorial canvas fell under 40% margin at a $6/h design assumption; ornaments and stockings are seasonal (index above 4.7). Your old pet-portrait line passes at 41% only because of 90 minutes of design time per order, which is the data saying why it felt thin.

## 3. Lane B: the final 15

Landed cost uses the playbook method (FOB ÷ 1.30 × (1.20 + duty), freight, broker, 3PL). Trade sell = 90% of a UK distributor's public price. Margins at the primary channel; marketplace lines are after Amazon 15% / eBay 13%.

| Rank | Line | Primary channel | FOB | MOQ | Landed | Trade sell | Gross margin |
|---|---|---|---|---|---|---|---|
| 1 | Copper-bonded earth rod 5/8" × 4 ft + clamp | Trade | $3.50 | 100 | £3.29 | £10.89 | 69% |
| 2 | BSPP reducing adaptors 1/8–3/4" | Trade | $0.20 | 50 | £0.19 | £2.34 | 92% |
| 3 | Genset filter service kit (fuel/oil/air) by engine | Trade | $40 | 10 | £36.92 | £77.14 | 52% |
| 4 | JIC/ORFS swivel adaptors | Trade | $0.60 | 100 | £0.55 | £5.86 | 90% |
| 5 | Type 2 single-phase SPD, DIN rail | Captive firm | $4.00 | 50 | £3.69 | £17.01 | 78% |
| 6 | NiCd emergency-lighting stick 4.8V 1.5–1.8Ah | Captive firm | $3.50 | 100 | £3.23 | £10.97 | 70% |
| 7 | Electrical warning / circuit-chart label packs | Captive firm | $1.50 | 200 | £1.45 | £7.29 | 80% |
| 8 | MIG wire ER70S-6 15 kg spool | Trade | $13.50 | 100 | £12.50 | £33.70 | 63% (retail bench only) |
| 9 | Flat T&E compression glands IP68 | Trade | $0.40 | 100 | £0.37 | £0.95 | 60% |
| 10 | NiCd 4Ah D-cell sticks | Captive firm | $7.50 | 100 | £6.92 | £18.00 | 61% |
| 11 | NiMH emergency-lighting packs | Captive firm | $2.00 | 100 | £1.85 | £8.91 | 79% |
| 12 | LV resin cable joint kits (SWA) | Trade | $6.00 | 10 | £5.54 | £11.30 | 51% |
| 13 | Type 1+2 / 3-phase SPD kits | Captive firm | $15 | 10 | £13.80 | £28.80 | 51% |
| 14 | Heat-shrink LV joint kits | Trade | $9.00 | 10 | £8.31 | £19.80 | 58% |
| 15 | SDS-plus masonry bits 5.5–12 mm | Marketplace | $0.60 | 100 | £0.55 | £1.68 | 55% after fee |

Near misses worth keeping warm: 12V 7Ah VRLA batteries (67% trade margin), PAT pass labels (71%, but MOQ 1,000 rolls = £3.6k), earth clamps, SWA gland packs, zirconia flap discs (65% on Amazon).

**Caution on the margins.** The 60–92% figures are landed cost against 90% of a distributor's list price. Real trade accounts will want 15–30% under list, and pre-sold prices will find the true level. Plan on 45–55% on the adaptor and earthing lines and 35–45% on the rest. Even at those levels every line clears the 30% gate.

**First 10 to pre-sell** (small MOQ, benchmark on record, low compliance burden): NiCd EL sticks (MOQ 100, £323 landed), Type 2 SPDs (MOQ 50, £185), earth rods (MOQ 100, £328, pallet), 12V 7Ah VRLA (MOQ 100, £516), warning-label packs (MOQ 200, £291), SWA gland packs BW/CW (MOQ 100), resin joint kits (MOQ 10, £55), genset filter kits by engine model (MOQ 10, £369), a 40-SKU hydraulic adaptor consignment rack (£1.5–2.5k), PAT labels only against a year's captive usage. Total first-order exposure if all ten pre-sell: about £6–8k.

**Held back:** MIG wire and abrasives until a real trade price is obtained (only an eBay retail bench exists); MCBs, RCDs and fuses (third-party certification and enclosure fit kill generic imports); anything lithium.

**Channel map:** captive firm for batteries, labels, earthing, SPDs, glands, joint kits and lockout kits per engineer; trade accounts for earth rods, VRLA strings, genset kits, MIG pallets and hydraulic racks; Amazon and eBay only for SPDs, NiCd sticks by voltage, VRLA, PAT label rolls, hole saws, disc boxes and SDS multipacks. Hose assemblies, genset kits and lithium stay off marketplaces.

**Compliance that must be in place before the first sale:** Batteries Regulations producer registration and take-back (1 t/yr BCS threshold, 32 kg/yr distributor take-back); NiCd only under the emergency-lighting exemption; VRLA as UN2800 non-spillable; no lithium until carrier rules are confirmed; UKCA/CE importer-of-record duties on everything; EN 12413 certificates for any bonded abrasive; ASTA/Kitemark expectations rule out generic protective devices.

## 4. Demand-proof gates (money goes out only after these)

| Gate | Lane A | Lane B |
|---|---|---|
| Listing test | 20 listings per line inside the two ranked shops, 30 days, no ads | Pre-sell listings on Amazon Business and eBay with a 10–14 day lead; one-page price list emailed to 30 firms |
| Pass | 2% conversion and 10 orders | 5 orders on a SKU |
| Then | Double listings; mirror to Amazon Custom and Walmart within 30 days | Buy the MOQ; second order only after 5 reorders inside 13 weeks |
| Kill | Under 25% margin for two months | No reorder in 13 weeks, or an account over 60 days late |

## 5. How it adds up

- Lane A: three launch lines at 110 orders/month each = 330 orders × $44.95 ≈ $14.8k/month ≈ £140k/yr at 51% gross margin ≈ £71k gross profit. Target met with three lines; survivors 4–10 are the second quarter's launches and the upsell tiers lift average order value.
- Lane B: at a conservative 45% margin, £200k of revenue needs £90k of gross profit, i.e. three to four SKUs at the £2,500/month rate plus a captive book. The captive book alone (one compliance firm's engineers buying batteries, labels, SPDs and glands) is plausibly £30–60k a year of it; ask the acquisition target for 12 months of wholesaler invoices to size it exactly.
- Together: £350k revenue, £130–160k gross profit, £50–70k net after fees, fulfilment, team and software, as in the system design.

## 6. Gaps the data could not close, and who closes them

| Gap | Why | Closed by |
|---|---|---|
| Etsy-native search volumes and sold counts | Etsy and Google Trends bot-blocked | Your Etsy stats on the existing shops; a $20–30 keyword tool for one month |
| Your actual partner costs and designer rate | Not on file | Dale: the print partner price list and what the Philippines team is paid per design |
| eBay sold velocity and Amazon seller counts for lane B | Blocked | Manual check of 10 SKUs on eBay sold listings, one hour |
| UK trade list prices for welding, abrasives, hose assemblies | Distributor sites blocked or JS-only | One trade-account application each at a welding and a hydraulics distributor to see the real list |
| Real supplier quotes | Alibaba CAPTCHA; Made-in-China used | RFQ emails to three suppliers per SKU before any order; a week |
| Captive-firm SKU spend | Unknown until a firm is in play | The HMD242 process: ask for 12 months of wholesaler invoices |

## 7. The next 30 days

1. Dale sends partner prices and designer rate; I rerun lane A margins on actuals and confirm the three launch lines.
2. Manuel builds 20 listings each for star map, birth-flower and custom map inside the two shops; Amazon Custom account opened; Walmart application submitted.
3. Lane B: RFQs to three suppliers for the first 10 SKUs; Batteries Regulations registration started; a trade price list drafted; Amazon Business and eBay pre-sell listings up.
4. Weekly dashboard live from week one, by lane and line, with the gates above written on it.
