# Fundamentals — TLN (Talen Energy Corporation) as of 2026-11-24

資料說明：本報告以 2026-11-24 為分析基準日。yfinance `info` / `fast_info` 為 cache 快照（cached_at 2026-11-23 17:59 UTC），價格 363.26 USD 為 2026-11-23 盤中價，非 11-24 收盤價。`balance_sheet` / `cashflow` / `financials` 為年度資料（最新為 FY2025-12-31）；`info` 內的 TTM 與 balance 欄位對應 2026-09-30（mostRecentQuarter）。未發現晚於 2026-11-24 的資料；下次財報日 2027-02-25 為未來排程。金額單位：USD，以 B（十億美元）或 M（百萬美元）標示。

## Executive summary
TLN 是以核能與天然氣電廠為主的獨立電力公司（Utilities / Independent Power Producers），FY2025 營收 2.626B USD 年增 26.7%，但營業利益僅 16M USD、淨利為 -219M USD，EBIT 對利息支出覆蓋僅 0.45x，財務體質偏弱（Total Debt 6.81B USD，Debt/Equity 約 6.2x）。FCF 在 FY2025 為正（498M USD），但扣除 526M USD 的股票型薪酬後轉為約 -28M USD，現金流品質需要保留。估值上 forward P/E 為 11.3x、當年度 P/E 為 15.1x，但 trailing EPS 為負，EV/EBITDA（TTM 35.2x）與 P/S（年度 6.0x）偏高；分析師共識 Strong Buy（均值 1.5，20 位），目標價均值 452.65 USD（較現價 +24.6%），但近兩季 EPS 連續不及預期，且空單比例快速上升。綜合判斷：營運成長與分析師預期正面，但獲利與槓桿指標尚未證明體質改善，估值是否具吸引力取決於 2027 年獲利兌現，本報告不提供交易建議。

## Revenue & profitability

- 營收（FY，USD）：2021 1.775B → 2022 2.412B → 2024 2.073B → 2025 2.626B。
- 4 年 CAGR（2021–2025）約 10.3%；3 年 CAGR（2022–2025）約 2.9%，顯示 2022–2024 波動大，2025 為主要成長年度（YoY +26.7%）。
- info 的 TTM totalRevenue 為 4.481B USD，revenueGrowth 為 +96.1%。此 TTM 與 FY2025 年度數字差距大，因缺少季度損益表，無法確認差異來源，請視為待確認資料。
- 業務組成：info 的 longBusinessSummary 描述為核能、化石燃料（天然氣、燃油、煤）電廠合計約 13.1 GW 發電資產，並向批發電力市場銷售電力、容量與輔助服務。未提供分部營收比重，segment mix 為 n/a。團隊背景提及 Susquehanna 的 Amazon 資料中心 PPA，此為團隊既有資訊，不在 yfinance 資料內，本報告未獨立驗證。

獲利能力（年度，依 financials 計算）：

| 年度 | 毛利率 (GP/Rev) | 營業利益率 (Operating Income/Rev) | 淨利率 (NI/Rev) |
|---|---|---|---|
| 2025 | 38.1%（GP 1,001M） | 0.6%（OI 16M） | -8.3%（NI -219M） |
| 2024 | 32.0%（GP 664M） | 8.0%（OI 165M） | 48.1%（NI 998M，含約 886M 出售事業收益，屬非經常性） |
| 2022 | 31.9% | 4.3% | -53.4%（含約 1.3B restructuring 項目） |

- 2025 營業利益率僅 0.6%，相較 2024 的 8.0% 明顯下滑，主因 SG&A 由 163M 升至 624M USD（+283%），與同期股票型薪酬 526M USD（2024 為 33M）高度吻合。
- 2025 normalized EBITDA 584M USD（22.2% 營收率），低於 2024 的 812M USD（39.2%）。
- info 的 TTM 數字：grossMargins 42.7%、operatingMargins 3.3%、ebitdaMargins 15.0%、profitMargins -5.7%，TTM EBITDA 674M USD。
- ROE：info 的 returnOnEquity 為 -16.5%（TTM）；以 FY2025 數字估算，NI / 期末股東權益（1,093M）為 -20.0%。
- ROIC（本報告估算）：FY2025 EBIT 136M × (1 - 25.6% 稅率) ÷ 平均 Invested Capital（(7,904M + 4,391M) / 2 = 6,148M）約 1.6%，遠低於資金成本，顯示資本效率偏低。
- 利息覆蓋：FY2025 interest expense 302M USD，EBIT / interest 為 0.45x，EBITDA / interest 為 1.7x。

