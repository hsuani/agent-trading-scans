# Fundamentals — 5455.TWO (英特磊 / Sheng Yi Development Co., Ltd) as of 2026-10-11

## Executive summary
英特磊（5455.TWO，Yahoo 登記名為 Sheng Yi Development Co.,Ltd，產業分類為 Real Estate - Development）財務體質偏弱：TTM 營收僅 26.57M TWD、TTM 淨損 -41.55M TWD，2025 年 FCF 為 -493.7M TWD，2026 年 6 月底總負債 2,794.7M TWD 全數為流動負債，股東權益僅 1,363.0M TWD。估值面 trailing P/E 與 EV/EBITDA 因虧損無法計算，P/B 1.48x 與 P/S 75.9x 在獲利消失的情況下不具吸引力，且 3 個月平均成交量僅 8,114 股、可流通股數約 55 萬股，流動性與資料完整度都需要納入風險考量。

資料限制：本次即時 Yahoo 介面 403 失敗，價格與財務皆取自本地 cache（fast_info 來源 cnyes，cached_at 2026-10-11T12:35 UTC）；insider、institutional holders、earnings date 皆為 DATA_UNAVAILABLE 或不完整。

## Revenue & profitability

**年度營收（TWD，來源：yf financials）**

| 年度 | Total Revenue | YoY | Gross Profit | Gross Margin | Operating Income | Op Margin | Net Income | Net Margin |
|---|---|---|---|---|---|---|---|---|
| FY2022 | 599.5M | n/a | 112.5M | 18.8% | 56.5M | 9.4% | 59.7M | 10.0% |
| FY2023 | 1,616.4M | +169.6% | 299.5M | 18.5% | 182.3M | 11.3% | 166.2M | 10.3% |
| FY2024 | 3,623.6M | +124.2% | 652.6M | 18.0% | 436.5M | 12.0% | 382.1M | 10.5% |
| FY2025 | 2,044.3M | -43.6% | 428.8M | 21.0% | 301.4M | 14.7% | 226.5M | 11.1% |

- 3 年營收 CAGR（FY2022 至 FY2025）約 50.5%。資料只提供 4 個年度，無法計算 5 年 CAGR。
- 營收呈現明顯的「認列時點集中」特徵：FY2024 與 FY2025 的營收高峰與 2025 Q2 單季 1,738.7M 高度吻合，屬於建案交屋或銷售認列的一次性集中。
- 業務描述（yf longBusinessSummary）：住宅大樓與公寓建築、租售、建材批發、室內裝修租售、不動產出租。資料未提供分部營收，segment mix 為 DATA_UNAVAILABLE。

**季度營收與獲利轉折（TWD，來源：yf quarterly_fin）**

| 季度 | Revenue | Gross Margin | Operating Income | Net Income | Diluted EPS |
|---|---|---|---|---|---|
| 2025 Q1 | DATA_UNAVAILABLE | n/a | n/a | n/a | 0.03 |
| 2025 Q2 | 1,738.7M | 22.9% | 310.9M | 235.6M | 3.59 |
| 2025 Q3 | 13.7M | 9.2% | -8.5M | -6.2M | -0.09 |
| 2025 Q4 | 4.8M | 26.3% | -6.3M | -4.7M | DATA_UNAVAILABLE |
| 2026 Q1 | 7.4M | 36.5% | -7.4M | -9.7M | -0.15 |
| 2026 Q2 | 0.65M | 51.2% | -6.7M | -20.9M | -0.32 |

- 2026 年上半年營收合計約 8.0M TWD，相較 2025 上半年 1,738.7M 以上（Q1 缺值），營收基本停擺。
- 毛利率單季波動大，原因是營收基數過小（Q2'26 毛利僅 0.33M TWD），不具可比性。
- Operating income 自 2025 Q3 起連續 4 季為負，合計約 -29.0M TWD（TTM）。yfinance info 欄位 operatingMargins 為 -10.33（-1,033%），與由季度表計算的 TTM 營業利益率約 -109% 不一致，本報告採計算值。
- 2026 Q2 稅費支出為 10.5M TWD，但稅前淨損為 -10.3M TWD，出現虧損下的所得稅費用，原因資料未揭露。

**獲利能力指標**

