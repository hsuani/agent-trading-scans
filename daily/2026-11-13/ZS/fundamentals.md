# Fundamentals — ZS (Zscaler, Inc.) as of 2026-11-13

資料來源聲明：本次所有 yfinance 查詢均因即時 feed 連線失敗（Cookie/crumb ConnectionError），自動回退至 repo cache `prices/yf/ZS.json`（`_refreshed_at` 2026-11-12T15:07:27Z）。報告內所有數字均標示 source: cache。未使用任何晚於 2026-11-13 的資料。財年終為 7 月底（FY26 = 2025-08 至 2026-07）。金額單位：USD B / USD M（本報告不使用億）。

## Executive summary

ZS 基本面為「高成長、高毛利、現金流為正，但仍屬 GAAP 虧損」：FY26 營收 USD 3.35B（YoY +25.4%），毛利率 76.8%，FCF USD 779M（FCF margin 23.2%），現金及短期投資 USD 3.47B。然而 GAAP 淨損 USD -63M，SBC（USD 822M）已超過 FCF，股權稀釋 3.0%，財務健康度尚可但品質有保留。估值方面，以 189.09 USD、市值 USD 30.8B 計，P/S 9.2x、forward P/E 33.6x、P/FCF 39.6x，相對成長率屬偏高估值區間（估計），分析師平均目標價 USD 235 (+24%)。

## Revenue & profitability

- **營收**：FY23 USD 1.617B → FY24 USD 2.168B → FY25 USD 2.673B → FY26 USD 3.353B。YoY 分別為 +34.1%、+23.3%、+25.4%。3 年 CAGR（FY23→FY26）約 27.5%，成長並未明顯減速。
- **季度動能**：FY26 各季營收 USD 788.1M（10 月季）、815.8M（1 月季）、850.5M（4 月季）、898.2M（7 月季）；7 月季 YoY 約 +24.9%（對比 FY25 7 月季 USD 719.2M），QoQ 約 +5.6%。
- **營收組合**：yfinance 未提供分部營收，僅有 longBusinessSummary 之產品描述（Zero Trust SASE、ZIA、ZPA、Data Security、Security for AI、Agentic SecOps 等）。分部營收占比：DATA_UNAVAILABLE。
- **毛利率**：FY24 78.0% → FY25 76.9% → FY26 76.8%；Q4 FY26 為 76.7%。毛利率略有下滑，但幅度極小。
- **營業利益（GAAP，Operating Income 列）**：FY23 USD -234.6M（-14.5%）、FY24 USD -121.5M（-5.6%）、FY25 USD -127.1M（-4.8%）、FY26 USD -121.1M（-3.6%）。營業虧損占比持續收斂，但絕對金額仍為負。FY26 另一列「Total Operating Income As Reported」為 USD -133.3M，兩列數字不一致，本報告以 Operating Income 列為準並標示此差異。
- **費用結構（FY26，占營收）**：R&D USD 903.4M（26.9%）、S&M USD 1,473.7M（44.0%）、G&A USD 303.3M（9.0%）。SBC USD 821.9M，占營收 24.5%（FY25 為 24.7%）。
- **淨利（GAAP）**：FY23 USD -202.3M（-12.5%）、FY24 USD -57.7M（-2.7%）、FY25 USD -41.5M（-1.6%）、FY26 USD -63.2M（-1.9%）。Q4 FY26 淨損收斂至 USD -3.4M（Q4 FY25 為 USD -17.6M）。
- **所得稅異常**：FY26 稅前損失 USD -17.1M，但稅費 USD +46.0M，有效稅率不具意義（n/m）。淨利息收入 USD 124.3M 為獲利主要緩衝來源。
- **非 GAAP EPS**：earnings_dates 顯示最近 4 季 Reported EPS 分別為 USD 1.19（FY26 Q4）、1.08、1.01、0.96；屬非 GAAP 口徑，與 GAAP 淨損需分開解讀。
- **ROE**：FY26 -2.9%（info returnOnEquity -0.0287；以 NI / 平均權益計算）；FY25 約 -2.7%。
- **ROIC（估計）**：以 Operating Income / 平均 Invested Capital（(4294.6+3500.0)/2）計算，約 -3.1%（稅前估計值，非 yfinance 欄位）。

## Cashflow & balance sheet

