# Fundamentals — INTC as of 2026-10-18

## Executive summary
INTC 的財務體質正在從谷底回升: Q2'26 營收 16,128M (YoY +25.4%)、營業利潤率回到 12.2%、TTM FCF 轉正 (約 2,831M), 但 TTM GAAP 淨損 -11,289M (EPS -2.12) 主要來自約 12.4B 非營業投資證券損失, 獲利品質偏低。資產負債表仍有負擔: 總債務 50,537M、Yahoo 口徑淨負債 37,663M, 且 Q2'26 發行 13B 新債, 加上股本 YoY 增加約 15%, 稀釋壓力明顯。估值上 forward P/E 42.7x、EV/EBITDA 29.1x、P/B 5.2x 已高於一般半導體估計中位數, 相對分析師目標均價 118.05 (+31%) 仍有想像空間, 但 52 週區間內波動極大 (beta 2.23, 52 週高點 142.35 至現價 89.85 回落 37%)。內部人 6 個月內唯一明確公開市場買入為 CEO Tan Lip-Bu 於 2026-08-11 以 95.00 買入 105,263 股 (約 10.0M)。

資料來源: `pipeline/tools/yf.py` (live 失敗後 fallback 到 `prices/yf/INTC.json`, `source: cache`, cached_at 2026-10-17T10:34Z)。報告 as-of 2026-10-18, 所有數據時間點均不晚於 2026-10-17, 無 post-date 資料。注意: 任務指定的 kind 名稱 (statements / ratings / holders) 不存在於工具中, 本報告改用對應的 financials / quarterly_fin / balance_sheet / quarterly_bs / cashflow / quarterly_cf / recommendations / rec_summary / major_holders / inst_holders。

## Revenue & profitability

**營收趨勢**
- FY 營收: FY22 63,054M → FY23 54,228M → FY24 53,101M → FY25 52,853M。FY25 YoY -0.5%。
- 3 年 CAGR (FY22–FY25): 約 -5.7% (本地計算)。工具只提供 4 個年度 IS, 5 年 CAGR 無法計算 (n/a)。
- 季度營收: Q2'25 12,859M → Q3'25 13,653M → Q4'25 13,674M → Q1'26 13,577M → Q2'26 16,128M。Q2'26 YoY +25.4%、QoQ +18.8%, 與 info.revenueGrowth 0.254 一致。
- TTM 營收 57,032M (四季加總, 與 info.totalRevenue 一致)。
- 分部營收: longBusinessSummary 只列出 CCG / DCAI / Intel Foundry 三個分部名稱, 工具未提供分部營收數字, 分部組合 DATA_UNAVAILABLE。

**利潤率趨勢**

| 期間 | 毛利率 | 營業利潤率 | 淨利率 |
|---|---|---|---|
| FY22 | 42.6% | 3.7% | 12.7% |
| FY23 | 40.0% | 0.06% | 3.1% |
| FY24 | 32.7% | -8.9% | -35.3% |
| FY25 | 34.8% | -0.04% | -0.5% |
| Q2'25 | 27.5% | -10.0% | -22.7% |
| Q1'26 | 39.4% | 6.9% | -27.5% |
| Q2'26 | 40.4% | 12.2% | -68.4% |
| TTM (Q3'25–Q2'26) | 38.9% (info.grossProfits 22,170M) | 約 7.6% (本地計算 4,308M/57,032M) | -19.8% (info.profitMargins) |

- 毛利率自 FY22 高點 42.6% 下滑至 FY24 低點 32.7%, FY25 回升至 34.8%, 近兩季持續改善 (Q2'25 27.5% → Q2'26 40.4%)。
- 營業利潤率 Yahoo info.operatingMargins 為 12.19%, 與本地以季度 Operating Income 加總計算的 TTM 7.6% 不同 (Yahoo 可能採用不同的非經常項目調整), 本報告以本地計算為主, 並標示差異。

**Net income 與 EPS 品質**
- FY25 淨利 -267M (FY24 -18,756M); 歸屬普通股東淨利 FY25 -267M, 稀釋 EPS -0.06。
- TTM 淨利 -11,289M (與 info.netIncomeToCommon 一致), trailing EPS -2.12。
- Q2'26 淨利 -11,033M, GAAP 稀釋 EPS -2.16; 其中 "Other Income Expense" -12,738M, 現金流量表對應的 "Gain Loss On Investment Securities" 為 +12,426M (非現金損失加回)。Q1'26 亦有 Write Off 4,027M 與 Asset Impairment 62M。
- Yahoo earnings_dates 的 "Reported EPS" (例如 Q2'26 0.42、Q1'26 0.29) 與 IS 的 GAAP 稀釋 EPS (-2.16、-0.73) 不一致, 前者應為調整後 (non-GAAP) EPS。本報告兩者均列出, 不混用。

