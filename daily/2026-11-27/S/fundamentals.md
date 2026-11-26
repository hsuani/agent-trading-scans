# Fundamentals — S (SentinelOne) as of 2026-11-27

資料說明: 價格與 info 快取 cached_at 2026-11-26 (source: cache, 屬預期)。財報最新為 2026-07-31 季 (FQ2 FY27, 2026-08-27 公布)，持股資料為 2026-09-30 (13F)，內部人交易最新為 2026-11-09。未發現 2026-11-27 之後的財務資料。公司財年結束於 1 月底 (FY26 = 2026-01-31)。金額單位: 財務報表為 M USD (百萬美元)，市值 / EV 為 B USD (十億美元)。

## 執行摘要

SentinelOne 仍是 GAAP 虧損公司 (FY26 淨損 -450.7M USD，TTM 淨損 -340.1M USD，EBITDA 為負)，但幾乎無有息負債、現金與短期投資 655.2M USD、流動比率 1.45，短期流動性沒有壓力。營收成長由 FY24 的 +47.1% 放緩至 2026-07 季的 +20.6%，營業虧損率則由 FY23 的 -95.4% 收斂至 Q Jul-26 的 -22.7%，但 TTM 自由現金流僅約 31M USD (依季度現金流加總推算)，遠低於同期股票報酬費用 SBC 322.0M USD，獲利品質仍弱。估值上 P/S 7.6x 低於同業中位數約 17.5x，forward P/E 52.3x 略低於同業中位數約 59.2x，但因 EBITDA 與 trailing EPS 為負，無法以獲利倍數定錨；整體財務健康度判定為「流動性佳、獲利與現金流尚未成形，中等偏弱」。本報告不提供交易建議。

## 營收與獲利能力

**營收成長**
- 財年營收 (M USD): FY23 422.2 → FY24 621.2 → FY25 821.5 → FY26 1,001.3。
- 3 年 CAGR (FY23→FY26) 約 33.4%。FY22 資料為 n/a，無法計算 4-5 年 CAGR。
- YoY 逐年放緩: FY24 +47.1%、FY25 +32.2%、FY26 +21.9%。
- 季度營收 (M USD): Jul-25 242.2、Oct-25 258.9、Jan-26 271.2、Apr-26 276.7、Jul-26 292.0；Jul-26 季 YoY +20.6%。
- TTM 營收 (info totalRevenue) 1,098.7 M USD，revenueGrowth 20.6%。
- 分部營收: yfinance 未提供分部拆分，business summary 僅列產品線 (Singularity Platform、Purple AI、SIEM、endpoint / cloud / identity 安全、exposure 管理、threat services)。分部營收與占比: DATA_UNAVAILABLE。

**毛利率 (Gross margin)**
- FY23 65.8% → FY24 71.1% → FY25 74.3% → FY26 74.1%，FY25 後趨於持平。
- 季度趨勢: Jul-25 75.0% → Oct-25 73.8% → Jan-26 72.6% → Apr-26 71.8% → Jul-26 72.1%，近四季小幅下滑。
- TTM 毛利率 (info) 72.5%，低於同業中位數約 76.2%。

**營業利益率 (Operating margin，yfinance Operating Income 口徑)**
- FY23 -95.4% → FY24 -59.8% → FY25 -40.1% → FY26 -30.9%。
- 季度: Jul-25 -31.7%、Oct-25 -27.1%、Jan-26 -29.5%、Apr-26 -28.8%、Jul-26 -22.7%，Jul-26 季為近六季最佳。
- 注意: Jul-26 季 yfinance as-reported 營業利益為 -90.8M，含 -24.4M 特殊項目 (重組 / 併購相關)，本表採 Operating Income -66.3M。
- 費用結構 FY26 (佔營收): S&M 52.5%、R&D 32.3%、G&A 20.2%。Jul-26 季 S&M 佔比 42.3% (Jul-25 季為 52.8%)，費用效率改善明顯。

**淨利率與每股盈餘**
- 淨利率 FY26 -45.0%、FY25 -35.1%；TTM -31.0% (info profitMargins -0.3095)。
- EPS (GAAP diluted): FY26 -1.37、FY25 -0.92；TTM -1.01 (與季度 EPS 加總 -0.27-0.23-0.33-0.18 一致)。
- 交叉驗證: FY26 淨損 -450.7M ÷ 稀釋股數 330.1M ≈ -1.37，與報表 EPS 一致。

