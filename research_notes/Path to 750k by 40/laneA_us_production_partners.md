# Lane A: US production partners for personalised wall art and gifts

Date: 2026-10-30. Companion file: `laneA_us_production_partners.csv` (46 rows, one per partner × product format). Every cost in the CSV carries its source URL, the date it was seen (2026-10-30) and a `cost_status` flag: Verified, Estimate, Stale or Blocked. Budget: about 92 searches and fetches against a target of about 100.

Context: the seller is UK-based and sells to US buyers on Etsy. Every item must be made and shipped inside the US. Price points come from `laneA_personalised_candidates.md/.csv`: poster 18x24 $44.95, canvas 16x20 $89.95, framed 16x20 $119, acrylic $129, address/metal sign $129, ornament $24.95, engraved cutting board $49.95. Where the shortlist has no price, the US Etsy market median from RankHero is used: metal print $85, gold foil print $21.03, custom metal sign $48.91, personalised ornament $17.98.

## 1. Method, and what was blocked

| Source | Result | Used for |
|---|---|---|
| **Printful public catalogue API** (`api.printful.com/products/{id}`) | **Worked.** Live variant prices for every wall-art product. These match the third-party Aug-2026 table to the cent. | All Printful costs |
| Printful v2 availability API (which facility makes what) | **401: needs OAuth.** Not pursued. | — |
| printful.com/shipping | Worked | Printful US shipping and timings |
| **Printify public catalogue API** (`api.printify.com/v1/catalog/...`) | Answered about 15 calls without a token (provider lists, provider locations, two shipping tables), then returned **"Unauthenticated"**. Stopped there; no workaround tried. | Provider names and cities, some shipping |
| printify.com/shipping-rates/{provider}/ | **Worked** (server-rendered HTML) | Printify shipping per provider |
| Printify product pages, listingview.io mirror | Client-side rendering, so no prices in HTML | Only the "From USD" prices visible in search snippets |
| lumaprints.com/pricing | **Worked.** Full trade price tables | All Lumaprints costs |
| Lumaprints shipping | Calculator only, nothing published | **Estimated** (Printful's rate for the same size used as a proxy) |
| prodigi.com product pages and product PDFs | Worked for specs, US-lab availability and "From" prices. Size prices sit behind "Get pricing", which needs a login. | Foil specs; foil cost **estimated** |
| gelato.com product pages | **403** (curl and WebFetch) | Gelato's own blog, its support centre and an Aug-2026 comparison article |
| gooten.com | Canvas volume prices are in the HTML; framed, metal and acrylic prices render client-side | Canvas only |
| finerworks.com | Dropship terms are readable; prices render client-side | Terms only |
| customcat.com/catalog | **403** | — |
| pictorem.com/pricing, printique.com/pricing | **404** | Review-site figures only |
| bayphoto.com price list | Client-side; the professional price list needs a login | Shipping via the Pic-Time help article |
| **trustpilot.com** | **403** on all 17 partner pages | Scores taken from search snippets (dates vary) |
| **reddit.com** | **403** (JSON). Searches returned no r/EtsySellers or r/printondemand threads. | Not obtained. Shopify app reviews and review-site tests used instead. |
| zonkraft.com/pricing, teelaunch.com product page, printkeg.com (Shopify JSON), stationeryhq.com (Shopify JSON), tog.ink, carlsoncraftproducts.com | Worked | Foil, sign and engraving costs |
| rankhero.com keyword pages | Worked | Market medians |

Etsy fees are the brief's figures: 6.5% transaction, 3% + $0.25 payment processing, $0.20 listing. Offsite Ads cases are 12% and 15%. All prices include free shipping to the buyer. Design labour is **excluded** here; the shortlist added $1–$15 per order for it.

## 2. Partner costs at a glance (USD, seen 2026-10-30)

| Format | Partner (provider, city) | Size A cost | Size B cost | US ship (first item) | Production / transit | Etsy link |
|---|---|---|---|---|---|---|
| Unframed matte | Printful Enhanced Matte 189gsm | 8x10 $7.03 | 18x24 $13.15 | $4.99 | 2–5 bd / 3–4 bd | Native app |
| Unframed matte | Printify, Sensaria (Longmont CO) | from $4.96 | 18x24 $10.50* | $7.49–7.69 | — / 3–8 bd | Native app |
| Unframed fine art | Lumaprints Archival Matte (Anaheim CA) | 8x10 $3.19 | 16x24 $10.37 (no 18x24) | not public (est $6–7) | 2–3 bd / — | Integration listed |
| Unframed | Gelato 170gsm coated silk (not premium matte) | 8x10 $4.49 | 18x24 $8.69 | not captured (403) | — | Native app |
| Framed, no mat | Printful (black/white/red oak) | 8x10 $20.76 | 16x20 $42.61 | $10.89 / $14.49 | 2–5 / 3–4 bd | Native app |
| Framed, mat | Printful, with mat (black; 12x16 and up only) | 12x16 $36.41 | 16x20 $45.73 | $10.89 / $14.49 | same | Native app |
| Framed, no mat / mat | Lumaprints 0.875in frame | 8x10 $20.08 / $28.83 (2in mat) | 16x20 $35.12 / $49.92 (2in mat) | not public | 2–3 bd | Listed |
| Framed | Printify, Jondo (Yorba Linda CA) | from $35.48 | 16x20 not found | $9.69 / $17.19 economy | 4–8 bd | Native app |
| Canvas | Printful 1.25in | 8x10 $15.81 | 16x20 $28.56 | $6.79 / $10.39 | 2–5 / 3–4 bd | Native app |
| Canvas | Lumaprints 1.25in (0.75in: $24.35) | 8x10 $10.99 | 16x20 $25.95 | not public | 2–3 bd | Listed |
| Canvas | Gooten (hand-stretched, USA) | 8x10 $8.58 vol. | 16x20 $16.42 vol. | not captured | — | Yes |
| Canvas | Gelato Slim | 8x8 $11.69 | 16x20 $28.19 | not captured | — | Native app |
| Metal | Printful Glossy Metal (US only) | 8x10 $39.48 | 16x20 $80.06 | $12.99 / $14.49 | 2–5 / 3–4 bd | Native app |
| Metal | Lumaprints | 8x10 $30.57 | 16x20 $82.46 | not public | 2–3 bd | Listed |
| Metal | Bay Photo (pro lab, CA) | from $15.75 (4x4 retail) | pro login | $18.62 (economy 6–9 bd) | 2–3 bd | None (manual) |
| Acrylic | Printify, Acrylic Idea Factory (Tucson AZ) | from $53.70 | 16x20 not found | $23.59 / $24.29 | 2–5 bd | Native app |
| Acrylic block | Printique (1in block) / Bay Photo | from $47.99 (review) | — | Bay $20.49 | 5–7 d | None (manual) |
| **Foil (metallic substrate)** | **Prodigi US lab**: gold/silver, UVgel on foil stock | 4x6 from $3.35 | 11x14 behind login (**est $15**) | **est $8.79** (11x14) | **72 h** / 6–9 d (review) | Etsy integration |
| Foil (framed) | Prodigi classic framed foil | 6x6 from £21 (~$28) | login | — | 72 h | Etsy |
| Foil-effect | Printkeg: Metallic Gold 100# / Pearl Silver 80# stock (USA) | 8x10 $9.99 | 13x19 $9.99 | not captured (est $6) | ships in 1–2 bd | Manual upload, free blind ship |
| **Real raised foil (digital)** | TOG.ink / Carlson Craft (North Mankato MN) | 10x8: 5 for $49.23 | 11x14: 5 for $39.76 | not captured | ~5 bd | Trade site, drop-ship unconfirmed |
| Real hot foil / digital foil | StationeryHQ (San Leandro CA) | 5x7 hot-foil card $9.34 ($80 die per design) | 8x10 digital-foil print: quote | — | 4–7 bd | Manual; 100% blind ship |
| Engraved board | Printify engraving (JDS blank; Printify Choice / Fancy Fanny KS) | 9x6 from $25.07 | — | $15.19 / $18.39 | 2–5 bd | Native app |
| Engraved board | teelaunch, maple / walnut | small $11.25 | walnut large $20.50 | $5.00 / $6.00 | — | Etsy (**2023 data, stale**) |
| Laser-cut steel sign | Zonkraft (Atlanta GA), 16ga galvanised, powder-coated | 18in $25.99 | 24in $39.99 | $15.00 / $17.50 | 3–5 bd | Etsy + Shopify |
| Die-cut steel sign | teelaunch (Louisiana), 18ga | $17.25–$105 range | — | $17.50 (18in and 24in) | 5–7 d | Etsy |
| Printed aluminium sign | Printify Metal Art Sign (Taylor, MN / Printify Choice) | from $13.56 | — | $18.39 / $19.29 | 2–5 bd | Native app |
| Ornament | Printful ceramic / metal Christmas | ceramic $6.34; 2-side $7.73 | metal $4.61–8.27 | $5.49 / $5.89 | 2–5 / 3–4 bd | Native app |
| Ornament | Printify ceramic 2-side (Colorway, Las Vegas NV) | from $9.79 | — | $5.89 | 2–5 bd | Native app |

\*Printify's $10.50 for 18x24 comes from the shortlist (podvector.ai's May-2026 table); the provider behind it is not named. Printful adds a $0.40 per-order US surcharge from 15 Oct 2026 to 17 Jan 2027; it is excluded from the margins below.