- ROE：TTM 淨損 -41.55M / 期末股東權益 1,363.0M ≈ -3.0%（yfinance info returnOnEquity = -3.03%，一致）。FY2025 ROE 以期末權益計算約 16.4%（226.5M / 1,380.5M）。
- ROIC（粗估）：FY2025 EBIT 306.5M × (1 - 24.8% 有效稅率) ≈ 230M NOPAT，除以期末 Invested Capital 3,084.0M ≈ 7.5%。TTM 營業利益為負，TTM ROIC 為負。
- 淨利率趨勢：FY2022 至 FY2025 維持 10–11%，但 2025 下半年至 2026 上半年轉為虧損，TTM 淨利率 -156.4%（info profitMargins = -1.564，一致）。

## Cashflow & balance sheet

**現金流量（TWD，來源：yf cashflow / quarterly_cf）**

| 年度 | Operating CF | FCF（yf） | FCF Margin | FCF / NI |
|---|---|---|---|---|
| FY2022 | -1,121.3M | -1,121.3M | n/a（-187.0%） | n/a |
| FY2023 | +729.2M | +729.2M | 45.1% | 4.39x |
| FY2024 | -105.8M | -105.8M | -2.9% | -0.28x |
| FY2025 | -492.9M | -493.7M | -24.2% | -2.18x |

- 2026 上半年 FCF 合計 -902.5M（Q1 -517.9M、Q2 -384.6M）；TTM FCF（2025 Q3 至 2026 Q2）合計約 -1,808.7M（季度加總），yfinance info freeCashflow 為 -1,798.5M，差異屬口徑差。
- FCF/NI 遠低於 0.9 健康門檻，且多數年份為負值，屬於現金流品質極差的狀態。
- 負向現金流的主因是存貨（Inventory）大幅增加：FY2025 存貨變動 -222.9M，2026 上半年存貨變動合計 -961.7M（Q1 -447.7M、Q2 -514.0M）。這與房地建案開發的資金佔用特性一致，屬推定，資料未明列。

**資產負債表（TWD）**

| 項目 | 2025-12-31 | 2026-03-31 | 2026-06-30 |
|---|---|---|---|
| Total Assets | 4,127.7M | 4,637.8M | 5,419.8M |
| Inventory | 3,734.6M | 4,194.0M | 4,721.3M |
| Cash & Equivalents | 3.5M | 25.9M | 195.8M |
| Total Debt | 1,703.9M | 2,241.7M | 2,794.7M |
| Net Debt | 1,700.0M | 2,215.6M | 2,598.7M |
| Total Liabilities | 2,747.1M | 3,267.2M | 4,056.8M |
| Stockholders Equity | 1,380.5M | 1,370.6M | 1,363.0M |
| Working Capital | 1,267.4M | 1,258.0M | 1,268.5M |

- 存貨佔總資產比重：2025-12-31 為 90.5%，2026-06-30 為 87.1%（4,721.3M / 5,419.8M）。
- 有息負債（Total Debt）全數列為流動負債（Current Debt 2,794.5M），Long Term Debt 為 0。半年內增加 1,091M（+64%），2026 年 Q1、Q2 分別淨舉債 +538M、+553M。
- Debt/Equity：205.0%（info debtToEquity 205.046，一致）；Net Debt/Equity 約 190.7%。
- Current ratio：1.313（5,324.4M / 4,056.0M，與 info 一致）。Quick ratio 0.056（info 值；扣除存貨與預付、遞延資產後的速動資產約 226.5M）。流動比率雖然大於 1，但流動資產主體是存貨，實際短期償債能力弱。
- 現金：2026-06-30 現金及約當現金 195.8M，相較 2026-03-31 的 25.9M 增加，主要來自當季舉債。
- 無 Long-term debt 與可辨識之利息資本化金額。Q2'26 利息費用 4.9M，TTM 利息費用約 8.1M，相對 2,794.7M 有息負債，年化利率僅約 0.7%（以 Q2 年化利息 19.6M 除以約 2.5B 平均有息負債），遠低於一般建案融資水準，推估大部分利息已資本化入存貨，損益表未完整反映融資成本（推定，資料未揭露）。
- 其他：Investment Properties 2026-06-30 為 58.4M（前一季 89.4M），Assets Held For Sale 29.7M 為 2026 Q2 新增項目，顯示有資產處分動作。

## Capital allocation & insider signal

**資本配置**

- Capex：FY2025 PPE 購置僅 0.8M；另有投資性不動產購置 25.0M（FY2024 為 10.0M）。資本支出極低，屬輕資產結構，但存貨（建案）投入是實質資本支出。
- 股利：trailingAnnualDividendRate = 0，dividendYield = 0，股利覆蓋率為 n/a（無配息）。
- 買回：流通股數自 2022 至 2026 年 6 月維持 65,502,000 股，無買回或增資記錄（依 yf balance_sheet / quarterly_bs 之 Ordinary Shares Number）。
- 融資：FY2025 淨舉債 +42.3M；2026 上半年淨舉債合計 +1,091M，資本配置實質依賴債務滾動。

