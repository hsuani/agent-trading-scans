# News — RGTI as of 2026-11-10

> 資料來源說明：yfinance 新聞端點 (`pipeline/tools/yf RGTI news`) 本次連續回傳 403 (Yahoo 網域被 gateway 政策拒絕)，無法取得 provider 新聞清單。本報告改以 WebSearch 補足，所有來源為搜尋結果所列連結。yf `info` 端點正常，僅用於價格快照與行事曆欄位。部分搜尋結果彼此矛盾，已於文中標註。

## Top company-specific headlines (last 14d)
- 2026-11-10 (預告) — Rigetti 公布 2026 Q3 財報並於 17:00 ET 召開法說會 (GlobeNewswire 2026-10-27 公告；yf earningsTimestamp 與此一致). Impact: neutral，待財報結果。Q3 為近期最主要催化劑，見 Forward calendar。
- 2026-11-05 (間接) — 量子股同步重挫，RGTI 與 QBTS、IONQ 同步下跌。TIKR 報導 RGTI 跌約 18%，但同標題寫 8%，數字互相矛盾；報導歸因為科技股整體拋售而非公司新聞。Impact: bearish（情緒面），非公司基本面事件。
- 2026-11-05 — IBM、ORNL、AMD 聯合發布量子糾錯 (QEC) 研究平台，IBM 120 qubit Nighthawk 與 ORNL Umbra (AMD MI355X) 整合，連結 DOE Quantum Genesis Mission 與 IBM Starling 2029 目標 (The Quantum Insider; ORNL 新聞稿). Impact: bearish（相對競爭）— 大型平台廠的 QEC 進展會拉高市場對 RGTI 技術路線的比較門檻，但本身為研究平台，無直接營收。
- 2026-09-08 — Rigetti 子公司 Rigetti & Co, LLC 與美國商務部簽署 CHIPS R&D 最高 100M USD 的 definitive agreement；政府取得少數非控制股權，資金分三年、三個研發項目 (The Quantum Insider; investors.rigetti.com 新聞稿). Impact: bullish — 非稀釋性研發資金與政府背書，但附帶股權條件，且先前於 2026-05 為 LOI 階段，本次是條款落定，非新增金額。
- 2026-08-06 — Rigetti 公布 Q2 2026 財報：營收 5.14M USD (YoY +185%，QoQ +16.8%，優於共識約 4.91M USD)；毛利率約 43%；營業虧損 28.1M USD；GAAP 淨虧損 52.6M USD、EPS -0.16 (共識 -0.06)，差距主要來自 warrant 與 earn-out 負債的非現金公允價值變動；現金與可供出售投資 541.3M USD、無負債 (The Quantum Insider; Quantum Computing Report; Earnings Whispers). Impact: 營收 bullish、EPS bearish (非現金因素為主)。
- 2026-01-20 — C-DAC (印度) 108 qubit 量子電腦採購訂單 8.4M USD；公司表示預計於 Q4 2026 認列收入 (須完成安裝與績效驗收) (Q2 財報電話會議摘要). Impact: bullish — 為 Q4 營收確定性來源，但時點依驗收而定，存在遞延風險。
- 2026 年內 — Cepheus-1-108Q 多晶片系統部署，公司稱為業界最大多晶片量子電腦 (公司新聞稿，WebSearch 摘要). Impact: neutral to bullish — 技術里程碑，商業化效益需由訂單驗證。
- 雜訊已剔除：單日股價漲跌百分比、分析師目標價調整等 churn 未列入。

## Sector macro
- 2026-11-05 — IBM / ORNL / AMD QEC 平台發布（同上）。Impact on quantum: 產業競爭與資金集中於大型平台；對小型純量子廠商的相對估值為壓力。
- 2026 (法案進行中) — National Quantum Initiative Reauthorization Act (S.3597 / H.R.8462) 將 NQI 延長至 2034；參議院商業委員會已一致通過 S.3597，眾議院科學委員會於 2026-04 通過 H.R.8462。可能透過 FY27 NDAA 附加。最新進度未能確認 (congress.gov 需人工核對)。Impact on quantum: bullish 若通過 — 研發預算與政策支持延續；出口管制與國際合作條款可能限制部分海外合作。
- 2026 (日期未確認) — 美國商務部 CHIPS 對量子公司的 R&D 資助行動 (RGTI、QBTS 皆已簽 definitive agreement，各最高 100M USD，含政府股權)。Impact on quantum: bullish 政策支持，但政府持股的股權稀釋與條件為中性偏負面的隱性成本。
- 宏觀利率 — 搜尋結果對 FOMC 日程與利率水準互相矛盾：一來源列 2026-10-27/28 FOMC 與 2026-12-08/09 會議；另一來源稱 2026-07-28/29 維持 3.50%-3.75%。未能取得可信的當前市場定價。Impact on quantum (高 beta, beta ≈ 2.15)：利率預期轉鴿通常對成長股估值有利，但需以 Fed 官網核對。
- 總體 CPI — 一來源稱 2026-10 CPI 於 2026-11-10 08:30 ET 公布，其他行事曆則列於 12 月，未確認。若 11-10 公布，與 RGTI 財報同日，會放大當日波動。

