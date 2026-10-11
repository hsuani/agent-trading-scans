# Sentiment — 3711.TW (日月光投控) as of 2026-10-11

資料注意: 本次可取得的新聞與分析師目標價多為 2026 年 7 月至 8 月的資料,沒有 10 月的最新報價或評等更新。Yahoo cookie/crumb 取得失敗但資料仍回傳。Reddit 與 StockTwits 無法連線。

## Analyst consensus
18 buy / 0 hold / 0 sell (6 strong buy, 12 buy)。來源: `yf rec_summary` 與 `yf recommendations` 回傳相同的月度彙總。

- 近 4 個月趨勢: strongBuy 由 7 降至 6,buy 維持 12,評等結構幾乎未變,全部為買進。
- 近期評等變動 (upgrade/downgrade 明細): DATA_UNAVAILABLE。`recommendations` 只回傳彙總計數,沒有逐筆評等變動紀錄。
- 目標價 (近期,來自 WebSearch 報導,日期為 7 月底至 8 月):
  - 中信投顧: 630 上修至 760 (買進,四家投顧中最高)
  - 富邦投顧: 750
  - 美銀證券: 750 (買進)
  - 凱基: 588 上調至 700
  - 元大: 550 上調至 700
  - 投資網站共識平均: 約 727.53 (Investing.com 頁面,時間不明); 另一來源平均 689.56
- 較早目標價: 大摩 338、高盛 350,來自較早的法說會報導,已被後續上修取代,不宜當現行參考。
- 來源間股價數字不一致 (漲停約 555、頁面 713、其他 677),我無法確認 10 月的實際價位。

## Retail social
- Reddit: DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 的 JSON 搜尋被 proxy 擋下 (無法連線)。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 無法解析網域。
- PTT / 台灣社群: 搜尋未找到 PTT Stock 板直接討論串。CMoney 股市爆料同學會 (https://www.cmoney.tw/forum/stock/3711) 有網友留言彙整,時間約為 7 月至 8 月。
  - 偏多: 看好 AI 成長動能與財報展望。
  - 偏空/謹慎: 對 700 元關卡的壓力、外資沽壓、估值偏高的疑慮。
  - 整體 tilt: 偏多但情緒謹慎,以估值擔憂為主。
- X / 新聞鏈: 未找到 10 月的相關討論,無法量化 buzz 量。
- 聲量 (buzz volume): 無法與平常基準比較 (DATA_UNAVAILABLE)。社群來源樣本稀少,僅能判定為低。

Themes:
1. AI 資料中心與先進封裝 (LEAP) 需求帶動成長,是多方主軸。
2. 資本支出上修 (2026 年約 85 億美元) 與晶圓廠外包趨勢擴大。
3. 估值偏高與 700 元附近的壓力,是主要的空方論點。
4. 對 AI 封裝依賴可能壓縮毛利率的疑慮 (長期)。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。`yf insider` 回傳空陣列 []。空值可能代表無交易,也可能代表此台股的內部人資料不在 Yahoo 來源中,無法區分兩者。
Notable: 無可驗證的內部人交易紀錄。

## Ownership shifts
- insidersPercentHeld: 24.41%
- institutionsPercentHeld: 35.01%
- institutionsFloatPercentHeld: 46.31%
- institutionsCount: 430
- 趨勢 (多季比較): DATA_UNAVAILABLE。`major_holders` 只有單一時點快照。

## Net sentiment score
Composite: **偏多 (bullish-leaning)**, 信心 **低-中**。
- 分析師端: 高度一致偏多 (18 買進、0 持有、0 賣出),目標價多在 700 至 760 之間。權重高,但資料停在 7 至 8 月。
- 散戶端: 樣本少 (僅 CMoney 論壇彙整),偏多但帶估值謹慎。Reddit、StockTwits 無資料,無法做量化校正。
- 內部人與持股變化: 資料不足。

Divergence flag: **弱分歧 (是, 低信心)**。分析師一面倒看多,散戶論壇則對估值與 700 元壓力較為謹慎。差距幅度小,且散戶樣本薄弱,只能視為方向性提示。

缺漏項目 (DATA_UNAVAILABLE): Reddit、StockTwits、X 量化 buzz、逐筆評等變動、內部人交易、持股趨勢、10 月的最新報價與目標價。建議在 10 月底 Q3 財報 (MarketScreener 預估 2026-10-28) 前後重新抓取。

SENTIMENT REPORT COMPLETE
