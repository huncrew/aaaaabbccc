"""7-year multi-channel ecommerce path (2027-2034), 3 days/week, Manuel + PH team, data-led line selection, Amazon/eBay/Etsy/direct.
Anchors: Dale's record (~£25-40k/yr profit avg, main product faded after ~3 yrs); Etsy 11% shops >$5k/mo; Amazon 70% <=$60k rev, 11% >$300k;
ONS online-retail 3-yr survival 35% (here applied per LINE, not per business, since the operator persists); platform shocks 8%/yr/channel.
"""
import numpy as np
rng=np.random.default_rng(11); N=50000; Y=8  # 2027..2034
def lognorm(med,p90,size): s=np.log(p90/med)/1.2816; return rng.lognormal(np.log(med),s,size)
def run(name, p_line=0.55, attempts=2, line_med=20000, line_p90=60000, line_surv=0.75, decay=0.10, p_b2b=0.20, b2b_med=15000,
        scale_thresh=60000, scale_g=0.15, blocks=2, sleeve=0.10, start=160000, burn=20000, show=True):
    profit=np.zeros((N,Y)); lines=[]  # each line: (start_year, plateau)
    line_profit=np.zeros((N,Y)); b2b=np.zeros((N,Y))
    active=np.zeros((N,0)); active_start=np.zeros((N,0),int)
    tot_prev=np.zeros(N)
    for y in range(Y):
        # new line attempts (fewer once profit is high: focus on scaling)
        n_att=np.where(tot_prev>scale_thresh, 1, attempts)
        for a in range(attempts):
            ok=(rng.random(N)<p_line)&(a<n_att)
            plat=lognorm(line_med,line_p90,N)*ok
            active=np.hstack([active,plat[:,None]]); active_start=np.hstack([active_start,np.full((N,1),y)])
        age=y-active_start
        ramp=np.clip((age+1)/2,0,1)                         # half in launch year, full from year 2
        surv=rng.random(active.shape)< (line_surv**np.clip(age-1,0,None))  # survival from year 2 onwards
        fade=(1-decay)**np.clip(age-2,0,None)
        lp=(active*ramp*fade*surv).sum(1)
        # b2b / direct deals
        newb=(rng.random(N)<p_b2b)*lognorm(b2b_med,b2b_med*3,N)
        b2b[:,y]=(b2b[:,y-1]*0.8 if y>0 else 0)+newb
        # platform shock: one channel loses a year -> -35% of line profit that year
        shock=rng.random(N)<(1-(1-0.08)**3)
        lp=lp*np.where(shock,0.65,1.0)
        # scaling: once over threshold, reinvest -> growth
        g=np.where(tot_prev>scale_thresh, 1+scale_g, 1.0)
        tot=(lp+b2b[:,y])*g
        profit[:,y]=tot; tot_prev=tot
    # net worth: contracting blocks + ecommerce profit after tax + index/crypto
    liquid=np.full(N,float(start))
    for y in range(Y):
        blk=np.where(profit[:,y]>80000, max(blocks-1,0), blocks)       # drop a block once ecommerce pays
        inc=blk*28500*0.67 + profit[:,y]*0.69 - burn
        idx=rng.normal(0.055,0.15,N); cry=rng.lognormal(np.log(1.25)-0.5*0.8**2,0.8,N)-1
        liquid=liquid*(1+(1-sleeve)*idx+sleeve*cry)+inc
    biz_value=np.where(profit[:,-1]>50000, profit[:,-1]*2.0, 0)*0.82     # saleable brand at 2x SDE, after tax
    nw=liquid+biz_value
    if show:
        med=np.median(profit,0); p75=np.percentile(profit,75,0); p25=np.percentile(profit,25,0)
        print(f"\n{name}")
        print("  year        "+"  ".join(f"{2027+y}" for y in range(Y)))
        print("  profit p25  "+"  ".join(f"{v/1e3:4.0f}" for v in p25)+"   (£k/yr)")
        print("  profit p50  "+"  ".join(f"{v/1e3:4.0f}" for v in med))
        print("  profit p75  "+"  ".join(f"{v/1e3:4.0f}" for v in p75))
        for t in [30000,60000,100000,150000]:
            print(f"  P(>= £{t/1e3:.0f}k in ANY year)={ (profit>=t).any(1).mean():4.0%}   P(>= £{t/1e3:.0f}k in 2034)={(profit[:,-1]>=t).mean():4.0%}   P(>= £{t/1e3:.0f}k for 3+ yrs)={((profit>=t).sum(1)>=3).mean():4.0%}")
        print(f"  Net worth 2034 (incl. 2 blocks/yr contracting, 10% sleeve, brand value): P(>=750k)={(nw>=750000).mean():4.0%}  P(>=500k)={(nw>=500000).mean():4.0%}  median={np.median(nw)/1e3:4.0f}k")
    return profit, nw
run("A. Dale, data-led, 2 line attempts/yr, lines survive 75%/yr, B2B 20%/yr, scale after £60k")
run("B. Same but lines fade faster (survival 60%/yr) - your pet-art experience", line_surv=0.60)
run("C. Same as A but evergreen, non-seasonal lines (survival 85%/yr, decay 5%)", line_surv=0.85, decay=0.05)
run("D. Same as A, B2B/direct works (40%/yr, £25k median accounts)", p_b2b=0.40, b2b_med=25000)
run("E. Haphazard: p_line 0.4, no B2B, no scaling", p_line=0.40, p_b2b=0.05, scale_g=0.0)
run("F. A with 25% crypto sleeve", sleeve=0.25)
