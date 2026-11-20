import json, os
import mc_model as M
p = M.load_params()
out = json.load(open("results.json"))
out["horizon"] = {}
routes = ["contract_only","contract_heavy","buy_distributor","hybrid_plan","hybrid_2blocks_2y","hybrid_3blocks_2y","hybrid_plan_app","build_services","build_aws_partner","build_ai_app"]
for route in routes:
    out["horizon"][route] = {}
    for yrs in (8, 10, 12):
        r = M.simulate(route, p, n=10000, overrides={"horizon.years": yrs})
        out["horizon"][route][str(2026 + yrs)] = {"p750": r["p_target_by_2034"], "p500": r["p_500k_by_2034"], "nw50": r["nw_percentiles_2034"]["50"], "p_floor": r["p_floor_breached"], "days": r["mean_employed_days_total"]}
    print(route, {k: round(v["p750"], 3) for k, v in out["horizon"][route].items()})
json.dump(out, open("results.json", "w"))

# compact summary for the report writer and the dashboard author
L = []
L.append("# Model results summary (n=20,000 paths per route; fit-adjusted unless stated)\n")
L.append("| route | P(£750k by 2034) fit | raw (fit=1) | P(£500k by 2034) | P(deal closes) | P(£750k given deal) | median NW 2034 | p10 / p90 NW | P(floor breached) | employed days 2027–34 | median draw when operating | mean hrs/wk yr1..yr8 |")
L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
for rt, r in out["routes_fit"].items():
    raw = out["routes_raw"][rt]
    c = r["conditional"]
    pg = "" if c["p_target_given_acquired"] is None else f"{c['p_target_given_acquired']:.0%}"
    L.append(f"| {rt} | {r['p_target_by_2034']:.1%} | {raw['p_target_by_2034']:.1%} | {r['p_500k_by_2034']:.1%} | {r['p_business_acquired']:.0%} | {pg} | £{r['nw_percentiles_2034']['50']:,.0f} | £{r['nw_percentiles_2034']['10']:,.0f} / £{r['nw_percentiles_2034']['90']:,.0f} | {r['p_floor_breached']:.0%} | {r['mean_employed_days_total']:.0f} | £{r['median_owner_draw_when_operating']:,.0f} | {' '.join(f'{h:.0f}' for h in r['mean_hours_by_year'])} |")
L.append("\n## Owner draw by year held (median, hybrid_2blocks_2y): " + ", ".join(f"yr{i+1}: £{d:,.0f}" if d is not None else f"yr{i+1}: n/a" for i, d in enumerate(out["routes_fit"]["hybrid_2blocks_2y"]["conditional"]["median_draw_by_year_held"])))
L.append("\n## Labour sweep (SOT hybrid plan: years of contracting before the search × blocks per year)\n")
L.append("| years before search | blocks/yr | P(£750k) | P(£500k) | P(deal) | median deal year | employed days | P(floor) | median NW |")
L.append("|---|---|---|---|---|---|---|---|---|")
for s in out["sweep_labour"]:
    L.append(f"| {s['years']} | {s['blocks_per_year']} | {s['p750']:.1%} | {s['p500']:.1%} | {s['p_acq']:.0%} | {s['acq_year']} | {s['days']:.0f} | {s['p_floor']:.0%} | £{s['nw50']:,.0f} |")
L.append("\n## Tornado (hybrid_2blocks_2y): P(£750k) at low / high value of each input\n")
L.append("| input | low → P | high → P | base value |")
L.append("|---|---|---|---|")
for k, t in sorted(out["tornado"].items(), key=lambda kv: -abs(kv[1]["p750_high"] - kv[1]["p750_low"])):
    L.append(f"| {k} | {t['low']} → {t['p750_low']:.1%} | {t['high']} → {t['p750_high']:.1%} | {t['base_value']} |")
L.append("\n## What has to be true (cumulative scenarios on hybrid_2blocks_2y)\n")
L.append("| scenario | P(£750k) | P(£500k) | P(deal) | P(£750k given deal) | median NW | employed days |")
L.append("|---|---|---|---|---|---|---|")
for name, s in out["scenarios"].items():
    L.append(f"| {name} | {s['p750']:.1%} | {s['p500']:.1%} | {s['p_acq']:.0%} | {s['p750_given_acq']:.0%} | £{s['nw50']:,.0f} | {s['days']:.0f} |")
L.append("\n## Horizon: P(£750k) by end-2034 (40) / end-2036 (42) / end-2038 (44)\n")
L.append("| route | 2034 | 2036 | 2038 | P(£500k) 2034/2036/2038 |")
L.append("|---|---|---|---|---|")
for rt, h in out["horizon"].items():
    L.append(f"| {rt} | {h['2034']['p750']:.1%} | {h['2036']['p750']:.1%} | {h['2038']['p750']:.1%} | {h['2034']['p500']:.0%} / {h['2036']['p500']:.0%} / {h['2038']['p500']:.0%} |")
open("results_summary.md", "w").write("\n".join(L))
print("summary written")
