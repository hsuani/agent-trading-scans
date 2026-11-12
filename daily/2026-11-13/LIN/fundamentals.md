# Fundamentals — LIN (Linde plc) as of 2026-11-13

**資料說明**
- 幣別：USD。金額以 B (十億美元) 或 M (百萬美元) 標示；不混用 億。
- 價格與市值：`info` 與 `fast_info` 均為 **source: cache**（info cached_at 2026-11-12T15:05:54Z；fast_info cached_at 2026-11-12T15:01:16Z）。即時 feed 失敗，已依規定回退快取，非錯誤。
- 財務報表 (annual / quarterly)、earnings_dates、insider、holders：CLI 輸出未附 source 標記，以 CLI 回傳值為準。
- 最新已公布季度：2026-09-30 (FY2026 Q3)，對應財報日 2026-10-29，皆早於 as-of 日期。
- 時間界線：`exDividendDate` 2026-12-03 與下次財報日 2027-02-04 為預定日程，尚未發生，僅列於 Catalysts，不作為已發生數據使用。
- 未取得資料（DATA_UNAVAILABLE）：segment 收入拆分、管理層 guidance、sector median 實際值（以下 sector median 皆為估計，非 feed 數據）。

## Executive summary
LIN 財務體質穩健：FY2025 營收 33.99 B USD (YoY +3.0%)、淨利 6.90 B USD、ROE 17.7%，TTM 淨利率 19.3%，淨負債/TTM EBITDA 1.70x，屬可承受水準。成長與現金流品質偏弱：FY2022-25 營收 CAGR 僅 0.6%，FCF/NI 0.74 低於 0.9 健康線，資本支出升至營收 15.5%，股利加買回占 FCF 146% 並以舉債支應。估值偏貴：trailing P/E 34.9x、EV/EBITDA 約 19.3x、P/FCF 47.5x，明顯高於估計 sector 中位數；分析師共識 Buy（27 家，平均目標價 551.04 USD，較現價 +4.9%），內部人 6 個月淨賣出約 7.45 M USD，占市值比例可忽略。

## Revenue & profitability

**年度趨勢（USD B；比率為自算）**

| 年度 | 營收 (B USD) | 營收 YoY | 毛利率 | 營業利益率 (reported) | 淨利率 | 稀釋 EPS (USD) |
|---|---|---|---|---|---|---|
| FY2022 | 33.36 | n/a | 41.7% | 16.1% | 12.4% | 8.23 |
| FY2023 | 32.85 | -1.5% | 46.8% | 24.4% | 18.9% | 12.59 |
| FY2024 | 33.01 | +0.5% | 48.1% | 26.2% | 19.9% | 13.62 |
| FY2025 | 33.99 | +3.0% | 48.8% | 26.3% | 20.3% | 14.61 |
| TTM (至 2026-09-30) | 36.24 | n/a | 47.9% | 25.3% | 19.3% | 15.05 |

