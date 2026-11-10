# Fundamentals — ASML as of 2026-11-10

資料來源：`pipeline/tools/yf`（live 抓取遭 Yahoo 403 封鎖，改用 `prices/yf/ASML.json` 快取，快取時間 2026-11-10 14:47 UTC，依指示視為有效）。貨幣單位：工具回傳為 USD，本報告金額統一以 USD B（十億美元）表示。ASML 原始財報為 EUR，工具之 USD 換算方式未驗證。資料截止於 2026-11-10，未發現晚於 as-of 日期的財報資料（最新已揭露季度為 2026-09-30，財報日 2026-10-14）。

## Executive summary

ASML 財務體質極佳：Q3 2026 毛利率 57.4%、營業利益率 44.4%，Q3 淨現金約 10.8B USD，TTM FCF 為季度加總的 21.0B USD，屬高品質獲利。估值面則明顯偏高，TTM EV/EBITDA 約 35.3x、trailing P/E 37–43x、P/FCF 約 28x，僅 forward P/E 23.9x 相對合理，代表市場已預期未來 EPS 顯著成長（forward EPS 63.40）。Yahoo 快取中有多個欄位數值明顯錯誤（EV、P/B、EV/EBITDA），本報告一律改以季度財報重新計算，並在紅旗段列出。

## Revenue & profitability

**營收**
- 年度營收（USD B）：FY2022 21.17 → FY2023 27.56 → FY2024 28.26 → FY2025 32.67
- FY2025 YoY +15.6%；FY2024 YoY +2.6%
- 2022–2025 三年 CAGR 約 15.6%；2023–2025 兩年 CAGR 約 8.9%
- TTM 營收 39.47B USD（季度加總，與 info.totalRevenue 39.47B 一致）
- 季度趨勢（USD B）：Q4'25 9.72 → Q1'26 8.77 → Q2'26 9.33 → Q3'26 11.66；Q3'26 YoY +55.2%（對 Q3'25 的 7.52B）
- 營收成長在 2026 年明顯加速，但 Q1'26 季增為負，單季波動大
- 業務結構：info.longBusinessSummary 列出光刻（EUV / DUV）、量測與檢測（YieldStar、HMI 電子束）、computational lithography、翻新升級與服務四大類，但未提供分部營收比重，**分部營收占比為 DATA_UNAVAILABLE**

**獲利能力（利潤率）**

| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 50.5% | 30.7% | 26.6% |
| FY2023 | 51.3% | 32.8% | 28.4% |
| FY2024 | 51.3% | 31.9% | 26.8% |
| FY2025 | 52.8% | 34.6% | 29.4% |
| Q4'25 | 52.2% | 35.3% | 29.2% |
| Q1'26 | 53.0% | 36.0% | 31.4% |
| Q2'26 | 54.0% | 37.1% | 31.3% |
| Q3'26 | 57.4% | 44.4% | 42.5% |
| TTM | 約 55% | 38.6% | 34.1% |

- TTM 營業利益 15.22B、淨利 13.47B、EBITDA 16.24B（季度加總）
- Q3'26 淨利率 42.5% 含約 0.51B USD 的非營業收入（Other Income Expense，列於營業利益之下），詳見紅旗段
- ROE：FY2025 約 50.5%（以年初年末平均權益計）；FY2024 約 47.4%；TTM 以 Q3 期末權益計約 61.1%
- ROIC：FY2025 約 38.7%（營業利益 × (1 − 有效稅率 17.7%) ÷ Invested Capital 240.03B USD），屬估算值

**EPS**
- FY2025 Diluted EPS 24.71（FY2024 19.24，FY2023 20.59，FY2022 16.07）
- 季度 Diluted EPS：Q3'25 5.48 → Q4'25 7.34 → Q1'26 7.15 → Q2'26 7.58 → Q3'26 12.93（Yahoo 季度財報）
- TTM EPS 以季度加總為 35.00；info.trailingEps 為 40.64，**兩者不一致，見紅旗**
- Earnings history：近 4 季 EPS surprise 分別為 +9.86%（Q3'26，財報日 2026-10-14）、+9.09%（Q2'26）、+7.99%（Q1'26）、−2.72%（Q4'25）

