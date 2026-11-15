# Fundamentals — AVGO as of 2026-11-16

資料來源：pipeline/tools/yf（yfinance 路由）。身分交叉驗證：公司為 Broadcom Inc.（Palo Alto, CA，Semiconductors / Technology），info、財報與股本數字彼此一致，未觸發 repo cache 比對。單位：營收、淨利、現金流、市值一律 USD B（本報告不使用億）。FY 年底為 10 月底 / 11 月初（FY25 結束於 2025-10-31）。最新已入帳季度為 FY26 Q3（截至 2026-07-31）。

資料時效注意：系統當前日期為 2026-11-15，分析基準日為 2026-11-16，因此價格快照與 feed 內容可能與 11-16 收盤不一致，需由下游確認。內部人交易 feed 最後一筆為 2026-07-10，2026-07-11 至 11-16 區間無資料。

## Executive summary
AVGO 財務體質強勁：最新 TTM 營收 USD 89.1B（最新季 YoY +85.5%）、TTM FCF 利潤率約 44%、淨負債/EBITDA 約 0.68x、流動比率 2.50。估值方面，以 GAAP TTM EPS 7.83 計 P/E 約 44.3x、EV/EBITDA 約 32.3x、P/FCF 約 42x，明顯高於估計的半導體板塊中位數；yfinance 提供的 forward P/E 17.9x 來源與季度共識不一致，僅供參考，不宜單獨作為估值依據。6 個月內內部人淨賣出約 USD 284M，佔市值不到 0.02%，屬減持訊號而非結構性風險。

## Revenue & profitability
**營收趨勢（USD B，來源 financials / quarterly_fin）**

| 期間 | 營收 | YoY | 淨利（普通股） | 稀釋 EPS (GAAP) |
|---|---|---|---|---|
| FY22 | 33.20 | — | 11.22 | 2.65 |
| FY23 | 35.82 | +7.9% | 14.08 | 3.30 |
| FY24 | 51.57 | +44.0% | 5.90 | 1.23 |
| FY25 | 63.89 | +23.9% | 23.13 | 4.77 |

- 3 年 CAGR（FY22→FY25）：約 **24.4%**。FY24 YoY +44% 含 VMware 併購整合全年效應，FY25 YoY +23.9%。
- 季度動能：FY25 Q3 15.95 → FY25 Q4 18.02 → FY26 Q1 19.31 → FY26 Q2 22.19 → FY26 Q3 29.59（USD B）。FY26 Q3 QoQ +33.3%，YoY +85.5%（yfinance info revenueGrowth 0.855 與此一致）。
- 分部營收：info 僅描述 Semiconductor Solutions 與 Infrastructure Software 兩大分部，並提及 AI networking 相關產品，但 feed 未提供分部營收拆分。**分部 mix：DATA_UNAVAILABLE**。

**獲利能力（TTM = FY25 Q4 至 FY26 Q3 四季加總）**

- 毛利率：FY25 67.8%；TTM 68.8%（由季度 gross profit 計算；季度毛利率由 68.0% 升至 69.2%）。注意 info grossMargins 為 75.5%，與季度加總不一致，本報告採季度計算值。
- 營業利益率：FY25 39.9%（reported operating income USD 25.5B）；TTM 48.1%（營業利益 USD 42.8B）；FY26 Q3 單季 53.9%。
- 淨利率：FY25 36.2%；TTM 42.9%（淨利 USD 38.3B，與 info profitMargins 0.429 一致）。
- ROE：FY25 NI / 平均權益 ≈ 31.0%；TTM NI / 平均權益（FY25 期末與 FY26 Q3 期末）≈ 42%，info returnOnEquity 為 44.2%。
- ROIC（估計）：FY25 EBIT USD 25.9B × (1 − 稅率 25.6%) ≈ NOPAT USD 19.3B，除以 invested capital USD 146.4B，約 **13.2%**。
- 稅率波動大：FY26 Q3 有效稅率 14.3%，FY26 Q2 8.1%，FY25 Q4 為負值（稅收利益）。GAAP 淨利易受稅務與無形資產攤銷影響。

## Cashflow & balance sheet
**現金流（USD B）**

| 期間 | 營運現金流 | 資本支出 | FCF | FCF/NI | FCF 利潤率 |
|---|---|---|---|---|---|
| FY24 | 19.96 | 0.55 | 19.41 | 3.29x（NI 5.90 受稅與整合費用壓低） | 37.6% |
| FY25 | 27.54 | 0.62 | 26.91 | 1.16x | 42.1% |
| TTM（FY26 Q3） | 40.65 | 1.25 | 39.41 | 1.03x | 44.2% |

