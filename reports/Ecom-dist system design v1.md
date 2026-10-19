# E-commerce / distribution: lane evaluation and system design (v1)

*Purpose: pick the lane, so the business does not drift from candles to hydraulic hose, and design it as a system that Dale, Manuel, Meg and the Philippines team can run on about three days a week of Dale's time. Target set by Dale: £300–400k revenue at 15–20% net, i.e. £50–80k profit, as the engine or the floor under the plan.*

## 1. What "reselling" actually offers: the five lanes

| Lane | What it is | Who buys | Demand comes from | Cash shape |
|---|---|---|---|---|
| A. Personalised, made-to-order consumer goods | Design-led products made by print/production partners on order; the Etsy model | US consumers, gifting | Marketplace search (Etsy, Amazon.com) | No stock. Cash positive on day one. |
| B. B2B consumables and spares to trade | Import or buy-in industrial lines; sell to contractors, service firms, fleets | UK trade: electricians, generator and HVAC service firms, plant hire | Amazon Business, eBay, trade accounts, the acquired firm's own contractors | Stock: £30k order → £35–39k landed, 13–30 weeks tied up |
| C. Private-label consumer goods (FBA) | Source a product, brand it, sell on Amazon | Consumers | Amazon search plus paid placement | Stock plus ad spend; 20% median margin |
| D. Exclusive agency distribution | Become the UK distributor for one overseas brand; sell to retailers and installers | Retailers, installers | The brand's pull plus your sales | Stock, credit to customers, a rep's time |
| E. Generic drop-ship / arbitrage | List others' stock, pass orders through | Consumers | Price | No stock, no moat, 5–10% margin |

## 2. Scoring against Dale's criteria

Scores 1–5. Evidence in brackets points to the research notes.

