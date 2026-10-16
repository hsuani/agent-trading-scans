# Fundamentals — SYM (Symbotic Inc.) as of 2026-10-16

## Executive summary
Symbotic 的營收規模與成長仍強（FY2025 營收 2,246.9M USD，較 FY2024 +25.6%；最近一季 FY26 Q3 (2026-06) YoY +21.7%），毛利率已由 2025-06 季的 18.9% 升至 2026-06 季的 22.3%，但 GAAP 獲利仍接近損益兩平（TTM 淨利約 12.6M USD，TTM 營業利益率約 1.2%）。財務體質上以約 1.75B USD 現金與極低金融負債（total debt 25.8M USD）為主要支撐，但 FCF 高度依賴客戶預收款與營運資本變動，最近一季 FCF 轉為負值（-164.6M USD），且近九個月股本稀釋約 14%。估值上 forward P/E 約 51.5x、PEG 約 4.7、EV/EBITDA 約 68x，相對工業機械同業估計中位數明顯偏貴；股價 39.76 USD 接近 52 週低點（36.47–87.88），做空比率（short % of float）31.8%，分析師平均目標價 62.86 USD。財務健康度評為「現金充裕但獲利與現金流品質待驗證」，估值相對同業偏高。

資料基準：最新快取報價 39.76 USD（由 regularMarketTime 推算約為 2026-10-15 收盤）；財報為 FY2025 年報（期末 2025-09-30）與 2026-06 季報；內部人交易截至 2026-10-05。未發現晚於 2026-10-16 的資料。yfinance 快取 source 皆為 cache，依指示視為正常。

## Revenue & profitability

**營收與成長**
- 年度營收（USD）：FY2022 593.3M → FY2023 1,176.9M (+98.4%) → FY2024 1,788.2M (+52.0%) → FY2025 2,246.9M (+25.6%)。
- 3 年 CAGR（FY2022→FY2025）約 55.9%；成長率逐年收斂，由 +98% 降至 +26%。
- 季營收序列（USD）：2025-06 592.1M → 2025-09 618.5M → 2025-12 630.0M → 2026-03 676.5M → 2026-06 720.8M。TTM 營收 2,645.8M（與 info totalRevenue 一致）。
- 最近一季 YoY：2026-06 季 720.8M vs 2025-06 季 592.1M，+21.7%（與 info revenueGrowth 0.217 一致）。QoQ 連續四季成長，2026-03 與 2026-06 兩季加速（+7.4%、+6.5%）。
- 分部（segment）資料：工具未提供 segment 拆分，標示 DATA_UNAVAILABLE。客戶集中度亦 DATA_UNAVAILABLE。

**毛利 / 營業 / 淨利率**
- 毛利率（年）：FY2022 16.8% → FY2023 16.1% → FY2024 13.7% → FY2025 18.8%。
- 毛利率（季）：2025-06 18.9%、2025-09 20.6%、2025-12 21.2%、2026-03 22.2%、2026-06 22.3%，連續上升，為近期最重要的正向訊號。TTM 毛利率約 21.6%（以季度加總計算）；info grossMargins 為 21.3%。
- 營業利益率（年）：FY2022 -23.6%（-140.4M）→ FY2023 -19.0% → FY2024 -6.5% → FY2025 -4.1%（營業利益 -92.1M）。
- 營業利益率（季）：2025-09 -2.5%、2025-12 1.5%、2026-03 0.9%、2026-06 4.6%（營業利益 32.9M），最新季首次達到較明顯正值。TTM 營業利益約 32.9M，營業利益率約 1.2%；info operatingMargins 為 4.6%（口徑差異，見紅旗）。
- 淨利率：FY2025 -0.8%（淨利 -16.9M）；TTM 淨利約 12.6M（季度加總），淨利率約 0.5%；info profitMargins 0.31%。
- 費用結構（FY2025）：R&D 216.0M（占營收 9.6%），SG&A 298.7M（占營收 13.3%）。最近一季（2026-06）R&D 43.8M、SG&A 84.2M，SG&A 較前一季 92.6M 下降。
- ROE：info returnOnEquity 4.39%；ROA 0.32%。
- ROIC：DATA_UNAVAILABLE（淨現金規模大、非控制權益規模大，以工具資料無法得到可信的投入資本口徑，不硬算）。
- 非控制權益（minority interest）：FY2025 為 261.9M USD，占總權益比重大，歸屬母公司的獲利與權益需以此調整；工具未說明其來源。

