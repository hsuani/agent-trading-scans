# Final decision — ASML as of 2026-08-31

FINAL TRANSACTION PROPOSAL: **BUY**

> **PRICE_DATA_UNAVAILABLE** — 所有價位以共識隱含錨點 ~$1,732 為基準推算，全部標示 **UNVERIFIED**。

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 錨點 -2% 至 -4%（UNVERIFIED ~$1,697 – ~$1,663），限價掛單、不追高 |
| Stop | 入場 -10%（UNVERIFIED ~$1,512），收盤價確認 |
| Target 1 | 入場 +15.5%（UNVERIFIED ~$1,940） |
| Target 2 | 入場 +28%（UNVERIFIED ~$2,150） |
| Size | Small（**0.40% NAV**），上限含加碼 1.0% NAV |
| Horizon | 1-3m（Q3 財報為第一節點，MATCH Act Q4 為終局） |
| Conviction | M（**6/10**） |
| R:R to T1 | **1.55**（至 T2 為 2.80） |
| Hedge | **OTM Put 必要（required）**：strike UNVERIFIED ~$1,450，expiry Jan 2027，成本上限為倉位市值 2% |

**Execution gate（不可跳過）**：下單前必須以即時報價確認實際價格落在錨點 ±3% 內。若實價偏離錨點超過 3%，本卡片全部作廢，須以真實價格重算 R:R，R:R 未達 1.5 則不執行。Put 未成交前，股票部位不得建立。

## Risk debate adjudication
- **Aggressive 最強論點**：MATCH Act 是二元事件，純股票多頭全程暴露於 -45% 尾部，用期權結構隔離尾部是被遺漏的效率化機會。此點成立，我採納了「必須有期權」的結論。
- **Conservative 最強論點**：立法公告若於收盤後發布，止損單對隔夜跳空毫無防護——止損在此標的上是失效的風控工具。此為本案最關鍵的結構性洞察。
- **Net**：我採 **neutral** 為主。Aggressive 的錯在方向：他用 Call spread 擴大總暴露而非限縮尾部，且要在 R:R 僅 1.2 的錨點立即建 1.0% NAV——信心不能替代入場紀律。Conservative 的錯在 0.25% NAV 使部位失去經濟意義，且 -7% 止損會被 ASML 正常波動洗出。結論：Conservative 的對沖邏輯 + Neutral 的規模與止損 + 序列式加碼。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 訂單能見度與指引執行力 | FY2026 指引維持上調軌跡 | 指引由 €36-40B 上調 13%+ 至 €43-45B；Q2 淨銷售 €9.3B 超預期 5.7% | 成立 |
| EUV 壟斷結構 | 無可替代供給、切換成本趨近無限 | Zeiss 獨供高 NA 光學、250+ NXE:3800E 安裝基礎，Canon 滯後 2-3 年 | 成立 |
| High-NA 採用節奏 | 多客戶接棒放量 | 三星延至 2030、TSMC 延至 2029（具名確認），量產客戶事實上僅 Intel 一家 | 觀察中 |
| MATCH Act 立法結果 | 風險可控 | 150 天條款橫跨 Q4，維保禁令毛利衝擊大於 14% 表面收入占比 | 觀察中 |

## 論點失效條件
- 若 **MATCH Act 正式通過且含維保服務禁令條款** → 該支柱失效 → **出場**（股票全數平倉，Put 續持至兌現）
- 若 **Q3 2026 淨銷售低於 €11B 指引下緣** → 能見度支柱失效 → **減碼至 0.2% NAV**
- 若 **Intel 正式公告削減先進製程資本支出或延後 Foundry 節點時程** → High-NA 支柱失效 → **減碼一半**
- 若 **連續兩季新增訂單（net bookings）YoY 為負** → AI 資本支出耐久性支柱失效 → **出場**

## Add gates（序列式，不得同時綁定亦不得跳階）
1. Q3 2026 淨銷售 ≥ €11B 且指引未下修 → 加至 **0.5% NAV**
2. MATCH Act 明確遭否決或維保條款被刪除 → 加至 **1.0% NAV**（硬上限）
3. 立法結果未明前，任何財報利多均不得越級加至 1.0%

## Monitoring trigger
若國會 MATCH Act 委員會排入表決議程、或 Intel 於財報外發布資本支出更新，立即重評，不等 Stop 觸及。Put 到期前 30 天須決定展期或平倉。

## Catalyst calendar
- 2026-09 月末 — Q3 2026 財報（驗證 €11-12B）
- 2026 Q4 前 — MATCH Act 150 天條款投票期限
- 持續 — Intel Foundry 資本支出、TSMC High-NA 採購時程

## Key risks
MATCH Act 隔夜跳空（止損失效，僅 Put 可防）、High-NA 單客戶依賴、62x trailing P/E 無估值緩衝、51:1 內部人士賣出比、+63.5% YTD 技術面過度延伸。

FINAL TRANSACTION PROPOSAL: BUY ASML 0.40% NAV

FINAL DECISION COMPLETE
