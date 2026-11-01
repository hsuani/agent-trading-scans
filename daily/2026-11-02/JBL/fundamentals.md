# Fundamentals — JBL as of 2026-11-02

資料基準: 工具快取報價 2026-11-01 (cached_at 13:10 UTC)，財報期間至 FY2026 (截至 2026-08-31)。未出現 2026-11-02 之後的資料。單位: USD，以 B (十億) / M (百萬) 標示。FY 結束於 8 月底。

## Executive summary
Jabil (JBL) 為大型 EMS (電子製造服務) 公司，FY2026 營收 35.95B USD (YoY +20.6%)、GAAP 淨利 1.04B USD (YoY +58.6%)、自由現金流 1.37B USD，獲利與現金流明顯改善；但毛利率僅 9.2%、營業利益率 5.1%，且 FY2026 併購與營運資金擴張 (主要靠應付帳款增加 7.98B USD) 使資產負債表大幅膨脹，流動比率 0.99x、有形淨值為負 (-0.215B USD)，財務體質判定為「獲利改善，但槓桿與營運資金依賴度高」。估值上 GAAP trailing P/E 28.0x 偏高，但以 forward EPS 22.17 計 forward P/E 僅 12.3x、EV/EBITDA 12.2x；股價自 52 週高點 428.93 下跌 36%，且低於 50 日與 200 日均線。分析師共識為 strong buy (平均目標價 425 USD)，內部人於 2026 年 1 至 4 月有約 33M USD 的公開市場賣出，近六個月則為小額、接近中性。

## Revenue & profitability

**營收 (USD B)**: FY2023 34.70 → FY2024 28.88 → FY2025 29.80 → FY2026 35.95。
- FY2026 YoY +20.6%；FY2025 YoY +3.2%；FY2024 YoY -16.8%。
- 3 年 CAGR (FY2023 至 FY2026): 約 +1.2%；2 年 CAGR (FY2024 至 FY2026): 約 +11.6%。FY2022 欄位為 null，無法計算 5 年 CAGR。
- Q4 FY2026 營收 10.616B USD，YoY +28.6% (vs 8.252B)，為近期加速最明顯的一季。
- 分部 (segment) 營收: info.longBusinessSummary 列出三大分部 (Regulated Industries、Intelligent Infrastructure、Connected Living and Digital Commerce)，但工具未提供分部營收數字，**分部占比: n/a**。

**獲利能力**

| 年度 | 毛利率 | 營業利益率 | 淨利率 | 稀釋 EPS (GAAP) |
|---|---|---|---|---|
| FY2023 | 8.3% | 4.6% | 2.4% | 6.02 |
| FY2024 | 9.3% | 5.0% | 4.8% (含 942M 出售事業收益) | 11.17 |
| FY2025 | 8.9% | 4.8% | 2.2% | 5.92 |
| FY2026 | 9.2% | 5.1% | 2.9% | 9.75 |

- 營業利益 (Operating Income, yfinance): FY2026 1.836B USD (YoY +27.8%)。Total Operating Income As Reported 為 1.704B USD，兩者口徑不同，此處採前者。info.operatingMargins 為 5.8%，與自算 5.1% 有差異，以自算為準。
- 淨利 FY2026 1.042B USD；Q4 FY2026 淨利 0.398B USD (YoY +82.6%)。
- Q4 FY2026 毛利率 9.4%、營業利益率 5.9%，與 Q4 FY2025 (9.5%、5.8%) 相比毛利率持平、營益率微升，獲利增長主要來自營收規模。
- **ROE**: info.returnOnEquity 66.4%。此數字受權益極小影響 (股東權益僅 1.613B USD，因庫藏股累計 9.02B USD)，**不具參考價值**，僅作為財務槓桿與回購的副產物看待。ROA 4.98%。
- **ROIC (自算)**: NOPAT = 營業利益 1.836B × (1 - 稅率 26.1%) ≈ 1.36B USD；平均投入資本 (4.398B + 4.992B) / 2 = 4.70B USD；ROIC ≈ 28.9%。若以 yfinance EBIT 1.589B 計算則約 25.0%。ROIC 高於一般資本成本，但主要因投入資本輕，且應付帳款支撐。

