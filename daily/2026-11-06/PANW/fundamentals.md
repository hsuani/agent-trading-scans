# Fundamentals — PANW as of 2026-11-06

資料截至 2026-11-05 (fast_info 快取時間 2026-11-05 14:30 UTC), 未見 2026-11-06 之後的資料; 下次財報 2026-11-18 在 DATE 之後, 屬未來事件。

## Executive summary
PANW 的營收動能強勁 (FY26 營收 11.48B USD, YoY +24.5%, Q4 YoY +34.4%), 現金流也維持高水準 (FY26 FCF 4.11B USD, FCF margin 35.8%)。但 GAAP 獲利大幅惡化 (FY26 GAAP EPS 0.40 vs FY25 1.60, Q4 GAAP 淨損 -282M USD), 且 FY26 出現大型併購 (商譽由 4.57B 增至 22.01B USD、股本由 667.9M 股增至 815M 股), 使每股盈餘與資本結構的可比性下降。估值為 forward P/E 約 71x、P/S 約 24.8x, 相對一般大型資安軟體估值偏高 (sector median 為估計值), 基本面面的估值吸引力偏低。

## Revenue & profitability
單位: USD (B = 十億美元, M = 百萬美元)。

| 年度 (FYE 7 月) | Revenue (B) | YoY | Gross margin | Operating margin (GAAP) | Net margin (GAAP) | Diluted EPS (GAAP) |
|---|---|---|---|---|---|---|
| FY23 | 6.89 | n/a | 72.3% | 5.6% | 6.4% | 0.64 |
| FY24 | 8.03 | +16.5% | 74.3% | 8.5% | 32.1%* | 3.64 |
| FY25 | 9.22 | +14.9% | 73.4% | 13.5% | 12.3% | 1.60 |
| FY26 | 11.48 | +24.5% | 70.4% | 6.1% | 2.7% | 0.40 |

*FY24 淨利率受稅務利益 -1.59B USD (Tax Provision) 墊高, 非經常性, 不宜當作正常獲利水準。

- 營收 3 年 CAGR (FY23→FY26): 約 18.5%。FY26 成長加速, 季度趨勢為 Q1 FY26 2.47B、Q2 2.59B、Q3 3.00B、Q4 3.41B, Q4 YoY +34.4%, QoQ +13.6%。Q4 跳升與併購併表時點高度吻合 (由股本與商譽變化推斷, 資料未直接標示)。
- 毛利率連續兩年下滑: FY25 73.4% → FY26 70.4% (-3.1pp); Q4 毛利率 67.6%, 與 Q3 的 67.6% 持平, 低於 FY25 Q4 的 73.2%。Cost of revenue FY26 3.40B, YoY +38.9%, 超過營收成長。
- GAAP 營業利益 FY26 695M USD (YoY -44%), 但季度序列顯示 Q3 營業利益 -183M, Q4 +172M。
- GAAP 淨利 FY26 307M USD (YoY -73%); 季度 Q4 淨損 -282M USD, Q3 淨損 -177M USD。
- Adjusted EPS (yfinance earnings_dates, 非 GAAP): FY26 Q4 (報告於 2026-09-01) 1.02 vs 預估 0.98, beat +4.35%。
- 資料一致性提醒: Q4 FY26 的 Operating Income 列為 172M, 但 EBIT 列為 -269M, 稅前淨利 -269M; 兩者差約 -441M 的非營業項目未在資料中拆解, 需以 10-K / 10-Q 核對。
- 獲利能力: ROE (NI / 平均股東權益) 約 1.7%; ROIC 粗估約 2.2% (NOPAT 以營業利益 × (1-40%) 計, 平均投入資本 18.5B)。兩者均被併購後的大幅權益擴張與 GAAP 費用稀釋。
- 分部營收: 資料未提供分部拆分 (info.longBusinessSummary 僅列產品線: Prisma Access、Cortex XSIAM/XDR/XSOAR、Unit 42 等), 分部占比 n/a。

