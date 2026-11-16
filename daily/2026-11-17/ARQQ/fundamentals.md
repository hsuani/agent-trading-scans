# Fundamentals — ARQQ (Arqit Quantum Inc.) as of 2026-11-17

資料基準: yfinance 快取快照 2026-11-16 (盤中/收盤附近, info.regularMarketTime 與 fast_info cached_at 2026-11-16 15:31–15:34 UTC)。財報為 FY2025 年報 (財年截止 2025-09-30) 與 FY2026 Q2 季報 (2026-03-31)。幣別 USD, 本報告統一以 USD M (百萬美元) 表示。非 TWD/KRW, 不涉及億換算。

## Executive summary
ARQQ 仍處於營收極小、持續燒錢的階段: FY2025 營收僅 USD 0.53M, 營業虧損 USD 35.2M, 營業現金流 USD -29.6M, 基本面依賴股權增發維持營運。資產負債表目前尚有淨現金 (2026-03-31 現金 USD 28.86M 大於總負債 USD 2.17M), 但以 FY2025 平均季度燒錢速度估算僅約 4 季跑道, 後續增資或稀釋風險高。估值面以盈餘或現金流計算均為負值, P/S 約 211x (TTM), 不存在可比的盈餘估值基礎, 估值吸引力在基本面上難以成立; 此為基本面評估, 非交易建議。

## Revenue & profitability

**營收趨勢 (USD M, 財年 9 月結)**
| 財年 | 營收 | 營業損益 | 淨利 (普通股) | 稀釋 EPS |
|---|---|---|---|---|
| FY2022 | 7.21 | -50.23 | +65.08 (含非經常項目) | 13.34 |
| FY2023 | 0.64 | -67.46 | -74.53 | -14.17 |
| FY2024 | 0.29 | -37.37 | -56.82 | -11.23 |
| FY2025 | 0.53 | -35.17 | -35.34 | -2.56 |

- 3 年 CAGR (FY2022→FY2025): 約 -58.1%。FY2022 營收來自前期業務, 之後營收已大幅萎縮, 不具有可持續的成長敘事基礎。
- FY2025 相對 FY2024 營收 +81% (0.29→0.53), 但基數極低。
- TTM 營收 (info.totalRevenue) USD 1.086M。yfinance 之 revenueGrowth 為 829.9% (即 +8.299 倍), 此數字基於極小基數, 不具代表性。
- 業務分部: info.longBusinessSummary 僅描述 QuantumCloud (PaaS 加密金鑰服務) 與維護支援、專業服務, 未提供分部營收拆分, 標記為 n/a。
- 員工數 87 人 (info.fullTimeEmployees)。

**獲利能力**
- 毛利率: info.grossMargins 49.7% (TTM 毛利 USD 0.54M)。毛利率看似正常, 但毛利絕對額極低, 無法覆蓋營運費用。
- FY2025 營業利益率: 約 -6,636% (營業損益 -35.17 / 營收 0.53); info.operatingMargins TTM 為 -4,617%。SG&A FY2025 USD 34.94M 幾乎是全部營運支出, 且 FY2025 總費用 USD 35.70M。
- FY2025 淨利率: 約 -6,668%。
- ROE: info.returnOnEquity -220.2%; ROA: -95.5%。
- ROIC (近似): FY2025 營業利益 / 期末投入資本 (USD 27.24M) ≈ -129%。
- 稅: FY2025 稅前虧損 USD -37.62M, 稅費 USD -2.19M (稅費為收益項, 不影響結論)。
- 非經常性項目: FY2025 Total Unusual Items USD -3.88M。

## Cashflow & balance sheet

**現金流 (USD M)**
| 項目 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| 營業現金流 | -26.72 | -32.83 | -34.13 | -29.55 |
| 資本支出 | -24.43 | -16.12 | -3.33 | -0.55 |
| 自由現金流 (FCF) | -51.15 | -48.95 | -37.45 | -30.10 |
| 股權發行收入 | 0.00 | 45.08 | 13.08 | 37.18 |

- FCF margin FY2025: 約 -5,680%。FCF/NI 比率: FY2025 FCF -30.10 / NI -35.34 ≈ 0.85, 但兩者皆為負值, 比率不具健康度意義, 判定為不適用 (n/a)。
- TTM FCF (info.freeCashflow) USD -19.70M, TTM 營業現金流 USD -42.75M。TTM 與 FY2025 數字差異大, 季報現金流 (quarterly_cf) 回傳為空, 無法逐季核對, 列為資料缺口。
- 資本支出由 FY2023 USD 16.1M 降至 FY2025 USD 0.55M, 屬大幅收縮, 但同時營運現金流仍為負。

