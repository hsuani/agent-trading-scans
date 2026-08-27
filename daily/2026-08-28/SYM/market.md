# 技術分析 — SYM 截至 2026-08-28

## 快照 (Snapshot)

**狀態：PRICE_DATA_UNAVAILABLE**

由於代理伺服器 HTTP 403 政策阻擋，無法從 yfinance 獲取即時價格數據。所有價格衍生指標均無法計算。

| 指標 | 數值 | 備註 |
|---|---|---|
| 最新價格 | PRICE_DATA_UNAVAILABLE | 代理無法連接 yfinance |
| MA20 | PRICE_DATA_UNAVAILABLE | — |
| MA50 | PRICE_DATA_UNAVAILABLE | — |
| MA200 | PRICE_DATA_UNAVAILABLE | — |
| RSI14 | PRICE_DATA_UNAVAILABLE | — |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | — |
| 布林帶 %B | PRICE_DATA_UNAVAILABLE | — |
| ATR14 | PRICE_DATA_UNAVAILABLE | — |
| 52 週高點 | PRICE_DATA_UNAVAILABLE | — |
| 52 週低點 | PRICE_DATA_UNAVAILABLE | — |

## 趨勢 (Trend)

無法分析。技術數據缺失，無法評估价格相對移動平均線的位置、黃金交叉/死亡交叉接近程度或趨勢強度。

## 動能 (Momentum)

無法分析。缺少 MACD、RSI 和多期間動能數據：
- 1 個月動能：PRICE_DATA_UNAVAILABLE
- 3 個月動能：PRICE_DATA_UNAVAILABLE
- 6 個月動能：PRICE_DATA_UNAVAILABLE
- 12 個月動能：PRICE_DATA_UNAVAILABLE

## 關鍵水位 (Key Levels)

無法識別。支撑位及阻力位的計算依賴於至少 120 根 K 棒的歷史數據。

- **阻力位**：PRICE_DATA_UNAVAILABLE
- **支撑位**：PRICE_DATA_UNAVAILABLE
- **止損建議**：PRICE_DATA_UNAVAILABLE

## 波動率特徵 (Volatility Profile)

無法計算。ATR14 及 20 天年化波動率依賴完整價格序列。

- 預期日振幅：PRICE_DATA_UNAVAILABLE
- 年化波動率：PRICE_DATA_UNAVAILABLE

## 技術設置 (Setup)

無法評估。缺少所有必要的價格數據和指標，無法判斷是否形成看漲/看跌/中性的技術形態。

## 指標表

| 指標 | 數值 | 解讀 |
|---|---|---|
| RSI14 | PRICE_DATA_UNAVAILABLE | 無法判斷超買/超賣 |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | 無法判斷動能 |
| 相對 MA200 % | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 布林帶 %B | PRICE_DATA_UNAVAILABLE | 無法判斷超買/超賣 |
| 1 月動能 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 3 月動能 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 6 月動能 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 12 月動能 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| ATR14 | PRICE_DATA_UNAVAILABLE | 無法計算 |
| 年化波動率 | PRICE_DATA_UNAVAILABLE | 無法計算 |

## 結論

**SYM 技術分析無法進行**。yfinance 數據來源因代理伺服器 HTTP 403 政策限制而不可用。未獲得實時價格數據前，所有技術指標、支撑/阻力水位及動能分析均無法生成。建議在解決代理連接問題後重新執行分析。

---

**市場報告完成** | 生成時間：2026-08-27 | 數據狀態：不可用