**ROE / ROIC**
- ROE (info.returnOnEquity): -10.7%。
- ROIC: 工具未直接提供, 本地估算 = TTM 營業利潤 4,308M × (1-21%) / Invested Capital 138,079M (Q2'26) ≈ 2.5%, 屬估算值。

## Cashflow & balance sheet

**現金流量品質**
- OCF: FY22 15,433M → FY23 11,471M → FY24 8,288M → FY25 9,697M。
- Capex: FY22 24,844M → FY23 25,750M → FY24 23,944M → FY25 14,646M (FY25 YoY -38.8%)。
- FCF (OCF - Capex): FY22 -9,411M / FY23 -14,279M / FY24 -15,656M / FY25 -4,949M。FY25 FCF margin 約 -9.4%。
- TTM FCF (本地, 四季加總): 2,831M, FCF margin 約 5.0%。Q2'26 單季 FCF +4,450M (OCF 7,006M - Capex 2,556M), Q1'26 為 -2,540M。
- info.freeCashflow 為 4,866M, 與本地 TTM 2,831M 不一致, 差異原因工具未說明, 本報告以本地季度加總為準並標示。
- FCF / NI: TTM 與 FY25 淨利皆為負, 比率無意義 (n/a), 無法依 >0.9 標準判定。FY25 OCF/NI 同樣不適用。
- SBC: FY25 2,434M (佔營收 4.6%); Q2'26 686M。

**資產負債表 (Q2'26, 2026-06-30)**
- 總資產 202,439M; 總負債 99,296M; 股東權益 (母公司) 87,542M; 含少數股權總權益 103,143M; 少數股權 15,601M (FY25 為 12,079M, 持續上升)。
- 現金及等價物 12,874M; 短期投資 16,853M; 現金+短期投資合計 29,727M (與 info.totalCash 一致)。
- 總債務 50,537M (長期 48,549M + 一年內到期 1,988M)。
- 淨負債 (Yahoo 口徑, 總債務 - 現金及等價物): 37,663M。若計入短期投資, 淨負債為 20,810M (本地計算)。兩種口徑請勿混用。
- 淨負債趨勢 (Yahoo 口徑): Q2'25 41,114M → FY25 32,320M → Q1'26 27,784M → Q2'26 37,663M。Q2'26 債務回升主要因發行 13,000M 新債 (Issuance of Debt), 同期償還 8,332M。
- 流動比率 1.60 (流動資產 57,213M / 流動負債 35,670M, 與 info.currentRatio 一致); 速動比率 1.16 (info.quickRatio)。
- 債務/權益 0.49x (總債務 / 含少數股權權益, 與 info.debtToEquity 48.997% 一致)。
- 利息保障: TTM GAAP EBIT (營業利潤) 4,308M / TTM 利息支出 1,150M ≈ 3.7x (本地估算)。
- 商譽: FY25 23,912M → Q1'26 起降至 20,465M (-3,447M, 約 -14.4%), 工具未說明減損原因, 需參閱 10-Q (DATA_UNAVAILABLE 細節)。
- 存貨: 12,492M (Q2'26), 高於 FY25 11,618M。應收帳款 4,033M。

## Capital allocation & insider signal

**資本配置**
- 股利: FY22 5,997M → FY23 3,088M → FY24 1,599M → FY25 0。目前股息率 0, info.payoutRatio 0, 股利已停付, 無覆蓋率可言。
- 買回: FY21 2,415M 之後無買回紀錄 (FY22–FY25 為 0 或 n/a)。
- 股本稀釋: 普通股流通股數 Q2'25 4,377M → Q2'26 5,043M (YoY +15.2%); 稀釋加權股數 Q2'25 4,369M → Q2'26 5,104M (YoY +16.8%)。FY25 股票選擇權行使收入 13,477M (Yahoo 現金流量表), 同期 FY25 淨債務償還 3,750M, 資金來源以股權與債務並重 (用途未由工具說明)。
- 資本支出: TTM 12,105M, 佔 TTM 營收 21.2%; Capex / D&A (FY25) 約 1.25x, 仍為重資產投入期。
- 債務償還 FY25 7,243M; 新發行 3,493M。

**內部人交易 (6 個月, 2026-04-18 至 2026-10-18)**

工具回傳 Transaction 欄位大多空白, 無法完全判定是否為 RSU 歸屬或稅務扣繳 (已標示為不明)。僅有價格與金額的筆數如下:

| 日期 | 內部人 | 職位 | 性質 | 股數 | 價格 | 金額 |
|---|---|---|---|---|---|---|
| 2026-08-11 | TAN LIP-BU | CEO | 公開市場買入 (Purchase, 間接持有) | 105,263 | 95.00 | 約 9,999,985 (約 10.0M) |
| 2026-05-29 | CHANDRASEKARAN N. | CTO | 賣出 (Sale) | 21,024 | 118.28 | 約 2,486,698 (約 2.49M) |
| 2026-05-01 | MILLER BOISE APRIL | Officer | 賣出 (Sale) | 40,256 | 99.53 | 約 4,006,519 (約 4.01M) |

其他無價格紀錄: 2026-07-30 CHANDRASEKARAN 33,007 股; 2026-06-01 ZINSNER 37,015 股; 2026-05-07 董事會成員多筆 12,552 股 (典型年度董事股權獎勵), 合計約 129,757 股; 2026-04-30 CHANDRASEKARAN 33,008 股。性質不明, 視為股權獎勵或稅務扣繳相關, 不計入買賣。

- 6 個月公開市場買入合計: 約 10.0M (CEO 一筆)。
- 6 個月公開市場賣出合計: 約 6.49M (CHANDRASEKARAN 2.49M + MILLER 4.01M)。
- 淨買入: 約 +3.5M。
- 相對市值 474,956M: 淨買入約 0.0007% 市值, 規模極小。訊號意義主要在於 CEO 以 95.00 買入, 現價 89.85 低於其買價約 5.4%。
- 前一期 (2025-10 至 2026-04) 紀錄: ZINSNER 於 2026-01-26 以 42.50 買入 5,882 股 (約 0.25M); MILLER 於 2026-02-02 以 49.05 賣出 20,000 股 (約 0.98M)。
- 持股比例: 內部人持股 13.99% (heldPercentInsiders), 機構持股 62.89%, 機構家數 4,415。
- 空頭: 空單 167.2M 股 (前月 152.2M, +9.8%), 佔流通股 3.16%, 空單回補天數 1.58 日。

**大股東 (2026-06-30 13F)**: BlackRock 8.46% (持股 -4.7%)、Vanguard Capital Management 5.65%、State Street 4.30%、Nvidia 4.26%、Invesco 3.13%、Geode 2.19%、FMR 1.87% (持股 +64.2%)、Vanguard Portfolio Management 1.77%、SoftBank 1.72%、Primecap 1.49%。前十大合計約 34.8%, 結構分散, 策略股東為 NVIDIA 與 SoftBank。

**治理風險 (Yahoo 評分, 1–10 越高風險越高)**: overallRisk 7、auditRisk 8、compensationRisk 9、boardRisk 4、shareHolderRightsRisk 2。CEO Tan Lip-Bu FY2025 總薪酬 3,828,200 美元。

## Valuation

- 現價 89.85 (2026-10-17 收盤, regularMarketChange -5.52, -5.79%); 當日區間 89.19–94.22; 成交量 121.4M, 高於 10 日均量 99.8M。
- 市值: 474,956M (info.marketCap, 以 5,286M 股計算)。注意 Yahoo sharesOutstanding 5,286M 與資產負債表 Q2'26 普通股流通數 5,043M 不一致, 市值數字可能包含後續發行, 此差異工具未說明。
- EV: 489,614M。

| 指標 | 數值 | 計算/來源 |
|---|---|---|
| Trailing P/E | n/a | EPS 為負 (-2.12) |
| FY26 P/E (priceEpsCurrentYear) | 58.8x | 89.85 / epsCurrentYear 1.528 |
| Forward P/E | 42.7x | info.forwardPE, 89.85 / epsForward 2.105 |
| PEG | 1.36 | info.pegRatio |
| EV/Revenue (TTM) | 8.6x | info.enterpriseToRevenue |
| EV/EBITDA (TTM) | 29.1x | info.enterpriseToEbitda, EBITDA 16,840M (Yahoo 口徑) |
| P/S (TTM) | 8.3x | info.priceToSalesTrailing12Months |
| P/B | 5.2x | 89.85 / bookValue 17.359 |
| P/FCF (TTM 本地) | 約 168x | 474,956 / 2,831 |
| P/FCF (Yahoo freeCashflow) | 約 98x | 474,956 / 4,866 |

- 分析師: 43 位, recommendationMean 2.47 (介於 Buy 與 Hold 之間, 1 為最強買進), recommendationKey "buy"。最新 rec_summary: strongBuy 1 / buy 14 / hold 32 / sell 1 / strongSell 1。近 3 個月 buy 由 13 增至 14, sell 由 1 增至 2 (-3m 時點), 整體變動不大。
- 目標價: 平均 118.05 (+31.4%)、中位數 115.00、高 200.00、低 80.00 (低於現價 -11%)。
- 價格位置: 52 週區間 32.89–142.35, 現價較 52 週高點 -36.9%、較 52 週低點 +173%; 50 日均線 103.17 (現價 -12.9%)、200 日均線 84.56 (現價 +6.3%); beta 2.23。
- 估值比較 (sector 中位數為估計值, 工具未提供): 半導體估計 forward P/E 約 25–30x, EV/EBITDA 約 18–22x, P/S 約 6–8x, P/B 約 4–5x。INTC 各項估值倍數均在估計區間上緣或以上。

## Key catalysts

- **下次財報**: 2026-10-29 (Yahoo 時間戳 20:00Z, 約美東 16:00, 通常為盤後; 工具為 earnings_dates 首筆, isEarningsDateEstimate = false)。
- **共識 EPS (Yahoo 調整口徑)**: 0.39 (earnings_dates 首筆 EPS Estimate)。
- **近四季 EPS 超預期紀錄 (調整後)**: Q3'25 0.23 vs 0.01 (+3,162%); Q4'25 0.15 vs 0.08 (+82%); Q1'26 0.29 vs 0.01 (+2,109%); Q2'26 0.42 vs 0.22 (+95%)。連續四季大幅超預期, 但 GAAP 仍連續虧損 (Q2'26 -2.16)。
- **FY26 / 次年共識**: epsCurrentYear 1.528、epsForward 2.105 (forward 年度定義工具未說明)。
- **分部/營運動態**: 分部組合數字 DATA_UNAVAILABLE; Q2'26 毛利率 40.4% 與營業利潤率 12.2% 為最新營運改善訊號。
- **管理層指引 (guidance)**: 工具未提供 guidance 欄位, DATA_UNAVAILABLE。
- **投資組合減損/證券公允價值**: Q2'26 約 12.4B 非營業損失 (對應 Gain/Loss on Investment Securities) 若在財報中延續, 將持續影響 GAAP EPS, 工具無法判定具體來源。
- **其他事件**: 2026-07-23 已公布 Q2'26 財報; 股利已停付, 不存在近期除息事件。

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (Q2'26) | 16,128M | +25.4% | 約 +10–15% (估計) | 強於估計, 成長回升 |
| 營收 3Y CAGR (FY22–FY25) | -5.7% | n/a | 約 +5–8% (估計) | 弱 |
| 毛利率 (Q2'26) | 40.4% | +12.8pp (Q2'25 27.5%) | 約 50–55% (估計) | 仍偏弱, 改善中 |
| 營業利潤率 (Q2'26) | 12.2% | +22.2pp (Q2'25 -10.0%) | 約 25% (估計) | 改善, 仍低於估計 |
| 營業利潤率 (TTM, 本地) | 7.6% | n/a | 約 25% (估計) | 偏弱 |
| 淨利率 (TTM) | -19.8% | n/a | 約 15–20% (估計) | 弱 |
| ROE (TTM) | -10.7% | n/a | 約 15–20% (估計) | 弱 |
| ROIC (估算) | 約 2.5% | n/a | 約 15% (估計) | 弱 |
| FCF (TTM, 本地) | 2,831M | 由 FY25 -4,949M 轉正 | n/a | 轉正, 但規模小 |
| FCF margin (TTM) | 5.0% | n/a | 約 20% (估計) | 偏弱 |
| FCF / NI | n/a (NI 為負) | n/a | >0.9 | 不適用 |
| Capex (TTM) / 營收 | 21.2% | FY25 Capex -38.8% | 約 10–15% (估計) | 仍高, 投資期 |
| 流動比率 | 1.60 | n/a | 約 2.0 (估計) | 尚可 |
| 速動比率 | 1.16 | n/a | 約 1.5 (估計) | 尚可 |
| 淨負債 (Yahoo 口徑) | 37,663M | Q2'25 41,114M (-8.4%) | n/a | 偏高, 但較去年下降 |
| 債務/權益 | 0.49x | n/a | 約 0.3–0.5x (估計) | 中性 |
| 利息保障 (TTM EBIT/利息) | 約 3.7x | n/a | 約 8–10x (估計) | 偏弱 |
| 普通股流通股數 | 5,043M | +15.2% (Q2'25 4,377M) | 約 +1–2% (估計) | 稀釋明顯 |
| 股利殖利率 | 0% | 股利 FY24 1,599M → FY25 0 | 約 1% (估計) | 已停付 |
| 買回 | 無 (FY22–FY25) | n/a | n/a | 無回購 |
| 內部人淨買賣 (6M) | 淨買入約 +3.5M (買 10.0M / 賣 6.49M) | n/a | n/a | 中性偏正, 規模小 |
| Forward P/E | 42.7x | n/a | 約 25–30x (估計) | 偏貴 |
| EV/EBITDA (TTM, Yahoo) | 29.1x | n/a | 約 18–22x (估計) | 偏貴 |
| P/FCF (TTM 本地) | 約 168x | n/a | 約 25–30x (估計) | 很貴 |
| P/S (TTM) | 8.3x | n/a | 約 6–8x (估計) | 偏貴 |
| P/B | 5.2x | n/a | 約 4–5x (估計) | 偏貴 |
| 分析師平均目標價 | 118.05 (+31.4%) | n/a | n/a | 上行空間 (分析師視角) |
| Beta | 2.23 | n/a | 約 1.2–1.5 (估計) | 高波動 |
| 空單佔流通股 | 3.16% | 空單 +9.8% (前月比) | 約 2–4% (估計) | 中性 |
| 治理風險 overallRisk | 7/10 | n/a | n/a | 偏高, compensationRisk 9 |

## Red flags
- GAAP 獲利品質低: TTM 淨損 -11,289M, Q2'26 淨損 -11,033M 主要來自約 12.4B 非營業投資證券損失; 調整後 EPS 與 GAAP EPS 差距極大 (Q2'26 0.42 vs -2.16), 獲利可靠度需以 GAAP 為準審視。
- 股本稀釋: 普通股流通股數 YoY +15.2%, 稀釋加權股數 YoY +16.8%, 股東權益與每股價值被稀釋。
- 淨負債回升: Yahoo 口徑淨負債 FY25 32,320M → Q2'26 37,663M; Q2'26 單季發行新債 13,000M。
- 股利已停付 (FY25 為 0), 且無買回, 資本配置以再投資與股權融資為主。
- 少數股權快速增加: 12,079M (FY25) → 15,601M (Q2'26), 其他股東所佔權益上升, 需關注合併報表結構。
- 商譽減記: 商譽 23,912M → 20,465M (-14.4%), 無法從工具判定原因, 屬非現金減損風險訊號。
- 估值偏高: forward P/E 42.7x、P/FCF 約 168x、EV/EBITDA 29.1x、P/B 5.2x, 估值對後續營運改善的兌現度依賴很高。
- 空頭與波動: beta 2.23, 單日 -5.79%, 空單 167.2M 股 (較前月增加 9.8%)。
- 內部人賣出 (CTO 2.49M、Officer 4.01M) 與 CEO 買入 (10.0M) 並存, 金額相對市值極小, 不足以構成明確內部人方向訊號。
- 治理風險: compensationRisk 9/10、auditRisk 8/10, overallRisk 7/10。
- 資料限制: 分部營收、管理層指引、商譽減損原因、Yahoo 口徑與本地 TTM FCF 差異 (4,866M vs 2,831M)、Yahoo 營業利潤率 (12.19%) 與本地 (7.6%) 差異, 均為 DATA_UNAVAILABLE 或需交叉核對。
- 資料為 cache 版本 (source: cache, cached_at 2026-10-17), 非即時報價; 報告 as-of 2026-10-18 下仍在 2026-10-29 財報前。

FUNDAMENTALS REPORT COMPLETE
