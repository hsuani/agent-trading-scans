FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 2376.TW as of 2026-09-10

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

（2376.TW 不在 held_tickers.txt，按新倉框架裁決。）

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE — 執行前以 TWSE 即時報價為錨，限價單不追價超過當日開盤 +2% |
| Stop | 入場價 -10%（收盤價判定） |
| Target 1 | 入場價 +18%（出一半倉） |
| Target 2 | 入場價 +40% |
| Size | Medium — 總上限 1.5% NAV（首批 0.75%，第二批 0.75% 需通過門檻） |
| Horizon | 1–3 個月，核心裁定點為 Q3 財報與 10 月法說會 |
| Conviction | M |
| R:R to T1 | 1.8 |

**對 trade proposal 的三項修改：**
1. 第二批 0.75% NAV 的門檻由「Q3 毛利率 ≥13%」收緊為**同時**滿足毛利率 ≥12.5% 與月營收維持 NT$45 億以上；單一條件達標不得補倉。
2. 刪除 aggressive 提出的 call spread —— TWSE 個股選擇權對 2376.TW 的流動性未經驗證，不可執行的工具不進交易卡。
3. 不強制 SOX／TSM puts 對沖。組合目前持有 MRVL、ANET、COHR、3017.TW，AI 供應鏈暴露確實存在，但對沖成本未量化即侵蝕 R:R；改以 1.5% NAV 的絕對上限控管板塊集中度。

## Risk debate adjudication
- Aggressive's strongest point: 倉位應匹配已驗證的定價錯誤幅度。forward P/E 約 11.7× 對應 EPS 年增 93%，三項支柱（月營收、EPS 軌跡、NVIDIA 官方指名）都是已公告事實而非預測。
- Conservative's strongest point: -10% 停損落在 -3%（分析師低位）與 -23%（熊市估值）之間的無支撐真空帶，財報跳空時停損大概率失效。
- Net: 我採 neutral 的權重最高。原因是 conservative 指出真空帶問題正確，但它自己提的 -7% 同樣在真空帶內，邏輯自相矛盾；aggressive 的 -15% 也一樣。既然停損位置在缺乏技術面數據時無法最佳化，正確的控管工具是**倉位上限**而非停損寬窄——這正是 neutral 的結論。aggressive 要求 2.5% NAV 在 FCF 與負債結構皆為 DATA_UNAVAILABLE 的情況下，等於把已知利多與未知利空不對稱處理，不予採納。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 伺服器營收動能 | 月營收 NT$45–55 億、YoY 維持高增 | 8 月 NT$47.4 億，+98.4% YoY；累計 +55.2% | 成立 |
| Vera Rubin 供應鏈地位 | 取得指名製造商資格並放量 | NVIDIA 官方新聞稿列名，已對接 CoreWeave／Azure／Google Cloud | 成立 |
| 毛利率改善路徑 | H2 毛利率脫離 10–11% 區間 | H1 僅 10.63%，Q1 12.01% 後回落 | 觀察中 |
| 估值安全邊際 | 全年 EPS 達 NT$30、forward P/E 11.7× | H1 EPS 17.73 已達成一半，H2 未驗證 | 觀察中 |

## 論點失效條件
- 若 Q3 毛利率低於 10%，毛利率改善支柱失效 → 出場（全部）
- 若 NVIDIA 公告 Vera Rubin 出貨遞延至 2027 年，供應鏈支柱失效 → 出場（全部）
- 若合併月營收連續兩個月低於 NT$40 億元，營收動能支柱失效 → 減碼至 0.5% NAV
- 若 10 月法說會將全年 EPS 指引下修至 NT$28 以下，估值支柱失效 → 減碼一半
- 若 Morgan Stanley 以外第二家券商降評至 Neutral 或以下，籌碼面裂縫擴大 → 減碼一半

## Monitoring trigger
若 9 月 15 日美台協議生效後兩個交易日內股價**下跌**（利多出盡型賣壓），暫停第二批建倉並重新檢視籌碼結構，不等 -10% 停損被打到。另：每月 10 日前後的合併營收公告為最高頻率的論點檢查點。

## Catalyst calendar
- 2026-09-15 — 美台貿易協議生效，對美關稅 20%→15%
- 2026-09-10 前後 — 8 月合併營收公告（已公布，+98.4% YoY）
- 2026-09 月底 — Q3 財報：毛利率為唯一裁判點
- 2026-10 — Q3 法說會，全年 EPS 指引更新
- 2026-Q4 — Vera Rubin 批量出貨節奏驗證

FINAL DECISION COMPLETE
