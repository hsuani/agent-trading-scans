# Fundamentals — ARQQ as of 2026-10-15

## 執行摘要
ARQQ (Arqit Quantum Inc., NasdaqCM) 財務體質極弱: TTM 營收僅 $1.086M、TTM EBITDA 為 -$49.9M, FY2025 (9/30 結束) 營業現金流 -$29.6M, 2026-03-31 現金及短期投資 $28.9M, 以目前燃燒速度僅約 8 至 12 個月資金跑道 (估算, 非公司指引). 估值層面 trailing P/E、forward P/E、EV/EBITDA、P/FCF 皆為負值無法使用, P/S 246x、P/B 8.9x 缺乏獲利或現金流支撐, 估值吸引力低. 股價自 10/6 收盤 $23.43 至 10/14 收盤 $15.37 下跌約 34.4%, 同期內部人於 10/2 至 10/6 有約 $0.33M 的公開市場賣出, 股東結構集中 (前兩大機構合計約 65%) 且流通股僅約 5.0M 股, 籌碼面波動風險高.

## 資料來源與時效說明
- 即時行情 feed 本次為 403 CONNECT 失敗, `info` 與 `fast_info` 皆取自本地 cache (`source: cache`, cached_at 2026-10-15T11:16-11:19 UTC), 屬預期行為. 最新收盤價 $15.37 為 2026-10-14 (regularMarketTime 對應 2026-10-14 收盤).
- 技術指標 (`ta snapshot`) as_of 2026-10-14, 無超出 `{DATE}` 的資料.
- 最新已申報資產負債表為 2026-03-31 (Q2 FY2026). 2026-06-30 季度資料未出現於工具輸出, 視為資料落後 (DATA_UNAVAILABLE).
- `quarterly_fin` 與 `quarterly_cf` 回傳空陣列, 季度損益表與季度現金流為 DATA_UNAVAILABLE. 季度趨勢只能依 info 的 TTM 欄位推估.
- 無同業中位數 (sector median) 資料, 估值比較欄位一律標 DATA_UNAVAILABLE.
- 美股 ARQQ 資料完整度尚可, 但 info 內部有多處不一致 (見紅旗段).

## 營收與獲利能力
**營收趨勢 (annual, USD, FY 9/30 結束)**

| 年度 | 營收 | YoY | 營業損益 | 淨利 (common) |
|---|---|---|---|---|
| FY2022 | $7.212M | n/a | -$50.230M | +$65.075M |
| FY2023 | $0.640M | -91.1% | -$67.459M | -$74.527M |
| FY2024 | $0.293M | -54.2% | -$37.369M | -$56.818M |
| FY2025 | $0.530M | +80.9% | -$35.171M | -$35.343M |

- 3 年 CAGR (FY2022 至 FY2025): -58.1%. 營收基期已大幅縮小, 負成長的 CAGR 不代表公司本身營運惡化的唯一訊號, 更重要的是營收規模極小, 營運費用 FY2025 為 $35.7M, 約為營收的 67 倍.
- TTM 營收 $1.086M (info.totalRevenue) 高於 FY2025 全年 $0.530M, 顯示 2026 年營收已自低點回升, 但 info.revenueGrowth 回傳 8.299 (單位與基期不明, 應視為 "約 830%" 的季度 YoY, 無法從工具輸出獨立驗證).
- 分部 (segment) 資料: info.longBusinessSummary 只描述單一產品線 QuantumCloud (PaaS 加密金鑰服務) 與維護/專業服務, 無分部營收拆分, 標 n/a.
- 毛利: TTM grossProfits $0.540M, 毛利率 49.7%. FY 毛利資料未在 `financials` 回傳欄位中出現, 標 n/a.

**獲利能力**
- 營業利益率 (FY2025): -6,636%; (FY2024): -12,754%. 淨利率 (FY2025): -6,668%. TTM 淨利率 -4,510% (netIncomeToCommon -$48.978M / revenue $1.086M). info.operatingMargins -49.3 (即 -4,932%) 與上述數字同量級, 公司仍處於營收遠小於固定營運成本的階段.
- ROE: -220.2% (info.returnOnEquity -2.2021). ROA: -95.5%. ROIC: 無工具欄位, 以 FY2025 EBIT -$37.568M / invested capital $27.236M 粗估約 -138%, 僅供參考.
- FY2022 淨利為正 ($65.1M) 主要受 Total Unusual Items $103.9M 影響 (非營運項目), 不代表核心營運獲利能力.
- EPS: FY2025 diluted -$2.56, FY2024 -$11.23 (已反映 2024-09 的 1:25 reverse split), TTM -$2.92, forward EPS 估計 -$1.06 (info.forwardEps).

