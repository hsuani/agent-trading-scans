# 技術分析 — TLT 截至 2026-07-25

## PRICE_DATA_UNAVAILABLE

### 狀況說明
無法取得 TLT (iShares 20+ Year Treasury Bond ETF) 的價格數據。

**失敗原因**: 代理伺服器阻止連線至 Yahoo Finance (fc.yahoo.com)，已多次重試。
- 錯誤類型: CONNECT tunnel failed (403 Policy Denial)
- 工具: `ta.py` 與 `yf.py` 均無法檢索歷史資料

### 無法提供的指標
由於缺乏價格數據，以下指標無法計算:
- MACD (Moving Average Convergence Divergence)
- RSI14 (Relative Strength Index)
- MA20 / MA50 / MA200 (移動平均線)
- Bollinger Bands (布林通道)
- ATR14 (平均真實波幅)
- 動量指標 (多時間框架收益率)
- 支撐/阻力位 (local highs/lows)
- 波動率 (annualized volatility)

### 建議行動
- 檢查網路連接與代理設定
- 確認 Yahoo Finance 服務可用性
- 稍後重試數據擷取

---

**報告生成時間**: 2026-07-25  
**資料來源**: yfinance (不可用)

MARKET REPORT COMPLETE
