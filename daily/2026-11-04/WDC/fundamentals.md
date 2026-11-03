# Fundamentals — WDC as of 2026-11-04

> 資料來源：`pipeline/tools/yf WDC` 各子命令（info、fast_info、financials、quarterly_fin、balance_sheet、quarterly_bs、cashflow、quarterly_cf、earnings_dates、insider、major_holders、inst_holders）。部分 yfinance 網路呼叫出現 cookie/crumb ConnectionError，但仍回傳資料；fast_info 的價格來源為 `source: cache`（cnyes feed，cached_at 2026-11-03T14:00 UTC），屬正常快取。
> 單位：本報告僅涉及 USD，以 B（十億）與 M（百萬）標示，未混用億。

## Executive summary
WDC 在 FY2026（財年截至 2026-07-03）與 FY27 Q1（季末 2026-10-02，已於 2026-10-22 公布）營運大幅改善：FY27 Q1 營收 4.38B USD、毛利率 57.8%、調整後 EPS 4.64 優於共識 4.10，財務槓桿已降至近乎零淨負債（淨現金約 0.53B USD）。估值需分開看：GAAP trailing P/E 11.9x 受 FY26 一次性處分利益 6.5B USD 扭曲，以調整後 TTM EPS 13.05 計算約 25.9x，EV/TTM 營業 EBITDA 約 20.7x，對 HDD 週期股而言並不算便宜；股價自 52 週高點 799.87 下跌 57.7%、目前 338.59 低於 50 日與 200 日均線，市場明顯已在反映高波動與循環風險。內部人於近 6 個月合計賣出約 27.6M USD、無公開市場買進，股本仍較一年前增加約 7%。本段僅為基本面評估，不構成交易建議。

## Revenue & profitability

**年度趨勢（USD B，yfinance annual）**

| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 營收 Total Revenue | 6.255 | 6.317 | 9.520 | 12.919 |
| 營收 YoY | n/a | +1.0% | +50.7% | +35.7% |
| 毛利 Gross Profit | 1.391 | 1.773 | 3.692 | 6.311 |
| 營業利益 Total Operating Income As Reported | -0.548 | -0.403 | 2.334 | 4.453 |
| 淨利 Net Income | -1.684 | -0.798 | 1.861 | 9.298 |
| 正規化淨利 Normalized Income | -0.794 | -0.393 | 2.112 | 3.781 |
| 稀釋 EPS (GAAP) | -5.44 | -1.72 | 5.14 | 24.28 |

- 營收 3 年 CAGR（FY23→FY26）約 27.4%。FY22 數據為 null，無法計算 5 年 CAGR。
- 驗算：FY26 淨利 9.298B ÷ 稀釋股數 383M ≈ 24.28，與工具 Diluted EPS 一致。

**利潤率趨勢**

| 指標 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| 毛利率 | 22.2% | 28.1% | 38.8% | 48.9% |
| 營業利益率（as reported） | -8.8% | -6.4% | 24.5% | 34.5% |
| GAAP 淨利率 | -26.9% | -12.6% | 19.5% | 72.0% |
| 正規化淨利率 | -12.7% | -6.2% | 22.2% | 29.3% |

FY26 GAAP 淨利率 72.0% 主要來自 Gain On Sale Of Business 6,498M USD，yfinance 未揭露該處分交易的性質，需以 10-K 確認。正規化淨利率 29.3% 才較能代表經常性獲利能力。

**季度趨勢（USD M）**

| 季度 | 營收 | 毛利率 | 營業利益率（as reported） | GAAP 稀釋 EPS | 調整後 EPS（earnings_dates） |
|---|---|---|---|---|---|
| 2025-09（FQ1 FY26） | 2,818 | 43.5% | 28.1% | 3.07 | 1.78 |
| 2025-12（FQ2 FY26） | 3,017 | 45.7% | 30.1% | 4.73 | 2.13 |
| 2026-03（FQ3 FY26） | 3,337 | 50.2% | 35.7% | 8.20 | 2.72 |
| 2026-06（FQ4 FY26） | 3,747 | 54.1% | 41.7% | 8.21 | 3.56 |
| 2026-09（FQ1 FY27） | 4,381 | 57.8% | 46.7% | 4.63 | 4.64 |

