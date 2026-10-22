# Fundamentals — SYM (Symbotic Inc.) as of 2026-10-22

## Executive summary
SYM 營收動能強勁（Q3 FY26 營收 720.8M，YoY +21.7%；3 年 CAGR 約 55.9%），毛利率由 FY25 的 18.8% 持續走高至 Q3 FY26 的 22.3%，營業利益於 FY26 前三季首度轉正，帳上現金 1,746.4M、負債僅 25.8M，短期償債與淨現金部位尚屬穩健。然而 TTM 歸屬母公司淨利僅 8.2M（GAAP trailing EPS 0.08），ROE 僅 4.4%，trailing P/E 高達 521.6x、forward P/E 56.1x，估值已大幅領先獲利；加上 Q3 FY26 營業現金流與自由現金流轉負、應收帳款暴增、股本 9 個月內增加 14.5%，以及 SoftBank 於 2026-05 大額出售（281.8M）與 31.8% 的 short float，綜合判斷財務體質（現金面）尚可、但估值缺乏獲利支撐，估值吸引力偏低。

資料說明：本報告所有數值以 `prices/yf/SYM.json` 快取（`_refreshed_at` 2026-10-22 11:41 UTC，symbol 已驗證為 SYM）為準。即時 yfinance 輸出於本次執行時曾回傳 TSLA 資料（跨 ticker 污染），已排除。最新財報期間為 2026-06-30（Q3 FY26）；下次財報日 2026-11-16 位於 as-of 之後，屬預定事件。

## Revenue & profitability

**營收與成長**
- 年度營收（FY 結束於 9 月底）：FY22 593.3M → FY23 1,176.9M → FY24 1,788.2M → FY25 2,246.9M。
- YoY：FY24 +51.9%、FY25 +25.7%。3 年 CAGR（FY22–FY25）約 55.9%；2 年 CAGR（FY23–FY25）約 38.2%。
- 季度營收：Q3 FY25 592.1M → Q4 FY25 618.5M → Q1 FY26 630.0M → Q2 FY26 676.5M → Q3 FY26 720.8M。Q3 FY26 YoY +21.7%，季增 +6.6%；Q2 季增 +7.4%，Q1 季增 +1.9%。TTM 營收 2,645.8M，與 info 的 totalRevenue 2,645.76M 一致。
- 分部：info 的 longBusinessSummary 僅描述單一自動化倉儲業務，未提供分部營收，分部 mix 為 DATA_UNAVAILABLE。

**獲利能力趨勢**
- 毛利率（年）：FY22 16.8%、FY23 16.1%、FY24 13.7%、FY25 18.8%。TTM 約 21.6%（info grossMargins 21.3%）。季度：Q3 FY25 18.9% → Q4 FY25 20.6% → Q1 FY26 21.2% → Q2 FY26 22.2% → Q3 FY26 22.3%。
- 營業利益率（年）：FY22 -23.7%、FY23 -19.0%、FY24 -6.5%、FY25 -4.1%。季度：Q3 FY25 -1.6%、Q4 FY25 -2.5%、Q1 FY26 +1.5%、Q2 FY26 +0.9%、Q3 FY26 +4.6%（營業利益 32.9M）。TTM 營業利益率約 +1.25%（由季度加總計算；info operatingMargins 為 4.59%，兩者不一致，見 Red flags）。
- 費用結構：Q3 FY26 R&D 43.8M（YoY 約 -12%，Q3 FY25 為 49.7M）；SG&A 84.2M（YoY 約 +18%，Q3 FY25 為 71.6M）。FY25 R&D 216.0M、SG&A 298.7M。
- 淨利：FY25 歸屬普通股淨利 -16.9M（EPS -0.16）；TTM 歸屬普通股淨利 8.2M（info netIncomeToCommon），淨利率 0.31%，已接近損益兩平。Q3 FY26 季度 diluted EPS 0.09。
- ROE：info 為 4.39%；FY25 以 FY25 期末權益計算約 -7.7%。ROA（info）0.32%。
- ROIC：工具未提供，估算（TTM 營業利益 32.9M ÷ 〔權益 708.8M + 負債 25.8M〕）約 4.5%（稅前），屬估算值。

## Cashflow & balance sheet

