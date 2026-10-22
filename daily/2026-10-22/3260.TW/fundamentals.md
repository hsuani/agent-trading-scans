# 基本面分析 — 3260.TW (威剛 ADATA) 截至 2026-10-22

## 執行摘要

威剛為記憶體模組/SSD 品牌商，屬記憶體供應鏈下游。yfinance 對本檔的財務資料覆蓋極薄——`info`、`financials`、`quarterly_fin`、`cashflow`、`balance_sheet` 等多數端點均回傳空值或 404 Not Found——無法依標準化數據驗證獲利結構。依公開月營收公告與法說會紀錄，2026 年上半年營收呈現 3 倍多年增，但公開市場分析師目標價分歧極大（200–556 TWD），反映法人對其獲利延續性信心不一。

**整體評估：** 財務資料不足，無法給出基本面健康度的量化評等；估值吸引力無法由標準工具驗證；位置規模化必須考量高資訊不確定性。

---

## 收入與獲利能力

**yfinance 資料可用性**

- `financials`、`quarterly_fin`、`cashflow`、`balance_sheet` 查詢均回傳空陣列，`info` 端點僅回傳 `trailingPegRatio: null`，無 P/E、營收、毛利率、營業利潤率等任何標準化數據
- 本檔為台股中小型模組廠於 yfinance 常見的資料缺口，非公司基本面本身的負面訊號

**公開月營收與法說摘要（非 yfinance 工具產出，方向性參考）**

| 期間 | 指標 | 數值 | 說明 |
|---|---|---|---|
| 2025 年全年 | EPS (TWD) | 23.18 | 公司公告；創歷史新高 |
| 2026 年 1 月 | 歸屬母公司淨利 YoY | +3,516% | 低基期效應；月度數據 |
| 2026 年 4 月 | 營收 YoY | +170% | 環比及年同對比 |
| 2026 年 6 月 | 月營收 (NTD B) | 146.61 | 月增 13.3%、年增 212.1% |
| 2026 年 H1 | 累計營收 (NTD B) | 642.72 | 年增 183.3% |

**指標評論**

由於上述數字並非來自 yfinance 標準化工具，本報告對其計算口徑與真實性不做背書，僅作為市場公開訊號參考。正式成長率判定以「DATA_UNAVAILABLE」標記。模組廠商業模式使其獲利對上游 DRAM/NAND 晶粒採購成本波動敏感；若上游報價上升速度快於終端售價調整，存在毛利率被壓縮風險。

---

## 現金流與資產負債表

**DATA_UNAVAILABLE**

- `quarterly_cf`、`cashflow`、`quarterly_bs`、`balance_sheet` 查詢均為空
- FCF、FCF/NI、淨債務、流動比率、負債/權益比等指標皆無法由工具驗證

---

## 資本配置與內部人信號

**DATA_UNAVAILABLE**

- `insider`、`major_holders`、`inst_holders` 查詢均為空，無內部人持股比例或買賣超資料
- 公司於 2026 年初公告實施庫藏股 4,000 張（非 yfinance 驗證數字，公開消息來源參考）

---

## 估值

**yfinance 資料可用性**

- `info` 端點無 `trailingPE`、`forwardPE`、`marketCap`、`targetMeanPrice` 等任何估值欄位（僅剩 `trailingPegRatio: null`）
- 無法由工具計算本益比或法人目標價隱含空間

**分析師目標價分歧（公開市場信息）**

| 日期 | 評等 | 目標價 (TWD) | 變化說明 |
|---|---|---|---|
| 2025 年 11 月 | Trading Buy | 200 | 券商下修；原目標 297.5 |
| 2026 年 5 月 | 買進 | 556 | 另一券商 |
| 現行 | — | 200–556 區間 | 分歧幅度 178% |

**估值評論**

分析師目標價分歧達 178%（200–556 TWD），本身即為風險訊號，顯示市場對其獲利能見度與延續性看法不一。P/E 無法由工具驗證，相對估值亦無行業中位數可供對標。

---

## 關鍵催化劑

**盈餘日期**

- `earnings_dates` 查詢回傳空值，DATA_UNAVAILABLE

**產業面催化劑**

1. **記憶體現貨價格走勢** — 若 DRAM/NAND 報價維持強勢，威剛作為下游品牌商可望受惠終端拉貨需求
2. **上游成本與終端定價節奏** — 模組廠毛利結構上游原物料成本占比高；若上游漲速快於下游售價調整，存在毛利率壓縮風險
3. **AI 伺服器記憶體需求** — 高效能運算市場對 DRAM/SSD 的驅動力

---

## 核心指標表

| 指標 | 單位 | 最新值 | YoY 變化 | 行業中位數預估 | 評論 |
|---|---|---|---|---|---|
| 營收成長率 | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| 毛利率 | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| 營業利潤率 | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| 淨利潤率 | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| ROE | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| ROIC | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| FCF 保證金 | % | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| FCF / NI | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| 淨債務 | NTD B | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| 流動比率 | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| 負債/權益比 | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| Trailing P/E | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| Forward P/E | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| EV/EBITDA | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| P/FCF | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |
| P/S | 倍 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | yfinance 無資料 |

---

## 紅旗警訊

1. **yfinance 財務資料全面缺失** — `financials`、`quarterly_fin`、`cashflow`、`balance_sheet`、`insider`、`rec_summary` 等均為空或 404 Not Found。台股中小型模組廠於 yfinance 常見的資料缺口，但對本框架的量化驗證能力造成完全阻礙。位置規模化必須在交易員與風控階段特別註記高資訊不確定性。

2. **分析師目標價分歧極大** — 200–556 TWD 區間，分歧幅度 178%，顯示市場對其獲利能見度與可延續性缺乏共識。部分券商於 2025 年 11 月下修評等至「Trading Buy」並砍目標價至 200 元（原 297.5 元），暗示法人信心動搖。

3. **產業成本風險** — 模組廠毛利結構對上游 DRAM/NAND 晶粒採購成本波動敏感。若上游報價上升速度快於終端定價調整能力，存在毛利率被壓縮風險，此為供應鏈下游通病。

4. **營收成長能見度** — 2026 年上半年營收 3 倍多年增係奠基於低基期與產業景氣上行；若產業進入週期調整，成長動能可能快速反轉。

---

## 資料來源與限制

| 面向 | 說明 |
|---|---|
| yfinance 查詢日期 | 2026-10-23 |
| 最後可用價格資料 | 328.0 TWD (前日收盤 332.5 TWD，日跌 -1.4%)；來源：cnyes 備用資料集 |
| 財務資料狀態 | 完全 DATA_UNAVAILABLE — `financials`、`balance_sheet`、`cashflow` 均為空；`info` 端點 404 Not Found |
| 公開營收/EPS 資料 | 源自公司官方月營收公告與法說會紀錄，非 yfinance 工具產出，計算口徑由公司自行定義，本報告不做背書 |
| 台灣上市公司覆蓋缺口 | yfinance 主要針對美國與部分主要國家市場優化；台灣上市公司（尤其中小型廠商）財務資料普遍稀缺 |

---

## 建議後續資訊補充管道

1. **台灣證交所官方** — TWSE Mops (https://mops.twse.com.tw)：最新季度與年度申報文件
2. **公司官方** — 年度報告、季度財務結果新聞稿、投資人關係網站
3. **機構級資料源** — Bloomberg、FactSet、TEDB 台灣電子資料庫，可取得完整審計後財務報表與分析師共識

---

**FUNDAMENTALS REPORT COMPLETE**
