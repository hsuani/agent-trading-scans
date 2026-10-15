# Fundamentals — OKTA as of 2026-10-16

## Executive summary
Okta 資產負債表極為穩健 (現金+短期投資 2,299M USD、總債務僅 53M USD、TTM FCF 約 959M USD, FCF margin 約 31%)，財務健康度沒有問題，但 GAAP 獲利仍薄 (TTM 淨利率 9.6%) 且 SBC 佔營收 16.4%，把 FCF 含金量大幅稀釋。營收成長已從 FY24 的 21.8% 放緩到 Q2 FY27 的 10.6%，而股價在 52 週內上漲約 140%，trailing P/E 127.7x、P/S 12.1x、forward P/E 48.4x 均屬高檔，估值吸引力偏低。內部人近 6 個月淨賣出約 46M USD (CEO 與 CFO 為主)，僅一筆 0.27M USD 的董事買進。

## Revenue & profitability

**營收與成長**
- 年度營收 (FYE 1/31): FY23 1,858M, FY24 2,263M, FY25 2,610M, FY26 2,919M USD。
- YoY 成長: FY24 +21.8%, FY25 +15.3%, FY26 +11.8%。3 年 CAGR (FY23→FY26) 約 16.3%。yfinance 僅提供 4 個年度資料，5 年 CAGR 為 n/a。
- 季度營收 (最近 5 季): Q2 FY26 (Jul-25) 728M, Q3 FY26 (Oct-25) 742M, Q4 FY26 (Jan-26) 761M, Q1 FY27 (Apr-26) 765M, Q2 FY27 (Jul-26) 805M。Q2 FY27 YoY +10.6%。Q1 FY27 的 YoY 因 yfinance 缺 Q1 FY26 資料而為 n/a。
- TTM 營收 3,073M USD (與 info.totalRevenue 一致)。
- 業務: 身分認證平台 (SSO、Adaptive MFA、Universal Directory、Lifecycle Management、Identity Governance、Privileged Access)，另有 Auth0 與 "Okta for AI Agents" 的 AI 代理身分產品線。yfinance 未提供分部營收，segment mix 為 n/a。

**獲利能力**

| 期間 | 毛利率 | GAAP 營業利益率 | GAAP 淨利率 |
|---|---|---|---|
| FY23 | 70.6% | -42.1% | -43.9% |
| FY24 | 74.3% | -20.3% | -15.7% |
| FY25 | 76.3% | -2.4% | 1.1% |
| FY26 | 77.4% | 5.2% | 8.1% |
| Q2 FY26 | 76.9% | 5.6% | 9.2% (※) |
| Q2 FY27 | 79.6% | 13.3% | 14.4% |
| TTM | 78.1% | 7.7% | 9.6% |

(※ Q2 FY26 淨利率 = 67M / 728M = 9.2%。TTM 毛利率、淨利率與 info.grossMargins 78.1%、info.profitMargins 9.6% 一致。)

- 毛利率持續擴張 (FY23 70.6% → Q2 FY27 79.6%)，代表雲端訂閱組合與 AI 相關產品定價有支撐。
- 獲利能力明顯改善，FY25 之前為虧損，FY26 首度轉正，Q2 FY27 營業利益率年增約 7.7 pp。
- info.operatingMargins 為 13.3%，與 GAAP TTM 營業利益率 7.7% 差異大，應視為非 GAAP 或另一計算口徑。
- ROE: info.returnOnEquity 4.3%，與 TTM 淨利 296M / 平均股東權益約 6.9B 相符。ROA 1.6%。
- ROIC (估計): TTM GAAP 營業利益 236M，以 10% 稅率計 NOPAT 約 212M；以股東權益 6,973M + 總債務 53M − 現金 2,299M ≈ 4,727M 為投入資本，ROIC 約 4.5%。屬估計值，非 yfinance 直接提供。

## Cashflow & balance sheet

**現金流品質**
- FY26 營運現金流 884M, FCF 863M (FCF = OCF − CapEx 21M)，FCF margin 29.6%。FY25 FCF 730M (28.0%)，FY24 488M (21.6%)，FY23 63M (3.4%)。
- TTM FCF (由季度加總) 959M，TTM FCF margin 31.2%。info.freeCashflow 為 1,038M，口徑略有不同。
- FCF / NI: FY26 為 863 / 235 = 3.7x；TTM 為 959 / 296 = 3.2x，遠高於 0.9 的健康門檻。但這主要是因為 SBC 為非現金費用 (TTM SBC 503M)，NI 被壓低。
- SBC 調整後 FCF (自算): TTM 959M − SBC 503M = 456M，約 14.8% margin。這是本報告最重要的品質保留。
- CapEx 極低，FY26 21M (0.7% 營收)，TTM 資本支出約 16M，資產輕。

