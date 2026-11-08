# Fundamentals — AVGO as of 2026-11-09

資料來源：`pipeline/tools/yf`（yfinance 快取，`source: cache` 為正常現象）。價格取自 2026-11-06 收盤（`regularMarketTime`），快取寫入時間 2026-11-08。財報以 USD 計，金額單位統一採 B（十億美元）與 M（百萬美元），未使用 億。同業中位數工具未提供，全部標記為 DATA_UNAVAILABLE。

## Executive summary
AVGO 的財務體質強健：TTM 營收 $89.1B、Q3 FY26（截至 2026-07-31）營收年增 +85.5%、TTM 淨利率 42.9%、TTM FCF $39.4B（FCF/NI 1.03），淨負債/EBITDA 僅 0.68×。估值以 GAAP 計偏高（trailing P/E 37.5×、EV/EBITDA 27.5×），但以 consensus forward EPS $19.47 計 forward P/E 為 15.1×，且股價較 52 週高點 $495.00 回落 40.7%。主要留意點在於 GAAP 盈餘品質（TTM 有效稅率僅 5.4%、SBC 占 FCF 21.5%）、商譽佔資產比重高，以及 insider 資料僅到 2026-07-10，已過時約四個月。

## Revenue & profitability

**營收規模與成長。** 年度營收自 FY22 $33.2B 成長至 FY25 $63.9B，FY22–FY25 3 年 CAGR 為 24.4%，FY25 年增 +23.9%（FY24 為 $51.6B）。季度營收加速明顯：2025-07 季 $15.95B、2025-10 季 $18.02B、2026-01 季 $19.31B、2026-04 季 $22.19B、2026-07 季 $29.59B，最新季年增 +85.5%。TTM 營收合計 $89.1B。

**分部結構。** 公司分為 Semiconductor Solutions 與 Infrastructure Software 兩大分部，業務摘要提及 AI networking 與 data center 相關產品。工具未提供分部營收數字，分部占比 DATA_UNAVAILABLE。

**獲利能力趨勢。**

| 年度 | 營收 | 毛利率 | 營業利益率（As Reported） | 淨利率 |
|---|---|---|---|---|
| FY22 | $33.2B | 66.5% | 42.8% | 33.8% |
| FY23 | $35.8B | 68.9% | 45.2% | 39.3% |
| FY24 | $51.6B | 63.0% | 26.1% | 11.4% |
| FY25 | $63.9B | 67.8% | 39.9% | 36.2% |
| TTM（至 2026-07） | $89.1B | 68.8% | 48.0% | 42.9% |

FY24 獲利率明顯下滑，原始資料顯示當年稅費 $3.75B，有效稅率 37.8%，屬一次性影響較大的年度。TTM 淨利率 42.9% 與 info 欄位 `profitMargins` 0.42944 一致，可交叉確認。

**ROE 與 ROIC。** info 的 `returnOnEquity` 為 44.2%，以 TTM 淨利 $38.3B 除以平均股東權益（2025-07 $73.3B 與 2026-07 $99.7B 平均 $86.5B）重算約 44.2%，一致。ROIC 為推導值：TTM 營業利益 $42.8B × (1 − 25.57% 稅率) ÷ 投入資本 $135.1B（總債務 $59.4B + 股東權益 $99.7B − 現金 $24.0B）≈ 23.6%。

**GAAP EPS 動能。** 最新季 GAAP diluted EPS $2.68，去年同季 $0.85，年增約 +215%（info `earningsQuarterlyGrowth` 2.161 一致）。TTM GAAP diluted EPS $7.83。

## Cashflow & balance sheet

**現金流品質。**
- FY25：營運現金流 $27.5B、資本支出 $0.6B、FCF $26.9B，FCF margin 42.1%，FCF/NI 1.16。
- TTM：營運現金流 $40.7B、資本支出 $1.25B、FCF $39.4B，FCF margin 44.2%，FCF/NI 1.03（高於 0.9 健康門檻）。
- FY24 FCF/NI 3.29 因當年淨利被一次性稅費壓低而失真，不宜作為趨勢依據。
- 資本支出相當低（TTM 僅占營收 1.4%），而 FY25 D&A 為 $8.8B，差距主要反映無形資產攤銷，需自行判讀。
- 工具欄位不一致：info `freeCashflow` 為 $30.6B，季度現金流加總為 $39.4B；info `grossMargins` 為 75.5%，損益表毛利加總為 68.8%。本報告採季度報表加總值，並以此為準。

