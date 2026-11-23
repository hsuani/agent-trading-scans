# HON 基本面分析 (Fundamentals)

- 標的: Honeywell International Inc. (HON), Industrials / Conglomerates, USD
- 分析日期: 2026-11-24
- 資料來源: `pipeline/tools/yf.py` 快取資料 (`source: cache`)。部分即時端點因網路封鎖無法取得 (cookie/crumb 失敗), 以快取為準。
- 價格基準: 221.81 (`currentPrice`), 市值 70.39B, EV 78.77B

## 1. 結論摘要

- **評級: 中性偏正面 (Neutral-to-Constructive)**。獲利面 (normalized) 穩定, 近 9 季 EPS 全數優於預期; 分析師共識 Buy, 平均目標價 253.87 (約 +14.5%)。
- **主要疑慮**: 營收成長趨緩 (最新季 YoY +1.3%), TTM 自由現金流偏薄 (約 1.5B), 股利覆蓋率不足 (以現金流計), 槓桿與利息負擔上升。
- **估值**: 以 forward P/E 22.5x 與 normalized trailing P/E 約 19.7x 看, 估值不算便宜; trailing P/E 11.0x 被 Q2 2026 的一次性處分利益 (約 5.9B) 扭曲, 不宜採用。
- **Quantinuum (約 54%)**: 屬少數但具上行選擇權的部位。快取資料未單獨揭露其公允價值, 本分析以 Honeywell 本體 (航太 / 建築科技 / 工業自動化) 為核心。

## 2. 營收與成長

| 期間 | 營收 (Revenue) | YoY |
|---|---|---|
| FY2023 | 33.01B | - |
| FY2024 | 34.72B | +5.2% |
| FY2025 | 37.44B | +7.8% |
| TTM (info) | 37.74B | 營收成長 `revenueGrowth` +1.3% |

- 年度序列 (FY2025 +7.8%) 與 info 的 `revenueGrowth` (+1.3%) 口徑不同, 後者應為最新季 YoY (2026-Q3: 4.99B vs 2025-Q3: 4.93B), 與季度資料一致。
- 季度營收序列在 2025-Q3 至 2026-Q3 之間出現明顯的不連續 (例如 2026-Q2 9.72B、2026-Q3 4.99B), 推測與組織調整 / 業務剝離的追溯重編有關 (例如 Solstice 分拆、航太分拆計畫), 但快取資料未證實, 需以原始 10-Q 核對。因此季度 QoQ 比較不具參考性, 僅適合看 YoY 與 normalized 指標。
- 此分析缺乏分部 (segment) 營收數據, 無法直接拆分航太 / 建築科技 / 工業自動化的成長貢獻。

## 3. 獲利能力與利潤率

| 指標 | FY2024 | FY2025 |
|---|---|---|
| Gross margin | 38.5% | 36.9% |
| Operating margin (GAAP) | 19.2% | 17.5% |
| EBITDA margin (reported) | 24.3% | 21.9% |
| Normalized EBITDA margin | 25.3% | 25.8% |
| Net margin (GAAP, 含非持續營運) | 16.4% | 12.6% |

- 毛利率與營業利益率 FY2025 皆較 FY2024 下滑, 但 normalized EBITDA margin 反而小幅提升, 表示 GAAP 下滑主要來自非經常性項目 (2025 Total Unusual Items 約 -1.4B; 其中資產減損約 0.99B、處分相關約 -0.45B)。
- Diluted EPS (GAAP): FY2024 17.42 -> FY2025 15.98 (-8.3%)。
- Normalized EPS (由 normalized income / diluted shares 推算): FY2024 約 15.94 -> FY2025 約 17.41 (+9.2%)。這是較能反映核心獲利的口徑。
- 最新季 (2026-Q3) 毛利率 40.4%, 營業利益率 14.8%; 2026-Q2 毛利率 37.6%, 營業利益率 18.4%; 季度利潤率波動大, 需留意處分與重組項目。
- 季度 Diluted EPS (GAAP) 2026-Q2 17.83 含 5.92B 處分利益, 不具代表性。

## 4. 現金流

- TTM Operating Cash Flow (2025-Q4 至 2026-Q3 加總): 約 1.95B。
- TTM Free Cash Flow (季度 FCF 加總): 約 1.52B; FCF yield 約 2.2% (1.52 / 70.39)。
- 2025-Q3 FCF 高達 3.33B, 2026-Q1 為 -0.87B, 季度波動極大, 單季不具參考性。
- 股利: `dividendRate` 2.80, 以此估算年度股利支出約 0.89B (2.80 x 約 317M 股)。若以 `Cash Dividends Paid` 季度序列加總 (約 2.58B TTM) 則覆蓋率明顯偏低, 兩者差異過大, 此為資料一致性問題 (見第 8 節)。
- 以 TTM FCF 1.52B 對照約 0.89B 股利, FCF 覆蓋率約 1.7x; 若採季度現金股利序列則覆蓋率僅約 0.6x。**股利安全性需以原始報表確認。**
- 2026 年 Q1 有 1.0B 買回股票, 其餘季度幾乎未買回 (買回意願偏低, 與資本支出 / 併購 / 去槓桿的資金需求一致)。
- 資本支出 (capex): 2025-Q3 約 0.51B, 2026-Q1 約 0.22B, 2026-Q2 約 0.32B; 資本密集度 (capex / revenue) 約 1% 左右 (以季度比例估算), 屬輕資本結構, 但需注意季度序列缺漏。

