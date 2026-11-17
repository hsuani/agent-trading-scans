# Fundamentals — COHR as of 2026-11-18

資料基準：yfinance 即時來源失敗（CONNECT 403），本次全部財務與估值數據取自 repo cache（`source: cache`，cached_at 2026-11-17T15:54 UTC）。股價以 info 的 regularMarketPrice 201.575 為基準（對應 marketCap USD 39.70B），與 fast_info（207.85）及 ta snapshot（203.11）存在差異，見資料品質說明。財報期間為 FY2026（截至 2026-06-30）與 FQ1 FY2027（截至 2026-09-30，已於 2026-11-04 公布），未見 as-of 之後的財報資料。

## Executive summary
COHR 營收與獲利動能明顯加速（FY2026 營收 USD 7,118.2M，YoY +22.5%；FQ1 FY2027 營收 USD 2,370.3M，YoY +49.9%），毛利率與營業利益率同步擴張，資產負債表仍可控（net debt / TTM EBITDA 約 1.47x，current ratio 2.29）。然而現金流品質極差：TTM FCF 為 USD -1,840.8M，資本支出由 FY2025 的 USD 440.8M 暴增至 FY2026 的 USD 1,110.1M，並依賴約 USD 2.0B 股權增資與借貸，流通股數自 2025-06 底的 155.6M 增至 2026-09 底的 196.9M；估值上 trailing P/E 41.7x、EV/EBITDA 25.9x，前瞻 P/E 介於 12.8x–19.4x 取決於 EPS 來源。結論：獲利成長強勁但自由現金流為負且高度稀釋，估值是否合理取決於前瞻獲利兌現與資本支出回收速度；近 6 個月內部人淨賣出 USD 7.27M，規模相對市值（USD 39.7B）僅 0.02%，訊號有限。

## Revenue & profitability
**營收趨勢（USD M）**

| 期間 | 營收 | YoY |
|---|---|---|
| FY2023（6/30） | 5,160.1 | n/a |
| FY2024 | 4,707.7 | -8.8% |
| FY2025 | 5,810.1 | +23.4% |
| FY2026 | 7,118.2 | +22.5% |

- 3 年 CAGR（FY2023→FY2026）約 **11.3%**；FY2024 為低點，FY2025 起進入加速期。
- 季度趨勢：FY2026 各季 1,581.4 → 1,685.6 → 1,805.6 → 2,045.5（USD M），呈逐季加速；FQ1 FY2027 為 2,370.3，較 FQ1 FY2026 的 1,581.4 增 **+49.9%**，季增約 +15.9%。
- TTM 營收 USD 7,907.0M（與 info totalRevenue 7,907.1M 相符）。
- 分部結構：info.longBusinessSummary 指出兩大分部為 Datacenter & Communications（收發模組、CPO、光學電路交換器等）與 Industrial（準分子／固態／CO2 雷射、半導體設備用雷射、工程材料等）。**各分部營收與佔比：DATA_UNAVAILABLE**（工具未提供 segment 財務）。

**獲利能力**

| 指標 | FY2023 | FY2024 | FY2025 | FY2026 | TTM |
|---|---|---|---|---|---|
| 毛利率 | 31.4% | 30.9% | 35.2% | 37.5% | 38.2% |
| 營業利益率（EBIT/營收） | 1.6% | 2.6% | 9.2% | 12.7% | 11.4% |
| 淨利率 | -5.0% | -3.3% | 0.9% | 11.3% | 12.2% |

- 毛利率 FY2026 USD 2,669.0M，FQ1 FY2027 進一步升至 39.1%（927.8 / 2,370.3）。
- 營業利益 FY2026 USD 901.5M；FQ1 FY2027 USD 386.4M（營業利益率 16.3%），為歷史新高區間。
- FY2026 淨利 USD 805.0M **含一次性項目**：出售事業利益 USD 124.1M，且有效稅率僅 7%（稅費 USD 60.8M 對稅前 USD 847.7M）。扣除後獲利的品質需保守看待。
- FQ1 FY2027 淨利 USD 384.7M，稅務為 **USD 22.8M 之稅務利益**（稅前 USD 358.8M），故此季淨利亦有非營業因素加成。
- ROE：info returnOnEquity 9.27%（TTM）；以最新權益 USD 11,330M 估算約 8.5%。
- ROIC（估計）：TTM EBIT USD 1,167.5M × (1-21%) ÷ 投入資本約 USD 14,124M（總債 4,347 + 權益 11,330 - 現金 1,553）≈ **6.5%**。稅率 21% 為本報告假設，非工具數據。
- EPS：FY2026 GAAP diluted EPS USD 4.12（FY2025 為 -0.52）；TTM GAAP diluted EPS 約 4.82（與 info trailingEps 4.83 相符）。FQ1 FY2027 GAAP diluted EPS 1.90（YoY +59.7%）。

