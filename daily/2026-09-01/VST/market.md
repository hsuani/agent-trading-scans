# 技術分析 — VST (Vistra Corp) 於 2026-09-01

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

由於組織代理政策限制，無法連接至 Yahoo Finance 資料服務 (query2.finance.yahoo.com, guce.yahoo.com, fc.yahoo.com 遭 403 拒絕)。

無法執行以下工具：
- `ta.py VST snapshot` — 連接失敗
- `yf.py VST fast_info` — 連接失敗

## 無法完成的分析項目

由於無法取得實時價格數據，以下技術指標無法計算：

### 快照資訊
- 現價 (Price)
- MA20 / MA50 / MA200
- RSI14
- MACD (線、信號線、直方圖)
- Bollinger Bands (中線、上下軌、%B)
- ATR14
- 52週高低點
- 交易量 (成交量、10日均量)

### 趨勢分析
無法判斷價格相對均線位置、黃金叉/死亡叉狀態。

### 動量指標
無法評估：
- MACD 柱狀圖加速度
- RSI 超買/超賣
- 1m/3m/6m/12m 報酬率

### 支撐/阻力位
無法從 `ta levels` 提取本地高低點。

### 波動率特徵
無法計算 ATR 隱含日波動幅度、年化波動率。

## 結論

無法在 2026-09-01 為 VST 提供技術分析報告。

需要：
1. 恢復對 Yahoo Finance 的網路連接
2. 檢查代理政策例外設定
3. 確認 VST 在 NYSE/NASDAQ 的上市狀態

---

MARKET REPORT INCOMPLETE — DATA UNAVAILABLE