Quality signals (Trustpilot via search snippets, since direct fetch returned 403):

| Partner | Trustpilot |
|---|---|
| Printful | 4.2 (~7.9k) |
| Printify | 4.5 (~7k–7.7k) |
| Gelato | 4.2–4.5 (~3.1–3.4k) |
| Pictorem | 4.6 (~670) |
| Prodigi | ~3.9–4.0 (~150) |
| FinerWorks | 4.2–4.5 (~30) |
| Lumaprints | 3.8 (7) |
| Gooten | TrustScore 3 (227) |
| CustomCat | 2.5 (14) |
| CanvasChamp | conflicting snippets |

Damage and reprint terms:

- **Printful and Printify:** free reprint or refund within 30 days for damage or manufacturing faults.
- **Lumaprints:** free reprint for transit damage on photo evidence; free branded invoice or thank-you note in each parcel.
- **Prodigi:** white-label shipping, 50% off the first sample order.
- **Printful samples:** 20% off, 1 sample order a month of up to 3 items.

## 3. Gross margin per order: best two partners per format

GM = (price − partner cost − US shipping − Etsy fees) ÷ price. Fees = 9.5% + $0.45.

| Format (size) | Price used | Partner | Landed cost | Etsy fees | GP | **GM** | GM with OSA 12% | GM with OSA 15% |
|---|---|---|---|---|---|---|---|---|
| Unframed (18x24) | $44.95 shortlist | Printful | $18.14 | $4.72 | $22.09 | **49.1%** | 37.1% | 34.1% |
| Unframed (18x24) | $44.95 | Printify/Sensaria | $18.19 | $4.72 | $22.04 | **49.0%** | 37.0% | 34.0% |
| Unframed (16x24 fine art) | $44.95 | Lumaprints (est. ship) | $17.37 | $4.72 | $22.86 | **50.9%** | 38.9% | 35.9% |
| Framed, no mat (16x20) | $119 shortlist | Lumaprints (est. ship) | $49.61 | $11.75 | $57.64 | **48.4%** | 36.4% | 33.4% |
| Framed, no mat (16x20) | $119 | Printful | $57.10 | $11.75 | $50.15 | **42.1%** | 30.1% | 27.1% |
| Framed with mat (16x20) | $119 | Printful | $60.22 | $11.75 | $47.03 | **39.5%** | 27.5% | 24.5% |
| Framed with 2in mat (16x20) | $119 | Lumaprints (est. ship) | $64.41 | $11.75 | $42.84 | **36.0%** | 24.0% | 21.0% |
| Canvas (16x20) | $89.95 shortlist | Lumaprints (est. ship) | $36.34 | $9.00 | $44.61 | **49.6%** | 37.6% | 34.6% |
| Canvas (16x20) | $89.95 | Printful | $38.95 | $9.00 | $42.00 | **46.7%** | 34.7% | 31.7% |
| Metal (8x10) | $85 market median | Lumaprints (est. ship) | $40.57 | $8.52 | $35.91 | **42.2%** | 30.2% | 27.2% |
| Metal (8x10) | $85 | Printful | $52.47 | $8.52 | $24.01 | **28.2%** | 16.2% | 13.2% |
| Acrylic (smallest size) | $129 shortlist | Printify/AIF ("from" price) | $77.29 | $12.70 | $39.01 | **30.2%** | 18.2% | 15.2% |
| Foil, metallic substrate (11x14) | $44.95 shortlist | Prodigi US (**est.** cost) | $23.79 | $4.72 | $16.44 | **36.6%** | 24.6% | 21.6% |
| Foil-effect stock (11x14) | $44.95 | Printkeg (est. ship) | $15.99 | $4.72 | $24.24 | **53.9%** | 41.9% | 38.9% |
| Real raised foil, personalised one-off (11x14) | $44.95 | TOG.ink (whole 5-pack per order) | $47.76 | $4.72 | −$7.53 | **−16.8%** | — | — |
| Engraved board | $49.95 shortlist | teelaunch (2023 price) | $16.25 | $5.20 | $28.50 | **57.1%** | 45.1% | 42.1% |
| Engraved board | $49.95 | Printify engraving | $40.26 | $5.20 | $4.49 | **9.0%** | −3.0% | −6.0% |
| Steel name sign (18in) | $129 shortlist | Zonkraft | $40.99 | $12.70 | $75.31 | **58.4%** | 46.4% | 43.4% |
| Ornament (ceramic) | $24.95 shortlist | Printful | $11.83 | $2.82 | $10.30 | **41.3%** | 29.3% | 26.3% |
| Ornament (metal, 2-side) | $24.95 | Printful | $10.50 | $2.82 | $11.63 | **46.6%** | 34.6% | 31.6% |
| Ornament (ceramic 2-side) | $24.95 | Printify | $15.68 | $2.82 | $6.45 | **25.9%** | 13.9% | 10.9% |

