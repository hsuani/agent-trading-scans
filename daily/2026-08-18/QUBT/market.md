# QUBT 市場技術分析 — 2026-08-18
**Quantum Computing Inc. (QUBT) | 量子運算族群 | 光子量子技術**

---

## 價格數據狀態

**PRICE_DATA_UNAVAILABLE — Yahoo Finance 403**

技術分析數據不可用，所有進出場價位待價格恢復後確認。

---

## 說明

yfinance 對 QUBT 返回 HTTP 403 錯誤，無法取得以下數據：

- 即時或歷史收盤價
- 成交量 / 均量
- RSI14、MACD、Bollinger Bands
- MA20 / MA50 / MA200
- ATR（Average True Range）
- 52 週高低點
- Beta 值

由於缺乏可靠的即時價格數據，本報告**不提供**任何技術層面的進出場建議。
根據 pipeline 完整性規範，下游 Trader Agent 及 Portfolio Manager **不得**基於推估或新聞敘述捏造任何進出場價位。

---

## 參考資訊（非 yfinance，僅供背景參考，不作為技術分析依據）

- StockAnalysis 約 2026-08-14 參考價格：**~$9.01**（非即時，精確度不保證）
- 分析師平均 12 個月目標價：**$18.33**（來源：多家分析師共識，非 yfinance）
- 市值參考：**~$2.05B**

以上數據僅供定性背景了解，不具備技術交易信號的有效性。

---

## Phase 1 市場信號評分

| 技術信號 | 判定 |
|---|---|
| RSI14 < 72 | PRICE_DATA_UNAVAILABLE |
| MACD 柱狀圖非深度負值 | PRICE_DATA_UNAVAILABLE |
| 價格 > MA50 | PRICE_DATA_UNAVAILABLE |
| 綜合評估 | **無法評分 — 跳過此信號** |

---

## 待辦事項

當 Yahoo Finance 403 限制解除後，需補充以下技術分析項目：

1. 日線趨勢確認（價格相對 MA20/50/200 位置）
2. 動能指標（RSI14 超買/超賣水準，MACD 信號線交叉）
3. 波動率評估（ATR，Bollinger Band 寬度）
4. 成交量結構（配合價格趨勢的量能確認）
5. 關鍵支撐/阻力位（基於近期技術結構）
6. 明確進場條件、止損位、第一/第二目標價

---

*報告生成時間：2026-08-18 | 分析師：市場技術代理 | 族群：quantum*
