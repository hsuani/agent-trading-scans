# Fundamentals — 8046.TW (南亞電路板 Nan Ya PCB) as of 2026-10-15

資料來源：`pipeline/tools/yf.py 8046.TW <kind>`，全部為 repo cache（`source: cache`，cached_at 2026-10-14）。價格為 2026-10-14 收盤附近（regularMarketTime 對應 2026-10-14）。最新已公布季報為 2026 Q2（2026-08-06 公布）。貨幣單位 TWD，除非另註，金額以 NT$ 百萬計。

## Executive summary

南電資產負債表極為穩健（淨現金約 NT$94 億、流動比 3.39、負債/權益約 2.3%），且 2026 年 Q1–Q2 營收與獲利明顯回升（Q2 營收 YoY +41.7%、營業利益率 21.4%），但 FY2025 整體毛利率僅 9.1%、FCF/NI 僅 0.31，獲利與現金流仍處於循環谷底後的復甦初期。估值以歷史盈餘計極度昂貴（TTM P/E 168.0x、EV/EBITDA 72.7x、P/S 19.7x、P/B 18.8x），僅能以 2026 後續獲利持續放大來消化；分析師均價 NT$1,758 較現價高約 22.9%，但依據為 14 位分析師共識，不可視為獨立驗證。本報告僅為基本面評估，不構成交易建議。

## Revenue & profitability

**營收趨勢（年度）**：FY2022 NT$64,647 → FY2023 NT$42,253（YoY -34.6%）→ FY2024 NT$32,283（YoY -23.6%）→ FY2025 NT$40,173（YoY +24.4%）。
- 3 年 CAGR（FY2022–FY2025）為 -14.7%，2 年 CAGR（FY2023–FY2025）為 -2.5%。yfinance 未提供 FY2021 有效數值，無法計算 4–5 年 CAGR，此為資料缺口。
- 2026 季度營收：Q1 NT$11,177（YoY +32.1%）、Q2 NT$13,576（YoY +41.7%）。TTM 營收 NT$46,885（info totalRevenue），較 FY2025 +16.7%。

**利潤率（年度，由 financials 計算）**

| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 40.0% | 36.5% | 30.0% |
| FY2023 | 19.4% | 14.9% | 13.8% |
| FY2024 | 1.1% | -3.9% | 0.6% |
| FY2025 | 9.1% | 4.9% | 4.8% |

**利潤率（季度，由 quarterly_fin 計算）**：Q2'25 毛利率 8.0% / 營業利益率 3.8% → Q1'26 15.8% / 12.1% → Q2'26 24.7% / 21.4%。Q2'26 為本次資料範圍（Q2'25 起）內最高的毛利率與營業利益率，且兩者皆為連續三季上升。

**EPS 序列（earnings_dates，Reported EPS）**：Q2'25 -0.29、Q3'25 1.12、Q4'25 1.86、Q1'26 2.03、Q2'26 3.50。TTM EPS 8.51（與季報加總一致）。Q2'26 EPS 較估計 3.34 高 4.79%。

**ROE / ROIC**
- ROE：info 提供 11.9%（TTM 基礎）。以 FY2025 NI 與平均權益計算約 4.3%。
- ROIC 為估計值（未提供 yfinance 原始欄位）：FY2025 NOPAT（EBIT 23.6 億 × (1-17.0%)）÷ 投入資本（權益 + 有息債 - 現金，約 NT$387 億）約 5%；此數字反映 FY2025 谷底。

**Segment mix**：yfinance 未提供分部營收。依 longBusinessSummary，業務包含傳統 PCB、高密度連接板、軟硬複合板、覆晶基板（flip chip, PGA/BGA）、打線基板（wire bond）、ABF 基板與 PP 基板。ABF 基板為 tw_ic_substrate 同業比較的核心產品，但其營收占比 yfinance 未提供，列為資料缺口。

## Cashflow & balance sheet

**現金流（年度）**

| 年度 | OCF | Capex | FCF | FCF/NI | FCF 利潤率 |
|---|---|---|---|---|---|
| FY2022 | 32,307 | 16,922 | 15,386 | 0.79 | 23.8% |
| FY2023 | 16,513 | 11,779 | 4,734 | 0.81 | 11.2% |
| FY2024 | 2,160 | 2,379 | -219 | -1.08（NI 僅 2.0 億） | -0.7% |
| FY2025 | 3,027 | 2,422 | 605 | 0.31 | 1.5% |

