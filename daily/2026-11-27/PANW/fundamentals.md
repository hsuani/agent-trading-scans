# Fundamentals — PANW as of 2026-11-27

資料時點說明：分析基準日 2026-11-27。價格來自 repo 快取（fast_info / info 的 regularMarketTime 對應 2026-11-25 收盤附近，快取寫入 2026-11-26 UTC 16:50），為 DATE 前一交易日價位。財報為 FY2026（會計年度截至 2026-07-31）年度與 FY27 Q1（2026-10-31 季，2026-11-18 公布）季度資料。金額以 USD 計，表格單位標於欄首（USD M = 百萬美元，USD B = 十億美元）。未與 TWD/KRW 混用。

## Executive summary
PANW 營收動能強勁（FY26 營收 11,480 M USD，年增 24.5%；FY27 Q1 單季年增 39.2%），自由現金流仍維持約 35% 營收率，且帳上為淨現金約 414 M USD。但 GAAP 獲利大幅惡化（FY26 淨利 307 M USD，較 FY25 的 1,134 M 下滑約 73%；TTM GAAP EPS 僅 0.57 USD）、SBC 占營收 15.5%、股數年增約 18%（併購發股，工具資料未揭露細節）、流動比率僅 0.66x、商譽占總資產近 46%，財務體質在併購後明顯轉弱。估值以任何 GAAP 指標衡量均屬極高（trailing P/E 約 625x、EV/EBITDA 約 180x），僅以 forward non-GAAP EPS 計算的 forward P/E 約 72x 仍明顯高於一般軟體同業估計區間，估值缺乏安全邊際。

## Revenue & profitability

**營收與成長**

| 期間 | 營收 (USD M) | 年增 |
|---|---|---|
| FY23（2023-07） | 6,892.7 | n/a |
| FY24（2024-07） | 8,027.0 | +16.5% |
| FY25（2025-07） | 9,221.0 | +14.9% |
| FY26（2026-07） | 11,480.0 | +24.5% |

- 3 年 CAGR（FY23→FY26）約 18.5%（由 yfinance 年度營收推算）。
- 季度營收序列（USD M）：Oct-25 2,474 → Jan-26 2,594 → Apr-26 3,002 → Jul-26 3,410 → Oct-26 3,445。FY27 Q1（Oct-26）年增 +39.2%（對照 Oct-25 季）。Jan-26 至 Oct-26 四季加總 12,451 M，與 info.totalRevenue 一致，TTM 數字可信。
- 2026 年 Apr 季起營收跳升，時點與 Q3 之後的股數、商譽、負債大幅變動吻合，符合併購併表的特徵。工具資料未揭露併購標的與併表貢獻，無法拆分有機成長與併購成長（DATA_UNAVAILABLE）。
- 業務組合：info.longBusinessSummary 列出 Prisma Access、Strata Cloud Manager、Prisma AIRS、Cloud 安全（CNAPP）、Cortex（XSIAM/XDR/XSOAR/Xpanse）、Unit 42 等產品線，但未提供分部或產品別營收占比。分部營收 DATA_UNAVAILABLE。

**獲利能力（GAAP，USD M）**

| 期間 | 毛利率 | 營業利益率 | EBITDA 率（reported） | 淨利率 |
|---|---|---|---|---|
| FY23 | 72.3% | 5.6% | 12.6% | 6.4% |
| FY24 | 74.3% | 8.5% | 15.9% | 32.1%（含 -1,590 M 稅務利益，非代表性） |
| FY25 | 73.4% | 13.5% | 21.1% | 12.3% |
| FY26 | 70.4% | 6.1% | 12.1% | 2.7% |
| TTM（至 Oct-26） | 69.0%（info.grossMargins 68.96%） | 3.9%（季度加總）；info.operatingMargins 為 4.95%，兩者不一致 | 季度 EBITDA 加總 1,333 M（10.7%） | 3.65%（淨利 455 M） |

- 毛利率由 FY25 73.4% 降至 FY26 70.4%，Oct-26 季降至 68.0%（2,342 / 3,445），顯示新產品組合或併購資產的成本結構拉低毛利。
- FY26 營業費用（Operating Expense）7,382 M，占營收 64.3%（FY25 為 59.9%）。
- Oct-26 季 GAAP 淨利 482 M，但稅前利潤僅 25 M，因 Tax Provision 為 -457 M（稅務利益）。此一次性稅務利益是 Oct-26 季 GAAP 獲利轉正的主因，工具資料未揭露成因（DATA_UNAVAILABLE），不應外推為經常性獲利。
- Apr-26 季（-177 M）與 Jul-26 季（-282 M）為 GAAP 淨損，2026 年 H1 獲利壓力明顯。

