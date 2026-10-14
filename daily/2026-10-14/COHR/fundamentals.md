# Fundamentals — COHR (Coherent Corp.) as of 2026-10-14

## Executive summary
COHR 的營運動能明顯轉強：FY26（2025-07 至 2026-06，6 月結束）營收 7,118.2M USD 年增 22.5%，Q4 FY26 單季年增 33.7%，毛利率升至 37.5%，調整後 EPS 全年 5.60 較前一年 3.60 成長約 56%。然而現金流品質明顯惡化：FY26 營業現金流僅 79.5M、資本支出 1,110.1M，FCF 為 -1,030.6M，且 FCF 已連續四季為負，同時靠股權募資約 2.0B 與 26% 的股本稀釋支撐資產擴張。估值方面，以前瞻 P/E 20.6x 計算尚可，但以 TTM 口徑看 EV/EBITDA 約 37.5x 至 41.2x、GAAP P/E 70.4x，估值成立與否高度取決於前瞻 EPS 兌現與資本支出回收速度。

## Revenue & profitability

**營收成長**
- FY 營收（yfinance annual income statement）：FY23 5,160.1M、FY24 4,707.7M（年減 8.8%）、FY25 5,810.1M（年增 23.4%）、FY26 7,118.2M（年增 22.5%）。
- 3 年 CAGR（FY23 至 FY26）約 11.3%。FY22 營收為 null，無法計算 4 年以上 CAGR。
- 季度趨勢加速：Q4 FY26（2026-06-30）營收 2,045.5M，年增 33.7%（對照 Q4 FY25 1,529.4M），環比增 13.3%（Q3 FY26 為 1,805.6M，環比增 7.1%，Q2 FY26 為 1,685.6M）。info 欄位 revenueGrowth 0.337 即為此單季年增率，並非全年數字。
- 分部營收：yfinance 未提供分部營收數字。依 longBusinessSummary，業務分為 Datacenter and Communications（transceivers、co-packaged optics、optical circuit switches、VCSEL、EEL 等）與 Industrial（excimer、solid-state、CO2 雷射，半導體設備、顯示器、材料加工，工程材料與光學元件）。分部占比與各分部成長率：DATA_UNAVAILABLE。

**獲利能力趨勢**
- 毛利率：FY23 31.4%、FY24 30.9%、FY25 35.2%、FY26 37.5%（gross profit 2,669.0M / 營收 7,118.2M）。Q4 FY26 單季毛利率 38.5%。
- 營業利益率：FY23 1.6%、FY24 2.6%、FY25 9.2%、FY26 12.7%（operating income 901.5M）。Q4 FY26 單季 14.9%。info 欄位 operatingMargins 為 11.8%，與報表計算值（12.7%）不同，本報告以報表計算值為準。
- 研發費用占營收：FY25 10.0%、FY26 10.2%（R&D 723.0M）；SG&A 占營收 FY26 14.7%。
- 淨利率（歸屬普通股東）：FY25 -1.4%（net income common -80.6M）轉為 FY26 10.8%（769.9M）。FY26 淨利（含非控制權益）805.0M，淨利率 11.3%，與 info profitMargins 0.11309 一致。
- EBITDA：FY26 normalized EBITDA 1,563.6M（22.0%）、FY25 1,136.1M（19.6%）。info ebitda 為 1,423.4M，與報表數字不一致，見紅旗段說明。
- EPS 口徑：GAAP 稀釋 EPS FY26 為 4.12（FY25 為 -0.52）。調整後 EPS（earnings_dates 的 Reported EPS）近四季為 Q1 FY26 1.16、Q2 1.29、Q3 1.41、Q4 1.74，全年合計 5.60；FY25 四季合計 3.60，年增約 56%。Q4 FY26 調整後 EPS 1.74 高於共識 1.62，超預期 7.6%。
- GAAP 獲利含一次性項目：FY26 含出售業務利益 124.1M、特殊項目 -3.7M，且所得稅率僅 7%（tax provision 60.8M / pretax 847.7M 約 7.2%）。FY25 所得稅率為 21%。因此 FY26 GAAP 淨利的品質需打折看待。
- ROE（info TTM）：7.98%。ROA（info）：3.39%。
- ROIC（估算）：以 FY26 營業利益 901.5M × (1 - 7%) 得 NOPAT 約 838.4M，除以期末 invested capital 14,125.7M，約 5.9%；以期初與期末平均 IC（約 11,729M）計算約 7.1%。屬本報告估算值，非 yfinance 直接欄位。