- TTM（info）：FCF NT$4,678、OCF NT$5,869、FCF/NI 0.85、FCF 利潤率 10.0%。
- FY2025 營運現金流被 NT$54.4 億營運資金佔用吸收（應收帳款 -24.8 億、存貨 -9.7 億、其他流動資產 -22.2 億），此為 FCF/NI 偏低的主因。
- Q2'26 單季：OCF NT$1,016、營運資金佔用 NT$32.7 億（應收 -19.6 億、存貨 -9.2 億），FCF NT$660，FCF 利潤率 4.9%。
- 季度 FCF 序列：Q2'25 -765 → Q1'26 1,564 → Q2'26 660。Q3'25 季報欄位缺失，以 TTM 差額推算約 NT$403（推算值）。

**資產負債表（2026 Q2，quarterly_bs）**
- 現金及約當現金 NT$10,383；含短期投資 NT$10,547。
- 總有息債務（含租賃）NT$1,109（長期 NT$895、流動 NT$214）。
- 淨現金約 NT$94.4 億（現金 10,547 - 債務 1,109）。
- 流動比率 3.39（流動資產 29,603 / 流動負債 8,739），info quickRatio 2.60。
- 負債/權益（yfinance debtToEquity 2.251，即 2.25%）；總負債 NT$15,583 / 權益 NT$49,261 約 31.6%。
- 權益 NT$49,261，賬面價值/股 NT$76.24，每股有形資產與權益一致（無商譽）。
- 股本 NT$6,462（646.2M 股，面額 10 元）。

**營運效率與資產基礎**
- 應收帳款 Q2'26 NT$11,287，YoY +45.4%；以營收換算週轉天數約 76 天（Q2'25 約 74 天），基本持平。
- 存貨 Q2'26 NT$6,709，YoY +45.8%；存貨天數約 60 天（Q2'25 約 48 天），上升約 12 天，為需追蹤項。
- 淨 PPE 由 FY2023 NT$448 億降至 Q2'26 NT$343 億（-23.4%）。資產基礎縮減，與 2024–2025 低 capex 一致。

## Capital allocation & insider signal

**Capex**
- Capex：FY2022 169 億 → FY2023 118 億 → FY2024 24 億 → FY2025 24 億。FY2025 capex/D&A 為 0.35（D&A NT$68.9 億）。
- 2026 季度 capex：Q1 NT$417、Q2 NT$357（年化約 NT$15–17 億），低於 D&A 季度約 NT$18 億。資本支出持續低於折舊，淨 PPE 仍在下降。yfinance 未提供管理層擴產指引，無法判斷是否為刻意的資本紀律或產能擴張延後。

**股利與回購**
- 股數自 FY2022 至 Q2'26 維持 646.2M，無回購、無稀釋。
- 現金股利：FY2022 支付 NT$64.6 億（NT$10/股）→ FY2023 NT$116.3 億（NT$18/股）→ FY2024 NT$35.5 億（NT$5.5/股）→ FY2025 NT$6.5 億（NT$1/股）。
- info：lastDividendValue NT$2.0、dividendYield 0.14%、payoutRatio 0.235（TTM 基礎）。Q2'26 資產負債表顯示應付股利 NT$12.9 億（即 NT$2/股已宣告未付）。
- 股利覆蓋：FY2025 FCF 對股利 0.94x；TTM FCF 對 NT$2/股年化股利約 3.6x。股利覆蓋在 TTM 基礎上已恢復，但 FY2025 尚未覆蓋。

**內部人與持股結構**
- insider（最近 6 個月交易明細）：yfinance 回傳空陣列，無法計算淨買賣，列為 n/a。
- major_holders：insidersPercentHeld 61.4%，institutionsPercentHeld 14.0%（132 家機構，inst_holders 無資料）。info 顯示公司為 Nan Ya Plastics Corporation 之子公司，持股高度集中，float 約 2.50 億股。
- 無個別內部人交易資料，因此內部人買賣訊號無法判定。

## Valuation

以 2026-10-14 價格 NT$1,430 計算（market cap 來自 info：NT$924.0 十億）：

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| Trailing P/E | 168.0x | info trailingPE，TTM EPS 8.51 |
| Forward P/E | 29.3x | info forwardPE，forwardEps 48.77 |
| 2026E P/E | 81.5x | info epsCurrentYear 17.56，priceEpsCurrentYear 81.46 |
| PEG | 11.3 | info pegRatio |
| EV/EBITDA（TTM） | 72.7x | info enterpriseToEbitda，EBITDA 126.7 億 |
| EV/Revenue（TTM） | 19.6x | info enterpriseToRevenue |
| P/FCF（TTM） | 197.5x | 924.0 十億 ÷ TTM FCF 4.68 十億（自算） |
| P/S（TTM） | 19.7x | 924.0 十億 ÷ TTM 營收 46.9 十億（自算） |
| P/B | 18.8x | info priceToBook |

