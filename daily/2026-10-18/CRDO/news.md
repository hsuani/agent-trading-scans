# News — CRDO as of 2026-10-18

資料來源說明: yfinance `news` 端點在本沙盒回傳 ConnectionError (proxy 403), 無法取得快取新聞; `ratings` 不是 yf.py 支援的子命令 (已改用 `rec_summary`); `earnings_dates` 與 `rec_summary` 來自快取。以下新聞主要來自 WebSearch 的二手媒體報導, 多數價格數字互相矛盾, 已在條目中標註。未找到任何日期在 2026-10-18 之後的資訊。

## Top company-specific headlines (last 14d 優先, 部分為近 30 日)

- 2026-10-12 — Credo 於 OCP Global Summit 發布 1.6T ZeroFlap Active Light Cable (ALC), 採 NRZ 將 200G 通道拆成多條低速光學通道, 目標 reach 最長 50m、每端約 12W、MTBF 目標 1 億小時; 出貨預計 2027 年 (DataCenterDynamics; 公司新聞稿 PDF, s205.q4cdn.com). Impact: bullish。光學產品線向中距離 (mid-reach) 延伸, 擴大 TAM; 但量產時點在 2027, 對近期財報影響有限。
- 2026-10-16 報導 — 高階主管 Chi Fung Cheng (媒體標示 CTO) 於 2026-10-12 賣出 3,790 股, 依預定 10b5-1 計畫執行 (Daily Political; Defense World). Impact: neutral。計畫性賣出, 金額與比例小。
- 2026-10-16 報導 — Rosenblatt 維持 Neutral, 目標價 $235 (Defense World). Impact: neutral。
- 2026-10 (確切日期未確認) — Mizuho 重申 Outperform, 目標價 $245, 於會晤公司管理層後發布 (Investing.com). Impact: bullish。
- 2026-10-16 前後 — 股價回檔: MarketBeat 報 10/16 盤中下跌 4.9%, 最低 $168.56, 最後成交 $169.70; Investing.com 則報 $179.23, 一週下跌約 15%。兩來源價位差距大。原因被歸為板塊獲利了結與估值擔憂, 以及近期內部人賣出。Impact: bearish (價格面, 屬於 price action, 不計入基本面)。
- 2026-09-01 — FQ1 FY27 財報 (季度截至 2026-08-01): 營收 $479.0M, 年增 115%, 季增 9.6%; 非 GAAP EPS $1.20 (共識 $1.17, 與快取一致); GAAP EPS $0.67; 非 GAAP 毛利率 68.0%, GAAP 毛利率 64.5% (前季 68.2%); 現金及短期投資約 $764M。FQ2 指引 $525–535M (中點 $530M), 高於分析師共識約 $516.5M (Pulse2 / 01net 新聞稿轉載; tikr; parameter.io). Impact: 營收與指引 bullish; 毛利率下滑 bearish。財報後股價下跌, 媒體描述幅度從 -8% (盤前) 到 -9%、甚至 -18% 不等。
- 2026-09 (財報電話會議) — 公司重申 FY27 光學營收預期 >$600M。媒體對全年營收成長指引描述不一 (有稱上修至 >85% 成長, 有稱僅為重申), 未能確認是否上修。Impact: bullish, 但指引細節未驗證。
- 近 30 日內無確認的 M&A、高階主管異動、監管或訴訟新聞。

背景 (日期早於 30 日, 僅供脈絡):
- FQ3 FY26 期間新增一家超大規模客戶採用 AEC (Zacks / Barchart, 日期未標示)。Impact: bullish, 客戶基礎擴大。
- 與 TensorWave 合作, 支援 AMD 基礎 AI 叢集 (公司新聞稿 PDF, 日期未確認)。Impact: neutral to bullish。

已排除: 無日期的 Weiss Ratings 下跌快訊 (價位 $210.70 與 $218.66, 無法對應到特定交易日); Google Finance 標示 "Oct 6" 的 $214.03 快照 (來源未明確日期, 不採用)。

## Sector macro

