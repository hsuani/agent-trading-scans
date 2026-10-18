# Fundamentals — ARM as of 2026-10-19

資料說明：價格來自 repo 快取（cnyes feed，`regularMarketTime` 推算為 2026-10-16 週五收盤），2026-10-19 為週一，尚未有新交易資料。財報期間以 ARM 會計年度（FY 結束於 3/31）計算：FY26 = 2026-03-31，TTM = 截至 2026-06-30 的四季合計。未來事件（2026-11-04 財報）僅列為排程，未發生。財務數據與 yfinance 欄位有部分不一致，已於 Red flags 標註。

## Executive summary
ARM 財務體質佳：現金與短期投資 3,888M USD、總債務 464M USD，淨現金約 3.4B USD，current ratio 5.25，TTM FCF 約 1.47B USD，營收仍維持約 23% 年增率。但獲利能力自 FY23 高點持續壓縮（營業利益率 25.3% 降至 FY26 的 18.5%，2026-06 季降至 7.6%），且 SBC 佔營收約 22%，FCF 品質需打折看待。估值極度昂貴：trailing P/E 234.8x、forward P/E 74.4x、EV/EBITDA 225.5x、P/S 47.2x；分析師平均目標價 290.71 USD 高於現價約 28%，但過去 6 個月 16 筆公開市場賣出（約 62.4M USD）、零筆公開市場買進。

## Revenue & profitability

**營收與成長**
- 年度營收（USD）：FY23 2,679M → FY24 3,233M → FY25 4,007M → FY26 4,920M。
- YoY：FY24 +20.7%、FY25 +23.9%、FY26 +22.8%。
- 3 年 CAGR（FY23→FY26）約 22.4%；2 年 CAGR（FY24→FY26）約 23.4%。
- TTM 營收 5,156M（yfinance totalRevenue 5,155,999,744），2026-06 季 1,289M，YoY +22.4%（2025-06 季 1,053M）。
- 分部營收：yfinance 無分部資料。`longBusinessSummary` 提及產品線包括 CPU IP、GPU/NPU、systems IP、compute subsystems（CSS）與軟體工具，但無分部營收數字，分部占比為 DATA_UNAVAILABLE。

**利潤率趨勢**

| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY23 | 96.0% | 25.3% | 19.6% |
| FY24 | 95.2% | 3.6% | 9.5% |
| FY25 | 97.0% | 20.7% | 19.8% |
| FY26 | 97.5% | 18.5% | 18.4% |
| TTM (至 2026-06) | 97.5% | 17.3% | 20.2% |
| 2026-06 季 | 97.2% | 7.6% | 21.0% |

- 毛利率極高（IP 授權模式），接近 97%，為結構性優勢。
- 營業利益率 FY23 → FY26 下滑約 6.8 個百分點；FY24 低點與 FY24 營業利益 117M 有關（FY24 OpEx 2,962M 大幅高於營收成長），資料未揭露原因。
- 2026-06 季營業利益僅 98M，營業利益率 7.6%。同季 unusual items 合計 121M，性質資料未揭露。
- 費用結構：R&D FY26 2,776M（占營收 56.4%），FY25 2,071M（占 51.7%），YoY +34%。SG&A FY26 1,115M，YoY +13%。2026-06 季 R&D 838M，YoY +28.9%，營收 YoY 僅 +22.4%，呈現負經營槓桿。
- EPS：FY26 稀釋 EPS 0.85（FY25 0.61，+39%）。TTM 稀釋 EPS 0.97（yfinance trailingEps 0.97）。

**ROE / ROIC**
- ROE：yfinance returnOnEquity 13.4%；以 TTM 淨利 1,044M / 2026-06 股東權益 8,630M 計算約 12.1%。
- ROIC（估計）：TTM 營業利益 892M × (1 − 約 22% 稅率) ≈ 696M，除以平均投入資本約 8,458M（8,286M 與 8,630M 平均），約 8%。此為粗估，非 yfinance 原始欄位。

## Cashflow & balance sheet

**現金流品質（以 OCF − Capex 定義 FCF）**

| 期間 | OCF | Capex | FCF | FCF margin | FCF/NI | SBC |
|---|---|---|---|---|---|---|
| FY23 | 739M | 93M | 646M | 24.1% | 1.23 | 79M |
| FY24 | 1,090M | 143M | 947M | 29.3% | 3.09 | 1,037M |
| FY25 | 397M | 239M | 158M | 3.9% | 0.20 | 820M |
| FY26 | 1,524M | 575M | 949M | 19.3% | 1.05 | 1,052M (21.4%) |
| TTM (至 2026-06) | 2,094M | 622M | 1,472M | 28.6% | 1.41 | 1,154M (22.4%) |

