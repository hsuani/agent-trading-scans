# News — SNDK as of 2026-10-21

資料範圍: 2026-09-21 至 2026-10-21 (30 天)。截止日後的資訊一律不納入。
資料限制:
- `pipeline/tools/yf SNDK news` 於執行時回傳 CONNECT tunnel 403 (proxy), 無法取得 yfinance 新聞清單, 公司新聞全部改由 WebSearch 補足, 來源多為二手媒體, 覆蓋深度不足。
- `pipeline/tools/yf SNDK info` 回傳為 cache (cached_at 2026-10-20T11:26 UTC), 其中價格欄位互相矛盾 (regularMarketChangePercent +5.53% 與 fulldayChangePercent -3.11% 並存), 本報告僅引用其估值、分析師與 52 週區間等非即時欄位。
- 一則 Oct 13 WSJ 報導 (據 INDmoney 轉述) 將 10 月中旬下跌歸因於 CXMT, 本次搜尋無法找到該 WSJ 原文, 也找不到 10 月的 CXMT 相關拋售報導。CXMT 拋售的可查證事件是 2026-07-27 (見下方), 故 10 月的歸因標為 DATA_UNAVAILABLE。

## Top company-specific headlines (last 14d)

本段優先列出近 14 天 (2026-10-07 起) 的公司層級事件。近 14 天內未找到 SanDisk 官方新聞稿, 唯一官方公告為 9/29 的財報日期通知。

- 2026-10-08 ~ 2026-10-15 — SNDK 連續六個交易日收跌, 10/15 收 $1,394.83, 較 10/1 收盤下跌約 22% (INDmoney 二手報導, 未見交易所或公司原始資料)。Impact: bearish (股價). 1-line why: 高估值、高 beta 的記憶體標的在 NAND 景氣仍強的情況下出現大幅修正, 市場焦點轉向競爭與週期風險。下跌原因 DATA_UNAVAILABLE (INDmoney 歸因於 WSJ 10/13 CXMT 報導, 無法驗證)。
- 2026-10-07 — Trefis 報導 SNDK 收 $1,692.42, 較 9/22 一個月收盤高點 $1,887.04 回落約 10% (Trefis, 股價紀錄, 歸為 context 而非獨立事件)。Impact: bearish (股價). 1-line why: 同上, 是 10 月下跌的起點。
- 2026-10-06 (資料時點) — 選擇權隱含 4 週財報波動約 ±10.99% (約 $182.40) (WebSearch 摘要, 日期為 10/6 快照)。Impact: neutral. 1-line why: 市場已預期 10/29 財報有大幅波動, 方向未定。
- 2026-10-01 — Citi 維持 Buy, 目標價 $2,100 (Investing.com 摘要, 二手)。Impact: bullish. 1-line why: 目標價仍高於現價約 53%, 分析師端維持正面。
- 2026-09-29 — 公司官方新聞稿: 確認 FQ1 FY2027 財報於 2026-10-29 公布, 美股收盤後, 電話會議太平洋時間 13:30 (SanDisk IR, 官方一手). Impact: neutral. 1-line why: 排程公告, 本身不含業績資訊, 但確立關鍵事件日。
- 2026-09-22 — Rosenblatt 維持 Buy, 目標價 $2,400 (Barchart/Investing.com 摘要, 二手)。Impact: bullish. 1-line why: 分析師目標價區間仍在 $1,000–$3,600 之間, 共識偏多。

近 30 天公司層級但非近 14 天之事件 (僅列作背景):
- 2026-08-05 — FQ4 FY2026 財報: 營收 $8.97B (超標 6.5%), non-GAAP EPS $39.25 (超標 13.5%), 下季指引營收 $10.3–10.8B、EPS $44–46, 盤後股價下跌 12.1% (WebSearch 摘要, 二手, 日期於多來源一致)。Impact: 業績偏多, 股價反應偏空 (市場對指引與估值的反應). 1-line why: 基本面超標但股價仍因預期過高而回落。

## Sector macro

