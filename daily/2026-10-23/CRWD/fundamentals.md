# Fundamentals — CRWD as of 2026-10-23

資料基準：yfinance（pipeline/tools/yf），股價為 fast_info 快取（cnyes feed，快取時間 2026-10-22T11:36 UTC，last_price 239.34 USD）。財年結束於 1 月底，TTM 以最近四季（2025-10 至 2026-07 季）加總計算。金額單位：USD，以 B（10 億）或 M（百萬）標示；本報告不使用 億。

## Executive summary
CrowdStrike（CRWD）營收維持高速成長，最近一季（FY27 Q2，止於 2026-07-31）YoY +25.8%，TTM 營業現金流約 2.02 B USD、FCF 約 1.52 B USD，淨現金約 4.19 B USD，資產負債表穩健。然而 GAAP 獲利接近零（TTM 淨利約 58.5 M USD，TTM 營業利益率 -2.2%），SBC 高達 TTM 營收的 23%，扣除 SBC 後的 FCF 僅約 0.28 B USD，估值極端（forward P/E 148.5x、P/S 45.4x），估值吸引力偏低。

## Revenue & profitability

**營收趨勢（USD M）**
- FY23（2023-01）2,241.2、FY24 3,055.6、FY25 3,953.6、FY26（2026-01）4,812.0。
- 3 年 CAGR（FY23 至 FY26）約 29.0%。5 年 CAGR 因 FY22 資料為 null 無法計算（n/a）。
- 年度 YoY：FY24 +36.3%、FY25 +29.4%、FY26 +21.7%，增速逐年放緩但仍維持 20% 以上。
- 季度 YoY：FY27 Q2（2026-07）1,470.9 vs 去年同季 1,169.0，YoY **+25.8%**，與 info.revenueGrowth 0.258 一致；QoQ 為 +6.2%（vs 1,385.6）。
- TTM 營收 5,396.1（與 info.totalRevenue 5,396,145,152 一致）。
- 分部營收：yfinance 未提供，segment mix n/a。依 longBusinessSummary，營收主要來自 Falcon 平台之 SaaS 訂閱（endpoint、cloud、identity、data、SIEM/SOAR 等模組）。

**毛利、營業利益、淨利率（年度）**

| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY23 | 73.2% | -8.5% | -8.2% |
| FY24 | 75.2% | -0.6% | 2.4% |
| FY25 | 74.9% | -2.9% | -0.4% |
| FY26 | 74.7% | -6.1% | -3.4% |

- TTM 毛利率約 75.2%（毛利合計 4,060.4 / 營收 5,396.1）；FY27 Q2 單季毛利率 74.6%。
- TTM 營業利益 -119.5（季度加總），TTM 營業利益率 -2.2%，與 info.operatingMargins -0.02259 一致，營業利益由負轉正尚未發生（僅 FY26 Q4 單季 +13.8）。
- TTM 淨利（季度加總）約 +58.5，淨利率約 1.1%；info.profitMargins 為 0.83%，兩者差異來自計算口徑，此處以季度加總為準。
- FY26 GAAP 淨利 -162.5，每股 GAAP 稀釋 EPS -0.16。

**ROE / ROIC**
- info.returnOnEquity 0.01461（TTM，約 1.5%）。FY26 以平均權益約 3.85 B 計，ROE 約 -4.2%。
- ROIC 無 yfinance 直接欄位（n/a）。粗估 TTM 營業利益 / FY26 Invested Capital（5,173.9）約 -2.3%，未做稅務調整，僅供量級參考。

**非 GAAP EPS**
- Yahoo earnings_dates 最近四次 EPS（口徑未明標，數值遠高於 GAAP，推測為 non-GAAP）：FY26 Q3 0.24、Q4 0.28、FY27 Q1 0.28、Q2 0.31，合計 TTM 1.11。
- Q2 FY27 實際 0.31 vs 預估 0.29，超預期 +6.38%。

## Cashflow & balance sheet

**現金流（USD M）**

