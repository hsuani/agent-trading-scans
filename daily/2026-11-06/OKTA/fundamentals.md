# Fundamentals — OKTA as of 2026-11-06

> 資料說明: 數據快照為 2026-11-05 約 14:30 UTC (盤中, 約開盤後 7 分鐘)。分析基準日 2026-11-06, 未見 2026-11-06 之後的資料。FY 定義: Okta 會計年度止於 1 月 31 日, FY26 = 2026-01-31 年度, Q2 FY27 = 2026-07-31 季度。所有金額為 USD, 以 M (百萬) 或 B (十億) 標示。

## Executive summary
OKTA 財務體質已由虧轉盈且為淨現金 (現金及短期投資 2.30B、總債務 0.05B), TTM 自由現金流 959M (FCF margin 31.2%), 但營收成長由 FY24 的 21.8% 持續降至 Q2 FY27 的 10.6%, 且 SBC 佔營收 16.4% (TTM), 扣除 SBC 後的 FCF 僅約 456M。估值方面, GAAP 追溯 P/E 104.3x、EV/EBITDA 約 68x (自算), 以 non-GAAP 前瞻 P/E 39.6x 計算仍屬高估值區間; 過去 6 個月內部人合計出售約 46.5M USD, 無公開市場買進。今日盤中股價較前收 191.05 下跌 9.3%, 原因未在工具資料中找到, 需後續確認。

## Revenue & profitability

**年度趨勢 (USD M)**

| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Total Revenue | 1,858 | 2,263 | 2,610 | 2,919 |
| YoY | n/a | +21.8% | +15.3% | +11.8% |
| Gross Profit | 1,312 | 1,682 | 1,992 | 2,258 |
| Gross margin | 70.6% | 74.3% | 76.3% | 77.4% |
| Operating income (GAAP, as reported) | -812 | -516 | -74 | 149 |
| Operating margin | -43.7% | -22.8% | -2.8% | 5.1% |
| Net income | -815 | -355 | 28 | 235 |
| Net margin | -43.9% | -15.7% | 1.1% | 8.0% |
| Diluted EPS (USD) | -5.16 | -2.17 | 0.06 | 1.31 |

- 營收 CAGR: FY23→FY26 三年 CAGR 約 16.3%; FY24→FY26 兩年 CAGR 約 13.6%。FY22 資料為 null, 無法計算 4-5 年 CAGR。
- 成長減速: 21.8% → 15.3% → 11.8%, 且 Q2 FY27 YoY 為 10.6%, 減速趨勢未止。
- 季度營收 (USD M): Q2 FY26 728 / Q3 FY26 742 / Q4 FY26 761 / Q1 FY27 765 / Q2 FY27 805。Q2 FY27 季增 +5.3%。Q1 FY26 (2025-04) 資料為 null, 無法計算 Q1 FY27 YoY。
- TTM 營收 3,073M (與 info.totalRevenue 3,072,999,936 吻合)。
- 營收結構: `longBusinessSummary` 列出 SSO、Adaptive MFA、Universal Directory、Identity Governance、Auth0 CIAM、AI Agents 等產品線, 但 info 與 financials 均未提供分部營收, 分部占比 n/a。

**季度獲利能力**

| 季度 | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | Q2 FY27 |
|---|---|---|---|---|---|
| Gross margin | 76.9% | 77.1% | 77.9% | 77.8% | 79.6% |
| Operating margin (GAAP) | 5.6% | 3.1% | 6.0% | 7.3% | 13.3% |
| Net margin | 9.2% | 5.8% | 8.3% | 9.7% | 14.4% |