**現金流**
- **營業現金流（OCF）**：FY23 USD 462.3M → FY24 USD 779.8M → FY25 USD 972.5M → FY26 USD 1,129.7M（YoY +16.2%）。
- **自由現金流（FCF = OCF - Capex）**：FY23 USD 333.6M → FY24 USD 585.0M → FY25 USD 726.7M → FY26 USD 779.1M（YoY +7.2%）。FCF margin 依序為 20.6%、27.0%、27.2%、23.2%，FY26 下滑約 4.0 個百分點。
- **Capex**：FY26 USD -350.5M（占營收 10.5%），FY25 USD -245.8M（9.2%）、FY24 USD -194.9M（9.0%）、FY23 USD -128.7M（8.0%）。Q4 FY26 單季 Capex 高達 USD -218.5M（Q4 FY25 為 USD -78.7M），FCF 逐季為 USD 413.3M（FY26 Q1）、169.1M（Q2）、136.0M（Q3）、60.8M（Q4），末季大幅下滑。
- **FCF / NI**：因 GAAP 淨損，比值 n/m。替代指標：FCF / SBC = 779.1 / 821.9 = 0.95。
- **FCF - SBC**：FY26 為 USD -42.8M（FY25 為 USD +65.3M），表示以股權報酬計算的自由現金流為負。
- **營運資金**：FY26 Change in Working Capital USD -97.6M；應收帳款增加 USD -140.0M（CF 列）。

**資產負債表（FY26 期末，2026-07-31）**
- **現金與投資**：Cash & Cash Equivalents USD 928.4M；Cash + Short-term investments USD 3,474.2M（FY25 為 USD 3,572.4M）。
- **總債務**：USD 1,855.8M（FY25 USD 1,796.6M，+3.3%）。其中長期債務 USD 1,696.4M（主要為可轉換債，性質以 10-K 為準，本工具未提供票面細節）。FY25 曾發行 USD 1,725M 並償還 USD 1,150M。
- **淨現金（自算）**：Cash+STI − Total Debt = USD 3,474.2M − 1,855.8M = **USD +1,618.4M**（FY25 為 USD +1,775.8M，-8.9%）。
- **Net Debt（yfinance 欄位）**：USD 768.0M。此數字與上述自算結果（淨現金 USD 1.62B）方向相反，定義不明（可能含租賃或其他項目），**本報告不採用**，列為資料品質問題。
- **流動比率**：1.70（info currentRatio 1.699；FY25 為 2.01）。速動比率 1.57。營運資金 USD 2,069.9M（FY25 USD 2,464.7M）。
- **負債權益比**：0.71x（total debt / equity；info debtToEquity 為 71.9%）；FY25 約 1.00x。
- **遞延收入（流動）**：USD 2,480.5M，YoY +20.8%（FY25 USD 2,054.4M）。為訂閱制預收款的主要指標，成長速度與營收相當。
- **應收帳款**：USD 1,149.1M，YoY +15.8%，慢於營收成長，無明顯收款惡化跡象。
- **商譽與無形資產**：Goodwill USD 1,218.1M（FY25 USD 417.7M）、無形資產 USD 214.4M（FY25 USD 47.3M）。FY26 Purchase of Business 現金支出 USD 918.1M，屬併購擴張。個別被併購公司名稱與價格：DATA_UNAVAILABLE。
- **股東權益**：USD 2,598.3M（FY25 USD 1,799.3M）；Retained Earnings USD -1,252.7M（累積虧損）。

## Capital allocation & insider signal

**資本配置**
- **股票回購**：現金流量表中無 repurchase 列，FY23–FY26 未見回購。
- **股息**：dividendYield 0.0，未配息。
- **股權稀釋**：流通股數由 FY25 158.3M 增至 FY26 163.1M，**+3.0%**；FY26 稀釋後平均股數 160.2M（FY25 154.4M，+3.8%）。SBC 以股換酬造成持續稀釋。
- **股票選擇權行使收入**：FY26 USD 63.4M（FY25 USD 67.1M）。
- **併購**：FY26 USD 918.1M 現金併購支出（占 FY26 OCF 81%），為本年資本配置最大項目。
- **Capex 趨勢**：占營收由 8.0%（FY23）升至 10.5%（FY26），資本支出加速。

