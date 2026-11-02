# News — IBM as of 2026-11-03

資料說明：`pipeline/tools/yf IBM news` 本次回傳 proxy 403（CONNECT tunnel failed），新聞清單無法取得，改以 WebSearch 補充。`info` 指令成功（快取時間 2026-11-02 15:33 UTC）。以下所有 headline 皆以 WebSearch 結果交叉比對，標註信心度。日期截止 2026-11-03，之後事件視為未知。

股價與估值快照（yf info，快取值，約延遲 15–20 分鐘）：

| 項目 | 數值 | 單位 |
|---|---|---|
| 最新價 | 258.35 | USD |
| 前收 | 257.81 | USD |
| 52 週區間 | 199.19 – 332.46 | USD |
| 50 日均線 / 200 日均線 | 235.17 / 249.16 | USD |
| 市值 | 約 244.2 | USD B |
| 企業價值 (EV) | 約 300.4 | USD B |
| TTM 營收 | 69.9 | USD B |
| TTM 淨利（netIncomeToCommon） | 11.2 | USD B |
| Trailing / Forward EPS | 11.72 / 13.23 | USD |
| 股息（季） / 殖利率 | 1.69 / 約 2.6% | USD |

交叉驗算：價格 258.35 × 流通股 945.1M ≈ 244.2B USD，與 marketCap 吻合；EPS 11.72 × 945.1M ≈ 11.1B USD，與淨利 11.2B USD 吻合，單位無誤。

## Top company-specific headlines (last 14d)

