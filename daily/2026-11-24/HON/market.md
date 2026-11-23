# HON 技術分析（Market Analyst）

- 報告日：2026-11-24
- 資料基準日：2026-11-23（最新可得資料）
- 資料狀態：價格可取得，來源為快取（`source: cache`）；yfinance 歷史資料與 Yahoo 請求因網路封鎖失敗。
- 價格差異：`ta.py` snapshot 價格 221.95 與 `yf.py fast_info` 價格 222.01 相差約 0.03%，屬快取時點差異，不影響結論。

## 1. 價格概況

- 最新價：221.95（snapshot）／222.01（fast_info, cache）
- 前收盤：212.64；當日區間：217.44 – 222.20
- 52 週區間：196.16 – 260.28；距 52 週高點 -14.7%，距 52 週低點 +13.1%

## 2. 趨勢（Moving Averages）

| 均線 | 數值 | 價格相對位置 |
|---|---|---|
| MA20 | 221.67 | 價格高於 +0.12%（貼近） |
| MA50 | 215.32 | 價格高於 +3.08% |
| MA200 | 229.68 | 價格低於 -3.36% |

判讀：價格已站上 MA20 與 MA50，短中期結構轉為偏多整理；但仍位於 MA200 之下，長期趨勢尚未確認翻多。

## 3. 動能指標

- MACD：0.796；Signal：1.776；Histogram：-0.980
  - MACD 仍在零軸之上，但已低於 Signal line，且 Histogram 為負、幅度不小，顯示上漲動能減弱，短線偏空訊號。
- RSI(14)：52.6，位於中性區間，無超買或超賣訊號。

## 4. 波動與布林通道

- Bollinger Bands（20, 2）：上軌 230.54／中軌 221.67／下軌 212.80
- %B：0.516，價格位於通道中軸上方，接近中性。
- ATR(14)：6.61，約為價格的 3.0%。
- 20 日年化波動率：37.6%，屬偏高水準，單日波動空間較大。

## 5. 動量（Momentum）

- 1M：+0.36%
- 3M：+2.91%
- 6M：-8.67%
- 12M：+12.49%

判讀：12 個月報酬為正，但 6 個月仍為負，中期表現偏弱；近一至三個月呈現止跌回穩，動能處於修復階段。

## 6. 支撐與壓力

| 類型 | 價位 | 依據 |
|---|---|---|
| 壓力 R1 | 221.7 – 222.2 | MA20 與當日高點，目前價格所在區 |
| 壓力 R2 | 229.7 | MA200 |
| 壓力 R3 | 230.5 | 布林上軌 |
| 壓力 R4 | 260.3 | 52 週高點 |
| 支撐 S1 | 217.4 | 當日低點（強度較弱） |
| 支撐 S2 | 215.3 | MA50 |
| 支撐 S3 | 212.8 | 布林下軌，接近前收盤 212.64 |
| 支撐 S4 | 196.2 | 52 週低點 |

## 7. 成交量

- 快取資料未提供當日成交量與 10 日平均成交量（`ten_day_average_volume` 為空），無法進行量價分析。
- 注意：報告中的 `vol_20d_annualized`（37.6%）為價格波動率，並非成交量指標。

## 8. 綜合判讀

- 整體技術面為中性偏整理：價格貼近 MA20 與布林中軸，RSI 中性；MACD Histogram 轉負，提示短線動能轉弱。
- 關鍵價位：222 為短期多空分界。站上 MA200（約 229.7）前，中長期趨勢仍偏弱。
- 風險位：跌破 MA50（約 215.3）將使短期結構轉弱，下一個關注點為布林下軌與前收盤區（212.6 – 212.8）。
- 限制：本分析僅依快取價格與技術指標，未含成交量與即時盤中資料，結論應搭配基本面與新聞面報告使用。

## 9. 指標總表

| Metric | Value | Signal / Note |
|---|---|---|
| Price (snapshot) | 221.95 | As of 2026-11-23 |
| Price (fast_info) | 222.01 | Cache, cnyes feed |
| Previous Close | 212.64 | fast_info |
| Day Range | 217.44 – 222.20 | fast_info |
| MA20 | 221.67 | Price +0.12% above, neutral |
| MA50 | 215.32 | Price +3.08% above, short-term constructive |
| MA200 | 229.68 | Price -3.36% below, long-term weak |
| MACD | 0.796 | Above zero |
| MACD Signal | 1.776 | MACD below signal |
| MACD Histogram | -0.980 | Negative, momentum weakening |
| RSI14 | 52.6 | Neutral |
| BB Upper | 230.54 | Resistance |
| BB Mid | 221.67 | Price near mid band |
| BB Lower | 212.80 | Support |
| BB %B | 0.516 | Mid-band |
| ATR14 | 6.61 | About 3.0% of price |
| Vol 20d (annualized) | 37.6% | Price volatility, elevated |
| Momentum 1M | +0.36% | Flat |
| Momentum 3M | +2.91% | Stabilizing |
| Momentum 6M | -8.67% | Medium-term weak |
| Momentum 12M | +12.49% | Positive over one year |
| 52W High | 260.28 | Price -14.7% from high |
| 52W Low | 196.16 | Price +13.1% from low |
| Trading Volume | N/A | Not provided in cache |
