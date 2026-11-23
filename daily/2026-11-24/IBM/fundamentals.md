# IBM 基本面分析 (fundamentals)

- **Ticker**: IBM (International Business Machines Corporation, NYSE)
- **分析日期**: 2026-11-24（資料截至 2026-11-23）
- **資料來源**: `pipeline/tools/yf.py` — info / financials / quarterly_fin / balance_sheet / quarterly_cf / earnings_dates / insider / major_holders。`source: cache`（cached_at 2026-11-23T17:58:28Z），屬正常情況。
- **股價基準**: 233.74 USD（當日 +4.14%），市值 ~2,209 億 USD，企業價值 (EV) ~2,689 億 USD

---

## 1. 結論摘要

- **基本面評等：中性偏正面 (Neutral-to-Positive)**。獲利品質與現金流穩健，估值不貴，但營收成長僅低個位數，且 2026 年併購後槓桿上升。
- **營收**：TTM revenue 698.7 億 USD；Q3 FY2026 營收 171.0 億 USD，YoY +4.7%。FY2022–FY2025 營收 CAGR 約 3.7%。
- **獲利能力**：毛利率 (gross margin) 三年持續擴張，FY2022 54.0% → FY2025 58.2%；TTM operating margin 18.3%。
- **現金流**：TTM operating cash flow 158.3 億 USD；TTM FCF 約 123.5 億（Yahoo info 口徑）至 140.2 億（季度加總口徑）。股利支出約 63.4 億，FCF 覆蓋約 2 倍。
- **槓桿**：2026 Q1 有約 104.6 億 USD 的企業併購現金流出（`Purchase of Business`），同期發行 74.4 億 USD 債券。淨負債由 FY2025 約 476.7 億升至目前約 560.8 億 USD，net debt / EBITDA 約 3.4x。
- **估值**：forward P/E 17.7x（FY2027E EPS 13.24）；trailing adjusted P/E 19.0x；EV/EBITDA 16.2x。股價 52 週跌幅 -26%，但 EPS 仍在成長。
- **內部人**：近期公開市場交易量小。2026-08-26 有一筆 25,000 股賣出（約 576 萬 USD，$230.32）；2026-02 兩位董事小額買進（合計約 11.3 萬 USD）。

---

## 2. 營收與成長

| 期間 | 營收 (USD) | YoY | 備註 |
|---|---|---|---|
| FY2022 | 605.3 億 | — | |
| FY2023 | 618.6 億 | +2.2% | |
| FY2024 | 627.5 億 | +1.4% | |
| FY2025 | 675.4 億 | +7.6% | 成長幅度高於 FY2022–2024，原因資料未拆分 |
| Q3 FY2025 | 163.3 億 | — | |
| Q4 FY2025 | 196.9 億 | — | 季節性最高季 |
| Q1 FY2026 | 159.2 億 | — | |
| Q2 FY2026 | 171.6 億 | — | |
| Q3 FY2026 | 171.0 億 | +4.7% | 與 info `revenueGrowth` 0.047 一致 |
| TTM | 698.7 億 | — | |

- **成長結構**：本次資料未提供 Software / Consulting / Infrastructure / Financing 的分部營收，無法量化 hybrid cloud 與 AI 各自貢獻。定性上，Software 為利潤核心，Consulting 偏人力與專案，Infrastructure 具週期性（大型主機換機循環）。
- **判讀**：營收成長穩定但偏低，約 4–5% 的 YoY 水準，代表 IBM 目前屬於「成熟獲利型」而非高成長型。

---

## 3. 獲利能力

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Gross margin | 54.0% | 55.4% | 56.7% | 58.2% | 58.0% |
| Operating margin | 13.5% | 15.2% | 16.0% | 18.5% | 18.3% |
| Net margin (GAAP) | 2.7% | 12.1% | 9.6% | 15.7% | 16.0% |
| R&D / 營收 | 10.9% | 11.0% | 11.9% | 12.3% | — |

- 毛利率與營業利益率皆呈持續擴張，顯示 mix 往軟體與高毛利服務移動，成效明確。
- **Q3 FY2026 單季**：毛利率 56.8%（Q3 FY2025 為 57.3%，略降 0.5pp），營業利益率 17.0%（持平）。GAAP 淨利 21.9 億 USD，YoY +26%，但主要來自稅率與其他項目，不是營業面改善。
- **Q4 FY2025 稅務利益**：當季 tax provision 為 -14.4 億 USD（利益），GAAP EPS 5.88，遠高於調整後 EPS 4.52。此項一次性因素使 GAAP trailing EPS (11.72) 被推高。若以約 25% 稅率重算 Q4 FY2025，TTM GAAP EPS 約為 9.1，trailing P/E 約 25.7x（估算值）。
- **ROE 34.8%** 數字偏高，原因是股東權益基數小（大量回購與 AOCI 負值）與 Q4 稅務利益，需謹慎解讀。

