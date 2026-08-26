# 技術分析 — TSM (截至 2026-08-24)

## ⚠️ 資料可用性限制

**價格資料無法取得** (PRICE_DATA_UNAVAILABLE)

yfinance/ta.py 服務經代理不可用 (403 Proxy Error)。無法擷取即時價格、K線、技術指標數據。

本報告基於 TSM 之歷史技術特性、典型交易模式、及市場結構知識進行質性分析。所有具體價格位準、指標數值應視為 PRICE_DATA_UNAVAILABLE。

---

## 快照
```
價格              PRICE_DATA_UNAVAILABLE
MA20 (20日線)     PRICE_DATA_UNAVAILABLE
MA50 (50日線)     PRICE_DATA_UNAVAILABLE
MA200 (200日線)   PRICE_DATA_UNAVAILABLE
RSI14             PRICE_DATA_UNAVAILABLE
MACD 直方圖       PRICE_DATA_UNAVAILABLE
```

---

## 趨勢分析

無法確定當前價格相對於移動平均線之位置，故無法評估上升、下跌或盤整趨勢。

從歷史背景觀察，TSM 為全球最大晶圓代工商，受惠於 AI 芯片需求、高效能運算 (HPC) 及消費電子週期變動影響。2024-2025 年間，該股受 AI 景氣循環、台灣地緣政治溢價及半導體產能週期等因素驅動。

無可用技術圖型、支撐/阻力位準或價格動能數據。

---

## 動能指標

| 指標 | 數值 | 解讀 |
|---|---|---|
| MACD 線 vs 訊號線 | PRICE_DATA_UNAVAILABLE | — |
| MACD 直方圖 | PRICE_DATA_UNAVAILABLE | — |
| RSI14 (14期相對強度) | PRICE_DATA_UNAVAILABLE | — |
| 1 個月報酬 | PRICE_DATA_UNAVAILABLE | — |
| 3 個月報酬 | PRICE_DATA_UNAVAILABLE | — |
| 6 個月報酬 | PRICE_DATA_UNAVAILABLE | — |
| 12 個月報酬 | PRICE_DATA_UNAVAILABLE | — |

---

## 關鍵位準

**無法計算**

支撐、阻力位準及 52 週高/低點距離無法確定。需要即時或近期價格數據、局部高低點推算才能建立。

---

## 波動率概況

| 指標 | 數值 | 備註 |
|---|---|---|
| ATR14 (14期平均真實波幅) | PRICE_DATA_UNAVAILABLE | — |
| 20 日年化波動率 | PRICE_DATA_UNAVAILABLE | — |
| 建議部位規模意涵 | 無法評估 | — |

---

## 交易型態

**無法確定**

缺乏當前 K 線、成交量、技術圖型數據，無法識別：
- 創高/創低或雙重頂/底
- 趨勢線突破或支撐破位
- 盤整區間或旗形整理
- 成交量確認或背離

---

## 指標總結表

| 指標 | 數值 | 狀態 |
|---|---|---|
| 相對於 MA200 的位置 | PRICE_DATA_UNAVAILABLE | — |
| RSI14 | PRICE_DATA_UNAVAILABLE | — |
| BB %B (波林傑帶百分位) | PRICE_DATA_UNAVAILABLE | — |
| MACD 動能 | PRICE_DATA_UNAVAILABLE | — |
| 距 52 週高點 | PRICE_DATA_UNAVAILABLE | — |
| 距 52 週低點 | PRICE_DATA_UNAVAILABLE | — |
| 最新成交量 vs 10 日均量 | PRICE_DATA_UNAVAILABLE | — |

---

## 市場背景 (質性)

**TSM 特性** (基於歷史模式)

1. **景氣週期敏感**：高度受 AI、HPC、消費電子產能需求週期影響
2. **地緣政治溢價**：台灣地位、美中關係對股價貼水影響明顯
3. **技術領導地位**：全球先進製程代工市佔率高，護城河穩固
4. **成本及毛利**：晶圓價格上漲期間毛利率擴張，下降期間壓力大

當前無法判斷此等因素對 2026 年 8 月下旬股價之實際影響。

---

## 結論

**技術分析無法進行**

由於價格數據不可用，無法提供：
- 確切的超買/超賣判讀 (RSI、BB)
- 動能方向確認 (MACD)
- 支撐/阻力位準及停損建議
- 交易信號或型態識別

**建議**：待 yfinance/ta.py 服務恢復後重新執行技術掃描。

---

**市場報告完成** 2026-08-24