**內部人與股東結構**

- Insider transactions（yf insider，近 6 個月）：回傳為空陣列，淨買賣金額與規模占市值比為 DATA_UNAVAILABLE。
- 董監持股比例 insidersPercentHeld = 70.3%（yf major_holders）。Officers 僅列 Chairman & GM Wenchi Chen 與會計主管，無持股金額資料。
- Institutional holders：institutionsPercentHeld = 0.0，inst_holders 回傳空陣列，屬 DATA_UNAVAILABLE。
- 可流通股數 floatShares = 553,492 股，佔總股數約 0.85%。平均成交量 3 個月 8,114 股，10 日平均 2,237 股，流動性極低。
- 結論：無法從 insider 資料判斷近期內部人買賣方向，但高達 70% 的內部人持股加上極低流通股數，意味著股價受少數人控制、可交易籌碼極少。

## Valuation

以 2026-10-11 cache 價格 30.8 TWD 計算（bid 30.35 / ask 30.75，當日成交量 2,000 股）：

- 市值（marketCap）：2,017.5M TWD；流通在外股數 65.502M；每股淨值 BVPS 20.81 TWD。
- 企業價值（EV）：4,616.4M TWD（市值 2,017.5M + 總負債 2,794.7M - 現金 195.8M，與 info enterpriseValue 一致）。
- P/E（trailing）：n/a（TTM EPS -0.63）。P/E（forward）：DATA_UNAVAILABLE（無分析師預估，recommendationKey = none）。
- P/B：1.48x（30.8 / 20.81）。
- P/S（trailing）：75.9x（2,017.5M / 26.57M）。
- EV/Revenue：173.7x。
- EV/EBITDA：n/a（TTM EBITDA 為負，info ebitda = -28.4M，enterpriseToEbitda = -162.4 無意義）。
- P/FCF：n/a（FCF 為負）。
- 與產業中位數比較：以下為估計值（非資料工具輸出，屬分析師估計）。台灣住宅建設業一般 P/B 約 0.6–1.2x、正常年度 P/E 約 10–20x、毛利率約 20–30%。英特磊 P/B 1.48x 高於估計區間，獲利面又為負，估值不便宜。
- 股價位置：30.8 位於 52 週區間 22.0–31.0 的高段（距 52 週高點 -0.6%），高於 50 日均價 29.73 與 200 日均價 27.31。
- 注意：info allTimeHigh 161.05、allTimeLow 4.4 為未調整歷史值（2014 年 0.15:1 減資等事件影響），不應用於估值判斷。

## Key catalysts

