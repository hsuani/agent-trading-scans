# Fundamentals — 6830.TW (汎銓 / MSSCORPS CO LTD) as of 2026-10-11

## Executive summary
汎銓 (6830.TW) 的財務體質在 2026 年上半年明顯轉弱: FY2025 營業利益率由 FY2024 的 7.0% 壓到 2.6%、FY2025 轉為淨損 TWD 36.7M, 2026Q1 單季虧損後 Q2 才回到小幅獲利, TTM 淨利率僅 0.6%. 現金流持續為負 (TTM OCF 約 TWD 785M, 但 PPE 資本支出約 TWD 1,098M, TTM FCF 約 -TWD 313M), 同時總負債由 2025Q2 的 TWD 2,382M 增至 2026Q2 的 TWD 2,609M, 流動負債與 capital lease 明顯上升, 利息保障倍數約 1.3x. 估值面以 EV/EBITDA 約 33–38x、P/B 8.5x、P/S 12.2x 計偏貴, 且 yfinance 僅有 1 位分析師覆蓋 (目標價 TWD 750), 股價 52 週漲幅 +228% 但未有獲利支撐; 整體結論是基本面不支撐目前股價水準, 但這不構成交易建議.

資料基準: 財報最新為 2026Q2 (期末 2026-06-30, 已於 2026-08-13 公布); 股價與 info 為 cache 資料 (cached_at 2026-10-11, feed cnyes/cache), 無超過 as-of 日期的財報資料. 幣別 TWD. yfinance 對台股覆蓋較薄, 部分欄位標示 DATA_UNAVAILABLE.

## Revenue & profitability

**營收**
- 年度營收 (TWD M): FY2022 1,726.4 → FY2023 1,880.6 → FY2024 1,966.7 → FY2025 2,178.6.
- FY2022–FY2025 3 年 CAGR 約 8.1%; FY2025 YoY +10.8%. 5 年 CAGR 無資料 (yfinance 僅提供 4 個年度).
- 季度營收: 2025Q2 544.8 / 2025Q3 576.9 / 2025Q4 592.2 / 2026Q1 578.7 / 2026Q2 635.2 (TWD M). 2026Q2 YoY +16.6%, 與 info revenueGrowth 0.166 一致.
- TTM 營收 2,383.0M (與 info totalRevenue 2,382,999,040 相符).
- 2025Q1 季度數據缺漏 (quarterly_fin 為 null), 無法計算 Q1 YoY 與 H1 完整 YoY.
- 業務組成: longBusinessSummary 只描述服務項目 (TEM/EDS、DB FIB/EDS、SEM/EDS、IC circuit repair、EMMI/OBIRCH、X-ray 等材料分析與失效分析服務, 並有電子元件製造與貿易), **未提供分部營收 (segment revenue) 拆分, DATA_UNAVAILABLE**.

**獲利能力 (毛利 / 營業 / 淨利)**

| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 40.3% | 21.9% | 16.7% |
| FY2023 | 37.1% | 18.4% | 13.9% |
| FY2024 | 26.7% | 7.0% | 3.3% |
| FY2025 | 23.7% | 2.6% | -1.7% |

- 毛利率 FY2022→FY2025 下滑約 16.6 個百分點; 季度毛利率 2026Q1 為 21.6% (為近期低點), 2026Q2 回升至 25.0%.
- 營業利益: FY2024 137.8M → FY2025 55.9M; 季度 2025Q2 41.4 / 2025Q3 33.6 / 2025Q4 29.6 / 2026Q1 -10.5 / 2026Q2 15.8 (TWD M). TTM (2025Q3–2026Q2) 營業利益約 68.5M, 營業利益率約 2.9% (info operatingMargins 為 2.5%, 定義略有差異).
- 淨利: FY2025 -36.7M; 季度 2025Q2 -14.7 / 2025Q3 +30.5 / 2025Q4 -3.7 / 2026Q1 -31.9 / 2026Q2 +18.6 (TWD M). TTM 淨利 13.6M (與 info netIncomeToCommon 13,615,000 相符), TTM 淨利率 0.6%.
- EPS: FY2024 diluted 1.33 → FY2025 -0.71; trailingEps 0.25; 2026Q2 單季 diluted EPS 0.35.
- ROE (info): 0.43%; ROA (info): 0.68%. FY2025 ROE 以期末股東權益計約 -1.2%.
- ROIC (估算): TTM NOPAT ≈ 營業利益 68.5M × (1-20%) ≈ 54.8M, 除以 2026Q2 invested capital 5,500.6M ≈ 1.0%. 屬估算值, 非 yfinance 直接提供.
- 折舊攤銷 (D&A) 規模大: FY2025 D&A 782.9M, 佔營收 35.9%. EBITDA 幾乎全數被折舊吃掉, 營業利益率低為資本密集的直接結果.

