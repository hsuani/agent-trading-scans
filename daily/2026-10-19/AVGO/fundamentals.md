# Fundamentals — AVGO as of 2026-10-19

資料說明: 分析基準日 2026-10-19 (台北)。價格為 2026-10-16 收盤 $328.75 (快取, live feed 被擋, 10/17 與 10/18 無 bar)。財報來自 `pipeline/tools/yf` 輸出 (`cnyes` 快取 / yfinance), TTM 以最近四季 quarterly 數字加總計算。所有工具輸出中沒有晚於 2026-10-19 的實際數字; 2026-12-09 財報日為未來預估。

## Executive summary
AVGO 的財務體質強勁: TTM 營收 $89.1B、Q3 FY26 年增 85.5%、TTM FCF $39.4B (FCF margin 44.2%), 淨負債已由 FY24 的 $58.2B 降至 Q3 FY26 的 $35.4B。估值面, 以 GAAP trailing P/E 43x、EV/EBITDA 30.7x、P/S 17.6x 衡量明顯偏高, 以 consensus forward P/E 17.0x 衡量則相對合理, 但 forward EPS 的口徑 (疑為 non-GAAP) 與 trailing GAAP 不可直接比較。內部人在近六個月呈現淨賣出, 且股價已自 52 週高點 $495 回落約 33.6%、位於 MA50 與 MA200 之下, 財報品質與估值風險需與趨勢一併判斷。

## Revenue & profitability

### 營收
| 期間 | 營收 | YoY |
|---|---|---|
| FY2022 (10/31) | $33.20B | n/a |
| FY2023 | $35.82B | +7.9% |
| FY2024 | $51.57B | +44.0% |
| FY2025 | $63.89B | +23.9% |
| TTM (至 Q3 FY26, 2026-07-31) | $89.10B | — |

- 3 年 CAGR (FY22 至 FY25): **24.4%**。FY21 數字為 null, 無法計算 4-5 年 CAGR。
- 季度趨勢加速明顯: Q3 FY25 $15.95B → Q4 FY25 $18.02B → Q1 FY26 $19.31B → Q2 FY26 $22.19B → Q3 FY26 $29.59B。Q3 年增 +85.5%, 與 info 的 revenueGrowth 0.855 一致。
- 分部營收: yf 無分部數字 (longBusinessSummary 只描述兩大分部: Semiconductor Solutions 與 Infrastructure Software), 分部佔比 n/a。
- 次要來源 (新聞快取, 未經 8-K 核實) 提及管理層將 FY26 AI 半導體營收指引上調至約 $58B, 並預期 FY27 AI 營收約再翻倍。此數字未能由工具驗證, 僅供參考。

### 獲利能力
| 期間 | Gross margin | Operating margin | Net margin |
|---|---|---|---|
| FY2022 | 66.5% | 43.0% | 34.6% |
| FY2023 | 68.9% | 45.9% | 39.3% |
| FY2024 | 63.0% | 29.1% | 11.4% |
| FY2025 | 67.8% | 40.8% | 36.2% |
| TTM (GAAP 計算) | 68.8% | 48.5% | 42.9% |
| Q3 FY26 | 69.1% (Q3 FY25: 67.1%) | 54.3% (Q3 FY25: 38.1%) | 44.2% (Q3 FY25: 26.0%) |

- FY24 獲利谷底主要與 VMware 收購相關的整合費用與攤銷有關 (Special Income Charges FY24 $1.53B, D&A $10.0B), 非營運面的結構性惡化。
- TTM ROE 約 40.8% (以 TTM NI $38.3B 除以 Q2–Q3 FY26 平均股東權益 $93.7B 估算); info 欄位為 44.2%。
- ROIC 約 20% (以 TTM operating income $43.2B × (1 − 25.57% 稅率) 得 NOPAT $32.2B, 除以 Q3 FY26 invested capital $159.1B)。
- Info 欄位 grossMargins 75.5%、operatingMargins 54.3% 與 GAAP TTM (68.8%、48.5%) 不同, 前者疑為非 GAAP 或單季口徑, 本報告以 GAAP 計算值為準。
- R&D 絕對值由 FY25 $11.0B 降至 FY26 季均約 $2.9B, 占營收由 Q3 FY25 的 19.1% 降至 Q3 FY26 的 9.8%, 規模效應明顯。

## Cashflow & balance sheet

### 現金流品質
| 期間 | OCF | Capex | FCF | FCF margin | FCF / NI |
|---|---|---|---|---|---|
| FY2022 | $16.74B | $0.42B | $16.31B | 49.1% | 1.42 |
| FY2023 | $18.09B | $0.45B | $17.63B | 49.2% | 1.25 |
| FY2024 | $19.96B | $0.55B | $19.41B | 37.6% | 3.29 (NI 受 FY24 一次性費用壓低) |
| FY2025 | $27.54B | $0.62B | $26.91B | 42.1% | 1.16 |
| TTM | $40.65B | $1.25B | $39.40B | 44.2% | 1.03 |

