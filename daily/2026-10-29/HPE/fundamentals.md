# Fundamentals — HPE as of 2026-10-29

資料說明: 財報口徑為美元 (USD)，單位用 B (十億美元) / M (百萬美元)。財年 (FY) 結束於 10 月底，FY25 = 截至 2025-10-31。價格取自 yfinance 快取 (`cached_at` 2026-10-28 12:40 UTC)，最近一個常規盤價 60.84 對應約 2026-10-27 收盤，盤前 61.50 (2026-10-28)。as-of 2026-10-29 的盤中或收盤資料不在本次取得範圍內。最新財報季為 2026-07-31 (FY26 Q3)。

## Executive summary
HPE 的財務體質在 FY26 明顯轉好: TTM 營收 41.87B、Q3 FY26 營收年增 33.7%、TTM FCF 4.16B、總債務自 2025-10 的 24.08B 降至 2026-07 的 20.24B。但 GAAP 獲利品質仍弱 (FY25 淨利僅 0.06B、有形淨值為負 -2.94B、商譽加無形資產佔總資產 35%)，且 Q3 GAAP 淨利含 444M 處分利益。估值方面，trailing P/E 31.4x 偏高，以 FY26 調整後 EPS 估 3.83 計算的 P/E 為 15.9x，forward P/E 12.9x，分析師均值目標價 72.44 高於現價 60.84 約 19%，估值吸引力視獲利正常化能否延續而定。

## Revenue & profitability

**營收與成長 (USD B)**
- FY22 28.50 → FY23 29.14 → FY24 30.13 → FY25 34.30
- FY25 YoY +13.8%; FY22–FY25 3 年 CAGR 約 6.4%; FY23–FY25 2 年 CAGR 約 8.5%
- 季度: Q3 FY25 9.14 → Q3 FY26 12.21，YoY +33.7% (與 yfinance `revenueGrowth` 0.337 一致)
- TTM 營收 41.87B (由 Q4 FY25 9.68 + Q1 FY26 9.30 + Q2 FY26 10.68 + Q3 FY26 12.21 相加，與 info `totalRevenue` 一致)
- 注意: FY25 下半年至 FY26 的跳升與 Juniper Networks 併購 (2025 年 7 月完成，背景知識，未由工具資料確認) 的合併效應高度相關，有機成長率需另行拆解。

**分部 (segment)**
- info `longBusinessSummary` 列出五大分部: Server、Hybrid Cloud、Networking、Financial Services、Corporate Investments and Other
- 分部營收與毛利: n/a (yfinance 未提供，需查 10-Q 或 earnings release)

**獲利能力 (GAAP)**

| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY22 | 33.4% | 7.8% | 3.0% |
| FY23 | 35.1% | 8.4% | 7.0% |
| FY24 | 32.8% | 8.3% | 8.6% |
| FY25 | 30.3% | 4.8% | 0.2% |
| Q3 FY25 | 29.2% | 4.7% | 3.3% |
| Q3 FY26 | 40.1% | 12.0% | 12.6% (含 444M 處分利益) |
| TTM | 36.7% | 7.8% | 6.7% |

- FY25 毛利率較 FY24 下降 2.5 個百分點，FY25 營業利益 1.64B 受 FY25 減損 1.62B 與重組 0.46B 拖累 (yfinance 年度損益表)
- 季度毛利率持續回升，Q3 FY26 為 40.1%，較 Q3 FY25 高 10.9 個百分點
- yfinance info `operatingMargins` 12.6% 與 GAAP TTM 營業利益率 7.8% 有明顯差距，前者應為調整口徑，本報告以 GAAP 為準

**ROE / ROIC**
- ROE 10.9% (info `returnOnEquity`)，與 TTM 淨利 2.79B / 平均股東權益約 25.6B 計算一致
- ROIC 約 5.5% (估算): TTM EBIT 3.28B × (1-21%) / 最新 invested capital 46.76B；稅率 21% 為假設值

**EPS 與股本**
- TTM GAAP 稀釋 EPS 1.92 (由季度相加)，info `trailingEps` 1.94
- FY26 調整後 EPS 軌跡 (earnings_dates): Q1 0.65、Q2 0.79、Q3 1.11，加上 Q4 估計 1.27 合計約 3.82，與 info `epsCurrentYear` 3.83 一致

## Cashflow & balance sheet

**現金流 (USD B)**

