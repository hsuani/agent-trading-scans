# Fundamentals — WDC (Western Digital) as of 2026-10-14

## Executive summary
WDC 的財務體質在 FY26（截至 2026-06-30）明顯改善：總債務由 FY25 的 47.1 億美元降至 10.5 億美元、現金 15.8 億美元、FY26 FCF 35.1 億美元（FCF margin 27.2%）。然而 FY26 GAAP 淨利 92.98 億美元含 64.98 億美元「出售業務收益」等一次性項目，trailing P/E 14.1x、ROE 130.9% 皆被扭曲，剔除後 normalized 淨利約 37.8 億美元，仍較 FY25 成長約 79%。估值方面，以 non-GAAP TTM EPS 計算 trailing P/E 約 37x、P/FCF 約 41x、EV/EBITDA 約 27x，估值已不便宜；forward P/E 落在 11.5x–18.6x 之間，取決於採用的 EPS 基準（資料源內部不一致，見 Red flags）。

## Revenue & profitability

**營收與成長**
- 總營收（Total Revenue）：FY23 62.55 億 → FY24 63.17 億 → FY25 95.20 億 → FY26 129.19 億美元。
- FY26 YoY +35.7%；FY25 YoY +50.7%；FY24 YoY +1.0%。
- FY23→FY26 三年 CAGR 約 27.3%（由 yfinance 年度數值計算）。yfinance 未提供 FY22 數據，無法做四年以上 CAGR。
- 季度趨勢（以季末日期標示）：2025-06 季 26.05 億 → 2025-09 季 28.18 億 → 2025-12 季 30.17 億 → 2026-03 季 33.37 億 → 2026-06 季 37.47 億美元。最新季 YoY +43.8%（對 2025-06 季 26.05 億），連續四季環比成長。
- 分部營收（segment mix）：yfinance 的 `longBusinessSummary` 僅列產品線（內接式 HDD、data center drives / platforms、外接式、可攜式、NAS），未提供分部營收占比。分部數據 DATA_UNAVAILABLE。

**獲利率（由 yfinance 年度損益表計算）**

| 年度 | Gross margin | Operating margin（reported） | Net margin（GAAP） | Normalized net margin |
|---|---|---|---|---|
| FY23 | 22.2% | -6.4% | -26.9% | 不適用（負值） |
| FY24 | 28.1% | 1.5% | -12.6% | 不適用（負值） |
| FY25 | 38.8% | 22.4% | 19.6% | 22.2% |
| FY26 | 48.9% | 35.6% | 72.0%（含一次性收益） | 29.3% |

- 毛利率與營業利益率連續三年擴張。季度層面，2025-06 季毛利率 41.0% → 2026-06 季 54.1%；營業利益率 26.1% → 42.9%。
- Normalized EBITDA margin：FY25 27.4% → FY26 35.9%（4.638 億 / 129.19 億 → 以 46.38 億美元計）。
- FY26 出現 65 億美元「Gain On Sale Of Business」（yfinance 欄位 6,498M），現金流量表 FY26 `Sale Of Business` 為 0，性質（現金或非現金、是否與 FY25 剝離案相關）需 10-K 確認，DATA_UNAVAILABLE。
- FY26 `Special Income Charges` 合計 +58.07 億美元（yfinance `Total Unusual Items`），GAAP 數字因此不可直接用於評估營運獲利。
- ROE：yfinance 報 130.9%（GAAP，受一次性收益影響）；以 normalized 淨利 37.81 億 / 平均股東權益約 72.02 億（期初 55.40 億、期末 88.64 億）計算約 52.5%。
- ROA（yfinance）20.8%。
- ROIC 估算：以 FY26 Operating Income 45.99 億、假設稅率 25%（接近 FY25 有效稅率 25.6%）計算 NOPAT 約 34.5 億；平均投入資本（yfinance Invested Capital 99.16 億 / 100.22 億）約 99.7 億 → ROIC 約 34.6%。此為模型估算，非資料源直接提供。

**EPS**
- GAAP diluted EPS：FY23 -5.37、FY24 -2.61、FY25 5.12、FY26 26.92（含一次性收益）。
- 公司 non-GAAP（adjusted）EPS（yfinance earnings_dates 的 Reported EPS）：2025-10 季 1.78、2026-01 季 2.13、2026-04 季 2.72、2026-08 季 3.56，TTM 合計 10.19 美元。
- Normalized diluted EPS（normalized 淨利 / FY26 diluted shares 3.83 億）約 9.87 美元（FY25 約 5.88 美元），成長約 68%。

