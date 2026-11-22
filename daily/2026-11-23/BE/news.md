# News — BE as of 2026-11-23

資料取得說明: `pipeline/tools/yf BE news` 回傳 403（CONNECT tunnel failed），本次新聞全部來自 WebSearch。`yf BE info` 可用，僅用於價格與估值快照。搜尋結果多數為無日期或日期不精確的轉載文章，條目中已標註。未引用任何 `daily/` 舊報告的數字。

金額單位: BE 為 USD，市值與營收以 B/M 標示。

## Top company-specific headlines (last 14d)
- 2026-11-20（週五，yf 最近一個收盤，時間戳記有時區偏差）— 股價單日 -15.3%，收 142.39（前收 168.11），盤中區間 140.69–163.38，成交量 28.5M，約為 10 日均量 16.4M 的 1.7 倍（yf）。Impact: bearish. 跌幅大且量能放大，但**未找到當日公司特定新聞**，DATA_UNAVAILABLE 於原因確認；無日期文章僅提及 AI 基建與資金面疑慮。
- 2026-11-19 — Tradingpedia 報導 BE 快速擴張 AI 電力業務與現金流之間的矛盾，指 Q3 自由現金流為 -181M USD。Impact: bearish. 現金流轉負是估值支撐的主要質疑點。注意 yf TTM FCF 顯示約 -1.7M USD，與此來源不一致，需以 10-Q 核對。
- 2026-11-12 — NVIDIA 股價走弱，拖累 AI 基建與電力族群，BE 隨族群回落（24/7 Wall St）。Impact: bearish（板塊 beta 效應，非公司新聞）。
- 2026-11-11 — 股價 +13.0%，市場歸因 CoreWeave 財報緩解「AI 獲利何時能覆蓋基建債務」的疑慮（Trefis、Motley Fool 11/11）。Impact: bullish，但反彈未能延續。收盤價來源不一：Trefis 寫 209.47，Benzinga 另列 11/4 為 200.51。
- 2026-11-05（Trefis 11/6 另有文章寫 11/6，日期有出入；窗口外，作為背景）— 股價 -16.4%，同日 S&P 500 -4.4%，市場擔心美國期中選舉後數據中心建設放緩（Trefis、AI 電力股相關報導）。Impact: bearish。同日公告 NTT DATA 900 MW 協議，但未能抵銷跌勢。
- 2026-11-05（窗口外，背景）— NTT DATA 同意部署 900 MW Bloom 燃料電池，為 Bloom 迄今最大國際專案，2027 年起首批出貨（NTT DATA 新聞稿、Bloom 新聞頁）。Impact: bullish（基本面），對股價無即時正面效果。
- 日期未確認（2026-11 內，多為轉載）— Google 與 AEP 於懷俄明州 Cheyenne 的 702 MW 燃料電池專案，20 年 PPA，AEP 持股約 92%，總投資約 40 億 USD，含碳捕捉，2028 年底全面運轉。Bloom 依既有最高 1 GW 協議供貨（初始 100 MW + 900 MW 選擇權）（Data Center Dynamics、Data Center Frontier）。Impact: bullish（訂單可見度）。注意：只有一篇來源把 BE 單日 -16% 與此消息連結，時序無法確認，且天然氣燃料與碳捕捉部分有爭議。
- 日期未確認 — California Resources（CRC）非約束性 MOU，評估由 Bloom 提供至少 1 GW SOFC 發電並搭配 CCS。Impact: neutral to bullish。非約束性，不應計入已確定訂單。
- 日期未確認（Stocktwits/MarketBeat 類文章）— COO Satish Chitoori 與 CCO Aman Joshi 為支付 RSU 稅款合計賣出約 1.3M USD 股票。Impact: neutral，屬例行性交易。
- 2026-10-22（窗口外，背景）— Q3 財報創紀錄：營收 1.24B USD（+138% YoY），non-GAAP EPS 0.94；2026 全年營收指引上修至 4.4–4.6B USD（前值 3.9–4.2B），non-GAAP EPS 指引 3.10–3.40；同期納入 S&P 500（Bloom IR 新聞稿、SEC 8-K、Zacks、Benzinga）。Impact: bullish（基本面）。但 11/5 至 11/20 的跌幅發生在上修之後，顯示定價主導因素是情緒與總經，而非盈餘。
- 已排除（PR 雜訊）— 2026-11-13 路易斯安那州 Baton Rouge 兩個基金會各捐 10,000 USD；無 Impact。

