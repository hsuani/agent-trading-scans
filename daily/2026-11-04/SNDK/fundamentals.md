# Fundamentals — SNDK as of 2026-11-04

> 資料截止：2026-11-03（價格取自 cnyes 快取，cached_at 2026-11-03T14:00 UTC）。yfinance 的 Cookie/crumb 取得失敗，但各表格資料皆有回傳；fast_info 來源為 `source: cache`。資料中未發現晚於 2026-11-04 的實際數據。
> 金額單位：USD B（十億美元）；本報告不含 TWD/KRW，故未使用 億。

## Executive summary
SanDisk 的 FY26（截至 2026-06-30）營收 20.25B USD、年增 175.3%，GAAP 淨利 11.43B USD，FCF 11.49B USD，資產負債表為淨現金（現金 4.76B USD、總負債僅 177M USD），財務體質目前極為健康。以 TTM EPS 125.12 計算，trailing P/E 僅 8.6x、forward P/E 3.7x，表面估值極低，但這反映市場對 NAND 高峰獲利可持續性的強烈折價，且股價自 52 週高點 2,354.39 USD 已回落 54%。6 個月內部人淨賣出約 130.3M USD（無公開市場買入），且資料中存在多處一次性收益與報價矛盾，需於後續研究中逐一確認。

## Revenue & profitability
**營收趨勢（USD B）**

| 年度 | Total Revenue | YoY | Gross Profit | Operating Income | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| FY23（2023-06-30） | 6.09 | n/a | 0.43 | -1.30 | -2.14 | -14.78 |
| FY24（2024-06-30） | 6.66 | +9.5% | 1.07 | -0.44 | -0.67 | -4.63 |
| FY25（2025-06-30） | 7.36 | +10.4% | 2.21 | 0.51 | -1.64 | -11.32 |
| FY26（2026-06-30） | 20.25 | +175.3% | 14.47 | 12.47 | 11.43 | 73.76 |

- 3 年 CAGR（FY23→FY26）為 49.3%。yfinance 未提供 FY22 之前的獨立年度資料，無法計算 4-5 年 CAGR，此處以 3 年 CAGR 替代。
- FY26 營收幾乎全部集中在 Q2–Q4 爆發：Q1 FY26（2025-09）2.31B、Q2（2025-12）3.03B、Q3（2026-03）5.95B、Q4（2026-06）8.97B（Q4 YoY 相對 Q4 FY25 的 1.90B 為 +371.6%）。
- 2026-10-02 結束的 FQ1 FY27 在 `info` 中可反推：`totalRevenue` 28.97B（TTM）減去 FY26 Q2–Q4 合計 17.94B，得 FQ1 FY27 營收約 11.03B（推導值，非直接欄位）。此值與 `info.revenueGrowth` 3.779（+378%）對 FQ1 FY26 的 2.31B 相符。
- 分部資料：yfinance 未提供分部拆分，`longBusinessSummary` 僅描述產品線（SSD、嵌入式快閃記憶體、可攜式卡、晶圓等），無金額比重，記為 DATA_UNAVAILABLE。

**獲利能力**

| 指標 | FY23 | FY24 | FY25 | FY26 | Q4 FY26 |
|---|---|---|---|---|---|
| Gross margin | 7.1% | 16.1% | 30.1% | 71.5% | 84.6% |
| Operating margin | -21.3% | -6.7% | 6.9% | 61.6% | 78.5% |
| Net margin | -35.2% | -10.1% | -22.3% | 56.5% | 77.0% |

- 毛利率由 FY25 的 30.1% 在一年內拉升至 FY26 的 71.5%，Q4 達 84.6%。這是 NAND 價格循環上行的直接結果，屬高度週期性的獲利，不應直接外推。
- Q4 FY26 淨利率 77.0% 含 `Gain On Sale Of Security` 808M USD（稅前，Q4 `Other Income Expense` 為 784M），非營業性質，若剔除則 Q4 淨利率會低於 77%（確切數字需公司財報）。
- ROE：FY26 以期末權益 15.74B USD 計為 72.7%，以平均權益（期初 9.22B、期末 15.74B）計為 91.6%。`info.returnOnEquity` 為 141%（TTM 基礎）。
- ROIC：以 NOPAT（EBIT 13.09B × (1 - 稅率 12%) = 11.52B）除以平均投入資本（期初 11.07B、期末 15.74B），約 86.0%；期末投入資本基礎為 73.2%。

## Cashflow & balance sheet
**現金流（USD B）**

| 項目 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Operating Cash Flow | -0.71 | -0.31 | 0.08 | 11.67 |
| Capex（Purchase of PPE） | -0.22 | -0.17 | -0.20 | -0.18 |
| Free Cash Flow | -0.93 | -0.48 | -0.12 | 11.49 |