| 指標 | FY22 | FY23 | FY24 | FY25 | TTM (至 2026-07) |
|---|---|---|---|---|---|
| 營業現金流 OCF | 4.59 | 4.43 | 4.34 | 2.92 | 6.69 |
| 資本支出 Capex | 3.12 | 2.83 | 2.37 | 2.29 | 2.54 |
| FCF (OCF − Capex) | 1.47 | 1.60 | 1.97 | 0.63 | 4.16 |
| FCF margin | 5.2% | 5.5% | 6.6% | 1.8% | 9.9% |
| FCF / 淨利 (NI) | 1.69x | 0.79x | 0.77x | 11x (NI 過低，失真) | 1.49x |

- FY25 OCF 2.92B，較 FY24 的 4.34B 下滑 33%，為本次主要紅旗之一
- TTM FCF 4.16B 以季度 OCF 與 Capex 相加計算。info `freeCashflow` 為 4.74B，兩者不一致，本報告採計算值
- 季度 FCF 波動大: Q4 FY25 1.82B、Q1 FY26 0.61B、Q2 FY26 0.83B、Q3 FY26 0.90B
- FCF/NI TTM 1.49x，高於 0.9 健康門檻，但 FY23–FY24 僅約 0.8x，品質不穩定
- Capex 佔營收比由 FY22 約 11% 降至 FY25 6.7%，TTM 6.1%

**資產負債表 (USD B，最新季 2026-07-31)**
- 現金及約當現金 6.22 (較 2025-10 的 5.77 增加)
- 總債務 20.24 (2025-10 為 24.08)，其中流動債務 2.90
- 淨債務 14.03 (2025-10 為 16.59；yfinance 定義)
- 淨債務 / EBITDA: 約 2.0x (以 info TTM EBITDA 6.89 計算)
- 流動比率 1.11、速動比率 0.53 (info)
- 負債 / 股東權益 (D/E) 76% (info `debtToEquity` 76.5%)
- 股東權益 26.51，有形淨值 (Tangible Book) -2.94，由負轉正前仍為負值
- 商譽加無形資產 29.45，佔總資產 83.60 之 35%
- 營運資金 3.43 (較 2025-10 的 0.35 改善)
- 總負債 57.02 (2026-07)，較 2025-10 的 51.15 增加，主要來自其他非流動負債 (由 0.79 跳升至 9.24，yfinance 分類變動，需確認)
- 利息: TTM 淨利息費用約 0.46B (季度 net interest 相加)；TTM EBIT / 淨利息約 7.1x

**債務結構變化 (USD B，FY25 全年現金流量)**
- 發行債務 9.19、償還債務 6.84，FY25 淨增加約 2.35
- TTM 季度相加: 發行 6.40、償還 9.86，淨償還約 3.46，顯示 FY26 以去槓桿為主

## Capital allocation & insider signal

**資本配置 (TTM，USD B)**
- 股票回購: 0.55 (FY25 為 0.20，FY24 為 0.15)
- 普通股股利: 約 0.74 (季度 0.171–0.190 區間)；特別股股利 0.116 (季度 0.029)
- 股利覆蓋: TTM FCF 4.16 / 普通股股利 0.74 = 約 5.6x；info `payoutRatio` 28.7%
- 殖利率 0.97% (info `dividendYield`)，五年平均殖利率 2.43%
- 股本: 流通股數 1,327.5M (info)；FY22 為 1,281M，過去約 3.5 年增加約 3.6%，有稀釋
- 季度稀釋股數 1,449M，與基本股數 1,336M 相差約 113M，推測與特別股或可轉換工具有關 (需 10-Q 驗證)

**內部人交易 (過去 6 個月，2026-04-28 至 2026-10-28)**
- 公開市場賣出合計約 41.4M USD、約 714k 股；公開市場買入: 0
- 主要賣出:
  - CEO Antonio Neri 2026-10-05 賣出 250,000 股，單價 68.31，約 17.1M USD
  - CEO Antonio Neri 2026-09-11 賣出 250,000 股，單價 60.44，約 15.1M USD
  - Networking 負責人 Rami Rahim 2026-09-29 賣出 34,456 股，約 2.1M USD；2026-07-02 有 1.12M 股選擇權轉換，另於 2026-07-07 贈與 655k 股
  - CFO Marie Myers 2026-05-05 賣出 93,583 股，約 2.8M USD
  - 董事 Gary Reiner 2026-06-03 與 2026-09-14 合計賣出約 37k 股，約 2.1M USD
