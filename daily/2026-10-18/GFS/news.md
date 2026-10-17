# News — GFS as of 2026-10-18

資料來源說明: `pipeline/tools/yf GFS news` 回傳 HTTP 403 (proxy CONNECT 失敗), 本次無法取得 yfinance 新聞清單, 公司新聞全部改由 WebSearch 補充, 來源為二手媒體與聚合網站, 多數未對照 GF 官方新聞稿。`ratings` 不是 yf.py 支援的子命令, 改用 `rec_summary`。未找到 2026-10-07 之後的 GFS 公司專屬新聞, 不作推論。

## Top company-specific headlines (last 14d)

本區間 (2026-10-04 至 2026-10-18) 未找到可確認的公司專屬新聞。以下為近 30 天內 (約 2026-09-18 起) 與近期重要事件:

- 2026-10-06 — Arete 上調 GFS 至 Buy, 目標價 $95 (Investing.com 評等表, 單一來源, 未交叉驗證)。Impact: bullish。分析師評等升級, 但來源可靠性低, 需以券商原文確認。
- 2026-09-30 (公告) — GF 宣布 2026-11-04 (週三) 08:30 ET 召開 Q3 2026 財報電話會議 (來源: finviz 轉載 GF 新聞稿標題)。Impact: neutral, 屬日程事件。
- 2026-09-17 — GF 與 Marvell 擴大多年期合作, 在 Burlington, Vermont 廠新增 SiGe 產能, 用於 pluggable optics、NPO、CPO 高速光連接晶片 (DatacenterDynamics、optionfinance 等多家報導)。Impact: bullish。直接對應 AI 資料中心光互連需求, 但未揭露財務條件與產能數字。
- 2026-09-02 至 09-24 — GF 2026 Technology Summit 系列 (Santa Clara 9/2、中國與台灣 9/22、9/24)。Impact: neutral, 產品路線圖宣傳性質。
- 2026-09-(約) — 董事會核准每股 $0.12 股利, 2026-10-09 支付, 除息登記日 2026-09-23 (單一聚合來源, 建議以 GF 投資人關係頁核對)。Impact: neutral。
- 2026-08-06 — TD Cowen 目標價由 $85 下調至 $75, 維持 Buy (MarketBeat 報導)。Impact: bearish (目標價下修), 評等未變。
- 2026-08-05 — Q2 2026 財報: 營收 $1.786B, 淨利 $167M, non-GAAP EPS $0.46 (yf 共識 $0.43, surprise +6.5%)。Q3 指引營收 $1.86B–$1.91B, non-GAAP EPS $0.46–$0.56。管理層將 AI 資料中心光學網路列為主要成長動能。Impact: bullish (營收與獲利超預期, 指引區間中位數高於共識 EPS $0.51 的中心附近)。
- 2026-07 (日期來源不一) — GF 與美國商務部簽署 LOI, 擬以 CHIPS and Science Act 名義提供 $300M 補助, 用於矽光子 3D hybrid bonding (near/co-packaged optics), 美國政府擬取得約 1% 股權。尚非最終授予。Impact: bullish (資金與政策支持), 但稀釋幅度小, 且尚未定案。
- 2025-11 (已在近 12 個月內) — GF 收購 Advanced Micro Foundry (AMF) 與 InfiniLink, 強化矽光子與光連接能力。背景事件, 非近期新聞。Impact: bullish (長期結構性)。
- 2026-06 附近 (Q1 2026 法說) — 管理層預期 2026 年矽光子營收約倍增, 並以 2028 年達 $1B 年化營收為目標 (單一來源轉述)。Impact: bullish (長期目標, 需追蹤兌現)。

## Sector macro

- 2026-01-14 — 美國依 Section 232 發布半導體關稅 proclamation, 對特定先進運算晶片及衍生品課 25% 關稅, 供美國供應鏈建置用途者豁免, 並表示未來可能擴大並配合關稅抵減計畫。Impact on 半導體代工: 以先進運算晶片為主, 對 GF 主力成熟製程直接衝擊有限, 但若第二階段擴大, 會影響成本結構與客戶拉貨。
- 2026-09-02 (單一來源, 未證實) — 商務部長 Lutnick 據報表示可能追加關稅, 範圍可能涵蓋伺服器、筆電與遊戲硬體。Impact on 半導體代工: 間接, 需求端風險大於直接關稅。可信度低, 建議查 Federal Register 或 Commerce 公告確認。
- 2026-06 (TrendForce 報告, 2026-06-08) — 台灣代工廠包括 TSMC、UMC、Vanguard、PSMC 因產能吃緊調漲價格, 漲價延續至 2027。Impact on 半導體代工: 偏多, 代工報價上行有利於 GF 定價, 但也可能讓部分客戶分散至其他代工廠。UMC 10% 漲價傳聞 (LinkedIn 來源) 未驗證。
- 2026-06 (TSMC 股東會, C.C. Wei 發言) — 規劃中的產能 (含美國新廠) 短期內無法滿足客戶需求。TSMC 2026 資本支出約 US$52–56B。Impact on 半導體代工: 偏多, 先進製程缺口可能外溢至成熟製程與替代代工廠。
- 2026 (SemiAnalysis 預測, 間接引用) — AI 相關晶圓約佔 TSMC N3 2026 年產出近 60%, 2027 年預計升至 86%; 行業預期至少兩年產能不足。Impact on 半導體代工: 偏多, 支持代工需求長期能見度, 但 GF 非先進邏輯主戰場。
- 2026 (成熟製程) — TSMC 與 Samsung 加速縮減 8 吋晶圓產能, 成熟製程供給收縮, 有利於利用率。Impact on 半導體代工: 偏多 (GF 為成熟製程主要供應商之一)。
- 2026 (中國成熟製程) — GF FY2025 20-F 指出中國以政策支持擴建成熟製程 (28nm 以上) 產能, 增速預期高於需求。出口管制主要針對 16/14nm FinFET 及以下。Impact on 半導體代工: 偏空 (中長期價格與市佔競爭壓力)。2026 年內新出口管制細節未找到。

