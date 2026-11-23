# QUBT 技術分析 (Market Analyst)

- 目標日期: 2026-11-24
- 資料基準日: 2026-11-23 (ta.py snapshot `as_of`)
- 價格狀態: 可取得, 未觸發 PRICE_DATA_UNAVAILABLE
- 價格來源:
  - `ta.py snapshot` price: 4.7962 (as_of 2026-11-23)
  - `yf.py fast_info` last_price: 4.7984 (`source: cache`, cached_at 2026-11-23T17:54:53Z)
  - 兩者差距約 0.05%, 本報告以 ta.py snapshot 為技術指標計算基準.
- 資料限制: 網路對即時來源受限, yfinance 連線失敗, 所有資料為快取. 成交量欄位 (`ten_day_average_volume`, 當日成交量) 為 null, 無法做量價分析.

## 1. 趨勢與均線 (Trend / Moving Averages)

- 價格 4.80 低於 MA20 (5.93, -19.1%)、MA50 (7.00, -31.5%)、MA200 (8.35, -42.5%).
- 均線呈 MA20 < MA50 < MA200 的空頭排列.
- 判讀: 短、中、長期趨勢皆偏空, 且價格與長期均線乖離大.

## 2. MACD

- MACD -0.615, Signal -0.506, Histogram -0.108.
- MACD 位於零軸下方且低於訊號線, 動能偏空.
- 柱狀體為負. 因未提供歷史序列, 無法判斷柱體是否收斂.

## 3. RSI14

- RSI14 = 33.7, 位於弱勢區, 接近超賣門檻 (30) 但尚未進入超賣區.
- 判讀: 短線有跌深後反彈的可能, 但目前缺乏動能翻正的確認.

## 4. 布林通道 (Bollinger Bands, 20, 2σ)

- 上軌 7.50 / 中軌 5.93 / 下軌 4.36.
- %B = 0.139, 價格位於下軌上方約 10% 的位置, 接近下軌.
- 通道寬度約為中軌的 53%, 顯示波動度處於擴張狀態.

## 5. 動量 (Momentum)

- 1M -26.9%, 3M -43.3%, 6M -58.9%, 12M -53.3%.
- 各週期動量皆為負值, 下跌趨勢具一致性.

## 6. 波動度 (Volatility)

- ATR14 = 0.482, 約為價格的 10.1%.
- 20 日年化波動率 = 102.2%, 單日波動幅度大, 停損與部位規模需相應調整.

## 7. 支撐與壓力 (Support / Resistance)

支撐:
- 52 週低點 4.37 (價格距離 +9.8%).
- 布林下軌 4.36. 與 52 週低點幾乎重疊, 為最關鍵的支撐區 (約 4.36–4.37).
- 當日盤中低點 4.76 (yf fast_info `day_low`, 快取資料).

壓力:
- 布林中軌 / MA20: 5.93, 為第一道壓力.
- MA50: 7.00, 為第二道壓力.
- MA200: 8.35, 為長期壓力.
- 當日盤中高點 5.08 (快取資料), 為短線近端壓力.

## 8. 成交量 (Volume)

- 無法評估. 快取資料未提供當日成交量與近期平均成交量.
- 快取的日內資訊顯示: 前收 4.40, 最新價 4.80, 約 +9.1%, 盤中區間 4.76–5.08. 僅供參考, 無成交量確認.

## 9. 綜合判斷 (Summary)

- 趨勢: 空頭, 三條均線皆在價格上方, 排列為空頭.
- 動能: 偏空. MACD 在零軸下方且低於訊號線, 動量全週期為負. RSI 接近超賣但未確認反轉.
- 位置: 價格貼近 52 週低點與布林下軌 (約 4.36–4.37), 為目前的主要技術支撐.
- 風險: 年化波動率 102%, ATR 約 10%, 跌破 4.36 將形成新低並打開下行空間.
- 關鍵觀察:
  1. 4.36–4.37 支撐能否守住.
  2. 能否站回 MA20 (5.93), 作為短線止跌與趨勢轉弱的初步確認.
  3. MACD 柱狀體是否由負轉正或收斂.
  4. 補足成交量資料後, 確認反彈是否有量能支持.

## 指標總表 (Metrics Table)

| Metric | Value | Note |
|---|---|---|
| Price (ta snapshot) | 4.7962 | as_of 2026-11-23, 計算基準 |
| Price (yf last_price) | 4.7984 | source: cache |
| Previous Close | 4.40 | cache |
| Day High / Day Low | 5.08 / 4.7601 | cache, intraday |
| MA20 | 5.9308 | price -19.1% vs MA |
| MA50 | 6.9969 | price -31.5% vs MA |
| MA200 | 8.3479 | price -42.5% vs MA |
| MA Alignment | MA20 < MA50 < MA200 | bearish |
| MACD | -0.6149 | below zero line |
| MACD Signal | -0.5065 | MACD below signal |
| MACD Histogram | -0.1084 | bearish |
| RSI14 | 33.66 | weak, near oversold |
| BB Upper | 7.5018 | |
| BB Mid | 5.9308 | = MA20 |
| BB Lower | 4.3598 | near price support |
| BB %B | 0.139 | lower band zone |
| ATR14 | 0.4824 | ~10.1% of price |
| Volatility 20D (annualized) | 102.2% | high |
| Momentum 1M | -26.9% | negative |
| Momentum 3M | -43.3% | negative |
| Momentum 6M | -58.9% | negative |
| Momentum 12M | -53.3% | negative |
| 52W High | 14.45 | |
| 52W Low | 4.37 | primary support |
| % from 52W High | -66.8% | |
| % from 52W Low | +9.8% | |
| Volume | N/A | not available in cache |
