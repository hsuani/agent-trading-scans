# 技術分析 — VST (2026-07-28)

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得技術分析所需的價格資料。代理伺服器透過網關政策阻止對 Yahoo Finance (fc.yahoo.com) 的連線，導致無法檢索 VST 的OHLCV 資料和技術指標。

### 嘗試詳情
- 工具：`ta.py snapshot` (2年週期) — 失敗
- 工具：`ta.py series` (1年週期) — 失敗  
- 工具：`ta.py levels` (1年週期) — 失敗
- 工具：`yf.py fast_info` — 失敗

### 網關狀態
- 來源主機：fc.yahoo.com:443
- 回應代碼：403 (政策拒絕或上游故障)
- 錯誤類型：CONNECT tunnel failed (curl error 56)

## 必要指標 - 無法計算

無法進行以下技術分析：

| 指標 | 狀態 |
|---|---|
| 現價 (Price) | N/A |
| MA20 / MA50 / MA200 | N/A |
| RSI14 | N/A |
| MACD (线/信号/柱状图) | N/A |
| Bollinger Bands (%B) | N/A |
| ATR14 | N/A |
| 動量 (多時域報酬) | N/A |
| 支撐/阻力位 | N/A |
| 成交量分析 | N/A |

## 結論

無法完成 VST 的技術分析報告。建議在網路連接恢復後重新執行此分析。

---

技術報告無法完成 — PRICE_DATA_UNAVAILABLE
