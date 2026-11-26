# Fundamentals — APD (Air Products and Chemicals, Inc.) as of 2026-11-27

資料說明: 價格與 info 欄位來源為 repo cache (`source: cache`, cached_at 2026-11-26T16:45 UTC), 屬預期行為。財報為 FY2026 (截至 2026-09-30) 年度與季度資料, 最近一次財報為 2026-11-05 (FQ4 FY26), 早於 as-of 日期, 無 post-date 資料。金額單位: USD B (十億美元) 與 USD M (百萬美元); 本報告未使用 億 單位。

## Executive summary
APD 核心業務獲利能力穩定 (FY26 營業利益率 24.4%、營收年增 7.9%), 但 FY26 GAAP 淨利僅 USD 0.53B (淨利率 4.1%), 主因約 USD 3.15B 非經常性損失, 且 net debt 達 USD 16.45B (約 3.0x 正規化 EBITDA), FCF 僅 USD 0.48B, 不足以覆蓋 USD 1.60B 股息, 財務健康度評為中性偏弱。估值方面, GAAP trailing P/E 131.5x 已失真; 以調整後 EPS 估算 trailing P/E 約 23.4x、forward P/E 20.2x, 股價 USD 314.26 低於分析師平均目標價 USD 346.95 約 10.4%, 估值屬中性偏貴、並非明顯便宜。

## Revenue & profitability

**營收趨勢 (USD B)**

| 年度 (FYE 9/30) | 營收 | YoY | 毛利率 | 營業利益率 | GAAP 淨利率 |
|---|---|---|---|---|---|
| FY2023 | 12.60 | n/a | 29.9% | 21.7% | 18.3% |
| FY2024 | 12.10 | -4.0% | 32.5% | 24.4% | 31.6% (含大額處分/非經常收益) |
| FY2025 | 12.04 | -0.5% | 31.4% | 24.0% | -3.3% (淨虧損 USD -0.39B) |
| FY2026 | 12.99 | +7.9% | 31.6% | 24.4% | 4.1% |

- 3 年 CAGR (FY23-FY26): 約 +1.0%。FY2022 資料為 n/a, 無法計算 3-5 年 CAGR。
- 最近一季 FQ4 FY26 (2026-09-30) 營收 USD 3.56B, YoY +12.3% (yfinance `info.revenueGrowth` 0.123 與此一致), 顯示 FY26 下半年成長加速。
- 季度營收: FQ1 FY26 USD 3.10B / FQ2 USD 3.17B / FQ3 USD 3.16B / FQ4 USD 3.56B。
- 分部營收 (segment mix): 工具資料未提供分部數字 (`longBusinessSummary` 僅列產品與終端市場, 無金額) → DATA_UNAVAILABLE。

**獲利品質**
- 毛利率與營業利益率在 FY24-FY26 大致穩定 (毛利率 31-33%, 營業利益率 24%), 核心營運未見惡化。
- GAAP 淨利與營業利益差距大: FY26 營業利益 USD 3.18B, 但 yfinance 認列 `Other Income Expense` USD -2.40B (包含 `Total Unusual Items` USD -3.15B), 使 pretax income 僅 USD 0.55B。
- 季度層面: FQ3 FY26 (2026-06-30) 單季 GAAP 淨損 USD -1.44B (EPS -6.47), 非經常性項目 USD -2.91B; 工具資料未揭示其認列原因 → 需查閱 10-Q/10-K 附註。
- yfinance 正規化淨利 (`Normalized Income`) FY26 為 USD 3.67B, FY25 為 USD 2.57B, 與 GAAP 差異巨大, 屬於 yfinance 自行調整值, 僅供參考。
- ROE: yfinance `info.returnOnEquity` 3.19% (GAAP)。以 FY26 GAAP 淨利 USD 0.53B 除以期末普通股權益 USD 14.28B 約 3.7%, 與 info 略有差異。以正規化淨利計算約 25.7%, 差距顯示 GAAP 與正規化獲利口徑差異極大。
- ROIC (自行估算): 以營業利益 USD 3.18B、平均 invested capital USD 32.39B 計, 稅前 ROIC 約 9.8%; 若假設稅率 21%, 稅後約 7.7% (稅率為本報告假設值, 非工具資料)。

## Cashflow & balance sheet

**現金流 (USD B)**

