# 新聞 — UUP as of 2026-11-28

注意事項：`pipeline/tools/yf UUP news` 回傳 403，無法取得 yfinance 新聞清單，因此公司新聞以 WebSearch 補足。`info` 可用（快取時間 2026-11-27 16:37 UTC）。多數搜尋結果日期不明或為 2025 / 早期 2026 資料，已排除或標註。依指示，無法確認者以 DATA_UNAVAILABLE 標示。未引用 daily/ 下舊報告的任何數字。

UUP 為 Invesco DB US Dollar Index Bullish Fund（做多 DXY 期貨的 ETF），本身沒有公司層級新聞，故「公司新聞」在此定義為 UUP 相關價格與基金事件。

## Top company-specific headlines (last 14d)
- 2026-11-27 — UUP 收盤 29.715 USD，較前收 29.60 上漲 +0.39%（yf info 快取）。日內區間 29.665–29.72，成交量 349,097 股，低於 10 日均量 1.81M，屬於低量小幅反彈。Impact: neutral。原因：單日波動小，無法判斷趨勢轉折。
- 2026-11-27 — 基金規模 totalAssets 約 0.48B USD（481,364,192 USD），費用率 0.75%。Impact: neutral。原因：流動性尚可，但 AUM 小，對資金流敏感。
- 無 DATA_UNAVAILABLE 以外的 UUP 基金事件（分配、換倉、結構調整）可確認。yf info 顯示 trailing 配息為 0。