**ROE / ROIC**
- ROE（info.returnOnEquity，TTM）2.4%。FY26 以年末權益計算為 307 / 27,492 = 1.1%；FY25 為 1,134 / 7,824 = 14.5%。
- ROIC（估算，NOPAT = EBIT × (1 - 0.40 normalized tax)，平均投入資本）：FY26 約 1.7%（EBIT 536 M × 0.6 = 322 M；平均 IC（7,824 + 29,266）/2 = 18,545 M）；FY25 約 16.3%（EBIT 1,599 M × 0.711 = 1,137 M；平均 IC 6,979 M）。此為本報告自行估算，非工具直接輸出。
- 併購後 IC 擴大（Invested Capital 由 Jul-25 的 7,824 M 增至 Jul-26 的 29,266 M），ROIC 因分母大幅擴張而快速稀釋，後續需觀察商譽與無形資產攤銷下的真實獲利能力。

## Cashflow & balance sheet

**現金流品質（USD M）**

| 期間 | OCF | Capex | FCF | FCF 率 | FCF / NI | FCF - SBC 率 |
|---|---|---|---|---|---|---|
| FY23 | 2,777.5 | 146.3 | 2,631.2 | 38.2% | 5.98x | n/a |
| FY24 | 3,258.0 | 157.0 | 3,101.0 | 38.6% | 1.20x | n/a |
| FY25 | 3,716.0 | 247.0 | 3,469.0 | 37.6% | 3.06x | 23.6%（3,469 - SBC 1,295） |
| FY26 | 4,553.0 | 440.0 | 4,113.0 | 35.8% | 13.4x（NI 受一次性項目影響，比率失真） | 20.4%（4,113 - SBC 1,774） |
| TTM（季度 FCF 加總） | n/a | n/a | 4,268（Jan-26 384 / Apr-26 788 / Jul-26 1,254 / Oct-26 1,842） | 34.3% | n/a | n/a |

- 現金流強於獲利：FCF 率連續 4 年維持 36–39%，是 PANW 最強的基本面特徵，主因是訂閱預收款（deferred revenue）。
- 季度 FCF 加總 4,268 M 與 info.freeCashflow 4,480 M 不一致（定義差異），本報告以季度加總為主。
- SBC 占營收：FY25 14.0%，FY26 15.5%。扣除 SBC 後的 FCF 率仍有約 20%，但 SBC 是真實的股東稀釋成本。

**資產負債（Oct-26 季，USD M）**

| 項目 | Oct-26 | Oct-25 | 變化 |
|---|---|---|---|
| Cash + 短期投資（Cash Cash Equivalents And STI） | 3,055 | 4,210 | -27.4% |
| Total Debt | 2,641 | 346 | 約 7.6 倍 |
| 淨現金（Cash+STI − Total Debt） | +414 | +3,864 | 縮小約 89% |
| Current Assets | 7,450 | 7,310 | +1.9% |
| Current Liabilities | 11,356 | 7,418 | +53.1% |
| Current Ratio | 0.66x | 0.99x | 惡化 |
| Quick Ratio（info） | 0.50x | n/a | n/a |
| Working Capital | -3,906 | -108 | 惡化 |
| Total Assets | 49,110 | 23,536 | +108.7% |
| Goodwill | 22,559 | 4,567 | 約 4.9 倍 |
| Goodwill / Total Assets | 45.9% | 19.4% | 上升 |
| Tangible Book Value | -763 | 3,375 | 轉負 |
| Stockholders Equity | 28,665 | 8,665 | +230.8% |
| Debt / Equity（total debt / equity） | 0.092x（info.debtToEquity 9.46%，以 info totalDebt 2,712 計為 0.095x） | 0.040x | 上升 |
| Deferred Revenue（current + non-current） | 14,589（7,730 + 6,859） | 12,230（6,132 + 6,098） | +19.3% |

- 負債結構：Oct-26 季 current debt 1,930 M、長期負債與資本租賃 711 M。債務在一年內到期部分占比高，需留意再融資或清償安排（工具未揭露到期結構，DATA_UNAVAILABLE）。
- 利息支出：FY26 Interest Expense 為 0，淨利息收入 374 M（利息收入為現金部位帶來的收益）。利息保障倍數不適用。
- 流動比率與負營運資本主要由預收款（deferred revenue 合計約 14.6B）造成，屬於訂閱模式的非典型結構，並非典型短期償債風險；但 Cash 較去年同期減少且 current debt 上升，淨現金空間已大幅縮小。