## Cashflow & balance sheet

**現金流品質**
- 營業現金流（OCF）：FY23 634.0M、FY24 545.7M、FY25 633.6M、FY26 79.5M（年減 87.4%）。FY26 OCF 占營收 1.1%。
- 營運資金吸收現金：FY26 change in working capital -1,102.2M，其中存貨 -1,183.0M、應收 -367.6M、應付 +748.5M、其他 -300.1M。
- 資本支出（capex）：FY23 436.1M、FY24 346.8M、FY25 440.8M、FY26 1,110.1M（年增 152%），占營收由 7.6% 升至 15.6%；capex / D&A（521.9M）為 2.1x。
- FCF（OCF - capex）：FY23 198.0M、FY24 198.9M、FY25 192.8M、FY26 -1,030.6M（FCF margin -14.5%）。
- 季度 FCF：Q1 FY26（2025-09）-58.0M、Q2（2025-12）-95.7M、Q3（2026-03）-383.5M、Q4（2026-06）-493.4M，四季合計 -1,030.6M，與年度數字吻合。季度 capex：103.9M、153.6M、289.7M、562.9M，呈加速上升。
- FCF / 淨利（FY26）：-1,030.6M / 805.0M = -1.28x，遠低於 0.9 的健康門檻。
- SBC：FY26 186.5M（占營收 2.6%）；扣除 SBC 後 FCF 約 -1,217M。

**資產負債表（2026-06-30）**
- 總資產 18,299.9M（FY25 14,910.9M，年增 22.7%）；商譽加無形資產 7,260.1M，占總資產 39.7%。有形帳面價值 3,643.4M（FY25 為 -2,031.3M，因股權募資與特別股轉換而轉正）。
- 現金及約當現金 1,162.0M；另有其他短期投資 825.0M，現金加短期投資合計 1,987.0M（FY25 909.2M）。
- 總債務 3,538.4M（長期債務 3,214.3M、長期資本租賃 254.8M、流動債務 7.9M、流動資本租賃 61.4M 等；FY25 為 3,893.7M，減少 355M）。
- 淨債務 2,060.2M（FY25 2,777.7M，下降 25.8%）。淨債務 / normalized EBITDA = 1.32x（FY25 為 2.44x）。
- 流動比率 2.43x（流動資產 6,925.5M / 流動負債 2,853.9M；FY25 為 2.19x）；速動比率（info）1.17x。
- 負債 / 權益：約 32%（總債務 3,538.4M / 股東權益 10,903.5M）；info debtToEquity 31.6 為同類口徑近似值。
- 利息覆蓋：FY26 利息費用 190.3M，營業利益 901.5M 覆蓋約 4.7x（FY25 約 2.2x）。
- 存貨 2,581.0M（年增 79.6%），以 COGS 推算 DIO 約 211 天（FY25 約 139 天）。應收 1,343.3M（年增 39.3%），DSO 約 68.9 天（FY25 約 60.5 天）。應付帳款 1,905.4M（年增 125%）部分抵銷存貨累積。

**資本結構變化**
- 普通股期末股數 195.75M（FY25 155.56M，增加 25.8%）；稀釋加權平均股數 FY26 195.4M（FY25 154.8M，增加 26.2%）。
- 特別股權益 FY25 為 2,483.3M，FY26 歸零，同期普通股增加約 40M 股，推測為特別股轉換為普通股。確切條款需參照 10-K 原文，本報告未取得。
- FY26 現金流量：股權發行 +1,998.6M；債務發行 +1,921.3M、償還 -2,399.6M（淨償還 -478.3M）；出售業務收款 +437.0M；購入投資 -1,025.0M、出售投資 +289.4M（將資金配置於短期投資）。

## Capital allocation & insider signal

**資本配置**
- 股利：無普通股股利（info dividendYield 0.0、payoutRatio 0.0）。現金股利支出 FY25 與 FY26 皆為 11.4M（口徑未明確，可能與特別股相關），股利保障倍數：n/a。
- 股票回購：FY23 至 FY26 無回購（Repurchase Of Capital Stock 為 null 或 0）。
- 資本配置重心：FY26 以資本支出（1,110.1M）、存貨累積、債務淨償還（478.3M）為主，資金來源主要為股權募資（約 2.0B）與出售業務收入（437.0M）。
- 固定資產：Gross PPE 4,782.4M（年增 36.9%）；在建工程 776.5M（年增 114%），顯示產能擴建仍在進行中。