- 2026-10-08 — Samsung 初步公布 2026 Q3 營業利益約 KRW 107.4 兆 (年增約 783%), 由 HBM、DRAM、NAND 需求帶動; 完整報告 10/29 (來源為 KuCoin 部落格, 屬較弱來源, 數字需再驗證). Impact on 記憶體/NAND: bullish (景氣與供應端定價力). 但公告後 Samsung 股價下跌, 市場對高基期與 "peak" 的擔憂仍在。
- 日期 DATA_UNAVAILABLE — TrendForce 預估 2026 Q4 NAND contract 價格上漲 15–20% QoQ, DRAM 上漲 10–15% (WebSearch 摘要, 發布日期無法確認)。Impact on NAND: bullish (定價 2nd derivative 仍正). 注意: 這是預估值, 非實際合約價。
- 2026-07-31 — Kioxia FQ1 報告: 毛利率 80% (不含 JV 項目為 82%), 但淨利低於市場一致預期 (JPY 842.1B vs 968.7B), Morningstar 指出品牌客戶 (如 Apple、Samsung) 毛利壓縮, 預期未來 NAND 漲價幅度將收斂 (Morningstar, 日期為 7 月底, 在 30 天窗口外)。Impact on NAND: bearish (定價斜率放緩的風險). 1-line why: 價格漲幅已被市場消化, 下一階段議價會更困難。
- 2026-07-27 — CXMT 於上海 STAR 市場掛牌, 首日股價大漲約 466%, 當日 SNDK 收跌超過 11%, Micron、WDC、STX 亦同步下跌 (WebSearch 摘要, 多來源一致)。Impact on NAND: bearish (競爭敘事, 市場擔心中國 DRAM 定價低 5–10%)。注意: 此為 30 天窗口外事件, 但為 10 月下跌的最後一個可查證的 CXMT 相關拋售, 須與 10 月歸因區分。
- 2026 年 (日期 DATA_UNAVAILABLE) — 長約與預付款模式: SanDisk 公司層級披露已簽署 5 份長約、覆蓋 FY2027 bit 量超過 1/3, 並可能超過 50%, 三份 FQ3 合約隱含最低合約營收約 $42B; 預付款在 FQ3 資產負債表約 $0.4B (Benzinga/CFO 於 5 月法說會, 窗口外)。Digitimes 1 月報導 "100% prepayment" 為單一付費來源, 無法驗證, 不採用。Impact: bullish (收入能見度與議價力). 1-line why: 把週期性定價轉為合約化, 降低景氣下行的波動。
- 日期 DATA_UNAVAILABLE — 美國半導體 Section 232 關稅與 H200 等晶片對中國出口許可規則 (25% 進口關稅 + 個案許可 / 美國本地測試): 來源多為 2026 年上半年, 10 月狀態未確認 (WebSearch 摘要)。Impact: neutral to bearish (中國市場與進出口成本), 影響程度 DATA_UNAVAILABLE。
- 2026-02 (SCOTUS, 日期確定) — Learning Resources v. Trump 判決 IEEPA 不授權關稅, 但 Section 232 關稅仍有效 (CRS 摘要)。Impact: neutral (為 232 路徑保留, 間接影響晶片關稅框架)。
- 2026-10-28 (預定) — FOMC 決議, 見 Forward calendar。現行聯邦基金利率區間來源互相矛盾 (3.50–3.75% 與 3.75–4.00%), DATA_UNAVAILABLE, 不列入判斷。

## Peer signals

- Samsung (005930.KS) — 2026 Q3 初步營業利益約 KRW 107.4 兆 (KuCoin 部落格, 需驗證), 10/8 公告後股價下跌; HBM 市占據報導已超過 30%, SK hynix 約 50% (WebSearch 摘要)。完整報告 2026-10-29。
- SK hynix — 2026 Q3 實際財報未找到 (DATA_UNAVAILABLE); 單一券商預估營業利益 70 兆韓元 (+16% QoQ), 低於市場一致預期, 歸因於匯率與 HBM 世代切換的出貨時點 (券商預估, 非財報)。
- Kioxia — FQ1 淨利低於預期, 宣布 3 比 1 股票分割 (10/1 生效) 與最多 ¥800B 買回, 2028 LTA 覆蓋率目標 50%。Kioxia 下次財報日期 DATA_UNAVAILABLE。
- Micron — 10 月公司層級資料 DATA_UNAVAILABLE; 7 月 Goldman 目標價 $2,000 (二手, 日期窗口外)。
- CXMT (非上市於美股之中國競爭者) — STAR 掛牌 (7/27) 後市場定價競爭風險; 10 月新動態 DATA_UNAVAILABLE。
- Western Digital / Seagate — 7/27 CXMT 拋售日下跌超過 4%; 10 月資料 DATA_UNAVAILABLE。