## Cashflow & balance sheet

現金流（USD，年度）：

| 項目 | FY2025 | FY2024 | FY2022 | FY2021 |
|---|---|---|---|---|
| Operating Cash Flow | 704M | 256M | 187M | -291M |
| Capex | -206M | -189M | -312M | -250M |
| Free Cash Flow | 498M | 67M | -125M | -541M |
| FCF margin | 19.0% | 3.2% | -5.2% | -30.5% |
| Stock-Based Comp | 526M | 33M | n/a | n/a |
| Repurchase of stock | -103M | -1,958M | 0 | n/a |

- FCF / NI：FY2025 淨利為負（-219M），FCF / NI 比值無意義（n/m），不符合「>0.9 健康」的判讀前提。
- SBC 調整：FY2025 CFO 包含 526M USD 股票型薪酬加回。若扣除 SBC，FY2025 FCF 約為 498M - 526M = -28M USD。這是本報告最重要的現金流品質風險點。
- info 的 TTM freeCashflow 941.6M USD、operatingCashflow 770M USD，因 TTM 期間與年度不同，未納入上述比較，需以季度現金流確認。

資產負債（USD，年度，期末 FY2025-12-31，對照 FY2024）：

| 項目 | FY2025 | FY2024 |
|---|---|---|
| Cash & equivalents | 689M | 328M |
| Total Debt | 6,811M | 3,004M |
| Net Debt | 6,122M | 2,676M |
| Total Assets | 10,905M | 6,106M |
| Net PPE | 7,546M | 3,154M |
| Stockholders' Equity | 1,093M | 1,387M |
| Current Assets / Current Liabilities | 1,349M / 1,050M（比 1.28x） | 1,040M / 455M（比 2.29x） |
| Debt / Equity | 6.23x（年度計算）；info 為 5.97x | n/a |

- 2025 年淨負債由 2.68B 增至 6.12B USD，Total Debt 增加約 3.8B USD。現金流量表顯示 2025 購入事業 (Purchase of Business) 3,793M USD，同時 Net PPE 由 3.15B 增至 7.55B，顯示 2025 有大規模資產併購，性質與交易對象需以 10-K 確認。
- 2025 融資現金流入 3,686M USD，其中 Net Other Financing Charges 3,806M USD 未細分，Issuance of Debt 僅 75M USD；債務來源需 10-K 確認。
- info 的最新資料（2026-09-30）：totalDebt 9.569B USD、totalCash 339M USD，net debt 約 9.23B USD；currentRatio 0.893，quickRatio 0.498。與年度資料相比，負債持續上升，流動性指標在 Q3 2026 低於 1.0。
- info 的 enterpriseValue 為 23.74B USD，以 market cap 15.80B + totalDebt 9.57B - totalCash 0.34B 直接計算約 25.03B USD，兩者差異約 1.3B USD，未能確認原因，EV 相關倍數以 info 報告值為準並保留誤差。
- 投資與其他資產：Investments And Advances 1.90B USD（2025），性質需確認。

## Capital allocation & insider signal

資本配置：
- Capex：FY2025 206M USD，FY2024 189M，FY2022 312M；Capex 佔 OCF 比率 2025 為 29%。
- 買回：FY2024 買回 1,958M USD，FY2025 僅 103M USD。流通股數由 2023 的 53.25M 股降至 2025 的 45.69M 股，info 的 sharesOutstanding 為 43.5M，floatShares 33.5M。
- 股息：dividendYield 0.0、payoutRatio 0.0，無配息。
- 股票型薪酬 2025 為 526M USD，相對營收約 20%，對股東稀釋的影響需以 10-K 與 proxy 確認。