**資產負債表（最新季 2026-07-31）。**
- 現金 $24.0B（2025-07 為 $10.7B，年增約 +124%）。
- 總債務 $59.4B（2025-07 為 $64.2B），淨負債 $35.4B（2025-07 為 $53.5B，年減約 33.8%）。
- 淨負債/TTM EBITDA 0.68×，總債務/TTM EBITDA 1.14×；FY25 利息費用 $3.2B，營業利益/利息費用約 8.0×（以 FY25 報告值計）。
- 流動比率 2.50×（FY25 為 1.71×）；速動比率 2.15×（info）。
- 股東權益 $99.7B，債務/權益 59.6%（FY25 為 80.1%，已改善）。
- 商譽與無形資產合計 $13.0B（FY25，占總資產 76%），其中商譽 $9.8B；有形資產淨值為 −$4.9B（FY25）。商譽於 FY24 由 FY23 的 $4.4B 升至 $9.8B，與同期大型併購相符（資產負債表推斷，工具未明示併購名稱），減損風險需持續監控。

## Capital allocation & insider signal

**資本配置。**
- 股息：目前年化股息 $2.60（每季 $0.65），殖利率 0.89%。TTM 股息支出 $12.1B，TTM FCF 為股息的 3.3 倍，股息覆蓋充足。最近一次除息日 2026-09-21，支付日 2026-09-30。
- 回購：TTM 回購 $8.5B（集中於 2026-01 季），FY25 回購 $6.3B，較 FY24 的 $12.4B 下降。
- 股本：流通股數由 2025-07 的 4.72B 股增至 2026-07 的 4.77B 股（+1.1%），回購未能抵銷股權稀釋。
- SBC：TTM SBC $8.5B，占 TTM FCF 21.5%；扣除 SBC 後的 FCF 約 $30.9B。FY25 SBC 較 FY24 增加約 32%。
- 併購與負債：FY24 債務發行 $4.0B；FY25 發行 $1.6B 新債、淨償還 $0.3B，總債務由 2025-07 的 $64.2B 降至 2026-07 的 $59.4B。

**Insider 活動（6 個月窗口 2026-05-09 至 2026-11-09）。** 工具回傳的交易紀錄最後日期為 2026-07-10，之後約四個月無資料，資料 DATA_UNAVAILABLE。窗口內可見交易如下：
- 賣出 7 筆，合計 740,885 股、約 $284M（主要為 Samueli, Henry 2026-06-24 賣出 654,241 股、約 $250M，以及 Brazeal, Mark David 多筆）。
- 買入 1 筆：董事 You, Harry L. 2026-06-11 買入 1,000 股，約 $0.37M。
- 淨額約 −$284M，占市值 $1,402B 約 0.02%，規模小。
- 長期脈絡：2024-12 至 2026-07 全部賣出 62 筆、約 $1.35B，其中 Samueli, Henry 約 $749M、CEO Hock E. Tan 約 $297M。多數為既定計畫性質的賣出或贈與，工具未提供 10b5-1 標記，無法確認。

**機構持股。** 機構持股比例 79.9%，內部人持股 1.9%。前三大持有人為 BlackRock 8.34%、Vanguard 6.48%、State Street 4.12%；FMR 2026-06-30 增持 16.3%。空頭部位 53.6M 股，占浮動籌碼 1.14%，short ratio 2.31 日（截至 2026-10-15）。

## Valuation

以 USD 價格 $293.69、流通股數 4.774B 股計算，市值約 $1,402B，EV $1,437B。