## 現金流與資產負債表
**現金流品質**

| 年度 | OCF | Capex | FCF | FCF 利潤率 | FCF/NI |
|---|---|---|---|---|---|
| FY2022 | -$26.719M | -$24.432M | -$51.151M | n/m | n/m |
| FY2023 | -$32.825M | -$16.123M | -$48.948M | n/m | n/m |
| FY2024 | -$34.126M | -$3.328M | -$37.454M | -12,783% | n/m |
| FY2025 | -$29.553M | -$0.549M | -$30.102M | -5,680% | 0.85 (兩者皆負, 比率僅供參考) |

- FCF 與淨利皆為負, FCF/NI 0.9 健康門檻不適用, 判定為不健康 (持續燃燒現金).
- TTM info.freeCashflow -$19.703M 與 info.operatingCashflow -$42.745M 的差距 (暗示 TTM capex 約 +$23M) 與 FY2025 年報不一致, 判定為資料不一致, 採保守口徑 (以較大的 OCF 燃燒量計算).
- Stock based compensation FY2025 $5.676M, 為非現金費用, 有助於降低現金燃燒但造成股權稀釋.

**資產負債表 (2026-03-31)**
- 現金及短期投資 $28.860M (FY2025 年底 $36.978M, 半年內下降 $8.118M).
- 總負債 $7.731M, 總資產 $36.236M, 股東權益 $28.505M.
- 總債務 $2.172M (FY2025 年底 $0.719M), 淨現金 $26.688M (cash - debt).
- Current ratio 4.88 (流動資產 $32.162M / 流動負債 $6.591M); quick ratio 4.61.
- Debt/Equity: info.debtToEquity 回傳 7.62 為百分比單位, 換算為 0.076x (2.172 / 28.505). 負債水準本身極低, 流動性風險主要來自現金燃燒而非負債到期.
- 有形帳面價值 (Tangible Book Value) FY2025 $25.124M; 每股 BVPS $1.719.
- 資金跑道估算: 現金 $28.86M / TTM OCF 燃燒 $42.745M ≈ 8.1 個月; 以 FY2025 OCF 計 ≈ 11.7 個月; 以 TTM FCF 計 ≈ 17.6 個月. 此為本報告估算, 非公司指引. 公司過去以股權募資 (FY2025 普通股發行 $37.2M) 支應營運, 後續再募資可能性高.

## 資本配置與內部人訊號
**資本配置**
- Capex: FY2022 $24.4M → FY2025 $0.5M, 降幅約 98%, 顯示公司已大幅收縮投資支出.
- 股份稀釋: 已發行股數 FY2024 (9/30) 11.55M → FY2025 15.29M (+32.4%) → 2026-03-31 16.58M (半年 +8.4%) → info.sharesOutstanding 17.40M (較 3/31 再 +5.0%). 9/2024 至今累計約 +51%.
- 普通股發行 (Common Stock Issuance): FY2023 $45.1M, FY2024 $13.1M, FY2025 $37.2M. 為主要資金來源.
- 股息: 0 (Cash Dividends Paid 各年皆為 0), 股息覆蓋率不適用 (payoutRatio 0.0).
- 買回 (buyback): 無 (Repurchase Of Capital Stock 欄位無資料, 視為無買回).

**內部人交易 (工具回傳約 2026-04-01 至 2026-10-12)**
- 公開市場買入 (Purchase): 0 筆.
- 公開市場賣出 (text 標示 "Sale at price"): 約 109,573 股, 總金額約 $2.84M, 約為市值 $267.5M 的 1.06%.
  - 其中董事 Lefebvre D'Ovidio (間接持股, Ownership: I) 於 2026-07-01 以 $30.07–30.24 賣出 54,444 股, 金額 $1.64M, 占總賣出金額約 58%. 扣除後, 其餘賣出約 $1.19M, 占市值約 0.45%.
  - 2026-10-02 至 10-06 期間多位管理層 (CEO Leaver, GC Willcocks, COO Wilder, Officer Feenan 與 Nilan, 董事 Ritchie) 以約 $23.78–24.47 出售合計約 $0.33M, 之後股價於 10/7 起 (10/8 單日 -17.8%, 量 828,900) 跌至 $15.37. 注意: 此段賣出時間點與股價重挫高度相鄰, 但工具不提供賣出原因, 不應直接推論為內部人預警.
