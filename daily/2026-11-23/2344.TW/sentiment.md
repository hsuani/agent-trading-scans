# Sentiment — 2344.TW 華邦電 (Winbond) as of 2026-11-23

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 成功 |
| yf insider | 成功但回傳空陣列，無資料 |
| yf major_holders | 成功 |
| Reddit r/wallstreetbets、r/stocks | 失敗，WebFetch 拒絕連線 |
| StockTwits | 失敗，api.stocktwits.com 無法解析 DNS，需在 session 網路設定允許此網域 |
| WebSearch（新聞與法人報告） | 成功，但多為新聞轉述，時間點不一 |
| PTT 股板 | 搜尋未找到相關討論 |

Yahoo cookie/crumb 取得失敗，但資料仍正常回傳。

## Analyst consensus

目前 8 位分析師：3 strongBuy / 4 buy / 1 hold / 0 sell，即 7 買進、1 持有、0 賣出。

| 期間 | strongBuy | buy | hold | sell | 買進合計 |
|---|---|---|---|---|---|
| 本月（0m） | 3 | 4 | 1 | 0 | 7 |
| 前一月（-1m） | 4 | 4 | 0 | 0 | 8 |
| 前二月（-2m） | 4 | 4 | 0 | 0 | 8 |
| 前三月（-3m） | 4 | 3 | 0 | 0 | 7 |

- 近期變化：本月出現 1 位 hold，strongBuy 由 4 降為 3。從數字推論，應有一位分析師由強力買進調為持有，但工具未提供個別分析師的調評紀錄，此為推論。
- 新聞提到中信投顧把評等由「增持」升為「買進」，目標價由 204 元微調為 200 元。此為新聞轉述，未在 yf 資料中核對。
- 目標價參考：7 月初外資報告曾調升至 222 元；7 月底本土法人維持「增加持股」，目標價 200 元，評價基礎為 2027 年 1.8 倍 P/B。11 月初部分法人小幅下修目標價，多數仍在 200 元上下。
- 11 月中外資認為 DDR4 等產品 2028 年將轉為供給略過剩，景氣高峰與定價動能可能提前見頂，評價面臨下修壓力。外資報告的具體目標價搜尋結果未載明。
- 獲利預估（新聞引用）：中信預估今明兩年 EPS 分別為 23.85 元與 50.08 元；華南預估約 30.87 元與 75.67 元。兩家差距很大，顯示 2027 年以後的獲利分歧高。

## Retail social

- Reddit：WebFetch 失敗，無法取得 r/wallstreetbets 與 r/stocks 的貼文。聲量與傾向皆無資料。
- StockTwits：DNS 解析失敗，無資料。
- X / PTT / 新聞論壇：WebSearch 未找到可靠的散戶討論；搜尋僅得到新聞與法人報告。
- 聲量：無法量化，無法與平常水準比較。
- 傾向：無法判定。
- 主題（僅依新聞與法說會報導整理，非散戶原文）：
  - 「記憶體法說魔咒」：法說會後股價反應偏弱，11/4 盤中一度回測 140 元。來源對跌幅的描述不一，一則寫跌 3.77%，另一則寫跌 8.5%。
  - 景氣見頂疑慮：外資 DDR4 供需轉平衡的論點。
  - 資本支出：董事會核准約 731.63 億元資本支出擴建高雄廠，Module B 預計 2029 年下半年小量出貨，2030 年全面開出。
  - 管理層立場：總經理陳沛銘表示 2027、2028 年市況無虞，並認為產業未泡沫化；風險點為消費電子需求疲弱與報價高檔反轉。

## Insider activity

yf insider 回傳空陣列，無近 6 個月內部人交易紀錄。無法判定買賣淨額，也無法確認 CEO、CFO 或其他董監事的動向。台灣的董監持股申報資料可能不在 yfinance 覆蓋範圍內，建議另查公開資訊觀測站的董監事持股異動申報。

## Ownership shifts

單一時點快照，無趨勢資料：

- 內部人持股比例約 28.8%
- 機構持股比例約 26.4%（佔流通股約 37.1%），機構數量 221 家

外資買賣超（新聞數據）：11 月初外資連續三天合計賣超約 4.4 萬張。只有單一時點，無法判斷機構集中度的變化方向。

## 價格脈絡（僅供參照，來源為新聞與財經網站）

- 11/4：盤中回測約 140 元
- 11/13：收盤 125 元
- 11/16：盤中一度跌約 9.6% 至 113 元。該頁面未明確標示日期，需再確認。

## Net sentiment score

- 分析師面：偏多（bullish），7/8 買進，0 賣出，目標價仍在 200 元附近。信心：中高。近期有一位分析師調為持有，且外資對景氣見頂的看法偏保守，故分析師面非全數一致。
- 散戶面：無資料，無法評分。
- 內部人面：無資料。
- 機構資金面：外資近期偏賣超（新聞數據，單點資料）。
- 綜合：中性偏多（neutral to bullish），信心低。主要原因是散戶與內部人資料缺失，且機構資金近期偏賣。

Divergence flag：無法判定。散戶傾向缺資料，無法確認是否與分析師傾向相反。

## 資料缺口與限制

1. Reddit 與 StockTwits 皆無法取得，散戶情緒為空白。若需補足，需允許 api.stocktwits.com 網域，或改用其他來源。
2. 內部人交易資料為空，需另行查證台灣公開資訊觀測站。
3. 新聞來源的股價與法人數據有時間差與互相矛盾之處（如 11/4 跌幅），本報告以引用為主，未逐一核實。
4. 分析師的個別評等變動與目標價變動，僅能從新聞部分得知，yf 資料不含日期與個別券商名稱。

## 主要來源

- [華邦電 2344 股價與統計（statementdog）](https://statementdog.com/analysis/2344)
- [businesstoday 11/4 報導](https://www.businesstoday.com.tw/article/category/183008/post/202611040025/)
- [businesstoday 11/3 報導](https://www.businesstoday.com.tw/article/category/183015/post/202611030039/)
- [wantrich 11/4 報導](https://wantrich.chinatimes.com/news/20261104900188-420101)
- [wantrich 11/3 報導](https://wantrich.chinatimes.com/news/20261103900449-420101)
- [wantrich 11/9 報導](https://wantrich.chinatimes.com/news/20261109900002-420101)
- [wantrich 11/11 報導](https://wantrich.chinatimes.com/news/20261111900384-420101)
- [setn 跌慘了也不降評 華邦電目標價](https://www.setn.com/news/1881355)
- [technews 報導](https://technews.tw/?p=1493931)
- [storm.mg 報導](https://www.storm.mg/article/11146112)

SENTIMENT REPORT COMPLETE
