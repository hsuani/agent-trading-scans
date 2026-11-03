# Fundamentals — MOD (Modine Manufacturing Company) as of 2026-11-04

資料說明: 工具資料來源為 `source: cache`（cached_at 2026-11-03T14:04 UTC，屬預期情況）。股價為 2026-11-03 盤前報價（marketState PRE），非收盤價。財年為 3 月結（FY26 = 2025-04 至 2026-03）。金額單位為 USD，以 B（十億）/ M（百萬）標示。FY26 年報與 Q1 FY27（2026-06-30）季報均已在資料內。Q2 FY27 財報（預定 2026-11-03 盤後公布）尚未出現在資料內，標示為 DATA_UNAVAILABLE。

## Executive summary

MOD 營收成長動能強勁：FY26 營收 $3.18B（YoY +23.1%），Q1 FY27 營收 $874.1M（YoY +28.0%），但獲利與現金流品質明顯轉弱，FY26 GAAP 淨利 $121.5M（YoY -34.0%），TTM FCF 僅 $100.2M（FCF margin 3.0%），且 Q1 FY27 毛利率壓縮至 20.8%（YoY -3.4 pt）。資產負債表尚可控（current ratio 2.04，net debt / TTM EBITDA 1.43x），但 net debt 從 2026-03-31 的 $362.8M 增至 2026-06-30 的 $432.9M。估值上，股價 $123.34 較 52 週高點 $323.25 下跌 61.8%，以前瞻 EPS 計 forward P/E 僅 12.8x，但以 GAAP trailing EPS 計 P/E 達 46.4x，且資料中 EV/EBITDA、FCF、目標價等欄位彼此不一致，需於下游審核時先行校正。

## Revenue & profitability

**年度營收與利潤率（USD B / %）**

| 財年 (3 月結) | 營收 (USD B) | YoY | 毛利率 | 營業利益率 | 淨利率 | Diluted EPS (USD) |
|---|---|---|---|---|---|---|
| FY23 | 2.30 | n/a | 16.9% | 6.8% | 6.7% | 2.90 |
| FY24 | 2.41 | +4.8% | 21.8% | 10.5% | 6.7% | 3.03 |
| FY25 | 2.58 | +7.3% | 24.9% | 12.1% | 7.1% | 3.42 |
| FY26 | 3.18 | +23.1% | 23.0% | 11.7% | 3.8% | 2.26 |

- 營收 3 年 CAGR（FY23 至 FY26）約 11.5%。成長在 FY26 明顯加速，且 FY26 內有 $182.4M 的企業收購現金支出（Jun25 季 $119.0M、Sep25 季 $63.1M、Dec25 季 $0.3M），因此部分成長屬於併購貢獻。收購標的名稱與營收貢獻：DATA_UNAVAILABLE。
- 分部營收拆分：DATA_UNAVAILABLE。業務描述顯示產品線涵蓋 HVAC 熱交換、data center 冷卻（chillers、CDU、immersion 等）、powertrain 冷卻與電池熱管理等，但資料中無分部營收數字。
- FY26 淨利率由 7.1% 降至 3.8%，原因之一為 FY26 內非營業項目：Other Non Operating Income Expenses -$119.6M，以及現金流量表標示的 Pension And Employee Benefit Expense $116.1M（非現金）。Dec25 季 GAAP 淨利為 -$47.4M（EPS -0.90），即由 Other Special Charges $116.1M 所致。調整後 EPS 則為正（見估值段）。

**季度趨勢（USD M）**

| 季度 | 營收 | YoY | 毛利率 | 營業利益率 | 淨利 | Diluted EPS |
|---|---|---|---|---|---|---|
| Q1 FY26（2025-06） | 682.8 | n/a | 24.2% | 11.8% | 51.2 | 0.95 |
| Q2 FY26（2025-09） | 738.9 | n/a | 22.3% | 10.9% | 44.4 | 0.83 |
| Q3 FY26（2025-12） | 805.0 | n/a | 23.1% | 12.0% | -47.4 | -0.90 |
| Q4 FY26（2026-03） | 954.4 | n/a | 22.5% | 11.8% | 73.3 | 1.36 |
| Q1 FY27（2026-06） | 874.1 | +28.0% | 20.8% | 9.0% | 73.9 | 1.37 |

