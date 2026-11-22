# Fundamentals — AVGO as of 2026-11-23

## Executive summary
AVGO 財務體質強勁: 最新季 (FQ3 FY26, 期末 2026-07-31) 營收 29.59B USD 年增 +85.5%，GAAP 淨利率 44.2%，TTM 自由現金流 39.4B USD，淨負債/EBITDA 僅 0.68x。估值仍偏貴: trailing P/E 38.9x、EV/EBITDA 28.5x、P/FCF 約 36.9x，只有 forward P/E 15.7x 看起來便宜，而這取決於 forward EPS 19.39 能否兌現。股價 304.41 USD 在 2026-11-22 快取中單日下跌 10.1%，並跌破 50 日與 200 日均線，工具無法說明原因。

資料說明: 本報告以 `pipeline/tools/yf.py` 讀取 repo 快取 (source=cache, cached_at 2026-11-22T14:27:56Z)，屬預期情況。股價為快取價，未確認是否為 2026-11-23 收盤。所有金額單位為 USD，統一以 B (十億美元) 表示；本報告無 TWD / KRW 金額，故不使用 億。2026-11-23 之後的資料一律視為未知；唯一的未來日期為已排程的 2026-12-09 財報日，其結果未知。

## Revenue & profitability

**營收趨勢 (USD B, 財年 FY 截至 10 月底或 11 月初)**

| 期間 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利率 (GAAP) |
|---|---|---|---|---|---|
| FY22 | 33.20 | n/a | 66.5% | 43.0% | 34.6% |
| FY23 | 35.82 | +7.9% | 68.9% | 45.9% | 39.3% |
| FY24 | 51.57 | +44.0% | 63.0% | 29.1% | 11.4% |
| FY25 | 63.89 | +23.9% | 67.8% | 40.8% | 36.2% |

- 3 年營收 CAGR (FY22→FY25): **+24.4%**。yfinance 只提供 4 個年度欄位，無法計算 5 年 CAGR。
- FY24 淨利率僅 11.4%，主因 Q 層級的 Restructuring 及 Amortization 費用 (FY24 SG&A 4.96B，Amortization 3.24B，Special Income Charges 1.53B)，以及 FY24 稅費 3.75B。
- 季度 TTM 營收 89.10B，與 info 的 totalRevenue 89.10B 吻合。季度序列 (USD B): FQ3 FY25 15.95 → FQ4 FY25 18.02 → FQ1 FY26 19.31 → FQ2 FY26 22.19 → FQ3 FY26 29.59。FQ3 FY26 相對 FQ2 季增 +33.4%，為可計算的四個環比數據中最高的一季。
- 分部: 基本資料描述為 Semiconductor Solutions 與 Infrastructure Software 兩大部門。**部門營收與 AI 網路營收比重 DATA_UNAVAILABLE**，yfinance 未提供分部數字。

**獲利品質 (季度, FQ3 FY26 為最新)**

| 季度 | 毛利率 | 營業利益率 | GAAP 淨利率 | GAAP 稀釋 EPS |
|---|---|---|---|---|
| FQ3 FY25 (2025-07) | 67.1% | 38.1% | 26.0% | 0.85 |
| FQ4 FY25 (2025-10) | 68.0% | 42.5% | 47.3%* | 1.74 |
| FQ1 FY26 (2026-01) | 68.1% | 44.9% | 38.1% | 1.50 |
| FQ2 FY26 (2026-04) | 69.5% | 48.9% | 42.0% | 1.91 |
| FQ3 FY26 (2026-07) | 69.1% | 54.3% | 44.2% | 2.68 |

\* FQ4 FY25 稅務為 -1.649B 的利益，淨利被抬高，不應視為常態。

- 毛利率穩定在 68-70%，營業利益率從 38% 提升到 54%，營運槓桿明顯。
- 每季 Operating Expense 約 4.4B (FQ3 FY26: R&D 2.90B + SG&A 1.00B + 其他)，相對營收快速下降，顯示成長主要來自毛利增加而非費用擴張。
- ROE (info): **44.2%**。以 TTM NI 38.27B / 平均股東權益約 86.5B 核對，吻合。
- ROIC (本報告估算): TTM EBIT 43.24B，以 TTM 有效稅率 5.4% 算 NOPAT 約 40.9B，除以期末 invested capital 159.1B，約 **25.7%**。此為估算值，非工具直接提供。