- 下次財報：earnings_dates 僅含 2007 年一筆紀錄，下次財報日期為 DATA_UNAVAILABLE。依台灣證交所規定，季報須於季末後 45 日內公告，2026 Q3 季報截止日約為 2026-11-14（規則推算，非公司公告）。
- 最近一季（2026 Q2，截至 2026-06-30）已揭露，但未見管理層指引（guidance）與 recommendationKey 資料，guidance 為 DATA_UNAVAILABLE。
- 營收轉折因子：2025 Q2 的 1,738.7M 營收可能來自建案交屋認列，之後營收近乎歸零。後續營收能否恢復取決於交屋時程與新建案銷售認列，屬資料未揭露之推定。
- 資產處分：2026 Q2 出現 Assets Held For Sale 29.7M，投資性不動產下降，後續處分進度值得追蹤。
- 融資壓力：2026 上半年淨舉債 +1,091M，若存貨不能轉為現金，短期債務滾動風險高。
- 股價催化劑（技術面）：目前股價位於近期高檔，技術面判斷屬其他分析師之範圍，本報告不做交易建議。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue TTM (TWD) | 26.6M | 2025 Q2 單季 1,738.7M，YoY 約 -100%（0.65M vs 1,738.7M，季度比較） | 估計營收為正且穩定 | 弱 |
| Revenue FY2025 | 2,044.3M | -43.6% | 估計 0–10% 年增 | 弱（波動大） |
| Revenue CAGR 3Y (FY22–25) | 50.5% | n/a | 估計 5–10% | 高但不具延續性 |
| Gross Margin FY2025 | 21.0% | +3.0 pp | 估計 20–30% | 中性 |
| Op Margin FY2025 | 14.7% | +2.7 pp | 估計 8–15% | 中性（TTM 為 -109%） |
| Net Margin TTM | -156.4% | n/a | 估計 5–15% | 極弱 |
| ROE TTM | -3.0% | n/a | 估計 5–10% | 弱 |
| ROE FY2025（期末權益） | 16.4% | n/a | 估計 5–10% | 強（但已逆轉） |
| FCF FY2025 | -493.7M | 較 FY2024 惡化 | 估計為正 | 極弱 |
| FCF TTM | -1,808.7M（季度加總） | n/a | 估計為正 | 極弱 |
| FCF / NI FY2025 | -2.18x | n/a | 估計 > 0.9 | 極弱 |
| Current Ratio (2026-06-30) | 1.31 | 較 2025-12 之 1.46 下降 | 估計 1.2–2.0 | 中性偏弱（存貨占流動資產 88.7%） |
| Quick Ratio (2026-06-30) | 0.06 | n/a | 估計 0.8–1.2 | 極弱 |
| Debt / Equity (2026-06-30) | 205.0% | 2025-12 為 123.4% | 估計 100–200%（建設業） | 偏高 |
| Net Debt (2026-06-30) | 2,598.7M | +52.9% vs 2025-12 | n/a | 偏弱 |
| Cash (2026-06-30) | 195.8M | 2025-12 為 3.5M | n/a | 偏低（相對有息負債） |
| Total Debt 短期占比 | 100% | n/a | 估計 < 50% | 極弱（全數流動） |
| Dividend Yield | 0.0% | n/a | 估計 3–5% | 無配息 |
| Share Count | 65.5M | 持平（2022 至今） | n/a | 中性 |
| Insider Net Buy/Sell 6M | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| Insider Ownership | 70.3% | n/a | 估計 20–40% | 集中度高，流通股僅 0.85% |
| Avg Volume 3M | 8,114 股 | n/a | n/a | 流動性極低 |
| P/E (trailing) | n/a（EPS -0.63） | n/a | 估計 10–20x | n/a（虧損） |
| P/E (forward) | DATA_UNAVAILABLE | n/a | 估計 10–20x | DATA_UNAVAILABLE |
| P/B | 1.48x | n/a | 估計 0.6–1.2x | 偏貴 |
| P/S (trailing) | 75.9x | n/a | 估計 1–3x | 極貴 |
| EV/EBITDA | n/a（EBITDA 為負） | n/a | 估計 8–15x | n/a |
| P/FCF | n/a（FCF 為負） | n/a | n/a | n/a |
| Next Earnings Date | DATA_UNAVAILABLE（法規截止約 2026-11-14） | n/a | n/a | DATA_UNAVAILABLE |

## Red flags
- 營收幾近歸零：2026 上半年營收合計約 8.0M TWD，TTM 淨損 -41.6M TWD，與 2025 上半年的 1,738.7M 營收形成斷崖式下滑。
- 現金流持續惡化：TTM FCF 約 -1.81B TWD，2026 上半年即負 902.5M，FCF 完全依賴債務支撐。
- 負債結構極度短期化：2,794.7M 有息負債全數流動，2026 上半年新增 1,091M（+64%），債務滾動風險高。
- 現金極低：2025 年底現金僅 3.5M TWD，2026 年 6 月底 195.8M，對有息負債覆蓋率約 7%。
- 存貨佔比過高：存貨 4,721.3M 佔總資產 87.1%，若存貨變現速度慢或跌價，權益（1,363.0M）將被快速侵蝕。
- 利息費用疑似資本化：TTM 利息費用僅約 8.1M，遠低於有息負債規模，損益表可能低估真實融資成本（推定）。
- 虧損下出現稅費：2026 Q2 稅費 10.5M，稅前淨損 -10.3M，原因未揭露。
- 留存盈餘異常減少：2026 上半年 Retained Earnings 由 661.4M 降至 608.1M（-53.3M），大於同期淨損 -30.6M，差額 -22.7M 原因未揭露（無股利記錄）。
- 內部人與流動性：董監持股約 70.3%，流通股數僅約 55 萬股（0.85%），3 個月平均成交量 8,114 股，價格發現與退出流動性不足。
- 資料完整度不足：Insider 交易、法人持股、下次財報日、分析師預估、分部資料皆為 DATA_UNAVAILABLE；即時 Yahoo 介面 403 失敗，價格與財務依賴本地 cache。
- 資料異常：yfinance info 的 operatingMargins（-10.33）與季度表計算值（約 -1.09）不一致；Q4 2025 Diluted EPS 缺值；quick ratio 與計算值口徑不同，本報告已標註採用來源。
- 時效說明：最新財報為 2026-06-30 季；未發現晚於 2026-10-11 的財務資料。

FUNDAMENTALS REPORT COMPLETE