## Cashflow & balance sheet

**現金流**

| 期間 | OCF | 資本支出 | FCF | FCF 利潤率 | FCF / NI |
|---|---|---|---|---|---|
| FY2022 | — | 1.32B | 7.17B | 33.9% | 1.27 |
| FY2023 | — | 2.20B | 3.25B | 11.8% | 0.41 |
| FY2024 | — | 2.08B | 9.08B | 32.1% | 1.20 |
| FY2025 | — | 1.63B | 11.03B | 33.8% | 1.15 |
| TTM（季度加總） | 22.73B | 1.73B | 21.00B | 53.2% | 1.56 |

- FY2025 FCF/NI 1.15，高於 0.9 健康門檻；FY2023 僅 0.41，顯示現金流波動大
- TTM FCF 之所以遠高於年度水準，主要來自 Q3'26 單季 OCF 達 11.80B USD；同期（Q4'25 至 Q3'26）應收帳款由 3.02B 升至 9.25B，但 OCF 仍大幅正向，代表可能有預收款或合約負債流入，**需以 10-Q 驗證**。Q1'26 OCF 為 −2.19B USD，單季波動極大
- info.freeCashflow 為 10.37B，與季度推算之 21.00B 不符，**不採用**

**資產負債表（Q3'26，2026-09-30）**
- 現金及短期投資 12.74B；總債務 1.96B；**淨現金約 10.77B USD**（Q4'25 為 8.93B）
- 股東權益 22.06B；總資產 58.98B；總負債約 36.92B
- Current ratio 1.49（Q4'25 為 1.26）
- Debt / Equity 0.089x（Yahoo 欄位 8.897 為百分比表示，非 8.9x）
- 總債務自 Q4'25 的 4.39B 降至 Q3'26 的 1.96B，槓桿明顯下降
- 存貨 Q3'26 為 1.19B；應收帳款 Q3'26 為 9.25B，較 Q4'25 大增
- 非流動負債 Q3'26 較 Q2'26 增加約 5.78B USD（由 6.24B 增至 12.01B），**內容 DATA_UNAVAILABLE**
- Goodwill 約 4.59B USD；Other Intangible Assets 約 0.54B USD

## Capital allocation & insider signal

**資本配置**
- 資本支出占營收：FY2022 6.2%、FY2023 8.0%、FY2024 7.4%、FY2025 5.0%；TTM 約 4.4%。資本支出絕對值自 FY2023 高點 2.20B 降至 FY2025 1.63B
- 買回股票：FY2024 0.50B、FY2025 5.95B；TTM 7.85B，其中 Q3'26 單季 4.07B（Q2'26 為 1.08B）
- 股利：FY2025 現金股利支出 2.55B；TTM 3.00B；info.dividendRate 9.31 USD/股，殖利率 0.62%，payout ratio 22.3%
- 股利覆蓋：FY2025 FCF 為股利的 4.3 倍，覆蓋充足
- 流通股數：FY2022 期末 Ordinary Shares 約 395M 股 → FY2025 約 385M 股（Q3'26 約 385M 股）；持續淨縮股
- info.exDividendDate 為 2026-10-27，早於 as-of 日期，**實際配息是否已發放未驗證**

**內部人交易（6 個月）**
- insider 端點回傳空陣列，**6 個月內內部人交易 DATA_UNAVAILABLE**，無法判定淨買或淨賣，亦不應推定為零交易
- 內部人持股比例 heldPercentInsiders 僅 0.008%，即使全數交易也只占極小比例，對市值影響可忽略
- 機構持股 20.4%（約 3,007 家），前幾大機構：FMR（1.41%，2026-06-30 增持 74%）、Fisher Asset Management（1.25%，2026-09-30 增持 2.1%）、Capital World Investors（0.96%，減持 0.2%）、Invesco（0.81%，增持 5.7%）