- FCF/NI TTM 1.03, FY25 1.16, 均高於 0.9 健康門檻。
- Capex 占營收僅約 1% (fabless 模式)。但 Q3 FY26 capex 為 $532M, 季增 +130%, 需留意未來擴產趨勢。
- SBC FY25 為 $7.57B (占營收 11.8%); TTM SBC $8.48B。扣除 SBC 後的 FCF 約 $30.9B, 約為 FCF 的 78%。
- Q3 FY26 營運現金流 $14.2B, 季增 +35%, 季度動能強。

### 資產負債表 (2026-07-31, Q3 FY26)
| 項目 | 數值 | 備註 |
|---|---|---|
| 現金 | $23.98B | FY25 末 $16.18B, Q3 FY25 $10.72B |
| Total debt | $59.42B | FY25 末 $65.14B, FY24 末 $67.57B |
| 淨負債 | $35.44B | FY25 末 $48.96B, Q3 FY25 $53.50B |
| 淨負債 / TTM EBITDA | 0.68x | EBITDA 以 quarterly 加總 $52.3B 計 |
| Current ratio | 2.50 | 流動資產 $52.17B / 流動負債 $20.84B |
| Debt / Equity | 59.6% | 股東權益 $99.69B |
| 股東權益 | $99.69B | 每股帳面價值 $20.88 |
| Goodwill + 無形資產 (FY25) | $130.07B | 占總資產 76.0%, 來自 VMware 收購 |
| Tangible book value (FY25) | −$48.78B | 有形權益為負 |
| 利息費用 (FY25) | $3.21B | 以 FY25 EBIT $25.9B 估算利息保障約 8.1x |

- 淨負債持續下降, 且 Q3 現金大幅回升, 短期流動性充裕。
- 有形權益為負、商譽比重極高, 屬收購型公司的結構特徵, 不代表現金流問題, 但減損風險需關注。
- 總負債中長期債 $57.17B, 短期債 $2.25B, 到期結構未由工具提供 n/a。

## Capital allocation & insider signal

### 資本配置
- 股利: 每季 $0.65 (年化 $2.60, 殖利率 0.79%)。TTM 股利支出 $12.08B, FCF / 股利 = **3.26x**, 股利安全邊際充足。TTM payout ratio (以 GAAP NI 計) 31.6%。
- 買回: FY24 $12.39B → FY25 $6.31B (−49%)。TTM 買回 $8.45B, 其中 Q1 FY26 單季 $7.85B, Q3 FY26 為 0。
- 股東報酬: FY25 股利 + 買回合計 $17.45B, 占 FCF 64.8%, 其餘用於去槓桿與現金累積。
- 稀釋: 流通股數 Q3 FY25 4,722M → Q3 FY26 4,774M, 年增 +1.1%, 買回尚未抵銷 SBC 稀釋。
- 投資活動: FY24 投資現金流 −$23.07B (工具未拆分項目, 疑與大型收購相關), FY25 投資現金流 −$0.58B, 大型併購現金支出於 FY25 已明顯趨緩。

### 內部人交易 (近六個月, 2026-04-19 至 2026-10-19)
資料狀況: 同一指令 (`pipeline/tools/yf AVGO insider`) 在本次執行中回傳兩組不一致資料:
- 快取 (`prices/yf/AVGO.json`, 最新交易 2026-07-10, 共 105 筆): 交易價格 $370–$400 區間, 與 `prices/AVGO.csv` 同期收盤價吻合, 可視為可靠來源。
- Live feed (102 筆, 最新交易 2026-08-21): 交易價格多在 $900–$1,190, 與同期 `prices/AVGO.csv` 收盤價 (約 $360–$500) 相差約 2.5 倍, 金額欄位不可靠。股數欄位可參考但未能獨立驗證。

| 來源 | 賣出股數 | 賣出金額 | 買入 | 備註 |
|---|---|---|---|---|
| 快取 (至 07-10) | 740,885 股 | 約 $283.7M (以 feed 金額, 與 repo 收盤估算一致) | 1 筆, 1,000 股 (Director Harry You, 06-11, 約 $0.37M) | 含 Samueli (Director) 間接持有 654,241 股, 約 $250M |
| Live (04-19 至 08-21) | 266,805 股 | 約 $105M (以 repo 收盤估算); feed 金額 $248M 不可靠 | 0 | CEO Sanjay Mehrotra 五筆共 200,000 股, 疑似固定批次 (非確認為 10b5-1 計畫) |

