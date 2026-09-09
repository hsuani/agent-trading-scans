FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 2308.TW as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## 部位判定
2308.TW 不在 `held_tickers.txt` 內 → 新倉框架，問題是「該不該進」。答案是進，但以
Neutral 的平衡方案為準：起始 0.5% NAV 試探倉，Q3 EPS 驗證後才放大。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無即時價格，暫不給進出場價位 |
| Stop | 無即時價格，暫不給進出場價位（改採事件驅動 stop，見下） |
| Target 1 | 無即時價格，暫不給進出場價位 |
| Target 2 | 無即時價格，暫不給進出場價位 |
| Size | Small — 0.5% NAV 起始；Q3 EPS > TWD 12 確認後升至 1.5% NAV（3% NAV 移出近期計畫） |
| Horizon | 1-3 個月，以 2026-10 Q3 法說會與 2027 Q1 800V HVDC 訂單為雙錨點 |
| Conviction | M — 55% |
| R:R to T1 | 質性判斷：偏正向但不壓倒性。基本情境上行 +15-20%，尾部情境 A 回撤 40%；以 0.5% NAV 承擔尾部 0.20% NAV，換取驗證後放大的選擇權價值。無報價，不給數字 R:R |

**事件驅動 hard stop（PRICE_DATA_UNAVAILABLE 期間唯一有效熔斷）**
- Q3 2026 單季 EPS < TWD 10 → 全數平倉
- 單季毛利率跌破 32% → 全數平倉
- 任一主要 hyperscaler 公開削減 2027 年 capex → 即時減碼至 0%
- 報價恢復後若已較 TWD 1,885 下跌逾 12% → 暫緩建倉並重新評估估值錨定，同步補設技術面價格 stop

## Risk debate adjudication
- Aggressive 最強論點：PRICE_DATA_UNAVAILABLE 是數據管道故障，不是市場訊號；讓系統故障
  替代投資判斷是錯的。這點我接受，故不因無報價而 REJECT。
- Conservative 最強論點：現行 stop 最早要等 10 月法說會才觸發，等於六週無熔斷窗口；而
  P/E 由 47x 壓縮到 28x 不需要任何基本面惡化，情緒轉向通常早於財報 4-8 週。
- Net：我採 neutral 較重。Aggressive 主張立即 1.5% NAV 錯在時序——在六週無熔斷窗口內把
  倉位放大三倍，是把 Conservative 指出的唯一真實漏洞放大三倍。Conservative 的 1.0% 上限
  與 TAIEX/KWEB 對沖則過度：對沖標的與 2308.TW 的 AI 電源訂單風險無相關性。結論是規模站
  Conservative（0.5% 起始），加碼路徑站 Aggressive/原計畫（1.5% 而非 1.0%）。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 營收結構性轉換 | 佔比持續擴張 | 一年內 23% → 40%+，液冷佔 9% | 成立 |
| 獲利動能已驗證 | Q2 為實績非預測 | EPS 9.68（YoY +80%）、毛利率 35.64% | 成立 |
| H2 加速兌現 | H2 須貢獻 22-26 TWD | H1 僅 17.59，未經驗證 | 觀察中 |
| 估值溢價可持續 | P/E 43-47x 以成長股定錨 | 溢價達產業均值 2-3 倍，95% 買進共識無空頭緩衝 | 觀察中 |

## 論點失效條件（論點紀律，與 Stop 分開）
- 若 Q3 2026 單季 EPS < TWD 10，或 Q3 與 Q4 連續兩季 AI 營收佔比未站上 40%，H2 加速支柱
  失效 → 出場
- 若單季毛利率跌破 32%，獲利動能支柱失效 → 出場
- 若任一主要 hyperscaler 於財報或法說中明確下修 2027 年 capex 金額，AI 結構性支柱失效 → 出場
- 若外資連續三週以上淨賣超，估值支柱轉為觀察失效 → 啟動減碼評估（需結合基本面同步判讀）
- 若 800V HVDC 量產時程自 2027 Q2 再度延後，護城河論點鬆動 → 減碼

## Monitoring trigger
報價恢復當日即重新評估：若股價已較 TWD 1,885 下跌逾 12%、或出現缺口高開後放量回落型態，
暫停建倉並重寫估值錨定，不等事件 stop。

## Catalyst calendar
- 2026-10 中旬 — Q3 2026 法說會（AI 營收佔比、毛利率、2027 訂單能見度）
- 2026-10 ~ 11 — Q3/Q4 獲利公告，H2 加速假設核心驗證
- 2026-11 前後 — FY2026 EPS 全年指引更新（40-44 TWD 共識是否可達）
- 2026 Q4 — ±400V HVDC 量產出貨高峰
- 2027 Q1 — 800V HVDC 商用訂單公告（主要上行觸發）

## 主要風險
估值壓縮風險（P/E 47x → 28x 即 -38~44%，無需基本面惡化）；95% 買進共識造成多殺多；
NT$70B capex 與德州廠月租為剛性承諾，需求降溫時侵蝕邊際獲利；零組件短缺；台海地緣尾部。

FINAL DECISION COMPLETE