**EPS 口徑**
- GAAP 稀釋後 EPS（quarterly_fin）：2025-06 -0.05、2025-09 -0.03、2025-12 0.02、2026-06 0.09；FY2025 -0.16。
- earnings_dates 的 Reported EPS 為 0.41（2026-08-05）、0.45（2026-05-06）、0.40（2026-02-04）、0.58（2025-11-24），顯示與 GAAP 口徑不同（疑似調整後/非 GAAP），本報告以 GAAP 為準做獲利判斷。

## Cashflow & balance sheet

**現金流量**
- 營業現金流（OCF）：FY2022 -148.2M、FY2023 +230.8M、FY2024 -58.1M、FY2025 +866.9M。
- 資本支出（capex）：FY2022 18.0M、FY2023 21.3M、FY2024 44.4M、FY2025 79.0M（年增 +78%）；TTM capex 約 99.0M，占營收約 3.7%。
- 自由現金流（FCF = OCF - capex）：
  - FY2025：OCF 866.9M - capex 79.0M = 787.9M（yfinance annual FCF 787.9M）。
  - 季度（2025-09 至 2026-06）：494.4M、189.5M、218.0M、-164.6M，TTM 合計 737.3M，TTM FCF margin 約 27.9%。
  - info freeCashflow 為 547.6M（FCF margin 約 20.7%），與季度加總有明顯差距，兩者並列供參考。
- FCF / NI：
  - FY2025 NI 為 -16.9M，比值無意義（n/m）。
  - TTM：737.3M / 12.6M ≈ 58x，數值遠超 0.9 的健康門檻，但分母極小，比值失真，不宜作為品質證據。
- 現金流品質判斷：FCF 主要來自營運資本，FY2025 營運資本變動貢獻 +714.0M（其中 other working capital +583.4M），與客戶預收款（current deferred revenue FY2025 1,242.3M，較 FY2024 676.3M 增加 83.7%）及應付帳款增加有關。2026-06 單季 OCF -147.3M、Change in Working Capital -252.6M，應收增加 -155.9M，顯示現金流仍不穩定。
- 股票酬償（SBC）：FY2025 183.9M（占營收 8.2%）；TTM 約 207.2M（占營收 7.8%）。若將 SBC 視為真實成本，FCF 含 SBC 後的有效獲利能力明顯縮水。

**資產負債表（2026-06 季末）**
- 現金及約當現金：1,746.4M USD（2025-09 為 1,245.0M；2026-03 為 2,009.4M，本季減少約 263M）。每股現金 13.45 USD，約占現價 34%。
- 總負債（financial debt）：25.8M USD（info totalDebt）。淨現金約 1,720.6M USD（1,746.4M - 25.8M）。
- 總資產 3,524.1M；總負債（不含非控制權益）2,390.2M；股東權益（stockholders equity）708.8M。
- 流動比率（current ratio）1.331、速動比率（quick ratio）1.162（info）。流動資產 2,857.8M、流動負債 2,147.1M，與 info 一致。營運資金 710.7M（2025-12 為 674.5M）。
- 應收帳款（含其他應收）：748.4M，較 2025-12 的 357.2M 增加約 109%，較前季增加 162.8M。以季營收粗估 DSO 約 94 天（2025-12 季估約 52 天），為現金流的關鍵觀察點。
- 存貨：220.8M（2025-12 為 183.7M，+20%）。
- 淨廠房與設備（Net PPE）：158.6M（2025-06 為 73.0M，成長顯著）。
- 商譽與無形資產：143.1M；FY2025 收購現金流出 141.8M（Purchase of Business）。
- 負債權益比（debt/equity）：2.278（info）。因財務負債極小，此比率主要反映營運負債（客戶預收款、應付款）而非利息負債。
- 償債能力：財務負債壓力極低，流動性以現金支撐，短期無償債風險。

