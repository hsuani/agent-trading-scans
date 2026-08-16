# NEE 基本面分析報告 — 2026-08-11

## PRICE_DATA_UNAVAILABLE

**原因**: 代理政策拒絕存取 fc.yahoo.com:443 及備用金融資料 API。  
Yahoo Finance、IEX Cloud 等外部財務資料來源均被組織出站政策封禁（HTTP 403）。

**無法取得的指標**: 營收成長 YoY、FCF、FCF/NI、Forward P/E、EV/EBITDA、資產負債表、內部人士交易。

下游 Trader / Portfolio Manager 不得捏造進出場價位，最終決策須標記「無即時財務資料，暫不給進出場價位」。

| 指標 | 值 |
|------|-----|
| 資料可用性 | UNAVAILABLE |
| 原因 | 代理政策封鎖 |
