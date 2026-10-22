# Fundamentals — FANUY (Fanuc Corp ADR) as of 2026-10-22

## Executive summary
Fanuc 財務體質極佳：零負債、現金及短期投資 (cash + STI) ¥7,539 億、FY3/2026 FCF ¥2,297 億（FCF/NI 1.38）、ROE 約 10%，但營收 3 年 CAGR 僅約 0.2%，獲利回升主要來自毛利率回升。估值面 trailing P/E 31.3x、forward P/E 27.5x、P/B 2.9x，相對工業機械同業偏貴（估計），且股價低於 50 日與 200 日均線，52 週區間位於低檔附近。整體結論：財務健全但成長動能弱、估值不便宜，且 ADR 流動性極薄（OTC Markets OTCPK，不可交易），需留意執行風險。

資料來源說明：本次 live Yahoo 與 pricefeed 因代理 403 被封鎖，數據全數取自 repo cache `prices/yf/FANUY.json`（refreshed 2026-10-22T11:40:07Z；fast_info 快取 2026-10-22T11:36:58Z）。財報單位為 JPY（yfinance `financialCurrency` = JPY），本報告以 ¥ 表示，單位「億」= 100M JPY。Yahoo 的 `enterpriseValue`、`enterpriseToEbitda`、`priceToSalesTrailing12Months` 因幣別混用而失真，本報告已以 JPY/USD 換算重算，見估值章節。

## Revenue & profitability
- **營收**：FY3/2023 ¥8,519.6 億 → FY3/2024 ¥7,952.7 億 → FY3/2025 ¥7,971.3 億 → FY3/2026 ¥8,578.3 億。
  - FY3/2026 YoY +7.6%。
  - 3 年 CAGR（FY23→FY26）約 +0.2%，4 年資料缺 FY2022（cache 為 null），故無 4-5 年 CAGR。
  - info 的 `revenueGrowth` 0.177 為近季 YoY（TTM 營收 ¥8,925 億，mostRecentQuarter 2026-06-30），顯示近期加速。
- **分部營收**：`longBusinessSummary` 僅列產品線（CNC、robots、robomachine、ROBOT、laser、servo），cache 無分部營收金額，分部占比為 DATA_UNAVAILABLE。
- **毛利率**：FY23 38.2% → FY24 34.7% → FY25 37.0% → FY26 38.3%，已回到 FY23 水準。
- **營業利益率**：FY23 22.5% → FY24 17.9% → FY25 19.9% → FY26 21.4%。營業利益 YoY +15.7%。
- **淨利率**：FY23 20.0% → FY24 16.7% → FY25 18.5% → FY26 19.4%。淨利 ¥1,665.4 億，YoY +12.9%。
- **EBITDA 利益率**：FY26 27.0%（EBITDA ¥2,315.4 億）。
- **EPS**：FY23 ¥89.3、FY24 ¥70.1、FY25 n/a（cache 缺）、FY26 ¥89.2。
- **ROE**：FY26 淨利 / 平均權益 = 9.3%；info 的 TTM ROE 為 10.05%。
- **ROIC（估計）**：NOPAT = EBIT ¥1,837.6 億 × (1 − 25.5% 稅率) ≈ ¥1,369 億。
  - 以總投入資本 ¥18,649 億計，ROIC ≈ 7.3%。
  - 扣除現金與短期投資後，營業用投入資本約 ¥11,110 億，ROIC ≈ 12.3%。
  - 以後者較能反映營運資產效率，但大量現金屬股東資金，兩者都應看。