內部人交易（最近 6 個月，約 2026-05-24 至 2026-11-23）：
- 公開市場賣出（Form 4 "Sale"）合計 4 筆，共 65,596 股、約 23.36M USD：
  - 2026-11-17 Brad L. Berryman（COO）賣出 56,091 股，價格區間 345.44–364.56，金額 19.83M USD。
  - 2026-11-17 Edward T. Casulli（Officer）賣出 3,602 股，354.52 USD，1.28M USD。
  - 2026-11-11 Edward T. Casulli 賣出 3,303 股，382.74 USD，1.26M USD；另有 300 股 gift（無金額）。
  - 2026-06-15 Gizman I. Abbas（Director）賣出 2,600 股，380.00 USD，0.99M USD。
- 占市值比例：23.36M USD / 15.80B USD = 約 0.15%，規模偏小；但 COO 單筆 19.8M USD 為近期最大宗，成交價區間 345–365，接近目前價位。
- 2026-05-22 有多位高階主管與董事的大量申報（CEO McFarland 354,865 股、Nutt 90,826 股、Berryman 99,138 股、Muller 62,862 股等），但 info 內無金額欄位，交易性質（授予、歸屬或其他）未能從 yfinance 判定，本報告不將其計為賣出。2026-07-15 Nutt 8,312 股同樣無金額。
- 淨方向：6 個月內可辨識的公開市場交易皆為賣出，無公開市場買入（除 2025-03-06 Horton 買入 1,000 股，已超出 6 個月窗口）。

機構持股（13F，2026-09-30）：
- Top holders：BlackRock 7.3%（4.31M 股）、Rubric Capital 6.1%（3.60M 股）、MFN Partners 5.5%（3.25M 股，季增 +8.3%）、ECP ControlCo 4.07%、Vanguard PM 3.78%、Vanguard CM 3.59%、Fred Alger 3.01%（季增 +14.9%）、Reaves 2.44%、State Street 2.33%、Sachem Head 1.96%（季減 -15.5%）。前十大合計約 40.1%。
- info 的 heldPercentInstitutions 為 114.7%，超過 100%，明顯為資料錯誤，本報告不採用；insiders held 1.36%；institutionsCount 809。
- 空單：shortPercentOfFloat 10.86%，sharesShort 4.58M 股，較前月 2.50M 增加約 83%，shortRatio 3.88 天。空單快速增加與 COO 賣出同期出現，需觀察是否延續。

## Valuation

資料基準：現價 363.26 USD（2026-11-23 盤中），market cap 15.80B USD，EV 23.74B USD（info 報告值）。

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E | n/m | TTM EPS -5.59 USD |
| Forward P/E | 11.3x | 363.26 / forwardEps 32.18 |
| 當年度 P/E | 15.1x | 363.26 / epsCurrentYear 24.03 |
| EV/EBITDA | 35.2x（TTM EBITDA 674M）；約 40.6x（FY2025 normalized EBITDA 584M） | info enterpriseToEbitda；本報告計算 |
| P/FCF | 16.8x（TTM FCF 941.6M）；31.7x（FY2025 FCF 498M） | market cap / FCF |
| P/S | 3.5x（TTM 營收 4.48B）；6.0x（FY2025 營收 2.63B） | info priceToSalesTrailing12Months；本報告計算 |
| P/B | 10.9x | info priceToBook |

- 同業中位數為估計值（非工具資料）：一般 IPP 類股 forward P/E 約 15–20x、EV/EBITDA 約 12–15x、P/S 約 2–4x。TLN 的 forward P/E 低於估計區間，但 EV/EBITDA 與 P/S（依年度）高於估計區間，原因是 FY2025 獲利基礎薄弱且負債高。
- 分析師目標價：mean 452.65、median 456.5、high 560.0、low 307.0 USD；相對現價分別為 +24.6%、+25.7%、+54.2%、-15.5%。推薦分布：strongBuy 6、buy 12、hold 2、sell 0、strongSell 0（共 20 位）。
- 股價位置：52 週區間 279.77–449.84，現價位於區間中段偏上（約 49% 位置，較 52 週高點低 19.2%）；較 50 日均線 338.19 高 7.4%、較 200 日均線 349.22 高 4.0%；52 週變動 -12.5%；beta 1.579。
- 當日變動：+9.1%（332.92 → 363.26）。盤中波動大，資料中未提供當日上漲原因，本報告不推測。