- 期權/權證行使 (Conversion of Exercise at $2.50): Calabria 120,000 股 (6/3), Ritchie 73,562 股 (6/5), Lefebvre 4.6M 股 (9/22, 間接持股). 屬行使而非賣出, 但若隨後賣出將構成潛在供給壓力. 工具無法確認行使後是否賣出.
- 多筆 CEO/CFO 相關交易 (Text 為空, Value null, 如 Leaver 2026-10-01/02/05/12 約 5,208 股) 無法分類為買入、賣出或稅務代扣, 標 DATA_UNAVAILABLE (交易類型).
- 內部人持股 heldPercentInsiders 2.68%, 持股偏低, 管理層利益與股東綁定程度有限.
- 賣出金額 vs 市值: 整體約 1.06%, 絕對金額不大, 但相對於流通股僅 5.0M 股 (約為已發行股數 28.8%), 同期 109,573 股賣出約占流通股 2.2%.

## 估值
- Trailing P/E: n/a (TTM EPS 為負). Forward P/E: -14.5 (forwardEps -$1.06), 為負值, 判定 n/m.
- P/S (trailing): 246.3x (info.priceToSalesTrailing12Months; 市值 $267.5M / TTM 營收 $1.086M 驗證一致).
- EV/Revenue: 210.1x (info.enterpriseToRevenue; EV $228.2M / TTM 營收 $1.086M).
- EV/EBITDA: -4.57x (EBITDA TTM -$49.9M), 負值 n/m.
- P/FCF: n/m (TTM FCF 為負).
- P/B: 8.94x (price $15.37 / BVPS $1.719).
- 同業中位數: DATA_UNAVAILABLE (工具無同業資料).
- 市值: $267.5M (price $15.37 × sharesOutstanding 17.40M, 工具 marketCap 驗證一致). EV 報告值 $228.2M, 以市值 + 總債務 - 現金自行計算為 $240.8M, 差額 $12.6M 未能由工具欄位解釋, 以 info 報告值為準並標註.
- 技術面 (ta snapshot, 2026-10-14): 收盤 $15.37, MA20 $21.60 (-28.9%), MA50 $21.37 (-28.1%), MA200 $18.74 (-18.0%); RSI14 29.9 (接近超賣區), MACD -1.10 / signal -0.12 (MACD 走弱), 布林 %B ≈ 0.00 (觸及下軌), ATR14 $1.80, 20 日年化波動 106%. 52W 區間 info 為 $11.52–$53.60; ta 的 hi52w 為 $61.11 (兩者來源不同, 以 info 為準, 差異待查).
- 估值結論: 以任何現金流或獲利指標衡量均無法支撐估值, 目前市值主要反映 "量子加密" 題材與未來募資/營收放量的選擇權價值, 而非既有基本面.