**ROE / ROIC**
- ROE (info returnOnEquity): -23.0%。
- ROIC (推算, TTM 營業利益 -296.0M ÷ 最新 invested capital 1,448.5M): 約 -20.4%。yfinance 未直接提供 ROIC，此為推算值。

**Net interest income (利息收入)**
- 季度利息收入由 Jul-25 季 12.2M 降至 Jul-26 季 6.2M (YoY 約減半)，TTM 約 31.2M，FY25 為 49.9M。隨現金與短期投資下降，利息收入成為淨虧損的緩衝越來越小。

## 現金流與資產負債表

**現金流品質**
- 營業現金流 (OCF): FY24 -68.4M → FY25 +33.7M → FY26 +76.6M。
- 資本支出 (capex): FY26 -24.9M (佔營收 2.5%)、FY25 -27.1M、FY24 -18.8M。
- 自由現金流 (OCF − capex): FY26 +51.7M (FCF margin 5.2%)、FY25 +6.6M、FY24 -87.1M。
- TTM 推算 (由季度加總): OCF 57.4M − capex 26.3M ≈ FCF 31.1M，FCF margin 約 2.8%。TTM OCF 57.4M 與 info operatingCashflow 57.3M 一致，可信。
- 資料不一致: info freeCashflow 為 296.9M，但同一份資料的 OCF 僅 57.3M，而 FCF = OCF − capex 在 capex 為負的情況下不可能大於 OCF。此欄位無法對帳，本報告不採用，以 31.1M 為準。
- FCF / NI: 淨利為負，比率無意義 (n/m)。健康門檻 (>0.9) 不適用。
- SBC: FY26 297.6M (佔營收 29.7%)、FY25 267.5M (32.6%)、FY24 216.9M (34.9%)；TTM 322.0M (29.3%)。扣除 SBC 後，TTM FCF 約 -291M，現金流並未真正為股東創造價值。

**資產負債表 (最新 2026-07-31)**
- 現金及約當現金 201.0M；現金 + 短期投資 655.2M (FY26 末 628.7M、Jul-25 季 810.8M，YoY -19.2%)。
- 有息負債: 幾乎為零。Total debt 最近可得值為 2026-01-31 的 15.0M (主要為租賃負債)；info totalDebt 為 0。
- 淨現金 (推算): 約 640M USD (655.2M − 15.0M，Jul-26 總負債數字 n/a，採 Jan-26 值)。
- 流動比率: 1.45 (info) ；Jul-26 季推算 998.3 ÷ 688.8 = 1.45，一致。
- Debt/Equity: 約 1.0% (Jan-26，15.0 ÷ 1,437.1)。info debtToEquity 為 n/a。
- 營運資本: 309.5M (Jul-26)，Jul-25 為 495.9M，下降 37.6%。
- 總資產 2,381.5M，總負債 933.0M (Jul-26)，股東權益 1,448.5M。
- 商譽: 912.7M (Jul-26)，FY25 末為 629.6M，FY26 增加約 283M，來自收購 (見下)。有形淨值 427.7M。
- 累積虧損 (Retained earnings) -2,247.8M，仍在持續擴大。
- 流動遞延收入 500.5M (Jul-26)，YoY +9.5%；含非流動部分總計 577.5M，YoY +5.6%。遞延收入成長低於營收成長 (+20.6%)，是需要追蹤的訊號。
- 2026-07 季 Other Non Current Liabilities 升至 167.2M (Jan-26 為 4.1M)，內容 DATA_UNAVAILABLE，無法判斷是否與收購相關。

## 資本配置與內部人訊號

**資本配置**
- 回購: FY26 回購 200.0M USD (FY25 與 FY24 皆為 0)。季度資料僅可見 Oct-25 -49.2M、Jan-26 -98.1M，其餘季度 n/a。
- 回購規模超過 FY26 FCF (51.7M) 約 3.9 倍，缺口由現金與短期投資支應 (FY26 現金 + 短期投資下降 12.9%)。
- 股數仍在增加: 流通股數 FY24 304.7M → FY25 325.6M → FY26 337.8M → Jul-26 346.0M。FY26 年增 +3.7%；Jul-26 較 Jul-25 (332.1M) 增 +4.2%。回購未能抵銷 SBC 稀釋。
- 股利: 無。dividendYield 0.0，現金流量表無股利支出。
- 收購: FY26 購併支出 249.0M (FY25 123.8M、FY24 13.6M、FY23 281.0M)。收購標的與整合績效: DATA_UNAVAILABLE。FY26 Q4 季 (Jan-26) 商譽跳升，可見收購集中於該季。
- 資本支出維持低水準 (佔營收約 2.5%-3.3%)，屬輕資產模式。