- FCF margin（FY26）為 56.8%；FCF / 淨利 = 11.494 / 11.433 = 1.005，高於 0.9 的健康門檻。OCF / 淨利 = 1.02。
- 品質注意：FY26 OCF 中的營運資金項目包括 應收帳款增加 -3.64B 與 應付帳款 +2.01B、應付所得稅 +1.37B（應付所得稅餘額由 43M 升至 1,286M，屬時間性現金流優勢，未來會反轉）。應付所得稅佔 OCF 約 11.7%。
- Q4 FY26 OCF 7.13B，其中應收帳款變動 -1.98B；FQ3（2026-03）OCF 3.04B，應收帳款變動 -1.49B。
- Capex 僅占營收 0.87%（FY26 177M USD），資本密集度極低。`info` 並未提供 JV（合資）投資支出；產能是否透過合資架構持有需於公司財報中確認，本報告未依一般認知假設。
- SBC FY26 232M USD，占營收 1.15%。

**資產負債表（期末 2026-06-30，USD B）**

| 項目 | FY25（2025-06-30） | FY26（2026-06-30） |
|---|---|---|
| Cash & equivalents | 1.48 | 4.76 |
| Total debt | 2.04 | 0.18（僅租賃負債） |
| Net debt（Total debt - Cash） | 0.37 | -4.59（淨現金） |
| Accounts receivable | 1.07 | 4.71 |
| Inventory | 2.08 | 2.70 |
| Total assets | 12.99 | 22.51 |
| Goodwill | 5.00 | 4.99 |
| Stockholders' equity | 9.22 | 15.74 |
| Current ratio | 3.56 | 2.29 |
| Debt / Equity | 0.22 | 0.011 |

- `info` 的 `totalCash` 5.21B 與 `totalDebt` 0.20B 為最新季（2026-09-30）資料，對應淨現金約 5.0B USD。`info.currentRatio` 2.58、`debtToEquity` 1.108（此欄位定義與上表不同，yfinance 原始值，需注意）。
- 長期債務已於 FY26 大幅償還：Repayment of Debt 1.90B USD，Total debt 由 2.04B 降至 0.18B（Q3 FY26 季末為 1.54B → Q2 為 0.79B，逐季償還）。
- 投資資產 1.78B USD（Available for sale 證券，非流動），未計入上表淨現金。
- 營運資金風險：Accounts Receivable 由 1.07B 增至 4.71B（年增約 341%）；Inventory 由 2.08B 增至 2.70B。以 Q4 營收與成本推算，DSO 約 48 天（Q4 FY25 約 51 天），但 DIO 約 178 天（Q4 FY25 約 135 天）。存貨天數上升是週期高點的警訊。
- Net debt 與 Net cash：yfinance 原生 `Net Debt` 欄位在 2026-06-30 為 None，本表為推導值。

## Capital allocation & insider signal
- 股票回購：FY26 `Repurchase of Capital Stock` 4.52B USD（占 FCF 39.4%），Treasury stock 期末 4.54B USD。普通股股數由 2026-03-31 的 148M 降至 2026-06-30 的 146M；`info.sharesOutstanding` 最新為 142.29M，顯示回購持續進行。
- 股利：無（dividendYield 0.0，trailingAnnualDividendRate 0.0）。
- 債務：FY26 償還 1.90B USD，利息支出 73M USD（annual）。
- 稀釋：加權平均稀釋股數由 FY25 的 145M 升至 FY26 的 155M，主要受股價上漲後的 SBC 與可轉換/認股權效應影響（精確來源未由 yfinance 提供）。

**內部人交易（過去 6 個月，2026-05-04 至 2026-11-03）**
- 公開市場賣出共 13 筆，合計 83,524 股，金額約 130.28M USD（以 `Value` 欄加總），占市值 152.97B USD 的 0.085%。
- 最大賣方為 CEO David V. Goeckeler：2026-09-14 賣出 33,838 股（約 51.70M USD，價格 1,522.59–1,541.88），2026-09-17 賣出 33,841 股（約 53.27M USD，價格 1,567.26–1,587.00）。兩筆合計 67,679 股、約 104.97M USD。
- 其他賣方：CFO Visoso 2026-09-15 賣 1,000 股（1.57M USD）；CTO Ilkbahar 2026-09-03 賣 4,712 + 400 股（合計約 7.88M USD）；Officer Shek Bernard 多次小額賣出；Officer Pokorny 2026-05-12 賣 2,446 股（3.49M USD）。
- 公開市場買入：0 筆。
- 贈與（Stock Gift）3 筆（Caulfield 兩筆、Ilkbahar 一筆），不計入賣出。
- 授予股票（Stock Award）為 0 價，不計入買賣。
- 2026-08-20 Ilkbahar 276 股的交易類型與金額為空白，記為 DATA_UNAVAILABLE，未納入計算。
- 規模比較：6 個月賣出 83.5k 股約占內部人持股（heldPercentInsiders 1.10%，約 1.57M 股）的 5.3%。內部人賣出規模對市值而言仍小，但全部為賣出、無買入，且 CEO 於 9 月集中出脫，屬偏負面的訊號。是否為 10b5-1 計畫，yfinance 無法判定。

