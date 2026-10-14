# Fundamentals — VRT (Vertiv Holdings) as of 2026-10-14

## Executive summary
Vertiv 基本面目前屬於高成長、現金流強勁的狀態：TTM revenue 為 $11,479.6M（YoY 約 +24%），TTM 自由現金流（以 OCF 減 capex 計算）約 $2,924M，FCF/NI 約 1.69，資產負債表約為現金與負債相當（cash & STI $3,110.6M vs total debt $3,338.2M）。估值在 TTM 基礎上明顯偏高（trailing P/E 53.7x、EV/EBITDA 34.2x、P/FCF 約 31–34x），但以 consensus forward EPS $9.19 計算 forward P/E 約 25.8x，且分析師平均目標價 $335.64 高於現價 $237.29 約 41%。2026 年上半年存貨與應收帳款快速增加、流動負債與總資產明顯擴張，為需要追蹤的風險點；內部人近六個月僅有一筆 $3.88M 的公開市場賣出，對市值（$91.35B）影響極小。

資料說明：本次 `info` 與 `fast_info` 明確標示為 cache（cached_at 2026-10-14T11:43 UTC），價格 $237.29 為 2026-10-13 常規盤收盤（regularMarketTime 2026-10-13 20:00 UTC）；盤前價 $235.95（2026-10-14 11:43 UTC）。財報、insider、holders 類資料回傳時未附來源標記，無法確認是否為即時資料。工具內未見 post-date 的已實現財務數據；唯一未來事件為下一次財報（Yahoo 估計 2026-10-21），屬預定事件而非既成數據。

## Revenue & profitability

**營收與成長**
- 年度 total revenue：2022 $5,691.5M、2023 $6,863.2M、2024 $8,011.8M、2025 $10,229.9M。YoY 分別為 2023 +20.6%、2024 +16.7%、2025 +27.7%。
- 2022–2025 3 年 CAGR 約 21.6%（工具中 2021 年資料為 n/a，無法計算 4–5 年 CAGR）。
- 季度 total revenue：Q2'25 $2,638.1M、Q3'25 $2,675.8M、Q4'25 $2,880.0M、Q1'26 $2,649.5M、Q2'26 $3,274.3M。Q2'26 YoY 約 +24.1%，與 Yahoo `revenueGrowth` 0.241 一致。
- 產品線（由 `longBusinessSummary` 摘錄）：AC/DC 電源管理、中低壓開關設備、熱管理（air-cooled 與 liquid-cooled）、integrated modular solutions、racks、UPS、rack power distribution、energy storage 以及 lifecycle services（維護、監控、軟體服務）。**Segment 營收拆分：DATA_UNAVAILABLE**（工具未提供分部營收與佔比）。

**毛利、營益與淨利率（年度）**

| 年度 | Gross margin | Operating margin | Net margin | Normalized NI |
|---|---|---|---|---|
| 2022 | 28.4% | 4.0% | 1.3% | $8.3M |
| 2023 | 35.0% | 13.4% | 6.7% | $635.2M |
| 2024 | 36.6% | 17.2% | 6.2% | $797.9M |
| 2025 | 36.3% | 18.5% | 13.0% | $1,385.0M |

- 2024 GAAP NI（$495.8M）受 Total Unusual Items -$466.2M 拖累，以 normalized NI 看 2025 成長約 +73.6%。
- 2025 Operating Income $1,896.2M（+37.2% YoY）。

**季度趨勢（Q2'26 vs Q2'25）**
- Gross margin：34.0% → 37.7%（+3.7pp）。
- Operating margin：16.8% → 19.5%（+2.7pp）。
- Operating income：$442.4M → $637.9M（+44.2%）。
- Net income：$324.2M → $497.8M（+53.5%）。
- GAAP diluted EPS：$0.83 → $1.27（+53.0%）。

**ROE / ROIC**
- ROE（Yahoo TTM）43.9%；ROA 10.9%。ROE 偏高部分來自權益基數相對小（equity 2024 年底 $2,434.3M，2025 年底 $3,941.3M，2026-06-30 為 $4,757.6M）。
- ROIC 為估算值（非工具直接提供）：TTM Total Operating Income As Reported $2,174.6M × (1 - 20%) ÷ 2026-06-30 Invested Capital $7,697.4M ≈ 22.6%。

## Cashflow & balance sheet