## Forward calendar (next 14d, 至 2026-11-04)

- 2026-10-27 至 10-28 — FOMC 會議; 決議於 10/28 美東 14:00 公布, 記者會 14:30 (Fed 官方頁面為 10/27–28, 時間來自第三方排程)。Expected impact: 高本益比與高 beta 股票對利率敏感, 波動放大。
- 2026-10-29 (盤後) — SanDisk FQ1 FY2027 財報與電話會議 (13:30 PT, 官方新聞稿確認)。Expected impact: 最大單一事件。需看 FQ1 營收與毛利、下季指引 (市場 FQ2 前瞻: 營收 $10.3–10.8B、EPS $44–46 為 FQ4 所給的指引, 須以 FQ1 報告為準), 以及長約覆蓋率與預付款更新。隱含波動 ±10.99%。
- 2026-10-29 — Samsung Q3 完整報告 (KuCoin 來源, 需與 Samsung IR 再確認)。Expected impact: NAND/HBM 景氣與定價指引的同業訊號。
- 日期 DATA_UNAVAILABLE — SK hynix Q3 2026 財報 (預期 10 月下旬, 未確認)。Expected impact: HBM 與 NAND 定價同業訊號。
- 日期 DATA_UNAVAILABLE — Kioxia 下次財報 (未確認)。Expected impact: NAND 定價與 LTA 進展。
- 日期 DATA_UNAVAILABLE — TrendForce / DRAMeXchange 10 月或 11 月合約價格公布 (未確認)。Expected impact: Q4 NAND 漲幅驗證。
- 窗口外: 2026-11-18 FOMC 紀錄 (Fed 官方頁面), 不列入本窗口。

## Net read

近 30 天的公司層級新聞以股價反應為主, 且多數為二手來源。基本面面向仍偏正面: Samsung 初步財報顯示記憶體景氣強勁, TrendForce 預估 Q4 NAND 合約價續漲 15–20%, SanDisk 的長約與預付款模式提高收入能見度, 分析師目標價區間仍在現價之上 (Citi 2,100、Rosenblatt 2,400、共識約 2,173, 24 位分析師, 推薦均值 1.52)。負面面向來自兩方: 一是 10 月股價由 9/22 高點約 $1,887 回落至 10/15 收盤 $1,394.83 (約 -26%), 且 Yahoo cache 之現價 $1,371.12 距 52 週高點 $2,354.39 仍有約 42% 的距離, 但 10 月下跌的觸發原因未能驗證 (INDmoney 之 CXMT/WSJ 歸因無法確認); 二是 Kioxia FQ1 淨利低於預期、Morningstar 預期 NAND 漲價收斂, 市場對定價斜率的擔憂可能是估值壓縮的主因。綜合判斷: 淨新聞傾向為中性偏正面, 情緒面受 10 月修正拖累, 而基本面與同業定價訊號仍偏多。淨新聞傾向: NEUTRAL, 強度中等 (信心中等, 因多數關鍵事實來自二手來源, 且 10 月拋售原因無法驗證)。下一個決定性事件為 2026-10-29 財報。

## Catalyst summary