## Capital allocation & insider signal

**資本配置（USD M）**

| 項目 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Capex | 146.3 | 157.0 | 247.0 | 440.0 |
| Capex / 營收 | 2.1% | 2.0% | 2.7% | 3.8% |
| 股票回購（Repurchase） | 272.7 | 567.0 | 0 | 1,000.0 |
| 債務償還（Repayment of Debt） | 1,692 | 1,033 | 966 | 160 |
| 股息 | 無（dividendYield 0%） | | | |

- Capex 占營收自 2.0% 升至 3.8%，與資料中心/基礎設施擴充一致，但幅度仍遠低於 FCF。
- 回購：FY26 回購 1,000 M，但期末股數仍由 667.9 M（Jul-25）增至 815.0 M（Jul-26），Oct-26 為 818.8 M，較 Oct-25 的 692.0 M 增加約 18.3%。回購完全未抵銷發股與併購發行。
- 稀釋：diluted average shares FY25 709 M → FY26 764 M（+7.8%）；Oct-26 季 diluted average shares 838 M。
- 無股息，資本配置以回購與併購為主，FCF 扣除回購與債務償還後，剩餘資金主要用於併購交易（工具未揭露交易明細，DATA_UNAVAILABLE）。

**內部人交易（最近 6 個月，2026-05-27 至 2026-11-26）**
- 公開市場賣出：20 筆，合計約 51.8 M USD，合計 149,209 股。
- 公開市場買入：0 筆。
- 淨額 -51.8 M USD，占市值（292.39 B USD）約 -0.018%，規模極小，不構成明顯的內部人看空訊號。
- 主要賣出：President William D. Jenkins Jr.（2026-11-02 約 6.5 M；2026-11-04 約 13.4 M）、CFO Dipak Golechha（2026-09-24 約 10.8 M）、Director James Joseph Goetz（2026-09-17 約 7.5 M）。
- 注意：資料未揭露是否為 10b5-1 計畫或稅務代扣，無法判斷是否為主動減持。
- 6 個月窗口外的重要事件：CEO Nikesh Arora 於 2026-03-27 公開市場買入 68,085 股，成交價區間 146.87–147.48 USD，約 10.0 M USD，為近期唯一的大額內部人買入，與目前股價（356.14）相比，該買入時點的價格低約 59%。
- 內部人持股比例（heldPercentInsiders）0.66%。

**機構持股**
- 機構持股比例（heldPercentInstitutions）約 84.2%，機構數量 4,083。
- 前十大持有人（2026-09-30 13F）：BlackRock 78.2 M 股、Vanguard Capital Management 53.3 M、State Street 37.1 M、FMR 31.9 M（季增 58.9%，明顯加碼）、Morgan Stanley 27.7 M、Invesco 27.3 M、JPMorgan 25.4 M、Geode 20.3 M、Vanguard Portfolio Mgmt 19.4 M、Bank of America 16.8 M。
- 資料異常：inst_holders 的 pctHeld 欄位（例如 BlackRock 0.8027）與 Shares 不一致；以 Shares / 821 M 股計算，BlackRock 約 9.5%、Vanguard 約 6.5%。本報告採後者，前者視為工具資料錯誤。

**空頭部位**
- Shares Short 20.03 M 股，占流通股 2.46%，Short Ratio 3.27 日；較上月 21.27 M 減少約 5.8%。

## Valuation

**估值倍數（以 USD 計）**

- 股價 356.14 USD（快取，前一交易日）。市值 292.39 B USD，企業價值（EV）292.05 B USD。股數 821 M（info.sharesOutstanding）。
- Trailing P/E：624.8x（trailingEps 0.57 USD，GAAP TTM）。
- Forward P/E：72.4x（forwardEps 4.92 USD）。epsCurrentYear 4.28 USD，對應 P/E 83.2x。forwardEps 與 consensus 之定義為 non-GAAP，與 GAAP trailing EPS 不可直接比較。
- PEG（pegRatio）11.8。
- EV / EBITDA：179.7x（info.enterpriseToEbitda，EBITDA 1,625 M）；若以季度 reported EBITDA 加總 1,333 M 計算，約 219x。
- EV / Revenue：23.5x。
- P/S（trailing）：23.5x。
- P/FCF：約 68.5x（292.39 B / 季度 FCF 加總 4,268 M）；以 info.freeCashflow 4,480 M 計為約 65.3x。
- P/B：10.2x（priceToBook，每股淨值 35.0 USD）。
- 52 週區間：139.57–432.33 USD。股價距 52 週高點 -17.6%，距低點 +155%。52 週漲跌幅 +87.3%（S&P 500 同期 +4.9%）。
- 均線：50 日均 366.18 USD（股價低於 50 日均線約 2.7%），200 日均 284.24 USD（股價高於 200 日均線約 25.3%）。
- Beta：0.97。