## Cashflow & balance sheet
- **營業現金流 (OCF)**：FY23 ¥995 億 → FY24 ¥1,718 億 → FY25 ¥2,553 億 → FY26 ¥2,509 億（較 FY25 小幅下滑 1.7%）。
- **資本支出 (capex)**：FY23 ¥470.7 億 → FY24 ¥538.8 億 → FY25 ¥408.1 億 → FY26 ¥211.8 億，連續兩年大幅下降。
- **FCF** = OCF − capex = ¥2,297 億（FY26）。
  - FCF 利益率 26.8%。
  - FCF / NI = 1.38（>0.9，健康）；OCF / NI = 1.51。
  - FCF 歷史：FY23 ¥524 億、FY24 ¥1,179 億、FY25 ¥2,145 億、FY26 ¥2,297 億。
- **資產負債表（FY3/2026）**：
  - 總資產 ¥20,907 億；總負債 ¥2,078 億；股東權益 ¥18,649 億。
  - 現金及約當現金 ¥7,181 億（YoY +21.6%），含短期投資 ¥7,539 億。
  - 流動資產 ¥12,370 億 / 流動負債 ¥1,795 億 → 流動比率 6.89（info TTM 7.34）。
  - 總債務：info `totalDebt` = 0，即淨現金部位，淨負債為負值（淨現金約 ¥7,539 億 − 0）。
  - 負債 / 權益 ≈ 0.11（總負債 / 權益），有息負債為 0。
  - 營運資金 ¥10,576 億。
- **淨現金換算 (USD)**：約 $5.0bn（以推算匯率 151 JPY/USD 換算，見估值章節），相當於 ADR 市值的約 15%。

## Capital allocation & insider signal
- **資本支出 / 營收**：FY23 5.5% → FY26 2.5%。**capex / D&A = 0.44x**（FY26 D&A ¥477.8 億），低於 1x，代表資本支出已明顯低於折舊，需要判斷是產能過剩循環或投資不足。
- **股利**：FY26 股利支付 ¥944.6 億（FY25 ¥831.3 億、FY24 ¥901.0 億、FY23 ¥964.9 億）。
  - 股利 / NI = 56.7%；info `payoutRatio` 0.583。
  - FCF / 股利 = 2.43x，覆蓋充足。
  - 每股股利換算約 ¥50.6（≈ $0.34，info `dividendRate` 0.34，殖利率 1.83%）。
  - 5 年平均殖利率 2.1%（info）。
- **買回**：FY26 買回僅 ¥0.55 億，FY25 ¥49.6 億、FY24 ¥28.4 億、FY23 ¥24.4 億。FY26 買回幾乎停止。
- **現金累積**：FY26 投資活動淨流出 ¥564 億，其中有價證券買入 ¥3,215 億、賣出 ¥2,869 億；現金及短期投資較 FY25 增加約 ¥1,474 億。
- **內部人**：cache 的 `insider` 為空陣列，內部人交易資料為 DATA_UNAVAILABLE。info 的 `heldPercentInsiders` = 0.0，`companyOfficers` 皆為 `exercisedValue` = 0、`unexercisedValue` = 0。
- **機構持股**：`heldPercentInstitutions` 0.229%，`institutionsCount` 27。最大持有人為 Aristotle Capital Management（3,559,342 股，2026-06-30，季減 5.8%）。機構持股比率極低，屬 OTC ADR 特性。

## Valuation
- **Price**：$18.44（cache fast_info，source = cache，52 週區間 $15.11–$27.54；距高點 −33.0%，距 50 日均線 −3.2%，距 200 日均線 −10.9%）。
- **P/E**：trailing 31.3x（info 31.25）；forward 27.5x（forwardEps $0.67）；PEG 2.45（info）。
- **P/B**：2.88x（bookValue $6.41 / ADR）。
- **EV 與 EBITDA（重算）**：
  - 市值 $34.11bn，淨現金 ¥762.3bn（TTM）≈ $5.04bn（推算 151 JPY/USD），EV ≈ $29.1bn ≈ ¥4,395 億。
  - EV/EBITDA TTM（EBITDA ¥2,429 億）≈ 18.1x；FY26（EBITDA ¥2,315 億）≈ 19.0x。
  - Yahoo 的 `enterpriseValue` 為 −$710.5bn、`enterpriseToEbitda` −2.9x，明顯是 JPY 現金與 USD 市值相減所致，不可使用。
