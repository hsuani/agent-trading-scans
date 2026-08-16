# 技術分析 — POET (2026-08-16)

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

由於網路限制，無法存取 yfinance/Yahoo Finance，因此無法取得 POET 的實時價格資料。本報告無法提供價格層級、技術指標值或市場分析。

## 資料限制說明

以下技術指標無法計算：

- **價格與移動平均線**：MA20, MA50, MA200 - PRICE_DATA_UNAVAILABLE
- **動量指標**：MACD (線、信號線、直方圖) - PRICE_DATA_UNAVAILABLE
- **超買/超賣**：RSI14, Bollinger Bands %B - PRICE_DATA_UNAVAILABLE
- **波動率**：ATR14, 20日年化波動率 - PRICE_DATA_UNAVAILABLE
- **支撐/阻力位**：本地高點/低點 - PRICE_DATA_UNAVAILABLE
- **52週高點/低點**：與當前價格距離 - PRICE_DATA_UNAVAILABLE
- **成交量確認**：最新成交量 vs 10日平均 - PRICE_DATA_UNAVAILABLE

## 通常分析內容（無法執行）

若能取得價格資料，技術分析將評估：

### 趨勢分析
- 價格相對於短期 (MA20)、中期 (MA50)、長期 (MA200) 移動平均線的位置
- 上漲/下跌/盤整的強度與方向
- 黃金交叉 (Golden Cross) 或死亡交叉 (Death Cross) 的接近程度

### 動量分析
- MACD 線與信號線的交叉信號
- MACD 直方圖的加速或減速
- 1個月/3個月/6個月/12個月報酬率的多時間框架動量

### 關鍵位置
- 最近的支撐位與阻力位 (基於本地高點/低點)
- 與52週高點/低點的距離
- 建議止損位置 (邏輯性止損，非投資建議)

### 波動率狀況
- ATR14 暗示的每日波動幅度
- 年化波動率百分比
- 對頭寸規模的影響

### 設置評估
- 多頭/空頭/中性的整體傾向
- 技術形態 (如更高的高點、破裂支撐、區間波動)

## 指標表格（無法完成）

| 指標 | 數值 | 解讀 |
|---|---|---|
| RSI14 | PRICE_DATA_UNAVAILABLE | — |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | — |
| MA200 偏差百分比 | PRICE_DATA_UNAVAILABLE | — |
| BB %B | PRICE_DATA_UNAVAILABLE | — |
| ATR14 | PRICE_DATA_UNAVAILABLE | — |
| 年化波動率 | PRICE_DATA_UNAVAILABLE | — |

## 報告階段

**Phase-1-Only** - 由於價格資料不可用，此報告無法進行技術分析。待網路連接恢復後，應重新執行完整掃描。

---

**市場報告狀態**：INCOMPLETE - PRICE_DATA_UNAVAILABLE
**生成時間**：2026-08-16
