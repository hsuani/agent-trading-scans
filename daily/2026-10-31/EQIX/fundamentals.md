# Fundamentals — EQIX (Equinix Inc) as of 2026-10-31

> **資料時點**：分析基準日 2026-10-31。股價為 2026-10-29 收盤 $1,036.67（yfinance 快取，寫入時間 2026-10-30 12:43 UTC）；財報明細至 2026-06-30 季（Q2'26）。2026-10-28 盤後公布的 Q3'26 僅有 EPS 與預期值（earnings_dates），完整損益表與營運指引在工具輸出中不可得，標示為 DATA_UNAVAILABLE。Q3'26 的營收、毛利、淨利為由 info TTM 欄位與季報相減推算，文中均註明「推算」。全文單位：USD，以 B（十億美元）與 M（百萬美元）表示，不使用 億。

## Executive summary

Equinix 營運面明顯改善：FY2025 營收 $9.217B（+5.4% YoY），Q2'26 營收 $2.625B（+16.4% YoY），Q3'26 標準化 EPS $5.22 高於預期 $3.96（+31.85%），GAAP 營業利益率由 FY24 的 15.2% 升至 FY25 的 20.0%。財務體質則承壓：FY25 FCF 為 -$0.40B，TTM FCF（至 Q2'26）為 -$1.46B，淨負債由 FY24 年底 $12.13B 增至 Q2'26 的 $18.73B（約 4.1x normalized EBITDA），TTM 股利 $1.96B 須仰賴 OCF 與新增舉債支應。估值偏高：trailing P/E 62.3x、forward P/E 51.5x、EV/EBITDA 27.0x、P/FFO 簡易代理值約 27.6x；官方 FFO/AFFO 與同業中位數皆為 DATA_UNAVAILABLE，故估值吸引力只能就成長性與槓桿面做部分判讀。

## Revenue & profitability

**年度趨勢（USD B / %）**

| 年度 | 營收 (USD B) | YoY | 毛利率 | GAAP 營業利益率 | 淨利率 | 稀釋 EPS (USD) |
|---|---|---|---|---|---|---|
| FY22 | 7.263 | — | 48.4% | 16.5% | 9.7% | 7.67 |
| FY23 | 8.188 | +12.7% | 48.4% | 17.6% | 11.8% | 10.31 |
| FY24 | 8.748 | +6.8% | 48.9% | 15.2% | 9.3% | 8.50 |
| FY25 | 9.217 | +5.4% | 51.1% | 20.0% | 14.6% | 13.76 |

- 營收 3 年 CAGR（FY22–FY25）為 8.3%。GAAP 營業利益 CAGR 為 15.5%（$1.200B → $1.848B），稀釋 EPS CAGR 為 21.5%（$7.67 → $13.76）。
- FY25 淨利 $1.350B，較 FY24 的 $0.815B 增 65.6%。FY24 含 $0.233B 減損（Impairment Of Capital Assets）與 $0.233B 核銷（Write Off），故 FY25 獲利躍升有基期效應。FY25 其他收益與費用由 FY24 的 -$0.329B 改善至 -$0.124B，但個別驅動因素需 10-K 原文，工具輸出不含，標示 DATA_UNAVAILABLE。
- 分部營收拆分（segment mix）：info.longBusinessSummary 僅描述業務屬性（數位基礎設施、資料中心、互連生態系），未提供分部營收數字，DATA_UNAVAILABLE。

**季度趨勢（USD B / %）**

| 季度 | 營收 (USD B) | YoY | 毛利率 | GAAP 營業利益率 | 淨利 (USD B) | 稀釋 EPS (USD) |
|---|---|---|---|---|---|---|
| Q2'25 | 2.256 | n/a | 52.0% | 21.9% | 0.368 | 3.75 |
| Q3'25 | 2.316 | n/a | 50.7% | 20.5% | 0.374 | 3.81 |
| Q4'25 | 2.420 | n/a | 50.5% | 17.4% | 0.265 | 2.69 |
| Q1'26 | 2.444 | n/a | 51.5% | 23.6% | 0.415 | 4.20 |
| Q2'26 | 2.625 | +16.4% | 53.1% | 25.3% | 0.479 | 4.83 |
| Q3'26（推算） | ≈2.658 | ≈+14.8% | ≈52.7% | DATA_UNAVAILABLE | ≈0.489 | ≈4.9 |