---

## 4. 現金流與股利

| 項目 | 數值 | 說明 |
|---|---|---|
| TTM Operating Cash Flow | 158.3 億 | 季度加總，與 info `operatingCashflow` 158.3 億一致 |
| TTM Capex (PPE + intangibles) | 約 18 億 | PPE 約 11.7 億、intangibles 約 6.3 億 |
| TTM FCF (info, `freeCashflow`) | 123.5 億 | FCF margin 17.7% |
| TTM FCF (季度加總) | 140.2 億 | FCF margin 20.1%；差異為計算口徑 |
| Q3 FY2026 OCF | 40.3 億 | YoY +31% (Q3 FY2025 為 30.8 億) |
| Q3 FY2026 FCF | 35.4 億 | YoY +33% |
| Q2 FY2026 FCF | 22.1 億 | 低點，主因營運資金 -13.5 億 |
| 股利 (dividendRate) | 6.76 USD/年 | 季配 1.69 USD |
| 股利殖利率 | ~2.9%（以 233.74 計） | Yahoo 顯示 3.01%，是以前一收盤 224.44 計算 |
| 股利支付率 (payout) | 57.5%（GAAP） / 約 55%（adjusted） | |
| FCF 股利覆蓋 | 約 1.9–2.2x | TTM 股利支付約 63.4 億 |
| 回購 (TTM) | 約 9.9 億 | 規模小，與稀釋大致抵銷 |
| 稀釋 | FY2025 加權股數 +1.2% YoY | 股本淨增，回購不足以抵銷員工股權 |
| 除息日 | 約 2026-11-10（已除息） | 依 Yahoo timestamp 換算，支付約 2026-12-10 |

- 股利穩定、覆蓋足夠，但殖利率已不算高。成長型資金配置偏向併購與債務償還，而非回購。
- 營運資金為負（working capital -17.1 億 FY2025，current ratio 0.86），主因是 current deferred revenue 達 161.0 億，屬於軟體與維運預收款，屬常見結構，不代表短期流動性風險。

---

## 5. 資產負債表與償債能力

| 項目 | 數值 | 說明 |
|---|---|---|
| Total debt (latest) | 671.4 億 | FY2025 為 646.1 億 |
| Cash & equivalents (latest) | 110.6 億 | `totalCash` |
| Net debt (latest) | 約 560.8 億 | FY2025 Yahoo 口徑為 476.7 億 |
| Net debt / EBITDA | 約 3.4x | 以 info `ebitda` 166.3 億計 |
| EBIT / Interest expense (FY2025) | 約 6.3x | EBIT 122.6 億，利息支出 19.4 億 |
| Debt / Equity | 185% | 依 info |
| Current ratio / Quick ratio | 0.86 / 0.68 | 負營運資金，見上節 |
| Goodwill + intangibles (FY2025) | 791.1 億 | 佔總資產約 52% |
| Tangible book value (FY2025) | -464.6 億 | 有形淨值為負，屬併購歷史累積結果 |
| Book value per share | 37.6 USD | P/B 6.2x |

- 2026 年負債增加的主因是 Q1 的併購（現金流出約 104.6 億）與約 74.4 億債券發行；Q2 償還約 42.1 億債務，Q3 再借 19.8 億。
- 利息保障倍數約 6.3x，對信用評等而言屬可接受，但整體槓桿已由 2025 年底的水準上升。
- 有形淨值為負屬於 IBM 長期資本結構特性，評估時應看 FCF 與 EBITDA 而非 book value。

---

## 6. 估值

| 指標 | 數值 | 口徑 |
|---|---|---|
| Trailing P/E (GAAP) | 19.9x | trailingEps 11.72 |
| Trailing adjusted P/E | 19.0x | 最近四季調整後 EPS 合計 12.31 |
| Trailing P/E (ex Q4 FY25 tax benefit，估算) | 約 25.7x | 見第 3 節 |
| Forward P/E (FY2027E) | 17.7x | forwardEps 13.24 |
| FY2026E P/E | 18.8x | epsCurrentYear 12.41 |
| EV / EBITDA (TTM) | 16.2x | EV 2,689 億 / EBITDA 166.3 億 |
| EV / Revenue | 3.85x | |
| Price / Sales | 3.16x | |
| Price / Book | 6.2x | |
| PEG | 2.11 | 成長性支撐度一般 |