- 2026-09-16 (Dell'Oro, 經 IEEE ComSoc Techblog 轉載) — 2Q26 全球資料中心 capex 年增 92%, 2026 年全球資料中心 capex 預估超過 $1T; 美國前四大雲端業者 Q1 capex 年增 78% (convergedigest). Impact on AI datacenter connectivity: bullish。AEC 與光學互連需求直接受 capex 驅動。報告亦提醒數據有統計口徑差異。
- 2026-08-14 (LightCounting 報告, 經 IEEE ComSoc Techblog) — 高速光學元件嚴重短缺, 雲端業者的供應商由 2–3 家擴大到 5–7 家. Impact on CRDO: 中性偏多。供應商多元化有利於新進者與替代方案, 但光學供應瓶頸也可能限制 Credo 光學模組出貨速度。
- 2026 (Tower Semiconductor Q2 報告; GlobalFoundries 擴產計畫, 經 IEEE ComSoc) — Tower 矽光子營收年增三位數; GlobalFoundries 計畫今年把矽光子業務翻倍。Impact: 光學供應鏈擴產, 中性。
- 2026-08 (Zacks 產業文章) — AI 叢集正從 400G 遷移到 800G, 1.6T 網路預計 2027 年開始。Impact: bullish, 與 1.6T ZeroFlap ALC 的時程一致。
- 2026-01-14 / 01-15 (White House 公告, Thomson Reuters 報導) — 美國 Section 232 半導體關稅第一階段: 針對特定先進 AI 晶片 (如 NVIDIA H200、AMD MI325X) 課徵 25% 關稅, 美國資料中心使用等情況豁免。Impact: neutral (主要影響上游 GPU, 對 CRDO 直接影響有限)。後續階段在本次搜尋中未查到, 狀態未確認。

## Peer signals

- MRVL — 宣布收購 XConn Technologies (PCIe / CXL switching, UALink scale-up fabric), 營收預計 FY27 下半年起認列 (日期未確認, 2026 年中前後). Impact on CRDO: 中性偏空, 在 PCIe/CXL 與 scale-up 互連領域競爭加劇。
- ALAB — Q1 2026 營收 $308M, 年增 93%, Gen 6 產品占營收超過三分之一 (Zacks, 2026 年中). Impact: 同屬 AI 連接賽道, 板塊情緒共振; 競爭面中性。
- AVGO — Zacks 指 FY25 AI 營收 $200 億, 年增 65%。本次搜尋未取得 AVGO AEC 或 SerDes 的市占資料。Impact: 大型競爭者, 中性。
- 板塊情緒 — 近期高估值 AI 與半導體股出現輪動性拋售 (Weiss 快訊, 日期不明, 本身未能對應到 10/16)。Impact: bearish 情緒面。

## Forward calendar (next 14d, 2026-10-18 至 2026-11-01)

- 2026-10-27 至 10-28 — FOMC 會議; 10/28 14:00 ET 發布利率決策與聲明, 14:30 記者會 (fedratecalc.com 與多家來源一致). Expected impact: 高估值成長股對折現率敏感, 利率意外可能放大 CRDO 的波動。本次未查到最新 Fed 對關稅的談話。
- 無已確認的 CRDO 財報日於此窗口內。
  - 快取 (yfinance earnings_dates) 顯示下一次財報日 2026-11-30, EPS 共識 $1.28。
  - WebSearch 另列 2026-12-01 (盤後) 或 12-07, 日期來源不一致。以上皆在 14 日窗口之外。
  - 另一則搜尋結果提到下季共識 EPS $1.03, 與快取數字不符, 判定為舊數字, 未採用。
- 同業財報與其他產業事件: 本次未確認具體日期, 未列入。

## Net read

近 30 日的基本面 headline 偏多。FQ1 FY27 營收年增 115%, FQ2 指引中點高於共識; 1.6T ZeroFlap ALC 發布, 技術路線與 800G→1.6T 的產業時程吻合; 分析師方面 (快取 rec_summary 近 3 個月為 Strong Buy 4 / Buy 14 / Hold 1 / Sell 0, Rosenblatt 維持 Neutral、Mizuho 維持 Outperform) 仍偏正面。數據面的主要負面是 FQ1 財報後股價下跌, 原因包括 GAAP 毛利率下滑 (64.5%, 前季 68.2%)、估值擔憂, 以及 10 月中的板塊性回檔與計畫性內部人賣出。板塊層面, AI capex (2Q26 年增 92%) 與光學供應短缺支持需求端, 而同業 MRVL 在 PCIe/CXL 領域的併購與 ALAB 的快速成長增加競爭。Net headline tilt: 偏多, 幅度中等 (基本面 bullish 較強, 價格與情緒面 bearish 較弱)。精確股價位在本次未能確認 (各來源在 $169 至 $219 之間), 因此股價位的判斷需以即時行情為準。FOMC 10/28 為最近的已知催化劑。本報告不含交易建議。

## Data quality notes

- yfinance news: 不可用 (403 proxy)。新聞覆蓋完全依賴 WebSearch 二手來源。
- 財報 EPS: 快取 (Reported EPS 1.20 vs 1.17) 與 WebSearch 中一則 (EPS $0.78 vs $0.93) 不一致。本報告採用快取與 Pulse2 新聞稿轉載的非 GAAP 數字。
- 全年指引: 有無上修存在分歧, 未確認。
- 股價: 10/16 前後各來源價位差距約 $10 至 $50, 不採用任何單一數字。
- 下次財報日: 快取 2026-11-30, 其他來源 12-01 或 12-07, 未確認。

NEWS REPORT COMPLETE