**調整後 EPS 與 GAAP EPS 口徑差異**: earnings_dates 表列之 Reported EPS 為公司調整後 (non-GAAP) EPS。FY2026 四季調整後 EPS 合計約 13.10 USD (2.85 + 2.69 + 3.16 + 4.40，為自算)，與 GAAP 稀釋 EPS 9.75 USD 相差約 34%，主要為重組、減損等特殊項目。

## Cashflow & balance sheet

**現金流 (USD B)**

| 指標 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| 營運現金流 OCF | 1.734 | 1.716 | 1.640 | 2.002 |
| 資本支出 CapEx | 1.030 | 0.784 | 0.468 | 0.628 |
| 自由現金流 FCF | 0.704 | 0.932 | 1.172 | 1.374 |
| FCF 利潤率 | 2.0% | 3.2% | 3.9% | 3.8% |
| FCF / 淨利 | 0.86x | 0.67x | 1.78x | 1.32x |

- FY2026 FCF YoY +17.2%；OCF YoY +22.1%。
- **FCF 品質警示**: FCF / 淨利 1.32x 雖高於 0.9 門檻，但 FY2026 營運現金流的主要來源是應付帳款增加 7.98B USD (FY2025 為 1.43B)；同年存貨 -2.68B、應收帳款 -2.62B、預付款 -2.54B 部分抵消。若剔除應付帳款變動，OCF 理論上為負。此類現金流依賴供應商付款條件，可逆性高。
- Q4 FY2026 FCF 0.487B USD、Q3 0.351B、Q2 0.308B、Q1 0.228B，逐季改善。

**資產負債表 (FY2026 年末，2026-08-31, USD B)**

| 項目 | FY2026 | FY2025 | 變化 |
|---|---|---|---|
| 現金及約當現金 | 1.739 | 1.933 | -10% |
| 總負債 (yf Total Debt) | 4.020 | 3.366 | +19% |
| 淨負債 (yf Net Debt) | 1.640 | 0.952 | +72% |
| 淨負債 (info totalDebt 減 totalCash) | 2.600 | n/a | 口徑見下 |
| 股東權益 | 1.613 | 1.513 | +7% |
| 商譽 + 無形資產 | 1.828 | 1.114 | +64% |
| 有形淨值 (Tangible Book) | -0.215 | 0.399 | 轉負 |
| 流動資產 | 21.520 | 13.720 | +57% |
| 流動負債 | 21.673 | 13.714 | +58% |
| 應付帳款 | 14.444 | 7.937 | +82% |
| 總資產 | 27.435 | 18.543 | +48% |

- **流動比率**: 0.99x (FY2025 為 1.00x)；速動比率 0.44x。營運資金 -0.153B USD。
- **負債權益比**: yfinance 口徑 2.49x (4.020 / 1.613)；info 口徑 268% (總債務 4.339B，含租賃等)。
- **淨負債 / EBITDA**: yf 口徑 0.72x (1.640 / 2.270)；以 info 口徑淨負債 2.600B 除以 info EBITDA 2.513B 則約 1.03x。
- **利息保障倍數**: EBIT 1.589B / 利息費用 0.181B ≈ 8.8x (FY2025 為 7.1x)；利息費用 YoY +23%。
- 季度淨負債走勢: FY2025 年末 0.952B → Q1 1.315B → Q2 2.046B (高點) → Q3 2.018B → Q4 1.640B。FY2026 期間發生收購 (Q2 購併現金流出 0.724B USD)，於 Q2 推升負債。
- 債務結構: 長期債務 2.880B、長期租賃 0.530B、流動債務 0.499B、流動租賃 0.111B。

**數據一致性注意**: yfinance 的 "Net Debt" (1.640B) 與 info 的 totalDebt 扣除現金後之數 (2.600B) 差距約 0.96B，原因可能為租賃與其他負債定義不同。下游研究請並列兩者，不宜只引用單一數字。

## Capital allocation & insider signal