**內部人交易（2026-04-14 至 2026-10-14，近 6 個月）**
- 公開市場賣出：共 11 筆，合計約 35,636 股、金額約 10.65M USD（依 insider 工具 Value 欄位加總）。
  - 2026-09-11 DiGirolamo Enrico（董事）賣出 5,315 股，約 1.63M。
  - 2026-09-01 Eng Julie Sheridan（CTO）賣出 13,077 股，約 3.58M。
  - 2026-08-31 Skaggs Stephen Andrew（董事）賣出 2,272 股，約 0.63M；同日 DiGirolamo 賣出 2,272 股，約 0.63M。
  - 2026-08-18、2026-07-22、2026-05-12、2026-04-22 CFO Sherri Luther 分批賣出合計 8,000 股，約 2.73M。
  - 2026-09-09 Beard Robert P 賣出 500 股，約 0.15M；2026-09-02 Neal-Graves Lisa 賣出 2,200 股，約 0.59M。
  - 2026-05-11 Xia Howard H（董事）賣出 2,000 股，約 0.71M，同時有 2,000 股選擇權行使（Conversion of Exercise）。
- 公開市場買入：窗口內 0 筆。最後一筆買入為 2024-12-02 CEO Anderson 購入 500 股。
- 無償贈與與獎勵：2026-08-28 年度股票獎勵（CEO Anderson 30,564 股、CFO Luther 8,731 股、CTO Eng 17,333 股等）與 2026-09-11、2026-03-06 贈與，屬非市場交易，不計入賣出金額。
- 規模比較：窗口內淨賣出金額約 10.65M，相當於市值 57.1B 的約 0.02%，對股價供需影響有限。整體屬常態性賣出（多為薪酬兌現或選擇權行使後出售），訊號強度偏低，偏中性略空。
- 10% 以上股東：Bain Capital Investors 於 2025-11-07 以 143.37 USD 賣出 7,500,000 股（約 1.075B），超出近 6 個月窗口；交易表另列該股東剩餘 7,754,252 股（欄位 Value 為 null，性質待確認）。
- 內部人持股：4.42%（info heldPercentInsiders）。

**機構持股與空單**
- 機構持股占比 87.2%（機構數 1,779 家）。前十大：BlackRock 8.43%（16.61M 股，季增 11.1%）、Vanguard Capital Management 6.48%（季增 4.8%）、FMR 5.59%（季減 51.4%，為最大減持者）、Vanguard Portfolio Management 5.09%、State Street 4.36%、NVIDIA 3.95%（7.79M 股，季持平）、Invesco 3.77%、Geode 2.68%、Capital International 1.83%（季增 100%）、Morgan Stanley 1.67%。
- 空單：11.04M 股，佔流通股 6.56%，約 1.76 日覆蓋；月增 2.6%（前月 10.76M）。

## Valuation

**市場價格與區間（以 info 與 fast_info 快取為準）**
- 現價 289.98 USD（前收 288.02，盤中區間 273.93 至 290.53；資料時點 2026-10-14 約 11:41 UTC，marketState 為 PRE，屬盤前快取，非收盤價）。
- 52 週區間 108.19 至 440.00；現價距 52 週高點約 -34.1%，52 週漲幅 +160.9%。
- 50 日均線 304.60（現價低約 4.8%）；200 日均線 293.12（現價低約 1.1%）。
- Beta 2.11，屬高波動標的。

**估值倍數**
- Trailing P/E（GAAP，EPS 4.12）：70.4x。此數字受 FY26 出售業務利益與低稅率影響，參考價值有限。
- Trailing P/E（調整後 EPS 5.60，本報告推算）：約 51.8x。
- Forward P/E（info forwardEps 14.05）：20.6x。另 info epsCurrentYear 為 9.42（對應 P/E 30.8x）；前瞻 EPS 所屬會計年度 info 未明確標示，本報告以 forward P/E 20.6x 為參考但需留意口徑。
- PEG（info）：0.92。
- EV/EBITDA：info 為 41.2x（EV 58.68B / TTM EBITDA 1.42B）；以 FY26 normalized EBITDA 1,563.6M 計算約 37.5x。
- P/S（TTM）8.0x，EV/Revenue 8.2x。
- P/B 5.2x（bookValue 55.7）。
- P/FCF：FCF 為負，n/m。
- 同業中位數（估計）：DATA_UNAVAILABLE（本次未取得同業資料）。

