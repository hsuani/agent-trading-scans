# Fundamentals — NVDA as of 2026-10-26

> 資料來源: `pipeline/tools/yf.py` (live feed 被 403 阻擋, 依規定 fallback 至 repo cache)。金額單位統一為 USD B (十億美元), 每股數字為 USD/股。財報期末日沿用 yfinance 標示 (FY 結束於 1 月, 例如 `2026-01-31` 即 FY26 年報; `2026-07-31` 為最新季)。
> 資料時點: 最新已披露財報為 2026-07-31 季 (2026-08-26 公布)。下一次財報 2026-11-17 尚未發布, 屬未來事件。工具未提供價格快照時間戳, 股價 210.96 視為 as-of 快照。未發現 2026-10-26 之後的已實現資料。

## Executive summary
NVDA 財務體質目前處於極強狀態: TTM 營收 302.97B USD、TTM GAAP 淨利 192.88B USD、2026-07 季營收 YoY +105.9%, 淨現金約 23.6B USD, 流動比率 4.59x。估值以 trailing P/E 26.7x 看不算便宜, 但以一致預期 forward EPS 15.91 計算 forward P/E 僅 13.3x, EV/EBITDA 21.6x–25.1x, P/FCF 約 40x, 估值是否合理取決於 EPS 翻倍的預期能否兌現。主要風險在於 2026-07 季營業現金流季減約 52%、應收帳款季增約 55%、帶息負債季增約 26.0B USD (工具資料無法解釋, 需查 10-Q), 以及董事於近 6 個月出售約 1.37B USD 股票且無公開市場買入紀錄。

## Revenue & profitability

**營收成長**
- 年度營收 (USD B): FY24 60.92 → FY25 130.50 → FY26 215.94。YoY: FY25 +114.2%, FY26 +65.5%。
- FY23 至 FY26 三年 CAGR 約 100% (26.97 → 215.94), 因 FY22 在工具中為 null, 無法計算 4-5 年 CAGR (DATA_UNAVAILABLE)。
- 季度營收 (USD B): 2025-07 46.74 → 2025-10 57.01 → 2026-01 68.13 → 2026-04 81.62 → 2026-07 96.22。QoQ 連續四季約 +18% 至 +22%。最新季 YoY +105.9%。
- TTM 營收 302.97B USD, 與 info `totalRevenue` 一致 (四季加總驗算通過)。
- 分部營收 (Compute & Networking vs Graphics): 工具無分部數字, 僅 info 敘述提及兩大分部與 data center 為主要市場 (DATA_UNAVAILABLE)。

**獲利能力 (margin 趨勢)**

| 期間 | 營收 (USD B) | 毛利率 | 營業利益率 | 淨利率 (GAAP) | 稀釋 EPS (USD) |
|---|---|---|---|---|---|
| FY24 (2024-01 yfinance 標示 2024-01-31) | 60.92 | 72.7% | 54.1% | 48.9% | 1.19 |
| FY25 (2025-01-31) | 130.50 | 75.0% | 62.4% | 55.8% | 2.94 |
| FY26 (2026-01-31) | 215.94 | 71.1% | 60.4% | 55.6% | 4.90 |
| 2025-07 季 | 46.74 | 72.4% | 60.8% | 56.5% | 1.08 |
| 2026-07 季 | 96.22 | 75.0% | 66.2% | 62.0% | 2.46 |

