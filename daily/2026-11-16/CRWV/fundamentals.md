# Fundamentals — CRWV (CoreWeave, Inc.) as of 2026-11-16

## Executive summary
CRWV 營收爆發式成長 (FY2025 派生營收約 5.13B USD, 較 FY2024 +168%; TTM 營收 9.886B USD), 但仍處於深度虧損與極度燒錢狀態: TTM 淨利 −2.527B USD, TTM FCF −19.65B USD (capex 高達 27.6B USD), 總負債 66.2B USD 對 股東權益 4.0B USD (D/E 16.5×), 流動比率僅 0.44。估值面 P/S 約 3.0×、EV/EBITDA 約 17.6× 在帳面上不貴, 但 EBITDA 不反映大量資本支出與利息, P/E 與 P/FCF 皆為負值無法比較, 財務體質判定為高風險、估值吸引力高度依賴資本支出回收假設。

資料說明: 價格為 2026-11-15 cnyes 快取 (53.13 USD), 最新已揭露財報為 2026 Q3 (2026-09-30, 於 2026-11-10 發布), 無 2026-11-16 之後資料。

## Revenue & profitability

**資料注意:** yfinance 的 `financials` / `quarterly_fin` 不含 Total Revenue 列, 營收以派生方式計算: 營收 = Total Expenses + Total Operating Income As Reported (FY2025: 5.177B + (−0.046B) = 5.131B USD; FY2024: 1.591B + 0.324B = 1.915B; FY2023: 0.243B + (−0.014B) = 0.229B; FY2022: 0.0387B + (−0.0229B) ≈ 0.0158B)。派生值與公司已知量級吻合, 但屬於推算, 非原始欄位。

**營收趨勢 (USD, 派生):**
- FY2022: 0.016B
- FY2023: 0.229B (YoY 約 +1,350%)
- FY2024: 1.915B (YoY +736%)
- FY2025: 5.131B (YoY +168%; info `revenueGrowth` = 1.682, 吻合)
- TTM (至 2026 Q3): 9.886B (info `totalRevenue`)

**CAGR:** 僅有 2022–2025 四個年度點, 2022 基期過小, 3–5y CAGR 不具意義。2023→2025 兩年 CAGR 約 +373%。TTM 9.886B 對 FY2025 5.131B 為 +93%, 但期間不同 (TTM 為 2025Q4–2026Q3), 僅供參考。

**季度 EBITDA (Normalized, USD):** 2025Q4 0.741B → 2026Q1 1.027B → 2026Q2 1.469B → 2026Q3 2.109B, 連續三季增長。

**獲利能力 (淨利率為主, 因毛利與營業利益定義衝突, 見紅旗):**
- 淨利率: FY2023 −259% (−0.594B / 0.229B), FY2024 −45.1% (−0.863B / 1.915B), FY2025 −22.7% (−1.167B / 5.131B), TTM −25.6% (−2.527B / 9.886B, 與 info `profitMargins` −0.2556 吻合)
- EBITDA 利潤率 (Normalized): FY2024 64.5%, FY2025 47.6%, TTM 52.6% (info `ebitdaMargins` 0.5263)
- 營業利益率 (info `operatingMargins`): −0.48%, TTM 營業利益 (季度 EBIT 加總) 約 +0.10B, 幾乎為零
- 毛利率: info `grossMargins` 66.75% (TTM), 但 `Reconciled Cost Of Revenue` FY2025 4.382B 推算毛利僅 14.6%, 兩者定義不同 (前者應排除折舊, 扣除 Reconciled Depreciation 2.454B 後推算毛利約 62.4%, 與 info 接近)。採用前者需註明定義。
- 每股盈餘: FY2025 diluted EPS −2.81 (年度表) ; TTM EPS −4.74 (info `trailingEps`)
- ROE: −63.95% (info); ROIC 無法以 NOPAT 正值計算, 以 TTM EBIT 0.097B × (1−40%) / 投入資本 50.9B 估算僅約 0.1%

## Cashflow & balance sheet

**現金流 (USD):**

| 期間 | 營業現金流 | 資本支出 | 自由現金流 | FCF 利潤率 |
|---|---|---|---|---|
| FY2024 | n/a (推算 OCF = FCF + Capex = −5.953 + 8.702 ≈ +2.749B) | −8.702B | −5.953B | n/m (FCF / 營收 ≈ −311%) |
| FY2025 | 推算 +3.058B | −10.309B | −7.251B | −141.3% |
| TTM (2026 Q3) | 7.197B (info) | −27.618B (季度加總) | −19.649B (info) | −198.8% |

