# Deal sheet: Hornblower HMD242 (London electrical testing) + comparators. Model rules as mc_model: VN 4y@5%, bank 10y@11%, deal costs £20k, WC 10% EV.
def ann(P,r,n): return P*r/(1-(1+r)**-n)
def sheet(label, ebitda, mult, vn_share, bank_share=0.6, mgr=0, dscr=1.3, pg=0.35, max_x=2.0, costs=20000, wc=0.10, stress=None):
    ev=ebitda*mult; vn=ev*vn_share; gap=ev-vn
    vs=ann(vn,0.05,4); bank=min(gap*bank_share, ebitda*max_x, max(((ebitda-mgr)/dscr-vs)/ann(1,0.11,10),0)); bs=ann(bank,0.11,10)
    cash=gap-bank+costs+ev*wc
    rows=[]
    for y in range(1,8):
        e=ebitda if stress is None else stress(y, ebitda)
        svc=(vs if y<=4 else 0)+bs
        pre=e-mgr-svc; rows.append((y,e,svc,pre,pre*0.69))
    print(f"\n{label}\n  price £{ev/1e3:.0f}k = {mult}x £{ebitda/1e3:.0f}k | vendor note £{vn/1e3:.0f}k (4y@5%) | bank £{bank/1e3:.0f}k (10y@11%) | CASH IN £{cash/1e3:.0f}k | PG ~£{bank*pg/1e3:.0f}k | DSCR yr1 {(ebitda-mgr)/((vs+bs) or 1):.2f}")
    print("  yr  EBITDA  debt svc  pre-tax to you  after tax(31%)")
    for y,e,svc,pre,post in rows: print(f"  {y:2d}  {e/1e3:5.0f}k   {svc/1e3:5.0f}k      {pre/1e3:6.0f}k        {post/1e3:6.0f}k")
    print(f"  7-yr after-tax cash to you £{sum(r[4] for r in rows)/1e3:.0f}k on £{cash/1e3:.0f}k in; business still owned (resale ~{2.5}x EBITDA ≈ £{2.5*rows[-1][1]/1e3:.0f}k)")
E5=(181042+140657+114912+129090+166821)/5
print(f"HMD242: EBITDA 2020-24 = 181/141/115/129/167k; 5-yr avg £{E5/1e3:.0f}k; 2022 trough £115k; adj EBITDA already includes directors' replacement cost (verify figure used)")
sheet("A. As a broker would price it: 3.0x on 2024 EBITDA £167k, 35% VN", 166821, 3.0, 0.35)
sheet("B. Negotiated: 2.3x on 5-yr average £146k, 50% VN", E5, 2.3, 0.50)
sheet("C. Seller-funded: 2.3x on 5-yr avg, 70% VN", E5, 2.3, 0.70)
sheet("D. Stress on B: EBITDA drops to 2022 level (£115k) in yrs 1-2, recovers to £146k", E5, 2.3, 0.50, stress=lambda y,e: 115000 if y<=2 else e)
sheet("E. Stress on B + you hire an ops manager anyway (£40k) because 3 days/wk", E5, 2.3, 0.50, mgr=40000, stress=lambda y,e: 115000 if y<=2 else e)
print("\n--- comparators, negotiated 2.3x, 50% VN ---")
sheet("P6 London/East: 2.3x on £175k (shareholders stay)", 175000, 2.3, 0.50)
sheet("P2 London/SE: 2.3x on £103k adj EBIT (owner likely on tools -> add £45k engineer)", 103000, 2.3, 0.50, mgr=45000)
sheet("P3 Bucks: 2.3x on £110k adj EBIT (50% margin on £215k T/O = owner IS the electrician; add £50k)", 110000, 2.3, 0.50, mgr=50000)
