# Sentiment — 6217.TWO (中探針) as of 2026-11-14

資料可用性: 本次僅取得新聞與公開網頁摘要。yfinance 分析師評等與內部人交易回傳空陣列 (Yahoo cookie/crumb 取得失敗)。Reddit 與 StockTwits 無法存取 (StockTwits DNS 解析失敗, 需於 session 網路設定中放行 api.stocktwits.com)。以下結論信心偏低。

## Analyst consensus
rec_summary 與 recommendations 皆回傳空資料, 無法列出 buy / hold / sell 家數與近期升降評等、目標價變動。
搜尋結果提到較早的法人說法認為轉機題材成立: 經濟日報報導指出, 法人預期半導體測試針營收占比將從去年約 20% 增至約 30%, 認為基本面具轉機題材。此為單一媒體轉述, 非正式評等紀錄, 日期亦早於本次報告期間, 不可視為當前共識。

## Retail social
- Reddit: 無法存取 (r/stocks 與 r/wallstreetbets 皆回傳錯誤), 無法評估討論量與多空傾向。
- StockTwits / X: StockTwits 無法存取。網路搜尋未找到可量化的論壇情緒統計。
- 新聞面與盤面相關訊息:
  - nStock 注意股訊息 (2026-11-09) 指出中探針近 5 日跌 28.29%, 列為電零組注意股, 盤面以賣壓為主。
  - 股價報價在不同來源有出入: nStock 顯示 131.0 (11/10), Goodinfo 顯示 119.5 (11/09), 需以交易所正式收盤價為準。
- 基本面相關訊息:
  - 2026 年 10 月營收 2.80 億 TWD, 年減 11.03%。
  - 2026 年 9 月自結每股淨損 0.3 元。
  - 2026 年 6 月單月營收 4.29 億 TWD, 年增 43.91%, 為歷史單月新高。此一高點與 10 月的年減形成明顯落差。
- Themes:
  - 轉機敘事 (半導體測試針占比提升) 與近期獲利轉弱並存。
  - 股價短期大幅下跌, 外資與自營商先前鎖碼的說法與近期走勢是否一致, 未能從資料中確認。
  - 籌碼面風險: Goodinfo 股東分級資料 (2026/11/06) 顯示超過 1000 張大戶持股約 13.1%。搜尋摘要另提及非獨立董監持股質押比例約 43.7%, 此數字來自摘要片段, 未經原始頁面核實, 建議人工確認。

## Insider activity
yfinance insider 資料為空, 無法計算近 6 個月淨買賣金額, 也無法辨識 CEO / CFO 或其他人員的交易。
Net 6mo: 無資料 (資料缺漏, 非確認為零交易)。

## Ownership shifts
- yfinance major_holders: insidersPercentHeld 約 17.2%; institutionsPercentHeld 約 1.8%; institutionsCount 8。此為 yfinance 對台股覆蓋不完整的指標, 僅供參考。
- 無歷史季度變化資料, 無法判斷機構集中度趨勢。

## Net sentiment score
Composite: 偏空 (confidence: 低)。
依據: 近期股價大幅下跌與注意股處置、10 月營收年減、9 月每股淨虧, 三者皆偏空; 轉機敘事為較早期且單一來源, 無法作為當前正向證據。分析師與內部人資料缺漏, 無法納入加權。

Divergence flag: 無法判定 (分析師與散戶資料皆缺, 無法比較兩者傾向)。

## 資料缺口與後續建議
- 補抓 yfinance rec_summary 與 recommendations 前, 請以 Yahoo cookie/crumb 重試或改用台灣來源 (如公開資訊觀測站內部人持股申報)。
- 放行 api.stocktwits.com 與 Reddit 存取後, 可補齊散戶情緒量化資料。
- 核實股價收盤與股東質押數字, 因不同來源有出入。

SENTIMENT REPORT COMPLETE
