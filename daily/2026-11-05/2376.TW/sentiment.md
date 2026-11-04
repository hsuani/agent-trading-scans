# Sentiment: 2376.TW (技嘉) as of 2026-11-05

**Status:** Partial. Analyst data is from the yf tool. Reddit, StockTwits, and insider data are unavailable. Retail tilt is not measured.

**Date check:** The environment date is 2026-11-04 and the requested as-of date is 2026-11-05. Nothing dated 2026-11 was found in any source, so the freshest data is around October 2026.

## Analyst consensus
12 analysts: 9 buy (3 strong buy + 6 buy) / 3 hold / 0 sell. Buy share is 75%.
- The yf `rec_summary` counts are identical for the 0m, -1m, and -2m periods. This suggests a stale snapshot or no change in coverage, not a verified trend.
- The yf `recommendations` tool returned only period counts, not individual upgrade or downgrade events. The recent moves below come from news search and are not verified against a broker source.
- Recent moves (news search):
  - Early June 2026: a US-based foreign broker raised its target from 299 to 487 after Computex. The rating was reported as 中立 (neutral). A 487 target with a neutral rating is inconsistent with the 75% buy share in the aggregate, and this is not reconciled.
  - Late June 2026: a domestic investment advisory reiterated 買進 with a 440 target. It cited a year-to-date gain above 38% and FY26-27 EPS of about 3 TWD, with a P/E near 11x.
  - Older aggregate cited in news: average target about 457.67 TWD from 12 analysts. This is undated and may be stale.
- Excluded as stale: 2024-11 broker targets (MS 400, CLSA 410, Nomura 378, Daiwa 390).

## Retail social
- **Reddit (r/wallstreetbets, r/stocks):** Blocked (WebFetch could not reach reddit.com). No posts sampled. Tilt: unknown.
- **StockTwits:** Blocked (api.stocktwits.com does not resolve in this session). Also, the ticker is a Taiwan listing, so coverage is likely thin.
- **PTT Stock board:** No threads surfaced in search. Not sampled.
- **News and web chatter (proxy for crowd tone, not retail posts):** Mostly positive. Themes are AI server share and the 2026 shareholder meeting outlook from the chairman, who said orders are visible through the second half and into next year.
- **Buzz volume:** Cannot quantify. No mention counts were available.
- **Themes (from news):**
  - AI server share: about 80% of revenue per an October 2026 report. Dec 2025 revenue was 303億 TWD, up 72% YoY.
  - Valuation gap versus peers: P/E near 11-14x per the sources.
  - Memory cost pressure on the motherboard and notebook margins. Management says it has largely passed this through.
  - AI PC planned for 2027 Q1.
  - Chairman's view that the stock is undervalued. The stock traded in a 223-320 TWD range over the past three years per the article.
- **Risk note:** One scoring site rated the company low on a screen (17% pass rate). It is a conservative, low-weight signal.

## Insider activity
Net 6mo: **no data returned**. The yf `insider` tool returned an empty list, and the Yahoo cookie and crumb fetch failed in this session. An empty result may be a tool failure rather than zero insider trading. Treat as unknown, not as zero.
- Ownership snapshot (yf `major_holders`): insiders hold 18.9%, institutions hold 37.2% (45.9% of float), institution count 178. This is a single snapshot, so no ownership-shift trend is available.

## Net sentiment score
**Composite: bullish, low confidence.**
- Analyst tilt: bullish (75% buy, no sells). Target-price trend is up from early-June data. Data is partly stale.
- Retail tilt: not measured. Reddit and StockTwits were blocked. Press tone is positive.
- Insider tilt: unknown.
- Price reference: 363 TWD close on 2026-10-08. No November price was found, so price context is incomplete.

**Divergence flag: no (cannot confirm).** Retail tilt is not measured, so an analyst-versus-retail divergence cannot be assessed.

## Unit note
TWD amounts are in 億 (for example 303億 TWD December 2025 revenue). No USD figures were used and no 億-versus-B mixing occurs.

## Sources (news and web, accessed this run)
- [yf tool outputs: recommendations, rec_summary, insider, major_holders] (local pipeline)
- [ctee.com.tw, 2026-06-05 foreign broker target raise](https://www.ctee.com.tw/news/20260605700981-430201)
- [wantrich.chinatimes.com, 2026-06-22 domestic advisory 440 target](https://wantrich.chinatimes.com/news/20260622900002-420101)
- [statementdog.com/analysis/2376, 2026-10-08 close 363 TWD](https://statementdog.com/analysis/2376)
- [moneyweekly.com.tw, AID=207444](https://www.moneyweekly.com.tw/_Article?AID=207444)
- [pocket.tw, company overview](https://www.pocket.tw/school/articles/6670/)
- [statementdog.com/news/15019, Q3 earnings and order visibility](https://statementdog.com/news/15019)

SENTIMENT REPORT COMPLETE