## Cashflow & balance sheet
單位: USD B。

現金流:
- FCF FY23-FY26: 2.63 / 3.10 / 3.47 / 4.11 B USD, FCF CAGR (FY23-26) 約 16%。
- FCF margin: FY23 38.2%、FY24 38.6%、FY25 37.6%、FY26 35.8%, 呈小幅下滑但仍在高檔。
- OCF FY26 4.55B USD, CapEx 0.44B USD (佔營收 3.8%, FY25 為 0.25B USD)。
- FCF / NI: FY26 為 13.4x (FY25 3.1x), 因 GAAP 淨利被 GAAP 費用壓低, 此比率失真, 不能單獨作為現金流品質的正面證據。以 FCF 對 SBC 看: SBC 1.77B USD, 佔營收 15.5%, 佔 FCF 43%, 是 FCF 的重要扣除項。
- 季度 FCF: Q1 FY26 1.69B、Q2 0.38B、Q3 0.79B、Q4 1.25B USD, 季度間波動大。

資產負債表 (2026-07-31):
- 現金與約當現金 2.51B USD; 含短期投資 Cash+STI 3.07B USD。
- 總債務 2.50B USD (FY25 為 0.34B USD), 其中長期債務 1.77B USD、Q3 的流動債務 0.16B USD。資料中的 interest expense 列為 0, 與債務增加不一致, 屬資料缺口。
- 淨現金: 以 BS 計約 0.57B USD (info 以 totalDebt 2.567B 計約 0.50B USD)。
- 流動比率 0.87, 速動比率 0.51, 營運資金 -1.28B USD; 流動負債中 Current Deferred Revenue 7.75B USD, 為訂閱制軟體的典型結構 (以預收收入支撐營運資金)。
- 權益比債務: 總債務 / 股東權益 約 9.1% (info debtToEquity 9.34, 單位為百分比); 總負債 / 股東權益 0.76x。
- 資產品質: 商譽 22.01B + 無形資產 7.02B = 29.03B USD, 佔總資產 48.46B USD 的 59.9%; 有形帳面價值 TBV 為 -1.54B USD。FY25 TBV 為 +2.49B USD。
- 股東權益 27.49B USD (FY25 7.82B USD), 增加主要來自股票對價 (Capital Stock 由 5.29B 增至 24.77B USD)。

## Capital allocation & insider signal
資本配置:
- 股利: 無 (dividendYield 0)。
- 買回: FY26 買回股票 1.00B USD (FY25 為 0, FY24 0.57B, FY23 0.27B); 占 FY26 FCF 24%。
- 併購: FY26 Purchase of Business 現金支出 4.66B USD (FY25 1.05B USD); 加上股票對價, 為 FY26 最主要的資本配置動作。資料未標示被併標的, 由商譽與股本變化推斷為大型收購。
- 股本: 期末普通股 815M 股 vs FY25 667.9M 股, 年增約 22%; 稀釋後平均股數 764M vs 709.3M, 年增 7.7%。買回金額未能抵銷股本擴張。
- CapEx 占營收 3.8%, 為輕資產模式。

內部人交易 (以 2026-05-05 至 2026-11-05 為 6 個月窗口):
- 共 20 筆公開市場賣出, 合計約 54.4M USD, 約 173k 股。
- 賣出金額前三名: Klarich Lee 16.3M、Goetz James Joseph 13.1M、Golechha Dipak 12.2M USD。
- 窗口內 0 筆公開市場買入。
- 規模: 54.4M USD 占市值 (以 348.04 × 818.4M 股 ≈ 284.9B USD 計) 約 0.02%, 數量級很小。
- 2026-03-27 CEO Nikesh Arora 買入 10.0M USD (146.87-147.48 USD/股), 在窗口之外, 但為近一年唯一的重要公開市場買入。
- 大量 Stock Award (2026-10-30 多名高管) 屬例行股權授予, 非市場交易。
- 機構持股 83.7%, 內部人持股 0.63%。
- 治理風險分數 (yfinance, 1-10, 數字越高風險越大): overall 9、compensation 10、board 9、shareholder rights 9、audit 1。薪酬風險評分最高, 需留意。

