# 基本面報告 — JBL (Jabil Inc.) as of 2026-10-26

## 執行摘要
Jabil (JBL) 的 TTM 營收約 33.6B USD、淨利率僅約 2.6%、毛利率約 9%, 財務槓桿高 (info 快照 D/E 約 2.68x, 流動比率約 0.98-0.99), 且 FY22-FY25 營收 3 年 CAGR 約 -3.8%, 但 FQ3 FY26 單季營收 YoY 已回升至 +11.8%, TTM FCF 約 1.31B 為正 (FCF/NI 約 1.5x), 利息保障倍數約 8x, 財務健康度屬中等偏弱但未見流動性危機。估值方面, 股價 273.97 USD 對應 forward P/E 約 12.4x、EV/EBITDA 約 12.3x、P/FCF 約 22x, 但以 GAAP 口徑 TTM EPS 計 P/E 約 34x, 結論高度依賴 EPS 口徑, 且 yfinance 多個欄位之間存在不一致 (見紅旗)。

## 資料時效說明
- 價格與報價時間: `regularMarketTime` 對應 2026-10-23 (週五) 收盤, 2026-10-24/25 為週末, 2026-10-26 開盤前資料無法取得。`cached_at` 為 2026-10-25 11:15 UTC。
- 財報期間: yfinance 的 FY 截止日為 8 月底。最新有完整損益/現金流的季度為 FQ3 FY26 (2026-05-31)。`earnings_dates` 顯示 FQ4 FY26 (2026-09-30 公布) 已有 Adj. EPS 4.40 (實際), 但 `quarterly_fin` 中 2026-08-31 欄位的營收、淨利為 null, 即 FQ4 FY26 的損益/資產負債表細項為 DATA_UNAVAILABLE。
- 單位: 全部為 USD。B = 十億、M = 百萬。

## 營收與獲利能力

**營收 (annual, USD M)**: FY22 33,478 / FY23 34,702 / FY24 28,883 / FY25 29,802
- 3 年 CAGR (FY22→FY25): 約 -3.8%。FY24 較 FY23 下滑 -16.8%, FY25 YoY +3.2%。
- 工具無 FY21 數據, 無法提供 5 年 CAGR。
- 季度 YoY 僅 May 季可比: FQ3 FY26 8,751 vs FQ3 FY25 7,828 = **+11.8%**。其他季度 (Nov25 8,305 / Feb26 8,282 / Aug25 8,252) 缺去年同期資料。
- TTM 營收 (Aug25–May26 四季加總): **33.59B**。info 的 `totalRevenue` 為 35.95B, 差額約 2.37B, 推測為 FQ4 FY26 含入, 但無法於工具內驗證 (DATA_UNAVAILABLE)。info 的 `revenueGrowth` 為 +28.6%, 期間未明示, 不採用。
- 分部營收: info 的 longBusinessSummary 列出三大部門 (Regulated Industries / Intelligent Infrastructure / Connected Living and Digital Commerce), 但無分部營收占比, 標示 n/a。

**毛利率 / 營業利益率 / 淨利率 (USD M, 由工具數值計算)**

| 期間 | 營收 | 毛利 | 毛利率 | 營業利益 | 營業利益率 | 淨利 | 淨利率 |
|---|---|---|---|---|---|---|---|
| FY22 | 33,478 | 2,632 | 7.9% | 1,411 | 4.2% | 996 | 3.0% |
| FY23 | 34,702 | 2,867 | 8.3% | 1,594 | 4.6% | 818 | 2.4% |
| FY24 | 28,883 | 2,676 | 9.3% | 1,437 | 5.0% | 1,388 | 4.8% (含出售業務收益 942) |
| FY25 | 29,802 | 2,646 | 8.9% | 1,436 | 4.8% | 657 | 2.2% |
| May25 單季 | 7,828 | 681 | 8.7% | 383 | 4.9% | 222 | 2.8% |
| May26 單季 | 8,751 | 828 | 9.5% | 456 | 5.2% | 275 | 3.1% |
| TTM (Aug25–May26) | 33,590 | 3,099 | 9.2% | 1,690 | 5.0% | 862 | 2.6% |

- 毛利率與營業利益率 YoY 改善: 單季 May 季毛利率 +76bp、營業利益率 +32bp。
- 淨利 FY24 含出售業務收益 (Gain On Sale Of Business 942M), 不具可比性。

**ROE / ROIC (derived)**
- info `returnOnEquity` = 66.4%, 但權益基數偏小 (buyback 與負債推升), 且與 FY25 NI/平均權益 (657 / 1,625) 的 40% 差距大, 應視為被扭曲的指標。
- ROIC (derived): FY25 EBIT 1,039 × (1 − 稅率 26.4%) ≈ 765 NOPAT ÷ Invested Capital 4,398 ≈ **17.4%**。
- ROA (info): 4.98%。

