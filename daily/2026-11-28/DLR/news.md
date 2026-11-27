# News — DLR as of 2026-11-28

資料來源與限制
- yfinance 新聞端點 (`pipeline/tools/yf DLR news`) 回傳 proxy 403 (CONNECT tunnel 被拒, Yahoo 主機不在本 session 允許範圍)，依規定不重試、不繞過。因此本報告的公司新聞全部來自 WebSearch，無法做到 yfinance 的逐篇時間戳與來源覆蓋。
- `pipeline/tools/yf DLR info` 正常: Sector = Real Estate, Industry = REIT - Specialty。
- 報告時間窗: 2026-10-29 至 2026-11-28 (30 天)。超過 2026-11-28 的資料一律視為未知。未引用任何舊版 daily/ 報告的數字。
- 股價、市值、成交量、分析師最新評等: DATA_UNAVAILABLE (搜尋結果無 2026-11 可驗證報價; 分析師目標價來源日期不明)。

## Top company-specific headlines (last 14d 與 30d 背景)

- 2026-10-29 — Q3 2026 財報: 核心 FFO 每股 $2.10 (年增 11%, 高於一致預期約 6.6%); 2026 核心 FFO 指引上調至 $8.30–8.35 (原 $8.15–8.20); 營收指引上調至 $7.05–7.125B (原 $6.85–6.95B); 創紀錄 bookings DLR 持分 $627M (100% 口徑年化 GAAP base rent $855M); backlog DLR 持分約 $1.85B (100% 口徑約 $2.5B) (Zacks / Finviz 新聞稿轉述)。Impact: bullish。理由: beat-and-raise 且 hyperscale 與 0–1 MW 租約同創高，直接支撐 2026 FFO 上修。
  - 來源: [Finviz 新聞稿](https://finviz.com/news/412047/digital-realty-reports-third-quarter-2026-results)、[Zacks](https://zacks.com/stock/news/3019741/dlr-q3-ffo-revenues-beat-estimates-on-rental-growth-26-view-raised)
- 2026-10-29 — Q3 季內土地支出 $741.9M，新增基地包括印第安納 (>1 GW IT 容量)、芝加哥 (約 360 MW)、夏洛特 (最高 600 MW)。Impact: neutral-to-bullish。理由: 供給儲備充足，但同時加重資本支出與槓桿壓力 (見下)。
  - 來源: [Capital.com 整理](https://capital.com/en-au/news/digital-realty-reports-third-quarter-2026-results)、WebSearch 結果彙整
- 2026-10-29 — 資本支出與資金成本指引: 2025–2029 年度 capex 指引 $5–7B/年; 管理層預期槓桿由 3.6x 上升約 1 turn; 加權資金成本約上升 150 bp。Impact: bearish。理由: 融資成本上行會壓縮開發利差與 FFO 增幅。
  - 來源: WebSearch 'Digital Realty Q3 2026 results' 彙整 (Webull 逐字稿摘要)
- 2026-11-05 — 於巴西聖保羅 Vinhedo II 園區開設拉丁美洲首座 Digital Realty Innovation Lab (DRIL), 供客戶測試多供應商 AI 基礎設施。Impact: neutral。理由: 產品與客戶體驗強化，財務影響極小。
  - 來源: [Finviz](https://finviz.com/news/417163/digital-realty-innovation-lab-sao-paulo-expands-ai-infrastructure-testing-in-latin-america)
- 2026-11-12 — 董事會宣告 Q4 2026 普通股與特別股現金股利 (新聞稿已發布)。Q1–Q3 普通股股利皆為 $1.22/股。Q4 金額、record date、payment date: DATA_UNAVAILABLE (搜尋結果截斷)。Impact: neutral。理由: 股利政策延續，無變化跡象。
  - 來源: [Finviz 新聞稿](https://finviz.com/news/422125/digital-realty-declares-quarterly-cash-dividends-for-common-and-preferred-stock)
- 2026-11-12 — Oxford Economics 報告: 資料中心 (US) 總報酬 Q3 2026 僅 0.4%，過去 12 個月 2.4%，歸因於大量在建與成本上升; 開發重心向 Midwest / Southeast / Mountain West 轉移 (電力、許可為瓶頸)。Impact: bearish (產業層級)。理由: 報酬降溫與新增供給可能壓抑未來租金成長與估值。
  - 來源: [Oxford Economics](https://www.oxfordeconomics.com/resource/us-data-center-real-estate-outperforms-as-development-expands-into-new-markets/)
- 2026-11-17 起 — 中期選舉後資料中心反彈議題升溫: Sen. Sanders 呼籲「全國資料中心暫停」; 紐約州為唯一州級 moratorium，地方層級約 40 州有禁令或暫停規定 (S&P Global 報導); 電費議題成為選戰主軸。Impact: bearish (政策與審批風險)。理由: 增加選址、併網與許可時程的不確定性，對以大型園區擴張為主的 DLR 相關。
  - 來源: [Fortune 2026-11-17](https://fortune.com/2026/11/17/democrats-ai-data-center-backlash-electricity-costs-regulation-economic-growth/)、[S&P Global](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/100126-data-center-backlash-shapes-midterm-ballots-campaigns-across-us)
- 2026-10-06 (30 天窗外, 僅作背景) — 歐元 €1B 5.125% 2036 年到期 guaranteed notes 定價 (99.289%); 另有 CHF 三批次票據 (淨收益約 CHF 508M, 約 US$611M, 日期與淨額來源間有差異)。Impact: bearish-on-cost (票息水準顯示融資成本抬升)。
  - 來源: [Finviz 新聞稿](https://finviz.com/news/399618/digital-realty-announces-pricing-of-1-billion-of-guaranteed-notes-due-2036)
- 分析師評等與目標價 (日期不明，不納入淨讀數): 來源包括 Scotiabank 目標價 $222 (Outperform)、JPMorgan 目標價 $230 (Overweight)、DBS $213 (Buy, 6 月重申)、CNN 彙整 33 家平均目標價 $220。Impact: 無法判定時點，僅作參考。
  - 來源: [Nasdaq](https://www.nasdaq.com/articles/do-wall-street-analysts-digital-realty-trust-stock)、[Yahoo Finance](https://finance.yahoo.com/news/wall-street-analysts-target-price-161148082.html)

## Sector macro

- 2026-09 (背景，已確立) — Fed 升息 25 bp 至 3.75%–4.00%，為三年來首次升息 (Chair Kevin Warsh 任內)。Impact on 不動產 / REIT: bearish。理由: 利率上行直接壓抑 REIT 估值; Nareit 指出 2026-09 REITs 下跌 5.7%，10 年期殖利率觸及 5.27%。
  - 來源: [Morningstar 10 月 FOMC 前瞻](https://www.morningstar.com/markets/what-expect-october-2026-fed-meeting)、[CRE Daily / Nareit](https://www.credaily.com/?p=223638)
- 2026-10 — 10 月 CPI 高於預期 (Cboe 與 MPA 報導); 10 月 FOMC 維持利率不變，但有兩位委員主張再升息 (Seeking Alpha 摘要)。Impact on REIT: bearish。理由: 通膨黏性提高再升息機率。
  - 來源: [Cboe](https://www.cboe.com/insights/posts/hot-cpi-report-puts-fire-under-interest-rate-hike-possibilities)、[MPA](https://www.mpamag.com/us/mortgage-industry/industry-trends/mortgage-rates-set-to-rise-as-october-cpi-tops-forecasts/596855)
- 2026-11-10 — CME FedWatch 顯示 12 月 8–9 日 FOMC 升息 25 bp (至 4.00%–4.25%) 機率約 90.5%，前一週約 77%–84%。Impact on REIT: bearish (已大幅計價)。理由: 若兌現，融資成本與 cap rate 壓力進一步上行; 若未升息，可能形成反彈空間。注意: 此為 11-10 快照，11-28 最新值 DATA_UNAVAILABLE。
  - 來源: [Cboe 2026-11-10 引用 CME FedWatch](https://www.cboe.com/insights/posts/hot-cpi-report-puts-fire-under-interest-rate-hike-possibilities)
- 2026-11-17 — 中期選舉後，民主黨與 AI 資料中心反彈、電價議題升溫，但國會實際行動停滯 (Bloomberg Law 報導)。Impact on 資料中心 REIT: bearish-policy-risk。理由: 電價敏感度上升，地方審批趨嚴。實證分歧: Dallas Fed 工作論文估計資料中心需求使全國批發電價上升約 6.9%，局部可達 15%; LBNL 認為 2019–2024 住宅電價大致追隨通膨; ITIF 反對 moratorium。
  - 來源: [Fortune](https://fortune.com/2026/11/17/democrats-ai-data-center-backlash-electricity-costs-regulation-economic-growth/)、[ITIF 2026-11-18](https://itif.org/publications/2026/11/18/data-centers-and-electricity-costs-assessment-leads-to-bad-policy/)
- 2026 年 hyperscaler capex — 次要來源估計約 $600B–$650B (年增約 60%)，數字互相衝突。Impact on DLR: bullish (需求端)。理由: 需求支撐 leasing 與 backlog; 但衝突來源須以原始 8-K / 財報校正。
  - 來源: [FourWeekMBA NVDA Q3](https://fourweekmba.com/ai-nvidia-q3-revenue-115-8b-5-7b-above-the-top-of-its-guide/)、[Yahoo Finance](https://finance.yahoo.com/news/nvidia-posts-75-2-margin-183202786.html)
- 供應鏈 — 元件製造商警告短缺可能延續至 2027 年以後 (Nvidia 法說摘要引述，次要來源)。Impact on DLR: 中性偏多 (需求旺) 但 build cost 與工期風險上升。
  - 來源: [XenoSpectrum](https://xenospectrum.com/en/nvidia-fy2027-q3-data-center-growth/)
- 2026-11-17 — Nvidia FY2027 Q3 營收 $115.8B (年增約 103%, 季增 20%), 資料中心營收 $107.6B, Q4 營收指引 $130.0B (次要來源 FourWeekMBA / Guru 類站點，與 FY26 Q3 $57.0B 之年增 103% 數字一致)。Impact on DLR: bullish (AI 需求證據)。
  - 注意: 同一搜尋結果中有「Jensen Huang 辭任 CEO」之單一來源敘述，無第二來源佐證，本報告不採用。
  - 來源: [FourWeekMBA](https://fourweekmba.com/ai-nvidia-q3-revenue-115-8b-5-7b-above-the-top-of-its-guide/)

## Peer signals

- EQIX (Equinix) — Q3 2026 營收 $2.57B (年增 11%)，2026 全年指引第三次連續上調 (2026-10-28)。Impact on DLR: bullish (同業需求與定價同步走強)。
  - 來源: [Finviz](https://finviz.com/news/410507/equinix-reports-third-quarter-results-and-raises-2026-guidance)、[Futurum](https://futurumgroup.com/insights/equinix-q3-fy-2026-pricing-and-interconnection-support-growth/)
- EQIX — 2026-11-06 新加坡 SG6 開幕 (首期 8 MW，綠色規範); 2026-11-16 附屬公司向德州 TDLR 提交 Dallas DA13 (約 $500M) 建案申報 (申報階段，非完工)。Impact on DLR: neutral-to-bullish (同業擴產證明需求，亦加劇供給競爭)。
  - 來源: [Finviz SG6](https://finviz.com/news/418199/equinix-opens-sg6-in-singapore-expanding-ai-ready-capacity-in-one-of-asia-pacifics-most-connected-markets)、Dallas 申報來自 WebSearch 'Equinix EQIX news November 2026' 結果 (無獨立 URL)
- EQIX — 公司表示 Q4 2026 預計交付 >13,000 cabinets，超過 20% 已預售。Impact on DLR: 中性 (同業需求可見度高)。
- NVDA (上游需求) — 見上節 Nvidia 財報; 需求端正向。
- 其他同業 (IRM、AMT/CoreSite 等): DATA_UNAVAILABLE (本次搜尋未取得 2026-11 可驗證新聞)。

## Forward calendar (next 14d, 2026-11-28 至 2026-12-12)

- 2026-12-08 至 12-09 — FOMC 會議 (12-09 決議)。Fed 日曆列為 12/8–9 (屬暫定，需於前次會議確認)。Expected impact: 市場於 11-10 已計價約 90% 升息機率。升息為 bearish (REIT 利率敏感); 按兵不動或鴿派可能帶來 REIT 反彈。最新機率 DATA_UNAVAILABLE。
  - 來源: [Kiplinger FOMC 日程](https://www.kiplinger.com/investing/when-is-the-next-fed-meeting)、[Federal Reserve 日曆](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 11 月 CPI 發布日 — DATA_UNAVAILABLE (未取得官方日程)。預期影響: 若高於預期，升息機率再度上行，REIT 承壓。
- DLR Q4 2026 股利 record date / payment date — DATA_UNAVAILABLE (公告截斷)。預期影響: 中性。
- DLR Q4 2026 財報 — 不在本窗口。Q4 2025 係 2026-02-05 發布，2027 年初確切日期尚未公告 (推論為 2027-02 初)，DATA_UNAVAILABLE。
- EQIX / 其他同業財報 — 本窗口內未查得已知日期，DATA_UNAVAILABLE。

## Net read

以公司基本面看，近 30 天新聞偏多: Q3 同時 beat 與上調全年核心 FFO 指引、bookings 與 backlog 創高、同業 EQIX 也連續上調指引、上游 NVDA 營收與指引超預期，支撐 AI 資料中心需求的敘事。但這些利多幾乎都是已知的 (Q3 財報於 10-29 公布)，而宏觀面明顯偏空: Fed 2026-09 已升息一次，10 月 CPI 偏熱，12 月 8–9 日 FOMC 升息機率於 11-10 達約 90%，直接壓抑 REIT 估值; 公司自身也預告資本支出 $5–7B/年、槓桿上升約 1 turn、加權資金成本約上升 150 bp，FFO 增幅與利差面臨壓力。另外，中期選舉後電價與資料中心 moratorium 議題升溫，增加審批與選址風險，Oxford Economics 亦指出資料中心報酬已降至 0.4% (Q3)。整體淨讀數: 混合偏空 (mixed, 宏觀利率與政策風險主導，公司層級利多為中等強度)。量化價格、評等與 12 月 FOMC 最新機率因資料不可得，無法更精確判定市場反應幅度。本報告不提供交易建議。

## 指標與摘要表

金額單位: USD (B = 十億美元, M = 百萬美元); 不使用億。

| 指標 | 數值 | 單位 | 日期 / 來源 | 狀態 / 備註 |
|---|---|---|---|---|
| Q3 2026 核心 FFO (每股) | 2.10 | USD/股 | 2026-10-29 | 年增 11%，beat 約 6.6% |
| 2026 核心 FFO 指引 (每股) | 8.30–8.35 | USD/股 | 2026-10-29 | 由 8.15–8.20 上調 |
| 2026 營收指引 | 7.05–7.125 | USD B | 2026-10-29 | 由 6.85–6.95 上調 |
| Q3 bookings (DLR 持分) | 627 | USD M | 2026-10-29 | 100% 口徑 $855M 年化 GAAP base rent |
| backlog (DLR 持分) | 1.85 | USD B | 2026-10-29 | 100% 口徑約 $2.5B |
| Q3 土地支出 | 741.9 | USD M | 2026-10-29 | 印第安納、芝加哥、夏洛特 |
| 年度 capex 指引 (2025–2029) | 5–7 | USD B / 年 | 2026-10-29 | 槓桿由 3.6x 升約 1 turn |
| 加權資金成本變動 | +150 | bp | 2026-10-29 | 管理層預期 |
| 普通股季度股利 (Q1–Q3) | 1.22 | USD/股 | 2026-02 至 2026-08 | Q4 金額 DATA_UNAVAILABLE |
| 歐元票據 (2036 到期) | 1.0 | USD B (EUR 等值) | 2026-10-06 | 票息 5.125%，窗口外背景 |
| 聯邦基金利率目標區間 | 3.75–4.00 | % | 2026-09 升息後 | 2026-10 維持 |
| 12 月升息機率 (CME FedWatch) | 約 90.5 | % | 2026-11-10 快照 | 11-28 最新值 DATA_UNAVAILABLE |
| 10 年期公債殖利率 (峰值) | 5.27 | % | 2026-09 | 引自 Nareit / CRE Daily，最新值 DATA_UNAVAILABLE |
| EQIX Q3 營收 | 2.57 | USD B | 2026-10-28 | 年增 11% |
| NVDA FY27 Q3 營收 | 115.8 | USD B | 2026-11-17 | 次要來源，Q4 指引 130.0 |
| hyperscaler 2026 capex 估計 | 600–650 | USD B | 次要來源 | 來源衝突 |
| 股價 / 市值 / 本益比 | DATA_UNAVAILABLE | — | — | 無可驗證 2026-11 報價 |
| 分析師平均目標價 | 220 | USD/股 | 日期不明 | 不納入淨讀數 |

交叉驗算: Q1–Q3 FFO 合計 2.04 + 2.13 + 2.10 = 6.27 USD/股 (Q1 為媒體引述之 FFO, 口徑未確認, Q2 為財報引述之核心 FFO); 2026 指引中點 8.325 減去前三季得 Q4 隱含約 2.05 USD/股，與季度水準一致。口徑差異僅供量級檢查。

NEWS REPORT COMPLETE