- FCF/NI 在 FY25 與 TTM 皆高於 0.9 的健康門檻。FY24 偏低主要因 GAAP 淨利受壓，非現金流惡化。
- 資本支出極低（TTM 約 1.4% 營收），為 fabless 商業模式特徵；FY26 Q3 單季 capex 升至 USD 0.53B，為近幾季新高，需留意是否為新產能或 AI 相關投資。
- yfinance info freeCashflow 為 USD 30.6B，與季度 OCF 減 capex 之加總 USD 39.4B 不一致，本報告以季度加總為準。

**資產負債表（最新季 FY26 Q3，2026-07-31；USD B）**

| 項目 | 最新 | FY25 期末 | 變化 |
|---|---|---|---|
| 現金及約當現金 | 23.98 | 16.18 | +7.8 |
| 總負債（含流動） | 59.42 | 65.14 | −5.7 |
| 淨負債 | 35.44 | 48.96 | −13.5（−27.6%） |
| 股東權益 | 99.69 | 81.29 | +18.4 |
| 總資產 | 188.15 | 171.09 | +17.1 |
| 商譽 | 97.80 | 97.80 | 持平 |
| 有形淨值（tangible book） | n/a（季度未提供） | −48.78 | 持續負值 |

- 淨負債/EBITDA：0.68x（EBITDA TTM USD 52.3B）。
- 負債權益比（book）：59.6%。
- 流動比率：2.50（流動資產 USD 52.2B / 流動負債 USD 20.8B）。
- 利息保障倍數（FY25）：EBIT USD 25.9B / 利息費用 USD 3.2B ≈ 8.1x。
- 債務去化：總債務由 FY24 期末 USD 67.6B 降至 FY26 Q3 USD 59.4B。TTM 償還債務約 USD 14.2B。
- 有形淨值為負（約 −USD 48.8B），主要來自商譽與無形資產佔比高（FY26 Q3 商譽加無形資產約 USD 124.1B，佔總資產約 66%）。這是併購結構的正常結果，但意味著資產端的減損風險需持續追蹤。

## Capital allocation & insider signal
**資本配置（USD B）**

| 項目 | FY22 | FY23 | FY24 | FY25 | TTM |
|---|---|---|---|---|---|
| 股利支出 | 7.03 | 7.65 | 9.81 | 11.14 | 12.08 |
| 股票買回 | 8.46 | 7.69 | 12.39 | 6.31 | 0.85 |
| 債務償還 | 2.36 | 0.40 | 19.61 | 18.48 | 14.19 |

- 股利：年化 USD 2.60/股，殖利率 0.75%（5 年平均殖利率 1.23%）。股利覆蓋率：FY25 FCF / 股利 = 2.4x；TTM 為 3.3x。以 GAAP 淨利計的 payout：TTM 約 31.6%，FY25 約 48%。
- 買回：FY24 USD 12.4B → FY25 USD 6.3B → TTM 僅 USD 0.85B（FY26 Q1 USD 0.79B、FY26 Q2 USD 0.06B，Q3 為 0）。資金明顯轉向債務償還。
- 股本：普通股 FY25 期末 4.741B 股，FY26 Q3 期末 4.774B 股（+0.7%）。買回暫停後稀釋壓力回升，需留意。

**內部人交易（yfinance insider，最後一筆 2026-07-10）**

- 6 個月窗口（2026-05-16 至 2026-11-16）：feed 內可見的公開市場賣出約 **USD 283.7M**，買進 USD 0.37M（Harry You，2026-06-11，1,000 股 @ 373.57）。淨額約 **−USD 283M**。
- 賣出金額佔市值（USD 1,656.5B）約 **0.017%**，規模極小。其中 USD 250.0M 為 Henry Samueli（董事，間接持股）於 2026-06-24 單筆出售，佔窗口賣出逾 88%。
- 高階主管（Mark Brazeal、Kawwas 等）以 10b5-1 式的定期減持為主，2026-03-17 另有 Brazeal、Kawwas、Spears、Velaga 集中賣出約 USD 88M（窗口外，作為背景）。
- 公開市場買進極少：自 2024-12 以來僅 Harry You 有數筆小額買進（2025-09 USD 1.2M、2025-12 USD 0.3M、2026-06 USD 0.4M）。
- 機構持股 79.5%，內部人持股 2.1%（major_holders）。

## Valuation
**估值倍數（市值 USD 1,656.5B；股價 USD 347.01；EV USD 1,691.9B = 市值 + 總債務 59.4 − 現金 24.0）**