**EPS 口徑差異 (重要)**
- GAAP 稀釋 EPS 與 earnings_dates 內的 Reported EPS 口徑不同。例如 FQ2 FY26 GAAP 為 1.91，但 earnings_dates 的 Reported EPS 為 2.44 (應為 non-GAAP)。
- trailing EPS 7.83 為 GAAP；forward EPS 19.39 口徑 yfinance 未說明，與 earnings_dates 的季度估值口徑可能不一致。

## Cashflow & balance sheet

**現金流 (TTM = FQ4 FY25 至 FQ3 FY26)**
- TTM OCF: **40.65B** (與 info operatingCashflow 40.65B 吻合)
- TTM Capex: **1.25B** (FY25 年度 0.62B，約 1.0% 營收；TTM 約 1.4%；FQ3 FY26 單季 0.53B，較 FQ3 FY25 的 0.14B 增加約 3.7 倍)
- TTM FCF (OCF − Capex): **39.40B**，FCF margin **44.2%** (最新季 46.2%)
- FCF / NI (TTM): **1.03x**，高於 0.9 健康門檻。FY25 年度 FCF/NI 為 1.16x。
- **資料不一致**: info.freeCashflow 為 30.60B，與季度加總的 39.40B 不同。本報告採季度加總值，但 downstream 若引用 info 的 FCF，P/FCF 會從 36.9x 變成 47.5x。
- SBC (TTM): **8.48B**，占營收 9.5%。扣除 SBC 後的 FCF 約 30.9B。

**資產負債表 (最新: 2026-07-31)**

| 項目 | 金額 (USD B) | 備註 |
|---|---|---|
| 現金及約當現金 | 23.98 | YoY +123.7% (FQ3 FY25 為 10.72) |
| 總負債 (Total Debt) | 59.42 | 自 FY24 67.57 → FY25 65.14 → 本季 59.42，持續去槓桿 |
| 淨負債 (Net Debt) | 35.44 | |
| 股東權益 | 99.69 | |
| 總資產 | 188.15 | |
| 商譽 | 97.80 | |
| 商譽 + 無形資產 | 124.13 | 占總資產 66.0% |
| 有形帳面價值 | -24.44 | 負值，資產以收購商譽為主 |
| 流動資產 / 流動負債 | 52.17 / 20.84 | Current ratio **2.50x** |
| 負債 / 股東權益 | 0.60x | info debtToEquity 59.6 (%) |

- 淨負債 / TTM EBITDA: **0.68x**；總負債 / TTM EBITDA: **1.14x**。
- EBITDA / 利息支出: TTM EBITDA 52.26B / TTM 利息 3.12B = **16.8x**，償債能力充足。
- 單季長期債償還: FQ3 FY26 償還 5.63B，FY25 年度償還 18.48B，去槓桿速度快。
- 應收帳款: FQ3 FY26 為 13.71B，YoY **+111%**，超過營收的 +85.5%。估算 DSO 約 42 天 (去年同期約 37 天)，需留意收款品質與客戶集中。
- 存貨: 4.52B，YoY +107.5%。

## Capital allocation & insider signal

**資本配置**
- 股利: 每季 3.10B 左右，TTM 股利總額 **12.08B**，每股年化 2.60 USD，殖利率 0.85%。
- 股利保障: TTM FCF / 股利 = **3.26x**；以 GAAP NI 計算的 payout 為 31.6% (info payoutRatio 32.4%)，保障足夠。
- 買回: FY25 年度 6.31B；TTM 買回 **8.45B**，但最新季 (FQ3 FY26) 為 **0**，FQ1 FY26 單季高達 7.85B，買回節奏不規則。
- 流通股數: 最新 4.774B，YoY 約 +1.1% (FQ3 FY25 為 4.722B)。TTM 買回 (8.45B) 與 SBC (8.48B) 大致相抵，但流通股數仍微幅增加。
- 併購: FY24 併購支出 25.98B (商譽增加因此形成，目前商譽 97.8B)；FY25 與 TTM 無併購現金流出。

**內部人交易 (最近 6 個月: 2026-05-23 至 2026-11-23)**
- yfinance insider 最後一筆資料為 **2026-07-10**，2026-07-10 之後至 2026-11-23 之間**無資料**，可能是 Form 4 資料缺口，DATA_UNAVAILABLE。
- 窗口內 11 筆: 公開市場賣出 7 筆，合計約 **283.7M USD**；公開市場買進 1 筆 (Director Harry You，2026-06-11，1,000 股，約 0.37M USD)；其他為 Stock Gift 與 Stock Award。
- 主要賣方: Henry Samueli (Director) 2026-06-24 賣出 654,241 股，約 **250.0M USD**；Mark Brazeal (CLO) 多次賣出，合計約 32.4M USD；Gayla Delly、Justine Page 各有小額賣出。
- 規模: 賣出約 283.7M USD，占市值 1,453.1B USD 約 **0.02%**，訊號強度低。內部人持股比例 1.96%。
- 淨交易: 賣出多於買進，方向偏賣，但多為大額執行與例行性 (Brazeal 固定 25,000 股) 交易，是否屬 10b5-1 計畫無法從工具確認。

