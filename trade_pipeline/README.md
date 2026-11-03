# Trade line listing pipeline (Amazon Business UK, eBay UK, trade price list)

`generate_trade_listings.py` holds the first 10 pre-sell SKUs (title, four bullets, description, keywords, category hints) and writes:
- `out/amazon_listings.csv`: columns in the Amazon category flat-file / Listings Items shape (standard price, business price, quantity discount tier, MFN, 12-day handling for pre-sell). Upload via Seller Central > Add Products via Upload, or push with the Selling Partner API (Listings Items) once the developer app is approved.
- `out/ebay_listings.csv`: eBay Seller Hub bulk-listing CSV shape (Action=Add, GTC fixed price, dispatch 12 days). Upload via Seller Hub > Reports > Upload, or push with the eBay Sell Inventory API once the app keys exist.
- `out/trade_price_list.md`: the one-page price list emailed to 30 firms (trade price = UK list x 0.90, ex VAT).
Placeholders to fill before upload: EAN/GTIN per SKU (buy GS1 UK barcodes or apply for Amazon brand/GTIN exemption), image URLs, shipping/return profile names as set up in each account.
Prices: marketplace = UK list bench x 0.95; trade = x 0.90. Landed costs from laneB_supplier_shortlist.csv; margins hold at 30%+ after Amazon 15% / eBay 13% on every SKU except glands (thin, trade-only).
