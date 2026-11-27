# Sentiment — IRM as of 2026-11-28

注意事項:
- 本機環境日期為 2026-11-27,任務指定 as-of 2026-11-28。本報告只採用可取得的資料,最新一筆內部人交易為 2026-11-12,未找到 11-13 之後的資料。11-28 當日數據一律標示 DATA_UNAVAILABLE。
- 依指示只使用 WebSearch 與本地 yf 工具,未對財經網站或 Reddit / StockTwits 做 WebFetch。Reddit 與 StockTwits 直接查詢未執行,改以搜尋摘要判斷。
- 未借用任何過往 daily/ 報告的數字。

## Analyst consensus
yf rec_summary (0m): 4 Strong Buy / 7 Buy / 0 Hold / 1 Sell / 0 Strong Sell,共 12 家。與 -3m 相比,Buy 由 6 增為 7,其餘不變。
- 其他來源數字不一致: Barchart 稱 9 Strong Buy / 1 Moderate Buy / 1 Hold / 1 Strong Sell (12 家),TipRanks 平均目標價 $125.57 (9 家),Benzinga 平均目標價 $126 (10 家,頁面可能過時),Barchart 平均目標價 $134、最高目標價 $153,Google Finance 平均目標價 $146.57 (7 家,資料約為 8 月)。
- 近期動作(以搜尋摘要為準,未能逐一核對原始券商公告):
  - JPMorgan 5/1 維持 Overweight,目標價 $121 升至 $138。
  - Barclays 7/1 維持 Overweight,目標價 $127 升至 $143,理由為超大規模與企業 AI 需求。
  - Wall Street Zen 7/25 由 buy 降為 hold (此為評等機構,非傳統券商)。
  - Wells Fargo 8/6 維持 Overweight,目標價 $135 升至 $140。
  - Truist 8/27 維持 Buy,目標價 $140 升至 $155。
- 11/5 Q3 財報後是否有新的券商評等變動,未找到可靠資料,標示 DATA_UNAVAILABLE。
- 結論: 券商整體偏多,但目標價來源彼此差距大 (約 $126 至 $155),且 8 月後的目標價資料可能已過時。

## Retail social
- Reddit: 搜尋只找到 2024-08 的 r/wallstreetbets DD 貼文 "Iron Mountain isn't worth $30 Billion Dollars DD",偏空,主張資料中心去槓桿與債務壓力。近期 (2026) 相關討論未搜尋到,標示 DATA_UNAVAILABLE。r/stocks 未查到。
- StockTwits: 搜尋摘要顯示頁面標示 "Bullish Sentiment",股價約 $128.31 (日期不明,可能早於 11 月財報),未能取得多空百分比。
- X / 新聞: AltIndex 顯示 X 情緒 86/100 偏多,提及量約 2 則/日,高於其近期平均 (該頁日期不明)。
- TipRanks 投資人情緒標示 Positive。SentiSense 30 日分數 12 (輕微偏多,快照日期 2026-09-23)。
- 聲量: 無可靠的同期提及數與基準比較,僅能定性為「低於大型股,但 X 上略高於平均」,信心低。
- Retail 傾向: 偏多但資料陳舊,無近期 (11 月) 散戶原文可引用。
- 主題:
  - 資料中心與 ALM (資產生命週期管理) 成長,被視為 AI 題材受益者。
  - 負債與 REIT 結構 (2024 DD 的主要論點)。
  - 11/5 財報後 revenue guidance 低於預期的疑慮。
- 代表性觀點 (摘要,非原文): 2024 DD 主張估值過高、債務需靠出售資料中心資產償還。

## Market reaction context (非情緒來源,僅作背景)
- 2026-11-05 Q3 財報: Adjusted EPS $0.64 優於 $0.61 預期,營收約 $2.0B 符合預期,上修全年展望並將股息提高 15%。
- 股價當日下跌約 11% (Trefis),11/6 收盤約 $105.02 (Fox Business)。市場反應主要因 Q4 與全年營收指引低於分析師預期,以及上修幅度未給出具體數字。
- 過去六個月股價約跌 15.6% (含股息),同期 S&P 500 約上漲 0.8% (Trefis)。

## Insider activity
統計區間 2026-05-28 至 2026-11-28 (yf 資料最後一筆為 11-12)。

