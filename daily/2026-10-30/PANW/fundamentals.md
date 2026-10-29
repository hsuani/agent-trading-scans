# Fundamentals — PANW as of 2026-10-30

## Executive summary
PANW 的現金流品質仍強（FY26 FCF 4.11B USD，FCF margin 35.8%；營收 11.48B USD，年增 24.5%），但大型併購後 GAAP 獲利明顯惡化（FY26 淨利率 2.7%，Q3、Q4 連續 GAAP 虧損），商譽由 4.57B 暴增至 22.01B USD，流動比率僅 0.87，淨現金由 2.57B 縮至 0.57B USD。估值極度偏高：forward P/E 80.9x、P/S 28.1x、P/FCF 78.5x，市場已先行定價成長與整合成功；10/29 盤前報 369.00（-6.5%）顯示股價對消息高度敏感。財務體質尚可但估值安全邊際薄，本報告不提供交易建議。

**資料時點說明**：DATE 為 2026-10-30，yfinance 快取時間為 2026-10-29 12:53 UTC。價格基準為 2026-10-28 常規收盤 394.49 USD，另有 10/29 盤前 369.00 USD（bid 380.76 / ask 414.78，價差過寬，僅供參考）。資料未含 10/30 之後的價格。財報最新期間為 FY26 Q4（截至 2026-07-31）。下次財報日 2026-11-19 為 yfinance 估計值（isEarningsDateEstimate = true），屬 DATE 之後的未來事件。

**會計基準說明**：公司 FY 結束於 7 月底。GAAP 數字（income statement、cashflow、balance sheet）與 info 中的 forward EPS（分析師一致預期，多為 non-GAAP）口徑不同，各節會分別標示。

**單位說明**：本報告金額皆為 USD，以 B（十億）或 M（百萬）標示，不使用億。

## Revenue & profitability

**營收成長**（USD B，FY 結束 7/31）
| 年度 | 營收 | YoY |
|---|---|---|
| FY23 | 6.89 | — |
| FY24 | 8.03 | +16.5% |
| FY25 | 9.22 | +14.9% |
| FY26 | 11.48 | +24.5% |

- 3 年 CAGR（FY23 至 FY26）為 18.6%。yfinance 僅提供 4 個年度（FY22 為 null），無法計算 5 年 CAGR。
- 季度營收 FY26：Oct-25 2.47 → Jan-26 2.59（QoQ +4.8%）→ Apr-26 3.00（QoQ +15.7%）→ Jul-26 3.41（QoQ +13.6%）。Q4 YoY 為 +34.4%（對比 Jul-25 的 2.54）。
- 成長在 Q3 後加速，與商譽跳升（Jan-26 6.93B → Apr-26 21.90B）同期。**營收加速中有多少來自併購並表、多少為有機成長，本資料無法區分，需公司揭露的 organic growth 數據。**
- Segment 拆分：info.longBusinessSummary 只列產品線（Prisma Access、Cortex、Unit 42 等），沒有分部營收數字，無法做 segment 占比分析。

**獲利率趨勢**
| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Gross margin | 72.3% | 74.3% | 73.4% | 70.4% |
| Operating margin（GAAP） | 5.6% | 8.5% | 13.5% | 6.1% |
| Net margin（GAAP） | 6.4% | 32.1%（含稅務利益） | 12.3% | 2.7% |