**現金流**

| 年度 | OCF | Capex | FCF | FCF margin | FCF/NI |
|---|---|---|---|---|---|
| 2022 | -$152.8M | $111.0M | -$263.8M | -4.6% | 負值（NI 僅 $76.6M） |
| 2023 | $900.5M | $134.6M | $765.9M | 11.2% | 1.66 |
| 2024 | $1,319.3M | $184.1M | $1,135.2M | 14.2% | 2.29 |
| 2025 | $2,113.8M | $226.4M | $1,887.4M | 18.4% | 1.42 |

- TTM（Q3'25–Q2'26）OCF $3,354.2M（與 Yahoo `operatingCashflow` 一致），capex $430.2M，FCF（計算值）$2,924.0M，FCF margin 25.5%，FCF/NI 1.69。
- Yahoo `freeCashflow` 為 $2,696.5M（FCF margin 23.5%、FCF/NI 1.56），與本次計算值差約 $227M，原因未知，兩者皆 > 0.9 的健康門檻。
- 2025 年 working capital 為正向貢獻 $339.3M（Change In Working Capital），部分 FCF 增幅來自營運資金。
- SBC 2025 為 $45.9M（約 0.45% 營收），稀釋壓力小。

**資產負債表（2026-06-30，季報）**
- Cash & cash equivalents $2,810.6M；cash + short-term investments $3,110.6M。
- Total debt $3,338.2M（Long-term debt $2,939.8M、long-term lease 等 $316.4M 併計；current debt & lease $82.0M）。
- 淨負債口徑差異：Yahoo `Net Debt` $129.2M；以 Total debt − cash & STI 計算為 $227.6M（與 Yahoo EV 計算吻合，enterpriseValue $91,581.4M − marketCap $91,353.8M = $227.6M）；若以 Total debt − cash & cash equivalents 則為 $527.6M。三種口徑需以 10-Q 定義為準，本報告以 $227.6M 為主。
- Debt/Equity 70.2%（Total debt ÷ Stockholders Equity $4,757.6M）。
- Current ratio 1.38（current assets $9,984.9M ÷ current liabilities $7,243.0M）；quick ratio（Yahoo）0.95；working capital $2,741.9M。
- Tangible book value $673.5M（2025 年底僅 $12.8M，因商譽與無形資產增加而大幅改善）。
- Interest expense 持續下降：2023 $180.1M → 2024 $150.4M → 2025 $86.1M（-52% vs 2023），Q2'26 為 $17.4M。

**資產負債表的變化（需留意）**
- 2025-12-31 至 2026-06-30 半年內：Total assets $12,212.4M → $15,900.9M（+30.2%）；Total liabilities $8,271.1M → $11,143.3M。
- Inventory $1,456.5M → $2,522.7M（+73.2%）；Accounts receivable $3,109.0M → $3,750.3M（+20.6%）。
- Current liabilities $4,407.0M → $7,243.0M（+64.4%），其中 Other current liabilities 於 2026-06-30 為 $722.3M（2026-03-31 為 $177.3M）。
- Goodwill $2,033.7M → $2,283.3M（+12.3%）；Goodwill + intangibles $3,928.5M → $4,084.1M。工具未說明交易內容，不能確認是否為收購；需查 10-Q。
- 以 Q2'26 收入計算的 DIO 約 113 天（Q4'25 約 76 天）；DSO 約 104 天（Q4'25 約 99 天）。

## Capital allocation & insider signal

**資本配置**
- Capex 占營收：2022 1.95%、2023 1.96%、2024 2.30%、2025 2.21%；TTM 上升至 3.7%。Q2'26 單季 capex $174.5M，相較 Q2'25 $45.9M 增加約 280%。
- Buyback：2024 年 $599.9M 買回（單年度，約為 2024 FCF $1,135.2M 的 53%）；2023、2025 年為 0。
- 股息：2025 年現金股息 $66.6M；2026 年每季約 $23.9M（Q1、Q2'26 皆為 $23.9M）；TTM 股息約 $86.0M。Yahoo `dividendYield` 0.11%，`payoutRatio` 5.1%。TTM FCF ÷ 股息 ≈ 34x，股息覆蓋極為充裕。
- 股本：Ordinary Shares 2026-06-30 為 384.9M（2025-06-30 為 381.8M，年增約 0.8%）；Diluted average shares 2026 Q2 為 392.7M。
- 債務：2024 年新增 $270.0M 長期債務；2025 年淨償還 $20.9M。