| Criterion | A. Personalised MTO | B. B2B consumables/spares | C. Private label FBA | D. Exclusive agency | E. Drop-ship |
|---|---|---|---|---|---|
| Fun / fits nature and talents | 4 (proven; design + ops coordination; no cold calls) | 4 (parts, systems, data; sales by email and trade price list) | 2 (ad optimisation is the job) | 3 (relationship-heavy with the principal) | 1 |
| Numbers: can it reach £300–400k at 15–20% | 3 (your record ≈ £130k/yr revenue; needs 2–3× with new lines) | 4 (trade consumables 30–35% GM; £350k revenue is 20–30 accounts plus marketplace) | 2 (median margin 20% before ads) | 3 (depends on one brand) | 1 |
| Likelihood of success | 4 (ranked shops, team, 1k reviews; 28–44% to £5k/mo in year 1, 80–90% to £30k/yr by 2034) | 3 (import lines up 14–19% y/y; needs the Amazon-ops assumption to hold) | 2 (70% of sellers under $60k revenue) | 2 (few brands available; long to land) | 1 |
| Can a system be built | 5 (already exists: designers, partner, listings, service) | 4 (stock, listing, trade account, delivery, credit control; standard) | 3 | 3 | 4 |
| Can Meg and Manuel be included | 5 (Manuel built it) | 4 (ops and listings transfer; sales is Dale) | 3 | 2 | 3 |
| Uncorrelated with the other lane | US consumer, gifting seasons, Etsy/Amazon.com platform risk | UK trade, maintenance cycles, Amazon Business/direct | Correlated with A (consumer, Amazon) | Correlated with B | Correlated with everything |
| Synchronises with the firm purchase | 2 (separate customers) | 5 (the firm's contractors and compliance customers are the buyers) | 1 | 3 | 1 |
| **Total (of 35)** | **27** | **28** | 14 | 18 | 11 |

Read: A and B are the two lanes. They score almost equally, they are genuinely uncorrelated (different country, customer, platform, season, cash shape), and together they cover both halves of your record: A is what you have already done, B is where the import and services data points. C, D and E are out: C is correlated with A and worse on margin; D is a later move once B has customers; E has no edge.

## 3. The chosen system: two lanes on one backbone

```
                 ┌────────────────────────── BACKBONE (one company, one P&L, one weekly review) ──────────────────────────┐
                 │  sourcing & supplier terms · listing engine · order desk · fulfilment & returns · bookkeeping · dashboard │
                 └──────────────┬───────────────────────────────────────────────────────┬───────────────────────────────┘
                                │                                                       │
            LANE A: personalised made-to-order (US)                 LANE B: B2B consumables & spares (UK trade)
            Etsy (2 ranked shops) + Amazon.com + eBay               Amazon Business + eBay + trade price list/accounts
            Owner: Manuel (ops/listings/service)                     Owner: Dale (sales, lines, pricing); Meg (ops/accounts)*
            Demand: marketplace search                               Demand: marketplace + the firm's contractors + emailed price list
            Cash: none tied; paid before production                  Cash: stock £15–40k; 30-day terms to accounts
            Kill rule: line < 25% GM after fees for 2 months         Kill rule: SKU not reordered within 13 weeks; account > 60 days late
```
*Meg's role to be confirmed by Dale.

### 3.1 Lane A: what changes from the old shops

- Shop location set to the UK with US shipping origin and the production partner disclosed on every listing (the honest configuration; the one thing that ever killed a shop of yours was a platform review).
- Two to three new made-to-order lines per quarter, chosen from Etsy and Amazon search demand, not the pet niche. The shops' 1,000-review ranking is the asset; new lines ride it.
- Mirror every winning SKU on Amazon.com and eBay within 30 days. Never one platform.
- Manuel runs it. Your time: one review a week, line selection once a quarter.

### 3.2 Lane B: the trade line

- Start with one category that the compliance firm's world buys and that the import data likes: electrical compliance consumables and spares (test-equipment accessories, labels and certificates, earthing and surge kit, cable glands, emergency-lighting batteries and lamps, generator filters and spares). Data: generator spares imports up 14% y/y, 1,070 importers; earthing/surge scored 80; filtration a £2bn import market.
- Three channels in order: (1) Amazon Business and eBay listings to read demand and sell to sole traders, (2) a trade price list emailed to 30–50 firms with 30-day accounts, (3) the acquired firm's own subcontractors and customers once a purchase completes.
- Pre-sell before stocking: list with a 10–14 day lead time; buy the first pallet only against orders. Second pallet only after five reorders.
- Your time: line selection, supplier terms, the price list and account opening (email, not calls), one weekly review. Ops, listings and order desk sit with the team.

## 4. The numbers: how £350k at 15–20% is built

| | Lane A | Lane B | Total |
|---|---|---|---|
| Revenue target, year 2–3 | £150k | £200k | **£350k** |
| Gross margin after product and partner cost | 45% → £68k | 32% → £64k | £132k |
| Marketplace fees and payments (A ~12%; B ~10% on the marketplace share) | −£18k | −£10k | −£28k |
| Ads (A only, capped at 5% of revenue) | −£8k | — | −£8k |
| Fulfilment, 3PL, returns, packaging (B stock handling) | −£2k | −£12k | −£14k |
| Team: Manuel, Meg, PH ops | −£14k | −£10k | −£24k |
| Software, insurance, accountancy, misc | −£3k | −£4k | −£7k |
| **Net before Dale's draw and tax** | **£23k (15%)** | **£28k (14%)** | **£51k (15%)** |

So £350k at 15% is £51k, at 20% it is £70k. The 20% case needs lane B's trade accounts (no marketplace fee) to be half of its revenue and lane A's ads below 5%. Working capital for lane B at £200k revenue with 6 stock turns: about £25–30k of stock plus £15k of debtors. Lane A needs none.

Against the goal: £50–70k from this system plus two contracting blocks (£38k net) clears £80k. If the firm is bought, lane B's revenue is partly captive and the two businesses share an order desk and bookkeeping.

## 5. Roles and the weekly cadence

| Who | Owns | Weekly | Quarterly |
|---|---|---|---|
| Dale (≤ 3 days/wk, most of it on the firm search) | Lane B sales and lines; lane A line selection; cash and kill rules | Monday 60-minute review of the dashboard: revenue by SKU, margin by lane, stock cover, debtors, ad spend; decisions only | Choose next quarter's 2–3 lines per lane from the demand data; supplier renegotiation |
| Manuel | Lane A end to end: listings, production partner, customer service, returns | Daily order desk; listing refreshes; weekly numbers into the dashboard | New-line launches; Amazon.com mirroring |
| Meg (to confirm) | Lane B operations: stock, trade accounts, invoicing, credit control, supplier POs | Daily order desk for B; weekly debtors and stock report | Account reviews; price-list updates |
| PH team | Design, listing copy and images, data entry, first-line service | Throughput on tickets | — |
| Claude (this chat) | Demand research per quarter; margin sheets per line; dashboard build; supplier shortlist; pricing; weekly numbers analysis | Reads the numbers before Monday; flags kills and reorders | Quarterly line research for both lanes |

## 6. The stack (keep it boring)

- Listings and orders: Etsy, Amazon Seller Central (US and UK/Business), eBay; one multi-channel tool to sync stock and orders (e.g. Linnworks or a cheaper equivalent) once lane B has more than 20 SKUs.
- Fulfilment: lane A via the production partner (no change); lane B via a UK 3PL from pallet one (£3–6.50 per pallet per week in the playbook), not your spare room.
- Money: one Ltd, Xero, a VAT registration (reverse-charges Etsy fees and recovers VAT on lane B stock; lane A US sales are outside the scope of UK VAT), one business account per lane for visibility.
- Dashboard: a single sheet fed weekly, by lane and by SKU: revenue, gross margin, fees, ads, stock weeks of cover, debtors over 30 days, cash. I build and maintain it.

## 7. Rules that keep it a system

1. No new lane. New lines yes, new lanes no, until both lanes clear their targets for two consecutive quarters.
2. A line is killed when it misses 25% gross margin after fees for two months (A) or is not reordered within 13 weeks (B).
3. Stock is bought only against pre-sold demand or a demonstrated reorder rate; the second pallet needs five reorders.
4. Cash cap for lane B stock: £40k until revenue passes £150k.
5. Every SKU on at least two platforms within 30 days of its first sale.
6. Dale's hours on this: a weekly review and a quarterly line choice. If it needs more, the system is wrong, not the hours.

## 8. 90-day plan

| Weeks | Lane A | Lane B | Backbone |
|---|---|---|---|
| 1–2 | Shop-location fix, partner disclosure, VAT and Ltd set-up decisions | Demand research: 20 candidate SKUs from Amazon Business/eBay sold counts and the import data; margin sheet per SKU | Xero, one dashboard sheet, roles agreed with Manuel and Meg |
| 3–6 | Launch 3 new made-to-order lines inside the two shops | Pre-sell listings for 10 SKUs with 10–14 day lead; email a one-page trade price list to 30 firms; first pallet only against orders | Weekly review starts |
| 7–10 | Kill the weakest line, double listings on the best; mirror to Amazon.com and eBay | Reorder the SKUs that sold; open the first trade accounts; 3PL in place | First margin review by lane |
| 11–13 | Read the number: on track for £5k/month across both lanes by month six? | Second pallet only on five reorders | Decide quarter two's lines |

## 9. What I need from Dale to turn v1 into the working plan

1. Meg: who she is, hours available, what she is good at.
2. Manuel: hours per week available, current pay basis, which parts of lane A he ran end to end.
3. Lane A today: which lines are live, orders per month, unit cost and sell price from the current print partner, peak-month profit from the old run.
4. Lane B: whether to start the demand research now (one agent, roughly a day) and whether the first category is the compliance-consumables set above or the plant/hose set from the import ranking.
5. Cash you will allocate to lane B stock in year one (the rule above says £40k cap; you may want less).