## 5. 資產負債表與槓桿

| 項目 | FY2024 | FY2025 |
|---|---|---|
| Total Assets | 75.20B | 73.68B |
| Total Debt | 32.08B | 35.56B |
| Cash & ST Investments | 10.29B | 12.93B |
| Net Debt | 21.13B | 22.09B |
| Stockholders' Equity | 18.62B | 13.90B |
| Goodwill + Intangibles | 27.64B | 27.82B |
| Current Ratio | 1.31 | 1.30 |

- 淨負債 FY2025 22.09B; 淨負債 / normalized EBITDA 約 2.3x (以 9.64B 計); 淨負債 / reported EBITDA 約 2.7x。
- 總負債 / 股東權益 (FY2025) 約 2.56x; 權益大幅下降 (-25%), 原因未於快取資料中揭露 (可能與分拆、減損、退休金或其他權益調整有關, 需查證)。
- 利息支出快速上升: FY2022 0.41B -> FY2023 0.75B -> FY2024 1.05B -> FY2025 1.34B。EBIT / interest 由 FY2022 約 16.4x 降至 FY2025 約 5.1x, 利息保障倍數顯著下滑, 是需要持續追蹤的風險點。
- Goodwill + intangibles 約 27.8B, 占總資產約 38%, 若有減損風險會直接影響權益。
- 快取 `info` 的 Total Debt 為 17.24B, 與年度資產負債表 35.56B 差距極大 (見第 8 節), 上述槓桿指標以年度資產負債表為準, `info` 的 debtToEquity (76.1) 不採用。

## 6. 內部人與機構持股

- 內部人持股 `heldPercentInsiders`: 0.058%, 持股比例極低, 利益一致性的訊號有限。
- 機構持股 `heldPercentInstitutions`: 82.3%, 機構持有人數 2,847。
- 內部人交易 (近 114 筆紀錄):
  - 快取資料的 `Transaction` 欄位全為空白, 無法分類為公開市場買入 / 賣出或 RSU 歸屬 / 稅款扣繳。
  - 較大筆者包括 2026-07-27 West Kenneth J 17,032 股 (約 3.3M 至 4.2M USD 不等的紀錄), 2026-10-26 Kapur Vimal M (CEO) 兩筆合計約 15,143 股, Lu Su Ping (GC) 兩筆合計約 6,976 股。
  - 部分紀錄的隱含每股價格與當時股價不符 (例如 2026-10-26 約 114 USD/股 vs 現價 221.81), 資料可信度存疑。
  - **結論: 無法確認淨買賣方向, 內部人交易訊號不作為主要依據。**
- 2026-07 前後有多位高管 (CEO、CFO、GC、Officer) 的小額紀錄, 多為定期歸屬 / 扣繳性質的可能性較高, 但未經證實。

## 7. 估值

| 指標 | 數值 | 說明 |
|---|---|---|
| Price | 221.81 | 52 週區間 196.16 - 260.28; 位於區間約 40% 位置 |
| Market Cap | 70.39B | 股本約 317.4M 股 |
| Enterprise Value | 78.77B | |
| Trailing P/E (info) | 11.0x | 受 Q2 2026 約 5.9B 處分利益扭曲, 不採用 |
| Normalized trailing P/E (推算) | 約 19.7x | normalized income TTM 約 3.59B / 約 319M 稀釋股數, EPS 約 11.2 |
| Forward P/E | 22.5x | forward EPS 9.88 |
| EV / EBITDA (info TTM) | 8.7x | EBITDA TTM 9.02B |
| EV / EBITDA (normalized 推算) | 約 11.6x | normalized EBITDA TTM 約 6.78B; 與上一列差異大, 見第 8 節 |
| P / B | 3.14x | |
| P / S (TTM) | 1.87x | |
| FCF yield (TTM) | 約 2.2% | 以季度 FCF 加總 1.52B 計 |
| Dividend yield | 約 1.3% | dividendRate 2.80 |
| 分析師目標價 (mean) | 253.87 | 範圍 186 - 290; 共 23 位分析師; 推薦 `buy` |

- 股價相對 200 日均線 (229.82) 仍偏低, 略高於 50 日均線 (214.90)。
- 盈餘公告紀錄: 近 9 季 EPS 全數優於預期, 平均超預期幅度約 6% (最近一季 2026-Q3: 實際 2.27 vs 預估 2.16, +4.9%)。下次財報估計日 2027-01-28, 預估 EPS 2.45。
- 估值判斷: 以 forward P/E 22.5x 與 normalized P/E 約 19.7x 計, 相對工業複合體的歷史水準偏高, 上行空間主要依賴盈餘成長兌現與分拆 / 組織重整後的重新估值, 而非目前的現金流規模。

## 8. Quantinuum 曝險與資料品質