| 指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E（GAAP） | 37.5× | TTM GAAP EPS $7.83 |
| Forward P/E | 15.1× | consensus forward EPS $19.47 |
| 目前財年 P/E（FY26 consensus EPS $11.67） | 25.2× | `epsCurrentYear` |
| EV/EBITDA（TTM） | 27.5× | TTM EBITDA $52.3B |
| EV/Revenue（TTM） | 16.1× | |
| P/S（TTM） | 15.7× | |
| P/FCF（TTM，季度加總） | 35.6× | FCF $39.4B |
| P/FCF（info 欄位） | 45.8× | info FCF $30.6B，與上列口徑不一致 |
| P/B | 14.1× | 每股淨值 $20.88 |
| PEG | 0.29 | info `pegRatio` |

**同業比較。** 工具未提供同業中位數，sector median 全部 DATA_UNAVAILABLE。以絕對值判讀：GAAP 口徑之 trailing 倍數偏高，forward 倍數與 PEG 顯示市場對 EPS 成長的定價相對保守。股價位於 50 日均線 $347.89 與 200 日均線 $367.09 之下，分別低 15.6% 與 20.0%；52 週漲跌幅 −18.1%，同期 S&P 500 為 +8.0%。

**分析師共識。** 47 位分析師，平均目標價 $533.42（中位數 $535，最低 $400，最高 $660），recommendation mean 1.24（strong_buy）。相對現價隱含上行 +81.6%。此為共識資料，非本報告之投資建議。

## Key catalysts

- **下次財報：2026-12-09**（FY26 Q4，即本財年最後一季），EPS consensus $3.84。
- **EPS 估計走勢：** FY26 Q2（2026-06-03 財報）估計 $2.40 → FY26 Q3（2026-09-02 財報）估計 $3.24 → FY26 Q4（2026-12-09 財報）估計 $3.84，估計值逐季上修。
- **財報紀錄：** 工具列出 23 季皆為 EPS beat，近 8 季平均超出幅度約 +2.6%；最近已公布季（2026-06-03，FY26 Q2）實際 $2.44 對估計 $2.40，超出 +1.7%。
- **Q3 FY26 缺口：** 2026-09-02 的非 GAAP 實際 EPS 在快取中為 null，DATA_UNAVAILABLE；季度 GAAP 數字（$2.68）可得。
- **股利：** 最近一次除息 2026-09-21；下次除息日 DATA_UNAVAILABLE。
- **分部與產品動態：** 工具未提供公司最新指引（guidance）文字與分部營收，相關催化劑 DATA_UNAVAILABLE。

## Metrics table