- 3 年營收 CAGR（FY2022→FY2025）：+0.6%。FY2021 營收為 n/a，無法計算 4-5 年 CAGR。
- 3 年淨利 CAGR：+18.5%（4.15 B → 6.90 B）；稀釋 EPS CAGR：+21.1%。獲利成長明顯快於營收，主要來自毛利率由 41.7% 提升至 48.8%，以及股數減少（稀釋股數 504M → 473M）。
- 最新季 FY2026 Q3（2026-09-30）：營收 9.40 B USD（YoY +9.2%，QoQ +1.3%）；毛利率 47.2%；GAAP 稀釋 EPS 3.66（YoY -10.5%）；GAAP 淨利 1.69 B（YoY -12.3%）。
- 盈餘口徑：earnings_dates 的 Reported EPS 為 4.59（估計 4.52，超出 +1.6%）；該值與 quarterly_fin 的 GAAP 稀釋 EPS 3.66 口徑不同，前者應為 adjusted EPS（feed 未明示）。GAAP 與 adjusted 差距主要來自特殊項目（FY2025 Total Unusual Items -430M；Restructuring 與 M&A 費用 488M）。
- 營業利益口徑：quarterly_fin 同時提供 Operating Income 2.548 B 與 Total Operating Income As Reported 2.150 B（Q3 2026），差額即特殊項目。本報告以 reported 為準。
- 獲利能力：ROE 17.7%、ROA 7.2%（info）。ROIC 為自算近似值：TTM NOPAT ≈ EBIT 9.58 B × (1 − 22%) ≈ 7.48 B，除以期末 Invested Capital 66.12 B，約 11.3%；FY2025 以平均 IC 計約 11.6%。
- 分部：segment 收入拆分 DATA_UNAVAILABLE。longBusinessSummary 僅描述業務為工業氣體（氧、氮、氬、氫、氦、電子與特殊氣體），終端市場涵蓋 healthcare、chemicals & energy、manufacturing、electronics 等，營運地區含 US、Brazil、Mexico、Canada、Germany、UK、China、Australia、South Korea、India 等。員工約 64,512 人。

## Cashflow & balance sheet

**現金流（USD B）**

| 年度 | 營業現金流 OCF | 資本支出 Capex | FCF | FCF 利潤率 | FCF / NI | Capex / 營收 |
|---|---|---|---|---|---|---|
| FY2022 | 8.86 | 3.17 | 5.69 | 17.1% | 1.37 | 9.5% |
| FY2023 | 9.31 | 3.79 | 5.52 | 16.8% | 0.89 | 11.5% |
| FY2024 | 9.42 | 4.50 | 4.93 | 14.9% | 0.75 | 13.6% |
| FY2025 | 10.35 | 5.26 | 5.09 | 15.0% | 0.74 | 15.5% |
| TTM (至 Q3 2026) | 10.71 | 5.63 | 5.08 | 14.0% | 0.73 | 15.5% |

- FCF/NI 近三年由 0.89 降至 0.74，低於 0.9 健康線。OCF/NI FY2025 為 1.50，OCF 本身健康，弱點在資本支出擴張。
- 資本支出 FY2022→FY2025 由 3.17 B 增至 5.26 B（+66%），為 D&A 3.76 B 的 1.40 倍，屬擴張期投資。

**資產負債表（USD B）**

| 項目 | FY2025 (2025-12-31) | Q3 2026 (2026-09-30) |
|---|---|---|
| 現金及約當現金 | 5.06 | 3.95 |
| 總負債 Total Debt | 28.07 | 26.70 |
| 淨負債 Net Debt | 21.93 | 22.76 |
| 普通股權益 Common Equity | 38.25 | 39.42 |
| 含非控制權益總權益 | 39.74 | 41.00 |
| 流動比 Current Ratio | 0.87 (13.33 / 15.20) | 0.86 (info 0.858) |
| 速動比 Quick Ratio | n/a | 0.64 (info) |
| 有形淨值 Tangible Book | -1.55 | 0.10 |

- 淨負債 Q3 2026 較 FY2025 增加 0.82 B（+3.7%），但較 Q2 2026 的 23.12 B 下降。
- 負債權益比 Total Debt / Total Equity（含 NCI）：0.65x（info debtToEquity 65.1%，與自算一致）。
- 淨負債 / TTM EBITDA：1.70x（TTM reported EBITDA 13.41 B；info 報 EBITDA 13.82 B，口徑略不同）。
- 利息保障：FY2025 EBIT 9.36 B / 利息費用 0.46 B ≈ 20.2x。
- 有形淨值接近零：Goodwill 27.93 B + 其他無形資產 11.87 B（FY2025）≈ 39.8 B，與普通股權益 39.4 B 相當，代表資產負債表高度依賴收購所產生的商譽。
- 營運資本為負（Q3 2026 -2.23 B），feed 未細分其成因；但流動比低於 1，需留意短期債務 (current debt 6.11 B) 之再融資。