- FQ1 FY27 營收 YoY +55.5%、QoQ +16.9%；毛利率較一年前提升約 14.3 個百分點。
- FQ1 FY27 淨利 1,779M ÷ 稀釋股數 384M ≈ 4.63，與 GAAP EPS 一致。
- 調整後 EPS 與 GAAP EPS 於 FQ3、FQ4 差距很大，因一次性項目影響，需以調整後數字比較季度趨勢。

**成長與結構**：yfinance info 的 longBusinessSummary 列出產品線為內接式 HDD、資料中心硬碟與平台、外接硬碟、NAS 等，但工具未提供分部營收，segment mix 為 DATA_UNAVAILABLE。

## Cashflow & balance sheet

**現金流（USD M）**

| 指標 | FY23 | FY24 | FY25 | FY26 | FQ1 FY27 |
|---|---|---|---|---|---|
| 營業現金流 OCF | -408 | -294 | 1,691 | 3,929 | 1,604 |
| 資本支出 Capex | -821 | -487 | -412 | -418 | -227 |
| 自由現金流 FCF | -1,229 | -781 | 1,279 | 3,511 | 1,377 |
| FCF margin | n/a | n/a | 13.4% | 27.2% | 31.4% |
| FCF / GAAP NI | n/a | n/a | 0.69 | 0.38 | 0.77 |
| FCF / 正規化 NI | n/a | n/a | 0.61 | 0.93 | n/a |
| SBC | 318 | 295 | 265 | 204 | 79 |

- FY26 FCF 3,511M 與 quarterly FCF 合計（599 + 653 + 978 + 1,281）一致。
- FCF / GAAP NI 僅 0.38，是因 6.5B 處分利益計入 NI 而未產生現金；以正規化淨利計為 0.93，達健康水準（> 0.9）。
- TTM（FQ2 FY26 至 FQ1 FY27）FCF 4,289M，FCF margin 約 29.6%。

**資產負債表（USD M）**

| 指標 | FY25（2025-06） | FY26（2026-06） | FQ1 FY27（2026-09） |
|---|---|---|---|
| 現金及約當現金 | 2,114 | 1,579 | 1,314 |
| 總負債（Total Debt） | 4,711 | 1,052 | 789 |
| 淨負債（Net Debt） | 2,597 | -527（淨現金，由 cash - debt 推算） | -525（淨現金） |
| 總資產 | 14,002 | 13,861 | 14,239 |
| 股東權益 | 5,540 | 8,864 | 9,348 |
| 流動比率 | 1.08 | 1.33 | 1.43 |
| 負債 / 股東權益 | 0.85 | 0.12 | 0.08 |
| 存貨 | 1,291 | 1,511 | 1,781 |
| 應收帳款 | 1,486 | 2,026 | 2,232 |
| 商譽 | 4,319 | 4,321 | 4,321 |

- FY26 yfinance 的 Net Debt 欄位為 n/a，淨現金為本報告以 cash 減 total debt 推算。FY26 的 Long Term Debt 亦為 n/a，Total Debt 1,052M 可能僅為流動負債中的債務，需以 10-K 核對。
- 利息覆蓋率：FY26 營業利益 4,453M ÷ 利息費用 165M ≈ 27x。
- 應收帳款較一年前增加約 65%（2,232 vs 1,355），高於 FQ1 營收 YoY +55.5%，需留意；存貨較一年前增加約 28%。

## Capital allocation & insider signal

**資本配置**

