"""Lane A catalogue: one entry per listing line, per shop. Prices anchored to the US market medians in
research_notes/.../laneA_personalised_candidates.csv (RankHero, Oct 2026); partners/costs from laneA_us_production_partners.csv.
Etsy rules applied: title <= 15 words / 140 chars, noun first; 13 tags <= 20 chars each; personalisation on; partner disclosed."""

LADDER = {  # format -> (variation label, price USD, partner, partner cost incl. US ship USD)
    "print_8x10":   ("8x10 in print, unframed",  None,   "Lumaprints (Anaheim CA)",  10.19),
    "print_12x16":  ("12x16 in print, unframed", None,   "Lumaprints (Anaheim CA)",  13.50),
    "print_18x24":  ("18x24 in print, unframed", 39.95,  "Printful (US)",            18.14),
    "canvas_16x20": ("16x20 in gallery canvas",  89.95,  "Lumaprints (Anaheim CA)",  36.34),
    "framed_16x20": ("16x20 in framed, black",   119.00, "Lumaprints (Anaheim CA)",  49.61),
}
def ladder(entry):  # entry price at the market median (rounded to .95, floor 22.95); 12x16 = entry + 8
    e = max(22.95, round(entry) - 0.05)
    return {"print_8x10": e, "print_12x16": round(e + 8, 2), "print_18x24": max(39.95, round(e + 15, 2)),
            "canvas_16x20": 89.95, "framed_16x20": 119.00}

COMMON_DESC = """{hook}

HOW IT WORKS
1. Add your details in the personalisation box ({fields}).
2. Our designers prepare a digital proof within 1-2 business days and send it to you by Etsy message.
3. Approve it (or ask for changes, included) and we print and ship from our US print partner within 2-4 business days.

SIZES & FINISHES
- 8x10 in and 12x16 in prints on archival matte paper, shipped flat
- 18x24 in print on enhanced matte paper, shipped rolled in a tube
- 16x20 in gallery-wrapped canvas, 1.25 in deep, ready to hang
- 16x20 in framed print, black wood frame, ready to hang

DETAILS
{details}

SHIPPING
Printed and shipped in the USA by our production partners (disclosed on this listing). Typical US delivery 5-8 business days after proof approval. Free US shipping on orders over $35.

QUESTIONS
Message us any time. We have made over 7,000 personalised pieces since 2020 and reply within one business day.
"""

