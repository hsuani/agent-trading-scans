# 技術分析 — 2382.TW（廣達電腦）2026-07-23

## 狀態：PRICE_DATA_UNAVAILABLE

**無即時價格，技術分析無法執行**

### 原因
Proxy 阻斷（403 error on fc.yahoo.com），yfinance/ta.py 工具無法連接。

---

## 影響範圍

由於無法取得即時價格數據，以下分析項目**無法執行**：

- ✗ 快照資料（Snapshot）：當前價格、MA20、MA50、MA200
- ✗ 趨勢分析（Trend）：價格相對移動平均線的位置
- ✗ 動能指標（Momentum）：MACD、RSI14、超買/超賣條件
- ✗ 關鍵支撐阻力位（Key Levels）：本地高點/低點、支撐位、阻力位
- ✗ 波動率分析（Volatility Profile）：ATR14、年化波動率
- ✗ 技術指標表（Indicators Table）：所有定量指標

---

## 重要提示（下游工作流程）

**交易員（Trader）與投資組合管理者（Portfolio Manager）必須注意：**

本報告**無虛構數據**。請勿基於此報告進行：
- 入場價格（Entry Price）設定
- 停損位（Stop-Loss）設定
- 獲利目標（Target Price）設定
- 部位規模（Position Sizing）決策

所有決策必須等待價格數據恢復後，由技術分析提供有效指標。

---

## 後續步驟

1. 確認 Proxy 連接恢復
2. 重新執行 `ta 2382.TW snapshot --period 2y` 與 `ta 2382.TW series --period 1y`
3. 確認數據可用後重新生成技術分析報告

---

**報告日期：** 2026-07-23  
**技術分析狀態：** 無法執行（Data Blocked）  
**上次更新：** N/A（無數據）

MARKET REPORT INCOMPLETE — PRICE DATA UNAVAILABLE