- Q2 FY27 營業利益率 13.3%, 較去年同期 +7.7 pp, 為連續擴張。
- ROE: info.returnOnEquity 4.3%, 與 TTM NI 296M / 權益 6,973M 約 4.2% 吻合。
- ROIC (估算): TTM 營業利益 232M × (1-21%) ÷ 投入資本約 4,727M (權益 6,973 + 債務 53 - 現金 2,299) ≈ 3.9%。
- 獲利品質提醒: FY26 稅前利潤 255M 中, 利息收入約 106M (約 42%), 且 FY26 稅率僅 7.9%, Q2 FY27 稅率為 7.9%。GAAP 獲利部分來自利息收入與低稅率, 而非純營業槓桿。

## Cashflow & balance sheet

**現金流 (USD M)**

| 指標 | FY23 | FY24 | FY25 | FY26 | TTM (Q3 FY26-Q2 FY27) |
|---|---|---|---|---|---|
| Operating cash flow | 86 | 512 | 750 | 884 | n/a (季度合計 ~974) |
| Capex | -23 | -24 | -20 | -21 | 季度合計 -27 |
| Free cash flow | 63 | 488 | 730 | 863 | 959 |
| FCF margin | 3.4% | 21.6% | 28.0% | 29.6% | 31.2% |
| FCF / NI | n/m | n/m | 26.1x | 3.67x | 3.24x |
| SBC | 677 | 684 | 565 | 544 | 503 |
| SBC % revenue | 36.4% | 30.2% | 21.6% | 18.6% | 16.4% |
| FCF 扣除 SBC | -614 | -196 | 165 | 319 | 456 |

- FCF/NI 遠高於 0.9 的健康門檻, 但分母 NI 受利息收入與低稅率提升, 分子 FCF 受 SBC (非現金費用) 推升, 單看此比率會高估現金流品質。扣除 SBC 後 TTM FCF margin 約 14.8%。
- FY23 營業現金流 86M 與 FY26 884M 相比明顯改善, 由於 SBC 占比下降與營收增長。
- Capex 極低 (FY26 占營收 0.7%), 資本密集度低。

**資產負債表 (2026-07-31, USD M)**

| 項目 | 數值 | 說明 |
|---|---|---|
| 現金及短期投資 | 2,299 | 與 info.totalCash 2,299M 吻合 |
| 總債務 | 53 | 自 2026-01 的 422 降至 53 |
| 淨現金 | 約 2,246 | 2,299 - 53, 自算 |
| 股東權益 | 6,973 | |
| 有形帳面價值 | 1,406 | |
| 流動資產 / 流動負債 | 3,089 / 2,025 | |
| 流動比率 | 1.53 | 與 info.currentRatio 1.525 吻合 |
| 速動比率 | 1.38 | info.quickRatio |
| 債務/權益 | 0.8% | info.debtToEquity 0.76 (百分比格式) |
| 流動遞延收入 | 1,751 | 佔流動負債約 86%, 為主要負債來源 |

- 負債結構以遞延收入為主, 有息債務已大幅清償: 2025-10 季度償還約 510M, 2026-07 總債務降至 53M。
- 遞延收入 (流動) 同比 +13.0% (1,751 vs 1,550), 為營收可見度的正面訊號。

## Capital allocation & insider signal

**資本配置**
- 股息: 無 (dividendRate 0)。
- 買回: FY26 買回 -73M; FY27 上半年 (Q1 -248M, Q2 -124M) 合計約 -372M。
- 股本: 普通股 177.36M (2026-01) → 174.82M (2026-07), 半年減少 1.4%。稀釋加權股數 Q2 FY27 178.8M vs Q2 FY26 181.0M, 同比 -1.2%。買回已超過 SBC 稀釋, 但 SBC 仍為主要成本。
- 債務: 優先清償可轉債類債務, 利息費用趨近於 0 (Q2 FY27 利息費用 0)。
- 資本支出: 極低, 無重大擴產。

**內部人交易 (6 個月窗口: 2026-05-05 至 2026-11-05)**

公開市場賣出 (Sale) 共 11 筆, 合計約 46.46M USD (約 312K 股), 占市值約 0.15%:

