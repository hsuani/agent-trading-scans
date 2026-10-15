# Fundamentals — JBL as of 2026-10-15

## Executive summary
Jabil (JBL) 是低毛利、重資產的 EMS (電子製造服務) 公司，FY25 (2025-08 結束) 毛利率僅 8.9%、淨利率 2.2%，但 TTM 獲利與現金流在 2026 年明顯改善 (最新季 GAAP EPS 2.59 vs 去年同季 2.03，最近 8 季 EPS 全數優於預期)，TTM FCF 約 $1.31B。財務槓桿與流動性偏緊 (2026-05 季 Debt/Equity 約 2.9x、流動比率 0.98)，ROE 高達 66% 主要是權益基數很小所致，不宜當作品質指標。估值上，trailing P/E 32.6x 偏高，但 forward P/E 約 13.3x (以 info.forwardEps 22.17 計)，分析師平均目標價 $425 (較現價 +44.6%)；同業中位數資料無法由工具取得，估值吸引力只能以絕對值判讀。

資料說明：本報告資料來自本地快取 (source: "cache")，為預期行為。最新季度財報只到 2026-05-31 (FQ3 FY26)；yfinance info 與 earnings_dates 顯示 2026-08 季 (FQ4 FY26) 已於 2026-09-30 公布 (調整後 EPS 4.40)，但該季損益表與資產負債表未在快取內，相關欄位標示 DATA_UNAVAILABLE。

## Revenue & profitability

**營收趨勢 (年度，FY 結束於 8 月)**
- FY22 $33.48B → FY23 $34.70B (+3.7%) → FY24 $28.88B (-16.8%) → FY25 $29.80B (+3.2%)
- FY22–FY25 三年 CAGR 約 -3.8%；FY22 為近年高點基礎，FY24 為低點，營收並未恢復至 FY22–FY23 水準。
- 季度 TTM 營收 (Aug-25 ~ May-26 四季加總) 為 $33.59B。最新季 (2026-05) $8.75B，較 2025-05 季 $7.83B 成長 +11.8%。
- yfinance info 的 totalRevenue $35.95B 與 revenueGrowth 28.6% 無法由季度快取重現 (推測包含 2026-08 季)，本報告不採用此數字作為基準，列為資料差異。

**利潤率 (年度)**
- 毛利率: FY22 7.9% → FY23 8.3%(計算值 2867/34702) → FY24 9.3% → FY25 8.9%
- 營業利益率 (Operating Income 行): FY22 4.2% → FY24 5.0% → FY25 4.8%
- 淨利率: FY22 3.0% → FY24 4.8% (含 $942M 業務出售利益) → FY25 2.2% (含 -$300M 非經常性項目)
- FY24 淨利 $1.39B 含出售業務利益，屬非經常性，不應外推。

**利潤率 (季度 TTM 與最新季)**
- TTM 毛利率 9.2% (毛利 $3.10B)；TTM 營業利益率 5.0% (營業利益 $1.69B)；TTM 淨利率 2.6% (淨利 $862M)。
- 最新季 (2026-05) 毛利率 9.5%，較 2025-05 季 8.7% 提升約 0.8 個百分點；營業利益率 5.2% vs 4.9%。
- 最新季淨利 $275M，較去年同季 $222M 成長 +23.9%；GAAP 稀釋 EPS $2.59 vs $2.03 (+27.6%)。
- 調整後 EPS (earnings_dates 的 Reported EPS 欄，非 GAAP 口徑): FY25 合計 $9.78 → FY26 合計 $13.10 (+33.9%)。FY26 四季為 2.85 / 2.69 / 3.16 / 4.40，均高於分析師預估。

**ROE / ROIC**
- info returnOnEquity 66.4%；以 TTM 淨利 $862M 除以 2025-08 與 2026-05 平均權益 $1.33B 估算約 65%。權益基數因大量買回庫藏股而縮小 (權益由 2025-08 的 $1.51B 降至 2026-05 的 $1.32B)，ROE 數值膨脹，屬低品質指標。
- ROIC (估算): TTM 營業利益 $1.69B × (1 - 24.7% 最新季稅率) ÷ 投入資本 $3.86B (權益 + 總負債 - 現金，2026-05) ≈ 33%。此為估算，計算方法見上，非 yfinance 直接欄位。

