# Fundamentals — SOI as of 2026-11-23

## Executive summary
本次無法取得 SOI 任何財務數據，財務健康度與估值吸引力均判定為 DATA_UNAVAILABLE，不做方向性結論。代碼身分需先釐清：美股 SOI 在 `prices/quotes.json` 回傳 Yahoo v8 HTTP 404，且 `yf SOI` 的 info 只回 `quoteType: NONE`；依 Serenity 貼文中的 Photonics-SOI 描述與 `serenity/strategy_2026-09-02.md` 的註記，推定其指 Soitec（Euronext Paris，Yahoo 代號推定為 SOI.PA），但此為推定，非工具輸出。現有可用資訊僅為 Serenity 社群貼文的引述（$25M 季度 Photonics-SOI 營收、$1.2B 長期產能承諾），屬未驗證的第三方說法，不能取代財報數據。

## Data source status
- `pipeline/tools/yf SOI <kind>` 全部 kind（info / fast_info / financials / quarterly_fin / balance_sheet / quarterly_bs / cashflow / quarterly_cf / earnings_dates / insider / major_holders / inst_holders）皆為空或 null。
- 即時呼叫 `pipeline/tools/yf SOI.PA info` 失敗：CONNECT tunnel failed, response 403（雲端沙箱無法連 Yahoo）。
- 快取 `prices/yf/SOI.json` 存在但所有欄位為空（`_refreshed_at` 2026-11-22T14:32:31+00:00，`_misses` 為空），info 僅含 `quoteType: NONE`、`financialCurrency: USD`。
- `prices/quotes.json` 記錄：`SOI: no history for SOI (yahoo_v8: HTTP Error 404: Not Found)`。
- `prices/` 目錄內無 SOI 或 SOI.PA 的價格 CSV。
- 資料時點：快取更新於 2026-11-22，早於 as-of 2026-11-23，未見超過 as-of 日期的資料；但因本身無資料，時點檢查無實質內容。

## Revenue & profitability
DATA_UNAVAILABLE。營收、CAGR、毛利率、營業利益率、淨利率、ROE、ROIC 均無法從工具取得，不做估算。

社群引述（未驗證，僅供背景）：
- Serenity（serenity/signals.json）引述：Photonics-SOI 季度營收約 $25M，且其表示「Revenue grew 39%, with Photonics-SOI leading the way」與「Margin expansion has come forward too」，但未附財報原文或數字來源。
- Serenity（serenity/strategy_2026-09-02.md、2026-09-08.md）稱 $200M 光子 SOI 收入為「絕對下限」；2026-11-17 筆記稱 FY2028 營收預測約 $400M。上述數字之間（季度 $25M 與年化 $200M 的關係、FY2028 $400M 的口徑）未經核對，無法調和。

## Cashflow & balance sheet
DATA_UNAVAILABLE。FCF、FCF/NI、淨負債、流動比率、負債權益比、現金部位均無資料。

## Capital allocation & insider signal
- 資本支出、股利、庫藏股：DATA_UNAVAILABLE。
- 內部人交易（近 6 個月）：DATA_UNAVAILABLE，無法計算淨買賣與相對市值比例。
- 社群引述：Serenity 稱 Soitec 取得約 $1.2B 多年期產能承諾，並提及「with cash deposits」（客戶以現金支付保證金）。此為客戶端承諾金額，是否列入營收、是否分期認列，皆無法由現有資料確認；應視為待財報確認的事項，而非已實現的訂單或收入。

## Valuation
DATA_UNAVAILABLE。無市值、股價、P/E（trailing / forward）、EV/EBITDA、P/FCF、P/S 資料，無法與半導體設備或光學元件同業中位數比較，sector median 一律標示 n/a。

## Key catalysts
- 下次財報日期：DATA_UNAVAILABLE（earnings_dates 為空）。
- 近期指引：無工具資料；社群引述 Serenity 轉述管理層說法：近封裝光學（NPO）預計於本財年底出現首批量產、次年放量；CPO 進入 scale-out 放量；TPO 為 scale-up 下一階段；FY2027 營收以 pluggable transceiver 為主。這些為二手轉述，未核對原始 earnings call。
- 客戶產能承諾：Serenity 指 $1.2B 長期產能承諾涵蓋 CY2027、CY2028 及之後；2026-09-12 筆記提到 80% 產能預訂協議預計兩週內落地。
- 分析師觀點：Serenity 引述 Citi 曾警示「investor expectations for Photonics-SOI growth might be excessive」。此為社群轉述，未核對 Citi 原文。
- 2026-11-20 Serenity 筆記語氣轉為防禦，提及對沖基金淨動能曝險自高點約 60% 降至 8%。此為社群觀察，非基本面數據。

## Metrics table
單位：USD（B / M）。TWD / KRW 不適用。所有財務欄位無資料，依規則標示 DATA_UNAVAILABLE；sector median 為 n/a。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 代碼身分（SOI 美股 / SOI.PA） | 美股 SOI 無效（404）；推定 Soitec SOI.PA | n/a | n/a | 待確認 |
| 市值（USD B） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 股價 / 50d / 200d MA | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 營收 TTM（USD M） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 營收 3-5y CAGR | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| 毛利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 營業利益率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 淨利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| ROE / ROIC | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| FCF margin / FCF÷NI（健康線 >0.9） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 淨負債（USD M） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 流動比率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 負債權益比 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 現金部位（USD M） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 資本支出 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 股利 / 庫藏股 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | DATA_UNAVAILABLE |
| 內部人淨買賣（近 6 月） | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| Trailing P/E | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| Forward P/E | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| EV/EBITDA | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| P/FCF | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| P/S | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| 下次財報日 / EPS surprise | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| 社群引述：Photonics-SOI 季度營收（USD M，未驗證） | 約 25（Serenity 引述） | n/a | n/a | 未驗證，不採信為財務數據 |
| 社群引述：多年期產能承諾（USD B，未驗證） | 約 1.2（Serenity 引述） | n/a | n/a | 未驗證，待財報確認 |

## Red flags
- 財務資料完全缺失：yfinance 無 SOI / SOI.PA 任何有效欄位，且即時連線被 proxy 擋下，快取亦為空。
- 代碼歧義：美股 SOI 無效，身分為推定（Soitec），未由工具確認。下游引用前須先確認交易所與代碼。
- 主要資訊來源為單一社群帳號（Serenity）的貼文與轉述，數字未附財報出處，且 $25M 季度、$200M 年化、FY2028 $400M 之間口徑未統一。
- 「$1.2B 長期產能承諾」是客戶承諾，非已認列營收；現金保證金的比例與條款未知。
- Serenity 引述的 Citi 警語（預期可能過高）與其 11-20 轉為防禦的語氣，顯示市場對此題材存在分歧。
- 無估值參照：即使後續取得資料，也需確認同業中位數來源，目前 sector median 無法估計。

FUNDAMENTALS REPORT COMPLETE