- **P/FCF**：FY26 FCF ¥229.7bn ≈ $1.52bn，P/FCF ≈ 22.5x。
- **P/S（重算）**：TTM 營收 ¥8,925 億 ≈ $5.90bn，P/S ≈ 5.8x（Yahoo 的 0.038 為幣別錯誤）。
- **分析師**：2 位，皆為 Hold（strongBuy/buy/sell 皆 0）。目標價 mean $21.72、median $21.72、high $22.81、low $20.63，相對現價 +17.8%。覆蓋極薄，參考價值有限。
- **同業比較（estimate）**：工業自動化同業（機器人、CNC、工具機控制）trailing P/E 約 25–30x、EV/EBITDA 約 14–18x、P/S 約 2–4x、ROE 約 12–15%。Fanuc 的估值相對同業偏貴，但淨現金與 FCF 強度可部分支撐。此為估計值，非實際 cache 數據。

## Key catalysts
- **下次財報**：2026-10-30（yfinance earnings_dates，EPS 預估 $0.13，ADR 口徑）。距離本次 as-of 日 8 天。
- **近期 EPS 公布紀錄**（ADR 口徑）：
  - 2026-07-31：實際 $0.17 vs 預估 $0.17（−0.97%）
  - 2026-04-24：實際 $0.17 vs 預估 $0.13（+23.9%）
  - 2026-01-26：實際 $0.09 vs 預估 $0.14（−33.9%）
  - 2025-10-31：實際 $0.15 vs 預估 $0.13（+8.7%）
  - 2025-07-25：實際 $0.14 vs 預估 $0.13（+7.3%）
  - 2025-04-23：實際 $0.17 vs 預估 $0.03（+473%，基數過小）
  - 結論：公布結果有波動，但以正向 beat 為主。
- **管理層指引**：cache 無公司指引資料，DATA_UNAVAILABLE。
- **分部變化**：cache 無分部營收，DATA_UNAVAILABLE。
- **除息日**：`exDividendDate` 為 2026-03-31（已過），下次除息日 n/a。
- **資料後置提醒**：cache 內無 as-of 日之後的財務資料，所有數據皆為 as-of 以前。唯一前瞻資訊為 2026-10-30 財報日與 analyst 目標價。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (Revenue, ¥億) | 8,578.3 (FY3/26) | +7.6% | n/a | 中性：短期回升，3 年 CAGR 僅 +0.2% |
| 毛利率 (Gross margin) | 38.3% | +1.3pp | 約 35–40% | 中性偏佳，已回到 FY23 水準 |
| 營業利益率 (Operating margin) | 21.4% | +1.5pp | 約 15–20% | 佳 |
| 淨利率 (Net margin) | 19.4% | +0.9pp | 約 12–15% | 佳 |
| EBITDA 利益率 | 27.0% | +1.2pp | 約 20–25% | 佳 |
| ROE | 9.3% (平均權益) / 10.05% (TTM) | — | 約 12–15% | 偏弱 |
| ROIC (扣除超額現金) | 12.3%（估計）/ 7.3%（含現金） | — | 約 10–12% | 中性 |
| OCF (¥億) | 2,509.0 | −1.7% | n/a | 中性，與 NI 同步 |
| FCF (¥億) | 2,297.2 | +7.1% | n/a | 佳 |
| FCF 利益率 | 26.8% | — | 約 10–15% | 佳 |
| FCF / NI | 1.38 | — | >0.9 健康 | 佳 |
| Capex / 營收 | 2.5% | 下降（FY25 5.1%） | 約 4–6% | 偏低，需留意 |
| Capex / D&A | 0.44x | — | 約 1.0–1.2x | 紅旗：投資不足或循環尾端 |
| 現金及短期投資 (¥億) | 7,538.7 | +24.3% | n/a | 佳，淨現金部位 |
| 總債務 (Total debt) | 0 | — | 工業股中位數低 | 佳 |
| 流動比率 (Current ratio) | 6.89 | — | 約 2.0 | 佳 |
| 負債 / 權益 | 約 0.11 | — | 約 0.5 | 佳 |
| 股利覆蓋 (FCF / 股利) | 2.43x | — | >1.5x | 佳 |
| 股利 / NI (payout) | 56.7% | — | 約 40–50% | 中性偏高 |
| 股利殖利率 | 1.83% | — | 約 2–3% | 中性 |
| 買回 (¥億) | 0.55 | 大幅下降（FY25 49.6） | n/a | 偏弱 |
| 內部人持股 / 交易 | 0% / DATA_UNAVAILABLE | — | — | 無法判斷 |
| 機構持股 | 0.23% | — | 約 — | 偏低（OTC ADR 特性） |
| Trailing P/E | 31.3x | — | 約 25–30x | 偏貴 |
| Forward P/E | 27.5x | — | 約 22–26x | 偏貴 |
| P/B | 2.88x | — | 約 2–3x | 中性 |
| EV/EBITDA (重算, TTM) | 約 18.1x | — | 約 14–18x | 中性偏貴 |
| P/FCF | 約 22.5x | — | 約 20–25x | 中性 |
| P/S (重算, TTM) | 約 5.8x | — | 約 2–4x | 偏貴 |
| 股價 vs 200 日均線 | −10.9% | — | — | 弱勢 |
| 分析師目標價 (mean) | $21.72 (+17.8%) | — | — | 覆蓋僅 2 位 |
| 流動性 (3 個月平均成交量) | 約 518k 股（約 $9.6mn/日） | — | — | 紅旗：OTCPK，不可交易 |