**內部人交易 (近 6 個月，2026-05-27 至 2026-11-26)**
- 公開市場賣出 (Sale): 31 筆，合計約 30.19M USD、約 1.40M 股。無公開市場買入。
- 其中 CEO Tomer Weingarten 賣出 23.04M USD (約 76%)，CFO Sonalee Parekh 2.57M USD，Keenan Conder 1.39M USD，Robin Tomasello 1.17M USD，Barry Padgett 1.07M USD，Ana Pinczuk 0.95M USD。
- 另有 2026-10-05 CEO 行使衍生性證券 500,000 股 (執行價 9.74 USD，約 4.87M USD)，同日以約 25.26 USD 賣出 527,368 股 (約 13.32M USD)，屬行權後賣出。
- 6 個月內 4 筆 (約 231,764 股) 無價格紀錄、6 筆為獎勵授予 (Stock Award, 0 USD)。
- 規模: 賣出總額約占市值 0.36% (30.19M ÷ 8.38B)，內部人持股 0.875%。以市值比例看規模不大，但方向為單邊賣出。
- 賣出價格區間約 13.37 → 25.33 USD，股價上漲期間持續賣出，屬獲利了結型態。CEO 近月有固定規模的重複性賣出 (約 57,941 股)，是否為 Rule 10b5-1 計畫: DATA_UNAVAILABLE。
- 機構持股 88.7% (678 家)。前十大 (2026-09-30): BlackRock 7.23% (+7.2% QoQ)、AQR 6.20% (-9.1%)、Vanguard PM 5.53% (-3.0%)、First Trust 4.49% (+40.2%)、Vanguard CM 4.42% (+3.7%)、Legal & General 3.28% (+15.2%)、Shaw D.E. 2.19% (+113.6%)、Voya 2.03%、Wellington 1.98% (+35.4%)、Point72 1.94% (+72.4%)。前十大中多數為增持。
- 放空比率 (short % of float): 8.44%，約 28.45M 股，short ratio 2.25 日 (info)。

## 估值

以下價格為快取 24.09 USD，市值 8.38B USD，EV 7.73B USD (info)。

- P/E (trailing): n/m (EPS -1.01)。
- P/E (forward): 52.3x (info forwardPE，forwardEps 0.461)。注意: forwardEps 的會計基礎 (GAAP 或 non-GAAP) 不明，與 yfinance 次季 EPS 估計 +0.09 的基礎並不一致，此倍數僅供參考。
- EV/EBITDA: -32.5x (EBITDA -237.8M，負值，n/m)。
- P/S (TTM): 7.6x (8.38B ÷ 1.099B)；EV/Revenue 7.0x。
- P/FCF: 約 270x (8.38B ÷ 推算 TTM FCF 31.1M)。info-based 的 28.2x 因 FCF 欄位不可靠，不採用。
- P/B: 5.75x (info priceToBook)。
- 同業中位數 (CRWD、ZS、OKTA、PANW 的 cache info 推算，4 檔，非正式產業中位數):
  - P/S 中位數約 17.5x；EV/Revenue 中位數約 17.1x；forward P/E 中位數約 59.2x；毛利率中位數約 76.2%；營收成長中位數約 24.4%；營業利益率中位數約 1.9%。
  - S 相對同業: P/S 折價約 56%，毛利率低約 3.7 個百分點，營收成長低約 3.8 個百分點，營業利益率低約 28 個百分點。
- 分析師共識 (info): 30 位分析師，recommendationMean 2.03 (偏買進)，目標價平均 25.28、中位數 26.0、最高 31.0、最低 17.5。相對 24.09 USD，平均目標價隱含約 +4.9% 空間。
- 股價位置: 52 週區間 11.81 – 26.50 USD，52 週漲幅 +48.6%；50 日均 23.67、200 日均 18.44 (info)。Beta 0.565。

