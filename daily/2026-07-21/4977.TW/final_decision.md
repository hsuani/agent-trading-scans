# Final decision — 4977.TW as of 2026-07-21

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY（核准做多，但下修規模並鎖定事件驅動觸發，採 neutral 平衡框架）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無即時價格，暫不給進出場價位（Yahoo Finance HTTP 403）。改以事件觸發：第一催化劑（8月月報 5/6月單月營收 MoM 轉正「或」Q2 GM 邊際改善，擇一）確認後次交易日建倉 |
| Stop | 事件驅動 + 硬性時間停損：Q2 財報後 7 個交易日內若 2026 全年 EPS 指引未轉正即全數出場；另品固整合延遲逾一季、或 Broadcom Tomahawk-5 Bailly 量產延遲逾一季，任一觸發即清倉 |
| Target 1 | 2026年9月 Broadcom/NVIDIA CPO 出貨數據確認下半年能見度 + 眾達取得 ELSFP 量產訂單書面確認 → 持倉向 2026E 估值上沿靠攏 |
| Target 2 | 2027 H1 EPS 轉正、台積電 COUPE 產能≥1.5萬片/月、ELSFP 1:32 乘數效應反映訂單簿 → 分批減碼 |
| Size | 初始 Small（0.40% NAV）→ 雙重催化劑確認後 Medium 上限 1.0% NAV |
| Horizon | 1–3m（催化劑節點）+ 3m+（完整 J-curve 需持至 2026 Q4–2027 H1） |
| Conviction | M |
| R:R to T1 | 0（PRICE_DATA_UNAVAILABLE，不作正式計算） |

## Risk debate adjudication
- Aggressive's strongest point：ELSFP 1:32 獨家認證是「已存在的護城河」而非預測，且雙重確認的時序問題真實——市場可能在第一份數據後即重新定價，等第二份等同追高。此點成立，故我接受「第一催化劑擇一即建初始倉」。
- Conservative's strongest point：Q1 EPS -1.18、4月營收 YoY -43%、FCF 負值、28.3億元收購債務，在此財務脆弱度下 1.5% NAV 過大；且空頭 4/10 含 DATA_UNAVAILABLE 偏差，下行尾部被系統性低估。此點成立，故上限由 1.5% 壓至 1.0% NAV，並加硬性時間停損。
- Net：本案我最採納 **neutral** 觀點。它同時修正了 aggressive 的過度暴露（2.0% NAV 在 60% 尾部情境縮損 1.2% NAV，與 MEDIUM conviction 不成比例）與 conservative 的過度壓縮（0.25% 初始倉在組合層面無意義、50% ETF put 對沖工具 beta 相關性不對稱且成本過重）。初始 0.40%、上限 1.0%、7 個交易日硬性時間停損為最佳風險/意義平衡。

## Monitoring trigger
若 8月中旬 Q2 財報揭露 2026 全年 EPS 指引仍為虧損且無具體轉正時間表，或品固四廠整合被財報附註證實落後逾一季——在停損被動觸發前主動全數出場，不留觀察倉。

## Catalyst calendar
- 2026年8月中旬 — Q2（4-6月）財報：GM 環比、EPS、FCF 揭露（Conservative 要求 FCF 須先揭露）
- 2026年8月底 — 5月、6月月營收公告，確認谷底是否已過
- 2026年9月 — Broadcom/NVIDIA CPO 出貨量數據（T1 里程碑）
- 2026年 Q4 — 台積電 COUPE 產能爬坡至 1.5萬片/月確認
- 2027年 H1 — Tomahawk-5 Bailly 全面量產、ELSFP 乘數效應顯現、EPS 轉正確認（T2）

## FINAL SCORE
- verdict_weight = 1.0（BUY）
- conviction_pct = 0.55（MEDIUM：J-curve 題材與 ELSFP 獨家認證具支撐，但 FCF 負值、EPS 虧損、-KY 治理折價、PRICE_DATA_UNAVAILABLE 壓抑信心）
- R:R T2 = 0（無價格數據）
- phase_modifier = 1.0（完整 pipeline）
- **Score = 1.0 × 0.55 × (1 + 0) × 1.0 × 100 = 55.0**

FINAL DECISION COMPLETE
