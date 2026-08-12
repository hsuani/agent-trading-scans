# 技術分析 — 2382.TW (廣達電腦) 截至 2026-08-13

## 資料可用性

**PRICE_DATA_UNAVAILABLE**

### 狀態說明

無法取得 2382.TW 的價格數據。代理伺服器目前阻止對 Yahoo Finance (fc.yahoo.com:443) 的連線，所有資料拉取均傳回 CONNECT tunnel 403 policy denial。

### 嘗試過的方法
- `ta.py 2382.TW snapshot` — 失敗，無歷史數據
- `yf.py 2382.TW fast_info` — 失敗，proxy 政策拒絕
- 重試等待 — 仍然被阻止

### 無法進行的分析
由於缺少即時價格數據，以下分析均無法進行：
- 移動平均線 (MA20, MA50, MA200) 對比
- RSI14、MACD、Bollinger Bands 等指標
- 支撐/阻力位識別
- 波動率計算
- 技術形態評估

### 建議後續行動
- 檢查代理伺服器政策設定
- 確認 Yahoo Finance API 連線是否恢復
- 確認 2382.TW 在 Yahoo Finance 上是否仍有有效報價

---

## 最終評估

**PRICE_DATA_UNAVAILABLE**

無法取得必要的市場數據來完成技術分析。