- FY24 淨利率 32.1% 含 -1.59B USD 稅務利益（Tax Provision 為負），不具可比性。
- 季度毛利率：Oct-25 74.2%、Jan-26 73.6%、Apr-26 67.6%、Jul-26 67.6%。Q3 起下滑約 6 個百分點。折舊攤提（Reconciled Depreciation）FY26 為 855M USD，FY25 為 343M USD（+149%），推測為併購無形資產攤提進入成本，**需確認 non-GAAP 毛利率**。
- 季度營業利益：Oct-25 309M、Jan-26 397M、Apr-26 -183M、Jul-26 +172M（USD）。
- 費用結構 FY26：R&D 2.55B（22.2% 營收，FY25 為 21.5%）、S&M 3.93B（34.2%，FY25 為 33.6%）、G&A 0.90B（7.8%，FY25 為 4.8%）。
- 非營業損益：FY26「Other Income Expense」為 -533M USD（FY25 為 -8M），是 Q3、Q4 GAAP 虧損的主因之一，yfinance 未說明項目內容。
- 稅率：FY26 有效稅率約 42.7%（稅 229M / 稅前 536M）。Q3、Q4 稅前為負但仍有正稅費，季度稅率無參考價值。
- ROE（info）為 1.74%，與 NI 307M / 平均股東權益約 17.66B 相符。ROA 為 1.40%。
- ROIC（本報告估算，非資料源）：以 operating income 695M × (1-21%) ÷ 期末 invested capital 29.27B ≈ 1.9%；以平均 invested capital 18.55B 計約 3.0%。明顯低於資本成本，反映併購資本注入後的回報尚未顯現。
- EPS：FY26 GAAP diluted EPS 為 0.40（FY25 為 1.60）。四個季度 GAAP EPS 相加為 0.51，與年度 0.40 不符，原因是季度股數變動及季度資料不完整，以年度數字為準。

## Cashflow & balance sheet

**現金流品質**（USD B）
| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Operating CF | 2.78 | 3.26 | 3.72 | 4.55 |
| Capex | -0.15 | -0.16 | -0.25 | -0.44 |
| FCF | 2.63 | 3.10 | 3.47 | 4.11 |
| FCF margin | 38.2% | 38.6% | 37.6% | 35.8% |
| FCF / NI（GAAP） | 6.0x | 1.2x | 3.1x | 13.4x |

- FCF / NI 在 FY26 高達 13.4x，**主要因 GAAP NI 被攤提與 SBC 壓低**，此比值在本例中不具「>0.9 為健康」的判讀意義。
- SBC FY26 為 1.77B USD（占營收 15.5%；FY25 為 1.30B，占 14.0%）。扣除 SBC 後的 FCF 為 2.34B USD，FCF 扣 SBC margin 約 20.4%。這是品質上的主要保留：一部分 FCF 實際上是以股權稀釋支付。
- 季度 FCF：Oct-25 1.69B、Jan-26 0.38B、Apr-26 0.79B、Jul-26 1.25B（USD）。Q1 與 Q2 波動大，年度數字較具代表性。
- info 的 freeCashflow 為 4.24B，與現金流量表計算的 4.11B 不符（差約 0.13B），本報告採用現金流量表數字。

**資產負債表**（USD B，期末）
| 項目 | Jul-25 | Jan-26 | Apr-26 | Jul-26 |
|---|---|---|---|---|
| Cash + ST investments | 2.90 | 4.54 | 3.11 | 3.07 |
| Total debt | 0.34 | 0.37 | 2.07 | 2.50 |
| Net cash（cash − debt） | +2.57 | +4.16 | +1.04 | +0.57 |
| Goodwill | 4.57 | 6.93 | 21.90 | 22.01 |
| Total assets | 23.58 | 24.98 | 46.27 | 48.46 |
| Stockholders' equity | 7.82 | 9.39 | 27.67 | 27.49 |

- **淨現金由 +2.57B 降至 +0.57B USD**。Total debt 2.50B 中，long-term debt 為 1.77B，capital lease 為 0.73B。
- 商譽 22.01B 佔總資產 45.4%；**tangible book value 為 -1.54B USD**（Jan-26 為 +1.21B）。商譽減損是重要的資產負債表風險。
- 流動比率（info 與 BS 一致）為 0.87，速動比率 0.735，營運資金 -1.28B USD。Current liabilities 9.92B USD，其中含遞延收入，對 SaaS 而言屬常態，但需留意。
- Debt / Equity（info 口徑）為 9.3%（0.09x），槓桿本身不高。
- 現金減少：Jan-26 4.54B 降至 Jul-26 3.07B，主要反映併購現金支出。但 cashflow 中 FY26 Issuance of Debt 僅 10M USD，**顯示新增負債多為非現金併入（併購承接）或 yfinance 分類問題，需查閱 10-K 確認**。
- 推斷：Jan-26 至 Apr-26 期間商譽增加約 15.0B USD，流通股數由 703M 增至 813M（+110M 股）。這與股權加現金的併購結構吻合。資料本身未標示併購標的名稱，此推論需另行查證。

