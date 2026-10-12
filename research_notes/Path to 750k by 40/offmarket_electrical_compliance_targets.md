# Off-market targets: electrical compliance / testing / critical-power maintenance (London & South East)

Companion CSV: `offmarket_electrical_compliance_targets.csv` (102 rows, scored 0–100, sorted by score).
Date of pull: 8 Oct 2026. Source: public Companies House web pages only (advanced search, officers pages, PSC pages, filing-history accounts PDFs). No API key, no paid data.

## Headline

The screen as specified (owner b.1955–70 who is PSC, 1–3 directors, NA £50–600k, 3–20 staff, London/SE, inc. 2000–15, compliance/testing/critical-power name) produces **6 firms that pass every stage**, plus **2 cash-rich one-man firms** that pass on net assets but have no staff to retain, out of 370 unique companies pulled. The reason is structural, not a search gap: firms whose *names* say "testing / PAT / EICR / compliance" are overwhelmingly one- or two-person micro-entities with net assets under £25k. The firms of the size the buyer wants (EBITDA £80–170k, a manager who stays) almost all trade under generic names ("X Electrical Services", "Y Power", "Z Building Services") and describe their compliance work only on their websites. The next tranche should therefore screen on **size and owner age first** (SIC 43210/71200, London/SE, inc. 2000–15, then officers DOB, then accounts) and treat the compliance keyword as a *website* filter applied afterwards, not a company-name filter.

## Method (150 HTTP fetches, the agreed budget)

1. **Advanced search** (`/advanced-search/get-results`), active companies, incorporated 1 Jan 2000–31 Dec 2015, UK-wide, name-contains keyword. The form accepts one SIC code per query (a repeated `sicCodes` param throws "value.trim is not a function"), so most queries were run without a SIC filter and SIC was recorded per company from the result row instead. 42 result pages across 32 keyword queries: electrical testing (3 pp), eicr (0 hits), pat testing (2), electrical compliance, electrical inspection(s), periodic inspection (0), thermographic, thermal imaging, emergency lighting, generator (SIC 33140 and 43210), generator services/maintenance, ups systems/ups power, uninterruptible, standby power, switchgear (2), critical power, power systems (4), power services (1 of 6 pp), electrical maintenance (3), testing and inspection, electrical safety (2), safety testing, compliance (SIC 71200), power protection, lightning protection, electrical certification (0), m e maintenance.
2. **Location filter** on the registered-office string: Greater London (by county word or postcode area), Surrey, Kent, Sussex, Hampshire, Berkshire, Buckinghamshire, Hertfordshire, Essex, Oxfordshire; Middlesex kept; Bedfordshire/Luton kept but scored 5/10 on location.
3. **Name-noise filter** (manual regex): removed printing, gaming, environmental, renewable, automotive, holding/group vehicles (Intertek, Sureserve, UKPN, etc.).
4. **Officers pages** for the 51 most relevant names: parsed current (non-resigned) directors, month/year of birth, appointment date. Age pass = any current director born 1955–1970.
5. **Filing history (accounts category)** for the 24 age-passes plus 3 near-misses born 1951–54: latest accounts type and date, PDF link.
6. **Accounts PDFs** (21): all are image scans with an empty text layer, so OCR'd with tesseract 5.3.4 at 300 dpi (`pdftoppm` → `tesseract --psm 6`), then net assets, cash, creditors < 1 yr, employees, fixed assets, debtors read from the balance sheet and notes. Figures were hand-checked against the OCR text; a few OCR glitches (e.g. "95.679") were corrected.
7. **PSC pages** for the top 5 by size fit (budget allowed no more).
8. Scoring: owner age 40 (b.1955–70 = 40; b.1950–54 = 32; b.1971–74 = 20; younger = 0; unknown = 15), size fit 30 (NA £50–600k and 3–20 staff = 30; NA in band but ≤2 staff = 18; NA < £50k with ≥3 staff = 12; tiny = 3; dormant = 0; unknown = 10), keyword strength 20, London/SE 10. Search-only rows are capped at 55; dormant/overdue/NIL-employee rows capped at 30.

## Counts at each stage

| Stage | Count |
|---|---|
| Result rows pulled (42 pages) | 399 |
| Unique companies, active, inc. 2000–15 | 370 |
| Registered office in London/SE (incl. Beds edge) | 121 |
| After name-noise filter | 102 (all in CSV) |
| Officers pages pulled | 51 |
| ≥1 current director b.1955–70 | 24 (+3 near-miss b.1951–54, +2 b.1971–72) |
| Of those with 1–3 directors | 23 (Bacon Lightning has 4) |
| Accounts pulled and OCR'd | 21 (6 skipped: 4 dormant, 2 with accounts overdue since 2019/2021) |
| Net assets £50–600k | 8 |
| …and 3–20 employees (full pass) | 6 |
| PSC confirmed = director | 5 (the rest inferred from sole-directorship) |