**分析師共識（info）**
- 23 位分析師，recommendationKey buy，平均推薦值 1.58（1 為強力買進）。
- 目標價：均值 412.52（較現價 +42.3%）、中位數 420.00、高 500.00、低 280.00。低標 280.00 略低於現價。

**估值小結**
- 以前瞻 P/E 看，市場給予約 20x 水準；以 TTM EV/EBITDA 與 P/S 看，估值已反映高成長與獲利改善。
- 自由現金流為負，無法以 FCF 收益率驗證估值；估值成立前提是資本支出進入回收期後 FCF 轉正。

## Key catalysts
- **下次財報**：2026-11-04（yfinance earnings_dates 列出之預期日，距今約 21 天）。共識 EPS 1.96（對照 Q4 FY26 調整後 EPS 1.74，環比增約 12.6%；對照 Q1 FY26 調整後 EPS 1.16，年增約 69%）。
- **最近一次財報（2026-08-12）**：調整後 EPS 1.74 超預期 7.6%；GAAP 稀釋 EPS 1.19；單季營收 2,045.5M 年增 33.7%。
- **EPS 超預期紀錄**：yfinance earnings_dates 列出的 2023-05 為唯一不及預期紀錄（-29.1%），之後各季（2023-08 起）皆超預期，近四季超預期幅度分別為 7.6%、1.1%、6.8%、11.3%（由新到舊：2026-08、2026-05、2026-02、2025-11）。
- **產能與資本支出**：季度 capex 由 103.9M 升至 562.9M，在建工程 776.5M。資本支出能否轉換為營收與毛利成長，是下季財報的重點。
- **存貨與營運資金**：存貨 DIO 升至約 211 天、應收 DSO 升至約 68.9 天。下季若存貨持續累積或應收未回收，將進一步壓縮 FCF。
- **股權結構**：NVIDIA 持有 3.95%（策略性持股，投資條款未於 yfinance 取得）；FMR 季減 51.4%。
- **指引與管理層說明**：近期公司 guidance 文字與法說會內容未於本工具組取得，標記 DATA_UNAVAILABLE。
- **債務到期結構**：DATA_UNAVAILABLE（本工具組未提供債務到期表）。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY26) | 7,118.2M USD | +22.5% (FY25 5,810.1M) | DATA_UNAVAILABLE | 成長強 |
| 營收 3Y CAGR (FY23 至 FY26) | 11.3% | n/a | DATA_UNAVAILABLE | 中高 |
| 單季營收 (Q4 FY26) | 2,045.5M | +33.7% | DATA_UNAVAILABLE | 加速 |
| 毛利率 (FY26) | 37.5% | +2.3pp (FY25 35.2%) | DATA_UNAVAILABLE | 改善 |
| 營業利益率 (FY26) | 12.7% | +3.5pp (FY25 9.2%) | DATA_UNAVAILABLE | 改善但仍偏低 |
| 淨利率 (歸普通股, FY26) | 10.8% | 由 -1.4% 轉正 | DATA_UNAVAILABLE | 轉正，含一次性項目 |
| 調整後 EPS (全年) | 5.60 | +55.6% (FY25 3.60) | n/a | 強 |
| ROE (info TTM) | 8.0% | n/a | DATA_UNAVAILABLE | 偏低 |
| ROIC (估算) | 5.9% | n/a | DATA_UNAVAILABLE | 偏低 |
| 營業現金流 (FY26) | 79.5M | -87.4% (FY25 633.6M) | DATA_UNAVAILABLE | 紅旗 |
| 自由現金流 FCF (FY26) | -1,030.6M | 由 +192.8M 轉負 | DATA_UNAVAILABLE | 紅旗 |
| FCF / 淨利 | -1.28x | n/a | > 0.9 為健康 | 不健康 |
| 資本支出 / 營收 | 15.6% | 由 7.6% 升至 | DATA_UNAVAILABLE | 高，擴產期 |
| 流動比率 | 2.43x | 由 2.19x 升 | DATA_UNAVAILABLE | 健康 |
| 淨負債 | 2,060.2M | -25.8% (FY25 2,777.7M) | n/a | 改善 |
| 淨負債 / EBITDA | 1.32x | 由 2.44x 降 | DATA_UNAVAILABLE | 改善 |
| 負債 / 權益 | 約 32% (info 31.6%) | n/a | DATA_UNAVAILABLE | 中性 |
| 利息覆蓋 (營業利益 / 利息) | 4.7x | 由 2.2x 升 | DATA_UNAVAILABLE | 改善 |
| 普通股期末股數 | 195.75M | +25.8% | n/a | 稀釋明顯 |
| 存貨週轉天數 (DIO) | 約 211 天 | 由 139 天升 | DATA_UNAVAILABLE | 紅旗 |
| 應收週轉天數 (DSO) | 約 68.9 天 | 由 60.5 天升 | DATA_UNAVAILABLE | 惡化 |
| 內部人交易 (6M) | 淨賣約 10.65M USD，0 筆買入 | n/a | n/a | 中性偏弱，規模小 |
| 股利 / 回購 | 無 | n/a | n/a | 無資本回報 |
| P/E (GAAP TTM) | 70.4x | n/a | DATA_UNAVAILABLE | 高 |
| P/E (調整後 TTM，推算) | 約 51.8x | n/a | DATA_UNAVAILABLE | 高 |
| P/E (Forward) | 20.6x | n/a | DATA_UNAVAILABLE | 中 |
| EV/EBITDA (FY26 normalized) | 約 37.5x (info 41.2x) | n/a | DATA_UNAVAILABLE | 高 |
| P/S (TTM) | 8.0x | n/a | DATA_UNAVAILABLE | 高 |
| P/FCF | n/m (FCF 為負) | n/a | n/a | 無法評估 |
| P/B | 5.2x | n/a | DATA_UNAVAILABLE | 高 |
| PEG | 0.92 | n/a | DATA_UNAVAILABLE | 合理 |
| 分析師目標價均值 | 412.52 (+42.3%) | n/a | n/a | 市場共識偏多 |
| 空單 / 流通股 | 6.56%（約 1.76 日覆蓋） | 月增 2.6% | n/a | 中等 |
| Beta | 2.11 | n/a | n/a | 高波動 |