**現金流量品質**
- 年度 OCF：FY22 -148.2M、FY23 +230.8M、FY24 -58.1M、FY25 +866.9M；年度 FCF：FY25 787.9M（FCF margin 35.1%），FY24 -102.5M。
- 季度 OCF：Q4 FY25 530.7M、Q1 FY26 191.5M、Q2 FY26 261.3M、Q3 FY26 **-147.3M**；Q3 FY26 FCF **-164.6M**。
- TTM（季度加總）：OCF 836.3M、資本支出 99.0M、FCF 737.3M，FCF margin 27.9%。info 的 operatingCashflow 894.4M、freeCashflow 547.6M 與季度加總不一致，本報告以季度加總為準。
- FCF / NI：TTM NI 僅 8.2M，比值約 90x，屬 n/m（無意義）；FY25 NI 為負，比值亦 n/m。FCF 顯著高於 NI 的主要來源為 SBC（FY25 183.9M，占營收 8.2%；TTM 約 207.3M，占 7.8%）與折舊攤銷（FY25 44.1M）及營運資金變化，而非淨利本身，品質需保留。
- 營運資金風險：應收帳款由 FY25 期末 368.4M 升至 Q3 FY26 748.4M（+103%），DSO 由約 60 天升至約 95 天（以季營收 ×91 估算）；存貨 220.8M（FY25 期末 164.4M）。Q3 FY26 營業現金流轉負主要與應收增加相關。

**資產負債表（2026-06-30）**
- 現金及約當現金 1,746.4M（FY25 期末 1,245.0M；Q3 FY25 777.6M）。Q1 FY26 有 424.4M 股權發行（季度 CF Net Common Stock Issuance）。
- 總負債（info totalDebt）25.8M；淨現金約 1,720.6M（現金減負債，未計少數股權）。
- 總資產 3,524.1M；流動資產 2,857.8M；流動負債 2,147.1M。流動比率 1.33（info currentRatio 1.331，與季度數字一致；FY25 期末為 1.09）；速動比率 1.16（info quickRatio）。營運資金 710.7M。
- 權益：歸屬母公司權益 708.8M，少數股權 425.2M，權益合計 1,134.0M（FY25 期末少數股權 261.9M）。少數股權持續增加，歸屬母公司的獲利與淨資產需扣除此部分。
- 負債權益比（以含少數股權權益計）約 2.3%（info debtToEquity 2.278，為百分比單位）；以歸屬母公司權益計約 3.6%（25.8M ÷ 708.8M）。
- 商譽 59.9M（FY25 因 Purchase Of Business 141.8M 增加）。

## Capital allocation & insider signal

**資本配置**
- 資本支出：FY22 18.0M、FY23 21.3M、FY24 44.4M、FY25 79.0M（占營收 3.5%）；TTM 99.0M（占營收 3.7%），資本支出呈上升趨勢但占比仍低。
- 併購：FY25 Purchase Of Business 141.8M（其他細節 DATA_UNAVAILABLE）。
- 股利與回購：無股息（dividendYield 0），無回購紀錄；股息覆蓋率 n/a。
- 股權融資與稀釋：普通股股數由 FY22 57.7M 增至 FY23 82.1M、FY24 104.7M、FY25 112.6M，2026-06-30 為 128.9M（自 FY25 期末增加 14.5%）。FY24 股權發行 258.0M；Q1 FY26 發行 424.4M。info sharesOutstanding 為 129.9M。
- 股權激勵：SBC 為主要的 "成本"，FY25 183.9M，約為 FY25 淨利虧損絕對值的 10 倍以上。

**內部人交易（2026-04-22 至 2026-10-22，共 41 筆）**
- 有金額的 28 筆中：
  - SoftBank Group（10% 以上受益人）：2026-05-27 出售 5,590,000 股，約 281.8M（均價約 50.42），占市值約 1.1%（以 info marketCap 25.26B 計），若以 Class A 市值 5.67B 計約 5.0%。
  - 其他內部人（董事、高階主管）：合計賣出約 230,768 股、約 11.6M，占市值約 0.05%。主要賣方：Krasnow（董事）約 3.49M、Alexander（高階主管）約 2.64M、Kuffner（CTO）約 2.31M、Boyd 約 1.15M、Martins（CFO）約 1.12M、Kane（董事）約 0.55M、Freve 約 0.36M。
- 無金額的 13 筆（約 313K 股）：性質無法從資料判定（可能為 RSU 歸屬或代扣稅），以 DATA_UNAVAILABLE 處理。
- 6 個月內未見公開市場的內部人買進紀錄。
- 小結：內部人淨賣出，金額上以 SoftBank 為主；非 SoftBank 的內部人金額小，但方向一致（全數為賣出）。

**持股結構**
- 內部人持股 13.6%、機構持股 79.4%（555 家機構）。
- 前三大：SoftBank 30.66%（39.8M 股）、Walmart 11.55%（15.0M 股）、Baillie Gifford 9.44%（12.3M 股，季減 1.7%）。SoftBank 的大股東地位與其在 2026-05 的出售形成持股壓力的潛在來源。
- 空單：shortPercentOfFloat 31.8%，sharesShort 17.69M 股（前月 16.84M，+5.1%），shortRatio 10.6 天（截至 2026-09-30）。