估值判讀: 相對營收，S 以 7.6x P/S 交易，明顯低於同業，但 S 的營收成長與毛利率也較同業低，且 TTM FCF 遠低於 SBC，折價有基本面依據。以 forward P/E 52x 衡量，與同業相當，但該 EPS 基礎不明，無法確認其含 SBC 與否。

## 催化劑

- 下次財報: 2026-12-03 (info earningsTimestamp，isEarningsDateEstimate = False)，對應 FQ3 FY27 (2026-10-31 季)。
- 近期財報表現: FQ2 FY27 (2026-08-27 公布) EPS -0.27，低於估計 -0.23 (miss -16.5%)。依 yfinance 所列 EPS 估計，近 8 季中 7 季低於估計 (2026-05 為唯一超越者)。EPS 估計的會計基礎不明，此結論僅作為方向參考。
- 次季 EPS 估計: +0.09 (yfinance)。此數字為正值，與過去 GAAP EPS 皆為負的歷史不同，基礎不明。
- 公司 guidance (營收 / EPS / FCF 指引): DATA_UNAVAILABLE。
- 營收共識 (下一季與全年): DATA_UNAVAILABLE。
- 產品與策略: AI 安全 (Purple AI)、與 AWS 合作推出 Bedrock AI 治理整合 (business summary)。
- 收購整合: FY26 購併 249M USD，對 FY27 營收與費用的貢獻: DATA_UNAVAILABLE。
- 最近新聞 (來自同日的 news.md，非本報告資料源): 2026-11-19 與新加坡 DCCOM 合作、2026-11-16 獲 Frost Radar 列為 Visionary Leader、2026-11-02 將 AI 安全擴展至 Claude Cowork。財務影響未揭露。

## Metrics table

金額單位: 營收、現金流、資產負債表欄位為 M USD；市值與 EV 為 B USD。同業中位數為 CRWD/ZS/OKTA/PANW 4 檔 cache info 推算，非正式產業中位數 (估計)。

| Metric | Latest | YoY | 同業中位數 (估計) | Verdict |
|---|---|---|---|---|
| 營收 TTM (M USD) | 1,098.7 | +20.6% (Jul-26 季) | 營收成長中位數 +24.4% | 成長放緩但仍健康，略低同業 |
| 營收 FY26 (M USD) | 1,001.3 | +21.9% | n/a | 三年 CAGR 33.4%，逐年放緩 |
| 毛利率 TTM | 72.5% | Jul-26 季 72.1% vs Jul-25 季 75.0% | 76.2% | 略低於同業且近期小幅下滑 |
| 營業利益率 Q Jul-26 (Operating Income 口徑) | -22.7% | Jul-25 季 -31.7% | TTM 中位數 +1.9% | 明顯改善，仍為虧損 |
| 淨利率 TTM | -31.0% | FY26 -45.0% | n/a | 虧損 |
| EPS TTM (GAAP diluted, USD) | -1.01 | FY26 -1.37 | n/a | 虧損 |
| ROE | -23.0% | n/a | n/a | 負值 |
| ROIC (推算, TTM) | -20.4% | n/a | n/a | 負值 |
| 自由現金流 TTM (推算, M USD) | 31.1 | FY26 51.7 | n/a (info 基礎約 34.9%) | 極薄，與 info 欄位不一致，採推算值 |
| FCF margin TTM (推算) | 2.8% | FY26 5.2% | n/a | 偏低 |
| FCF / NI | n/m | n/a | 健康門檻 >0.9 | 淨利為負，不適用 |
| SBC TTM (M USD, 佔營收) | 322.0 (29.3%) | FY25 32.6% | n/a | 高，但佔比下降 |
| 現金 + 短期投資 (M USD) | 655.2 | Jul-25 810.8 → -19.2% | n/a | 下降中 |
| 有息負債 (M USD) | 15.0 (Jan-26，主要租賃) | n/a | n/a | 幾乎無債 |
| 淨現金 (推算, M USD) | 約 640 | n/a | n/a | 充足 |
| 流動比率 | 1.45 | n/a | n/a | 良好 |
| Debt / Equity | 約 1.0% | n/a | n/a | 極低 |
| 營運資本 (M USD) | 309.5 | Jul-25 495.9 → -37.6% | n/a | 下降，需留意燃燒 |
| 流通股數 (M shares) | 346.0 | Jul-25 332.1 → +4.2% | n/a | 持續稀釋 |
| 回購 FY26 (M USD) | 200.0 | FY25 0 | n/a | 規模超過 FCF，未抵銷稀釋 |
| Capex FY26 (M USD, 佔營收) | 24.9 (2.5%) | FY25 27.1 (3.3%) | n/a | 輕資產 |
| 收購支出 FY26 (M USD) | 249.0 | FY25 123.8 | n/a | 商譽增加約 283M，效益 DATA_UNAVAILABLE |
| 遞延收入 流動 (M USD) | 500.5 | +9.5% | n/a | 慢於營收成長，需追蹤 |
| P/E trailing | n/m | n/a | n/a | 不適用 |
| P/E forward | 52.3x | n/a | 約 59.2x | 略低於同業，EPS 基礎不明 |
| EV/EBITDA | n/m (EBITDA -237.8M) | n/a | n/m | 不適用 |
| P/S TTM | 7.6x | n/a | 約 17.5x | 明顯折價 |
| EV/Revenue TTM | 7.0x | n/a | 約 17.1x | 明顯折價 |
| P/FCF (推算) | 約 270x | n/a | n/m | 估值依賴 FCF 改善 |
| P/B | 5.75x | n/a | n/a | 偏高 (因股東權益小) |
| 內部人淨賣出 6 個月 (M USD) | 30.19 賣出，0 買入 | 占市值 0.36% | n/a | 單邊賣出，規模小 |
| 機構持股比例 | 88.7% | n/a | n/a | 高 |
| 放空比率 (% float) | 8.44% | n/a | n/a | 中等 |
| 分析師目標價均值 (USD) | 25.28 (+4.9% vs 24.09) | 中位數 26.0 | n/a | 接近現價 |
| 下次財報 | 2026-12-03 | n/a | n/a | 於 as-of 後 |

