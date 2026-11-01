# Lane A listing pipeline (Etsy)

1. `catalogue.py` holds every line per shop: title (<=15 words), 13 tags (<=20 chars), description, personalisation box, price ladder, partner per format, launch date and the demand numbers it was chosen on.
2. `python3 generate_listings.py` writes `listings/<shop>/<slug>/listing.json` (Etsy createDraftListing shape), `inventory.json` (variations = the price ladder), `listing.md` (readable) and `listings/master.csv`.
3. `etsy_client.py`: once Dale creates an Etsy developer app (keystring), `auth` per shop, then `push <folder>` (dry run) and `push <folder> --live` to create DRAFT listings with the ladder as variations. Images are uploaded separately once the mockups exist; listings go active by hand after review.
4. Mockups: Printful/Lumaprints mockup generators or the designer team, three per listing (flat lay, room scene, size guide), consistent house style per shop.

Rules baked in: noun-first titles, no occasion stuffing, 13 long-tail tags, personalisation required, production partners disclosed, US free shipping over $35, processing 3-7 days, prices anchored to the US market median with canvas/framed as the margin tiers.