## Cashflow & balance sheet

**現金流品質**
- FY25 OCF $1.64B、資本支出 $468M、FCF $1.17B (= OCF - PPE 購置，與 yfinance FCF 欄一致)。
- FY25 FCF 利潤率 3.9%；FCF / NI = 1.78x，但 FY25 NI 含非經常性項目，比值失真。
- FY24 FCF/NI 0.67x (NI 含 $942M 出售利益)；FY23 0.86x；FY22 0.27x。
- TTM (Aug-25 ~ May-26): OCF $1.86B、資本支出 $551M、FCF $1.31B、FCF 利潤率 3.9%、FCF / NI = 1.52x (>0.9，健康)。
- 最新季 FCF $351M，較去年同季 $320M +9.7%；但最新季資本支出 $184M，較去年同季 $86M 增加 +114%，為資本支出重新加速的訊號。
- info freeCashflow $1.28B、operatingCashflow $2.00B 與季度加總值不同，期間定義不明，以季度加總為準。

**資產負債表 (2026-05-31，最新季快取)**
- 現金及約當現金 $1.36B (2025-08 為 $1.93B，下降)
- 總債務 $3.89B (長期債務 $2.88B + 流動債務 $0.50B + 租賃等其他)
- yfinance Net Debt 欄 $2.02B；以 總債務 - 現金 直接計算為 $2.53B。兩者差異來源未知 (可能是 yfinance 對現金或租賃的定義不同)，標示為資料差異。
- 股東權益 $1.32B；Debt/Equity 約 2.9x (以 2026-05 計算)；info debtToEquity 為 248.6 (期間不同，見上)。
- 流動資產 $18.16B / 流動負債 $18.51B = 流動比率 0.98；營運資金 -$353M。info currentRatio 0.993、quickRatio 0.441 (期間不明，推測為 2026-08)。
- 存貨 $5.93B (較 2025-08 $4.68B 增加 +26.7%)，應收帳款 $6.94B (較 2025-08 $5.10B 增加 +36.2%)。存貨與應收同步大增，對營運資金造成壓力，需追蹤 (應收增幅快於營收)。
- 商譽 $1.23B (2025-08 為 $0.84B)，2026 年商譽增加，對應 2026 年收購活動，但細節不在快取內。

## Capital allocation & insider signal

**資本配置**
- 買回: FY23 $487M → FY24 $2.50B → FY25 $1.00B；TTM (Aug-25 ~ May-26) 約 $916M，約佔 TTM FCF 的 70%。
- 股本: 流通股數由 2025-08 的 107.5M 降至 2026-05 的 104.8M (-2.5%)；FY24→FY25 稀釋後平均股數由 124.3M 降至 110.9M (-10.8%)。買回對每股盈餘的助益明顯。
- 股利: 季度 $0.08 (trailing 年化 $0.32)，TTM 現金股利支出約 $35M，殖利率 0.1%，payoutRatio 4.0%。FCF 對股利覆蓋倍數約 37x，股利安全性極高，但股息佔報酬比重極低。
- 買回 + 股利 > FCF 的年度: FY24 (買回 $2.5B 遠超 FCF $932M)，股東權益因此由 $2.87B 降至 $1.74B。FY25 以後買回回落到與 FCF 大致相當的水準。
- 槓桿: FY24 買回大量借助現金與出售業務收入，FY25–FY26 的 Net Debt 由 $0.68B (FY24) 上升至 $2.02B (2026-05)。

**內部人交易 (2026-04-15 至 2026-10-15，約 6 個月，以 yfinance insider 明細加總)**
- 公開市場賣出 6 筆，合計 12,023 股，約 $3.87M:
  - Gary K. Schick (SVP & CHRO): 2026-04-30 賣 1,000 股 @ $340.00；2026-07-15 賣 1,000 股 @ $315–330
  - Steven D. Borges (Officer): 2026-04-17 賣 5,126 股 @ $317.51 (約 $1.63M)
  - Andrew D. Priestley (COO): 2026-04-20 賣 3,169 股 @ $330.00 (約 $1.05M)
  - May Yee Yap (Senior VP & CIO；insider 明細標示 CTO): 2026-04-16 賣 1,634 股 @ $306.74 (約 $0.50M)
  - Matthew Crowley (Officer): 2026-07-06 賣 94 股 @ $345.00