| 年度 | OCF | Capex | FCF（OCF-Capex） | FCF margin | SBC |
|---|---|---|---|---|---|
| FY23 | 941.0 | 266.4 | 674.6 | 30.1% | 526.5 |
| FY24 | 1,166.2 | 237.1 | 929.1 | 30.4% | 648.7 |
| FY25 | 1,381.7 | 313.8 | 1,067.9 | 27.0% | 861.4 |
| FY26 | 1,612.3 | 370.9 | 1,241.5 | 25.8% | 1,096.7 |

- TTM（季度加總）OCF 2,016.6、Capex 494.0、FCF **1,522.6**，TTM FCF margin 約 28.2%。
- **資料不一致**：info.freeCashflow 為 1,995.4，與季度加總 OCF-Capex 的 1,522.6 差距約 473 M USD。本報告採用可重現的季度加總 1,522.6，並標示此差異。
- **FCF / NI**：TTM NI 約 58.5，FCF/NI ≈ 26x。數學上遠高於 0.9，但分母接近零，比率無經濟意義（n/m）。FY26 淨利為負，FCF/NI 同樣 n/m。
- **SBC 調整後 FCF**：TTM SBC 1,244.0，FCF 1,522.6 減 SBC 後僅約 278.6（margin 約 5.2%）。這是本公司現金流品質最大的疑慮。

**資產負債表（USD M）**

| 指標 | 最新（2026-07-31） | 前一期（2026-01-31） | 備註 |
|---|---|---|---|
| 現金與短期投資 | 5,013.8 | 5,230.1 | |
| 總負債（Total Debt） | 820.2 | 820.1 | |
| 淨現金（現金-總負債） | **+4,193.7** | +4,410.0 | 約 4.19 B |
| 股東權益 | 5,101.7 | 4,428.4 | |
| 負債/權益 | 15.96%（info） | | 總負債 / 權益約 16.1% |
| Current ratio | 1.57（info） | 1.77（FY26 資產 7,419.1 / 負債 4,184.2） | |
| Quick ratio | 1.37（info） | | |
| Deferred revenue（流動） | 3,497.1 | 3,421.1 | YoY +25.7%（vs 2,781.2） |

- 淨現金為正，流動性充足，債務負擔低（利息支出 TTM 約 26.6 M USD，對 4.19 B 淨現金影響極小）。
- 遞延收入 YoY +25.7%，與營收成長同步，為未來營收能見度的正向訊號。

## Capital allocation & insider signal

**資本配置**
- Capex 逐年增加：FY23 266.4 → FY26 370.9，FY26 年增 +18.2%；TTM capex 494.0，約佔營收 9.2%。
- 併購支出（Purchase of Business）：FY24 239.0、FY25 310.3、FY26 382.3（USD M），FY26 併購支出甚至超過 capex，併購對營收貢獻未在資料中揭露（n/a）。
- 買回：FY27 Q1（2026-04）買回 175.6；FY27 Q2 為 0。FY26 全年買回欄位為 null（n/a）。
- 股利：info 無 dividendRate 欄位（n/a），未見配息紀錄。
- **股本稀釋**：基本股數 FY24 917.5M → FY25 991.5M → FY26 1,013.5M（FY26 YoY +2.2%）。稀釋後平均股數 FY27 Q2 1,044.5M，相較去年同季 999.6M 增加 +4.5%。SBC 持續發放導致股本持續擴張。

**內部人交易（2026-04-22 至 2026-10-22，6 個月）**
- 共 119 筆賣出，合計約 1.567M 股，金額約 **457–485 M USD**（若排除 4 筆價格異常列，約 457 M；含全部則約 485 M）。
- 買入：0 筆（無公開市場買入）。
- 最大賣方：CEO George Robert Kurtz，6 個月賣出約 97.7 萬股，金額約 270–290 M USD，賣出頻率幾乎每週多次，屬於持續性出售。
- 其他賣方：Director Sameer Gandhi 約 15.2 萬股、President Michael Sentonas 約 13.6 萬股、Director Gerhard Watzinger 約 13.0 萬股、CFO Burt Podbere 約 6.8 萬股等。
- 占市值比：約 0.19–0.20%（市值 245.07 B）；占流通股數約 0.16%。以金額看，規模不大，但方向一致為淨賣出。
- 同期有 RSU/選擇權授予（例如 2026-04-16 CEO 授予 66,558 股），屬於 SBC 常態發放。
- 資料異常：2026-06-30 至 2026-07-06 有 4 筆價格異常（3,090.96、3,052.56、765.93-785.70、189.43-775.92 USD），與同期市價 ~190-210 不符，判定為資料錯誤，金額已另列計算。
- 解讀：內部人持續出售（CEO 為主）對估值形成壓力信號，但單一樣本無法判斷是否為預定交易計畫（10b5-1 n/a）。內部人持股僅 1.35%，持股比例低，與管理層利益綁定主要靠 SBC。

