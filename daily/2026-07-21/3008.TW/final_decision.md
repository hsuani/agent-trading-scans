# Final decision — 3008.TW 大立光 as of 2026-07-21

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | **無即時價格，暫不給進出場價位**（事件驅動分批建倉） |
| Stop | 事件型停損（見下方 Invalidation） |
| Target 1 | Citi 5,325 NTD（情境估算，未驗證錨點） |
| Target 2 | Goldman 6,231 NTD（情境估算，未驗證錨點） |
| Size | Small：初始 0.25% NAV → 最高 0.75% NAV |
| Horizon | 3–6 個季度；Q3 法說（2026-10）為中期檢查點 |
| Conviction | M |
| R:R to T1 | 不可量化（PRICE_DATA_UNAVAILABLE，ATR 不可得） |

## 建倉與加碼條件（事件驅動）
- **啟動 0.25% NAV**：7 月月營收（2026-08-10 前）MoM 正成長。
- **加至 0.50% NAV**：8 月月營收（2026-09-10 前）確認第二個月 MoM 正成長。
- **解鎖第三檔至 0.75% NAV（三項須同時滿足）**：① 即時股價驗證並算出有效 ATR；② 8、9 月連續 MoM 正成長；③ CPO 試產線 Q3 底如期完工公告。
- 部位超過 0.50% NAV 時，買入小量 TAIEX Puts 尾部保護（預算 ≤ 0.05% NAV）。
- 不採原提案「條件 3」現價試倉：股價未驗證，不建錨點。

## Invalidation（任一觸發即出清）
- 連續兩個月 MoM 萎縮，或管理層 Q3 法說明確下調 Q4 展望。
- CPO 試產線延至 2027 Q1 後完工，或主要客戶訂單取消。
- FY2026 EPS 指引低於 155 NTD。

## Risk debate adjudication
- Aggressive 最強點：Goldman 升評剛發生、CPO 首張量產訂單稀缺，先行者確有 Alpha 窗口。
- Conservative 最強點：ATR 不可得使任何 NAV% 都隱含未知每股風險；6 月營收 YoY -10% 是已實現硬數據，非指引。
- Net：我採 **neutral** 為主。激進方 R:R 2.1:1 以未知損失做分母，邏輯自相矛盾；保守方「全面凍結」則否定了事件停損架構本身。中性方將「價格未驗證（技術問題，靠事件停損解）」與「基本面不確定（靠分批節奏解）」分開處理，最貼合 PRICE_DATA_UNAVAILABLE 現實。0.25%→0.75% 的階梯把尾部風險壓在約 −0.075% NAV（初始倉情境 A）。

## Monitoring trigger
若 7 月月營收（2026-08-10 前）仍 MoM 萎縮，則「8 月優於 7 月」指引已破，需在任何加碼前重新評估核心論文，不等停損事件。

## Catalyst calendar
- 2026-08-10 前 — 7 月月營收（動能是否啟動）
- 2026-09-10 前 — 8 月月營收（第二個月 MoM 驗證）
- 2026-09-30 前 — CPO 試產線完工里程碑
- 2026-09 — iPhone 18 Pro 發布
- 2026-10 — Q3 法說：全年 EPS 指引與 Q4 展望
- 2027-Q1 — iPhone 18 標準版拉貨、CPO 首次財務披露

## FINAL SCORE
- verdict_weight = 1.0（BUY）
- conviction_pct = 0.55（信念 MEDIUM，多方 7/10、6 月硬數據與價格不可得壓抑上限）
- R:R T2 = 0（no price data）
- phase_modifier = 1.0
- **Score = 1.0 × 0.55 × (1 + 0) × 1.0 × 100 = 55.0**

FINAL DECISION COMPLETE
