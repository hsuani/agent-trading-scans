# Final decision — 6217.TWO as of 2026-11-20

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
Phase-1-only stub（未進入 Phase 2-4）

## 說明
6217.TWO（中探針）於 Phase 1 評分未達 positive-pick 門檻（5 項訊號中僅 1 項通過：估值）。依 mode=plan_all 規則，非 positive pick 的 ticker 僅作 Phase-1-only stub，不進入 bull/bear debate、trader、risk debate 或 portfolio-manager 決策。

### Phase-1 訊號檢查（5 項取 ≥3 才算 positive pick）
| 訊號 | 結果 | 判定 |
|---|---|---|
| Fundamentals (YoY>15% 且 FCF/NI>-1) | 營收 FY2025 YoY +19.1% 通過，但淨利與 FCF 持續為負（TTM 淨利率 -1.0%），非健康獲利結構 | 不通過 |
| Market (RSI<72 且 MACD 未深度負值 且 price>MA50) | RSI 25.98 可通過，但 MACD hist -3.28、價格遠低於 MA50 (85.9 vs 156.76) | 不通過 |
| News (淨傾向正面) | "Net headline tilt is BEARISH, medium-high magnitude" | 不通過 |
| Sentiment (分析師 ≥60% buy 或機構流向淨正) | yf 無分析師覆蓋（recommendationKey none），無法確認 | 不通過 |
| Valuation (forward P/E<35x 或 EPS 催化劑確認) | Forward P/E 21.6x（但建立在未經核實的 forwardEps 3.98 上） | 通過 |

**無法給出進出場價位（未進入 trader 階段）。** 本 ticker 未持倉（不在 held_tickers.txt）。

## 論點支柱
- 營收成長：成立（2026Q2 YoY +38.8%）。
- 獲利能力：已失效（連續多年營業利益與淨利為負）。
- 技術面：已失效（跌停，空頭排列，跌破所有均線）。
- 財務槓桿：已失效（淨負債/EBITDA 約 7 倍，流動借款佔比高）。

## 論點失效條件（若要重新評估為 positive pick）
- 營業利益與淨利轉正並維持至少兩季。
- 股價止跌並重新站回 MA50 (約 156.76) 以上。
- 2026Q3 財報公布並確認槓桿與現金流狀況未進一步惡化。

FINAL DECISION (STUB) COMPLETE
