# 技術面 — ETN（伊頓公司）截至 2026-09-08

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法獲取 ETN 的市場資料。代理伺服器政策阻止訪問 Yahoo Finance 資料源（fc.yahoo.com、query2.finance.yahoo.com 等網域返回 HTTP 403）。

## 資料取得嘗試

- `ta ETN snapshot --period 2y`：失敗 — 無歷史數據
- `yf ETN fast_info`：未嘗試（初始請求已失敗）

## 分析報告

無法執行技術分析。缺少以下資訊：

- 當日價格
- 移動平均線（MA20、MA50、MA200）
- 相對強度指數（RSI14）
- MACD 指標
- 布林帶指標
- ATR 波動率
- 支撐與阻力位
- 成交量數據

## 建議行動

1. 確認 Yahoo Finance 資料源的網路連接
2. 替代資料源驗證
3. 後續重新嘗試資料擷取

---

**市場報告完成**

```
生成時間: 2026-09-08
資料狀態: PRICE_DATA_UNAVAILABLE
代理連接: 被組織政策阻止
```