SHOPS = {
 "GrumpyRabbitPrints": {"lane": "maps, stars and words", "lines": [
  dict(slug="star_map", launch="2026-12-26", entry=26.98, keyword="star map", searches=18100, lps=1.0, si=1.22,
       title="Custom Star Map Print, Night Sky by Date and Place, Anniversary Wedding Birth Gift",
       tags=["custom star map","star map print","night sky print","custom gift","anniversary gift","wedding gift","the night we met","constellation map","celestial print","birth star map","first date gift","new baby gift","gift for him"],
       fields="date, location, optional line of text", hook="The night sky exactly as it looked above the place and moment that mattered: a first date, a wedding, a birth, a goodbye.",
       details="- Astronomically accurate star chart for your date and coordinates\n- Choose dark navy, black or white background\n- Up to two lines of custom text and the date\n- Optional coordinates and constellation lines",
       personalization="Date (DD/MM/YYYY), city or address, and up to two lines of text", mockups=["flat lay 18x24 on oak table", "framed in living room scene", "size guide with all five formats"]),
  dict(slug="custom_map", launch="2026-11-10", entry=29.95, keyword="custom map", searches=18100, lps=5.4, si=2.19,
       title="Custom City Map Print, Any Location Coordinates, Personalized Housewarming Travel Gift",
       tags=["custom map print","city map print","coordinates print","custom map gift","housewarming gift","travel gift","map of our home","first home gift","any city map","minimalist map","closing gift","realtor gift","gift for couple"],
       fields="city or address, optional title and coordinates", hook="A clean, minimalist street map of the place that means home, printed for the wall.",
       details="- Any address or city worldwide, drawn from map data at print resolution\n- Choose monochrome, navy or sand palette\n- Add a title, coordinates and a date\n- Pair with the star map for a matched set",
       personalization="City or full address, title line, optional date and coordinates", mockups=["flat lay 18x24", "hallway framed scene", "size guide"]),
  dict(slug="housewarming_map", launch="2027-01-15", entry=32.47, keyword="housewarming gift", searches=6050, lps=26.4, si=1.8,
       title="Housewarming Gift Map Print, New Home Address and Date, Personalized First Home Gift",
       tags=["housewarming gift","new home gift","first home gift","new homeowner","closing gift","realtor gift","address print","home sweet home","custom home print","moving gift","our first home","new house gift","gift for couple"],
       fields="address, move-in date, family name", hook="Mark the day the keys were handed over: the street map of the new home, the address and the date.",
       details="- Street map centred on the new address\n- Family name, address and move-in date\n- Three colour palettes\n- Ships straight to the new address if you like",
       personalization="Full address, family name, move-in date", mockups=["flat lay", "entryway scene", "size guide"]),
  dict(slug="anniversary_story", launch="2027-01-15", entry=23.99, keyword="anniversary gift", searches=4950, lps=41.4, si=1.8,
       title="Anniversary Gift Print, Our Story Star Map and City Map, Personalized Couple Keepsake",
       tags=["anniversary gift","our story print","couple gift","custom couple gift","where it all began","star map anniversary","wedding anniversary","first anniversary","paper anniversary","gift for wife","gift for husband","valentines gift","love story print"],
       fields="two dates, two places, names", hook="Where you met, where you married, the sky that night: three moments on one print.",
       details="- Up to three panels: map, star map, dates\n- Names and a short line of text\n- Matches the star map and city map prints", personalization="Names, up to three dates and places", mockups=["flat lay", "bedroom scene", "size guide"]),
  dict(slug="retirement_print", launch="2027-04-15", entry=23.00, keyword="retirement gift", searches=4065, lps=9.3, si=1.33,
       title="Retirement Gift Print, Years of Service Personalized Keepsake for Coworker, Boss, Teacher",
       tags=["retirement gift","retirement print","years of service","gift for coworker","gift for boss","teacher retirement","nurse retirement","police retirement","retirement keepsake","retirement present","happy retirement","farewell gift","office gift"],
       fields="name, years, employer, retirement date", hook="Forty years in one frame: name, dates, the place, and the words the team wants to say.",
       details="- Name, role, employer and service dates\n- Space for a short team message\n- Framed option arrives ready to present", personalization="Name, role, employer, start and retirement dates, message", mockups=["framed on desk", "flat lay", "size guide"]),
  dict(slug="wedding_print", launch="2027-01-15", entry=22.95, keyword="wedding gift", searches=3310, lps=92.3, si=1.8,
       title="Wedding Gift Print, Names Date and Venue Map, Personalized Keepsake for the Couple",
       tags=["wedding gift","wedding keepsake","couple gift","names and date","venue map print","custom wedding gift","bride and groom","wedding present","newlywed gift","engagement gift","mr and mrs","bridal shower gift","wedding sign"],
       fields="names, wedding date, venue", hook="The venue on a map, the names, the date: a wedding gift that is not another photo frame.",
       details="- Venue street map or star map on the wedding night\n- Names and date in a choice of typefaces\n- Canvas and framed tiers for the gift table", personalization="Two names, wedding date, venue address", mockups=["framed gift table", "flat lay", "size guide"]),
  dict(slug="family_name_sign", launch="2026-11-10", entry=48.00, keyword="family name sign", searches=2400, lps=34.9, si=1.78,
       title="Established Family Name Sign, Personalized Last Name Canvas, Wedding Anniversary Gift",
       tags=["family name sign","established sign","last name sign","custom canvas sign","family est sign","wedding gift","anniversary gift","housewarming gift","farmhouse sign","custom name sign","family wall art","gift for parents","christmas gift"],
       fields="surname, established year, optional first names", hook="The family name and the year it all started, printed large for the hallway or above the sofa.",
       details="- Surname, year, optional first names and a short line\n- Farmhouse, modern and script styles\n- Best as the 16x20 canvas; also as prints", personalization="Surname, established year, optional first names", mockups=["canvas above sofa", "flat lay", "size guide"]),
 ]},
 "FrameMyFamilyArt": {"lane": "people and pets", "lines": [
  dict(slug="birth_flower_bouquet", launch="2027-02-01", entry=25.00, keyword="birth flower", searches=22625, lps=1.4, si=1.14,
       title="Birth Flower Family Bouquet Print, Personalized Mothers Day Gift for Mom and Grandma",
       tags=["birth flower print","family bouquet","birth month flower","mothers day gift","gift for mom","gift for grandma","custom family print","birth flower art","custom bouquet","family gift","nana gift","botanical print","gift for her"],
       fields="names and birth months of each family member", hook="One bouquet, one flower for every birth month in the family, with their names beneath.",
       details="- Up to 12 birth flowers in one bouquet, hand-drawn style\n- Names under each stem, family name as the title\n- Choose watercolour or line-art style and background", personalization="Each family member's name and birth month (up to 12)", mockups=["flat lay", "kitchen wall scene", "size guide"]),
  dict(slug="watercolor_portrait", launch="2026-11-10", entry=28.13, keyword="watercolor portrait", searches=3600, lps=43.4, si=1.03,
       title="Custom Watercolor Portrait from Photo, Personalized Family Couple or Pet Painting Print",
       tags=["watercolor portrait","custom portrait","portrait from photo","family portrait","couple portrait","pet portrait","custom painting","photo to painting","anniversary gift","gift for mom","memorial portrait","wedding portrait","custom illustration"],
       fields="upload photo(s), names, optional text", hook="Your photo, repainted by hand in soft watercolour, with a proof to approve before it prints.",
       details="- Up to 6 people or pets from one or several photos\n- Names and a line of text optional\n- Proof in 2-4 days, unlimited changes until approved", personalization="Upload photos after purchase; add names and text here", mockups=["flat lay", "living room scene", "size guide"]),
  dict(slug="pet_portrait", launch="2026-11-10", entry=29.95, keyword="pet portrait", searches=12100, lps=41.1, si=1.64,
       title="Custom Pet Portrait from Photo, Personalized Dog Cat Illustration Print, Pet Lover Gift",
       tags=["custom pet portrait","pet portrait","dog portrait","cat portrait","pet lover gift","dog mom gift","pet illustration","portrait from photo","pet memorial","custom pet gift","dog dad gift","pet wall art","christmas pet gift"],
       fields="upload photo, pet name, style", hook="The portrait that made our name: your pet from a photo, in the style you choose, proofed before printing.",
       details="- Modern, royal, watercolour or line-art style\n- Pet name and optional dates\n- Up to 4 pets on one print", personalization="Pet name(s), style choice; upload photo after purchase", mockups=["flat lay", "hallway scene", "size guide"]),
  dict(slug="nursery_stats", launch="2027-07-15", entry=22.68, keyword="nursery wall art", searches=2400, lps=602.2, si=1.03,
       title="Nursery Name Print with Birth Stats, Personalized New Baby Gift, Baby Shower Keepsake",
       tags=["nursery wall art","birth stats print","new baby gift","baby shower gift","custom nursery art","baby name print","birth announcement","nursery decor","newborn gift","baby girl gift","baby boy gift","first birthday","godparent gift"],
       fields="name, birth date and time, weight, length", hook="Name, date, time, weight and length, set in a print for the nursery wall.",
       details="- Name and all birth stats\n- Animal, floral or minimalist themes\n- Matches the birth flower print", personalization="Baby's name, birth date and time, weight, length, theme", mockups=["nursery scene", "flat lay", "size guide"]),
  dict(slug="baptism_print", launch="2027-03-15", entry=22.95, keyword="baptism gift", searches=2960, lps=15.7, si=1.41,
       title="Baptism Gift Print, Personalized Christening Keepsake with Name Date and Verse",
       tags=["baptism gift","christening gift","baptism keepsake","godchild gift","godparent gift","custom baptism gift","baby dedication","christening print","religious gift","baptism boy","baptism girl","first communion","baby blessing"],
       fields="name, baptism date, church, verse", hook="Name, date, church and a chosen verse, in a print that stays on the wall long after the day.",
       details="- Name, baptism date, church and godparents\n- Choice of verse or your own words\n- Soft neutral palettes", personalization="Child's name, date, church, godparents, verse", mockups=["nursery scene", "flat lay", "size guide"]),
  dict(slug="memorial_print", launch="2026-11-10", entry=32.41, keyword="memorial gift", searches=6600, lps=90.8, si=1.84,
       title="Memorial Gift Print, In Loving Memory Personalized Photo and Poem, Sympathy Keepsake",
       tags=["memorial gift","in loving memory","sympathy gift","remembrance gift","loss of mother","loss of father","memorial print","bereavement gift","custom memorial","photo memorial","condolence gift","grief gift","memorial keepsake"],
       fields="name, dates, photo, poem or words", hook="A gentle place for a photo, the dates and the words that are hardest to say.",
       details="- Photo repainted or kept as a photograph\n- Name, dates and a poem or your own words\n- Proof sent before printing, changes included", personalization="Name, dates, chosen poem or words; upload photo after purchase", mockups=["flat lay", "mantel scene", "size guide"]),
  dict(slug="pet_memorial", launch="2026-11-10", entry=28.95, keyword="pet memorial", searches=6600, lps=69.0, si=1.24,
       title="Pet Memorial Portrait Print, Personalized Dog Cat Loss Gift with Name and Dates",
       tags=["pet memorial","pet loss gift","dog memorial","cat memorial","rainbow bridge","pet sympathy gift","memorial portrait","pet remembrance","custom pet gift","dog loss gift","paw print memorial","pet keepsake","in memory of pet"],
       fields="pet name, dates, photo", hook="Their portrait from your favourite photo, with their name, their dates and a line of their own.",
       details="- Portrait in watercolour or line-art style\n- Name, dates and a short line\n- Proof before printing", personalization="Pet name, dates, optional line; upload photo after purchase", mockups=["flat lay", "shelf scene", "size guide"]),
 ]},
}
