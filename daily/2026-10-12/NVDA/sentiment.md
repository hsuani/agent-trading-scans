# Sentiment — NVDA as of 2026-10-12

資料品質摘要: 分析師評等與內部人交易來自 pipeline/tools/yf (live feed 被 proxy 阻擋, 使用 repo cache prices/yf/NVDA.json 與 tool-results 內保存的輸出)。Reddit 與 StockTwits 的 WebFetch 依指示未使用, 改以 WebSearch 查詢; 未取得 2026-10 當月的實際貼文或 StockTwits 訊息流, 下列散戶部分為間接指標, 不是當期直接量測。

## Analyst consensus
62 位分析師: 10 strongBuy / 49 buy / 2 hold / 1 sell / 0 strongSell (買方佔 95%, 即 59/62)。
近四個月趨勢: 0m 與 -1m 相同 (59 買 / 2 持有 / 1 賣); -2m 為 57 買 / 2 持有 / 1 賣; -3m 為 58 買 / 2 持有 / 1 賣。評等結構穩定, 無明顯降評潮。
Recent moves: 來源 feed 只回傳彙總counts, 未列出個別 upgrade / downgrade 事件與目標價 (price target) 變動, 因此無法確認近期個別評等異動與目標價修正方向。Web 搜尋找到的唯一個別評等為 2025 年底 Raymond James 的 Buy 建議 (Barchart/Yahoo 報導), 已超過六個月, 僅供背景參考。