## Red flags
- **FCF 連續四季為負**：FY26 FCF -1,030.6M，Q4 FCF -493.4M，且 capex 季度內由 103.9M 加速至 562.9M。獲利成長未轉為現金。
- **營運資金大幅吸收現金**：存貨年增 79.6%（DIO 由約 139 天升至約 211 天），應收年增 39.3%，FY26 營運資金變動 -1,102.2M。應付帳款增加部分抵銷，但仍需觀察應付是否可持續。
- **股本稀釋約 26%**：普通股由 155.6M 增至 195.8M，並以約 2.0B 股權募資支應資本支出。現有股東每股盈餘與每股現金流被攤薄。
- **GAAP 獲利含一次性與低稅率因素**：FY26 含出售業務利益 124.1M，稅率僅約 7%。GAAP trailing EPS 4.12 與調整後 5.60 有明顯差距，Q4 FY26 GAAP EPS 1.19 對比調整後 1.74 亦然。判讀獲利時應區分口徑。
- **商譽與無形資產佔總資產約 40%**：7,260.1M。有形帳面價值剛轉正（3,643.4M），若未來出現減損，帳面會再次受壓。
- **估值對前瞻兌現高度敏感**：TTM EV/EBITDA 約 37.5x 至 41.2x，GAAP P/E 70.4x，P/B 5.2x。前瞻 P/E 20.6x 的 EPS 口徑（14.05 對 9.42）需進一步確認。
- **資料不一致**：info 之 ebitda（1,423.4M）、freeCashflow（TTM -650.0M）與 operatingMargins（11.8%）與報表計算值（normalized EBITDA 1,563.6M、FY26 FCF -1,030.6M、營業利益率 12.7%）不一致。本報告以報表數字為主，info 數字僅作參考。
- **資料來源限制**：本次 Yahoo 即時連線失敗（CONNECT 403），資料來自本地快取（約 2026-10-14 11:38 至 11:41 UTC）；fast_info 之 market cap 與 50/200 日均線欄位為 null，改以 info 為準。
- **機構與空單動向**：FMR 季減 51.4%，空單佔流通股 6.56% 且月增 2.6%。Bain Capital 於 2025-11 大額賣出，後續是否仍有出售計畫待觀察。
- **高 Beta**：2.11。市場波動時股價可能放大。
- **資料缺口（DATA_UNAVAILABLE）**：分部營收、同業中位數、債務到期結構、管理層指引文字、特別股轉換條款。

(以上為基本面分析，未包含交易建議。)

FUNDAMENTALS REPORT COMPLETE
