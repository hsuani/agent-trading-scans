# 技術面分析 — PANW（截至 2026-09-04）

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

技術分析工具（pipeline/tools/ta.py 及 pipeline/tools/yf.py）無法連接至 Yahoo Finance 資料源。Agent proxy 根據組織安全政策阻擋所有對以下伺服器的連線：

- query2.finance.yahoo.com
- guce.yahoo.com  
- fc.yahoo.com

所有連線嘗試返回 HTTP 403 CONNECT tunnel failed 錯誤。

## 無法獲取之資料項目

由於無法存取價格資料，以下技術指標、水位及分析項目均無法生成：

### 快照（Snapshot）
- 當前價格
- MA20、MA50、MA200
- RSI14、MACD（線值、信號線、柱狀圖）
- Bollinger Bands %B
- ATR14（每日波動含義）
- 52周高點/低點

### 技術水位（Key Levels）
- 支撐位（Support）
- 壓力位（Resistance）
- 止損建議邏輯點位

### 成交量分析（Volume）
- 最新成交量 vs 10日平均

### 動能及趨勢
- 1月/3月/6月/12月報酬率
- MACD 姿態
- 相對位置（% from MA200）
- 波動率特徵

## 結論

PANW 的技術面分析因網路限制無法完成。不生成虛構的進場/出場/停損價位。

建議：
1. 確認組織安全政策是否允許存取 Yahoo Finance
2. 配置替代數據源（如直接連線證券商 API）
3. 重新執行資料擷取

---

**市場分析報告已完成**