## Valuation

**估值倍數**（價格 41.73；info marketCap 25.26B；implied shares 605.4M，share-basis 與 Class A 差異見 Red flags）
- trailing P/E：521.6x（trailing EPS 0.08）；forward P/E：56.1x（forward EPS 0.744）；本年度 EPS 估 0.569，對應 P/E 約 73.3x；PEG：4.9（info pegRatio），trailingPegRatio 5.39。
- P/S（TTM）：9.55x；P/B：7.59x（bookValue 每股 5.497）。
- P/FCF（TTM FCF 737.3M）：34.3x（以 marketCap 25.26B）；若以 Class A 市值 5.67B 計約 7.7x。
- EV/EBITDA：info 報 72.95x（enterpriseValue 4.12B，EBITDA 56.5M）；但依 marketCap 25.26B 重新計算 EV 約 23.97B（市值 - 現金 + 負債 + 少數股權），EV/EBITDA 約 424x。兩者差異極大，需由 downstream 確認 EV 基準。EV/Revenue：info 1.56x，重算約 9.1x。
- 同業中位數（估計，非工具輸出）：Specialty Industrial Machinery 中位數 forward P/E 約 25–30x、EV/EBITDA 約 15–20x、P/S 約 2–3x、P/FCF 約 20–25x、P/B 約 3x。

**市場與分析師共識**
- 52 週區間 36.47–87.88；現價較 52 週高點低 52.5%；52 週漲跌 -35.2%（S&P 500 同期 +15.1%）。
- 股價 41.73 低於 50 日均線 41.74（幾乎持平）與 200 日均線 49.19（-15.2%）。beta 1.97。
- 分析師 14 家：推薦均值 2.29（buy 區間）；目標價平均 62.86（較現價 +50.6%）、中位數 67.5、最高 85.0、最低 38.0（較現價 -9%）。近 1 個月 SB 1、B 8、H 5、S 2、SS 1（與 3 個月前相比 B 由 9 降至 8）。

**估值判讀**：以 forward P/E 56x、P/S 9.5x、P/B 7.6x 相較於同業估計中位數，估值溢價顯著，目前的價格隱含的成長假設需要獲利大幅改善才能支撐。

## Key catalysts
- 下次財報：2026-11-16（as-of 之後，預定事件）；EPS 一致預期 0.16（earnings_dates）。
- 最近一季（2026-08-05 發布 Q3 FY26）：earnings_dates 記錄 EPS 0.41 vs 預估 0.13（surprise +218.5%），但季度 diluted EPS 為 0.09；兩者差異可能源於 non-GAAP 調整，工具未說明口徑，需標註。
- 季度趨勢：毛利率連續四季改善（18.9% → 22.3%）；營業利益率由負轉正（Q3 FY26 4.6%）；應收帳款與存貨增加是下一季的關鍵觀察點。
- 最近的股權與股東事件：2026-05-27 SoftBank 出售 5.59M 股（後續是否持續減持為未知）；Q1 FY26 股權發行 424.4M 已反映於現金。
- 管理指引（guidance）與分部/客戶集中度（Walmart 為 11.55% 股東，其客戶占比未揭露）：DATA_UNAVAILABLE。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue TTM | 2,645.8M | +21.7%（Q3 FY26） | 約 8%（成長率估計） | 強 |
| Revenue 3y CAGR (FY22–25) | 55.9% | FY25 +25.7% | 約 8% | 強 |
| Gross margin (TTM) | 21.6%（info 21.3%） | Q3 FY26 22.3% vs Q3 FY25 18.9% | 約 30% | 偏低，持續改善 |
| Operating margin (TTM) | +1.25%（info 4.59%） | FY25 -4.1% → TTM +1.25% | 約 10% | 剛轉正，偏弱 |
| Net margin (TTM) | 0.31% | FY25 -0.75% | 約 7% | 弱 |
| ROE | 4.4%（info） | FY25 約 -7.7% | 約 12–15% | 弱 |
| ROIC（估算，稅前） | 約 4.5% | n/a | 約 10% | 弱 |
| FCF margin (TTM) | 27.9% | FY25 35.1% | 約 8–10% | 數字強，品質待確認 |
| FCF / NI | n/m（NI 8.2M） | n/m | > 0.9 | 無法判定 |
| OCF Q3 FY26 | -147.3M | n/a | n/a | 警示 |
| Current ratio | 1.33 | FY25 1.09 | 約 2.0 | 中性 |
| Quick ratio | 1.16 | n/a | 約 1.5 | 中性 |
| Cash & equivalents | 1,746.4M | 較 FY25 期末 +40.3% | n/a | 佳 |
| Net cash（現金 - 負債） | 約 1,720.6M | n/a | n/a | 佳 |
| Debt / Equity（含少數股權） | 約 2.3% | n/a | 約 40% | 佳 |
| Receivables / DSO | 748.4M / 約 95 天 | 應收 +103%（vs FY25 期末） | 約 60 天 | 警示 |
| Capex / Revenue (TTM) | 3.7% | FY25 3.5% | 約 3–5% | 中性 |
| Dividend / Buyback | 無 | 無 | n/a | 中性 |
| Share count | 128.9M | +14.5%（vs FY25 期末） | n/a | 稀釋 |
| SBC / Revenue (TTM) | 約 7.8% | FY25 8.2% | 約 3–5% | 偏高 |
| Insider net (6mo, ex-SoftBank) | 賣出約 11.6M，買進 0 | n/a | n/a | 偏空（金額小） |
| SoftBank sale (6mo) | 281.8M（5.59M 股，@50.42） | 占市值 1.1% | n/a | 需留意 |
| Short % of float | 31.8%（10.6 天回補） | 空單 +5.1%（月） | 約 3–5% | 高 |
| P/E trailing | 521.6x | n/a | 約 25x | 極高 |
| P/E forward | 56.1x | n/a | 約 25–30x | 偏高 |
| EV/EBITDA | 72.95x（info）/ 約 424x（重算） | n/a | 約 15–20x | 極高，基準待確認 |
| P/S (TTM) | 9.55x | n/a | 約 2–3x | 高 |
| P/FCF (TTM) | 34.3x（市值 25.26B） | n/a | 約 20–25x | 偏高 |
| P/B | 7.59x | n/a | 約 3x | 高 |
| Analyst mean target | 62.86（+50.6%） | n/a | n/a | 分析師樂觀 |
| Beta | 1.97 | n/a | 約 1.0 | 高波動 |
| 52-week change | -35.2%（S&P +15.1%） | n/a | n/a | 弱 |
| Price vs 200-day MA | -15.2% | n/a | n/a | 弱 |

