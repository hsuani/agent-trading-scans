# News — INTC as of 2026-11-01

資料時效說明: 執行當下日期為 2026-10-31，新聞最新可取得的事件為 2026-10-30 (Q3 財報後的股價反應)。2026-11-01 當日的新聞無法取得，本報告不含該日內容。

資料來源狀態:
- `pipeline/tools/yf INTC news` 失敗: proxy 拒絕 query2.finance.yahoo.com / guce.yahoo.com 的 CONNECT (403)，無法取得 yfinance 新聞清單。
- `pipeline/tools/yf INTC info` 可用 (cache 2026-10-31 12:10 UTC)，作為價格與估值參考。
- WebSearch 作為主要新聞來源；SEC 8-K (sec.gov) DNS 無法解析，無法直接核對 Q3 財報原文。
- 多數新聞來源為二手聚合站，數字有互相矛盾處，已於各條標註。

## Top company-specific headlines (last 14d)

- 2026-10-29 (盤後) — Intel 公布 2026 Q3 財報: non-GAAP EPS $0.52，高於分析師約 $0.40 的預期。DCAI (資料中心與 AI) 營收年增 78% 至 $7.3B (24/7 Wall St / Morningstar 引述)。Impact: neutral (獲利面 beat，但被指引抵銷)。1 行原因: 獲利與 AI 資料中心需求強勁，但 beat 被 Q4 指引完全蓋過。
- 2026-10-29 (盤後) — Q4 指引 revenue $15B–$16B，低於分析師約 $17.08B 的共識；Q4 non-GAAP EPS 指引 $0.25，低於約 $0.44 共識 (Investing / Morningstar 引述)。Impact: bearish。1 行原因: 營收指引約低於共識 $1B 以上，為本次股價重挫主因。注意: 另一來源 (Q4 non-GAAP EPS $0.08，GAAP $(0.14)) 數字不同，本報告未能以原始 8-K 核對，以 $0.25 版本為主，僅供參考。
- 2026-10-30 — 股價重挫。前收 $92.07；盤後曾跌約 23% 至 $70.87 (Fool / Yahoo 引述)。yfinance cache 顯示當日 open $68.35、low $63.20、high $68.77、收盤 $65.76，較前收 -28.6%；Morningstar 稱收盤跌約 31%。Impact: bearish。1 行原因: 單日跌幅大，52 週高點 $142.35 已回落約 54%；精確收盤價來源分歧，以 cache 為準但未能獨立核對。
- 2026-10-30 — 管理層歸因: 記憶體 (DRAM / NAND) 價格飆升擠壓企業 IT 預算，抑制 PC 處理器需求 (Fool / Morningstar 引述 CEO Lip-Bu Tan 說法)。Impact: bearish (CCG 客戶端面)。1 行原因: 這是 PC 端需求的結構性壓力，非單季雜訊。
- 2026-10-30 — Morningstar 分析師 Brian Colello 將 INTC 公允價值由 $105 下調至 $85 (Morningstar 引述)。Impact: bearish。1 行原因: 具權威性的賣方研究下修，但仍在現價之上。
- 2026-10-22 — 芯片股大幅回檔期間 INTC 單日約跌 8% 至 $85.49，公司未改變展望 (單一來源，tradingkey 引述)。Impact: bearish (sector beta)。1 行原因: 反映 sector 拋售而非公司特定事件，數據僅單一來源。
- 2026-10-14 — 以色列 Kiryat Gat 晶圓廠爆炸，2 名員工死亡、1 名重傷 (Times of Israel / Israel Hayom 引述)。Impact: neutral-to-bearish (營運風險)。1 行原因: 疑似氣瓶爆炸，曾有 NF3 外洩疑慮；產能影響未獲證實。此事件已超出 14 天窗口 (10-18 起算)，列於此作為持續性營運風險參考。
- 2026-06 (背景，超出 14d) — Q2 財報超預期，股價大漲；CEO Lip-Bu Tan 自購 $10M 股票 (undated 聚合站資料，僅作背景)。

## Sector macro

- 2026-10 (持續) — 記憶體價格大幅上漲。Micron 9M FY26 DRAM 銷量年增 211%，平均售價約上漲 140% (Micron 申報資料經 WebSearch 引述)。Impact on 半導體 / 客戶端 CPU: 對 PC 出貨與 BOM 成本構成壓力，為 INTC CCG 業務主要逆風；對記憶體供應商為順風。
- 2026-10-15 前後 — 通膨數據偏熱，科技與芯片股被拋售；另有殖利率與油價上行的壓力 (WebSearch 聚合資料，日期不完全明確)。Impact on 半導體: 高估值成長股對利率敏感，短期估值承壓。
- 2026-10 (背景) — 伺服器 CPU 供給偏緊；分析師 (KeyBanc) 稱 INTC 2026 年伺服器 CPU 大致售罄 (undated，引述先前報導)。Impact on INTC DCAI: 正面，支撐 DCAI 成長；但 Q4 指引偏弱顯示供給或產品組合仍是限制因素 (推論)。
- 2026-10-14 — Kiryat Gat 事件所在的以色列廠區，為 Intel Foundry / 製造版圖的一部分 (公司概況)。Impact: 若產能受影響，將影響 Foundry 與 supply 節奏；目前未有產能影響公告。
- 未查證: 關稅、出口管制、地緣政治 (美伊停火等) 在 14 天內的具體新聞，本次 WebSearch 未獲得可靠的 10 月日期結果，未納入。

## Peer signals