- FY26 毛利率 (71.1%) 低於 FY25 (75.0%), 但季度毛利率於 2026-01 至 2026-07 維持約 75%, 顯示年度下滑主要集中在較早季度, 工具未提供季度分拆 (需參考 10-K/10-Q)。
- 2026-07 季營業利益 63.73B USD, YoY +124.1%。稀釋 EPS 2.46 USD, YoY +127.8%。
- 注意 GAAP 與非 GAAP 差異: 2026-07 季 `Total Unusual Items` = 7.77B USD (稅後效果 1.28B), 去除後 normalized net income 約 53.20B USD, 故 GAAP 淨利 59.69B 含約 6.5B USD 非經常性收益 (稅後估計)。`earnings_dates` 所列 Reported EPS 2.22 USD 與 GAAP 稀釋 EPS 2.46 USD 不同, 前者應為調整後口徑 (53.20B / 24.29B 股 ≈ 2.19 USD 與之吻合)。
- 2026-04 季 NI (58.32B) 高於營業利益 (53.54B), 差額屬非營運項目, 工具未拆解 (需查證)。
- ROE: 以 TTM NI 192.88B / 2026-07 期末權益 228.98B 計算約 84%; yfinance info 報 117.2%, 兩者定義不同, 以前者為保守值。
- ROIC (估計): TTM 營業利益 197.58B × (1 − 16.5% 稅率) ≈ 165B USD NOPAT, 除以 (權益 228.98 + 負債 38.35 − 現金及短期投資 62.47 ≈ 204.9B) ≈ 80%。

## Cashflow & balance sheet

**現金流量**
- 營業現金流 (OCF, USD B): FY24 28.09 → FY25 64.09 → FY26 102.72。
- 自由現金流 (FCF = OCF − capex, USD B): FY24 27.02 → FY25 60.85 → FY26 96.68。FCF margin FY26 = 44.8%。
- 季度 OCF: 2025-07 15.37 → 2025-10 23.75 → 2026-01 36.19 → 2026-04 50.34 → 2026-07 24.08。2026-07 季 OCF 較前一季 −52%, 但較去年同季 +57%。
- 季度 FCF: 2026-07 21.40 / 2026-04 48.59 / 2026-01 34.90 / 2025-10 22.12, TTM 合計 127.0B USD, FCF margin TTM 41.9%。
- FCF / NI 比率: FY24 0.91、FY25 0.84、FY26 0.81, TTM 0.66 (以 127.0 / 192.88 計算), 低於 0.9 健康門檻。2026-07 單季僅 0.36。OCF / NI TTM 0.70。
- 警示原因之一: 應收帳款 (AR) 2026-07 為 63.06B USD, 較 2026-04 的 40.71B 增加 55%, 同期營收僅 +18%。DSO 估計約 60 天 (2026-07), 去年同季約 54 天。存貨 31.58B USD, 較前季 +22%, 存貨天數估計約 119 天 (去年同季約 106 天)。
- info 的 `freeCashflow` 為 41.81B USD, 與季度 OCF 與 capex 推算之 TTM FCF 127.0B 明顯不符。本報告採用季度推算值, info 數字為 DATA_CONFLICT, 不採用。

**資產負債表 (2026-07-31)**
- 總資產 320.27B USD, 總負債 91.29B USD, 股東權益 228.98B USD (FY26 為 157.29B, 半年增加 45.6%)。
- 現金及等價物 22.44B USD, 含短期投資之現金與投資 62.47B USD。
- 總負債 (Total Debt, 含租賃) 38.35B USD, 較 2026-04 的 12.35B USD 增加約 26.0B USD。同期 quarterly 利息費用由 102M USD 升至 227M USD。工具資料無法說明此增加來源 (例如新發債券、融資性安排或會計分類變動), 需查 10-Q 確認。
- 淨現金 (cash & ST investments − total debt): 約 24.1B USD (BS 口徑) 或 23.6B USD (info totalCash 62.47B − totalDebt 38.86B)。balance_sheet 工具的 Net Debt 欄位為 10.92B USD, 與上述定義不一致, 僅列為參考。
- 流動比率 4.59x (流動資產 197.41B / 流動負債 43.02B), 速動比率 2.92x。D/E = 0.17x (38.35 / 228.98), yfinance debtToEquity 16.97 為百分比表示。
- 營運資金 (FY26): 93.44B USD。

## Capital allocation & insider signal