What the table means for pricing:

- **Offsite Ads is the dominant risk.** It takes 12–15 points off every line. Only Zonkraft signs, teelaunch boards and Printkeg metallic prints stay above 40% on an attributed order.
- **Prices needed to reach 40% before Offsite Ads:**
  - Acrylic (Printify/AIF): about $155.
  - Lumaprints 16x20 metal: about $195.
  - Printify engraved board: about $80.
- **Zonkraft signs depend heavily on price.** At the market median of $48.91 an 18in sign makes 5.8%. At $79.95 it makes 38.7%.
- **UK-based seller caveat (not verified; help.etsy.com returned 403 in the earlier scan):** a GBP payout account pays more than the brief's 3% + $0.25 processing rate (about 4% + £0.20), plus about 2.5% currency conversion if listings are priced in USD. Allow roughly **3.5 more points** on every line. On a $44.95 poster that is about −$1.57.

## 4. Recommended partner per format

| Format | Recommendation | Why |
|---|---|---|
| Unframed premium matte print | **Printful** (Lumaprints as the fine-art upgrade) | Every cost verified, 18x24 lands at $18.14 for 49% GM, native Etsy app, and a 30-day reprint guarantee. Lumaprints is cheaper on true archival paper but its shipping is unpublished and it has no 18x24. |
| Framed print, black/white/natural, no mat | **Lumaprints**, with Printful as fallback | $35.12 for 16x20 against Printful's $42.61. Mat widths run 1–5in in half-inch steps. Free damage reprint and a free branded insert. Confirm shipping is at or under about $15 with the calculator first. |
| Framed print with mat | **Printful** | 39.5% verified at $119 against Lumaprints' 36% (estimated). Printful's mat version starts at 12x16, so use Lumaprints for 8x10 and 11x14 matted pieces. |
| Gallery canvas | **Lumaprints**, with Printful as fallback | 1.25in 16x20 at $25.95 against $28.56. A canvas specialist. GM about 50%, or 46.7% at Printful. |
| Metal print | **Lumaprints** | 8x10 at $30.57 against Printful's $39.48. 16x20 is too dear for the $85 median at both, so lead with 8x10 and 11x14. |
| Acrylic print | **Printify / Acrylic Idea Factory (Tucson)** | The only US acrylic dropship with a captured price and a native Etsy app. Price at about $155 or more, not $129. |
| Acrylic block | **No recommendation yet** | Only professional labs (Printique, Bay Photo) without Etsy links, and no unit prices captured. Get quotes. |
| Foil | **Prodigi US lab** (see section 5) | Real metallic surface, made in the US, white-label, Etsy integration, 72 h production. |
| Engraved wood (boards) | **teelaunch**, re-verify first | 57% at $49.95 on 2023 prices. Printify's engraved board is only 9% at $49.95. |
| Engraved wood signs and plaques | **No US POD dropshipper found** | Colorado Heirloom (trade, blind drop-ship) is the lead to quote. Printify "Wood Signs" are UV-printed, not engraved. |
| Outdoor/indoor metal name sign | **Zonkraft (Atlanta)** | Laser-cut, powder-coated galvanised steel, Etsy integration, flat published prices, 3–5 bd. 58% at $129. |
| Ornaments (ceramic or metal) | **Printful** | Ceramic $6.34 or 2-sided aluminium $4.61 plus $5.49–5.89 shipping gives 41–47% at $24.95. Printify's ceramic gives 26%. |