- TTM FCF/NI 1.41，高於 0.9 健康門檻；但 FY25 僅 0.20，FCF 逐年波動大。
- SBC 佔營收 21–22%，TTM SBC 約與 TTM 淨利相當。扣除 SBC 後的 TTM FCF 約 318M，FCF margin 約 6%。這是本報告最重要的品質警示。
- Capex 加速：FY26 575M（占營收 11.7%），FY25 為 239M（6.0%），2026-06 季 208M。
- yfinance `freeCashflow` 欄位為 1,334.5M，與上表以季度 OCF − Capex 加總的 1,472M 不一致，兩者定義差異未揭露，本報告以財報逐項計算值為準。

**資產負債表（2026-06-30）**
- 現金及短期投資 3,888M；現金及約當現金 3,058M；總債務 464M；淨現金約 3,424M（約占市值 1.4%）。
- Current ratio 5.25（流動資產 6,339M / 流動負債 1,207M）；quick ratio 5.06。
- 股東權益 8,630M；Debt/Equity 約 5.4%（以 464M / 8,630M 計算）。yfinance `debtToEquity` 為 5.62，推測為百分比單位，與計算值吻合。
- 總資產 11,196M；商譽 1,623M（2026-03 數據），有形帳面價值 6,790M。
- 營運資金 5,132M。
- 財務槓桿極低，償債能力無疑慮。

## Capital allocation & insider signal

**資本配置**
- 股利：無（yfinance dividendYield 0.0，現金流量表無股利支付資料）。
- 買回：現金流量表無 repurchase 資料，視為無顯著回購。
- 股本稀釋：流通股數由 2025-06 的 1,059.3M 增至 2026-06 的 1,068.0M，YoY 約 +0.8%，主要來自 SBC 發行。
- Capex 與研發為主要資金用途；現金累積速度快（現金及短期投資由 FY25 的 2,825M 增至 2026-06 的 3,888M）。

**內部人交易（近 6 個月：2026-04-19 至 2026-10-19）**
- 公開市場賣出：16 筆，合計約 62.4M USD，涉及 6 位內部人。
  - CFO Jason Child：約 16.8M（2026-04-22、05-15/05-20、08-27、09-21，其中 8-27 與 9-21 各 10,400 股，形式上可能為預定交易計畫，但資料未確認）。
  - Spencer Collins（EVP 兼 Chief Legal Officer，資料列為 Officer）：約 19.8M（2026-05-11、05-19）。
  - William Abbey（EVP 兼 Chief Commercial Officer，資料列為 Officer）：約 12.0M（05-15 至 06-01 多筆）。
  - Laura Bartels（Officer）：約 4.4M（2026-06-02，392.70 USD）。
  - Charlotte Eaton（Officer）：約 4.2M（2026-05-21）。
  - Richard Grisenthwaite（Officer）：約 5.1M（2026-05-18）。
- 公開市場買進：0 筆。
- CEO Rene Haas 最近一筆公開市場賣出為 2026-04-14（超出 6 個月窗口，不計入），窗口內僅有 64 股的小額 grant（2026-08-31）與 2026-05-15 大額 grant（265,643 股，Value 0，非市場交易）。
- 規模：62.4M / 市值 243.3B ≈ 0.026%，占市值比例極小，但方向全為賣出、無買進。
- 賣出時點多落在 2026-05 財報後窗口（股價 200–290 區間）以及 2026-06 股價 380–415 高點，目前股價 227.8 已較 9-21 的 300 USD 賣出價低約 24%。

**股東結構**
- 機構持股 96.25%（1,311 家），內部人持股 0.07%。
- 前十大機構（2026-06-30）：Invesco 1.20%、DZ Bank 0.61%、Capital World 0.41%、Arrowstreet 0.38%、FMR 0.38% 等，無單一機構超過 2%。
- 流通股（float）僅 142.6M 股，占流通股本 1,068.0M 的約 13%。yfinance 與 `longBusinessSummary` 均指出 ARM 為 SoftBank Group 子公司，但母公司持股比例為 DATA_UNAVAILABLE。
- 空單：16.19M 股，占 float 11.15%，days-to-cover 2.93，較上月 16.74M 下降約 3.3%。

## Valuation

