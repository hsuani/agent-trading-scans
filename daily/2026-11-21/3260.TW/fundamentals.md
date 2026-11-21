## 3260.TW 威剛 基本面報告 (as of 2026-11-21) — DATA_UNAVAILABLE

狀態: DATA_UNAVAILABLE。基本面資料無法取得，本報告不含任何估值或財務比率數字。

### 查詢紀錄
- 執行過的工具: `pipeline/tools/yf 3260.TW` 的 info, fast_info, financials, quarterly_fin, balance_sheet, quarterly_bs, cashflow, quarterly_cf, earnings_dates, insider, major_holders, inst_holders，共 12 項，並於 20 秒後重試 info, financials, earnings_dates。
- 結果:
  - info: 只回傳 `trailingPegRatio: null`，其餘欄位皆缺。
  - financials, quarterly_fin, balance_sheet, quarterly_bs, cashflow, quarterly_cf, insider, major_holders, inst_holders: 回傳空陣列 `[]`。
  - earnings_dates: 回傳 `ConnectionError`，原因是 `CONNECT tunnel failed, response 403`。
  - Yahoo cookie/crumb 取得失敗 (ConnectionError)，屬於代理層 403 拒絕。
- 工具輸出中有 "possibly delisted; no price data found" 字樣，但這是抓取失敗的連帶訊息，並非確認下市，不應作為下市判斷依據。

### 唯一可用資料 (fast_info, feed: cnyes, source: cache, cached_at 2026-11-21T14:32:37Z)
| 項目 | 數值 | 單位 |
|---|---|---|
| 最新價 (last_price) | 235.5 | TWD |
| 前收 (previous_close) | 254.0 | TWD |
| 日高 / 日低 | 250.0 / 232.5 | TWD |
| 當日漲跌幅 (由上述兩價計算) | 約 -7.3% | % |
| 50日 / 200日均線 | n/a | TWD |
| 52週高 / 低 | n/a (NaN) | TWD |
| 市值, 股數, 成交量 | n/a | — |

此價格資料為 cache，時間戳與分析日同為 2026-11-21，未發現晚於 2026-11-21 的資料。

### 缺漏項目 (全部 n/a，未推算)
- 營收與 3-5 年 CAGR、毛利 / 營業利益 / 淨利率趨勢、ROE、ROIC
- FCF、FCF/NI、經營現金流、資本支出、庫藏股與股利
- 淨負債、流動比率、負債權益比、現金部位
- 內部人交易 (近 6 個月)、大股東與法人持股
- P/E、forward P/E、EV/EBITDA、P/FCF、P/S 及產業中位數比較
- 下次財報日、EPS 驚喜歷史、近期法說指引

### 對下游的提示
- 基本面無法評估財務健全度與估值吸引力，不應以本報告推論基本面方向。
- 交易員若需要基本面依據，請等 yfinance 恢復後重跑本分析，或改用 TWSE / MOPS 公開資訊觀測站資料 (本次未查詢)。
- 價格面僅見單日 -7.3% 的急跌 (前收 254.0 → 235.5)，其成因 (財報、產業、指數或其他) 本報告無法判定。

FUNDAMENTALS REPORT COMPLETE (DATA_UNAVAILABLE)