**機構持股**
- 機構持股 77.8%（機構數 3,267）。前十大包括 BlackRock 2.13%、Vanguard Capital 1.58%、State Street 1.13%、Invesco 0.82%、JPMorgan 0.80%、FMR 0.76%。

## Valuation

**價格與技術位置**
- 最新價 239.34 USD（前收 227.37，單日 +5.3%）；50 日均線 233.84、200 日均線 162.31，股價位於兩條均線之上。
- 52 週高低點 n/a（year_high、year_low 為 NaN）。Beta 1.197。

**估值指標（以 info 與季度資料計算）**

| 指標 | 數值 | 說明 |
|---|---|---|
| 市值 | 245.07 B | 與 price × shares 1,023.9M 一致 |
| 企業價值 EV | 240.91 B | 市值 - 淨現金 4.19 B，一致 |
| Trailing P/E（GAAP） | 3,989x | TTM EPS 0.06（info）；季度 GAAP EPS 加總約 0.03，n/m |
| TTM P/E（non-GAAP） | 約 216x | 239.34 / TTM 1.11 |
| Forward P/E | **148.5x** | 239.34 / forwardEps 1.611 |
| EV/EBITDA | 2,254x（info） | EBITDA 0.107 B；季度 normalized EBITDA 加總 0.437 B 則約 551x，皆 n/m |
| P/S（TTM） | 45.4x | info |
| P/FCF（TTM） | 約 161x | 245.07 / 1.523；若用 info FCF 1.995 則約 123x |
| P/B | 48.0x | 239.34 / BVPS 4.98 |

**相對行業（估計，非工具資料）**
- 大型雲端資安與 SaaS 同業 forward P/E 估計約 40–60x，P/S 約 12–18x，non-GAAP EV/EBITDA 約 40–60x，P/FCF 約 35–50x。此為粗估區間，並非 yfinance 提供之 sector median，僅供量級比較。
- 以此估計，CRWD 各項估值倍數約為同業區間的 2–4 倍，估值溢價明顯。

**分析師共識**
- targetMeanPrice 246.15（相較現價 +2.8%），recommendationKey buy，分析師數 50。共識目標價與現價幾乎持平，上行空間有限。