## Cashflow & balance sheet

**現金流品質**
- OCF (TWD M): FY2022 663.1 / FY2023 657.7 / FY2024 694.9 / FY2025 742.8. TTM OCF 785.1 (與 info operatingCashflow 785,072,000 相符).
- PPE 資本支出 (TWD M): FY2022 589.4 / FY2023 971.6 / FY2024 1,628.3 / FY2025 1,181.6. TTM 資本支出約 1,098.4 (2025Q3–2026Q2 合計 204.0 / 294.1 / 354.1 / 246.2).
- FCF (OCF - PPE capex): FY2022 +71.9 / FY2023 -320.9 / FY2024 -944.3 / FY2025 -439.2 (TWD M, yfinance 年度 FCF 欄位). FCF margin: FY2022 +4.2% / FY2023 -17.1% / FY2024 -48.0% / FY2025 -20.2%.
- TTM FCF: 以 OCF - PPE capex 計約 -313M; yfinance quarterly FCF 欄位加總 -315.3M; info freeCashflow 為 -336.1M. 三者差異源於定義 (是否含 intangible 與其他項目), 方向一致: **TTM 自由現金流為負**.
- FCF / NI: FY2025 NI 為負, FCF/NI 不適用 (n/m); 健康門檻 >0.9 **未達成**. OCF/EBITDA (TTM): 785 / 924 ≈ 85%, 營運現金轉換尚可, 問題在於資本支出規模.

**資產負債表 (2026-06-30)**
- 現金及約當現金: TWD 682.4M (2025Q2 為 878.5M, YoY 約 -22%).
- 總債務 (total debt): TWD 2,608.8M (2025Q2 為 2,382.0M, YoY +9.5%). 其中:
  - 短期債務 (current debt) 886.6M, 2025Q2 僅 313.5M, 短債大幅上升, 需留意再融資.
  - 長期債務 1,218.8M.
  - capital lease 合計 503.4M (FY2025 年末為 187.9M, 2026 上半年大增約 315M, 原因需看公司公告, yfinance 未說明).
- 淨負債 (net debt): TWD 1,423.0M (2025Q2 為 1,299.4M).
- 淨負債 / TTM EBITDA: 約 1.5x (以季度 EBITDA 加總 923.7M 計); info 的 TTM EBITDA 為 803.7M, 對應約 1.8x.
- Total debt / TTM EBITDA: 約 2.8x (季度 EBITDA 基準).
- 利息保障倍數 (TTM 營業利益 / 利息費用): 約 1.3x (利息費用 TTM 約 53.6M). 偏弱.
- Debt/Equity: 76.8% (info); FY2025 年末為 81.9%.
- Current ratio: 1.21 (2026Q2), FY2025 年末 1.09; Quick ratio 1.11.
- 營運資金 (working capital): 280.3M (2025Q2 為 1,004.3M), 下滑主因為短債重分類.
- 股東權益 3,395.2M, 每股淨值 BVPS 約 62.4 TWD (info bookValue 62.396). 有形淨值 3,387.6M.
- 總資產 6,583.4M, 其中 Net PPE 4,476.3M (佔總資產約 68%), 資產重度依賴設備.
- 應收帳款 773.3M (2025Q2 為 700.3M), 營收成長 16.6% 同期應收帳款成長約 10.4%, 需留意收現.

## Capital allocation & insider signal

**資本配置**
- 資本支出: 2024 年達高峰 TWD 1,628M, FY2025 降至 1,182M, TTM 1,098M; 2026Q2 單季 246M 為近四季最低, 擴產節奏放緩但仍高於 OCF 的一半以上 (TTM 資本支出/營收約 46%).
- 股利: 每股股利 1.0 TWD (dividendRate), 殖利率 0.19%. 現金股利支出: FY2022 185.7M / FY2023 257.3M / FY2024 210.5M / FY2025 51.8M. FY2025 現金股利未被獲利覆蓋 (淨利為負) 亦未被 FCF 覆蓋 (FCF 為 -439M); 股利實際由舉債與增資支應. info payoutRatio 8.0 (800%) 顯示獲利基礎極薄. 2026 年除息日約為 2026-04-09 (ex-dividend 時間戳 1775692800), 2025Q4 季度無股利支出.
- 增資/稀釋: 2024 年現金增資 600M (Issuance of capital stock); 2026 年上半年股本由 52.02M 股增至 54.66M 股 (+5.1%), 股本由 TWD 517.8M 增至 544.1M, APIC 由 2,033.7M 增至 2,382.8M (+349M), 增資來源未於 yfinance 中說明, 需查公司公告.
- 買回庫藏股: 無資料顯示 (treasury shares 2023 年為 0, 之後無記錄). 目前無 buyback 跡象.
- 債務淨增加: FY2024 大量舉債 (Issuance of debt 1,972M, Repayment 782M); FY2025 淨舉債約 250M; 2026 上半年 total debt 持續增加.

