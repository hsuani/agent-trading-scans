FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — SOI as of 2026-11-23

## FINAL TRANSACTION PROPOSAL: **HOLD**

部位狀態：新倉（SOI 不在 `pipeline/tools/held_tickers.txt`），走 A 框架。此處 HOLD 的意思是「不交易、零曝險」，不是續抱。

## Verdict
REJECT

## Final trade card (if not REJECT)
不適用。本輪沒有任何價格資料，Entry / Stop / Target / R:R 一律不填，也不回填臆測數字。Size 為 0% NAV。

## Dealbreaker
這是「無法評估」，不是看空的基本面判斷。

- 代碼身分未確認：美股 SOI 查詢回 404、quoteType 為 NONE；Soitec（SOI.PA）只是推定，沒有任何工具驗證。
- 沒有價格：fundamentals.md 與 market.md 全部 DATA_UNAVAILABLE，連快取都沒有 OHLCV 或財報。
- 沒有價格就沒有停損錨點，R:R 無法計算，任何部位金額都無法追溯。
- 同樣不放空：資料缺口不是看空證據。

## Risk debate adjudication
- Aggressive's strongest point：「資料不足」不等於「沒有機會」。資料修復後應以小額、虧損有上限的工具試探，而不是永久退場。
- Conservative's strongest point：代碼身分未確認前，連傳聞數字屬於哪家公司都不確定；資料只恢復一部分時不得草率進場。
- Net：三方對「今天零曝險」沒有分歧。重啟門檻我採 neutral 的版本：代碼身分與價格序列兩項確認後，才可提出不超過 0.5% NAV 的試探方案；財報或法說會原文是加碼的前提。Conservative 提的 STM／SOXX 替代標的已超出風控範圍，不採納。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Photonics-SOI 指引上修 | FY2027 Q2 約 50% YoY，季營收約 $25M | 只有媒體轉述，未核對財報或法說會原文 | 觀察中 |
| 多年期產能承諾 | 傳聞 $1.2B | 任何可查來源都找不到此金額；公司只揭露 10 餘份協議與押金機制 | 觀察中 |
| 光通訊產業順風 | 同業營收與股價同步走強 | COHR 營收 +50%，LITE 股價約 +11%；但屬類比，不是 SOI 本身的證據 | 觀察中 |
| 可交易性（代碼與價格） | 可確認掛牌並取得 OHLCV | 代碼 404，無任何價格序列 | 已失效 |

第四根是其餘三根的前提，它失效就足以否決本輪交易。

## 論點失效條件
與價格紀律分開；本輪無 Stop，以下只是論點紀律，供日後重啟評估時使用。
- 若 FY2027 Q2 財報顯示 Photonics-SOI 營收 YoY 低於 30%，或全年指引自「FY2026 基數的 2.5–3 倍」下修，指引支柱失效 → 不建倉。
- 若公司公告或 AMF 文件證實產能協議總額明顯低於 $1.2B，或該數字為口徑混淆，產能支柱失效 → 不得用它作為部位大小依據。
- 若 CEO 所稱「80% 協議於 1–2 週內簽署」在下次財報時仍未兌現，產能支柱失效 → 不建倉。
- 若查證後 SOI 並非 Soitec（SOI.PA），或該標的已下市、合併，本檔所有分析作廢 → 從 Phase 1 重跑。

## Monitoring trigger
若以下兩項同時成立，重跑完整流程，不沿用本輪結論：(1) 有工具確認的代碼身分；(2) 可用的 SOI.PA OHLCV 序列（目前 yfinance 經 proxy 回 403）。只恢復其中一項時，維持 REJECT。

## Catalyst calendar
- 日期待確認 — 資料來源修復（yfinance／Euronext／AMF）
- 日期待確認 — Soitec FY2027 Q2 財報（須先確認代碼身分）
- 日期待確認 — 產能協議簽署進度；原報導連結日期為 2026-08-31，時效存疑

FINAL DECISION COMPLETE
