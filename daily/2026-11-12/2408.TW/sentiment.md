# Sentiment — 2408.TW (南亞科) as of 2026-11-12

## Analyst consensus
目前 14 家: 12 buy (4 strong buy + 8 buy) / 1 hold / 1 sell / 0 strong sell。買進比例約 86%。

近 3 個月趨勢 (yfinance rec_summary 快照):

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 目前 (0m) | 4 | 8 | 1 | 1 | 14 |
| -1m | 4 | 8 | 1 | 1 | 14 |
| -2m | 4 | 7 | 0 | 1 | 12 |
| -3m | 4 | 7 | 0 | 1 | 12 |

Recent moves: 過去一個月評等分布無變化。-2m 至 -1m 之間新增 1 家 hold 與 1 家 buy (合計家數 +2)，工具未提供個別券商名稱。新聞檢索提及摩根士丹利 (大摩) 由「加碼」轉「中立」，目標價由 348 元下調至 298 元 (2026 年，確切日期未確認)。這與上表 hold 由 0 增至 1 的時點可能吻合，但未能直接對應，需人工核對。另有資料指出部分外資目標價仍停留於 2025 年 10 月，屬過時資料，不宜作為現況依據。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 回傳 "unable to fetch"，本沙箱網路受限，未重試。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (不在允許網域內)，依規定未重試，需於 session 網路設定中允許該網域後才能補抓。
- X / 新聞 (WebSearch 摘要): 可取得的是財經新聞與節目評論，非原始散戶貼文，無法計算提及量。以下為新聞層級觀察:
  - 「南亞科法說會行情失靈股價跌停」 (新聞標題，反映法說後賣壓)
  - 「毛利率叩關7成卻陷震盪」 (新聞標題，反映基本面與股價落差)
  - 2026 年 8 至 9 月某財經節目邀 5 位專家評比，1 人偏多、1 人中立、3 人偏空 (時點較舊)
- 散戶聲量 (buzz volume): 無法量化，標示為「未知」。新聞層級討論密度屬高 (多篇報導與法說分析)，但這不等同於散戶社群聲量。
- 散戶傾向 (tilt): 無法可靠判定。新聞與節目評論偏謹慎，認為股價漲幅已超前基本面；但缺乏直接散戶樣本，信心低。

Quote samples (新聞標題，非散戶原文):
- 「南亞科法說會行情失靈股價跌停」
- 「毛利率叩關7成卻陷震盪」

Themes (新聞層級):
1. 基本面創高: 2026Q3 營收 1,336.49 億元，季增約 62%、年增約 612%；10 月營收約 464.76 億元，年增近五倍。
2. 2027 年價格能否續強: 公司表示 2027 年上半年前出貨量持平，價格可能維持高檔；市場對價格高峰時點分歧。
3. 估值與股價落差: 股價漲幅被認為已超前基本面；有人建議轉向記憶體以外的 AI 供應鏈。
4. 資本支出與股利: 股利維持穩定，但資本支出龐大，目前無庫藏股計畫。

## Insider activity
Net 6mo: 無資料 (yfinance insider 回傳空清單)。

注意: 空清單不等於「6 個月無交易」。台灣內部人申報資料主要來自 MOPS (公開資訊觀測站)，yfinance 對 TW 個股的覆蓋可能不完整。在取得 MOPS 資料前，內部人淨買賣金額標示為「未知」，不可推論為中性。

Ownership snapshot (yfinance major_holders):
- 內部人持股約 51.66%
- 機構持股約 15.98% (佔流通股約 33.06%)
- 機構家數約 239
- 單一快照，無法判斷機構持股趨勢。內部人持股比例高，代表股權集中，籌碼穩定度高，但也代表自由流通股比例低。

## Net sentiment score
Composite: **偏多 (bullish)，信心中等偏低**

- 分析師面: 偏多，信心中高 (86% 買進，近 3 個月無大幅降評)。
- 散戶面: 無法可靠量化，新聞層級偏謹慎，信心低。
- 內部人面: 無資料，不納入計分。
- 籌碼面: 內部人持股高，不構成明確情緒訊號。

Divergence flag: **待確認 (yes/no 無法判定)**。若以新聞與節目評論為代理，散戶/市場評論偏謹慎，與分析師偏多方向可能相反，這類背離有參考價值；但代理樣本時點偏舊且非散戶原文，故不作為確定性結論。需補充 Reddit 或 StockTwits 資料後再判定。

## 資料缺口與注意事項
1. Reddit、StockTwits 無法取得 (網路限制)。
2. 內部人交易資料為空，需以 MOPS 補查。
3. WebSearch 摘要內部有數字不一致的地方 (例如 2026 年 8 月股價描述與 11/9 收盤約 370 元的關係，以及 EPS 與毛利率數字)，未經原始來源核實，此報告僅引用標題與方向性結論。
4. 數字單位: 營收採「億元」(TWD)；未出現 USD 數字。依 EPS 25.40 元 × 約 29.7 億股 (需以公司資料核實) 估算當季稅後淨利約 754 億元，與營收 1,336 億元相比，淨利率約 56%，偏高，建議與財報原文核對。

## 來源
- yfinance tools: pipeline/tools/yf 2408.TW recommendations / rec_summary / insider / major_holders
- WebSearch 新聞摘要 (2026 年 11 月檢索，多來源，時點不一):
  - https://www.stockfeel.com.tw/?p=277564
  - https://www.businesstoday.com.tw/article/category/183008/post/202609010044/
  - https://udn.com/news/story/7253/9440595
  - https://udn.com/news/story/7253/9397708
  - https://money.udn.com/money/amp/story/5607/9276376
  - https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=2408+

SENTIMENT REPORT COMPLETE