- 毛利率計算由 quarterly_fin 之 Gross Profit / Total Revenue 導出；Q2 FY26 至 Q4 FY26 之 YoY 因 Q2 至 Q4 FY25 季度資料未於本次抓取中完整呈現，標示 n/a。
- Q1 FY27 毛利率 20.8%，較 Q1 FY26 的 24.2% 下降 3.4 pt，為本報告最需追蹤的趨勢。Q1 FY27 營業利益率 9.0%（YoY 較 11.8% 下降 2.8 pt）。

**TTM（2025-09 至 2026-06）**

- 營收 $3.37B（與 info totalRevenue $3.37B 一致）。
- 毛利 $747.7M，毛利率 22.2%（與 info grossMargins 22.2% 一致）。
- 營業利益（statement Operating Income 加總）$369.2M，營業利益率 10.9%。注意：info operatingMargins 為 9.0%，與 statement 不一致，見紅旗段。
- 淨利 $144.2M，淨利率 4.3%（與 info netIncomeToCommon $144.2M、profitMargins 4.28% 一致）。
- ROE：13.1%（info returnOnEquity）；ROIC（估算）約 14.1%，以 TTM 營業利益 × (1 − 33.9%，FY26 有效稅率) ÷ Invested Capital $1,729.7M 計算，屬估算值。

## Cashflow & balance sheet

**現金流（USD M）**

| 期間 | 營業現金流 | 資本支出 | FCF | FCF / NI | FCF margin |
|---|---|---|---|---|---|
| FY23 | 107.5 | 50.7 | 56.8 | 0.37 | 2.5% |
| FY24 | 214.6 | 87.7 | 126.9 | 0.79 | 5.3% |
| FY25 | 213.3 | 84.0 | 129.3 | 0.70 | 5.0% |
| FY26 | 248.7 | 143.3 | 105.4 | 0.87 | 3.3% |
| TTM（至 2026-06） | 262.4 | 162.2 | 100.2 | 0.69 | 3.0% |

- FCF / NI 門檻 0.9 以上為健康。FY26 的 0.87 接近門檻，但分母 NI 因非現金 pension 與特殊項目而被壓低，不能直接解讀為現金流品質良好。TTM FCF / NI 為 0.69，未達門檻。
- Q1 FY27 營業現金流僅 $41.4M（去年同季 $27.7M），資本支出 $46.4M，單季 FCF 為 -$5.0M。主因為營運資金吸金：應收帳款 $659.9M（YoY +27.7%）、存貨 $609.0M（YoY +40.1%）。FY26 營運資金變動為 -$68.4M，Q1 FY27 為 -$58.9M。
- info freeCashflow 為 -$73.7M，與 statement 導出之 TTM FCF $100.2M 不一致，見紅旗段。

**資產負債表（2026-06-30，USD M）**

| 項目 | 數值 | 備註 |
|---|---|---|
| 現金及約當現金 | 95.3 | 現金流量表期末現金 95.5，差異 0.2 |
| 總債務 | 528.2 | 長期 476.2 + 短期 52.0（BS 口徑） |
| Net debt | 432.9 | 較 2026-03-31 之 362.8 增加 19.3%（QoQ） |
| 股東權益 | 1,201.5 | |
| 商譽及無形資產 | 480.4 | 佔股東權益 40.0% |
| 有形帳面價值 | 721.1 | |
| 流動資產 / 流動負債 | 1,526.9 / 749.8 | Current ratio 2.04 |
| Quick ratio（info） | 1.11 | |
| D/E（BS 口徑） | 0.44x | info debtToEquity 55.5%，口徑不同 |
| Net debt / TTM EBITDA | 1.43x | 以 statement TTM EBITDA $303.0M 計；以 info EBITDA $449.7M 計為 0.96x |
| 利息保障倍數（TTM） | 11.5x | TTM 營業利益 $369.2M ÷ TTM 利息費用 $32.2M |

- 流動性與償債能力尚可。債務增加主要來自 Q1 FY27 發行 $375.3M 及償還 $283.4M 的循環式再融資，以及收購資金需求。總債務於 Q1 FY27 增加 21.0% QoQ。
- info totalDebt 為 $671.4M，與 BS 總債務 $528.2M 差 $143.2M，推測 info 包含租賃負債，但資料內未驗證。

## Capital allocation & insider signal

**資本配置**