**資本配置**
- CapEx 趨勢: FY2023 1.030B → FY2024 0.784B → FY2025 0.468B → FY2026 0.628B (YoY +34%)，占營收約 1.7%；CapEx / 折舊 = 0.92x (折舊攤銷 0.681B)，以維持性支出為主，FY2026 有回升。Q4 FY2026 CapEx 0.246B，為單季高點，需留意是否為新一輪擴產。
- 庫藏股: FY2026 回購 1.060B USD (FY2025 1.000B、FY2024 2.500B、FY2023 0.487B)。FY2026 回購占 FCF 77%。逐季: Q1 0.300B、Q2 0.300B、Q3 0.291B、Q4 0.169B。
- 股利: FY2026 現金股利 0.035B USD，為 0.08 USD / 季 (年 0.32 USD)，股息殖利率 0.12%，payoutRatio 3.3%。股利覆蓋 (FCF / 股利) 約 39x，股利屬象徵性。
- 股本: 稀釋加權平均股數由 FY2023 135.9M 降至 FY2026 106.9M (-21%)，回購顯著減少股本。info sharesOutstanding 102.97M。
- 總股東回報 (回購 + 股利) FY2026 1.095B USD，占 FCF 80%。
- 併購: FY2026 購併現金流出 0.852B USD (其中 Q2 FY2026 為 0.724B)，商譽與無形資產由 1.114B 增至 1.828B。
- 債務: FY2026 發行 2.773B、償還 2.528B，淨增 0.245B，屬再融資為主。

**內部人交易 (近六個月: 2026-05-01 至 2026-11-01)**
- 公開市場賣出 (Sale): 3 筆，合計 2,094 股，約 0.629M USD
  - 2026-07-06 CROWLEY MATTHEW 94 股 @345 (32,430 USD)
  - 2026-07-15 SCHICK GARY K. (Officer) 1,000 股 @315–330 (319,857 USD)
  - 2026-10-20 SCHICK GARY K. 1,000 股 @274–280 (277,161 USD)
- 公開市場買進 (Purchase): 1 筆 — 2026-07-17 董事 TYAGARAJAN NALLICHERI VYDIANATHAN 500 股 @299.63 (149,815 USD)
- 淨額: 約 -0.48M USD，占市值 28.08B USD 之 0.002%，**判定為中性、無明顯訊號**。
- 2026-10-22 之大量 Stock Award (CEO DASTOOR MICHAEL 93,490 股等) 為例行股權授予，非市場交易，不計入買賣。
- 較早期賣出 (2026-01 至 2026-04，超出六個月窗口，僅作背景): 合計約 33.0M USD 公開市場賣出。主要賣方包括 MONDELLO MARK T (2026-01 約 14.5M USD，Officer and Director)、DASTOOR MICHAEL (CEO，2026-01 3.70M、2026-04 2.71M)、BORGES STEVEN D (2026-04 約 5.7M)、PRIESTLEY ANDREW (2026-04 約 2.2M)。賣出價格多在 231–340 USD，高於現價 272.72。
- 內部人持股比例 1.27% (heldPercentInsiders)，持股比例低，賣出規模對股價的壓力有限；但多位高階主管於同期賣出，是需要留意的訊號。

**機構持股與空方**
- 機構持有比例 (heldPercentInstitutions) 報 101.1%，超過 100% 屬資料重複計算，**不可信，不作為判讀依據**；institutionsCount 1,521。
- 前十大持有人合計約 48.4%: BlackRock 9.84%、Vanguard Capital Management 6.69%、Texas Yale Capital 6.10%、Vanguard Portfolio Management 5.28%、State Street 4.79%、Wellington 4.18%、Primecap 3.08%、UBS 2.94% (季變化 +79%)、Geode 2.90%、JPMorgan 2.64%。
- 空方部位: 2.75M 股，占流通股 3.13%，short ratio 1.73 日；較前月 2.86M 減少 3.6%，空方壓力不高。

**治理風險 (Yahoo 量表，數值越高風險越大)**: overallRisk 8、boardRisk 10、auditRisk 9、shareholderRightsRisk 5、compensationRisk 4。董事會與審計風險分數偏高，值得在下游研究中留意。

## Valuation

