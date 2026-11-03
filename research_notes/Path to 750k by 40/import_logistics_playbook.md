# UK sole-founder B2B import playbook: end-to-end logistics and cost structure (as of 28 September 2026)

Scope: a UK sole founder importing one technical/industrial product line (consumables or spare parts; £25–50k first stock run) from Asia or Europe, selling B2B to UK trade customers, with a third-party warehouse (3PL) packing. All figures GBP/USD as quoted by the source, dated, and traceable to a URL. Where a figure comes from a forwarder/3PL/broker "quote page" or marketing rate card rather than an index or government source, this is stated. FX conversions in worked examples are flagged as assumptions (no FX rate was sourced in this research).

Access notes: trade-tariff.service.gov.uk news pages, commonslibrary.parliament.uk, Hapag-Lloyd news, and the Stevens & Bolton briefing returned 403/307 to the fetch tool and were not circumvented; the trade-tariff JSON API (api/v2/commodities) was accessible and was used directly. Freightos route pages show charts without numbers in text form. Maersk PSS notice failed to parse (header overflow). Anglia Market blog returned 503.

---

## 1. Freight: current sea FCL/LCL, road groupage, air, transit and 2026 surcharges

### Takeaway
As of 24 September 2026, Asia–North Europe spot rates are falling from a mid-2026 Middle East-driven spike: Drewry WCI Shanghai–Rotterdam is US$3,485/40ft, Xeneta Far East–North Europe US$3,945/FEU, and Freightos FBX11 shows US$3,376/40ft; forwarder quote pages put a 20ft China–UK at roughly US$1,700–3,400 and LCL at US$45–150/cbm plus handling, with Cape-routed transit of 37–53 days to Felixstowe. European road groupage to the UK is roughly £78–£225 per pallet on instant-quote pages, and air freight from China runs about US$4.50–9.00/kg.

### Cited Findings