- 資本支出：FY26 $143.3M，YoY +70.6%，佔營收 4.5%（FY25 為 3.3%），資本支出／折舊攤銷 1.8x（D&A $79.7M）。擴張性投資明顯升高，但資料未說明資本支出用途與產能別，需由後續法說會確認。
- 併購：FY26 支出 $182.4M。
- 買回：FY26 $7.0M（FY25 $30.9M、FY24 $17.7M），Q1 FY27 大幅升至 $64.6M。Treasury stock 由 $104.6M（2026-03-31）升至 $169.2M（2026-06-30），與季度買回金額吻合。然而流通股數仍由 52.8M（2026-03-31）升至 53.1M（2026-06-30），顯示買回被股權激勵發行所抵銷。
- 股利：無。info dividendYield 0.0、payoutRatio 0.0；info fiveYearAvgDividendYield 3.03% 為歷史數據，不代表現行配息。股利覆蓋率：不適用。

**內部人交易（過去 6 個月，2026-05-03 至 2026-11-03，資料來源 insider）**

| 日期 | 內部人 | 職位 | 股數 | 金額 (USD) | 性質 |
|---|---|---|---|---|---|
| 2026-06-01 | MCGINNIS ERIC S | Officer | 38,082 | 10.86M | 公開市場賣出 $280.13–290.79 |
| 2026-06-01 | LASZLO ARTHUR JR | Officer | 900 | 0.27M | 公開市場賣出 $295.76 |
| 2026-06-16 | ASHLEMAN ERIC D | Director | 15,000 | 4.33M | 公開市場賣出 $286.27–291.12 |
| 2026-06-18 | AGEN BRIAN JON | Officer | 38,282 | 11.30M | 公開市場賣出 $284.80–300.04 |
| 2026-06-18 | MCGINNIS ERIC S | Officer | 1,020 | 0.30M | 公開市場賣出 $295.06 |
| 2026-09-10 | AGEN BRIAN JON | Officer | 4,306 | 0.78M | 公開市場賣出 $180.30 |
| 2026-09-10 | AGEN BRIAN JON | Officer | 5,269 | 0.06M | 選擇權行使（conversion） |
| 2026-05-20 至 2026-08-20 | 多位 Officer / Director | 多位 | 約 390,211 股合計 | 0 | 股票授與（grant），非市場交易 |

- 公開市場賣出合計 97,590 股，金額約 $27.8M，佔市值 0.42%。買進：0 筆。
- 賣出主要集中於 2026-06 月初至中旬，成交價約 $280–300；2026-09-10 Agen 另以 $180.30 賣出 4,306 股。目前股價 $123.34 低於所有賣出價格。
- 內部人持股比例 1.94%（info heldPercentInsiders）。整體解讀：6 個月內以賣出為主、無買進，賣出價格明顯高於現價，屬偏負面訊號，但金額相對市值很小。

**機構持股（inst_holders，資料日期 2026-06-30）**

- 機構持股家數 787（info institutionsCount）。
- 前十大機構合計持股約 30.65%。
- 前三大：BlackRock 5.40%（2.87M 股，QoQ -29.8%）、Vanguard Capital Management 4.48%（QoQ +0.7%）、Vanguard Portfolio Management 4.15%（QoQ -6.7%）。
- 其他重要變動：Capital Research Global Investors 2.79%（QoQ -13.2%）、Artisan Partners 2.24%（QoQ +20.7%）、State Street 2.20%（QoQ -21.3%）。
- info institutionsPercentHeld 為 100.67%，超過 100%，屬資料異常，不採用為精確持股比例。
- 空單：sharesShort 2.50M 股，佔流通股 4.78%，short ratio 1.77 日，較上月 3.36M 股減少 25.6%。

## Valuation

**價格基礎**
- 現價 $123.34（info currentPrice；盤前，regularMarketChange -4.95%）。
- 市值 $6.56B（info marketCap，與價格 × 流通股數 53.2M 吻合）。
- EV $7.14B（info enterpriseValue）。以 statement 總債務計算約 $6.99B。
- 52 週區間 $111.18 至 $323.25，現價較 52 週高點下跌 61.8%，較 50 日均線 $173.07 低 28.7%，較 200 日均線 $216.10 低 42.9%。
- Beta 1.84。