| 日期 | 事件 | 類型 | 預期影響 | 來源可信度 |
|---|---|---|---|---|
| 2026-09-29 | SanDisk 公告 FQ1 FY27 財報日 | 公司 | 中性 (日程) | 官方一手 |
| 2026-10-01 | Citi 維持 Buy, PT $2,100 | 公司 | 偏多 | 二手 |
| 2026-10-06 | 選擇權隱含財報波動 ±10.99% | 公司/市場 | 中性 | 二手 |
| 2026-10-08 | Samsung 初步 Q3 OP ~KRW 107.4 兆 | 同業/產業 | 偏多 (景氣), 股價反應偏空 | 較弱 (部落格) |
| 2026-10-08 ~ 10-15 | SNDK 連續下跌, 10/15 收 $1,394.83 (-22% vs 10/1) | 公司股價 | 偏空 | 二手 (INDmoney) |
| 2026-10-13 | WSJ 報導 CXMT 相關拋售 (據 INDmoney 轉述) | 產業 | DATA_UNAVAILABLE | 無法驗證 |
| 2026-10-27 ~ 10-28 | FOMC, 10/28 14:00 ET 決議 | 總經 | 利率敏感股波動 | Fed 官方 (日期); 利率水準矛盾 |
| 2026-10-29 盤後 | SanDisk FQ1 FY27 財報 | 公司 | 最大事件, 隱含 ±10.99% | 官方一手 |
| 2026-10-29 | Samsung Q3 完整報告 | 同業 | 偏多/中性 | 需再驗證 |
| DATA_UNAVAILABLE | SK hynix Q3 財報 | 同業 | DATA_UNAVAILABLE | 未找到 |
| DATA_UNAVAILABLE | Kioxia 下次財報 | 同業 | DATA_UNAVAILABLE | 未找到 |
| DATA_UNAVAILABLE | TrendForce / DRAMeXchange 合約價公布 | 產業 | 偏多 (預估 Q4 NAND +15–20%) | 日期未確認 |
| 2026-07-27 (窗口外) | CXMT STAR 掛牌, SNDK 當日 -11% | 產業 | 偏空 (競爭) | 多來源一致 |
| 2026-07-31 (窗口外) | Kioxia FQ1 淨利未達預期, 漲價收斂疑慮 | 同業 | 偏空 (定價斜率) | 二手 |
| 2026-08-05 (窗口外) | SanDisk FQ4 FY26 財報超標, 盤後 -12% | 公司 | 業績偏多, 股價偏空 | 二手 |

## Net sentiment

NEUTRAL

Sources:
- [Sandisk to Report First Quarter Fiscal Year 2027 Results on October 29, 2026 (SanDisk 官方新聞稿, 2026-09-29)](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-09-29-sandisk-to-report-first-quarter-fiscal-year-2027-results-on-october-29-2026)
- [Sandisk Q1 FY27 earnings release details (IR)](https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29)
- [Trefis: Is SanDisk Stock's Fall A Bargain Or A Warning? (2026-10-08)](https://www.trefis.com/stock/sndk/articles/617813/is-sandisk-stocks-fall-a-bargain-or-a-warning/2026-10-08)
- [INDmoney: SanDisk Stock Slides for Six Sessions](https://www.indmoney.com/blog/us-stocks/sandisk-stock-fall-and-recovery)
- [Barchart: SanDisk eyes doubling memory prices](https://www.barchart.com/story/news/37005071/as-sandisk-eyes-doubling-memory-prices-should-you-buy-red-hot-sndk-stock)
- [Investing.com SanDisk Corp (SNDK) analyst consensus](https://www.investing.com/equities/sandisk-corp)
- [Samsung Q3 2026 preliminary (KuCoin, weak source)](https://www.kucoin.com/blog/ae-samsung-q3-2026-earnings-operating-profit-surges-783-as-ai-chip-demand-fuels-memory-boom)
- [Korea Herald / Sammyfans Q3 2026 estimates](https://www.sammyfans.com/2026/09/24/samsung-and-sk-hynix-eye-190-trillion-won-profit-in-q3-2026/amp/)
- [TrendForce / Kioxia FQ1 2026 coverage (2026-07-31)](https://www.trendforce.com/news/2026/07/31/news-kioxia-1qfy26-gross-margin-hits-80-reaffirms-50-lta-target-for-2028/)
- [Morningstar: Kioxia Earnings, Softer NAND Price Hikes Expected](https://www.morningstar.com/stocks/kioxia-earnings-softer-nand-price-hikes-expected-investment-discipline-keeps-us-positive)
- [247wallst: SanDisk Sinks 12%... as China's CXMT IPO Rattles Memory Stocks (2026-07-27)](https://247wallst.com/investing/2026/07/27/sandisk-sinks-12-micron-drops-5-sk-hynix-falls-8-as-chinas-cxmt-ipo-rattles-memory-stocks/)
- [Benzinga: SanDisk bets big on multi-year contracts](https://cdn1.benzinga.com/markets/equities/26/05/52205851/sandisk-bets-big-on-multi-year-contracts-as-ai-chip-demand-booms)
- [Federal Reserve: October 2026 meeting calendar](https://www.federalreserve.gov/newsevents/2026-october.htm)
- [Section 232 / export control overview (CRS, 2026-03-23)](https://www.everycrsreport.com/files/2026-03-23_LSB11409_8bef47ae63160e57718d8bc6bd0b5f41b7c32738.html)

NEWS REPORT COMPLETE
