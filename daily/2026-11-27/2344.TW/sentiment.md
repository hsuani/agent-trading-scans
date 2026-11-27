# Sentiment — 2344.TW (華邦電) as of 2026-11-27

## Analyst consensus

8 家券商：3 strong buy / 4 buy / 1 hold / 0 sell / 0 strong sell（yfinance rec_summary，期間 0m）。
近 3 個月趨勢（表格，單位：家數）：

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 0m（本期） | 3 | 4 | 1 | 0 | 8 |
| -1m | 4 | 4 | 0 | 0 | 8 |
| -2m | 4 | 4 | 0 | 0 | 8 |
| -3m | 4 | 3 | 0 | 0 | 7 |

本期出現 1 家 Hold，Strong Buy 由 4 降為 3。工具只給彙總家數，無法確認是哪家券商，也不能確定是評等下修還是家數變動。

目標價：中信、國票、元大等機構在 2026 年 11 月法說會後因估值調整下修目標價（wantrich.chinatimes.com 11/4 報導）。中信估今明兩年 EPS 約 23.85 元與 50.08 元；華南投顧估明年 EPS 約 75.67 元。各家估值差異大，且多為不同時點的數字，不宜直接比較。

較早的目標價（2025 年 12 月上調至 100 元等）已過時，僅供背景參考。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：抓取被拒（WebFetch 無法連線 www.reddit.com），無資料。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，疑為 session 網路白名單未放行），無資料。
- PTT 及其他中文論壇：本次搜尋未取得散戶討論內容。
- X / 新聞鏈：網頁搜尋只抓到法人與新聞報導，未抓到散戶貼文。
- 聲量：無法量化，無法判斷相對於平常的水準。
- 散戶傾向：無法判斷（資料缺口）。
- 主題（取自新聞，不代表散戶看法）：
  - 記憶體供需緊俏與價格續漲預期（Q4 合約價續升、供給緊到 2027 年）
  - 股價「好消息不漲」，法說後一度回到 140 元附近
  - 記憶體景氣高點與價格反轉風險
  - 高雄廠擴建約 731 億元資本支出，2029 年下半年小量量產、2030 年全面開出
  - 消費性電子需求疲弱、雲端業者 capex 可能下修的風險
  - 員工獎金約 30 個月薪資（新聞標題引述董事長焦佑鈞）

## Insider activity

- yfinance insider 回傳空陣列，但 cookie/crumb 取得失敗，此結果可信度低，不代表沒有內部人交易。
- 第三方彙整（stock.wearn.com 申報轉讓表，非官方來源）顯示：董事華新麗華股份有限公司於 2026 年有多筆申報轉讓：
  - 2/26 申報 30,000 張
  - 4/2 申報 14,145 張
  - 5/25 申報 14,145 張
  - 合計約 58,290 張，發生於 2026 年 2–5 月。
- 申報前原持股約 97.9 萬至 99.5 萬張；新聞稱目前仍持有約 96.5 萬張（兩者時點與口徑不一致，需再核對）。
- 近 6 個月（2026-05-27 至 2026-11-27）：本次搜尋未找到新的買進或賣出申報，淨額無法確認。5/25 的申報已接近視窗起點，需以公開資訊觀測站（MOPS）核對。
- 金額粗估：若以假設價 NT$130 計算，58,290 張約值 75.8 億元（僅供量級參考，實際需以各次成交價計算）。
- 申報為「轉讓」，不一定是市場賣出（可能為關係人間移轉），需看 MOPS 的交易原因。
- 角色：董事法人（非 CEO/CFO）。未找到 CEO/CFO 的買賣紀錄。

## Ownership shifts

- 內部人持股約 28.8%，機構持股約 26.3%（占流通股約 37.0%），機構家數 222 家（yfinance major_holders）。
- 機構持股趨勢：只有單期快照，無法判斷增減。
- 大股東可能的持續調節（見上節）是本期最值得追蹤的籌碼訊號。

## Net sentiment score

**綜合：偏多（bullish lean），信心低。**
- 分析師：偏多，信心中。8 家無賣方評等，但目標價在法說後下修，本期出現 1 家 Hold，動能略降。
- 散戶：無資料，不計入評分。
- 內部人：偏空傾向（若轉讓屬實為籌碼調節），但證據為第三方資料，信心低。

**Divergence flag: 無法判斷（no）。** 因缺少散戶資料，無法比較散戶與分析師的方向。
另一個值得注意的落差是：基本面與法人評等偏多，但股價在法說後沒有跟上（「好消息不漲」）。這屬於價格與基本面的背離，不是散戶與法人的背離。

## 資料品質與限制

- 股價資料衝突：11/13 收盤 NT$125（statementdog，-1.96%）；11/4 盤中回到 NT$140；另一無日期報價 NT$139.5。最新價格無法確認，請以即時報價為準。
- 營收換算（TWD，億元）：10 月營收 293.61 億元（較 9 月 +3.9%，年增 257.0%）；前 10 月累計 2,097.88 億元（年增 195.4%）；Q3 營收約 823.3 億元（年增約 278%）。Q3 合計與 9 月、10 月月營收量級一致，可互相印證。EPS 7.58 元未能用股本數重新驗算，因本次未取得股本資料。
- 所有資料均不晚於 2026-11-27。
- 本報告僅為情緒彙整，不構成交易建議。

## 來源

- statementdog 2344 股價頁 — https://statementdog.com/analysis/2344
- technews 10 月營收報導 — https://finance.technews.tw/2026/11/06/wec-2344-202610-financial-report/
- wantrich 11/4 法人報導 — https://wantrich.chinatimes.com/news/20261104900124-420101
- businesstoday 法人與高雄廠資本支出報導 — https://www.businesstoday.com.tw/article/category/183008/post/202611040025/
- setn 轉載法人觀點 — https://tw.news.yahoo.com/%E7%86%B1%E9%96%80%E8%82%A1-%E8%8F%AF%E9%82%A6%E9%9B%BB%E5%8F%88%E4%B8%8A%E8%AA%BF-5%E5%88%B8%E5%95%86%E6%96%B0%E7%9B%AE%E6%A8%99%E5%83%B9%E6%9B%9D-171600879.html
- wearn 申報轉讓表（第三方）— https://stock.wearn.com/declare_trans.asp?s=1&k=2344
- wantrich 2026-05-26 報導 — https://wantrich.chinatimes.com/news/20260526900207-420101
- technews 員工獎金報導 — https://finance.technews.tw/2026/11/07/winbond-electronics-employees-are-expected-to-receive-an-average-bonus-of-approximately-30-months-salary/

SENTIMENT REPORT COMPLETE