- 公開市場買入 1 筆: 董事 Tyagarajan Nallicheri Vydianathan 2026-07-17 買 500 股 @ $299.63 (約 $0.15M)。
- 其他: 2026-04-23 董事股票獎勵 (Tyagarajan 與 John C. Plant 各 600 股)；2026-04-10 董事 Steven A. Raymund 贈與 5,120 股 (非市場交易，未計入)。
- 窗口外的邊界交易: 2026-04-08 至 04-13 期間另有多筆高層賣出，包括 CEO Michael Dastoor 9,467 股 (約 $2.71M)、Borges 合計 14,000 股、Priestley 4,000 股等，因落在 6 個月窗口之外未計入上方淨額；若採較寬鬆窗口，賣出金額會明顯增加。
- 淨額 (窗口內): 買入 $0.15M、賣出 $3.87M，淨賣出約 $3.72M，佔目前市值 $30.80B 的 0.012%，規模極小，不構成強烈的內部人訊號。
- 注意: 窗口內賣出價格區間約 $306–345，多為 2026-04 至 07 的高價位時段；目前股價 $293.91，低於多數賣出價格，主管的賣出與目前價位的關聯性有限。

**機構與持股結構**
- 機構持股 99.1%，內部人持股 1.19%，機構數 1,546 家。
- 前三大持有人: BlackRock 9.67% (10.13M 股，季增 +4.7%)、Vanguard Capital Management 6.58%、Texas Yale Capital 6.00%。
- 空單: 空單股數 2.80M，佔流通股 3.17%，short ratio 2.06 天；前月空單 2.99M，空單較前月減少。

## Valuation

**估值倍數 (以現價 $293.91 計算)**
- 現價來源: 快取 regularMarketTime 對應 2026-10-14 收盤 $293.91 (前收 $317.86，單日跌 -7.5%)。2026-10-15 盤前報 $286.70 (-2.5%)。
- 工具數據未解釋 2026-10-14 的大幅下跌原因，需由 catalyst 或新聞管線補充。
- trailing P/E: 32.6x (info trailingPE；以 trailingEps $9.02)。若以季度 GAAP EPS 加總 $8.01 計，約 36.7x。
- forward P/E: 13.3x (info forwardEps $22.17)。若採 epsCurrentYear $17.69 (即 FY27 估計，yfinance priceEpsCurrentYear)，P/E 為 16.6x。
- PEG: 0.82 (info pegRatio)。
- EV/EBITDA: info enterpriseToEbitda 13.1x (EV $33.09B，EBITDA $2.52B)；以季度 normalized EBITDA TTM $2.28B 計算約 14.5x。
- P/S (TTM): 約 0.92x (市值 $30.80B / TTM 營收 $33.59B)。
- P/FCF (TTM): 約 23.6x (市值 / TTM FCF $1.31B)；info 的 FCF 口徑為 24.1x。
- P/B: 19.1x (info priceToBook，bookValue/share $15.39)；因權益基數小，P/B 不具參考性。
- 同業中位數 (sector median): DATA_UNAVAILABLE (工具未提供同業資料，不估算)。

**分析師共識 (9 位)**
- 推薦均值 1.4 (strong_buy)；目標價均值 $425、中位數 $430、最高 $475、最低 $365。
- 相對現價: 均值 +44.6%、最高 +61.6%、最低 +24.2%。
- 股價相對 52 週區間: 區間 $189.60 – $428.93，現價距高點 -31.5%、距低點 +55.0%。
- 股價低於 50 日均線 $315.71 與 200 日均線 $304.81 (info 欄位)。fast_info 的均線欄位為 null，以 info 數值為準。