- Forward EPS 48.77 與 2026E EPS 17.56 相差近 3 倍，代表 forwardEps 所指的期間應為 2027E 或更遠，且僅 14 位分析師，可信度低。以 2026E EPS 推算，H2'26 需達成約 NT$12.0 每股（Q3+Q4 平均約 NT$6.0/季），即 Q2'26 水準的約 1.7 倍，前提為毛利率延續上升。
- 分析師共識（info）：recommendationMean 1.36（strong_buy），14 位分析師，目標價 NT$1,095（低）/ NT$1,700（中位）/ NT$1,758（均價）/ NT$2,500（高）。均價較現價 +22.9%。
- 價格位置：現價 NT$1,430，52 週區間 NT$232–1,560（現價較 52 週高點低 8.3%，較 52 週低點高 516%）。info 的 52WeekChange +411.5%、beta 2.105。
- 50 日均線約 NT$1,209、200 日均線約 NT$832（依 info fiftyDayAverageChange / twoHundredDayAverageChange 反推，非直接欄位）。
- Sector median：工具未提供同業估值中位數（3037.TW、3189.TW 本次未拉取），依規定列為 n/a，不做估計。

估值判斷（基本面層面）：以歷史盈餘與 TTM 現金流計算，估值處於極高檔；估值合理性高度依賴 2026 H2 至 2027 獲利能否延續 Q2'26 的毛利率與營收成長。

## Key catalysts

- **下次財報**：yfinance 未提供未來財報日期（earnings_dates 最新紀錄為 2026-08-06，info isEarningsDateEstimate = true 且時間戳為 2025 年舊值）。依歷史慣例（2023-11-02、2024-11-05、2025-11-05），Q3'26 財報預估於 2026 年 11 月初公布，此為推估，非官方日期。
- **管理層指引**：yfinance 未提供。Q2'26 獲利大幅超過估計（+4.79%），但無法從資料確認 Q3 指引。
- **股利**：NT$2/股已宣告（應付股利 NT$12.9 億），除息日已於 2026-06 過去（exDividendDate 欄位）。
- **營運資金**：Q2'26 應收與存貨大增，若 Q3 營收持續成長，營運資金佔用可能持續壓縮 FCF，需於 Q3 財報驗證。
- **分部轉移**：ABF 與 PP 基板為 longBusinessSummary 所列產品，但分部營收未提供，無法量化其占比變化。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM, NT$十億） | 46.9 | +16.7%（vs FY2025） | n/a | 成長回升中 |
| 營收（Q2'26, NT$十億） | 13.58 | +41.7% | n/a | 強 |
| 毛利率（Q2'26） | 24.7% | +16.7 pp（Q2'25 8.0%） | n/a | 改善中，仍低於 FY2022 水準 |
| 營業利益率（Q2'26） | 21.4% | +17.6 pp（Q2'25 3.8%） | n/a | 改善中 |
| 淨利率（TTM，自算） | 11.7% | n/a | n/a | 中等 |
| ROE（TTM，info） | 11.9% | FY2025 約 4.3% | n/a | 中等，循環谷底後回升 |
| ROIC（FY2025 估計） | 約 5% | n/a | n/a | 偏低 |
| FCF 利潤率（TTM） | 10.0% | FY2025 1.5% | n/a | 改善 |
| FCF/NI（TTM） | 0.85 | FY2025 0.31 | 0.9 以上為健康（規格門檻） | 接近門檻，尚未達標 |
| 淨現金（Q2'26, NT$十億） | +9.4 | n/a | n/a | 強 |
| 流動比率（Q2'26） | 3.39 | n/a | n/a | 強 |
| 負債/權益（Q2'26） | 2.25% | n/a | n/a | 極低 |
| Capex/D&A（FY2025） | 0.35 | FY2024 0.37 | n/a | 資本支出低於折舊，需追蹤 |
| 股利覆蓋（TTM FCF / 股利） | 約 3.6x | FY2025 0.94x | n/a | 恢復 |
| 股數（Q2'26） | 646.2M | 0%（無回購、無稀釋） | n/a | 中性 |
| 內部人 6 個月淨買賣 | n/a（無資料） | n/a | n/a | 無法判定 |
| 內部人持股 | 61.4% | n/a | n/a | 高度集中（母公司控股） |
| 應收帳款週轉天數（Q2'26） | 約 76 天 | 約 +2 天 | n/a | 持平，需留意 |
| 存貨天數（Q2'26） | 約 60 天 | 約 +12 天 | n/a | 上升，需留意 |
| Trailing P/E | 168.0x | n/a | n/a | 極高（谷底盈餘所致） |
| Forward P/E | 29.3x | n/a | n/a | 高（forwardEps 期間與可信度存疑） |
| 2026E P/E | 81.5x | n/a | n/a | 極高 |
| EV/EBITDA（TTM） | 72.7x | n/a | n/a | 極高 |
| P/FCF（TTM） | 197.5x | n/a | n/a | 極高 |
| P/S（TTM） | 19.7x | n/a | n/a | 極高 |
| P/B | 18.8x | n/a | n/a | 極高 |
| 分析師均價目標 / 上行空間 | NT$1,758 / +22.9% | n/a | n/a | 共識偏多（14 家，樣本少） |
| Beta | 2.105 | n/a | n/a | 高波動 |

