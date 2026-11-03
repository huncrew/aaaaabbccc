"""Pull every ACTIVE listing of the benchmark shops with the Etsy Open API v3 (public endpoints: API key only, no OAuth).
Outputs competitors/<shop>.csv (listing_id, title, price, currency, quantity, num_favorers, views, tags, materials, created, last_modified,
is_digital, has_variations, section) and competitors/keyword_bank.csv (tag -> count across the shop's listings, which is the copy-the-leaders tag set).
Usage: ETSY_API_KEY=... python3 etsy_competitors.py PawtraitDesignArt TheStarsAboveCo TheMapShop OrbitalPerspective PopOfInk"""
import os, sys, csv, json, time, urllib.request, urllib.parse, collections
API="https://openapi.etsy.com/v3/application"; KEY=os.environ.get("ETSY_API_KEY") or sys.exit("set ETSY_API_KEY")
def get(path, **q):
    u=f"{API}{path}?{urllib.parse.urlencode(q)}" if q else f"{API}{path}"
    r=urllib.request.Request(u, headers={"x-api-key": KEY}); time.sleep(0.12)   # 10 req/s cap
    return json.load(urllib.request.urlopen(r))
os.makedirs("competitors", exist_ok=True); bank=collections.Counter(); prices=[]
for name in sys.argv[1:]:
    shop=get("/shops", shop_name=name)["results"][0]; sid=shop["shop_id"]
    print(f"{name}: shop_id {sid}, listings_active {shop.get('listing_active_count')}, sales {shop.get('transaction_sold_count')}, reviews {shop.get('review_count')}, rating {shop.get('review_average')}, opened {shop.get('create_date')}")
    rows=[]; off=0
    while True:
        page=get(f"/shops/{sid}/listings/active", limit=100, offset=off, includes="Images")
        for L in page["results"]:
            p=L["price"]; price=p["amount"]/p["divisor"]; tags=L.get("tags",[]); bank.update(tags); prices.append(price)
            rows.append({"listing_id":L["listing_id"],"title":L["title"],"price":price,"currency":p["currency_code"],"quantity":L.get("quantity"),"num_favorers":L.get("num_favorers"),"views":L.get("views"),
                         "tags":"|".join(tags),"materials":"|".join(L.get("materials",[])),"created":L.get("original_creation_timestamp"),"last_modified":L.get("last_modified_timestamp"),
                         "is_digital":L.get("listing_type")=="download","has_variations":L.get("has_variations"),"section":L.get("shop_section_id"),"url":L.get("url")})
        off+=100
        if off>=page["count"]: break
    with open(f"competitors/{name}.csv","w",newline="") as f: w=csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"  {len(rows)} active listings saved; digital {sum(r['is_digital'] for r in rows)}, median price {sorted(r['price'] for r in rows)[len(rows)//2]:.2f}")
with open("competitors/keyword_bank.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["tag","count"]); w.writerows(bank.most_common())
print(f"keyword bank: {len(bank)} distinct tags across {len(prices)} listings")
