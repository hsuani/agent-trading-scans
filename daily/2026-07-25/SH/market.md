# 技術分析 — SH 截至 2026-07-25

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得技術分析數據。組織網路政策阻止連接至 Yahoo Finance 資料來源（fc.yahoo.com, ws.api.cnyes.com）。

## 原因

- API 呼叫層級：代理伺服器返回 403 CONNECT 拒絕
- 受影響的主機：
  - fc.yahoo.com:443（Yahoo Finance）
  - ws.api.cnyes.com:443（另一金融資料源）
- 狀態：組織政策性阻擋，無法迴避

## 無法提供的分析

由於缺乏價格資料，以下指標無法計算：
- 快照（Snapshot）：價格、MA20、MA50、MA200、RSI14、MACD
- 趨勢分析（Trend）
- 動能指標（Momentum）：MACD 柱狀圖、RSI 水位、多期間報酬率
- 關鍵水位（Key Levels）：支撐、阻力、52 週高低點
- 波動率概況（Volatility Profile）：ATR、年化波動率
- 布林帶（Bollinger Bands）%B 指標

## 建議

請聯絡網路管理員以調整網路政策，允許存取 Yahoo Finance 資料來源，以便進行後續技術分析。

---

**市場報告無法完成** — 資料可用性受限