**資產負債表 (截至 2026-07-31, Q2 FY27)**
- 現金+短期投資 2,299M USD (info.totalCash 一致)，現金及約當現金 763M，其餘為短期投資 1,536M。
- 總債務 53M USD，全數為租賃負債 (Capital Lease)。4 月時尚有 350M 的流動債務，7 月已清償。FY26 Q3 (Oct-25) 曾償還 510M。
- 淨現金 (cash − debt) 約 2,246M USD，約 13.4 USD/股 (info.totalCashPerShare 13.15)。
- 流動比率 1.53 (流動資產 3,089M / 流動負債 2,025M)；速動比率 1.38 (info.quickRatio)。
- 負債/權益: 依 Q2 FY27 總債務 53M 自算約 0.8%。info.debtToEquity 為 0.76，明顯與自算不一致，可能含遞延收入或其他口徑，**此欄位不可直接採信**。
- 總資產 9,138M，其中商譽與無形資產 5,567M (約 61%)，有形淨值 (TBV) 僅 1,406M，股東權益 6,973M。
- 遞延收入 (流動) 1,751M，佔總負債 2,165M 的 81%，反映 SaaS 預收款特性，是營運現金流的重要來源。
- 應收帳款 469M (Jan-26 為 711M，季節性明顯)。

## Capital allocation & insider signal

**資本配置**
- 股票回購: FY26 全年 73M；FY27 上半年 (Q1 248M + Q2 124M) 合計 372M，已開始實質回購。
- 股本變化: 基本股數 Jan-26 177.4M → Jul-26 174.8M (下降 1.4%)；較 Jul-25 的 176.3M 下降 0.8%。稀釋抵銷 (SBC 16.4% 營收) 使淨減少幅度有限。
- 攤薄後平均股數: Q2 FY27 178.8M，較 Q2 FY26 的 181.0M 下降 1.2%。
- 無股息 (dividendYield 0.0)。
- 併購: Q4 FY26 (Oct-25) 有 53M 企業收購現金流出。
- 資本支出極低，FCF 的主要用途為回購與現金累積。

**內部人交易 (2026-04-15 至 2026-10-15，約 6 個月)**

| 日期 | 人員 | 職位 | 動作 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-09-22 | Todd McKinnon | CEO | 賣出 | 48,822 | 9.45M |
| 2026-09-18 | Eric Kelleher | President | 賣出 | 6,395 | 1.17M |
| 2026-09-11 | Eric Kelleher | President | 賣出 | 2,549 | 0.43M |
| 2026-09-02 | Brett Tighe | CFO | 賣出 | 80,000 | 12.88M |
| 2026-07-08 | Todd McKinnon | CEO | 賣出 | 68,936 | 10.11M |
| 2026-06-22 | Larissa Schwartz | Officer | 賣出 | 2,463 | 0.30M |
| 2026-06-18 | Eric Kelleher | President | 賣出 | 3,977 | 0.45M |
| 2026-06-08 | Brett Tighe | CFO | 賣出 | 65,000 | 7.62M |
| 2026-06-02 | Larissa Schwartz | Officer | 賣出 | 24,971 | 3.35M |
| 2026-05-18 | Shellye Archambeau | Director | 賣出 (間接) | 2,500 | 0.21M |
| 2026-05-07 | Larissa Schwartz | Officer | 賣出 | 6,377 | 0.49M |
| 2026-04-16 | David Schellhase | Director | **買進** | 3,712 | 0.27M |

- 合計: 公開市場賣出約 46.5M USD (約 311,990 股)，買進 0.27M USD，**淨賣出約 46.2M USD**。
- 相對市值 (37.05B USD) 約 0.13%，規模不大，但方向一致偏賣。
- 主要賣方為 CEO McKinnon (約 19.6M) 與 CFO Tighe (約 20.5M)，兩人於 Sept 與 June 皆有大額出售。
- 另有 Kelleher 2026-09-15 持股 16,279 股的交易 (無價格，疑為歸屬稅款代扣或其他非市價交易)，以及 Tighe 2026-09-02 間接持有的 41,251 股，皆未計入金額。
- 資料未揭露是否為 10b5-1 計畫，無法判斷是否為預先排程的例行出售。近 6 個月的賣出價格在 76.7–198 USD，目前股價 211.9 高於多數近期賣價。
- 機構持股 99.1%，內部人持股僅 0.51%。
- 空單: 7.93M 股，佔流通股 5.31%，days to cover 約 2.0，逐月小幅增加 (7.69M → 7.93M)。