- 庫藏股：FY26 回購 2,592M，FY25 僅 149M。FQ1 FY27 回購 1,001M。
- 股利：FY26 支付 184M（普通股 174M、特別股 10M），FY25 為 44M。info 的 dividendRate 為 0.70 USD/股，dividendYield 0.21%，payoutRatio 1.9%。股利相對 FCF 極為保守，FY26 FCF ÷ 股利約 19x。
- 回購 + 股利合計佔 FCF 比例：FY26 約 79%，FQ1 FY27 約 77%。
- 債務：FY26 償還 2,884M、發行 1,946M，淨償還 938M。FQ1 FY27 償還 1,170M、發行 900M。
- 股本（Ordinary Shares，單位 M）：FY24 343 → FY25 347 → FY26 361 → FQ1 FY27 374。FQ1 FY27 較 2025-09 的 349 增加約 7.2%；FY26 稀釋平均股數 383M，較 FY25 的 359M 增加約 6.7%。**在回購規模大的情況下股本仍上升，工具資料未揭露原因（可能為股權發行或其他股份來源），列為紅旗。**

**內部人交易（insider，統計區間 2026-05-04 至 2026-10-21）**

| 項目 | 數值 |
|---|---|
| 公開市場賣出（Sale）筆數 | 19 |
| 賣出合計金額 | 約 27.55M USD |
| 賣出股數 | 約 58,803 股 |
| 公開市場買進 | 0 筆 |
| 佔市值比例 | 約 0.02%（市值 126.7B USD） |
| 內部人持股比例 | 0.27%（heldPercentInsiders） |

- 主要賣出者：CEO Irving Tan 約 8.9M USD（2026-08-11，20,000 股，價格區間 441.48–447.18）；Brian Scott Davis 約 5.0M USD；Vidyadhara Gubbi 約 4.3M USD；董事 Martin Cole 約 3.9M USD；Cynthia Tregillis 約 2.6M USD；董事 Stephanie Streeter 約 2.5M USD；董事 Bruce Kiddoo 約 0.4M USD。
- 無公開市場買進。另有 8 筆 Stock Award（Grant）與 2 筆 Stock Gift，為非市場交易，本報告不計入買賣方向。
- 解讀：賣出金額相對市值極小，但多名高階主管與董事同時、持續賣出，且無買進，屬偏中性偏負面的訊號。是否為 10b5-1 計畫無法由工具判定。

**機構與空頭**

- 機構持股 88.4%（約 2,443 家機構）。前幾大：BlackRock 8.8%（季減 7.9%）、FMR 6.9%（季減 17.8%）、Vanguard 6.0%（季增 2.2%）、JPMorgan 4.5%、Capital World Investors 4.4%（季增 39.7%）、State Street 4.4%、Invesco 3.9%。
- 空頭：做空股數 19.45M，較前月 17.28M 增加約 12.5%；佔流通股 5.2%（shortPercentOfFloat）；shortRatio 2.15 天（資料日期 2026-10-15）。

## Valuation

**價格基準**：fast_info last_price 338.59 USD（cache，2026-11-03）。info 的 previousClose 366.11、fulldayPrice 350.49，且 bid 367.61 高於 ask 340.89，報價欄位不一致，故以快取 last_price 為準。該價格與 info 的 marketCap 126.74B（= 338.59 × 374.3M 股）吻合。

| 估值指標 | 數值 | 說明 |
|---|---|---|
| 市值 | 126.7B USD | info.marketCap |
| 企業價值 EV | 126.35B USD | info.enterpriseValue |
| Trailing P/E（GAAP） | 11.9x | trailingEps 28.43，含一次性利益，失真 |
| Trailing P/E（調整後） | 25.9x | 以調整後 TTM EPS 13.05（2.13+2.72+3.56+4.64）計 |
| Forward P/E（yfinance） | 8.4x | forwardEps 40.40，數值與季度共識不一致，需存疑 |
| P/E（Q2 共識年化） | 14.4x | 以 FQ2 EPS 估計 5.87 × 4 = 23.5 計 |
| P/S（TTM） | 8.75x | TTM 營收 14.48B |
| EV / TTM 營收 | 8.7x | |
| EV / TTM 營業 EBITDA | 20.7x | TTM 營業利益 5.707B + D&A 0.391B = 6.098B；EV 126.35B |
| P/FCF（TTM） | 29.6x | TTM FCF 4.289B |
| P/B | 13.5x | bookValue 24.995 USD/股 |