- Q2'26 淨利 $0.479B，較 Q2'25 的 $0.368B 增 30.2%。毛利率與營業利益率皆較 Q2'25 提升（+1.1pp、+3.4pp）。
- Q3'26 推算方式：info TTM 營收 $10.147B 減去 Q4'25 至 Q2'26 三季合計 $7.485B 得 ≈$2.658B；同理 TTM 淨利 $1.648B 推算 Q3'26 淨利 ≈$0.489B。
- 標準化 EPS（earnings_dates 的 Reported EPS，接近 normalized 口徑）：Q3'25 $3.89、Q4'25 $3.37（較預期 -13.0%）、Q1'26 $4.17（-3.8%）、Q2'26 $5.10（+6.3%）、Q3'26 $5.22（+31.9%）。近八季盈餘驚喜不一致，Q4'25 與 Q1'26 為不及預期。
- 獲利能力：info ROE（TTM）11.45%；以 FY25 淨利除以平均股東權益（$13.84B）估算為 9.8%。ROIC 簡易估算：FY25 GAAP 營業利益 $1.848B × (1 - 有效稅率 10.6%) = $1.652B，除以平均投入資本 $30.90B，約 5.3%（年底投入資本 $33.07B 計為 5.0%）。

## Cashflow & balance sheet

**現金流量（USD B）**

| 年度 | OCF | Capex | FCF (OCF - Capex) | FCF / NI | Capex / 營收 | 股利支付 |
|---|---|---|---|---|---|---|
| FY22 | 2.963 | 2.278 | 0.685 | 0.97 | 31.4% | 1.152 |
| FY23 | 3.217 | 2.781 | 0.436 | 0.45 | 34.0% | 1.375 |
| FY24 | 3.249 | 3.066 | 0.183 | 0.22 | 35.0% | 1.643 |
| FY25 | 3.911 | 4.311 | -0.400 | -0.30 | 46.8% | 1.856 |
| TTM（至 Q2'26） | 3.942 | 5.406 | -1.464 | n/a | n/a | 1.957 |

- FCF 品質：FY22–FY23 的 FCF/NI 尚可（0.97、0.45），FY24 降至 0.22，FY25 轉為 -0.30，遠低於 0.9 的健康門檻。FY25 OCF 年增 20.4%，但 Capex 年增 40.6%，吃掉全部營運現金流。
- Q2'26 單季 OCF $1.067B（YoY +13.0%），Capex $1.578B（YoY +59.6%），單季 FCF 為 -$0.511B。
- **REIT 指標**：官方 FFO（Nareit 定義）與公司定義 AFFO 在工具輸出中皆不存在，標示 DATA_UNAVAILABLE，無法直接判讀 AFFO 覆蓋率與 AFFO/股。
- 簡易代理（非 Nareit、非公司定義，僅供參考）：NI + D&A。TTM（Q3'25–Q2'26）NI $1.533B + D&A $2.185B = $3.718B，除以 Q2'26 稀釋股數 99.136M，約 $37.50/股；FY25 為 $3.416B，約 $34.8/股。此代理值未扣除維持性 Capex，且 Capex 多為擴張性，因此不能視為 AFFO。

**資產負債表（USD B）**

| 項目 | Q2'25 (6/30/25) | FY25 (12/31/25) | Q2'26 (6/30/26) |
|---|---|---|---|
| Total debt | 21.851 | 22.726 | 23.356 |
| Net debt | 14.275 | 17.185 | 18.730 |
| Cash & ST investments | 4.532 | 3.227 | 2.224 |
| Cash & equivalents | 3.660 | 1.727 | 0.979 |
| Total assets | 38.849 | 40.141 | 41.076 |
| Stockholders' equity | 14.084 | 14.156 | 14.382 |
| Goodwill + intangibles | 7.371 | 7.300 | 7.116 |
| Current ratio | 1.54x | 1.32x | 1.13x |

- 淨負債：Q2'26 $18.73B，較 Q2'25 增 31.2%，較 FY24 年底 $12.13B 增 54.4%。以 normalized EBITDA TTM $4.579B 計，淨負債/EBITDA 約 4.1x（FY24 為 3.2x，FY25 為 4.1x）。
- 利息保障：TTM EBIT（Yahoo 口徑）$2.274B ÷ TTM 利息費用 $0.569B ≈ 4.0x。
- 短期流動性：Q2'26 現金與短期投資 $2.224B，對應短期債務與租賃負債 $1.511B（Current Debt $1.179B + Current Capital Lease $0.332B），覆蓋約 1.5x。流動比率由 Q2'25 的 1.54x 降至 1.13x。info 顯示 currentRatio 為 1.04。
- 負債權益比：info debtToEquity 為 181.5%（口徑含租賃等項目）；以季報 Total Debt / 股東權益計算為 162%（Q2'26 $23.356B ÷ $14.382B）。兩者口徑不同，已於資料注意事項說明。
- **債務到期結構（maturity schedule）**：工具輸出無分年到期表，DATA_UNAVAILABLE。目前僅能確認 Q2'26 流動負債中的債務為 $1.18B，長期債務為 $18.53B。
- 上市 REIT 之 Net debt/Total assets 約 46%（$18.73B ÷ $41.08B）。

