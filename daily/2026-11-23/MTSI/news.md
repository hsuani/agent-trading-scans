# News — MTSI as of 2026-11-23

資料來源與限制：
- `pipeline/tools/yf MTSI news` 回傳 403 (proxy CONNECT tunnel failed)，無法取得 Yahoo 新聞清單，改以 WebSearch 補充。
- `pipeline/tools/yf MTSI info` 可用，但為 cache 快照 (cached_at 2026-11-22T14:31 UTC)，最近交易日資料取自該快照，未即時核對。
- SEC EDGAR 新聞稿 (8-K ex99.1) 無法連線 (DNS 失敗)，Q4 FY26 與 Q1 FY27 guidance 數字取自 Zacks / Earnings Whispers / finviz 等二手彙整，未與原始新聞稿逐字核對。
- 多個來源對 11/04–11/20 的股價與跌幅數字互相矛盾，以下標示為 unverified。
- 不採用任何 daily/ 舊報告的數字。所有資訊日期截止 2026-11-23。

## Top company-specific headlines (last 14d)

| 日期 | 事件 | 來源 | 影響 | 說明 |
|---|---|---|---|---|
| 2026-11-05 | FY26 Q4 財報：營收 $424.8M (YoY +62.7%)，adj. EPS $2.09 vs 共識 $2.00；營收落在管理層 $415–425M 區間上緣 | Zacks, finviz, Earnings Whispers (WebSearch 彙整) | 偏多 (基本面) | 營收與 EPS 雙超預期，adj. GM 61.3%、adj. op margin 38.2%。FY26 全年營收 $1,327.6M (YoY +37.3%)，與 yf totalRevenue 一致 |
| 2026-11-05 | FY27 Q1 guidance：營收 $450–460M (共識 ~$431.3M)；adj. GM 62–63%；adj. EPS $2.21–2.29 (共識 ~$2.02)；non-GAAP 稅率約 6%、稀釋股數 79.0M | Zacks, Earnings Whispers | 偏多 | guidance 明顯高於共識。毛利率擴張預期放緩、稅率約翻倍是需注意的細節 |
| 2026-11-05 | 管理層中長期框架：FY27 成長 >30%，data center 基本情境上修至約 80%；~$2B FY27 營收、~$10 EPS、$5B 2030 營收「雄心」 | Earnings Whispers (WebSearch 彙整) | 偏多但不確定 | 屬管理層目標而非正式 guidance，且僅見於二手彙整，標示 unverified |
| 2026-11-05 | FY27 資本支出指引 $100–110M，約 60% 投入 wafer fab；book-to-bill 由 1.6 降至 1.4，但 backlog 創新高 | WebSearch 彙整 | 中性偏空 | 資本支出大幅上升與訂單節奏放緩，是股價反應的主要疑慮來源 |
| 2026-11-05 | 財報後股價大跌，Benzinga 記為當日 −18.4%、當年最大量 | WebSearch 彙整 (Benzinga) | 偏空 (價格) | 跌幅數字 unverified；另一來源僅稱「營收超預期但股價下跌」。市場焦點為 capex 與訂單節奏，非明確 guidance 下修 |
| 2026-11-04 | 財報前滑落至 inter-earnings 低點 $209.51 (自 10/06 高點 $353.54 回落約 41%) | WebSearch 彙整 | 偏空 (價格) | 財報前已大幅跌價，AI 資本支出疑慮與 Semtech 等同業同步走弱 |
| 2026-11-11 | 收盤 $249.86 (Benzinga 記載) | WebSearch 彙整 | 中性 | 價格脈絡點，未獨立驗證 |
| 2026-11-20 (Fri) | 快照顯示 regular session 收 $194.91，單日 −10.8% (前收 $218.55)，日內區間 $192.99–$214.18；盤後反彈 +3.6% 至 $202.00 | yf info 快照 | 偏空 (價格) | 單日跌幅原因未在任何來源找到。Benzinga 另稱 11/20 低點 $155.39，與快照 day low $192.99 及 52 週低點 $158.02 矛盾，**unverified** |
| 2026-09-17 (press release，非近 14d) | 推出 3.2T front-end chipset (8 通道 448G PAM-4，driver / photodiode / TIA)，ECOC 2026 (9/21–23) 展示 | financialcontent / GlobeNewswire 摘要 | 偏多 (產品面，背景) | 超出 14 天窗口，僅作背景。一則「股價 +5%」的 RTT 快訊日期不明，不採信為近期催化 |
| — | 管理層異動、M&A、訴訟、監管事件 | 未找到 | 無 | 未發現近 14 天相關新聞。yf info 管理層名單：CEO Stephen Daly、CFO John Kober (無變動跡象，快照未註明異動) |

## Sector macro

