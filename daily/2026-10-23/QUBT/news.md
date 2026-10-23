# News — QUBT as of 2026-10-23

資料品質說明:
- `pipeline/tools/yf QUBT news` 回傳 DATA_UNAVAILABLE。原因是 proxy 對 fc.yahoo.com 的 CONNECT 回 403（政策阻擋），未嘗試繞過。
- 近 14 日新聞以 WebSearch 補足。多數來源為聚合站與 AI 摘要，未逐一對照一手新聞稿、8-K 或 SEC Form 4。下列標示「未核實」者僅供參考。
- 未引用 2026-10-23 之後的資訊。過往 daily/ 報告未作回填。

## Top company-specific headlines (last 14d: 2026-10-09 ~ 10-23)
- 2026-10-14 — QUBT 與 INmune Bio 宣布合作，以量子優化與 AI 協助阿茲海默症藥物研發（WebSearch 聚合報導，未見一手新聞稿）。Impact: neutral。合作財務條款未揭露，對營收影響難以評估，屬應用場景延伸。
- 2026-10-17 — Wall Street Zen 將 QUBT 評等下調至 "Strong Sell"（聚合站，未核實）。Impact: bearish（情緒面）。量化評等權重低。
- 2026-10-19 — Rosenblatt 重申 "Buy" 評等（聚合站，未核實）。Impact: bullish（情緒面）。與 Wall Street Zen 評等分歧。
- 2026-10-22 — 報導指五年內量子股（IONQ、RGTI、QUBT）內部人合計出售逾 10 億 USD 股票，並質疑估值（foreignpolicyjournal.com）。Impact: bearish（情緒面）。來源可信度低，數字未經 Form 4 核對，不作為主要依據。
- 價格脈絡（非獨立事件）: 2026-10-15 盤中觸及 52 週低 6.08 USD（Investing.com）。部分來源報導 10-19 單日跌約 7.09%，但價格與 yf info 不一致，以 yf info 現價 6.59 USD 為準（來源未同步）。

窗口外背景（14d 前，供脈絡參考）:
- 2026-10-02 — 8-K 揭露三項 2026 年收購案（聚合站，未核實）。Impact: neutral，併購細節待查。
- 2026-10-01 — Dirac-3S optimization machine 推出（聚合站）。Impact: 中性偏多，產品進展。
- 2026-08-10 — Q2 2026 財報（WebSearch 聚合彙整）:
  - 營收約 5.6M USD（前一年同期 0.061M USD，Q1 3.7M USD）。
  - 淨損 11.8M USD，EPS -0.05（手算: 11.8M ÷ 約 226M 股 ≈ -0.052，與 EPS 吻合）。
  - 營運費用 21.8M USD，年增 114%，含收購相關費用約 7.3M USD。
  - 現金及投資約 1.3B USD（聚合站）。yf info totalCash 為 954M USD（0.95B USD），兩者不一致，未能核實。
  - Backlog 42.5M USD。完成 NHanced Semiconductors 收購，啟動 Fab 2，交付 Dirac-3 系統。
  - Impact: 中性偏空。營收成長主要來自併購，有機成長與虧損擴大並存。股價當日約跌 2.5%。

## Sector macro
- 2026-10-28 — FOMC 利率決議（14:00 ET，無 SEP）。Impact on 量子運算（高 beta、尚未獲利）: 資金成本與利率預期直接影響估值。各來源對 9 月決議與目前target range 說法不一（一說 9/16 升息 25bp 至 3.75–4.00%，一說維持 3.50–3.75%）。目前利率為 DATA_UNAVAILABLE（未能取得一致來源）。10 月是否調整之市場定價亦分歧（約 20% 加息機率 vs 約 80% 維持）。
- 2026-06-22 — 行政命令 EO 14411，設定維持量子科技戰略領先之國家目標，要求多機構與盟國對齊管制（Jenner & Block 分析，WebSearch）。Impact on 量子運算: 中性偏空。出口管制可能收緊，零組件供應鏈承壓；但政府支持與採購為正面訊號。
- 2026-05-21 — 美國商務部就 Diraq 簽署最多 3,800 萬 USD（38M USD）之意向書，並取得少數股權（WebSearch）。Impact on 量子運算: 間接正面，顯示政府以股權形式參與產業。
- FY2026 聯邦量子研發經費 — 大致持平（產業展望，無明確日期）。Impact: neutral。
- 關稅 — 未找到針對量子硬體之新關稅行動。DATA_UNAVAILABLE。

## Peer signals
- IONQ — 2026 Q2 營收約 80.1M USD（年增 287%），RPO 約 485M USD（聚合站，未核實）。另有報導稱 IonQ 一項 1.3B USD 交易後，量子股整體下跌（日期未明，未核實）。2026 年 1 月宣布以 1.8B USD 收購 SkyWater Technology（先前報導）。
- QBTS (D-Wave) — Q2 營收持平；商務部意向書最多 1 億 USD 潛在資金（日期未明，聚合站）。
- RGTI (Rigetti) — C-DAC（印度）訂購 108 qubit 系統（日期不明確）。路線圖目標 2026 年底 150+ qubits（聚合站）。
- 同業整體 — 報導指四家量子股（QUBT、IONQ、RGTI、QBTS）2026 年跌幅部分回復（Fast Company，日期不明）。同業未見 2026-10-09 ~ 10-23 期間之重大公告（WebSearch 未找到）。

## Forward calendar (next 14d: 2026-10-23 ~ 11-06)
- 2026-10-27 ~ 10-28 — FOMC 會議，10-28 14:00 ET 公布利率決議。Expected impact: 高 beta 量子股對利率意外敏感，決議前後波動放大。
- 窗口外參考: QUBT Q3 2026 財報估計於 11/10（yf info，isEarningsDateEstimate=true）或 11/13（WebSearch 聚合站）。未經公司確認，且超出 14 日窗口。
- 窗口外參考: 2026-11-18 FOMC 會議紀錄公布。
- 同業財報日與 QUBT 重大產品或政策時程 — DATA_UNAVAILABLE。

## 市場快照（yf info，USD，2026-10-23 盤前快取）
- 現價 6.59 USD（前收 6.82，當日 -3.37%）。52 週區間 6.08–17.35 USD。50 日均 8.02 USD，200 日均 8.90 USD。
- 市值約 1.49B USD（6.59 × 約 226M 股，手算吻合）。Enterprise value 約 0.56B USD。
- 現金 totalCash 約 0.95B USD（與財報摘要 1.3B USD 不一致）。TTM 營收約 9.8M USD。
- Short % of float 約 33.6%，short ratio 9.86 日。Beta 3.75。
- 分析師 6 位，平均目標價 18.67 USD（區間 10–32 USD），recommendationKey = buy。

## Net read
14 日內可核實之公司重大事件偏少，多為聚合站資訊，可信度有限。整體新聞面為 mixed 偏空，幅度中等。偏空面包括: 股價逼近 52 週低並低於 50 日與 200 日均線；Strong Sell 量化評等；內部人出售之負面報導；Q2 虧損與營運費用擴大；空單占流通股比例高。偏多面包括: Buy 評等（Rosenblatt）、INmune Bio 合作、商務部與政府股權參與之產業訊號，以及約 0.95–1.3B USD 現金部位。宏觀上，10-28 FOMC 為窗口內最重要催化劑，對高 beta 量子股影響大。本報告僅彙整新聞，不構成交易建議。

NEWS REPORT COMPLETE
