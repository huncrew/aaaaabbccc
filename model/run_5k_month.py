"""P(£5k/month profit) within 6/9/12 months from relaunching inside the two existing Etsy shops + Amazon.com + eBay (+ optional direct/B2B line).
Evidence anchors (research_notes/build_from_zero_base_rates.md, Etsy/Amazon survey data):
 - Dale's own record: ~$500k revenue over ~3 years full-time, haphazard, ill = ~$14k/month avg revenue; at 25-30% margin = ~£2.5-3.3k/month profit AVERAGE. £5k/month profit = ~£17-20k revenue/month = ~1.5-2x his historical average run-rate.
 - Etsy: ~11% of active shops > $5k/month revenue; his shops were in that tier. Established shops with 1k+ reviews rank faster than new ones.
 - Amazon: 58% of surveyed sellers profitable within 12 months (survivor-biased -> ~40-45% unconditional); 70% make <= $60k/yr revenue; median product margin 20%.
 - Platform risk: he has already lost one shop; assume ~8%/yr per channel of a suspension/ranking collapse.
"""
import numpy as np
rng = np.random.default_rng(7); N = 50000; MONTHS = 12
def lognorm(med, p90, size): s = np.log(p90/med)/1.2816; return rng.lognormal(np.log(med), s, size)
def scenario(name, p_line, etsy_med, etsy_p90, p_amz, amz_med, amz_p90, p_ebay, p_direct, direct_med, ramp_lo, ramp_hi, platform_pa=0.08):
    profit = np.zeros((N, MONTHS+1))
    # product-line search: up to 2 rounds (months 1-2, then 3-4). line_ok month = month a working line is live
    r1 = rng.random(N) < p_line; r2 = rng.random(N) < p_line
    live = np.where(r1, 2, np.where(r2, 4, 99))
    def channel(p_works, med, p90, start_offset, ramp_lo, ramp_hi):
        works = rng.random(N) < p_works
        plateau = lognorm(med, p90, N) * works
        start = live + start_offset
        ramp = rng.integers(ramp_lo, ramp_hi+1, N)
        shock_month = np.where(rng.random(N) < platform_pa, rng.integers(1, MONTHS+1, N), 99)
        out = np.zeros((N, MONTHS+1))
        for m in range(1, MONTHS+1):
            frac = np.clip((m - start) / ramp, 0, 1)
            out[:, m] = plateau * frac * (m < shock_month)
        return out
    profit += channel(1.0, etsy_med, etsy_p90, 0, ramp_lo, ramp_hi)          # existing ranked shops
    profit += channel(p_amz, amz_med, amz_p90, 1, ramp_lo+1, ramp_hi+2)       # Amazon.com, launches a month after
    profit += channel(p_ebay, 400, 1200, 1, 2, 4)                             # eBay, small
    profit += channel(p_direct, direct_med, direct_med*2.5, 4, 2, 4)          # direct/B2B larger-quantity line
    profit[:, :] *= (live[:, None] < 99)
    hit = profit >= 5000
    p6, p9, p12 = hit[:, 6].mean(), hit[:, 9].mean(), hit[:, 12].mean()
    any12 = hit[:, 1:].any(1).mean()
    three = np.array([(hit[:, m-2] & hit[:, m-1] & hit[:, m]).any() for m in range(3, MONTHS+1)]).any(0) if False else None
    consec = np.zeros(N, bool)
    for m in range(3, MONTHS+1): consec |= hit[:, m-2] & hit[:, m-1] & hit[:, m]
    med12 = np.median(profit[:, 12]); p25, p75 = np.percentile(profit[:, 12], [25, 75])
    print(f"{name:66s} P(>=5k @m6)={p6:4.0%}  @m9={p9:4.0%}  @m12={p12:4.0%}  3 consecutive months by m12={consec.mean():4.0%}  month-12 profit p25/50/75 = {p25/1e3:3.1f}/{med12/1e3:3.1f}/{p75/1e3:3.1f}k")
print("P(£5k/month profit) from relaunch; 3 days/week on it; team in the Philippines; data-led line selection unless stated.\n")
scenario("Dale: experience + ranked shops + team + data-led lines", p_line=0.65, etsy_med=3000, etsy_p90=8000, p_amz=0.5, amz_med=1500, amz_p90=5000, p_ebay=0.6, p_direct=0.25, direct_med=1500, ramp_lo=3, ramp_hi=6)
scenario("  same, haphazard line choice (p_line 0.45) and no Amazon", p_line=0.45, etsy_med=3000, etsy_p90=8000, p_amz=0.0, amz_med=1500, amz_p90=5000, p_ebay=0.6, p_direct=0.15, direct_med=1500, ramp_lo=3, ramp_hi=6)
scenario("  same as Dale but Etsy plateau only back to old average (2.5k)", p_line=0.65, etsy_med=2500, etsy_p90=6000, p_amz=0.5, amz_med=1500, amz_p90=5000, p_ebay=0.6, p_direct=0.25, direct_med=1500, ramp_lo=3, ramp_hi=6)
scenario("  same as Dale, Amazon works like Etsy did (p 0.65, med 2.5k)", p_line=0.65, etsy_med=3000, etsy_p90=8000, p_amz=0.65, amz_med=2500, amz_p90=7000, p_ebay=0.6, p_direct=0.25, direct_med=1500, ramp_lo=3, ramp_hi=6)
scenario("  same as Dale, direct/B2B line lands (p 0.5, med 2.5k)", p_line=0.65, etsy_med=3000, etsy_p90=8000, p_amz=0.5, amz_med=1500, amz_p90=5000, p_ebay=0.6, p_direct=0.5, direct_med=2500, ramp_lo=3, ramp_hi=6)
scenario("Generic new seller, no shops, no team, no record (population)", p_line=0.4, etsy_med=800, etsy_p90=3000, p_amz=0.4, amz_med=800, amz_p90=3000, p_ebay=0.5, p_direct=0.1, direct_med=1000, ramp_lo=5, ramp_hi=9)
