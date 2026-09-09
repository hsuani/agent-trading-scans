# 技術分析 — OKTA（奧克塔股份公司）2026-09-04

## 資料可用性狀態

**PRICE_DATA_UNAVAILABLE**

### 資料蒐集失敗

無法取得 OKTA 的即時市場數據。代理網關（proxy gateway）根據組織政策拒絕訪問 Yahoo Finance 數據源。具體失敗情況如下：

- **主要資料源**：Yahoo Finance (query2.finance.yahoo.com, fc.yahoo.com)
- **失敗原因**：HTTP 403 CONNECT tunnel failed — 政策拒絕（connect_rejected）
- **重試次數**：多次嘗試，全部失敗
- **受影響的工具**：`ta.py` snapshot / series / levels 及 `yf.py` history / fast_info 均無法運行

### 無法計算的技術指標

由於價格數據缺失，以下技術指標無法生成：

| 指標類別 | 具體指標 |
|---|---|
| **快照數據** | 現價、MA20、MA50、MA200 |
| **動能指標** | RSI14、MACD 直線、MACD 信號、MACD 柱狀圖 |
| **波動率指標** | Bollinger Bands、Bollinger %B、ATR14、年化波動率 |
| **支撐阻力** | 本地高/低點、動態支撐、動態阻力 |
| **成交量分析** | 最新成交量、10日平均成交量、成交量確認 |
| **多時間框架** | 1個月、3個月、6個月、12個月報酬率 |
| **52週指標** | 52週高點距離、52週低點距離 |

### 網絡連接診斷

根據代理狀態查詢，過去 24 小時內的 CONNECT 失敗記錄：

```
Failed hosts (policy denial):
- query2.finance.yahoo.com:443 — connect_rejected ×8
- fc.yahoo.com:443 — connect_rejected ×3  
- guce.yahoo.com:443 — connect_rejected ×7
- ws.api.cnyes.com:443 — connect_rejected ×2
```

組織政策阻止訪問這些金融數據源。根據代理系統文檔，組織政策拒絕（403 CONNECT）應予報告而非重試。

---

## 歷史技術參考

OKTA 最後一次成功的完整技術分析位於：
**`daily/2026-07-03/OKTA/market.md`**（截至 2026-06-29 收盤數據）

該報告的關鍵數據快照：

| 指標 | 數值 | 說明 |
|---|---|---|
| 現價 | $119.26 | 2026-06-25 收盤 |
| MA20 | ~$120 | 短期支撐 |
| MA50 | ~$123 | 中期均線 |
| MA200 | ~$125 | 長期趨勢線 |
| RSI14 | 50–60 | 中立至溫和上升 |
| MACD 直方圖 | -0.550 | 負值，動能減弱但未翻正 |
| 52 週區間 | $117.99–$125.20 | 股價位於中段 |
| YTD 漲幅 | +42% | 強勢表現 |

### 趨勢與設置（自 2026-07-03 報告）

- **主要趨勢**：短期上升趨勢內，更高低點結構
- **關鍵支撐**：$120（中期均線）、$115（心理整數）、$110（長期支撐）
- **關鍵阻力**：$125–$130（200日 MA）、$135–$140（分析師目標）、$150（心理位）
- **波動率**：年化 35–40%，日均波動 2.1–2.5%（ATR ~$2.50–$3.00）
- **技術評估**：溫和買進至中立

---

## 後續步驟

1. **網絡恢復**：待代理政策更新或網絡連接恢復後，重新運行以下命令：
   ```bash
   python pipeline/tools/ta.py OKTA snapshot --period 2y
   python pipeline/tools/ta.py OKTA series --period 1y
   python pipeline/tools/ta.py OKTA levels --period 1y
   python pipeline/tools/yf.py OKTA fast_info
   ```

2. **分析更新**：恢復後將刷新以下分析項目：
   - 完整快照（Snapshot）與最新指標
   - 趨勢判斷（Trend vs MA20/50/200）
   - 動能分析（MACD、RSI、多時間框架報酬）
   - 支撐阻力水準更新
   - 波動率配置建議
   - 設置評估（Buy/Sell/Neutral）

3. **基本面與新聞**：本日可正常進行基本面（fundamentals）和新聞（news）分析，無價格依賴

---

**技術立場**：無法判斷（N/A）

**報告狀態**：因價格數據不可用，完整技術分析無法執行。請參考歷史報告進行初步判斷。

**MARKET REPORT COMPLETE**