**估值倍數（以 2026-10-16 收盤 227.80 USD 計算）**
- 市值 243.29B USD（yfinance marketCap，與 227.8 × 1,068.0M 股吻合）；企業價值 EV 239.89B USD。
- Trailing P/E：234.8x（227.8 / TTM EPS 0.97）。
- Forward P/E：74.4x（yfinance forwardPE，基礎為 forwardEps 3.06276）。注意：epsCurrentYear 為 2.228，以其計算的 P/E 約 102.2x。兩個 forward EPS 的來源與期間不一致，forward P/E 基礎為 DATA_UNAVAILABLE（yfinance 未標明期間）。
- EV/EBITDA（TTM）：225.5x（EBITDA TTM 1,063.7M）。
- EV/Revenue（TTM）：46.5x。
- P/S（TTM）：47.2x。
- P/FCF（TTM，OCF − Capex 1,472M）：約 165x；以 yfinance freeCashflow 1,334.5M 計算約 182x。
- P/B：28.2x（bookValue/share 8.08）。
- PEG：yfinance pegRatio 1.87（trailing 2.73）。
- 估值含義：要支撐 forward P/E 74x，EPS 需由 TTM 0.97 成長至 FY27 consensus 2.23（+130%）。EPS 成長預期是估值的核心前提。

**同業比較（估計）**
- 以大型半導體公司粗估：forward P/E 中位數約 30x、EV/EBITDA 約 25–30x、P/S 約 10–12x、ROE 約 15–20%、毛利率約 60%。此為估計值，非來自工具。
- ARM 以 IP 授權為主，毛利率與 ROE 結構與晶片商不同，直接比較僅供參考。

**分析師共識（40 位分析師）**
- 評級分布：Strong Buy 8、Buy 21、Hold 12、Sell 1、Strong Sell 1；recommendationMean 1.91（buy）。
- 目標價：平均 290.71（+27.6%）、中位數 278.6（+22.3%）、最高 500（+119.5%）、最低 125（-45.1%）。
- 近 3 個月評級結構穩定，Strong Buy + Buy 由 27 家（-3m）增至 29 家（0m），無顯著下調趨勢。

**價格與技術背景（僅供估值脈絡）**
- 現價 227.80，前收 244.79，當日 -6.94%。
- 52 週區間 100.02–452.70；距 52 週高點 -49.7%，距低點 +127.8%。
- 50 日均線 267.88（現價在下方，約 -15%）；200 日均線 223.44（現價在上方，約 +2%）。
- Beta 3.79。