## Top 20 (score, why)

Full pass (owner age, size, staff, location):
1. **Critical Power Supplies Ltd** (07024862, Thame, Oxon; SIC 43210/46520) — 94. NA £270k, cash £453k, 11 staff (14 prior yr), debtors £1.03m / creditors £1.34m so turnover is probably £3–6m: UPS and generator sales plus service. PSC/founder Jason Koffler b.1970 (56); his wife (b.1960) was appointed director in 2026, which often precedes a sale or restructuring. Best strategic fit on the list (critical power, recurring service) but likely **above** the £200–400k EV band; worth an approach anyway because the buyer's band could cover a service-division carve-out or a vendor-financed deal.
2. **McNeilly Electrical & Maintenance Services Ltd** (03964068, Breachwood Green, Herts; 43210) — 94. Founder David McNeilly b.1964 sole director; he and wife are PSCs. NA £106k, cash £109k, creditors £54k, 3 staff, bank loan £10k, turnover-recognition note refers to "electrical installations". Classic owner-managed, 26 years old, debt-light.
3. **The Electrical Maintenance Company Ltd** (04340888, Chelmsford, Essex; 43210) — 94. Michael Donnelly b.1957 (69) founder-director since 2001; PSCs are Michael and Wendy Donnelly. NA £118k, cash £79k, 4 staff, tax/NI creditor £56k. **Son (b.1990) and a colleague (b.1992) were made directors in 2025** — succession is already in motion; an approach could be to fund the family buy-out or buy with the son staying as manager.
4. **Power Systems Service Ltd** (07753202, Guildford, Surrey; 82990) — 90. Craig Arnold b.1969 sole director. NA £551k (top of band), fixed assets £401k, debtors £258k, cash £95k, creditors only £28k, 3 staff; prior year had £650k debtors and £623k creditors, so project-driven. Needs a website check to confirm it is generator/UPS service rather than something else.
5. **Switchgear Technology Ltd** (05173031, Bromley, Kent; SIC 27900 manufacture) — 90. Luke Fagan b.1960 sole PSC (co-founder Hilton exited 2022); two directors b.1995/96 appointed 2024, which looks like an internal succession/MBO being set up. NA £135k, cash £151k, debtors £255k, stock £33k, creditors £331k, 9 staff. The biggest "real business" on the list in headcount; switchgear build + service/maintenance.
6. **M.B. Power Services (Essex) Ltd** (04105556, Hockley, Essex; 43210) — 86. Karl Burridge b.1963 PSC and brother/son Brent b.1970; both appointed 2015 into a company incorporated 2000 (probably acquired then). NA £96k, current assets £117k, creditors £37k, 4 staff. Micro-entity so no cash figure.

Net assets fit, no staff (buy the contract book, not a business):
7. **B S Electrical & Testing Ltd** (07042291, Southampton; 43210) — 83. Bahadar Singh Takhar b.1956 (70), sole director, NA £106k, creditors £216, 1 employee. Cash-rich shell-like; obvious retirement seller, but there is no manager to keep.
8. **Concept Electrical and Maintenance Ltd** (05113065, Basingstoke, Hants; 43210) — 82. Anthony Simmons b.1965, sole director, NA £72k, current assets £89k, 1 employee, £24k long-term creditor (probably BBL/director loan).

Age fit but too small to be a business (contact for a tuck-in of contracts only):
9. Bacon Lightning Protection & Maintenance Ltd (09157590, Maldon, Essex) — 74; directors b.1957 and b.1966 but 4 directors; accounts not pulled.
10. Connect PAT Testing Ltd (06654293, Harrow) — 73; Levy husband & wife b.1962/65, NA £4k, 2 staff.
11. J.R.B. Electrical Testing Services Ltd (05348921, Chelmsford) — 73; Morgans b.1964/65, NA £557.
12. Mistry Electrical Testing Ltd (08895196, Harrow) — 73; b.1968, NA £1.4k.
13. PAT Testing Services Ltd (05637482, Ealing) — 73; Emmanuel Borg b.1966, NA £23k, 1 staff.
14. Three Counties PAT Testing Ltd (05665950, Tring) — 73; b.1969, NA £4k.
15. Reeds Electrical & Safety Ltd (06380319, Haywards Heath) — 67; Reeds b.1967/69, net liabilities £40k.
16. Etheringtons Electrical Testing Ltd (06265100, Guildford) — 65; George Dunsmuir b.1954 + son b.1984, NA £1k, 2 staff.
17. JMC Electrical Testing Services Ltd (06427184, Harlow) — 65; b.1954, NA £4k, one-man.
18. PAT Inspection & Testing Ltd (04870639, Leigh-on-Sea) — 65; Colin Fitzgerald b.1951, NA £350, one-man.
19. Oceanas Lightning Protection Ltd (09265710, Polegate) — 63; Graham Boyce b.1958, NA £4k, 2 staff.
20. PKS Power Systems Ltd (04497973, Hitchin) — 63; Longstaffs b.1962, net liabilities £18k, 2 staff.

