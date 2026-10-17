# Fundamentals — 5455.TWO as of 2026-10-18

## ⚠️ 資料完整性警示：代碼對應疑似錯誤

本報告依既定流程使用 `pipeline/tools/yf.py 5455.TWO info/financials/...` 取得資料，但回傳結果顯示：

- `longName`: **Sheng Yi Development Co., Ltd.**（中文曾用名「訊力系統工程」，2017 年更名為「盛餘開發」）
- `sector` / `industry`: **Real Estate / Real Estate - Development**
- `longBusinessSummary`: 該公司從事「台灣住宅建築營造、建材銷售、室內裝修租售、不動產租賃及建材批發」業務，總部位於新竹市。

此與 tw_photonics sector 定義中「5455.TWO = 英特磊（Episil-Precision，化合物半導體磊晶代工廠）」**完全不符**——英特磊應為半導體 / 光電材料公司，而非不動產開發商。本報告所引用的所有數字（股價、營收、財報）均為 yfinance／repo 快取對 `5455.TWO` 這個代碼所回傳的資料，三個獨立資料源（`yf.py info`、`ta.py snapshot`、repo 內 `prices/5455.TWO.csv` 快取）**互相一致**，顯示這不是單一資料來源的暫時性錯誤，而是代碼對應本身的問題（可能原因：TPEx 代碼重複使用、股票代碼變更、或 sector universe 定義與 yfinance 的代碼解析不一致）。

**建議**：本報告數據不應用於評估英特磊的基本面。下文仍依流程完整呈現 `5455.TWO` 查得的實際公司（盛餘開發）數據以保留稽核軌跡，但 Phase 2-4（辯論、交易、風險）**不應**基於此資料對英特磊做出任何多空判斷。

## Executive summary（針對「5455.TWO = 盛餘開發」本身）
盛餘開發為新竹地區住宅營造／不動產開發公司，與矽光子 / 光通訊產業無關。FY2025 營收年減 -43.6%，淨利率 -156.4%（重度虧損），FCF 連續轉負，財務體質疲弱，與 tw_photonics sector 之投資主題完全不相關。

## Revenue & profitability
- FY2025 營收 20.44 億 TWD，較 FY2024 的 36.24 億衰退 -43.6%（不動產認列收入本質上具有高度季度波動，與建案交屋時點有關，非持續性經營指標）。
- 淨利率 -156.4%、營業利益率 -1032.8%，顯示近期處於嚴重虧損狀態。
- ROE -3.03%。

## Cashflow & balance sheet
- FY2025 FCF -4.94 億、FY2024 FCF -1.06 億，連續兩年現金流為負。
- 現金 1.96 億，總負債 27.95 億，淨負債龐大，財務槓桿高，符合不動產開發商重資產、高槓桿的典型特徵，而非光電科技公司的資本結構。

## Capital allocation & insider signal
- 內部人持股高達 70.3%（典型家族掌控型不動產開發商持股結構），機構持股 0%（無機構關注）。
- `insider` 交易明細資料為空。

## Valuation
- trailingPE / forwardPE 均為 None（無法計算，因近期獲利為負）。
- 現價 30.0 TWD，52 週區間 22.0–32.25，波動相對平緩（beta ≈ 0），與高波動光電成長股特徵相反。

## Key catalysts
- 無與矽光子 / 光通訊相關之催化劑；`earnings_dates` 資料庫中最新一筆日期為 2007-04-27（資料斷層達近 20 年），進一步佐證此代碼在 yfinance 資料庫中對應的是一家長期未受分析師覆蓋的小型地產公司。

## Metrics table
| Metric | Latest | YoY | Sector median（估，僅供參照） | Verdict |
|---|---|---|---|---|
| 營收（FY2025） | 20.44 億 TWD | -43.6% | — | 與矽光子無關，不適用 |
| 淨利率 | -156.4% | — | — | 重度虧損 |
| FCF | -4.94 億 TWD | 連續兩年負 | — | 財務疲弱 |
| Trailing/Forward P/E | n/a | — | — | 獲利為負，無法計算 |

## Red flags
- **代碼與公司身分不符**（本報告最重要的紅旗）：無法確認此為英特磊之真實數據。
- 即便忽略身分問題，單就「5455.TWO = 盛餘開發」本身而言，財務表現亦顯著惡化（營收腰斬、重度虧損、現金流轉負）。
- 零機構覆蓋、財報資料庫斷層近 20 年，資料可信度與完整性皆低。

FUNDAMENTALS REPORT COMPLETE