| 項目 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| 營運現金流 (OCF) | 3.21 | 3.65 | 3.26 | 4.68 |
| 資本支出 (Capex) | -4.63 | -6.80 | -7.02 | -4.20 |
| 自由現金流 (FCF = OCF - Capex) | -1.42 | -3.15 | -3.77 | 0.48 |
| FCF margin | -11.3% | -26.0% | -31.3% | 3.7% |
| FCF / GAAP 淨利 | -0.62x | -0.82x | NM | 0.90x |

- FY26 FCF 由負轉正, 主要來自 Capex 自 FY25 的 USD 7.02B 降至 USD 4.20B (-40%), 而非 OCF 大幅成長 (OCF 增 +44%, 但 FQ1 FY26 OCF 僅 USD 0.90B, 後三季逐季改善)。
- FCF / GAAP 淨利 為 0.90x, 數字上接近 0.9 門檻, 但 GAAP 淨利含大額非經常性損失, 以正規化淨利 USD 3.67B 計算僅 0.13x, 盈餘品質需保守看待。
- 季度 FCF: FQ1 FY26 USD -0.35B、FQ2 USD -0.00B、FQ3 USD +0.31B、FQ4 USD +0.52B, 下半年轉正趨勢明顯。

**資產負債表 (USD B, 2026-09-30)**
- 現金及約當現金: USD 1.33B (FY25: USD 1.86B, -28%)。
- Total debt: USD 18.30B (FY25: USD 18.41B), 其中 long-term debt USD 16.78B、current debt USD 1.00B。
- Net debt: USD 16.45B (FY25: USD 15.84B, +3.8%)。Net debt / 正規化 EBITDA (USD 5.45B) 約 3.0x; 以 yfinance `info.ebitda` USD 4.68B 計約 3.5x。
- Current ratio: 1.07x (流動資產 USD 5.02B / 流動負債 USD 4.71B), FY25 為 1.38x; working capital 由 USD 1.61B 降至 USD 0.31B。
- Debt / Equity: yfinance `info.debtToEquity` 107.7%。以 total debt / 總權益 (含少數股東權益) 計 106.7%, FY25 為 106.1%。
- 少數股東權益 (Minority Interest) 由 FY23 USD 1.35B 增至 FY26 USD 2.87B, 代表子公司合夥人出資增加; EV 計算應納入。
- 商譽加無形資產 USD 1.21B, 有形帳面價值 USD 13.07B (FY25 USD 13.77B)。
- 利息覆蓋: 營業利益 / 利息費用 = 3,175 / 220 ≈ 14.4x, 利息負擔可控。

## Capital allocation & insider signal

**資本支出**
- Capex 走勢: FY23 USD 4.63B → FY24 USD 6.80B → FY25 USD 7.02B → FY26 USD 4.20B; 占營收比由 FY24 56% 降至 FY26 32%。
- 季度 Capex 持續下降: FQ4 FY25 USD 1.52B → FQ1 FY26 USD 1.25B → FQ2 USD 1.11B → FQ3 USD 1.00B → FQ4 FY26 USD 0.85B。
- 工具資料未提供未來 capex 指引 → DATA_UNAVAILABLE。

**股東報酬**
- 股息: FY26 股息支付 USD 1.60B (約 USD 7.20/股, 以期末股數估算), `info.dividendYield` 2.3%。
- 股息覆蓋率: 以 FCF 計 0.30x (不足); 以 OCF 計 2.92x; 以正規化淨利計 2.29x; 以 GAAP 淨利計 0.33x。yfinance `payoutRatio` 為 302% (GAAP 口徑)。
- 買回 (buyback): 現金流量表未出現 repurchase 欄位 → n/a (工具資料無買回紀錄)。
- 股本: 流通股數約 222.7M, 近三年大致持平。Share Issued 由 249.46M 降至 222.69M, 與庫藏股數量 (約 26.8M) 相符, 推測為庫藏股註銷 (本報告推論, 未經公告文件確認)。
- 負債: FY26 發行債務 USD 0.83B、償還 USD 0.69B, 相較 FY25 發行 USD 4.39B 大幅縮減, 負債規模持平。