**倍數**

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E（GAAP） | 46.4x | info trailingEps $2.66 |
| Trailing P/E（調整後） | 22.5x | earnings_dates 最近四季 Reported EPS 合計 $5.49（推測為 adjusted EPS，未於資料內確認定義） |
| Forward P/E | 12.8x | info forwardEps $9.66 |
| Current-year P/E | 18.7x | info epsCurrentYear $6.61 |
| PEG（info） | 0.47 | |
| EV / EBITDA | 15.9x（info）/ 23.5x（statement TTM） | info EBITDA $449.7M；statement TTM EBITDA $303.0M，兩者差距大，需核對 |
| EV / Normalized EBITDA | 21.4x | statement TTM Normalized EBITDA $334.2M |
| P / S | 1.95x | TTM 營收 $3.37B |
| P / B | 5.45x | Book value per share $22.63 |
| P / FCF | 65.5x | TTM FCF $100.2M（info freeCashflow 為負，n/m） |

**分析師共識（info 欄位，9 位分析師）**
- 評級均值 1.1（strong buy）。
- 目標價：平均 $290.78、中位數 $285.00、低 $245.00、高 $355.00。
- 平均目標價相對現價隱含 +135.8% 上行空間。此差距異常大，可能代表目標價尚未反映近期股價下跌，或目標價更新時間早於股價修正。目標價日期：DATA_UNAVAILABLE。
- ratings 子命令於 yf 工具中不存在（invalid choice），因此以 info 內之 recommendation 欄位代替。

**相對同業（估計值，非工具資料）**
- 同業中位數為本報告依 Building Products & Equipment 產業之一般水準估計，並非由工具取得。估計值：trailing P/E 約 25x、EV/EBITDA 約 14x、P/S 約 2.0x、P/FCF 約 25x、毛利率約 25–30%、ROE 約 15%。
- 以前瞻 P/E 看，MOD 低於估計同業；以 GAAP trailing P/E、EV/EBITDA（statement 口徑）與 P/FCF 看，MOD 高於估計同業。估值的解讀高度依賴盈餘基準，GAAP 與調整後的差距很大。

## Key catalysts

1. **Q2 FY27 財報（預定 2026-11-03，約 16:00 ET 盤後）**：EPS 一致預期 $1.52（earnings_dates EPS Estimate）。實際財報結果：DATA_UNAVAILABLE（截至 cache 時點尚未公布）。報告 2026-11-04 之後應立即核對實際 EPS、毛利率與 FCF。
2. **盈餘公布紀錄**：近 12 季 EPS 皆優於一致預期。最近一季 Q1 FY27 調整後 EPS $1.53 對 $1.27 預估，超出 20.0%。歷史上僅 2021 年兩季未達標。
3. **毛利率趨勢**：Q1 FY27 毛利率 20.8%（YoY -3.4 pt）。若 Q2 毛利率持續低於 22%，將構成盈利壓力的延續訊號。
4. **營運資金**：應收帳款與存貨的成長速度（分別 YoY +27.7% 與 +40.1%）是否在 Q2 回收，將決定 FCF 能否回升至 FY26 水準以上。
5. **收購與分部**：FY26 收購 $182.4M 的整合進度與營收貢獻，以及分部營收拆分：DATA_UNAVAILABLE。
6. **管理層指引**：公司未來營收與獲利指引：DATA_UNAVAILABLE。
7. **內部人與機構動向**：後續 Form 4 與 13F 申報可驗證內部人是否仍持續賣出，以及機構是否延續減持。

## Metrics table