- 2026-11-03 — 德州州長選舉結果：Gina Hinojosa 當選，競選承諾於 2027-01-19 就任後暫停新 data center 開發，直到州議會通過水資源、電費與稅收相關保護。Impact on 半導體 / AI 基礎建設: **偏空**。德州約佔美國規劃中 data center 容量 25–27% (Goldman / Wells Fargo 引述)。注意：此為候選人承諾，尚未實施；部分來源對勝選結果的細節仍 **unverified**。
- 2026-08 — 德州州長 Abbott 已先行暫停 PUCT / ERCOT 的 data center 審批 (TechCrunch 2026-08-04)，為既有政策背景，非本次新事件。Impact: **偏空** (電力與審批瓶頸延長)，對 MTSI data center 出貨節奏的直接影響 unverified。
- 2026-11-04 至 11-06 — AI 資本支出與 neocloud 疑慮引發半導體拋售。SOX 單日跌幅來源不一 (約 7%–12%)；UBS 估計美國 2028 年 data center 容量新增中約 30% 有暫停風險 (IBTimes 引述)。Impact on 半導體: **偏空**，且與 MTSI 的 data center 成長敘事直接相關。
- 利率：Morningstar 與 Schwab 的 10 月資料顯示 fed funds 目標區間 3.75%–4.00%，9 月升息後 10 月維持，兩位委員主張升息；當時市場預期 12 月可能再升息。**目前市場隱含機率 unverified** (資料截至 10 月)。Impact on MTSI (beta ~1.83)：利率上行壓抑高 beta 估值，**偏空**。
- 光通訊族群：COHR、LITE、CRDO、AAOI 出現過反彈與賣壓交替，日期多不明。Impact: 族群情緒 **混合**，無法確認 11 月的具體價格路徑。

## Peer signals

- NVDA — FY27 Q3 (季度止於 10/25) 於 2026-11-17 公布。來源 (TechPowerUp, Shacknews) 稱營收約 $115.8B (YoY +103%)、adj. EPS $2.68 vs 共識 $2.49，盤後上漲。一份 Yahoo 預覽稱公布日為 11/19，與官方 11/17 不一致，採信 11/17。TechPowerUp 另一行提到 $107.6B，與標題數字矛盾。**整體 AI 需求訊號偏多**，但數字需以 NVIDIA IR 原文核對 (investor.nvidia.com 本次未能直接讀取)。
- SMTC (Semtech)、LSCC (Lattice)、WDC — 2026-11-04 至 11-06 與 MTSI 同步下跌 (StockStory、Barchart)，顯示板塊性拋售而非個股事件。Impact: **偏空** (情緒傳染)。
- COHR、LITE、CRDO — 光通訊族群有反彈 (COHR +13%、LITE +11% 等) 與賣壓 (CRDO 財報後約 −15%) 的報導，日期不一。Impact: **混合**，為 MTSI 光學與 3.2T 產品的直接競品與同題材股。
- AVGO — 本次搜尋未找到可靠的 11 月資料，**無法評估**。

## Forward calendar (next 14d, 2026-11-23 至 2026-12-07)

- 2026-11-26 (Thu) — 美國感恩節，股市休市 (標準 NYSE 假期，未逐項核對)。週五 11/27 通常提前收盤。流動性偏薄，波動可能放大。
- 2026-12 初 (日期 unverified) — FOMC 12 月會議。來源未能確認確切日期，僅見 2025 年的 12/9–10 資料，需以 Federal Reserve 官方行事曆確認。升息機率為關鍵變數。
- 2026-12 初 (日期 unverified) — 其他 AI 基礎建設與光學同業財報 (如 AVGO、MRVL 等) 的確切日期未找到，**unverified**。
- MTSI 下一次財報：yf info 的 earningsTimestamp 為估計值 (isEarningsDateEstimate: true)，換算約 2027-02-04，超出 14 天窗口，**非窗口內催化**。
- 德州 data center 政策：Hinojosa 於 2027-01-19 就任，超出窗口。

## Net read

近 14 天的公司基本面新聞以偏多為主：FY26 Q4 營收 $424.8M、adj. EPS $2.09 雙超共識，FY27 Q1 guidance ($450–460M 營收、$2.21–2.29 EPS) 明顯高於市場預期，data center 成長目標上修，book-to-bill 雖降但 backlog 創新高。然而市場對這些利多的反應極為負面，股價從 10/06 高點 $353.54 跌至快照中 11/20 收盤 $194.91，單日 −10.8%，52 週區間 $158.02–$418.90。市場關注點在 capex 大幅上升 ($100–110M)、訂單節奏放緩與 AI data center 監管風險 (德州選舉結果、審批暫停、UBS 的 2028 年容量風險估計)，加上板塊性 AI 拋售，使新聞的實際 price-moving 效果偏空。綜合判斷：**混合偏空，強度中等**。基本面新聞為強烈正向，但價格驅動的情緒與板塊宏觀 headline 為負向，且 11/20 的單日跌幅原因仍未確認。最大的不確定性來自資料品質：yf 新聞端點失效、SEC 原文無法讀取、多項價格與日期互相矛盾，建議在使用本報告前以即時報價與原始新聞稿複核 11/05 與 11/20 的數字。

NEWS REPORT COMPLETE