- 董事年度股權獎勵 (2026-06-30、2026-09-30) 金額小，屬例行授予，非市場買入
- 規模判讀: 6 個月賣出約 41.4M，相對市值 80.76B 約 0.05%；內部人持股 0.24% (info)
- 本報告無法判定上述賣出是否屬 10b5-1 預定計畫，需查 Form 4 附註
- 信號: 沒有任何公開市場買入，且 CEO 在股價區間高點附近連續大額賣出，為偏負面訊號，但金額相對市值極小

**機構持股 (yfinance)**
- 機構持股比例 91.4%，共 2,048 家機構
- 前幾大: BlackRock 10.1%、Vanguard (兩個實體合計) 約 12.0%、State Street 5.1%、Capital World Investors 4.5%、JPMorgan 3.0%

## Valuation

**估值倍數 (價格 60.84，市值 80.76B，企業價值 94.93B)**

| 倍數 | 數值 | 計算依據 |
|---|---|---|
| Trailing P/E | 31.4x | 價格 / TTM GAAP EPS 1.94 |
| FY26 P/E (調整後) | 15.9x | 價格 / 3.83 (info `epsCurrentYear`) |
| Forward P/E | 12.9x | 價格 / forward EPS 4.71 (info `forwardEps`，推測為 FY27 共識，需確認) |
| EV/EBITDA (TTM) | 13.8x | info `enterpriseToEbitda`，EBITDA 6.89B |
| P/FCF (TTM) | 19.4x | 市值 80.76B / 計算 FCF 4.16B |
| P/S (TTM) | 1.93x | info `priceToSalesTrailing12Months` |
| P/B | 3.05x | info `priceToBook` |
| PEG | 0.47 | info `pegRatio` |

- 板塊中位數為估計值 (無工具資料來源): Communication Equipment / IT 硬體同業 Forward P/E 約 18–22x、EV/EBITDA 約 14–18x、P/S 約 2–3x、P/FCF 約 20–25x
- 相對板塊估計: trailing 偏貴，forward 與 FY26 調整後口徑處於板塊區間偏低

**股價與市場資料**
- 52 週區間 19.84–73.56，現價距高點約 −17%；52 週漲幅 +150.7% (S&P 500 同期 +12.1%)
- 50 日均線 59.46，200 日均線 40.24
- Beta 1.40
- 放空比例 4.47% (佔流通股)，short ratio 2.47 天

**分析師共識 (21 位)**
- 平均評級 2.0 (Buy)
- 目標價: 均值 72.44、中位數 70.0、最高 92.0、最低 62.0 (最低目標價仍高於現價)
- 均值目標價相對現價隱含上行約 19%

## Key catalysts

- **下次財報**: 2026-12-03 (yfinance `earnings_dates`，為 Q4 FY26 財報，日期來源為 yfinance，尚未由公司正式公告確認)
- **Q4 FY26 EPS 共識**: 1.27，對比 Q4 FY25 實際 0.62，隱含 YoY 約 +105%
- **歷史超預期紀錄**: 過去 14 季中 13 季 EPS 超過共識，近三季超預期幅度分別 +10.8%、+48.0%、+18.4%；唯一不及預期為 2025-03 (−1.8%)
- **FY26 全年調整後 EPS 隱含**: 約 3.82 (三季實際 + Q4 共識)
- **公司指引 (guidance)**: yfinance 無提供，n/a，需查 FY26 Q3 earnings release 或 8-K
- **分部動向**: 分部營收 n/a；Networking 與 Hybrid Cloud 的成長貢獻需由 release 拆解
- **已發生事件**: 2026-09-02 Q3 FY26 財報超預期 (EPS 1.11 vs 估計 0.94)；Q3 GAAP 淨利含 444M 處分利益 (事件性質 n/a，需查 10-Q)
- **除息與配息**: 季度股利 0.143 (yfinance `lastDividendValue`)，最近除息日 2026-09 (ex-dividend)，下一次除息日 n/a

