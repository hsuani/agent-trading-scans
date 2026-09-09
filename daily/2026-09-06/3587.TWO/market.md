# 技術分析 — 3587.TWO 截至 2026-09-06

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

### 錯誤說明

無法取得 3587.TWO (閎康科技) 的即時價格數據。

- **ta.py snapshot** 命令：HTTP 403 連接被拒 (agent proxy policy)
- **yf.py fast_info** 命令：HTTP 403 連接被拒 (agent proxy policy)
- 目標伺服器：query2.finance.yahoo.com, guce.yahoo.com, fc.yahoo.com
- 根本原因：Agent proxy 組織政策限制對這些 Yahoo Finance 端點的出站連接

### 影響範圍

由於無法存取價格數據，以下指標無法計算：

| 指標 | 狀態 |
|---|---|
| 現價 | 無法取得 |
| MA20 / MA50 / MA200 | 無法計算 |
| RSI14 | 無法計算 |
| MACD (線 / 信號 / 直方圖) | 無法計算 |
| ATR14 | 無法計算 |
| Bollinger Bands %B | 無法計算 |
| 支撐 / 阻力位 | 無法識別 |
| 年化波動率 | 無法計算 |
| 過去 1m/3m/6m/12m 報酬 | 無法計算 |

## 市場信號

**FAIL** — 資料不可用

無法進行技術面分析。建議：

1. 確認 agent proxy 設定與組織政策
2. 檢查 Yahoo Finance 替代數據源的可用性
3. 嘗試其他市場數據提供者 (Bloomberg, CapitalIQ, 台股官方接口)
4. 確認 3587.TWO 是否仍在 Taiwan TPEx 上市 (可能已除牌)

---

**分析完成時刻**：2026-09-06  
**資料完整性**：0%  
**MARKET REPORT INCOMPLETE — DATA UNAVAILABLE**