Excluded after filing check (do not approach): Lowery Power Systems, Generator Power Systems (Braintree), Primec Compliance, Inotec Emergency Lighting (all filing dormant accounts); UK Electrical Safety Ltd (Redhill) and Electrical Safety Services (GB) Ltd (accounts overdue since 2021 and 2019 — likely heading for strike-off). EPT (Electrical Portable Testing) and Alrita Compliance file NIL employees.

## Natural consolidators / too big (names only, from the same pulls; accounts not pulled, flagged by group ownership or scale signals)

1. Intertek Testing and Inspection Services UK Ltd (Brentwood) — Intertek plc.
2. Sureserve Compliance Electrical North Ltd / Sureserve Compliance Electrical Holdings Ltd (London) — Sureserve group (Cap10).
3. UK Power Networks Services Holdings Ltd (London).
4. Uninterruptible Power Supplies Ltd (Hook, Hants) — Kohler group; SIC 70100 head-office entity.
5. Critical Power Supplies Ltd (Thame) — on the target list above, but at 11–14 staff and ~£1m debtors it is also the most likely local acquirer of the smaller firms.
6. Bowman Power Systems (UK) Ltd (Southampton).
7. Microvast Power Systems UK Ltd (Swanley) — subsidiary of Microvast Inc.
8. Enegen Power Systems Ltd (Portsmouth).
9. Renewable Power Systems Holdings Ltd and sister companies (Bedford) — group structure.
10. Acquiesce Environmental Compliance Ltd (Crawley) — compliance-services roll-up signal (2015 inc., SIC 71200).
Also present in the pulls but not competitors: Electrical Safety First Ltd (the charity), Gordon Murray Advanced Power Systems (automotive), Proton Motor Power Systems (fuel cells).

## Gaps and caveats

- **Turnover is never disclosed.** All 21 sets of accounts are micro-entity, total-exemption-full or abridged, with no P&L filed. EBITDA cannot be read from Companies House for any firm in this band; it must come from the owner conversation or from a proxy (staff count × £80–120k revenue per head for testing/maintenance firms; debtors × ~5–6 for firms with 60-day terms).
- **Cash at bank** is only visible in full/TEF accounts (6 of 21); micro-entity balance sheets show "current assets" only. The CSV marks these n/d.
- **PSC** was confirmed on only 5 companies (budget). For sole-director companies the CSV says "inferred (sole director)"; for 2–3-director firms it says "not checked". No corporate-parent PSC was seen in any of the 5 checked, and none of the 51 officer-screened firms shows a corporate director.
- **Websites** were not searched (the 150-fetch budget was consumed by Companies House). The top 8 need a one-search website check before any letter goes out — in particular Power Systems Service Ltd (SIC 82990 is uninformative) and M.B. Power Services.
- **Age data is month/year only**; "oldest director" is used for scoring, but for Critical Power Supplies the owner is the younger director (b.1970) and the b.1960 director is a 2026 appointee.
- **Search coverage**: keyword-in-name search misses firms with generic names, which is where most of the right-sized businesses sit. "EICR", "periodic inspection" and "electrical certification" returned zero 2000–15 incorporations; the word "generator" alone was not run UK-wide without a SIC filter (too broad). "Power services" (120 results) and "electrical maintenance" (59) were only partly paginated (1 of 6 pages and 3 of 3 respectively).
- **OCR**: every accounts PDF was a scanned image. Figures were read from tesseract output and spot-checked; treat ±£1k differences as OCR noise, and re-read the PDF before quoting a number to a seller.
- **Search-only rows (51)** in the CSV have no officer or accounts data and are capped at 55 points; they are a queue for the next tranche, not conclusions.

## Suggested next tranche (another ~150 fetches)

1. Officers + accounts for the 51 search-only rows with keyword score ≥ 4 (about 30 firms, ~90 fetches).
2. Size-first search: SIC 43210, London/SE counties via `registeredOfficeAddress`, inc. 2000–15, and read officers for firms whose names contain "services", "contractors", "building services", "M&E", "facilities" — then website-check for EICR/PAT/emergency-lighting/thermography content.
3. Website + Google check of the top 8, and PSC pages for M.B. Power Services and Power Systems Service.