## Valuation

以 2026-11-10 快取價 1513.25 USD 計算（市值以 info.marketCap 584.79B USD 為準；價格 × 股數 385.4M 股 ≈ 583.2B，差異約 0.3%）。EV 以 市值 + 總債務 − 現金 重算為 574.0B USD。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | 37.3x（info）／43.2x（TTM EPS 35.00 重算） | 兩者差異來自 EPS 來源不一致 |
| Forward P/E | 23.9x | forwardEps 63.40 |
| EV/EBITDA（TTM） | 35.3x | EBITDA 16.24B |
| EV/Revenue（TTM） | 14.5x | |
| P/S（TTM） | 14.8x | info.priceToSalesTrailing12Months 14.81，一致 |
| P/FCF（TTM，季度推算） | 27.8x | FCF 21.00B |
| P/FCF（info） | 56.4x | 不採用，見紅旗 |
| P/B | 26.5x | 以 Q3'26 權益 22.06B 重算；info.priceToBook 1302.8 明顯錯誤 |

- 股價位於 52 週區間中段（52W 低 946.11、高 1999.96，位置約 54%），低於 50 日均線 1673.60（−9.6%）與 200 日均線 1600.77（−5.5%）
- 分析師共識（快取 rec_summary，0m）：7 Strong Buy、31 Buy、2 Hold、1 Sell、0 Strong Sell；info.targetMeanPrice 2145.62，較現價上行約 41.8%；numberOfAnalystOpinions 17；recommendationKey strong_buy
- 估值判讀：以 trailing 指標看偏貴，以 forward 指標看合理。forward EPS 63.40 相對 TTM EPS 35.00 隱含約 81% 的盈餘成長預期，估值成敗高度取決於此成長兌現程度

## Key catalysts

- **已發布**：Q3'26 財報於 2026-10-14 發布，EPS 實際 11.82（Yahoo earnings_dates）／12.93（季度財報），超出預期 EPS 10.76 約 9.9%
- **下次財報**：2027-01-27（Q4'26），consensus EPS 15.39
- **近期指引（guidance）文字**：DATA_UNAVAILABLE，工具未提供管理層展望數字
- **業務面**：Q3'26 毛利率與營業利益率明顯跳升，若能持續，將驗證 2026 年的營收加速；EUV / 先進製程需求為主要變數，但本報告未取得需求端的具體來源，不予推論
- **資本回報**：Q3'26 單季買回 4.07B USD，為近年最大單季買回，後續是否延續需觀察 10-Q / 公告
- **股利**：ex-dividend 日 2026-10-27 已過，發放狀況待確認

## Metrics table