- 兩組賣出股數合計約 1.0M 股, 以 repo 收盤估算約 $390M, 占市值 $1,569B 約 0.025%, 絕對規模小。
- 但方向一致偏賣: 高階主管與董事有大量賣出, 公開市場買入僅 1,000 股 (快取) 與 2026-01-14 Director Liu 約 23,200 股 (live, 屬六個月窗口外)。
- 內部人持股 1.9%, 機構持股 79.7%, 前五大機構為 BlackRock 8.34%、Vanguard 6.48%、State Street 4.12%、FMR 3.02%、Vanguard PM 2.66%。6 月底 FMR 持股增加 16.3%。

## Valuation

| 指標 | 數值 | 計算基礎 |
|---|---|---|
| 股價 | $328.75 | 2026-10-16 收盤 (快取) |
| 市值 | $1,569.3B | info marketCap, 流通股 4,774M |
| EV | $1,604.8B | 市值 + 淨負債 $35.4B |
| Trailing P/E (GAAP) | 43.3x (info) / 42.0x (TTM 季度 EPS 加總 $7.83) | trailingEps 7.59 與季度加總有差異 |
| Forward P/E | 17.0x | forwardEps $19.39 (consensus, 口徑未標示, 疑為 non-GAAP) |
| EV/EBITDA (TTM) | 30.7x (info) / 30.4x (normalized) | EBITDA $52.3B |
| P/FCF (TTM) | 39.8x | 季度 FCF 加總 $39.4B |
| P/FCF (info) | 51.3x | info freeCashflow $30.6B, 與季度加總差異大, 以季度為準 |
| P/S (TTM) | 17.6x | 營收 $89.1B |
| P/B | 15.7x | 每股帳面價值 $20.88 |
| PEG | 0.33 | info 欄位 |

- 與半導體板塊中位數比較 (以下為估計值, 非工具輸出): Trailing P/E 約 35x、Forward P/E 約 25x、EV/EBITDA 約 25x、P/FCF 約 30x、P/S 約 9x。
- 結論: 以 trailing 指標衡量, AVGO 明顯高於板塊中位數; 以 forward P/E 衡量則略低於估計板塊中位數, 但估值依賴 consensus EPS 能否兌現。
- 分析師: 47 位 (info) / 50 位 (rec_summary 0m 合計), 7 Strong Buy、40 Buy、3 Hold、0 Sell。平均目標價 $527.59, 相對現價 +60.5%。推薦均值 1.26 (新聞快取)。
- 價格位置: 較 MA20 $355.39 低 7.5%, 較 MA50 $365.73 低 10.1%, 較 MA200 $368.19 低 10.7%; 12 個月報酬 −6.4%, 3 個月 −13.1% (ta 工具)。