**價格與市值 (以 2026-11-01 快取報價計)**
- 現價 272.72 USD (當日 -4.98%；52 週區間 189.60 至 428.93)；50 日均線 299.55、200 日均線 307.77，股價低於兩者。
- 市值 28.08B USD；企業價值 (EV) 30.69B USD。
- Beta 1.295；52 週漲幅 +23.8% (S&P 500 同期 +10.6%)。

**估值倍數**

| 倍數 | 數值 | 計算 / 來源 |
|---|---|---|
| Trailing P/E (GAAP) | 27.97x | 272.72 / TTM EPS 9.75 |
| Trailing P/E (調整後, 自算) | 約 20.8x | 272.72 / 四季調整後 EPS 合計 13.10 |
| Forward P/E | 12.30x | 272.72 / forwardEps 22.17 |
| Current-year P/E (info) | 15.42x | priceEpsCurrentYear (epsCurrentYear 17.69) |
| EV/EBITDA (info EBITDA 2.513B) | 12.2x | info enterpriseToEbitda |
| EV/EBITDA (yf EBITDA 2.270B) | 約 13.5x | 30.69 / 2.27 |
| EV/Sales | 0.85x | info enterpriseToRevenue |
| P/S | 0.78x | info priceToSalesTrailing12Months |
| P/FCF (FY2026 FCF 1.374B) | 約 20.4x | 28.08 / 1.374 |
| P/B | 17.7x | info priceToBook (bookValue 15.44) |
| PEG | 0.82 | info pegRatio |

- 估值解讀: 以 GAAP trailing 計 P/E 偏高，但 forward P/E 與 PEG 顯示市場未完全反映 FY2027 獲利成長。forwardEps 22.17 與 epsCurrentYear 17.69 差異頗大，口徑未確認，**下游使用 forward 數字時應謹慎**。
- 分析師: 9 位，recommendationMean 1.4 (strong_buy)。目標價: 平均 425 (+55.8%)、中位數 430 (+57.7%)、低 365 (+33.8%)、高 475 (+74.2%)。此為市場共識資訊，非本報告建議。

**同業中位數 (估計，非工具資料)**: Electronic Components / EMS 同業 (如 FLEX、CLS、SANM、PLXS) 之一般區間估計 trailing P/E 約 20–25x、forward P/E 約 15–20x、EV/EBITDA 約 10–14x、P/S 約 0.5–1.0x、毛利率約 6–10%、營業利益率約 3–6%。以上為經驗估計，請下游以同業實際資料校正。

## Key catalysts
- **Q1 FY2027 財報**: 預估 2026-12-16 (isEarningsDateEstimate = true，尚未確認)；EPS 共識 4.05 USD。前八季 EPS 中有七季超出預期 (Q4 FY2026 調整後 EPS 4.40 vs 預估 4.08，+7.96%；Q3 +1.35%，Q2 +7.22%，Q1 +4.36%)。
- **股利**: 每季 0.08 USD，除息日 2026-11-16 (公司已公告)。
- **指引 (guidance)**: 工具未提供公司指引數字，**n/a**。
- **FY2026 併購整合**: 商譽與無形資產增加約 0.7B USD，後續整合成效與毛利率回升是觀察重點。
- **應付帳款與營運資金**: 下一季 OCF 是否延續 FY2026 的應付帳款擴張，將決定 FCF 的可持續性。
- **利息成本**: 利息費用 YoY +23%，淨負債仍在高位，對利率環境敏感。