## Key catalysts

- 下次財報：yfinance earnings_dates 列出 2027-02-25，EPS 共識 12.48（非 info 的 earningsTimestamp，該欄對應已發生的 2026-11-03 財報）。日期來自 yfinance，未經公司公告確認。
- 近期財報表現：
  - 2026-11-03（Q3 2026）EPS 實際 5.89 vs 估計 7.46，不及預期 -21.0%。
  - 2026-08-05（Q2 2026）EPS 實際 2.37 vs 估計 3.39，不及預期 -30.0%。
  - 2026-05-05（Q1 2026）EPS 4.38 vs 4.26，優於 +2.9%。
  - 2026-02-26（Q4 2025）EPS 4.38 vs 4.33，優於 +1.2%。
  - 2025-11-05（Q3 2025）EPS 3.29 vs 3.67，不及預期 -10.3%。
  - 近 5 季中 3 季不及預期，最近兩季皆為大幅不及預期。
- 指引（guidance）：yfinance 未提供管理層指引文字，本項 n/a。
- 分部變化：未提供，n/a。
- 其他觀察點：2026 年底為 FY2026 結束（nextFiscalYearEnd 2026-12-31）；空單比例與內部人賣出同期上升；Q3 2026 資產負債數字（totalDebt 9.57B）若持續擴大，利息負擔將壓縮獲利。

## Metrics table

單位：USD（B / M），比例以 %，倍數以 x。Latest 為 info 最新值（2026-09-30 或 cache 日）或 FY2025 年度值，已於欄位註明。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (FY2025，USD) | 2.63B | +26.7% | n/a（估計成長 3–8%） | 成長強，但來源為併購與容量變化，需確認 |
| Revenue TTM (info，USD) | 4.48B | +96.1%（revenueGrowth） | n/a | 與 FY 差異大，待季度資料確認 |
| Gross margin (FY2025) | 38.1% | 較 FY2024 +6.1pt | n/a | 改善 |
| Operating margin (FY2025) | 0.6% | 較 FY2024 -7.4pt | 約 15–25%（估計） | 偏弱 |
| Net margin (FY2025) | -8.3% | 由 +48.1% 轉負 | 約 5–15%（估計） | 偏弱，FY2024 為非經常性 |
| EBITDA normalized (FY2025，USD) | 584M | -28.1%（vs 812M） | n/a | 下滑 |
| EBITDA margin normalized | 22.2% | 較 FY2024 -17.0pt | 約 30–40%（估計） | 偏弱 |
| ROE | -16.5%（info TTM） | n/a | 約 8–12%（估計） | 負值，不合格 |
| ROIC (本報告估算，FY2025) | 1.6% | n/a | 約 6–8%（估計） | 低於資金成本 |
| FCF (FY2025，USD) | 498M | +643%（vs 67M） | n/a | 正值，但受 SBC 影響 |
| FCF margin (FY2025) | 19.0% | 較 FY2024 +15.8pt | 約 10–20%（估計） | 尚可 |
| FCF / NI | n/m（NI 為負） | n/a | >0.9 健康 | 無法判讀 |
| FCF 扣除 SBC (FY2025，USD) | -28M | n/a | n/a | 警訊 |
| Interest coverage (EBIT / interest, FY2025) | 0.45x | n/a | 約 3x 以上（估計） | 不合格 |
| Net Debt (2026-09-30 info，USD) | 9.23B（= 9.57B - 0.34B） | 年度口徑 6.12B vs 2.68B | n/a | 槓桿顯著上升 |
| Debt / Equity (FY2025) | 6.23x（info 5.97x） | 由 n/a（FY2024 約 2.2x，以 3,004M / 1,387M 計） | 約 1–2x（估計） | 高槓桿 |
| Current ratio (info 2026-09-30) | 0.89x | FY2025 年度 1.28x | 約 1.2–1.5x（估計） | 流動性偏緊 |
| Cash (FY2025，USD) | 689M | +110%（vs 328M） | n/a | 改善 |
| Capex (FY2025，USD) | 206M | +9%（vs 189M） | n/a | 投資中等 |
| Buyback (FY2025，USD) | 103M | -95%（vs 1,958M） | n/a | 大幅縮減 |
| Dividend yield | 0.0% | n/a | 約 2–4%（估計） | 無配息 |
| SBC (FY2025，USD) | 526M | 由 33M 增至 526M | n/a | 重大警訊 |
| Forward P/E | 11.3x | n/a | 約 15–20x（估計） | 相對便宜，但 EPS 高度不確定 |
| P/E 當年度 | 15.1x | n/a | 約 15–20x（估計） | 接近估計中位數 |
| Trailing P/E | n/m（EPS -5.59） | n/a | 約 15–20x（估計） | 無法判讀 |
| EV/EBITDA (info TTM) | 35.2x | n/a | 約 12–15x（估計） | 偏貴 |
| P/FCF (TTM) | 16.8x | n/a | 約 15–20x（估計） | 中性 |
| P/S (TTM) | 3.5x | n/a | 約 2–4x（估計） | 中性偏高 |
| Analyst recommendation mean | 1.5（strong buy） | n/a | 約 2.0（估計） | 偏正面 |
| Analyst target mean | 452.65 USD（+24.6%） | n/a | n/a | 上行空間 |
| EPS surprise (最近 2 季) | -21.0%、-30.0% | n/a | n/a | 偏弱 |
| Short % of float | 10.9% | 月增 +83% | 約 3–6%（估計） | 偏高且增加 |
| Insider net sales (6M，USD) | -23.4M（4 筆公開市場賣出） | n/a | n/a | 占市值 0.15%，偏弱訊號 |
| Institutional top-10 holding | 約 40.1%（13F 2026-09-30 加總） | n/a | n/a | 集中度中高 |
| Beta | 1.58 | n/a | 約 0.8–1.2（估計） | 高波動 |