## 現金流與資產負債表

**現金流 (USD M)**

| 指標 | FY23 | FY24 | FY25 | TTM (Aug25–May26) |
|---|---|---|---|---|
| 營業現金流 (OCF) | 1,734 | 1,716 | 1,640 | 1,857 |
| 資本支出 (Capex) | 1,030 | 784 | 468 | 551 |
| 自由現金流 (FCF) | 704 | 932 | 1,172 | **1,306** |
| FCF margin | 2.0% | 3.2% | 3.9% | 3.9% |
| FCF / NI | 0.86 | 0.67 | 1.78 | **1.52** |
| OCF / NI | 2.12 | 1.24 | 2.50 | 2.15 |

- FCF/NI 年度變化大 (FY24 0.67、FY25 1.78), FY25 FCF 高於 NI 主因為應付帳款增加 +1,426M 及折舊攤銷 674M。
- info `freeCashflow` 為 1,283M, `operatingCashflow` 為 2,002M, 與季度加總略有差異, 來源期間不明, 以季度加總為準。

**資產負債表 (FQ3 FY26, 2026-05-31, USD M)**
- 總資產 23,819 / 總負債 (由總資產 − 權益推算) 約 22,496 / 股東權益 1,323
- 現金 1,360 / 總負債 (Total Debt) 3,892 (其中 Long Term Debt 2,879、Current Debt 499 + 其他)
- 淨負債: yfinance `Net Debt` = **2,018**; Total Debt − Cash 計算值 = 2,532。兩者不一致, 兩個數字都列出, 差異未能於工具內解釋。
- 流動資產 18,158 / 流動負債 18,511 → 流動比率 **0.98**; 營運資金 **−353M**
- 應付帳款 (AP) 11,908 vs 一年前 (May25) 7,614, YoY **+56%**; 存貨 5,933 vs 4,772, +24%; 應收帳款 5,473 vs 4,004, +37%
- 商譽 1,228 vs 831 (YoY +48%), 主因為 FQ2 FY26 之併購 (Purchase of Business −724M)
- info 快照 (期間未明示, 推測為 FQ4 FY26 2026-08-31): totalCash 1,739, totalDebt 4,339, 淨負債 2,600, debtToEquity 268.3% (約 2.68x), currentRatio 0.993, quickRatio 0.441, bookValue 15.44 USD/股

**償債與利息保障**
- TTM EBIT (yfinance `EBIT` 季度加總) = 1,328M; TTM 利息費用 = 163M → **利息保障倍數約 8.1x**
- 淨負債 / TTM EBITDA (yf 季度 EBITDA 加總 2,025M) = 2,018 / 2,025 ≈ **1.0x**

## 資本配置與內部人訊號

**Capex**: FY22 1,385 → FY23 1,030 → FY24 784 → FY25 468, 持續下降; Capex/營收 FY25 1.6%, 低於 D&A (674M), 呈輕資產 / 節制資本支出模式。

**併購**: TTM 淨併購支出約 −898M (主要為 FQ2 FY26 −724M), 商譽與 Goodwill 因此上升。營收增長部分來自併購, 無法拆分有機成長 (n/a)。

**股東回報**
- 回購: FY22 696 / FY23 487 / FY24 2,500 / FY25 1,000; TTM (Aug25–May26) 約 916M (25 + 300 + 300 + 291)。
- 股本: diluted average shares FY24 124.3M → FY25 110.9M (−10.8%); FQ3 FY26 106.5M。流通股數 (sharesOutstanding info) 104.79M。
- 股息: 季度 $0.08, 年化 $0.32, 殖利率 0.12%, payout ratio 4.0% (info)。FY25 股息支付 36M。公司公告 ex-date 2026-11-16, 每股 $0.08 (corporateActions)。
- 股息覆蓋: FY25 FCF 1,172 / 股利 36 ≈ 32x, 覆蓋極為充足; 回購 (TTM ~916M) 與 FCF (1,306M) 相當, 回購主要靠 FCF 支撐, 但 FQ2 FY26 淨舉債 (Issuance 1,478M / Repayment 569M) 顯示同期有 debt 融資。

**內部人交易 (6 個月窗口 2026-04-25 至 2026-10-25, 來源 yf insider)**
- 賣出 4 筆 (合計 **969,448 USD**):
  - 2026-04-30 Gary K. Schick (Officer) 1,000 股, 340,000 USD
  - 2026-07-06 Matthew Crowley (Officer) 94 股, 32,430 USD
  - 2026-07-15 Gary K. Schick (Officer) 1,000 股, 319,857 USD
  - 2026-10-20 Gary K. Schick (Officer) 1,000 股, 277,161 USD
