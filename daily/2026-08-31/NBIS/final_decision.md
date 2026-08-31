FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — NBIS as of 2026-08-31

> **價格資料狀態**：PRICE_DATA_UNAVAILABLE。以下所有價位均由 Goldman Sachs 目標價 $328 [UNVERIFIED] 單一錨點推算，皆標記 [UNVERIFIED]。
> **執行閘門**：未取得實時報價前一律不下單。取得報價後須確認落於進場區間（GS anchor −10% ~ −15%）且出現至少一根收盤確認K線，方可執行；若實際報價與錨點推算偏離超過 5%，整份價格架構作廢並重算。

## FINAL VERDICT
**BUY — MODIFY**（新倉，NBIS 不在 held_tickers.txt）
**Conviction：6 / 10**

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $279 – $295 [UNVERIFIED]（GS anchor −15% ~ −10%） |
| Stop | $262 [UNVERIFIED]（GS anchor −20%，收盤價確認） |
| Target 1 | $328 [UNVERIFIED] |
| Target 2 | $394 [UNVERIFIED] |
| Size | Small（3% NAV 初始；Q3 確認後上限 4-5% NAV） |
| Horizon | 3-6 個月，Q3 2026 財報為硬性檢查點 |
| Conviction | M（6/10） |
| R:R to T1 | 1.6（進場中點 $287） |

附帶：可配置 0.5% NAV 的 OTM put（到期涵蓋 Q3 財報）對沖 Meta 削單跳空風險。此為選配，不改變主倉尺寸。

## Risk debate adjudication
- **Aggressive 最強論點**：EV/EBITDA 3.8-4.2x 對應 454% YoY 成長，與同業 8-12x 的落差不是噪音，且 $13B+ 積壓訂單是硬收入能見度；催化劑行情不會給第二次回調窗口。
- **Conservative 最強論點**：ATR 不可量化、17.1% 空頭利率、C-suite 64 筆賣出零買入三者疊加，任一負面事件在跳空情境下讓止損計算值失真 2-3 倍。
- **Net**：我採納 **neutral** 較多。Aggressive 要求放寬止損至 −25% 是自相矛盾——他自己承認空頭瀑布風險，卻把止損放到瀑布下方；而 −5%~−8% 進場等於買在分析師目標價旁邊，沒有安全邊際。Conservative 的 2% NAV 與 −17% 止損則在正確方向上缺乏回報能力，且 −17% 對單月 +51% 的標的必被洗出。3% NAV + −20% 止損 + 回調進場閘門是唯一同時尊重「錯誤定價存在」與「驗證尚未發生」兩個事實的組合。加碼權留給 Q3 財報，不留給敘事。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Meta 合約與 $13B+ 積壓訂單 | 合約完整、無提前終止 | 未見削單或終止公告 | 成立 |
| 估值折價（EV/EBITDA 3.8-4.2x） | 相對同業 8-12x 存在 2-3x 重估空間 | 折價仍在，但重估未啟動 | 成立 |
| CapEx 見頂 / FCF 轉正路徑 | Q3 CapEx/Revenue 季環比收窄 | 尚無 Q3 數據 | 觀察中 |
| 內部人行為 | 管理層與股東利益一致 | CIO 六個月套現 $115.7M、64 筆賣出零買入 | 觀察中（偏負面） |

## 論點失效條件
（與 Stop 分開；論點先壞不必等價格觸及 $262）
- 若 Meta 公告自建集群取代 NBIS 合約，或啟動提前終止條款 → 支柱一失效 → **立即出場**（不等 Stop）。
- 若 Q3 2026 CapEx/Revenue 比率 >80% 且未較 Q2 收窄，或 EBITDA 邊際率 <40% → 支柱三失效 → **減碼至 1% NAV 以下**。
- 若未來 90 天 SEC 申報顯示新增內部人賣出 >$50M 且零買入 → 支柱四失效 → **減碼一半**。
- 若美國對 NBIS 適用 GPU 出口許可限制，或 NVIDIA $2B 夥伴關係公告中止 → 支柱一、二同時受損 → **出場**。

## Monitoring trigger
若實時報價未回落至 $295 [UNVERIFIED] 以下即進入 Q3 財報週，取消本次進場，財報後重新評估；不追高。若空頭利率自 17.1% 單週下降超過 4 個百分點（軋空啟動訊號），在確認 K 線後容許以區間上緣執行。

## Catalyst calendar
- 2026-09 ~ 10 — Q3 2026 財報：EBITDA ≥40%、CapEx/Revenue 趨勢（決定加碼或減碼）
- 2026-12 — 5 GW 電力容量里程碑確認
- 2027-Q1 — 全年 $30-34B 達成率與 2027 指引

## Metrics summary
| Metric | Value |
|---|---|
| Verdict | BUY (MODIFY) |
| Conviction | 6 / 10 |
| Direction | LONG |
| Size (% NAV) | 3%（Q3 確認後上限 4-5%） |
| Entry | $279 – $295 [UNVERIFIED] |
| Stop | $262 [UNVERIFIED] |
| T1 | $328 [UNVERIFIED] |
| T2 | $394 [UNVERIFIED] |
| R:R T1 | 1.6 |
| R:R T2 | 4.3 |
| Time horizon | 3-6 個月 |

FINAL DECISION COMPLETE