## Red flags

- GAAP 持續虧損: FY26 淨損 -450.7M USD，TTM 淨損 -340.1M USD，EBITDA 為負 (-237.8M USD)，trailing P/E 與 EV/EBITDA 無法作為估值錨。
- 營收成長持續放緩: FY24 +47.1% → FY25 +32.2% → FY26 +21.9%，Jul-26 季 +20.6%。
- 自由現金流薄弱且被 SBC 吞噬: TTM FCF 推算約 31M USD，SBC 322.0M USD；扣除 SBC 後現金流為負。
- info freeCashflow (296.9M USD) 與 OCF (57.3M USD) 無法對帳，任何以該欄位計算的 FCF 倍數 (如 P/FCF 28x) 不可採用。
- 遞延收入成長落後營收: 流動遞延收入 +9.5% YoY，總計 +5.6%，營收 +20.6%。
- 股本持續稀釋: 流通股數 Jul-26 較 Jul-25 增 +4.2%；FY26 回購 200M USD 不足以抵銷。
- 回購以現金支應 (FY26 回購約為 FCF 3.9 倍)，現金與短期投資 YoY -19.2%，營運資本 YoY -37.6%。
- 利息收入減半 (Jul-25 季 12.2M → Jul-26 季 6.2M)，原本支撐淨損的緩衝正在消失。
- 收購 (FY26 249M USD) 使商譽增至 912.7M USD，有形淨值僅 427.7M USD；收購效益與整合風險 DATA_UNAVAILABLE。
- 所得稅費用 FY26 171.0M USD，在稅前虧損 -279.7M USD 的情況下仍有大額稅費；原因 (推測為估值備抵變動) DATA_UNAVAILABLE。
- Other Non Current Liabilities 於 Apr-26 季跳升至 167.2M USD，內容 DATA_UNAVAILABLE。
- EPS 估計對比: 近 8 季中 7 季低於估計 (2026-08 季 miss -16.5%)。EPS 估計的會計基礎不明。
- 次季 EPS 估計 (+0.09) 與 forwardEps (0.46) 與歷史 GAAP EPS 基礎不一致，前瞻估值的可比性不足。
- 內部人單邊賣出 6 個月合計約 30.19M USD，CEO 占 76%；未見公開市場買入。
- 資料缺口: 公司 guidance、營收共識、分部營收、10b5-1 計畫狀態、收購標的、Other Non Current Liabilities 內容，皆為 DATA_UNAVAILABLE，相關判斷需待下次財報後再確認。

FUNDAMENTALS REPORT COMPLETE