## Cashflow & balance sheet

**現金流量品質**
- 營業現金流（OCF）：FY24 -2.94 億 → FY25 16.91 億 → FY26 39.29 億美元。
- Capex：FY26 4.18 億（占營收 3.2%；FY25 4.3%，FY24 7.7%，FY23 13.1%）。
- FCF（OCF - capex）：FY25 12.79 億、FY26 35.11 億美元。FCF margin：FY25 13.4%、FY26 27.2%。
- FCF / 淨利（GAAP）：FY26 0.38（受收益扭曲）；FY25 0.69。FCF / normalized 淨利：FY26 約 0.93（達健康門檻 0.9）；FY25 約 0.61。
- 最新季（2026-06）FCF 12.81 億美元（OCF 13.89 億、capex 1.08 億），季度 FCF 自 2025-09 季起連續四季成長：2025-06 季 6.75 億 → 2025-09 季 5.99 億 → 2025-12 季 6.53 億 → 2026-03 季 9.78 億 → 2026-06 季 12.81 億美元。
- SBC：FY26 2.04 億美元（占營收 1.6%）。

**資產負債表（FY26 期末，2026-06-30）**
- 現金及約當現金：15.79 億美元（FY25 21.14 億；2026-03 季末 32.37 億含短期投資，季度內下降約 16.6 億，yfinance 未拆解原因，DATA_UNAVAILABLE）。
- 總債務（Total Debt）：10.52 億美元（FY25 47.11 億，FY24 74.34 億）。兩年內減少約 64.2 億，FY26 單年減少 36.59 億（-78%）。
- 淨負債：FY26 約為淨現金 5.27 億美元（1.579 - 1.052 = 0.527）。FY25 淨負債 25.97 億美元。
- yfinance `totalDebt`（info）為 11.91 億（含租賃）。
- 長期債務（Long Term Debt）FY26 為 null，全部債務皆列於 Current Debt 10.52 億，此分類需 10-K 核實（可能為到期重分類）。
- 流動比率（Current Ratio）1.33（流動資產 56.34 億 / 流動負債 42.40 億）；速動比率（yfinance quickRatio）0.85。
- 營運資本：14.94 億（FY26）vs 4.38 億（FY25）。
- 股東權益：88.64 億美元（FY25 55.40 億，+60%）。Debt / Equity（含租賃，yfinance）13.4%；以 Total Debt 計算約 11.9%。
- 商譽加無形資產 43.21 億美元；有形帳面價值（tangible book）45.43 億美元。
- 存貨：15.11 億美元（FY25 12.91 億，+17%，低於營收成長 +36%，庫存效率改善）。

## Capital allocation & insider signal

**資本配置**
- 買回股票（Repurchase of Capital Stock）：FY24 0.05 億、FY25 1.49 億、FY26 25.92 億美元。FY26 四季分別為 5.53 億、6.15 億、7.52 億、6.72 億。
- 股利：FY25 起開始配息。FY26 現金股利合計 1.84 億美元（含特別股股利 0.10 億）。最新季股利 0.15 美元/股（yfinance `lastDividendValue`），目前殖利率 0.16%（yfinance `dividendYield`）。
- 股利覆蓋：FY26 FCF / 股利 約 19.1x；買回 + 股利合計 27.76 億，約為 FY26 FCF 的 79%。
- 債務：FY26 償還 28.84 億、新增 19.46 億，淨償還 9.38 億美元。
- 稀釋：FY26 基本加權股數 3.45 億、稀釋加權 3.83 億，差距約 11%；期末流通股數 3.61 億（FY25 3.47 億），yfinance `sharesOutstanding` 3.74 億（當前）。儘管買回 25.9 億，期末股數仍較 FY25 增加，需關注 SBC 與可轉換/特別股轉換的稀釋影響。
- 特別股：FY25 資產負債表有 2.29 億特別股，FY26 期末為 0。

