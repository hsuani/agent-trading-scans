# UUP 市場報告 — 2026-08-29

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

## 問題說明

無法取得 UUP (Invesco DB US Dollar Index Bullish Fund) 的即時價格和技術指標數據。

### 根本原因

組織網路政策已封鎖對 Yahoo Finance 域名的訪問：
- guce.yahoo.com
- query2.finance.yahoo.com  
- fc.yahoo.com

所有數據檢索嘗試（`ta snapshot`、`yf fast_info`、`ta levels`、`ta series`）均因代理閘道返回 HTTP 403（政策拒絕）而失敗。

### 技術細節

- 代理狀態：已啟用
- 近期中繼故障：20+ 次 CONNECT 連線被拒
- 故障類型：gateway answered 403 to CONNECT (policy denial or upstream failure)

## 技術分析無法進行

由於無法訪問基礎市場數據，以下分析無法執行：

- MACD、RSI14 等技術指標計算
- MA50/MA200 移動平均線分析
- Bollinger Bands 布林帶評估
- 支撐/阻力水位級別識別
- 成交量確認檢驗
- 動能和波動率評估

## 建議行動

1. 聯絡網絡管理員申請豁免 Yahoo Finance 域名訪問
2. 探索替代數據源（如 IEX、Alpha Vantage、Finnhub 等）
3. 確認 UUP ETF 是否仍在活躍交易（檢查上市狀態）

---

**Phase-1 Market Signal: DATA_UNAVAILABLE**
