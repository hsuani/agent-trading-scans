# Sentiment — LAES as of 2026-11-10

資料截止: 2026-11-10。Reddit 與 StockTwits 本次無法取得 (見下方資料缺口)。板塊對照組 (IONQ, RGTI, QBTS, QUBT, ARQQ, HON, IBM) 本次未抓取情緒資料。

## Analyst consensus
yf rec_summary (0m): 2 buy (含 1 strongBuy) / 0 hold / 0 sell。前期 (-1m) 結構相同。
- 與 MarketBeat (2026-08 快照) 不一致: MarketBeat 列 1 buy / 1 hold / 1 sell, 共識 Hold, 平均目標價 $6.00。兩來源分布差異大, 且覆蓋家數極少 (約 2-3 家), 共識參考價值有限。
- Recent moves: yf recommendations 工具只回傳期數彙總, 未回傳個別升降評等紀錄, 目標價變動亦無資料。本期無法確認近期 upgrade / downgrade。

## Retail social
- Reddit: 無法取得 (r/wallstreetbets, r/stocks 搜尋遭工具拒絕)。無法估算提及量與多空傾向。
- StockTwits: 無法取得 (api.stocktwits.com DNS 解析失敗, 需於 session 網路設定中允許該網域)。
- X / 新聞: 網頁搜尋結果以 2026-08 與 2026-11-03 快照為主, 缺乏 11 月專門的散戶情緒文章。
  - 2026-11-03 股價約 $1.39, 當月下跌約 5%, AAII 動能評分 "Very Weak" (四季相對強弱 -37%)。
  - Simply Wall St 轉載文章指出 P/S 21.6x, 遠高於半導體產業均值 6.1x, 估值偏貴的論點常見。
  - Benzinga (2026-08) 顯示空單占流通股約 5.9%, put/call 比 0.04。數據已過時, 僅供參考。
- Buzz volume: 無法量化 (資料缺口)。
- Themes (由網頁摘要歸納, 非散戶貼文直接統計):
  - 後量子 (post-quantum) 晶片與安全基礎設施的題材敘事, 是多頭論點的主軸。
  - 估值過高與股價大幅回落, 是空頭論點的主軸。
  - 技術面偏弱 (TipRanks 技術讀數為負, 價格位於均線之下, 頁面日期不明)。
  - Equibles 綜合評級 Strong Sell (情緒中性), 日期不明。
- Retail tilt: 無法判定 (資料不足)。以價格與動能推論, 偏空或中性偏空, 信心低。

## Insider activity
Net 6mo (2026-05-10 至 2026-11-10): $0.00M 公開市場買入 / 約 $0.63M 賣出。
- 6 個月內所有交易皆為賣出或期權行權後賣出, 沒有公開市場買入紀錄。
- 行權 (以 $0.01 轉換) 後隨即賣出的模式反覆出現, 這類交易多為既有期權變現, 並非新增持股信心的訊號。
- 主要賣方:
  - ENGUENT JEAN-PIERRE (Officer): 2026-11-03 以 $1.38 賣出 35,000 股 (約 $48K), 行權日為 11-02。其餘 2026-07 至 2026-10 有多次月度賣出, 每筆約 $36K-86K。6 個月內合計賣出約 $0.36M。
  - O'HARA JOHN CHARLES (CFO): 2026-05 至 2026-06 多次賣出, 每筆約 $0.5M 以內, 價格區間 $3.50-3.69。
  - MOREIRA CARLOS CREUS (CEO): 2026-05-29 與 2026-06-03 賣出, 合計約 $0.11M。
  - BUONANNO FRANCK JEAN (Officer): 2026-05-14 以 $2.90 賣出 20,000 股 (約 $58K)。
- 注意: 6 個月內價格由 $3.5 左右下跌至 $1.38, 賣出價格逐期走低, 但仍持續賣出。
- 合計約 $0.63M 為工具回傳 Value 欄位加總, 由 Shares × Price 手工核對 (例: 35,000 × 1.38 ≈ $48.3K) 一致。

## Ownership shifts
- 內部人持股 3.36%, 機構持股 6.49% (機構占流通股 6.71%), 機構家數 122。
- 機構持股比例偏低, 集中度不高。僅有單期快照, 無法判斷季度趨勢。
- 大股東集中度的風險不在於單一大戶, 而在於機構參與度低, 流動性與承接力相對弱。

## Net sentiment score
Composite: **偏空 (bearish)**, 信心 **低**。
- 空方依據: 內部人 6 個月持續淨賣出且無公開市場買入; 股價由 $3.5 跌至約 $1.39; 動能評分 Very Weak; 估值 P/S 21.6x 偏離產業均值。
- 多方依據: 分析師 2 buy / 0 sell (yf), 但覆蓋極少, 且與 MarketBeat 分布不同。
- 散戶情緒未能取得, 整體結論主要依賴分析師、內部人與價格動能三項, 因此信心降為低。

Divergence flag: **無法判定 (資料不足)**。分析師 (偏多) 與內部人 / 價格動能 (偏空) 方向不一致, 但散戶端缺資料, 無法確認是否與散戶同向或反向。若日後取得 Reddit / StockTwits 資料, 應優先補充此項。

## 資料缺口與來源狀態
- Reddit (r/wallstreetbets, r/stocks): 工具拒絕抓取, 已略過。
- StockTwits: DNS 解析失敗 (api.stocktwits.com 未於 session 網路允許), 已略過。
- yf 工具: Yahoo cookie / crumb 抓取失敗, 但 recommendations, rec_summary, insider, major_holders 皆有回傳資料。
- 網頁搜尋: 結果日期分散 (2026-08 至 2026-11-03), 價格快照互相矛盾 (約 $1.39 至 $6 以上), 已以最近期的 2026-11-03 數據為準。

SENTIMENT REPORT COMPLETE