## Sector macro
- 2026-11-19 — FOMC 會議紀錄（minutes）被 FXStreet 描述為「非常鷹派」([FXStreet, 2026-11-19](https://www.fxstreet.com/analysis/the-last-fed-meeting-minutes-were-very-hawkish-202611191521))。Impact on 美元: bullish。原因：支撐 12 月升息預期，利差支撐美元。
- 2026-10-28 — Fed 維持利率不變，區間 3.75%–4.00%（多數來源），投票 10–2，Cook 與 Hammack 主張立即升息。美元僅小幅走弱，DXY 約 102.1（[FXStreet](https://www.fxstreet.com/news/the-federal-reserve-holds-rates-and-two-officials-vote-for-a-hike-why-the-us-dollar-stayed-flat-anyway-202610291142)、[TradingEconomics](https://tradingeconomics.com/united-states/currency/news/595937)）。Impact on 美元: neutral to bullish。原因：市場反應有限，但鷹派異議票顯示內部偏緊。
  - 注意：一則 Forex.com 報導寫區間 3.50%–3.75%、11–1 投票，與其他來源矛盾，未採用。
- Fed 主席 Warsh 在 10 月會議後拒絕承諾 12 月行動，市場解讀為略偏鴿（[Investinglive](https://investinglive.com/central-banks/warsh-won-t-prejudge-rest-of-2026-names-october-and-december-as-decision-points/)）。Impact on 美元: 略偏空。原因：保留彈性削弱升息的確定性。
- 10 月會議後 12 月升息機率被引用為約 78%–88%（CME FedWatch，來源日期為 10 月底，目前數字 DATA_UNAVAILABLE）。Impact on 美元: 若 12 月升息定價被撤回，將引發美元修正。
- 利差：ECB 存款利率 2.50%（9 月升息後），10 月底 FXStreet 仍認為 12 月升息為基本情境；BoJ 政策利率 1.25%（9 月升息），11 月初 BoJ 會議紀錄支持續升。Impact on 美元: 美元相對 EUR/JPY 的利差方向大致中性偏多，但近期 EUR/JPY、USD/JPY 即時水準 DATA_UNAVAILABLE。
- 避險流向：一則 TradingEconomics 文章（日期 2026-10-23）提到殖利率急跌、日圓受益、美元接近三週低點。Impact on 美元: 偏空。原因：風險迴避時流向日圓而非美元，美元避險地位不再單純。
- DXY 水準：一則未標註日期的 TradingEconomics 摘要稱 DXY 跌至 101.6，為兩週低點，本週約跌 0.4%。日期無法確認，僅作參考。10 月初 DXY 高點約 101.61，為 2026 年 6 月以來最高（該標題數字與內文不一致，視為不可靠）。
- 無法取得 11 月中至 11 月 27 日的 DXY 日線資料，以及 11 月內的關稅、地緣政治新聞：DATA_UNAVAILABLE。

## Peer signals
- EUR（ECB）— 基本情境 12 月再升息 1 次，利差支撐歐元相對美元（以 10 月底資料為準，目前 DATA_UNAVAILABLE）。
- JPY（BoJ）— 1.25%，持續升息預期，日圓為近期避險受益者。
- 其他 G10 最新 11 月資料 DATA_UNAVAILABLE。
- 無 UUP 直接同類 ETF（UDN 為做空 DXY，未查詢）。

## Forward calendar (next 14d)
- 2026-12-04（週五）08:30 ET — 美國 11 月非農（Nonfarm Payrolls），由 BLS 公布，為 12 月 FOMC 前最後主要就業數據。預期影響：強勁數據支撐美元，弱數據削弱 12 月升息定價。
- 2026-12-09 — FOMC 會議。預期影響：為本期最大事件，若升息定價撤回，UUP 承壓；點陣圖與 Warsh 措辭為關鍵。
- 2026-12-10 — 11 月 CPI，僅單一來源（financecalendar.com），BLS 未確認：標註為未驗證。若落在 FOMC 後，影響延後至 12 月 10 日。
- ECB 與 BoJ 12 月會議日期 DATA_UNAVAILABLE（本次未查到確切日期）。

## Net read
本期（近 30 日）新聞對美元的淨傾向為偏多但幅度有限，偏多 · 中低強度。支撐面來自 10 月底 FOMC 維持利率但兩票主張升息，以及 11 月 19 日公布的鷹派會議紀錄，市場仍定價 12 月升息的機率高（10 月底約 78%–88%）。反面因素包括 Warsh 拒絕承諾 12 月行動、避險資金流向日圓而非美元、以及 DXY 在 10 月高點 101.6 附近停滯，顯示美元上行動能減弱。UUP 當日收盤 29.715，位於 52 週區間 26.40–29.84 的上緣（距高點約 0.4%），高於 50 日均線 29.04 與 200 日均線 28.14，趨勢偏多。關鍵變數為 12 月 4 日非農與 12 月 9 日 FOMC。注意：本報告的數據多數為 10 月底至 11 月中，11 月下旬的 DXY 與利率期貨定價缺口較大，結論信心偏低。

## 指標摘要表

| 指標 | 數值 | 日期 / 來源 | 備註 |
|---|---|---|---|
| UUP 收盤價 | 29.715 USD | 2026-11-27 (yf info) | 前收 29.60，+0.39% |
| 日內區間 | 29.665–29.72 USD | 2026-11-27 (yf info) | |
| 52 週區間 | 26.40–29.84 USD | yf info | 距高點約 -0.4% |
| 50 日均線 | 29.04 USD | yf info | |
| 200 日均線 | 28.14 USD | yf info | |
| 今年以來報酬 (YTD) | +7.13% | yf info | |
| 基金規模 (AUM) | 0.48B USD | yf info | 481,364,192 USD |
| 費用率 | 0.75% | yf info | |
| 成交量 / 10 日均量 | 349,097 / 1.81M 股 | yf info | 當日量偏低 |
| 聯邦基金利率區間 | 3.75%–4.00% | 2026-10-28 (多來源) | 一則來源 3.50%–3.75%，未採用 |
| 10 月 FOMC 投票 | 10–2（主張升息 2 票） | 2026-10-28 | Cook, Hammack |
| 12 月升息機率 | 78%–88% | 10 月底 | 目前 DATA_UNAVAILABLE |
| DXY 水準 | 約 101.6（未確認日期） | TradingEconomics | 2026 年 10 月初高點約 101.61 |
| ECB 存款利率 | 2.50% | 9 月升息後 | 12 月再升息為基本情境 |
| BoJ 政策利率 | 1.25% | 9 月升息後 | |
| 下一次非農 | 2026-12-04 08:30 ET | BLS | |
| 下一次 FOMC | 2026-12-09 | FedRateCalc | |
| 11 月 CPI | 2026-12-10（未驗證） | financecalendar.com | 單一來源 |
| 美元淨傾向 | 偏多，中低強度 | 本報告 | 信心偏低 |

## 來源
- [FXStreet — 2026-11-19 FOMC minutes very hawkish](https://www.fxstreet.com/analysis/the-last-fed-meeting-minutes-were-very-hawkish-202611191521)
- [FXStreet — Fed holds, two dissent for hike (2026-10-29)](https://www.fxstreet.com/news/the-federal-reserve-holds-rates-and-two-officials-vote-for-a-hike-why-the-us-dollar-stayed-flat-anyway-202610291142)
- [TradingEconomics — Dollar weakens on dovish Fed signals](https://tradingeconomics.com/united-states/currency/news/595937)
- [TradingEconomics — Dollar pressured by lower Treasury yields (2026-10-23)](https://tradingeconomics.com/united-states/currency/news/594451)
- [Investinglive — Warsh won't prejudge rest of 2026](https://investinglive.com/central-banks/warsh-won-t-prejudge-rest-of-2026-names-october-and-december-as-decision-points/)
- [Investinglive — Much ado about nothing, December hike bets](https://investinglive.com/central-banks/much-ado-about-nothing-fed-chair-warsh-talks-up-a-storm-but-december-rate-hike-bets-barely-budge/)
- [BabyPips — FOMC event guide Oct 2026](https://www.babypips.com/analysis/event-guide-forex-us-fomc-statement-october-2026-10-27)
- [FXStreet — Central banks a pause (2026-10-30)](https://www.fxstreet.com/analysis/central-banks-a-pause-while-waiting-for-more-information-202610301646)
- [OANDA — Daily market news (2026-11-04 note)](https://www.oanda.com/eu-en/node/369997)
- [FXStreet — USD index new 2026 highs (2026-10-02)](https://www.fxstreet.com/analysis/the-us-dollar-index-just-hit-new-2026-highs-above-10220-this-chart-shows-the-runaway-move-202610021505)
- [BLS — 2026 December release schedule](https://www.bls.gov/schedule/2026/12_sched.htm)
- [FedRateCalc — December 2026 US economic calendar](https://fedratecalc.com/us-economic-calendar/december-2026/)