**分析師共識（info，51 位分析師）**
- 平均目標價 412.12 USD（相對現價 +15.7%）；中位數 425 USD；最高 510 USD；最低 190 USD。
- 推薦平均值 1.63（1 = Strong Buy，5 = Sell），key 為 buy。
- 此為共識資料彙整，不構成本報告的交易建議。

**與同業中位數比較（估計）**
- 工具未提供同業中位數，以下為本報告估計的一般大型軟體/資安基礎設施區間，非資料直接輸出：forward P/E 35–45x、EV/EBITDA 30–40x、P/FCF 30–35x、P/S 8–12x、P/B 5–8x。
- PANW 在 trailing 指標上為極端高值，在 forward non-GAAP 指標上仍高於估計同業區間約 60–100%；估值以高成長預期為前提，對 GAAP 獲利回升的依賴度高。

## Key catalysts

- 最近一次財報：2026-11-18（FY27 Q1，Oct-26 季）。non-GAAP EPS 實際 1.05 USD，預估 0.97 USD，驚喜 +8.21%。過去 20 季財報中，EPS 幾乎全數超越預期（驚喜幅度多為 +3%–+12%）。
- 下一次財報：2027-02-16（yfinance 標示為估計日期，isEarningsDateEstimate = true），EPS 預估 1.01 USD。
- 最近兩季 FCF 與營收動能：FY27 Q1 營收 3,445 M、FCF 1,842 M，為 TTM 內最高單季 FCF。
- 併購整合：商譽由 Jan-26 的 6,931 M 升至 Oct-26 的 22,559 M，股數與負債同步大增。併購整合進度、綜效、與無形資產攤銷，是後續 GAAP 獲利能否回升的關鍵。工具未揭露交易細節（DATA_UNAVAILABLE）。
- 公司指引（guidance）：工具未提供 FY27 營收或 EPS 指引數字（DATA_UNAVAILABLE）。
- 分部或產品別營收占比：DATA_UNAVAILABLE。

## Metrics table

營收、獲利、現金流、資產負債欄位單位為 USD M（除非另標示）；市值與企業價值為 USD B。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue, TTM（USD M） | 12,451 | Oct-26 季 +39.2% | 約 12%–18%（估計成長率） | 強 |
| Revenue, FY26（USD M） | 11,480 | +24.5% | 約 12%–18% | 強 |
| Gross margin, TTM | 69.0% | FY26 70.4%，FY25 73.4%（-3.0 pt） | 約 75%–80%（non-GAAP 估計） | 偏弱 |
| Operating margin, FY26（GAAP） | 6.1% | FY25 13.5% | 約 15%–25%（non-GAAP 估計） | 弱（GAAP） |
| Net margin, FY26（GAAP） | 2.7% | FY25 12.3% | 約 10%–15% | 弱 |
| ROE, TTM（info） | 2.4% | FY25 14.5%（年末權益計算） | 約 10%–20% | 弱 |
| ROIC, FY26（本報告估算） | 1.7% | FY25 16.3% | 約 10%–15% | 弱 |
| FCF margin, FY26 | 35.8% | FY25 37.6% | 約 25%–30% | 強 |
| FCF / NI, FY26 | 13.4x（NI 受一次性影響） | FY25 3.06x | >0.9 為健康 | 強（但 NI 失真） |
| FCF - SBC margin, FY26 | 20.4% | FY25 23.6% | 約 15%–20% | 中性 |
| SBC / Revenue, FY26 | 15.5% | FY25 14.0% | 約 8%–10% | 紅旗 |
| Current ratio, Oct-26 | 0.66x | Oct-25 0.99x | 約 1.5x | 偏弱（deferred revenue 結構性） |
| Net cash, Oct-26（USD M） | +414 | Oct-25 +3,864 | 視同業 | 縮小 |
| Debt / Equity, Oct-26 | 0.09x | Oct-25 0.04x | 約 0.3x–0.5x | 低，但上升 |
| Goodwill / Total Assets, Oct-26 | 45.9% | Oct-25 19.4% | 約 10%–25% | 紅旗 |
| Tangible Book Value, Oct-26（USD M） | -763 | Oct-25 +3,375 | 正值 | 紅旗 |
| Capex / Revenue, FY26 | 3.8% | FY25 2.7% | 約 3%–5% | 中性 |
| Buyback, FY26（USD M） | 1,000 | FY25 0 | 視同業 | 中性（未抵銷稀釋） |
| Shares outstanding, Oct-26（M） | 818.8 | Oct-25 692.0（+18.3%） | 約 0%–2%/年 | 紅旗 |
| Dividend yield | 0% | 0% | 約 0.5%–1% | 無股息 |
| Trailing P/E（GAAP） | 624.8x | n/a | 約 40x | 極高 |
| Forward P/E（non-GAAP） | 72.4x | n/a | 約 35x–45x | 偏高 |
| EV / EBITDA（info） | 179.7x | n/a | 約 30x–40x | 偏高 |
| P / FCF（TTM） | 68.5x | n/a | 約 30x–35x | 偏高 |
| P / S（trailing） | 23.5x | n/a | 約 8x–12x | 偏高 |
| P / B | 10.2x | n/a | 約 5x–8x | 偏高 |
| Market cap（USD B） | 292.4 | n/a | n/a | n/a |
| Insider net, 6 mo（USD M） | -51.8（0 筆買入） | n/a | n/a | 中性偏空，規模小（-0.018% 市值） |
| Short interest, % float | 2.46%（Short Ratio 3.27 日） | 上月 -5.8% | 約 3%–5% | 低 |
| Analyst mean target（USD） | 412.12（+15.7% vs 現價） | n/a | n/a | 共識 Buy（1.63） |
| Next earnings | 2027-02-16（估計） | n/a | n/a | n/a |
| Guidance FY27 | DATA_UNAVAILABLE | n/a | n/a | n/a |
| Segment revenue mix | DATA_UNAVAILABLE | n/a | n/a | n/a |

