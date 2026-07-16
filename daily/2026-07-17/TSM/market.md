# 技術面分析 — TSM (台積電) 截至 2026-07-17

## PRICE_DATA_UNAVAILABLE

**資料狀態**: 無法取得即時價格數據

由於代理層政策限制，無法存取 Yahoo Finance (fc.yahoo.com) 及鉅亨網 API。代理回應 HTTP 403 (policy denial)，導致無法獲取以下數據來源:
- fc.yahoo.com (Yahoo Finance 價格/指標)
- ws.api.cnyes.com (鉅亨網實時報價)

**無法生成技術指標**: 
- 快照數據 (價格、MA20/50/200、MACD、RSI14、BB%、ATR14)
- 支撐/阻力級別
- 動能指標 (1m/3m/6m/12m 報酬率)
- 波動率指標 (20d annualized vol)
- 52 週高點/低點

## 建議的替代方案

1. **檢查代理設置**: 確認防火牆/代理政策是否允許存取 Yahoo Finance
2. **使用替代數據源**: 
   - 台灣股市官方 API (TWSE - 台灣證券交易所)
   - 其他金融數據提供商 (Bloomberg, Refinitiv 等)
3. **人工驗證**: 通過經紀商平台直接查詢 TSM 即時報價

---

**MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE**

報告無法完成。請在取得實時價格數據後重新運行技術分析。
