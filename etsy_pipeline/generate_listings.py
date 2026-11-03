"""Generate listing skeletons (Etsy API v3 payload shapes + human-readable MD) for every line in catalogue.py.
Usage: python3 generate_listings.py  -> writes listings/<shop>/<slug>/{listing.json,inventory.json,listing.md} and listings/master.csv"""
import json, csv, os, re
from catalogue import SHOPS, LADDER, ladder, COMMON_DESC, DIGITAL_LINES
OUT = os.path.join(os.path.dirname(__file__), "listings"); os.makedirs(OUT, exist_ok=True)
FEE_RATE, FEE_FIXED, LABOUR = 0.13, 0.45, 1.50   # UK/GBP-paid Etsy seller approx (6.5%+3%+~3.5pt) ; $0.25+$0.20 ; design labour/order
rows = []
def check(line):
    assert len(line["tags"]) == 13, line["slug"]
    for t in line["tags"]: assert len(t) <= 20, (line["slug"], t)
    assert len(line["title"]) <= 140 and len(line["title"].split()) <= 15, (line["slug"], len(line["title"].split()))
for shop, s in SHOPS.items():
    for line in s["lines"]:
        check(line)
        prices = ladder(line["entry"])
        products = []
        for fmt, (label, _, partner, cost) in LADDER.items():
            if fmt == "digital" and line["slug"] not in DIGITAL_LINES: continue
            price = prices[fmt]
            gp = price - cost - (FEE_RATE*price + FEE_FIXED) - LABOUR
            products.append({"sku": f"{line['slug'].upper()}-{fmt.upper()}", "property_values": [{"property_name": "Size / Finish", "values": [label]}],
                             "offerings": [{"price": price, "quantity": 999, "is_enabled": True}], "_partner": partner, "_partner_cost_usd": cost, "_gross_profit_usd": round(gp,2), "_gross_margin": round(gp/price,3)})
        desc = COMMON_DESC.format(hook=line["hook"], fields=line["fields"], details=line["details"])
        listing = {"title": line["title"], "description": desc, "price": prices["digital"] if line["slug"] in DIGITAL_LINES else prices["print_8x10"], "quantity": 999, "who_made": "i_did", "when_made": "made_to_order",
                   "taxonomy_id": "<SET: Etsy taxonomy id for Art & Collectibles > Prints > Digital/Giclée Prints>", "tags": line["tags"], "materials": ["archival matte paper", "canvas", "wood frame"],
                   "shipping_profile_id": "<SET: US free-shipping-over-35 profile>", "return_policy_id": "<SET>", "processing_min": 3, "processing_max": 7, "type": "physical",
                   "is_personalizable": True, "personalization_is_required": True, "personalization_char_count_max": 256, "personalization_instructions": line["personalization"],
                   "production_partner_ids": ["<SET: Lumaprints partner id>", "<SET: Printful partner id>"], "should_auto_renew": True, "is_supply": False, "state": "draft",
                   "_meta": {"shop": shop, "lane": s["lane"], "launch_live_by": line["launch"], "anchor_keyword": line["keyword"], "us_searches_month": line["searches"], "listings_per_search": line["lps"], "seasonality_index": line["si"], "mockups": line["mockups"]}}
        d = os.path.join(OUT, shop, line["slug"]); os.makedirs(d, exist_ok=True)
        json.dump(listing, open(os.path.join(d, "listing.json"), "w"), indent=2)
        json.dump({"products": products, "price_on_property": [513], "quantity_on_property": [], "sku_on_property": [513], "_note": "property id 513 = Size placeholder; use the shop's custom property id from getListingInventory"}, open(os.path.join(d, "inventory.json"), "w"), indent=2)
        md = [f"# {line['title']}", f"**Shop:** {shop} ({s['lane']})  **Live by:** {line['launch']}  **Keyword:** {line['keyword']} ({line['searches']:,} US searches/mo, {line['lps']} listings per search, seasonality {line['si']})", "",
              "## Price ladder", "| Format | Price | Partner | Partner cost | Gross profit | Margin |", "|---|---|---|---|---|---|"]
        for pr in products: md.append(f"| {pr['property_values'][0]['values'][0]} | ${pr['offerings'][0]['price']:.2f} | {pr['_partner']} | ${pr['_partner_cost_usd']:.2f} | ${pr['_gross_profit_usd']:.2f} | {pr['_gross_margin']:.0%} |")
        md += ["", "## Tags (13)", ", ".join(line["tags"]), "", "## Personalisation box", line["personalization"], "", "## Mockups to produce", *[f"- {m}" for m in line["mockups"]], "", "## Description", desc]
        open(os.path.join(d, "listing.md"), "w").write("\n".join(md))
        for pr in products:
            rows.append({"shop": shop, "slug": line["slug"], "title": line["title"], "launch_live_by": line["launch"], "format": pr["property_values"][0]["values"][0], "price_usd": pr["offerings"][0]["price"], "partner": pr["_partner"], "partner_cost_usd": pr["_partner_cost_usd"], "gross_profit_usd": pr["_gross_profit_usd"], "gross_margin": pr["_gross_margin"], "keyword": line["keyword"], "us_searches_month": line["searches"], "listings_per_search": line["lps"], "seasonality_index": line["si"]})
with open(os.path.join(OUT, "master.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(f"wrote {len(rows)} variations across {sum(len(s['lines']) for s in SHOPS.values())} listings in {len(SHOPS)} shops -> {OUT}")