**Insider 活動（近六個月：2026-04-14 至 2026-10-14）**
- 公開市場賣出：1 筆。MONSER EDWARD L（Director）2026-09-01 賣出 15,287 股，價格區間 $249.43–$256.36，金額 $3,880,209；同日行權（Conversion of derivative，行權價 $11.50）15,287 股，金額 $175,800。
- 公開市場買入：列表中未見 Purchase 紀錄。
- 其他：ALBERTAZZI GIORDANO（CEO）2026-09-08 贈與（Stock Gift）118,523 股（無價金）；2026-06-25 與 2026-10-05 為 stock award / grant（RESHA MICHAEL 2026-10-05 grant 3,193 股，@ $253.62，價值 $809,809）。
- 六個月內賣出金額 $3.88M，占 marketCap $91.35B 約 0.004%，規模極小。
- 背景參考（超出 6 個月窗口，僅供趨勢觀察）：2026-02-26 至 03-06 期間有一波大額賣出，合計約 $123.4M（FRADIN ROGER B $51.4M、REINEMUND STEVEN S $25.4M、MONSER EDWARD L $19.0M、COTE DAVID M $10.2M、VAN DOKKUM $9.8M、KARLBORG ANDERS $7.5M）。此波集中於董事與前高層，但不屬於本次六個月窗口。
- 持股：insidersPercentHeld 0.24%；institutionsPercentHeld 84.7%（2,714 家機構）。前幾大機構為 BlackRock 9.33%、Vanguard（兩實體合計約 11.2%）、State Street 4.29%（2026-06-30 資料）。

**做空部位**
- sharesShort 14.38M（占 float 3.74%），short ratio 2.75 天，較前一月 13.76M 增加約 4.5%。

## Valuation

**倍數（以現價 $237.29 計）**

| 指標 | 數值 | 計算/來源 |
|---|---|---|
| Trailing P/E | 53.7x | 237.29 ÷ TTM EPS $4.42（GAAP，Q3'25–Q2'26 diluted 合計） |
| Forward P/E | 25.8x | 237.29 ÷ forwardEps $9.19 |
| PEG | 0.81 | Yahoo pegRatio |
| EV | $91,581.4M | Yahoo enterpriseValue |
| EV/EBITDA（TTM） | 34.2x | Yahoo enterpriseToEbitda；TTM EBITDA $2,678.8M（Yahoo 口徑）。季度相加法為 $2,553.1M，對應約 35.9x |
| EV/Revenue（TTM） | 7.98x | Yahoo enterpriseToRevenue |
| P/S（TTM） | 7.96x | Yahoo priceToSalesTrailing12Months |
| P/FCF（TTM） | 33.9x（Yahoo FCF）／31.2x（計算 FCF） | 市值 $91,353.8M ÷ FCF |
| P/OCF（TTM） | 27.2x | 市值 ÷ OCF $3,354.2M |
| P/B | 19.2x | bookValue $12.359/share |

**分析師與目標價**
- Yahoo recommendationKey：strong_buy；recommendationMean 1.37（1 = strong buy）。
- 目標價：mean $335.64（相對現價 +41.4%）、median $338.50（+42.7%）、high $427.00（+79.9%）、low $236.00（-0.5%）。
- 分析師數：info 為 28 位；rec_summary 合計 30 位（strongBuy 3、buy 23、hold 4、sell 0）。數字不一致，屬工具口徑差異。

**技術面位置（僅作估值參考）**
- 50 日均線 $259.04（現價 -8.4%）；200 日均線 $267.57（現價 -11.3%）。
- 52 週區間 $147.82–$379.94，現價較高點 -37.5%，較低點 +60.5%；52 週漲幅 +31.5%。
- Beta 2.05。

**相對同業估值（sector median 為估計值，非工具數據，信心低）**
- 估計同業（工業電氣與 AI 數據中心基礎設施）forward P/E 約 25–35x，EV/EBITDA 約 18–25x，P/FCF 約 25–35x，P/S 約 2–4x。VRT 在 TTM 倍數上高於估計區間，forward P/E 落於估計區間內。

