# News — NVDA as of 2026-11-09

資料說明: `pipeline/tools/yf NVDA news` 回傳 proxy 403 失敗，本期新聞以 WebSearch 為主。多數搜尋結果為聚合站或二手來源，且含 2025 年舊聞，日期與數字需以原始來源核對。價格與估值取自 `yf info` 的 cache 資料（cached_at 2026-11-08）；其中單日漲幅欄位間有 2.8% 與 3.9% 差異，nameChangeDate / prevName 等欄位明顯異常，已忽略。

快照（USD）:

| 項目 | 數值 | 備註 |
|---|---|---|
| 最近收盤價 | 186.64 USD | cache，最近常規交易時段 |
| 市值 | 4,507B USD (4.51T) | 186.64 × 24.147B 股 ≈ 4,507B，一致 |
| TTM 營收 | 302.97B USD | yfinance |
| TTM 淨利 | 192.9B USD | 交叉驗證: TTM EPS 7.91 × 24.147B 股 ≈ 191.0B，差約 1%，合理 |
| Trailing P/E / Forward P/E | 23.6x / 11.7x | Forward EPS 15.91 |
| 52 週區間 | 164.27 – 243.37 USD | 現價距高點約 -23% |
| 50 日 / 200 日均線 | 219.8 / 204.7 USD | 現價位於兩線之下 |
| 分析師 | 58 家，平均建議 1.29（strong buy），平均目標 327.1 USD，中位數 315 USD，最低 180 USD | yfinance |

## Top company-specific headlines (last 14d)
- 2026-10-22 — NVDA 單日跌約 4.4%，盤中低點 211.26 USD，收於約 212.21 USD，前收 221.97 USD；同期報導提及 GTC Berlin 強調從 GPU 延伸至完整 AI factory 的佈局 (MarketBeat 即時快訊，二手)。Impact: 中性偏空。屬 14 天窗口邊緣的背景資料，反映 10 月下旬股價已從 230 USD 附近回落。
- 2026-10 (GTC Berlin，確切日期未確認) — Vera Rubin 宣布進入 full production，公司敘事轉向交付整套 AI factory；Google Cloud 表示 A5X（Vera Rubin NVL72）將於次月推出 (Phemex 二手報導)。Nvidia 官方 GTC Taipei 稿件之摘要稱量產出貨自今年秋季開始。Impact: 偏多。但 Vera Rubin 已於 CES 2026 與 GTC 2026 宣稱量產，「full production」可能是重複宣告，屬於既有敘事的延續，非全新里程碑。分析師提醒首波出貨可能集中於 2026 Q4，完整放量或要到 2027 年初。
- 2026-08-26 — 公司給出 FQ3（10 月季）營收指引 105.8–110.2B USD，高於市場共識 103.5B USD (MarketBeat，二手，超出 14 天窗口，列為最近一次正式指引)。Impact: 偏多。共識 EPS 約 2.47 USD（單一來源）。
- 其他: 本期未找到可靠的 NVDA 專屬 M&A、高管異動、產品新聞或訴訟報導（11/6–11/9 無可確認之公司級新聞）。

## Sector macro
- 2026-11-03 至 11-05 — 美國中期選舉後民主黨橫掃相關報導，市場擔心國會與地方政府對資料中心擴建加強限制。費城半導體指數 (SOX) 11/3 +2.63%（財報前反彈）、11/4 -3.13%，11/5 續跌。Chip 與記憶體類股自 10/6 起合計蒸發約 3.7T USD 市值（Yahoo Finance 經 WebSearch 轉引，截至 11/3）。Impact on 半導體 / AI 基礎建設: 偏空，屬政策與情緒折價，非基本面下修。各來源對 11/5 大盤跌幅與道瓊漲幅描述不一致，以個股與板塊數據為準。
- 2026-10-28 — FOMC 維持利率不變，10–2 投票（一來源為 3.75%–4.00%，另一來源為 3.50%–3.75%，區間待核對）。聲明稱通膨仍偏高、經濟「強勁擴張」，未明確釋出 12 月升息訊號。Impact on NVDA: 估值對利率敏感，偏中性偏空。下次會議為 12 月，本期無 11 月 FOMC。
- 2026-01-14 / 01-15 — 總統令對部分先進晶片進口課徵 25% Section 232 關稅；BIS 規則生效後，中國與澳門先進 AI 晶片出口許可改為 case-by-case 審查。H200 可出口中國（2025 年 12 月宣布），但 Blackwell 仍禁止。Impact: 中性。中國銷售有鬆動，但需承擔 25% 成本，且 Blackwell 缺席。
- 2026-06-01 — 美國商務部指引: AI 晶片出口許可規範適用於中國總部或中國母公司之企業，包括其海外子公司（Aljazeera 鏡像站，日期 2026/6/1）。Impact: 偏空，縮小中國企業海外採購管道。
- 2026-11-01 — 中國公布草案，擬新增 40 項受出口管制技術，其中 23 項屬 AI（含 LLM、AI agent、計算叢集），14 項禁出口、26 項限制（StockHub 二手，未核原文）。Impact: 中性偏空，影響取決於最終版本與中國本土 AI 供應鏈的取代程度。
- 超大型雲端 capex — 2026 年四大雲端 capex 規劃約 725B USD（Q1 後上修，Alphabet 185B、Meta 125–145B 等），年增約 77%。Evercore 與 BofA 估 2027 年合計超過 1T USD。Impact: 偏多，需求端仍具支撐。注意: 本期未找到 2026 年 10 月財報季的可靠更新，上述數字為 Q1 後與 7 月底前後之資料。
- 供應鏈 / 大宗商品: 本期未搜尋到具體的 HBM、CoWoS 或稀土事件。Gallium / germanium 出口暫停（期限 11/27）為二手來源，未確認。