## Valuation

**價格與市值 (快取價 304.41 USD)**
- 市值 (marketCap): **1,453.1B USD** (流通股 4.774B × 304.41 吻合)
- 企業價值 (EV): **1,488.6B USD** (市值 + 總負債 59.42 − 現金 23.98)
- 52 週區間: 289.77 – 495.00 USD；現價距 52 週低點 +5.1%，距高點 −38.5%
- 50 日均線 342.71 (現價低 11.2%)；200 日均線 367.82 (現價低 17.2%)
- Beta 1.508；空單占浮動股 1.11%

**估值倍數**

| 指標 | 數值 | 計算 |
|---|---|---|
| Trailing P/E | 38.9x | 304.41 / trailing EPS 7.83 (GAAP) |
| Forward P/E | 15.7x | 304.41 / forward EPS 19.39 |
| EV / EBITDA (TTM) | 28.5x | info enterpriseToEbitda 28.48 (EBITDA 52.26B) |
| EV / Revenue (TTM) | 16.7x | 1,488.6 / 89.10 |
| P / S (TTM) | 16.3x | 1,453.1 / 89.10 |
| P / FCF (TTM, 季度加總) | 36.9x | 1,453.1 / 39.40 |
| P / FCF (info.freeCashflow) | 47.5x | 1,453.1 / 30.60，口徑不同，僅供參考 |
| P / B | 14.6x | info priceToBook |
| PEG | 0.30 | info 值，earningsGrowth 215% 受 FY24 低基期影響，**不具參考性** |

**分析師共識 (47 位)**
- 推薦: strong_buy；目標價均值 526.47 USD，最高 660.00，最低 398.47。均值相對現價上行 +72.9%。
- 注意: 目標價時點與本次股價下跌的先後關係未知，工具未提供目標價日期。

**與產業中位數比較 (估計值，非工具數據)**
大型半導體股的一般區間估計: trailing P/E 約 30–35x，forward P/E 約 22–25x，EV/EBITDA 約 20–25x，P/FCF 約 30x，P/S 約 8–10x。AVGO 的 trailing 與 P/S 明顯高於估計中位數，forward P/E 則低於估計中位數，反映市場對其 EPS 快速成長的預期。

## Key catalysts

- **下一次財報: 2026-12-09** (FQ4 FY26，earnings_dates 時間戳 21:00 UTC，即美東 12-09 16:00 盤後)。共識 non-GAAP EPS 為 **3.83** (earnings_dates)。
- **FQ3 FY26 財報 (2026-09-02)**: earnings_dates 的 Reported EPS 為 null，共識估計為 3.24。**本季實際 non-GAAP EPS 未回填，DATA_UNAVAILABLE**，無法確認是否達標。
- **歷史財報表現**: earnings_dates 內 23 筆已報告季度的 EPS 全部高於共識，超額幅度多在 0.5%–6% 之間，平均約 2%。最近 4 季超額依序為 2025-09 的 1.60%、2025-12 的 4.38%、2026-03 的 1.32%、2026-06 的 1.74%。顯示穩定超預期的紀錄。
- **財測與指引: DATA_UNAVAILABLE**。yfinance 未提供管理層營收或 EPS 指引。
- **分部與 AI 營收: DATA_UNAVAILABLE**。
- **未解釋的股價 −10.1% 單日跌幅** (346.65 → 304.41，日內低點 301.02): 工具無法確認原因，建議 downstream 另查新聞或公告。

## Metrics table