**獲利預期**
- Q3'26（預計 2026-10-21 發布）consensus EPS $1.83。對比 Q3'25 Yahoo `Reported EPS` $1.24（同口徑），約 +48%；若對比 GAAP diluted $1.02，約 +79%（口徑不同，僅供參考）。
- Yahoo `epsCurrentYear` $6.74（FY2026 consensus）。以 Yahoo `Reported EPS` 口徑推算：Q1'26 $1.17、Q2'26 $1.52、Q3'26 est $1.83，則 Q4'26 隱含約 $2.22（為推算值，非工具直接提供），高於 2026 年前三季任一季。
- 最近 8 季的 EPS 相對 consensus 平均 beat 約 +12.6%（以 Yahoo 調整後 EPS 計算）。

## Key catalysts
- **下次財報**：Yahoo 估計 2026-10-21（`isEarningsDateEstimate` = true，時間 12:30 UTC）。consensus EPS $1.83。Yahoo 歷史資料中最近一次（2026-07-29）`Reported EPS` 為 $1.52（consensus $1.43，beat +6.4%）；該口徑未在工具中明載，高於 GAAP diluted EPS $1.27，推測為調整後口徑，需於財報中核對。
- **近期財務里程碑**：Q2'26 收入、毛利率、營益率三項皆年增（毛利率 37.7%，較 Q2'25 的 34.0% 提升）。
- **Guidance**：DATA_UNAVAILABLE（工具未提供公司指引或 backlog / order book 數據）。
- **Segment 轉移**：DATA_UNAVAILABLE（工具未提供分部營收）。
- **M&A / 商譽增加**：2026 年上半年商譽增加約 $249.6M，原因待 10-Q 確認。
- **實體變更**：Yahoo 顯示 `prevName` 為 Vertiv Holdings Co.、`shortName` 為 Vertiv Holdings, LLC，`nameChangeDate` 為 2026-10-14。請查證是否為公司實體轉換或命名變更，確認對證券與報告主體的影響。
- **股息**：下一次 ex-dividend 相關日期（exDividendDate 工具值 2026-09-14）已過，dividendDate 為 2026-09-24（每季約 $0.063/股）。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue（TTM） | $11,479.6M | +24.1%（Q2'26） | 估計 YoY 約 +5–15% | 高於同業，成長強勁 |
| Revenue CAGR 2022–2025 | 21.6% | n/a | 估計 約 5–10% | 強 |
| Gross margin（Q2'26） | 37.7% | +3.7pp（vs 34.0%） | 估計 30–35% | 優於同業，改善中 |
| Operating margin（Q2'26） | 19.5% | +2.7pp（vs 16.8%） | 估計 12–15% | 優於同業 |
| Net margin（2025） | 13.0% | +6.8pp（vs 6.2%） | 估計 8–10% | 優於同業 |
| ROE（TTM） | 43.9% | n/a | 估計 約 15% | 高（權益基數小，需一併看 ROIC） |
| ROIC（估算） | 約 22.6% | n/a | 估計 約 10–12% | 優於同業（估算值） |
| FCF margin（TTM，計算） | 25.5% | 2025 年為 18.4% | 估計 約 10–15% | 強 |
| FCF/NI（TTM，計算） | 1.69 | 2025 年為 1.42 | 健康門檻 > 0.9 | 健康 |
| Capex / Revenue（TTM） | 3.7% | 2025 年為 2.2% | 估計 約 2–4% | 上升中，需留意 |
| Net debt（EV 口徑） | $227.6M | n/a（yf 口徑 $129.2M） | 估計 約 0.5–1.5x EBITDA | 低 |
| Debt / Equity | 70.2% | 2025 年底 約 81.9%（3,227.9 ÷ 3,941.3） | 估計 約 50% | 中性偏高，但權益成長快 |
| Current ratio | 1.38 | 2025 年底 約 1.55（6,819.5 ÷ 4,407.0） | 估計 約 1.8–2.0 | 偏低，流動負債增加 |
| Cash & STI | $3,110.6M | +70.2%（vs 2025 年底 $1,827.9M） | n/a | 改善 |
| Inventory（季末） | $2,522.7M | +73.2%（vs 2025 年底） | n/a | 需關注（DIO 約 113 天） |
| Accounts receivable（季末） | $3,750.3M | +20.6%（vs 2025 年底） | n/a | DSO 約 104 天，需關注 |
| Interest expense（TTM 代理） | Q2'26 $17.4M | 2025 年 -43%（$86.1M vs $150.4M） | n/a | 利息負擔下降 |
| Dividend coverage（FCF / 股息） | 約 34x | n/a | n/a | 極充裕 |
| Share count（ordinary） | 384.9M | +0.8%（vs 381.8M） | n/a | 稀釋低 |
| Insider sell 6m | $3.88M | 6m 外另有 $123.4M（2026-02/03） | n/a | 近期規模小 |
| Insider buy 6m | $0 | n/a | n/a | 無公開市場買入 |
| Short interest（占 float） | 3.74% | short ratio 2.75 天 | n/a | 偏低 |
| Trailing P/E | 53.7x | n/a | 估計 約 30–40x | 偏高 |
| Forward P/E | 25.8x | n/a | 估計 約 25–35x | 落於估計區間 |
| PEG | 0.81 | n/a | n/a | 具吸引力（依 Yahoo 口徑） |
| EV/EBITDA（TTM） | 34.2x | n/a | 估計 約 18–25x | 偏高 |
| P/FCF（TTM） | 31–34x | n/a | 估計 約 25–35x | 中性偏高 |
| P/S（TTM） | 7.96x | n/a | 估計 約 2–4x | 偏高 |
| Analyst mean target | $335.64（+41.4%） | n/a | n/a | 分析師普遍看多（rec mean 1.37） |
| Next earnings | 2026-10-21（估計） | Q3'26 EPS est $1.83（vs Q3'25 Reported $1.24，約 +48%） | n/a | 關鍵事件 |
| Guidance / Segment mix | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法評估 |