## Key catalysts
- **Q3 FY26 財報 (2026-09-02, 已公布)**: 工具回傳 Reported EPS 為 null, 無法驗證 beat/miss。Consensus EPS 估計 $3.24 為 non-GAAP 口徑, 季度 GAAP diluted EPS 為 $2.68, 兩者不可直接比較。次要來源報導標題為「Missed Expectations, Sees Revenue Below Estimates」, 未經 8-K 核實, 需獨立確認。
- **Q4 FY26 財報 (工具: 2026-12-09, 非確認)**: EPS 估計 $3.83。第三方日曆分歧為 12/2、12/9 或 12/10, 尚未官方確認, 超出本報告分析基準日。
- **大型雲端業者財報 (2026-10 下旬, 未確認日期)**: AI 資本支出指引直接影響 AVGO 的 FY27 需求能見度, 屬高影響事件。
- **管理層言論**: 次要來源提及 Hock Tan (2026-10-12) 認為資本取得與融資成本可能成為 AI 基礎建設的主要限制, 此為近期股價走弱的主要敘事之一。
- **NVDA 財報 (約 2026-11-18, 次要來源估計)**: AI 晶片需求的同業指標。
- **股價技術位置**: 收盤已跌破 $335.81 (2026-09-16 local low), 下方結構支撐為 $328.58 (10/16 盤中低點) 與 52 週低點 $289.96 (ta 工具輸出)。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價 (2026-10-16 收盤) | $328.75 | 12 個月 −6.4% (ta) | n/a | 偏弱, 低於 MA50 與 MA200 |
| 市值 / EV | $1,569B / $1,605B | n/a | n/a | 超大型股 |
| 營收 TTM | $89.1B | Q3 FY26 +85.5% | 約 +10–15% | 顯著優於板塊 |
| 營收 3 年 CAGR (FY22–25) | 24.4% | n/a | 約 10% | 優 |
| Gross margin TTM (GAAP) | 68.8% | Q3 69.1% vs 67.1% | 約 55% | 優 |
| Operating margin TTM (GAAP) | 48.5% | Q3 54.3% vs 38.1% | 約 25% | 優 |
| Net margin TTM (GAAP) | 42.9% | Q3 44.2% vs 26.0% | 約 15% | 優 |
| ROE (TTM 估算) | 40.8% | n/a | 約 18% | 優 |
| ROIC (估算) | 約 20% | n/a | 約 12% | 優 |
| FCF TTM | $39.4B | FY25 +38.6% (26.9 vs 19.4) | n/a | 強 |
| FCF margin TTM | 44.2% | FY25 42.1% | 約 15% | 優 |
| FCF / NI TTM | 1.03 | FY25 1.16 | >0.9 健康 | 合格 |
| 淨負債 (Q3 FY26) | $35.4B | vs Q3 FY25 −33.7% | n/a | 改善中 |
| 淨負債 / EBITDA TTM | 0.68x | n/a | 約 1.0x | 健康 |
| Current ratio | 2.50 | n/a | 約 2.0x | 健康 |
| Debt / Equity | 59.6% | n/a | 約 40–50% | 中等偏高 |
| 現金 | $24.0B | vs Q3 FY25 +123.7% | n/a | 充裕 |
| Capex TTM / 營收 | $1.25B / 1.4% | Q3 capex vs Q3 FY25 +275% | 約 3–5% | 輕資產, 需留意上升 |
| 股利殖利率 | 0.79% | n/a | 約 1.0% | 中性 |
| FCF / 股利 TTM | 3.26x | n/a | 約 2–3x | 健康 |
| 買回 TTM | $8.45B | FY25 買回 −49% vs FY24 | n/a | 力度下降 |
| 流通股數 | 4,774M | +1.1% | n/a | 輕度稀釋 |
| SBC FY25 / 營收 | 11.8% | n/a | 約 5–8% | 偏高 |
| 內部人淨賣出 (6 個月) | 約 1.0M 股 (約 $390M, 估計) | n/a | n/a | 偏空 (規模占市值極小) |
| 內部人持股 / 機構持股 | 1.9% / 79.7% | n/a | n/a | 機構集中 |
| Trailing P/E (GAAP) | 43.3x (42.0x TTM 加總) | n/a | 約 35x | 偏貴 |
| Forward P/E | 17.0x | n/a | 約 25x | 合理 (依 consensus) |
| EV/EBITDA TTM | 30.7x | n/a | 約 25x | 偏貴 |
| P/FCF TTM | 39.8x | n/a | 約 30x | 偏貴 |
| P/S TTM | 17.6x | n/a | 約 9x | 偏貴 |
| 分析師平均目標價 | $527.59 (+60.5%) | n/a | n/a | 共識偏多 (7 SB / 40 B / 3 H / 0 S) |

## Red flags
- 內部人淨賣出: 快取資料顯示 Samueli (Director) 間接持股賣出 654,241 股 (約 $250M); live feed 顯示 CEO 五筆共 200,000 股。買入僅見 1,000 股, 信號偏空, 但絕對規模占市值約 0.025%。
- 資料完整性: 內部人交易資料兩組來源不一致, live feed 價格與 repo 價格序列相差約 2.5 倍; Q3 FY26 Reported EPS 為 null; info trailingEps 與季度加總不同; info freeCashflow 與季度加總相差約 $8.8B。以上數字在決策前需以 SEC 8-K/10-Q 與 Form 4 核對。
- 估值: GAAP trailing P/E 43x、EV/EBITDA 30.7x、P/FCF 約 40x、P/S 17.6x, 對市場情緒與 AI 需求敘事高度敏感。
- 趨勢與價格: 股價低於 MA20 / MA50 / MA200, MA50 已位於 MA200 之下 (death cross 狀態, 交叉日未由工具確認), 距 52 週高點 −33.6%。
- AI 融資與客戶集中: 次要來源提及管理層對資本取得與融資成本的警示, 以及客戶集中風險, 屬非財報型風險。
- 收購型資產負債表: Goodwill + 無形資產占總資產 76%, 有形權益為 −$48.8B (FY25), 若 AI 業務成長不及預期, 存在減損風險。
- SBC 與稀釋: SBC 占營收 11.8%, FCF 扣除 SBC 後約為 78%, 流通股仍逐年增加。
- 獲利波動: FY24 GAAP 淨利率僅 11.4%, 說明 GAAP 獲利受收購整合與攤銷影響大, 單季數字需對照口徑。
- 買回力度下降: FY25 買回金額較 FY24 減少 49%, Q3 FY26 買回為 0。

FUNDAMENTALS REPORT COMPLETE