**內部人交易（過去 6 個月，2026-05-13 至 2026-11-13）**
- 共 28 筆 insider 紀錄（in window），其中 **23 筆為 open-market "Sale"，合計 USD 14.94M（79,666 股）**；**0 筆 open-market 買入**。另有 option conversion 合計 USD 5.35M、RSU/stock award（無現金價值）若干筆。
- 淨買賣：淨賣出 USD 14.94M，占市值（USD 30.83B）**0.048%**，幅度極小。
- 主要賣方（Sale 金額）：Adam Geller（CPO）USD 8.57M；Kevin Rubin（CFO）USD 2.13M；Robert Schlossman（CLO）USD 1.94M；Michael Rich USD 1.32M；Jagtar Singh Chaudhry（CEO）USD 0.91M；James Beer（董事）USD 0.06M。
- 觀察：2026-09-16 於 USD 192.76 同日多位高管同價賣出（CEO、CFO、CLO、Rich），疑為 sell-to-cover 或 10b5-1 計畫；工具資料無法確認交易性質，列為待確認。
- 最近一筆：2026-11-02 Adam Geller 以 USD 238.00 賣出（USD 247,758），同日伴隨 option conversion，為近期賣壓紀錄；其價位高於目前 189.09。
- 持股集中度：insider 持股 34.68%（共同創辦人兼 CEO Jagtar Singh Chaudhry 為主要內部人），機構持股 53.42%（1,231 家），機構持股分散。前三大機構：BlackRock 6.07%、Vanguard Portfolio Management 3.80%、Vanguard Capital Management 2.90%。
- 治理風險評分（info）：overallRisk 7、boardRisk 8、shareHolderRightsRisk 8（1–10 分，越高越差）。

## Valuation

以 info.currentPrice 189.09 USD（cache, 2026-11-12）計算。fast_info.last_price 為 188.90（cache 15:01），兩者差異 0.1%，以 189.09 為準。

| 指標 | 數值 | 計算 / 來源 |
|---|---|---|
| 市值 | USD 30.83B | info.marketCap；189.09 × 163.05M 股 ≈ 30.83B（驗算一致） |
| 企業價值 EV | USD 29.99B | info.enterpriseValue |
| Trailing P/E | n/m | TTM GAAP EPS USD -0.39 |
| Forward P/E | 33.6x | info.forwardPE；forward EPS USD 5.62 |
| 當年 EPS 本位 P/E | 38.5x | info.priceEpsCurrentYear；epsCurrentYear USD 4.91 |
| P/S (TTM) | 9.2x | info.priceToSalesTrailing12Months；TTM 營收 USD 3.35B（四季加總 3,352.6M 與 FY26 一致） |
| EV / Revenue (TTM) | 8.9x | info.enterpriseToRevenue |
| EV / EBITDA | n/m（~168x 以報表 EBITDA 計） | info.enterpriseToEbitda 684x（使用 info.ebitda USD 43.9M）；報表 EBITDA USD 178.5M 計算 EV/EBITDA ≈ 168x；兩者定義不一，皆偏高 |
| P / FCF (TTM) | 39.6x | 30.83B / FCF 779.1M（報表）；若採 info.freeCashflow 1,074.9M 則為 28.7x，兩者不一致，本報告採報表值 |
| P / B | 11.9x | info.priceToBook；bookValue USD 15.94 |
| PEG | 1.99 | info.pegRatio |

**相對估值（sector median 為估計值，非工具資料）**
- Software-Infrastructure 同業中位數（估計）：P/S 約 6–10x、forward P/E 約 25–35x、P/FCF 約 25–35x。ZS 在 P/S 與 forward P/E 位於或略高於區間上緣，在 P/FCF 位於區間上緣。
- 估值相對成長率屬偏高；以 PEG 1.99 計，市場已定價大部分成長預期。

**股價與技術位置**
- 52 週區間 USD 114.63 – 316.85，現價較 52 週高點 -40.3%、較低點 +65.0%；52 週漲跌幅 -37.2%。
- 50 日均價 USD 208.75（現價 -9.4%）；200 日均價 USD 166.72（現價 +13.4%）。
- 單日變動 -2.43%（USD 193.80 → 189.09）。Beta 0.84。
- 空頭：shares short 5.88M，占流通股 5.52%，days to cover 2.17。

**分析師共識（45 位）**
- recommendationMean 1.62（buy），recommendationKey = buy；strongBuy 7、buy 29、hold 11、sell 0、strongSell 0。
- 目標價：平均 USD 235.19（+24.4%）、中位數 USD 247.00（+30.6%）、最高 USD 298.00（+57.6%）、最低 USD 164.75（-12.9%）。

## Key catalysts