## Valuation
價格基準: fast_info 最新價 348.04 USD (快取 2026-11-05)。info 的 marketCap 259.65B USD 與 forwardPE 65.0x 對應約 317 USD/股 (較舊的價格基準), 本報告統一以 348.04 USD 重算。

| 指標 | 數值 | 計算 / 來源 |
|---|---|---|
| Trailing P/E | 約 870x | 348.04 / GAAP EPS 0.40 (info 顯示 793x 為舊價格基準); 不具參考性 |
| Forward P/E | 約 71x | 348.04 / forwardEps 4.88 (info 顯示 65.0x) |
| P/S (TTM) | 約 24.8x | 市值 284.9B / Revenue 11.48B (info 22.6x 為舊基準) |
| EV/Revenue | 約 24.8x | EV ≈ 284.9B + 2.50B 債 - 3.07B 現金 ≈ 284.3B |
| EV/EBITDA | 約 204x (FY26 EBITDA 1.39B USD); info 182x (TTM EBITDA 1.56B USD) | GAAP EBITDA 受併購費用影響 |
| P/FCF | 約 69x | 市值 284.9B / FCF 4.11B |

- 分析師: 50 位, 推薦 buy, 平均目標價 398.52 USD (約較現價 +14.5%)。
- 價格位置: 52 週區間 139.57-432.33 USD, 現價距 52 週高點 -19.5%; 距 50 日均線 372.17 USD 為 -6.5%; 高於 200 日均線 272.27 USD 約 +27.9%。Beta 0.97。
- 與同業比較: 資料未提供 sector median, 以下為估計值 (非工具輸出): 大型資安軟體 forward P/E 約 40x、P/S 約 12x、P/FCF 約 35x、非 GAAP 營業利益率約 28%、毛利率約 78%。PANW 以 GAAP 計算的毛利率與獲利率均明顯低於估計中位數, 但 forward P/E 與 P/S 皆約為估計中位數的 1.8-2 倍。

## Key catalysts
- 下次財報: 2026-11-18 (yfinance 時間 21:00 UTC, 即美股盤後), 距 DATE 12 天。Consensus adjusted EPS 0.97 USD。
- 歷史: yfinance 資料內的 24 個已報告季度, adjusted EPS 全部優於預估, 平均 surprise 約 +8%; 最近一季 (2026-09-01) +4.35%。
- 營收動能: Q4 FY26 YoY +34.4% 是否在併購併表後延續, 為下一季核心觀察點。
- 毛利率: 需確認 70.4% 的下滑來自併購攤銷 / 整合成本, 或是產品組合與定價壓力。
- 指引 (guidance): 工具資料未提供 management guidance, 此項 n/a。
- 分部: 分部營收 n/a。
- 整合與槓桿: 2.5B USD 債務與 29.0B USD 無形資產的減損風險 (商譽佔總資產 60%) 為中期關注點。

## Metrics table
單位: 營收與市值 (USD B); 比率 (%, x)。

