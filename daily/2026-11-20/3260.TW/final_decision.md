# Final decision — 3260.TW as of 2026-11-20

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
Phase-1-only stub（未進入 Phase 2-4）

## 說明
3260.TW（威剛）於 Phase 1 評分未達 positive-pick 門檻（5 項訊號中僅 1 項勉強成立），且基本面報告為 DATA_UNAVAILABLE（yfinance 財務三表、現金流、資產負債表、內部人與股東資料全數連線失敗，403）。依 mode=plan_all 規則，非 positive pick 的 ticker 僅作 Phase-1-only stub，不進入 bull/bear debate、trader、risk debate 或 portfolio-manager 決策。

### Phase-1 訊號檢查（5 項取 ≥3 才算 positive pick）
| 訊號 | 結果 | 判定 |
|---|---|---|
| Fundamentals (YoY>15% 且 FCF/NI>-1) | 無資料可驗證（DATA_UNAVAILABLE） | 不通過 |
| Market (RSI<72 且 MACD 未深度負值 且 price>MA50) | RSI 18.66 可通過，但 MACD hist -5.21 深度負值、價格遠低於 MA50 (234 vs 349.9) | 不通過 |
| News (淨傾向正面) | 中性偏空，強度中等（毛利率不及預期、買回取消、NAND 現貨下跌） | 不通過 |
| Sentiment (分析師 ≥60% buy 或機構流向淨正) | 僅 1 筆當期評等（玉山 增持），樣本過少、置信度低 | 勉強/不採計 |
| Valuation (forward P/E<35x 或 EPS 催化劑確認) | 無法驗證（基本面資料缺失） | 不通過 |

**無即時可驗證之財務資料，暫不給進出場價位。** 本 ticker 未持倉（不在 held_tickers.txt），故不適用加碼/減碼框架。

## 論點支柱
- 產業面（記憶體缺貨敘事延續至 2027）：觀察中，缺乏公司自身財務資料佐證。
- 股價技術面：已失效（空頭排列，死亡交叉已成立，屢創新低）。

## 論點失效條件（若要重新評估為 positive pick）
- yfinance 對 3260.TW 的連線恢復，可取得財務三表、earnings_dates、insider 資料。
- 股價止跌並重新站回 MA50 (約 349.9) 以上。
- 出現至少 2 家以上機構於近 30 天內給出評等，形成可統計的 analyst consensus。

## 建議
下次排程時優先重新抓取 3260.TW 基本面資料；若資料恢復且技術面同步改善，可重新評分進入 Phase 2-4。

FINAL DECISION (STUB) COMPLETE