- **下一次財報**：2026-12-02（earnings_dates 與 info.earningsTimestamp 一致，時間戳 21:00 UTC 約為美東盤後）。isEarningsDateEstimate = False。consensus EPS（非 GAAP）USD 1.16。
- **財報歷史**：最近 24 次有實際值之財報（2020-12 至 2026-09）全數 EPS 優於預期。最近 8 季平均 surprise 約 +12.2%（最近 4 季：+9.18%、+7.11%、+12.56%、+11.42%）。
- **最新季動能**：FY26 Q4 營收 USD 898.2M（YoY +24.9%）、非 GAAP EPS USD 1.19（surprise +9.18%）。
- **未來指引（guidance）**：yfinance 未提供管理層最新營收與 EPS 指引數字，本報告無法引用：DATA_UNAVAILABLE。
- **遞延收入與 RPO**：遞延收入（流動）USD 2,480.5M 年增 20.8%；剩餘履約義務（RPO）與續約率：DATA_UNAVAILABLE。
- **併購整合**：FY26 收購支出 USD 918.1M，商譽增加 USD 800M 以上；整合效果與被併購公司資料：DATA_UNAVAILABLE。
- **資本支出**：Q4 FY26 Capex 年增約 2.8 倍，後續季度是否延續為觀察重點。

## Metrics table

以下表格金額單位於欄位中標示。「Sector median (estimate)」為依一般市場經驗的估計區間，非工具資料，僅供參考。

| Metric | Latest (FY26 / 2026-11-13) | YoY (vs FY25) | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 Revenue (USD B) | 3.35 | +25.4% | 約 10–15% 成長（估計） | 高成長，優於同業 |
| 營收 3Y CAGR (FY23–26) | 27.5% | n/a | 約 12–18%（估計） | 優 |
| 毛利率 Gross margin | 76.8% | -0.1 pt（FY25 76.9%） | 約 72–78%（估計） | 優，穩定 |
| 營業利益率 Operating margin (GAAP) | -3.6% | +1.2 pt（FY25 -4.8%） | 約 0–10%（估計） | 改善中，仍虧損 |
| 淨利率 Net margin (GAAP) | -1.9% | -0.3 pt（FY25 -1.6%） | 約 0–10%（估計） | 未獲利 |
| ROE | -2.9% | -0.2 pt（FY25 -2.7%） | 約 5–15%（估計） | 弱 |
| ROIC（稅前估計） | -3.1% | n/a | 約 5–12%（估計） | 弱 |
| 自由現金流 FCF (USD M) | 779.1 | +7.2%（FY25 726.7） | n/a | 穩定正向 |
| FCF margin | 23.2% | -4.0 pt（FY25 27.2%） | 約 20–25%（估計） | 尚可，略降 |
| FCF / NI | n/m（淨損） | n/a | n/a | 不適用 |
| FCF / SBC | 0.95x | FY25 1.10x（726.7/661.4） | 約 1.0x 以上為佳（估計） | 偏弱 |
| FCF - SBC (USD M) | -42.8 | FY25 +65.3 | n/a | 紅旗 |
| SBC / 營收 | 24.5% | -0.2 pt（FY25 24.7%） | 約 10–15%（估計） | 偏高 |
| 營業現金流 OCF (USD M) | 1,129.7 | +16.2%（FY25 972.5） | n/a | 優 |
| Capex (USD M) | 350.5（占營收 10.5%） | +42.6%（FY25 245.8） | 約 3–6%（估計） | 投資加速，留意 |
| 流動比率 Current ratio | 1.70 | -0.31（FY25 2.01） | 約 1.5–2.5（估計） | 可 |
| 淨現金（現金+STI−總債務）(USD M) | +1,618.4 | -157.4（FY25 +1,775.8） | n/a | 健康，但逐年縮減 |
| 總債務 Total debt (USD M) | 1,855.8 | +3.3%（FY25 1,796.6） | n/a | 中性 |
| 負債權益比 Debt/Equity | 0.71x | -0.29x（FY25 約 1.00x） | 約 0.3–0.8x（估計） | 可 |
| 遞延收入（流動）(USD M) | 2,480.5 | +20.8%（FY25 2,054.4） | n/a | 正向訂閱動能 |
| 應收帳款 Receivables (USD M) | 1,149.1 | +15.8%（FY25 992.2） | n/a | 正常 |
| 流通股數 Shares out (M) | 163.1 | +3.0%（FY25 158.3） | n/a | 稀釋中 |
| 內部人 6 個月淨賣出 (USD M) | 14.94 淨賣出（0 筆買入） | n/a | n/a | 幅度小（占市值 0.048%） |
| 機構持股 | 53.4%（1,231 家） | n/a | n/a | 正常 |
| 市值 Market cap (USD B) | 30.83 | n/a | 視同業（估計） | 中大型 |
| EV (USD B) | 29.99 | n/a | n/a | n/a |
| Trailing P/E | n/m | n/a | 約 25–40x（估計） | 不適用 |
| Forward P/E | 33.6x | n/a | 約 25–35x（估計） | 中上 |
| P/S (TTM) | 9.2x | n/a | 約 6–10x（估計） | 偏高 |
| EV / Revenue | 8.9x | n/a | 約 6–10x（估計） | 偏高 |
| EV / EBITDA | 約 168x（報表 EBITDA）；info 684x | n/a | 約 25–35x（估計） | 不具比較意義 |
| P / FCF (TTM) | 39.6x | n/a | 約 25–35x（估計） | 偏高 |
| P / B | 11.9x | n/a | 約 4–8x（估計） | 偏高 |
| PEG | 1.99 | n/a | 約 1.5–2.0（估計） | 中性偏高 |
| 分析師平均目標價 (USD) | 235.19（+24.4%） | n/a | n/a | 共識偏多（buy 1.62） |
| 股價 vs 200 日均 | +13.4%（200DMA 166.72） | n/a | n/a | 長期趨勢仍在上方 |
| 股價 vs 50 日均 | -9.4%（50DMA 208.75） | n/a | n/a | 短期偏弱 |
| 空頭占流通股 | 5.52% | n/a | n/a | 中性 |
| 下一次財報 | 2026-12-02，consensus EPS USD 1.16 | n/a | n/a | 催化劑 |