## 關鍵催化劑
- 下次財報日: 2026-12-09 (earnings_dates 回傳, EPS Estimate 為 null, 屬工具列出的預估日). 該日期位於 FY2026 年度結束 (2026-09-30) 之後, 預期為 FY2026 全年報告.
- 2026-06-30 季度 (FY2026 Q3) 財報與 2026-03-31 以後的資產負債表: DATA_UNAVAILABLE. 最新 info 日期 (earningsTimestampStart 1779366600) 對應 2026 年 5 月, 為前一次財報窗口.
- 近期股價事件: 10/7 至 10/9 三日累計跌幅約 -24% (22.55 → 17.23), 10/8 單日 -17.8%, 量能放大至 828,900 (平均量約 30 萬). 工具不提供新聞與公告內容, 無法判斷事件原因, 標 DATA_UNAVAILABLE.
- 公司名稱記錄: info.prevName 為 Centricus Acquisition Corp., nameChangeDate 2026-10-15. 屬 SPAC 合併後的名稱歷史紀錄, 不一定代表 2026-10-15 有新公告, 不列為催化劑, 僅註記.
- 融資事件: 公司歷來依賴股權募資 (FY2023 $45.1M, FY2025 $37.2M), 現金跑道 8 至 12 個月的條件下, 近期募資公告或稀釋為高機率事件 (估計, 非工具資料).
- 大股東 (Defiance ETFs, Penserra) 於 2026-06-30 季報持股增加 (pctChange 約 +2.5%); 2026-09-30 季報 (Kessler 等) 持股變動僅列出部分. 完整 13F 資料未出齊, 標 DATA_UNAVAILABLE.

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價 (收盤, 2026-10-14) | $15.37 | 52W -57.4% (info) | DATA_UNAVAILABLE | 弱勢, 跌破 MA20/50/200 |
| 市值 | $267.5M | n/a | DATA_UNAVAILABLE | 小型股 |
| 營收 (TTM) | $1.086M | FY2025 +80.9% (FY 基準) | DATA_UNAVAILABLE | 規模極小 |
| 營收 3 年 CAGR (FY22–FY25) | -58.1% | n/a | DATA_UNAVAILABLE | 差 |
| 毛利率 (TTM) | 49.7% | n/a | DATA_UNAVAILABLE | 毛利結構尚可, 但絕對額小 |
| 營業利益率 (FY2025) | -6,636% | FY2024 -12,754% | DATA_UNAVAILABLE | 差, 改善中但仍極端 |
| 淨利率 (TTM) | -4,510% | n/a | DATA_UNAVAILABLE | 差 |
| EPS (TTM) | -$2.92 | FY2025 -$2.56 (FY24 -$11.23, 已 split 調整) | DATA_UNAVAILABLE | 差 |
| ROE | -220.2% | n/a | DATA_UNAVAILABLE | 差 |
| ROA | -95.5% | n/a | DATA_UNAVAILABLE | 差 |
| ROIC (粗估, FY2025) | -138% | n/a | DATA_UNAVAILABLE | 差 |
| OCF (FY2025) | -$29.6M | FY2024 -$34.1M (改善 13%) | DATA_UNAVAILABLE | 持續燃燒 |
| FCF (FY2025) | -$30.1M | FY2024 -$37.5M (改善 20%) | DATA_UNAVAILABLE | 持續燃燒 |
| FCF 利潤率 (FY2025) | -5,680% | n/a | DATA_UNAVAILABLE | 差 |
| FCF / NI (FY2025) | 0.85 (兩者皆負) | n/a | 0.9 (健康門檻) | n/m, 不健康 |
| 現金及短期投資 (2026-03-31) | $28.86M | 半年 -$8.12M (vs FY25) | DATA_UNAVAILABLE | 偏低, 跑道約 8–12 個月 |
| 總債務 (2026-03-31) | $2.17M | FY25 $0.72M | DATA_UNAVAILABLE | 低 |
| 淨現金 (2026-03-31) | $26.69M | n/a | DATA_UNAVAILABLE | 尚可, 但燃燒快 |
| Current ratio | 4.88 | n/a | DATA_UNAVAILABLE | 強 (短期) |
| Quick ratio | 4.61 | n/a | DATA_UNAVAILABLE | 強 (短期) |
| Debt / Equity | 0.076x | n/a | DATA_UNAVAILABLE | 低 |
| Capex (FY2025) | -$0.55M | FY2024 -$3.33M (-84%) | DATA_UNAVAILABLE | 投資大幅收縮 |
| 股息 / 買回 | 0 / 無 | n/a | DATA_UNAVAILABLE | 不適用 (無回饋股東) |
| 股數 (已發行) | 17.40M | Sep-24 起 +51% | DATA_UNAVAILABLE | 高度稀釋 |
| 內部人公開市場買入 (6 個月) | 0 筆 | n/a | DATA_UNAVAILABLE | 無買進訊號 |
| 內部人公開市場賣出 (6 個月) | 約 $2.84M (1.06% 市值) | n/a | DATA_UNAVAILABLE | 偏負面 (含 $1.64M 單一董事間接持股賣出) |
| 機構持股比例 | 82.6% | n/a | DATA_UNAVAILABLE | 集中, 前兩大約 65% |
| 內部人持股比例 | 2.68% | n/a | DATA_UNAVAILABLE | 低 |
| 流通股 (float) | 5.01M 股 (約 29% 已發行) | n/a | DATA_UNAVAILABLE | 籌碼薄, 波動大 |
| 空單 / 流通股 (shares short / float) | 45.1% (本報告以 sharesShort ÷ floatShares 計算) | 月內 -13.1% (2.60M → 2.26M) | DATA_UNAVAILABLE | 偏高, 需留意軋空 |
| 空單占流通股 (shortPercentOfFloat, 工具欄位) | 17.8% | n/a | DATA_UNAVAILABLE | 與上列不一致, 待確認 |
| Short ratio (days to cover) | 6.12 天 | n/a | DATA_UNAVAILABLE | 回補需時偏長 |
| Forward P/E | -14.5 (forwardEps -$1.06) | n/a | DATA_UNAVAILABLE | n/m |
| Trailing P/E | n/a | n/a | DATA_UNAVAILABLE | n/m |
| P/S (trailing) | 246.3x | n/a | DATA_UNAVAILABLE | 極高 |
| EV/Revenue | 210.1x | n/a | DATA_UNAVAILABLE | 極高 |
| EV/EBITDA | -4.57x | n/a | DATA_UNAVAILABLE | n/m |
| P/FCF | n/m (FCF 為負) | n/a | DATA_UNAVAILABLE | n/m |
| P/B | 8.94x | n/a | DATA_UNAVAILABLE | 偏高 |
| Beta | 2.79 | n/a | DATA_UNAVAILABLE | 高波動 |
| 技術: RSI14 / MACD hist | 29.9 / -0.98 | n/a | DATA_UNAVAILABLE | 弱勢, 近超賣 |
| 技術: 20 日年化波動 | 106% | n/a | DATA_UNAVAILABLE | 極高 |
| 下次財報日 | 2026-12-09 (預估) | n/a | DATA_UNAVAILABLE | 尚未公告 EPS 預期 |

