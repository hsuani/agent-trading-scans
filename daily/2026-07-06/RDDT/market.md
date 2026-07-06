# 技術面分析 — RDDT 截止 2026-07-06

**⚠️ 數據可用性聲明**：因組織出口代理伺服器政策限制，無法取得 RDDT (Reddit Inc) 的即時或歷史市場數據。所有金融數據源（Yahoo Finance、Google Finance、StockAnalysis 等）均被代理伺服器阻止（HTTP 403 政策拒絕）。本次分析無法進行。

---

## 數據檢索嘗試紀錄

1. **ta RDDT snapshot --period 2y** → 失敗：ProxyError 403 (CONNECT 被拒絕)
2. **yf RDDT fast_info** → 失敗：ProxyError 403 (CONNECT 被拒絕)
3. **python3 yfinance** 直接調用 → 失敗：curl_cffi ProxyError, code 56 CONNECT tunnel failed
4. **替代數據源** (polygon.io, alpaca, 其他) → 均被同一代理伺服器阻止
5. **本地快取數據** → 不存在（RDDT 在本次掃描中尚無緩存記錄）

---

## 必要的技術指標（無法取得）

| 指標 | 狀態 | 用途 |
|---|---|---|
| RSI14 | ❌ 無法取得 | 判斷超買/超賣狀態；PASS/FAIL 條件之一 |
| MACD 直方圖 | ❌ 無法取得 | 評估動能方向；PASS/FAIL 條件之一 |
| 現價 | ❌ 無法取得 | 基礎定價 |
| MA50 | ❌ 無法取得 | 中期趨勢判斷；PASS/FAIL 條件之一 |
| MA20 / MA200 | ❌ 無法取得 | 短期/長期趨勢 |
| MACD / Signal / ATR14 | ❌ 無法取得 | 動能、波動率分析 |
| 52週高/低 | ❌ 無法取得 | 相對位置評估 |
| 成交量 | ❌ 無法取得 | 趨勢確認 |
| Bollinger Bands | ❌ 無法取得 | 過度擴張判斷 |

---

## RDDT 背景（已知信息）

- **上市日期**：2024年3月
- **現狀**：IPO 後上市逾 15 個月，歷經高波動期
- **行業**：社群媒體 / 內容平台
- **特徵**：波動性高，適合技術面交易

---

## PASS/FAIL 條件（無法評估）

根據任務要求，分析需滿足以下條件：

```
PASS 條件：
  • RSI14 < 72 [無法驗證 — 數據缺失]
  • MACD 非深度負值 [無法驗證 — 數據缺失]
  • 價格 > MA50 [無法驗證 — 數據缺失]

若以上三項均滿足 → PASS
否則 → FAIL
```

**當前狀態**：無法評估任何條件，因全部必要輸入數據皆缺失。

---

## 解決方案

### 短期
1. **要求組織允許** Yahoo Finance / finance.yahoo.com 在出口代理伺服器上的訪問
2. **配置替代數據來源**（如 polygon.io 免費層、Alpha Vantage 免費層），確保代理伺服器允許訪問
3. **使用本地/共享緩存**：若存在組織內部的實時/日結行情數據存儲，直接使用而非依賴外部 API

### 長期
- 在 `pipeline/tools/requirements.txt` 中添加備用數據提供商
- 實現多數據源容錯機制（yfinance 作主，備用提供商作備選）
- 在 ta.py / yf.py 中添加離線模式或 mock 數據支持

---

## 技術架構說明

Pipeline 依賴鏈：
```
market-analyst.md (本報告)
  ↓
pipeline/tools/ta.py (技術指標計算)
  ↓
yfinance (市場數據源)
  ↓
finance.yahoo.com (被代理伺服器阻止 403)
```

**阻點**：finance.yahoo.com 連接在代理伺服器出口層被拒絕。

---

## 結論

**PASS/FAIL 評估結果**：

```
FAIL — 因數據不可取得，無法進行技術分析
```

- **RSI14**：[數據缺失]
- **MACD 直方圖**：[數據缺失]
- **價格 vs MA50**：[數據缺失]

**建議下一步**：
1. 確認組織代理伺服器政策是否可調整
2. 評估替代數據源的可行性
3. 如可取得 RDDT 數據，重新運行本分析

---

**MARKET REPORT COMPLETE**

報告日期：2026-07-06  
數據截止：無可用數據  
分析結果：不可進行，待數據源可用  
阻塞原因：組織出口代理伺服器策略拒絕（HTTP 403） 至所有金融數據端點
