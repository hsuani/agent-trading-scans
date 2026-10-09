# Sentiment — SH (ProShares Short S&P 500) as of 2026-10-10

> 資料時效聲明：本報告指定 as-of 日期為 2026-10-10，但實際執行日為 2026-10-09，無法取得 10-10 當日資料。下列數據為搜尋可得的最新讀數，時間落在 2026-10-01 前後至 2026-09-23 之間，已逐項標註日期。不得將這些數字視為 10-10 當日值。

## 標的性質與解讀框架

SH 為 -1x 反向 S&P 500 ETF，屬於避險／做空大盤工具。以下判讀採「大盤情緒極端 → 對做空部位是否有利」的反向角度，並不構成交易建議。資料缺口較多，多數指標標為 DATA_UNAVAILABLE。

## 1. 市場情緒極端指標

| 指標 | 最新可得讀數 | 日期 | 判讀 |
|---|---|---|---|
| AAII 散戶情緒 Bullish / Neutral / Bearish | 32.7% / 19.2% / 48.1% | 週末 2026-09-23 | Bearish 高於歷史均值 31.5%，Bullish 低於均值 37.5%，偏悲觀 |
| AAII 近三週前序列 | 9/16：28.8 / 17.9 / 53.3；9/9：38.0 / 22.7 / 39.3 | 2026-09 | 9/16 週 Bearish 達 53.3%，之後回落 |
| AAII 10-01 週 | DATA_UNAVAILABLE | 2026-10-01 | 未找到 |
| VIX 收盤 | 16.39（+0.31%） | 2026-10-01 | 中低檔，屬平靜波動區間 |
| VIX 期限結構（VIX9D/VIX/VIX3M） | DATA_UNAVAILABLE | — | Cboe 頁面快取日期不明，無法確認當前是正價差或倒掛 |
| CNN Fear & Greed | DATA_UNAVAILABLE（當週） | — | 9 月中約 30（Fear），7 月 21 日約 40（Fear），5 月中約 63–66（Greed），時序不連續，僅供參考 |

注意：AAII 頁面列出 9/24 週「1-Year Bearish High 100.0%」，明顯為資料錯誤，本報告不採用。

## 2. 選擇權部位比率

- 總 Put/Call（股票＋指數）：約 0.78，來源為 2026-10 初的一則摘要頁面，係由當日成交張數換算，屬間接計算。
- 股票專用 Put/Call：最新可靠讀數為 0.55（2026-08-03），低於其長期均值約 0.58，代表個股買權交易相對活躍，偏樂觀。
- 指數專用 Put/Call：0.88（2026-08-03），高於股票值，顯示機構／投資人仍以指數 put 做對沖。
- 2026-10 指數 Put/Call：DATA_UNAVAILABLE（未找到 Cboe 官方 10 月統計頁）。

## 3. 機構 vs 散戶部位

- 2026 年 3 月起的空頭潮：一則 Crypto Briefing 報導指出，Goldman Sachs prime brokerage 數據顯示，3 月期間對沖基金放空與買進比例約 7.6:1，約 76% 的放空集中於大盤指數與 ETF。4 月 8 日停火消息後快速回補，為 2020 年 3 月以來最快的回補速度。
- 10 月淨部位（CFTC COT、prime brokerage）：DATA_UNAVAILABLE。搜尋結果中的 2023、2025 年資料已過時，不納入判讀。
- 對 SH 的含意：若 3 月的擁擠空頭已於 4 月回補，目前是否重新累積空頭部位無從確認。

## 4. 市場脈絡（2026-10-01 收盤）

- S&P 500 收 7,666.45（+0.19%），年初至今 +11.78%。
- 能源與科技為當日主要上漲板塊，醫療保健為最弱板塊（-2.65%）。
- 10 年期公債殖利率 5.24%（-1.06%）。
- 季節性：10 月傳統上為波動較大的月份，有評論認為 VIX 仍處下行趨勢，但屬於季節性觀點，非當日數據。

## 5. 綜合情緒判讀

- 散戶情緒（AAII）：偏悲觀，Bearish 高於均值，且 9 月中出現單週 53.3% 的高點，後回落。
- 波動率（VIX 16.4）：平靜，未見恐慌極端。
- 選擇權（股票 P/C 0.55）：偏樂觀，與 AAII 的悲觀方向相反。
- 機構：2026 年 3 月的空頭擁擠已在 4 月消化，目前部位資料缺失。

綜合判讀：**中性偏多頭（neutral-to-bullish）**，信心度：低。

理由：價格與波動率仍偏穩（VIX 16、S&P 年初至今 +11.8%），股票選擇權偏樂觀，對於做空大盤不利；AAII 偏悲觀則是反向訊號的正面因子，但單一週訊號力道有限，且缺乏 10 月數據。

Divergence flag：**是**。散戶（AAII）偏空，與股票選擇權買權活躍、價格走勢偏多的方向不一致，兩者分歧。

## 6. 資料缺口與後續查核建議

1. AAII 2026-10-01 與 10-08 週讀數：查 aaii.com/sentimentsurvey（每週四發布）。
2. VIX 與 VIX 期限結構當日值：查 Cboe term structure 即時頁面。
3. CNN Fear & Greed 當日值：查 CNN Business 頁面。
4. 股票與指數 Put/Call 當日官方值：查 Cboe daily market statistics。
5. 機構淨部位：查 CFTC COT 最新一期的 S&P 500 期貨非商業淨部位。

## 資料來源（搜尋結果）

- AAII Investor Sentiment Survey: https://www.aaii.com/sentiment-survey
- Cboe VIX Term Structure: https://www.cboe.com/tradable_products/vix/term_structure
- Put/Call 摘要與 Equity P/C 追蹤: https://www.thetrading.tools/put-call-ratio
- Fear & Greed 歷史數據: https://www.finhacker.cz/en/fear-and-greed-index-historical-data-and-chart/
- 市場收盤 2026-10-01: https://tapeboard.com/blog/market-pulse-2026-10-01
- 機構空頭潮 2026-03/04: https://cryptobriefing.com/hedge-funds-resume-shorting-after-short-squeeze/

SENTIMENT REPORT COMPLETE
