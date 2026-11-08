# Fundamentals — SKHY as of 2026-11-09

## Executive summary
代碼身分驗證失敗：`pipeline/tools/yf SKHY info` 回傳的公司為 **SK hynix Inc.**（Icheon-si, South Korea, 半導體 DRAM/NAND），並非任務指定的 Sky Harbour Group。本報告不對 SKHY 給出財務健康度或估值結論，以免把 SK hynix 的資料誤套到 Sky Harbour 身上。下游研究員與交易員請勿引用本檔任何數字作為 SKHY 的基本面依據。需要任務方確認正確代碼（Sky Harbour Group 的 NYSE American 代碼可能為 SKYH，但本次 `pipeline/tools/yf SKYH info` 未回傳任何可解析欄位，無法確認）後重新執行。

## 代碼驗證結果
| 項目 | 回傳值 | 判定 |
|---|---|---|
| shortName / longName | SK hynix Inc. | 與 Sky Harbour Group 不符 |
| symbol / quoteType | SKHY / EQUITY | 代碼存在 |
| exchange | NMS | 與任務所述之 Sky Harbour 上市地不符（Sky Harbour 為 NYSE American 系列） |
| sector / industry | Technology / Semiconductors | 與 Sky Harbour（私人飛機停機坪營運）產業不符 |
| longBusinessSummary | DRAM、NAND、SSD、foundry | 與 Sky Harbour 業務不符 |
| 官網 / 地址 | skhynix.com / Icheon-si, Korea | 非美國本地公司 |
| SKYH info 測試 | 無任何 longName / shortName 欄位回傳 | 無法確認 |

## 資料可用性與單位問題（僅供追查，不作為 SKHY 結論）
- `info` 中 currency 標示 USD，但 `financials`、`balance_sheet`、`cashflow` 的數值量級為 KRW（例如 2025-12-31 的 Free Cash Flow 為 24,793,783,000,000，Net Income From Continuing And Discontinued Operation 約 42,919,287,000,000,000 級別），單位標示互相矛盾。
- `info` 中 marketCap 為 897,967,652,864，與 enterpriseValue 為 -97,741,602,553,856 並存，EV 為負值且數值量級不一致，無法用於估值。
- `info` 中 trailingPE 8.12、forwardPE 3.01、priceToSalesTrailing12Months 0.0033 等比率彼此不一致（P/S 0.0033 與 marketCap 相比明顯失真），不可採信。
- `fast_info` 的 last_price 127.34 USD、previous_close 123.90 USD、52 週區間 122.20–199.87 來自 cache fallback（live 報價主機被 proxy 阻擋，屬本環境正常現象）。此價格對應的是回傳的 SK hynix 資料，不能視為 Sky Harbour 的價格。
- 依規定，若無法確認價格對應的標的，應視為 PRICE_DATA_UNAVAILABLE。本次對 SKHY（Sky Harbour）而言，價格資料無法確認歸屬。

## 日期覆蓋（僅供參考）
- earnings_dates 最近一筆已報告季為 2026-10-28（EPS 實際 4.10 vs 預估 6.24，-34.24%），下一次財報預定 2027-01-27（EPS 預估 8.96）。這些資料屬於 as-of 日期 2026-11-09 之後或接近期間，且屬 SK hynix 而非 SKHY 目標公司。
- 今日為 2026-11-08，部分資料日期晚於今日，屬於數據異常，需要檢查來源。

## Revenue & profitability
本節無法對 SKHY（Sky Harbour）作答，因為營收與獲利資料全部來自 SK hynix。未計算任何 CAGR、毛利率、ROE 或 ROIC。

## Cashflow & balance sheet
本節無法對 SKHY 作答。未計算 FCF / NI、net debt、current ratio 或 D/E。

## Capital allocation & insider signal
- `insider`（近 6 個月）回傳為空陣列 `[]`，無法判定內部人買賣方向。
- `major_holders`：insidersPercentHeld 2e-05（約 0.002%）、institutionsPercentHeld 0.0102（約 1.02%）、機構數 441，屬 SK hynix 的持股數據，不能套用於 Sky Harbour。
- 股利與回購資料來自 SK hynix（dividendRate 0.11、exDividendDate 1788134400），不採用。

## Valuation
本節不給出估值結論。`info` 的 P/E、forwardPE、PEG 0.16、P/B 3.95 與 EV/EBITDA -0.452 相互矛盾（EV 為負），且屬 SK hynix，無法與 Sky Harbour 的分析師目標價比較。

## Key catalysts
- 無可靠的 SKHY（Sky Harbour）催化劑資料。
- 回傳資料中的下次財報 2027-01-27 屬 SK hynix，不採用。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 公司身分 | SK hynix Inc. | n/a | n/a | 不符，阻擋 |
| Revenue (USD B / 億) | n/a | n/a | n/a | 未採用 |
| Net margin | n/a | n/a | n/a | 未採用 |
| FCF / NI | n/a | n/a | n/a | 未採用 |
| Net debt | n/a | n/a | n/a | 未採用 |
| Trailing P/E | 8.12（SK hynix） | n/a | n/a | 不採用 |
| EV/EBITDA | -0.452（SK hynix，EV 為負） | n/a | n/a | 不採用 |
| P/S | 0.0033（失真） | n/a | n/a | 不採用 |
| 內部人淨買賣 (6 個月) | 空陣列 | n/a | n/a | 無資料 |
| 價格 | 127.34 USD（cache，歸屬不明） | n/a | n/a | PRICE_DATA_UNAVAILABLE（歸屬無法確認） |

## Red flags
- 代碼 SKHY 解析為 SK hynix Inc.，與任務指定公司 Sky Harbour Group 不符，屬於標的錯誤風險。
- 價格、財報與 info 的單位標示互相矛盾（USD 標示 vs KRW 量級）。
- EV 為負值、P/S 0.0033 等比率失真，info 欄位不可信。
- 內部人交易資料為空，無法判斷內部人信號。
- 部分資料日期晚於今日 2026-11-08，屬於數據異常。
- 下游需要先由任務方確認正確代碼，再重新執行本流程。

FUNDAMENTALS REPORT COMPLETE