**資本配置**
- 買回 (buyback, USD B): FY24 9.53 → FY25 33.71 → FY26 40.09, FY26 YoY +18.9%。TTM 買回 55.3B USD (2026-07 季 19.73B, 2026-04 季 19.31B)。
- 資本支出 (capex, USD B): FY24 1.07 → FY25 3.24 → FY26 6.04, FY26 YoY +86.7%。TTM capex 7.35B USD, 佔營收 2.4%, 屬輕資產模式, 但增速快。
- 股利: info `dividendRate` 1.00 USD/年, `dividendYield` 0.47%。FY26 現金股利支出 0.97B USD, 股利覆蓋率極高。
- 異常: 2026-07 季現金股利支付 6.05B USD, 遠高於前幾季的約 0.24B USD 水準, 工具未說明 (可能為一次性股利, 需查證)。info 中 `trailingAnnualDividendRate` 0.28 與 `dividendRate` 1.00 亦不一致 (DATA_CONFLICT)。
- 股本: 流通股數由 FY24 24.64B 降至 FY26 24.30B; info sharesOutstanding 24.15B。稀釋股數 (季度) 由 2025-07 24.53B 降至 2026-07 24.29B, 買回實際抵銷部分 SBC 稀釋。
- 併購與研發: R&D (TTM) 約 23.6B USD, 佔 2026-07 季營收 7.3%; 2026-07 季 R&D 7.05B USD, YoY 約 +64% (7.054 / 4.291 − 1)。

**內部人交易 (yfinance insider, 6 個月窗口: 2026-04-26 至 2026-10-26)**
- 期間共 9 筆公開市場賣出, 0 筆買入。合計約 1.37B USD、約 6.20M 股。
- 主要賣方: 董事 Mark A. Stevens 5 筆, 合計約 1.35B USD、約 6.12M 股 (2026-06-04 $221.1M, 2026-06-18 $186.0M, 2026-09-02 $410.8M, 2026-09-04 $235.6M, 2026-09-18 $300.1M), 持股屬間接 (ownership: I)。其餘為 General Counsel Timothy Teter (2026-08-31, 2026-09-21, 各約 6.5M/6.8M USD) 與董事 Stephen Neal、John Dabiri 小額賣出。
- 占市值比: 1.37B / 5,094B ≈ 0.03%, 絕對金額大但對市值佔比極低。
- 執行長 Jen-Hsun Huang 在 2025-07 至 2025-10 有多筆固定規模 (約 225,000 股/筆) 賣出, 最後一筆為 2025-10-29; 2026 年 6 個月內無其賣出紀錄。
- 過去 18 個月 (2025-03 至 2026-09) 總計 91 筆賣出、約 3.78B USD, 持續性賣出為常態, 賣出時點多在股價高點區間。
- 贈與 (Stock Gift) 共 18 筆, 其中 Director Tench Coxe 於 2026-07-01、2026-08-05、2026-09-02 各贈與 500,000 股, 屬非市場交易, 不計入賣出。

**機構持股 (major_holders / inst_holders, 資料日 2026-06-30)**
- 機構持股比例 71.4% (7,703 家機構); 內部人持股 4.0%。
- 前十大持股合計約 33.8%: BlackRock 8.06% (1,941.9M 股, 季增 +0.85%)、Vanguard Capital Mgmt 6.39%、FMR 4.26% (季增 +3.24%)、State Street 4.19%、Geode 2.52%、Vanguard Portfolio Mgmt 2.15%、JPMorgan 1.86%、T. Rowe Price 1.53% (季減 0.07%)、Morgan Stanley 1.48% (季增 +3.93%)、Invesco 1.37%。
- 機構持股變動整體為小幅淨增加 (FMR、Morgan Stanley 增持), 未見大型機構大幅減持。

## Valuation