## Sector macro
- 2026-11-03 至 11-05（期中選舉結果）— 民主黨在選舉中取得優勢（部分報導稱為橫掃），市場擔心政策轉向可能拖慢美國數據中心擴建，AI 電力股同步拋售（tikr、Trefis）。Impact on 電力/數據中心: bearish。BE 的主要成長來源是數據中心訂單，政策風險直接影響需求假設。
- 2026-11-19 — Fed 會議紀要（Fortune、24/7 Wall St）：目前維持利率，但多數委員把 AI 投資的持續性列為等待更多數據的理由；部分委員表示若通膨持續，12 月可能升息超過 25 bp。Impact on 電力/成長股: bearish。BE forward P/E 約 26.7、P/B 約 21.8（yf），對折現率高度敏感。
- 2026-11-19 — 地方政府限制：Fortune 引述有 44 個地區通過限制數據中心的措施（從俄亥俄到內華達）；Pew 調查 60% 美國成人對附近新建數據中心「不太舒服」或「完全不舒服」。Impact on 數據中心電力需求: bearish（中長期，許可與地方審查延遲風險）。
- 2026-11（Moody's 與 Citadel 評論）— 數據中心融資由建設貸款轉向長期債務；大量債券發行可能壓制資本市場吸收能力。Impact: neutral to bearish（融資成本上行風險，對資本密集的 AI 基建鏈條不利）。

## Peer signals
- FuelCell Energy（FCEL）— 11/5 同日跌約 15.3%，幅度接近 BE，屬燃料電池族群同步下跌。
- Plug Power（PLUG）— 燃料電池族群拋售加劇，單日跌約 4%（Webull，日期不精確）。
- CoreWeave — 11/11 財報帶動 AI 基建股反彈，BE 當日 +13%。Impact: 正向板塊情緒。
- NVIDIA — 11/12 股價下跌，AI 基建股跟跌；NVDA 下一次財報日期未於本次搜尋確認。
- GE Vernova、Vertiv — 一篇無日期 Motley Fool 文章指 BE 與兩者在一週內下跌 10–24%，屬 AI 電力族群共同拋售。
- Lumentum — 「AI 電力股在民主黨橫掃後回落」的報導中同列，單日跌約 11%（tikr，日期不精確）。
- Oklo、Vistra — DATA_UNAVAILABLE：本次搜尋無 2026-11 相關結果，無法評估其近期走勢。

## Forward calendar (next 14d)
- 2026-11-26（週四）— 美國感恩節休市（NYSE 規定）；11-27 通常為提前收盤，流動性偏薄。Expected impact: 低，但週末前後的消息面可能放大波動。
- 日期未確認（通常為 11 月下旬）— NVIDIA 財報。Expected impact: 高。BE 在 11/12 已因 NVDA 走弱而同步下跌，NVDA 指引是 AI 基建族群的主要情緒錨。
- 日期未確認（通常為 12 月中）— FOMC 12 月會議。Expected impact: 高。會議紀要已提示升息可能，若大於 25 bp 會直接壓抑高估值成長股。
- DATA_UNAVAILABLE — BE 下一次財報日期：yf 顯示的 earningsTimestamp 為 2026-10-22/23，已過；下一次財報通常在 2027 年 2 月，本次未確認。
- DATA_UNAVAILABLE — Google/AEP Cheyenne 專案建設啟動與 CRC MOU 進展：未找到明確時程。AEP 目標 2028 年底全面運轉，Black Hills 指 2027 年下半年開始供電（窗口外，僅作為背景）。

