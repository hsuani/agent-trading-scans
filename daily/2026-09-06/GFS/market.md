# 技術分析 — GFS (GlobalFoundries) 截至 2026-09-06

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 GFS 的價格數據。通過 Yahoo Finance 的所有連線嘗試均遭組織代理政策阻止 (403 CONNECT rejection)。代理拒絕連線至以下域名：
- query2.finance.yahoo.com:443
- guce.yahoo.com:443
- fc.yahoo.com:443

此情況影響以下無法執行的分析：
- 實時價格與移動平均線 (MA20/MA50/MA200) 對比
- RSI14、MACD 直方圖與信號線
- Bollinger Bands 位置分析
- 支持/阻力位分析
- 成交量確認
- 動量多期間回報率 (1m/3m/6m/12m)
- ATR 與波動率分析

## 建議後續動作

1. 驗證組織網路政策是否允許 Yahoo Finance 數據訪問
2. 考慮使用替代數據來源 (如本地市場數據、付費 API)
3. 確認 GFS 股票代碼是否正確及上市狀態

---

**MARKET REPORT INCOMPLETE** — 無可用價格數據
