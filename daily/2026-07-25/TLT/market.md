# 技術面 — TLT 於 2026-07-25

## 數據不可用

**PRICE_DATA_UNAVAILABLE**

由於組織網路政策限制，無法連接至 Yahoo Finance API (`fc.yahoo.com`)，導致無法取得 TLT 價格數據。代理服務器已拒絕所有連往該主機的連接 (403 政策拒絕)。

## 診斷

- 工具: `ta.py` 及 `yf.py`
- 狀態: 連接被拒
- 錯誤: curl: (56) CONNECT tunnel failed, response 403
- 原因: 組織 egress 政策 - fc.yahoo.com:443 被封鎖
- 時間戳: 2026-07-24T17:51:20Z 至 2026-07-24T17:51:42Z (多次重試)

## 無法執行的分析項目

下列技術面分析無法進行，因為缺乏必要的價格數據：

- 現價及 52 週區間
- MACD (訊號線、直方圖趨勢)
- RSI-14 (超買/超賣狀態)
- 移動平均線: MA20、MA50、MA200 與價格關係
- 布林帶 (Bollinger Bands)
- 成交量趨勢
- 支撐/阻力位
- 利率敏感度分析
- 債券收益率與 TLT 價格圖表關係

## 建議

需要解除對 `fc.yahoo.com:443` 的網路政策限制，或使用替代數據源 (如 Alpha Vantage、IEX Cloud 等)，方可進行 TLT 的技術分析。

---

**MARKET REPORT INCOMPLETE — PROXY POLICY DENIAL**