## Capital allocation & insider signal

**資本配置**
- Capex 占營收：FY23 2.1%、FY24 2.0%、FY25 2.7%、FY26 3.8%。Capex 占 OCF 為 9.7%，資本需求仍輕。
- 買回：FY23 273M、FY24 567M、FY25 0、FY26 1.00B USD。FY26 買回 1.00B USD **仍低於同期 SBC 1.77B USD，買回並未抵銷股權稀釋**。季度 cashflow 中 Jul-26 季為 0，其餘季度為 null，無法確認買回時點。
- 股本稀釋：期末流通股數 Jul-25 668M → Jul-26 815M（+22.0%）；FY26 平均稀釋股數 764M，較 FY25 的 709M 增加 7.7%。
- 股利：無（dividendYield 0，payoutRatio 0）。
- 債務：FY23 還款 1.69B、FY24 1.03B、FY25 0.97B、FY26 0.16B USD；償債後又在併購期間借入，槓桿回升。

**內部人交易（最近 6 個月，2026-04-29 至 2026-10-29）**
- 公開市場買進：0 筆、0 股、0 USD。
- 公開市場賣出：19 筆、約 155K 股、約 47.9M USD。
- 相對市值 322.87B USD，賣出金額僅約 0.015%，規模不大，與 SBC 解鎖與選擇權行權後的例行出售相符。
- 主要賣方：Klarich Lee（2026-05-22 賣出 62.9K 股，約 16.3M USD）、Golechha Dipak（CFO，2026-09-24 賣出 27.5K 股，約 10.8M USD）、Goetz James Joseph（董事，2026-09-17 賣出 20K 股，約 7.5M USD）、Paul Joshua D.（Senior VP & Chief Accounting Officer，定期小量出售）。
- 唯一大額公開買進：CEO Nikesh Arora 於 2026-03-27 以 146.87–147.48 USD 買進 68,085 股，約 10.0M USD。此事件距今約 7 個月，不在 6 個月窗口內，但仍是近兩年內極少見的內部人買進。
- 判讀：6 個月內為淨賣出、無公開買進。股價自 2026-03 的約 147 USD 漲至 394 USD 後，內部人持續在高點出售，與估值偏高的判斷方向一致。規模屬小，不足以單獨構成結論。
- 機構持股：84.1% 股權由機構持有（主要為 BlackRock、Vanguard、State Street）。做空方面：空單 21.27M 股，佔 float 2.6%，days to cover 3.73 天，較上月 21.87M 股略減。
- 治理風險（yfinance 評分，1 為最低、10 為最高）：overall 9、compensation 10、board 9、shareholder rights 9、audit 1。**薪酬與治理風險分數偏高**。CEO FY26 總薪酬約 4.33M USD。

## Valuation

**估值倍數**（市值 322.87B USD，股價 394.49 USD，流通股數 818.4M）
| 指標 | 數值 | 驗算 / 說明 |
|---|---|---|
| Trailing P/E（GAAP） | 986.2x | TTM EPS 0.40，n/m |
| Forward P/E | 80.9x | 394.49 ÷ forward EPS 4.879 |
| 當年度 EPS 倍數 | 94.1x | 394.49 ÷ epsCurrentYear 4.191 |
| PEG | 2.05 | info 提供 |
| P/S（TTM） | 28.1x | 322.87 ÷ 營收 11.48 = 28.1 |
| EV / Revenue | 28.1x | EV 322.19B ÷ 11.48B |
| EV / EBITDA（TTM，info） | 206.5x | EV 322.19B ÷ EBITDA 1.56B；GAAP 口徑 |
| P/FCF | 78.5x | 322.87 ÷ FCF 4.11 |
| P/B | 11.7x | info 提供 |