## Valuation

目前股價 211.915 USD (regularMarketPrice; 最近收盤資料時間為 2026-10-14)，市值 37.05B USD，企業價值 (EV) 34.80B USD。52 週區間 62.66–235.00 USD，距 52 週高點約 9.8%；較 50 日均線 177.79 高約 19%，較 200 日均線 117.42 高約 80%。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | 127.7x | GAAP TTM EPS 1.66 |
| Forward P/E | 48.4x | forwardEps 4.38 (yfinance 口徑，期間與 GAAP/non-GAAP 基礎未明) |
| 當年度 P/E | 53.9x | epsCurrentYear 3.93 |
| EV/Revenue | 11.3x | TTM 營收 3,073M |
| EV/EBITDA | 108.4x (info) / 約 84x (自算) | info.ebitda 321M；以季度 EBITDA 加總 412M 自算 |
| P/S | 12.1x | priceToSalesTrailing12Months |
| P/FCF | 約 38.6x (自算) / 35.7x (info) | 市值 / TTM FCF 959M 或 1,038M |
| P/B | 5.3x | bookValue 39.89 |
| PEG | 1.62 | pegRatio |

**分析師共識**
- 43 位分析師，recommendationMean 1.66 (接近 Buy)，averageAnalystRating "1.7 - Buy"。
- 目標價: 平均 212.60、中位 223.00、最高 250.00、最低 127.00。平均目標價與現價幾乎相同 (+0.3%)，隱含上行空間有限。

**與產業中位數比較 (估計值，非 yfinance 提供)**
以 Software-Infrastructure 同業中位數估計: trailing P/E 約 60x、forward P/E 約 30x、EV/EBITDA 約 30–35x、P/S 約 6–7x、P/FCF 約 25x。OKTA 各項估值指標均顯著高於估計中位數，但其毛利率 (78%) 與 FCF margin (31%) 也屬同業前段。估值溢價主要來自 GAAP 獲利仍在爬升中，以及市場對 AI 身分議題的定價。

## Key catalysts

