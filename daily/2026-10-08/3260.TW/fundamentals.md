# Fundamentals — 3260.TW (威剛科技) as of 2026-10-08

## Executive summary
本報告無法取得任何財務報表、財務比率、內部人交易、法人持股或分析師評等資料（Yahoo Finance 端點被 agent proxy 以 403 政策拒絕，本地 cache `prices/yf/3260.TW.json` 的財務欄位皆為空陣列）。目前僅能確認價格面：2026-10-07 收盤 365 TWD，較 2026-10-06 的 370 下跌 1.4%，同時低於 50 日均線（約 398.6）與 200 日均線（約 368.3），1 個月報酬約 -11.4%。在缺乏營收、獲利、現金流與估值資料的情況下，財務健康度與估值吸引力均無法判定（DATA_UNAVAILABLE），此份報告不足以作為基本面決策依據。

## Revenue & profitability
- 營收趨勢：DATA_UNAVAILABLE（`financials` / `quarterly_fin` 回傳空陣列）。
- 3-5 年營收 CAGR：DATA_UNAVAILABLE。
- 毛利率 / 營業利益率 / 淨利率趨勢：DATA_UNAVAILABLE。
- ROE / ROIC：DATA_UNAVAILABLE。
- 最近一季 EPS 與 earnings surprise：DATA_UNAVAILABLE（`earnings_dates` 直接連線失敗，cache 為 null）。
- 產品組合 / 業務分部：`info.longBusinessSummary` 無法取得，無法引用。依公司定位屬台灣記憶體模組與儲存品牌（ADATA），但分部營收占比與毛利結構未有可引用數據。

## Cashflow & balance sheet
- FCF、FCF / NI、FCF margin：DATA_UNAVAILABLE（`cashflow` / `quarterly_cf` 空陣列）。
- 淨負債、流動比率、負債權益比、現金部位：DATA_UNAVAILABLE（`balance_sheet` / `quarterly_bs` 空陣列）。
- 資產負債表結論：無法判定。

## Capital allocation & insider signal
- Capex 趨勢、庫藏股、股利覆蓋率：DATA_UNAVAILABLE。
- 內部人交易（近 6 個月淨買賣）：DATA_UNAVAILABLE（`insider` 回傳空陣列，cache 同為空）。無法計算相對市值之規模。
- 大股東集中度與法人持股：DATA_UNAVAILABLE（`major_holders` / `inst_holders` 空陣列）。
- 分析師評等（`recommendations` / `rec_summary`）：DATA_UNAVAILABLE。

## Valuation
- 本地價格資料可計算的技術面基準（來源 `prices/3260.TW.csv`，最新列 2026-10-07）：
  - 收盤 365.0 TWD；前收 370.0 TWD（2026-10-06）。
  - 50 日均線約 398.6、200 日均線約 368.3，現價位於 50 日與 200 日均線下方（200 日均線之下約 0.9%）。
  - 1 年區間（2025-10-07 起）高 525.0（2026-03-19 歷史高點）、低 165.0。
  - 20 日平均成交量約 4,986（csv volume 欄位原始單位）。
  - 1 個月報酬約 -11.4%，3 個月報酬約 -9.7%。
- P/E（trailing / forward）、EV/EBITDA、P/FCF、P/S：DATA_UNAVAILABLE。
- 與產業中位數比較：DATA_UNAVAILABLE（無可引用之產業估值資料，故不提供估計數字）。
- 估值吸引力判定：無法判定。

## Key catalysts
- 下次財報日與 EPS 預估：DATA_UNAVAILABLE（`earnings_dates` 連線被拒）。
- 近期法說會 / 營收月報 / 指引：DATA_UNAVAILABLE（工具未涵蓋；未以外部網頁補充，以免引入未經驗證數字）。
- 價格面事件：2026-10-06 收於 370（成交量 5,898）、2026-10-07 跌至 365（成交量 7,059），近兩日量能放大，屬價格面觀察重點，非基本面催化劑。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價 (TWD, 2026-10-07) | 365.0 | DATA_UNAVAILABLE | n/a | 價格面資料，可用 |
| 1 個月報酬 | -11.4% | n/a | n/a | 價格面走弱 |
| 50 日均線 | 約 398.6 | n/a | n/a | 現價低於均線 |
| 200 日均線 | 約 368.3 | n/a | n/a | 現價接近均線 |
| 1 年高 / 低 | 525.0 / 165.0 | n/a | n/a | 區間波動極大 |
| 營收 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| 毛利率 / 營益率 / 淨利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| ROE / ROIC | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| EPS（最近一季） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| FCF / NI | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| 淨負債 / 流動比率 / D/E | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| 內部人淨買賣（6 個月） | DATA_UNAVAILABLE | n/a | n/a | 無法判定 |
| Trailing / Forward P/E | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| EV/EBITDA、P/FCF、P/S | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |
| 分析師評等 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判定 |

## Red flags
- 基本面資料完全缺失（financials、balance_sheet、cashflow、insider、holders、ratings 全部為空），財務健康度無法驗證，這本身即為分析上的最大限制。
- 價格面：現價 365 低於 50 日均線約 8.4%，1 個月跌幅約 11.4%，且 2026-10-06 與 10-07 連續收跌、量能放大。
- 1 年價格區間 165 至 525，波幅極大，單靠技術面難以判斷其價值支撐。
- 資料來源限制：Yahoo Finance 端點遭 agent proxy 政策拒絕（`fc.yahoo.com`、`guce.yahoo.com` 等 CONNECT 403），本次未嘗試繞過；此為組織政策限制，需由維運端確認。
- 日期備註：本報告以 2026-10-08 為 as-of，但今日系統日期為 2026-10-07；價格資料最後一筆為 2026-10-07，未發現晚於 as-of 日期之資料。

FUNDAMENTALS REPORT COMPLETE