What to disclose on Etsy as the production partner (name and location of the facility that makes the item):

- "Printful (USA)"
- "Lumaprints, Anaheim, California"
- "Acrylic Idea Factory, Tucson, Arizona" (via Printify)
- "Sensaria, Longmont, Colorado" (via Printify)
- "Prodigi (US print lab)"
- "Zonkraft, Atlanta, Georgia"
- "teelaunch (USA)"
- "Printkeg (USA)"

With Printify, disclose the named provider you pin, not "Printify". Printful's v2 API that names the exact facility needs OAuth, so confirm the facility in the dashboard.

## 5. Best US route for the foil designs

**Real hot-foil stamping, made per order with a buyer's name, is not available from any US print-on-demand dropshipper found.**

- **StationeryHQ** (San Leandro CA) does real hot-stamped foil with blind dropship, but only on stationery up to A9 (5.5x8.5in). It needs a new **$80 die per design**, so it does not work for a name that changes on every order.
- **TOG.ink / Carlson Craft** (North Mankato MN) sells real **digital raised foil** on 8x10 and 11x14 art prints in 4 foil colours, with no die. The minimum is 5 prints: 11x14 is 5 for $39.76. Ordering is through a trade/retailer account, and drop-shipping to the end buyer is not confirmed. That gives −17% GM on a personalised one-off at $44.95.

