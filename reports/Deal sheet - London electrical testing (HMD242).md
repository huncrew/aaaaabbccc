# Deal sheet: London electrical testing & maintenance company (Hornblower ref HMD242)

Live listing, 19 Oct 2026. Source: https://hornblower-businesses.co.uk/business-for-sale/electrical-testing-maintenance-and-installation-services-company-hmd242/ . Comparators from the SE scan (`research_notes/Path to 750k by 40/listings_services_se_scan.csv`). Deal mechanics as in `model/mc_model.py` (vendor note 4 yrs @ 5%, bank/GGS loan 10 yrs @ 11%, £20k deal costs, 10% of price as working-capital reserve, PG ≈ 35% of bank facility). Script: `model/deal_sheet_p1.py`.

## 1. What is for sale (as stated by the broker)

| Item | Stated |
|---|---|
| Business | NICEIC Approved Contractor; electrical testing (EICR, PAT), maintenance, installation, safety & security systems. London. |
| Customers | Private landlords and property managers (residential portfolios), commercial: industrial premises, retail chains, arts/leisure venues, "high-profile brands". Concentration not stated. |
| Repeat custom | "around 90%"; regular testing is legally required, so it recurs on a calendar. |
| Delivery model | "uses a network of qualified electrical contractors" (subcontract engineers; fixed staff count not stated). |
| Financials (YE 30 April) | 2020: £480k rev / £181k adj EBITDA (38%) · 2021: £461k / £141k (31%) · 2022: £412k / £115k (26%) · 2023: £406k / £129k (32%) · 2024: £498k / £167k (33%). Gross margin 47–55%. |
| Adjusted EBITDA basis | "Directors' replacement cost is included" (i.e. a salary for someone doing the directors' job has already been deducted; verify the figure). |
| Price | Offers invited. |
| Not stated | Employee count/roles, manager, owner hours, premises/rent, reason for sale, handover, vehicles/assets, customer concentration, 2025 figures. |

Read-across: a subcontract-engineer compliance book with 90% repeat and a replacement-cost adjustment is the closest live match to the plan. The 2020–23 dip (−36% EBITDA to the 2022 trough) is the thing to understand before pricing.

## 2. Money in, finance, and what is left for you

| Scenario | Price | Vendor note | Bank loan | **Cash at completion** | PG | Debt service yrs 1–4 | Pre-tax to you yrs 1–4 | After tax (31%) | Pre-tax yrs 5–7 | After tax |
|---|---|---|---|---|---|---|---|---|---|---|
| A. Broker pricing: 3.0× on 2024 £167k, 35% VN | £500k | £175k | £195k | **£200k** | £68k | £83k | £84k | £58k | £134k | £92k |
| **B. Negotiated: 2.3× on 5-yr average £147k, 50% VN** | £337k | £168k | £101k | **£121k** | £35k | £65k | £82k | £56k | £129k | £89k |
| C. Seller-funded: 2.3×, 70% VN | £337k | £236k | £61k | **£94k** | £21k | £77k | £70k | £48k | £136k | £94k |
| D. B, but EBITDA falls to the 2022 level (£115k) in yrs 1–2 | £337k | £168k | £101k | £121k | £35k | £65k | £50k (yrs 1–2) | £35k | £129k | £89k |
| E. D, and you hire an ops manager at £40k on top (3 days/wk) | £337k | £168k | £101k | £121k | £35k | £65k | £10k (yrs 1–2), £42k (3–4) | £7k / £29k | £89k | £62k |

7-year after-tax cash to you: A £509k on £200k in; B £494k on £121k; C £474k on £94k; D £450k; E £257k. In all cases you still own the business (indicative resale 2.5× EBITDA ≈ £365–415k).

Against the £80k-a-year minimum: B clears it pre-tax from year 1 (£82k) and after tax from year 5 (£89k). Years 1–4 after tax are £56k, so the gap to £80k is one to two contracting blocks a year until the vendor note is repaid. E (stress plus a hired manager) does not clear £80k until the note is gone; that is the scenario the price and the DD have to protect against.

## 3. Practical side

- **Employees.** Not stated. The "network of contractors" wording suggests a small core (owner/directors, scheduler/admin, possibly 1–2 employed engineers) with subcontract electricians doing most tests. Ask for the org chart, PAYE headcount, and the subcontractor list with 12-month spend per sub.
- **Manager.** Not stated. The replacement-cost adjustment means the broker has priced in paying someone to run it. Either an existing scheduler/ops person can step up (ask), or you hire one (scenario E shows the cost if that is on top of the stated EBITDA rather than inside it).
- **Your involvement.** Sales and relationships (landlords, property managers, FM firms), pricing, subcontractor terms, the annual test calendar. No tools, no certificates: you cannot sign an EICR and do not need to. Realistic: 2–3 days/wk in year 1 during handover, 1–2 days/wk from year 2 if an ops person is in place. Health: the subcontract model means a flare does not stop the work.
- **Premises.** Not stated. Compliance firms of this size usually run from a small office or home; if there is a lease, get the terms (rent appears as a cost already inside EBITDA).
- **Assets.** Vehicles, test equipment, software (scheduling/certification portal) not stated. Ask what transfers.

## 4. Questions to the broker before any offer

1. 2025 and YTD 2026 management accounts; the directors' replacement cost figure used; any other add-backs.
2. What happened in 2021–23 (EBITDA −36% to the trough): lost client, COVID, pricing, owner illness?
3. Revenue by customer for the top 10; share of revenue on annual/multi-year test contracts vs ad-hoc installation.
4. Headcount (PAYE), roles, salaries; subcontractor list and spend; who schedules the work day to day.
5. Owner's hours and role; willingness to stay 6–12 months on a consultancy; vendor-note appetite and term.
6. Lease, vehicles, equipment, software; NICEIC registration transfer (the Qualified Supervisor must remain or be replaced).
7. Reason for sale and timetable.

## 5. Comparators at the same negotiated terms (2.3×, 50% vendor note)

| Firm | EBITDA basis | Price | Cash in | Pre-tax to you yrs 1–4 | Note |
|---|---|---|---|---|---|
| P6 London/East England, £598k T/O | £175k EBITDA | £402k | £141k | £98k | Shareholders willing to remain = manager solution built in; HE contract 2 yrs left; larger. |
| **HMD242 London (this sheet)** | £147k 5-yr avg | £337k | £121k | £82k | Best-documented; 90% repeat; subcontract model. |
| P2 London/SE, £306k T/O | £103k adj EBIT, less £45k engineer | £237k | £96k | £13k | 34% margin on £306k implies the owner is on the tools; after replacing them, little is left for debt. Only works at a lower price or as a bolt-on. |
| P3 Buckinghamshire, £215k T/O | £110k adj EBIT, less £50k electrician | £253k | £110k | £14k | 50%+ margin means the owner is the business. Same conclusion as P2. |

Ranking for a first purchase: P6 or HMD242. P2 and P3 are bolt-ons for later, priced on EBITDA after a replacement engineer, not on the broker's adjusted EBIT.

## 6. How this sits with the plan

- Cash in £94–121k on the negotiated structures is inside the "£80–140k above the floor by 2028–29" planning number; the PG (£21–35k) is well inside the risk pot.
- Years 1–4 after tax (£48–56k) plus 1–2 contracting blocks a year clears £80k; from year 5 the firm alone does.
- The ecommerce/distribution line runs alongside and, if the firm is bought, its B2B parts supply has an immediate customer in the firm's own subcontractors.