**內部人交易（2026-04-14 至 2026-10-14，6 個月）**
- 公開市場賣出：20 筆，合計 78,359 股，依 yfinance `Value` 欄位合計約 3,562 萬美元。
- 賣出金額依人員：Irving Tan（CEO）約 1,714 萬（2026-05-01 賣 20,000 股 約 823 萬；2026-08-11 賣 20,000 股 約 890 萬）、Brian Scott Davis 約 501 萬、Vidyadhara Gubbi 約 427 萬、Martin Cole（Director）約 386 萬、Stephanie Streeter（Director）約 252 萬、Cynthia Tregillis 約 242 萬、Bruce Kiddoo 約 40 萬。
- 公開市場買入：0 筆。
- 非市場交易：股票獎勵（Grant）47,052 股（2026-08-25 年度授予為主）；贈與（Gift）112,600 股（Tan 11.25 萬股於 2026-09-01、Kiddoo 100 股於 2026-05-15）。贈與不計為賣出。
- 規模比較：6 個月賣出約 3,562 萬美元 / 市值 1,425 億美元 ≈ 0.025%，佔比極小。內部人持股僅 0.27%（yfinance `heldPercentInsiders`），對股價的訊號意義有限。
- 注意：Tan 的兩筆 2 萬股賣出分別位於 2026-05-01（約 $410）與 2026-08-11（約 $444），價位高於現價 380.71；2026-09 之後無新增公開市場賣出紀錄。

**機構持股**
- 機構持股比率 88.9%（yfinance `heldPercentInstitutions`），機構數 2,474 家。
- 前幾大持股（2026-06-30 申報）：BlackRock 8.8%（季變 -7.9%）、FMR 6.9%（-17.8%）、Vanguard Capital Mgmt 6.0%（+2.2%）、JPMorgan 4.5%（-2.9%）、Capital World 4.4%（+39.7%）、State Street 4.35%（+5.2%）、Invesco 3.9%（+14.2%）。前十大有增有減，無明顯單向集中出貨或加碼。
- 空單：短期空單 1,829 萬股，占浮動股數約 5.46%，回補天數（short ratio）2.77 日，較前月（1,989 萬股）下降約 8%。

## Valuation

**價格資料**
- 最新常規交易收盤價 380.71 美元（2026-10-13 16:00 EDT，較前收 386.94 下跌 1.61%）。
- 2026-10-14 盤前報價 372.68 美元（-2.11%）。此為 as-of 日當日盤前資料，非 post-date。
- 52 週區間 113.50–799.87；現價距 52 週高點 -52.4%，較 52 週低點 +235%。
- 50 日均線 451.52（現價低 15.7%）；200 日均線 407.95（現價低 6.7%）。
- Beta 2.169。

**估值倍數（以現價 380.71、市值 1,425.1 億計算，或採用 yfinance info 欄位）**

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E（GAAP） | 14.1x | yfinance trailingPE，受一次性收益扭曲 |
| Trailing P/E（non-GAAP TTM） | 約 37.4x | 380.71 / 10.19（4 季 adjusted EPS 合計） |
| Forward P/E | 11.5x | yfinance forwardPE（forwardEps 33.09） |
| Forward P/E（current year） | 18.6x | 380.71 / 20.52（epsCurrentYear），與上列不一致 |
| EV / EBITDA | 27.4x | yfinance enterpriseToEbitda（EBITDA 50.02 億） |
| EV / EBITDA（normalized） | 約 29.5x | EV 1,368.7 億 / normalized EBITDA 46.38 億 |
| P / FCF | 約 40.6x | 1,425.1 億 / FY26 FCF 35.11 億 |
| P / S（trailing） | 11.0x | yfinance priceToSalesTrailing12Months |
| P / B | 15.5x | yfinance priceToBook（BVPS 24.55） |
| PEG | 0.74 | yfinance pegRatio（trailingPegRatio 0.90） |

**分析師共識（24 家）**
- 推薦均值 1.54（Buy）。目標價：平均 668.5、中位數 650、最高 1,050、最低 420。
- 相對現價上行空間：平均 +75.6%、中位數 +70.7%、最低 +10.3%。全部目標價皆高於現價。

**與板塊中位數比較（模型估計，非 yfinance 來源）**
- 儲存 / 記憶體硬體板塊估計：forward P/E 約 15–20x、EV/EBITDA 約 12–16x、P/FCF 約 20–30x、P/S 約 2–4x、毛利率約 30–40%、ROE 約 10–20%。
- 以此估計，WDC 的 forward P/E 處於中位數附近或略低，EV/EBITDA 與 P/FCF 偏高，P/S 明顯偏高。