## Key catalysts
- 下次財報: earnings_dates 與 info 均顯示 2026-12-16 為估計日期 (isEarningsDateEstimate: true)，FQ1 FY27 EPS 估計 $4.05。
- 最近一次財報: 2026-09-30 公布 FQ4 FY26 調整後 EPS $4.40，優於估計 $4.08 (+7.96%)。此季完整損益與資產負債表不在快取內，無法驗證營收、毛利率與指引內容。
- 最近 8 季 EPS 皆優於預期 (surprise +1.35% 至 +11.69%)；在已檢視的歷史中，2024-03 季為小幅不及 (-0.12%) 的一筆。
- 近期 EPS 上修跡象: info epsCurrentYear $17.69 與 forwardEps $22.17 高於 FY26 實際調整後 EPS $13.10，代表市場預期獲利大幅成長，但該預估的口徑與來源未在工具中揭露。
- 營運上需追蹤: 存貨與應收同比增加 (2026-05 季) 與資本支出回升 (2026-05 季 +114%)，可能反映業務成長前的備貨或產能投資。
- 2026-10-14 單日 -7.5% 的原因需由新聞或 catalyst 管線補充。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, 季度加總) | $33.59B | 最新季 +11.8% (vs 2025-05) | DATA_UNAVAILABLE | 成長回升，但 FY22–FY25 CAGR -3.8% |
| 營收 (FY25) | $29.80B | +3.2% (vs FY24) | DATA_UNAVAILABLE | 持平偏弱 |
| 毛利率 (TTM) | 9.2% | 最新季 9.5% vs 8.7% (+0.8 pp) | DATA_UNAVAILABLE | 低毛利結構，但改善中 |
| 營業利益率 (TTM) | 5.0% | 最新季 5.2% vs 4.9% | DATA_UNAVAILABLE | 普通 (EMS 特性) |
| 淨利率 (TTM) | 2.6% | 最新季 3.1% vs 2.8% (計算) | DATA_UNAVAILABLE | 偏低 |
| 稀釋 EPS (最新季 GAAP) | $2.59 | +27.6% (vs $2.03) | DATA_UNAVAILABLE | 強 |
| 調整後 EPS (FY26) | $13.10 | +33.9% (vs FY25 $9.78) | DATA_UNAVAILABLE | 強 |
| ROE | 66.4% (info) | n/a | DATA_UNAVAILABLE | 失真，權益基數小 |
| ROIC (估算) | ~33% | n/a | DATA_UNAVAILABLE | 高，但為估算值 |
| FCF (TTM) | $1.31B | 最新季 +9.7% | DATA_UNAVAILABLE | 健康 |
| FCF 利潤率 (TTM) | 3.9% | FY25 3.9% (FY24 3.2%) | DATA_UNAVAILABLE | 普通 |
| FCF / NI (TTM) | 1.52x | FY25 1.78x (含非經常項目) | DATA_UNAVAILABLE | 健康 (>0.9) |
| 資本支出 / 營收 (TTM) | 1.6% | 最新季資本支出 +114% YoY | DATA_UNAVAILABLE | 注意回升 |
| 現金 (2026-05) | $1.36B | 2025-08 $1.93B (-29.6%) | DATA_UNAVAILABLE | 下降 |
| 總債務 (2026-05) | $3.89B | 2025-08 $3.37B (+15.6%) | DATA_UNAVAILABLE | 上升 |
| Net Debt (yfinance) | $2.02B | 2025-08 $0.95B | DATA_UNAVAILABLE | 上升，需注意 |
| Debt / Equity (2026-05) | 2.9x | 2025-08 2.2x (計算，3,366/1,513) | DATA_UNAVAILABLE | 偏高 |
| 流動比率 (2026-05) | 0.98 | n/a | DATA_UNAVAILABLE | 偏緊 |
| 營運資金 (2026-05) | -$353M | 2025-08 +$6M | DATA_UNAVAILABLE | 轉負 |
| 存貨 (2026-05) | $5.93B | 2025-08 $4.68B (+26.7%) | DATA_UNAVAILABLE | 增加，需追蹤 |
| 應收帳款 (2026-05) | $6.94B | 2025-08 $5.10B (+36.2%) | DATA_UNAVAILABLE | 增幅大於營收，需追蹤 |
| 買回 (TTM) | $916M | FY25 $1.00B, FY24 $2.50B | DATA_UNAVAILABLE | 與 FCF 相當 |
| 股利殖利率 | 0.1% | n/a | DATA_UNAVAILABLE | 極低 (FCF 覆蓋 37x) |
| 流通股數 | 104.8M (2026-05) | -2.5% vs 2025-08 | DATA_UNAVAILABLE | 股本縮減 |
| 內部人淨交易 (6 個月) | -$3.72M | 佔市值 0.012% | DATA_UNAVAILABLE | 中性，規模極小 |
| trailing P/E | 32.6x | n/a | DATA_UNAVAILABLE | 偏高 |
| forward P/E (forwardEps) | 13.3x | n/a | DATA_UNAVAILABLE | 低 |
| forward P/E (FY27 est.) | 16.6x | n/a | DATA_UNAVAILABLE | 中性 |
| EV/EBITDA (info) | 13.1x | n/a | DATA_UNAVAILABLE | 中性偏高 (EMS 特性) |
| EV/EBITDA (normalized TTM) | 14.5x | n/a | DATA_UNAVAILABLE | 中性偏高 |
| P/S (TTM) | 0.92x | n/a | DATA_UNAVAILABLE | 低 (受低毛利限制) |
| P/FCF (TTM) | 23.6x | n/a | DATA_UNAVAILABLE | 中性 |
| P/B | 19.1x | n/a | DATA_UNAVAILABLE | 不具參考性 |
| PEG | 0.82 | n/a | DATA_UNAVAILABLE | 偏低 |
| 分析師目標價均值 | $425 (+44.6%) | n/a | DATA_UNAVAILABLE | 共識強烈看多 (9 位) |
| Beta | 1.295 | n/a | DATA_UNAVAILABLE | 高於大盤 |

