# Fundamentals — 3260.TW (威剛) as of 2026-11-24

## Executive summary
本次無法完成基本面評估：yfinance 財報三表（損益表、資產負債表、現金流量表，年度與季度）全部回傳空陣列，earnings_dates 與 insider、持股資料也都失敗或為空，info 僅剩快取中的 trailingPegRatio: null。現有可用資料只有行情：最新價 271.0 TWD，前收 249.5 TWD，當日高 274.0 / 低 270.0（cnyes 來源，快取時間 2026-11-24 05:32 UTC），上漲約 8.6%。財務健康度與估值吸引力目前判定為「資料不足，無法判斷」，不應依此報告做出基本面結論。

## Data status（資料完整度）
- 重試一次後仍失敗，錯誤為 `CONNECT tunnel failed, response 403`（yfinance 經 proxy 被拒），並有 `Cookie/crumb fetch failed`。這是資料來源端問題，不是該股無資料的證據。
- 可用：fast_info（價格，來源 cnyes，快取）。
- 不可用或為空：info（市值、P/E、beta、產業、profile 皆缺）、financials、quarterly_fin、balance_sheet、quarterly_bs、cashflow、quarterly_cf、earnings_dates、insider、major_holders、inst_holders。
- fast_info 的 market_cap、shares、50/200 日均線、52 週高低、10 日均量皆為 null 或 NaN，因此無法從資料推算市值或技術位階。
- 本報告未引用任何外部網頁數字。所有數值皆為上述工具 JSON 的原值。
- 因財報完全缺失，本報告不產生任何 TWD 金額（億元）或 USD 金額，因此沒有單位換算風險；日後補資料時需以 億 TWD 標示，不混用 B。
- 資料時間：快取時間為 2026-11-24 當日，與分析日期 DATE 相同，未見超出 DATE 的資料。

## Revenue & profitability
資料不足。營收、毛利率、營業利益率、淨利率、ROE、ROIC 的 CAGR 與趨勢皆無法計算，全部標為 n/a。
產業背景（非數據）：威剛為台灣 DRAM 模組與工控/車用記憶體廠商，獲利通常隨 DRAM 合約價與庫存跌價損失週期波動，這需要財報佐證，本報告無法驗證。

## Cashflow & balance sheet
資料不足。FCF margin、FCF/NI、淨負債、流動比率、負債權益比、現金部位皆為 n/a。
無法判斷現金流品質是否達到 FCF/NI > 0.9 的健康門檻。

## Capital allocation & insider signal
資料不足。資本支出趨勢、庫藏股、現金股利覆蓋率皆為 n/a。
insider 交易（近 6 個月）回傳空陣列，但由於 yfinance 請求失敗，空陣列不能解讀為「無內部人交易」。內部人買賣淨額與市值比無法計算。
大股東與機構持股集中度（major_holders、inst_holders）皆為空，無法評估。

## Valuation
資料不足。trailing / forward P/E、EV/EBITDA、P/FCF、P/S 皆為 n/a，無法與產業中位數比較。
market_cap 為 null，因此無法換算估值。
僅有股價 271.0 TWD 可記錄，但沒有每股盈餘或每股淨值可對照，無法判斷便宜或昂貴。

## Key catalysts
- 下次財報日期：n/a（earnings_dates 請求失敗）。
- 近期法說會、指引、產品組合變化：yfinance 無資料，無法驗證。
- 價格面：單日 +8.6%（249.5 → 271.0），來源僅為單日報價，無法判斷是否伴隨基本面消息，需由其他 agent 的新聞或籌碼報告補足。

## Metrics table
單位：財務金額欄位以 億 TWD 標示（目前無資料）；股價為 TWD。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 股價（TWD） | 271.0 | 前收 249.5，日變動 +8.6% | n/a | 已取得（cnyes 快取） |
| 營收（億 TWD） | n/a | n/a | n/a | 資料不足 |
| 毛利率 | n/a | n/a | n/a | 資料不足 |
| 營業利益率 | n/a | n/a | n/a | 資料不足 |
| 淨利率 | n/a | n/a | n/a | 資料不足 |
| ROE | n/a | n/a | n/a | 資料不足 |
| ROIC | n/a | n/a | n/a | 資料不足 |
| FCF margin | n/a | n/a | n/a | 資料不足 |
| FCF / NI | n/a | n/a | >0.9 健康 | 資料不足 |
| 淨負債（億 TWD） | n/a | n/a | n/a | 資料不足 |
| 流動比率 | n/a | n/a | n/a | 資料不足 |
| 負債權益比 | n/a | n/a | n/a | 資料不足 |
| 資本支出（億 TWD） | n/a | n/a | n/a | 資料不足 |
| 內部人淨買賣（6 個月） | n/a（空陣列，不可解讀） | n/a | n/a | 資料不足 |
| Trailing P/E | n/a | n/a | n/a | 資料不足 |
| Forward P/E | n/a | n/a | n/a | 資料不足 |
| EV/EBITDA | n/a | n/a | n/a | 資料不足 |
| P/FCF | n/a | n/a | n/a | 資料不足 |
| P/S | n/a | n/a | n/a | 資料不足 |
| 市值（億 TWD） | n/a | n/a | n/a | 資料不足 |

## Red flags
- 財報三表完全缺失，基本面無法評估，這本身就是最大風險：任何依賴本報告的下游判斷都缺乏財務依據。
- insider 與持股資料為空，無法排除內部人大量減持或籌碼集中風險。
- 單日 +8.6% 的價格變動缺乏可驗證的基本面或消息支撐，需由其他報告確認原因。
- 未取得下次財報日期，無法判斷財報前後的事件風險。
- 建議上游以其他資料源（例如公開資訊觀測站或公司 IR 公告）補充威剛的月營收與季報後，再重新執行本報告。

FUNDAMENTALS REPORT COMPLETE