## Red flags
- 營收規模極小 (TTM $1.086M) 對應營運費用約 $35–38M/年, 商業模式尚未證明可規模化.
- 所有獲利與現金流指標為負, 估值指標 (P/E, EV/EBITDA, P/FCF) 全部無法使用, P/S 246x.
- 現金跑道估算僅約 8–12 個月, 未來數月內很可能需再募資, 高機率再度稀釋. 股數 FY2024 至今已增加約 51%.
- 內部人於 2026-10-02 至 10-06 集中出售 (約 $0.33M), 之後股價下跌約 34%; 另有董事間接持股 $1.64M 賣出 (2026-07-01). 無任何公開市場買入.
- 股票 52 週跌幅 -57%, 近兩週 (10/7 至 10/14) 跌幅約 -32%, 工具無法解釋原因 (DATA_UNAVAILABLE), 需由 catalyst 或新聞來源補足.
- 股權結構集中: 前兩大機構 (Defiance ETFs 32.6%, Penserra 32.5%) 合計約 65%; 流通股僅約 5.0M 股, 單一機構出場即可造成大幅價格衝擊.
- 空單占流通股高 (45.1% 依 sharesShort/floatShares 計算, 工具欄位 17.8%), 兩者不一致, 解讀時需謹慎.
- 資料完整度問題: 季度損益與季度現金流為空 (DATA_UNAVAILABLE); 最新資產負債表停在 2026-03-31; 即時 feed 失敗改用 cache.
- info 內部不一致: (a) EV $228.2M 與自算 $240.8M 不符; (b) nonDilutedMarketCap $392.6M 隱含股數約 25.5M, 與 sharesOutstanding 17.40M 不符; (c) TTM FCF (-$19.7M) 與 TTM OCF (-$42.7M) 隱含 capex 方向不合理; (d) fast_info 的 open 與 market_cap 為 null; (e) allTimeHigh $1,038 未做 split 調整 (1:25 reverse split 2024-09), 不應用於判斷.
- 52W 高點不一致: info 為 $53.60, ta 為 $61.11 (來源差異), 技術面位階判斷需以單一來源為準.
- 非營運項目影響歷史獲利 (FY2022 淨利為正由 unusual items $103.9M 造成), 不得以單一年度淨利判斷獲利能力.

FUNDAMENTALS REPORT COMPLETE