## Peer signals
- AMD — 11/3 財報前反彈約 5%；11/5 盤中約 -15%，媒體歸因於資料中心政策擔憂。AMD 財報細節與股價高點（一度報 613.31 USD、市值破 1T USD）之日期未確認，不可直接引用。
- Intel — 11/5 約 -7%，同屬資料中心 / 晶片板塊的連動下跌。
- Micron、SanDisk — 11/4 明顯下跌（Motley Fool 11/4 報導），跌幅未確認。
- Seagate、Western Digital 等儲存股 — 同期重挫（StockStory），跌幅未確認。
- IREN、Applied Digital、Nebius（neocloud 客戶）— 11/5 跌逾 14%。neocloud 為 NVDA 主要下游客戶，其股價走弱反映融資與擴建風險。
- Broadcom — 未找到 2026 年 11 月的專屬新聞，僅有舊資料（Q1 FY26 AI 營收 8.4B USD，年增 106%），不納入判斷。
- 超大型雲端（MSFT、AMZN、META、GOOGL）— 本期無 10 月財報的可靠數據，7 月底資料已過時。

## Forward calendar (next 14d)
- 2026-11-17（週二）盤後 — NVDA FQ3 FY27 財報，電話會議 17:00 ET。依據: yfinance earningsTimestamp 換算為 16:00 ET，isEarningsDateEstimate 為 false；Earnings Whispers 亦列 11/17。其他日曆列 11/18，公司官方尚未於本期來源中確認，需以 NVIDIA IR 為準。Expected impact: 高。比較基準為指引 105.8–110.2B USD 與共識 103.5B USD；市場焦點包括下一季指引、Vera Rubin 出貨時程、毛利率與中國營收假設。
- 11 月中旬（日期未確認）— 10 月 CPI 發布，影響利率預期與高估值股評價。
- 本期窗口內無 FOMC 會議（下次為 12 月）。
- 持續追蹤（日期未定）— 國會與州層級資料中心監管提案；中國出口管制草案之最終公告與意見期；美國商務部對中國企業的 AI 晶片許可實務。

## Net read
本期新聞淨傾向為偏空，幅度中等。近期頭條主要由政策與情緒主導: 中期選舉後對資料中心擴建的監管疑慮，帶動 11/3–11/5 半導體與 AI 基礎建設股急跌，NVDA 股價 186.64 USD 已低於 50 日與 200 日均線，且距 52 週高點約 -23%。另一方面，基本面與產業敘事仍具支撐: GTC Berlin 的 Vera Rubin 量產與出貨說法、超大型雲端 2026 年約 725B USD 的 capex 規劃、2027 年估計超過 1T USD，以及 8/26 指引高於共識。中國面的出口管制仍在收緊（H200 需付 25% 關稅、Blackwell 持續禁止、中國草案新增 AI 管制項目），屬於利空的不確定性。公司層面 14 天內缺乏明確的獨家利多或利空，因此短期方向很大程度取決於 11/17 財報能否以指引與出貨時程化解資料中心政策的折價。分析師共識仍為 strong buy（平均 1.29、58 家），但最低目標價 180 USD 已接近現價，顯示部分研究員對短期風險保留。

資料缺口: yf news 工具失敗；多數搜尋結果為舊聞或未註明日期；NVDA 在 11/5 的個股跌幅未於來源中明確確認；財報日期與部分指引數字為單一或二手來源。

來源 (依 WebSearch 結果):
- MarketBeat NVDA 快訊（2026-10-08、2026-10-22）與 NVDA 新聞頁
- Phemex GTC Berlin 報導；NVIDIA Vera Rubin full production 新聞稿（nvidianews.nvidia.com）
- Motley Fool 2026-11-04 / 2026-11-05 AMD、Intel、Micron 個股報導
- devdiscourse、americanbazaaronline、stocktwits 關於 11/5 AI 資料中心股下跌之報導
- StockHub 2026-11-01 中國出口管制草案（二手）
- Morgan Lewis、Mayer Brown 關於 2026-01 BIS 規則與 25% 關稅之法律分析
- Aljazeera 2026-06-01 報導（鏡像站）
- Wealth Management / Barchart 關於 2026-10-28 FOMC 之報導
- 247wallst 2026-11-03 芯片股反彈報導
- Fool 2026-08-03 hyperscaler capex 整理

NEWS REPORT COMPLETE