- **下一次財報**: 2026-12-01 (Q3 FY27)，yfinance 標示 isEarningsDateEstimate = false。EPS 共識 0.93 USD (non-GAAP)。
- **財報歷史**: 最近 8 季 EPS 全部超出預期，最近 4 季平均超出幅度約 7.5% (8.93%、6.69%、6.29%、8.05%)。Q2 FY27 實際 1.05 vs 估計 0.96，YoY (Q2 FY26 0.91) 約 +15%。
- **財測與指引**: yfinance 不提供正式指引資料，**FY27 全年指引 n/a**，需人工比對 IR 公告。
- **AI 代理身分產品**: "Okta for AI Agents" 與 Auth0 for AI Agents 為明確的新成長敘事，是股價大漲的主要驅動，也是未來幾季成長的關鍵觀察點。
- **資本回購**: H1 FY27 已回購 372M USD，持續性與規模為每季觀察點。
- **內部人出售**: 未來幾週仍可能有 Form 4 申報，對短線情緒會有影響。
- **空單**: 空單比例 5.3% 不高，但股價波動大，若財報不及預期可能引發回檔。
- **資料缺口**: yfinance 未提供分部營收、Q1 FY27 YoY、正式營收與 EPS 指引，建議人工補充。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收成長 (Q2 FY27) | 805M USD / +10.6% | FY26 +11.8% (FY25 +15.3%) | 約 12–15% | 略低於同業，放緩中 |
| 毛利率 | 79.6% (Q2) / 78.1% (TTM) | +2.7 pp (Q2) | 約 75% | 優於 |
| GAAP 營業利益率 | 13.3% (Q2) / 7.7% (TTM) | +7.7 pp (Q2) | 約 5–10% | 改善中 |
| GAAP 淨利率 | 9.6% (TTM) | FY26 8.1% (FY25 1.1%) | 約 5–10% | 中性偏正 |
| ROE | 4.3% | n/a | 約 0–10% | 中性 |
| ROIC (自算估計) | 約 4.5% | n/a | 約 5–10% | 偏低 |
| FCF margin | 31.2% (TTM) | FY26 29.6% (FY25 28.0%) | 約 20–25% | 優於 |
| FCF / NI | 3.2x (TTM) | FY26 3.7x | >0.9 為健康 | 優 (但受 SBC 影響) |
| SBC / 營收 | 16.4% (TTM) | 下降 (Q2 FY26 19.8%→Q2 FY27 14.2%) | 約 10–12% | 偏高 |
| SBC 調整後 FCF margin (自算) | 約 14.8% | n/a | n/a | 中性 |
| 現金+短期投資 | 2,299M USD | Jan-26 2,553M | n/a | 充足 |
| 總債務 | 53M USD (全為租賃) | Jan-26 422M | n/a | 極低 |
| 淨現金 | 約 2,246M USD | n/a | n/a | 強 |
| 流動比率 | 1.53 | Jan-26 1.43 (自算 3,644/2,554) | 約 1.5–2.0 | 健康 |
| 負債/權益 | 0.8% (自算) / info 0.76 | n/a | 約 0.3–0.6 | 自算採信，info 不可用 |
| Trailing P/E | 127.7x | n/a | 約 60x | 極度偏高 |
| Forward P/E | 48.4x | n/a | 約 30x | 偏高 |
| EV/EBITDA | 108x (info) / 約 84x (自算) | n/a | 約 30–35x | 極度偏高 |
| P/S | 12.1x | n/a | 約 6–7x | 偏高 |
| P/FCF | 約 36–39x | n/a | 約 25x | 偏高 |
| 52 週股價漲幅 | +139.9% | n/a | n/a | 動能強，但已大幅反映 |
| 基本股數變化 | 174.8M | Jul-25 176.3M (-0.8%) | n/a | 小幅縮減 |
| 內部人淨買賣 (6mo) | 淨賣約 46.2M USD | n/a | n/a | 偏空 (規模約市值 0.13%) |
| 空單 / 流通股 | 5.31%, days 2.0 | 月增 +3% | 約 3–5% | 中性 |
| 分析師平均目標價 | 212.6 USD (現價 211.9) | n/a | n/a | 上行空間有限 |

## Red flags
- **估值極度昂貴**: trailing P/E 127.7x、EV/EBITDA 108x (info)、P/S 12.1x，股價 52 週漲幅約 140%，接近 52 週高點 235，對任何財報不及預期的反應都會放大。
- **成長放緩**: 營收成長從 FY24 21.8% 降至 Q2 FY27 10.6%，TTM 仍無法支撐目前估值倍數。
- **SBC 偏高**: TTM SBC 503M，佔營收 16.4%，為 GAAP 淨利 296M 的 1.7 倍。SBC 調整後的 FCF 約 456M，遠低於表面 959M，是 FCF/NI 指標失真的主因。
- **內部人持續賣出**: 6 個月淨賣約 46M USD，CEO 與 CFO 為主要賣方，買進僅 0.27M USD。需確認是否屬於 10b5-1 計畫。
- **股權稀釋抵銷回購**: 2026 上半年回購 372M USD，但基本股數僅減少約 0.8% YoY，回購效果被 SBC 抵銷。
- **資料一致性問題**: info.debtToEquity (0.76) 與自算 (0.8%) 差異大；forwardEps 與 epsCurrentYear 期間定義不明；info.operatingMargins (13.3%) 與 GAAP TTM (7.7%) 不同口徑；EBITDA 來源 321M vs 季度加總 412M。
- **Governance 風險指標偏高**: yfinance overallRisk 10 (滿分 10)、shareHolderRightsRisk 10、compensationRisk 9、boardRisk 8。CEO 2026 總薪酬 1.16M USD 但 exercised value 達 46.5M USD。
- **商譽佔比高**: 商譽與無形資產佔總資產 61%，有形淨值僅 1.41B，若未來出現減損會影響帳面淨值。
- **資料時效**: 報價來自 yfinance 快取 (2026-10-15 11:20 UTC)，fast_info 資料源因連線失敗改由 info 補足，最近收盤為 2026-10-14。無資料晚於 DATE 2026-10-16 的情況。

FUNDAMENTALS REPORT COMPLETE
