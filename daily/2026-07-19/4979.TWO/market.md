# 技術分析報告 — 華星光通 (4979.TWO)
**日期：** 2026-07-19
**分析師：** 市場技術分析師 (Phase 1)
**產業：** tw_photonics / CPO 光通訊中游光模組

---

## 一、價格數據取得狀態

```
[PRICE_DATA_UNAVAILABLE]
```

**嘗試來源：**
- `pipeline/tools/ta.py 4979.TWO snapshot` → HTTP 403 / 連線失敗（代理伺服器阻斷）
- `pipeline/tools/yf.py 4979.TWO fast_info` → HTTP 403 / ProxyError

兩個數據來源均回傳 **403 CONNECT tunnel failed**，無法取得即時或近期歷史價格數據。根據本報告協定，所有技術指標一律標示為 **PRICE_DATA_UNAVAILABLE**，不得推算或捏造數值。

---

## 二、技術指標狀態

| 技術指標 | 數值 | 狀態 |
|---|---|---|
| 收盤價 | PRICE_DATA_UNAVAILABLE | — |
| MA50（50 日均線）| PRICE_DATA_UNAVAILABLE | — |
| RSI14（14 日相對強弱指數）| PRICE_DATA_UNAVAILABLE | — |
| MACD | PRICE_DATA_UNAVAILABLE | — |
| 布林通道（Bollinger Bands）| PRICE_DATA_UNAVAILABLE | — |
| 成交量趨勢 | PRICE_DATA_UNAVAILABLE | — |
| 支撐 / 壓力位 | PRICE_DATA_UNAVAILABLE | — |

---

## 三、補充資訊（非技術分析）

雖無法取得即時技術指標，以下為來自公開網路搜尋的補充價格參考（**非本報告之正式評分依據**）：

- 某財經文章（2026 年第二季）提及股價約 **NT$588 元**，惟此價格之時間點及來源無法驗證，不納入通過/失敗判定。
- 外資持續買超（連續 5 買 as of 2026/04/29）隱含中短期技術面有一定支撐，但此為籌碼面資訊，非技術面確認。

---

## 四、通過標準

**Pass 條件：** RSI14 < 72 AND MACD not deeply negative AND price > MA50

由於無法取得任何技術指標數值，**無法評估是否通過**。

---

## 五、判決

**VERDICT: N/A（PRICE_DATA_UNAVAILABLE）**

**理由：**
數據來源 ta.py 及 yf.py 均因代理伺服器阻斷（HTTP 403）而無法取得 4979.TWO 之任何價格資料。本報告依協定標示為 **N/A**，不視為 FAIL，亦不計入正向分數。

**後續建議：**
- 改用台灣本地數據源（如 MIS.TWSE 或 TPEX API）重新查詢
- 或於網路環境許可時重執行技術分析

---

*資料來源：pipeline/tools/ta.py, pipeline/tools/yf.py（均返回 403 錯誤）*
*本報告係基於截至 2026-07-19 可取得之公開資訊撰寫*