| 指標 | AVGO | 說明 |
|---|---|---|
| Trailing P/E（GAAP TTM EPS 7.83） | 44.3x | 與 info trailingPE 一致 |
| Trailing P/E（non-GAAP 近似） | 約 35.8x | 以 Q4 FY25 1.95 + Q1 FY26 2.05 + Q2 FY26 2.44 + Q3 FY26 共識 3.24 估算，非實際 non-GAAP |
| Forward P/E（yfinance） | 17.9x | 來源 forwardEps 19.41，與季度共識推算不符，**未驗證** |
| Forward P/E（run-rate） | 約 22.6x | 以 Q4 FY26 共識 non-GAAP EPS 3.84 × 4 = 15.36 估算 |
| EV/EBITDA（TTM） | 32.3x | info enterpriseToEbitda 32.4x，一致 |
| P/FCF（TTM） | 約 42.0x | 市值 / TTM FCF USD 39.4B |
| P/S（TTM） | 18.6x | 市值 / TTM 營收 USD 89.1B |
| PEG（yfinance） | 0.34 | 依 yfinance trailingPegRatio，使用 earningsGrowth 215%，參考價值有限 |

**與板塊比較（估計值，非工具輸出）**：大型半導體板塊中位數估計 trailing P/E 約 30–35x、forward P/E 約 22–26x、EV/EBITDA 約 20–25x、P/FCF 約 30–40x、P/S 約 10–13x。AVGO 在 trailing 倍數上高於板塊，在 forward 與 non-GAAP 基礎上接近板塊或略高，估值是否合理取決於 AI 相關營收的持續性。

**分析師觀點**：47 位分析師，recommendationKey = strong_buy，目標價均值 USD 529.24（較現價 +52.5%）。目標價為 yfinance 彙整數字，非本報告推薦。

**股價位置**：現價 USD 347.01，當日 −6.58%（前收 USD 364.36）。52 週區間 USD 289.77–495.00，現價距高點 −29.9%、距低點 +19.7%。50 日 / 200 日均線：DATA_UNAVAILABLE（fast_info 回傳 null）。

## Key catalysts
- **下次財報**：2026-12-09（盤後，yfinance 日期；屬於 FY26 Q4）。共識 EPS 3.84（non-GAAP 基礎推估）。
- **前一次財報**：FY26 Q3 於 2026-09-02 盤後發布（yfinance 日期）。共識 EPS 3.24，但 earnings_dates 的 Reported EPS 欄位為 null，**實際 non-GAAP EPS 與超預期幅度 DATA_UNAVAILABLE**。季度 GAAP 稀釋 EPS 為 USD 2.68（quarterly_fin），與共識基礎不同，不應直接比較。
- **近四季超預期紀錄**（non-GAAP vs 共識）：FY25 Q4 +4.4%、FY26 Q1 +1.3%、FY26 Q2 +1.7%；更早年度多數季度亦為小幅超預期（約 +0.5% 至 +6%）。
- **股利**：exDividendDate 2026-09-21、支付日約 2026-09-30（均已過）。下一次股利宣告通常隨財報發布，預期於 2026-12-09 前後，**具體日期 DATA_UNAVAILABLE**。
- **營收指引與管理層展望**：feed 未提供，**DATA_UNAVAILABLE**。
- **分部轉變**：feed 無分部拆分，**DATA_UNAVAILABLE**。主管團隊：info 列出 CFO 為 Amie Thuener O'Toole；內部人交易紀錄顯示前任 CFO Kirsten Spears 於 2026-03 仍有減持，屬管理層交接訊號，需與公告核對。