以現價 210.96 USD、市值 5,094.05B USD、EV 5,060.5B USD 計算:

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E | 26.7x | 210.96 / TTM GAAP EPS 7.91 |
| Forward P/E | 13.3x | 210.96 / forward EPS 15.91 (一致預期) |
| 隱含 EPS 成長 | 約 +101% | forward EPS / TTM EPS − 1 |
| EV/EBITDA | 21.6x 或 25.1x | 季度加總 EBITDA 233.9B (21.6x); info ebitda 201.3B (25.1x), 兩者定義差異 |
| P/FCF (TTM) | 40.1x | 5,094.05 / 127.0 |
| P/FCF (FY26) | 52.7x | 5,094.05 / 96.68 |
| P/S (TTM) | 16.8x | 5,094.05 / 302.97 |
| P/B | 22.2x | 市值 / 2026-07 權益 228.98 (BVPS 9.48 USD 以股數計) |
| PEG (info) | 0.26 | 工具數值, 受一致預期成長率影響大, 僅供參考 |

- 股價區間: 52 週高 243.37 USD (亦為歷史高點), 52 週低 164.27 USD。現價距高點 −13.3%、距低點 +28.4%。
- 均線: 50 日均價 222.48 (現價低於 −5.2%)、200 日均價 203.67 (現價高於 +3.6%)。
- Beta 2.22, 屬高波動標的。
- 分析師: 58 位, 平均目標價 328.95 USD (較現價 +56%), 高目標 515.00, 低目標 180.00 (低於現價), 推薦等級 strong_buy (評分 1.3)。
- 行業中位數為估計值 (非工具資料): 大型半導體 trailing P/E 約 30x、forward P/E 約 25x、EV/EBITDA 約 20x、P/S 約 8x、P/FCF 約 30x。以此為基準, NVDA trailing 與 forward 估值分化明顯, P/S 與 P/FCF 偏高。

## Key catalysts
- **下一次財報 2026-11-17 (預估)**: 一致預期 EPS 2.47 USD (earnings_dates 列出)。距 as-of 日約 22 天。
- **上一次財報 2026-08-26**: EPS 2.22 USD vs 預估 2.09 USD, 超預期 +6.2%。近八季皆為正向 surprise, 區間 +3.5% 至 +8.5%。
- **營收與 margin 動能**: 季度營收 QoQ 連續約 18%–22%, 毛利率穩定於約 75%。
- **資本回報**: 季度買回穩定於約 12–20B USD 區間 (2026-04、2026-07 皆約 19–20B USD)。
- **營運資金**: 2026-07 AR、存貨大增, 下季財報若 AR 回落則為正面訊號; 若持續增加則為現金轉換風險。
- **負債來源**: 26.0B USD 負債增加之用途與條件需於 10-Q / 下季財報釐清。
- **分部與指引**: 公司未來季度營收指引、data center 與 graphics 分部數字、毛利率指引 — DATA_UNAVAILABLE (工具未提供)。
- **公司治理**: 董事會風險分數 10 (滿分 10), 整體治理風險 8, 審計風險 5, 薪酬風險 4 (yfinance 評分)。

