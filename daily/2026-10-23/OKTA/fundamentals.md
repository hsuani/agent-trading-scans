# Fundamentals — OKTA as of 2026-10-23

## Executive summary
OKTA 財務體質已明顯改善：最新季 (2026-07-31，FY27 Q2) 營收 805M USD 年增 10.6%，GAAP 營業利益率轉為 13.3%，帳上現金與短期投資 2.30B USD 大於總債務 53M USD，屬淨現金公司。FCF 強勁但大部分被股權激勵 (SBC) 抵銷，GAAP ROE 僅 4.3%。估值明顯偏貴：forward P/E 47.7x、P/S 11.9x、P/FCF 約 35–38x，相對軟體基礎架構同業應屬高估值區間。結論：基本面品質提升、資產負債表穩健，但估值已充分反映成長預期。

## Revenue & profitability

**單位：USD B/M。** 資料來源為 yfinance (`pipeline/tools/yf OKTA financials / quarterly_fin / info`)。

**營收趨勢（年度，FY 於 1 月底結束）**
- FY23 (2023-01-31)：1,858M USD (1.86B)
- FY24 (2024-01-31)：2,263M USD (2.26B)，YoY +21.8%
- FY25 (2025-01-31)：2,610M USD (2.61B)，YoY +15.3%
- FY26 (2026-01-31)：2,919M USD (2.92B)，YoY +11.8%
- 3 年 CAGR (FY23→FY26)：約 16.3%。FY22 資料為 null，無 4 年 CAGR。
- 成長呈減速趨勢：21.8% → 15.3% → 11.8%。

**季度營收**
- 2026-07-31 (FY27 Q2)：805M USD，去年同季 728M USD，YoY +10.6%
- 2026-04-30 (FY27 Q1)：765M USD
- 2026-01-31 (FY26 Q4)：761M USD
- TTM 營收：3,073M USD (3.07B)，與 info.totalRevenue 3,072,999,936 一致

**業務組成**：yfinance 未提供分部營收。依 info.longBusinessSummary，產品線包括 Single Sign-on、Adaptive MFA、API Access Management、Universal Directory、Identity Governance (Lifecycle Management / Okta Workflows)、Privileged Access、Okta for AI Agents 等。分部營收 n/a。

**獲利能力（GAAP）**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | 淨利 (USD M) | 攤薄 EPS (GAAP) |
|---|---|---|---|---|---|
| FY23 | 70.6% | -42.1% | -43.9% | -815 | -5.16 |
| FY24 | 74.3% | -20.3% | -15.7% | -355 | -2.17 |
| FY25 | 76.3% | -2.4% | 1.1% | 28 | 0.06 |
| FY26 | 77.4% | 5.2% | 8.1% | 235 | 1.31 |

- FY26 淨利 235M USD 高於營業利益 153M USD，主因利息收入 110M USD (Interest Income) 與所得稅率僅 7.9%。
- 季度趨勢持續改善：2026-07 季毛利率 79.6% (641/805)，去年同季 76.9%；營業利益率 13.3% (107/805)，去年同季 5.6% (41/728)；淨利率 14.4% (116/805)。

**Non-GAAP EPS (earnings_dates 的 Reported EPS)**
- 2026-08-26 公布 FY27 Q2：1.05 vs 預估 0.96，超出 8.9%；YoY 0.91→1.05，+15.4%
- 2026-05-28 FY27 Q1：0.91 vs 0.85，超出 6.7%
- 2026-03-04 FY26 Q4：0.90 vs 0.85，超出 6.3%
- 2025-12-02 FY26 Q3：0.82 vs 0.76，超出 8.1%
- 連續多季 EPS 超預期，幅度約 6–9%。

**ROE / ROIC**
- ROE (info.returnOnEquity)：4.3%（GAAP TTM）
- ROIC（自行估算：FY26 營業利益 153M × (1 − 7.9%) ÷ 投入資本 7,349M）：約 1.9%。投入資本含大量現金，數值偏低屬正常，僅供參考。

## Cashflow & balance sheet

**現金流品質（單位：USD M）**