金額單位: USD B (十億美元)；比率為 %、x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD B) | 89.10 | +85.5% (最新季) | n/a (估計值: 成長 15–25%) | 高速成長，優於產業 |
| 毛利率 (最新季) | 69.1% | 較 FQ3 FY25 +2.0 pt | 約 60–70% | 高檔穩定 |
| 營業利益率 (最新季) | 54.3% | +16.2 pt | 約 20–30% | 優異 |
| GAAP 淨利率 (TTM) | 42.9%* | n/a | 約 15–25% | 優異 (*TTM NI 38.27 / 營收 89.10 = 42.9%) |
| ROE (info) | 44.2% | n/a | 約 15–20% | 優異 |
| ROIC (估算) | 約 25.7% | n/a | 約 10–15% | 良好 |
| TTM OCF (USD B) | 40.65 | n/a | n/a | 充裕 |
| TTM FCF (USD B) | 39.40 | n/a | n/a | 充裕 |
| FCF margin (TTM) | 44.2% | n/a | 約 20–30% | 優異 |
| FCF / NI (TTM) | 1.03x | n/a | 約 0.8–1.0x | 健康 (>0.9) |
| 淨負債 (USD B) | 35.44 | 較 FY24 (58.18) 下降 | n/a | 改善中 |
| 淨負債 / EBITDA | 0.68x | n/a | 約 1–2x | 低 |
| Current ratio | 2.50x | n/a | 約 2.0x | 健康 |
| Debt / Equity | 0.60x | n/a | 約 0.3–0.5x | 偏高但可控 |
| 有形帳面價值 (USD B) | -24.44 | n/a | n/a | 負值，商譽依賴高 |
| Capex (TTM, USD B) | 1.25 | 單季 +3.7x | n/a | 輕資產，仍在增加 |
| 股利保障 (FCF / 股利) | 3.26x | n/a | n/a | 充足 |
| 買回 (TTM, USD B) | 8.45 | 最新季為 0 | n/a | 節奏不穩 |
| 流通股數 (B) | 4.774 | +1.1% | n/a | 微幅稀釋 |
| SBC (TTM, USD B) | 8.48 | 占營收 9.5% | n/a | 偏高 |
| 應收帳款 YoY | 13.71 | +111% | n/a | 高於營收成長，需追蹤 |
| Trailing P/E | 38.9x | n/a | 約 30–35x | 偏貴 |
| Forward P/E | 15.7x | n/a | 約 22–25x | 相對便宜 (依賴 EPS 兌現) |
| EV / EBITDA (TTM) | 28.5x | n/a | 約 20–25x | 偏貴 |
| P / FCF (TTM) | 36.9x | n/a | 約 30x | 偏貴 |
| P / S (TTM) | 16.3x | n/a | 約 8–10x | 明顯偏貴 |
| 內部人 6 個月淨賣出 (USD M) | 約 283.7 (賣) / 0.37 (買) | n/a | n/a | 占市值約 0.02%，訊號弱 |
| 分析師目標均值 (USD) | 526.47 | 相對現價 +72.9% | n/a | 共識偏多 |
| 股價 vs 200 日均線 | −17.2% | n/a | n/a | 弱勢 |

## Red flags

- **股價單日 −10.1% 並跌破 50/200 日均線**: 工具無法說明原因，屬高度未知事件。
- **估值偏貴**: trailing P/E 38.9x、EV/EBITDA 28.5x、P/S 16.3x 均高於估計的產業中位數，EPS 若未如預期成長，估值壓縮風險高。
- **有形帳面價值為負 (−24.4B)**: 資產大量來自收購商譽 (97.8B)，減損風險存在。
- **稅率異常低**: TTM 有效稅率約 5.4%，FQ4 FY25 出現 −1.65B 稅費利益，GAAP 淨利可能被低稅率抬高；若以 15% 稅率重算，TTM NI 約低 3.9B，trailing P/E 約升至 43x。
- **應收帳款成長快於營收**: YoY +111% vs 營收 +85.5%，DSO 由約 37 天升至約 42 天。
- **內部人大額賣出**: Samueli 2026-06 賣出約 250M USD；同期 Brazeal 固定賣出。金額占市值比例小，但方向偏賣。
- **SBC 占營收 9.5%，股數仍增加**: 扣除 SBC 後 FCF 約 30.9B；買回在最新季停止。
- **FQ3 FY26 實際 non-GAAP EPS 未回填**: 無法驗證最近一季是否達標。
- **FCF 口徑不一致**: info 30.60B vs 季度加總 39.40B，差異約 8.8B，下游引用需確認。
- **forward EPS 口徑未知**: 19.39 與季度 non-GAAP 估計 (2026-09 季 3.24、2026-12 季 3.83) 的加總口徑需確認，避免高估或低估前瞻 P/E。
- **資料缺口**: 內部人交易 2026-07-10 之後無資料；指引、分部營收、AI 營收 DATA_UNAVAILABLE；快取價格時點不明。

FUNDAMENTALS REPORT COMPLETE