## Cashflow & balance sheet
**現金流（USD M）**

| 指標 | FY2023 | FY2024 | FY2025 | FY2026 | TTM（至 FQ1 FY27） |
|---|---|---|---|---|---|
| 營業現金流（OCF） | 634.0 | 545.7 | 633.6 | 79.5 | -59.1 |
| 資本支出（Capex） | -436.1 | -346.8 | -440.8 | -1,110.1 | -1,781.7 |
| 自由現金流（FCF） | 198.0 | 198.9 | 192.8 | -1,030.6 | -1,840.8 |

- FCF margin：FY2026 **-14.5%**，TTM **-23.3%**（TTM 營收 USD 7,907.0M）。
- FCF / NI：FY2026 **-1.28**，TTM **-1.91**，遠低於 0.9 健康門檻。
- Capex 強度：FY2026 佔營收 15.6%（FY2025 為 7.6%），Capex / D&A 約 2.1x（D&A FY2026 USD 521.9M）。FQ1 FY2027 單季 Capex USD 775.5M，約為 FY2026 第二至第四季合計（153.6 + 289.7 + 562.9 = 1,006.2）的 77%，顯示擴產投資仍在加速。
- SBC：FY2026 USD 186.5M（FY2025 160.2M）。
- 連續 4 季 FCF 皆為負：FQ2 FY26 -95.7、FQ3 -383.5、FQ4 -493.4、FQ1 FY27 -868.2（USD M）。

**資產負債表（USD M，最新為 2026-09-30）**

| 項目 | 2026-06-30 | 2026-09-30 |
|---|---|---|
| 現金及等價物 | 1,162.0 | 1,552.9 |
| 現金 + 短期投資 | 1,987.0 | 1,752.9 |
| 總債務 | 3,538.4 | 4,347.0 |
| Net debt（Yahoo 定義） | 2,060.2 | 2,447.7 |
| 流動資產 / 流動負債 | 6,925.5 / 2,853.9 | 7,924.3 / 3,456.6 |
| 股東權益 | 10,903.5 | 11,330.0 |
| 商譽 | 4,375.6 | 4,448.3 |
| 總資產 | 18,299.9 | 20,247.6 |

- Current ratio：**2.29**（最新）；quick ratio 0.97（info）。
- Debt / Equity：**38.4%**（總債 / 權益，自算；info debtToEquity 為 37.3%）。
- Net debt / TTM EBITDA：**1.47x**（TTM EBITDA USD 1,662.3M，info ebitda）；總債 / EBITDA 2.62x。
- 利息覆蓋：TTM EBIT USD 1,167.5M ÷ TTM 利息費用 USD 177.9M ≈ **6.6x**。
- 商譽佔總資產 22%、佔權益約 39%；有形權益約 USD 6,882M。
- 存貨：FY2026 USD 2,581.0M，較 FY2025（1,437.6）增 **+79.5%**，遠高於營收增速；應收帳款 USD 1,343.3M，較 FY2025（964.1）增 +39.3%。營運資金佔用明顯上升。

## Capital allocation & insider signal
**資本配置**
- 股本：流通股數由 FY2025 末 155.6M 增至 FQ1 FY2027 末 196.9M（**+26.5%**）；FY2026 普通股發行現金流入 USD 1,998.6M。稀釋幅度顯著。
- 債務：FY2026 舉債 USD 1,921.3M、償還 USD 2,399.6M；FQ1 FY2027 再舉債 USD 785.0M。
- 股票回購：FY2023–FY2026 皆為 0（非回購型）。
- 股息：現金股利 FY2026 USD 11.4M（FY2025 同額，FY2024 為 0）；另有特別股股利 USD 35.1M（FY2025 為 USD 129.9M）。FCF 為負，股利無 FCF 覆蓋。info dividendYield 與 trailingAnnualDividendRate 皆為 0，與現金流量表之股利支出不一致，**標記為資料不一致**。