## Capital allocation & insider signal

**資本配置**

- Capex：FY25 $4.311B（+40.6%），Q2'26 $1.578B（+59.6%）。Capex 強度（占營收比）由 FY22 的 31.4% 升至 FY25 的 46.8%，資本支出仍在擴張期。Capex 的專案明細與投資報酬預期工具輸出未提供，DATA_UNAVAILABLE。
- 融資：FY25 舉債流入 $4.311B、償還 $1.355B，淨舉債 $2.956B。H1'26 舉債流入 $2.419B（Q1 $1.492B、Q2 $0.927B），償還 $1.471B，淨舉債 $0.948B。
- 股利：年化股利 $20.64（季配 $5.16），殖利率 1.99%（5 年平均 1.88%）。info payoutRatio 為 121%。以 TTM 標準化 EPS $17.86 計，payout 約 116%；以 GAAP TTM 稀釋 EPS 計約 133%。
- 股利覆蓋：FY25 OCF/股利 = 2.11x（FY24 為 1.98x），但 FCF/股利 = -0.22x，即股利未由自由現金流覆蓋。以 NI + D&A 簡易代理計，股利覆蓋約 1.8x，然而該代理未扣除 Capex，結論需以 AFFO（DATA_UNAVAILABLE）驗證。
- 回購：現金流量表與工具輸出中無回購紀錄，判定為無回購。股權發行：FY24 $1.673B、FY25 $0.099B。
- 股本稀釋：普通股數由 FY22 的 92.6M 增至 FY25 的 98.2M，CAGR 約 2.0%/年；Q2'26 為 98.7M（稀釋平均 99.136M）。
- 併購與投資（FY25）：企業收購 $0.311B、投資性不動產購置 $0.994B、淨投資買賣 -$0.962B。

**內部人交易（Yahoo insider 資料，2026-05-01 至 2026-10-30）**

| 日期 | 內部人 | 職位 | 股數 | 金額 (USD M) | 性質 |
|---|---|---|---|---|---|
| 2026-05-06 | Meyers Charles John | Executive Chairman / Director | 5,224 | 5.67 | 賣出（$1,081.92–1,089.26） |
| 2026-05-18 | Paisley Christopher B. | Director（間接持有） | 125 | 0.13 | 賣出 |
| 2026-06-02 | Fox-Martin Adaire | CEO | 2,935 | 3.10 | 賣出（$1,052.25–1,061.53） |
| 2026-06-02 | Lin Jonathan / Pletcher Kurt / Abdel Raouf F | Officer | 150 / 79 / 158 | 0.16 / 0.08 / 0.17 | 賣出 |
| 2026-06-08 | Morandi Brandi Galvin | Chief People Officer | 3,726 | 4.01 | 賣出（$1,076.36） |
| 2026-08-03 | Paisley Christopher B. | Director（間接持有） | 4,000 | 4.08 | 賣出（$1,019.28） |
| 2026-08-18 / 08-20 | Paisley / Pletcher Kurt | Director / Officer | 125 / 135 | 0.14 / 0.15 | 賣出 |
| 2026-09-02 / 09-04 | Paladin Michael Shane | EVP & Chief Customer and Revenue Officer | 203 / 307 | 0.21 / 0.32 | 賣出 |

- 6 個月窗口內有價格的公開市場賣出合計 17,167 股、約 USD 18.21M；買進 0 筆。以市值 $102.62B 計，賣出金額占比約 0.018%；內部人持股比例 0.27%（heldPercentInsiders）。
- 另有無價格紀錄的交易（2026-05-21 董事 6 筆合計 1,633 股、2026-06-01 合計 6,464 股、2026-09-01 Paladin 510 股、2026-05-06 Morandi 贈與 112 股）。多集中於特定歸屬日，可能為股權獎勵歸屬或扣繳性質，需以 Form 4 交易代碼核實，工具輸出未提供，標示 DATA_UNAVAILABLE。
- 窗口前背景：CEO Fox-Martin 於 2026-02-18（$3.95M）與 2026-03-12（$1.05M）賣出，Meyers 於 2026-03-04 賣出 $2.62M，成交價約 $925–970。目前股價較當時賣出價區間高約 7–12%。
- 判讀：內部人以賣出為主且金額相對市值極小，屬於例行性減持的可能性高於強烈負向訊號；但連續多月的賣出仍是需要記錄的負向訊號。
- 機構持股：2,005 家機構，institutionsPercentHeld 為 100.6%（超過 100% 屬資料口徑異常）。Short interest 為 1.62M 股，佔流通股 1.87%，short ratio 3.33 天。