## Capital allocation & insider signal

**資本配置（USD B）**

| 年度 | 股利支出 | 股票買回 | 股東回報合計 | 占 FCF 比 | 股利 / NI |
|---|---|---|---|---|---|
| FY2022 | 2.34 | 5.17 | 7.51 | 132% | 56% |
| FY2023 | 2.48 | 3.96 | 6.44 | 117% | 40% |
| FY2024 | 2.66 | 4.48 | 7.14 | 145% | 40% |
| FY2025 | 2.81 | 4.60 | 7.41 | 146% | 41% |
| 9M 2026 | 2.21 | 2.63 | 4.85 | 138% (FCF 3.51) | n/a |

- FY2025 股利 / FCF 覆蓋倍數為 1.81x，股利本身可被 FCF 覆蓋；但股利加買回合計超過 FCF，缺口由淨舉債支應（FY2025 Net Issuance of Debt 2.91 B；淨負債 FY2024 16.77 B → FY2025 21.93 B）。
- 股息：年股利 6.40 USD，殖利率 1.22%（以 525.49 計）；5 年平均殖利率 1.29%；payoutRatio 41.8%（info）。
- 股數：稀釋平均股數 FY2024 482.1M → FY2025 472.9M（-1.9%）→ Q3 2026 462.5M。流通股數 459.1M。買回仍在執行，每股盈餘受益。
- 股票投資 / 併購：FY2025 Purchase of Business 0.41 B，併購規模小於 FY2023 的 0.95 B。

**內部人交易（窗口：2026-05-13 至 2026-11-13，6 個月）**

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD M) | 價格 (USD) |
|---|---|---|---|---|---|---|
| 2026-11-02 | BICHARA GUILLERMO | Officer | 公開市場賣出 | 9,350 | 4.85 | 518.91 |
| 2026-11-02 | BICHARA GUILLERMO | Officer | 衍生性商品行使 (conversion, strike 173.13) | 26,155 | 4.53 (以行使價計) | n/a |
| 2026-08-18 | REYNOLDS PAULA ROSPUT | Director | 公開市場買進 | 100 | 0.05 | 479.12 |
| 2026-06-08 | INNOCENZI STEFANOS | Officer | 無價格記錄 (非市場交易，性質未明) | 4,035 | n/a | n/a |
| 2026-05-15 | WOOD ROBERT L. | Director | 公開市場賣出 | 5,215 | 2.64 | 506.39 - 508.76 |

- 窗口內公開市場賣出合計 7.49 M USD；公開市場買進 0.05 M USD；淨賣出約 7.45 M USD。
- 占市值比例：7.45 M / 241.24 B ≈ 0.003%，影響可忽略。
- 行使衍生性商品後當日賣出（Bichara 2026-11-02）屬例行選擇權處理；執行長與財務長於窗口內無公開市場交易。
- 歷史參考：CEO Sanjiv Lamba 於 2025-12-08 以 396.68 USD 買進 2,520 股（約 1.00 M USD），為近期較明確的內部人買進訊號。
- 股東結構：內部人持股 0.25%；機構持股 89.1%（3,369 家）。前三大為 BlackRock 7.69%、Vanguard Capital 6.23%、State Street 4.20%。
- 空單：sharesShort 6.65 M（2026-10-30），占流通股 1.45%，short ratio 3.1 日；空單壓力低。

## Valuation

**估值（以 info currentPrice 525.49 USD，source: cache，2026-11-12）**