**內部人交易（近 6 個月，2026-05-18 起）**

| 日期 | 人員 | 職務 | 類型 | 股數 | 金額（USD M） |
|---|---|---|---|---|---|
| 2026-11-09 | James Robert Anderson | CEO | 買進 @199.48 | 5,000 | 1.00 |
| 2026-11-10 | Enrico DiGirolamo | 董事 | 買進 @222.88 | 1,000 | 0.22 |
| 2026-09-11 | Enrico DiGirolamo | 董事 | 賣出 @305.98 | 5,315 | 1.63 |
| 2026-09-09 | Robert P. Beard | 高管 | 賣出 @309.32 | 500 | 0.15 |
| 2026-09-02 | Lisa Neal-Graves | 董事 | 賣出 @268.42 | 2,200 | 0.59 |
| 2026-09-01 | Julie Sheridan Eng | CTO | 賣出 @270.69–276.83 | 13,077 | 3.58 |
| 2026-08-31 | Enrico DiGirolamo / Stephen Skaggs | 董事 | 賣出 @276.85 / 276.88 | 4,544 合計 | 1.26 |
| 2026-08-18 | Sherri R. Luther | CFO | 賣出 @324.00 | 3,000 | 0.97 |
| 2026-07-22 | Sherri R. Luther | CFO | 賣出 @306.68 | 1,000 | 0.31 |

- 買進合計：**USD 1.22M**（2 筆，6,000 股）；賣出合計：**USD 8.49M**（8 筆，29,636 股）；淨額 **USD -7.27M**。
- 另有 8 月底之股票授予（Grant）與禮物轉讓（Gift），不計入買賣。
- 規模：淨賣出佔市值（USD 39.70B）約 **0.02%**，買進佔市值約 0.003%，對股價訊號強度有限。
- 解讀要點：賣出集中於 USD 270–325 區間（股價高點 440 之後的反彈期），買進則發生於 USD 199–223，即目前股價附近。CEO 於 11 月初以市價買進為近期唯一的大額自主買入，方向上為正面訊號，但金額小。
- 機構持股：87.6%（info heldPercentInstitutions），1,769 家機構。前五大為 BlackRock 8.68%、Vanguard Capital 6.50%、Vanguard Portfolio 5.13%、State Street 4.37%、FMR 4.16%（FMR 最新一季減持 25.6%）。
- 空單：short interest 約 10.0M 股，佔流通股 5.1%，short ratio 1.31 日。

## Valuation
**估值倍數（以 USD 201.575 計）**

| 指標 | 數值 | 計算／來源 |
|---|---|---|
| 市值 | USD 39.70B | info marketCap |
| 企業價值（EV） | USD 42.99B | info enterpriseValue |
| Trailing P/E | 41.7x | 201.575 ÷ TTM EPS 4.83 |
| Forward P/E（epsForward 15.79） | 12.8x | info forwardPE |
| Forward P/E（epsCurrentYear 10.41） | 19.4x | 201.575 ÷ 10.41，自算 |
| EV / TTM EBITDA | 25.9x | info enterpriseToEbitda，TTM EBITDA USD 1,662.3M |
| EV / TTM 營收 | 5.44x | info enterpriseToRevenue |
| P / TTM FCF | n/a | FCF 為負，無意義 |
| P / TTM 營收（P/S） | 5.02x | 39.70B ÷ 7,907.0M，與 info 一致 |
| P / B | 3.50x | info priceToBook |
| PEG | 0.46 | info pegRatio（以 forward EPS 之成長率計，未經 FCF 校正，參考價值低） |

- 同業中位數：**DATA_UNAVAILABLE**（工具未提供產業或同業估值資料，不以估計值替代）。
- 分析師共識（25 位）：平均目標價 USD 371.92（較現價 +84.5%）、中位數 USD 380、低標 USD 228（+13.1%）、高標 USD 524.96；推薦均值 1.54（buy）。此為外部共識，非本報告判斷。
- 技術位置（ta snapshot）：價格 USD 203.11 位於 MA20 214.76（-5.4%）、MA50 261.72（-22.4%）、MA200 296.67（-31.5%）下方；RSI14 42.2；52 週區間 130.42–440.00，距高點 -53.8%。20 日年化波動 130%，ATR14 USD 23.0，beta 2.23。