| 日期 | 事件 | 來源 | 影響 | 一句話理由 |
|---|---|---|---|---|
| 2026-10-21 | 2026 Q3 財報：營收約 17.1 USD B（年增約 5%）；Software 年增 8%（固定匯率 9%）、Infrastructure 年增 4%、Consulting 持平 | [SEC 8-K Ex.99](https://www.sec.gov/Archives/edgar/data/0000051143/000005114326000093/ibm-20261021xex991.htm)、[TechNews](https://finance.technews.tw/2026/10/22/ibm-q3-earnings-positives-weak-gross-margin-after-hours-stock-falls-4-percent/)、[INDmoney](https://www.indmoney.com/blog/us-stocks/ibm-stock-q3-earnings-analysis) | 偏多 | 營收與 EPS 優於市場預期，軟體動能回溫 |
| 2026-10-21 | 獲利：營運 diluted EPS 2.95 USD（年增 11%）；GAAP EPS 約 2.30 USD（來源對「adjusted/operating」定義不一，需以 8-K 為準） | 同上 | 偏多 | 獲利成長，但不同來源 EPS 口徑不同，需注意 |
| 2026-10-21 | 毛利率：GAAP 毛利率 56.8%（年減 50 bp）；營運毛利率 58.5%（年減 20 bp）；營運稅前利潤率升 70 bp 至 19.3% | [StockHub](https://stockhub.kr/en/insights/20261022-ibm-cy26q3)、[Quartr](https://quartr.com/events/international-business-machines-corp-ibm-q3-2026_3PPXZ5Fe) | 偏空 | 毛利率未達華爾街預期，是本季主要扣分項 |
| 2026-10-21 | 現金流：Q3 FCF 3.0 USD B（年增 0.7 USD B）；YTD FCF 7.8 USD B（年增 0.6 USD B）；全年 FCF 預期年增超過 1 USD B（上修） | [Storage Newsletter](https://www.storagenewsletter.com/?p=306426)、[Goldesel](https://goldesel.de/aktien/news/ibm-aktie-q3-ubertrifft-erwartungen-doch-die-aktie-fallt-trotz-hoherer-cashflow-prognose) | 偏多 | FCF 指引上修是本季最實質的正面訊號 |
| 2026-10-21 | 全年指引：固定匯率營收成長維持 4%–5%（未上修）；部分來源提及營業稅前利潤率擴張約 100 bp | 同上 | 中性 | 營收指引不動，但市場解讀本季 beat 有部分來自合約遞延入帳 |
| 2026-10-21 至 10-22 | 股價反應：盤後初漲至約 255 USD 後回落；德文媒體標題為「Q3 優於預期但股價下跌」。收盤幅度無法於來源確認 | [TechNews](https://finance.technews.tw/2026/10/22/ibm-q3-earnings-positives-weak-gross-margin-after-hours-stock-falls-4-percent/)、[Goldesel](https://goldesel.de/aktien/news/ibm-aktie-q3-ubertrifft-erwartungen-doch-die-aktie-fallt-trotz-hoherer-cashflow-prognose) | 中性偏空 | 反應分歧；目前價 258.35 已站上 50 日與 200 日均線，顯示事後已部分修復（以 yf 快照推算） |
| 2026-11-10（已公告） | 季度股息 1.69 USD，除息日 2026-11-10（yf corporateActions） | [Yahoo Finance info 資料] | 中性 | 例行事件，對基本面無改變 |
| 2026-10-10 | Qiskit C API 原生綁定發布（Rust core 之 Qiskit v2.0，提供 Fortran / C++ / Julia 介面，目標 HPC 使用者） | [Quantum Computing Report](https://quantumcomputingreport.com/ibm-expands-qiskit-beyond-python-with-native-c-api-bindings-for-fortran-c-and-julia/amp/) | 偏多（量子生態） | 強化 Qiskit 在 HPC 端的採用面；但在 14 天窗口之外，列於量子段落 |

低信度 / 未確認項目（不計入 net read）：
- TipRanks 列表出現「IBM 與 NVIDIA 共建 AI 系統以組織數據」（無日期，相對時間戳）。無法確認發布日，暫列為未驗證。
- Autobound 頁面最後更新 2026-09-24，早於窗口，未採用。

已剔除之舊聞（非 14 天內，僅作背景）：
- 2025-11-06 IBM 進入 DARPA Quantum Benchmarking Initiative Stage B（11 家入選之一；Stage C 為最終階段）。[IBM Newsroom](https://newsroom.ibm.com/2025-11-06-ibm-advances-to-next-phase-of-darpa-quantum-benchmarking-initiative)、[DARPA](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection)
- 2025 Q4 裁員（低個位數百分比全球員工，推估數千人）。[Computing.co.uk](https://www.computing.co.uk/news/2025/ibm-cuts-3000-roles)
- Confluent 收購（EV 11 USD B，每股 31 USD），來源稱 2026-03-17 完成，原定 2026 年中。日期來自二手來源，未見 IBM 官方新聞稿確認。[Techzine](https://www.techzine.eu/news/infrastructure/137056/ibm-to-acquire-confluent-for-11-billion/)、[Letsdatascience](https://letsdatascience.com/news/ibm-acquires-confluent-to-power-real-time-ai-d2e5f439)

## Sector macro

- 2026-10-28 — FOMC 維持利率不變，來源多稱目標區間 3.75%–4.00%，投票 10–2（Cook 與 Hammack 主張升息 25 bp）。前次為 2026-09-16 升息 25 bp。影響科技 / IT 服務：偏緊縮的利率環境對高本益比（forward P/E 約 19.5x）與長天期成長股估值形成壓力；市場定價 12 月升息機率。注意：不同來源的利率區間前值不一致（3.50–3.75% 與 3.75–4.00%），需以 Fed 官方聲明核對。[Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/fomc-october-2026-fed-holds-rates)、[InvestingLive](https://investinglive.com/central-banks/fomc-decision-oct-28/)、[Babypips](https://www.babypips.com/analysis/event-guide-forex-us-fomc-statement-october-2026-10-27)
- 關稅 / 供應鏈 / 地緣：本次搜尋未取得可用的 2026-10 至 11 月關稅相關資料。此項為資料缺口，未納入判斷。
- 企業 IT 支出：IBM 的 Consulting 本季持平，顯示企業諮詢需求仍偏保守；Software 成長為主要支撐。無可用的產業級支出數據。

## Quantum / Qiskit roadmap context（thesis 背景）

- 2026-10-10 — Qiskit v2.0 Rust core 原生 C API（qiskit.h），含 Fortran / C++ / Julia 綁定。偏多，強化 HPC 整合故事。[Quantum Computing Report](https://quantumcomputingreport.com/ibm-expands-qiskit-beyond-python-with-native-c-api-bindings-for-fortran-c-and-julia/amp/)
- IBM 官方 roadmap（標準頁，非 2026-10 更新）：2026 年目標為展示首個科學性 quantum advantage 示範，以及 fault-tolerant module；2029 年目標 fault-tolerant 系統（Starling 名稱僅見一則贊助型開發者部落格，可信度低）。未找到 2026-10 之官方 roadmap 修訂。[IBM Quantum Roadmap 2026](https://ibm.com/roadmaps/quantum/2026)、[AI Integration blog](https://blog.codercops.com/blog/quantum-computing-2026-developers)
- Qiskit v2.4 已於 IBM Research 頁列為 Release News，但內容細節未取得。[IBM Research](https://research.ibm.com/quantum)
- DARPA QBI Stage B 入選（2025-11-06）：為 IBM 量子技術的第三方驗證里程碑，後續進入 Stage C 的條件是 Stage B 結案。
- 量子同業：Quantinuum 據一則 Motley Fool Canada 報導於 2026-06 以獨立公司形式上市（代號 QNT），僅單一來源，未經核實。IonQ、Rigetti 在 2026-10 底的股價或財報事件未能取得可用資料。

## Peer signals

- Kyndryl（KD）— 2026-08-05 季報營收 3.6 USD B，低於估計約 1.1%；下一季財報日期來源不一致（2026-11-04 或 11-06，盤前）。KD 為 IT 基礎設施服務同業，其下季指引可作為企業 IT 服務需求的參照。[SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001867072/000110465926055902/kd-20260505xex99d1.htm)、[TipRanks](https://www.tipranks.com/stocks/kd/earnings-calendar)
- Accenture、Oracle：本次搜尋無 2026-10 至 11 月的財報或股價資訊，無法評估。
- IonQ、Rigetti、Quantinuum：無 2026-10 之可用新聞，無法判斷量子同業情緒。
- 資料缺口：同業股價走勢未能以可靠來源取得，不宜據此推論板塊動能。

## Forward calendar (next 14d, 2026-11-03 至 2026-11-17)

- 2026-11-04 或 11-06（待確認）— Kyndryl 季報（盤前）。IT 服務同業參照，影響中性。
- 2026-11-10 — IBM 除息日，股息 1.69 USD。機械性調整，無基本面影響。
- 2026-11-11 至 11-13 — IBM Quantum Developer Conference（第三屆，預計更新 Quantum Roadmap 與 advantage 相關主張）。主要事件性風險在於是否揭露新的 quantum advantage 證據或 Starling 進度。申請截止 2026-09-21，已於 10-12 發送最後錄取通知，對外新聞需待會後。[IBM QDC 2026](https://www.ibm.com/quantum/blog/qdc-application-2026)、[Sahm Capital](https://www.sahmcapital.com/news/content/ibm-opens-applications-for-quantum-developer-conference-2026-2026-06-29)
- 公司財報：IBM 下一季財報 yf 估計為 2027 年 1 月下旬，超出 14 天窗口。
- FOMC：下次會議約 12 月上旬（超出 14 天窗口）。窗口內無已知之重大 Fed 事件。

## Net read

整體來說，本期 headline 偏向混合，偏多幅度為小至中等。正面因素是 Q3 營收與營運 EPS 優於預期、Software 年增 8%、全年 FCF 指引上修超過 1 USD B，且股價目前（258.35 USD）已站上 50 日與 200 日均線，對應 forward P/E 約 19.5 倍，低於 TTM 的 22 倍。負面因素是 GAAP 毛利率年減 50 bp、部分營收 beat 來自合約遞延入帳、全年營收指引未上修，以及股價在財報後反應分歧。宏觀面 10 月 FOMC 偏鷹（持有且市場計價 12 月升息），對高估值科技股構成壓力。量子面的 Qiskit C API 與 11 月 QDC 是主要的題材催化劑，但目前缺乏具體的新量子營收或商業化證據，對基本面的實際影響有限。主要資料缺口包括 yf 新聞清單失效、同業股價缺失、關稅相關新聞缺失，以及部分來源之 FOMC 利率區間與 Q3 EPS 口徑不一致，判讀時需以 IBM 8-K 與 Fed 官方聲明為準。

NEWS REPORT COMPLETE
