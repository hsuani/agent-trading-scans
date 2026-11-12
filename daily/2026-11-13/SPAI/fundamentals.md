# Fundamentals — SPAI (Safe Pro Group Inc.) as of 2026-11-13

資料來源說明: 本次 yfinance live feed 的 cookie/crumb 取得失敗，工具自動回退至 repo cache (`prices/yf/`)。info 與 fast_info 明確標示 `source: cache` (info cached_at 2026-11-12 15:06 UTC)。財務報表 (年度/季度 IS、BS、CF) 同樣經由工具回退取得，以下數字皆取自工具 JSON 並以 USD 百萬 (USD M) 表示。股價時點為 regularMarketTime 2026-11-12 15:05 UTC，未使用 2026-11-13 之後的任何資料。公司為美國上市 (NCM) 小型國防/安防公司，無 TWD/KRW 數字，故全文只用 USD M。

## Executive summary
SPAI 仍處於高度虧損、現金燒耗的早期階段: TTM 營收 2.88 USD M、淨虧損 -14.41 USD M、FCF -8.48 USD M，期末 (2026-06-30) 現金 10.23 USD M、有息負債僅 0.16 USD M，以目前燒速估約 14 個月跑道，財務體質以「淨現金 + 低負債」支撐，但靠股權稀釋與高額 SBC 維持營運。估值上 P/S 21.7x、EV/Revenue 18.1x、P/B 5.07x 在毫無獲利、EPS 連續 4 季不及預期的條件下偏貴，估值完全依賴 2026 年 Q1 起的營收躍升能否延續 (Q2'26 年化 run-rate 約 5.33 USD M)。內部人方面 CEO 於 2026-09-09 以 $4.00 出售 1,000,000 股 (約 4.0 USD M，占市值 6.4%)，且 2026 年上半年仍有 2.33 USD M 回購，與現金流出方向相反，需納入風險判斷。

## Revenue & profitability

**營收趨勢 (USD M, source: cache)**

| 期間 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|---|
| FY2022 | 1.151 | n/a | 45.1% | -43.7% | -44.1% |
| FY2023 | 0.918 | -20.2% | 33.9% | -687% | -688% |
| FY2024 | 2.169 | +136.3% | 41.8% | -330% | -343% |
| FY2025 | 0.607 | -72.0% | 33.3% | -2,259% | -2,360% |
| Q2'25 | 0.093 | n/a | 34.4% | n/a | n/a |
| Q3'25 | 0.101 | n/a | 33.7% | n/a | n/a |
| Q4'25 | 0.228 | n/a | 32.9% | n/a | n/a |
| Q1'26 | 1.220 | Q1'25 為年度扣除三季後推算 0.185 (衍生值，非直接揭露) | 68.0% | -239% | -229% |
| Q2'26 | 1.332 | +1,332% (≈14.3x) | 64.0% | -246% | -238% |

- 3 年 CAGR (FY2022→FY2025): 約 -19.2%。工具僅提供 4 個年度資料點，無法計算 4-5 年 CAGR (DATA_UNAVAILABLE)。
- 近季爆發: 營收自 Q4'25 0.228 跳升至 Q1'26 1.220 (QoQ 約 +435%)，Q2'26 再升至 1.332。工具未揭露成長原因 (新客戶、併購或一次性訂單)，屬 DATA_UNAVAILABLE。
- info 之 `revenueGrowth` = 13.362 (約 +1,336%)，與 Q2'26 YoY 一致。TTM 營收 2,881,329 USD 與季度加總 (0.101+0.228+1.220+1.332=2.881) 吻合。
- 業務組成 (info.longBusinessSummary): 爆炸物處理 (EOD/UXO) 產品、防彈背心/頭盔/防彈毯、無人機巡檢管理服務、AI 影像偵測與資料分析。**分部營收比重 DATA_UNAVAILABLE** (工具未提供 segment 拆分)。
- 毛利率: 2025 全年 33.3% 偏低，但 Q1'26 (68.0%) 與 Q2'26 (64.0%) 大幅提升，TTM 毛利率依季度加總為 62.2% (毛利 1.792 USD M)；info `grossMargins` 為 65.2%，`grossProfits` 為 1.878 USD M，兩者與季度加總略有差異，以季度加總為準。
- 營業費用: 2025 全年營業費用 13.92 USD M，其中 SG&A 13.22 USD M、R&D 0.39 USD M。TTM 營業費用 15.77 USD M，TTM 營業利益 -13.98 USD M (-485% margin，與 info `operatingMargins` -4.85 一致)。
- 淨利 TTM -14.41 USD M，與 info `netIncomeToCommon` -14,405,550 一致。info `profitMargins` 回傳 0.0，與淨利資料矛盾，視為無效欄位。
- 2025 年有一筆 0.831 USD M 無形資產減損 (Q3'25)，商譽 0.685 USD M 於 2025 年底歸零。

**獲利能力**
- ROE: -198.2% (info `returnOnEquity` -1.98)。ROA: -102.3% (info)。
- ROIC (計算值): TTM 營業利益 -13.98 / Q2'26 投入資本 12.12 USD M ≈ -115%。NOPAT 為負，ROIC 為負。

## Cashflow & balance sheet

**現金流 (USD M, source: cache)**

| 期間 | 營運現金流 (OCF) | 資本支出 (Capex) | FCF | 股權募資 | SBC |
|---|---|---|---|---|---|
| FY2022 | 1.079 | -0.026 | 1.053 | 1.176 | 0.000 |
| FY2023 | -2.004 | -0.030 | -2.034 | 1.005 | 3.617 |
| FY2024 | -4.095 | -0.436 | -4.532 | 4.669 | 2.853 |
| FY2025 | -6.216 | -0.241 | -6.458 | 20.762 | 6.907 |
| TTM (Q3'25–Q2'26) | -8.288 | -0.188 | -8.476 | n/a | 5.997 |

- FCF margin TTM: -294% (FCF -8.48 / 營收 2.88)。FY2025 FCF margin: -1,064%。
- FCF / NI: TTM 0.59、FY2025 0.45，但 FCF 與淨利皆為負值，比率無經濟意義，不能視為「健康」(>0.9 門檻不成立)。
- SBC 佔淨虧損: TTM SBC 5.997 / 淨虧損 14.405 ≈ 42%，SBC 為主要非現金成本來源。
- 資料差異: info `freeCashflow` = -3.60 USD M，與季度 FCF 加總 -8.48 USD M 不一致。本報告以季度加總為準，並列為資料品質問題。

**資產負債表 (2026-06-30, USD M, source: cache)**
- 現金及約當現金: 10.23 (Q1'26 14.80；YE25 16.79)，較 YE25 下降 39.1%。
- 有息負債: 0.16 (長期負債 0.146 + 流動資本租賃 0.016)。info `totalDebt` 0.595 另含關係人應付 0.433。
- 淨現金 (以有息負債計): 10.07 USD M (占市值 16.1%)。以 info totalDebt 計為 9.64 USD M。
- 流動比率: 8.76x (計算: 流動資產 12.38 / 流動負債 1.41，與 info 一致)。速動比率: 8.13x (info)。
- 負債/權益: 有息負債口徑 1.4%；info 口徑 (0.595/11.97) 為 5.0%，info 欄位 `debtToEquity` 4.971 為百分比單位。
- 股東權益: 11.97 (YE25 17.72，下降 32.4%)。累積虧損 (Retained Earnings) -34.54。
- 總資產: 13.53；營運資金: 10.97。
- 應收帳款: 1.250 USD M，自 Q1'26 0.062 暴增約 20 倍；應收/年化營收約 85 天 (1.25 / (1.332×4) × 365，計算值)。收現品質為本季主要觀察點。
- 存貨: 0.757 USD M (YE25 0.615；Q1'26 0.454)。
- 遞延收入: 0.204 USD M (Q1'26 0.028)。
- 商譽: 0 (2025 年減損)；無形資產 0.782；淨 PPE 0.360。
- **現金跑道 (計算值)**: H1'26 FCF 合計 -4.23 USD M，年化約 -8.46 USD M；以 10.23 USD M 現金估算約 14.5 個月 (靜態、未計 Q3'26 之後的變化、未計新增融資)。

## Capital allocation & insider signal

**資本配置**
- 股權稀釋: 流通股數 (ordinary shares, 期末) 2023 13.68M → 2024 14.54M → 2025 20.74M (2025 年 +42.7%) → 2026-06-30 20.36M (H1 淨減 1.8%，因回購)。
- 股權募資: FY2025 發行股票 20.76 USD M (其中普通股 19.71、特別股 1.05)，為 2024 年 (4.67) 的 4.4 倍。Q3'25 6.77、Q4'25 12.95。
- 回購: FY2025 -0.61 USD M；2026 H1 合計 -2.33 USD M (Q1 -0.73、Q2 -1.60)，庫藏股 2026-06-30 為 3.01 USD M。**在 H1 營運現金流流出 4.06 USD M (FCF -4.23 USD M) 的同時進行回購，屬資本配置矛盾點。**
- 資本支出: TTM -0.19 USD M，占營收約 6.5%，規模極小；FY2024 -0.44 含無形資產投入 -0.37。
- 股息: 無 (dividendYield 0.0)。股息覆蓋率 n/a。
- 負債: 長期負債 0.146 USD M 自 2023 起持平，無償還或新增。

**內部人交易 (yfinance insider，近 6 個月窗口 2026-05-13 至 2026-11-13)**
- 公開市場賣出: ERDBERG DANIYEL (Founder/CEO/Chairman) 於 2026-09-09 賣出 1,000,000 股，每股 $4.00，合計 4.00 USD M，持股性質 D (直接)。
- 公開市場買入: 0 筆。
- 淨買賣: 淨賣出 1,000,000 股 / 約 -4.00 USD M。
- 相對市值: 4.00 / 62.52 = 6.4%；相對流通股 (20.98M) 4.8%；相對浮動股 (11.76M) 8.5%。
- 成交價 $4.00 高於現價 2.98 約 34%，即賣出價位高於目前交易價。
- 窗口外之獲獎 (Grant): MACK BRIAN WILLIAM 300,000 股 (2026-05-01)、MATHEWS JARRET 20,000 股 (2026-04-01)，均於窗口外或屬無償授予，不計入買賣。CEO 另有 2026-03-06 (9,000 股) 與 2025-12-23 (24,000 股) 之贈與紀錄，屬非市場交易。
- 內部人持股比例: 42.8% (`heldPercentInsiders`)，集中度高；CEO 單人持股規模未由工具提供具體股數 (DATA_UNAVAILABLE)。

**機構與空單**
- 機構持股 11.6% (31 家)；前 10 大機構合計約 9.6% (Vanguard Capital 2.69% 最大，563,837 股，2026-06-30)。
- 空單: 622,571 股 (2026-10-30)，較前期 413,501 股增加約 50.5%；佔浮動股 5.18%；以 3 個月平均量 346,296 股計，回補天數約 1.8 天。

## Valuation

價格基準: 2.98 USD (info currentPrice，regularMarketTime 2026-11-12 15:05 UTC)。fast_info (cnyes feed cache) 顯示 last_price 3.04 / previous_close 3.04，與 info 不同，以 info 為準並註記。

| 項目 | 數值 | 說明 |
|---|---|---|
| 市值 | 62.52 USD M | info marketCap；2.98 × 20.98M 股 = 62.5 (已驗算) |
| 企業價值 EV | 52.27 USD M | info enterpriseValue |
| P/E (TTM) | n/a | EPS TTM -0.74 為負 |
| P/E (Forward) | n/a | info 無 forwardEps |
| P/S (TTM) | 21.7x | 62.52 / 2.881 = 21.7 (已驗算) |
| EV/Revenue (TTM) | 18.1x | info enterpriseToRevenue |
| EV/EBITDA (TTM) | -3.8x | EBITDA TTM 為負，不適用 |
| P/FCF | n/a | FCF TTM 為負 |
| P/B | 5.07x | 2.98 / 每股淨值 0.588 |
| 市值 / Q2'26 年化營收 | 11.7x | 62.52 / (1.332×4 = 5.33)，計算值 |

- 相對產業中位數: 工具未提供行業中位數，**Sector median 為 DATA_UNAVAILABLE**，故不做數字比較，僅定性: 在持續虧損 (EPS 負、FCF 負) 的前提下，21.7x P/S 屬高估值區間。
- 價格位置: 52 週區間 2.75–6.70，現價距低點 +8.4%、距高點 -55.5%；52 週變動 -33.0% (info)。
- 均線: 50 日均 3.925 (現價低 24.1%)，200 日均 4.362 (現價低 31.7%)，股價位於兩條均線之下。
- 波動: beta 3.911 (info)，屬高波動股。
- 分析師: 3 位覆蓋，recommendationMean 1.0 (strong_buy)，目標價均值 10.67 USD (高 13.00 / 低 9.00)，較現價 +258%。覆蓋家數少，代表性低，僅作為資料呈現，不構成建議。

## Key catalysts

- **最近一次財報**: 2026-08-14 (Q2'26)，EPS -0.15 vs 預估 -0.14，不及預期 -7.1%。
- **下次財報**: yfinance 未提供下次財報日 (DATA_UNAVAILABLE)。依過往模式 (Q3'25 於 2025-11-14 公布) 推估 Q3'26 財報約在 2026-11 中旬，此為依歷史模式的估計，非工具揭露；截至 2026-11-13 之 Q3'26 財務數字不在資料中。
- **EPS 歷史 surprise (最近四季)**: 2025-11-14 (Q3'25) -163.6% (含 0.831 USD M 減損)；2026-03-31 (Q4'25) -28.0%；2026-05-15 (Q1'26) -16.7%；2026-08-14 (Q2'26) -7.1%。**連續四季不及預期。**
- **管理層指引**: DATA_UNAVAILABLE (工具不提供 guidance)。
- **營收動能**: Q1'26 與 Q2'26 連續兩季營收超過 1.2 USD M，為 2025 全年每季不到 0.25 USD M 的 5 倍以上。能否延續，是估值成敗的核心。
- **融資風險**: 現金 10.23 USD M、約 14 個月跑道；若 2027 年前需再募資，稀釋風險高 (2025 年已募資 20.76 USD M)。
- **空單與內部人**: 空單 2026-10-30 增加 50.5%；CEO 2026-09-09 大額出售，兩者皆屬需追蹤的訊號。

## Metrics table

單位: 金額 USD M (百萬美元)；股數 M 股；比率 %、x。
Sector median 欄位全部為 DATA_UNAVAILABLE (工具無行業中位數)。

| Metric | Latest | YoY / 比較 | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD M) | 2.88 | Q2'26 YoY +1,332%；FY25 YoY -72.0% | DATA_UNAVAILABLE | 規模極小，近季成長但歷史不穩 |
| 營收 Q2'26 年化 run-rate (USD M) | 5.33 | 較 FY25 (0.61) 放大約 8.8x | DATA_UNAVAILABLE | 估值依賴此 run-rate 延續 |
| 毛利率 TTM | 62.2% (info 65.2%) | FY25 33.3%；Q2'26 64.0% vs Q2'25 34.4% | DATA_UNAVAILABLE | 明顯改善，需更多季度確認 |
| 營業利益率 TTM | -485% | FY25 -2,259%；FY24 -330% | DATA_UNAVAILABLE | 極差 |
| 淨利率 TTM | -500% | FY25 -2,360% | DATA_UNAVAILABLE | 極差 |
| ROE | -198% (info) | FY25 n/a (同期權益變動) | DATA_UNAVAILABLE | 負，弱 |
| ROIC (計算) | ≈ -115% | n/a | DATA_UNAVAILABLE | 負，弱 |
| 營運現金流 TTM (USD M) | -8.29 | FY25 -6.22 (FY24 -4.10) | DATA_UNAVAILABLE | 燒錢速度加快 |
| FCF TTM (USD M) | -8.48 | FY25 -6.46 | DATA_UNAVAILABLE | 負 |
| FCF margin TTM | -294% | FY25 -1,064% | DATA_UNAVAILABLE | 負 |
| FCF / NI | n/a (兩者皆負) | FY25 0.45 | DATA_UNAVAILABLE | 不適用，不通過 >0.9 門檻 |
| SBC TTM (USD M) | 6.00 | FY25 6.91 vs FY24 2.85 (+142%) | DATA_UNAVAILABLE | 偏高，佔淨虧損約 42% |
| 現金 2026-06-30 (USD M) | 10.23 | 較 YE25 16.79 下降 39.1% | DATA_UNAVAILABLE | 約 14 個月跑道 |
| 有息負債 (USD M) | 0.16 (info 口徑 0.60) | 持平 | DATA_UNAVAILABLE | 低 |
| 淨現金 (USD M) | 10.07 | 較 YE25 下降 | DATA_UNAVAILABLE | 正，但持續收縮 |
| 流動比率 | 8.76x | n/a | DATA_UNAVAILABLE | 極佳 (規模小，參考性有限) |
| 速動比率 | 8.13x | n/a | DATA_UNAVAILABLE | 極佳 |
| 負債/權益 (有息負債口徑) | 1.4% | n/a | DATA_UNAVAILABLE | 低 |
| 股東權益 (USD M) | 11.97 | 較 YE25 17.72 下降 32.4% | DATA_UNAVAILABLE | 下降中 |
| 流通股數 (M 股) | 20.36 (2026-06-30) | FY25 YE 較 FY24 YE +42.7% | DATA_UNAVAILABLE | 稀釋明顯 |
| 股權募資 FY25 (USD M) | 20.76 | FY24 4.67 (4.4x) | DATA_UNAVAILABLE | 依賴股權融資 |
| 回購 2026 H1 (USD M) | 2.33 | FY25 全年 0.61 | DATA_UNAVAILABLE | 與燒現金方向矛盾 |
| 資本支出 TTM (USD M) | 0.19 | FY25 0.24 vs FY24 0.44 (-45%) | DATA_UNAVAILABLE | 極低 |
| 股息殖利率 | 0% | n/a | DATA_UNAVAILABLE | n/a |
| 應收帳款 (USD M) | 1.25 | Q1'26 0.06 (約 20x) | DATA_UNAVAILABLE | 需追蹤收現 |
| P/E (TTM) | n/a | n/a | DATA_UNAVAILABLE | 無獲利 |
| P/E (Forward) | n/a | n/a | DATA_UNAVAILABLE | 無預估 EPS |
| P/S (TTM) | 21.7x | n/a | DATA_UNAVAILABLE | 偏貴 |
| EV/Revenue (TTM) | 18.1x | n/a | DATA_UNAVAILABLE | 偏貴 |
| EV/EBITDA (TTM) | -3.8x | n/a | DATA_UNAVAILABLE | 不適用 (EBITDA 為負) |
| P/FCF | n/a | n/a | DATA_UNAVAILABLE | 不適用 (FCF 為負) |
| P/B | 5.07x | n/a | DATA_UNAVAILABLE | 偏高 |
| 市值 (USD M) | 62.52 | n/a | DATA_UNAVAILABLE | 微型股 |
| 股價 (USD) | 2.98 | 52 週 -33.0%；低於 50DMA 3.925 與 200DMA 4.362 | DATA_UNAVAILABLE | 弱勢趨勢 |
| Beta | 3.91 | n/a | DATA_UNAVAILABLE | 高波動 |
| 內部人持股 | 42.8% | n/a | DATA_UNAVAILABLE | 高度集中 |
| 機構持股 | 11.6% (31 家) | n/a | DATA_UNAVAILABLE | 偏低 |
| 內部人淨買賣 (6 個月, USD M) | -4.00 (1,000,000 股) | 無買入 | DATA_UNAVAILABLE | 負向訊號 |
| 空單佔浮動股 | 5.18% (2026-10-30) | 空單股數 +50.5% | DATA_UNAVAILABLE | 上升中 |
| EPS surprise 最近四季 | -163.6% / -28.0% / -16.7% / -7.1% | 連續不及預期 | DATA_UNAVAILABLE | 負向 |
| 分析師目標價均值 (USD) | 10.67 (3 位覆蓋) | 較現價 +258% | DATA_UNAVAILABLE | 覆蓋少，參考性低 |

## Red flags
- **現金燒耗與跑道有限**: TTM FCF -8.48 USD M，現金 10.23 USD M，靜態跑道約 14.5 個月；若未來季度燒速增加，需再融資。
- **持續股權稀釋**: 2025 年流通股數 +42.7%，股權募資 20.76 USD M。
- **回購與燒現金並行**: 2026 H1 回購 2.33 USD M，同期 FCF 流出 4.23 USD M，資本配置方向與現金狀況不一致。
- **CEO 大額出售**: 2026-09-09 出售 1,000,000 股 @ $4.00 (4.0 USD M，占市值 6.4%)，窗口內無任何買入。
- **EPS 連續四季不及預期**，最近一季 Q2'26 EPS -0.15 vs 預估 -0.14。
- **應收帳款暴增**: 2026-06-30 應收 1.25 USD M，較 Q1 之 0.06 增約 20 倍，年化約 85 天，收現品質待驗證。
- **SBC 偏高**: TTM SBC 6.00 USD M，佔淨虧損約 42%；2025 年 SG&A 13.22 USD M 中 SBC 6.91 USD M 為非現金成本。
- **營收歷史極不穩定**: FY2025 營收 -72%，2024-2025 季度營收由 0.09 跳至 1.33 USD M，單季波動幅度大，樣本不足以判斷可持續性。
- **估值**: P/S 21.7x、EV/Revenue 18.1x、P/B 5.07x，在持續虧損下估值需完全依賴成長兌現。
- **技術與市場結構**: 股價低於 50 日與 200 日均線、52 週跌 33%、beta 3.91、空單佔浮動股 5.2% 並上升 50%。
- **覆蓋與資料可信度低**: 分析師僅 3 位，目標價 10.67 USD 與現價差距 +258%，代表性有限。
- **資料品質註記 (工具內部不一致)**:
  - info `freeCashflow` -3.60 USD M vs 季度加總 -8.48 USD M，採季度加總。
  - info `profitMargins` = 0.0，與 TTM 淨利率 -500% 矛盾，視為無效。
  - info `grossProfits` 1.878 USD M vs 季度毛利加總 1.792 USD M。
  - info `totalDebt` 0.595 USD M 含關係人應付 0.433，有息負債口徑為 0.162。
  - info `debtToEquity` 4.971 為百分比單位 (即 5.0%)，非倍數。
  - fast_info last_price 3.04 vs info currentPrice 2.98，採 info 並註記。
  - 季度 Q1'25 營收/IS 欄位為 None，本報告之 Q1'25 營收 0.185 為年度扣除三季之衍生值。
  - 股價為 2026-11-12 時點資料，財報最新為 2026-06-30 (Q2'26)；Q3'26 (2026-09-30) 財報在資料中不存在，視為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