**估值判讀（事實層面）**
- 以 TTM GAAP 獲利計算，估值偏高（P/E 41.7x），但 FY2026–FQ1 FY2027 獲利呈倍數成長（FQ1 EPS 年增 +59.7%），P/E 隨獲利追趕而快速下修。
- 以前瞻 EPS 計算，P/E 落於 12.8x–19.4x，兩者差異來自 yfinance 欄位定義不一致（epsForward 15.79 大於 epsCurrentYear 10.41，超出一年的成長幅度需以官方財測確認）。
- 以 FCF 計算，估值無法評估（FCF 為負），實際估值取決於 Capex 何時轉為現金流。

## Key catalysts
- **已公布：FQ1 FY2027（2026-11-04 盤後）**：調整後 EPS USD 2.09，高於估計 1.97（+6.0%）；GAAP diluted EPS 1.90；營收 USD 2,370.3M（YoY +49.9%）。
- **下次財報**：2027-02-03（yfinance earnings_dates），EPS 估計 USD 2.40。日期來源為 yfinance，未經公司確認。
- **財測／指引（guidance）**：DATA_UNAVAILABLE（工具未提供管理層指引文字）。
- **分部營收轉變**：DATA_UNAVAILABLE（僅有業務描述，無分部財務數字）。
- **獲利紀錄**：近 9 季 EPS 皆超出估計，驚喜幅度 +1.1% 至 +11.3%（2025-11 為 +11.3%、2025-08 為 +8.7%、2026-02 為 +6.8%、2026-05 為 +1.1%、2026-08 為 +7.6%、2026-11 為 +6.0%）。此為一致性強的 beat 紀錄。
- **資本支出擴產**：FQ1 FY2027 Capex USD 775.5M。Capex 何時轉為營收與 FCF 之正向貢獻，是下一季最重要的觀察點。
- **融資動態**：FY2026 股權增資 USD 2.0B；FQ1 FY2027 再舉債 USD 785M。後續是否仍需外部融資，將直接影響稀釋幅度。

## Metrics table
單位：USD M（除非另註明）；USD B 僅用於市值與 EV。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 FY2026（USD M） | 7,118.2 | +22.5% | DATA_UNAVAILABLE | 強 |
| 營收 FQ1 FY2027（USD M） | 2,370.3 | +49.9% | DATA_UNAVAILABLE | 強 |
| 營收 3 年 CAGR（FY23–26） | 11.3% | n/a | DATA_UNAVAILABLE | 中性 |
| 毛利率（FY2026） | 37.5% | +2.3 pt | DATA_UNAVAILABLE | 改善中 |
| 營業利益率（TTM） | 11.4% | FY25 9.2% → FY26 12.7%（+3.5 pt） | DATA_UNAVAILABLE | 改善中 |
| 淨利率（TTM） | 12.2% | 含一次性項目，品質待確認 | DATA_UNAVAILABLE | 偏弱（品質） |
| ROE（TTM，info） | 9.3% | n/a | DATA_UNAVAILABLE | 偏低 |
| ROIC（估計，21% 稅率假設） | 約 6.5% | n/a | DATA_UNAVAILABLE | 偏低 |
| OCF（TTM，USD M） | -59.1 | n/a | DATA_UNAVAILABLE | 差 |
| FCF（TTM，USD M） | -1,840.8 | FY26 -1,030.6（FY25 +192.8） | DATA_UNAVAILABLE | 差 |
| FCF margin（TTM） | -23.3% | FY26 -14.5% | DATA_UNAVAILABLE | 差 |
| FCF / NI（TTM） | -1.91 | FY26 -1.28 | 健康門檻 > 0.9 | 差 |
| 資本支出（FY2026，USD M） | 1,110.1 | +151.8% | DATA_UNAVAILABLE | 投資期 |
| 資本支出佔營收（FY26） | 15.6% | FY25 7.6% | DATA_UNAVAILABLE | 偏高 |
| Net debt（2026-09-30，USD M） | 2,447.7 | 2026-06 為 2,060.2 | DATA_UNAVAILABLE | 可控 |
| Net debt / TTM EBITDA | 1.47x | n/a | DATA_UNAVAILABLE | 可控 |
| Current ratio（2026-09-30） | 2.29 | n/a | DATA_UNAVAILABLE | 良好 |
| Debt / Equity（2026-09-30） | 38.4% | n/a | DATA_UNAVAILABLE | 中性 |
| 利息覆蓋（TTM EBIT / 利息） | 6.6x | n/a | DATA_UNAVAILABLE | 尚可 |
| 流通股數（2026-09-30，M） | 196.9 | vs FY25 末 155.6 → +26.5% | DATA_UNAVAILABLE | 稀釋中 |
| 股票回購（FY23–FY26） | 0 | n/a | DATA_UNAVAILABLE | 無 |
| 內部人淨買賣（6 個月，USD M） | -7.27（買 1.22 / 賣 8.49） | 佔市值 0.02% | DATA_UNAVAILABLE | 中性偏弱（規模小） |
| Trailing P/E | 41.7x | n/a | DATA_UNAVAILABLE | 偏高 |
| Forward P/E（epsForward 15.79） | 12.8x | n/a | DATA_UNAVAILABLE | 偏低（依賴前瞻 EPS） |
| EV / TTM EBITDA | 25.9x | n/a | DATA_UNAVAILABLE | 偏高 |
| P / TTM FCF | n/a（FCF 為負） | n/a | DATA_UNAVAILABLE | 無法評估 |
| P / TTM 營收 | 5.02x | n/a | DATA_UNAVAILABLE | 偏高 |
| P / B | 3.50x | n/a | DATA_UNAVAILABLE | 偏高 |
| 分析師平均目標價 | USD 371.92（+84.5%） | n/a | DATA_UNAVAILABLE | 共識正面 |
| 股價相對 52 週高點 | -54.2%（現價 201.575 / 高點 440） | n/a | DATA_UNAVAILABLE | 技術弱 |