| 日期 | 內部人 | 職位 | 股數 | 金額 (USD M) |
|---|---|---|---|---|
| 2026-05-07 | Schwartz | Officer | 6,377 | 0.49 |
| 2026-05-18 | Archambeau | Director | 2,500 | 0.21 |
| 2026-06-02 | Schwartz | Officer | 24,971 | 3.35 |
| 2026-06-08 | Tighe | CFO | 65,000 | 7.62 |
| 2026-06-18 | Kelleher | President | 3,977 | 0.45 |
| 2026-06-22 | Schwartz | Officer | 2,463 | 0.30 |
| 2026-07-08 | McKinnon | CEO | 68,936 | 10.11 |
| 2026-09-02 | Tighe | CFO | 80,000 | 12.88 |
| 2026-09-11 | Kelleher | President | 2,549 | 0.43 |
| 2026-09-18 | Kelleher | President | 6,395 | 1.17 |
| 2026-09-22 | McKinnon | CEO | 48,822 | 9.45 |

- 窗口內公開市場買進: 0 筆。最近一筆買進為 2026-04-16 Schellhase (董事) 約 0.27M USD, 已超出窗口。
- 淨額: 約 -46.5M USD。賣方以 CEO 與 CFO 為主 (合計約 40.0M, 佔 86%)。是否為 10b5-1 預定計畫或稅務代扣, 工具資料無法判定。
- 占比: 市值 30.28B, 賣出金額占 0.15%, 幅度有限, 但方向一致 (連續賣出, 無買進)。
- 持股: 內部人持股 0.51%, 機構持股 98.7%, 空單佔流通股 4.66% (6.96M 股, 約 1.9 天覆蓋)。

## Valuation

**股價與市值**
- 現價 173.215 (2026-11-05 盤中); 前收 191.05; 日內 -9.33%, 日內區間 173.00-184.53。
- 52 週區間 62.66-235.00, 現價距 52 週高點 -26.3%。50 日均線 196.16 (現價 -11.7%), 200 日均線 125.98 (現價 +37.5%)。
- 市值 30.28B (= 現價 × 普通股 174.82M)。
- 注意: info.sharesOutstanding 為 167.14M, 與 impliedSharesOutstanding 174.82M 不一致, 本報告採用 174.82M。

**估值倍數 (自算, USD)**

| 指標 | 數值 | 計算 |
|---|---|---|
| Trailing P/E (GAAP, TTM EPS 1.66) | 104.3x | info.trailingPE |
| Forward P/E (forwardEps 4.38, non-GAAP) | 39.6x | info.forwardPE |
| Current-year P/E (epsCurrentYear 3.93) | 44.1x | 173.215 ÷ 3.929 |
| EV (自算) | 28.04B | 市值 30.28B - 淨現金 2.25B |
| EV/Sales (TTM 3.07B) | 9.1x | 28.04 ÷ 3.07 |
| EV/EBITDA (TTM 季度 EBITDA 412M) | 約 68x | 28.04B ÷ 0.412B |
| P/S (TTM) | 9.9x | info.priceToSalesTrailing12Months 9.85 |
| P/FCF (TTM 959M) | 31.6x | 30.28 ÷ 0.959 |
| EV/FCF (TTM) | 29.2x | 28.04 ÷ 0.959 |
| P/B | 4.3x | info.priceToBook |
| PEG | 1.36 | info.pegRatio |

- 分析師: 43 位, 評等均值 1.66 (Buy), 目標價均值 214.72 (較現價 +24.0%), 最高 250 (+44.3%), 最低 127 (-26.7%)。

**相對同業 (sector median 為粗估, 非工具資料)**
- Software-Infrastructure 中位數 (估計) 的 forward P/E 約 30-35x, EV/Sales 約 6-8x, P/FCF 約 25-30x, Gross margin 約 75%。OKTA 的 forward P/E、P/FCF 高於估計中位數; Gross margin 高於中位數。

