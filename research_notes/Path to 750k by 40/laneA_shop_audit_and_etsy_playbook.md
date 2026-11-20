# Lane A: shop audit, Etsy ranking playbook and launch calendar

Date: 2026-10-30. Builds on `laneA_personalised_candidates.md` (64-line scan, 15 survivors). Budget: about 80 searches and fetches used. 19 RankHero keyword pages were downloaded with plain `curl` (HTTP 200, no evasion) and parsed locally. Each one counts as a fetch.

**How to read this file**
- Every figure has a URL beside it or in the section's source list.
- **[Etsy]** marks something Etsy itself stated: Seller Handbook, Help Center, a community announcement, SEC filings, or Etsy's own shop-page text.
- **[3P]** marks a third-party claim or opinion.
- **[Judgement]** marks my own inference.
- Etsy blocked automated fetches again (HTTP 403). Every Etsy URL was tried once only (list in section 0). Etsy facts were therefore taken from search-engine snippets of Etsy pages and from third parties that quote Etsy.

---

## 0. Access log (what was blocked)

| URL tried once | Result |
|---|---|
| https://www.etsy.com/shop/FrameMyFamilyArt | 403 |
| https://www.etsy.com/uk/shop/GrumpyRabbitPrints | 403 |
| https://www.etsy.com/listing/1013117315/step-brothers-family-portrait-for | 403 |
| https://www.etsy.com/seller-handbook/article/how-etsy-search-works/22722480255 | 403 |
| https://www.etsy.com/seller-handbook/article/1399426136697 (2025 title guidance) | 403 |
| https://help.printify.com/hc/en-us/articles/28662580598161-Etsy-Search-Visibility-Changes | 403 |
| https://www.craftcount.com/shop.php?name=GrumpyRabbitPrints and ...?name=FrameMyFamilyArt | 403 / 403 |
| https://ehunt.ai/shop/GrumpyRabbitPrints and /FrameMyFamilyArt (EtsyHunt redirect) | 404 / 404 (no public page) |
| alura.io site search for both shop names | No indexed page for either shop |
| EverBee, eRank and Insight Agent public shop pages | None found for either shop by search. eRank and EverBee shop analytics need a login. |

Search-engine snippets of the Etsy shop and listing pages did come through. Section 1 is built from those snippets.

---

## 1. Shop audit (public data only)

### 1a. What is visible