- **分析性區間**：以 FY2027E EPS 13.24 乘以 16–20x，得到約 212–265 USD。目前股價 233.74 位於區間中下段。此為分析性推估，非目標價。
- **分析師共識**：23 位分析師，recommendationMean 2.28（偏買進）；目標價平均 259.85、中位數 265、高 300、低 174，相對現價約 +11%。
- **相對表現**：52 週 -26.2%，同期 S&P 500 +3.1%；股價距 200 日均線 (244.97) 約 -4.6%。

---

## 7. 盈餘品質與分析師預期

| 季度 | 預估 EPS | 實際 adjusted EPS | Surprise |
|---|---|---|---|
| Q3 FY2026 (2026-10-21) | 2.87 | 2.95 | +2.7% |
| Q2 FY2026 (2026-07-22) | 2.93 | 2.93 | -0.1% |
| Q1 FY2026 (2026-04-22) | 1.81 | 1.91 | +5.5% |
| Q4 FY2025 (2026-01-28) | 4.29 | 4.52 | +5.3% |
| Q3 FY2025 (2025-10-22) | 2.45 | 2.65 | +8.3% |
| Q2 FY2025 (2025-07-23) | 2.65 | 2.80 | +5.5% |
| Q1 FY2025 (2025-04-23) | 1.43 | 1.60 | +12.1% |
| Q4 FY2024 (2025-01-29) | 3.78 | 3.92 | +3.8% |

- 近八季 7 次 beat，平均 surprise 約 +5.4%，盈餘可預測性高。
- 下次財報日為 2027-01-27（資料標示為估計值，`isEarningsDateEstimate: true`）。FY2026Q4 EPS 預估 4.63。
- **留意 GAAP 與 adjusted 差異**：Q3 FY2026 GAAP diluted EPS 為 2.30，adjusted 為 2.95。分析時應分清楚口徑。

---

## 8. 內部人交易與股東結構

**內部人交易**（資料期間約 2026-01 至 2026-08）

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 / 價格 |
|---|---|---|---|---|---|
| 2026-08-26 | Robert D. Thomas | Senior VP, Software & CCO | 公開市場賣出 | 25,000 | 約 576 萬 USD @ $230.32 |
| 2026-07-01 | Anne E. Robinson | Senior VP & CLO | 性質未標註 | 7,295 | 無金額 |
| 2026-06-04 | Nicolas A. Fehring | Officer | 贈與 | 400 | 無金額 |
| 2026-02-25 | Michelle J. Howard | Director | 公開市場買進 | 50 | 約 1.2 萬 USD @ $237.83 |
| 2026-02-25 | Michael Miebach | Director | 公開市場買進 | 434 | 約 10.1 萬 USD @ $233.33 |
| 2026-01/02 | 多位高階主管 | — | 授予 / 歸屬 | 數千至數萬股 | 無金額（授予類） |

- 公開市場交易以董事買進為主（合計約 11.3 萬 USD），唯一較大金額的交易為 Thomas 的賣出（約 576 萬 USD）。規模相對於 IBM 市值很小，訊號強度有限。
- 內部人持股比例僅 0.16%，對股價影響不大。

**股東結構**
- 機構持股 64.6%（共 4,294 家），float 持股 64.7%。
- 放空比例 (short % of float) 2.1%，days to cover 約 3.1 天，放空壓力低。
- Overall governance risk 6/10（Audit risk 8、Board risk 7、Compensation risk 3）。審計風險分數偏高，屬需持續留意的治理項目。

---

## 9. 量子運算 / Qiskit 選擇權

- IBM 在超導量子運算與開源 Qiskit 生態系具領先地位，屬於長期策略性選擇權。
- 本次資料未單獨揭露量子業務的營收或獲利，目前對營收的貢獻應視為微小，不宜計入 FY2027 的估值主體。
- Qiskit 的價值在於開發者與企業的生態系鎖定，以及未來若量子商業化時的先發優勢。路線圖時程與里程碑未經本次工具驗證，需另行確認。

---

## 10. 主要風險與資料限制