## Peer signals
- QBTS (D-Wave) — 2026-11-10 盤前 (08:00 ET 電話會議) 公布 Q3 2026 財報；Business Wire 2026-10-27 確認。搜尋摘要指 H1 2026 營收約 5.9M USD，需下半年約 36.5M USD 才能達到分析師 2026 年估計，目標難度高。亦已與商務部簽 definitive agreement (最高 100M USD)。Impact on RGTI: 同日 (11-10) 早盤的 QBTS 數字會先行反映到量子板塊情緒。
- IONQ — 2026 Q2 營收 80.1M USD (YoY +287%)，調整後 EBITDA 虧損 120.3M USD；10 月宣布以約 1.3B USD 收購 Elisity。Impact on RGTI: 營收規模與資本配置對比明顯，IONQ 的併購與高虧損可能被市場拿來對比 RGTI 的資本效率。
- IBM — 2026-11-05 與 AMD、ORNL 發布 QEC 平台（同上）。Impact on RGTI: 大型平台的糾錯進展屬長期競爭，短期內對 RGTI 的估值比較影響大於基本面。
- QUBT / ARQQ / LAES / HON — 本次搜尋未取得具體 11 月新聞，無可靠資料，不列入判斷。

## Forward calendar (next 14d)
- 2026-11-10 (盤後，17:00 ET 法說會) — RGTI 2026 Q3 財報與電話會議。yf 顯示 EPS 共識約 -0.187 (current year) / forward EPS -0.206；需關注營收是否延續 Q2 的 QoQ 成長，以及 C-DAC 收入認列時點與 Cepheus 訂單 pipeline。Expected impact: 高波動，方向未定。
- 2026-11-10 (盤前，08:00 ET) — QBTS Q3 2026 財報，為同日量子板塊第一個情緒指標。
- 2026-11-10 — 疑似 10 月 CPI 公布 (單一來源，未確認)。
- 2026-11-18 — 前述 FOMC 會議紀要 (若 10-27/28 會議屬實；未確認)。
- 2026-12-08/09 — 下次 FOMC 會議 (單一來源，未確認)。
- 進行中 — NQI 再授權法案與 FY27 NDAA 談判，時間不確定。

## Net read
公司層面，本週最重要的事件是 2026-11-10 盤後的 Q3 財報：Q2 營收 YoY 大增、CHIPS 100M USD 資金已落定，屬基本面正面；但 GAAP EPS 持續為大額負值（Q2 淨虧損 52.6M USD，營收僅 5.14M USD，約 10 倍於營收的虧損規模），加上 2026-11-05 量子板塊重挫與 IBM/AMD 的 QEC 平台發布，情緒面偏空。yf 快照顯示 2026-11-09 盤中 RGTI 報 12.775 USD，較前收 11.75 USD 上漲約 8.7%，市值約 4.26B USD，距 52 週低點 9.19 USD 與高點 34.71 USD 之間，空單佔流通股約 21.4%，屬高空單比例。綜合而言，headline 偏 **mixed**，多頭因素（營收成長、政府資金、C-DAC 訂單）與空頭因素（巨額虧損、板塊情緒、大型競爭者進展）大致拉扯，幅度中等。主要不確定性在於財報結果與 QBTS 同日盤前數據。

資料品質註記：(1) yf 新聞端點不可用，provider 層級 headline 未涵蓋；(2) 11-05 selloff 跌幅與 FOMC/CPI 日期來源互相矛盾，已標註；(3) yf 的 totalCash 為 393.7M USD，與 Q2 財報的 541.3M USD (含可供出售投資) 口徑不同，下游引用時需標明口徑；(4) 11-09 價格為盤中快照 (15 分鐘延遲)，非收盤價。

NEWS REPORT COMPLETE
