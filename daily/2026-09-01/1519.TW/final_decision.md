FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — 1519.TW as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

> 部位歸屬判定：1519.TW 不在 `held_tickers.txt`，屬**新倉**框架。今日結論為「條件性核准、尚未觸發」——不建倉、不追價，觸發條件成立前部位為零。對 trader proposal 的處置為 MODIFY（採納 neutral 的觸發與分批紀律，收緊關稅條件與第二批門檻）。

> **無即時價格，暫不給即時進出場價位；以基本面錨定價格執行。** PRICE_DATA_UNAVAILABLE（Yahoo Finance proxy 封鎖）為全 session 狀態，下列價位全部由 EPS × P/E 推導，無即時 ATR、無現價驗證。執行前必須先取得即時報價確認現價是否落在入場區間，否則不得下單。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（條件性，觸發前不建倉） |
| Entry zone | $700.00 – $720.00 TWD（≒47-48x P/E × EPS 14.93） |
| Stop | $670.00 TWD（45x P/E × EPS 14.93 ≒ 672；PRICE_DATA_UNAVAILABLE，無 ATR 驗證，需以即時報價複核後生效） |
| Target 1 | $908.00 TWD（FY2027E EPS 16.5 × 55x） |
| Target 2 | $1,140.00 TWD（FY2027E EPS 19.0 × 60x） |
| Size | Small（**0.5% NAV** 上限，分兩批各 0.25%） |
| Horizon | 3m+（季度級別，Q3 法說會為首個重評節點） |
| Conviction | M（**55%**） |
| R:R to T1 | 4.95 |

最大停損損失 ≈ **0.028% NAV**；T1 上行 ≈ **+0.14% NAV**。

## Risk debate adjudication
- Aggressive's strongest point：訂單能見度是已公告事實（台電 NT$5,645 億框架、AIDC NT$140 億、Q2 EPS 3.23 元 +45% YoY），等滯後的月營收數據確認，確實可能錯過最佳定價窗口。
- Conservative's strongest point：主觸發「9 月單月 YoY 轉正」可能只是 2025 年低基期效應，不等於出貨節奏回升；單月數據不構成趨勢。
- Net：我採 **neutral** 較重。激進方要求「在 PRICE_DATA_UNAVAILABLE 下立即建倉 0.75% NAV」是在不知成交價的情況下押注，程序上不可接受；保守方 Stop 695 落在入場帶內側（僅 0.7% 緩衝），數學上自相矛盾，且「須待 USTR 正面豁免公告」是無限期否決。維持 670 TWD 是唯一同時具估值錨且不在入場帶內的止損。同時採納保守方的雙月確認邏輯管住第二批。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 訂單能見度與交期壁壘 | 全球變壓器交期 >160 週、台電框架已核定 | 8/19 行政院核定 NT$5,645 億；AIDC NT$140 億已公告 | 成立 |
| 出貨動能兌現（下半年加速） | 月營收 YoY 由負轉正 | 7 月 −8.32% YoY、YTD −3.68% | **觀察中（尚未證實）** |
| 北美關稅未落地 | 北美 >50% 出貨、無新加徵 | USTR 對台電力設備無新公告 | 觀察中 |
| 高 P/E 可維持 | 50-66x 由 EPS +30-45% 支撐 | 動能未確認前倍數無防護 | 觀察中 |

## 論點失效條件
- 若 **9 月與 10 月月營收 YoY 任一為負**（10/10、11/10 公告），出貨動能支柱失效 → 放棄入場；若已建倉則出場。
- 若 **USTR 正式公告對台灣電力設備加徵額外關稅**，關稅支柱失效 → 立即出場，不等 Stop。
- 若 **台中港廠投產時程宣告延後超過一季**，2027 產能支柱失效 → 減碼一半。
- 若 **管理層在 Q3 法說會下修全年營收指引至 NT$321 億以下**，估值支柱失效 → 出場。

## Monitoring trigger
入場觸發須**同時**成立：①9 月合併月營收 YoY 轉正（10/10 前後）；②無新 USTR 加徵公告；③屆時現價在 700-720 TWD 內（>720 不追價）。第二批 0.25% NAV 須待 10 月營收 YoY 亦為正（連續兩個月）方執行。

## Catalyst calendar
- 2026-10-10 前後 — 9 月合併月營收（最關鍵驗證點）
- 2026-Q4 — 觀音 3B 廠投產公告
- 2026-11-10 前後 — 10 月月營收（趨勢確認）
- 2026-11 月 — Q3 法說會／EPS 指引更新
- 持續 — USTR 對台電力設備關稅進展
- 2027-Q2 — 台中港廠投產

FINAL DECISION COMPLETE
