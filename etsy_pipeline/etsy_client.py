"""Minimal Etsy Open API v3 client for pushing the generated skeletons as DRAFT listings.
Setup: create an app at https://www.etsy.com/developers/your-apps -> keystring; set ETSY_API_KEY, ETSY_SHOP_ID.
Run `python3 etsy_client.py auth` once per shop (OAuth 2.0 + PKCE, scopes listings_r listings_w shops_r), token saved to .etsy_token_<shop>.json (git-ignored).
Then `python3 etsy_client.py push listings/<shop>/<slug> [--live]` (dry-run prints the payloads unless --live)."""
import os, sys, json, hashlib, base64, secrets, urllib.parse, urllib.request
API = "https://openapi.etsy.com/v3/application"; KEY = os.environ.get("ETSY_API_KEY", ""); SHOP = os.environ.get("ETSY_SHOP_ID", "")
REDIRECT = "http://localhost:3003/oauth/redirect"; SCOPES = "listings_r listings_w shops_r"
def auth():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_hex(8)
    url = "https://www.etsy.com/oauth/connect?" + urllib.parse.urlencode({"response_type": "code", "redirect_uri": REDIRECT, "scope": SCOPES, "client_id": KEY, "state": state, "code_challenge": challenge, "code_challenge_method": "S256"})
    print("1. Open this URL, log in to the shop owner account, approve:\n", url, "\n2. Paste the full redirect URL here:")
    code = urllib.parse.parse_qs(urllib.parse.urlparse(input().strip()).query)["code"][0]
    data = urllib.parse.urlencode({"grant_type": "authorization_code", "client_id": KEY, "redirect_uri": REDIRECT, "code": code, "code_verifier": verifier}).encode()
    tok = json.load(urllib.request.urlopen(urllib.request.Request("https://api.etsy.com/v3/public/oauth/token", data=data)))
    json.dump(tok, open(f".etsy_token_{SHOP}.json", "w")); print("token saved")
def call(method, path, body=None, form=False):
    tok = json.load(open(f".etsy_token_{SHOP}.json"))["access_token"]
    hdr = {"x-api-key": KEY, "Authorization": f"Bearer {tok}"}
    data = None
    if body is not None:
        data = urllib.parse.urlencode(body, doseq=True).encode() if form else json.dumps(body).encode()
        hdr["Content-Type"] = "application/x-www-form-urlencoded" if form else "application/json"
    req = urllib.request.Request(f"{API}{path}", data=data, headers=hdr, method=method)
    return json.load(urllib.request.urlopen(req))
def push(folder, live=False):
    L = json.load(open(os.path.join(folder, "listing.json"))); inv = json.load(open(os.path.join(folder, "inventory.json")))
    body = {k: v for k, v in L.items() if not k.startswith("_")}
    for k, v in body.items():
        if isinstance(v, str) and v.startswith("<SET"): raise SystemExit(f"fill {k} first ({v})")
    if not live: print(json.dumps(body, indent=2)[:2000], "\n... DRY RUN. add --live to create the draft listing"); return
    created = call("POST", f"/shops/{SHOP}/listings", body, form=True); lid = created["listing_id"]; print("draft listing", lid)
    products = [{k: v for k, v in pr.items() if not k.startswith("_")} for pr in inv["products"]]
    call("PUT", f"/listings/{lid}/inventory", {"products": products, "price_on_property": inv["price_on_property"], "sku_on_property": inv["sku_on_property"]})
    print("inventory set; upload images via POST /shops/{shop}/listings/{lid}/images (multipart) then set state=active when mockups are in")
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "auth": auth()
    elif cmd == "push": push(sys.argv[2], "--live" in sys.argv)
    else: print(__doc__)
