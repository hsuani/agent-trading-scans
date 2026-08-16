# Final decision — QBTS as of 2026-08-11

FINAL TRANSACTION PROPOSAL: **SELL**

## FINAL TRANSACTION PROPOSAL: **SELL**
（表達方式：定義風險之 Put Debit Spread；現有股票部位一律清倉，不建立任何多頭）

## Verdict
MODIFY — 採納 neutral 的條件式 Put Spread 架構，否決 aggressive 的直接空頭與催化劑前進場，同時否決 conservative 的全面零倉位。

## Final trade card
| Field | Value |
|---|---|
| Direction | SHORT（QBTS Nov-2026 $20 / $10 Put Debit Spread，僅選擇權，禁止裸空股票） |
| Entry zone | **無即時價格，暫不給進出場價位**；僅設條件：2026-08-15 CHIPS 條款以中性至負面落地後，標的位於 $21–23 區間方可建倉 |
| Stop | N/A — 最大損失鎖定為已付 premium，無滑點與缺口跳倉風險 |
| Target 1 | 標的 $16（spread 市值約 $10,000） |
| Target 2 | 標的 $10（spread 全額兌現 $25,000） |
| Size | Small — 0.75% NAV premium 上限（$1M NAV 基準即 $7,500） |
| Horizon | 90 天，以 2026-11 Q3 財報背訂單轉化率為核心驗證點 |
| Conviction | M |
| R:R to T1 | 0.3（+$2,500 / −$7,500）；R:R to T2 = 2.3 |

**執行紀律**：T1 不是獲利了結點，本結構的正期望值全部來自 T2；若 Aug-15 後標的未回落至 $23 以下，本次視窗作廢，不追價。禁止在 2026-08-15 前建立任何部位。

## Risk debate adjudication
- Aggressive 最強論點：三重熊證（Forward P/S 355x、FY2026 年化營收年減約 50%、CEO/CFO 淨售 $1.74M）同時成立，純迴避等同浪費研究結論；且 Put Spread 確實封頂了尾部風險。
- Conservative 最強論點：PRICE_DATA_UNAVAILABLE 下沒有可核驗的 ATR 與借券成本，止損無執行保障；Aug-15 CHIPS 與 Sep 17-qubit 兩個正面催化劑落在 35 天內，缺口機率 27–47%。
- Net：**我採 neutral 的權重最高**。Conservative 的缺口與止損反對意見對「直接空頭」完全成立，因此 aggressive 的 1.5% NAV 裸空被整段刪除；但同一套邏輯不適用於 Put Spread——最大損失即 premium，缺口只影響未兌現收益，不會擴大虧損。Conservative 將定義風險工具與無限風險工具等同處理，是本次辯論中唯一的邏輯錯誤。Neutral 同時解決了三項疑慮：Put Spread 解缺口、Aug-15 後進場解催化劑時序、0.75% NAV 解 ATR 未知。

## Monitoring trigger
若 2026-08-15 CHIPS 條款披露**不含不利控制權安排且明確載明政府算力採購金額**，或標的日收盤價站上 $28，則本次空頭論點的時程假設被證偽——立即取消進場；若已建倉，於次一交易日以市價平倉 spread，不等 premium 歸零。

## Catalyst calendar
- 2026-08-15 — CHIPS Act 量子條款落地／條件披露（進場前置條件）
- 2026-09（預期）— 17-qubit 超導閘極系統交付與客戶驗收
- 2026-11（預期）— Q3 2026 財報，背訂單轉化率決定是否持有至到期

FINAL DECISION COMPLETE
