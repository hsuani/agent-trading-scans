# Sentiment — 6830.TW (汎銓) as of 2026-11-23

> 資料完整度偏低: Reddit 與 StockTwits 無法連線, 券商評等資料稀少, 內部人交易資料為空。本報告的情緒判讀主要依據新聞流與營收數據, 信心度低。

## Analyst consensus
目前 Yahoo 資料顯示 1 buy (strongBuy) / 0 hold / 0 sell, 樣本僅 1 家, 不足以構成有意義的共識。找不到其他券商的目標價或投資評等。近期評等變動 (recommendations) 歷史為空, 無升評或降評紀錄可用。

一個需要注意的線索: 2026-01-30 Yahoo 主力買超名單中出現美商高盛 (買超 78 張、賣出 42 張), 這只是買賣超資料, 不是評等。

## Retail social
- Reddit: 無法取得。WebFetch 對 r/wallstreetbets 與 r/stocks 的搜尋皆回傳無法連線錯誤, 無法判斷散戶語氣。
- StockTwits / X: StockTwits 因網域無法解析而失敗 (api.stocktwits.com 不在允許網域內), 未取得訊息。X 端改以新聞搜尋替代, 找到的是新聞與財經媒體報導, 沒有可辨識的散戶貼文樣本。
- 媒體與論壇語氣 (替代指標, 非散戶原始貼文): 基本面新聞偏正面, 營收數字連續創同期新高; 股價層面則有「營收創高但股價回檔」的落差討論。
  - 代表性說法 (新聞摘要, 非貼文原文): 「設備能否轉為實際營收是討論焦點」。
- 聲量 (buzz volume): 無法與平時基準比較。可觀察到的是媒體報導集中在 10 月至 11 月中旬, 主題集中於 MSS HG 矽光子檢測設備。
- Themes (由新聞推得):
  1. 矽光子 / CPO 商業化: 自製檢測設備 MSS HG 於 11 月 5 日竹北亮相, 市場關注能否拿到第一批付費訂單。
  2. 營收成長: 2026 年 10 月營收約 2.55 億, 年增約 48.5%, 年初至 10 月累計約 22.28 億, 年增約 26.7%。
  3. 股價與估值: 一篇 10 月初分析指出股價曾衝上約 850 元後回檔逾三成, 但另一來源股價頁面顯示約 476 元, 兩者日期不一致, 無法確認現價位置。
  4. 獲利與資本支出: 第三季合併營收約 7.59 億, 單季 EPS 約 1.56 元, 稅後淨利約 0.85 億, 年增約 1.8 倍。另有 2026 年上半年 EPS 為負的紀錄, 與第三季獲利回升並存。
  5. 增資: 2026 年完成約 30 億的現金增資, 定價每股 500 元。是否有董監事認購, 未查到資料。
- Retail tilt: 無法直接判定。替代指標偏正面 (營收與獲利回升、矽光子題材), 但股價回檔與估值疑慮使語氣偏混合。

## Insider activity
Net 6mo: 資料不足。Yahoo insider 交易紀錄為空, 無法計算淨買賣金額。
- 搜尋未找到 2026 年董監事持股申報的具體增減持明細。
- 2026 年的現金增資屬於公司籌資行為, 不應直接視為內部人買入訊號。
- 建議以 MOPS 公開資訊觀測站的董監事持股申報查詢補足。

## Ownership shifts
- insidersPercentHeld: 21.2%
- institutionsPercentHeld: 9.3%
- institutionsFloatPercentHeld: 11.8%
- institutionsCount: 10
- 機構持股比例偏低、機構數量少, 籌碼集中度主要來自內部人與大股東。缺乏時間序列, 無法判斷持股趨勢是增加或減少。

## Net sentiment score
Composite: **neutral** (信心度: 低)

理由:
- 分析師面: 樣本僅 1 家且為 strongBuy, 偏正面但代表性不足。
- 散戶面: 無直接樣本, 無法判斷。
- 新聞與基本面替代指標: 營收與獲利回升偏正面, 矽光子訂單未定與股價回檔為不確定因素。
- 內部人面: 無資料。

Divergence flag: **no (資料不足, 無法判定)**。散戶端沒有可用樣本, 無法與分析師端比較。若日後取得 Reddit 或 StockTwits 資料, 應重新檢視此項。

## 資料來源與限制
- Yahoo 資料經 yf 工具取得時出現 cookie/crumb 取得失敗的警告, 但仍回傳資料, 內容可能不完整。
- 新聞來源日期多在 2026 年 10 月至 11 月中旬, 無 11 月 23 日當日的直接資料。依規定, 2026-11-23 之後的資料一律視為未知, 本報告未採用。
- 股價數字 (850 元與 476 元) 來源日期不一致, 不應作為現價依據。

來源 (供查核):
- [汎銓 10 月營收創單月次高 (wantrich)](https://wantrich.chinatimes.com/news/20261113900101-420101)
- [汎銓矽光子與 CPO 業務加速商業化 (udn)](https://udn.com/news/story/7240/9560871)
- [汎銓 MSS HG 矽光子檢測設備 (bnext)](https://www.bnext.com.tw/article/92306/mastech-6830-ai-silicon-photonics)
- [汎銓 2026 現金增資 (Goodinfo 申報轉讓)](https://goodinfo.tw/tw/EquityTransfer.asp?STOCK_ID=6830)
- [汎銓 10 月營收與股價回檔分析 (winvest)](https://winvest.tw/en/News/Detail/98076)
- [Yahoo 股市 6830 券商分點](https://tw.stock.yahoo.com/quote/6830.TW/broker-trading)

SENTIMENT REPORT COMPLETE
