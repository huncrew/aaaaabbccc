# Findings summary for the SOT agent (as of 25 Oct 2026)

*Purpose: everything this analysis found, in one place, with the weights this agent used stated explicitly so the agent with personal context can re-weight. All numbers trace to files in `huncrew/aaaaabbccc`, branch `claude/trusting-goldberg-r42wys` (§10). Probabilities are Monte Carlo outputs for "£750k invested by end-2034" unless stated; they condition on a 3-day contracting week, a £60k floor at completion, £20k burn, and a 10% crypto sleeve unless stated.*

## 1. The goal, and the one reframing proposed

- SOT goal: £750k invested, £30k/yr passive, by 40 (end-2034), through business, at high probability, within health (Crohn's, energy as the binding constraint) and a 3-day week.
- Dale's floor, stated 24 Oct: "£20k a year forever doing something I love is probably enough."
- Proposed reframing: goal as a range, £750k between 2034 and 2038, life conditions fixed, date as the variable. The 2034 version needs a lever (other people's labour, capital at risk, or distribution at scale). The 2036 version needs a £30k loved business plus two contracting blocks a year. Deterministic lifestyle paths (index returns only, no sleeve):

| Lifestyle plan | NW 2034 | 2036 | 2038 | £750k reached |
|---|---|---|---|---|
| £30k loved business + 1 block/yr | £453k | £551k | £661k | 2040 |
| £30k loved business + 2 blocks/yr | £638k | £797k | £974k | 2036 |
| £20k + 1 block/yr | £381k | £455k | £537k | after 2040 |
| £30k, no contracting | £267k | £305k | £348k | not on path |

## 2. Routes ranked (P(£750k by 2034))

| Route | P | Notes and the key assumptions |
|---|---|---|
| Buy a contracted-servicing firm (electrical compliance first choice; HVAC fallback), origination in bench time, 2.3× with 50% vendor note, contracting tapering 3-2-1-0 | 57–64% | Assumes close at ≤2.3× with seller finance (unnegotiated asking prices → 53%), manager stays 85%, severe yr-1 decline 4–6%, growth 8%. Fit multiplier 1.05–1.10; fit range 0.8–1.2 moves P by ±8 points (50–69%). |
| Build ecommerce as a top-1% operator (two ranked Etsy shops, Manuel, PH team, data-led lines), contracting alongside | 61–69% | Rests on owner profit reaching £60k yr 2, £125k yr 3; one bad platform year → 45%. Population-median curve → 5%. 7-year run calibrated to Dale's record: median profit £58k in 2034, P(≥£30k in 2034) 79%, P(≥£100k) 22%, P(NW ≥ £750k) 64%. |
| Buy an ecommerce brand at 2.3× and add Dale's skill (15% growth) | 63% | Fewer listings, 2.2× entry, manager stays only 50%, platform risk. |
| Smaller firm (EV ~£250k), 65% vendor note, 2 blocks/yr throughout (Dale's chosen variant, 30 Sep) | 57% (64% with 25% sleeve) | Cash at completion ~£80k; draw £34k yr 1 rising to ~£118k by yr 5. |
| Business full time, no contracting, seller-funded | 45–48% | ~100 employed days total. |
| AWS consultancy build + 3-day contracting | 33% | AWS SA day rates −16.7% y/y. |
| Contract 3 days + index/crypto only | 29% (64% for £500k) | |
| AI app (incl. logistics-specific) | 15–21% | Worst fit (0.6), no owned distribution. |
| Build services/import firm from zero | 16–27% | Survival curves too slow. |
| Coffee carts ×5, vending ×20, YouTube niche, Udemy course, HMOs | Not modelled as routes; see §7 | None reaches £80k/yr within the constraints without becoming a labour-management or capital business. |

Weights this agent used that the SOT agent may change: fit multipliers (distributor 1.10, services 1.05, HVAC 1.0–1.05, ecommerce 0.7 → 1.0–1.2 after the Etsy record), the 3-day cap, the £60k floor flex, crypto sleeve 10–25% at +25% mean / 0.8 vol, two contracting blocks a year as tolerable.

## 3. What the market evidence says

- 81 priced UK listings (Sep 2026): vendor finance advertised on none; retiring sellers 39–42%; services 2.5×, logistics 2.6×, hire 3.4×, distribution 2.8×.
- SE contracted-servicing scan (54 listings): electrical compliance/critical power best supplied in envelope (5 London/SE firms); HVAC cheapest (2.05–3.3×) with F-gas engineer scarcity; fire has consolidator demand (PE did 70% of 2025 deals); water hygiene no SE supply; lifts no open-market supply.
- Seller finance: typical 20–40% of price over 2–4 years at Bank Rate +2–4; "over 50%" where bank debt is thin; never in the listing, always at offer stage. Competition for sub-£500k firms is thin: no institutional buyers below ~£1m EBITDA; the seller's alternative is often no sale.
- Scale-up evidence (Companies House, 21 firms): "largest independent" is a sale trigger (Cromwell, Hayley, Hydraquip ~£65m, R&G ~£100m); no UK distribution/servicing group reached £25m+ from one small acquisition without outside money; wave winners pre-dated the wave (solar distributors by 4–6 years); normal growers took 15–40 years. HTS Spares (non-genuine JCB parts): £13.9m T/O, £2.0m PBT, founded 2011 by buying an existing trade.
- Consolidation: enter as the buyer of the fragmented servicing/parts layer in the installed-base phase; target a £1–1.5m exit, not £30m. Drones/robotics/flight: no fleet, no ageing-owner base, no spares trade yet (UK drone imports ~£30m, DJI-dominated); hold as a post-2034 cycle.
- Forward demand (electrification, data centres, grid) is a filter on customers, not a business type: more EICRs, critical-power maintenance, installers needing parts. Transformer lead times 15 months–4 years; generator spares imports +14% y/y, 1,070 importers.

## 4. The live purchase target and the practical side

- Hornblower ref HMD242, London NICEIC electrical testing & maintenance: revenue/adj. EBITDA 2020–24 £480k/£181k, £461k/£141k, £412k/£115k, £406k/£129k, £498k/£167k; 90% repeat; subcontract-engineer model; directors' replacement cost already deducted. Offers invited. NDA signed and enquiry submitted 19 Oct; awaiting the information memorandum.
- Deal sheet (negotiated, 2.3× on 5-yr avg £147k, 50% VN): price £337k, cash at completion £121k, PG ~£35k, pre-tax to Dale £82k/yr in yrs 1–4 (£56k after tax), £129k from yr 5. Seller-funded 70% VN: £94k in, £70k pre-tax. Stress (EBITDA at 2022 level for 2 yrs + £40k hired manager): £10k pre-tax in yrs 1–2 — the case the price must protect against.
- Comparators: P6 (London/East, £175k EBITDA, shareholders willing to remain) is the only one stronger. P2 and P3 are owner-on-the-tools firms: after a replacement engineer, £13–14k/yr is left for debt; bolt-ons later, not a first purchase.
- Dale's role if bought: sales, pricing, subcontractor terms, the test calendar; no tools, no certificates; 2–3 days/wk yr 1, 1–2 from yr 2 if an ops person/QS exists. Open questions to the broker are in `Broker enquiry - HMD242 draft.md` (role, QS, scheduler, software, 2021–23 dip, top-10 customers, vendor-note appetite).
- Off-market list: 102 Companies House firms scored; 6 full passes (owner b.1955–70, NA £50–600k, 3–20 staff): McNeilly Electrical (Herts), The Electrical Maintenance Company (Chelmsford, succession under way), Switchgear Technology (Bromley, young directors added 2024), Power Systems Service (Guildford), M.B. Power Services (Essex), Critical Power Supplies (Thame, probably above band).

## 5. The ecommerce/distribution system (if that lane leads)

- Two lanes on one backbone, nothing else: Lane A US personalised made-to-order (Etsy ×2 ranked shops, Amazon Custom, Walmart Marketplace, eBay; Faire for unframed poster sets); Lane B UK trade consumables/spares (Amazon Business, eBay, trade price list; captive customers if the firm is bought). Scored 27 and 28 of 35 on Dale's criteria; private label 14, exclusive agency 18, drop-ship 11.
- Target £350k revenue (A £150k, B £200k) → £51k net at 15%, £70k at 20%. Lane B stock cap £40k; ~£23k average stock at 6 turns.
- Lane A survivors (15 of 64): launch star map, birth-flower family bouquet, custom map/housewarming — template renders on the existing poster SKU, 51% Etsy margin, ~110 orders/month each for $2,500 GP; three lines = the lane target. Pet portraits pass at 41% only because of 90 min design time. Golf seasonal (4.2). Amazon/Walmart take 15% vs Etsy 9.5%.
- Lane B final 15 (of 66): earth rods, hydraulic adaptors (BSPP/JIC), genset filter kits, Type 2 SPDs, NiCd/NiMH emergency-lighting batteries, warning-label packs, T&E glands, resin and heat-shrink joint kits, SDS bits. Landed→trade margins 50–92% against 90% of distributor list; plan on 45–55% after real trade discounts. First 10 pre-sell SKUs total £6–8k exposure. Held back: MIG wire/abrasives (no trade bench), MCB/RCD/fuses (certification), lithium. Compliance before first sale: Batteries Regulations registration/take-back, NiCd under the EL exemption, UKCA/CE importer duties.
- Gates: no stock until 5 orders; second order only after 5 reorders in 13 weeks; kill at <25% margin for 2 months (A) or no reorder in 13 weeks (B). Dale's time: one weekly review, one quarterly line choice.
- Year-1 odds of £5k/month profit: 17% Amazon-led with the Etsy shops idle; 28% with the shops running their own new lines; 44% with Etsy lines + strong Amazon + a direct/B2B line. Experience and Manuel move a generic 1% to 17%; the ranked shops are worth another 10–25 points.
- Etsy: shop country is UK (account/bank), public shop-location field set to US. Dale has run it 5 years this way and chose to leave it; this agent's view was to set location to UK with US shipping origin, or get Etsy's written OK. Amazon Handmade is dead for him. US-to-US made-to-order supplies are outside the scope of UK VAT; VAT registration would reverse-charge Etsy fees (accountant to confirm).

## 6. Fit and health weights (for re-weighting)

- PrinciplesYou: Shaper; Non-Conforming 96, Agile 96, Demanding 96, Independent 94; Empathetic 1, Status-Seeking 1, Detail-Oriented 15, Modest 10. Least like Implementer/Helper.
- This agent read that as: electrical compliance (systematic, calendar-driven, low drama, customers buy on certificate and price) best fit; HVAC people-heavy; distribution suits independence but needs an ops person for inventory detail; ecommerce fit 1.0–1.2 for marketplace selling after the $500k Etsy record (demand-capture strong, demand-creation weak: Shopify stores failed, Etsy worked).
- The Etsy success happened while broke, ill and rushed; this agent raised the build-route ceiling for that but kept the health cap at 3 days/wk and treated "fast" and "calm" as in tension.
- Dale's self-assessment: top 1% as AI SA and as a logistics-adjacent operator; "90%+ if I really go for it". This agent's framing: the model already prices "going for it" (two data-led launches a year for 7 years, team, three channels); persistence cannot buy the hit, and the £100k+ outcome stays ~1 in 5.

## 7. Options evaluated and set aside, with the number that decided it

| Option | Decisive data |
|---|---|
| Coffee carts ×3–5 | Listed vans net £28–30k with the owner on the cart; with a barista, ~£17k per van; 5 vans ≈ £55k with a manager on £125–375k capital. One cart = freedom-plan business. |
| Vending/gaming in barbers ×10–20 | Gaming machines not permitted outside alcohol-licensed premises/FEC permits. Snack vending in barbers ~£15–40/week per machine; 20 machines £15–40k/yr; £80k needs 60–80 machines and a van route (buy a route, not build). |
| YouTube niche (GoT, boxing, history) | Median RPM $2.30; half of views unmonetised; copyright on clips; power-law. Hobby with an option. |
| Udemy AI course | ~$2k average per instructor; 75% under $1k; instructor share falling to 15%. Out. |
| HMOs | Gross 8–12%, net 6–9%; £150k buys one; net £10–15k/yr. Store of wealth after £750k. |
| AI app (logistics-specific) | 15–21%; build as internal tooling only. |
| Private-label Amazon FBA | Median margin 20%, 70% of sellers under $60k; correlated with lane A. |
| Build-from-zero services/import/AWS | 16–33%. |

## 8. Decisions already taken by Dale (as this agent understood them)

- 3 days/week contracting, already decided; business to replace it over time.
- Open to the floor flexing to £60k at completion; crypto sleeve is in and not to be warned about.
- Buy route accepted as main option; smaller firm with more vendor finance and a £40k draw plus contracting top-up is acceptable.
- Ecommerce/distribution as the co-lead; lanes A and B as designed; coffee/vending/YouTube/course/HMO parked.
- Hornblower NDA signed and enquiry sent (19 Oct).
- Shop-location field stays as is (Dale's call).

## 9. Open items

1. Hornblower: information memorandum, owner call, proof of funds, a lender conversation (GGS lenders), accountant and solicitor names.
2. Lane A actuals from Dale: print-partner price list, designer rate, current orders/month, peak-month profit.
3. Lane B: RFQs to three suppliers for the first 10 SKUs; one hour on eBay sold listings; trade-account applications at a welding and a hydraulics distributor; Batteries Regulations decision.
4. Meg: role, hours, skills. Manuel: hours, pay basis.
5. SOT updates proposed: goal as a 2034–2038 range; floor rule; two-blocks-a-year rule; one-block-in-flight list; both plans (ambition and freedom) named.
6. Dashboard republish with the relaxed runs (not done).

## 10. Files

- Reports: `Path to 750k by 40.md` (full write-up), `Decision brief - buy a servicing firm.md`, `Deal sheet - London electrical testing (HMD242).md`, `Broker enquiry - HMD242 draft.md`, `Acquisition profile - Dale Grant.md`, `Ecom-dist system design v1.md`, `Product plan v1 - two lanes.md`.
- Model: `model/mc_model.py`, `params.json` (380+ sourced leaves), runs `run_benchtime.py`, `run_fulltime.py`, `run_sideline.py`, `run_services_scan.py`, `run_fit.py`, `cash_needed.py`, `run_smaller_deal.log`, `run_ecom_track.log`, `run_ecom_strategic.py`, `run_5k_month.py` (+v2 log), `run_ecom_7yr.py`, `deal_sheet_p1.py`.
- Research notes (`research_notes/Path to 750k by 40/`): listings (distributors, services/hire/logistics, digital/agency, SE services scan), deal market & multiples, acquisition finance, post-acquisition base rates, build-from-zero base rates, contracting market, investment returns & tax, health/personality evidence, sector economics, buyer cases, AWS/AI app, import line candidates (+ranked), import logistics playbook, data-centre/grid gaps, becoming-the-supplier evidence, off-market electrical targets, lane A and lane B candidate CSVs and notes.
- Dashboard (original constrained runs only): https://claude.ai/artifact/YHETEia2u1hYdUrHu4wGHW