## Red flags

- **SBC 超過 FCF**：FY26 SBC USD 821.9M 高於 FCF USD 779.1M，FCF - SBC = USD -42.8M；股東實際承擔的稀釋成本高於現金產生能力。
- **GAAP 持續虧損**：FY23–FY26 淨利均為負（FY26 -63.2M），GAAP 營業利益仍為負；獲利主要來自利息收入（FY26 淨利息收入 USD 124.3M）。
- **FCF 年增率放緩**：FY26 FCF 成長僅 +7.2%，低於營收成長 +25.4%，FCF margin 由 27.2% 降至 23.2%；Q4 FY26 單季 FCF 僅 USD 60.8M。
- **Capex 與併購同時加速**：Q4 FY26 Capex USD 218.5M（YoY 約 2.8 倍）；FY26 併購支出 USD 918.1M，商譽增至 USD 1.22B。
- **股權稀釋持續**：流通股 +3.0%，稀釋後股數 +3.8%；無回購以抵銷。
- **流動比率與淨現金縮減**：流動比率由 2.01 降至 1.70；淨現金由 USD 1.78B 降至 USD 1.62B。
- **Net Debt 資料矛盾**：yfinance 報告 Net Debt USD 768.0M，與自算淨現金 USD +1,618M 方向相反，需回報資料源。
- **EBITDA / FCF 定義不一致**：info.ebitda USD 43.9M 與報表 EBITDA USD 178.5M 差距大；info.freeCashflow USD 1,074.9M 與報表 FCF USD 779.1M 差距 USD 296M；Operating Income 兩列（-121.1M 與 -133.3M）不同。使用前需核對。
- **所得稅異常**：FY26 稅前虧損但稅費 USD +46.0M。
- **估值偏高**：P/S 9.2x、P/FCF 39.6x、forward P/E 33.6x、PEG 1.99，估值對執行力要求高。
- **內部人持續賣出**：6 個月 USD 14.94M，雖占市值極小，但 CEO/CFO/CLO 均有出售紀錄；0 筆買入。
- **治理風險評分偏高**：overallRisk 7、boardRisk 8、shareHolderRightsRisk 8（info）。
- **股價距高點 -40%**：52 週跌幅 -37.2%，雖高於 200 日均，但已跌破 50 日均；分析師最低目標價 USD 164.75 低於現價。
- **資料缺口（DATA_UNAVAILABLE）**：分部營收、管理層指引數字、RPO / 續約率、併購標的細節、債務票面與到期結構、Q4 FY26 earnings call 內容。

FUNDAMENTALS REPORT COMPLETE
