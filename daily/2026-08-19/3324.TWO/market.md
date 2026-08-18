# 技術分析 — 3324.TWO (雙鴻科技) 截至 2026-08-19

## 狀態

**PRICE_DATA_UNAVAILABLE**

無法取得即時價格數據。yfinance 連接被代理阻止 (fc.yahoo.com 回應 403 Policy denial)。根據價格數據完整性規則，在缺乏真實市場數據的情況下，不應推斷或編造任何技術水位、RSI 值或關鍵支撐阻力位。

### 連接問題詳情

- **錯誤**: CONNECT tunnel failed, response 403 (gateway policy denial)
- **影響的主機**: fc.yahoo.com:443
- **工具**: yfinance / pipeline/tools/ta.py
- **重試次數**: 5 次嘗試 (1.5s ~ 7.5s backoff)
- **替代 ticker 格式**: 3324.TWO、3324.TW 均失敗

### 尋求解決方案

請確認：
1. 代理策略是否允許 Yahoo Finance 存取
2. 是否有替代數據源可用 (例如本地股票數據服務、或更新代理例外清單)
3. 連接恢復後重新執行掃描

---

## Phase 1 評分表

| 標準 | 結果 |
|------|------|
| RSI14 < 72 | ❌ PRICE_DATA_UNAVAILABLE |
| MACD 未嚴重負值 | ❌ N/A (無數據) |
| 價格 > MA50 | ❌ N/A (無數據) |
| **技術面總評** | **❌ PRICE_DATA_UNAVAILABLE** |

---

## 結論

3324.TWO 無法進行技術分析。建議待連接恢復後重新掃描。

