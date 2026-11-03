FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — SNDK as of 2026-11-04

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 判定框架
SNDK 不在 `held_tickers.txt` → 新倉，問題是「該不該進」。答案：現在不進，但 trader 的「上行觸發後直接轉 LONG MEDIUM、可加到半倉」太鬆，改為條件式小倉試單。目前部位為零，下方 trade card 為**觸發後才生效**的唯一方案。

## Final trade card (conditional — 觸發前不執行)
| Field | Value |
|---|---|
| Direction | LONG（條件式） |
| Entry zone | $1,150.89 – $1,175（需連續兩日收盤站穩 $1,150.89；上緣為觸發價 + 0.25x ATR14，推算值） |
| Stop | $998.19（2026-07-29 局部低點；split 後約 $124.77） |
| Target 1 | $1,387.31（MA20；split 後約 $173.41） |
| Target 2 | $1,547.49（MA50；split 後約 $193.44） |
| Size | Small（1/8 部位，約 2.5–3% NAV；停損打到約損失 NAV 0.4%） |
| Horizon | 戰術數週（11-20 split 後至 Kioxia 財報），驗證至 2027-02-15 FQ2 財報 |
| Conviction | L |
| R:R to T1 | 1.5（以 $1,150.89 計；T2 為 2.6，不對稱主要在 T2） |

觸發條件：(1) 連續兩個交易日收盤 ≥ $1,150.89；且 (2) Kioxia 財報或 TrendForce 合約價**任一**確認 NAND 2026 Q4–2027 Q1 續漲。11-09 至 11-20 split 窗口內，純技術訊號不算數；基本面驅動的消息可算。2026-11-20 起所有價位除以 8。

## Risk debate adjudication
- Aggressive's strongest point: 等 +7% 反彈才進場等於把最肥一段讓出去；run-rate P/E 約 5x、淨現金 $5.0B 是真實的估值底。這點成立，所以我不接受「永遠等 MA20」，只要求兩日確認。
- Conservative's strongest point: Crux 3（財報後 -19%）是資料缺口而非論述分歧，疊加 split 窗口的套利／再平衡雜訊、內部人 6 個月賣出 $130.3M、FMR 持股季減 41.3%，單日收盤觸發極易被假突破騙進。
- Net: 我偏向 **conservative**，因為 MACD hist 仍在擴大（-21.3）、價格低於三條均線，動能尚未止跌，且年化波動率 80.8% 下「超賣」不是進場訊號。但採納 neutral 的折衷：單一基本面確認即可、初始 1/8 而非 1/4，停損維持 $998.19 不拉寬（拉寬至 $925 無新證據支持，激進方同時放大倉位與容忍度是雙重加碼）。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 估值底與財務緩衝 | TTM EPS 125.12、淨現金 $5.0B 撐住下檔 | run-rate P/E 約 5x、EV/EBITDA 7.0x，負債僅租賃 | 成立 |
| NAND 漲價週期延續至 2027 | 合約價 Q4 2026–Q1 2027 續漲 | 僅有二手彙整，缺 2026-10 TrendForce 數據 | 觀察中 |
| 財報後重挫屬錯殺（Crux 3） | 跌幅為 split 前獲利了結，非指引轉弱 | 8-K 中 FQ2 指引未查核 | 觀察中 |
| 技術面止跌 | 收復 $1,150.89 並守住 | 價格低於 MA20/50/200，MACD 擴大，1.95x 量急跌 | 已失效（目前） |

技術支柱失效是「現在不進場」的直接理由；其餘三根決定觸發後是否值得試單。

## 論點失效條件
與 Stop 分開：下列任一成立即取消觸發或出清試單，不等價格打到 $998.19。
- 若 8-K 原文顯示 FQ2 FY27 營收或 EPS 指引低於共識 57.12 → Crux 3 以空方版本解決 → 取消觸發／出場
- 若 TrendForce 公布 2026 Q4 NAND 合約價 QoQ 持平或下跌，或 Kioxia 財報明示 2027 上半年供給轉鬆 → 週期支柱失效 → 出場
- 若 Samsung／SK hynix／Kioxia／Micron 任一宣布擴大 NAND capex → 出場
- 若 FY27 EPS 共識下修超過 10% → 減碼至零
- 若觸發後連續兩日收盤回落至 $1,150.89 以下 → 視為假突破，出場（不等停損）

## Monitoring trigger
If 11-09 至 11-20 期間出現單日放量收盤 ≥ $1,150.89 但無基本面消息配合，視為 split 雜訊，不進場；若 11-20 後以 split 後價格連續兩日收盤 ≥ $143.86 且 Kioxia／TrendForce 任一確認，執行試單。若收盤跌破 $998.19（split 後 $124.77），轉為 SHORT_OR_AVOID 重新評估。

## Catalyst calendar
- 2026-11-09 — 8:1 forward split record date
- 2026-11-20 — split effective date，之後所有價位除以 8
- 2026-11 — TrendForce／DRAMeXchange NAND 合約價更新
- 待定 — Kioxia 財報，檢視 2027 供給說法
- 2027-02-15 — SNDK FQ2 FY27 財報，forward EPS 287.26 可信度主要檢驗點

FINAL DECISION COMPLETE