| 指標 | FY23 | FY24 | FY25 | FY26 | TTM (至 2026-07) |
|---|---|---|---|---|---|
| 營業現金流 | 86 | 512 | 750 | 884 | 987 |
| 資本支出 | -23 | -24 | -20 | -21 | -28 |
| 自由現金流 (FCF) | 63 | 488 | 730 | 863 | 959（自行計算：OCF − capex） |
| FCF margin | 3.4% | 21.6% | 28.0% | 29.6% | 31.2% |
| FCF / NI | 負值（不適用） | 負值（不適用） | 26.1（NI 僅 28M） | 3.67 | 3.24（TTM NI 296M） |
| SBC | 677 | 684 | 565 | 544 | 約 114+117+134+138 ≈ 503（季度加總，去年 Q2 起算口徑） |
| FCF − SBC | -614 | -196 | 165 | 319 | 約 456（以 TTM FCF 959 減 TTM SBC 約 503） |

- FCF/NI 遠高於 0.9 健康門檻，但主要原因是 SBC 為非現金費用，且 GAAP 淨利基數低。SBC 佔營收約 18.6% (FY26)，扣除 SBC 後 FY26 FCF 僅約 319M USD，FCF-SBC margin 約 10.9%。這是判讀現金流品質時最重要的修正。
- info.freeCashflow 為 1,037.6M，與季度加總的 959M 不一致（差約 79M），本報告以季度資料為準並註明差異。

**資產負債表（最新 2026-07-31，單位：USD M）**
- 現金及短期投資：2,299M（info.totalCash 2,299M 一致）
  - 現金及約當現金 763M；其他短期投資 1,536M
- 總債務：53M（2026-04-30 為 411M；FY26 年底為 422M，本季已償還 350M 流動債務）
- 淨現金 (Net cash)：約 2,246M（現金 2,299M − 債務 53M）
- 流動比率 (current ratio)：1.53（3,089 ÷ 2,025，與 info.currentRatio 1.525 一致）
- 負債/權益：info.debtToEquity = 0.76，依 Yahoo 百分比單位解讀為 0.76%（53M ÷ 股東權益 6,973M ≈ 0.76%）
- 股東權益：6,973M；每股帳面值 39.89 USD (info.bookValue)；P/B 5.23x
- 商譽與無形資產：5,578M（FY26 年底），佔總資產約 57%，有減損風險但目前無跡象
- 遞延收入 (流動)：1,751M（2026-07），季減 2.3%，屬年費預收模式，為現金流領先指標；需追蹤後續季度

**營運資本**：年底 Working Capital 1,090M (FY26)，較 FY24 的 1,198M 下降。

## Capital allocation & insider signal

**資本配置**
- 資本支出極低：FY26 capex 21M，佔營收 0.7%，屬輕資產模式。
- 股利：無 (dividendYield 0, payoutRatio 0)；股利覆蓋率 n/a。
- 買回：FY26 買回 73M；FY27 上半年 (2026-04 季 248M、2026-07 季 124M) 合計 372M。
- 債務償還：FY24 償還 937M、FY25 償還 280M、FY26 償還 510M；淨債務由 FY23 的 1,929M 降至 FY26 年底轉為淨現金（總債務 422M，現金及短期投資 2,553M）。
- 股數變化：年底流通股數由 FY23 161.3M 升至 FY26 177.4M（+10%，SBC 稀釋明顯）。FY27 Q2 季末為 174.8M，自 FY26 年底減少 1.5%，買回開始抵銷稀釋。
- 注意：info.sharesOutstanding = 167.1M 與季度資料 174.8M 不一致（info 數值疑似過期）。市值 36.47B 與 208.64 × 174.8M 吻合，本報告採 174.8M。

**內部人交易（2026-04-22 至 2026-10-22，過去 6 個月）**
- 公開市場賣出：11 筆，合計約 46.5M USD，約 311,990 股。
- 公開市場買入：0 筆。
- 主要賣出人：CFO Brett Tighe 約 20.5M USD（2026-06-08 與 2026-09-02 合計）；CEO Todd McKinnon 約 19.6M USD（2026-07-08 與 2026-09-22）；President Eric Kelleher 約 2.1M USD；Larissa Schwartz 約 4.1M USD；Director Shellye Archambeau 約 0.2M USD。
- 相對市值：46.5M ÷ 36,470M ≈ 0.13%；占流通股約 0.18%。
- 解讀：規模小，絕對金額亦不大，且無買入，但 CEO/CFO 在股價由 100 多 USD 走高後持續出售，屬中性偏警示訊號。部分賣出可能屬既定交易計畫，yfinance 未標示 10b5-1 旗標，此項無法確認。
- 機構持股：約 99.5%，1,219 家機構；前三大為 BlackRock 11.2%、FMR 9.7%（季增 43.5%）、Vanguard 5.4%。內部人持股僅 0.51%。