- Sector median 為本報告估計值（yfinance 不提供），供參考：大型雲端資安 / 基礎設施軟體 forward P/E 約 35–45x、P/S 約 10–14x、EV/EBITDA 約 30–40x、P/FCF 約 28–35x。上述區間未經資料來源驗證。
- 相對估計中位數，PANW 在所有指標上都溢價約 2 倍以上。PEG 2.05 高於 1，代表成長定價已相當充分。

**分析師預期與價格**
- 50 位分析師，recommendationMean 1.71（Buy 區間）。
- 目標價：平均 398.52（+1.0%）、中位數 415.00（+5.2%）、最高 525.00（+33.1%）、最低 190.00（-51.8%）。平均目標價已接近現價，上行空間有限。
- 價格位置：52 週區間 139.57–432.33；現價較 52 週高點低 8.8%，較 50 日均線 371.40 高 6.2%，較 200 日均線 267.99 高 47.2%。52 週漲幅 +80.7%。
- 10/29 盤前報 369.00（-6.5%），bid 380.76 / ask 414.78 價差極寬，僅可作為情緒訊號，不可作為可執行價格。

## Key catalysts
- **下次財報**：yfinance 估計 2026-11-19（尚未確認，isEarningsDateEstimate = true），consensus EPS 0.97（non-GAAP 口徑，依 earnings_dates）。前一季（Jul-26 季）non-GAAP EPS 1.02 對比 0.98 預期，小幅超出。
- **歷史超預期紀錄**：近 4 季皆超出預期，幅度 4.4%–9.9%（Nov-25 +4.4%、Feb-26 +9.9%、Jun-26 +6.6%、Sep-26 +4.4%）。yfinance earnings_dates 所列自 2020 年起的約 24 季皆為超預期。
- **併購整合與 GAAP 轉正**：Q3、Q4 GAAP 虧損，需觀察攤提與 SBC 下降後能否回正。Q4 營業利益由 Q3 的 -183M 轉為 +172M，是正向訊號。
- **毛利率**：Q3 起由 74% 降至 68%，需確認是否為一次性攤提，或為併購產品結構的長期壓力。
- **Guidance**：資料源未提供管理層最新 FY27 guidance 數字，需查閱 Q4 FY26 earnings release。
- **內部人與股權稀釋**：CFO、董事持續出售，若 SBC 與股權發行持續，每股指標會被稀釋。

## Metrics table

金額單位：USD（B 或 M）。TWD 與 KRW 不適用於本報告。

| Metric | Latest（FY26 / Jul-26） | YoY（vs FY25 / Jul-25） | Sector median（估計） | Verdict |
|---|---|---|---|---|
| 營收 Revenue（USD B） | 11.48 | +24.5% | 中高成長約 12–18% | 偏強 |
| Q4 營收 YoY（USD B） | 3.41 | +34.4% | — | 偏強（含併購） |
| 營收 3Y CAGR（FY23–26） | 18.6% | — | 約 15% | 偏強 |
| Gross margin | 70.4% | -3.0 pt | 約 75% | 偏弱 |
| Operating margin（GAAP） | 6.1% | -7.4 pt | 約 15–25%（non-GAAP 更高） | 偏弱 |
| Net margin（GAAP） | 2.7% | -9.6 pt | 約 5–10% | 偏弱 |
| ROE（info） | 1.7% | — | 約 10% | 偏弱 |
| ROIC（本報告估算） | 約 1.9%–3.0% | — | 約 8–12% | 偏弱 |
| OCF（USD B） | 4.55 | +22.5% | — | 強 |
| FCF（USD B） | 4.11 | +18.6% | — | 強 |
| FCF margin | 35.8% | -1.8 pt | 約 25–30% | 強 |
| FCF / NI（GAAP） | 13.4x | 不適用 | >0.9 健康 | 不具判讀意義 |
| FCF 扣 SBC margin | 20.4% | — | 約 15–20% | 中性 |
| SBC / 營收 | 15.5% | +1.5 pt | 約 10–15% | 偏弱 |
| Capex / 營收 | 3.8% | +1.1 pt | 約 3–5% | 中性 |
| 買回金額（USD B） | 1.00 | 由 0 增至 1.00 | — | 中性（不足以抵銷 SBC） |
| 期末流通股數（M 股） | 815M | +22.0% | 約 0–2%/年 | 偏弱（稀釋） |
| Total debt（USD B） | 2.50 | +7.4 倍（0.34 → 2.50） | — | 偏弱（槓桿回升） |
| Net cash（USD B） | +0.57 | -78%（+2.57 → +0.57） | — | 偏弱 |
| Debt / Equity | 0.09x | — | 約 0.2–0.4x | 中性 |
| Current ratio | 0.87 | — | 約 1.5x | 偏弱 |
| Goodwill / Total assets | 45.4% | +20.0 pt | 約 20–30% | 偏弱 |
| Tangible book value（USD B） | -1.54 | 由 +2.49 轉負 | — | 偏弱 |
| Trailing P/E（GAAP） | 986x | — | — | n/m |
| Forward P/E | 80.9x | — | 約 35–45x | 偏貴 |
| EV / EBITDA（TTM） | 206.5x | — | 約 30–40x | 偏貴 |
| P/S（TTM） | 28.1x | — | 約 10–14x | 偏貴 |
| P/FCF | 78.5x | — | 約 28–35x | 偏貴 |
| P/B | 11.7x | — | 約 4–6x | 偏貴 |
| 6 個月內部人淨買進（USD M） | -47.9（淨賣出） | — | — | 偏弱 |
| 做空比例（float） | 2.6% | 空單 -2.7% MoM | 約 3–5% | 中性 |
| 機構持股比例 | 84.1% | — | 約 70–80% | 中性 |
| 平均分析師目標價 vs 現價 | +1.0% | — | — | 中性 |

