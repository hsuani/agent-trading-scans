# Technical — SOI as of 2026-11-23

## 狀態
**PRICE_DATA_UNAVAILABLE**

本次無法取得 SOI 的任何可用價格資料，因此未產出任何價位、均線、指標數值或支撐壓力位。依規定不以推測值補足。

## 資料來源檢查
- `pipeline/tools/ta SOI snapshot --period 2y`：失敗，`no history for SOI`（yfinance 連線遭 proxy 以 403 拒絕，CONNECT tunnel failed）。
- `pipeline/tools/ta SOI levels --period 1y`、`series --period 1y`：同樣失敗，原因相同。
- `pipeline/tools/yf SOI fast_info`：回傳全部為 null（last_price、50d/200d MA、52w 高低點、成交量皆無）。
- 本地快取 `prices/yf/SOI.json`：僅含 metadata，`quoteType` 為 `NONE`，無任何 OHLCV 歷史。
- 本地快取 `prices/quotes.json`：不含 SOI 欄位。
- `prices/*.csv` 與 `daily/` 內其他檔案：未發現 SOI 價格序列。repo 中出現 "SOI" 字樣的檔案（如 `serenity/` 下的社群情緒與策略文字）皆為文字提及，不含可用價格。
- 注意：請求日期 2026-11-23 晚於目前系統日期 2026-11-22，即使資料源可用，當日收盤資料也尚未產生。

## 無法計算的項目
| 項目 | 狀態 |
|---|---|
| 價格、MA20 / MA50 / MA200 | 無資料 |
| RSI14 | 無資料 |
| MACD / 訊號線 / 柱狀體 | 無資料 |
| BB %B、布林上下軌 | 無資料 |
| ATR14、20 日年化波動率 | 無資料 |
| 1m / 3m / 6m / 12m 報酬 | 無資料 |
| 支撐 / 壓力位（local min/max） | 無資料 |
| 52 週高低點 | 無資料 |
| 成交量 vs 10 日均量 | 無資料 |
| 停損建議 | 無法提供（無價位基準） |

## 趨勢、動能、型態
無法判讀。沒有價格序列，無法判定上升、下降或盤整，也無法評估動能、型態（如高低點結構、跌破支撐）或量能確認。

## 建議後續動作
1. 恢復 yfinance 或 cnyes 等價格來源的連線後，重新執行 `pipeline/tools/ta SOI snapshot --period 2y`。
2. 或確認 SOI 的正確代碼與交易所（目前 repo 內 `prices/yf/SOI.json` 顯示 quoteType 為 NONE，代碼可能不在目前的價格來源涵蓋範圍內）。
3. 於當日收盤後（2026-11-23 之後）再執行本分析，以取得該日資料。

## 結論
本次技術面分析無法完成。在取得可驗證的 SOI 價格資料前，不提供趨勢判斷、指標讀數或交易價位。

MARKET REPORT COMPLETE
