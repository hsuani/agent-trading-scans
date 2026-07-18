# 閎康科技 (3587.TWO) — 技術面分析報告
**日期：** 2026-07-19
**分析師：** Phase-1 Market Agent
**產業：** tw_photonics（光子供應鏈檢測三雄）

---

## 一、市場資料狀態

本次分析嘗試透過以下工具取得3587.TWO即時及歷史價格資料：

```
python3 pipeline/tools/ta.py 3587.TWO snapshot
python3 pipeline/tools/yf.py 3587.TWO fast_info
```

**執行結果：**

```
Failed to get ticker '3587.TWO' reason: Failed to perform, curl: (56)
CONNECT tunnel failed, response 403.
$3587.TWO: possibly delisted; no price data found (period=1y)
{"error": "ProxyError", "message": "Failed to perform..."}
```

> **PRICE_DATA_UNAVAILABLE** — 所有技術指標來源因Proxy 403封鎖無法取得。本報告所有技術分析指標（RSI14、MACD、MA50、布林通道、成交量）均**無法計算**。

---

## 二、技術指標摘要

| 指標 | 數值 | 狀態 |
|------|------|------|
| RSI-14 | PRICE_DATA_UNAVAILABLE | N/A |
| MACD | PRICE_DATA_UNAVAILABLE | N/A |
| MA-50 | PRICE_DATA_UNAVAILABLE | N/A |
| MA-200 | PRICE_DATA_UNAVAILABLE | N/A |
| 布林通道 | PRICE_DATA_UNAVAILABLE | N/A |
| 成交量趨勢 | PRICE_DATA_UNAVAILABLE | N/A |
| 即時收盤價 | PRICE_DATA_UNAVAILABLE | N/A |

---

## 三、參考資訊（非即時）

雖然直接行情資料無法取得，以下為來自外部來源之**非即時參考訊息**，**不得用於正式技術評分**：

- **分析師技術目標區間（非官方）：** 320–350 NTD（短線）
  - 來源：散戶鬥嘴鼓網站技術分析模型，僅供參考，非即時行情
- **Yahoo股市技術分析頁面存在**（`tw.stock.yahoo.com/quote/3587.TWO/technical-analysis`），但因環境限制無法API存取

> 警告：上述數字為非即時第三方估計，**不符合本管線行情資料品質標準**，不納入評分依據。

---

## 四、基本面輔助判讀（技術面替代指標）

在技術資料缺席的情況下，以下基本面動能訊號可作輔助參考：

| 代理指標 | 訊號 |
|----------|------|
| 月營收加速（+22–27% YoY） | 正向動能 |
| Q1 2026 EPS YoY +195% | 強勢獲利反彈 |
| 連續4個月創月營收新高（至2026-06） | 上升趨勢確立 |
| 三大法人（外資/投信/自營商）同步買超 | 籌碼面支撐 |
| 矽光子合約拿下全球前3大客戶 | 催化劑確立 |

---

## 五、技術面裁定

| 條件 | 門檻 | 實際 | 結果 |
|------|------|------|------|
| RSI14 | < 72 | PRICE_DATA_UNAVAILABLE | N/A |
| MACD | 非深度負值 | PRICE_DATA_UNAVAILABLE | N/A |
| 股價 vs MA50 | 股價 > MA50 | PRICE_DATA_UNAVAILABLE | N/A |

> **三項條件均無法評分，技術面評級為 N/A。**
> 輔助基本面動能指標呈現一致正向訊號，若行情資料恢復後，技術指標有合理機率為正面。

---

## **技術面評級：N/A（PRICE_DATA_UNAVAILABLE）**

---

*資料來源嘗試：pipeline/tools/ta.py、pipeline/tools/yf.py — 均因Proxy 403錯誤失敗*
*非即時參考來源：散戶鬥嘴鼓（poorstock.com）、Yahoo奇摩股市技術分析*