**內部人與大股東**
- 內部人交易 (insider, 最近 6 個月): yfinance 回傳空陣列 `[]`, **標示 DATA_UNAVAILABLE**. 空陣列不代表無交易, 無法計算淨買賣金額與占市值比例.
- 內部人持股 (heldPercentInsiders): 21.3%, 顯示股權相對集中.
- 機構持股 (heldPercentInstitutions): 6.85%, institutionsCount 9; inst_holders 清單為空, **DATA_UNAVAILABLE** 於單一機構明細.

## Valuation

(價格 TWD 530.0, 2026-10-11 cache; 前收 530.0; 日內區間 520–536; 市值 TWD 28,972M; 企業價值 EV TWD 30,766M; 流通股數 54.66M; 52 週區間 145–1,000; 50 日均 502.0; 200 日均 467.4; beta 1.22; 3 個月日均量約 193 萬股.)

| 估值指標 | 數值 | 註記 |
|---|---|---|
| P/E (trailing) | 2,120x | n/m, TTM EPS 僅 0.25, 不具參考價值 |
| P/E (forward) | 34.6x | 基於 forwardEps 15.32; 但 epsCurrentYear 為 4.3 (P/E 約 123x), 兩者不一致, 需以公司指引核實 |
| EV/EBITDA | 38.3x (info, TTM EBITDA 803.7M) / 約 33.3x (季度 EBITDA 加總 923.7M) | 偏貴 |
| EV/Revenue | 12.9x | — |
| P/S (TTM) | 12.2x | 偏貴 |
| P/B | 8.5x | 偏貴 |
| P/FCF | n/m | TTM FCF 為負 |
| PEG | DATA_UNAVAILABLE | — |

- 與同業比較: yfinance 未提供行業中位數; 下表 "Sector median (estimate)" 為分析師估計值 (無可靠資料來源), 僅作量級參考, 非實測.
- 分析師: numberOfAnalystOpinions = 1, recommendationKey buy, targetMeanPrice 750 TWD (相對現價約 +41.5%). 單一分析師覆蓋, 共識強度不足以作為參考.
- 價格動能: 52 週漲幅 +228%, 自高點 1,000 回落約 47%, 股價位於 50 日與 200 日均線之上. 估值與 52 週漲幅同時偏高, 基本面與股價走勢脫節.