## Peer signals

- TSMC — 先進製程與 AI 晶圓滿載, 2026 年多次表態產能不足, 漲價延續至 2027 (TrendForce 2026-06)。對 GFS: 偏多, 外溢需求 (AI 光學與部分特殊製程)。
- UMC / Vanguard / PSMC — 成熟製程代工廠同步漲價 (TrendForce 2026-06-08)。對 GFS: 偏多, 同業報價同步上行。
- Intel Foundry — CFO 於 BofA 會議表示晶圓代工可能比原計畫提早一季達成損益兩平; 目標 2030 年成為全球第二大代工廠 (Herald Corp, 2026 年中)。對 GFS: 偏空, 美國本土代工競爭加劇 (尤其是美國政府支持的製造題材)。
- Samsung Foundry — Q2 2026 法說稱 2nm 訂單預期 2026 年較 2025 年增加一倍以上, 洽談 Broadcom 等客戶 (Ground News 轉述)。對 GFS: 中性偏空, 先進製程競爭, 對成熟製程影響間接。
- Marvell (合作夥伴, 非競爭對手) — 2026-09-17 擴大與 GF 的 SiGe 合作。對 GFS: 偏多, 直接客戶需求訊號。
- Tower Semiconductor (競爭對手, SiGe/矽光子) — GF 於 2026 年 3 月於美國提起多項專利侵權訴訟 (單一來源)。對 GFS: 中性, 法律風險與競爭對手互動, 結果未知。

## Forward calendar (next 14d)

- 2026-10-09 — 每股 $0.12 股利支付日 (已宣布, 來源單一, 需核對)。Expected impact: 中性, 無實質影響。
- 2026-10-17 至 10-31 — 美股半導體同業財報季 (TSMC 10 月中旬營收、Samsung 與 SK Hynix 財報、ASML 等) 可能改變 AI 晶圓與成熟製程需求判讀。Expected impact: 中性至偏多, 取決於 AI 資本支出指引。（日期為推估, 未逐一核實。）
- 2026-11-04 (週三) 08:30 ET — GF Q3 2026 財報與電話會議 (公司確認)。Consensus EPS 約 $0.51 (yf 估計), 公司指引區間 $0.46–$0.56。Expected impact: 關鍵催化事件, 焦點為矽光子營收進度、Q4 指引與 Marvell 合作的產能落地。
- 2026-11 (未確認) — 美國 Section 232 第二階段或商務部新關稅公告的可能時點, 尚無確定日期。Expected impact: 中性偏空, 需追蹤。

## Net read

整體新聞訊號偏多, 強度中等。正面因子集中在三點: 一是 Q2 財報與 Q3 指引超出共識, 並以 AI 資料中心光學網路為主要驅動; 二是 Marvell 擴大 SiGe 合作與美國政府 $300M 矽光子 LOI, 強化 AI 光互連的長期定位; 三是 TSMC 與台灣成熟製程代工廠同步漲價、8 吋產能收縮, 有利於 GF 的報價與利用率。負面因子包括 Intel Foundry 與 Samsung 在先進製程與美國本土的競爭、中國成熟製程擴產的中長期壓力, 以及 Section 232 關稅擴大的不確定性。分析師評等偏正面 (yf rec_summary 近 1 個月為 4 Strong Buy、10 Buy、8 Hold、0 Sell、1 Strong Sell), 但 TD Cowen 等機構近期下修目標價, 評等與目標價方向未完全一致。價格資料來源彼此矛盾 (9/15 約 $42.75, 10/1 約 $48.68, 另一處 $47.88 與 $53.18), 且 2026 年 7 月單月跌幅 39.3%, 波動很大, 本報告不採用任何單一價格作為結論。最需要確認的缺口是: 2026-10-07 至 10-18 之間是否有 GF 公司級新聞, 以及 yfinance 新聞端點恢復後的完整清單。

NEWS REPORT COMPLETE