**資產負債表 (USD M)**
| 項目 | 2025-09-30 (FY25 年末) | 2026-03-31 (Q2 FY26) |
|---|---|---|
| 現金及約當現金 | 36.98 | 28.86 |
| 總負債 | 15.62 | 7.73 |
| 總債務 (含租賃負債) | 0.72 | 2.17 |
| 股東權益 | 27.24 | 28.51 |
| 有形帳面價值 | 25.12 | 26.46 |
| 營運資金 | 25.12 | 25.57 |
| 總資產 | 42.85 | 36.24 |

- 淨現金 (現金 - 總債務) 2026-03-31: 約 USD +26.69M。
- 流動比率 info.currentRatio 4.88; 速動比率 info.quickRatio 4.61。
- 負債/股東權益: info.debtToEquity 7.62 (即 7.6%, yfinance 以百分比表示), 槓桿極低。
- 現金變化: 2025-09-30 → 2026-03-31 半年內現金減少 USD 8.12M; 同期 APIC 由 USD 206.5M 增至 USD 238.0M (約 +31.5M, 含股權發行與股票報酬), 顯示半年期間仍靠增發補充。
- 平均季度燒現金速度 (以 FY2025 營業現金流 / 4 估算): 約 USD 7.4M/季, 現金 USD 28.86M 可支撐約 3.9 季 (約 1 年) 的同等燒速, 此為推算值, 非公司揭露之跑道。
- 不確定項: 2026 年 H1 的現金流量表缺漏, 無法確認實際燒速。

## Capital allocation & insider signal

**資本配置**
- 股利: 無 (Cash Dividends Paid 歷年為 0, payoutRatio 0)。
- 買回: 無公開買回紀錄。
- 融資: 以股權融資為主。FY2023 發行股票 USD 45.08M, FY2024 USD 13.08M, FY2025 USD 37.18M。FY2025 另有認股權證/選擇權行使 USD 10.0M。
- 稀釋: 流通股數由 FY2024 年末 11.55M 增至 FY2025 年末 15.29M, 2026-03-31 為 16.58M, 目前 info.sharesOutstanding 17.40M。期間約增加 51% (2024 年末 → 目前)。
- 股票分割: 2024-09-25 發生 1:25 反向分割 (lastSplitFactor 1:25)。
- 高度依賴外部融資, 這是本公司基本面最重要的風險因子之一。

**內部人交易 (近 6 個月, 2026-05-16 至 2026-11-16, 資料來源 yfinance insider)**
- 公開市場賣出 (Form 4 "Sale at price"): 合計約 USD 2.68M。其中:
  - 董事 Lefebvre D'Ovidio Manfredi 2026-07-01 賣出 54,444 股 (@ 30.07–30.24), 金額 USD 1.64M, 為最大單筆。
  - CEO Andrew Leaver 合計約 USD 0.48M (2026-07-02 USD 0.25M; 2026-10-02 至 10-13 多筆合計約 USD 0.23M)。
  - 其餘為其他高階主管與董事 (Willcocks, Feenan, Wilder, Nilan, Ritchie, Bers) 的小額賣出。
- 行權 / 轉換 (Conversion of derivative security @ 2.50): 董事 Lefebvre D'Ovidio 2026-09-22 4.60M 股 (value 約 USD 11.5M, 行權價 2.50); 另 Ritchie 73,562 股、Calabria 120,000 股。性質為行權, 非市場買入或賣出。
- 大量小額 Form 4 (無價格標註, 股數頻繁) 多為歸屬或稅務扣繳類交易, 性質不明, yfinance 未提供交易代碼。
- 買入紀錄: 近 6 個月無公開市場買入 (open market buy) 紀錄。
- 規模: 賣出金額 USD 2.68M / 市值 USD 229.7M ≈ 1.2%。絕對金額不大, 但全部為賣出 (無買入), 且 2026-10 高價 (~24 USD) 後跌至 13.20, 方向上為內部人減持訊號, 需注意 Form 4 中大量 "無價格" 項目的解讀不確定性。
- 2026-04 另有 CEO 賣出 (USD 0.10M @ 13.51) 與 CFO Nicholas Pointon 小額賣出 (USD 0.02M @ 15.87); info.companyOfficers 列出的現任 CFO 為 Rob Russell, 人事異動未在本報告核實。