營收與獲利金額單位為 B USD；Insider 金額為 M USD。Sector median 欄位皆為 DATA_UNAVAILABLE。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM，B USD） | 89.1 | Q3 FY26 年增 +85.5%；FY25 年增 +23.9% | DATA_UNAVAILABLE | 強 |
| 營收 3 年 CAGR（FY22–FY25） | 24.4% | — | DATA_UNAVAILABLE | 強 |
| 毛利率（TTM） | 68.8% | FY25 vs FY24 +4.8pp | DATA_UNAVAILABLE | 強 |
| 營業利益率（TTM，As Reported） | 48.0% | FY25 vs FY24 +13.8pp | DATA_UNAVAILABLE | 強 |
| 淨利率（TTM） | 42.9% | FY25 36.2% vs FY24 11.4% | DATA_UNAVAILABLE | 強 |
| ROE | 44.2% | — | DATA_UNAVAILABLE | 強 |
| ROIC（推導） | 23.6% | — | DATA_UNAVAILABLE | 良 |
| FCF margin（TTM） | 44.2% | FY25 42.1% vs FY24 37.6% | DATA_UNAVAILABLE | 強 |
| FCF / NI（TTM） | 1.03 | FY25 1.16 | DATA_UNAVAILABLE（健康門檻 > 0.9） | 健康 |
| 有效稅率（TTM） | 5.4% | FY25 為稅務利益；FY24 37.8% | DATA_UNAVAILABLE | 需留意（盈餘品質） |
| 淨負債（B USD） | 35.4 | 2025-07 為 53.5，年減 33.8% | DATA_UNAVAILABLE | 良 |
| 淨負債 / TTM EBITDA | 0.68× | — | DATA_UNAVAILABLE | 良 |
| 流動比率 | 2.50× | FY25 1.71× | DATA_UNAVAILABLE | 強 |
| 債務 / 權益 | 59.6% | FY25 80.1% | DATA_UNAVAILABLE | 良 |
| 有形資產淨值（FY25，B USD） | −4.9 | — | DATA_UNAVAILABLE | 需留意（商譽占比高） |
| 資本支出（TTM，B USD） | 1.25 | FY25 0.62 vs FY24 0.55 | DATA_UNAVAILABLE | 偏低，需自行判讀 |
| 股息覆蓋（TTM FCF / 股息） | 3.3× | — | DATA_UNAVAILABLE | 強 |
| 回購（TTM，B USD） | 8.5 | FY25 6.3 vs FY24 12.4 | DATA_UNAVAILABLE | 中性 |
| SBC（TTM，B USD） | 8.5 | FY25 年增約 +32% | DATA_UNAVAILABLE | 需留意（占 FCF 21.5%） |
| 流通股數（B 股） | 4.77 | 2025-07 為 4.72，+1.1% | DATA_UNAVAILABLE | 中性 |
| 內部人淨交易（6 個月，M USD） | −284（賣出 740,885 股） | 資料截至 2026-07-10 | DATA_UNAVAILABLE | 需留意（資料過時） |
| 內部人淨交易占市值 | 約 −0.02% | — | DATA_UNAVAILABLE | 規模小 |
| Trailing P/E（GAAP） | 37.5× | — | DATA_UNAVAILABLE | 偏高 |
| Forward P/E | 15.1× | — | DATA_UNAVAILABLE | 相對合理 |
| EV/EBITDA（TTM） | 27.5× | — | DATA_UNAVAILABLE | 偏高 |
| P/FCF（TTM） | 35.6× | — | DATA_UNAVAILABLE | 偏高 |
| P/S（TTM） | 15.7× | — | DATA_UNAVAILABLE | 偏高 |
| PEG | 0.29 | — | DATA_UNAVAILABLE | 相對低 |
| 股價 vs 52 週高點 | $293.69 vs $495.00，−40.7% | — | DATA_UNAVAILABLE | 留意 |
| 股息殖利率 | 0.89% | — | DATA_UNAVAILABLE | 低 |
| 分析師平均目標價 vs 現價 | $533.42 vs $293.69，+81.6% | 47 位分析師 | DATA_UNAVAILABLE | 共識偏多 |

## Red flags
- **GAAP 盈餘品質：** TTM 有效稅率 5.4%，2025-10 季出現 −$165M 稅務利益，當季淨利被墊高；FY25 淨利 $23.1B 高於稅前利益 $22.7B。以稅率正常化後的獲利可能低於報告值，trailing P/E 解讀需保守。
- **SBC 占比高：** TTM SBC $8.5B，占 FCF 21.5%；股本仍增加 1.1%，回購未能完全抵銷稀釋。
- **商譽與有形資產：** 商譽加無形資產占 FY25 總資產 76%，有形資產淨值為負（−$4.9B），併購減損風險與資產品質需追蹤。
- **內部人大額賣出：** 2026-06 至 2026-07 窗口內有 $284M 賣出，其中 Samueli, Henry 單筆約 $250M；工具未標示計畫性質。
- **股價與基本面背離：** 最新季營收年增 +85.5%、EPS 年增約 +215%，但股價較 52 週高點回落 40.7%、低於 50 日與 200 日均線。工具未提供下跌原因（如指引、客戶、產業資料），無法判定是否為基本面以外因素。
- **資料一致性：** info 的 FCF（$30.6B）與季度加總（$39.4B）、info 毛利率（75.5%）與損益表毛利率（68.8%）不一致；info `epsCurrentYear` 與 forward EPS 來源口徑未明，估值倍數採 GAAP 與 consensus 並列呈現。
- **資料缺口：** Q3 FY26 非 GAAP 實際 EPS 缺漏、insider 資料止於 2026-07-10、分部營收與公司指引 DATA_UNAVAILABLE、同業中位數 DATA_UNAVAILABLE、價格為 2026-11-06 收盤快取值（非 2026-11-09 即時價）。

FUNDAMENTALS REPORT COMPLETE