## Red flags
- **自由現金流連續 4 季為負**：FQ2 FY26 至 FQ1 FY27 分別為 -95.7 / -383.5 / -493.4 / -868.2（USD M），且 Capex 仍在加速（FQ1 FY27 單季 USD 775.5M）。
- **股本大幅稀釋**：流通股數 155.6M → 196.9M（+26.5%），FY2026 股權增資 USD 1,998.6M；稀釋與 FCF 缺口相互強化。
- **FY2026 獲利品質**：淨利含 USD 124.1M 出售事業利益，有效稅率 7%；FQ1 FY27 含 USD 22.8M 稅務利益。調整後 EPS（2.09）與 GAAP diluted EPS（1.90）存在差距。
- **營運資金膨脹**：存貨 +79.5%、應收帳款 +39.3%，遠高於營收增速 +22.5%（FY2026）。
- **商譽與無形資產**：商譽 USD 4,448M，佔總資產 22%；若發生減損，權益將受影響。
- **利息負擔**：TTM 利息費用 USD 177.9M，雖覆蓋 6.6x，但債務規模 USD 4,347M 在 Capex 高峰期將持續增加。
- **股利資料不一致**：現金流量表顯示股利支出 USD 11.4M、特別股股利 USD 35.1M，info 股息殖利率為 0；FCF 為負下股利不具覆蓋能力。
- **治理風險分數（yfinance，1–10，數值越高風險越高）**：overallRisk 8、shareHolderRightsRisk 9、compensationRisk 7、boardRisk 4、auditRisk 3。
- **股價技術面弱勢**：現價低於 MA20 / MA50 / MA200，距 52 週高點 -54%，beta 2.23，20 日年化波動 130%，短空部位佔流通股 5.1%。
- **機構動向**：FMR 最新一季減持 25.6%。
- **資料品質**：（1）即時來源失敗，全部數據來自 cache；（2）三個股價來源不一致：info 201.575、fast_info 207.85（cnyes cache）、ta 203.11；（3）epsForward 15.79 與 epsCurrentYear 10.41 差距過大，forward P/E 區間寬；（4）info 中 nameChangeDate 為 2026-11-17、prevName 為 II-VI Incorporated，屬 yfinance 欄位，未影響財務判讀但需留意；（5）Segment 財務、管理層指引、同業估值均為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