## Red flags
- **GAAP 獲利崩落**：FY26 淨利率 2.7%（FY25 為 12.3%）。Q3 與 Q4 皆為 GAAP 淨虧損（-177M、-282M USD）。
- **估值極端**：forward P/E 80.9x、P/S 28.1x、EV/EBITDA 206.5x，相對估計同業中位數溢價約 2 倍以上。盤前 -6.5% 顯示對任何 guidance 不如預期的反應會很劇烈。
- **SBC 與稀釋**：SBC 1.77B USD（占營收 15.5%），FY26 買回 1.00B USD 無法抵銷，期末股數 +22%。扣 SBC 後的 FCF 品質明顯低於表面 FCF margin。
- **商譽與有形資產**：商譽 22.01B USD（占總資產 45%），tangible book 為 -1.54B USD。若併購標的不如預期，有減損風險。
- **淨現金大幅縮水與流動性偏緊**：淨現金由 2.57B 降至 0.57B USD；流動比率 0.87，營運資金為 -1.28B USD。
- **毛利率下滑**：Q3 起由 74% 降至 68%，攤提與結構變化尚未釐清。
- **非營業損失與高稅率**：FY26 Other Income Expense -533M USD，有效稅率 42.7%，兩者都壓低 GAAP EPS，項目內容待確認。
- **內部人淨賣出**：6 個月約 47.9M USD 淨賣出、0 筆公開買進；CFO、董事於 2026-09 集中出售，股價在高點。規模上不足以單獨判斷，但方向一致。
- **治理與薪酬分數偏高**：yfinance overall governance risk 9、compensation risk 10（1–10 制）。
- **資料缺口**：(1) 季度買回與債務發行資料不完整，無法確認併購融資與買回時點；(2) 營收加速中併購貢獻與有機成長無法拆分；(3) info 的 FCF 與現金流量表不一致（4.24B vs 4.11B USD）；(4) 季度 EPS 加總（0.51）與年度（0.40）不一致；(5) 無 segment 數據與管理層最新 FY27 guidance；(6) 部分 yfinance 呼叫因 proxy 403 失敗，改用快取資料，數字需以 10-K 與 earnings release 驗證。
- **資料時效**：價格資料為 10/28 收盤與 10/29 盤前，DATE 為 10/30，10/30 之後價格未納入；下次財報日 2026-11-19 為估計值。

FUNDAMENTALS REPORT COMPLETE