**內部人交易 (最近 6 個月, 2026-05-27 至 2026-11-26)**
- 買入: 0 筆。
- 賣出: 1 筆 — KURT LEFEVERE (Officer) 2026-11-16 賣出 450 股, 價格 USD 316.86, 金額約 USD 0.14M。
- 淨額: 約 USD -0.14M。占市值 USD 69.98B 約 0.0002%, 訊號強度極弱。
- 工具回傳含 6 個月以外紀錄, 本報告已排除: CFO MELISSA N. SCHAEFFER 2026-05-01 賣出 2,714 股 (USD 0.82M); 10% 以上大股東 MANTLE RIDGE, L.P. 2026-02-12 賣出 70,175 股 (USD 19.94M, 價格 USD 284.21)。後者為較大規模減持, 屬歷史事件, 非近期訊號。
- 內部人持股 1.90% (yfinance major_holders), 機構持股 94.5% (機構數 2,246)。

## Valuation

**基礎數據**
- 股價: USD 314.26 (cache, 2026-11-26), 前收 USD 308.58, 日內高/低 USD 315.99 / 305.55。
- 52 週區間: USD 229.11 - 324.00, 目前位於區間約 90% 位置。
- 50 日均線 USD 297.91 (股價高於約 5.5%); 200 日均線 USD 293.70 (股價高於約 7.0%)。
- 市值: USD 69.98B (流通股 222.69M)。EV: USD 89.98B (含 total debt USD 18.46B、現金 USD 1.34B、少數股東權益 USD 2.87B)。
- Beta: 0.67 (低波動)。

**估值倍數**

| 指標 | 數值 | 計算 / 口徑 |
|---|---|---|
| Trailing P/E (GAAP) | 131.5x | EPS USD 2.39, 受非經常性損失扭曲, 不具參考性 |
| Trailing P/E (調整後) | 約 23.4x | FY26 四季調整後 EPS 合計 USD 13.44 (3.16+3.20+3.47+3.61) |
| Trailing P/E (正規化) | 約 19.1x | 正規化淨利 USD 3.67B / 222.9M 股 ≈ USD 16.48 |
| Forward P/E | 20.2x | forwardEps USD 15.54 (yfinance 預估) |
| EV/EBITDA (info) | 19.2x | info EBITDA USD 4.68B |
| EV/EBITDA (正規化) | 約 16.5x | 正規化 EBITDA USD 5.45B |
| P/FCF | 約 146.8x | 市值 USD 69.98B / FCF USD 0.48B |
| P/S (trailing) | 5.39x | info priceToSalesTrailing12Months |

- 同業中位數 (sector median) 工具未提供, 以下為估計值 (非工具資料, 僅供參考): forward P/E 約 18-22x、EV/EBITDA 約 14-18x、P/S 約 3-5x。以此估計, APD 的 forward P/E 與 EV/EBITDA 位於區間中段偏上, P/S 偏高。
- 分析師: 21 位, 推薦 key 為 buy, 平均目標價 USD 346.95 (較現價 +10.4%)。

## Key catalysts
- 最近一次財報: 2026-11-05 (FQ4 FY26), 調整後 EPS USD 3.61, 與預估 USD 3.61 持平 (surprise -0.02%)。
- 下次財報: 2027-01-29 (yfinance 列示), 預估 EPS USD 3.43 (FQ1 FY27)。
- 財報歷史: 最近 9 季 (2024-11 至 2026-11) 中 7 季超預期, 1 季低於預期 (2025-05, -4.86%), 1 季持平 (2026-11, -0.02%)。FQ2 FY26 (2026-04) 超預期 4.54%, FQ3 FY26 (2026-07) 超預期 3.8%。
- 公司官方 FY27 指引 (guidance): 工具資料未提供 → DATA_UNAVAILABLE。
- 分部與專案進展 (hydrogen 專案等): 工具資料僅有業務描述, 無金額與時程 → DATA_UNAVAILABLE。
- 非經常性損失來源 (FQ3 FY26 USD -2.91B): 工具資料未揭示 → 需檢視 10-Q/10-K。
- Capex 下降能否持續 (FQ4 FY26 USD 0.85B) 是 FCF 能否覆蓋股息的關鍵。

## Metrics table