- MU (Micron) — 記憶體價格強勁，2026-10-15 收 $931.24 (+1.9%) (WebSearch 引述)。Note: 記憶體漲價是 INTC PC 需求的成本逆風，對 MU 為順風，屬於同一題材的對向訊號 (推論)。10-30 當日 MU 表現未能查證。
- AMD — 10-30 當日股價與 PC / 資料中心指引反應未能查證。AMD 同屬 x86 CPU 與 PC 客戶端曝險，INTC 的 CCG 逆風若為產業性，AMD 應有類似的 PC 需求 read-through (推論，待確認)。
- NVDA / AVGO / TSM / SK hynix / Samsung — 本次未能取得 10-30 當日可靠新聞，無法列出具體訊號。
- 芯片股整體 — 10 月中旬 (AI 芯片約 8 日內 $2T 市值蒸發後反彈，聚合站來源，日期模糊) 顯示板塊波動大。

## Forward calendar (next 14d)

- 2026-11-01 ~ 11-03 — INTC 10-Q / 財報後續文件與分析師調整目標價 (預期) — 可能出現大量 PT 下調，影響情緒。
- 2026-11-06 (週五，依慣例推算，未核實) — 美國非農就業報告 (NFP)。對高 beta 科技股 (INTC beta 2.23) 有明顯波動性。
- 2026-11 上旬 (日期未核實) — AMD 財報，可作為 PC / 資料中心需求的同業 read-through。
- 2026-11-12 ~ 11-13 (依慣例推算，未核實) — 美國 10 月 CPI。10 月通膨數據熱度曾引發芯片拋售，本次數據為風險事件。
- 不在窗口內的已知事件: FOMC 10/27–28 已結束；下次 FOMC 約 12/8–9；INTC 下一季財報依 yfinance cache 預估約 2027-01 下旬。

## Net read

整體新聞傾斜為 **偏空 (bearish)，幅度大**。Q3 財報本身 non-GAAP EPS 優於預期 (DCAI 年增 78% 為強勁成長)，但 Q4 營收與獲利指引大幅低於共識，且管理層點名記憶體漲價壓縮 PC 需求，這兩點構成的負面敘事直接驅動 10-30 單日約 23%–31% 的重挫。Morningstar 同日下修公允價值，賣方情緒轉弱。板塊面，記憶體成本上漲與通膨熱度共同形成估值壓力，而 Kiryat Gat 事故是一項尚未量化的營運風險。正面因素主要來自 DCAI 與伺服器 CPU 供給緊俏，但目前不足以抵銷指引衝擊。資料缺口方面，yfinance 新聞清單無法取得、SEC 原文無法核對，且 Q4 EPS 指引在不同來源間有分歧，因此本段結論的幅度判斷應以財報與股價反應的一致性為主，細節數字需待原始 8-K 核實後再定案。

## Sources

- [Intel Q3 earnings beat / guidance miss, Fool 2026-10-30](https://www.fool.com/investing/2026/10/30/why-intel-stock-crashed-on-friday/)
- [Is Intel Stock a Buy After Its Post-Earnings Plunge? Fool 2026-10-30](https://www.fool.com/investing/2026/10/30/is-intel-stock-a-buy-after-its-post-earnings-plunge/)
- [Intel plummets over 28% as weak forecast overshadows earnings beat, Investing.com](https://www.investing.com/news/stock-market-news/intel-plunges-20-as-weak-q4-forecast-overshadows-earnings-beat-4984988)
- [Tech Stocks Sell Off as Intel, Amazon Earnings Spook Investors, Morningstar](https://www.morningstar.com/markets/tech-stocks-sell-off-amazon-intel-earnings-spook-investors)
- [Intel Stock Crashes 23% Overnight, Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/intel-stock-crashes-23-overnight-032819790.html)
- [Live: Will Intel's Q3 Earnings Tonight Spark a Recovery, 24/7 Wall St](https://247wallst.com/investing/2026/10/29/live-will-intels-q3-earnings-tonight-spark-a-recovery-after-20-selloff/)
- [Intel's Make-or-Break Margin Test Is Arriving on Oct. 29, 24/7 Wall St](https://247wallst.com/investing/2026/10/25/intels-make-or-break-margin-test-is-arriving-on-oct-29/)
- [Intel Stock News (Oct 21, 2026), HeyGoTrade](https://www.heygotrade.com/en/news/intel-intc-stock-news-october-21-2026/)
- [Intel Stock Fell 5% in a Day as Chip Stocks Sold Off Ahead of Its October 29 Report, TIKR](https://www.tikr.com/blog/intel-stock-fell-5-in-a-day-as-chip-stocks-sold-off-ahead-of-its-october-29-report-heres-where-the-stock-could-go)
- [Intel Stock Fell 8.04% Oct 22 (tradingkey), TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/262235573-intel-stock-forecast-q3-earnings-preview-margin-foundry-81-support-october-25-2026-tradingkey)
- [Second worker dies of wounds sustained in Intel plant blast, Times of Israel](https://www.timesofisrael.com/second-worker-dies-of-wounds-sustained-in-intel-plant-blast-in-southern-israel/)
- [Wednesday Oct 14, 2026, Israel Hayom](https://www.israelhayom.com/2026/10/14/intel-plant-explosion-kiryat-gat-3-injured/)
- [Micron Stock News (Oct 16, 2026), HeyGoTrade](https://www.heygotrade.com/en/news/micron-mu-stock-news-october-16-2026/)
- [Intel Q3 2026 8-K (sec.gov) — 未能抓取，僅於搜尋摘要中見到](https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000188/q326earningsrelease.htm)

NEWS REPORT COMPLETE