**機構持股與空方**
- 機構持股 84.14%（2,382 家）。前五大：BlackRock 7.12%（-1.0% QoQ）、Vanguard Capital 6.69%、FMR 5.44%（持股減少 41.3%）、State Street 4.10%、Invesco 3.88%（增加 381%）。
- 空方：sharesShort 4.70M（前月 5.62M，減少約 16%），shortPercentOfFloat 3.28%，shortRatio 0.55 日。空方壓力低。

## Valuation
**估值倍數（以 2026-11-03 價格 1,075.08 USD 計算）**

- 市值 152.97B USD（與 1,075.08 × 142.29M 股之乘積核對一致）；EV 147.97B USD。
- Trailing P/E：8.6x（TTM EPS 125.12）。以 FY26 GAAP 稀釋 EPS 73.76 計算為 14.6x。
- Forward P/E：3.7x（`forwardEps` 287.26）。
- 注意：TTM EPS 125.12 與 FY26 年度 GAAP EPS 73.76 不同，原因為 TTM 包含 FQ1 FY27 的 GAAP 稀釋 EPS 52.60；加總 Q2 5.15 + Q3 23.03 + Q4 43.97 + FQ1 FY27 52.60 = 124.75，與 125.12 誤差在 0.3% 內，故判定 TTM 口徑正確。
- P/FCF（TTM FCF 11.24B）：13.6x。
- P/S（TTM 營收 28.97B）：5.3x。
- EV/EBITDA（TTM EBITDA 21.21B）：7.0x。EV/Revenue 5.1x。
- P/B：8.5x（bookValue 125.93 USD）。

**Forward EPS 一致性檢查**
- 2027-02-15 下一次財報的 EPS 估計為 57.12。加上 FQ1 FY27 已公布的 49.51（調整後口徑），FY27（截至 2027-07-03）EPS 287.26 隱含 H2 FY27 需達約 180.6（約每季 90）。此為大幅上修或舊估計，需檢視分析師組成。

**股價與分析師**
- 最新價 1,075.08 USD，前收 1,150.89（-6.6%），當日區間 1,067.40–1,159.31，成交量 10.55M（10 日均量 9.13M）。
- 報價異常：bid 1,111.26 高於 ask 1,073.71，為交叉報價，不可靠；`fulldayPrice` 1,121.20 與 `currentPrice` 不一致，本報告以 `currentPrice` 與 `previousClose` 為準。
- 技術位置：50 日均線 1,547.49（價格低 30.5%）、200 日均線 1,262.50（價格低 14.8%）、52 週高點 2,354.39（低 54.3%）、52 週低點 183.00。
- 分析師（24 家）：recommendationMean 1.52（偏買入）；strongBuy 6、buy 11、hold 0、sell 0。目標價 mean 2,029.04、median 2,000、high 3,000、low 870；相對現價，平均目標價隱含 +88.7%，最低目標價隱含 -19.1%。

**產業中位數（估計）**：以下數字為 AI 估計值，非工具輸出，僅供參考。半導體/記憶體股 trailing P/E 約 25x、EV/EBITDA 約 14x、P/S 約 5x、P/B 約 4x、P/FCF 約 20x。

## Key catalysts
- 已發生：2026-10-29 FQ1 FY27 財報，調整後 EPS 49.51 vs 預估 46.41，超出 +6.69%（前一季 2026-08-05 超出 +13.72%；2026-04-30 超出 +59.67%；2026-01-29 超出 +74.97%）。連續四季超預期。
- 下一次財報：2027-02-15（預估 EPS 57.12），對應 FQ2 FY27。
- GAAP vs 調整後口徑差異：FQ4 FY26 GAAP 稀釋 EPS 43.97 vs earnings_dates 的 Reported EPS 39.25，差距約 4.7，接近 808M 證券利益除以稀釋股數 157M 的稅前值 5.15 扣除稅負後的水準（推論，需確認）。
- 股價與基本面背離：Q1 FY27 公布後股價仍在 1,067–1,159 區間震盪，且較 50 日均線下跌 30.5%，市場可能已將週期頂部納入定價。
- 資本配置：持續回購（股數 146M → 142.3M）、債務已基本清償，後續現金累積可能帶來更多回購或投資。
- 行業：NAND 價格與 AI 資料中心需求為最大變數（資料未含價格指標，記為 DATA_UNAVAILABLE）。

