# Sentiment — 4908.TWO (前鼎) as of 2026-10-11

資料可得性總結：分析師評等、內部人交易、Reddit、StockTwits 皆為 DATA_UNAVAILABLE；社群資料僅有無日期的 CMoney 留言摘要；持股結構資料來源互相矛盾。整體結論信心低，不足以形成可靠的情緒判斷。

## Analyst consensus
- 評等分布：DATA_UNAVAILABLE。`pipeline/tools/yf 4908.TWO rec_summary` 與 `recommendations` 皆回傳空陣列（Yahoo cookie/crumb 取得失敗，疑為 Yahoo 對台股 OTC 代號覆蓋不足）。
- 近期調評與目標價變動：DATA_UNAVAILABLE。網路搜尋未找到券商或分析師對前鼎 2026 年的正式目標價。
- 唯一可見的估值參考為 poorstock 的 AI 技術面推算，短期區間 125–140 元，屬技術判讀而非券商目標價，不應視為分析師共識。

## Retail social
- Reddit（r/stocks、r/wallstreetbets）：DATA_UNAVAILABLE。WebFetch 回報無法連線 reddit.com，且此檔為台股，美股論壇樣本量本來也很少。
- StockTwits / X：DATA_UNAVAILABLE。api.stocktwits.com 解析失敗（ENOTFOUND）。X 搜尋未得到 2026 年 10 月的相關貼文。
- PTT：未取得。
- CMoney 股市爆料同學會（時間不明，非 10 月）：留言整體偏謹慎到偏空。代表性看法（摘錄）：「沒主力很沒力」、「缺乏主力支撐」。亦有少數多頭留言認為高檔有買盤承接。討論區中對「轉型不做光通」的消息反應偏負面。
- 聲量：DATA_UNAVAILABLE（無法取得提及次數，無法與歷史基準比較）。
- 主題：籌碼面（主力缺席）、股價高檔與本益比、AI 需求與營收成長（nStock 引用 2026 年 6 月營收年增 29.72%，為偏多因素）、公司業務轉型消息。

## Insider activity
Net 6mo: DATA_UNAVAILABLE（`insider` 工具回傳空陣列）。
- 替代來源（玩股網）：董監持股比例 2026/05/22 至 07/17 維持 13.14%，期間無變動，代表近期董監未有顯著增減持申報。此為比例觀察，不等同於 6 個月淨買賣金額。
- 公司治理資訊（前鼎董事長葉政彥、總經理李昌祐）來自新聞搜尋，未逐筆核對 MOPS 申報。
- 個別董事的買賣明細：DATA_UNAVAILABLE，建議至公開資訊觀測站（mops.twse.com.tw）查詢。

## Ownership shifts
- `major_holders` 回傳 insidersPercentHeld 44.18%、institutionsPercentHeld 0.90%、institutionsCount 5。這些數字與台灣來源的董監持股 13.14% 明顯不一致，且 institutions 指標似乎是 Yahoo 美股口徑，屬低可信度，不應直接用於判斷集中度。
- `inst_holders`：DATA_UNAVAILABLE（回傳空陣列）。
- 趨勢（季度對季度）：DATA_UNAVAILABLE。

## Net sentiment score
Composite: 中性 偏謹慎（信心：低）。
- 依據：唯一可用的社群訊號偏空但時間不明；基本面數據（2026 Q1 EPS 0.76 元、6 月營收年增 29.72%）偏多；董監持股 2026 年 5 月至 7 月持平；分析師與內部人資料皆無。
- 價格參考點：近期報價散見於 7 月的 135 至 150 元區間，無 2026 年 10 月的收盤價可供核對，本報告未納入任何價格判斷。

Divergence flag: DATA_UNAVAILABLE（缺分析師評等，無法判定散戶與分析師方向是否相反）。

## 資料來源與限制
- Yahoo（yf 工具）：cookie/crumb 取得失敗，rec_summary、recommendations、insider、inst_holders 皆為空，major_holders 數字與台灣來源不符。
- Reddit：無法存取。StockTwits：DNS 解析失敗。
- 網路搜尋：找到的股價與社群資料多停在 2026 年 7 月，非 10 月。來源包括 nStock、玩股網、CMoney、MoneyLink、poorstock、Yahoo 股市等。
- 建議後續補充：MOPS 董監申報、券商研究報告（如法說會後的目標價更新）、TPEx 當日報價與三大法人買賣超。

SENTIMENT REPORT COMPLETE