## Metrics table
數字單位：營收、淨利、現金流、市值、EBITDA 為 USD B；比率為 %、倍數為 x。板塊中位數為估計值。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（USD B） | 89.1 | +85.5%（最新季） | 約 +10–15% | 遠高於板塊，成長加速明顯 |
| 營收 FY25（USD B） | 63.9 | +23.9% | — | 強 |
| 毛利率 TTM（季度計算） | 68.8% | FY25 67.8% | 約 55–60% | 高於板塊 |
| 營業利益率 TTM | 48.1% | FY25 39.9% | 約 25–30% | 高於板塊 |
| 淨利率 TTM | 42.9% | FY25 36.2% | 約 20–25% | 高於板塊 |
| FCF 利潤率 TTM | 44.2% | FY25 42.1% | 約 25% | 高於板塊 |
| FCF / NI（TTM） | 1.03x | FY25 1.16x | 約 0.8–1.0x | 健康（>0.9） |
| ROE（TTM，平均權益） | 約 42% | FY25 約 31% | 約 15–20% | 高於板塊 |
| ROIC（FY25 估計） | 13.2% | — | 約 10–12% | 略高於板塊 |
| 淨負債（FY26 Q3，USD B） | 35.4 | FY25 49.0（−27.6%） | — | 去化中 |
| 淨負債 / EBITDA | 0.68x | FY25 約 1.4x | 約 1.0–1.5x | 健康 |
| 負債權益比（book） | 59.6% | FY25 80.1% | 約 40–60% | 中性偏高（商譽與併購造成） |
| 流動比率 | 2.50x | FY25 1.71x | 約 1.5–2.0x | 健康 |
| 有形淨值（USD B） | DATA_UNAVAILABLE（FY25 −48.8） | — | — | 負值，需留意 |
| 股利殖利率 | 0.75% | — | 約 1.0–1.5% | 偏低，但覆蓋率高（FCF 3.3x） |
| 股票買回（TTM，USD B） | 0.85 | FY24 12.39 → TTM −93% | — | 明顯收縮，轉向去槓桿 |
| Trailing P/E（GAAP） | 44.3x | — | 約 30–35x | 偏貴 |
| Trailing P/E（non-GAAP 近似） | 約 35.8x | — | 約 30–35x | 略偏貴 |
| Forward P/E（yfinance，未驗證） | 17.9x | — | 約 22–26x | 表面偏便宜，需驗證 |
| Forward P/E（run-rate） | 約 22.6x | — | 約 22–26x | 接近板塊 |
| EV/EBITDA（TTM） | 32.3x | — | 約 20–25x | 偏貴 |
| P/FCF（TTM） | 約 42.0x | — | 約 30–40x | 偏貴 |
| P/S（TTM） | 18.6x | — | 約 10–13x | 偏貴 |
| 內部人淨交易（6 個月，USD M） | −283.7（買進 0.37） | — | — | 規模小，減持為主 |
| 分析師目標價均值 | USD 529.24（+52.5%） | — | — | 偏樂觀，共識強烈買進 |

## Red flags
- **資料一致性**：yfinance info 的 grossMargins（75.5%）、freeCashflow（USD 30.6B）、forwardEps（19.41，隱含遠高於季度共識的 forward 獲利）、payoutRatio（0.324）與季度財報加總不一致，本報告以季度計算為準，下游應避免直接引用 info 欄位。
- **EPS 基礎不一致**：earnings_dates 的共識與實際多為 non-GAAP，quarterly_fin 為 GAAP。Trailing P/E 44.3x 以 GAAP 計，會高估與共識比較的倍數；反之 forward P/E 17.9x 來源不明。
- **Q3 FY26 實際超預期結果缺失**：2026-09-02 盤後的 Reported EPS 為 null，無法判斷最新一季是 beat 或 miss。
- **估值偏高**：EV/EBITDA 32x、P/FCF 42x，在 AI 營收動能放緩時倍數壓縮風險較大。近期單日 −6.6% 顯示市場對高估值敏感。
- **營收成長可持續性**：最新季 YoY +85.5%、QoQ +33.3%，為極高成長，但 feed 缺乏指引與分部，無法判斷是否為一次性拉貨或結構性成長。
- **買回收縮與稀釋**：TTM 買回僅 USD 0.85B，普通股由 FY25 4.741B 增至 FY26 Q3 4.774B。
- **有形淨值為負**：約 −USD 48.8B（FY25），商譽加無形資產佔總資產約 66%，減損風險需追蹤。
- **內部人持續減持**：6 個月淨賣出約 USD 284M（規模小），但 2026-03 與 2026-06 有多名高管與董事集中出售，屬行為上的警示。feed 最後日期為 2026-07-10，之後的內部人交易無法確認。
- **稅率波動**：FY26 Q3 有效稅率 14.3%、Q2 8.1%、FY25 Q4 為負值，GAAP 獲利品質需以非 GAAP 或現金流交叉確認。
- **資料時效與抓取穩定度**：yfinance 多次因 Yahoo cookie/crumb 失敗與 proxy 403 而降級，fast_info 之 market_cap、50/200 日均線為 null，price snapshot 日期需與 2026-11-16 核對。

**DATA_UNAVAILABLE 清單**：分部營收拆分、營收與獲利指引、FY26 Q3 實際 non-GAAP EPS、2026-07-11 至 2026-11-16 內部人交易、50 日與 200 日均線、有形淨值（季度）、下一次股利宣告日期、板塊中位數（僅為估計，非工具資料）。

FUNDAMENTALS REPORT COMPLETE
