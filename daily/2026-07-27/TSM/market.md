# 技術分析 — TSM 截至 2026-07-27

## 狀態

**PRICE_DATA_UNAVAILABLE**

## 資料蒐集失敗說明

無法取得 TSM 的價格資料及技術指標。

### 失敗原因

代理伺服器（proxy gateway）拒絕連接至以下資料來源：
- **fc.yahoo.com:443** - 政策拒絕（policy denial）
- **ws.api.cnyes.com:443** - 政策拒絕

資料工具已執行多次重試（最少 3 次），所有連接均遭代理政策攔截，回傳 403 錯誤。

### 嘗試之工具

1. `ta TSM snapshot --period 2y` - 失敗
2. `ta TSM levels --period 1y` - 失敗  
3. `yf TSM fast_info` - 失敗

### 結論

無基礎價格資料可用，因此無法執行以下分析：
- 快照（price, MA20, MA50, MA200, RSI14, MACD）
- 趨勢判斷（上升、下降、盤整）
- 動能指標（MACD、RSI、多期間報酬）
- 關鍵技術水位（支撑、阻力）
- 波動率檔案（ATR、年化波動率）
- 交易設置評估

---

**技術報告無法完成**

MARKET REPORT INCOMPLETE — PRICE_DATA_UNAVAILABLE