**股東結構**
- 機構持股 80.6% (institutions 97 家), 內部人持股 4.3% (heldPercentInsiders 0.04319)。
- 做空: shortRatio 7.68 天, shortPercentOfFloat 16.65%, sharesShort 2.12M (前月 2.26M, 略降)。流通股 floatShares 5.85M 與 shortPercentOfFloat 的數字彼此不完全一致, 流通股口徑存疑。

## Valuation

**價格資訊 (USD)**
- info.regularMarketPrice 13.20 (日內 -10.57%, 前收 14.76); fast_info.last_price 13.49 (cache, cnyes feed)。兩者差 0.29, 以 info 13.20 為主要參考, 並標註差異。
- 52 週高/低: 31.75 / 11.52 (52 週變動 -43.1%)。
- 50 日均線 18.70, 200 日均線 17.70, 現價低於兩條均線。
- Beta 3.011 (極高波動)。
- 市值 info.marketCap USD 229.7M (13.20 × 17.40M 股, 核對一致); 非稀釋市值 USD 257.0M。
- EV info.enterpriseValue USD 218.0M。以市值 - 現金 + 債務 估算約 USD 203.0M, 與 yfinance EV 有 USD 15M 差距, 差異來源未揭露, 以 yfinance 為準並標註。

**估值倍數**
- 追蹤本益比 (trailing P/E): n/a (TTM EPS -3.21, 不適用)。
- 預期本益比 (forward P/E): info.forwardPE -12.45 (forward EPS -1.06), 負值, 不具比較意義。
- EV/EBITDA: info.enterpriseToEbitda -4.37 (EBITDA USD -49.9M), 負值, n/a。
- EV/Revenue: 200.8x (TTM)。
- P/S: 211.5x (TTM, 市值 / TTM 營收 USD 1.086M)。
- P/FCF: TTM FCF 為負, n/a。
- P/B: 7.68x (bookValue 1.719/股)。
- 與產業比較: 軟體-基礎設施 (Software - Infrastructure) 中位數估計 P/S 約 5–10x, 企業 EV/EBITDA 估計約 20x 以上 (估計值, 非來源資料); ARQQ 的 P/S 約為該區間的 20 倍以上。

**分析師評級**
- recommendationKey "none", 未見分析師目標價或評級資料 (info 相關欄位 n/a)。

## Key catalysts
- 下次財報: 2026-12-09 (yfinance earnings_dates, isEarningsDateEstimate=true, EPS estimate 為 n/a)。此日期為估計值, 屬於本報告 as-of 日期之後的未來事件。
- 最近一次財報: 約 2026-05-21 (earningsCallTimestamp), 季報 Q2 FY26 (2026-03-31) 已揭露, 其 EPS 與 surprise 資料 n/a。
- 業績指引 (guidance): n/a。yfinance 未提供管理層指引; info.forwardEps -1.06 為數據源估計值。
- 融資 / 稀釋事件: 2026-09-22 董事行權 4.6M 股 (行權價 2.50) 與近期股權增加, 顯示潛在稀釋持續。若公司再次增資, 需留意條款與折價幅度。
- 公司名稱異動: info.nameChangeDate 2026-11-16 (前身 Centricus Acquisition Corp., SPAC 背景), 其名稱與業務變動對後續揭露的影響尚未確認。
- 股價事件: 2026-11-16 單日跌幅 -10.57%, 原因未由 yfinance 揭露; 需由新聞與公告補充, 本報告不推測。