金額單位標示於欄位: USD B = 十億美元, USD M = 百萬美元。同業中位數為估計值, 非工具資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY26, USD B) | 12.99 | +7.9% | 約 0-5% 成長 (估計) | 中性, 成長回升 |
| 毛利率 (FY26) | 31.6% | +0.2pp | 約 30-35% (估計) | 中性 |
| 營業利益率 (FY26) | 24.4% | +0.4pp | 約 15-20% (估計) | 優於一般化工 (估計) |
| GAAP 淨利率 (FY26) | 4.1% | +7.4pp (由 -3.3%) | 約 8-10% (估計) | 偏弱, 受非經常性損失影響 |
| ROE (yfinance, GAAP) | 3.19% | n/a | 約 10-12% (估計) | 偏弱 |
| ROIC (自行估算, 稅前) | 9.8% | n/a | 約 8-9% (估計) | 中性 |
| FCF (FY26, USD B) | 0.48 | 由 -3.77 轉正 | 正值 (估計) | 改善中, 規模仍小 |
| FCF margin | 3.7% | 由 -31.3% | 約 5-8% (估計) | 偏弱 |
| FCF / GAAP 淨利 | 0.90x | n/a | 約 1.0x (估計) | 邊緣 |
| 現金 (USD B) | 1.33 | -28% | n/a | 偏低 |
| Net debt (USD B) | 16.45 | +3.8% | n/a | 偏高 |
| Net debt / 正規化 EBITDA | 3.0x | 由 3.1x | 約 2.5-3.0x (估計) | 偏高 |
| Current ratio | 1.07x | 由 1.38x | 約 1.2-1.5x (估計) | 偏弱 |
| Total debt / equity (含 MI) | 106.7% | +0.6pp | n/a | 偏高 |
| Capex (FY26, USD B) | 4.20 | -40.1% | n/a | 投資期結束, 轉向收割 |
| 股息覆蓋率 (FCF) | 0.30x | n/a | 約 1.0x 以上 (估計) | 不足 |
| 股息覆蓋率 (正規化淨利) | 2.29x | n/a | 約 1.5-2.5x (估計) | 尚可 |
| 股息殖利率 | 2.3% | n/a | 約 2-3% (估計) | 中性 |
| 買回 (FY26) | n/a | n/a | n/a | DATA_UNAVAILABLE |
| 內部人 6 個月淨額 (USD M) | -0.14 (賣出) | n/a | n/a | 訊號極弱 |
| Trailing P/E (GAAP) | 131.5x | n/a | n/a | 不具參考性 |
| Trailing P/E (調整後) | 約 23.4x | n/a | 約 25x (估計) | 中性偏貴 |
| Forward P/E | 20.2x | n/a | 約 18-22x (估計) | 中性 |
| EV/EBITDA (info / 正規化) | 19.2x / 16.5x | n/a | 約 14-18x (估計) | 中性偏貴 |
| P/FCF | 約 146.8x | n/a | n/a | 偏貴 |
| P/S (trailing) | 5.39x | n/a | 約 3-5x (估計) | 偏高 |
| 分析師平均目標價 (USD) | 346.95 (+10.4%) | n/a | n/a | 正面 |
| Beta | 0.67 | n/a | n/a | 低波動 |

## Red flags
- FY26 GAAP 淨利 USD 0.53B 與正規化淨利 USD 3.67B 差距達 USD 3.1B, 連續兩年 (FY25 USD -3.77B、FY26 USD -3.15B) 出現大額非經常性項目, 盈餘品質需查證 (工具未揭示原因)。
- FQ3 FY26 單季 GAAP 淨損 USD -1.44B (EPS -6.47), 為一次性事件或潛在減損待確認。
- 股息 USD 1.60B 遠高於 FCF USD 0.48B, 股息覆蓋依賴 OCF 與資產處置; GAAP payout ratio 302%。
- Net debt / 正規化 EBITDA 約 3.0x, 負債權益超過 100%, 且 net debt 較 FY25 增加。
- 現金 USD 1.33B、current ratio 1.07x、營運資金 USD 0.31B, 短期流動性偏緊 (但 FY26 OCF USD 4.68B 可支撐)。
- 少數股東權益由 USD 1.35B 增至 USD 2.87B (FY23-FY26), 代表外部權益資本增加。
- 資料不一致: yfinance `info.freeCashflow` 為 USD -0.29B, 與財報計算 FCF USD +0.48B 不符; `info.ebitda` USD 4.68B 與財報正規化 EBITDA USD 5.45B 不同; `info.returnOnEquity` 3.19% 與自行計算約 3.7% 不同。本報告以財報原始數據為主。
- 大型持股者減持: MANTLE RIDGE (10% 以上) 2026-02-12 減持約 USD 19.9M, 非近期事件但屬重要歷史紀錄。
- DATA_UNAVAILABLE 項目: 分部營收、公司指引 (guidance)、資本支出指引、買回紀錄、FQ3 FY26 非經常性損失原因、同業中位數實際數字。

FUNDAMENTALS REPORT COMPLETE