## Key catalysts
- 下次財報: 2026-12-01 (Q3 FY27), isEarningsDateEstimate = False。EPS 共識 (non-GAAP) 0.93。
- 最近一季 (Q2 FY27, 2026-08-26 公告): non-GAAP EPS 實際 1.05 vs 共識 0.96, 超出 +8.9%; GAAP 稀釋 EPS 0.65。
- 近 7 季 EPS 超出共識幅度: 平均約 +7.9%, 連續 7 季正超出。
- 正式財測 (guidance): 工具資料無法取得, n/a。
- 今日 -9.3% 下跌原因: 工具資料中無新聞或公告, 需確認是否與產品、競爭對手、監管或同業事件有關。

## Metrics table
| Metric | Latest | YoY | Sector median (估計) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, USD B) | 3.07 | +10.6% (Q2 FY27) | 約 10-15% | 中等, 持續減速 |
| 營收成長 (FY26, %) | 11.8% | FY25 15.3% | 約 12% | 中等偏弱 |
| Gross margin (Q2 FY27) | 79.6% | +2.7 pp | 約 75% | 優 |
| Operating margin (Q2 FY27, GAAP) | 13.3% | +7.7 pp | 約 5-10% | 良, 快速改善 |
| Net margin (TTM) | 9.6% | 由負轉正 | n/a | 含利息收入與低稅率 |
| ROE (TTM) | 4.3% | n/a | 約 10% | 偏弱 |
| ROIC (估算) | 約 3.9% | n/a | 約 8-10% | 偏弱 |
| FCF margin (TTM) | 31.2% | 較 FY25 +3.2 pp | 約 20% | 優 |
| FCF 扣除 SBC margin (TTM) | 14.8% | n/a | 約 10% | 中等 |
| FCF / NI (TTM) | 3.24x | n/a | n/a | 高估 (NI 偏低) |
| SBC % revenue (TTM) | 16.4% | -5.2 pp (FY25→TTM) | 約 10% | 偏高 |
| 淨現金 (USD B) | 2.25 | n/a | 視情況 | 優 |
| 流動比率 | 1.53 | n/a | 約 1.5 | 中性 |
| 債務/權益 | 0.8% | 大幅下降 | 約 30% | 優 |
| Trailing P/E (GAAP) | 104.3x | n/a | 約 n/a (多數負值) | 偏高 |
| Forward P/E | 39.6x | n/a | 約 30-35x | 偏高 |
| EV/EBITDA (TTM, 自算) | 約 68x | n/a | 約 25-30x | 偏高 |
| P/FCF (TTM) | 31.6x | n/a | 約 25-30x | 偏高 |
| EV/Sales (TTM) | 9.1x | n/a | 約 6-8x | 偏高 |
| 內部人淨買賣 (6 個月) | -46.5M USD | n/a | n/a | 淨賣出, 占市值 0.15% |

## Red flags
- 營收成長持續減速: 21.8% → 15.3% → 11.8% → Q2 FY27 10.6%。
- SBC 偏高: FY26 SBC 544M (18.6% 營收); TTM 扣除 SBC 後 FCF margin 約 14.8%, 而非表面的 31.2%。
- GAAP 獲利品質: FY26 稅前利潤中約 42% 來自利息收入, 稅率僅 7.9%, 獲利基礎薄。
- GAAP 與 non-GAAP 差距大: Q2 FY27 GAAP EPS 0.65 vs non-GAAP 1.05。
- 內部人連續賣出: 6 個月內 CEO 與 CFO 合計賣出約 40M USD, 窗口內無公開市場買進。
- 估值偏高: 前瞻 P/E 39.6x, EV/Sales 9.1x, P/FCF 31.6x。
- 今日 -9.3% 跌幅, 現價距 52 週高點 -26%, 原因未明。

FUNDAMENTALS REPORT COMPLETE