- 市值 241.24 B USD；企業價值 EV 266.06 B USD（自算 EV ≈ 市值 241.24 + 淨負債 22.76 + NCI 約 1.57 = 265.6 B，與 info 266.06 B 差距約 0.2%）。
- Trailing P/E：34.9x（GAAP TTM EPS 15.05，計算一致）。
- Forward P/E：26.9x（info forwardPE）；info epsCurrentYear 17.90 對應 P/E 29.4x。
- EV/EBITDA：19.3x（info，EBITDA 13.82 B）；自算 TTM reported EBITDA 13.41 B 為 19.8x。
- P/FCF（TTM FCF 5.08 B）：47.5x；FCF 殖利率 2.1%。
- P/S（TTM 營收 36.24 B）：6.66x；P/B：6.12x（BVPS 85.87）。
- PEG：2.07（info）。
- Sector median（估計，非 feed）：P/E 約 25x、EV/EBITDA 約 14x、P/S 約 2.5x、P/FCF 約 35x。LIN 各項皆高於估計中位數，屬品質溢價。

**分析師共識（info，27 家）**
- recommendationMean 1.69（averageAnalystRating: 1.7 - Buy）。
- 目標價：平均 551.04 USD（+4.9%）、中位數 560.00（+6.6%）、最高 600（+14.2%）、最低 400（-23.9%）。

**價格位置（info / fast_info）**
- 現價 525.49（info）；fast_info last_price 527.68（cache，15:01Z，略早於 info 快照）。
- 50 日 MA 488.62（現價 +7.5%）；200 日 MA 495.96（現價 +6.0%）。
- 52 週區間 387.78 – 548.20（ATH 548.20）；現價距 52 週高點 -4.1%。
- Beta 0.68。

## Key catalysts
- **最新財報（已公布）**：2026-10-29，adjusted EPS 4.59 vs 估計 4.52（+1.6%）；營收 9.40 B（YoY +9.2%）。GAAP EPS 3.66 仍年減 10.5%。
- **下次財報（預定，Yahoo 日期）**：2027-02-04，EPS 估計 4.67。日期為 feed 預定值，未經公司確認。
- **除息（預定）**：exDividendDate 2026-12-03，年股利 6.40 USD。此日期晚於 as-of，僅為日程資訊。
- **資本配置**：2026 年前三季買回 2.63 B、股利 2.21 B，合計 4.85 B，高於同期 FCF 3.51 B。後續買回節奏與淨負債變化為重點觀察項。
- **FY2026 年底**：2026-12-31（nextFiscalYearEnd）。
- **Guidance**：DATA_UNAVAILABLE（feed 無管理層 guidance）。
- **Segment 轉變**：DATA_UNAVAILABLE（無分部收入）。
- **資本支出週期**：Q3 2026 Capex 1.39 B，維持高位（FY2025 5.26 B），若後續季度回落，FCF/NI 有望回升。

## Metrics table

