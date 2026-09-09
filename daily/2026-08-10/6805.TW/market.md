# 技術分析 — 6805.TW (富世達) | 2026-08-10

## 數據狀態

**PRICE_DATA_UNAVAILABLE**

### 原因

代理閘道拒絕連接至下列資料源 (403 policy denial or upstream failure)：
- fc.yahoo.com:443 (Yahoo Finance)
- ws.api.cnyes.com:443 (鉅亨網台灣資料)

Python 工具 `ta.py` 和 `yf.py` 無法檢索 6805.TW 的即時價格、技術指標及歷史 OHLCV 數據。

### 影響範圍

無法提供以下分析：
- 當前價格、移動平均線 (MA20/MA50/MA200)
- 相對強度指數 (RSI14)、MACD、布林帶
- 支撐位/阻力位、年高/年低
- 成交量確認、波動率指標 (ATR)
- 趨勢強度評估

### 建議

- 確認網路/代理政策是否許可訪問 Taiwan TWSE 資料源
- 檢查替代數據提供商是否可用
- 待連接恢復後重新運行分析

---

MARKET ANALYSIS COMPLETE