## Key catalysts
- **下次財報**：2026-12-01（yfinance earnings_dates 列出，屬預估日期，需確認）。預估 EPS 0.31（FY27 Q3）。
- **最近一次財報**：2026-08-26，FY27 Q2 EPS 0.31 vs 預估 0.29（+6.4%），營收 1,470.9 M，YoY +25.8%。
- **EPS 成長催化**：non-GAAP EPS 由 FY26 Q2 的 0.23 升至 FY27 Q2 的 0.31，與去年同季 FY26 Q2（2025-08，EPS 0.23）相比，YoY 約 +35%。forwardEps 1.611 隱含後續年度大幅成長，但 yfinance 未提供 guidance 原文，guidance 為 n/a。
- **遞延收入加速**：遞延收入 YoY +25.7%，為下季營收能見度正向指標。
- **策略合作**：Cognizant（AI 安全）、Snowflake（AI-native 安全與資料）、Fortanix（Confidential AI）；longBusinessSummary 所列，財務影響未揭露。
- **分部轉移**：segment 資料 n/a，無法評估 AI 或新模組佔比變化。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate, 非工具資料) | Verdict |
|---|---|---|---|---|
| 營收（USD M，TTM） | 5,396.1 | FY26 +21.7%；季度 +25.8% | 高成長 SaaS 約 20–30% | 強（高成長） |
| 季度營收（USD M，FY27 Q2） | 1,470.9 | +25.8% | 同上 | 強 |
| 毛利率（TTM） | 75.2% | 與 FY25 持平 | 雲端資安約 70–80% | 優 |
| 營業利益率（TTM） | -2.2% | FY26 -6.1% → TTM -2.2%，改善 | 成熟 SaaS 約 10–20%（non-GAAP） | 弱（GAAP 仍虧） |
| 淨利率（TTM，季度加總） | 約 1.1% | FY26 -3.4% | 同上 | 弱 |
| ROE | 1.46%（info） | FY26 約 -4.2% | 約 10–15% | 弱 |
| FCF 利潤率（TTM） | 28.2% | FY26 25.8% | 約 20–30% | 優 |
| FCF（USD M，TTM，季度加總） | 1,522.6 | FY26 1,241.5（+16.3% vs FY25 1,067.9） | — | 優 |
| FCF / NI（TTM） | 約 26x | n/m | >0.9 為健康 | 數學達標，但 n/m |
| SBC 調整後 FCF（USD M，TTM） | 約 278.6 | — | — | 弱 |
| SBC / 營收（TTM） | 23.1% | FY26 22.8% | 成熟 SaaS 約 10–15% | 弱 |
| 淨現金（USD B） | 4.19 | Jan26 4.41 | — | 優 |
| Current ratio | 1.57 | Jan26 1.77 | 約 1.5–2.5 | 中性 |
| 負債/權益 | 約 16% | — | 約 30–50% | 優 |
| 股本稀釋（基本股數） | — | FY26 +2.2%；稀釋 +4.5%（YoY） | 約 0–2% | 弱 |
| 遞延收入（USD M） | 3,497.1 | +25.7% | — | 優 |
| Forward P/E | 148.5x | — | 約 40–60x | 極度昂貴 |
| P/S（TTM） | 45.4x | — | 約 12–18x | 極度昂貴 |
| P/FCF（TTM） | 約 161x | — | 約 35–50x | 昂貴 |
| 內部人淨賣出（6 個月） | 約 457–485 M USD；0 筆買入 | — | — | 負面 |
| 分析師目標價 | 246.15（+2.8%） | — | — | 中性 |

## Red flags
- **GAAP 獲利接近零**：FY26 淨利 -162.5 M，TTM 淨利僅約 58.5 M，GAAP 每股 EPS 0.06（info）；trailing P/E 達 3,989x，無法作為估值參考。
- **SBC 壓縮真實現金流**：TTM SBC 1,244.0 M 佔營收 23%，扣除 SBC 後 FCF 僅約 278.6 M，較 FCF 表面數字低約 82%。
- **股本持續稀釋**：稀釋後股數 YoY +4.5%，SBC 發放與股本擴張同步，每股價值增長被稀釋。
- **估值極端**：forward P/E 148.5x、P/S 45.4x、P/B 48.0x，遠高於估計的同業區間，任何成長放緩都可能引發估值重估。
- **內部人持續淨賣出**：6 個月約 0.46 B USD，CEO 為主，0 筆買入；雖占市值僅約 0.19%，但方向一致。
- **TTM 營業利益仍為負**：營業利益率 -2.2%，尚未達到損益平衡後的穩定獲利。
- **併購支出上升**：FY26 併購 382.3 M，超過 capex，併購對營收與毛利貢獻未揭露。
- **營收成長減速**：年度 YoY 由 FY24 +36.3% 降至 FY26 +21.7%，但季度 +25.8% 略有回升，需後續確認是否為趨勢。
- **資料品質問題**：(1) info.freeCashflow 1,995 M 與季度加總 1,523 M 不一致；(2) EBITDA 定義差異（info 0.107 B vs 季度加總 0.437 B）；(3) info.trailingEps 0.06 與季度 GAAP EPS 加總約 0.03 不一致；(4) 4 筆內部人交易價格異常（3,090.96 等）；(5) 下次財報日 2026-12-01 為預估；(6) fast_info 為快取資料，非即時報價。
- **資料期限**：本報告 as-of 2026-10-23，價格快取時點為 2026-10-22，內部人交易最新至 2026-10-20，未見 as-of 日之後的財務資料。

FUNDAMENTALS REPORT COMPLETE
