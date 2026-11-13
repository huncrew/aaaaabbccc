"""Score product lines on REAL sales data collected in the browser (browser_findings.csv, schema = candidates_template.csv).
Usage: python3 score_lines.py [browser_findings.csv] -> ranked.csv + printed table. Blank fields are skipped, never guessed.
Score /100: demand 30 (units actually sold), openness 25 (not dominated: seller share, click share, review moat), margin 25 (after fees, at the real sold price),
capital/ease 10 (MOQ value, no hazmat/cert), momentum 10 (search growth, successful launches). Kill: Amazon is a seller, margin < 25%, top seller > 60%."""
import csv, sys, math
def f(r,k):
    try: return float(str(r.get(k,"")).replace(",","").replace("%","").replace("£",""))
    except: return None
def band(x, lo, hi): return None if x is None else max(0.0, min(1.0, (x-lo)/(hi-lo)))
def avg(xs): xs=[x for x in xs if x is not None]; return sum(xs)/len(xs) if xs else None
rows=list(csv.DictReader(open(sys.argv[1] if len(sys.argv)>1 else "browser_findings.csv"))); out=[]
for r in rows:
    landed=f(r,"landed_cost_gbp"); ep=f(r,"ebay_avg_sold_price_gbp"); ap=f(r,"amz_avg_price_gbp")
    em = None if None in (ep,landed) else (ep/1.2 - landed - (f(r,"ebay_fvf_pct") or 12.9)/100*ep - 0.30 - 2.50)/(ep/1.2)      # ex-VAT, £2.50 3PL pick+post
    am = None if None in (ap,landed) else (ap/1.2 - landed - (f(r,"amz_referral_pct") or 15)/100*ap - (f(r,"amz_fba_fee_gbp") or 3.2))/(ap/1.2)
    margin=max([m for m in (em,am) if m is not None], default=None)
    eu=f(r,"ebay_sold_90d"); au=f(r,"amz_units_sold_90d")
    demand=avg([band(math.log10(eu+1) if eu is not None else None,1.5,4.0), band(math.log10(au+1) if au is not None else None,2.5,5.0)])
    ts=f(r,"ebay_top_seller_share_pct"); cs=f(r,"amz_top5_click_share_pct"); rv=f(r,"amz_avg_review_count_top")
    openness=avg([None if ts is None else 1-band(ts,15,60), None if cs is None else 1-band(cs,30,80), None if rv is None else 1-band(math.log10(rv+1),2.0,3.7)])
    moqv=None if None in (landed,f(r,"moq")) else landed*f(r,"moq")
    ease=avg([None if moqv is None else 1-band(moqv,200,4000), 0.3 if r.get("hazmat_or_cert","").strip() else 1.0])
    nl=f(r,"amz_new_products_launched_180d"); sl=f(r,"amz_successful_launches_180d")
    momentum=avg([band(f(r,"amz_search_growth_90d_pct"),-10,40), None if not nl else band(sl/nl if sl is not None else None,0,0.4)])
    parts={"demand":(demand,30),"openness":(openness,25),"margin":(band(margin,0.25,0.6),25),"ease":(ease,10),"momentum":(momentum,10)}
    have=sum(w for v,w in parts.values() if v is not None); score=sum(v*w for v,w in parts.values() if v is not None)/have*100 if have else None
    kills=[k for k,c in [("Amazon is a seller", r.get("amz_amazon_is_seller","").lower().startswith("y")),("margin under 25%", margin is not None and margin<0.25),("top seller over 60%", ts is not None and ts>60)] if c]
    monthly_gp=None if margin is None else margin*avg([None if eu is None else eu/3*ep/1.2*0.05, None if au is None else au/3*ap/1.2*0.03])  # a 5% eBay / 3% Amazon unit share
    out.append({"line":r["line"],"score":None if score is None else round(score,1),"data_coverage_pct":have,"best_margin":None if margin is None else round(margin,3),"ebay_sold_90d":eu,"amz_units_90d":au,"gp_month_at_small_share_gbp":None if monthly_gp is None else round(monthly_gp),"kill":"; ".join(kills)})
for o in out:
    if o["data_coverage_pct"]<50 and not o["kill"]: o["kill"]="NEEDS DATA (under 50% of fields filled)"; 
out.sort(key=lambda o:(o["kill"].startswith("NEEDS"), bool(o["kill"]), -(o["score"] or -1)))
with open("ranked.csv","w",newline="") as fo: w=csv.DictWriter(fo,fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
for o in out: print(f"{o['line'][:44]:44s} score={o['score']} cover={o['data_coverage_pct']}% margin={o['best_margin']} eBay90d={o['ebay_sold_90d']} amz90d={o['amz_units_90d']} GP/mo@small share=£{o['gp_month_at_small_share_gbp']} {('KILL: '+o['kill']) if o['kill'] else ''}")