- 公開市場買入 (open-market buy): 0 筆。
- 公開市場賣出 (USD): 約 $33.2M,共 14 筆,以 Sale 計,另含 Option 行使後賣出。
- 行使選擇權 (conversion at $37.00) 本身不計入買入。
- 其他: 董事 Walter Rakowich 於 11/12 有 5,000 股贈與 (gift),價值 0,不計入買賣。

按人員:
- William L. Meaney (CEO): 6 筆賣出,約 $27.0M,約 230,844 股 (每月約 38,474 股,伴隨同量選擇權行使,6/1 至 11/6)。
- Mark Kidd (Officer): 4 筆賣出,約 $2.9M,24,000 股 (6/1、7/1、8/7、9/1)。
- Greg McIntosh (Officer): 4 筆賣出,約 $3.2M,約 26,839 股 (含 8/6 一筆約 $1.5M)。

觀察: 賣出高度規律,每月初 (6/1、7/1、8/7、9/1、10/1、11/2、11/6) 重複出現,與預定計畫性賣出一致,但無法確認是否屬 10b5-1 計畫,需查 SEC Form 4 註記。CEO 持續賣出,未見公開市場買入。

## Ownership shifts
- yf major_holders: 機構持股 87.9% (流通股 88.7%),機構數 1,593 家。內部人持股 0.88%。
- 機構持股的時間序列 (季度增減) 未取得,標示 DATA_UNAVAILABLE。

## Net sentiment score
Composite: 中性偏多 (信心: 低)
- 券商面: 偏多 (11 Buy / 1 Sell),目標價調升多於下調。
- 內部人面: 偏空 (CEO 持續規律賣出,無公開買入)。
- 散戶面: 偏多但資料陳舊 (AltIndex 86/100、SentiSense 12、TipRanks Positive),無 11 月樣本。
- 價格面: 財報後急跌,六個月弱勢,市場情緒趨於保守。

Divergence flag: 無法判定。券商與散戶 (陳舊資料) 偏多,與 CEO 持續賣出及財報後市場反應偏空,屬於內部人與市場反應之間的分歧,但缺乏 11 月散戶資料,故無法確定散戶傾向是否與券商相反。

## Metrics table

| 指標 | 數值 | 日期 / 來源 | 備註 |
|---|---|---|---|
| 分析師評等 (Strong Buy / Buy / Hold / Sell / Strong Sell) | 4 / 7 / 0 / 1 / 0 (12 家) | yf rec_summary 0m | 其他來源分布不同 |
| 平均目標價 | $125.57 至 $146.57 (來源分歧) | TipRanks / Benzinga / Barchart / Google | 日期各異,多為 8 月前後 |
| 近期評等下調 | Wall Street Zen buy → hold (7/25) | MarketBeat 搜尋摘要 | 非傳統券商 |
| 公開市場內部人買入 (6 個月) | 0 筆 / $0 | yf insider | 區間至 11/12 |
| 公開市場內部人賣出 (6 個月) | 約 $33.2M (14 筆) | yf insider | CEO 約 $27.0M |
| 內部人淨買賣 (6 個月) | 淨賣出約 $33.2M | 計算 | 不含 gift 與 conversion |
| 機構持股比例 | 87.9% | yf major_holders | 機構數 1,593 |
| 內部人持股比例 | 0.88% | yf major_holders | |
| Reddit 近期貼文 | DATA_UNAVAILABLE | WebSearch | 僅找到 2024-08 DD |
| StockTwits 多空比 | DATA_UNAVAILABLE | WebSearch | 僅標示 Bullish |
| X 情緒分數 | 86 / 100 (偏多) | AltIndex | 日期不明 |
| X 提及量 | 約 2 則/日 | AltIndex | 日期不明,定性 |
| SentiSense 30 日分數 | 12 (輕微偏多) | SentiSense | 2026-09-23 |
| 2026-11-05 財報後股價跌幅 | 約 -11% | Trefis | 不同來源差異大 |
| 11/6 收盤價 | $105.02 | Fox Business | 11-28 收盤 DATA_UNAVAILABLE |
| 過去 6 個月股價報酬 (含股息) | 約 -15.6% | Trefis | 同期 S&P 500 約 +0.8% |
| 綜合情緒 | 中性偏多 (信心低) | 本報告 | 無 11 月散戶資料 |
| 分歧旗標 | 無法判定 | 本報告 | |

SENTIMENT REPORT COMPLETE