## Metrics table
| Metric | Latest | YoY / 變化 | Sector median（估計） | Verdict |
|---|---|---|---|---|
| Total Revenue FY26（USD B） | 20.25 | +175.3% | ~10%（YoY 估計） | 強勁，但屬週期性 |
| Revenue 3y CAGR FY23–26 | 49.3% | n/a | ~8%（估計） | 高 |
| Gross margin FY26 | 71.5% | +41.4 ppt | ~55%（估計） | 異常高，週期頂部風險 |
| Operating margin FY26 | 61.6% | +54.7 ppt | ~15%（估計） | 異常高 |
| Net margin FY26 | 56.5% | +78.8 ppt | ~10%（估計） | 含一次性收益，需調整 |
| ROE（FY26，平均權益） | 91.6% | n/a | ~18%（估計） | 極高（低基數效應） |
| ROIC（FY26，平均投入資本） | 86.0% | n/a | ~12%（估計） | 極高 |
| FCF margin FY26 | 56.8% | n/a | ~12%（估計） | 強 |
| FCF / 淨利 FY26 | 1.005 | n/a | ~0.8（估計） | 健康（>0.9） |
| Net cash（2026-06-30，推導） | +4.59B USD | 由 -0.37B 轉正 | n/a | 充裕 |
| Current ratio（2026-06-30） | 2.29 | 由 3.56 降 | ~2.0（估計） | 健康 |
| Debt / Equity（2026-06-30） | 0.011 | 由 0.22 降 | ~0.4（估計） | 極低 |
| Capex / Revenue FY26 | 0.87% | 由 2.8% 降 | ~8%（估計） | 資本輕，需確認 JV 結構 |
| Buyback FY26 | 4.52B USD | 由 0 增 | n/a | 積極 |
| Dividend yield | 0.0% | n/a | ~0.5%（估計） | 無股利 |
| SBC / Revenue FY26 | 1.15% | 由 2.4% 降 | ~5%（估計） | 低 |
| Trailing P/E（TTM EPS 125.12） | 8.6x | n/a | ~25x（估計） | 低，反映週期折價 |
| Forward P/E（EPS 287.26） | 3.7x | n/a | ~18x（估計） | 極低，需檢驗估計 |
| P/FCF（TTM） | 13.6x | n/a | ~20x（估計） | 低 |
| EV/EBITDA（TTM） | 7.0x | n/a | ~14x（估計） | 低 |
| P/S（TTM） | 5.3x | n/a | ~5x（估計） | 中性 |
| P/B | 8.5x | n/a | ~4x（估計） | 偏高（ROE 支撐） |
| 6 個月內部人淨交易 | 賣出 130.3M USD，買入 0 | n/a | n/a | 偏負面 |
| Short % of float | 3.28% | 空方股數 -16% | n/a | 低 |
| 機構持股比率 | 84.14% | n/a | n/a | 高 |
| 分析師平均目標價 | 2,029 USD（+88.7%） | n/a | n/a | 分歧大（870–3,000） |
| 股價距 52 週高點 | -54.3% | n/a | n/a | 動能偏弱 |

## Red flags
- 週期性極強：FY26 毛利率由 30.1% 跳升至 71.5%，FY26 營收為 FY25 的 2.75 倍。這類獲利在記憶體業通常為週期高峰，forward P/E 3.7x 不應被視為低估的確認。
- 一次性收益：Q4 FY26 含 808M USD 證券處分利益（Gain On Sale of Security），佔 Q4 稅前利益約 10%。GAAP 與調整後 EPS 差異（43.97 vs 39.25）印證此點。
- 應付稅款推升 OCF：應付所得稅由 43M 升至 1,286M，佔 FY26 OCF 約 11.7%，屬時間性優勢。
- 營運資金膨脹：應收帳款年增約 341%（1.07B → 4.71B），存貨天數由約 135 天升至約 178 天（推算值）。若需求放緩，存貨與應收可能成為減損或現金回收壓力來源。
- 內部人賣出集中：2026-09 CEO 與 CTO 合計賣出約 120M USD，且 6 個月內無任何公開市場買入。
- 股價動能：價格低於 50 日與 200 日均線，較 52 週高點回落 54.3%。
- 資料缺口與矛盾：yfinance cookie/crumb 失敗，多數資料取自快取；bid/ask 交叉；FQ1 FY27 在 quarterly_fin 中缺少營收與資產負債表（僅由 TTM 推導）；earnings_dates 的 Reported EPS 與 GAAP 稀釋 EPS 口徑不同；2026-08-20 內部人交易金額缺失；Forward EPS 287.26 隱含 H2 FY27 大幅成長，與季度估計不一致。
- 產業中位數全為估計值，非工具來源；結論需以實際同業資料校正。

FUNDAMENTALS REPORT COMPLETE