金額單位：USD B；比率單位：%、x。「Sector median (estimate)」為**估計值，非資料源計算**，僅供參照。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（USD B） | 39.47 | Q3'26 YoY +55.2%；FY25 YoY +15.6% | 成長 約 8–12%（估計） | 強，高於同業估計 |
| 毛利率（Q3'26） | 57.4% | FY25 52.8%（FY24 51.3%，+1.5pt） | 約 45%（估計） | 優 |
| 營業利益率（TTM） | 38.6% | FY25 34.6%（FY24 31.9%，+2.7pt） | 約 25%（估計） | 優 |
| 淨利率（TTM） | 34.1% | FY25 29.4%（FY24 26.8%） | 約 20%（估計） | 優；Q3 含非營業收入 |
| ROE（FY25 平均權益） | 50.5% | FY24 47.4% | 約 15%（估計） | 優 |
| ROIC（FY25 估算） | 38.7% | — | 約 12%（估計） | 優，為估算值 |
| FCF 利潤率（TTM） | 53.2% | FY25 33.8% | 約 15%（估計） | 優，但單季波動大 |
| FCF / NI（FY25） | 1.15 | FY24 1.20；FY23 0.41 | > 0.9 為健康 | 健康，但 FY23 偏弱 |
| 淨現金（Q3'26，USD B） | +10.77 | Q4'25 +8.93 | 約 0 至小幅淨現金（估計） | 強 |
| Debt / Equity（Q3'26） | 0.089x | Q4'25 0.22x（4.39/19.61） | 約 0.3x（估計） | 優 |
| Current ratio（Q3'26） | 1.49 | Q4'25 1.26 | 約 2.0（估計） | 偏低於同業估計，但仍 > 1 |
| 資本支出 / 營收（FY25） | 5.0% | FY24 7.4% | 約 5–7%（估計） | 中性 |
| 買回金額（TTM，USD B） | 7.85 | FY25 5.95；FY24 0.50 | — | 積極 |
| 股利覆蓋（FY25 FCF / 股利） | 4.3x | — | 約 2–3x（估計） | 充足 |
| 股利殖利率 | 0.62% | 5 年平均 0.77% | 約 1%（估計） | 偏低 |
| 6 個月內部人交易 | DATA_UNAVAILABLE | — | — | 無法判定 |
| 機構持股比例 | 20.4% | — | — | 中性 |
| Trailing P/E | 37.3x（info）／43.2x（重算） | — | 約 30x（估計） | 偏貴 |
| Forward P/E | 23.9x | — | 約 25–30x（估計） | 略低於同業估計 |
| EV/EBITDA（TTM） | 35.3x | — | 約 20–25x（估計） | 偏貴 |
| P/S（TTM） | 14.8x | — | 約 6–10x（估計） | 偏貴 |
| P/FCF（TTM，季度推算） | 27.8x | — | 約 25–30x（估計） | 中性 |
| P/B | 26.5x | — | 約 4–6x（估計） | 偏貴 |

## Red flags

- **EPS 來源不一致**：Q3'26 Diluted EPS 季度財報為 12.93，Yahoo earnings_dates 的 Reported EPS 為 11.82；差額約 1.11 USD，與 Q3 的非營業收入約 0.51B USD（稅後約 0.43B）相符，推估 11.82 為排除該項目後的數字。TTM EPS 亦出現 35.00（季度加總）與 40.64（info.trailingEps）的落差。**需以公司公告確認 EPS 定義**
- **Yahoo info 欄位明顯錯誤，未採用**：enterpriseValue 為 3.22e13 USD（約為市值的 55 倍）、enterpriseToEbitda 1989.8、priceToBook 1302.8、info.freeCashflow 10.37B 與季度推算 21.00B 不符。本報告 EV、EV/EBITDA、P/B、P/FCF 皆以季度數據重算
- **TTM FCF 高度依賴 Q3'26 單季**：Q1'26 FCF 約 −2.61B USD、Q3'26 FCF 約 11.35B USD；應收帳款由 Q4'25 3.02B 升至 Q3'26 9.25B，若為收款時點差異，後續季度可能回落
- **Q3'26 非流動負債增加約 5.78B USD**，性質 DATA_UNAVAILABLE；Q3'26 投資活動現金流為 −4.69B USD，亦未拆解
- **Q3'26 淨利率 42.5%** 含非營業收入，單季利潤率高點不宜外推至 Q4'26
- **估值偏貴**：trailing P/E、EV/EBITDA、P/S、P/B 皆為高位，估值支撐完全來自 forward 盈餘成長（forward EPS 63.40 隱含約 81% 成長）
- **內部人交易資料缺失**：insider 端點回傳空陣列，不應視為無交易
- **股利資料時序**：ex-dividend 日 2026-10-27 已早於 as-of 日期，發放與金額未驗證
- **資料來源**：live 抓取遭 Yahoo 403 封鎖，全部數據來自快取；ASML 原始財報為 EUR，本報告以工具回傳之 USD 計算，換算依據未知
- **Sector median 全部為估計值**，非資料源計算，判讀時請視為參考

FUNDAMENTALS REPORT COMPLETE