## Valuation

**估值倍數（以 $1,036.67 計）**

- 市值 $102.62B，企業價值 EV $126.68B（info）。
- Trailing P/E 62.3x（trailingEps $16.65）；以 Yahoo earnings_dates 標準化 EPS TTM $17.86 計約 58.0x；forward P/E 51.5x（forwardEps $20.125）；FY2026 EPS 預估 $18.155 對應 P/E 57.1x。PEG 2.99。
- EV/EBITDA 27.0x（TTM EBITDA $4.69B）；EV/Revenue 12.5x；P/S 10.1x；P/B 7.06x（每股淨值 $146.86）。
- P/FFO 簡易代理值 27.6x（$1,036.67 ÷ $37.50）。官方 P/FFO 與 P/AFFO 為 DATA_UNAVAILABLE。
- P/FCF：TTM FCF 為負，倍數不適用（n/a）。
- 同業中位數（sector median）：工具輸出無同業資料，全部 DATA_UNAVAILABLE，無法判斷相對估值是否偏貴或偏便宜。

**市場與分析師背景**

- 股價 52 週區間 $720.62–$1,128.68，距高點 -8.2%，距低點 +43.9%；12 個月動能 +27.0%。收盤位於 MA20 之上 3.3%、MA50 之上 1.3%、MA200 之上 2.7%。RSI(14) 57.8、MACD 柱狀體為正（+4.24）、BB %B 0.80。
- 分析師（32 家）平均目標價 $1,235.72（較現價 +19.2%），中位數 $1,230，區間 $1,100–$1,380；推薦均值 1.46（strong buy 區段）。
- 以上為市場參考資訊，非本報告之交易建議。

## Key catalysts

1. **Q3'26 財報（2026-10-28 盤後，已公布）**：標準化 EPS $5.22 對比預期 $3.96，驚喜 +31.85%；隔日（10-29）股價收於 $1,036.67，單日 +2.88%。營收與營運指引的正式文字 DATA_UNAVAILABLE，需由 10-K 或法說會稿件補充。
2. **除息日 2026-11-18**：每股 $5.16（corporateActions 公告）。
3. **下一次財報**：Yahoo 排程為 2027-02-10（FY26 Q4），預估 EPS $4.02。
4. **資本支出與再融資節奏**：H1'26 Capex $2.834B，淨舉債 $0.948B。後續的債務到期與再融資條件、Capex 完工後的營收貢獻，是觀察重點，工具輸出中無相關明細。
5. **估值與共識**：分析師目標價中位數較現價高約 18.7%，但 trailing P/E 與 EV/EBITDA 位於高位，業績能否持續超預期是關鍵。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 FY25 (USD B) | 9.217 | +5.4% | DATA_UNAVAILABLE | 穩健 |
| 營收 Q2'26 (USD B) | 2.625 | +16.4% | DATA_UNAVAILABLE | 加速 |
| 營收 TTM (USD B, info) | 10.147 | +10.4% (revenueGrowth) | DATA_UNAVAILABLE | 改善 |
| 毛利率 FY25 | 51.1% | +2.2pp | DATA_UNAVAILABLE | 改善 |
| GAAP 營業利益率 FY25 | 20.0% | +4.8pp | DATA_UNAVAILABLE | 改善 |
| 淨利率 FY25 | 14.6% | +5.3pp | DATA_UNAVAILABLE | 改善 |
| ROE (info TTM) | 11.45% | n/a | DATA_UNAVAILABLE | 中等 |
| ROIC (簡易估算 FY25) | 5.0%–5.3% | n/a | DATA_UNAVAILABLE | 偏低 |
| OCF FY25 (USD B) | 3.911 | +20.4% | DATA_UNAVAILABLE | 強 |
| FCF FY25 (USD B) | -0.400 | 由 +0.183 轉負 | DATA_UNAVAILABLE | 弱 |
| FCF TTM (USD B) | -1.464 | n/a | DATA_UNAVAILABLE | 弱 |
| FCF / NI FY25 | -0.30 | 0.22 → -0.30 | >0.9 為健康門檻 | 不健康 |
| Capex / 營收 FY25 | 46.8% | +11.8pp | DATA_UNAVAILABLE | 高，擴張期 |
| 淨負債 Q2'26 (USD B) | 18.730 | +31.2% | DATA_UNAVAILABLE | 上升 |
| 淨負債 / normalized EBITDA (TTM) | 4.1x | FY24 3.2x → 4.1x | DATA_UNAVAILABLE | 偏高 |
| 利息保障 (TTM EBIT / 利息) | 4.0x | n/a | DATA_UNAVAILABLE | 尚可 |
| 流動比率 Q2'26 | 1.13x | Q2'25 1.54x | DATA_UNAVAILABLE | 偏緊 |
| 負債權益比 (info) | 181.5% | n/a | DATA_UNAVAILABLE | 偏高（口徑含租賃） |
| 官方 FFO / AFFO | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判讀 |
| 股利殖利率 | 1.99% | 5 年平均 1.88% | DATA_UNAVAILABLE | 中性 |
| 股利覆蓋 OCF / 股利 FY25 | 2.11x | FY24 1.98x | DATA_UNAVAILABLE | 尚可 |
| 股利覆蓋 FCF / 股利 FY25 | -0.22x | n/a | DATA_UNAVAILABLE | 未覆蓋 |
| P/FFO（簡易代理，非官方） | 27.6x | n/a | DATA_UNAVAILABLE | 偏高 |
| Trailing P/E | 62.3x | n/a | DATA_UNAVAILABLE | 偏高 |
| Forward P/E | 51.5x | n/a | DATA_UNAVAILABLE | 偏高 |
| EV/EBITDA (TTM) | 27.0x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/S (TTM) | 10.1x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/FCF | n/a（FCF 為負） | n/a | DATA_UNAVAILABLE | 不適用 |
| 內部人賣出 (6 mo, USD M) | 18.21（買進 0 筆） | n/a | DATA_UNAVAILABLE | 小比例、偏負向 |
| 分析師平均目標價 (USD) | 1,235.7（+19.2%） | n/a | DATA_UNAVAILABLE | 正向（sell-side） |