- 注意：yfinance 的 normalized EBITDA 在 FY26 與 FQ4 FY26 出現異常（FQ4 為 -3,095M），因其扣除方式與一次性項目互相抵銷，本報告改以營業利益加 D&A 計算。
- 同業中位數：工具未提供同業資料。以下為團隊估計值，非工具資料：HDD/儲存硬體 forward P/E 約 15–25x、EV/EBITDA 約 10–15x、P/S 約 2–4x。依此判斷，WDC 以 GAAP forward P/E 看似低估，但以調整後 TTM 與 EV/EBITDA 看則不便宜，取決於 FY27 盈餘能否延續。
- 股價表現：52 週高點 799.87、52 週低點 132.43、目前 338.59，較高點 -57.7%；50 日均線 419.04、200 日均線 419.56，目前價格分別低於 19.2% 與 19.3%。Beta 2.34，平均成交量 8.1M 股（10 日均量 9.3M）。
- 資料矛盾：forwardEps 40.40 與 FQ1 實際 4.64 加上 FQ2 共識 5.87 不符（前兩季合計僅 10.51），除非下半年 EPS 大幅跳升，否則 forward P/E 8.4x 不宜直接採用。

## Key catalysts

- 上一財報：2026-10-22 公布 FQ1 FY27，EPS 4.64 vs 共識 4.10，超出 +13.2%；營收 4.381B USD、毛利率 57.8%。
- 下一財報：2027-01-28（yfinance 日期，屬預估），FQ2 FY27 EPS 共識 5.87。
- 近 10 季 EPS 超預期 9 次（僅 2025-01 季略低 -2.7%），盈餘驚喜紀錄強。
- 股利：yfinance 列出 exDividendDate 為 2026-12-04，該日期晚於本報告基準日，為待確認的預定日期。
- 指引（guidance）：工具未提供公司文字指引，guidance 為 DATA_UNAVAILABLE。
- 業務分拆背景：依一般公開資訊，WDC 的 NAND 業務已於 2025 年分拆為 Sandisk，目前以 HDD 為核心；此背景非工具直接揭露，需以 10-K 核對。FY25 現金流中的 Sale of Business 401M、FY26 的 Gain on Sale of Business 6,498M，其交易細節需由公告確認。
- 股價催化：資料中心 HDD 需求與 AI 相關容量擴張是主要的營收動能；應收與存貨增速、股本增加與內部人持續賣出是需追蹤的變數。
- 量子運算合作（Open Quantum Design）見於 info 業務描述，對營收影響不明，視為非核心。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD B) | 14.48 | FQ1 FY27 YoY +55.5% | 估計 ~ 中高個位數至高成長 | 優 |
| 毛利率 (FQ1 FY27) | 57.8% | +14.3 pp | 估計 ~ 40% | 優 |
| 營業利益率 as reported (FY26) | 34.5% | +10.0 pp (FY25 24.5%) | 估計 ~ 15–20% | 優 |
| GAAP 淨利率 (FY26) | 72.0% | 含一次性利益 | n/a | 失真，不採用 |
| 正規化淨利率 (FY26) | 29.3% | FY25 22.2%（+7.1 pp） | 估計 ~ 15% | 優 |
| ROE（平均權益，GAAP） | 129% | FY25 22.4% | n/a | 失真，不採用 |
| ROE（正規化） | 52.5% | FY25 22.4% | 估計 ~ 15% | 優 |
| ROIC（25% 稅率假設） | 約 33.5% | FY25 約 12.3% | 估計 ~ 10% | 優 |
| FCF margin (FY26) | 27.2% | FY25 13.4%（+13.8 pp） | 估計 ~ 10–15% | 優 |
| FCF / GAAP NI (FY26) | 0.38 | FY25 0.69 | > 0.9 為健康 | 弱（受一次性利益影響） |
| FCF / 正規化 NI (FY26) | 0.93 | FY25 0.61 | > 0.9 為健康 | 中性偏優 |
| 淨負債 (FY26, USD B) | -0.527（淨現金） | FY25 +2.597 | 估計 ~ 中性 | 優 |
| 流動比率 (FQ1 FY27) | 1.43 | FY25 1.08 | 估計 ~ 1.5 | 中性 |
| 負債 / 股東權益 (FQ1 FY27) | 0.08 | FY25 0.85 | 估計 ~ 0.5 | 優 |
| 利息覆蓋率 (FY26) | 約 27x | n/a | 估計 ~ 8x | 優 |
| 資本支出 / 營收 (FY26) | 3.2% | FY25 4.3% | 估計 ~ 5–8% | 優 |
| 回購 + 股利 / FCF (FY26) | 79% | FY25 約 15% | n/a | 中性 |
| 股息殖利率 | 0.21% | 5 年平均 2.55% | 估計 ~ 0.5–1.5% | 中性（股息極低） |
| 股本 YoY（Sep 2026 vs Sep 2025） | 374M | +7.2% | 估計 ~ 0–2% | 負面 |
| 內部人淨買賣（6 個月） | 賣出約 27.55M USD，買進 0 | n/a | n/a | 負面 |
| 空頭比例（佔流通股） | 5.2% | 空單 +12.5% MoM | 估計 ~ 2–4% | 中性偏負 |
| Beta | 2.34 | n/a | 估計 ~ 1.2–1.5 | 高波動 |
| P/E trailing（GAAP） | 11.9x | n/a | n/a | 失真 |
| P/E trailing（調整後） | 25.9x | n/a | 估計 ~ 20x | 中性偏貴 |
| P/E forward（yfinance） | 8.4x | 數據存疑 | 估計 ~ 20x | 需存疑 |
| P/E 年化（Q2 共識 × 4） | 14.4x | n/a | 估計 ~ 20x | 中性偏優 |
| EV / TTM 營業 EBITDA | 20.7x | n/a | 估計 ~ 10–15x | 偏貴 |
| P / FCF (TTM) | 29.6x | n/a | 估計 ~ 15–20x | 偏貴 |
| P / S (TTM) | 8.75x | n/a | 估計 ~ 2–4x | 偏貴 |
| P / B | 13.5x | n/a | 估計 ~ 2–3x | 偏貴（一次性利益與股東權益變動影響） |
| 股價距 52 週高點 | -57.7%（338.59 vs 799.87） | n/a | n/a | 負面（高波動） |