## Red flags
- 資料時效: 最新季度財報 (FQ4 FY26，2026-08) 與 FY26 年報未在快取內，但 info 與 earnings_dates 顯示其已公布；本報告的 TTM 與資產負債表停在 2026-05，可能低估最新變化。
- 資料內部不一致: info totalRevenue ($35.95B)、totalCash ($1.74B)、totalDebt ($4.02B)、freeCashflow ($1.28B) 與季度快取不符；yfinance Net Debt ($2.02B) 與 總債務 - 現金 ($2.53B) 亦不同。以上差異未能釐清來源。
- 資產負債表壓力: 2026-05 季 Debt/Equity 約 2.9x，流動比率 0.98，營運資金轉負；現金由 $1.93B 降至 $1.36B，總債務上升，淨負債由 $0.95B 升至 $2.02B。
- 股東權益縮小: 權益由 $1.51B 降至 $1.32B，主要因買回庫藏股 (庫藏股由 $7.90B 增加)，使 ROE 數字膨脹，不宜單獨作為品質指標。
- 營運資金惡化: 存貨 +26.7%、應收 +36.2% (2025-08 至 2026-05)，增幅明顯高於 TTM 營收增幅，需追蹤營運資金周轉與壞帳風險。
- 資本支出回升: 最新季資本支出 $184M，較去年同季 +114%，TTM 資本支出 $551M 仍低於 FY22 的 $1.39B，但趨勢轉向。
- 低毛利結構: 毛利率 8–9.5%，營業利益率約 5%，EMS 業務議價能力有限，獲利對營收與客戶集中度敏感。
- 非經常性項目: FY24 淨利含 $942M 業務出售利益，FY25 含 -$300M 非經常性項目，歷史 EPS 比較需排除這些項目。
- 治理風險分數 (yfinance，1–10，越高越差): overallRisk 8、boardRisk 10、auditRisk 9、compensationRisk 4、shareHolderRightsRisk 5。董事會與審計風險分數偏高，需進一步查證。
- 股價波動: 2026-10-14 單日跌 -7.5%，盤前 2026-10-15 再跌 -2.5%；Beta 1.295；52 週波動區間 $189.60–$428.93，股價低於 50 日與 200 日均線。
- 內部人賣出: 窗口內 6 筆合計賣出 12,023 股 (約 $3.87M)，規模小；另有窗口外 2026-04-08 至 04-13 的 CEO 等多筆賣出，整體賣壓高於窗口內數字。

FUNDAMENTALS REPORT COMPLETE