## Net read
過去兩週 BE 的新聞面可分為兩段。基本面消息仍偏多：Q3 營收大幅成長、全年指引連續上修、NTT DATA 900 MW 與 Google/AEP 702 MW 兩項大型訂單，以及 CRC 的非約束性 MOU，都顯示訂單能見度高。但股價在 11/5 至 11/20 間從約 209 USD（11/11）跌到 142.39 USD，較 11/11 收盤回落約 32%，較 52 週高點 351.28 USD 下跌約 59%（yf），且 11/20 單日 -15.3% 的主因未能確認。拖累股價的主要是情緒與總經：期中選舉後的政策不確定性、Fed 會議紀要所示的升息風險、地方數據中心限制，以及自由現金流轉負的質疑，再加上燃料電池與 AI 電力族群的同步拋售。淨新聞傾向為偏空，強度高；公司層面的正向消息無法抵銷板塊層面的負面敘事。分析師共識仍為 Buy（26 位，平均目標價約 282.69 USD，yf），但目標價與現價差距大，反映市場對 2027 年需求可見度的分歧。

## 來源與資料品質注意
- 主要來源: Trefis、Motley Fool（多為日期明確的 11 月文章）、24/7 Wall St、Webull、tikr、Tradingpedia、Fortune、Bloom IR 新聞稿、SEC 8-K、NTT DATA 新聞稿、Data Center Dynamics、Data Center Frontier、Zacks、Benzinga、yfinance（info 快照）。
- 已排除: Motley Fool 與 Nasdaq 的「November 17% 下跌」文章（2025 年舊文）、多篇 2025 年 12 月文章，以及無日期且無法對應 2026-11 的舊文。
- 矛盾點: (1) 11/5 與 11/6 的大跌日期來源不一；(2) 11/11 收盤 209.47 (Trefis) 與 200.51 (Benzinga, 11/4) 數字不一致；(3) TTM FCF 與 Q3 FCF 數字不一致；(4) 52 週高點 351.28（yf）與 345.85 收盤高（Benzinga）不一致。
- DATA_UNAVAILABLE 項目: 11/20 單日 -15.3% 的公司特定原因、Oklo 與 Vistra 2026-11 相關新聞、BE 下一次財報日期、NVDA 與 FOMC 12 月確切日期。

## 來源清單
- Trefis: https://www.trefis.com/stock/be/articles/623337/what-is-behind-thursdays-drop-in-bloom-energy-stock/2026-11-06
- Trefis（11/11 漲幅）: https://www.trefis.com/stock/be/articles2/624707/what-sent-bloom-energy-stock-higher-on-wednesday/2026-11-12
- Motley Fool 11/11: https://fool.com/investing/2026/11/11/here-s-why-bloom-energy-stock-popped-today
- 24/7 Wall St: https://247wallst.com/investing/2026/11/13/bloom-energy-is-down-27-in-a-month-what-will-it-take-to-get-be-stock-back-to-250/
- Tradingpedia: https://www.tradingpedia.com/2026/11/19/bloom-energys-rapid-ai-power-push-collides-with-cash-flow-concerns/
- NTT DATA: https://www.nttdata.com/en-us/news/2026/11/ntt-data-announces-agreement-with-bloom-energy
- Data Center Dynamics（Google/AEP）: https://datacenterdynamics.com/en/news/google-signs-20-year-ppa-with-aep-for-702mw-wyoming-fuel-cell-project
- Data Center Frontier（AEP/Google）: https://www.datacenterfrontier.com/energy/article/55413102/aep-google-advance-4-billion-fuel-cell-project-to-power-cheyenne-data-centers
- Bloom Q3 2026 新聞稿（SEC 8-K）: https://www.sec.gov/Archives/edgar/data/0001664703/000162828026066890/ex991_q326financialresults.htm
- Zacks Q3 摘要: https://www.zacks.com/stock/news/3017009/bloom-energy-q3-earnings-call-highlights-guidance-hike-&-capacity-plan
- Fortune（Fed 與數據中心限制, 11/19）: https://fortune.com/2026/11/19/fed-minutes-ai-inflation-data-centers-midterms-2027-rate-hike/
- Webull（燃料電池拋售）: https://www.webull.com/news/15940405349565440
- tikr（AI 電力股 vs 民主黨橫掃）: https://www.tikr.com/blog/bloom-energy-sinks-8-lumentum-down-11-as-ai-power-stocks-fade-after-democrat-sweep
- Motley Fool（Nov 3 漲 10%）: https://www.fool.com/investing/2026/11/03/why-did-bloom-energy-stock-jump-10-today/

NEWS REPORT COMPLETE