金額單位：USD B（除非標示 M）。Sector median 為估計值，非 feed 數據。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, B USD) | 36.24 | Q3 YoY +9.2% | n/a | 良好 |
| 營收 3Y CAGR (FY22-25) | +0.6% | n/a | ~3-4% | 偏弱 |
| 毛利率 (TTM) | 47.9% | 同期提升 | ~30-35% | 優 |
| 營業利益率 (TTM, reported) | 25.3% | Q3 2026 22.9% vs Q3 2025 27.5%；FY25 26.3% | ~15% | 優 |
| 淨利率 (TTM) | 19.3% | FY25 20.3% | ~10% | 優 |
| 稀釋 EPS (TTM, GAAP, USD) | 15.05 | Q3 GAAP -10.5% | n/a | 中性 |
| ROE | 17.7% | n/a | ~12% | 良好 |
| ROIC (自算) | ~11.3% | FY25 ~11.6% | ~9% | 中性 |
| 營業現金流 (TTM, B USD) | 10.71 | n/a | n/a | 良好 |
| 自由現金流 FCF (TTM, B USD) | 5.08 | FY25 5.09 (持平) | n/a | 中性 |
| FCF 利潤率 (TTM) | 14.0% | FY25 15.0% | ~10% | 良好 |
| FCF / NI | 0.73 (TTM) | FY25 0.74 (FY24 0.75) | >0.9 健康 | 偏弱 |
| Capex / 營收 | 15.5% (TTM) | FY25 15.5% vs FY22 9.5% | ~8-10% | 偏高 |
| 淨負債 (Q3 2026, B USD) | 22.76 | +3.7% vs FY25 | n/a | 中性 |
| 淨負債 / TTM EBITDA | 1.70x | n/a | ~2.0x | 良好 |
| 負債權益比 (Total Debt / Total Equity) | 0.65x | n/a | ~0.6x | 中性 |
| 流動比 | 0.86 | FY25 0.87 | ~1.2x | 偏弱 |
| 速動比 | 0.64 | n/a | ~0.9x | 偏弱 |
| 有形淨值 (Q3 2026, B USD) | 0.10 | 較 FY25 -1.55 改善 | n/a | 偏弱 |
| 利息保障 EBIT / Interest (FY25) | 20.2x | n/a | ~8x | 良好 |
| 股利殖利率 | 1.22% | 5Y avg 1.29% | ~2.0% | 中性 |
| 股利 / NI (payout) | 41% | FY24 40% | ~40% | 中性 |
| 股利 FCF 覆蓋 (FY25) | 1.81x | n/a | ~2x | 良好 |
| 股東回報 / FCF (FY25) | 146% | 9M 2026 138% | <100% | 偏弱 |
| 股數 (稀釋平均, M) | 462.5 (Q3 2026) | -1.9% vs Q3 2025 (471.5) | n/a | 良好 |
| 內部人 6M 淨交易 (USD M) | -7.45 | 占市值 0.003% | n/a | 中性 |
| 機構持股 | 89.1% | n/a | n/a | 中性 |
| Trailing P/E | 34.9x | n/a | ~25x | 偏貴 |
| Forward P/E | 26.9x | n/a | ~22x | 偏貴 |
| EV/EBITDA (TTM, info) | 19.3x | n/a | ~14x | 偏貴 |
| P/FCF (TTM) | 47.5x | n/a | ~35x | 偏貴 |
| P/S (TTM) | 6.66x | n/a | ~2.5x | 偏貴 |
| P/B | 6.12x | n/a | ~2.5x | 偏貴 |
| PEG | 2.07 | n/a | ~1.5 | 偏貴 |
| 分析師平均目標價 (USD) | 551.04 (+4.9%) | n/a | n/a | 中性 |
| 分析師評級 (recommendationMean) | 1.69 (Buy) | n/a | n/a | 正面 |
| 52 週位置 | -4.1% vs 52W 高 | n/a | n/a | 中性 |

## Red flags
- FCF / NI 0.74（TTM 0.73）低於 0.9 健康線，且自 FY2022 的 1.37 持續下滑；資本支出由營收的 9.5% 升至 15.5%。
- 股東回報合計占 FCF 146%（FY2025）與 138%（9M 2026），缺口由淨舉債支應，淨負債 FY2024 → FY2025 增加 5.2 B。
- 營收 3 年 CAGR 僅 0.6%，成長主要依靠毛利率提升與股數減少；FY2025 營收成長僅 +3.0%（feed 未拆分匯率影響）。
- Q3 2026 GAAP 淨利與 EPS 分別年減 12.3% 與 10.5%，特殊項目（重組、併購費用）持續出現（FY2025 Total Unusual Items -430 M）。
- 有形淨值接近零，商譽與無形資產 39.8 B 相當於普通股權益的 101%，若未來減損風險需留意。
- 流動比 0.86、速動比 0.64；短期債務 current debt 6.11 B 需持續再融資。
- 估值明顯高於估計 sector 中位數（P/E 34.9x、P/FCF 47.5x），估值安全邊際有限。
- 內部人無重大買進，窗口內僅一筆小額公開市場買入；執行長 2025-12 買進為正向訊號但規模小。
- 資料缺口：segment、guidance、sector median 實際值皆為 DATA_UNAVAILABLE 或估計；info/fast_info 為 cache 快照，非即時行情。

FUNDAMENTALS REPORT COMPLETE