| Metric | Latest (FY26 或 2026-11-05) | YoY | Sector median (estimate, 非工具資料) | Verdict |
|---|---|---|---|---|
| Revenue (USD B) | 11.48 | +24.5% | n/a | 強 |
| Q4 Revenue (USD B) | 3.41 | +34.4% | n/a | 強 (含併購效果) |
| Gross margin (GAAP) | 70.4% | -3.1pp | 約 78% | 弱 |
| Operating margin (GAAP) | 6.1% | -7.4pp | 約 28% (non-GAAP) | 弱 |
| Net margin (GAAP) | 2.7% | -9.6pp | 約 10% | 弱 |
| Diluted EPS (GAAP, USD) | 0.40 | -75% | n/a | 弱 |
| ROE | 1.7% | n/a | 約 10% | 弱 |
| ROIC (粗估) | 約 2.2% | n/a | 約 10% | 弱 |
| FCF (USD B) | 4.11 | +18.5% | n/a | 強 |
| FCF margin | 35.8% | -1.9pp | 約 25% | 強 |
| FCF / NI | 13.4x | 失真 | >0.9 健康 | 不具參考性 |
| SBC / revenue | 15.5% | 約 +1.6pp (FY25 14.0%) | 約 12% | 偏高 |
| Net cash (USD B, BS) | 約 +0.57 | 由 FY25 淨負債 (-) 轉為淨現金 | n/a | 中性 |
| Total debt (USD B) | 2.50 | +640% (FY25 0.34) | n/a | 需留意 |
| Current ratio | 0.87 | FY25 0.94 | 約 1.5 | 偏弱 (訂閱預收結構) |
| Debt / Equity | 9.1% | n/a | 約 20% | 健康 |
| Goodwill+Intangibles / Assets | 59.9% | 由 FY25 22.6% 升 | 約 30% | 偏高 |
| Tangible BV (USD B) | -1.54 | 由 +2.49 轉負 | n/a | 弱 |
| CapEx / revenue | 3.8% | +1.1pp | 約 3-5% | 中性 |
| Buyback (USD B) | 1.00 | 由 0 增加 | n/a | 不足以抵銷稀釋 |
| Shares outstanding (M) | 815 | +22% | n/a | 稀釋 |
| Insider net sales 6mo (USD M) | 54.4 (0 買入) | n/a | n/a | 小幅賣出, 規模 0.02% 市值 |
| P/E forward (x) | 約 71 | n/a | 約 40 | 偏貴 |
| P/S TTM (x) | 約 24.8 | n/a | 約 12 | 偏貴 |
| P/FCF (x) | 約 69 | n/a | 約 35 | 偏貴 |
| EV/EBITDA (x) | 約 204 (GAAP) | n/a | 約 40 (non-GAAP) | 不具參考性 (GAAP EBITDA 低) |
| Adj. EPS beat rate (24Q) | 24/24 beat | n/a | 約 75% | 強 |

## Red flags
- GAAP 獲利大幅惡化: FY26 淨利 307M USD (YoY -73%), Q4 淨損 -282M USD, Q3 淨損 -177M USD, GAAP 毛利率下滑 3.1pp。
- Q4 FY26 營業利益 (172M) 與 EBIT (-269M) 不一致, 約 -441M 非營業項目需以財報核對, 資料單獨不足以判定。
- 大型併購 (FY26 現金 4.66B USD + 股票對價, 商譽增加 17.4B USD) 使前後期不可比; 有形權益轉負 (TBV -1.54B USD), 商譽減損風險。
- 債務由 0.34B 增至 2.50B USD, 但 interest expense 為 0, 與債務規模不符, 需確認利息成本與債務條款。
- 股本擴張 22%, SBC 1.77B USD (佔 FCF 43%), 買回 1.0B USD 未抵銷稀釋。
- 估值偏高: forward P/E 約 71x、P/S 約 24.8x、P/FCF 約 69x。
- 治理與薪酬風險評分高 (compensation 10/10, overall 9/10)。
- 價格 348.04 USD 低於 50 日均線 (-6.5%), 距 52 週高點 -19.5%; 近期內部人在 347-396 USD 區間持續賣出。
- 資料缺口: fast_info 的 50/200 日均線與市值欄位為 null (以 info 替代); Yahoo cookie/crumb 多次失敗; info 與 fast_info 價格基準不一致; 分部營收、管理層指引、sector median 均為 n/a 或估計值。

FUNDAMENTALS REPORT COMPLETE