## Red flags
- 獲利與估值脫節：TTM 淨利 8.2M、trailing EPS 0.08、ROE 4.4%，對應 trailing P/E 521.6x、forward P/E 56.1x。
- Q3 FY26 營業現金流 -147.3M、FCF -164.6M；應收帳款 748.4M（+103% vs FY25 期末），DSO 約 95 天（FY25 約 60 天）。
- 股本稀釋：普通股 9 個月內增加 14.5%（112.6M → 128.9M）；Q1 FY26 股權發行 424.4M；SBC 占 TTM 營收約 7.8%。
- 大股東出售：SoftBank（持股 30.66%）於 2026-05-27 出售 5.59M 股、約 281.8M，成交價 50.42 高於現價 41.73，後續持股減持壓力未知。
- 空單比例高：short float 31.8%，days-to-cover 10.6 天。
- 少數股權快速增加：少數股權由 FY25 期末 261.9M 增至 2026-06-30 的 425.2M，歸屬母公司權益占比下降。
- 資料一致性問題（需 downstream 留意）：
  - info marketCap 25.26B 以 implied shares 605.4M 計算，但 sharesOutstanding 僅 129.9M（Class A 市值 5.67B）；工具未揭露股份類別結構，市值基準為 DATA_UNAVAILABLE。
  - info enterpriseValue 4.12B 與 marketCap 25.26B 不一致，EV 倍數（EV/EBITDA、EV/Revenue）在兩種基準下相差近 6 倍。
  - info operatingCashflow 894.4M、freeCashflow 547.6M、operatingMargins 4.59% 與季度加總（836.3M、737.3M、1.25%）不一致。
  - earnings_dates 的 Reported EPS（0.41）與季度 diluted EPS（0.09）口徑不同。
  - 即時 yfinance 輸出於執行時曾回傳 TSLA 資料（跨 ticker 污染），本報告僅採用已驗證 symbol 為 SYM 的快取；pricefeed 即時報價因連線被阻擋未取得，價格採快取 regularMarketPrice 41.73（時間戳 2026-10-21）。
  - info 的 regularMarketChange（+5.14%）與 fulldayChange（-2.76%）方向相反，當日漲跌方向待確認。
- 分部與指引資料缺漏：分部營收、管理層指引、客戶集中度（Walmart）為 DATA_UNAVAILABLE，無法評估營收品質的結構性風險。

FUNDAMENTALS REPORT COMPLETE