## Metrics table
單位標示: 金額 USD B (十億) / USD M (百萬)；比率為 %、x。同業中位數為估計值。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (USD B) | 35.95 (FY2026) | +20.6% | 成長約 5–10% (估計) | 強於產業，但 3 年 CAGR 僅 1.2% |
| 毛利率 | 9.2% | +0.35pp | 6–10% (估計) | 處於 EMS 中段，持平 |
| 營業利益率 | 5.1% | +0.29pp | 3–6% (估計) | 中性 |
| GAAP 淨利率 | 2.9% | +0.7pp | 2–4% (估計) | 中性 |
| ROE (info) | 66.4% | n/a | 約 15% (估計) | 失真，不作參考 |
| ROIC (自算) | 約 25–29% | n/a | 約 10–12% (估計) | 優於同業，但受輕資產與應付帳款支撐 |
| FCF (USD B) | 1.37 | +17.2% | n/a | 成長，品質待觀察 |
| FCF / 淨利 | 1.32x | 由 1.78x 降至 | 約 0.9–1.1x (估計) | 達標，但依賴應付帳款 |
| FCF 利潤率 | 3.8% | -0.1pp | 2–5% (估計) | 中性 |
| 流動比率 | 0.99x | -0.01x | 約 1.5x (估計) | 偏弱 |
| 淨負債 (USD B, yf) | 1.64 | +72% | n/a | 上升，需留意 |
| 淨負債 / EBITDA (yf) | 0.72x | +0.16x | 約 1.5x (估計) | 槓桿可接受 |
| 負債權益比 (yf) | 2.49x | 上升 | 約 0.8x (估計) | 偏高 |
| 有形淨值 (USD B) | -0.215 | 由 +0.399 轉負 | n/a | 紅旗 |
| 利息保障倍數 | 約 8.8x | 由 7.1x 升 | 約 6–8x (估計) | 良好 |
| CapEx / 營收 | 1.7% | +0.1pp | 約 2–3% (估計) | 低 |
| 回購 (USD B) | 1.06 | +6% | n/a | 占 FCF 77%，股本減少 3.6% |
| 股利殖利率 | 0.12% | n/a | 約 1% (估計) | 象徵性 |
| 內部人淨買賣 (近六個月) | 約 -0.48M USD | n/a | n/a | 中性 |
| Trailing P/E (GAAP) | 27.97x | n/a | 約 22x (估計) | 偏高 |
| Forward P/E | 12.30x | n/a | 約 16x (估計) | 偏低 |
| EV/EBITDA (info) | 12.2x | n/a | 約 11x (估計) | 略高 |
| P/FCF | 約 20.4x | n/a | 約 18x (估計) | 中性偏高 |
| P/S | 0.78x | n/a | 約 0.7x (估計) | 中性 |
| 分析師平均目標價 | 425 USD | n/a | n/a | 隱含上行約 56%，非本報告建議 |

## Red flags
- **營運資金依賴供應商融資**: 應付帳款 FY2026 增加 7.98B USD (+82%)，超過全年 OCF 2.00B。FCF 亮眼的基礎脆弱，若付款條件收緊將迅速逆轉。
- **流動性緊繃**: 流動比率 0.99x、營運資金 -0.153B USD、速動比率 0.44x。
- **有形淨值轉負** (-0.215B USD)：商譽與無形資產 1.83B USD 超過股東權益 1.61B USD。
- **權益被庫藏股壓縮**: 庫藏股累計 9.02B USD，股東權益僅 1.61B USD，使 ROE (66%) 與負債權益比 (2.5x 至 2.7x) 失真。
- **淨負債擴大**: 淨負債 YoY +72%，利息費用 YoY +23%；FY2026 期間因收購一度升至 2.05B USD。
- **治理風險偏高**: boardRisk 10、auditRisk 9、overallRisk 8。
- **內部人於 2026 年 1 至 4 月大量賣出** (約 33M USD，含 CEO 與多位高階主管)；近六個月雖較平靜，但需與股價走勢一併評估。
- **股價動能偏弱**: 現價低於 50 日與 200 日均線，較 52 週高點 428.93 下跌 36%；單日跌 5%。
- **獲利結構薄**: 毛利率 9%、營業利益率 5%，對成本與產能利用率敏感。
- **資料品質問題 (下游需留意)**:
  - 淨負債口徑差異 (yf 1.64B vs info 2.60B)。
  - 期末股數欄位不一致 (FY2026 Share Issued 104.5M vs 2026-05-31 季報 279.4M 含庫藏股)，以 info sharesOutstanding 102.97M 為準。
  - 機構持股比例 101.1%，不可信。
  - Forward EPS (22.17) 與 current-year EPS (17.69) 差異，口徑未確認。
  - FY2022 數據全部為 null。
  - 報價來源為快取 (source: cache)，yfinance 多個端點出現 Yahoo cookie / crumb 連線失敗，數據品質需以後續更新為準。

FUNDAMENTALS REPORT COMPLETE