## Valuation

**價格基礎（fast_info 快取，feed = cnyes，cached 2026-10-22 11:36 UTC）**
- 最新價 208.64 USD；前收 194.02 USD；日內高 210.86、低 192.91 USD
- 50 日均線 182.76 USD；200 日均線 120.19 USD（來自 info；fast_info 的均線欄位為 null）
- 股價較 200 日均線高 73.6%，較 50 日均線高 14.2%；52 週漲幅 +135.6% (info.52WeekChange)
- 市值 36.47B USD（info.marketCap 36,474,638,336；以 208.64 × 174.8M 股手算吻合）
- 企業價值 EV 34.23B USD（市值 − 淨現金 2.25B）

**估值倍數**

| 指標 | 數值 | 計算依據 |
|---|---|---|
| Trailing P/E (GAAP) | 125.7x | info.trailingPE；TTM EPS 1.66 |
| Trailing P/E (Non-GAAP) | 約 56.7x | 208.64 ÷ (0.82+0.90+0.91+1.05) = 208.64 ÷ 3.68 |
| Forward P/E | 47.7x | info.forwardPE；forwardEps 4.378 |
| EV/EBITDA | 106.6x | info.enterpriseToEbitda；EBITDA TTM 321M（季度 normalized EBITDA 加總約 416M，依此計算約 82x） |
| P/FCF (TTM) | 約 38.0x | 市值 36.47B ÷ FCF 959M（自行計算）；若用 info FCF 1,037.6M 則約 35.1x |
| P/S (TTM) | 11.9x | info.priceToSalesTrailing12Months |
| EV/Revenue (TTM) | 11.1x | info.enterpriseToRevenue |

**與同業比較**：yfinance 未提供同業中位數，以下為估計值（非工具輸出）。軟體基礎架構同業 forward P/E 估計約 30x 上下、EV/Revenue 約 6–8x、P/FCF 約 25x 上下。OKTA 各項倍數均明顯高於估計同業水準。

**估值判讀**：以 forward P/E 47.7x 計，市場定價需要 EPS 持續高速成長。目前 FY27 Q2 Non-GAAP EPS 年增 15.4%，但營收成長已降至 10% 上下，EPS 成長主要靠營益率擴張與利息收入。估值對 SBC 與營收增速放緩的容忍度低。

## Key catalysts

- **下次財報**：2026-12-01（yfinance 日期，時間 20:00 UTC），Q3 FY27 Non-GAAP EPS 預估 0.93，較去年同季 0.82 年增約 13%。
- **近期財報**：2026-08-26 FY27 Q2 EPS 1.05 超出預估 8.9%；營收 805M USD 年增 10.6%；營業利益率 13.3%。
- **管理層指引**：yfinance 不提供公司指引數字，本欄 n/a。需另查 8-K 或法說會資料。
- **分部／產品轉移**：yfinance 無分部資料；info 描述顯示公司重點推向 Okta for AI Agents、Identity Governance、Privileged Access 等新產品線，但營收占比 n/a。
- **股價驅動**：股價 52 週漲幅 135.6%，財報後 EPS 超預期與 AI 身分治理敘事為主要上行催化；內部人持續賣出與估值過高則為主要下行風險。

## Metrics table