## Metrics table
金額單位: USD B; 每股: USD; 比率: x 或 %。Sector median 欄位為估計值, 非工具資料, 僅作對照。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue, quarterly (2026-07) | 96.22 USD B | +105.9% | 約 +10%–15% | 強勁 |
| Revenue, TTM | 302.97 USD B | n/a (季度不完整) | n/a | 強勁 |
| Revenue, FY26 | 215.94 USD B | +65.5% | n/a | 強勁 |
| Revenue 3-yr CAGR (FY23–FY26) | 約 100% | n/a | 約 10%–15% | 強勁 |
| Gross margin (2026-07 季) | 75.0% | +2.6 pt (72.4%) | 約 55%–60% | 優 |
| Operating margin (2026-07 季) | 66.2% | +5.4 pt (60.8%) | 約 20%–25% | 優 |
| Net margin GAAP (2026-07 季) | 62.0% | +5.5 pt (56.5%) | 約 15%–20% | 優 (含非經常收益) |
| Net margin normalized (2026-07 季) | 約 55.3% | n/a | 約 15%–20% | 優 |
| ROE (TTM NI / 期末權益) | 約 84% (info 117.2%) | n/a | 約 15%–20% | 優 |
| ROIC (估計) | 約 80% | n/a | 約 10%–12% | 優 |
| OCF, TTM | 134.36 USD B | n/a | n/a | 強 |
| FCF, TTM | 127.0 USD B | n/a | n/a | 強 |
| FCF margin, TTM | 41.9% | n/a | 約 15%–20% | 優 |
| FCF / NI, TTM | 0.66x | FY26 0.81x, FY25 0.84x | > 0.9 健康 | 警示 |
| OCF, 2026-07 季 | 24.08 USD B | +56.7% YoY, −52% QoQ | n/a | 警示 |
| Cash & ST investments (2026-07) | 62.47 USD B | 較 FY26 末 62.56 持平 (−0.1%) | n/a | 充足 |
| Total debt (2026-07) | 38.35 USD B | QoQ +26.0 USD B | n/a | 需查證 |
| Net cash (2026-07) | 約 24.1 USD B | n/a | n/a | 淨現金 |
| Current ratio | 4.59x | n/a | 約 2.0x | 優 |
| Debt / Equity | 0.17x | n/a | 約 0.3x | 優 |
| Capex, FY26 | 6.04 USD B | +86.7% | 約 3%–5% of revenue | 偏低 (2.8% of revenue) |
| Buyback, FY26 | 40.09 USD B | +18.9% | n/a | 積極 |
| Dividend yield | 0.47% | n/a | 約 1% | 低 |
| Trailing P/E | 26.7x | n/a | 約 30x | 合理 |
| Forward P/E | 13.3x | n/a | 約 25x | 偏低 (依一致預期) |
| EV/EBITDA | 21.6x–25.1x | n/a | 約 20x | 略高至合理 |
| P/S (TTM) | 16.8x | n/a | 約 8x | 偏高 |
| P/B | 22.2x | n/a | 約 6x | 偏高 |
| P/FCF (TTM) | 40.1x | n/a | 約 30x | 偏高 |
| Insider net sales, 6 mo | 約 1.37 USD B, 6.20M 股, 0 筆買入 | n/a | n/a | 偏賣 (占市值 0.03%) |
| Institutional ownership | 71.4% | n/a | n/a | 高 |
| Analyst mean target | 328.95 USD | +56% vs 現價 | n/a | 正面 |
| Beta | 2.22 | n/a | 約 1.2 | 高波動 |
| EPS surprise, last quarter | +6.2% | 近八季皆正向 | n/a | 優 |

## Red flags
- 負債急增: 2026-04 至 2026-07 總負債由 12.35B 增至 38.35B USD (+26.0B), 利息費用季增約 2.2 倍, 工具無法解釋, 需優先於 10-Q 確認。
- 現金轉換下降: 2026-07 季 OCF 24.08B USD (前季 50.34B), FCF/NI TTM 0.66x, 低於 0.9 健康門檻。
- 應收與存貨快速累積: AR QoQ +55%、存貨 QoQ +22%, DSO 約 60 天、存貨天數約 119 天。
- GAAP 獲利含非經常收益: 2026-07 季 unusual items 7.77B USD, 季度 GAAP EPS 2.46 與調整後 2.22 存在差異, 獲利品質需以 normalized 數字驗證。
- 內部人大額賣出: 近 6 個月約 1.37B USD、6.20M 股, 無公開市場買入; 董事 Mark Stevens 占大部分。
- 股利與現金分配資料矛盾: 2026-07 季現金股利 6.05B USD 異常; info 股利欄位彼此不一致; info freeCashflow (41.8B) 與季度推算 (127.0B) 不符。
- 治理風險評分: board risk 10 (滿分 10), overall risk 8。
- 估值偏高指標: P/S 16.8x、P/B 22.2x、P/FCF 約 40x; 估值支撐主要依賴 forward EPS 翻倍的預期。
- 高波動: beta 2.22, 股價目前低於 50 日均線約 5.2%, 距 52 週高點約 13.3%。
- 資料缺口 (DATA_UNAVAILABLE): 公司財測/指引、分部營收、FY22 完整財務、季度 YoY 歷史 (2025-04 以前季度為 null)、利息費用與負債明細、價格快照時點。

FUNDAMENTALS REPORT COMPLETE
