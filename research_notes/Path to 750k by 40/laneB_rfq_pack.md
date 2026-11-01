# Lane B: supplier shortlist and RFQ pack for the first 10 pre-sell SKUs (as of 1 November 2026)

Companion CSV: `laneB_supplier_shortlist.csv` (40 rows = 10 SKUs x 3 import candidates + 1 UK buy-in fallback each; 29 columns: platform page, product page, quoted price and tiers, MOQ, stated certifications, the required UK standard and whether the supplier claims it, member badge and year, audit status, sample policy, lead time, payment terms, Incoterms, contact route, UK trade price, playbook landed cost, caveats, fetch date). Inputs: `laneB_trade_candidates.md` §6 (the 10-SKU pre-sell order) and `laneB_trade_candidates.csv` (columns `fob`, `moq`, `duty`, `code`, `sup`, `bench`). Raw downloads: `/tmp/claude-0/-home-user-aaaaabbccc/a0801067-c63e-55a8-9f5e-0cc1f9db97b0/scratchpad/rfq_dl/` (93 files); parsers and the CSV builder in `.../scratchpad/rfq_scripts/`.

## 0. Method and access log

Budget ~100 fetches; actual 94: 5 access probes, 19 Made-in-China keyword searches (570 product cards parsed), 29 supplier product pages + 28 company-profile pages for the 30 shortlisted listings (Tcbest's two pages were part of the probes), 11 UK fallback pages, 2 GlobalSources attempts. No searches via a search engine were needed; all prices below are read from the supplier's own listing or the UK wholesaler's page on 1 Nov 2026 unless marked "(23 Oct note)".

| Site | Result | Consequence |
|---|---|---|
| Made-in-China.com search, product and company-profile pages | HTTP 200 throughout | Primary source. Company profiles expose business type, year established, headcount, management-system certs, payment terms, Incoterms, lead time, export years; product pages expose price tiers, MOQ, sample price, HS code, certification field. **MIC publishes no transaction volume**; the "Audited Supplier" badge (SGS/BV/TUV report ID) is the only verification signal. |
| Alibaba.com search | HTTP 200 but AWSC CAPTCHA / "Access denied" punish page | Not circumvented; no Alibaba cross-quotes (same as 23 Oct) |
| GlobalSources.com search | HTTP 429 "Too much connections" on both attempts | Not used |
| TLC Direct listing pages (7) | 200 (warning-labels index 404) | Fresh UK bench for 6 SKUs; NICEIC label price reused from 23 Oct note |
| Hydraquip public WooCommerce store API | 200 | Fresh hydraulic bench |
| Agriline FFK093 | 200 (product out of stock) | Price confirmed £85.71 ex VAT |
| Tayna (Yuasa NP7-12) | 200 | £18.60 inc VAT = £15.50 ex VAT |
| pat-labels.co.uk | TLS alert (handshake failure), not retried | No UK short-run PAT-label printer quote |
| BES search | 404 | Not used |

Selection rule per SKU: from the parsed cards, keep listings whose title matches the spec, prefer Diamond/Gold + Audited, MOQ <= 3x the plan, then read the product page and the company profile. "Years on platform" is the member-since year on the profile. Where a listing price is a range (US$1.00-200.00 etc.), the CSV says so and the RFQ asks for a firm tier price.

## 1. Import vs buy-in at a glance (per unit, £, ex VAT)

Landed cost = FOB US$ ÷ 1.30 × (1.20 + duty), the playbook method; duty from `laneB_trade_candidates.csv`. "CSV FOB" is the figure the scoring used on 23 Oct; "best shortlist FOB" is the lowest credible tier price found on 1 Nov at or near the plan MOQ.

| # | SKU (CSV id) | Duty (code) | CSV FOB → landed | Best shortlist FOB → landed | UK fallback (ex VAT) | Import as % of buy-in |
|---|---|---|---|---|---|---|
| 1 | NiCd EL stick 4.8V 1.5-1.8Ah (C1-10) | 0% (8507302090) | US$3.50 → £3.23 | Tcbest US$4.20 @100 → £3.88; US$3.50 @1,000 → £3.23; JYH AA800 US$2.50-3.50 @3,000 → £2.31-3.23 | TLC EM B980/315 £12.19 (5+ £11.17); LT DL3BAT 1800mAh £6.30 | 32-62% |
| 1b | NiCd 4Ah D-cell stick (C1-11, proxy) | 0% | US$7.50 → £6.92 | not separately quoted; included in RFQ 1 | TLC EM B170/44 £19.95 | 35% |
| 2 | Type 2 SPD 1P+N (C1-24) | 0% (8536301000) | US$4.00 → £3.69 | Sunpeace US$2.90 @5-999 → £2.68; Leeyee TUV-CB 2P US$4.50-5.00 → £4.15-4.62; Zhengkai US$1.50-3.00 → £1.38-2.77 | TLC BG SPDT21N £18.90 | 14-24% |
| 3 | Earth rod 5/8"x4ft + stud + clamp (C1-27) | 2% (7326909800) | US$3.50 → £3.28 | Ying Yi rod US$3.00 @100 → £2.82; Changdi US$3.60-4.80 → £3.38-4.50; add ~US$1.00-1.50 for stud + clamp (not yet quoted) → set ≈ £3.9-5.9 | TLC ER58 £10.50 + stud £1.60 + EC58 clamp £4.90 = £17.00 | 23-35% |
| 4 | VRLA 12V 7Ah (C1-16) | 2% (8507208090) | US$5.50 → £5.16 | Minhua MS7-12 US$4.91-5.77 @100 → £4.61-5.41; Vesion/NPP US$7.00 @10 → £6.57 | TLC TS B7 £17.34; Tayna Yuasa NP7-12 £15.50 | 30-42% |
| 5 | Warning-label pack of 25 (C1-08, proxy) | 6% (3926909790) | US$1.50 → £1.45 | Itech US$0.04/label x 25 = US$1.00 @3,000 labels → £0.97 | TLC NICEIC pack of 25 £8.10 (23 Oct note) | 12% |
| 6 | SWA gland pack BW20 (C1-29) / CW20 (C1-30) | 0% (8547900000) | US$2.20 → £2.03 / US$3.50 → £3.23 | Hongxiang US$1.00/gland @50 + ~US$0.40 shrouds/tags → £2.22 per BW pair; Hongdu US$0.86 @500 → £1.59 | TLC B20 £4.10 (10+ £3.50); C20 £7.35 (10+ £6.60) | 45-63% (BW) |
| 7 | LV resin joint kit 1.5-6mm² (C1-33) | 0% (8547200000) | US$6.00 → £5.54 | Johnn MM11 US$2.95 @5 → £2.72; Wellco S1/S2 US$6.00 @50 → £5.54 (US$2.45 @1,000 → £2.26) | TLC WK WSJA0 £12.60 (2+ £11.55) | 24-48% |
| 8 | Genset filter kit per engine (C1-42) | 0% (8421230090) | US$40.00 → £36.92 | Congben Perkins fuel filter US$3.00 @100; kit of 4 filters est. US$12-16 → £11-15 (estimate, kit not yet quoted) | Agriline FFK093 (1104D) £85.71; Vicary 3CX kit £46.67 | 13-32% |
| 9 | Hydraulic adaptors, 40-SKU rack (C2-02 / C2-03) | 0% (7307998099) | US$0.20 → £0.18 / US$0.60 → £0.55 | Beiteer US$0.20 @50 → £0.18; Ningji US$0.45-0.47 @100 → £0.42; Pehel US$0.50 @200 → £0.46 | Hydraquip reducers £2.34-3.34; 60° coned swivels £10.86-13.69 | 5-20% |
| 10 | PAT PASS labels roll of 500 (C1-06) | 0% (4821101000) | US$3.88 → £3.58 | Guanhua US$1.04-1.80 @1,000 rolls → £0.96-1.66 (must switch to synthetic face); Huibochen US$3.87 → £3.57 | TLC KT 500PASS £13.50; TM LAB1 £14.00 | 7-26% |

Reading: every SKU imports at 5-63% of the UK buy-in price, but the gap is thinnest on BW gland packs (45-63%) and widest on hydraulics, labels and SPDs. First-order MOQ values at the best shortlist FOB: NiCd £388 (100), SPD £134-231 (50), earth rods ~£390-590 (100 sets), VRLA £461-541 (100), warning labels £116 (3,000 labels = 120 packs), glands £111-222 (50-100 pairs), joint kits £14-277 (5-50), filter kits £110-150 (10 kits, est.), hydraulic rack ~£400-1,800 depending on size mix (40 SKUs x 50-100 pcs; the note's £1.5-2.5k allowed for freight), PAT labels £960-3,570 (1,000 rolls).

## 2. RFQ pack: shared terms, then one copy-ready email per SKU

Send each email through the "Send Inquiry" button on the product page listed in the CSV (Made-in-China hides supplier emails until you log in; the first reply will carry the sales contact's email and WeChat). Paste the same text to all three suppliers for the SKU, changing only the product reference line. Replace the bracketed fields once: [Company Ltd], [UK address + postcode], [EORI GB...], [your name], [phone/WhatsApp], [GS1 prefix].

Common terms (quoted in every email, repeated here so the buyer can defend them):
- Quantities: price at MOQ and at 3 x MOQ, each as a firm unit price, plus the price break above that.
- Incoterms: three columns - FOB [named China port], EXW factory, and DDP [UK postcode] (duty and UK VAT shown separately). Ask which freight forwarder they use for LCL to Felixstowe/Southampton.
- Documents with the quote: Declaration of Conformity (CE and/or UKCA) naming the product model and the standard, the type-test report from a CB/TUV/SGS/Intertek lab, ISO 9001 certificate, factory audit report (SGS/BV/TUV, the one behind the MIC "Audited Supplier" badge), product datasheet and drawing, and where relevant the SDS and transport classification letter.
- Samples: 2-5 pieces, paid at sample price plus courier on the buyer's DHL/FedEx account, credited against the first PO.
- Packaging for UK resale: inner retail pack with the buyer's label (artwork supplied), EAN-13 barcode printed on the pack (buyer supplies GS1 numbers), "Imported by [Company Ltd], [UK address]" and the CE/UKCA mark where required, English instructions; master cartons <= 20 kg, carton label with PO, SKU, quantity, gross/net weight; pallets ISPM-15 heat-treated, 1.2 x 1.0 m, max 1.6 m high.
- Lead time: days from deposit to ex-works for the MOQ order and for 3 x MOQ.
- Payment: 30% T/T deposit, 70% against copy B/L, or 100% through Made-in-China Secured Trading (escrow) for orders under US$5,000; LC at sight for orders above US$10,000.
- Quote validity: 30 days (copper and lead items: 30 days with the LME index date stated).
- Standard questions: factory or trading company; year founded; number of production lines; do you already export to the UK/EU and to whom; private-label/OEM minimum; warranty terms; defect/return handling.

### RFQ 1 - NiCd emergency-lighting battery sticks 4.8V (C1-10, and the 4Ah D-cell variant C1-11)
To: Shenzhen Tcbest Battery Industry (product BZCJMgeOkzhf); JYH Technology (product hBjnCXwAyFpl, AA800 4.8V high-temp EL pack); Ningbo NBCELL (product oKeJrvsWCzpU)

Subject: RFQ - 4.8V NiCd emergency-lighting battery sticks, high-temperature cells, 100 / 300 pcs, UK

Hello,

[Company Ltd] is a UK trade supplier of electrical compliance consumables to electrical contractors and emergency-lighting maintenance firms. We are sourcing replacement NiCd battery sticks for self-contained emergency luminaires and would like your quotation for the items below.

Item A - 4.8V 1.5-1.8Ah stick: 4 x sub-C (SC1500 or SC1800) high-temperature NiCd cells, series, inline "stick" format (end-to-end, approx. 23 x 180 mm), 150 mm 20 AWG leads red/black, connector [2-pin JST-XH / bare tinned ends - we will confirm against our sample], heat-shrink sleeve white.
Item B - 4.8V 4Ah stick: 4 x D (D4000) high-temperature NiCd cells, series, inline stick, same leads/connector.
Item C - 3.6V versions of A and B (3 cells) - please price as an option.
Cells: high-temperature grade rated for continuous trickle charge at 0.05C at up to 55-70 °C for 4 years, cells to IEC/BS EN 61951-1; capacity at 0.2C after 28-day storage stated; please name the cell manufacturer and give the cell datasheet.
Quantity: 100 pcs of A and 100 pcs of B (your MOQ), and 300 pcs of each. Please also state your price at 1,000 pcs.
Standards and documents required with the quote: cell datasheet; IEC 61951-1 test report (capacity, charge retention, endurance at elevated temperature); CE/UKCA Declaration of Conformity; RoHS declaration (cadmium exemption for emergency lighting - Directive 2006/66/EC Art. 4(3)(a) equivalent); safety data sheet for the cells; UN38.3 is not required for NiCd but please confirm the pack is "not restricted" for sea and road under current IATA/IMDG/ADR and provide a non-dangerous-goods statement.
Marking: each stick printed with voltage, capacity, "Ni-Cd", the crossed-out wheeled bin, "Cd" below it, date code, and "For emergency lighting use only"; our brand and "Imported by [Company Ltd], [UK address]" on the retail sleeve.
Samples: 2 x A and 2 x B with the cells you would use in production, on our courier account, before any order.
Incoterms: quote FOB Shenzhen/Guangzhou, EXW, and DDP [UK postcode] (duty 0%, UK VAT separate).
Packaging: each stick in a labelled poly bag with EAN-13 barcode (numbers supplied), 10 sticks per inner box, master carton <= 20 kg, short-circuit protection per IATA PI/ADR requirements.
Lead time from deposit for 100 + 100 pcs and for 300 + 300 pcs; payment 30% deposit / 70% against B/L copy or Secured Trading; quote valid 30 days.
Please also confirm: factory or trading; year founded; whether you supply any EU/UK emergency-lighting brands; OEM label minimum.

Kind regards,
[your name], [Company Ltd], [UK address], EORI [GB...], [phone/WhatsApp]

### RFQ 2 - Type 2 single-phase SPD, DIN rail (C1-24)
To: Wenzhou Leeyee Electric (ask for the "TUV CB SPD 2 Poles 10/20kA 275V" model, not LY1-B80); Sunpeace Electric (product jzeYGiNlELVs); Wenzhou Zhengkai Electric (product wRGruvXJXLhN)

Subject: RFQ - Type 2 SPD 1P+N 275V 20/40kA to BS EN 61643-11, 50 / 150 pcs, UK

Hello,

[Company Ltd] supplies UK electrical installers. We need a Type 2 surge protective device for single-phase 230 V TN-C-S and TT installations fitted in consumer units under BS 7671 regulation 534.
Specification: Type 2 (Class II / T2) to IEC/BS EN 61643-11:2012+A11:2018; configuration 1P+N "CT2 / 1+1" (MOV L-N, GDT N-PE) with a 2-pole alternative also priced; Uc >= 275 V AC; In 20 kA (8/20 µs); Imax 40 kA; Up <= 1.5 kV (please state actual Up at In); pluggable modules with thermal disconnector and visual status window; remote-signalling contact as an option; 35 mm DIN rail; 2 modules wide (36 mm); terminals 4-25 mm²; IP20; operating -40 to +70 °C.
Quantity: 50 pcs (our first order) and 150 pcs; state the price break at 500 pcs.
Documents required with the quote (the order depends on them): full IEC 61643-11 type-test report from a CB-scheme or TUV/SGS/Intertek laboratory for the exact model quoted (not a family certificate alone), CB certificate number so we can verify it, CE and UKCA Declaration of Conformity (Low Voltage Directive / Electrical Equipment (Safety) Regulations 2016 and EMC where applicable), RoHS declaration, datasheet with Up/In/Imax/Uc/Ifi, wiring instructions in English, and the recommended back-up fuse/MCB rating.
Marking: product face printed with Type 2, Uc, In, Imax, Up, standard number, CE and UKCA, our brand and model; retail box with EAN-13, "Imported by [Company Ltd], [UK address]".
Samples: 5 pcs at sample price on our courier account; we will have them independently checked before ordering.
Incoterms: FOB Ningbo, EXW, and DDP [UK postcode] (duty 0%). Lead time for 50 and 150 pcs. Payment 30/70 or Secured Trading. Validity 30 days.
Please confirm: factory or trading; year founded; existing UK/EU customers for this model; private-label minimum; replacement-module price.

Kind regards, [signature]

### RFQ 3 - Copper-bonded earth rods 5/8" x 4 ft with driving stud and clamp (C1-27)
To: Shandong Ying Yi Import & Export (product bFefqSiolHaM); Qingdao Changdi Electric Power Equipment (product KLQUErJyFacA); Jiangsu Chuandu Electrical Technology (product KypEqGfJhFho)

Subject: RFQ - copper-bonded earth rod 14.2 mm x 1200 mm, 250 µm, with stud and clamp, 100 / 300 sets, UK

Hello,

[Company Ltd] supplies UK electrical contractors with earthing materials for TT installations and generator earths. Please quote the set below.
Rod: copper-bonded low-carbon steel, nominal 5/8" (14.2 mm) x 1200 mm (4 ft), copper layer >= 250 µm (0.254 mm) molecularly bonded/electroplated, both ends threaded 5/8" UNC (one end chamfered/pointed), steel tensile >= 600 N/mm², straightness <= 1 mm/m.
Accessories per set: 1 x threaded driving stud (hardened), 1 x rod coupler (please price separately as well), 1 x rod-to-cable clamp for 5/8" rod taking 6-25 mm² (BS 951 pattern or U-bolt clamp, copper alloy / gunmetal).
Also price the 3/8" (9 mm) x 1200 mm rod and 5/8" x 1500 mm rod as options.
Quantity: 100 sets and 300 sets; state the price break at 1,000.
Standards and documents: test report to IEC/BS EN 62561-2 (copper thickness, adhesion/bend test, salt-spray corrosion) for the 14.2 mm rod - please state the laboratory and date; mill certificate for steel and copper; UL 467 listing if held; ISO 9001 certificate; the rods are for use under BS 7430, so please confirm the copper thickness is measured not nominal.
Marking: each rod stamped or laser-marked with diameter, length, copper thickness and your mark; bundles of 10 strapped; stud and clamp bagged per rod with our label and EAN-13.
Samples: 2 complete sets by courier on our account.
Incoterms: FOB Qingdao/Shanghai, EXW, and DDP [UK postcode] (duty 2%); please quote pallet weight and dimensions for 100 and 300 sets (rods are 1.2 m, so we will take pallets). Lead time for 100 and 300 sets. Payment 30/70 or LC at sight above US$10,000. Validity 30 days with the LME copper reference date stated.
Please confirm: factory (mill) name and location if you are a trading company; year founded; UK/EU customers.

Kind regards, [signature]

### RFQ 4 - VRLA 12V 7Ah fire-panel / UPS battery (C1-16)
To: Fujian Minhua Power Source (product snerJWNMfIVF, MHB MS7-12); Fujian Jiage Power Tech / GEM (product ynNpcXIMAYWH, GS12-7); Vesion Group (product YUWrVPcAqqkn, NPP NP12-7)

Subject: RFQ - VRLA AGM 12V 7Ah, F1 and F2, 5-year design life, UN2800, 100 / 300 pcs, UK

Hello,

[Company Ltd] supplies UK fire-alarm maintenance firms and electrical contractors. Please quote your 12V 7Ah VRLA battery to the specification below.
Specification: AGM, valve-regulated, non-spillable; 151 x 65 x 94 (+6 terminal) mm; 2.0-2.2 kg; terminals F1 (4.8 mm) and F2 (6.3 mm) - price both; capacity 7.0 Ah at C20 to 10.5 V; standby/float design life 5 years at 20 °C (Eurobat "long life" class or better); float 13.5-13.8 V; max charge 2.1 A; case ABS, with the UL94 V-0 flame-retardant case priced as an option (fire-panel customers ask for it); shelf-life/self-discharge figures; date code on the case.
Quantity: 100 pcs (10 per carton) and 300 pcs; state the price break at 1,000 and whether price is indexed to LME lead (if so, give the index date and formula).
Documents required with the quote: IEC 60896-21/-22 test report (or BS EN 61056-1 for small VRLA) for this model; UN2800 non-spillable test letter (vibration and pressure differential test per IATA Special Provision A67 / ADR SP 238) so we can ship as non-dangerous goods; safety data sheet; CE/UKCA Declaration of Conformity; RoHS; ISO 9001 and the SGS/BV audit report; datasheet with discharge tables and dimensional drawing.
Marking: case printed with 12V 7Ah, model, terminal type, crossed-out wheeled bin with "Pb", recycling symbol, date code, our brand; carton with EAN-13 and "Imported by [Company Ltd], [UK address]"; short-circuit protection (terminal caps) in the carton.
Samples: 4 pcs (2 x F1, 2 x F2) on our courier account; we will load-test them.
Incoterms: FOB Xiamen/Shenzhen, EXW, and DDP [UK postcode] (duty 2%); pallet weight and dimensions for 100 and 300 pcs. Lead time for both quantities. Payment 30/70 or LC at sight above US$10,000. Validity 30 days.
Please confirm: factory or trading; year founded; UK/EU brands you already manufacture for (OEM); warranty (we need 12 months minimum); whether you also make 12V 2.1-3.2Ah and 12V 17-18Ah in the same range (our next SKUs).

Kind regards, [signature]

### RFQ 5 - Electrical warning-label packs (C1-08)
To: Jiangsu Itech Packaging Printing (product jUDYVuvGhykJ); Shenzhen Huibochen Technology (product mPBUqYsJItVn); Hangzhou Qianxi Crafts (product idUGhItKYyTx, for the engraved circuit-chart upsell only)

Subject: RFQ - printed self-adhesive electrical warning-label packs, UK wording, 200 / 600 packs

Hello,

[Company Ltd] supplies UK electricians with the labels required by the UK wiring regulations (BS 7671, section 514). We need a mixed pack of 25 self-adhesive labels; artwork (vector PDF, UK English, exact wording) will be supplied by us.
Pack content (25 labels): 5 x "Danger 230 V" triangle W012 (ISO 7010) 50 x 50 mm; 5 x RCD quarterly test notice 75 x 50 mm; 5 x mixed cable colours warning (BS 7671 514.14) 75 x 50 mm; 5 x circuit chart / schedule 100 x 75 mm write-on; 5 x "Electrical installation - periodic inspection" notice 75 x 50 mm.
Material: white PVC/vinyl 0.08-0.10 mm or polypropylene, UV-stable, permanent acrylic adhesive, suitable for outdoors and for the inside of consumer-unit lids; print 4-colour process + black; write-on labels with a matt varnish; kiss-cut on one A5 sheet (or 2 sheets) per pack, so one pack = 25 labels.
Quantity: 200 packs (5,000 labels) and 600 packs (15,000 labels); please also price per 1,000 labels for each size.
Documents: material datasheet (face, adhesive, UV rating), ISO 9001 certificate, a digital proof before production and 3 physical pre-production samples; no electrical standard applies but wording must match our artwork exactly.
Packaging: each pack in a resealable poly bag with header card carrying our brand, EAN-13 and "Made in China. Imported by [Company Ltd], [UK address]"; 50 packs per carton.
Incoterms: FOB Shanghai/Ningbo, EXW, and DDP [UK postcode] (duty 6%). Lead time from artwork approval. Payment 30/70 or Secured Trading. Validity 30 days.
Please confirm: factory or broker; year founded; your smallest label size and tolerance; whether you can also supply the labels on 500-label rolls (see our separate RFQ for PAT labels).

Kind regards, [signature]

### RFQ 6 - SWA gland packs BW20 indoor and CW20 outdoor (C1-29 / C1-30)
To: Zhejiang Hongxiang Connector (product QzvREOMxuAhJ); Wenzhou Zhechi Electric (product lSLnkyuGbMYv); Hebei Hongdu Technology (product PGLpTwoCEyRO)

Subject: RFQ - UK-pattern BW and CW brass glands for SWA cable, packed in pairs, 100 / 300 packs each, UK

Hello,

[Company Ltd] supplies UK electrical contractors. We need UK-pattern armoured-cable glands packed as pairs.
Pack A (BW20 indoor): 2 x BW 20 (and 20S) 2-part brass glands for steel-wire-armoured cable, thread M20 x 1.5, armour range 0.9-1.25 mm, cable bedding 11.7-15.3 mm (20S: 8.9-11.7), to BS EN 62444; 2 x brass locknuts; 2 x brass earth tags M20; 2 x black PVC shrouds.
Pack B (CW20 outdoor IP66): 2 x CW 20 (and 20S) 3-part brass glands with outer-sheath seal, IP66 (IP68 to 5 m if available), same accessories plus 2 x neoprene/nylon sealing washers.
Also price the 25 and 32 sizes of both.
Material: brass CZ121/CW614N, natural or nickel-plated (price both), ambient -20 to +80 °C; please state the applicable standard marking on the body (BS EN 62444 or BS 6121) and whether the thread is marked.
Quantity: 100 packs of A and 100 of B, then 300 of each; price break at 1,000 packs.
Documents: dimensional drawing per size, material certificate for the brass, IP test report (CW), ISO 9001; RoHS declaration; UKCA/CE is not required for glands, but a Declaration of Conformity to BS EN 62444 is.
Packaging: each pair with accessories in a printed header-card bag with EAN-13 and "Imported by [Company Ltd], [UK address]"; 50 packs per carton.
Samples: 2 packs of each size, nickel-plated and natural, on our courier account.
Incoterms: FOB Ningbo/Shanghai/Tianjin, EXW, and DDP [UK postcode] (duty 0%). Lead time for 100 and 300 packs. Payment 30/70 or Secured Trading. Validity 30 days with the LME copper date stated.
Please confirm: factory or trading; year founded; UK/EU customers for BW/CW pattern; whether you hold tooling for 20S/20/25/32 UK sizes or would make it (tooling cost and time).

Kind regards, [signature]

### RFQ 7 - LV resin straight joint kits for SWA 1.5-6 mm² (C1-33)
To: Shanghai Wellco International (product GFBakmjPXbAo, size S1/S2); Zhejiang Johnn Electrical (product crOYkJEVafWX, MM11 and any smaller size); Shenzhen Elekv Technology (product XPgRkJpoaAVK, resin only - ask for pouch-size resin)

Subject: RFQ - LV cast-resin straight-through joint kit for 4-core SWA 1.5-6 mm², 50 / 150 kits, UK

Hello,

[Company Ltd] supplies UK electrical contractors with low-voltage cable accessories. Please quote a resin straight-through joint kit for underground use.
Specification: 0.6/1 kV; for 4-core steel-wire-armoured cable 1.5-6 mm² (cable OD approx. 11-19 mm); two-piece clear plastic shell approx. 150-185 mm; two-part polyurethane (preferred) or epoxy resin in a two-compartment pouch with mixing barrier, pre-measured (state the volume in ml), cure time at 20 °C; 4 x mechanical screw connectors or crimp connectors for 1.5-6 mm² (state which); armour continuity by constant-force springs or tinned-copper braid with worm-drive clips (we need the earth path through the armour); roll of sealing tape; sealing plugs; English instructions with pictures; also price the 1.5-10 mm² 5-core and 4-25 mm² sizes.
Quantity: 50 kits and 150 kits; price break at 500 and at 1,000.
Documents required: type-test report to BS EN 50393 (test sequence for LV joints: electrical, thermal cycling, water immersion) or an equivalent IEC 60502-4 report; resin safety data sheet (SDS, UK/EU 16-section format) and CLP hazard classification of parts A and B; declaration that the resin is not classified dangerous for transport in the retail pouch; ISO 9001; RoHS.
Packaging: each kit in a printed retail box with contents list, cure time, hazard pictograms as required by CLP, EAN-13 and "Imported by [Company Ltd], [UK address]"; 20 kits per carton; resin pouches with a 24-month shelf life and batch/expiry printed.
Samples: 3 kits on our courier account for a joint-and-immersion test.
Incoterms: FOB Shanghai/Ningbo, EXW, and DDP [UK postcode] (duty 0%). Lead time for 50 and 150 kits. Payment 30/70 or Secured Trading. Validity 30 days.
Please confirm: factory or trading; who manufactures the resin; shelf life; year founded; UK/EU customers.

Kind regards, [signature]

### RFQ 8 - Genset filter service kits by engine model (C1-42)
To: Hebei Congben Vehicle Fittings (product UpVRdIrUqYhT); Cangzhou Zhuorun Auto Parts / Jieshi (product QGlRDgXEOvWq); Qinghe Jinyao Auto Parts (product eQJRjUHrqDYb)

Subject: RFQ - diesel generator filter service kits (fuel / pre-fuel / oil / air) for Perkins 1103-1104, Kubota V-series, Yanmar, 10 / 30 kits per engine, UK

Hello,

[Company Ltd] supplies UK generator service companies. We want to buy filters assembled as per-engine service kits in our own box. The OEM part numbers below are our cross-reference; please confirm each equivalent you offer by your own part number and tell us if any is not available.
Kit P1 - Perkins 1103A-33G / 1103C-33 genset: fuel filter 26560201 (element 26560163 alternative), pre-fuel/water separator 26560143, oil filter 2654407, air filter [to be confirmed from the genset build - typically 26510342 or 26510337].
Kit P2 - Perkins 1104A-44TG / 1104C-44TAG: fuel filter 26560201, pre-fuel 26560143 (or 4415122 / 130306380 where fitted), oil filter 2654407, air filter [as above].
Kit K1 - Kubota V2203 / V2403 genset: fuel 15231-43560 (or 1G311-43380), oil HH150-32094, air [to be confirmed].
Kit K2 - Kubota V3300 / V3800: fuel 1G311-43380, oil HH1C0-32430, air [to be confirmed].
Kit Y1 - Yanmar 4TNV88 / 4TNV98: fuel 129A00-55800, oil 129150-35153, air [to be confirmed].
Quantity: 10 kits per engine (50 kits) and 30 per engine (150 kits); also price per filter.
Quality requirements and documents: filter media efficiency and capacity reports to ISO 19438 (fuel), ISO 4548-12 (oil) and ISO 5011 (air) for the quoted part numbers, burst/collapse pressure for spin-on canisters, IATF 16949 or ISO 9001 certificate, factory audit report; please state which filters are made in your own plant and which are bought in; micron rating of each.
Marking: each filter boxed individually with its part number and our cross-reference; kit in a printed carton with our brand, engine model, contents list, EAN-13 and "Imported by [Company Ltd], [UK address]"; no OEM trademarks on the product or box.
Samples: 1 kit P1 and 1 kit K1 on our courier account for fitment check.
Incoterms: FOB Tianjin/Qingdao, EXW, and DDP [UK postcode] (duty 0%). Lead time for 50 and 150 kits. Payment 30/70 or Secured Trading. Validity 30 days.
Please confirm: factory or trading; year founded; filter brands you produce for (OEM/private label); UK/EU customers.

Kind regards, [signature]

### RFQ 9 - Hydraulic adaptor starter rack, 40 SKUs BSPP / JIC (C2-02 / C2-03)
To: Ningbo Ningji Machinery Technology (product RgkpEtuYTrWo, model 9B); Ningbo Yinzhou Pehel Machinery (product WvknBXoxrDhj); Hebei Beiteer Hydraumatic Equipment (product FfhULRglOQcV, model 2BJ)

Subject: RFQ - 40-line hydraulic adaptor assortment, BSPP and JIC, carbon steel zinc-plated, 50 / 150 pcs per line, UK

Hello,

[Company Ltd] supplies UK plant-hire depots and agricultural engineers with a consignment rack of hydraulic adaptors. Please quote the 40 lines below, each at 50 pcs and 150 pcs, and state carton quantity per line.
Group A - BSPP male/male equal and reducing adaptors (60° cone, BS 5200 / ISO 1179-2 / ISO 8434-6): 1/8, 1/4, 3/8, 1/2, 3/4 equal (5 lines); 1/4-1/8, 3/8-1/4, 1/2-3/8, 3/4-1/2, 1/2-1/4 reducing (5 lines).
Group B - BSPP male x BSPP female reducing bushes and extenders: 1/4M-1/8F, 3/8M-1/8F, 3/8M-1/4F, 1/2M-3/8F, 3/4M-3/8F, 3/4M-1/2F (6 lines).
Group C - BSPP female swivel 60° cone to BSPP male, straight: 1/4, 3/8, 1/2 (3 lines); 90° compact elbow swivel 1/4, 3/8, 1/2 (3 lines).
Group D - JIC 37° (SAE J514 / ISO 8434-2) male/male: -4, -6, -8, -10, -12 (5 lines); JIC male x BSPP male: -6 x 1/4, -6 x 3/8, -8 x 3/8, -8 x 1/2, -10 x 1/2, -12 x 3/4 (6 lines); JIC female swivel 90° elbow -6, -8, -10 (3 lines).
Group E - plugs and caps: BSPP hex plugs 1/4, 3/8, 1/2; JIC caps -6, -8 (5 lines) [adjust to reach 40 lines; Pehel please also price your 64-piece JIC plug & cap kit in the carry case].
Material and finish: carbon steel (20# / C22 or better), zinc-plated trivalent clear or yellow passivate with >= 72 h neutral salt spray to ISO 9227, forged or bar-stock stated per line, size stamped on the hex; working pressure per size with 4:1 safety factor stated; bonded seals for Group A/B as an option.
Documents: drawing pack per line with thread and cone dimensions, pressure rating table, plating test report, material certificate, ISO 9001.
Packaging: each line in a labelled poly bag of 10 or 25 with part number, size and EAN-13 (numbers supplied); cartons <= 20 kg; "Imported by [Company Ltd], [UK address]" on the carton.
Samples: one of each of 10 lines we will name after your quote, on our courier account, for gauge checks.
Incoterms: FOB Ningbo/Tianjin, EXW, and DDP [UK postcode] (duty 0%). Lead time for the 40-line order at 50 and at 150 pcs per line. Payment 30/70 or Secured Trading. Validity 30 days.
Please confirm: factory or trading; year founded; stock lines vs made-to-order; UK/EU customers; whether you can supply the printed rack labels.

Kind regards, [signature]

### RFQ 10 - PAT test labels, PASS roll of 500 and FAIL roll of 250 (C1-06 / C1-07)
To: Suzhou Guanhua Paper Factory (product JXVmMqeChEUW); Shenzhen Huibochen Technology (product dzuRehkPEpWZ); Henan Henglun Paper Industry (product luYpCyMGhrki)

Subject: RFQ - printed PAT test labels on rolls (PASS 500, FAIL 250), synthetic write-on stock, 1,000 / 3,000 rolls, UK

Hello,

[Company Ltd] supplies UK portable-appliance-testing firms. We need durable printed labels on rolls; artwork (vector PDF) will be supplied.
Label 1 - PASS: 50 x 25 mm, green and white print, text "PASSED - Appliance ID / Date tested / Retest due / Tested by" with write-on boxes; 500 labels per roll, 25 or 40 mm core, outside-wound, perforation between labels optional.
Label 2 - FAIL: 50 x 25 mm red and white, "FAILED - DO NOT USE", 250 per roll.
Label 3 (option) - PASS 38 x 19 mm small, 500 per roll.
Material: NOT thermal paper - matt white polypropylene or vinyl 60-80 µm, top-coated for ballpoint/permanent marker, permanent acrylic adhesive, service temperature -20 to +80 °C, UV-stable for 2 years indoors; flexographic or digital print, 2 colours.
Quantity: 1,000 rolls PASS + 1,000 rolls FAIL (your MOQ) and 3,000 of each; price per roll and per 1,000 labels; also price 500 rolls as a trial run at a premium.
Documents: material and adhesive datasheets, ISO 9001, digital proof before print, 3 physical pre-production rolls; no electrical standard applies.
Packaging: each roll shrink-wrapped with a core label carrying our brand, EAN-13 and "Imported by [Company Ltd], [UK address]"; 50 rolls per carton.
Incoterms: FOB Shanghai/Tianjin, EXW, and DDP [UK postcode] (duty 0%). Lead time from proof approval for 1,000 and 3,000 rolls. Payment 30% deposit / 70% before shipment or Secured Trading. Validity 30 days.
Please confirm: factory or broker; year founded; whether you can run synthetic (PP/vinyl) stock on the same presses; smallest label size; UK/EU customers.

Kind regards, [signature]

## 3. Compliance checklist per SKU (hold before the first listing)

Common to all 10: your name and UK address on product or packaging as importer (Product Safety / UKCA-CE importer duty); GS1 UK barcode numbers; product-liability insurance (£2-5m) in force before the first sale; a technical-file folder per SKU (supplier DoC, test report, datasheet, drawings, photos of markings, batch records) kept 10 years; WEEE registration is not triggered by batteries, rods, glands, labels or filters, but SPDs are EEE (check your WEEE producer obligation once volumes exceed the small-producer threshold). "UN38.3 not needed" applies to every SKU here: no lithium cells are in the first 10 SKUs.

| # | SKU | Documents to hold | Marking on product/pack | Regulatory registrations | Transport class / carrier note |
|---|---|---|---|---|---|
| 1 | NiCd EL sticks | Cell datasheet; IEC 61951-1 report; CE/UKCA DoC (Batteries & Accumulators (Placing on the Market) Regs 2008; RoHS cadmium exemption for emergency lighting); SDS for the cells; supplier's non-DG statement | Crossed-out wheeled bin, "Cd" chemical symbol, capacity, "Ni-Cd", "for emergency lighting only"; importer name | **Register as a battery producer** (Waste Batteries and Accumulators Regs 2009): below 1 t/yr portable batteries register directly with the Environment Agency; above 1 t join a compliance scheme; offer free take-back once >32 kg/yr supplied; report tonnage | Not dangerous goods (dry NiCd), but packs must be short-circuit protected; no air restriction beyond packing; note NiCd is being phased down in EU battery reg 2023/1542 - UK position unchanged, keep the exemption statement on file |
| 2 | Type 2 SPD | BS EN 61643-11 type-test report for the exact model + CB certificate; CE and UKCA DoC (LVD / Electrical Equipment (Safety) Regs 2016, EMC Regs 2016 statement, RoHS); English instructions; datasheet (Uc, In, Imax, Up) | CE + UKCA on the body; Type 2 / Uc / In / Imax / Up; model; importer on pack | WEEE producer registration (EEE category) when volumes warrant; Amazon UK requires the DoC + test report upload for SPDs (restricted electrical category) | Not DG; standard parcel |
| 3 | Earth rods + stud + clamp | BS EN 62561-2 test report (copper thickness, adhesion, corrosion); mill certs; supplier DoC to BS EN 62561-2; drawing | Diameter, length, copper thickness, maker's mark on rod; clamp size range on bag | None (not EEE); BS 7430 is guidance for the installer | Not DG; 1.2 m length exceeds most parcel limits - pallet freight or 2-rod tubes at length surcharge |
| 4 | VRLA 12V 7Ah | IEC 60896-21/22 or BS EN 61056-1 report; UN2800 non-spillable test letter (SP238/A67); SDS; CE/UKCA DoC (Batteries Regs 2008, RoHS); datasheet; UL94 V-0 case statement if claimed | 12V 7Ah, model, terminal type, Pb crossed-out bin, recycling symbol, date code; "Non-spillable battery" on carton; importer | **Battery producer registration** - fire-panel/UPS batteries are normally "industrial" batteries: register directly with the EA, no scheme needed, but you must take back waste industrial batteries free of charge when supplying new ones; above 1 t/yr portable also applies if sold as portable | UN2800 Class 8 but exempt from ADR when SP238 met and terminals protected; mark cartons "non-spillable"; most UK parcel carriers accept with a battery declaration; 2.2 kg each - weight bands and surcharges |
| 5 | Warning-label packs | Material/adhesive datasheet; proof sign-off record; artwork file with BS 7671 514 wording checked against the current amendment | Pack: importer, EAN, country of origin | None | Not DG |
| 6 | SWA gland packs | Supplier DoC to BS EN 62444; drawings; brass material cert; IP66 report (CW) | Thread size on body; pack: size, cable range, importer, EAN | None | Not DG |
| 7 | Resin joint kits | BS EN 50393 (or IEC 60502-4) type-test report; resin SDS (parts A and B, UK REACH/CLP format); CLP classification; supplier DoC; English instructions | CLP hazard pictograms, signal word and H/P statements on the retail box if the resin is classified (most PU resins are: skin/resp. sensitiser); importer; EAN | UK REACH: you are an importer of a mixture - keep SDS, check tonnage band (<1 t/yr = no registration, but SDS and CLP duties apply); poison-centre notification is not required in GB but keep the SDS available | Not DG in retail pouch quantities (confirm from SDS section 14); keep out of air mail if classified UN3082/UN2735 in bulk |
| 8 | Genset filter kits | ISO 19438 / 4548-12 / 5011 media reports; IATF 16949 or ISO 9001; your own cross-reference sheet with the source of each OEM number; fitment test record | Part number + your x-ref on each filter box; "aftermarket, not OEM"; importer | None; **do not use Perkins/Kubota/Yanmar trademarks** beyond nominative "fits" references | Not DG |
| 9 | Hydraulic adaptors | Drawing pack and pressure-rating table; plating test; material cert; ISO 9001; your own catalogue page stating working pressure and that adaptors are components (no PED/pressure-system approval needed below the assembly level) | Size stamped on hex; bag label with size, thread standard, pressure, EAN | None | Not DG |
| 10 | PAT labels | Material datasheet; proof sign-off | Core label with importer, EAN | None | Not DG |

## 4. Recommended first supplier per SKU

1. NiCd sticks: **Shenzhen Tcbest** - Diamond since 2020, third-party audited, 5.0 rating, MOQ 100 at US$4.20 (US$3.50 at 1,000), sample at US$4.20, explicit UN38.3/KC/CE/ISO file and a lab with a temperature/humidity chamber; JYH is the better technical match (purpose-built high-temp EL packs) but its 3,000-pc MOQ only works once the captive firm's volume is proven - run both RFQs and buy the first 100 from whichever supplies the IEC 61951-1 report.
2. Type 2 SPD: **Wenzhou Leeyee** - the only one claiming IEC 61643-11 compliance with a TUV/CB-certified 2P 20 kA model (US$4.50-5.00); est. 2010, 57 staff, 10 export years. Sunpeace (MOQ 5, US$2.90) is the trial-quantity source once its report is in hand.
3. Earth rods: **Shandong Ying Yi** - its spec table already lists 14.2 mm x 1200 mm with 0.254 mm copper and cites BS 7430 / BS EN 50164-2 at US$3.00 (100-999); it is a trading company, so the RFQ asks for the mill. Changdi (250 µm, SGS-verified profile, ISO 9001/14001/45001) is the direct-factory alternative.
4. VRLA 12V 7Ah: **Fujian Minhua (MHB)** - est. 1998, 1,434 employees, Bureau Veritas audit MIC-ASR247395, ISO 9001/14001/45001, IEC 60896/BS 6290 claims, US$4.91-5.77 at MOQ 100; buy the 20-unit trial from Vesion/NPP (MOQ 10, in stock) while Minhua's documents and samples arrive.
5. Warning labels: **Jiangsu Itech** - vinyl warning labels at US$0.02-0.04 each, free samples, 7-10 day production, ISO 9001/SGS; it is a small print broker, so approve a physical proof first.
6. SWA gland packs: **Zhejiang Hongxiang** - est. 2006, Diamond since 2017, BW glands at US$1.00 with MOQ 50; the only candidate that can plausibly pack UK-pattern pairs at a 100-pack first order. Hongdu is cheaper but exported for the first time in March 2026.
7. Resin joint kits: **Zhejiang Johnn** - MOQ 5 at US$2.95, published size table, TUV/CB/ISO claims; cheapest way to run the immersion test. Wellco is the volume source (US$2.45 at 1,000).
8. Genset filter kits: **Hebei Congben** - widest Perkins cross-reference list, IATF 16949 + ISO 9001 + CE claims, 50-100 pc MOQ, 15-day lead time, payment by LC/T/T/PayPal; it can assemble kits rather than sell single part numbers.
9. Hydraulic adaptors: **Ningbo Ningji** - 40,000-piece stock of SAE/BSP/metric adaptors, no MOQ on stock lines, 7-15 day dispatch, ISO 9001:2015, US$0.45-0.47 - the practical way to fill 40 lines in one shipment; Beiteer (US$0.15-0.20) for the high-volume reducers once the rack sells.
10. PAT labels: **Suzhou Guanhua** - Diamond since 2007, est. 2003, Europe its main market, 30% deposit terms published, free sample pack in 2 days, US$1.04-1.80 per roll; the RFQ's job is to move them from thermal paper to PP/vinyl stock. If they cannot, Huibochen (US$3.87, the note's original quote) is the fallback, and a UK short-run printer should be priced for the first 500 rolls.

## 5. Five gaps

1. **No Alibaba or GlobalSources cross-quotes.** Alibaba served its CAPTCHA page and GlobalSources returned HTTP 429 on both attempts; every FOB above is a Made-in-China listing price and several (Jiage VRLA, Zhechi glands, Chuandu rods) are wide ranges. Fix: the RFQs themselves - three firm tier prices per SKU replace the listing ranges within a week.
2. **No supplier has yet shown the UK-critical test report.** Not one listing displays a BS EN 61643-11 report (SPD), a BS EN 62561-2 report (rods), a UN2800 letter (VRLA) or a BS EN 50393 report (joint kits); the CSV records "claimed" vs "not stated" per supplier. Fix: make the report a condition of the sample order, and budget £300-600 per SKU for a UK lab spot-check (e.g. SPD Up/In verification, rod copper-thickness micrograph) before the first listing.
3. **Transaction history and factory/trader status are not verifiable from the platform.** Made-in-China publishes no order volumes; "Audited Supplier" covers licence and premises, not export performance. Four shortlisted suppliers (Sunpeace, Vesion, Hongdu, Henglun) became exporters or Diamond members in 2025-26. Fix: ask each for two export references and a bill of lading to the EU/UK, and use Secured Trading escrow for first orders under US$5,000.
4. **UK fallback prices are list prices, not trade-account prices, and two benches are stale or missing.** The NICEIC label pack (£8.10) is from the 23 Oct note because TLC's warning-label index returned 404; no UK short-run PAT-label printer was reached (pat-labels.co.uk TLS failure); Agriline's FFK093 is out of stock; Yuasa/Enersys distributor trade prices (vs Tayna's £15.50 retail ex VAT) and BES/Electricbase earth-rod prices were not obtained. Fix: open trade accounts at TLC, Tayna/Yuasa, Hydraquip and Agriline and ask for the 30-day account price list - that is also the no-import route for the first pre-sold orders.
5. **Engine-model part numbers and the 40-line hydraulic assortment are buyer assumptions.** The OEM cross-references in RFQ 8 are typical for Perkins 1103/1104, Kubota V-series and Yanmar TNV gensets but were not verified against a parts book this session, and the 40-line rack in RFQ 9 is a reasoned starter list, not a depot's usage data. Fix: confirm the filter numbers with one generator PPM firm's last 12 months of service sheets, and let the first plant-hire depot mark up the 40-line list before the PO.