- FCF/NI: FY2025 與 TTM 皆為負數 (NI 為負), 比值不具意義 (n/m), 健康度判定為不健康。
- 季度 FCF 惡化: 2025Q4 −2.50B → 2026Q1 −4.71B → 2026Q2 −5.74B → 2026Q3 −7.47B。
- 資本支出/營收: FY2025 2.01×; TTM 2.79× (季度 capex 2026Q3 單季 9.441B, 為營收的多倍)。

**資產負債表 (2026-09-30, USD):**
- 總負債 (Total Debt, 含 Capital Lease Obligations 19.346B): 66.219B (2025 年底 29.822B, 2026 Q1 35.147B, Q2 51.608B, Q3 66.219B, 九個月增長 +122%)
- 股東權益: 4.025B (2026Q2 5.024B, 下降 −20%)
- 有形淨值 (Tangible Book Value): 2.691B
- 現金 (季度現金流表 End Cash Position): 6.404B; info `totalCash` 4.228B (兩者不一致, 見紅旗)
- 淨負債 (總負債 − 現金 6.404B): 約 59.8B; Yahoo 資料中 `Net Debt` 列為 42.751B, 與推算不符, 以推算值為準
- 淨負債 / TTM EBITDA: 約 11.5×
- 流動比率: 0.443 (info); 速動比率 0.349 (info); 營運資金 −13.583B
- D/E (info `debtToEquity` 1,645%): 16.5×
- 利息保障: TTM EBITDA / TTM 利息支出 (2.41B) = 2.16×; 2026Q3 EBIT / 利息 = 0.220 / 0.846 = 0.26× (利息已超過營業利益)
- 利息支出 TTM 約 2.41B (2026Q4→Q3 季度加總; 2026Q3 單季 0.846B, 較 Q1 0.536B 增 +58%)

## Capital allocation & insider signal

**資本配置:**
- 資本支出: FY2023 2.943B → FY2024 8.702B (+196%) → FY2025 10.309B (+18%); TTM 27.6B。資本密集度為核心特徵。
- 融資: 債務發行 FY2025 11.829B; 2026Q1–Q3 債務發行合計 27.05B (Q1 3.290 + Q2 13.457 + Q3 10.301), 償還 TTM 約 7.98B。
- 股權融資: FY2025 普通股發行 1.491B; 2026Q1 1.985B, 2026Q2 0.997B。股本由 2025 年底 502.4M 股增至 2026Q3 554M 股, 年內稀釋約 +10.3%。
- 股息: FY2025 優先股股息 0.029B (普通股股息為 0); 無回購 (FY2025 無回購列)。股息覆蓋率 n/m (無配息且 FCF 為負)。
- 結論: 資金全數依賴外部債務與股權融資支撐資本支出, 屬於擴張型但高度外部依賴的資本配置。

**內部人與持股 (6 個月, 2026-06-17 至 2026-11-09):**
- 無公開市場買入紀錄 (purchase 類為 0)。
- 有價格揭露之賣出: 79 筆, 合計約 1.231B USD, 約 1,285 萬股。佔市值約 4.2% (1.231 / 29.55B)。
- 主要賣方 (金額): Magnetar Financial (10% 以上大股東) 0.512B; Michael Intrator (CEO) 0.419B; Brannin McBee (共同創辦人) 0.225B; Kristen McVeety 0.022B; Brian Venturo 0.021B; Nitin Agrawal (CFO) 0.019B。
- 另有 66 筆無價格紀錄 (多為間接持股/衍生性證券轉換, 未估值)。
- 解讀: 大規模賣出集中於創辦人與主要持股人, 2026 Q3 期間特別密集 (9 月 CEO 單筆 (307,692 股) 約 2,670 萬美元), 無買入訊號。
- 機構持股 77.3%, 內部人 20.0%; 機構數 1,371。前五大: Magnetar 11.35% (52.06M 股, 季增 −24.1%)、NVIDIA 10.29% (47.21M 股, 持平)、BlackRock 5.25%、Goldman Sachs 3.95%、Vanguard (兩實體合計) 約 7.2%。
- 放空: 空單股數 74.21M (上月 59.95M, 月增 +23.8%); 流通股放空比 23.3% (info `shortPercentOfFloat`); 以 info 股數計 13.3%; 回補天數 1.34 日。

## Valuation

以 53.13 USD 價格與 554M 股 (2026Q3 BS 股數) 計算市值約 29.4B USD; info `marketCap` 29.55B USD 反推股數約 556M, 兩者差異 <1%, 採用約 29.5B USD。EV 91.54B USD (= 市值 29.55 + 總負債 66.22 − 現金 4.23)。