單位：營收、利潤、市值、現金、債務等為 USD B/M；比率為 %/x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY26, USD M) | 2,919 | +11.8% | 約 +10–12% (估計) | 成長中，但持續減速 |
| 營收 (季, 2026-07, USD M) | 805 | +10.6% | 估計 | 中段成長 |
| 3 年營收 CAGR (FY23→FY26) | 16.3% | n/a | 估計 約 12–15% | 高於同業估計 |
| 毛利率 (季, GAAP) | 79.6% | +2.7pt | 約 75% (估計) | 優 |
| 營業利益率 (季, GAAP) | 13.3% | +7.7pt | 約 10–15% (估計) | 改善中 |
| 淨利率 (FY26, GAAP) | 8.1% | +7.0pt | 約 5–10% (估計) | 合理，受利息收入與低稅率助益 |
| ROE (TTM, GAAP) | 4.3% | n/a | 約 10–15% (估計) | 弱 |
| ROIC (估算) | 約 1.9% | n/a | 約 8–12% (估計) | 弱（含大量現金） |
| FCF margin (TTM) | 31.2% | n/a | 約 20–25% (估計) | 優 |
| FCF / NI (TTM) | 3.24 | n/a | >0.9 健康 | 高，但主要因 SBC 與低 GAAP NI |
| FCF − SBC margin (FY26) | 約 10.9% | n/a | 估計 | 中性，揭示 SBC 壓力 |
| SBC / 營收 (FY26) | 18.6% | -3.0pt | 約 10–15% (估計) | 偏高 |
| 淨現金 (USD M) | 2,246 | n/a | 估計 | 強 |
| 流動比率 | 1.53 | n/a | 約 1.5–2.0 (估計) | 合理 |
| Debt/Equity | 0.76% | n/a | 估計 | 極低 |
| 流通股數 (M 股) | 174.8 | +1.5% (自 FY26 年底) | n/a | 稀釋尚未完全抵銷 |
| 內部人 6 個月淨買賣 | -46.5M USD (淨賣) | n/a | n/a | 中性偏警示 |
| Trailing P/E (GAAP) | 125.7x | n/a | 約 40–60x (估計) | 偏貴 |
| Forward P/E | 47.7x | n/a | 約 30x (估計) | 偏貴 |
| EV/EBITDA | 106.6x | n/a | 約 30–40x (估計) | 偏貴 |
| P/FCF (TTM) | 約 38.0x | n/a | 約 25x (估計) | 偏貴 |
| P/S (TTM) | 11.9x | n/a | 約 6–8x (估計) | 偏貴 |
| 市值 (USD B) | 36.47 | n/a | n/a | — |
| EV (USD B) | 34.23 | n/a | n/a | — |
| 52 週漲幅 | +135.6% | n/a | n/a | 動能強，估值已反映 |
| 下次財報 | 2026-12-01 | n/a | n/a | — |

## Red flags

- **估值極高**：forward P/E 47.7x、P/S 11.9x、EV/EBITDA 106.6x（info）；市場對成長與利潤率擴張的定價已相當完整，任何不及預期都可能引發大幅修正。
- **SBC 高**：FY26 SBC 544M 佔營收 18.6%，為 FY26 GAAP 淨利 235M 的 2.3 倍；扣除 SBC 後 FCF 利潤率大幅縮水。FCF/NI 3.2–3.7 倍的表面健康數字需打折判讀。
- **營收成長持續減速**：21.8% → 15.3% → 11.8%，季度 YoY 10.6%。
- **GAAP 獲利才剛轉正**：FY26 首次 GAAP 淨利為正；TTM ROE 僅 4.3%，ROIC 約 1.9%。
- **內部人持續賣出**：6 個月 CEO/CFO 合計約 40M USD 賣出，無買入。
- **股數稀釋**：FY23→FY26 流通股數增加約 10%，FY27 才開始小幅回購。
- **利息收入占比高**：FY26 利息收入 110M，佔稅前利潤相當比例；利率下行會直接壓低 GAAP 獲利。
- **遞延收入季減**：流動遞延收入由 FY26 年底 1,875M 降至 2026-07 的 1,751M，屬季節性或續約節奏變化，需持續追蹤。
- **資料品質**：yfinance 連線多次出現 Cookie/crumb 失敗與 403 錯誤，fast_info 來自快取；info.sharesOutstanding (167.1M) 與季度股數 (174.8M) 不一致；info.freeCashflow (1,037.6M) 與季度加總 (959M) 不一致；管理層指引與分部營收均為 n/a。

FUNDAMENTALS REPORT COMPLETE