## Retail social
- Reddit: 未取得 r/wallstreetbets 或 r/stocks 2026-10 的搜尋結果 (WebSearch 查無當月 WSB 討論)。無可引用的代表性貼文。
- StockTwits / X: 未取得 2026-10 的 StockTwits 訊息流。間接指標: AltIndex 綜合 Reddit、StockTwits 與論壇的情緒分數, 2026-06 為 76/100 (偏多), 2026-01 至 05 介於 74 至 77 (來源: [WebSearch 結果, AltIndex](https://altindex.com/ticker/nvda/sentiment) 列於 WebSearch 摘要中)。Vanda Research 曾在 2026 年初指出 NVDA 有 $706M 五日淨散戶流入 (來源: Yahoo/Benzinga 相關報導, 日期不一致, 可信度中)。
- Options flow (低可信度, 第三方自動化頁面): historicaloptiondata.com 於 2026-09-02 與 09-04 的分析顯示 calls 佔 64.6% 至 71.2% 的成交量, 偏多; 8 月下旬曾描述為中性偏多。
- Buzz volume: 無當月提及次數可量化, 無法與歷史基準比較。以 Web 上的密度判斷, 2026 年 NVDA 仍是熱門題材, 但無法給出可靠的 mention count。
- Themes (由間接來源歸納, 非貼文直接引用): AI 資料中心需求、接近歷史高點的價格動能、估值泡沫擔憂 (反覆出現的空方論點)、中國出口限制與晶片出貨恢復的不確定性。
- 2025 年 10 月 Yahoo 報導指出, 社群情緒曾由 89/100 快速跌至 41/100 (市場焦慮驅動, 非公司新聞), 顯示散戶情緒的波動性高。

Retail tilt: 最近可驗證的散戶傾向為偏多 (2026-06 AltIndex 76/100; 2026-09 選擇權 calls 佔比偏高); 2026-10 的實際傾向無法確認 (unknown)。

## Insider activity
統計區間: 2026-04-12 至 2026-10-12 (6 個月), 以 feed 內 Sale (公開市場賣出) 與 Buy 計算, 排除 Stock Gift (贈與) 與 Stock Award (授予)。

Net 6mo: 公開市場 buys = $0; sells 約 $1.37B (8 筆 Sale 合計)。
主要賣方明細:
- Mark A. Stevens (Director): 2026-09-02 賣出 1,848,501 股 (約 $410.8M, 價格 $220.06-226.27); 2026-09-04 賣出 1,022,239 股 (約 $235.6M, $227.70-234.00); 2026-09-18 賣出 1,366,000 股 (約 $300.1M, $219.72-220.42); 2026-06-04 賣出 1,000,000 股 (約 $221.1M); 2026-06-18 賣出 885,000 股 (約 $186.0M)。6 個月內合計約 $1.35B, 為最大賣方。
- Colette M. Kress (CFO): 6 個月窗口內無公開市場賣出 (最後一筆 2026-03-20, 不在區間內)。
- Timothy S. Teter (General Counsel): 2026-08-31 賣出 30,000 股 (約 $6.5M); 2026-09-21 賣出 30,460 股 (約 $6.8M)。
- Jen-Hsun Huang (CEO): 6 個月內無公開市場賣出, 僅 2026-06-16 贈與 400,000 股 (非交易); 上一筆公開市場賣出為 2025-10-29, 距今約一年。
- Stephen C. Neal (Director): 2026-06-03 賣出 15,500 股 (約 $3.3M)。
- John O. Dabiri (Director): 2026-05-27 賣出 625 股 (約 $0.13M)。
- Tench C. Coxe (Director): 2026-09-02、08-05、07-01 各 500,000 股贈與 (Stock Gift), 不計入買賣金額。

觀察: 賣出高度集中於董事 Stevens 與 Teter, CEO 與 CFO 在區間內未見公開市場賣出。Feed 未標示是否為 10b5-1 預設交易計畫, 無法判斷賣出是否屬計畫性; 公開市場 buys 為零是明確的中性偏空訊號。
## Ownership shifts
- 內部人持股 (insidersPercentHeld): 4.007%
- 機構持股 (institutionsPercentHeld): 71.406%; 流通股機構持股 (institutionsFloatPercentHeld): 74.387%
- 機構數量 (institutionsCount): 7,673
- 趨勢: 來源僅為單一時點快照, 無法判斷近期機構集中度是增加或減少。

## Net sentiment score
Composite: 中性偏多 (neutral-to-bullish), 信心: 中低。

依據:
- 分析師面 (權重最高, 信心中): 59/62 買方, 結構穩定, 偏多。
- 內部人面 (信心中): 6 個月約 $1.37B 公開市場賣出、零公開市場買進, 偏空訊號, 但集中於董事且可能為計畫性交易, 強度需打折。
- 散戶面 (信心低): 最近可驗證資料偏多, 但 2026-10 無直接資料, 且情緒歷史上波動大。

Divergence flag: 部分是。散戶 (最近可驗證資料) 與分析師傾向皆偏多, 但內部人 (董事與法務長) 持續減持, 與分析師偏多形成分歧。散戶與分析師之間並無明顯反向; 主要分歧在於內部人與外部評等之間。資料缺口: 若無 2026-10 的 StockTwits 或 WSB 直接資料, 無法確認散戶是否已轉為反向。

資料限制與待補項:
1. 個別評等異動與目標價變動 (feed 未提供)。
2. 2026-10 的 Reddit、StockTwits、X 直接討論量與情緒分數 (WebFetch 依指示未用, WebSearch 無結果)。
3. 內部人交易是否為 10b5-1 計畫 (需 SEC Form 4 原文確認)。
4. 機構持股的時間序列 (需多期資料)。

Sources (WebSearch 結果, 僅作背景參考):
- [AltIndex NVDA sentiment](https://altindex.com/ticker/nvda/sentiment)
- [Yahoo Finance: Sentiment in Nvidia Turns Negative, Down to 41/100](https://finance.yahoo.com/news/sentiment-nvidia-turns-negative-down-155127891.html)
- [Benzinga: Nvidia Overtakes Tesla As The Most Popular Stock Among Retail Investors](https://benzinga.com/z/37436392)
- [historicaloptiondata.com NVDA Trading Analysis 09/04/2026](https://historicaloptiondata.com/?p=87374) (低可信度)

SENTIMENT REPORT COMPLETE