## Key catalysts
- **下一次財報**: yfinance earnings_dates 最後一筆為 2026-08-13 (Q2 2026), EPS estimate 1.08 vs reported 0.35, surprise -67.6%. 下次 (2026Q3) 財報日期 **DATA_UNAVAILABLE** (未列於資料中; 台股季報通常於季後約 45 日內公布, 僅作一般慣例參考).
- **盈餘歷史**: 近 10 筆可比較資料中 8 筆低於預估 (含 2026Q2 -67.6%), 僅 2023-08 與 2023-03 兩筆優於預估. EPS 預估穩定性偏低, 歷史 miss 幅度大.
- 2025Q2、2025Q3、2025Q4 的財報日期未出現在 earnings_dates 中, 資料有缺漏.
- **管理層指引 (guidance)**: DATA_UNAVAILABLE (yfinance 不提供).
- **業務 / 產能**: 資本支出自 2024 高峰回落, 2026Q2 單季 246M; 後續擴產節奏與 capital lease 增加的用途 (設備或廠房) 為重要觀察點, 需參閱公司法說與公告.
- **再融資**: 短期債務 886.6M 佔總債務約 34%, 下一季債務到期與續借條件為近期關注事項.
- **增資後股本**: 股本已增至 54.66M 股, 後續 EPS 基準會受攤薄影響.
- **股利**: 2026 除息已發生 (約 2026-04); 下次股利政策需等待公司公告.

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (TWD M) | 2,383.0 | Q2'26 YoY +16.6% | n/a | 成長回溫 |
| 營收 FY2025 (TWD M) | 2,178.6 | +10.8% | n/a | 中等 |
| 營收 3Y CAGR (FY22–25) | 8.1% | — | 估計 5–10% | 中等 |
| 毛利率 TTM | 25.1% | FY25 23.7% vs FY24 26.7% (-3.0pp) | 估計 35–45% | 偏弱 |
| 營業利益率 TTM | 2.5%–2.9% | FY25 2.6% vs FY24 7.0% | 估計 10–15% | 偏弱 |
| 淨利率 TTM | 0.6% | FY25 -1.7% vs FY24 3.3% | 估計 8–12% | 偏弱 |
| ROE | 0.4% (info) | FY25 約 -1.2% | 估計 10%+ | 偏弱 |
| ROIC (估算) | 約 1.0% | — | 估計 8–10% | 偏弱 |
| FCF margin TTM | 約 -13% | FY25 -20.2% vs FY24 -48.0% | 估計 >5% | 偏弱 |
| FCF / NI | n/m (NI 為負或接近零) | — | >0.9 | 未達標 |
| OCF / TTM EBITDA | 約 85% | — | 估計 >70% | 尚可 |
| 資本支出 / 營收 TTM | 約 46% | FY25 54% vs FY24 83% | 估計 15–25% | 偏高 |
| 淨負債 (TWD M) | 1,423.0 | +9.5% (vs 2025Q2) | — | 上升 |
| 淨負債 / TTM EBITDA | 約 1.5x (季度基準) | — | 估計 <2x | 可接受, 偏高 |
| 利息保障倍數 (TTM 營業利益 / 利息) | 約 1.3x | — | 估計 >5x | 偏弱 |
| Current ratio | 1.21 | FY25 1.09 | 估計 1.5 | 偏低 |
| Debt / Equity | 76.8% | FY25 81.9% | 估計 <50% | 偏高 |
| 現金及約當現金 (TWD M) | 682.4 | -22% (vs 2025Q2) | — | 下降 |
| 股本增加 | 52.02M → 54.66M 股 | +5.1% | — | 稀釋 |
| 現金股利 (TWD M) | FY25 51.8 | FY24 210.5 (-75%) | — | 未被獲利覆蓋 |
| 內部人買賣 (6 個月) | DATA_UNAVAILABLE | — | — | DATA_UNAVAILABLE |
| 內部人持股 | 21.3% | — | — | 集中 |
| P/E trailing | 2,120x | — | 估計 25–35x | n/m |
| P/E forward | 34.6x (epsCurrentYear 基準為 123x) | — | 估計 25–35x | 偏貴 |
| EV/EBITDA | 38.3x (info) / 約 33x (季度) | — | 估計 15–20x | 偏貴 |
| P/S (TTM) | 12.2x | — | 估計 3–5x | 偏貴 |
| P/B | 8.5x | — | 估計 2–4x | 偏貴 |
| Beta | 1.22 | — | — | 中高 |
| 分析師目標價 | 750 TWD (1 位) | 相對現價 +41.5% | — | 覆蓋不足 |

## Red flags
- 獲利急速惡化: 營業利益率由 FY2022 21.9% 降至 FY2025 2.6%; FY2025 淨損 TWD 36.7M; 2026Q1 單季虧損 31.9M.
- 毛利率連續下滑: 40.3% → 37.1% → 26.7% → 23.7%, 2026Q1 低至 21.6%.
- 自由現金流持續為負: FY2023–FY2025 皆為負值, TTM 約 -313M; 資本支出主要依賴舉債與增資支應.
- 債務與租賃負債上升: total debt TWD 2,609M (+9.5% YoY), capital lease 由 FY2025 的 188M 增至 503M, 短期債務 887M.
- 利息保障倍數偏低 (約 1.3x), 獲利若再下滑, 償債壓力會迅速放大.
- 現金水位下降: 現金 682M, 較 2025Q2 減少約 22%.
- 股本稀釋: 2026 上半年股本 +5.1%, 攤薄 EPS.
- 盈餘預估失準: 近 10 筆可比資料中 8 筆 miss, 2026Q2 EPS 實際 0.35 vs 預估 1.08 (-67.6%).
- 股利未被覆蓋: FY2025 現金股利 51.8M, 獲利為負, FCF 為負; info payoutRatio 800%.
- 估值與基本面背離: EV/EBITDA 約 33–38x, P/B 8.5x, 52 週漲幅 +228%, 但 TTM 淨利率僅 0.6%.
- 分析師覆蓋極少 (1 位), 目標價與共識不具統計意義.
- 內部人持股 21.3%, 股權集中; 內部人交易資料 DATA_UNAVAILABLE, 無法判斷近期內部人買賣方向.
- 資料一致性問題: (a) TTM EBITDA info 803.7M vs 季度加總 923.7M; (b) forwardEps 15.32 vs epsCurrentYear 4.3; (c) TTM FCF info -336.1M vs 季度加總 -315.3M; (d) 2025Q1 與 2025Q4 部分季度欄位缺漏 (null). 使用時應以年報/法說為準.
- 資料來源為 cache (cached_at 2026-10-11), 非即時 Yahoo 回應; 價格與估值指標需於交易前再以即時資料核對.

FUNDAMENTALS REPORT COMPLETE