## Metrics table
數值單位: 營收、利潤、現金流、市值為 USD B；比率為 %、倍數為 x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, USD B) | 41.87 | +33.7% (Q3 季) | n/a (估計成長 3–6%) | 強，但含併購效應 |
| 毛利率 (TTM) | 36.7% | Q3 季 +10.9 pp | 約 35–40% | 中性，已回升 |
| GAAP 營業利益率 (TTM) | 7.8% | FY25 −3.5 pp | 約 10–12% | 偏弱 |
| GAAP 淨利率 (TTM) | 6.7% | n/a (FY25 0.2%) | 約 8–10% | 中性偏弱 |
| ROE | 10.9% | n/a | 約 12–15% | 中性偏弱 |
| ROIC (估算) | 約 5.5% | n/a | 約 8–10% | 偏弱 |
| OCF (TTM, USD B) | 6.69 | FY25 −33% (年度) | n/a | 中性 |
| FCF (TTM, USD B) | 4.16 | FY25 0.63 → TTM 4.16 | 約 3–5% FCF margin | 恢復中 |
| FCF margin (TTM) | 9.9% | FY25 1.8% | 約 5–8% | 良好 |
| FCF / NI (TTM) | 1.49x | FY24 0.77x | 約 0.9–1.0x | 健康 |
| 總債務 (USD B) | 20.24 | 2025-10 24.08 (−16%) | n/a | 改善中 |
| 淨債務 / EBITDA | 約 2.0x | 2025-10 約 2.7x | 約 1.5–2.5x | 中性 |
| 流動比率 | 1.11 | n/a | 約 1.3–1.5 | 偏低 |
| D/E | 76% | n/a | 約 40–60% | 偏高 |
| 有形淨值 (USD B) | −2.94 | 由 −5.45 (2025-10) 改善 | 正值 | 紅旗 |
| 商譽+無形資產 / 總資產 | 35% | n/a | 約 15–25% | 偏高 |
| Trailing P/E | 31.4x | n/a | 約 25x | 偏貴 |
| FY26 P/E (調整後) | 15.9x | n/a | 約 20x | 合理 |
| Forward P/E | 12.9x | n/a | 約 20x | 偏低 (需確認 FY27 口徑) |
| EV/EBITDA (TTM) | 13.8x | n/a | 約 14–18x | 中性偏低 |
| P/FCF (TTM) | 19.4x | n/a | 約 20–25x | 中性 |
| P/S (TTM) | 1.93x | n/a | 約 2–3x | 中性偏低 |
| 股利殖利率 | 0.97% | n/a | 約 1–2% | 低 |
| 股利覆蓋 (FCF / 普通股股利) | 約 5.6x | n/a | 約 2–3x | 充裕 |
| 內部人 6 個月淨買賣 | 賣出 41.4M / 買入 0 | n/a | n/a | 偏負面 (金額小) |
| 分析師平均評級 | 2.0 (Buy) | n/a | 約 2.2–2.5 | 偏正面 |
| 目標價均值 / 現價 | 72.44 / 60.84 (+19%) | n/a | n/a | 上行空間 |

## Red flags
- GAAP 獲利品質弱: FY25 淨利僅 0.06B，TTM 重組費用約 0.42B 連續多季出現，減損 FY25 達 1.62B
- Q3 FY26 GAAP 淨利 1.54B 含 444M 處分利益，剔除後正常化淨利約 1.21B，單季 GAAP 數字需打折看待
- 有形淨值為負 (−2.94B)，商譽與無形資產佔總資產 35%，併購減損風險仍存
- FY25 OCF 較 FY24 下滑 33%，季度 FCF 波動大 (0.61–1.82B)，現金流穩定性尚未證實
- 淨債務仍達 14.03B (約 2.0x EBITDA)，流動比率 1.11 偏低，TTM 仍需支付約 0.46B 淨利息
- 內部人在 6 個月內賣出約 41.4M、零買入，CEO 在 2026-09 至 10 月連續大額賣出 (需查是否為 10b5-1)
- Trailing P/E 31.4x，股價 52 週上漲 150.7%，市場已大幅反映 FY26 獲利改善，估值安全邊際有限
- 稀釋股數 1,449M 與基本股數 1,336M 相差約 113M，FY26 Q3 每股盈餘口徑需以稀釋股數為準
- 資料一致性問題: info `freeCashflow` (4.74B) 與季度相加計算值 (4.16B) 不一致；info `operatingMargins` (12.6%) 與 GAAP TTM (7.8%) 不一致；forward EPS 4.71 與 FY26 調整後 EPS 3.83 的年度口徑需確認
- 資料來源限制: 本次 yfinance `fast_info` 與多個 Yahoo 端點因 CONNECT 403 或 cookie/crumb 失敗，價格與部分欄位改用快取 (cnyes feed) 補齊；`fast_info` 的 50/200 日均線與市值欄位為 null，已改由 info 欄位取得
- 分部營收、公司指引、Juniper 併購後的有機成長率等關鍵資料 n/a，需補充 10-Q 與 earnings release 後再評估

FUNDAMENTALS REPORT COMPLETE