## Red flags

- **自由現金流為負**：FY25 FCF -$0.40B、TTM -$1.46B，股利（TTM $1.96B）由 OCF 支應但未由 FCF 覆蓋，持續性取決於 Capex 能否回落或營收能否快速轉換為現金。
- **淨負債快速上升**：Q2'26 淨負債 $18.73B（YoY +31.2%），淨負債/EBITDA 由 3.2x 升至 4.1x；H1'26 淨舉債 $0.95B。
- **流動性收緊**：現金由 FY24 的 $3.08B（現金與等價物口徑）降至 Q2'26 的 $0.98B，流動比率 1.13x。
- **官方 AFFO 缺失**：無法驗證股利是否由 AFFO 覆蓋，payout ratio 121% 為紅旗項目。
- **估值極高**：trailing P/E 62.3x、PEG 2.99、EV/EBITDA 27.0x、P/FFO 簡易代理值 27.6x。若業績不及預期，估值壓縮風險高。
- **盈餘驚喜不穩定**：近八季中 Q4'25（-13.0%）與 Q1'26（-3.8%）不及預期，Q3'26 +31.9% 為單季高點，需留意一次性或會計因素（工具未提供細項）。
- **內部人持續賣出**：6 個月窗口內 17,167 股、約 $18.2M 公開市場賣出，0 筆買進；另有 2026-02 至 2026-03 的 CEO 賣出。金額相對市值小，但方向一致。
- **治理風險評分偏高**（Yahoo 評分，數值越高風險越大）：board risk 8、compensation risk 7，overall risk 3。
- **資料注意事項**：
  - info freeCashflow 為 $3.18B，與季度現金流表推算之 TTM FCF -$1.46B 差距過大，本報告採用現金流量表口徑，info 欄位不採用。
  - 2025 年報與季報的資產負債表部分項目不一致（例如 Gross PPE、Accounts Payable 在 FY25 與 Q2'26 之間的分類差異），本報告以季報 Q2'26 為最新值。
  - institutionsPercentHeld 為 100.6%，屬資料口徑異常。
  - info totalDebt $26.41B 與季報 Total Debt $23.36B 口徑不同，本報告以季報為主、info 為輔。
  - 近期 earnings_dates 的 EPS 預估值序列有跳動（例如 Q2'26 預估 $4.80、Q3'26 預估 $3.96），預估值可靠度有限。

FUNDAMENTALS REPORT COMPLETE