**Sea FCL indices (Asia–Europe, weekly)**
- Drewry World Container Index composite: US$4,468/40ft on 24 September 2026 (down 1% w/w); Shanghai–Rotterdam US$3,485/40ft (down 4%); Shanghai–Genoa US$3,835/40ft (down 5%); Suez transits rose from 41 (wk 37) to 48 (wk 38); 7 Asia–Europe blank sailings announced for the following week; Drewry expects further declines as Golden Week approaches. — [Drewry WCI, 24 Sep 2026](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry)
- Shanghai–Rotterdam WCI progression in September 2026: US$4,092 (3 Sep, -5%), US$3,997 (10 Sep, -2%), US$3,626 (17 Sep, -9%), US$3,485 (24 Sep, -4%). — [DCN, WCI 17 Sep 2026](https://www.thedcn.com.au/news/world-container-index-17-september-2026); [DCN, WCI 24 Sep 2026](https://www.thedcn.com.au/news/world-container-index-24-september-2026)
- Xeneta Far East–North Europe spot: US$4,103/FEU on 17 September 2026, +84.9% versus 28 February 2026 (pre-"Hormuz crisis"); Far East–Mediterranean US$4,434/FEU (+33.2%); Xeneta expected "one more freight rate push at the start of October" ahead of Golden Week before softening. — [AJOT / Xeneta weekly update, 18 Sep 2026](https://www.ajot.com/news/xeneta-weekly-ocean-container-shipping-market-update-september-18-2026)
- Xeneta Far East–North Europe spot: US$3,945/FEU on 24 September 2026, down 28.7% (US$1,590/FEU) from 1 July. — [IndexBox summary of Xeneta, Sep 2026](https://www.indexbox.io/blog/xeneta-far-east-container-spot-rates-may-be-nearing-a-turning-point/)
- Freightos FBX11 (China/East Asia–North Europe) page showed US$3,376/40ft (no date visible in extracted text; page is dynamic; fetched 28 Sep 2026). FBX11 covers Shanghai/Ningbo to Rotterdam/Hamburg, not UK ports directly. — [Freightos FBX11](https://www.freightos.com/enterprise/terminal/fbx-11-china-to-northern-europe/)

**Forwarder quote pages, China → Felixstowe/Southampton (indicative, not indices)**
- ExFreight (indicative 2026, "rates fluctuate 20 to 30 percent within a single month"): 20ft US$1,700–2,200; 40ft/40HC US$2,800–4,600; LCL US$45–90/cbm plus origin/destination handling minimums; LCL/FCL break-even about 13–15 cbm; air US$4.50–9.00 per chargeable kg; transit port-to-port FCL 30–40 days, LCL 32–45 days, air 5–8 days; door-to-door FCL 38–50 days, LCL 42–55 days, air 8–12 days. — [ExFreight quote page](https://www.exfreight.com/shipping-from-china-to-uk/)
- SinoShipment (rates dated July 2026): 20GP US$2,700–3,400; 40GP US$4,800–5,900; 40HQ US$5,000–6,200; LCL ~US$55/cbm; air US$5–8/kg (5–10 days), express US$12–15/kg (3–5 days); rail 20GP US$4,500–5,500 (18–25 days); UK THC US$200–400 per container; fuel surcharges US$100–300 per container. — [SinoShipment quote page, Jul 2026](https://sinoshipment.com/blogs/freight-costs-from-china-to-uk/)
- DTFU Logistics (article dated 19 March 2026): 20ft low season US$1,500–2,200, peak US$2,500–3,800+; 40ft/40HQ low US$2,800–4,000, peak US$4,500–6,500+; LCL US$80–150/cbm low, US$180–300/cbm peak; UK-side example charges: THC ~US$350 for a 40HQ, customs clearance ~US$80–150 per shipment, port-to-warehouse haulage US$650 in one example; demurrage after 5–7 days free time. — [DTFU quote page, Mar 2026](https://www.dtfulogistics.com/news/sea-shipping-cost-from-china-to-uk/)
- Freightos route page (updated September 2026): sea door-to-door 30–40 days; air around 8–10 days; express at least three days; price spikes at Chinese New Year (late Jan/early Feb) and Golden Week (from 1 October); sea peak July–October. — [Freightos China–UK route page, Sep 2026](https://www.freightos.com/shipping-routes/shipping-from-china-to-the-uk/)
- Freightos Air Index (FAX) is published daily as an all-in general-cargo US$/kg spot rate; a 2026 Far East–Europe reading cited was about US$4.88/kg (undated within 2026 in the snippet). — [Freightos FAX Greater China–Europe](https://www.freightos.com/enterprise/terminal/fax-greater-china-asia-to-europe/); [Suaid Global summary citing Freightos](https://suaidglobal.com/insights/air-freight-cost-per-kg/)

**Transit times**
- Shanghai–Felixstowe via Cape of Good Hope: 37–53 days as of July 2026 (Cubic); another guide gives sea transit 40–55 days and door-to-door 50–65 days because Maersk, MSC and COSCO diverted Asia–Europe services around the Cape, adding roughly 3,500 nautical miles. — [Cubic China–Felixstowe](https://www.gocubic.io/shipping-routes/china/felixstowe); [Efanda Logistics guide](https://efandatrans.com/shipping-from-shanghai-to-felixstowe/)
- Drewry's 24 September 2026 note records Suez transits recovering (41→48 per week), which shortens transit on services that have returned to Suez. — [Drewry WCI, 24 Sep 2026](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry)

**2026 surcharges (Asia–Europe)**
- Peak Season Surcharges filed for June/July 2026: CMA CGM US$500/20ft–US$1,000/40ft (1–14 June) rising to US$1,000/20ft–US$2,000/40ft to North Europe from 1 July; Hapag-Lloyd US$500/20ft–US$1,000/40ft from 8 June; HMM US$600/20ft–US$1,200/40ft from 15 June; ONE US$500/20ft–US$1,000/40ft from 15 June; Maersk US$300/600 (10 Jun–6 Jul), US$750/1,500 (7 Jul–2 Aug), US$250/500 (from 3 Aug) and US$0 from 1 September (all PSS removed); MSC "targeting US$6,000/40ft as a new all-in rate" through GRI from mid-June. — [Shypple PSS tracker 2026](https://help.shypple.com/en/peak-season-surcharges-asia-europe-2026)
- Hapag-Lloyd PSS Far East–North Europe/Med: US$500/20ft and US$1,000/40ft, effective 8 June 2026 until further notice, all container types. — [Container News](https://container-news.com/hapag-lloyd-introduces-pss-from-far-east-to-north-europe-and-mediterranean/)
- Maersk removed its LCL Peak Season Surcharge from Far East Asia to North Europe and the Mediterranean from 17 September 2026. — [Container News](https://container-news.com/maersk-removes-lcl-peak-season-surcharge-from-asia-to-europe/)
- A GRI effective early October 2026 was announced by one major line at US$1,200/20ft and US$2,000/40ft Far East–North Europe; Mid-Autumn Festival (25–27 Sep) runs into Golden Week (1–7 Oct 2026); scheduled Asia–North Europe capacity over the four-week Golden Week period is about 1.50 million TEU, +27% year on year. — [YQN ocean freight increase 2026](https://www.yqn.com/intro/blog/post/ocean_freight_increase_2026); [Global Maritime Hub](https://globalmaritimehub.com/golden-week-capacity-surge-raises-october-schedule-risks/)
- Carriers stack GRI, PSS and equipment-imbalance surcharges per TEU/FEU in Q3–Q4 on Asia–Europe lanes. — [GoFreight surcharge guide 2026](https://gofreight.com/blog/carrier-peak-season-surcharges)

**Road groupage, Europe → UK (per pallet, instant-quote pages)**
- Pallet2Ship import Poland → UK "price examples": mini-quarter (150 kg) £136.25; quarter (300 kg) £160.65; half (600 kg) £181.19; full-lite (750 kg) £205.31; full (1,200 kg) £223.15. Export UK → Poland full pallet from £192.89. — [Pallet2Ship Poland](https://www.pallet2ship.co.uk/send-pallets/Poland/)
- Pallet2Ship Germany: 100 kg pallet (120×80×50 cm) road "starting at £77.66", air "starting at £381.30"; economy road 3–5 working days, express road 2–4, air 1–3; customs clearance adds 1–2 working days; commercial invoice, HS codes and EORI for both parties required. — [Pallet2Ship Germany](https://www.pallet2ship.co.uk/send-pallets/Germany/)
- Pallet2Ship Turkey: 100 kg pallet by air £460.66 (sample price); road freight about 6 working days; commercial invoice required for company shipments. No road price example shown. — [Pallet2Ship Turkey](https://www.pallet2ship.co.uk/send-pallets/Turkey/)
- Turkey–UK groupage: standard departures every Wednesday and Friday from Istanbul and Izmir depots; transit quoted as 6–10 days by one forwarder. — [Plexus Freight Turkey](https://www.plexusfreight.com/turkey/)
- Cross-border EU groupage benchmark: roughly EUR 150–300 per standard EUR pallet between neighbouring countries; booking ahead rather than spot saves 10–20%. — [Logifie](https://www.logifie.com/blog/pallet-shipping-cost-europe); [Trans-road 2026](https://www.trans-road.com/en/blog/freight-cost-per-pallet-europe)

### Inferences
- For a £25–50k first run of dense industrial consumables (typically 8–15 pallets, 10–25 cbm), a 20ft FCL is usually the right unit: the ExFreight LCL break-even of 13–15 cbm and DTFU's LCL US$80–150/cbm imply LCL costs roughly match a 20ft above ~15 cbm once origin/destination handling minimums are added.
- September 2026 is a falling-rate window (Drewry, Xeneta, Freightos all down since July) but the October GRI/Golden Week push means booking for sailing in late October or November, rather than the first week of October, is the cheaper play.
- All-in landed sea freight for one 20ft China→UK warehouse in Sept 2026 is plausibly US$2,000–3,500 ocean plus roughly £600–1,000 UK-side (THC, port surcharge, haulage, clearance), i.e. about 8–15% of a £30k FOB order; a 40ft carries roughly 2.2x the volume for about 1.4–1.7x the ocean cost.
- European road groupage to the UK at £80–225 per pallet means a 10-pallet Poland/Germany order lands for roughly £1,000–2,300 in 3–7 days — comparable to a 20ft from China but with 6–7 weeks less transit and no Cape-routing risk.

### Gaps
- No public, dated FCL rate specifically to Felixstowe/Southampton from an index: Drewry/Xeneta/FBX quote Rotterdam/Hamburg/Genoa; UK rates are typically quoted by forwarders as a small premium/discount to North Europe but no source was found quantifying it.
- No specific 20ft index value (indices are per 40ft); the 20ft figures are forwarder quote pages.
- No dated per-kg FAX value for September 2026 was retrievable (terminal is subscription-gated); the ~US$4.88/kg figure is a 2026 secondary citation.
- No published Turkey→UK road groupage price per pallet was found; only transit times.
- Air freight per kg to the UK specifically (rather than Europe) was only available from forwarder quote pages.

---

## 2. Customs: EORI, UK Global Tariff examples, rules of origin (India/EU/Turkey/CPTPP), import VAT and PVA, broker fees, CDS, Incoterms

### Takeaway
A first-time importer needs a GB EORI (free, usually immediate), a commodity code (many industrial parts are 0–8% under the UK Global Tariff and 0% with EU/Turkey/Japan/Vietnam/India preference if origin rules are met), and should use Postponed VAT Accounting (no approval needed) so import VAT is never paid in cash; broker clearance runs roughly £50–150 per entry plus £2.75–3.50 CDS charge and £35–70 port surcharge. FOB is the sensible default Incoterm for a first-timer sourcing from China; the UK–India CETA has been in force since 15 July 2026.

### Cited Findings

**EORI**
- An EORI is needed to move goods between Great Britain and any other country including the EU; you get your GB EORI "immediately unless HMRC needs to make any checks", in which case "up to 5 working days"; applicants need UTR, business start date, SIC code, VAT number (if registered), NI number (sole traders) and a Government Gateway login; no fee is stated. — [GOV.UK: EORI](https://www.gov.uk/eori); [GOV.UK: apply for EORI](https://www.gov.uk/eori/apply-for-eori)

**UK Global Tariff duty examples (live query of the UK Integrated Online Tariff API, 28 Sep 2026)**
- 8482 10 90 00 (ball bearings, other): third-country duty 8.00%; preference 0.00% for EU, India, Japan, Turkey, Vietnam; 1.60% under the CPTPP "all members" staging. — [Tariff API 8482109000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8482109000)
- 6216 00 00 00 (gloves, mittens and mitts, textile): 6.00% third country; 0.00% EU/India/Japan/Turkey/Vietnam/CPTPP. — [Tariff API 6216000000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/6216000000)
- 3926 20 00 00 (plastic apparel/gloves): 6.00% third country; 0.00% preferences as above. — [Tariff API 3926200000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/3926200000)
- 8421 23 00 90 (oil/fuel filters for engines, other): 0.00% third country. — [Tariff API 8421230090](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8421230090)
- 8207 50 10 00 (drilling tools with diamond working part): 0.00% third country. — [Tariff API 8207501000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8207501000)
- 8536 50 19 00 (switches, other): 0.00% third country. — [Tariff API 8536501900](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8536501900)
- 8544 42 90 90 (insulated cables fitted with connectors, other): 2.00% third country; 0.00% EU/India/Japan/Turkey/Vietnam/CPTPP. — [Tariff API 8544429090](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8544429090)

**Rules of origin and preference claims**
- UK–India CETA entered into force on 15 July 2026. — [Menzies LLP](https://www.menzies.co.uk/uk-india-free-trade-agreement-comes-into-force-on-15-july-2026/); [business.gov.uk campaign page](https://www.business.gov.uk/campaign/alive-with-opportunity/the-uk-india-trade-deal/); the UK Integrated Online Tariff news story confirming the date exists at [trade-tariff.service.gov.uk](https://www.trade-tariff.service.gov.uk/news/stories/india-free-trade-agreement-enters-into-force-on-15-july-2026--13-july-2026) (page returned 403 to the fetch tool; title confirms date).
- UK importers of Indian goods may claim preference on the basis of (1) a self-certified origin declaration from the Indian exporter, (2) a certificate of origin issued by an Indian authority, or (3) importer's knowledge with "sufficient evidence – including documentation"; importers relying on importer's knowledge "are responsible for substantiating their preference claim"; "Incorrect claims may result in delays, penalties, or loss of preferential treatment." — [business.gov.uk: tariffs and customs India](https://www.business.gov.uk/export-from-uk/markets/india/trade-agreement/tariffs-and-customs-for-imports-from-and-exports-to-india/)
- UK–India origin declarations are valid for 12 months from completion; one declaration may cover multiple goods in a single shipment; templates published 8 July 2026 (export-side guidance). — [GOV.UK: UK-India CETA origin declaration](https://www.gov.uk/government/publications/uk-india-ceta-origin-declaration)
- UK–EU TCA: preference can be claimed with either a statement on origin made out by the exporter or importer's knowledge; EU exporters need a REX number for consignments over EUR 6,000; the importer bears responsibility for the accuracy of the claim; claims can be made retrospectively within 3 years of import. — [GOV.UK: proving origin UK–EU](https://www.gov.uk/guidance/proving-originating-status-and-claiming-a-reduced-rate-of-customs-duty-for-trade-between-the-uk-and-eu); [Customs Support: REX](https://www.customssupport.com/rex-statements-eu-preferential-origin/)
- UK–Turkey FTA: in force (effective 31 December 2020); industrial goods 0% preferential tariff; rules of origin follow a PEM-style protocol aligned since 14 April 2021 with the TCA product-specific rules; EU materials/processing may be cumulated; proof is a declaration on origin (electronic acceptable, must carry the exporter's reference, valid 24 months for UK imports), entered on CDS with statement codes U110/U111; guidance last updated 21 November 2022. — [GOV.UK: summary of UK–Turkey agreement](https://www.gov.uk/guidance/summary-of-the-uk-turkey-trade-agreement); [GOV.UK: rules of origin protocol update April 2021](https://www.gov.uk/government/publications/continuing-the-uks-trade-relationship-with-turkey-parliamentary-report/ukturkey-rules-of-origin-protocol-update-april-2021)
- A UK–Türkiye Exchange of Letters signed 7 May 2025 (CP 1409, presented September 2025, marked "not in force" at presentation) replaces Chapter 4 (Technical Barriers to Trade) and inserts Annexes 4-A (chemicals) and 4-B; it does not amend rules of origin. — [GOV.UK: CS Turkey 2.2025 (PDF)](https://assets.publishing.service.gov.uk/media/68c0522beeb238b20672a8df/CS_Turkey_2.2025_Exchange_Letters_Amending_Free_Trade_Agreement_UK_Turkey.pdf)
- CPTPP entered into force for the UK with Japan on 15 December 2024; CDS claims use preference code 9081 with document codes 9U01 (exporter certification), 9U02 (producer) or 9U03 (importer); the Vietnam and Japan bilateral FTAs continue alongside CPTPP (the tariff API shows 0% Japan and Vietnam bilateral preferences alongside a 1.6% CPTPP staged rate on bearings). — [GOV.UK CPTPP collection](https://www.gov.uk/government/collections/the-uk-and-the-comprehensive-and-progressive-agreement-for-trans-pacific-partnershipcptpp); [UK Tariff stop press 5 Dec 2024](https://www.trade-tariff.service.gov.uk/news/stories/tariff-stop-press-notice---05-december-2024); [business.gov.uk CPTPP Vietnam](https://www.business.gov.uk/export-from-uk/markets/vietnam/trade-agreement/cptpp-rules-of-origin-in-vietnam); [Tariff API 8482109000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8482109000)

**Import VAT, Postponed VAT Accounting, deferment**
- PVA: VAT-registered businesses importing into GB or NI can "declare and recover import VAT on the same VAT Return, rather than paying it upfront when the goods are imported and recovering it later"; "You do not need any approval"; select it by entering the VAT number at header level in CDS Data Element 3/40 (cannot be changed after submission); monthly postponed import VAT statements are provided online; goods must be for business use with the right to dispose of them. — [GOV.UK: account for import VAT on your VAT Return](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return)
- Duty deferment account: defers customs duty, import VAT and excise for payment monthly by Direct Debit (up to 45 days); guarantee waiver approvals exist for up to £10,000 per month, or a specified amount above £10,000 if net assets (excluding goodwill) equal or exceed the maximum to be deferred; eligibility requires no serious customs/tax breaches in 3 years, no serious criminal convictions, and positive net assets; HMRC charges no application fee. — [GOV.UK: how to use your duty deferment account](https://www.gov.uk/guidance/how-to-use-your-duty-deferment-account); [GOV.UK: guarantee waivers](https://www.gov.uk/guidance/guarantees-and-guarantee-waivers/waivers); [Goodwille DDA explainer](https://goodwille.com/what-is-a-duty-deferment-account/)

**Customs broker / clearance fees and CDS**
- UK broker fees: £30–150 per import declaration for straightforward commercial shipments; most brokers £75–150 for basic single-commodity clearance; per-line charging can turn a "£50 clearance" into £250 for a 5-line entry; CDS charge around £2.75 per entry; statutory port/CDS charges £3.50–70 per container; demurrage £50–200/day if collection is delayed. — [GXpress broker fees 2026](https://www.gxpresss.co.uk/customs-broker-fees-uk.html); [GXpress clearance cost 2026](https://www.gxpresss.co.uk/uk-customs-clearance-cost.html)
- Market benchmark (compiled from port tariffs, broker rate cards; "no official UK-government or BIFA-published single benchmark"): standard import declaration £50–150 per entry; additional commodity line £5–15; CDS System Development Charge £2.75 per entry or £3.50 per container (effective 1 January 2026); origin-charge port surcharge £35–70 per container at Southampton, London Gateway, Felixstowe, Grangemouth; Felixstowe full-container import charge £26.16 (official tariff, effective 1 April 2026). — [GXpress UK Customs Clearance Cost Report 2026](https://www.gxpresss.co.uk/uk-customs-clearance-cost-report-2026.html)

**Incoterms for a first-timer**
- FOB: seller handles packing, inland transport to port, export clearance and loading; buyer takes over once goods are on the ship and chooses their own forwarder, giving "greater flexibility with regards to cost, terms, and shipping planning"; "For most importers, FOB is a better starting point because it keeps the export-side logistics with the seller." — [Freightos Incoterms guide 2026](https://www.freightos.com/freight-resources/incoterms-plain-english-freight-shipping-guide/); [Cosmo Sourcing](https://www.cosmosourcing.com/blog/incoterms-defined-fob-exw)
- EXW makes the buyer responsible for export procedures in a foreign country, "which can be complicated"; DDP is "the easiest and most stress-free" but "comes at a higher cost, and buyers have less visibility into shipping and customs expenses". — [Sino-Shipping](https://www.sino-shipping.com/cif-vs-fob-ddp-exw-which-incoterm-is-best/); [OVRSEA Incoterms 2020](https://www.ovrsea.com/insights/en/guides/incoterms-2020-who-pays-what)

### Inferences
- For a £30k FOB order of 6%-duty goods, duty is roughly £1,900 (6% of CIF ~£32k) and import VAT ~£6,800; with PVA the VAT is a VAT-return entry only, so the real cash items at clearance are duty + broker (£75–150) + port/CDS (~£40–75) + haulage.
- A GB importer who is not yet VAT-registered cannot use PVA and would pay ~£6.8k VAT at the border on a £30k order and be unable to reclaim it; VAT registration before the first import is therefore a cash-flow decision, not just a compliance one.
- Duty preference from the EU/Turkey/India/Japan/Vietnam requires the supplier to issue a statement/declaration on origin (or REX/exporter reference in the EU); a first-timer should ask for this at quotation stage and put it in the purchase order, because retrospective claims (3 years under the TCA) are possible but require the proof to exist.
- FOB (China) or FCA (EU/Turkey, where the seller loads the groupage truck) is the right default: it keeps export clearance with the seller while letting the buyer control the forwarder, insurance and UK clearance. DDP is acceptable for the very first sample-sized shipment but hides costs and gives no control over the UK declaration (including whether PVA is used).

### Gaps
- No official HMRC/BIFA benchmark for broker fees exists (stated by the benchmark source itself); the £50–150 range is a compilation of rate cards.
- The UK-side share of tariff lines liberalised for Indian imports under CETA and staging schedules were not retrievable (Commons Library and tariff news pages returned 403); the live tariff API shows 0% India preference on all six sample codes queried.
- Duty rates for gaskets (4016 93), bolts (7318 15), valves (8481 80), pumps (8413) were not retrieved because the guessed 10-digit codes returned "not found"; use the tariff API with the correct declarable code.
- The status of the May 2025 UK–Türkiye TBT amendment (whether it has since entered into force) was not confirmed; the PDF is marked "not in force" as of September 2025.

---

## 3. Product compliance: UKCA/CE in 2026, UK REACH, PPE, Machinery, LVD/EMC, fire safety/construction products, who is the importer, product liability

### Takeaway
CE marking is recognised indefinitely in Great Britain for the 21 DBT-managed product regulations (including machinery, PPE, LVD, EMC, RoHS) under the Product Safety and Metrology (Amendment) Regulations 2024, so a UK importer generally does not need UKCA on CE-compliant goods — but the importer must put its name and address on the product, verify the manufacturer's conformity assessment, hold the technical documentation for 10 years, and is strictly liable as a "producer" under the Consumer Protection Act 1987 for goods imported into the UK. UK REACH transitional registration deadlines have been pushed to 2029–2031, and basic product liability cover for a low-risk small business is advertised from about £50–150 a year (quote pages; more for electrical/PPE).

### Cited Findings

**UKCA / CE status**
- "the UK continues to recognise the CE marking, alongside or in place of the UKCA marking, for the Great Britain market" under The Product Safety and Metrology (Amendment) Regulations 2024; guidance last updated 21 August 2026 (technical correction to the Declaration of Conformity template). — [GOV.UK: using the UKCA marking](https://www.gov.uk/guidance/using-the-ukca-marking)
- The 2024 Regulations made recognition indefinite for 21 product regulations; CE recognition covers the DBT regimes including electromagnetic compatibility, radio equipment, low voltage, machinery, ecodesign, RoHS and civil explosives; medical devices (MHRA) are separate, with a consultation on indefinite CE recognition launched in early 2026; CE (not UKCA alone) is required in Northern Ireland. — [Conformery, 2026](https://www.conformery.com/blog/is-ukca-marking-still-required-2026); [Complir UKCA guide](https://www.complir.io/resources/guides/ukca-marking-guide); [Inside EU Life Sciences, Feb 2026](https://www.insideeulifesciences.com/2026/02/17/uk-mhra-announces-consultation-on-the-indefinite-recognition-of-ce-marked-medical-devices/)
- Construction products: the 30 June 2025 CE cut-off "will no longer apply", CE remains valid indefinitely in GB, but the name and address of the responsible economic operator in GB must be shown and full technical documentation kept; the UK is consulting on a distinct building-safety product framework. — [Designing Buildings wiki](https://www.designingbuildings.co.uk/wiki/Construction%20Products%20Regulation%20amendments%20GB%20in%20context); [Landmark Global, 23 Feb 2026](https://landmarkglobal.com/eu/en/news-insights/ukca-vs-ce-marking-in-2026/)
- The Product Regulation and Metrology Act 2025 (Royal Assent, in effect 21 July 2025) is an enabling Act allowing regulations to place duties on manufacturers, importers, distributors, installers and online marketplaces; substantive measures come via secondary legislation progressively. — [legislation.gov.uk 2025 c.20](https://www.legislation.gov.uk/ukpga/2025/20); [Jones Day, Jul 2025](https://www.jonesday.com/en/insights/2025/07/product-regulation-and-metrology-bill-receives-royal-assent)

**Who is the importer and what must they do**
- An importer is "any individual or business established in the UK who supplies a product from a country outside the UK for distribution, consumption or use in the course of a commercial activity"; importers must put their "name, trade name or trademark, and postal address" on products, verify the manufacturer "carried out the correct conformity processes, drawn up the relevant technical documentation, affixed the correct marking, and fulfilled their identification obligations", retain technical documentation (approximately 10 years), ensure storage/transport does not jeopardise compliance, monitor compliance, cooperate with market surveillance and keep a line of contact with the manufacturer; an importer that places products under its own name/trademark, or modifies them, assumes manufacturer responsibilities. Guidance last updated 21 August 2026. — [GOV.UK: placing UKCA or CE marked products on the GB market](https://www.gov.uk/guidance/placing-ukca-or-ce-marked-products-on-the-market-in-great-britain)
- Supply of Machinery (Safety) Regulations 2008 (GB): importers are "responsible persons"; CE accepted indefinitely where assessed by an EU notified body; UK or EU Declaration of Conformity must accompany machinery; the technical file must be "compiled and made available on request"; until 31 December 2027 importer identification may be provided on accompanying documentation; guidance updated 24 March 2025. — [GOV.UK: Supply of Machinery (Safety) Regulations 2008 GB](https://www.gov.uk/government/publications/supply-of-machinery-safety-regulations-2008/supply-of-machinery-safety-regulations-2008-great-britain)
- PPE: Regulation 2016/425 as retained plus the PPE (Enforcement) Regulations 2018 apply in GB; manufacturers must keep the declaration of conformity and technical documentation for 10 years after placing PPE on the GB market. — [OPSS guide to PPE regulations (PDF)](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1041523/Guide-to-ppe-regulations-2018-version-6.pdf)
- Consumer Protection Act 1987 s.2(2)(c): liability as producer extends to "any person who has imported the product into the United Kingdom in order, in the course of any business of his, to supply it to another"; s.2(2)(b) to any person who puts their name or trade mark on the product. — [legislation.gov.uk CPA 1987 s.2](https://www.legislation.gov.uk/ukpga/1987/43/section/2)

**UK REACH**
- The REACH (Amendment) (No. 2) Regulations 2026 (July 2026) extended UK REACH transitional registration deadlines from 27 Oct 2026/2028/2030 to 27 October 2029 (≥1,000 t/yr, CMRs ≥1 t, very toxic to aquatic ≥100 t, and Candidate List SVHCs listed on or before 27 Oct 2027), 27 October 2030 (≥100 t/yr; SVHCs listed 28 Oct 2027–27 Oct 2028) and 27 October 2031 (all other substances ≥1 t/yr). — [REACH24H](https://en.reach24h.com/news/industry-news/chemical/uk-reach-transitional-registration-deadlines-extension); [Defra consultation](https://consult.defra.gov.uk/reach-policy/extending-the-uk-reach-submission-deadlines); [Womble Bond Dickinson](https://www.womblebonddickinson.com/uk/insights/articles-and-briefings/uk-reach-extending-transitional-registration-deadlines)
- GB-based downstream users/distributors who previously relied on EU REACH registrations can notify HSE (DUIN) to keep importing. — [HSE DUIN](https://www.hse.gov.uk/REACH/duin.htm)

**Product liability insurance cost**
- Simply Business: product liability "from £5.40* per month"; public liability limits up to £2m and product liability up to £10m available. — [Simply Business](https://www.simplybusiness.co.uk/business-insurance/product-liability-insurance/)
- Guide figures (search snippets; blog returned 503 on fetch): £50–150 per year for basic product liability for low-risk small businesses in 2026, rising 25%+ for electronics or toys; low-risk businesses with turnover under £500k might pay £100–500 per year. — [Anglia Market guide 2026](https://blog.angliamarket.com/post/product-liability-insurance-for-small-business-uk-a-complete-guide-2026); [Suited Insure 2026](https://www.suited.insure/post/how-much-does-liability-insurance-cost-for-a-small-business)
- Public/product liability combined from about £6 per month; product liability is usually sold as part of public liability. — [Trade Direct Insurance](https://www.tradedirectinsurance.co.uk/insurance/public-liability/faq/how-much-does-public-liability-insurance-cost/)

### Inferences
- For a UK sole founder buying from a Chinese factory, the founder is the legal importer (and, if own-branding, the "manufacturer") under both the product safety regime and CPA 1987 strict liability. The practical minimum is: importer name/address label on product or packaging, a copy of the EU/UK Declaration of Conformity and test reports in the technical file, and a written agreement that the factory supplies the technical file on request.
- Buying from an EU/Turkish manufacturer that already CE-marks does not remove the GB importer's duties, but it means the conformity assessment and technical file already exist in a form GB recognises, which is the main compliance advantage of European sourcing.
- Product liability premium is a rounding error (roughly £100–500/yr) compared with freight and duty; the material risk is the uncapped strict liability, so a £5m limit and an indemnity clause in the supplier contract are more important than the premium.

### Gaps
- No single GOV.UK page listing all 21 regulations with indefinite CE recognition was retrieved; the secondary sources name machinery, PPE, LVD, EMC, radio, toys, RoHS, ecodesign, ATEX and civil explosives.
- No source was found giving a dated 2026 premium for product liability specific to an importer of industrial consumables; the figures above are consumer-oriented quote pages.
- Fire safety products beyond the construction-products regime (e.g. extinguishers, fire doors, flame-retardant PPE) were not separately researched.

---

## 4. Supplier side: finding and verifying manufacturers, MOQ/samples, payment terms, inspection, distribution agreements, agent vs distributor

### Takeaway
Asia-first sourcing runs through Alibaba (Trade Assurance escrow, 30/70 T/T), Global Sources (star ratings, audited Gold suppliers) and Made-in-China; Europe-first through Europages and Kompass; the autumn Canton Fair runs 15 Oct–4 Nov 2026 and Hannover Messe 5–8 April 2027. Third-party pre-shipment inspection costs about US$290–700 per man-day (QIMA from US$309 all-inclusive; SGS US$300–600). A UK distributor is not protected by the Commercial Agents Regulations 1993 (compensation/indemnity), whereas an agent is, so a founder who wants an exclusive UK arrangement should structure it as a distribution agreement with territory, minimum purchases and a 2–3 year initial term.

### Cited Findings

**Finding and verifying manufacturers**
- Global Sources provides supplier audit/inspection details and certifications; suppliers carry a one-to-six star rating based on verified information; Gold Supplier status requires an annual onsite audit. — [Global Sources: how to find verified suppliers](https://www.globalsources.com/knowledge/how-to-find-verified-suppliers-from-china/); [SourceReady directories](https://www.sourceready.com/blog/best-supplier-directories-for-smbs)
- Europages is one of the broadest European B2B marketplaces (search, contact, RFQ); Kompass is a global company database with strong European coverage and a structured classification; Made-in-China and Global Sources are "Asia-first"; Wonnda/Kompass/Europages are "Europe-first". — [SourceReady: European manufacturers](https://www.sourceready.com/blog/sourcing-platforms-european-manufacturers); [Wonnda Thomasnet alternatives 2026](https://wonnda.com/magazine/thomasnet-alternatives/)
- Trade shows: 140th Canton Fair Phase 1 (advanced manufacturing: electronics, machinery, hardware, vehicles, lighting, chemicals) 15–19 October 2026, Phase 2 23–27 October, Phase 3 31 October–4 November 2026, Guangzhou. — [Canton Fair official](https://www.cantonfair.org.cn/en-US); [Sino Business Partner guide](https://sinobusinesspartner.com/insights/canton-fair-2026-guide)
- Hannover Messe 2027: 5–8 April 2027. — [Visit Hannover](https://www.visit-hannover.com/en/Messen-Kongresse/Messestadt-Hannover/Messekalender-Hannover/HANNOVER-MESSE/HANNOVER-MESSE-2027)
- PPMA Show 2026: 22–24 September 2026, NEC Birmingham. — [PPMA Show](https://www.ppmashow.co.uk/)
- Hillhead 2026 (quarrying, construction, recycling; biennial): 23–25 June 2026, Hillhead Quarry, Buxton. — [Hillhead](https://www.hillhead.com/)
- Southern Manufacturing & Electronics 2027: 2–4 February 2027, Farnborough International. — [Southern Manufacturing](https://www.southern-manufacturing-electronics.com/en/)

**MOQ and samples**
- Typical Chinese MOQs (updated June 2026): simple stock items 50–500 units; custom packaging/branding 500–3,000; custom-moulded/tooled 1,000–10,000+; electronics with custom PCB 500–5,000. — [Plutonia Global MOQ guide](https://www.plutoniaglobal.com/guides/minimum-order-quantities-china)
- MOQ reflects factory economics (setup, tooling, material procurement account for 60%+ of MOQ rationale); the commercial package to negotiate includes MOQ, payment terms, sample cost, tooling amortisation, packaging, lead time, AQL standards and defect remedies; contact at least 5 factories; factories accept lower MOQs in slow periods. — [Supplier Ally playbook](https://supplierally.com/uncategorized/negotiate-moq-pricing-china-factories-guide/); [Aitakon 2026](https://www.aitakon.com/how-to-negotiate-with-chinese-manufacturer)

**Payment terms**
- Common arrangement: 30% deposit, 70% on shipment; the "defensible" T/T structure is 30% deposit to start production and 70% released after buyer or third-party inspector verifies goods, against the Bill of Lading. — [Alibaba seller blog: T/T + Trade Assurance](https://seller.alibaba.com/blogs/2026/southeast-asia/agricultural-waste/tt-trade-assurance-payment-guide-alibaba-b2b); [Shanghai Garment](https://shanghaigarment.com/what-are-the-best-payment-terms-for-new-clothing-supplier-relationships/)
- Trade Assurance: Alibaba holds buyer funds in escrow and releases to the supplier after the buyer confirms receipt or the inspection period expires; suppliers see fees of about 1–2% of order value; guidance is to keep using Trade Assurance for a new supplier until at least three successful orders; for orders US$500–10,000 platform protection is "free, fast, and covers quality and delivery disputes well". — [Alibaba help centre](https://helpcenter.alibaba.com/s/buyer/knowledge?questionId=92572963d7b2496680fabbb2038ac60asgvpc278077001&categoryId=9207651&categoryId=9207651&questionId2=20153048&pageId=128&category=9207651&knowledge=20153048&language=en); [China-Electronics guide](https://china-electronics.com/sourcing/alibaba-trade-assurance/); [Alibaba seller blog 2026](https://seller.alibaba.com/businessblogs/how-sellers-protect-margins-with-alibaba-trade-assurance-in-2026-px002dh4m)
- Letters of credit: issuing bank fee typically 0.75–1.5% of LC value; advising fee flat US$50–300 or ~0.05%; confirmation 0.25–2%; "on a $4,000 repeat order ... you'll pay $500–$1,200 in bank fees", so fixed costs make LCs expensive for small transactions. — [Trade Financer](https://tradefinancer.com/what-are-the-costs-associated-with-letters-of-credit/); [Importivity](https://importivity.com/blog/letters-of-credit-trade-finance/)

**Third-party inspection**
- QIMA: inspectors on site within 48 hours, same-day reports, "all-inclusive pricing", 100+ countries. — [QIMA](https://www.qima.com/your-eyes-in-the-factory)
- QIMA pricing from US$309/man-day for Zone A (China), all-inclusive (travel and reporting bundled); Q1–Q2 2026 range US$290 (basic apparel) to US$700 (specialised chemical/heavy industrial); US$300–380 band covers 70%+ of invoice volume. — [Xilink QIMA pricing 2026 (third-party summary)](https://xilinkglobaltrade.com/qima-inspection-pricing-2026/); [TradeAider comparison](https://www.tradeaiders.com/qima-alternatives-for-small-importers-7-third-party-inspection-options-compared.html)
- SGS typically US$300–600 per man-day in China (not published; negotiated); Bureau Veritas US$380–450 per man-day in South China; independent specialists US$250–350; market floor US$150–350. — [ChinaWithMe PSI guide 2026](https://chinawithme.com/guides/pre-shipment-inspection-china); [Change Sourcing top 10 2026](https://change-sourcing.com/third-party-inspection-companies-in-china-2/)

**Exclusive UK distribution agreements: typical terms**
- An exclusive distribution agreement grants a single distributor the right to market and resell specified goods in a defined territory and the supplier agrees not to appoint others there. — [LexisNexis glossary](https://www.lexisnexis.com/en-gb/legal/glossary/exclusive-distribution-agreement)
- Typical clauses: territory and product scope (define by country/region, not "UK and Europe"), exclusivity carve-outs (key accounts, government tenders, existing customers), minimum purchase targets (exclusivity continues only if quarterly minimums are hit), marketing obligations, reporting, non-compete, IP/licensing, online sales, termination for non-performance; initial term often 2–3 years; UK competition law (vertical agreements) constrains territorial carve-ups and price fixing. — [Sprintlaw UK: exclusive distribution](https://sprintlaw.co.uk/articles/exclusive-distribution-agreement-key-clauses-and-legal-tips/); [Sprintlaw UK: distribution key terms](https://sprintlaw.co.uk/articles/distribution-agreement-key-terms-risks-and-best-practices/); [Templates UK guide 2026](https://templatesuk.com/distribution-agreement-guide-uk/)

**Agent vs distributor (Commercial Agents (Council Directive) Regulations 1993)**
- All commercial agents are entitled on termination to either compensation (the default unless the contract expressly provides for indemnity) or an indemnity; compensation is uncapped and values the agency as if it had continued; the indemnity is capped at one year's remuneration averaged over the preceding five years (or the agency period if shorter). — [Weightmans](https://www.weightmans.com/insights/commercial-agents-council-directive-regulations-1993-rules-for-principals-and-agents/); [Geldards on calculating compensation](https://www.geldards.com/insights/calculating-compensation-under-the-commercial-agents-regulations/); [HCR Law](https://www.hcrlaw.com/news-and-insights/the-commercial-agents-regulations/)
- Distributors buy and resell on their own terms and prices, so the supplier loses control of onward sale; "Distributor agreements however are not subject to the same statutory implications as commercial agents." — [Birch Law](https://birchlaw.co.uk/services-businesses/commercial-law-commercial-agents-and-distributors/); [Oury Clark quick guide](https://ouryclark.com/resources/quick-guide/commercial-agents-regulations/)

### Inferences
- For a £25–50k first order of consumables, the cheapest robust protection stack is: Trade Assurance (or 30/70 T/T with the 70% released only after a passed third-party inspection), plus one QIMA/SGS man-day (~US$300–400) — about 1% of the order — rather than a letter of credit whose fixed fees (US$500–1,200) are proportionally heavier and which factories dislike for small orders.
- A UK founder acting as the exclusive UK *distributor* of a foreign manufacturer's line takes title and price risk but gains an asset (the customer base) and avoids the 1993 Regulations; conversely if the founder appoints UK *sub-agents* on commission, those agents will be owed compensation/indemnity on termination — so pick distributors or employees for the UK sales channel and keep any agency contracts short with an express indemnity clause.
- Ask the manufacturer for a 2–3 year exclusive with modest year-1 minimums (roughly the first container) stepping up, carve-outs for existing UK accounts and online marketplaces, and a right to sell the line under a private label — these are the terms the law-firm guides show as standard.

### Gaps
- No source gave typical sample charges (e.g. whether sample fees are refunded against the first order) or typical production lead times for industrial consumables; these vary by product and must be quoted.
- SGS/BV do not publish rates; the figures are secondary compilations.
- The outcome of the UK government's 2024 consultation on deregulating the Commercial Agents Regulations was not retrievable (Stevens & Bolton page redirected); as of the sources found, the Regulations remain in force.
- Alibaba buyer-side transaction fees (card/T/T processing percentages) were not captured; the 1–2% figure is supplier-side.

---

## 5. UK fulfilment: 3PL pricing for B2B pallet-in/parcel-out, small-account 3PLs, pallet networks, parcel rates, returns

### Takeaway
UK 3PL published price lists in 2026 put pallet storage at roughly £3–6.50 per pallet per week (Beckdale £4.10 standard, £6.00 with picking access), container devanning at £100–300 per box, pick/pack at about £1.50–2.20 per order for starter volumes plus £0.20–0.35 per extra item, and returns at £1.50–2.50 per unit; outbound parcels via a 3PL account run about £3–6 (Royal Mail Tracked 24/48, DPD next day £4–6.25) and UK pallet-network deliveries from about £45–90 per full pallet nationally (from £67.99 via Palletways on a broker page). Several UK 3PLs (Beckdale, Choice, Gus Logistics, On Time Media, Make and Supply) publicly state no minimum volumes.

### Cited Findings

**Published 3PL price lists**
- Beckdale Shipping (published price list): standard pallet storage £4.10/week (£17.77/month), pallet with picking access £6.00/week; racking full bay £21.00/week; picking bins £0.13–0.26/week; goods-in base £1.50 per delivery + £0.005/item (max £7 per SKU); pallet unloading £4.25/pallet; 20ft container palletised £100, loose £180; 40ft palletised £160, loose £300; base pick £0.45–3.80 by item size/SKU count; cartons from £0.30; shipping via 3PL account: Tracked 48 parcel £3.14, Tracked 24 £4.08, DPD Next Day £6.25, Parcelforce 24 (to 30 kg) £8.35; "No Monthly Account Fee", no contracts, returns processed at the goods-in rate. — [Beckdale pricing](https://www.beckdaleshipping.co.uk/Pricing_Costs_Calculations)
- Ogden Fulfilment pricing guide (dated 1 June 2026): ambient pallet storage £10–30 per pallet position per month; inbound palletised £10–25 per pallet, cartons £1.50–3.00; pick first unit £0.80–1.50, additional units £0.10–0.30; all-in single-item order £1.00–2.00; returns £1.50–2.50 per unit (complex £3–5); industry minimum monthly spend £300–800 (Ogden: no minimum); Q4 peak surcharges 10–25% on pick rates; illustrative outbound: Royal Mail Tracked 48 £2.20–3.00, Tracked 24 £3.00–3.80, DPD Next Day £4.00–6.00. — [Ogden Fulfilment pricing](https://www.ogdenfulfilment.co.uk/fulfilment-pricing-uk/)
- Eightx UK 3PL Cost Index (13 June 2026): pick-and-pack £1.50–2.20 per order at <2,500 orders/month, £0.45–1.00 at 10,000+; pallet storage from £1.50/week bulk, £3.00–5.00 mid-market, up to £6.50 South East/overflow; inbound £1.50/SKU + £0.005/unit or £5–16/pallet; RH&D £1.30–3.50/pallet; extra items £0.20–0.35; all-in per order before shipping £2–6. — [Eightx UK 3PL Cost Index 2026](https://eightx.co/blog/uk-3pl-cost-index)
- US benchmark for B2B orders (case picks, pallet building, retailer routing guides): average US$4.80 per order. — [Fulfill.com 3PL pricing 2026](https://www.fulfill.com/3pl-pricing)

**UK 3PLs that take small B2B accounts (self-described)**
- Beckdale: "no minimum and no maximum", B2B and B2C, no monthly fees, small parcels from £3.81. — [Beckdale small parcel pricing](https://www.beckdaleshipping.co.uk/Fulfilment/3pl/3pl-small-parcel-pricing-uk-transparent-costs)
- Gus Logistics (Cheshire): B2B/wholesale fulfilment with pallet delivery, mixed B2B/B2C from one warehouse, no minimum volumes. — [Gus Logistics](https://www.guslogistics.co.uk/b2b-fulfilment-cheshire/)
- Choice Fulfilment (Devon): no minimum contract or order quantity; handles from small boxes to pallets. — [Choice Fulfilment](https://choicefulfilment.com/)
- Rapid Pack: B2B with retailer-specific labelling, pallet and parcel. — [Rapid Pack](https://rapidpack.co.uk/b2b-fulfilment); Make and Supply: no minimum order volumes. — [Make and Supply](https://makeandsupply.com/uk-3pl-fulfilment-companies-with-no-minimum-order-volumes/); On Time Media Logistics: small parcels and pallets. — [On Time Media](https://ontimemedialogistics.com/3pl-for-small-business-uk/)

**Pallet networks (UK domestic)**
- 2026 guide: quarter pallet (to ~250 kg) roughly £25–45; half (to ~500 kg) £35–60; full (1.2×1.0 m, to ~1,000 kg) £45–90 nationally; headline "from £25" rarely matches totals once tail-lift, timed slots and awkward postcodes are added. — [We Got The Move 2026](https://www.wegotthemove.co.uk/blog/how-much-does-pallet-delivery-cost-uk-2026)
- Parcel2Go Palletways: "Send a pallet from only £67.99 exc VAT", up to 1,200 kg per pallet. — [Parcel2Go Palletways](https://www.parcel2go.com/couriers/palletways)
- Pall-Ex offers pallet storage and delivery via its UK network. — [Pall-Ex](https://www.pallex.co.uk/)

**Parcel carriers (business accounts)**
- DPD next-day from £7.50 ex VAT (Door 2 Door); a next-day medium parcel with DPD £8.99–19.99 by weight (online "from" rates); Parcelforce business accounts "save up to 45% off standard contract tariff rates"; DPD business account via Parcel2Go for those "sending more than 50 parcels a week". — [ShippyPro UK parcel costs](https://www.shippypro.com/blog/en/how-much-does-it-cost-to-ship-a-package-in-the-uk); [Parcelforce account benefits](https://www.parcelforce.com/business-parcels/account-benefits/apply-for-an-account); [Parcel2Go DPD business](https://www.parcel2go.com/business/dpd-business-account)
- Small business carrier guide: DPD urgent tracked £5–10, Parcelforce for heavier items from £10. — [Q Couriers guide](https://qcouriers.co.uk/2025/11/small-business-courier-services-uk/)

### Inferences
- For 10 pallets of consumables at Beckdale-type rates the first three months' storage is about £530 (10 × £4.10 × 13 weeks) to £780 with picking access; add £100–180 to devan a 20ft. At the Eightx mid-market band (£3–5/wk) it is £390–650.
- A B2B order profile (fewer, larger orders — cartons or part-pallets) pushes per-order cost toward the £2–6 all-in band plus carrier; a 20-line trade order picked as cartons is cheaper per £ of revenue than parcel e-commerce, which is why the 3PL model suits trade sales.
- Outbound cost per trade order for a founder using the 3PL's carrier accounts: roughly £4–9 for a parcel up to 30 kg, £45–90 for a full pallet — so pallet-quantity orders to trade customers should be priced with delivery included above a threshold (e.g. £250–500) and a delivery charge below it.

### Gaps
- Palletways/Pall-Ex do not publish tariff cards; all pallet figures are broker "from" prices or blog benchmarks.
- No DPD/UPS/Parcelforce business account rate card was retrievable; the figures are "from" prices on comparison pages.
- No UK 3PL published a specific B2B per-order (case/pallet-pick) rate; the only B2B per-order benchmark found is US (US$4.80).

---

## 6. Trade credit and cash cycle: 30-day terms, credit insurance, invoice finance, worked first-container cash cycle

### Takeaway
UK SMEs actually get paid in about 27–28 days on average (June 2026 data) but pay their own suppliers in ~37 days and about half of SME invoices are overdue; credit insurance costs roughly 0.1–0.7% of insured turnover and invoice finance advances 70–95% at a 0.5–3% service fee plus SONIA +2.5–4.5%. On a £30k FOB first order from China the founder has ~£9k out at week 0, ~£30k by week 5–6, ~£35k+ by week 13–14 (landed), and only starts to get cash back around week 19–20, with full recovery around week 30 — roughly 6–7 months of working capital.

### Cited Findings
- UK small businesses waited about 28 days to be paid in June 2026 (29.6 days a year earlier). — [NudgeBadger late payment statistics UK 2026](https://www.nudgebadger.co.uk/guides/late-payment-uk-statistics)
- Sage SME Performance Pulse (published 15 June 2026, ~150,000 SMEs): SMEs paid 27 days after invoicing; SMEs took 37.1 days to pay suppliers (up from 31.9); 49% of SME invoices overdue; late payment costs the UK economy £11bn a year. — [ITBrief UK, 15 Jun 2026](https://itbrief.co.uk/story/uk-small-business-profits-rise-as-late-payments-bite)
- DBT statistics published July 2026: large businesses paid suppliers in an average of 32 days during 2025, paying 15% of invoices late (25% when reporting began in 2018). — [NudgeBadger citing DBT](https://www.nudgebadger.co.uk/guides/late-payment-uk-statistics)
- £50bn of invoices overdue at any one time; SMEs spend 1.5 million days a year chasing; ~£25,000 average overdue per SME (June 2026, indicative). — [Spark Finance UK Late Payments Report 2026](https://www.sparkfinance.co.uk/research/uk-late-payments-report)
- Trade credit insurance: typical UK premium 0.05–1.0% of insured turnover; Atradius range 0.1–0.5%; Coface/Davies 0.2–0.7% for SMEs; 0.2% common; named-buyer policies can cut premium by up to 50%; Allianz Trade cites "often less than £13,500 on a £4 million turnover". — [iwoca trade credit insurance cost](https://www.iwoca.co.uk/trade-credit/trade-credit-insurance-cost); [Impello 2026](https://www.impelloglobal.com/trade-credit-insurance-cost); [Davies](https://www.daviescorporate.co.uk/commercial-insurance/credit-insurance/how-much-does-it-all-cost)
- Invoice finance (Spark Finance index, June 2026, next review Sept 2026): advance 70–90%; service fee 0.2–3.0% (0.8–1.8% of turnover typical for established SMEs); discount margin SONIA +1.5–7.0%, standard SME SONIA +2.5–4.5%; minimum turnover £100k (some from £50k); start-ups considered with 3–6 months' trading; a £1m-turnover business might pay £8–25k a year. — [Spark Finance rate index](https://www.sparkfinance.co.uk/data/uk-invoice-finance-rate-index)
- Invoice finance: advance 80–95% (specialists to 99%); service charge 0.5–3% of invoice value plus discount charge 1–3% over Bank of England base; base rate 3.75% in September 2026 giving ~5.25–8.25% on drawn balances; hidden costs (setup, audit, minimum usage, exit) £500–2,000+; dilution above 5% materially lowers usable advance. — [Capitalise 2026](https://capitalise.com/gb/insights/payments/7-top-invoice-finance-providers); [MarketInvoice costs](https://marketinvoice.co.uk/guides/costs/); [Funding Fred](https://fundingfred.com/blog/invoice-financing-costs-in-the-uk-typical-fees-discount-rates-and-total-interest)
- PVA removes the up-front import VAT payment; a duty deferment account with guarantee waiver (up to £10,000/month) lets duty be paid monthly by Direct Debit. — [GOV.UK PVA](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return); [GOV.UK guarantee waivers](https://www.gov.uk/guidance/guarantees-and-guarantee-waivers/waivers)

**Worked first-container cash cycle (inference built from the cited inputs; FX and lead-time assumptions flagged)**
Assumptions: £30,000 FOB Shanghai, 6% duty product (e.g. gloves 6216/3926), one 20ft, 10 pallets, VAT-registered with PVA, 30/70 T/T, 5-week production lead time (assumption — supplier quote governs), 6.5-week sea transit (within the 37–53-day Cape range), stock sells evenly over 13 weeks after landing on 30-day terms with customers actually paying at ~30–37 days (Sage/DBT data), £/US$ 1.30 (ASSUMPTION, not sourced).

| Week | Event | Cash out (cumulative £) | Source for input |
|---|---|---|---|
| 0 | PO placed; 30% deposit £9,000 | 9,000 | 30/70 T/T ([Alibaba seller blog](https://seller.alibaba.com/blogs/2026/southeast-asia/agricultural-waste/tt-trade-assurance-payment-guide-alibaba-b2b)) |
| 0 | Product liability policy ~£100–500/yr | ~9,300 | [Suited Insure](https://www.suited.insure/post/how-much-does-liability-insurance-cost-for-a-small-business) |
| 5 | Pre-shipment inspection 1 man-day ~US$309–400 (~£240–310) | ~9,600 | [Xilink/QIMA 2026](https://xilinkglobaltrade.com/qima-inspection-pricing-2026/) |
| 5–6 | 70% balance £21,000 against B/L; cargo insurance ~0.1–0.3% × 110% × CIF (~£35–110) | ~30,700 | [Seafreightgo insurance guide](https://seafreightgo.com/marine-cargo-insurance-cost-guide/) |
| 6 | Vessel departs Shanghai | | |
| 12–13 | Arrives Felixstowe (37–53 days via Cape) | | [Cubic](https://www.gocubic.io/shipping-routes/china/felixstowe) |
| 13 | Ocean freight 20ft ~US$2,000–3,400 (~£1,540–2,600) + UK THC/port/CDS (~£300–400) + haulage (~£400–500) + broker (£75–150) | ~33,300–34,300 | [ExFreight](https://www.exfreight.com/shipping-from-china-to-uk/); [SinoShipment Jul 2026](https://sinoshipment.com/blogs/freight-costs-from-china-to-uk/); [GXpress 2026](https://www.gxpresss.co.uk/uk-customs-clearance-cost-report-2026.html) |
| 13 | Duty 6% × CIF (~£32,000) ≈ £1,920 (paid via broker or deferred to next month's DDA direct debit); import VAT ≈ £6,780 via PVA = no cash | ~35,200–36,200 | [Tariff API 6216000000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/6216000000); [GOV.UK PVA](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return) |
| 13–14 | 3PL devanning £100–180 + first month storage (10 pallets × £4.10 × 4 = £164) | ~35,500–36,500 | [Beckdale](https://www.beckdaleshipping.co.uk/Pricing_Costs_Calculations) |
| 14 | Stock live; first trade invoices issued on 30-day terms | | |
| 14–27 | Sales run (13 weeks); storage ~£40/week declining; pick/pack + carrier per order | | [Eightx](https://eightx.co/blog/uk-3pl-cost-index) |
| 19–20 | First customer cash arrives (27–37 days after invoice) | peak tied-up ≈ £36–37k | [ITBrief/Sage](https://itbrief.co.uk/story/uk-small-business-profits-rise-as-late-payments-bite) |
| 27 | Last stock invoiced | | |
| 31–33 | Last invoices paid | cash cycle complete | |

Result: roughly 31–33 weeks from deposit to final cash on a single container; the peak cash exposure is about £36–37k (≈120% of FOB value) from week 13 until first receipts around week 19–20. Without PVA (not VAT-registered), add ~£6.8k at week 13, taking peak exposure to ~£43k. With 30/70 T/T the first £9k is at risk for 5 weeks before any independent inspection, which is why Trade Assurance or inspection-conditioned balance payment matters.

### Inferences
- Invoice finance at an 85% advance would release ~£25k of a £30k sales ledger within days of invoicing, pulling the cash cycle in by 4–5 weeks at a cost of roughly 1–2.4% of turnover; but most lenders want £50–100k turnover and 3–12 months' trading, so it is a second-container tool, not a first-container one.
- Credit insurance on a small trade ledger costs roughly £60–210 per £30k of insured sales at 0.2–0.7%; named-buyer cover on the two or three largest accounts is the cheap version.
- A second order must be placed around week 14–18 (when the first stock lands and starts selling) to avoid a stock-out at week ~27, which means funding a second deposit before any cash from the first container arrives — the classic two-container working-capital trap.

### Gaps
- No sourced £/US$ rate; the worked example uses an assumed 1.30 and must be re-run at the day's rate.
- No sourced typical production lead time for industrial consumables; 5 weeks is an assumption.
- No source gives a B2B-specific average days-to-pay for industrial trade customers; the 27–37-day figures are all-sector SME averages.

---

## 7. Selling channels for trade: trade counters, wholesalers, Amazon Business, eBay Business & Industrial, own B2B site, marketplaces vs competitors

### Takeaway
Amazon Business is the largest third-party B2B marketplace (US$60bn annualised gross sales, 11 million organisations, UK included) and costs a £25/month Professional plan plus referral fees with B2B discounts; eBay UK's Business, Office & Industrial category charges a 12.5% final value fee plus 30–40p per order since February 2026. National MRO distributors such as RS Group and Cromwell are competitors (and potential large customers), not channels, and no UK-specific market-share data for B2B marketplaces was found.

### Cited Findings
- Amazon Business surpassed US$60bn in annualised gross sales in Q2 2026, serving 11 million+ organisations across 11 countries including the UK; 1.8 million organisations joined in H1 2026; 97 of the Fortune 100. — [Digital Commerce 360, Jul 2026](https://www.digitalcommerce360.com/article/amazon-business-sales/); [ChannelX, Jul 2026](https://channelx.world/2026/07/amazon-business-hits-60-billion-annual-sales-with-11-million-customers/); [Modern Distribution Management](https://www.mdm.com/article/technology/digital-commerce/amazon-business-surpasses-60b-in-annualized-gross-sales-heres-what-to-know/)
- Amazon Business UK seller page: Professional plan £25 (ex VAT) per month plus selling fees; B2B customers order 75% more units per order and make 30% fewer returns than B2C; tools include quantity discounts, business-only pricing and the VAT Calculation Service (VAT-exclusive prices and automatic invoices); "FBA and referral fee discounts on multi-unit business orders with at least 3% business discounts"; "Reduced 2026 fees" banner. — [Amazon Business UK sell page](https://sell.amazon.co.uk/programmes/amazon-business)
- Business orders over US$1,000 of a single product can earn referral fee rates as low as 5% (US programme description). — [ImpactWolves guide](https://impactwolves.com/amazon-business-b2b-marketplace-guide/)
- eBay UK Business, Office & Industrial final value fee rose to 12.5% from February 2026; fixed per-order fee 30p (orders ≤£10) or 40p (>£10); regulatory operating fee ~0.32–0.42%; 20% VAT on fees; Top Rated Seller discount 10% off the variable fee. — [Value Added Resource, 2026](https://www.valueaddedresource.net/ebay-raises-final-value-fees-in-uk-germany-2026/); [eBay UK rate card change](https://www.ebay.co.uk/sellercentre/news/2026-january/rate-card-change); [eBay business seller fees](https://www.ebay.co.uk/help/selling/fees-credits-invoices/fees-business-sellers-activated-managed-payments?id=4809)
- eBay generated US$1.68bn net revenue in the UK; 29% of eBay's top sellers are UK-based. — [Statista eBay UK revenue](https://www.statista.com/statistics/1048213/ebay-net-revenue-in-the-united-kingdom-uk/); [Skillademia eBay statistics](https://www.skillademia.com/statistics/ebay-statistics-2/)
- RS Group and Cromwell Group are named among major MRO distributors; Cromwell is described as "a leading European MRO distributor offering industrial tools, maintenance products, and safety equipment"; the European MRO distribution market was ~US$202.9bn in 2021 growing ~2.8% CAGR; RS Group published FY to 31 March 2026 results on 20 May 2026. — [Precedence Research MRO distribution](https://www.precedenceresearch.com/mro-distribution-market); [SkyQuest Europe MRO](https://www.skyquestt.com/report/europe-mro-distribution-market/market-size); [RS Group FY25/26 results (PDF)](https://www.rsgroup.com/media/oyxhkuz1/rs-group-2025-26-results.pdf)

### Inferences
- For a single industrial line, the realistic channel mix is: (1) direct trade accounts (installers, maintenance contractors, small OEMs) invoiced on 30 days via an own B2B site or simple trade portal; (2) Amazon Business and eBay Business & Industrial for discovery and low-value orders, costing roughly 12.5–15% of sale plus fixed fees, which the 30%-fewer-returns/75%-more-units B2B profile partly offsets; (3) regional wholesalers/merchants and trade counters as *customers* at distributor margin. RS/Cromwell/Zoro-type nationals are the price benchmark and, if the product is differentiated, a later listing target rather than a day-one channel.
- Marketplace fees (12.5–15%) plus 3PL pick/pack and carrier (£4–9) mean a £40 B2B parcel order nets roughly £27–30 before product cost, so marketplace channels only work at trade-margin products (>40% gross) or for carton/multi-unit orders.

### Gaps
- No UK-specific Amazon Business GMV or share of UK B2B online sales was found (only the global US$60bn figure).
- No public eBay UK Business & Industrial category volume data was found.
- No source describing typical trade-counter/wholesaler purchasing terms (margins, listing fees, rebates) for a new industrial line was found in this research.

---

## 8. One-page checklist and cost stack for a £30k FOB order

### Takeaway
A £30k FOB (China, 20ft, 6% duty) order lands at roughly £35–36.5k all-in at September 2026 rates — about 17–22% on top of FOB — with import VAT (~£6.8k) a non-cash item under PVA; the largest variable items are ocean freight (depends on the week booked and Golden Week surcharges) and duty (0–8% depending on commodity code and whether preference applies).

### Cited Findings (cost stack, £30,000 FOB Shanghai, 10 pallets, one 20ft, VAT-registered, PVA; FX assumed £1 = US$1.30 — assumption)
| Item | Low £ | High £ | Basis / source |
|---|---|---|---|
| Goods FOB | 30,000 | 30,000 | given |
| Pre-shipment inspection (1 man-day) | 240 | 460 | US$309–600 ([Xilink/QIMA](https://xilinkglobaltrade.com/qima-inspection-pricing-2026/); [ChinaWithMe SGS](https://chinawithme.com/guides/pre-shipment-inspection-china)) |
| Ocean freight 20ft China–UK | 1,540 | 2,620 | US$2,000–3,400 ([ExFreight](https://www.exfreight.com/shipping-from-china-to-uk/); [SinoShipment Jul 2026](https://sinoshipment.com/blogs/freight-costs-from-china-to-uk/)); note WCI Shanghai–Rotterdam US$3,485/40ft on 24 Sep 2026 ([Drewry](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry)) |
| Peak/GRI risk (if sailing early Oct) | 0 | 920 | GRI US$1,200/20ft announced for early Oct ([YQN](https://www.yqn.com/intro/blog/post/ocean_freight_increase_2026)); Maersk PSS US$0 from 1 Sep ([Shypple](https://help.shypple.com/en/peak-season-surcharges-asia-europe-2026)) |
| Marine cargo insurance (110% CIF × 0.1–0.3%) | 35 | 110 | [Seafreightgo](https://seafreightgo.com/marine-cargo-insurance-cost-guide/) |
| UK THC + fuel surcharge | 230 | 540 | US$200–400 THC + US$100–300 fuel ([SinoShipment](https://sinoshipment.com/blogs/freight-costs-from-china-to-uk/)) |
| Port origin-charge surcharge + Felixstowe import charge + CDS | 65 | 100 | £35–70 + £26.16 + £3.50 ([GXpress report 2026](https://www.gxpresss.co.uk/uk-customs-clearance-cost-report-2026.html)) |
| Customs broker declaration | 50 | 150 | [GXpress](https://www.gxpresss.co.uk/customs-broker-fees-uk.html) |
| Haulage port → 3PL | 400 | 500 | US$650 example ([DTFU Mar 2026](https://www.dtfulogistics.com/news/sea-shipping-cost-from-china-to-uk/)) |
| Import duty 6% × CIF (~£32,000) | 1,920 | 1,920 | 6% gloves ([Tariff API 6216000000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/6216000000)); 0% for filters/tools/switches ([8421230090](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8421230090)); 8% bearings ([8482109000](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8482109000)) |
| Import VAT 20% × (CIF + duty) ≈ £6,780 | 0 cash | 0 cash | PVA: declared and recovered on the same return ([GOV.UK](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return)); £6,780 cash if not VAT-registered |
| 3PL devanning (20ft) | 100 | 180 | palletised/loose ([Beckdale](https://www.beckdaleshipping.co.uk/Pricing_Costs_Calculations)) |
| 3PL storage, 10 pallets, 13 weeks | 390 | 780 | £3–6/pallet/week ([Eightx](https://eightx.co/blog/uk-3pl-cost-index); [Beckdale](https://www.beckdaleshipping.co.uk/Pricing_Costs_Calculations)) |
| Product liability insurance (annual) | 100 | 500 | [Suited Insure](https://www.suited.insure/post/how-much-does-liability-insurance-cost-for-a-small-business); from £5.40/month ([Simply Business](https://www.simplybusiness.co.uk/business-insurance/product-liability-insurance/)) |
| **Landed + first 3 months, cash** | **~35,070** | **~38,780** | ≈ 17–29% over FOB (upper end includes October GRI and high-end freight) |
| Memo: import VAT (PVA, non-cash) | 6,780 | 6,780 | |

Per-unit landed cost multiplier at the 6% duty case: roughly 1.17–1.29 × FOB before 3PL pick/pack and outbound carriage; at 0% duty roughly 1.11–1.23.

**One-page checklist (each item traces to a section above)**
1. Register: GB EORI (immediate to 5 working days, free) — [GOV.UK](https://www.gov.uk/eori/apply-for-eori); VAT registration before first import so PVA can be used — [GOV.UK PVA](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return); consider a duty deferment account with ≤£10k/month guarantee waiver — [GOV.UK waivers](https://www.gov.uk/guidance/guarantees-and-guarantee-waivers/waivers).
2. Classify: confirm the 10-digit commodity code and duty via the tariff API; check preference (EU/Turkey/India/Japan/Vietnam 0% on all sample codes) — [Tariff API](https://www.trade-tariff.service.gov.uk/api/v2/commodities/8482109000).
3. Origin proof in the PO: statement on origin (EU, REX if >EUR 6,000), declaration on origin (Turkey, U110/U111), self-certified origin declaration or importer's knowledge (India) — [GOV.UK EU](https://www.gov.uk/guidance/proving-originating-status-and-claiming-a-reduced-rate-of-customs-duty-for-trade-between-the-uk-and-eu); [GOV.UK Turkey](https://www.gov.uk/guidance/summary-of-the-uk-turkey-trade-agreement); [business.gov.uk India](https://www.business.gov.uk/export-from-uk/markets/india/trade-agreement/tariffs-and-customs-for-imports-from-and-exports-to-india/).
4. Supplier verification: audited/verified supplier status, 5+ quotes, MOQ/sample/tooling package negotiated — [Global Sources](https://www.globalsources.com/knowledge/how-to-find-verified-suppliers-from-china/); [Supplier Ally](https://supplierally.com/uncategorized/negotiate-moq-pricing-china-factories-guide/).
5. Payment: Trade Assurance or 30/70 T/T with 70% conditional on passed inspection — [Alibaba](https://seller.alibaba.com/blogs/2026/southeast-asia/agricultural-waste/tt-trade-assurance-payment-guide-alibaba-b2b).
6. Compliance file: EU/UK DoC, test reports, technical file access, importer name/address on product, 10-year retention — [GOV.UK placing on market](https://www.gov.uk/guidance/placing-ukca-or-ce-marked-products-on-the-market-in-great-britain); CE recognised indefinitely — [GOV.UK UKCA](https://www.gov.uk/guidance/using-the-ukca-marking); UK REACH position if chemical consumables — [REACH24H](https://en.reach24h.com/news/industry-news/chemical/uk-reach-transitional-registration-deadlines-extension).
7. Insurance: product liability £2–5m limit; marine cargo 110% CIF — [Simply Business](https://www.simplybusiness.co.uk/business-insurance/product-liability-insurance/); [Seafreightgo](https://seafreightgo.com/marine-cargo-insurance-cost-guide/).
8. Incoterm: FOB (China) / FCA (EU, Turkey); avoid EXW; DDP only for samples — [Freightos Incoterms](https://www.freightos.com/freight-resources/incoterms-plain-english-freight-shipping-guide/).
9. Book freight: avoid first week of October (GRI/Golden Week); ask forwarder for all-in quote incl. THC, port surcharge, CDS, haulage — [Drewry](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry); [Shypple PSS](https://help.shypple.com/en/peak-season-surcharges-asia-europe-2026).
10. Inspection: book QIMA/SGS 48 h ahead of ship date — [QIMA](https://www.qima.com/your-eyes-in-the-factory).
11. 3PL onboarded before arrival: devanning rate, pallet storage, B2B order handling, carrier accounts, returns rate — [Beckdale](https://www.beckdaleshipping.co.uk/Pricing_Costs_Calculations); [Ogden](https://www.ogdenfulfilment.co.uk/fulfilment-pricing-uk/).
12. Clearance: broker instructed with EORI, VAT number for PVA (DE 3/40), commodity codes, origin proof, DDA number — [GOV.UK PVA](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return); [GXpress](https://www.gxpresss.co.uk/uk-customs-clearance-cost-report-2026.html).
13. Trade terms: 30 days net, credit-check accounts, named-buyer credit insurance on largest 2–3 accounts; plan for 27–37-day actual payment — [ITBrief/Sage](https://itbrief.co.uk/story/uk-small-business-profits-rise-as-late-payments-bite); [iwoca](https://www.iwoca.co.uk/trade-credit/trade-credit-insurance-cost).
14. Channels: own B2B site + Amazon Business (£25/month + fees) + eBay B&I (12.5% + 30–40p) + direct trade accounts; wholesalers as customers — [Amazon Business UK](https://sell.amazon.co.uk/programmes/amazon-business); [eBay fees](https://www.ebay.co.uk/sellercentre/news/2026-january/rate-card-change).
15. Distribution agreement: exclusive UK territory, 2–3 year term, stepped minimums, carve-outs, private-label right; use distributor not agent structure to avoid 1993 Regulations exposure — [Sprintlaw](https://sprintlaw.co.uk/articles/exclusive-distribution-agreement-key-clauses-and-legal-tips/); [Weightmans](https://www.weightmans.com/insights/commercial-agents-council-directive-regulations-1993-rules-for-principals-and-agents/).
16. Cash plan: peak exposure ≈ 120% of FOB from week 13 to ~20; order container two by week 14–18 — see Section 6 worked example.

### Inferences
- The cost stack shows freight + duty + UK handling of roughly £5–8.8k on £30k FOB; a European (Poland/Germany) source for the same 10 pallets would replace the ~£2.3–4.7k freight/port block with ~£0.8–2.3k of road groupage ([Pallet2Ship Poland](https://www.pallet2ship.co.uk/send-pallets/Poland/); [Pallet2Ship Germany](https://www.pallet2ship.co.uk/send-pallets/Germany/)) and 0% duty under the TCA, so the FOB price gap that China must beat is roughly 8–15% of order value plus the working-capital cost of ~7 extra weeks.
- Because import VAT is the single largest cash number in the stack (~£6.8k), the order of operations for a first-timer is VAT registration → EORI → PVA instruction to the broker, before the first container sails.

### Gaps
- FX assumption (US$1.30/£) is unsourced; the £ figures for US$-denominated items must be recomputed at the transaction date.
- Pick/pack and outbound carriage per order are excluded from the stack because they depend on order profile; use the £2–6 all-in per order plus carrier figures in Section 5.
- No sourced figure for bank T/T charges or Alibaba buyer-side payment fees on a £21k balance transfer.
