# 技術分析 — ETN (截至 2026-08-25)

## 資料狀態警告

**PRICE_DATA_UNAVAILABLE**

由於代理閘道政策封鎖 (HTTP 403)，Yahoo Finance 與鉅亨網資料源無法連接。所有技術指標、價格數據與圖表分析均無法執行。

---

## 快照

```
即時價格：UNAVAILABLE
MA20：UNAVAILABLE
MA50：UNAVAILABLE
MA200：UNAVAILABLE
RSI14：UNAVAILABLE
MACD 柱狀圖：UNAVAILABLE
```

---

## 趨勢分析

無法進行趨勢判定。缺乏：
- 價格相對於 MA20/MA50/MA200 之位置判斷
- 黃金交叉 / 死亡交叉等長期趨勢信號
- 近期價格動作與移動平均線互動之強度評估

---

## 動能評估

無法計算動能指標：

- **MACD 狀態**：無法判定 (信號線、柱狀圖皆不可得)
- **RSI14 讀數**：無法判定 (超買/超賣區間無法判斷)
- **多時段回報**：1m/3m/6m/12m 動量無法計算

---

## 關鍵點位

無法識別支撐與阻力位：

- **阻力位**：UNAVAILABLE (近期本地高點無法確定)
- **支撐位**：UNAVAILABLE (近期本地低點無法確定)
- **止損建議**：無法提供 (缺乏有效之技術參考點位)

---

## 波動率特徵

無法評估波動率特徵：

| 指標 | 狀態 |
|---|---|
| ATR14 日內波動估計 | UNAVAILABLE |
| 20 日年化波動率 | UNAVAILABLE |
| 52 週高/低 | UNAVAILABLE |
| 相對 52 週高位之距離 | UNAVAILABLE |

---

## 交易設定

**可交易性判定**：不適用

缺乏以下必要資訊：
- 趨勢方向（上升 / 下降 / 橫盤）
- 進場訊號確認 (RSI、MACD、價格形態)
- 出場參考點位 (支撐/阻力)
- 風險評估 (ATR 波動、邊際止損)

---

## 技術指標表格

| 指標 | 數值 | 讀數 |
|---|---|---|
| RSI14 | UNAVAILABLE | 無法判定 |
| MACD 柱狀圖 | UNAVAILABLE | 無法判定 |
| % from MA200 | UNAVAILABLE | 無法判定 |
| BB %B (Bollinger Band) | UNAVAILABLE | 無法判定 |
| ATR14 | UNAVAILABLE | 無法判定 |
| 年化波動率 (20d) | UNAVAILABLE | 無法判定 |
| 1 月回報 | UNAVAILABLE | 無法判定 |
| 3 月回報 | UNAVAILABLE | 無法判定 |
| 6 月回報 | UNAVAILABLE | 無法判定 |
| 12 月回報 | UNAVAILABLE | 無法判定 |

---

## 後續行動

1. **資料連線恢復**：待環境代理允許對 `fc.yahoo.com:443` / `ws.api.cnyes.com:443` 之連接後，重新執行本分析

2. **替代資訊來源**：若存在其他獨立之即時行情 API（Bloomberg、FactSet、Wind 等），可轉用備用管道

3. **基本面補充**：並行由基本面分析團隊評估 ETN 之營收成長、利潤率、資本支出指引、資料中心市場占有率等定性因素

4. **風險管理**：在缺乏技術面數據下，應避免以技術信號為主之交易決策；可轉向事件驅動或基本面導向之策略

---

**MARKET REPORT COMPLETE**

*報告時間：2026-08-25 | 資料源狀態：代理封鎖 (403) | 技術分析：不可執行*
