# 技術分析 — GLD (2026-07-25)

## 價格數據狀態

**PRICE_DATA_UNAVAILABLE**

無法檢索 GLD (SPDR 黃金股票 ETF) 的價格數據。代理代理對 Yahoo Finance (fc.yahoo.com) 的連接被網關政策阻止 (403 政策拒絕)。

### 詳細資訊

- **命令執行結果**: 無法連接到數據源
- **嘗試次數**: 3 次重試（均失敗）
- **根本原因**: 代理級 403 連接被拒絕 — 上游網關政策限制
- **受影響的工具**: 
  - `python3 pipeline/tools/ta.py GLD snapshot`
  - `python3 pipeline/tools/yf.py GLD fast_info`

### 無法提供的指標

由於數據不可用，無法產生以下技術分析：

- RSI14 — 相對強弱指數
- MACD — 移動平均收斂散度
- MA20/MA50/MA200 — 移動平均線
- Bollinger Bands — 布林帶
- ATR14 — 真實波幅
- 動能指標 — 多時間框架回報
- 支撐/阻力位 — 本地極值
- 波動率配置文件 — ATR 和年化波動率

### 建議

請解決代理連接問題或等待網關政策更新以重新啟用對 Yahoo Finance 的訪問。

---

**MARKET REPORT COMPLETE**