- 買入 1 筆: 2026-07-17 Nallicheri Vydianathan Tyagarajan (Director) 500 股 @299.63, 149,815 USD
- 淨賣出約 **−819,633 USD**, 占市值 (28.71B) 約 0.003%, 規模極小。
- 窗口邊界外 (2026-04-08 至 2026-04-20) 另有 11 筆賣出, 合計約 **12.86M USD**, 含 CEO Michael Dastoor 2,713,611 USD (04-08), Steven Borges 合計約 3.69M, Andrew Priestley 合計約 2.25M。占市值約 0.045%, 仍屬小比例, 但集中且金額較大。
- 2025 年 6 月起 Mark T. Mondello (Officer & Director) 持續大量賣出 (2025-06-17 單筆 150,000 股, 約 29.0M USD), 2026 年 1 月之後未見其交易。
- 內部人持股比例 1.16% (info `heldPercentInsiders`), 持股集中度低, 機構持股 99.5%。

## 估值

**價格與市值 (info / fast_info)**: 收盤價 273.97 USD (2026-10-23), 市值 28.71B, EV 30.82B, 流通股 101.0M。
- 52 週區間 189.60–428.93, 距高點 −36.1%, 距低點 +44.5%
- 50 日均線 305.57 / 200 日均線 306.51, 股價低於兩者約 10%

**倍數**

| 倍數 | 數值 | 計算 / 來源 |
|---|---|---|
| Trailing P/E (info) | 28.1x | 以 info trailingEps 9.75 |
| Trailing P/E (GAAP 季度加總) | 約 34.2x | 273.97 / (1.99+1.35+2.08+2.59 = 8.01) |
| Trailing P/E (Adj. EPS 四季加總, FY26) | 約 20.9x | 273.97 / (2.85+2.69+3.16+4.40 = 13.10) |
| Forward P/E (info) | 12.4x | forwardEps 22.17 |
| P/E (current FY, info) | 15.5x | priceEpsCurrentYear 15.49, epsCurrentYear 17.69 |
| PEG (info) | 0.82 | |
| EV/EBITDA (info) | 12.3x | EBITDA 2,513M |
| EV/EBITDA (FY25 yfinance EBITDA 1,713M) | 約 18.0x | 30,816 / 1,713 |
| P/FCF (TTM 季度加總) | 約 22.0x | 28,709 / 1,306 |
| P/S (TTM, info) | 0.80x | |
| P/B (info) | 17.7x | bookValue 15.44 |

- 注意: `forwardEps` (22.17) 與 `epsCurrentYear` (17.69) 不一致, 來源定義不同, forward P/E 區間為 12.4x–15.5x。

**分析師共識 (info)**: 9 位分析師, recommendationMean 1.40 (strong_buy), 目標價 低 365 / 均 425 / 中位 430 / 高 475 USD。相對現價: 均值目標 +55.1%、低目標 +33.2%。分析師目標價為參考, 不代表投資建議。

**同業估值中位數**: 工具未提供同業資料, 下列為估計值 (未經工具驗證): EMS 同業 trailing P/E 約 20–30x、EV/EBITDA 約 10–14x、P/S 約 0.5–1.0x。JBL 的 P/S 0.80x 處於估計區間中段, EV/EBITDA 12.3x 接近區間中位, P/E 視口徑而定。

## 關鍵催化劑
- **下次財報**: yfinance `earnings_dates` 估計 2026-12-16 (EPS 估計 4.05; `isEarningsDateEstimate` = true)。
- **前次財報 (2026-09-30)**: Adj. EPS 4.40 vs 估計 4.08, **超預期 +7.96%**。近四季皆超預期: 2026-06-17 +1.35%、2026-03-18 +7.22%、2025-12-17 +4.36%、2025-09-25 +11.69%。過去 12 季中有 2024-03 小幅不及 (−0.12%) 之外, 其餘皆超預期。
- **股息**: ex-date 2026-11-16, $0.08。
- **指引 (guidance)**: 工具輸出無正式 guidance 文字, 標示 n/a。
- **併購整合**: FQ2 FY26 併購支出 724M, 後續整合效益與商譽減損風險為待觀察項。

## 指標總表