**基本面風險**
1. **成長偏低**：營收 YoY 約 4–5%，顯示核心業務擴張有限，估值主要依賴 EPS 成長與股利。
2. **槓桿上升**：2026 併購後淨負債約 561 億 USD，若利率維持高檔或併購整合不順，FCF 配置空間會被壓縮。
3. **併購整合**：Q1 FY2026 獲利率下滑（operating margin 13.9%，Q4 FY2025 為 24.6%），含 restructuring 費用 3.6 億 USD，整合風險需追蹤。
4. **營運資金與流動性**：current ratio 0.86，依賴預收款循環，若客戶續約或預付款放緩，現金流會受影響。
5. **市場敘事**：股價 52 週大跌 26%，但 EPS 上升。市場可能對成長前景或 AI 轉型的獲利性存有疑慮，這是市場評價風險，不是財報數字風險（此為推測，本次資料未直接驗證）。

**資料限制**
- Yahoo cookie/crumb 取得失敗，資料取自快取，`source: cache`。數值為 2026-11-23 版本，非即時。
- Yahoo 的 FCF 兩種口徑（info 123.5 億 vs 季度加總 140.2 億）有差異，本文兩者皆列出。
- 分部營收、量子業務數據、Q1–Q2 FY2025 完整季度資料皆不在本次資料中。
- TTM EBITDA 以 info 數值為準（166.3 億），季度加總約 177.3 億，兩者口徑不同。

---

## 11. 關鍵指標表

| 指標 | 數值 | 期間 / 口徑 | 備註 |
|---|---|---|---|
| Ticker | IBM | NYSE | Information Technology Services |
| Price | 233.74 USD | 2026-11-23 快取 | 當日 +4.14% |
| Market cap | 2,209 億 USD | 即時快取 | |
| Enterprise value (EV) | 2,689 億 USD | | |
| Revenue (TTM) | 698.7 億 USD | TTM | |
| Revenue growth (YoY) | +4.7% | Q3 FY2026 | FY2025 為 +7.6% |
| Revenue CAGR | +3.7% | FY2022–FY2025 | |
| Gross margin | 58.0% | TTM | FY2022 為 54.0% |
| Operating margin | 18.3% | TTM | |
| EBITDA margin | 23.8% | TTM (info) | |
| Net margin (GAAP) | 16.0% | TTM | 含 Q4 FY2025 稅務利益 |
| ROE | 34.8% | TTM | 股東權益基數小，偏高 |
| ROA | 5.3% | TTM | |
| Diluted EPS (GAAP) | 11.72 USD | TTM | |
| Adjusted EPS | 12.31 USD | TTM（最近四季） | |
| EPS growth (FY2025 GAAP) | +73.8% | FY2025 vs FY2024 | 含稅務利益 |
| Trailing P/E | 19.9x | GAAP | |
| Trailing adjusted P/E | 19.0x | 調整後 | |
| Forward P/E | 17.7x | FY2027E | |
| FY2026E P/E | 18.8x | | |
| EV / EBITDA | 16.2x | TTM | |
| EV / Revenue | 3.85x | | |
| Price / Sales | 3.16x | | |
| Price / Book | 6.2x | | |
| PEG | 2.11 | | |
| Operating cash flow | 158.3 億 USD | TTM | |
| Free cash flow | 123.5 億 USD | TTM (info) | 季度加總 140.2 億 |
| FCF margin | 17.7%–20.1% | TTM | |
| Total debt | 671.4 億 USD | latest | |
| Net debt | 約 560.8 億 USD | latest | |
| Net debt / EBITDA | 約 3.4x | TTM | |
| EBIT / Interest | 約 6.3x | FY2025 | |
| Debt / Equity | 185% | latest | |
| Current ratio | 0.86 | latest | 負營運資金 |
| Tangible book value | -464.6 億 USD | FY2025 | |
| Dividend per share | 6.76 USD | 年化 | |
| Dividend yield | 約 2.9% | 以 233.74 計 | |
| Payout ratio | 57.5% | GAAP | |
| FCF / dividends | 約 1.9–2.2x | TTM | |
| Share repurchases | 約 9.9 億 USD | TTM | |
| Diluted share change | +1.2% | FY2025 YoY | |
| Beta | 0.76 | | |
| 52-week change | -26.2% | | S&P 500 同期 +3.1% |
| Analyst mean target | 259.85 USD | 23 位分析師 | 相對現價 +11% |
| Recommendation mean | 2.28 | 1 = Strong Buy, 5 = Sell | 偏買進 |
| EPS beat rate (last 8Q) | 7 / 8 | 平均 surprise +5.4% | |
| Insider ownership | 0.16% | | |
| Institutional ownership | 64.6% | 4,294 家 | |
| Short % of float | 2.1% | days to cover 3.1 | |
| Overall governance risk | 6 / 10 | Audit 8 / Board 7 | 審計風險偏高 |
| **基本面評等** | **中性偏正面** | 基於本次資料 | |
