# Sentiment — 2408.TW 南亞科 as of 2026-11-26

## 資料來源狀態

| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations / rec_summary | 成功 | 僅有彙總家數, 無個別券商評等明細 |
| yf insider | 成功但無資料 | 回傳空陣列, 不代表零交易, 無法判定 6 個月淨買賣 |
| yf major_holders | 成功 | 只有持股比例彙總 |
| Reddit r/wallstreetbets, r/stocks | 失敗 | 主機無法連線 (WebFetch 拒絕), 零樣本 |
| StockTwits | 失敗 | api.stocktwits.com DNS 無法解析, 需在 session 網路設定允許該網域後才能重試 |
| WebSearch 新聞與論壇 | 部分可用 | 僅取得新聞彙整, 日期不一致, 見下方可信度說明 |

## Analyst consensus

14 家券商: 4 strongBuy / 8 buy / 1 hold / 1 sell / 0 strongSell。買進方 12 家 (約 86%), 中性 1 家, 賣出 1 家。

| 期間 | strongBuy | buy | hold | sell | 合計 |
|---|---|---|---|---|---|
| 0m (當期) | 4 | 8 | 1 | 1 | 14 |
| -1m | 4 | 8 | 1 | 1 | 14 |
| -2m | 4 | 7 | 0 | 1 | 12 |
| -3m | 4 | 7 | 0 | 1 | 12 |

近期變化: 過去約 2 個月內, 中性家數由 0 增至 1, 且家數由 12 增至 14。新聞指大摩將目標價由 348 元降至 298 元並改評中立, 與 hold 增加的時間點大致吻合, 但 yf 資料未列出個別券商, 此為推估。

新聞中提到的目標價 (時間點不一):
- 富邦投顧: 買進, 目標價 660 元, 認為未來 4 季營收與 EPS 上行空間有限, 股價驅動來自偏低評價。
- 某投顧: 買進, 隱含漲幅約 37.7%, 預估今年 EPS 75.93 元。

## Retail social

- Reddit: 無法取得 (連線失敗)。
- StockTwits: 無法取得 (DNS 失敗)。
- X / 論壇: 搜尋未取得即時個股貼文, 只有新聞與財經網站。
- 散戶情緒傾向: 無法直接量測, 無法判定 bullish / bearish。
- 聲量: 無法與平時基準比較。
- 間接線索: 新聞描述 11 月初外資賣壓明顯, 股價自高點回落。此屬於價格與資金面訊號, 不是散戶情緒的直接量測。

主題 (依新聞彙整, 非散戶貼文):
- 基本面極強: 2026Q3 營收約 1,336.49 億 (季增 61.9%, 年增 611.7%), 毛利率 85.7%, EPS 25.40 元。
- 10 月營收約 464.76 億, 年增約 487.7%, 創紀錄。
- 核心疑慮: 2027 年上半年出貨量持平下, ASP 能否維持獲利。
- 供需缺口支撐: 陸廠長鑫存儲擴產, 但估約佔全球 15% 產能; 新聞估 DDR4 明年供需缺口至少 20%。
- 價格與股價背離: 新聞稱股價由高點約 537 元回落, 最新報價數字互相矛盾 (見可信度說明)。

## Insider activity

Net 6mo: 無法判定。yf insider 回傳空陣列, 不能確定是否真的沒有內部人交易。

持股結構 (yf major_holders):
- 內部人持股約 51.7%。這一數字含大股東 (南亞集團相關) 持股, 不代表 CEO 或 CFO 個人買賣。
- 機構持股約 16.0% (流通股占比約 33.1%), 機構家數 241。
- 本期無機構持股趨勢資料, 無法判斷增減。

## Net sentiment score

- 分析師面: 偏多 (12/14 買進方, 高信心)。
- 散戶面: 無資料 (低信心)。
- 內部人面: 無資料。
- 價格與資金面: 近期偏弱 (新聞稱外資賣壓與股價回落)。
- 綜合: 偏多 (信心中等, 因散戶與內部人資料缺失, 且價格面與評等面方向不一致)。

Divergence flag: 無法判定。散戶情緒無資料, 無法確認是否與分析師傾向相反。但分析師家數偏多, 而股價近期下跌, 價格面與評等面出現背離, 值得注意。

## 可信度說明

- WebSearch 回傳的新聞數字互相矛盾: 同一來源提到 414 元與 325 元兩個近期價位, 且 325 元為依 Goodinfo 快照推估。股價數字不能直接使用, 需以行情資料核對。
- 2026Q3 EPS 25.40 元有做手動驗算: 以約 23.9 億股估算, 淨利約 607 億元, 對營收 1,336 億元約為 45% 淨利率。數量級合理, 但股數為假設值, 且 EPS 來源僅為單一新聞。
- 目標價來源日期不一, 大摩降評日期不明, 可能早於近期股價走勢。

Sources:
- [stockfeel](https://www.stockfeel.com.tw/?p=277564)
- [goodinfo 2408](https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID=2408)
- [stockfeel 2026Q3 法說會](https://www.stockfeel.com.tw/%E5%8D%97%E4%BA%9E%E7%A7%91-2408-2026q3-%E6%B3%95%E8%AA%AA%E6%9C%83/)
- [wantrich 2026-11-09](https://wantrich.chinatimes.com/news/20261109900002-420101)
- [wantrich 2026-10-27](https://wantrich.chinatimes.com/news/20261027900074-420101)
- [udn money](https://money.udn.com/money/amp/story/5607/9227944)
- [statementdog 11 月營收](https://statementdog.com/news/15204)
- [udn 大摩降評](https://udn.com/news/story/7253/9397708)

SENTIMENT REPORT COMPLETE