## Key catalysts
- 下次財報：2026-11-04（yfinance earnings_dates，排程，尚未發生）。FQ2 FY27（2026-09 季）consensus EPS 0.47。
- 近 4 季 EPS 超預期幅度：Nov-25 +17.7%、Feb-26 +5.1%、May-26 +3.6%、Jul-26 +11.4%。近 13 季共 12 次超預期、1 次持平（Jul-25，-0.31%）。
- 注意：earnings_dates 的 EPS（如 Jul-26 實際 0.45）為調整後口徑，與季度 GAAP 稀釋 EPS（Jun-26 季 0.25）不同，比較時須統一口徑。
- 公司指引（guidance）：DATA_UNAVAILABLE，工具未提供管理層未來季度或全年指引。
- 分部轉變：營收結構由純 IP 授權朝 CSS、NPU/GPU 等較完整產品線擴張（依 longBusinessSummary 描述）。對毛利率與研發投入的影響，數據面無法量化。
- SoftBank 持股變動、鎖定期或出售計畫：DATA_UNAVAILABLE。
- 內部人持續賣出（CFO 與多位 Officer）是窗口內可觀察的事件風險。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM，USD） | 5,156M | +22.4%（2026-06 季） | 約 10–15% | 高成長，優於同業估計 |
| 營收 CAGR（FY23–FY26） | 22.4% | — | 約 10–12% | 高成長 |
| 毛利率（TTM） | 97.5% | FY25 97.0% → FY26 97.5% | 約 60% | 極優（IP 授權模式） |
| 營業利益率（TTM） | 17.3% | FY25 20.7% → FY26 18.5% | 約 15–20% | 中性，趨勢走弱 |
| 營業利益率（2026-06 季） | 7.6% | 2025-06 季 10.8% | — | 警示，單季惡化 |
| 淨利率（TTM） | 20.2% | FY25 19.8% → FY26 18.4% | 約 12–15% | 良好 |
| ROE | 13.4%（yfinance） | — | 約 15–20% | 中性偏弱 |
| ROIC（估計） | 約 8% | — | 約 10–12% | 偏弱 |
| R&D / 營收（FY26） | 56.4% | FY25 51.7%（+4.7pp） | 約 15–25% | 警示，研發強度高 |
| FCF（TTM，OCF − Capex） | 1,472M | FY25 158M → FY26 949M | — | 改善，但波動大 |
| FCF margin（TTM） | 28.6% | FY26 19.3%（FY25 3.9%） | 約 20–25% | 良好 |
| FCF / NI（TTM） | 1.41 | FY26 1.05 | > 0.9 健康門檻 | 健康 |
| FCF − SBC margin（TTM） | 約 6% | — | — | 警示 |
| SBC / 營收（TTM） | 22.4% | FY25 20.5% → FY26 21.4% | 約 5–10% | 警示，稀釋成本高 |
| Capex / 營收（FY26） | 11.7% | FY25 6.0% | 約 5–8% | 上升中 |
| Current ratio | 5.25 | — | 約 1.5–2.5 | 優 |
| Debt / Equity | 約 5.4% | — | 約 30% | 優 |
| 淨現金（2026-06） | 約 3.42B | 現金 YoY +34%（2025-06 2,906M → 3,888M） | — | 優 |
| 流通股數 YoY | 1,068.0M | +0.8% | — | 稀釋低 |
| 股利 / 回購 | 無 | — | — | 中性（成長型） |
| 內部人淨買賣（6 個月） | 淨賣出約 62.4M，買進 0 筆 | — | — | 警示 |
| Trailing P/E | 234.8x | — | 約 30–40x | 極度昂貴 |
| Forward P/E | 74.4x（EPS 3.06）/ 102.2x（FY27 EPS 2.23） | — | 約 30x | 極度昂貴 |
| EV/EBITDA（TTM） | 225.5x | — | 約 25–30x | 極度昂貴 |
| P/S（TTM） | 47.2x | — | 約 10–12x | 極度昂貴 |
| P/FCF（TTM） | 約 165x | — | 約 30x | 極度昂貴 |
| PEG（yfinance） | 1.87 | — | 約 1.5–2 | 中性，依賴 EPS 成長兌現 |
| 分析師平均目標價 | 290.71（+27.6%） | — | — | 偏多 |
| 分析師評級均值 | 1.91（buy） | — | — | 偏多 |
| Beta | 3.79 | — | 約 1.2–1.5 | 高波動 |
| 空單佔 float | 11.15% | 月變化 -3.3% | 約 3–5% | 偏高 |
| 機構持股 | 96.25% | — | 約 70–80% | 高 |

## Red flags
- 估值極端：trailing P/E 235x、EV/EBITDA 225x、P/S 47x。獲利必須大幅成長才能支撐現價，任何 EPS 低於預期都會放大回檔風險。
- SBC 佔營收約 22%，與 TTM 淨利相當。扣除 SBC 後 FCF margin 只剩約 6%，真實股東獲利品質弱於表面 FCF 數字。
- 營業利益率由 FY23 的 25.3% 降至 FY26 的 18.5%，2026-06 季單季降至 7.6%；R&D 年增 34% 遠快於營收的 23%，經營槓桿為負。
- 2026-06 季 unusual items 121M，性質未揭露，需要財報附註確認是否為一次性項目。
- Capex 於 FY26 增至 575M（FY25 為 239M），FCF 歷史上 FY25 僅 158M，現金流穩定性不足。
- 6 個月 62.4M 公開市場賣出、零買進，且 CFO 多次出售。
- 股價距 52 週高點 -49.7%，低於 50 日均線約 15%，Beta 3.79，空單佔 float 11%，波動與籌碼壓力並存。
- Float 僅約 13%（142.6M / 1,068.0M），流動性與母公司 SoftBank 持股相關的供給風險需關注（母公司持股比例 DATA_UNAVAILABLE）。
- 資料一致性問題：
  - yfinance freeCashflow（1,334.5M）與季度 OCF − Capex 加總（1,472M）不同。
  - yfinance operatingMargins 7.6% 實為 2026-06 單季值，非 TTM（TTM 為 17.3%）。
  - yfinance debtToEquity 5.62 應為百分比單位。
  - yfinance nonDilutedMarketCap 355B 與現價及股本（市值 243B）不一致，本報告未採用。
  - forwardPE 與 epsCurrentYear 的 EPS 基準不同，forward P/E 基準期間未明。
  - earnings_dates 的 EPS 與季度 GAAP EPS 口徑不同。
- 上述資料缺口：公司指引、分部營收、SoftBank 持股比例、同業估值中位數（僅為估計值）。

FUNDAMENTALS REPORT COMPLETE