## Metrics table
單位: 營收/損益/現金/市值 為 USD M; 倍數與比率為 x 或 %。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025, USD M) | 0.53 | +81% (vs FY24 0.29) | 數十億級別 (非可比) | 極弱: 規模過小 |
| 營收 3Y CAGR (FY22→FY25) | -58.1% | n/a | 約 +5%–10% | 弱 |
| TTM 營收 (USD M) | 1.09 | n/a | n/a | 弱 |
| 毛利率 (TTM) | 49.7% | n/a | 約 60%–75% (軟體) | 中性偏弱 |
| 營業利益率 (FY2025) | -6,636% | n/a | 約 10%–25% | 極弱 |
| 淨利率 (FY2025) | -6,668% | n/a | 約 5%–15% | 極弱 |
| ROE (TTM) | -220.2% | n/a | 約 10%–20% | 極弱 |
| ROIC (FY25 近似) | -129% | n/a | 約 10%–15% | 極弱 |
| FCF margin (FY2025) | -5,680% | 改善 (FY24 -12,784%) | 約 15%–25% | 極弱 |
| FCF / NI | n/a (兩者皆負) | n/a | 約 0.9+ 為健康 | 不適用 |
| 現金 (2026-03-31, USD M) | 28.86 | -22% vs 2025-09-30 (36.98) | n/a | 中性偏弱: 燒錢中 |
| 總債務 (2026-03-31, USD M) | 2.17 | +202% vs 2025-09-30 (0.72) | n/a | 中性 |
| 淨現金 (USD M) | +26.69 | n/a | n/a | 中性 |
| 流動比率 | 4.88 | n/a | 約 1.5–2.5 | 強 (但短期有效性受燒錢速度影響) |
| 負債/股東權益 | 7.6% | n/a | 約 30%–60% | 強 |
| 股數 (目前, M) | 17.40 | +51% vs FY24 年末 (11.55) | n/a | 弱: 稀釋明顯 |
| 股權融資 (FY2025, USD M) | 37.18 | 較 FY24 (13.08) 增加 | n/a | 依賴外部融資 |
| 股利 / 買回 | 無 | n/a | n/a | n/a |
| 內部人賣出 (近 6 月, USD M) | 2.68 | n/a | n/a | 偏負面 (金額占市值約 1.2%) |
| 內部人買入 (近 6 月) | 0 | n/a | n/a | 偏負面 |
| 機構持股 | 80.6% | n/a | 約 60%–80% | 中性 |
| 做空比例 (float) | 16.65% | 前月 sharesShort 2.26M → 2.12M | 約 3%–8% | 偏高 |
| Beta | 3.01 | n/a | 約 1.0–1.3 | 極高波動 |
| 追蹤 P/E | n/a | n/a | 約 25x–35x | n/a (虧損) |
| 預期 P/E | -12.45 | n/a | 約 25x–30x | n/a (虧損) |
| EV/EBITDA | -4.37 | n/a | 約 20x | n/a (虧損) |
| P/S (TTM) | 211.5x | n/a | 約 5x–10x | 極貴 |
| P/FCF | n/a (FCF 為負) | n/a | 約 20x–30x | n/a |
| P/B | 7.68x | n/a | 約 3x–6x | 偏貴 |

## Red flags
- 營收規模極小 (FY2025 USD 0.53M), 且 FY2022→FY2025 3 年 CAGR 為 -58%, 商業化進展無法從財報驗證。
- 營業與淨虧損高度持續, FY2023–FY2025 每年營業虧損 USD 35M–67M, 與營收完全不成比例。
- FCF 連續 4 年為負 (FY2022–FY2025), 目前 TTM FCF USD -19.7M, 營業現金流 TTM USD -42.7M。
- 依賴股權融資: FY2023–FY2025 累計股權發行約 USD 95.3M; APIC 半年內增加約 USD 31.5M。流通股 2024 年末至今增加約 51%。
- 跑道偏短: 以 FY2025 平均燒速推算, 現金約 4 季, 可能需於 2027 年前再次融資 (估算, 非公司揭露)。
- 內部人近 6 個月淨賣出 USD 2.68M (公開市場賣出), 無買入紀錄; 包含董事大額賣出 USD 1.64M。
- 估值倍數全數不具意義 (P/E、EV/EBITDA、P/FCF 皆為負或 n/a), 唯一可比指標 P/S 211x 遠超產業中位數估計。
- 股價 52 週跌幅 -43.1%, 現價低於 50 日與 200 日均線, 單日 -10.57%; Beta 3.01, 波動性極高。
- 做空比例 16.65% (float), short ratio 7.68 天, 空方持倉集中。
- 資料缺口: quarterly_fin 與 quarterly_cf 回傳為空; 季度損益與季度現金流無法核實; fast_info 與 info 價格不一致 (13.49 vs 13.20); EV 無法由市值、現金、債務完全復原; 分部營收、管理層指引、分析師評級均為 n/a。
- 資料來源以 yfinance 快取為主, 部分 Yahoo cookie/crumb 取得失敗, 部分欄位可能非即時。
- 日期提醒: 本報告 as-of 2026-11-17, 但市場與內部人資料截止 2026-11-16 (價格) 與 2026-10-16 (內部人 Form 4 最新紀錄); 財報下次日期 2026-12-09 為未來估計。

FUNDAMENTALS REPORT COMPLETE