| 指標 | 最新值 | YoY / 對比 | 同業中位數 (估計) | 判定 |
|---|---|---|---|---|
| 營收 (TTM, B USD) | 33.59 | FQ3 FY26 單季 +11.8% | n/a | 中性 |
| 營收 3 年 CAGR (FY22–FY25) | −3.8% | n/a | n/a | 偏弱 |
| 毛利率 (TTM) | 9.2% | 單季 May 季 +76bp | 約 5–10% (估計) | 中性偏強 (EMS 區間內) |
| 營業利益率 (TTM) | 5.0% | 單季 May 季 +32bp | 約 3–6% (估計) | 中性 |
| 淨利率 (TTM) | 2.6% | FY25 2.2% | 約 2–4% (估計) | 偏弱 |
| ROE (info) | 66.4% | 權益基數偏小 | n/a | 不可靠 (扭曲) |
| ROIC (derived, FY25) | 約 17.4% | n/a | n/a | 尚可 |
| FCF margin (TTM) | 3.9% | FY25 3.9% | 約 3–5% (估計) | 中性 |
| FCF / NI (TTM) | 1.52x | FY25 1.78x | >0.9 為健康 | 健康 (但依賴 AP) |
| 淨負債 (yf, M USD) | 2,018 | FY25 952 | n/a | 偏高 |
| 淨負債 / TTM EBITDA | 約 1.0x | n/a | 約 1–2x (估計) | 中性 |
| 利息保障倍數 (TTM) | 約 8.1x | n/a | n/a | 尚可 |
| 流動比率 (FQ3 FY26) | 0.98 | info 0.993 | 約 1.2–1.8x (估計) | 偏弱 |
| D/E (info) | 268% | n/a | 約 50–100% (估計) | 偏高 |
| Trailing P/E (Adj.) | 20.9x | n/a | 約 20–30x (估計) | 合理 |
| Forward P/E | 12.4x | n/a | 約 20x (估計) | 偏低 |
| EV/EBITDA (info) | 12.3x | n/a | 約 10–14x (估計) | 合理 |
| P/FCF (TTM) | 22.0x | n/a | n/a | 中性 |
| P/S (TTM) | 0.80x | n/a | 約 0.5–1.0x (估計) | 合理 |
| 內部人 6 個月淨賣出 | −819,633 USD | 占市值 0.003% | n/a | 訊號微弱 |
| 股價 vs 200 日均線 | −10.6% | RSI14 39.1, MACD 柱 −2.83 | n/a | 偏弱 (技術面) |

## 紅旗
- **營收 3 年負成長**: FY22→FY25 CAGR −3.8%, FY24 單年 −16.8%。FQ3 FY26 雖回升, 但僅單季證據, 不足以確認趨勢反轉。
- **自由現金流依賴應付帳款**: AP 於 9 個月內由 7,937 (FY25 末) 增至 11,908 (FQ3 FY26), 增幅約 +50%, 同期營運資金為 −353M, 流動比率 0.98。FCF 的 Change in Payables 貢獻 +1,426M (FY25)。若供應商付款條件收緊, FCF 可能回落。
- **淨負債與舉債**: FQ2 FY26 Total Debt 峰值 4,389M, 季度 Issuance 1,478M, 同時仍有回購 300M。
- **盈餘口徑不一致**: 同一公司 TTM EPS 有 8.01 (GAAP 季度加總)、9.75 (info)、13.10 (Adj.) 三種, P/E 落於 21x–34x 之間。forwardEps 22.17 與 epsCurrentYear 17.69 亦不一致。
- **資料缺口**: FQ4 FY26 (2026-08-31) 的 quarterly_fin / quarterly_bs 細項為 null (DATA_UNAVAILABLE); info 的 totalRevenue (35.95B) 與季度加總 (33.59B) 差約 2.37B; 淨負債兩種算法 (2,018 vs 2,532) 不符; 工具無 segment 營收占比。
- **ROE 失真**: 66% 來自權益基數小, 不可作為品質指標。
- **技術面弱勢**: 股價低於 MA20 (295.73) / MA50 (305.57) / MA200 (306.51), 6 個月動能 −19.8%, 距 52 週高 −36.1%。ATR14 為 13.96 (約 5.1% 股價), 20 日年化波動 58%。
- **內部人集中賣出**: 2026-04-08 至 04-20 合計約 12.86M USD (含 CEO 2.71M), 雖占市值比例極小, 但屬於同一週期集中行為。

## 總結判定 (不構成交易建議)
財務健康度: 中等偏弱。槓桿與流動性指標偏緊, 營收與利潤率基礎薄, 但 TTM FCF 為正、利息保障尚可、近四季財報皆超預期, 無明顯償債危機。估值: 依 forward EPS 偏低 (12.4x), 依 Adj. TTM 合理 (20.9x), 依 GAAP TTM 偏高 (34x), 結論依 EPS 口徑而異, 建議下游研究員以 Adj. EPS 與 FCF 口徑交叉驗證。

FUNDAMENTALS REPORT COMPLETE
