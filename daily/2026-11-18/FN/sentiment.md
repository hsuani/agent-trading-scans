# Sentiment — FN as of 2026-11-18

資料品質總結: 分析師評等快照 (yf rec_summary) 可用但四個期間數字完全相同, 疑似靜態快照; 分析師評等變動歷史 (yf recommendations) 未回傳評等變動, 僅回傳與 rec_summary 相同的彙總, 視為 DATA_UNAVAILABLE; 散戶 Reddit / StockTwits 直接抓取受阻, WebSearch 結果多為 2026-05 以前或無日期的聚合站頁面, 無 2026-11 當期散戶資料。整體信心偏低。

## Analyst consensus
yf rec_summary (0m, 四期相同): 7 buy (strongBuy 3 + buy 4) / 2 hold / 0 sell, 合計 9 家。sell 為 0。

Recent moves: DATA_UNAVAILABLE。yf recommendations 未回傳個別評等升降級紀錄; 無法確認近期 upgrade / downgrade 或目標價變動的時間點。

WebSearch 補充 (2026-05 前後, 非當期, 來源為聚合站點): MarketBeat 顯示 "Moderate Buy" 共識, 平均目標價約 664.25 USD, 5 buy / 5 hold (與 yf 9 家的分布不一致, 來源與樣本不同, 未合併計算); Zacks 於 2026-05 升級至 strong-buy; Needham 重申 Buy; JPMorgan 下修目標價至 680 USD 並維持 neutral。以上皆為 2026-05 資料, 不能代表 2026-11-18 當下評等。

## Retail social
- Reddit: 直接抓取受阻 (依任務指示改用 WebSearch)。WebSearch 僅找到一則 r/wallstreetbets 貼文 (標題 "Good week so far with $FN", ChartExchange 情緒分數約 0.44, 偏正面), 發文日期相對於 2026-11-18 無法確認, 單一樣本不足以代表趨勢。Tilt: 樣本不足, DATA_UNAVAILABLE。
- StockTwits / X: StockTwits 直接抓取受阻, WebSearch 未找到當期 StockTwits 訊息流。AltIndex 頁面顯示約 1,899 位 StockTwits 追蹤者, 但 mentions 為 N/A 且無日期, 僅作參考。X 方面未找到 2026-11 的可用貼文。
- Buzz volume (提及量相對於一般水準): DATA_UNAVAILABLE。無可靠的 mention count。
- Themes (由有限的 WebSearch 聚合文字歸納, 非直接社群樣本): 
  - AI 資料中心與光學 (optical) 需求題材, 常見於財經聚合頁的正面敘述。
  - 估值偏高 (P/E 在 2026-05 的 MarketBeat 頁面約 69) 與營收集中於電信 (telecom) 的疑慮, 來自 2026-05 的分析文字。
  - 股價大幅波動 (2026-05 多次跳空、回檔; Nasdaq 聚合轉述一則無日期的 "sank 23.4% this week")。
- Retail tilt: DATA_UNAVAILABLE (樣本不足, 不宜判定 bullish / bearish / mixed)。

## Insider activity
資料窗口: 2025-11-18 至 2026-11-18 之中, 6 個月窗口為 2026-05-18 至 2026-11-18。

Net 6mo (USD): 公開市場買進 $0.00M, 公開市場賣出約 $2.74M (合計 2 筆)。
- 2026-05-22: Director BAHRAMI HOMA 賣出 2,500 股, 約 $1.78M (約 711.91 USD/股)
- 2026-09-03: Officer ARCHER EDWARD T 賣出 2,500 股, 約 $0.96M (約 385.58–386.34 USD/股)

Notable: 
- 6 個月內無 CEO / CFO 公開市場賣出; CEO GRADY SEAMUS 與 CFO SVERHA CSABA 於 2026-08 有 Stock Award(Grant) 紀錄, 性質為授予、非現金買賣, 未計入淨買賣金額。
- 6 個月內無任何公開市場買進紀錄。
- 2025-08 至 2025-12 期間之賣出紀錄較多 (含 CEO GRADY SEAMUS 約 $10.0M 之 2025-11-26 賣出), 超出本次 6 個月窗口, 僅作背景。

資料註記: 2026-09 後的股價水準 (約 385 USD) 與 2026-05 (約 712 USD) 差距大, 與 WebSearch 的股價 (有頁面列 348.52 與 654.16 等不一致數字) 無法互相驗證, 股價僅供參考, 未用於計算。

## Ownership shifts
- insidersPercentHeld: 0.259% (內部人持股極低)。
- institutionsCount: 975。
- institutionsPercentHeld: 100.27%, institutionsFloatPercentHeld: 100.53%。超過 100% 不合理, 判定為資料錯誤, 不可用於判斷機構集中度趨勢。
- 趨勢 (近 2 至 4 期的變動): DATA_UNAVAILABLE。

## Net sentiment score
Composite: neutral (信心低)。
- 分析師面: 偏多 (7 buy / 2 hold / 0 sell), 但快照期間疑似未更新。
- 內部人面: 偏空 / 中性 (6 個月內僅 2 筆公開市場賣出、無買進, 金額約 $2.74M, 規模對 FN 市值而言屬小額; 授予性質之股票不計入)。
- 散戶面: DATA_UNAVAILABLE。

Divergence flag: 無法判定 (DATA_UNAVAILABLE)。散戶 tilt 缺漏, 無法確認是否與分析師傾向相反。若日後取得可靠的散戶樣本, 可再比對。

Confidence: 低。主要限制: (1) rec_summary 疑似靜態; (2) 評等變動歷史缺漏; (3) 機構持股比例資料錯誤; (4) 散戶來源 (Reddit / StockTwits) 受阻, 聚合搜尋無當期結果。

SENTIMENT REPORT COMPLETE
