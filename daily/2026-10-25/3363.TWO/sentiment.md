# Sentiment — 3363.TWO (上詮) as of 2026-10-25

注意: 工具與搜尋結果最新只到 2026 年 7 月，未能驗證 8 月至 10 月的資料。

## 資料來源狀態
- yf recommendations / rec_summary / major_holders: 有回傳 (但 yf 的 Yahoo cookie/crumb 取得失敗, 仍有資料)。
- yf insider: 回傳空陣列, 無法計算 6 個月內部人淨買賣。
- Reddit (r/wallstreetbets, r/stocks): WebFetch 被拒絕存取, 無法取得, 已略過。
- StockTwits: DNS 解析失敗 (api.stocktwits.com 無法連線), 已略過。
- X / 新聞搜尋: 有結果, 但多為 2026 年 7 月前後的報導, 無 8–10 月內容。
- 台灣散戶論壇 (PTT / Dcard) 未搜尋, 散戶面向缺口很大。

## Analyst consensus
目前 (0m) 共 3 家券商覆蓋: 2 buy (strongBuy 1 + buy 1) / 1 hold / 0 sell。
近期走勢 (yf rec_summary 月度快照):
- -3m: 2 buy / 0 hold / 0 sell
- -2m: 2 buy / 0 hold / 0 sell
- -1m: 3 buy (strongBuy 2 + buy 1) / 0 hold / 0 sell
- 0m: 2 buy / 1 hold / 0 sell

近一個月出現一家由買進轉為持有的變化 (buy 由 3 降為 2, hold 由 0 升為 1)。yf 的 historical recommendations 回傳為空, 無法確認是哪家券商、升降評等方向或目標價變動。目標價資料不可得。覆蓋家數只有 3 家, 樣本太少, 統計意義有限。

## Retail social
- Reddit: 無法取得 (存取被拒)。
- StockTwits: 無法取得 (連線失敗)。
- X / 新聞: 無可量化的提及數。以新聞敘述推估, 討論主軸偏謹慎:
  - 櫃買中心多次將 3363 列為注意股 (2025 年 12 月 31 日一次; 2026 年 4 月再次提示, 當時收盤價 990.00 NT$)。
  - 本益比達千倍級別, 2025 年 12 月的股價淨值比為 18.51。
  - 週轉率偏高, 屬於投機性交易。
- 一篇第三方 AI 生成的 poorstock 分析 (2026 年 7 月 31 日) 主張短空與均線空頭排列, 可信度低, 權重不高。
- 散戶聲量: 無法量化 (無 Reddit/StockTwits 數據), 定性判斷為低到中等, 信心低。
- Tilt: 無法直接判定散戶多空。新聞面與注意股語境偏空。
- 主要主題 (由新聞推估): 注意股標記、極端估值、高週轉、外資與法人賣超。

## Insider activity
Net 6mo: 無法計算 (yf insider 空資料)。
- 持股結構參考: 內部人持股比例 (insidersPercentHeld) 26.4%, 屬於高集中度, 但未取得持股增減記錄。
- 台灣董監事持股申報 (公開資訊觀測站) 未能取得。網路搜尋只找到董事長林松福、總經理胡頂達的基本資料, 沒有 2026 年的增減數字。
- 注意: 網路上的法人買賣超 (三大法人、外資) 不等於董監事申報, 不應當作內部人交易。

## Ownership shifts
- 內部人持股 (insidersPercentHeld) 26.4%
- 機構持股 (institutionsPercentHeld) 11.4%, 浮動股持股 (float) 15.4%
- 機構家數 33 家
- 只有單一時點快照, 無法判斷集中度趨勢。
- 三大法人動向 (新聞): 2026 年 7 月 7 日報導近 5 日三大法人合計賣超 872 張, 其中外資賣超 894 張 (1 張 = 1,000 股)。7 月 23 日 Histock 顯示外資單日大幅賣超, 合計約 -289 張。這是流向資料, 不代表長期持股變化。

## 基本面與價格參考 (僅供背景)
- 資本額 NT$11.36 億 (來源: 公司基本資料頁)。
- 股價資料前後不一致: 2026 年 7 月 21 日盤中約 NT$509, 另一頁顯示 NT$589 (上漲 4.06%)。無法確認 10 月的價位, 不應直接採用。
- 未計算市值, 因股本與價格來源不一致, 無法可靠換算。

## Net sentiment score
- 分析師面: 偏正向但樣本極薄 (3 家, 無賣出評等), 近期出現一家降為持有。
- 散戶面: 無法量化, 新聞語境偏謹慎。
- 機構流向: 2026 年 7 月出現外資與法人淨賣超。
- 綜合: 中性偏空 (neutral-to-bearish), 信心低 (Low)。主要原因是資料缺口大, 且缺乏 8–10 月的資料。
- Divergence flag: 條件性 yes (信心低)。賣方偏多/持有, 但外資流向與注意股語境偏空, 方向有分歧。若要確認, 需補 Reddit/StockTwits/PTT 資料與 8–10 月的法人與董監申報。

## 建議後續補充 (供呼叫端參考)
1. 公開資訊觀測站董監持股申報 (取得 2026 年 6 個月內增減)。
2. 櫃買中心注意股公告 (確認 2026 年 8–10 月是否仍在名單內)。
3. 三大法人近 20 日買賣超 (Histock / 玩股網 / 嗨投資)。
4. PTT Stock 版與 Dcard 對 3363 的討論量與多空比例。
5. 分析師報告 (券商名稱、目標價) 直接查證。

## Sources
- [MONEY LINK 公司基本資料](https://ww2.money-link.com.tw/TWStock/StockBasic.aspx?SymId=3363)
- [Histock 3363](https://histock.tw/stock/3363)
- [wantrich 2026-04-22 注意股](https://wantrich.chinatimes.com/news/20260422900081-420101)
- [wantrich 2026-07-07 法人賣超](https://wantrich.chinatimes.com/news/20260707900088-420101)
- [poorstock 3363 (AI 生成, 低可信)](https://poorstock.com/stock/3363)
- [goodinfo 股權異動](https://goodinfo.tw/tw/EquityTransfer.asp?STOCK_ID=3363)

SENTIMENT REPORT COMPLETE