## Red flags
- **存貨與應收快速增加**：2026-06-30 季末存貨較 2025 年底增加 73.2%，DIO 由約 76 天升至約 113 天；AR 增加 20.6%。若需求放緩，存貨減值與收款風險會上升。
- **流動負債擴張**：流動負債增加 64.4%，其中 Other current liabilities 由 $177.3M（Q1'26）跳升至 $722.3M（Q2'26）。性質未知（可能為客戶預付款或其他應計項目），需查 10-Q 以確認是否為現金流持續性的來源。
- **總資產短期快速成長**：半年內總資產增加 30.2%，商譽增加 $249.6M。若為收購，需評估整合風險與對 ROIC 的影響。
- **Capex 季度跳增**：Q2'26 capex $174.5M，較 Q2'25 增加約 280%，TTM capex 佔營收由 2.2% 升至 3.7%。
- **估值高**：trailing P/E 53.7x、EV/EBITDA 34.2x，對於業績波動或指引下修的容忍度低。
- **股價動能弱於基本面**：現價低於 50 日與 200 日均線（-8.4% / -11.3%），較 52 週高點回落 37.5%。
- **治理風險分數（Yahoo）**：overallRisk 10/10、boardRisk 10、shareHolderRightsRisk 10、compensationRisk 9、auditRisk 8（數值越高越差）。此為第三方評分，本報告僅列示，未做獨立判斷。
- **內部人大額賣出歷史**：2026-02 至 03 合計約 $123.4M（窗口外），其後 2026-09 仍有賣出。近六個月規模小，但趨勢未見內部人加碼買入。
- **資料不一致**：（1）FCF 計算值 $2,924.0M 與 Yahoo $2,696.5M 差 $227M；（2）Net debt 三種口徑 $129.2M / $227.6M / $527.6M；（3）分析師數 28 vs 30；（4）調整後 EPS $1.52 vs GAAP diluted EPS $1.27（Q2'26）。以上需以 10-Q/10-K 為準。
- **實體名稱變更**：Yahoo 顯示 nameChangeDate 2026-10-14、shortName 為 "Vertiv Holdings, LLC"，需確認是否影響報告主體或證券代碼。
- **Q4'26 隱含 EPS 高**：consensus FY26 EPS $6.74 隱含 Q4'26 約 $2.22（推算，Reported EPS 口徑），高於 2026 年前三季任一季。若該季未達預期，forward 估值支撐可能下降。
- **資料缺口**：segment 營收、公司指引、backlog / order book、2021 年以前財報皆為 DATA_UNAVAILABLE 或 n/a，限制了長期 CAGR 與分部分析的可信度。

FUNDAMENTALS REPORT COMPLETE