## Capital allocation & insider signal

**資本配置**
- 股利：無（dividendYield 0.0%，payoutRatio 0.0%）。
- 買回：工具資料未顯示 repurchase 紀錄，視為無實質買回。
- 股權籌資與稀釋：FY2024 籌資 258.0M；2025-12 季籌資 424.4M（Common stock issuance）。流通股數由 FY2025-09 的 112.6M 增至 2026-06 的 128.9M，約 +14.4%（9 個月）；diluted average shares 2026-06 季為 133.3M。
- 資本支出：FY2025 capex 79.0M，較 FY2024 上升 78%，最近兩季 capex 波動大（2026-03 43.4M、2026-06 17.3M），擴張節奏不穩。
- 股利覆蓋率：不適用（無股利）。

**內部人與大股東交易（2026-04-16 至 2026-10-16，6 個月）**
- 買入：0 筆、0 股。
- 賣出：28 筆、合計 5.82M 股、約 293.4M USD。
- 其中 SoftBank Group Corp（10% 以上大股東，非董監事）於 2026-05-27 以 50.42 USD 賣出 5.59M 股，約 281.8M USD，占 6 個月賣出金額約 96%。
- 扣除 SoftBank 後，董監事與高階主管賣出約 0.23M 股、約 11.6M USD（主要為 CTO James Kuffner、CFO Izilda Martins、Director Todd Krasnow、Charles Kane 等）。例如 CFO Martins 於 2026-07-27 以 40.80 USD 賣出 27,463 股（約 1.12M USD）。
- 相對市值（以 nonDilutedMarketCap 5.67B 計）：全部賣出約 5.2%；扣除 SoftBank 約 0.2%。
- 另有 13 筆交易文字欄位空白（如 Kuffner、Alexander、Boyd、Freve 等），性質未確認，推測為 RSU 歸屬或稅務扣繳，未計入賣出統計。
- 解讀：內部人與管理層未見買入，賣出規模主要來自 SoftBank 單一大宗減持；扣除後內部人賣壓輕微。

**持股結構**
- 內部人持股 13.6%，機構持股 79.4%（機構家數 552；機構佔流通股 91.9%）。
- 做空：short interest 17.69M 股，占流通股 31.8%，short ratio 10.6 天；前月為 16.84M 股，月增約 5.1%。高做空比率意味著股價波動與軋空風險並存。

## Valuation

**估值倍數（現價 39.76 USD）**
- 市值：info marketCap 為 24.07B，但 impliedSharesOutstanding 為 605M，與 sharesOutstanding 129.9M 不符，判定為資料異常，本報告不採用。以 nonDilutedMarketCap 5.67B（約 39.76 × 129.9M = 5.16B）為參考，區間約 5.2–5.7B。
- 企業價值（EV）：info enterpriseValue 3.87B；以 5.67B 市值計算約 3.95B。
- Trailing P/E：497x（TTM EPS 0.08，n/m）。
- Forward P/E：51.5x（forwardEps 0.7716）；FY2026 current-year EPS 0.569，對應 P/E 約 69.8x。
- PEG：4.68（info pegRatio）。
- EV/EBITDA：68.4x（EBITDA TTM 56.5M，info）。
- EV/Revenue：1.46x（info enterpriseToRevenue）。
- P/S（TTM）：以 5.67B 市值計約 2.1x（info priceToSalesTrailing12Months 9.10 因市值口徑異常，不採用）。
- P/FCF：以 5.67B 市值計，TTM FCF 737.3M 時約 7.7x；info FCF 547.6M 時約 10.4x。
- P/B：7.23x（每股淨值 5.497 USD）。