## Key catalysts
- **下次財報**：2026-10-22（yfinance `earningsTimestamp`，`isEarningsDateEstimate` = false）。FQ1 FY27 EPS 共識估計 4.08 美元（yfinance `earnings_dates`）。
- **上次財報**（2026-08-05 公布）：adjusted EPS 3.56 美元，對 3.30 美元共識 +7.87% 超預期。
- **盈餘超預期紀錄**：近 8 季中 7 季超預期，平均超預期幅度約 +10%；2025-01 季為唯一低於預期（-2.68%）的季度。
- 隱含 QoQ 成長：4.08 / 3.56 - 1 ≈ +14.6%（以共識估計計算）。
- **股利**：最近一次除息日 2026-09-08（yfinance `exDividendDate`），每股 0.15 美元；下次除息日 DATA_UNAVAILABLE。
- **指引（guidance）**：yfinance 無公司指引文字，DATA_UNAVAILABLE。
- **FY26 一次性項目**：6.5 億美元級別「出售業務收益」的性質與未來是否還有類似收益，需以 10-Q/10-K 與 earnings release 核實。
- **資料時間**：本報告以 as-of 2026-10-14 整理，yfinance 快取時間 2026-10-14 11:38–11:43 UTC，最新數據與 as-of 日同日，無明顯 post-date 資料。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（FY26） | 129.19 億 | +35.7% | 不適用（需板塊資料） | 強勁成長 |
| 三年營收 CAGR（FY23–26） | 27.3% | 不適用 | 不適用 | 高成長，週期性需留意 |
| 毛利率（FY26） | 48.9% | +10.1 pp | 30–40% | 優於板塊 |
| 營業利益率（FY26，reported） | 35.6% | +13.2 pp | 10–20% | 優於板塊 |
| Normalized 淨利率（FY26） | 29.3% | +7.1 pp | 10–15% | 優於板塊 |
| GAAP 淨利率（FY26） | 72.0% | 不適用（一次性收益） | 不適用 | 不可用於評估 |
| ROE（normalized，估算） | 約 52.5% | 不適用 | 10–20% | 優於板塊 |
| ROE（GAAP，yfinance） | 130.9% | 不適用 | 10–20% | 受收益扭曲，不可用 |
| ROIC（估算） | 約 34.6% | 不適用 | 8–12% | 高於 WACC，屬優質 |
| 營業現金流（FY26） | 39.29 億 | +132% | 不適用 | 強勁 |
| FCF（FY26） | 35.11 億 | +175% | 不適用 | 強勁 |
| FCF margin | 27.2% | +13.8 pp | 10–15% | 優於板塊 |
| FCF / normalized 淨利 | 約 0.93 | 由約 0.61 改善 | 約 0.8–1.0 | 健康 |
| Capex / 營收 | 3.2% | -1.1 pp | 約 5–8% | 資本開支輕 |
| 現金 | 15.79 億 | -25.3% | 不適用 | 足夠但較 FY25 減少 |
| 總債務 | 10.52 億 | -77.7% | 不適用 | 大幅去槓桿 |
| 淨負債（淨現金） | 約 -5.27 億（淨現金） | 由 +25.97 億 改善 | 約 0–2x EBITDA | 健康 |
| 流動比率 | 1.33 | 由 1.08 改善（見注 1） | 約 1.5–2.0 | 尚可 |
| Debt / Equity（含租賃，yfinance） | 13.4% | 由 84.9% 降低 | 約 20–40% | 優於板塊 |
| 股東權益 | 88.64 億 | +60.0% | 不適用 | 改善 |
| 有形帳面價值 | 45.43 億 | +358% | 不適用 | 改善 |
| 股利 / FCF 覆蓋 | 約 19.1x | 不適用 | 不適用 | 股利安全 |
| 買回金額（FY26） | 25.92 億 | 約 17x（FY25 1.49 億） | 不適用 | 積極回購 |
| 稀釋加權股數 | 3.83 億 | +6.7% | 不適用 | 期末股數仍增，需關注 |
| 內部人 6 個月賣出 | 約 3,562 萬美元（78,359 股） | 不適用 | 不適用 | 占市值 0.025%，訊號弱 |
| 內部人公開買入 | 0 筆 | 不適用 | 不適用 | 中性偏弱 |
| 機構持股比率 | 88.9% | 不適用 | 不適用 | 高 |
| 空單佔浮動股數 | 5.46% | 下降約 8%（月） | 約 3–8% | 正常 |
| Trailing P/E（GAAP） | 14.1x | 不適用 | 約 15–20x | 被收益扭曲，不可用 |
| Trailing P/E（non-GAAP TTM） | 約 37.4x | 不適用 | 約 15–20x | 偏高 |
| Forward P/E | 11.5x（forwardEps）/ 18.6x（current yr） | 不適用 | 約 15–20x | 依 EPS 基準而異 |
| EV / EBITDA | 27.4x | 不適用 | 約 12–16x | 偏高 |
| P / FCF | 約 40.6x | 不適用 | 約 20–30x | 偏高 |
| P / S | 11.0x | 不適用 | 約 2–4x | 明顯偏高 |
| P / B | 15.5x | 不適用 | 約 2–4x | 明顯偏高 |
| PEG | 0.74 | 不適用 | 約 1.0–1.5 | 便宜（依分析師成長假設） |
| 分析師平均目標價 | 668.5 | 相對現價 +75.6% | 不適用 | 共識正向 |
| 盈餘超預期（最近一季） | +7.87% | 不適用 | 不適用 | 強勁 |