## Red flags

- **估值極高**：TTM P/E 168x、EV/EBITDA 72.7x、P/S 19.7x、P/B 18.8x。基本面估值需要獲利持續成長才能支撐，對獲利下修敏感。
- **FY2025 獲利與現金流薄弱**：FY2025 毛利率 9.1%、營業利益率 4.9%、FCF/NI 0.31，FY2024 為淨利 2.0 億、FCF 為負。2026 好轉尚未跨越一個完整財年驗證。
- **營運資金佔用**：Q2'26 應收 YoY +45.4%、存貨 YoY +45.8%，營運資金佔用單季 NT$32.7 億，Q2'26 FCF 利潤率僅 4.9%。
- **資本支出低於折舊**：FY2025 capex/D&A 0.35，淨 PPE 自 FY2023 下降 23.4%。若 ABF 產能擴張未獲足夠投入，未來成長上限需要質疑（yfinance 無擴產指引可驗證）。
- **FY2024 至 FY2025 股利收縮**：現金股利由 FY2023 NT$18/股降至 FY2025 NT$1/股，顯示獲利波動對股利政策的影響大。
- **Forward EPS 可信度低**：forwardEps 48.77 與 epsCurrentYear 17.56 矛盾，僅 14 位分析師，分析師目標價區間 NT$1,095–2,500 寬。
- **內部人交易資料缺失**：insider 回傳空陣列，無法驗證近期內部人買賣方向。
- **高 beta**：beta 2.105，52 週股價漲幅 +411.5%，價格波動與估值風險並存。

## 資料品質與缺口（需下游注意）

- **單位異常**：quarterly_bs 2025-06 Total Tax Payable 原始值 34000（疑似單位錯誤，未採用）；cashflow FY2025 Net Other Investing Changes 原始值 78000（疑似單位錯誤，未採用）。
- **重複值**：quarterly_cf 五季 Change In Other Current Assets 皆為 -554.5（疑似快取錯誤，未採用）。
- **Q3'25 缺欄**：quarterly_fin、quarterly_bs、quarterly_cf 皆缺 2025-09 欄位。Q3'25 營收、NI、FCF 以 TTM 差額推算（營收約 NT$109.7 億、NI 約 NT$7.2 億、FCF 約 NT$4.0 億），僅供參考。
- **info 指標不一致**：info operatingMargins 21.4% 與 Q2'26 單季營業利益率相同，非 TTM 值；info enterpriseValue NT$921.0 十億與自算約 NT$914.7 十億有差異。本報告 EV 相關倍數以 info 值為主，並標示。
- **Market cap / fast_info 缺欄**：fast_info 的 market_cap、50/200 日均線、shares 皆為 null；市值以 info marketCap 與 impliedSharesOutstanding 交叉核對（NT$924.0 十億）。
- **insider / inst_holders**：兩者皆為空陣列。
- **Sector median**：工具未提供，列為 n/a。
- **非美國上市**：8046.TW 為台股本地掛牌，yfinance 覆蓋偏薄（無 segment、無 guidance、無 insider 明細）。

FUNDAMENTALS REPORT COMPLETE
