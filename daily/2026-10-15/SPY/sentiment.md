# Sentiment — SPY as of 2026-10-15

## 資料可得性總結

| 面向 | 狀態 | 說明 |
|---|---|---|
| 分析師共識 | 不適用 | SPY 為 ETF，無個股評等。yf rec_summary / recommendations 回傳空 |
| 散戶社群 (Reddit) | DATA_UNAVAILABLE | WebSearch 未找到 r/wallstreetbets 或 r/stocks 的 2026-10 內容 |
| StockTwits | 未查詢 | 依任務要求以 WebSearch 為主，未直接抓取 |
| 內部人交易 / 持股集中度 | 不適用 | ETF 略過 |
| 基金資金流向 | DATA_UNAVAILABLE | 找不到 2026-10 的 SPY 週資金流數據 |
| VIX | DATA_UNAVAILABLE | 最新可得讀數為 2026-04 (19.17)，非當期 |
| SPY put/call | DATA_UNAVAILABLE | 最新可得為 2026-05 (1.13)，非當期 |
| 價格與實現波動率 | 已取得 | 來源為 repo 快取 prices/SPY.csv 與 prices/yf/SPY.json |

## 價格與波動背景 (快取，最後完整交易日 2026-10-13)

- 收盤 778.01。快取 info 的 regularMarketPrice 為 769.6，與 CSV 不一致，視為不可靠，未採用。2026-10-14 資料未在快取內。
- 報酬: 1 週 -0.14%，1 個月 +2.25%，3 個月 +3.07%，年初至今約 +14.1% (以 2026-01-02 收盤 681.92 為基準，近似值)。
- 位置: 距 52 週收盤高點 779.09 (2026-10-06) 僅 -0.14%，接近新高。52 週低點 629.28 (yf info)。近一年最大回撤約 -9.1%。
- 實現波動率 (年化): 10 日 6.8%，21 日 9.5%，63 日 10.9%。短期波動低於中期。
- 成交量: 近 10 日平均約 3,756 萬股。10/12 為 1,869 萬、10/13 為 2,585 萬，明顯低於近期均量，屬於量縮墊高。

## 分析師共識
不適用 (ETF)。

## 散戶社群 (Reddit / StockTwits / X)
- Reddit: DATA_UNAVAILABLE。WebSearch 找到的 historicaloptiondata.com 期權流分析為 2026-04 至 2026-07 期間，且非 Reddit 內容，不能代表 wallstreetbets 情緒。
- StockTwits: 未查詢。
- X / 新聞: 未找到 2026-10 的 SPY 或大盤情緒文章。
- 預測市場 (PredScope): 2026-10-05 與 10-09 的 SPY 單日漲跌市場，「上漲」機率約 96%。每個市場交易量約 1.5 萬美元，樣本少，僅供參考，不代表廣泛情緒。
- 主題: 無可靠主題可歸納。

## 資金流與部位 (fund flows / positioning)
- 基金資金流: 找不到 2026-10 數據。搜尋結果都是 2022 年或年份不明的舊資料，不採用。
- 歷史脈絡 (非當期，僅作背景): 2026-06 有報導稱 VIX call/put 未平倉比率升至 2026 年高點，顯示investors 在低 VIX 下買進波動率保護。2026-06 週資金流數據亦有引用，但未能驗證。
- 期權流 (historicaloptiondata.com): 2026-06-11 偏空 (puts 佔 64.6% 美元量)、06-26 偏多 (calls 66.9%)、07-02 中性 (puts 58.6%)。只能看出 4 至 7 月之間偏中性震盪，無 10 月資料。

## 內部人與持股
不適用 (ETF)。

## 淨情緒分數
綜合: **中性 (信心: 低)**

依據:
- 價格接近 52 週新高、短期實現波動率偏低、成交量縮，這些屬於平靜、偏樂觀的價格面訊號。
- 缺少 VIX、put/call、資金流、社群情緒等核心情緒指標，無法確認市場是否真的處於低恐慌或過度樂觀。
- 預測市場的高度單邊共識樣本太小，權重低。

若當期 VIX 仍低、put/call 偏低且資金持續流入，可能是過度樂觀訊號；若 VIX 快速上升或 put/call 升高，則應重新評估。以上為描述性觀察，不構成交易建議。

背離旗標: 不適用 (無分析師端，無法比較散戶與分析師傾向)。

## 建議後續補查 (資料缺口)
1. CBOE VIX 當日收盤與 VIXCLS (FRED)。
2. CBOE SPY 或全市場 put/call ratio。
3. ETF 週資金流 (etf.com 資金流工具或 FactSet / Bloomberg)。
4. AAII 情緒調查與 CNN Fear & Greed 指數。
5. 補抓 2026-10-14 的 SPY 收盤資料。

## 參考來源
- [PredScope: SPY Up or Down on October 5, 2026](https://predscope.com/event/spy-up-or-down-on-october-5-2026)
- [PredScope: SPY Up or Down on October 9, 2026](https://predscope.com/event/spy-up-or-down-on-october-9-2026)
- [Historical Option Data: SPY Trading Analysis 07/02/2026](https://historicaloptiondata.com/?p=65974)
- [Historical Option Data: SPY Trading Analysis 06/26/2026](https://historicaloptiondata.com/?p=64627)
- [Historical Option Data: SPY Trading Analysis 06/11/2026](https://historicaloptiondata.com/?p=61198)
- [Cryptobriefing: Investors seek downside protection as VIX call options surge to 2026 highs](https://cryptobriefing.com/vix-call-options-surge-downside-protection/)
- [XTB: VIX trims today rally almost in half to 27 (2026-04 報導，非當期)](https://xtb.com/en/market-analysis/vix-trims-today-rally-almost-in-half-to-27-as-wall-street-rebounds-from-multi-month-lows)
- 本地快取: /home/user/agent-trading-scans/prices/SPY.csv、/home/user/agent-trading-scans/prices/yf/SPY.json

SENTIMENT REPORT COMPLETE
