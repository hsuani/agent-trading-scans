# Fundamentals — INTC as of 2026-10-11

資料說明: 金額單位為十億美元 (B)。資料來源為 pipeline/tools/yf 輸出 (yfinance 快取, cached_at 2026-10-11)。最近交易日收盤價 104.70 (2026-10-11 為週日, 最近交易日為 10-09)。最新已公布季報為 2026-06-30 (Q2'26)。未出現任何晚於 DATE 的已公布財務數據; 下一次財報日 2026-10-29 為未來事件。

## Executive summary
INTC 財務體質在 2026 年 Q2 單季明顯轉好 (營收 16.13B, YoY +25.4%, 毛利率 40.4%, 營業利益 1.97B), 但 TTM 淨損 -11.29B (淨利率 -19.8%), 2025 年自由現金流為 -4.95B, 股本 YoY 增加約 15%, 且 Q2 的非營業損失 (Other Income Expense -12.74B) 主導了單季淨損, 整體仍屬弱勢。估值面 forward P/E 50.3x、EV/EBITDA 33.5x、P/S 9.7x、P/B 6.0x, 相對半導體同業估計中位數明顯溢價, 而 ROE 為負、ROIC 估計僅約 2.5%, 估值合理性取決於營運獲利能否在 2026-10-29 Q3 財報中延續。內部人近 6 個月公開市場以 CEO 於 2026-08-11 以 $95 買入約 $10.0M 為主, 淨買入約 $3.5M, 占市值比例極小, 不構成強烈方向性訊號。

## Revenue & profitability

**營收趨勢**
- 年度營收: 2022 63.05B → 2023 54.23B (-14.0%) → 2024 53.10B (-2.1%) → 2025 52.85B (-0.5%)。
- 2022–2025 三年 CAGR 約 -5.7%。yfinance 年度損益表僅提供 2022–2025, 2021 欄位為 null, 無法計算 4–5 年 CAGR。
- 季度營收: Q2'25 12.86B → Q3'25 13.65B → Q4'25 13.67B → Q1'26 13.58B → Q2'26 16.13B。Q2'26 YoY +25.4% (info.revenueGrowth 0.254 一致), 為單季明顯跳升。
- TTM 營收 57.03B (與 info.totalRevenue 57.03B 一致)。
- 分部營收: DATA_UNAVAILABLE。longBusinessSummary 僅列出 CCG (client computing)、DCAI (data center & AI)、Intel Foundry 三大分部, 未提供分部營收數字。

**毛利率 / 營業利益率 / 淨利率**
- 毛利率 (年度): 2022 42.6% → 2023 40.0% → 2024 32.7% → 2025 34.8%。
- 毛利率 (季度): Q2'25 27.5% → Q3'25 38.2% → Q4'25 36.2% → Q1'26 39.4% → Q2'26 40.4%, 近三季持續回升。
- TTM 毛利率約 38.6% (自算, 季度毛利加總 22.02B / TTM 營收 57.03B); info.grossMargins 為 38.9%。
- 營業利益率 (年度, GAAP 營業利益): 2022 3.7% → 2023 0.1% → 2024 -8.9% → 2025 0.0% (營業利益 -0.02B)。
- 營業利益率 (季度): Q2'25 -10.0% → Q3'25 6.3% → Q4'25 4.0% → Q1'26 6.9% → Q2'26 12.2%。注意 info.operatingMargins 12.19% 與 Q2'26 單季數字相同, 並非 TTM 數字; TTM 營業利益 4.31B, 營業利益率約 7.6% (自算)。
- 淨利 (common stockholders): 2022 8.01B (12.7%) → 2023 1.69B (3.1%) → 2024 -18.76B (-35.3%) → 2025 -0.27B (-0.5%)。
- TTM 淨利 -11.29B, 淨利率 -19.8% (與 info.profitMargins 一致)。
- Q2'26 淨利 -11.03B (淨利率 -68.4%), 其中 Other Income Expense 為 -12.74B (稅前淨損 -10.82B), 營業層級是正的。此非營業項目的性質需以 10-Q 附註確認 (yfinance 欄位 Gain On Sale Of Security -12.48B 為最大組成)。
- 費用結構: R&D 2025 13.77B (26.1% 營收), 2022 為 17.53B; SG&A 2025 4.62B, 2022 為 7.00B。TTM R&D 約 13.19B (23.1%), 費用持續收斂。
- EPS: 年度 GAAP diluted EPS 2022 1.94 → 2023 0.40 → 2024 -4.38 → 2025 -0.06; TTM -2.12 (info.trailingEps)。
- ROE: -10.7% (info.returnOnEquity)。ROIC: 自算約 2.5% (TTM 營業利益 4.31B × (1-21%) ÷ 2026-06-30 投入資本 138.08B), 屬估計值。
- info.returnOnAssets 為 +1.41%, 與負淨利方向不一致, 判定為 provider 口徑差異, 不採用。

## Cashflow & balance sheet

**現金流品質**
- 營運現金流 (OCF): 2022 15.43B → 2023 11.47B → 2024 8.29B → 2025 9.70B。
- 資本支出 (Capex): 2022 24.84B → 2023 25.75B → 2024 23.94B → 2025 14.65B (2025 YoY -38.8%)。
- 自由現金流 (FCF, OCF − Capex): 2022 -9.41B → 2023 -14.28B → 2024 -15.66B → 2025 -4.95B。年度 FCF 連續四年為負。
- FCF margin: 2025 -9.4%, 2024 -29.5%。
- TTM OCF 14.94B (與 info.operatingCashflow 一致), TTM capex 12.11B, TTM FCF 2.83B, FCF margin 約 5.0% (自算)。info.freeCashflow 為 4.87B, 與季度加總不一致, 本報告以季度報表加總為準。
- 季度 FCF: Q3'25 0.12B → Q4'25 0.80B → Q1'26 -2.54B → Q2'26 4.45B, 波動大。
- FCF / NI: 不具意義 (NI 為負, 2023 年 FCF 為負而 NI 為正)。品質判定為不健康: 盈餘轉現金能力未達 0.9 門檻。

**資產負債表 (2026-06-30, Q2'26)**
- 現金及約當現金 12.87B; 現金加短期投資 29.73B (info.totalCash 29.73B 一致)。
- 總負債 (Total Debt) 50.54B, 其中長期負債 48.55B, 流動負債 1.99B。
- 淨負債 (Net Debt) 37.66B。季度走勢: 2025 YE 32.32B → Q1'26 27.78B → Q2'26 37.66B, 單季上升約 9.9B。
- 淨負債 / TTM EBITDA: 約 2.2x (以 info.ebitda 16.84B 計); 以季度 normalized EBITDA TTM 18.14B 計約 2.1x (自算)。
- 利息保障倍數: TTM 營業利益 4.31B ÷ TTM 利息費用 1.15B ≈ 3.7x (自算)。若以 GAAP EBIT 計則為負。
- 流動比率 1.60 (流動資產 57.21B ÷ 流動負債 35.67B; info.currentRatio 1.604 一致); 速動比率 1.16 (info.quickRatio)。
- 負債權益比: 49.0% (info.debtToEquity 49.0, 以含少數股權之總權益 103.14B 計); 若以歸屬股東權益 87.54B 計為 57.7% (自算)。
- 股東權益 (歸屬母公司) 由 2025 YE 114.28B 降至 2026-06-30 的 87.54B, 6 個月減少約 26.7B (-23%)。同期 Retained Earnings 由 48.98B 降至 33.84B。
- 少數股權 (Minority Interest) 由 2025 YE 12.08B 增至 15.60B。
- 商譽 (Goodwill) 由 2025 Q3 23.91B 降至 2026 Q1 20.47B, 單季減少約 3.45B, 同季 yfinance 欄位 Write Off 為 4.03B, 與減損有關的推論需以 10-Q 確認。Q2'26 Asset Impairment Charge 4.22B。
- 有形帳面價值 (Tangible Book Value) 64.53B (Q2'26), 2025 YE 為 87.60B。
- 營運資金 21.54B (Q2'26), 2026 Q1 為 35.27B, 下降明顯。
- 總資產 202.44B; 總負債 99.30B。

## Capital allocation & insider signal

**資本配置**
- 股利: 2022 5.997B → 2023 3.088B → 2024 1.599B → 2025 0 (未配息); 2026 H1 無配息。目前 dividendYield 0.0%、payout ratio 0.0%。股利覆蓋率: n/a (已停發)。
- 庫藏股 (Buyback): 2021 2.42B, 2022 至 2025 無買回。目前無回購。
- 股權融資: 2023 發行股本 1.51B; 2024 發行股本 12.71B (Issuance Of Capital Stock)。2025 年 yfinance 另列 Proceeds From Stock Option Exercised 13.48B, 性質需以 10-K 確認 (本報告未採信為發行股本)。
- 流通股數: 2024 YE 4.33B → 2025 YE 4.99B → 2026 Q1 5.02B → 2026 Q2 5.04B。Q2'26 vs Q2'25 (4.38B) 增加約 15.2%。Diluted average shares Q2'26 5.10B, 較 Q2'25 (4.37B) 增加約 16.8%。股東稀釋明顯。
- Capex / 營收: 2025 27.7%, 2024 45.1%, 2023 47.5%。TTM Capex / 營收 21.2%。Capex / D&A (2025) 約 1.25x (D&A 11.71B)。資本支出仍高於折舊, 但已明顯收斂。
- Net debt 增加與 Q2'26 籌資現金流: 借款淨增 4.67B (Net Issuance Payments Of Debt), 其他籌資項目 -12.01B (Net Other Financing Charges, 性質待確認), 籌資現金流合計 -7.34B。

**機構持股 (2026-06-30 資料, inst_holders)**
- 機構持股比例 62.6% (4,422 家機構); 內部人持股 14.0% (heldPercentInsiders)。
- 前十大: BlackRock 8.46% (季減 -4.7%)、Vanguard Capital Management 5.65% (+1.1%)、State Street 4.30%、Nvidia 4.26% (214.8M 股, 持平)、Invesco 3.13%、Geode 2.19%、FMR 1.87% (季增 +64.2%)、Vanguard Portfolio Management 1.77%、SoftBank 1.72% (86.96M 股, 持平)、Primecap 1.49% (季減 -0.7%)。
- 做空: 空單 167.2M 股, 占流通股 3.16% (shortPercentOfFloat), shortRatio 1.58 日, 空單較上月增加約 9.8%。

**內部人交易 (近 6 個月: 2026-04-11 至 2026-10-11)**
| 日期 | 人員 | 類型 | 股數 | 金額 | 備註 |
|---|---|---|---|---|---|
| 2026-08-11 | Lip-Bu Tan (CEO) | 買入 @ $95.00 | 105,263 | $10.00M | 間接持有 (Ownership I), 公開市場買入 |
| 2026-07-30 | N. Chandrasekaran (CTO) | 無價格紀錄 | 33,007 | n/a | 性質待 Form 4 確認 |
| 2026-06-01 | David Zinsner (CFO) | 無價格紀錄 | 37,015 | n/a | 性質待 Form 4 確認 |
| 2026-05-29 | N. Chandrasekaran (CTO) | 賣出 @ $118.28 | 21,024 | $2.49M | 直接持有 |
| 2026-05-07 | 多位董事 | 無價格紀錄 (年度董事授予) | 2,730–26,611 股/人 | n/a | 性質待 Form 4 確認 |
| 2026-05-01 | April Miller Boise (Officer) | 賣出 @ $99.53 | 40,256 | $4.01M | 直接持有 |
| 2026-04-30 | N. Chandrasekaran | 無價格紀錄 | 33,008 | n/a | 性質待 Form 4 確認 |

- 近 6 個月有價格的公開市場交易: 買入 1 筆 $10.00M (CEO); 賣出 2 筆合計 $6.49M (CTO + Officer)。淨買入約 $3.5M。
- 相對市值 553.46B: 買入占比約 0.0018%、賣出占比約 0.0012%、淨買入占比約 0.0006%。規模極小, 信號強度低。
- 無價格紀錄的多筆交易 (授予、歸屬、稅務扣繳等) 無法判定為買或賣, 本報告不納入淨值計算。
- 2025 年 (2025-05 至 2025-12) 同類型交易以無價格紀錄為主, 未見大規模內部人公開市場賣出。

## Valuation

以 regularMarketPrice 104.70、市值 553.46B、企業價值 (EV) 564.52B 計算。
- Trailing P/E: n/m (TTM EPS -2.12)。
- Forward P/E: 50.3x (forwardEps 2.08)。2026 年 calendar EPS 估計 1.52, 對應 P/E 68.8x (priceEpsCurrentYear)。
- PEG: 1.36 (info.pegRatio)。
- EV/EBITDA: 33.5x (info.enterpriseToEbitda, EBITDA 16.84B); 以季度 normalized EBITDA TTM 18.14B 計約 31.1x (自算)。
- EV/Revenue: 9.9x (info.enterpriseToRevenue)。P/S (TTM): 9.7x。
- P/B: 6.0x (bookValue/share 17.36)。
- P/FCF: 以季度加總 TTM FCF 2.83B 計約 195.5x; 以 info.freeCashflow 4.87B 計約 113.7x。兩者差異大, 本報告以季度報表為準。
- 52 週區間 32.89–142.35; 現價較 52 週高點低 26.4%, 較 52 週低點高 218%; 52 週漲幅 +181.3%。
- 技術位置 (fast_info): 50 日均線 103.08、200 日均線 83.03, 現價位於兩線之上。Beta 2.23。
- 分析師 (43 家): 平均目標價 118.05 (+12.7%), 中位數 115.00 (+9.8%), 最高 200.00, 最低 80.00; recommendationMean 2.47 (偏買進)。

**同業中位數 (估計, 非工具取得)**: 半導體同業 forward P/E 約 25–35x、EV/EBITDA 約 18–25x、P/S 約 5–8x、P/B 約 4–6x。

## Key catalysts
- **下次財報**: 2026-10-29 (earnings_dates, 時間戳 2026-10-29 20:00 UTC)。Q3'26 EPS 一致預期 0.39 (yfinance 為調整後口徑)。
- **上次財報 (Q2'26, 2026-07-23)**: 調整後 EPS 0.42 vs 預期 0.22 (+94.6%)。GAAP diluted EPS 為 -2.16, 兩者口徑不同, 需於解讀時分開。
- **財測 / 指引**: DATA_UNAVAILABLE (工具未提供管理層指引文字)。
- **分部變化**: DATA_UNAVAILABLE (無分部營收數據)。
- **策略合作**: longBusinessSummary 提及與 Infosys 合作建置多層 AI fabric。影響幅度無法由工具量化。
- **內部人**: CEO 於 2026-08-11 以 $95 公開買入 (約 $10.0M)。
- **治理 / 風險分數**: overallRisk 7、compensationRisk 9、auditRisk 8 (yfinance 治理評分, 1–10, 越高風險越高)。
- **資本結構事件**: Q2'26 借款淨增 4.67B、淨負債升至 37.66B; 後續再融資或資產處置動態需追蹤 10-Q。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM) | 57.03B | Q2'26 +25.4%; FY25 -0.5% | 估計 +5~10% | 單季改善, 年度仍負成長 |
| 毛利率 (TTM) | 38.9% (info) / 38.6% (自算) | Q2'26 40.4% vs Q2'25 27.5% | 50–55% | 劣於同業, 回升中 |
| 營業利益率 (TTM) | 7.6% (自算); Q2'26 單季 12.2% | FY25 0.0% vs FY24 -8.9% | 15–25% | 劣於同業, 改善中 |
| 淨利率 (TTM) | -19.8% | FY25 -0.5% (FY24 -35.3%) | 10–20% | 明顯劣勢 |
| ROE | -10.7% | n/a | 15–25% | 劣勢 |
| ROIC | ~2.5% (自算) | n/a | 8–12% | 劣勢 |
| FCF (TTM) | 2.83B (自算) | FY25 -4.95B | 為正且穩定 | 偏弱, 季度波動大 |
| FCF margin (TTM) | 5.0% (自算) | FY25 -9.4% | 15–20% | 偏弱 |
| FCF / NI | n/m | n/a | >0.9 | 不健康 (NI 為負) |
| 淨負債 | 37.66B | Q1'26 27.78B; YE25 32.32B | 視同業 | Q2 明顯上升 |
| 淨負債 / EBITDA | 約 2.2x | n/a | 1.0–2.0x | 略偏高 |
| 利息保障倍數 (TTM 營業利益) | 約 3.7x (自算) | n/a | 5x 以上 | 偏弱 |
| 流動比率 | 1.60 | n/a | 2.0–2.5x | 偏低 |
| 負債權益比 | 49.0% (含 MI) / 57.7% (歸屬) | 股東權益 YoY 約 -23% (自 YE25) | 30–50% | 略偏高 |
| Capex / 營收 | 21.2% (TTM) | FY25 27.7% vs FY24 45.1% | 8–12% | 重資產, 持續收斂 |
| 股利殖利率 | 0.0% | 2025 起停發 | 1–2% | 無配息 |
| 庫藏股 | 無 | 2022 起無 | n/a | 無回購 |
| 流通股數 | 5.04B (Q2'26) | +15.2% YoY | 視同業 | 稀釋明顯 |
| 內部人 6 個月淨交易 | 淨買入約 $3.5M | n/a | n/a | 規模小, 信號弱 |
| Forward P/E | 50.3x | n/a | 25–35x | 明顯溢價 |
| EV/EBITDA | 33.5x | n/a | 18–25x | 明顯溢價 |
| P/S (TTM) | 9.7x | n/a | 5–8x | 溢價 |
| P/B | 6.0x | n/a | 4–6x | 偏高 |
| P/FCF (TTM) | 約 195x (自算) / 114x (info) | n/a | 30–40x | 明顯溢價 |
| Beta | 2.23 | n/a | 約 1.2 | 高波動 |
| 分析師平均目標價 | 118.05 (+12.7%) | n/a | n/a | 分析師偏多 |
| 市值 | 553.46B | n/a | n/a | 大型股 |

## Red flags
- 淨損與非營業損失: Q2'26 Other Income Expense 為 -12.74B, 淨利 -11.03B; 單季獲利品質不能僅看營業面。
- 現金流未轉正: 年度 FCF 2022–2025 連續為負, TTM FCF 僅 2.83B (自算), 且季度波動大 (Q1'26 -2.54B)。
- 股本稀釋: 流通股數 YoY +15.2%, diluted shares YoY +16.8%; 2024 年融資 12.71B。
- 淨負債快速回升: Q1'26 27.78B → Q2'26 37.66B; 總負債 50.54B。
- 權益大幅縮減: 歸屬股東權益 2025 YE 114.28B → 2026-06-30 87.54B (約 -23%); 有形帳面價值 64.53B。
- 商譽與減損: 商譽 Q3'25 23.91B → Q1'26 20.47B; Q2'26 Asset Impairment Charge 4.22B。
- 少數股權擴大: 12.08B (YE25) → 15.60B (Q2'26), 歸屬股東獲利能力被稀釋。
- 估值溢價: forward P/E 50.3x、EV/EBITDA 33.5x、P/B 6.0x, 相對估計同業中位數顯著偏高。
- 股利停發, 無回購, 資本回報目前完全依賴股價與成長。
- 資料一致性問題 (已於本報告揭露並採取保守口徑):
  - info.freeCashflow 4.87B 與季度報表 TTM FCF 2.83B 不一致。
  - info.nonDilutedMarketCap 648.08B 隱含股數約 6.19B, 與 info.marketCap 553.46B 隱含股數 5.29B 不一致。
  - info.returnOnAssets +1.41% 與 TTM 淨損方向不一致。
  - earnings_dates 的 Reported EPS (調整後) 與報表 GAAP diluted EPS 口徑不同, 不可直接比較。
  - info.operatingMargins 12.19% 為 Q2'26 單季, 非 TTM。
- 內部人無價格交易多, 性質不明, 本報告無法判定其淨方向。
- 資料缺口 (DATA_UNAVAILABLE): 分部營收、管理層財測指引、4–5 年 CAGR (2021 年欄位缺失)、Q1'25 季度數據、同業中位數 (本報告所列為估計值)、內部人交易性質 (無價格紀錄者)。

FUNDAMENTALS REPORT COMPLETE