| Item | FrameMyFamilyArt (FMFA) | GrumpyRabbitPrints (GRP) |
|---|---|---|
| Total sales | **3.6k** ("4.9 (1.2k) · 3.6k sales · 5 years on Etsy · 1 shop member"), from the snippet of listing page https://www.etsy.com/listing/1001598056/custom-royal-portrait-personalized (the listing is dated Oct 2, 2026) | **3,996** on the newer snapshot of https://www.etsy.com/shop/GrumpyRabbitPrints and **3,890** on the older snapshot of https://www.etsy.com/in-en/shop/GrumpyRabbitPrints. Neither snapshot is dated, so the difference of about 100 sales is not a rate. |
| Reviews and rating | **4.9 from about 1.2k ratings** (same snippet). A different listing's structured data showed **4.9 from 731 reviews**, which is probably an older cache. **[Etsy]** The shop rating is "a recency-weighted average… a rating's value decreasing by half each year" (Etsy shop-page text in the same snippets). | Newer snapshot: **4.9 from 1,329 reviews**, latest visible review dated Jun 21, 2026. Older snapshot: **5.0 from 1.3k reviews**. |
| Star Seller | **Not visible.** No snippet mentions the badge, so treat it as unverified. | The **older** India snapshot showed **Star Seller**. The newer snapshot does not mention it, so the current status is unverified. |
| Open date | "5 years on Etsy" points to roughly 2021 **[Judgement from the snippet]**. | "On Etsy since **2020**" |
| Shop location shown | **Los Angeles, California**. Listings say "ships from Los Angeles, CA". | **New Jersey, United States**. A foil song-lyric listing says "ships from NJ". |
| Listing count | **Not visible** | **Not visible** |
| Categories and lines seen | Custom family portraits, including pop-culture parodies such as the "Step Brothers" family portrait and a "Custom Royal Portrait", plus custom pet portraits. | Shop tagline: **"Premium Home Art · Foil Maps · Stars & Song Prints"**. Lines seen: custom star/celestial maps in copper, gold and rose-gold foil; location map + star map combos; foil sound-wave and song-lyric prints; foil quote prints; metallic foil city/location maps; and pop-culture pet portraits ("Top Gun", "Star Wars"). The section name "Metal foil prints" is visible. |
| Price points seen | Step Brothers family portrait **$24.99**. The Royal portrait price was not captured. | Custom Foil Song Lyrics Print **$40.00 with free shipping** (https://www.etsy.com/listing/4302845517/custom-foil-song-lyrics-print). A second foil listing was also $40 with free shipping. |
| Best-sellers visible | Step Brothers family portrait carries a **Bestseller** badge, **181 five-star reviews** and **5,454 favourites** (https://www.etsy.com/listing/1013117315/step-brothers-family-portrait-for, via snippet). | None visible. A custom bunny portrait listing (https://www.etsy.com/listing/1460433805) came up in the same search but could not be tied to GRP. |
| Production partner disclosure | **Not visible** in any snippet | **Not visible** in any snippet |
| Process and policy text | Royal portrait: "after 2–4 days you will receive a preview… once approved… shipped out within 72 hours". It also offers a "100% money-back guarantee". Returns and exchanges accepted within 30 days, buyer pays return shipping. | "Crafted with over 10 years of experience". Reviews praise fast shipping and communication. |
| Name history | — | The search index shows **https://etsy.com/shop/FrameMyPetArt titled "GrumpyRabbitPrints - Etsy"**, and the FMFA Royal-portrait description still says "FrameMyPet". **[Judgement]** GRP was probably renamed from *FrameMyPetArt*, and Etsy redirects the old shop URL. |
| Branding and banner style | Banner, logo, announcement and About were not visible. | Same: only the tagline is visible. |

Sources for 1a: search-snippet extractions of https://www.etsy.com/listing/1001598056/custom-royal-portrait-personalized, https://www.etsy.com/listing/1013117315/step-brothers-family-portrait-for, https://www.etsy.com/shop/GrumpyRabbitPrints, https://www.etsy.com/in-en/shop/GrumpyRabbitPrints, https://www.etsy.com/listing/4302845517/custom-foil-song-lyrics-print and https://etsy.com/shop/FrameMyPetArt.

**Cross-check:** 3.6k + 3,996 ≈ **7.6k lifetime sales**, which fits the brief's "about 8,000".

### 1b. What I could not see
1. Current Star Seller status for either shop.
2. Listing count, sections and their order, banner and logo, announcement, About page, and shop policies beyond one listing's return text.
3. The full price range and price distribution, and which listings sell most beyond the one FMFA bestseller badge.
4. Production-partner disclosure (it appears on the listing "Item details" and in Shop Manager, but no snippet included it).
5. Any revenue, traffic, conversion or time-series sales data. No public third-party page indexes either shop.

### 1c. Audit findings that need action **[Judgement unless marked]**

1. **Location and ships-from accuracy is the biggest risk to the 7.6k-sale asset.**
   - **[Etsy]** House Rules require "an accurate representation of how the item was made, by whom, and where it is being shipped from" (https://www.etsy.com/it/help/article/4507, via snippet).
   - Both shops show a US city as their location while the owner lives in the UK.
   - GRP's foil listings say "ships from NJ", yet the brief says metal-foil designs can **only be produced in the UK**. If foil orders actually ship from the UK, that listing claim is inaccurate and US delivery estimates will be wrong.
   - **[3P/community]** Etsy community replies say the shop's finance/bank country is fixed at setup and can't simply be changed (https://community.etsy.com/t5/Technical-Issues/Shop-s-Finance-Country/m-p/146430267/highlight/true). The shop-page location is a separate setting (https://help.etsy.com/hc/articles/115015306687).
   - Check with Etsy Support which country each shop is registered and paid out in, and set ships-from per listing to the partner's real print location. This is not legal advice.
2. **Multi-shop disclosure.** **[Etsy]** "If you choose to run multiple shops on Etsy, you must list all the shops you run in the Public Profile section of each account", and duplicate listings across shops are not allowed (https://help.etsy.com/hc/en-us/articles/360017604474, via snippet). Check that FMFA and GRP list each other.
3. **Production partners.** **[Etsy]** A production partner "physically produces items based on your own, original designs". Using non-qualifying businesses "may result in penalties up to and including account suspension" (https://help.etsy.com/hc/articles/360000336547, via snippet). Every US print partner and the UK foil producer must be listed in Shop Manager › Settings › Production partners, with the location set to where the item is printed (https://support.printful.com/hc/en-us/articles/41396445789841-What-should-I-know-about-Etsy-s-Creative-Standards-policy; https://www.insightagent.app/guides/etsy-creative-standards-policy).
4. **Template leftovers.** The FMFA Royal-portrait copy still says "FrameMyPet". It reads as careless and should be cleaned up.
5. **Lanes overlap.** Both shops sell pet portraits, and GRP mixes pop-culture pet portraits with foil maps and song prints. Section 4 proposes separate lanes.

---

## 2. Etsy search and ranking, 2025–2026

### 2a. What Etsy has said

| Factor | What Etsy said | Source |
|---|---|---|
| Holistic matching | Titles needn't "do all the work", because search "takes a holistic view of your listing, including title, tags, attributes, descriptions, first photo, reviews, and more". | Etsy Seller Handbook, "New Guidance for Listing Titles, and a Tool to Help" (Aug–Sep 2025), https://www.etsy.com/seller-handbook/article/1399426136697 (403; text via snippet and https://help.erank.com/blog/seo/etsy-title-update-2025-how-to-write-better-etsy-listing-titles/) |
| **Title rules (2025)** | Keep titles **under 15 words**. Lead with the noun. Add only the top 3 objective details (colour, size, material). Remove repeated words. Move aspirational phrases ("gift for him") and subjective words ("perfect") to tags or attributes. **Only add occasions if essential.** Leave out sale, shipping and price terms ("Etsy adds this automatically"). An optional AI title tool sits in the Search Visibility page. eRank reports Etsy confirmed older-style titles are **not penalised** and updating is optional. | Same handbook article, as quoted by eRank (27 Aug 2025), URL above. Etsy's own example title: "Personalised 100% Cotton Dad T-Shirt: Custom Kids' Names S-XL" (https://mydesigns.io/blog/etsy-search-algorithm-update-2026/) |
| Title length limit | 140 characters is the platform limit. An older handbook checklist said "ideally 40 characters or less". | https://www.etsy.com/seller-handbook/article/648735427806 (snippet) |
| **Search Visibility page** | Shows how listings perform in "three key areas that factor into Etsy search: your **shop, listing, and customer service quality**". It flags title quality, shipping price, missing attributes and photo quality, and supports bulk edits. | Handbook, Aug 26 2025, https://www.etsy.com/seller-handbook/article/366470356778 (snippet). Flag list from MyDesigns citing handbook article 1289139008351 (https://mydesigns.io/blog/etsy-search-algorithm-update-2026/) |
| **Attributes** | Attributes are category-specific and built from buyer search research. "Add all the attributes that are relevant… skip any that don't apply." | Same Aug 2025 handbook article (snippet) |
| **Shipping price** | From **1 Oct 2024**, US listings with domestic shipping **under $6** are prioritised in search. Exempt: sellers outside the US, listings **over $35 from shops offering the free-shipping guarantee**, calculated shipping, and digital listings. | Etsy announcement "Etsy Updates: 5 things to know for September 2024", https://community.etsy.com/forum/announcements-290/topic/etsy-updates-5-things-to-know-for-september-2024-22360/ (snippet); also https://help.erank.com/blog/etsys-october-1st-shipping-visibility-change/ |
| US free-shipping guarantee | Search priority since **30 July 2019** for shops offering free shipping on US orders of **$35+**. | https://www.growingyourcraft.com/blog/should-i-offer-free-shipping-on-etsy (summarising Etsy) |
| **Quality signals weighted up (Q3 2026)** | Etsy is "increasing the weight of quality signals within search and recommendations" and "evolving how we define a great match in Search". | Etsy Q3 2026 shareholder letter, https://www.sec.gov/Archives/edgar/data/0001370637/000137063726000090/q326shareholderletter.htm |
| Personalised ranking | "Personalization improvements alone contributed approximately **two percentage points**" to annualised GMS growth. Some personalisation is being extended to signed-out users. | Same Q3 2026 letter |
| App and mobile | App GMS **+10.4%** year on year against **+7.5%** non-app. Mobile is about **47%** of GMS (Q3 2026). The app was 46% of GMS in Q3 2025. | Q3 2026 letter; Q3 2025 figure via https://blog.marmalead.com/etsy-algorithm-2026/ citing https://investors.etsy.com/news-events/press-releases/detail/213/etsy-inc-reports-third-quarter-2025-results |
| **Photos and video** | Up to **20 photos** per listing (raised from 10 in Aug 2025). Video is 5–15 s in the listing guide (one Help article says 3–15 s). A second video per listing has been reported. | Handbook "Anatomy of a Well-Crafted Etsy Listing", Aug 26 2025, https://www.etsy.com/seller-handbook/article/1347574487014 (snippet); https://listperfectly.com/selling/etsy-20-images-per-listing-list-perfectly/; https://www.alura.io/news/two-videos-per-listing |
| **Star Seller** | Over a rolling 3 months: **≥95% of messages** answered within 24 h; **≥95% of orders shipped on time with tracking**; **average review ≥4.8**; at least **5 orders** (some guides also say **$300** in sales, which I could not confirm); first sale at least 90 days ago. Evaluated monthly. Buyers can filter to Star Sellers, and the article says Etsy has confirmed it is a search factor. | https://craftybase.com/blog/how-to-become-etsy-star-seller (updated Apr 2026) [3P summary of Etsy]; $300 figure from https://listingview.io/blogs/how-to-become-an-etsy-star-seller-in-2026 [3P, conflicting] |
| **Gift Mode** | Launched Jan 2024. Shoppers enter the recipient and occasion, and machine learning assigns one of about **200 personas**, then recommends items "through machine learning, paired with curation by style experts". Etsy describes no seller opt-in. | https://www.digitalcommerce360.com/2024/01/26/etsy-tries-new-gift-mode-recommendations-with-ai/ |
| **AI and LLM discovery** | ChatGPT Instant Checkout started Sep 2025 and **ended Mar 2026**. The **Etsy app inside ChatGPT launched May 2026**. Etsy is testing an on-site conversational **"Gifting Assistant" (beta, holiday 2026)**. Selling through Google AI Mode and Gemini started Jan 2026. "Gen AI-powered shopping is an… increasingly important discovery channel." | https://techcrunch.com/2026/05/05/etsy-launches-its-app-within-chatgpt-as-it-continues-its-ai-push/; https://www.retailbrew.com/stories/2026/05/04/etsy-launches-chatgpt-app-tests-ai-search-agent-to-help-with-gifting; https://www.digitalcommerce360.com/2026/01/15/etsy-selling-through-google-ai-mode-gemini/amp/; Q3 2026 letter |
| **Etsy Ads** | Q3 2026 take rate was **26.2%** (+50 bp), "primarily driven by further enhancements to Etsy Ads". "The majority of Etsy Ads revenue comes from sellers with less than $100,000 in annual GMS." | Q3 2026 letter |
| **Offsite Ads** | **15%** of the order total, or **12%** for shops with $10k+ in trailing-12-month sales. **Mandatory at $10k+**. 30-day attribution window. Does not stack with Etsy Ads. One source cites a **$100 per-order cap** (single source). | [3P, Etsy fee page blocked] https://www.gelato.com/blog/how-much-does-etsy-take-from-a-sale; https://checkoutpage.com/blog/etsy-fees; https://listingview.io/blogs/how-etsy-ads-work-in-2026-and-when-to-turn-them-off |
| Base fees | $0.20 listing, **6.5%** transaction (including shipping), **3% + $0.25** US payment processing. | Same fee guides [3P] |
| Creativity Standards | POD goods fall under "designed by a seller" and must use the seller's own original designs, with partners disclosed. One vendor dates a tightening to 10 Jun 2025 (unverified). | https://help.etsy.com/hc/articles/360000336547 (snippet); https://www.listadum.com/blog/etsy-creativity-standards [3P] |
| Personalisation field | Etsy's character limit for the personalisation box was **not found** in budget. | Gap |

### 2b. Third-party claims (not confirmed by Etsy)

| Claim | Who | Verdict **[Judgement]** |
|---|---|---|
| A listing-quality score is built from CTR, favourites, add-to-cart and conversion. Meaningful edits (thumbnail, title, attributes, price or shipping) trigger re-testing, but "tag shuffling does nothing". | Marmalead, Dec 2025, https://blog.marmalead.com/etsy-algorithm-2026/; eRank https://help.erank.com/?p=34818 | Plausible and consistent with Etsy's "quality signals" wording. Treat it as the working model. |
| Shop-quality score (reviews, fulfilment, cases, policy completeness) affects the **whole catalogue**. | Marmalead (same) | Consistent with Etsy's three areas (shop, listing, customer service). This is why a new line in an established shop has an advantage. |
| The first 3–5 words of the title matter most because the app truncates titles. | Marmalead (same) | Sensible given app GMS +10.4% and mobile at 47%. |
| "Golden rule": don't edit bestselling listings; edit in batches and measure over 1–3 months. Review AI title suggestions because they drop keywords. | eRank, Aug 2025 (URL above) | Follow this. |
| Fix flagged listings in batches of 10–20 and wait 2–4 weeks before judging. | MyDesigns, Feb 2026 (URL above) | Sensible. |
| From 2026, descriptions feed query matching. | https://listinglab.pro/blog/etsy-seo-guide-2026 | Unverified, but Etsy's "holistic view" includes descriptions. |
| Recency boost; listings untouched for 6 months lose about 3% a month. | https://www.fryntavo.cloud/blog/how-etsy-algorithm-works-2026 | **Unsupported number.** Ignore it. |
| A "70-character" title limit, and "10 photos outperform". | Assorted 2026 blogs (https://listybox.com/blog/etsy-algorithm-search-ranking-guide-2026) | Unsourced, and contradicted by Etsy's own 15-word and 20-photo guidance. Ignore. |
| The $6 shipping rule is "new in 2026". | MyDesigns | It is the Oct 2024 rule restated. |

### 2c. What this means for these two shops **[Judgement]**
- A POD poster sold with free shipping at $35 or more clears the shipping signal without trouble. Every survivor line from the earlier scan is priced at $39.95 or more. Turn on the $35 free-shipping guarantee in both shops.
- Titles: write "Custom Star Map Print, Gold Foil Night Sky by Date" (noun first, under 15 words). Put "anniversary gift for him / wedding / the night we met" in tags and in the Occasion and Recipient attributes.
- Star Seller is the cheapest shop-wide lever. A 2–4 day proof cycle on portraits plus partner production makes the "95% shipped on time" criterion risky. Set processing times to what the slowest path actually takes.
- Etsy now weights quality signals more and personalises results per buyer. Conversion on the first listings of a new line matters more than how many listings there are. Launch 3–6 strong listings per line, not 40 thin ones.
- AI channels such as ChatGPT, Gemini and the Gifting Assistant read structured data. Complete attributes and plain descriptions that name the occasion, recipient, size and personalisation are what those channels can match.

---

## 3. 12-month US gifting calendar and launch plan (Nov 2026 – Oct 2027)

### 3a. Demand inputs

**Monthly search series, Oct 2025 – Sep 2026 (or Sep 2025 – Aug 2026).**
- Source: RankHero keyword pages, `https://www.rankhero.com/keywords/<term>`, downloaded 2026-10-30.
- These are global, Google-type, bucketed volumes (for example 165,000 then 201,000), not Etsy-native volumes. Use them for timing, not for size.

| Term | Peak month(s) | Trough | Notes |
|---|---|---|---|
| star map | **Jan 60.5k** (all other months 49.5k) | Jul 40.5k | Flat. Valentine's run-up. US share 37% (18.1k). Median price $26.98; 46% of listings priced $25–50. |
| custom star map | Dec 4.4k | Apr 2.4k | −19% year on year |
| birth flower | **Mar–May 201k** | 165k in all other months | Mother's Day lift on a flat base |
| birth flower bouquet | Jan, Mar, Apr, Jul–Sep **14.8k** | Nov 9.9k | **+22% year on year**, difficulty 32, 17,288 listings, US 2.9k/mo, median ~$25 |
| custom map | **Nov–Dec 110k**, **Aug 74k**, Jan 60.5k | Oct, Mar–May 27.1k | Strong Q4 gifting spike plus an August bump |
| custom city map | flat ~210 | — | Tiny. Buyers type "custom map", not "city map". |
| housewarming gift | **Feb 450k, Mar 368k** | Apr–Jul 165k | Searches lead the June peak in home sales. **[Judgement]** Likely spring buyers plus gift planning. |
| house portrait | **Dec 2.4k** | Apr, Jun, Jul 1.0k | US 720/mo. A Christmas gift as much as a housewarming one. |
| wedding gift | **Feb–Mar 368k**, Nov 301k | Jun–Jul 110k | Counter-intuitive against when weddings happen. **[Judgement]** Bucketed data, so verify in Etsy Marketplace Insights. |
| anniversary gift | **Feb 450k**, Nov and Mar 368k | Jul–Sep 135k | Valentine's |
| baptism gift | **Apr 33.1k** | Dec 14.8k | Easter and spring baptism or first-communion season |
| retirement gift | **May–Jun 74k** | Oct and Feb 40.5k | End of school and fiscal year |
| memorial gift | **Dec 18.1k**, Nov 14.8k | Jun 6.6k | Holiday grief gifting |
| family name sign | **Dec 5.4k**, Nov 4.4k | 2.4k floor | Q4 |
| established sign | Dec 1.3k | 880 floor | Q4 |
| business sign | **Sep 27.1k**, Oct and Mar 22.2k | Dec and Jul–Aug 14.8k | **[Judgement]** Pre-Q4 and spring openings |
| watercolor portrait | flat 9.9k | Jul–Aug 8.1k | Evergreen |
| baby stats | flat ~720 (Nov and Jan 880) | — | Evergreen and small |
| foil print | Sep–Oct 12.1k | 9.9k flat | US 2.4k/mo, relevant to GRP's foil range |

**Occasion and event data**
- **Valentine's 2026:** $29.1bn, a record. **35% of consumers bought Valentine's gifts for pets** ($2.1bn). Source: NRF, https://nrf.com/media-center/press-releases/valentine-s-day-spending-expected-to-reach-new-records
- **Mother's Day 2026:** $38bn, average $284.25 per person. Source: NRF, https://nrf.com/media-center/press-releases/mother-s-day-spending-expected-to-hit-record-38-billion
- **Father's Day 2026:** $27.9bn, average $226.58. Source: NRF, https://nrf.com/media-center/press-releases/father-s-day-spending-to-hit-record-27-9-billion
- **Weddings:** October and June are top at 16% each, then May 14%, September 13%, August 10%. 41% of weddings fall Sep–Nov. January and February are 2% each. Source: The Knot, https://www.theknot.com/content/fall-most-popular-wedding-season and https://www.theknot.com/content/is-there-an-off-season-for-weddings
- **Engagements:** December is the top month for engagements (older Knot study, year not stated).
- **Births:** August is the peak month for US births (about 320k in Aug 2023 against about 271k in Feb). There were 3,591,328 births in 2023. Sources: https://www.themotherbabycenter.org/blog/2026/01/most-popular-birth-month/ ; CDC provisional 2023 via https://stacks.cdc.gov/view/cdc/151797/cdc_151797_DS1.pdf
- **Home sales:** May–Aug account for about 40% of annual existing-home sales, and June is the peak. Sources: NAR, https://www.nar.realtor/blogs/economists-outlook/seasonality-in-the-housing-market ; June = 10.2% of US annual sales (1990–2015), https://trerc.tamu.edu/wp-content/uploads/files/PDFs/Articles/2142.pdf

**Lead times (when Etsy buyers start searching and when to list)**
- **[3P, eRank]** Holiday listings should be live in early autumn, because listings need time to gather clicks. Easter searches begin in late January. Sources: https://help.erank.com/blog/holiday-trend-reports-etsy-sellers/ ; https://help.erank.com/blog/plan-for-easter-with-eranks-keyword-tool/
- **[3P, Marmalead]** Plan at least 3 months ahead. Have fall products live by late July, because Etsy starts promoting them in mid-August. Source: https://blog.marmalead.com/etsy-holiday-mistakes/
- **[3P, vendor calendars]** Personalised Valentine's searches peak **Jan 25–Feb 5** (citing Marmalead data). List Mother's Day by Mar 15–31, Father's Day by May 1–15, graduation by Apr 15–30 and Christmas by Sep 1–15 (last chance Oct 1–15). Source: https://sellertoolshq.com/guides/etsy-seasonal-launch-calendar-2026/
- **[3P, vendor calendars]** Valentine's by Jan 5 (ideally Dec 28), US Mother's Day by Apr 1, Father's Day by May 1, Christmas by Sep 15 (latest Oct 1), and summer weddings 4–6 months ahead. Source: https://www.listifyai.net/blog/etsy-holiday-calendar-2026
- **[Judgement]** Rule used below: **list 8–10 weeks before the event, and earlier for Q4.** A listing then has 3–6 weeks to earn clicks before the buyer search window opens, which is about 4–6 weeks before a gift date and later for self-purchase.

**2026–27 dates** (computed): Thanksgiving 26 Nov 2026, Black Friday 27 Nov, Cyber Monday 30 Nov. Valentine's Sun 14 Feb 2027. UK Mothering Sunday 7 Mar 2027. Easter 28 Mar 2027. Teacher Appreciation Week 3–7 May 2027. Mother's Day 9 May 2027. Father's Day 20 Jun 2027. Grandparents Day 12 Sep 2027. Boss's Day Sat 16 Oct 2027. Thanksgiving 25 Nov 2027.

### 3b. Month-by-month calendar (shortlisted lines)

"Peaking" means the RankHero series or event data is at or near its high in that month. "List by" is when the next wave of listings must be live.

| Month | Occasions driving demand | Shortlisted lines peaking | List by this month (for later peaks) |
|---|---|---|---|
| **Nov 2026** | Thanksgiving, BFCM, Christmas, engagement season starting | **Custom map** (110k), **memorial** (14.8k), **family-name/established sign** (4.4k), wedding/anniversary secondary peak (301k/368k) | Too late to rank brand-new Q4 lines. Put existing GRP map and star listings into Christmas trim (attributes, photos, shipping cut-off). Build Valentine's star map / "our story" listings. |
| **Dec** | Christmas, Hanukkah, **top engagement month** | **Custom map** (110k), **house portrait** (2.4k), **memorial** (18.1k), **family-name sign** (5.4k), custom star map (4.4k) | **Valentine's star map, anniversary and couple portrait listings live by 26 Dec–5 Jan.** Housewarming and custom-map spring listings drafted. |
| **Jan 2027** | Valentine's search window (peaks ~Jan 25–Feb 5), New Year moves | **Star map** (60.5k, its peak), custom map (60.5k), birth flower bouquet (14.8k), housewarming (301k) | **Birth-flower family bouquet live by ~1 Feb** for the Mar–May peak. Baptism/Easter listings live (Easter searches start late Jan). |
| **Feb** | Valentine's (Sun 14), Galentine's, pets as Valentine's recipients (35%) | **Anniversary** (450k), **housewarming** (450k), **wedding gift** (368k), star map | **Mother's Day birth-flower and family portraits** fully live by 15 Feb–15 Mar. UK foil Mothering Sunday (7 Mar) for the UK channel. |
| **Mar** | Spring weddings booked, Easter (28 Mar), UK Mothering Sunday | **Birth flower** (201k from Mar), **wedding** (368k), **housewarming** (368k), retirement (60.5k), business sign (22.2k) | **Retirement** prints live by 1 Apr. **Graduation** variants by 15–30 Apr. Father's Day by 1 May. |
| **Apr** | Easter season, baptisms and first communions, Mother's Day run-up | **Baptism** (33.1k, its peak), **birth flower** (201k), retirement (60.5k) | Father's Day (golf map, dad star map) live by 1 May. Summer wedding items live. |
| **May** | **Mother's Day (9 May)**, Teacher Appreciation (3–7 May), graduation, weddings (14%), home-sale season begins (May–Aug ≈ 40%) | **Retirement** (74k, its peak), **birth flower** (201k), weddings | Housewarming summer push. Nursery and birth-stats listings refreshed for the Jul–Aug birth peak. |
| **Jun** | **Father's Day (20 Jun)**, **weddings (16%)**, home-sale peak month, end of school year | **Retirement** (74k), custom map (40.5k), wedding events | Back-to-school and teacher listings (optional). Start Q4 design work. |
| **Jul** | Birth peak season (Jul–Aug), moving season, Christmas in July | **Birth flower bouquet** (14.8k), nursery/birth-stats (evergreen), watercolour portraits (evergreen) | **Fall and Q4 products live by late July** (Marmalead: Etsy starts promoting mid-August). Grandparents Day items. |
| **Aug** | **Peak birth month**, college move-in, home sales, weddings (10%) | **Custom map** (74k, second peak), housewarming (201k), baptism (27.1k), birth flower bouquet (14.8k) | **Christmas listings for all Q4 lines by 1–15 Sep**: custom map, family-name sign, memorial, house portrait, star map gift sets. |
| **Sep** | **Grandparents Day (12 Sep)**, weddings (13%), Q4 small-business prep | **Business sign** (27.1k, its peak), foil print (12.1k), baptism (27.1k), birth flower bouquet | Last-chance Christmas listings by **1 Oct**. Boss's Day (16 Oct) retirement and corporate. |
| **Oct** | **Top wedding month (16%)**, Boss's Day, Christmas searches climbing | Foil print (12.1k), wedding events, baptism (27.1k), business sign (22.2k), custom map ramp | Valentine's 2028 drafts. Review the year in Etsy Stats. |

**Coverage check [Judgement]:** at least one shortlisted line peaks every month.
- Nov–Dec: maps, family-name signs, memorial and house portraits.
- Jan–Feb: star map, anniversary and housewarming.
- Mar–May: birth flower, wedding, baptism and retirement.
- Jun: retirement and Father's Day.
- Jul–Aug: births and custom map.
- Sep–Oct: business sign and wedding/foil.

The quiet months are **July** and **October**. They are covered by evergreen lines (watercolour, star map at 40.5k minimum, birth flower at a 165k floor) rather than by a single peaking line.

**Conflict to resolve with Etsy data:** the Google-type "wedding gift" series bottoms out in Jun–Jul, exactly when weddings peak (Knot). Etsy-native volumes from Marketplace Insights may differ. Until then, list wedding prints by March and keep them live through October.

---

## 4. Branding and store structure

### 4a. Do focused single-niche shops outrank broad shops?
- **No direct evidence found.** No Etsy statement and no third-party study comparing niche and broad shops turned up in budget. Searches for eRank, Marmalead, EverBee and Alura material on this returned none.
- **[Etsy]** Search scores "shop, listing, and customer service quality" (https://www.etsy.com/seller-handbook/article/366470356778). The shop-level part of that is service quality, not topical focus. Nothing Etsy has published says a shop is rewarded for staying in one niche.
- **[3P, eRank]** When all your listings serve one buyer type the shop "becomes more relevant in search", and a second shop lets you "double down on niche-specific keywords". But "each new shop starts at square one" with no reviews or sales (https://help.erank.com/?p=38028, via snippet).
- **[3P, Alura]** If a new line "significantly differs" from the current store, a second store keeps the brand consistent (https://alura.io/docs/article/a-sellers-guide-to-running-multiple-shops-on-etsy).
- **[3P, Marmalead]** A shop-quality score lifts the whole catalogue (https://blog.marmalead.com/etsy-algorithm-2026/). That argues for adding lines to an established shop.
- **[Judgement]** Per-buyer personalisation (Etsy Q3 2026) rewards listings that match each buyer's history, not shop focus as such. Focus mainly helps **conversion and brand recall**: a buyer who lands on a star map sees a shop full of star maps. Reviews are shop-wide, so a focused shop also shows more relevant reviews.

**Example of a young, focused shop ranking**
- **OrbitalPerspective** (Etsy member since 30 Jul 2024) sells star maps only and discloses a production partner.
- It has a "Rave reviews" badge, and its "Custom Star Map • Paper Anniversary Gift…" listing at **$23** has **4,959 favourites and 91,564 views**, ranking #3 in RankHero's sample for "custom star map".
- Sources: https://www.rankhero.com/keywords/custom-star-map ; https://www.etsy.com/listing/1804553990 (snippet); https://community.etsy.com/t5/user/viewprofilepage/user-id/13759794 (snippet)

### 4b. Examples by niche

RankHero samples 12 top listings per keyword and shows price, **favourites and views (not sales)**. Etsy lifetime sales figures come from search snippets, with their age noted.

| Niche | Shop | Public figure | Price seen | Naming style | Source |
|---|---|---|---|---|---|
| Star map | PaperEmporiumCo (UK) | Listing: **61,479 favourites / 2.14M views**. Shop says it was "one of the first of its kind on Etsy" with "thousands of five-star reviews". | **£5.00 entry variant**; $37 elsewhere | "Paper" + "Emporium" + Co: a brand plus material | https://www.rankhero.com/keywords/star-map ; https://www.etsy.com/listing/1029301545 |
| Star map | PaperNoteCoUK | 8,292 favourites | £22.00 | Brand + Co + country | same |
| Star map | ThreeMemoryVivid | 6,464 favourites | $19.98 | Abstract | same |
| Star map | OrbitalPerspective | 4,658–4,959 favourites, member since 2024 | $23.00 | **Niche-evocative brand** | same + custom-star-map page |
| Star map | EmmaAndTheBeanHOME | 645 favourites | $35.00 | Person + HOME | https://www.rankhero.com/keywords/custom-star-map |
| Star map | TheStarsAboveCo (Vancouver) | **~12,800 lifetime sales**, on Etsy since 2016. The snapshot is ~725 days old. | n/a | Niche-literal | https://www.etsy.com/shop/TheStarsAboveCo (snippet) |
| Custom map | TheMapShop | **23,675 lifetime sales**, since 2011. The snapshot is ~653 days old. | n/a | Niche-literal | https://www.etsy.com/shop/TheMapShop (snippet) |
| Custom map | HometownGiftsCo / WellTold | 9,951 and 999 favourites (etched city-map glassware) | $21.50 / $24.95 | Occasion/brand | https://www.rankhero.com/keywords/custom-city-map |
| Custom map | StudioLocale | 880 favourites, set of 3 city prints | £14.99 | Brand | same |
| Birth flower | PopOfInk | 303 favourites, "Family Birth Flower Bouquet… CUSTOM Framed Physical Print" | $25.50 | Brand | https://www.rankhero.com/keywords/birth-flower |
| Birth flower | COCOandLILLI | 318 favourites, watercolour family bouquet | $42.99 | Person names | https://www.rankhero.com/keywords/birth-flower-bouquet |
| Birth flower | SolidRockDesignCo | 98 favourites | $54.11 | Brand + DesignCo | birth-flower page |
| Birth flower (format note) | — | The top 'birth flower' listings are a **mug (11,603 favourites, $43)**, a sticker ($3) and **digital tattoo/print files ($1–$15)**. One digital bouquet shows 16.2k reviews and a framed one 4.4k (shop-level review counts). | — | — | birth-flower page; https://www.etsy.com/market/birth_flowers_prints (snippet) |
| House portrait | (shops not named in snippets) | Top listings show **7.9k** and **22.5k** review counts. Digital $4–12; hand-painted or framed $20–300. | — | — | https://www.etsy.com/market/house_portraits (snippet) |
| Family-name sign | FalkelDesign / JaxleyDesign / mrcwoodproducts | 129,120 / 96,908 / 37,112 favourites | $130 wood / $48 pallet / **$40.87 canvas** | Maker names | https://www.rankhero.com/keywords/family-name-sign |
| Business sign | Pupax / Febzer / NVSprinting | 9,874 / 8,789 / 1,985 favourites | $30 laser / $56.67 / A$88 acrylic | Brand | https://www.rankhero.com/keywords/business-sign |
| Pet portraits (scale benchmark) | **PawtraitDesignArt** | **157,415 lifetime sales**, opened **2023** (Alura, data as of 17 Oct 2026) | n/a | **Niche keyword in the name** | https://www.alura.io/top-etsy-sellers/prints |

**Patterns [Judgement]**
1. Star-map leaders anchor **low entry prices** (£5–£8 digital or small sizes) with physical upsells. A $40+ foil star map needs to look premium in its **first photo** to justify roughly 1.5× the $26.98 median.
2. Mockup and photo style were **not checked**. Images were not viewed, which is a gap. Look at the top-12 thumbnails on the RankHero pages by hand.
3. Leading names are short brand names with an optional material or niche word ("Paper…", "Orbital…", "…MapShop", "Pawtrait…"), not keyword-stuffed strings.
4. Birth-flower demand on Etsy goes mostly to mugs, jewellery and digital files. The **physical framed family-bouquet print** has fewer, smaller competitors (300-favourite listings in the top 12). That is consistent with the earlier scan's "1.4 listings per search" finding.

### 4c. What a portrait-heavy shop should do **[Judgement]**

**Recommendation: two lanes, one per existing shop. No new shop yet.**
- **GrumpyRabbitPrints becomes the "maps, stars and words" shop.** It already calls itself "Foil Maps · Stars & Song Prints".
  - Lines: star maps, custom maps/coordinates, housewarming house + address, anniversary/wedding "our story", family-name/established signs, song/soundwave.
  - UK-made foil is the premium variant and GRP's differentiator.
  - Move the pop-culture pet portraits out to FMFA, or retire them.
- **FrameMyFamilyArt becomes the "people and pets" shop.**
  - Lines: family and pet portraits, watercolour portraits, birth-flower family bouquet (a family gift and Mother's Day line), nursery/birth stats, baptism, memorial, retirement portrait.
- **Why not new niche shops?** Each new shop "starts at square one" (eRank). Star Seller needs a 90-day-old first sale and 5+ orders. A shop-quality score built on 3.6k–4k sales is the main asset to reuse.
- **Sections:** in each shop, create sections by **product line**, plus one or two **seasonal occasion sections** rotated with the calendar ("Valentine's & Anniversary", "Mother's Day", "Christmas Gifts").
- **Small-business logo signs** serve a different buyer (B2B) with different keywords and reviews. Test them later as a third shop or on another channel, only after the consumer lines are running.
- **Rename?** Not now. The FrameMyPetArt → GrumpyRabbitPrints redirect suggests Etsy keeps history on a rename, but a name change during a relaunch adds risk with no evidence of ranking gain. Change the banner, announcement, About and section order instead.
- **Rules to respect:** Etsy requires the shops to be listed in each other's Public Profile and forbids duplicate listings across shops (https://help.etsy.com/hc/en-us/articles/360017604474). Each listing therefore lives in exactly one shop.

---

## 5. The ten highest-leverage actions, in order **[Judgement, built on the evidence above]**

1. **Compliance first (week 1).** In both shops:
   - Confirm with Etsy Support the registered and finance country against the shown location.
   - Set accurate **ships-from per listing**. UK-made foil must not say "ships from NJ" unless it does.
   - List every production partner with its real print location.
   - Cross-list the two shops in Public Profile and remove any duplicate listings.
   - Fix the "FrameMyPet" template text.

   Why first: House Rules and production-partner penalties extend to account suspension, and both 4k-sale shops are at stake.
2. **Pull Etsy Stats and the orders CSV, open the Search Visibility page, and fix flagged listings in batches of 10–20.** Do not touch current bestsellers such as the Step Brothers portrait. Measure after 2–4 weeks (eRank, MyDesigns).
3. **Recover or protect Star Seller in both shops.** Set processing times to the real proof-plus-partner time, reply to all messages within 24 h, and upload tracking for every order. It is a confirmed search factor and buyer filter.
4. **Set the shipping profile everywhere:** free shipping on US orders, prices of $35 or more, and the **$35 free-shipping guarantee** turned on. This clears the Oct-2024 sub-$6 shipping rule outright.
5. **Assign the lanes and restructure:** GRP as maps, stars and words; FMFA as people and pets. Rewrite the banner, announcement, About and sections to match. Move overlapping pet-portrait listings into FMFA.
6. **Launch the star-map line in GRP by 26 Dec 2026 – 5 Jan 2027**, with a gold, copper or rose-foil premium tier and a standard POD tier. "Star map" peaks in January and personalised Valentine's searches peak around Jan 25–Feb 5.
7. **Apply one listing standard to every new listing:**
   - Title under 15 words, noun first.
   - 13 tags covering occasion, recipient and style.
   - Every relevant attribute (occasion, holiday, recipient, room, colour).
   - All 20 photos: hero mockup, size chart, personalisation example, proof-process graphic, foil close-up.
   - 1–2 videos of 5–15 s.
   - A clear personalisation-box prompt.

   This matters more under Etsy's heavier weighting of quality signals and the structured-data needs of AI channels.
8. **Launch the birth-flower family bouquet print in FMFA by about 1 Feb 2027.** "Birth flower" runs 201k from Mar to May, "birth flower bouquet" is up 22% year on year, and the physical framed format has thin competition. Add a UK foil version for Mothering Sunday (7 Mar).
9. **Launch custom map + housewarming house-and-address in GRP by mid-January**, for the Feb–Mar housewarming peak. Follow with **retirement and baptism** (in FMFA or GRP by template) by 1 Mar for the April baptism and May–June retirement peaks. Keep **wedding/anniversary "our story"** listings live from March to October.
10. **Lock Q4 2027 by 1–15 Sep 2027.** Custom map Christmas sets, family-name/established signs, memorial and house portrait listings must be live then (Christmas lists close by 1 Oct at the latest).
    - Run Etsy Ads only on listings already converting.
    - Budget for Offsite Ads at 12%. It is mandatory above $10k a year, so price it into margins: the earlier scan shows a $44.95 poster falling from 50.6% to 38.6% gross margin on an attributed order.

## 6. Five gaps only the seller's own Etsy Stats and orders export can close

1. **Line-level history:** units, revenue and refunds/remakes by listing and month across 2020–2026. This shows which portrait lines faded, the shop's own seasonality, and repeat-buyer rate. It replaces the Google-type series in section 3.
2. **Search terms and conversion per listing:** Stats › "How shoppers found you" queries, plus impressions, CTR and conversion for each listing. Together with **Marketplace Insights** (Etsy-native keyword volume) this confirms the Etsy demand for star map, birth flower and wedding gift that the RankHero data can't.
3. **Service metrics:** current Star Seller status and its four metrics, case and cancellation rates, and actual dispatch times per production partner (US POD against UK foil). This decides the processing times to set.
4. **Traffic and ad economics:** search against Etsy Ads, Offsite Ads, app and social. Also Offsite Ads fees paid in the last 12 months and Etsy Ads spend against attributed revenue, per shop.
5. **Buyer mix and order economics:** buyer country (US vs UK vs other), average order value, personalisation-field usage, proof-revision count per portrait order, and real partner cost and shipping per SKU. These replace the public Printify/Printful prices and the $6/hour design assumption in the earlier unit-economics table.

---

## 7. Source index

**Shops (search-snippet extraction):**
- https://www.etsy.com/listing/1001598056/custom-royal-portrait-personalized
- https://www.etsy.com/listing/1013117315/step-brothers-family-portrait-for
- https://www.etsy.com/shop/GrumpyRabbitPrints
- https://www.etsy.com/in-en/shop/GrumpyRabbitPrints
- https://etsy.com/shop/FrameMyPetArt
- https://www.etsy.com/listing/4302845517/custom-foil-song-lyrics-print

**Etsy policy and Etsy statements:**
- https://www.etsy.com/it/help/article/4507
- https://help.etsy.com/hc/articles/360000336547
- https://help.etsy.com/hc/en-us/articles/360017604474
- https://help.etsy.com/hc/articles/115015306687
- https://www.etsy.com/seller-handbook/article/1399426136697
- https://www.etsy.com/seller-handbook/article/366470356778
- https://www.etsy.com/seller-handbook/article/1347574487014
- https://www.etsy.com/seller-handbook/article/648735427806
- https://community.etsy.com/forum/announcements-290/topic/etsy-updates-5-things-to-know-for-september-2024-22360/
- https://www.sec.gov/Archives/edgar/data/0001370637/000137063726000090/q326shareholderletter.htm
- https://community.etsy.com/t5/Technical-Issues/Shop-s-Finance-Country/m-p/146430267/highlight/true

**Third-party guides:**
- https://help.erank.com/blog/seo/etsy-title-update-2025-how-to-write-better-etsy-listing-titles/
- https://help.erank.com/blog/etsys-october-1st-shipping-visibility-change/
- https://help.erank.com/?p=38028
- https://help.erank.com/blog/holiday-trend-reports-etsy-sellers/
- https://help.erank.com/blog/plan-for-easter-with-eranks-keyword-tool/
- https://blog.marmalead.com/etsy-algorithm-2026/
- https://blog.marmalead.com/etsy-holiday-mistakes/
- https://mydesigns.io/blog/etsy-search-algorithm-update-2026/
- https://craftybase.com/blog/how-to-become-etsy-star-seller
- https://listingview.io/blogs/how-to-become-an-etsy-star-seller-in-2026
- https://listingview.io/blogs/how-etsy-ads-work-in-2026-and-when-to-turn-them-off
- https://www.gelato.com/blog/how-much-does-etsy-take-from-a-sale
- https://checkoutpage.com/blog/etsy-fees
- https://www.growingyourcraft.com/blog/should-i-offer-free-shipping-on-etsy
- https://listperfectly.com/selling/etsy-20-images-per-listing-list-perfectly/
- https://www.alura.io/news/two-videos-per-listing
- https://alura.io/docs/article/a-sellers-guide-to-running-multiple-shops-on-etsy
- https://www.alura.io/top-etsy-sellers/prints
- https://support.printful.com/hc/en-us/articles/41396445789841-What-should-I-know-about-Etsy-s-Creative-Standards-policy
- https://www.insightagent.app/guides/etsy-creative-standards-policy
- https://www.listadum.com/blog/etsy-creativity-standards
- https://listinglab.pro/blog/etsy-seo-guide-2026
- https://www.fryntavo.cloud/blog/how-etsy-algorithm-works-2026
- https://listybox.com/blog/etsy-algorithm-search-ranking-guide-2026
- https://sellertoolshq.com/guides/etsy-seasonal-launch-calendar-2026/
- https://www.listifyai.net/blog/etsy-holiday-calendar-2026

**AI and Gift Mode:**
- https://techcrunch.com/2026/05/05/etsy-launches-its-app-within-chatgpt-as-it-continues-its-ai-push/
- https://www.retailbrew.com/stories/2026/05/04/etsy-launches-chatgpt-app-tests-ai-search-agent-to-help-with-gifting
- https://www.digitalcommerce360.com/2026/01/15/etsy-selling-through-google-ai-mode-gemini/amp/
- https://www.digitalcommerce360.com/2024/01/26/etsy-tries-new-gift-mode-recommendations-with-ai/

**Demand and timing:**
- RankHero keyword pages (fetched 2026-10-30): https://www.rankhero.com/keywords/ followed by star-map, custom-star-map, birth-flower, birth-flower-bouquet, custom-map, custom-city-map, housewarming-gift, house-portrait, wedding-gift, anniversary-gift, baptism-gift, retirement-gift, memorial-gift, family-name-sign, established-sign, business-sign, watercolor-portrait, baby-stats, foil-print
- https://nrf.com/media-center/press-releases/valentine-s-day-spending-expected-to-reach-new-records
- https://nrf.com/media-center/press-releases/mother-s-day-spending-expected-to-hit-record-38-billion
- https://nrf.com/media-center/press-releases/father-s-day-spending-to-hit-record-27-9-billion
- https://www.theknot.com/content/fall-most-popular-wedding-season
- https://www.theknot.com/content/is-there-an-off-season-for-weddings
- https://www.themotherbabycenter.org/blog/2026/01/most-popular-birth-month/
- https://stacks.cdc.gov/view/cdc/151797/cdc_151797_DS1.pdf
- https://www.nar.realtor/blogs/economists-outlook/seasonality-in-the-housing-market
- https://trerc.tamu.edu/wp-content/uploads/files/PDFs/Articles/2142.pdf

**Niche shops:**
- https://www.etsy.com/shop/TheStarsAboveCo
- https://www.etsy.com/shop/TheMapShop
- https://www.etsy.com/listing/1804553990
- https://www.etsy.com/listing/1029301545
- https://community.etsy.com/t5/user/viewprofilepage/user-id/13759794
- https://www.etsy.com/market/birth_flowers_prints
- https://www.etsy.com/market/house_portraits