注 1：FY25 流動比率為計算值（流動資產 58.56 億 / 流動負債 54.18 億 = 1.08），yfinance 未直接提供；FY26 1.33 與 yfinance info `currentRatio` 一致。

## Red flags
- **GAAP 獲利被一次性收益大幅扭曲**：FY26 GAAP 淨利率 72.0%、ROE 130.9%、trailing P/E 14.1x 皆不可直接使用；需以 normalized 或 non-GAAP 數字評估。
- **一次性收益性質不明**：FY26 「出售業務收益」65 億美元，但現金流量表無對應現金流入（Sale of Business = 0），需確認是否為非現金交易、是否可重複。
- **估值已反映大幅成長**：non-GAAP trailing P/E 約 37x、P/FCF 約 41x、EV/EBITDA 約 27x、P/S 11x，對週期性硬體公司而言偏高；估值仰賴 HDD 需求持續高位。
- **Forward EPS 來源不一致**：yfinance `forwardEps` 33.09 與 `epsCurrentYear` 20.52 差距達 61%，forward P/E 在 11.5x 至 18.6x 之間，無法確定哪一個為正確共識；另 `freeCashflow`（info）22.68 億與報表 FCF 35.11 億不一致，`operatingMargins`（info）43.6% 與報表計算 35.6% 不一致。以上須以原始來源核實。
- **季度現金下降**：2026-03 季末現金及短期投資 32.37 億，2026-06 季末降至 15.79 億（季減約 16.6 億），同期買回 6.72 億、償債、FCF 12.81 億，其餘流出 yfinance 未拆解，DATA_UNAVAILABLE。
- **債務全部列為流動負債**：FY26 Long Term Debt 為 null，Current Debt 10.52 億，若屬實則 12 個月內到期債務需以 1.58 億現金與 FCF 支應，需核實。
- **股數仍在增加**：儘管 FY26 買回 25.9 億美元，期末股數 3.61 億較 FY25 的 3.47 億增加；稀釋加權股數 3.83 億較基本 3.45 億高約 11%，每股買回效果被稀釋抵銷一部分。
- **歷史獲利波動大**：FY23 淨損 16.84 億、FY24 淨損 7.98 億，FY25 才轉正；HDD 週期性強，股價 52 週區間 113.5–799.87，波動極大（beta 2.17）。
- **股價距高點大幅回落**：現價 380.71 較 52 週高點 799.87 回落 52.4%，且低於 50 日與 200 日均線，趨勢面偏弱，與基本面改善的敘事背離，需由 technical 與 sentiment 報告補充。
- **資料缺口**：分部營收、公司指引、一次性收益性質、FY22 以前歷史數據皆為 DATA_UNAVAILABLE；FY24 與 FY23 營收可能未反映剝離後的可比基礎（推測，需 10-K 核實）。

FUNDAMENTALS REPORT COMPLETE