**Closest workable US dropship route: Prodigi's metallic foil prints made in its US lab** ([product page](https://www.prodigi.com/products/prints-and-posters/specialist-prints/metallic-foil-prints/)):

- A 350gsm metallic-foil stock printed with UVgel ink. Anything left white or transparent in the file shows as gold or silver foil.
- Gold or silver only. **No rose gold.**
- Sizes 4x6 to 40x80, with classic and box framed versions.
- 72 h production, white-label packaging, Etsy integration, 50% off the first sample order.
- It is a metallic surface, not a pressed or raised foil, so sample it next to the UK product before relying on it.
- Size prices are behind a free login. The 36.6% GM above uses an **estimated** $15 base for 11x14. Sign up and replace the estimate before listing.
- Artwork must be re-made as a "foil = knock-out" layer (Prodigi's foil setup guide).

Fallbacks, in order:

1. **Printkeg metallic gold / pearl silver stock** ($9.99 any size 8x8–13x19, free blind shipping, made in the US). The whole sheet is metallic and the CMYK is printed on top. Cheapest at about 54% GM, but it is a foil-effect product, not foil.
2. **StationeryHQ custom quote** for an 8x10 or 11x14 digital-foil art print (JETvarnish "Elevated Ink", no die, blind ship). This is the most likely US route to a real raised digital foil on a one-off print. Get the quote before deciding.
3. **For foil designs that are not personalised** (same foil artwork for every buyer): batch-order TOG.ink raised-foil prints (11x14 works out at $7.95 each in a 5-pack, cheaper per unit in larger packs). Then either hold stock at a US 3PL or overprint names digitally on pre-foiled stock. This needs a stockholding partner and was not costed.

## 6. Sample-order plan (judge in hand before any listing)

**Samples must be delivered to a US address.** Printful, Prodigi and Gelato route an order to the lab nearest the delivery address, so a sample sent to the UK would be made in a UK or EU lab and would not test US production. Use a US contact, a US-based assistant, or a US parcel-forwarding address. Forwarding framed and canvas pieces to the UK was not costed; it is likely to be significant.

| # | Partner | Items | Approx. cost incl. US shipping |
|---|---|---|---|
| 1 | Printful, sample order 1 (20% off) | 18x24 enhanced matte poster; 16x20 black framed, no mat; 16x20 canvas 1.25in | ~$97 ($84.32 × 0.8 + ~$30 shipping) |
| 2 | Printful, sample order 2 (next month; limit is 1 sample order a month) | 16x20 framed with mat; ceramic ornament; metal 2-side ornament | ~$66 |
| 3 | Lumaprints | 16x24 archival matte; 16x20 framed no mat; 16x20 framed with 2in mat; 16x20 canvas 1.25in; 8x10 metal | ~$197 ($151.93 + est $45 shipping) |
| 4 | Prodigi US lab (50% off first sample order) | 11x14 gold foil; 11x14 silver foil; one small classic-framed gold foil | ~$60 (est.) |
| 5 | Printkeg | 11x14 Metallic Gold; 11x14 Pearl Silver | ~$28 |
| 6 | TOG.ink (if a trade account is granted) | 11x14 digital raised-foil 5-pack | ~$50 |
| 7 | StationeryHQ | Digital-foil A7 card plus hot-foil A7 card (to judge foil quality); request a quote for an 8x10 digital-foil print | ~$30 |
| 8 | Zonkraft | 18in powder-coated steel family-name sign | $40.99 |
| 9 | teelaunch | Small maple engraved board (confirms the 2023 price) | ~$16 |
| 10 | Printify engraved board, optional | 9x6 board | $40.26 |
| 11 | Printify / Acrylic Idea Factory, optional | Smallest acrylic, only if the B2B acrylic sign line goes ahead | ~$77 |

**Total about $585 for the core set (items 1–9), or about $700 with both optional items**, before any forwarding to the UK. Several figures are estimates: Lumaprints and Printkeg shipping, and the Prodigi foil size prices.

Order rounds 1, 3, 4 and 5 first. They decide the poster, framed, canvas and foil lines, which make up 13 of the shortlist's 15 survivors.

## 7. Five gaps

1. **Size prices hidden by logins, client-side rendering or 403s.**
   - Prodigi (including every foil size), Gelato (403), FinerWorks, Gooten framed/metal/acrylic, CustomCat (403) and Bay Photo/WHCC professional price lists.
   - Printify per-size prices: its public API stopped answering without a token, so only "From" prices were captured. Printify's acrylic, sign and board margins are therefore lower bounds on cost.
   - Fix: create free accounts (Prodigi, Gelato, Printify) and read the dashboard prices.
2. **Shipping for Lumaprints, Printkeg, Prodigi and Gelato is estimated or third-party.** The Lumaprints framed, canvas and metal recommendations depend on the calculator confirming shipping at or under Printful's rate. Fix: run each calculator to a mid-US ZIP code (e.g. 66044).
3. **Quality evidence is thin.**
   - Trustpilot (403) and Reddit (403) could not be read directly. Scores come from undated search snippets.
   - Lumaprints has 7 Trustpilot reviews and FinerWorks 30.
   - No independent review of Prodigi's foil exists, and none of a US digital-foil art print.
   - Samples (section 6) are the only reliable check.
4. **No per-order US real-foil or engraved-sign dropship.** No US partner was found that does real hot or raised foil on a one-off personalised wall print and drop-ships it with an Etsy link; rose gold is not covered at all. The same applies to engraved wood signs and plaques. These need a StationeryHQ digital-foil quote and a Colorado Heirloom engraving quote. The teelaunch board price dates from 2023.
5. **UK-seller cost items not verified.**
   - Etsy's payment processing and currency conversion for a GBP payout account.
   - Whether US partners charge sales tax to a non-US seller on Etsy orders (Etsy collects as marketplace facilitator, but partners may want an exemption certificate).
   - Printful's $0.40 seasonal surcharge.
   - The cost of forwarding samples to the UK.
   - Each changes margin by 1–4 points and should be confirmed in the seller's own Etsy and partner accounts.

## 8. Source index (all seen 2026-10-30)

- Printful: https://api.printful.com/products (and /products/1, 2, 3, 171, 588, 614, 794, 795, 881, 900, 901) ; https://www.printful.com/shipping ; https://help.printful.com/hc/en-us/articles/360014067959 ; https://help.printful.com/hc/en-us/articles/360014006800-What-if-the-order-gets-damaged-in-the-mail
- Printify: https://api.printify.com/v1/catalog/blueprints.json ; https://api.printify.com/v1/catalog/blueprints/{282,555,928,1206,1236,1297,1530,1599,1600,2020}/print_providers.json ; https://api.printify.com/v1/catalog/print_providers/{2,36,48,66,70,99,104,105,228,234,259,261,450}.json ; https://printify.com/shipping-rates/{sensaria,printify-choice,jondo,acrylic-idea-factory,colorway,printed-mint}/ ; https://printify.com/app/products/home-and-living/posters ; https://printify.com/app/products/1236/generic-brand/framed-paper-posters ; https://printify.com/app/brand/163/jds-industries ; https://printify.com/app/products/1599/generic-brand/ceramic-ornaments-2-side-print ; https://listingview.io/products/metal-art-sign-1206-2443 ; https://help.printify.com/hc/en-us/articles/4483625769105 ; https://podvector.ai/articles/printify/costs-and-charges/printify-sample-order-discount-full-breakdown-for-pod-sellers
- Lumaprints: https://www.lumaprints.com/pricing/ ; https://www.lumaprints.com/faq/ ; https://www.photographytalk.com/lumaprints-review-7-products-tested-over-2-years/
- Prodigi: https://www.prodigi.com/products/prints-and-posters/specialist-prints/metallic-foil-prints/ ; https://www.prodigi.com/products/wall-art/framed-prints/classic-framed-metallic-foil-prints/ ; https://www.prodigi.com/products/foil-prints/ ; https://www.prodigi.com/download/product-range/Prodigi%20Metallic%20foil%20prints.pdf ; https://www.prodigi.com/etsy-print-on-demand/ ; https://printify.com/shipping-rates/prodigi/ (search snippet)
- Gelato: https://apparelhub.ai/blog/best-print-on-demand-supplier-for-posters-wall-art ; https://www.gelato.com/it/blog/benefits-of-selling-framed-wall-art ; https://support.gelato.com/en/articles/8996293-do-you-offer-foil-printing ; https://support.gelato.com/en/articles/8996243-are-packaging-inserts-and-branded-labels-available-for-all-products-and-regions ; https://www.gelato.com/legal/quality-and-delivery ; https://apps.shopify.com/reviews/2049250 ; product pages 403
- Gooten: https://www.gooten.com/print-on-demand/canvas-wraps/ ; /framed-prints/ ; /metal-prints/ ; /acrylic-prints/
- FinerWorks: https://finerworks.com/dropship.aspx ; https://finerworks.com/prices.aspx ; https://support.finerworks.com/ufaqs/does-finerworks-integrate-with-etsy/
- Bay Photo / Printique / Pictorem / WHCC: https://help.pic-time.com/en/articles/10063390-bay-photo-shipping-fee-breakdown ; https://www.photoworkout.com/best-metal-photo-prints ; https://www.slrlounge.com/printique-review-is-it-for-pro-photographers/ ; https://apps.shopify.com/pictorem ; https://www.pictorem.com/pricing (404) ; https://www.printique.com/pricing/ (404)
- Foil and engraving: https://www.stationeryhq.com/products.json ; https://www.stationeryhq.com/pages/the-independent-designer-s-guide-to-custom-metallic-foil-printing-in-the-usa ; https://www.stationeryhq.com/pages/digital-foil-printing-elevate-your-designs-with-premium-metallic-finishes ; https://tog.ink/Paper-Goodies/Art-Prints/3358-PFSX261114DEF1V-11-x-14-Art-Print-Digital-and-1sided-Enhanced-Foil.pro ; https://carlsoncraftproducts.com/Paper-Goodies/Art-Prints/3358-PFSX25810DEF1H-10-x-8-Art-Print-Digital-and-1sided-Enhanced-Foil.pro ; https://www.printkeg.com/products/singles ; https://www.printkeg.com/pages/blind-shipping ; https://www.printkeg.com/products/8x10-art-prints ; https://printify.com/knowledge-hub/gold-foil-printing-print-on-demand/ ; https://graphics-pro.com/?p=455221 (Colorado Heirloom) ; https://blog.teelaunch.com/2023/05/chop-slice-and-save-teelaunch/ (403; snippet)
- Signs: https://zonkraft.com/pricing ; https://zonkraft.com/ ; https://teelaunch.com/products/die-cut-metal-signs/ ; https://ecomposer.io/blogs/pod/top-rated-pod-metal-sign-suppliers ; https://ecomposer.io/blogs/pod/top-10-print-on-demand-wood-sign-suppliers
- Market medians: https://www.rankhero.com/keywords/gold-foil-print ; /foil-print ; /metal-print ; /custom-metal-sign ; /personalized-ornament ; /engraved-sign
- Quality: Trustpilot search snippets for printful.com, printify.com, gelato.com, prodigi.com, lumaprints.com, gooten.com, www.finerworks.com, pictorem.com, customcat.com, canvaschamp.* (direct fetch 403) ; reddit.com (403)
