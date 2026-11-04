# Sentiment — 8358.TWO (金居開發) as of 2026-11-05

資料狀態說明：本次執行為 Phase 1 sentiment-analyst。Reddit 與 StockTwits 主機於本沙盒被封鎖，依指示未重試，相關欄位標示 DATA_UNAVAILABLE。內部人交易資料 (yf insider) 回傳空陣列，金額欄位標示 DATA_UNAVAILABLE。WebSearch 結果多數停留在 2026 年 8 至 9 月，未找到 2026 年 10 至 11 月的最新分析師報告或目標價，時效性有限。

## Analyst consensus

yf rec_summary (本期, period 0m)：**4 buy / 0 hold / 0 sell**（strongBuy 2、buy 2）。

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m（本期） | 2 | 2 | 0 | 0 | 0 | 4 |
| -1m | 2 | 1 | 0 | 0 | 0 | 3 |
| -2m | 1 | 1 | 0 | 0 | 0 | 2 |

- 近兩個月評等由 2 家增至 4 家，且全部偏多，無 hold 或 sell。覆蓋家數少，單一評等變動即可大幅改變比例。
- 目標價 (TP)：本期 DATA_UNAVAILABLE（yf 未提供 target price 欄位，WebSearch 未找到 2026 年 10 至 11 月的目標價）。
- 較早法人目標價（2026 年 1 月）：統一投顧 321 元買進、中信投顧 300 元與國泰證期研究 310 元買進。時點已過久，僅供參考。
- 另一投資網站顯示近 12 個月平均目標價約 735 元，但該頁未標示更新日期，且與 2026 年初的目標價區間差距過大，不採信。
- 近期評等動向：2026 年 9 月報導指出美系外資維持「加碼」評等，當時股價盤中走跌。

## Retail social

- Reddit：DATA_UNAVAILABLE（主機被沙盒封鎖，未重試）。
- StockTwits：DATA_UNAVAILABLE（主機被沙盒封鎖，未重試）。
- X / 新聞輿情：WebSearch 僅找到新聞型內容，無可量化的社群提及次數。buzz 量能無法與歷史常態比較，標示 DATA_UNAVAILABLE。
- 新聞輿情傾向：偏多。2026 年 7 月出現爆量漲停的報導，報導將漲勢歸因於銅箔報價上漲與 AI 題材。
- 主要論述主題（來自新聞，非社群）：
  - 銅箔加工費與銅價同步上漲，帶動售價與毛利。
  - 高階 HVLP3 / HVLP4 銅箔（AI 伺服器用途）占營收比重預估於下半年提升至約 20 至 25%。
  - 高階銅箔供給缺口可能延續至 2028 年。
  - 2026 年至 2027 年營收可望逐年擴增。
- 主要風險論述：股價大幅拉升後的估值壓力，以及前高附近的賣壓。此類論述來源有限，僅能從單篇報導推斷。

## 基本面與價格脈絡（輔助判讀情緒）

- 2026 年 8 月營收：約 NT$10.56 億（原始報導寫 NT$1.056 billion，已換算為億）。
- 2026 年 1 至 8 月營收年增約 47%；8 月營收年增約 60%。
- 2026 年前 8 月每股盈餘 (EPS)：NT$5.82。
- 法人全年 EPS 估算：約 NT$4.2 元（udn 報導，時點未確認，與前述 5.82 元 8 個月 EPS 不一致，需以公司正式財報為準）。
- 股價資料來源互相矛盾（一處顯示 2026 年 10 月 15 日收盤 461.5 元，另一處顯示 2026 年 7 月 21 日約 394.5 元），無法確認本期價位，標示 DATA_UNAVAILABLE。

## Insider activity

Net 6mo：DATA_UNAVAILABLE（yf insider 回傳空陣列；WebSearch 未取得 2026 年董監申報轉讓明細）。
Notable：DATA_UNAVAILABLE。
持股結構參考（yf major_holders）：內部人持股 17.9%，法人持股 24.8%（占流通股 30.3%），法人機構家數 51 家。

## Ownership shifts

- 法人持股比例 24.8%、法人機構 51 家。僅單期快照，無歷史趨勢，趨勢判斷標示 DATA_UNAVAILABLE。
- 無法確認 2026 年內機構持股比例變化方向。

## Net sentiment score

- 分析師面：**偏多（信心：中）**。4 家全部買進，無 hold 或 sell，且覆蓋家數自 2 家增至 4 家。但家數少，且缺少 2026 年 10 至 11 月的目標價更新。
- 散戶面：**DATA_UNAVAILABLE**。Reddit、StockTwits 無資料，僅有新聞型內容偏多，無法作為散戶情緒的獨立證據。
- 綜合：**偏多（信心：低）**。主要依據為分析師一致偏多與基本面營收成長，但時效不足、覆蓋家數少，且缺少社群與內部人資料。

Divergence flag：**無法判定（DATA_UNAVAILABLE）**。由於散戶傾向無資料，無法判斷散戶與分析師方向是否背離。

## 資料缺口與後續建議

1. Reddit 與 StockTwits 於沙盒被封鎖，需在可連線環境補抓 r/wallstreetbets、r/stocks 與 StockTwits 串流。
2. 2026 年 10 至 11 月的分析師目標價與評等變動需直接查閱券商研究報告或 MOPS 公告。
3. 董監事申報轉讓需查閱 MOPS「董監事持股轉讓事前申報表」與事後申報，yf 對 TWO 上櫃股的內部人資料覆蓋不足。
4. 股價資料來源相互矛盾，需以交易所收盤價校正後再用於價位判讀。

SENTIMENT REPORT COMPLETE
