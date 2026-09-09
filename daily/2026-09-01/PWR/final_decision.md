# Final decision — PWR as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG（條件式，尚未建倉） |
| Entry zone | 無即時價格，暫不給進出場價位（新聞參考錨 ~$687，未驗證） |
| Stop | 無即時價格，暫不給進出場價位（價格資料恢復後設於參考錨下方 6% 以內） |
| Target 1 | 無即時價格，暫不給進出場價位（研究情境 Bull P/E 22x ≈ $836，未驗證） |
| Target 2 | 待 Q3 2026 財報確認 backlog $53B+ 後重估 |
| Size | Small — 首筆 0.5% NAV，條件達成後上限 1.25% NAV |
| Horizon | 3m+（2–4 季） |
| Conviction | M |
| R:R to T1 | 無法計算（缺已驗證 entry / stop） |

PWR 不在 held_tickers.txt，屬新倉判定。結論是「論點通過、執行未通過」：方向核准為 LONG，但在價格資料恢復前**不下單**，故第一行為 HOLD。

## Risk debate adjudication
- Aggressive's strongest point: trade_proposal 的 0.5% NAV 與 investment_plan 自訂的「半倉至三分之二」互相矛盾，用縮倉掩蓋 stop 缺失，是紀律缺失而非審慎；short interest 降至 2.6%、月減 25.5% 確實是實質動能訊號。
- Conservative's strongest point: 倉位大小必須以「止損觸發時最大虧損佔 NAV 百分比」為錨。這個錨在 PRICE_DATA_UNAVAILABLE 下根本不存在，因此任何倉位數字都是無依據的。CEO 6 個月 26 筆、$120M、均價高於現價 12–14% 的套現，在 P/E 23–26x（同業 12–15x）與淨利率 5–6.5% 的組合下，是需要確認而非搶跑的訊號。
- Net: 我在此偏向 **conservative**，但採納 neutral 的分批架構。理由是兩個障礙互相獨立且同時存在：(1) 沒有可驗證報價就沒有可執行 stop，(2) ERCOT 審計是 4 週內的二元監管事件。Aggressive 主張的 $618 stop 距錨點逾 10%，用「給震盪空間」包裝了未量化的風險；在價格盲區內用未驗證數字算出 2.2:1 的 R:R，是把論點正確當成交易紀律。等待的機會成本是實的，但可用分批建倉補償，價格盲區下的未定義風險則無法補償。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Backlog 能見度 | Record backlog $53B，涵蓋 2–2.5 年營收 | Q2 2026 已達 $53B，總管線 $65–75B | 成立 |
| 執行力兌現 | 營收與 EPS 持續超預期 | Q2 營收 $9.56B（YoY +41%，超預期 11%）、EPS $4.24（超預期 28.9%）、全年指引上調 13% | 成立 |
| 德州數據中心跑道暢通 | ERCOT 互連佇列正常推進 | 2026-08-03 州長凍結 474 GW 佇列（90% 為數據中心），審計最快 9 月末出爐 | 觀察中 |
| 估值溢價的正當性 | 2027E EPS 成長維持 15–20%+ 以支撐 P/E 23–26x | 尚無 2027 指引；CEO 系統性套現構成反向證據 | 觀察中 |

## 論點失效條件
- 若 ERCOT 審計對數據中心互連施加**永久性**容量上限或額外收費，「德州跑道」失效 → 不建倉；若已建倉則出場。
- 若 Q3 2026 財報 backlog 低於 $53B（首次下滑）或 book-to-bill < 1.0x，「backlog 能見度」失效 → 出場。
- 若 2027 全年 EPS 指引成長低於 12%（同業區間），「估值溢價正當性」失效 → 減碼至 0，不再重啟。
- 若微軟、Google、Meta 任一家公開下修 2027 基礎設施 capex，「數據中心跑道」失效 → 減碼一半並暫停加倉。

## Monitoring trigger
價格資料恢復後 24 小時內完成 entry / stop / ATR 重算並提交本卡；在此之前不下任何訂單。進場閘門為兩者依序成立：(1) ERCOT 審計結案且無永久性限制 → 建首筆 0.5% NAV；(2) Q3 財報 backlog > $53B 且 book-to-bill > 1.2x → 加至 1.25% NAV。若 ERCOT 結果為負面，整個計畫作廢，不改以「跌深買入」重新包裝。

## Catalyst calendar
- 2026-09 月末 — 德州 ERCOT 互連佇列審計裁決（最關鍵短期事件）
- 2026-10 月中 — PWR Q3 2026 財報：backlog、book-to-bill、全年與 2027 初步指引
- 持續 — AEP / Duke 2027 capex 更新；超大規模科技商 AI 基礎設施 capex 指引；MasTec 大型數據中心合約公告

FINAL DECISION COMPLETE