## Red flags
- **流動性與可交易性**：ADR 在 OTC Markets OTCPK 掛牌，yfinance `tradeable` = false；今日成交量 31,207 股，遠低於 3 個月平均 518k 股，bid/ask 價差 $0.02，執行成本與滑價風險高。
- **成長動能弱**：FY23–FY26 營收 3 年 CAGR 僅約 0.2%，FY26 的 +7.6% 仍低於 FY23 水準；獲利回升主要來自毛利率與成本，而非量的成長。
- **資本支出大幅下降**：capex 由 FY23 ¥470.7 億降至 FY26 ¥211.8 億，capex/D&A 僅 0.44x，可能反映產能利用率低或未來投資不足。
- **股價趨勢弱勢**：現價 $18.44 低於 50 日 ($19.05) 與 200 日 ($20.69) 均線，距 52 週高點 −33%。
- **估值偏貴**：trailing P/E 31x、forward P/E 27.5x、P/S 約 5.8x，相對工業自動化同業明顯溢價（估計）。
- **資料品質**：Yahoo `enterpriseValue`（−$710.5bn）、`enterpriseToEbitda`（−2.9x）、`priceToSalesTrailing12Months`（0.038）皆因 JPY/USD 混用失真，已棄用；股數口徑在資產負債表（Ordinary Shares 9.3 億）與損益表（Diluted 18.7 億）不一致，每股數據換算需再確認。
- **覆蓋與揭露不足**：分析師僅 2 位（皆 Hold）；內部人交易、管理層指引、分部營收皆為 DATA_UNAVAILABLE；機構持股 0.23%。
- **買回停止**：FY26 買回僅 ¥0.55 億，現金卻累積至 ¥7,539 億，資本配置偏保守，股東報酬主要依賴股利。
- **ROE 偏低**：TTM ROE 約 10%，淨現金龐大拖累 ROE，資本效率有待改善。
- **財報事件**：2026-10-30 財報為近期催化劑，過去 6 季 EPS surprise 波動大（−33.9% 至 +23.9%）。

FUNDAMENTALS REPORT COMPLETE