金額單位：營收與獲利為 USD M / USD B；倍數為 x；比率為 %。Sector median 為估計值，非工具取得。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（USD B） | 3.37 | +28.0%（Q1 FY27） | 約 5–8% 成長（估計） | 強於同業 |
| 毛利率 TTM | 22.2% | Q1: 20.8% vs 24.2%（-3.4 pt） | 約 25–30% | 偏弱 |
| 營業利益率 TTM（statement） | 10.9% | Q1: 9.0% vs 11.8% | 約 10–12% | 中性 |
| 淨利率 TTM | 4.3% | FY26: 3.8% vs FY25 7.1% | 約 6–8% | 偏弱 |
| ROE（info） | 13.1% | n/a | 約 15% | 中性 |
| ROIC（估算） | 14.1% | n/a | 約 10–12% | 中性偏佳 |
| FCF margin TTM | 3.0% | FY26: 3.3% vs FY25 5.0% | 約 6% | 偏弱 |
| FCF / NI TTM | 0.69 | FY26: 0.87 vs FY25 0.70 | >0.9 為健康 | 未達門檻 |
| Current ratio | 2.04 | n/a | 約 1.8 | 健康 |
| Net debt / TTM EBITDA | 1.43x | Net debt Jun25 $402.6M → Jun26 $432.9M（+7.5%） | 約 2.0x | 可控 |
| D/E（BS 口徑） | 0.44x | n/a | 約 0.6x | 健康 |
| 利息保障倍數 TTM | 11.5x | n/a | 約 6x | 健康 |
| 資本支出 / 營收（FY26） | 4.5% | 資本支出 YoY +70.6% | 約 3% | 偏高（擴張中） |
| P/E（GAAP trailing） | 46.4x | n/a | 約 25x | 偏貴 |
| P/E（調整後 trailing） | 22.5x | n/a | 約 25x | 略便宜 |
| P/E（forward） | 12.8x | n/a | 約 20x | 便宜（前瞻） |
| EV / EBITDA | 15.9x（info）/ 23.5x（statement） | n/a | 約 14x | 依口徑而異 |
| P / FCF | 65.5x | n/a | 約 25x | 偏貴 |
| P / S | 1.95x | n/a | 約 2.0x | 中性 |
| P / B | 5.45x | n/a | 約 2.5x | 偏貴 |
| 股價相對 52 週高點 | -61.8% | 52 週 -15.6% | n/a | 弱勢 |
| 內部人 6 個月淨額 | 賣出 $27.8M，買進 $0 | n/a | n/a | 偏負面 |
| 空單佔流通股 | 4.78% | 較上月 -25.6%（股數） | 約 3% | 中性 |
| 分析師平均目標價隱含上行 | +135.8% | n/a | n/a | 異常，需核對日期 |

## Red flags

- **GAAP 獲利明顯惡化**：FY26 營收 +23.1%，但淨利 -34.0%（$121.5M 對 $184.0M），Dec25 季度出現 GAAP 淨損 -$47.4M，主因 Other Special Charges $116.1M（現金流量表標示為 pension and employee benefit 相關，非現金）。
- **毛利率壓縮**：Q1 FY27 毛利率 20.8%，較去年同季 24.2% 下降 3.4 pt，營業利益率亦下降 2.8 pt，營收成長未能轉化為獲利成長。
- **營運資金吸金、現金流轉弱**：Q1 FY27 營業現金流 $41.4M，單季 FCF -$5.0M；應收帳款 +27.7%、存貨 +40.1%（YoY）。
- **槓桿上升**：總債務 QoQ +21.0%（$436.3M 至 $528.2M），net debt QoQ +19.3%；Q1 FY27 再融資規模大（發行 $375.3M、償還 $283.4M）。
- **內部人持續賣出、無買進**：6 個月內 6 筆公開市場賣出（$27.8M），賣出價格多在 $280–300，現價 $123.34。
- **股價趨勢弱**：現價低於 50 日與 200 日均線，較 52 週高點下跌 61.8%；空單比例 4.78%。
- **分析師目標價與現價落差過大**：平均目標 $290.78 相對現價隱含 +135.8%，目標價可能過時，需核對發布日期。
- **資料不一致（需於下游校正）**：
  - info freeCashflow -$73.7M 與 statement TTM FCF $100.2M 不一致。
  - info EBITDA $449.7M 與 statement TTM EBITDA $303.0M（Normalized $334.2M）不一致，導致 EV/EBITDA 由 15.9x 至 23.5x 差距很大。
  - info operatingMargins 9.0% 與 statement TTM 營業利益率 10.9% 不一致。
  - info totalDebt $671.4M 與 BS 總債務 $528.2M 不一致。
  - info institutionsPercentHeld 為 100.67%，超過 100%。
  - info lastSplitFactor 為 1086:1000，lastSplitDate 推算為 2026-10-01，未於其他資料驗證；statement 之股數未顯示分割調整，此欄位視為待核對。
  - fast_info market_cap 與 shares 為 null，fast_info 之 50 日與 200 日均線為 null，不採用。
  - info fiveYearAvgDividendYield 3.03% 與現行無配息矛盾，採用 dividendYield 0.0。
- **盈餘口徑未明確**：earnings_dates 之 Reported EPS 未明確標示為 GAAP 或 adjusted，本報告以 TTM 合計 $5.49 推測為 adjusted EPS，需確認。
- **財報待公布**：Q2 FY27 結果 DATA_UNAVAILABLE，本報告之結論需於財報公布後更新。

FUNDAMENTALS REPORT COMPLETE
