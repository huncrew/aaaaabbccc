# Lane B: cheap-end UK price check (20 Nov 2026)

Purpose: test the challenge that big players already sell the shortlisted trade lines. Six web searches, prices as shown in search results (not fetched pages; Amazon and eBay listings did not surface). Earlier benchmarks came from one wholesaler's list price (TLC Direct, Hydraquip), which overstated the price a new seller must beat.

| Line | Earlier benchmark (ex VAT) | Cheapest found (ex VAT unless stated) | Source | Landed import | Read |
|---|---|---|---|---|---|
| Earth rod 5/8in x 4ft | TLC £10.50 rod | Rapid £6.04 (out of stock); Screwfix £9.44 inc VAT = £7.87 | rapidonline.com/unistrand-5-8-4ft-copper-earth-rod-28-4772 ; screwfix.com/p/pro-fix-earth-rod-5-8-x-4-/87633 | £2.82 | Benchmark ~35% too high. Long heavy parcel. Marketplace single: no. |
| Type 2 SPD 1P+N | TLC BG £18.90 | Toolstation Axiom £16.66 (out of stock); Screwfix MK £26.99 inc VAT = £22.49 | toolstation.com/bg-type-2-single-phase-surge-protection-device-spd/p79903 ; screwfix.com/p/mk-sentry-h6821s-1p-n-type-2-spd-40ka/111YW | £4.15-4.62 | Benchmark holds. Open question: will electricians fit an unknown brand in a branded board. |
| 12V 7Ah VRLA | Tayna Yuasa £15.50 | RS Landport £14.49 | uk.rs-online.com/web/p/lead-acid-batteries/0297041 | £4.61-5.41 | Benchmark holds at distributors; marketplace cheap end not seen. 2kg+ parcel. |
| NiCd 4.8V 4Ah emergency-lighting stick | TLC £19.95 | TradeSuperstore £33.59-41.29; Rapid Emmerich £39.00 | tradesuperstoreonline.co.uk ; rapidonline.com/emmerich-48d4000s-emergency-lights-battery-4-8v-4000mah-64-5819 | £6.92 | Gap is larger than modelled. Fitment-specific. Strongest of the six. |
| PAT PASS labels, roll of 500 | TLC £13.50 | Tester £7.29 (VAT basis unclear); eBay 1,000 for £17.00 | tester.co.uk/electrical-electronic/pat-testing-equipment/pat-labels ; ebay.com/itm/111044770891 | £0.96-1.66 | Benchmark ~45% too high. Low ticket, MOQ 1,000 rolls. |
| Hydraulic adaptor 1/2in BSP male/male | Hydraquip £2.34-3.34 | L&S Engineers £1.65; HTS Spares £2.28 | lsengineers.co.uk ; htsspares.com (hydraulic BSP male/male adaptors) | £0.18-0.46 | Benchmark ~30% too high. Pennies per unit; served by established part-number catalogues. |

Conclusions
1. Every line is already sold by large and small UK sellers. None is unserved.
2. In 3 of 6 checks the cheap-end price is 30-45% below the benchmark used in `laneB_trade_candidates` and `laneB_rfq_pack`. Margins in those files are overstated for those lines.
3. The import-cost advantage is real but is the same advantage existing importers hold; it is not an edge by itself.
4. The lines where the gap survives are fitment-specific (battery packs by luminaire, filter kits by engine), where the cross-reference catalogue is the barrier.
5. Not verified here: Amazon and eBay prices and sold volumes. Those need the browser findings sheet (`line_selection/`).
