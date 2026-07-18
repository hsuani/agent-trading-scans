# 上詮光電 (3363.TWO) — 技術面分析報告
**日期：** 2026-07-19
**分析師：** 市場技術研究模組 (Phase-1)
**產業：** tw_photonics｜CPO 光通訊中游 — FAU 精密對準組件

---

## 一、價格資料狀態

```
PRICE_DATA_UNAVAILABLE
```

**說明：**
- 執行 `pipeline/tools/ta.py 3363.TWO snapshot` → **HTTP 403（CONNECT tunnel failed）**
- 執行 `pipeline/tools/yf.py 3363.TWO fast_info` → **HTTP 403（ProxyError）**
- yfinance 錯誤訊息：`"no history for 3363.TWO"` / `"possibly delisted"`

由於台灣 TPEx（上櫃）股票行情資料受地域限制，量化 TA 工具無法於本環境取得即時歷史 K 線，故以下技術指標計算值均**無法核實**。

---

## 二、網路資訊補充（僅供參考，非工具驗證）

以下數據來自公開財經網站搜尋結果（非 TA/YF 工具，不列入 PASS/FAIL 計算）：

| 項目 | 數值 | 來源 |
|------|------|------|
| 2026-07-16 收盤價 | ~555 元（漲停，+7.04%） | 財經新聞搜尋結果 |
| 成交量（7/16） | 2,178 張 | 搜尋結果 |
| 2025 H2 區間 | 270-307 元 | Threads 資訊 |
| Morgan Stanley 目標價 | 708 元 | 大摩研究報告（2026） |
| 短期均線狀況 | 死亡交叉（MA5 向下穿越 MA20） | 財經網站技術分析 |
| 中期趨勢 | 年初以來強勢上漲（270→550+ 元） | 搜尋彙整 |

### 補充說明
- 2026 年以來，3363 股價從 2025 年底的 270-307 元區間，大幅攀升至 2026 年 7 月的 550-700+ 元（年漲幅 70-130%），主力題材為 CPO FAU 量產預期。
- 近期出現短期技術調整訊號（死亡交叉），但 7/16 盤中一舉亮燈漲停，顯示市場仍存在強勁買盤支撐。
- 鑒於長紅（漲停）K 棒，若後續確認，短期趨勢可能恢復偏多。

---

## 三、技術指標評估

| 指標 | 計算值 | 狀態 |
|------|--------|------|
| RSI14 | 無法取得 | PRICE_DATA_UNAVAILABLE |
| MACD | 無法取得 | PRICE_DATA_UNAVAILABLE |
| MA50 | 無法取得 | PRICE_DATA_UNAVAILABLE |
| Bollinger Band | 無法取得 | PRICE_DATA_UNAVAILABLE |

---

## 四、判決

```
PASS 條件：RSI14 < 72 AND MACD 非深度負值 AND 收盤價 > MA50
實際狀況：所有量化 TA 指標無法由工具取得（HTTP 403）

[M = N/A]
```

> **價格資料不可用（PRICE_DATA_UNAVAILABLE）。** 技術面評分不納入本次 Phase-1 綜合評估，此項目標記為 N/A，不計入總分。如需技術面驗證，請透過具備 TPEx 資料授權之本地環境另行執行。