| 指標 | 數值 | 說明 |
|---|---|---|
| 本益比 (trailing) | n/m | TTM EPS −4.74 |
| 本益比 (forward) | n/m | info forwardPE −29.97 (forward EPS −1.77) |
| P/S (TTM) | 2.99× | 29.55 / 9.886 |
| EV/Sales (TTM) | 9.26× | info enterpriseToRevenue |
| EV/EBITDA (TTM) | 17.6× | 91.54 / 5.203 |
| P/OCF (TTM) | 4.1× | 29.55 / 7.197 |
| P/FCF (TTM) | n/m | FCF −19.65B |
| P/B | 7.3× | 53.13 / 7.265 |

**分析師共識 (38 位):** 平均目標價 115.47 USD (較現價 +117%)、最低 39.00 (−27%)、最高 278.00; 推薦均值 1.78 (買進區間)。

**價格位置:** 52 週區間 40.58–138.25 USD, 現價較 52 週高點 −61.6%, 較 50 日均線 72.60 低 −26.8%, 較 200 日均線 88.99 低 −40.3%; 52 週漲跌 −29.5%。

**Sector median (估計):** Software-Infrastructure 同業中位數 (估計, 非 yfinance 欄位): P/S 約 6–8×, EV/EBITDA 約 20–25×, 毛利率約 70%。CRWV 之 P/S 低於估計中位數、EV/EBITDA 略低, 但其淨負債與 FCF 結構與同業差異極大, 直接比較之參考價值有限。

**Beta:** DATA_UNAVAILABLE (info 無 beta 欄位)。

## Key catalysts
- **最近財報:** 2026-11-10 發布 2026 Q3 (2026-09-30 季)。EPS −1.27 vs 預估 −1.55, 優於預期 18.2%; 營收 / 指引: DATA_UNAVAILABLE (yfinance 不提供)。
- **下次財報:** yfinance `earnings_dates` 顯示 2027-02-25 (EPS 預估 −0.94); 此為 yfinance 預估日期, 請以公司公告為準。
- **近期 EPS 紀錄 (earnings_dates):** 2025Q4 −0.89 (miss −30%), 2026Q1 −1.12 (miss −22%), 2026Q2 −1.14 (beat +22%), 2026Q3 −1.27 (beat +18%)。
- **Segment 結構:** info 業務描述含 GPU/CPU 運算、網路、託管服務、Weights & Biases (AI 開發平台)、印度 AdaniConneX 資料中心合作; 分部營收表: DATA_UNAVAILABLE。
- **客戶集中度、合約積壓 (backlog)、資料中心產能與資本支出指引:** DATA_UNAVAILABLE (yfinance 無此欄位)。
- **融資事件:** 2026Q2 單季債務發行 13.46B、Q3 10.30B, 後續再融資條件與利率為關鍵觀察點 (2026Q3 利息支出 0.846B)。
- **大股東動向:** Magnetar 季度減持 −24.1%, 放空比例自 59.95M 升至 74.21M 股。