**Quantinuum (約 54% 持股)**
- 屬於 Honeywell 的少數部位, 對整體營收貢獻有限, 但具有上行選擇權。
- 2026-Q2 出現約 5.92B 的 Gain On Sale of Business, 快取資料未說明其來源; 若與 Quantinuum 相關, 可能代表估值重估或交易事件, 需查證公告。
- 快取資料中無 Quantinuum 的獨立財務數據或公允價值, 無法量化其在 SOTP 中的價值, 本分析不做具體估值。

**資料品質 (重要)**
1. `info` 的 `freeCashflow` (7.02B) 與 `operatingCashflow` (1.95B) 不一致 (FCF 不可能大於 OCF, 除非 capex 為負); 本分析採用季度 FCF 加總 (約 1.52B)。
2. `info` 的 `totalDebt` (17.24B) 與年度資產負債表的 Total Debt (35.56B) 差距過大, 需以原始報表為準。
3. `info` 的 `currentRatio` (0.96) 與年度資產負債表算出的 1.30 不一致。
4. 季度序列 (2025-Q3 至 2026-Q3) 的營收、EPS 出現不連續, 可能是追溯重編、分拆調整或混用不同口徑所致。
5. 季度 `Cash Dividends Paid` 與 `dividendRate` 推算的股利支出差距約 3 倍, 無法確定。
6. 季度 Diluted EPS (GAAP) 加總 (約 23.4) 與 `trailingEps` (20.17) 不一致。
7. 內部人交易紀錄無交易代碼, 部分隱含價格不合理。
8. 無分部 (segment) 資料, 無法分析航太 / 建築科技 / 工業自動化各自的成長與利潤率。
9. `info` 的 `earningsGrowth` (-63.6%) 受 2025 vs 2026 處分利益基數影響, 不宜作為核心成長指標。

建議: 下一步以原始 10-K / 10-Q 與 8-K 核對 (1) 分拆與重編後的分部數據, (2) 2026 年股東權益大幅變動原因, (3) 股利支付與 FCF 覆蓋率, (4) 2026-Q2 處分利益的交易性質與 Quantinuum 相關性。

## 9. 指標表 (Metrics Table)

| 指標 (Metric) | 數值 (Value) | 備註 |
|---|---|---|
| Price | 221.81 USD | 52W 196.16 - 260.28 |
| Market Cap | 70.39B | |
| Enterprise Value | 78.77B | |
| Revenue FY2025 | 37.44B | YoY +7.8% |
| Revenue growth (latest qtr, YoY) | +1.3% | `revenueGrowth` |
| Gross Margin FY2025 | 36.9% | FY2024 38.5% |
| Operating Margin FY2025 (GAAP) | 17.5% | FY2024 19.2% |
| Normalized EBITDA Margin FY2025 | 25.8% | FY2024 25.3% |
| Net Margin FY2025 (GAAP) | 12.6% | |
| Diluted EPS FY2025 (GAAP) | 15.98 | FY2024 17.42 |
| Normalized EPS FY2025 (推算) | 約 17.41 | FY2024 約 15.94 (+9.2%) |
| TTM Operating Cash Flow | 1.95B | |
| TTM Free Cash Flow | 1.52B | 季度加總; info 數值 7.02B 不一致 |
| FCF yield (TTM) | 約 2.2% | |
| Dividend rate / yield | 2.80 / 約 1.3% | |
| Dividend coverage (FCF / est. dividends) | 約 1.7x | 季度現金股利序列推算約 0.6x, 需查證 |
| Total Debt FY2025 | 35.56B | info 17.24B, 不一致 |
| Net Debt FY2025 | 22.09B | |
| Net Debt / Normalized EBITDA | 約 2.3x | |
| Debt / Equity (FY2025) | 約 2.56x | 權益 13.90B |
| Current Ratio FY2025 | 1.30 | info 0.96, 不一致 |
| EBIT / Interest FY2025 | 約 5.1x | FY2022 約 16.4x, 持續下滑 |
| Goodwill + Intangibles | 27.82B | 約占總資產 38% |
| Trailing P/E (info) | 11.0x | 受處分利益扭曲 |
| Normalized Trailing P/E (推算) | 約 19.7x | |
| Forward P/E | 22.5x | forward EPS 9.88 |
| EV / EBITDA (info TTM) | 8.7x | |
| EV / EBITDA (normalized 推算) | 約 11.6x | |
| P / B | 3.14x | |
| P / S (TTM) | 1.87x | |
| Analyst Target Mean | 253.87 | 約 +14.5%; 範圍 186 - 290; 23 位 |
| Recommendation | Buy | |
| Last EPS Surprise (2026-Q3) | +4.9% | 近 9 季皆超預期 |
| Next Earnings Date | 2027-01-28 | 預估 EPS 2.45 |
| Insider Ownership | 0.058% | 內部人交易方向無法確認 |
| Institutional Ownership | 82.3% | 2,847 家 |
| Beta | 0.88 | |
| 綜合評級 | 中性偏正面 | 獲利穩定與共識目標價支撐, 但現金流 / 槓桿 / 估值為主要限制 |