**與同業比較**
- 同業中位數為本報告估計值（非工具資料）：Specialty Industrial Machinery / 工業自動化 forward P/E 約 25x、EV/EBITDA 約 18x、P/S 約 2.5x、P/FCF 約 20x、P/B 約 3x、毛利率約 30%、營業利益率約 10%、ROE 約 12%。
- SYM 在 forward P/E、EV/EBITDA、P/B 皆明顯高於估計中位數；P/S 與 P/FCF 因營收規模與 FCF 波動，看似低於同業但品質不對等。

**分析師預期**
- 分析師家數 14；recommendationMean 2.29（info averageAnalystRating 2.3 - Buy）。
- 目標價：平均 62.86 USD、中位數 67.5 USD、最高 85.0 USD、最低 38.0 USD。平均目標價較現價高約 58%；最低目標價低於現價約 4%。

**價格位置與技術背景（基本面視角）**
- 52 週區間 36.47–87.88；現價位於區間低端，較 52 週高點下跌約 54.8%，52 週變動 -44.7%。
- 50 日均線 41.93、200 日均線 49.76，現價低於兩條均線。
- beta 1.973，波動度高。

## Key catalysts
- 下次財報：yfinance 估計 2026-11-16（EPS 估計 0.16），為財年第四季（FY2026 Q4）。前一季（2026-08-05）報告 EPS 0.41（口徑見上）、估計 0.13。
- 近四季財報 EPS 皆大幅超出市場估計（surprise 由 +218.5% 至 +665.5%），但 surprise 基準為低估計值，且 yfinance EPS 口徑與 GAAP 不一致，需保留判讀空間。
- 營運指引（guidance）：工具資料未提供 management guidance，標示 DATA_UNAVAILABLE。
- 關鍵觀察：(1) 季營收能否維持 YoY 20% 以上成長；(2) 毛利率能否續升至 22% 以上；(3) 應收帳款與客戶預收款的變化是否帶動 OCF 轉正；(4) SoftBank 後續持股動向；(5) 做空比率能否回落。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (TTM, USD) | 2,645.8M | 最近季 YoY +21.7% | n/a（同業估計 成長約 8%） | 成長強，但減速 |
| Revenue growth YoY（FY） | FY2025 +25.6% | FY2024 +52.0% | 約 8% | 高於同業，持續收斂 |
| Revenue 3Y CAGR（FY22–FY25） | 約 55.9% | n/a | 約 8% | 高成長，基期效應 |
| Gross margin（最近季） | 22.3% | 2025-06 季 18.9%（+3.4pt） | 約 30% | 改善中，仍低於同業 |
| Gross margin（FY2025） | 18.8% | FY2024 13.7%（+5.1pt） | 約 30% | 改善，仍偏低 |
| Operating margin（TTM） | 約 1.2% | FY2025 -4.1% | 約 10% | 接近轉正，尚未穩定 |
| Operating margin（最近季） | 4.6% | 2025-06 季 -1.6% | 約 10% | 首次明顯正值 |
| Net margin（TTM） | 約 0.5% | FY2025 -0.8% | 約 6% | 薄弱 |
| ROE | 4.39% | n/a | 約 12% | 偏低 |
| ROIC | DATA_UNAVAILABLE | n/a | 約 10% | 無法可靠計算 |
| FCF（TTM，季度加總） | 737.3M | FY2025 787.9M | n/a | 規模大但不穩 |
| FCF margin（TTM） | 27.9%（info 口徑 20.7%） | n/a | 約 10% | 高，但依賴營運資本 |
| FCF / NI（TTM） | 約 58x | FY2025 n/m（NI 為負） | 約 1.0x | n/m，不可作為品質證據 |
| OCF（最近季 2026-06） | -147.3M | 2026-03 季 +261.3M | n/a | 季度波動大 |
| Capex / Revenue（TTM） | 約 3.7% | FY2025 3.5%（FY2024 2.5%） | 約 4% | 合理，擴張中 |
| SBC / Revenue（TTM） | 約 7.8% | FY2025 8.2% | 約 3% | 偏高，稀釋壓力 |
| Net cash | 約 1,720.6M | 2025-09 約 1,245M（現金） | n/a | 充裕 |
| Current ratio | 1.331 | n/a | 約 2.0 | 偏低，但可接受 |
| Quick ratio | 1.162 | n/a | 約 1.2 | 中性 |
| Debt / Equity（info） | 2.278 | n/a | 約 0.5 | 偏高，主因營運負債 |
| Receivables（季末） | 748.4M | 2025-12 357.2M（+109% QoQ） | n/a | 警示 |
| Share count（outstanding，季末） | 128.9M | 2025-09 112.6M（+14.4%） | n/a | 稀釋明顯 |
| Trailing P/E | 497x | n/a | 約 25x | n/m |
| Forward P/E | 51.5x | n/a | 約 25x | 明顯偏貴 |
| EV/EBITDA | 68.4x | n/a | 約 18x | 明顯偏貴 |
| P/S（TTM，以 5.67B 市值） | 約 2.1x | n/a | 約 2.5x | 略低於估計中位數 |
| P/FCF（TTM） | 約 7.7x（info FCF 口徑 10.4x） | n/a | 約 20x | 表面便宜，需扣除營運資本因素 |
| P/B | 7.23x | n/a | 約 3x | 明顯偏貴 |
| PEG | 4.68 | n/a | 約 1.5 | 偏貴 |
| Dividend yield | 0.0% | n/a | 約 1.5% | 無股利 |
| Insider net flow（6M） | 賣出 293.4M（扣除 SoftBank 約 11.6M） | n/a | n/a | 大宗減持集中於 SoftBank |
| Short % of float | 31.8% | 前月 short 股數 +5.1% | 約 3–5% | 極高，軋空與波動風險 |
| Beta | 1.973 | n/a | 約 1.0 | 高波動 |
| Analyst mean target | 62.86 USD（現價 +58%） | n/a | n/a | 上行空間依分析師假設 |