## Red flags

- GAAP 獲利大幅惡化：FY26 淨利 307 M USD（-73% YoY），營業利益率 6.1%（FY25 13.5%），Apr-26 與 Jul-26 兩季為 GAAP 淨損。Oct-26 季獲利轉正主要依賴 -457 M 的稅務利益（成因 DATA_UNAVAILABLE），非經常性獲利。
- SBC 占營收 15.5%，且 FY26 的 SBC 較 FY25 增加 37%；股東稀釋成本高。
- 股數年增約 18%，FY26 回購 1,000 M 未抵銷稀釋，淨股東價值成長受壓。
- 商譽占總資產 45.9%，有形淨值 -763 M，後續若併購資產減損或攤銷上升，GAAP 獲利可能再受衝擊。
- 流動比率 0.66x、負營運資本 -3.9 B；淨現金由 3.9 B（Oct-25）降至 0.4 B；current debt 1.93 B 上升，需留意到期結構與再融資條件。
- 估值極高：trailing P/E 約 625x、EV/EBITDA 約 180x、P/FCF 約 68x；forward P/E 72x 亦明顯高於估計同業區間。
- 毛利率連續兩年下滑（FY25 73.4% → FY26 70.4%，Oct-26 季 68.0%），需確認是否為併購資產或雲端產品結構所致。
- 短期股價動能與基本面背離：52 週上漲 +87%，但股價距 52 週高點 -17.6%，且 Jul-26 至 Oct-26 期間 GAAP 盈利與估值未同步改善。
- 資料一致性風險（本報告以季度加總為主，已標示差異）：
  - TTM 營業利益：季度加總 482 M（3.9%）vs info.operatingMargins 4.95%（約 616 M）。
  - TTM EBITDA：季度 reported 加總 1,333 M vs info.ebitda 1,625 M。
  - TTM FCF：季度加總 4,268 M vs info.freeCashflow 4,480 M。
  - TTM EPS：info.trailingEps 0.57 vs 季度 diluted EPS 加總 0.61；earnings_dates 的 Reported EPS（1.05）為 non-GAAP，與 income statement 的 GAAP EPS 不可直接比較。
  - FY24 淨利 2,578 M 含 -1,590 M 稅務利益，FY24 獲利率不具代表性。
  - inst_holders 的 pctHeld 與 Shares 不一致（見機構持股段）。
  - Jul-26 季 quarterly_fin 的 Operating Income（172 M）與 EBIT（-269 M）方向不同，需以 10-K/10-Q 核對。
- 資料缺口（DATA_UNAVAILABLE）：FY27 指引、分部營收、併購標的與對價結構、Oct-26 季稅務利益成因、債務到期結構、同業中位數（工具未提供，本報告所列為估計）。

FUNDAMENTALS REPORT COMPLETE