## Metrics table
(營收/獲利/現金流/資產負債單位: B USD; 比率單位如表內)

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (派生, FY2025, B USD) | 5.131 | +168% | n/a | 高成長 |
| 營收 (TTM, B USD) | 9.886 | n/a | n/a | 持續擴張 |
| 毛利率 (info, TTM) | 66.8% | n/a | ~70% (估計) | 與同業相近, 定義需確認 |
| EBITDA 利潤率 (TTM) | 52.6% | FY2025 47.6% | ~30% (估計) | 偏高, 不含資本支出與利息 |
| 營業利益率 (TTM) | ~1% (近零) | n/a | ~10% (估計) | 偏弱 |
| 淨利率 (TTM) | −25.6% | FY2025 −22.7% | ~5–15% (估計) | 不健康 |
| ROE (info) | −63.95% | n/a | ~15% (估計) | 不健康 |
| FCF (TTM, B USD) | −19.65 | 較 FY2025 −7.25 惡化 | 正值 (估計) | 不健康 |
| FCF / NI | n/m (兩者皆負) | n/a | >0.9 | 不具意義, 不健康 |
| 資本支出 / 營收 (TTM) | 2.79× | FY2025 2.01× | ~0.2–0.3× (估計) | 極高 |
| 總負債 (2026Q3, B USD) | 66.22 | 2025 年底 29.82 (+122% 9M) | n/a | 高風險 |
| 股東權益 (2026Q3, B USD) | 4.03 | 2025 年底 3.34 | n/a | 薄弱 |
| D/E | 16.5× | 2025 年底 ~8.9× | ~0.5–1× (估計) | 極高 |
| 淨負債 / EBITDA (TTM) | ~11.5× | n/a | ~2–3× (估計) | 極高 |
| 流動比率 | 0.44 | n/a | ~1.5–2× (估計) | 流動性不足 |
| 利息保障 (TTM EBITDA/利息) | 2.16× | n/a | ~10× (估計) | 偏弱 |
| 股數 (2026Q3, M) | 554 | 2025 年底 502 (+10.3%) | n/a | 稀釋中 |
| 股息殖利率 | 0% | n/a | ~1% (估計) | 無配息 |
| 內部人淨買入 (6M) | 0 (無公開買入) | 賣出 1.231B USD | n/a | 負面 |
| 內部人賣出 / 市值 | 4.2% | n/a | n/a | 偏高 |
| 流通股放空比 | 23.3% | 空單 +23.8% (月) | ~3–5% (估計) | 極高 |
| 本益比 (TTM) | n/m | n/a | ~30× (估計) | 無法比較 |
| P/S (TTM) | 2.99× | n/a | ~6–8× (估計) | 帳面偏低, 但負債與燒錢需扣減 |
| EV/EBITDA (TTM) | 17.6× | n/a | ~20–25× (估計) | 帳面偏低 |
| 分析師平均目標價 (38 位) | 115.47 USD | 較現價 +117% | n/a | 分歧大 (低點 39, 高點 278) |
| 股價 vs 52 週高點 | −61.6% | n/a | n/a | 大幅回落 |

## Red flags
- **現金流深度為負且惡化:** TTM FCF −19.65B USD, 季度 FCF 由 −2.50B 連續惡化至 −7.47B; 資本支出 TTM 27.6B USD 為營收 2.8 倍。
- **槓桿急速攀升:** 總負債 2025 年底 29.8B → 2026Q3 66.2B USD (九個月 +122%); 淨負債/EBITDA 約 11.5×。
- **利息保障薄弱:** 2026Q3 EBIT 0.220B 低於利息支出 0.846B (倍數 0.26×); TTM EBITDA/利息 2.16×。
- **流動性不足:** 流動比率 0.44, 營運資金 −13.6B USD, 短期負債壓力大。
- **股權被稀釋與權益萎縮:** 股數 YTD +10.3%, 股東權益由 Q2 5.02B 降至 Q3 4.03B USD。
- **內部人與大股東大幅賣出:** 6 個月揭露賣出約 1.23B USD, 無公開買入; 含 CEO、共同創辦人、Magnetar (>10% 持股) 賣出。
- **放空比例高:** 流通股放空 23.3%, 空單 6 個月 +24% (月增), 股價較 200 日均線低 40%。
- **治理風險分數高:** yfinance 風險評分 overallRisk 9 (10 為最高), shareHolderRights 10, auditRisk 9, boardRisk 8 (依 yfinance 欄位, 量表以高者為風險高)。
- **資料不一致 (需下游留意):**
  - 毛利率定義衝突: info grossMargins 66.8% vs 財報 Reconciled Cost of Revenue 推算 14.6%。
  - 淨負債口徑衝突: 推算 59.8B vs Yahoo Net Debt 列 42.75B vs info totalCash 4.23B (現金 6.40B 來自季度現金流 End Cash Position)。
  - 股數衝突: info sharesOutstanding 465.8M (過時) vs 2026Q3 資產負債表 554M; info marketCap 29.55B 與 554M 股 × 53.13 (29.4B) 相符, 採用 554M。
  - Q1 2026 EPS: quarterly_fin 列 −1.40, earnings_dates 列 −1.12; TTM EPS 採 info −4.74 (與 −1.40 版本較接近)。
  - TTM FCF: info −19.65B vs 季度加總 −20.42B (差 0.77B, 小)。
  - 季度 EBITDA 加總 5.35B vs info TTM EBITDA 5.20B (差 0.14B)。
- **資料缺口 (DATA_UNAVAILABLE):** Total Revenue 與分部營收 (財報無此列), Beta, 公司指引 (guidance), 客戶集中度, 合約積壓, 資本支出指引, 股利 (不適用)。
- **資料時效:** 價格來自 2026-11-15 快取, 非 2026-11-16 收盤價; 所有財報與內部人交易資料皆早於 2026-11-16, 無後續資料外洩問題。

FUNDAMENTALS REPORT COMPLETE