## Red flags
- 獲利薄弱：TTM 淨利僅約 12.6M USD，GAAP 營業利益率僅約 1.2%，EV/EBITDA 達 68x，獲利能力與估值嚴重不匹配。
- FCF 品質存疑：FY2025 FCF 高度依賴營運資本（+714.0M），客戶預收款大增；最近一季 OCF -147.3M、FCF -164.6M。
- 應收帳款急增：季末 748.4M，較前季 +162.8M，較 2025-12 +109%，粗估 DSO 約 94 天。
- 股權稀釋：流通股數 9 個月增加約 14.4%，2025-12 季籌資 424.4M；SBC TTM 約 207M，占營收約 7.8%。
- 大股東減持：SoftBank 於 2026-05-27 以 50.42 USD 賣出 5.59M 股（約 281.8M USD），目前股價已較該價格下跌約 21%。
- 做空比率極高：short % of float 31.8%，short ratio 10.6 天，且月增加；波動與軋空風險並存。
- 股價趨勢偏弱：52 週跌幅 -44.7%，現價低於 50 日與 200 日均線，接近 52 週低點。
- 資料口徑不一致：
  - info marketCap 24.07B 與 nonDilutedMarketCap 5.67B 差距明顯（implied shares 605M），影響 P/S 與 EV 計算。
  - info freeCashflow 547.6M 與季度 FCF 加總 737.3M 不一致。
  - info operatingMargins 4.6%（TTM）與季度加總 1.2% 不一致。
  - EPS 報告口徑（yfinance Reported EPS）與 GAAP 稀釋 EPS 不一致。
- 流動性指標偏緊：current ratio 1.33、quick ratio 1.16，對比同業估計中位數偏低。
- 非控制權益規模大（FY2025 261.9M），歸屬母公司的經濟價值需扣除。
- 資料缺口：segment 拆分、客戶集中度、management guidance、ROIC、repurchase 明細均為 DATA_UNAVAILABLE；無法評估收入來源集中風險。
- 屬性提示：13 筆交易文字欄位空白，性質未確認；SBC 與 RSU 歸屬可能造成申報賣出的表面數字與實際出售意圖不一致。

FUNDAMENTALS REPORT COMPLETE