## Red flags

- 獲利結構弱化：FY2025 營業利益僅 16M USD、淨利 -219M USD，EBIT 對利息覆蓋 0.45x，利息負擔不足以由營業獲利支應。
- 股票型薪酬暴增：SBC 由 33M 增至 526M USD，扣除後 FY2025 FCF 為負（約 -28M USD）。
- 槓桿快速攀升：FY2025 Total Debt 由 3.0B 增至 6.8B USD；info 最新 totalDebt 9.57B USD，Debt/Equity 約 6x，股東權益 1.09B USD 相對薄弱。
- 流動性指標偏緊：info current ratio 0.89、quick ratio 0.50（2026-09-30）。
- ROE 與 ROIC 皆為低值或負值，資本效率未見改善跡象。
- 近兩季 EPS 大幅不及預期（-21%、-30%），且 FY2024 獲利依賴 886M USD 出售事業收益，獲利品質不穩。
- 內部人近期賣出：COO Berryman 於 2026-11-17 賣出 56,091 股（19.8M USD），為 6 個月內最大宗；賣出金額相對市值小（0.15%），成交價接近目前價位。
- 空單比例快速上升：shortPercentOfFloat 10.9%，較前月增加約 83%。
- 股價波動大：beta 1.58，當日 +9.1%，且 52 週區間 279.77–449.84，波動區間大。
- 資料品質警示（需在下游使用時注意）：
  - info 與 fast_info 為 cache，價格為盤中價。
  - info bid 382.72 高於 ask 318.13，報價為異常值，未採用。
  - institutional percent held 114.7%，超過 100%，未採用。
  - 2021–2022 財報中 diluted average shares（450,000）與 Diluted EPS（如 -2,864 USD）明顯異常，未採用這兩年 EPS。
  - info TTM revenue（4.48B）與 FY2025 revenue（2.63B）差距大，無季度資料可核對。
  - info EV（23.74B）與直接計算值（約 25.03B）不一致。
  - 本報告未取得 quarterly_fin、quarterly_bs、quarterly_cf、guidance 與 segment 資料，相關項目標示 n/a。

FUNDAMENTALS REPORT COMPLETE
