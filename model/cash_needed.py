# Deterministic cash-at-completion table using the model's own deal-sizing rules (mc_model.py lines 208-221)
def annuity(P, r, n): return P * r / (1 - (1 + r) ** -n) if r else P / n
def deal(ev, mult, vn_share, bank_term=10, bank_rate=0.11, vn_rate=0.05, vn_term=4, mgr=20000, dscr=1.3, pg_share=0.35, max_x=2.0, deal_costs=20000, wc=0.10, bank_share=0.6, risk_pot=None):
    e0 = ev / mult; vendor = ev * vn_share; gap = ev - vendor
    vs = annuity(vendor, vn_rate, vn_term); bank_af = annuity(1.0, bank_rate, bank_term)
    caps = {"lender share of gap": gap * bank_share, "2x EBITDA": e0 * max_x, "DSCR 1.3": max(((e0 - mgr) / dscr - vs) / bank_af, 0)}
    if risk_pot is not None: caps["PG cap (risk pot / 0.35)"] = risk_pot / pg_share
    bank = min(caps.values()); binding = min(caps, key=caps.get)
    equity = gap - bank + deal_costs + ev * wc
    yr1_service = vs + bank * bank_af
    draw = e0 - mgr - yr1_service
    return dict(ev=ev, ebitda=e0, vendor=vendor, bank=bank, binding=binding, equity=equity, pg=bank, service=yr1_service, draw=draw)
rows = [
 ("Surrey HVAC as listed: £295k, 3.1x, 35% VN", 295000, 3.1, 0.35),
 ("Surrey HVAC negotiated: 2.3x on same profit (£221k), 50% VN", 221000, 2.3, 0.50),
 ("London EICR as listed: ~£500k, 3.0x, 35% VN", 500000, 3.0, 0.35),
 ("London EICR negotiated: 2.3x on £167k (£385k), 50% VN", 385000, 2.3, 0.50),
 ("Same, seller-funded 80% VN", 385000, 2.3, 0.80),
 ("Model median deal: £300k, 2.6x, 50% VN", 300000, 2.6, 0.50),
]
print(f"{'Deal':62s} {'EBITDA':>7s} {'VN':>6s} {'Bank':>6s} {'binding':>24s} {'CASH':>6s} {'PG':>6s} {'yr1 svc':>7s} {'draw':>6s}")
for name, ev, m, vn in rows:
    d = deal(ev, m, vn)
    print(f"{name:62s} {d['ebitda']/1e3:6.0f}k {d['vendor']/1e3:5.0f}k {d['bank']/1e3:5.0f}k {d['binding']:>24s} {d['equity']/1e3:5.0f}k {d['pg']/1e3:5.0f}k {d['service']/1e3:6.0f}k {d['draw']/1e3:5.0f}k")
print("\nCASH = cash paid at completion (equity + £20k deal costs + 10% of EV working capital). PG = personal guarantee on the bank loan (35% of facility typical).")
print("Floor rule: cash above floor must cover CASH, and risk pot must cover PG x 0.35. With floor £60k and ~£160k start + 2 years of 3-day contracting, cash above floor at 2029 ≈ £150-200k in the median path.")