註：Sector median 欄位為團隊估計值，非工具資料；n/a 表示工具欄位缺失或不適用。

## Red flags
- FY26 GAAP 淨利 9.3B 中含 6.5B 處分利益，GAAP 的 trailing P/E、ROE、淨利率均失真，不宜單獨引用。
- 股本於回購 2.6B USD 的同時增加約 7%（FY26 稀釋股數 +6.7%），原因工具未揭露，需追查。
- 內部人 6 個月合計賣出約 27.6M USD、無公開市場買進，多名高階與董事參與。
- 應收帳款年增約 65%，高於營收增速；存貨年增約 28%。若需求轉弱，庫存與應收風險會放大。
- forwardEps 40.40 與季度共識明顯不符，forward P/E 8.4x 可能誤導。
- 股價自高點下跌 57.7%、Beta 2.34、空單比例上升，波動與情緒風險高。
- 資料品質：fast_info 為 cache 價格；info 的 bid/ask 不一致；yfinance cookie/crumb 多次 ConnectionError；FY26 Net Debt 與 Long Term Debt 為 n/a；分部營收與公司指引 n/a；ex-dividend 日期晚於基準日。
- 股息極低（殖利率 0.21%），對收益型投資人吸引力有限，但目前 FCF 覆蓋充足。

FUNDAMENTALS REPORT COMPLETE
