# Sentiment — DLR (Digital Realty Trust) as of 2026-10-31

> 資料時點: 分析師評等與內部人交易來自 yf 工具 (yfinance repo 快取)；社群情緒來自 WebSearch (截至 2026-10-30)。Reddit/StockTwits 於沙箱皆無法連線，標記 DATA_UNAVAILABLE。

## Executive summary
分析師面相當正向：yf rec_summary 顯示 34 位分析師中 29 位給買進 (含 Strong Buy)、5 位持有、0 位賣出，近三個月持有評等由 7 家降到 5 家。社群情緒無法量化：Reddit、StockTwits 於沙箱皆被封鎖，WebSearch 也找不到可用的提及量或多空比例，零售端標記 DATA_UNAVAILABLE。內部人近六個月以小額賣出為主，無公開市場買入紀錄。股價近一個月走弱 (約 -4.8%)，但未見負面情緒數據可直接印證。綜合判斷：偏多，信心中等 (受限於零售端資料缺失)。

## 零售與社群情緒
- Reddit (r/stocks、r/wallstreetbets)：DATA_UNAVAILABLE，WebFetch 無法連線取得貼文樣本。
- StockTwits/X：DATA_UNAVAILABLE，DNS 無法解析。
- WebSearch 間接訊號：多為聚合站/SEO 頁面，日期不一致，多空標籤泛化，可信度低。
- 主題 (來自新聞標題，非社群原文)：資料中心需求與 AI 基建題材 (Q1 2026 FFO/營收優於預期)；股價自 7 月底約 198.63 回落至 10/23 約 172.37；分析師 Q2 後上調目標價 (TD Cowen 升評 Buy 目標 222、JPMorgan 目標 235 維持 Overweight)；Brookfield Corp 持股減少 (僅標題，細節未確認)。
- 聲量與多空比例：DATA_UNAVAILABLE，不提供百分比。

## 分析師共識
### 評等分布 (yf rec_summary，家數)
| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 當前 (0m) | 5 | 24 | 5 | 0 | 0 | 34 |
| -1m | 5 | 24 | 5 | 0 | 0 | 34 |
| -2m | 5 | 23 | 5 | 0 | 0 | 33 |
| -3m | 5 | 21 | 7 | 0 | 0 | 33 |

當前買進側佔比 29/34 ≈ 85.3%；持有 14.7%；賣出 0%。近三個月買進側由 26 家增至 29 家，未見降評。

### 目標價 (WebSearch 聚合，來源不一致)
| 來源 | 指標 | 數值 (USD) |
|---|---|---|
| MarketBeat | 平均 12 個月目標價 | 218.17 |
| Barchart | 平均目標價 | 173.04 |
| Barchart | 最高目標價 | 212 |
| TD Cowen (Q2 後) | 目標價 | 222 |
| JPMorgan (Q2 後) | 目標價 | 235 |

來源間口徑不一致 (Barchart 評等家數 25 位 vs yf 34 位)，不採單一數字作結論。

## 機構與內部人活動
### 內部人交易 (yf insider，近六個月 2026-05-01 至 2026-10-31)
- 公開市場賣出：Mark R. Patterson (Director) 2026-08-27 賣出 200 股 @193.96 USD，約 38,792 USD。
- 公開市場買入：無紀錄。
- 獎勵發放 (非買賣)：Jean F.H.P. Mandeville (Director) 2026-05-29 獲配 1,289 股。
- 判讀：規模小、以董事為主，未見 CEO/CFO 近六個月交易，訊號中性。

### 機構持股 (yf major_holders)
- 機構持股家數：1,840。institutionsPercentHeld 原始值 1.049 (104.9%)，明顯口徑異常，不採信。
- 歷史趨勢：DATA_UNAVAILABLE。已知事件：Brookfield Corp 持股減少 (2026-07-27，僅標題)。

## 綜合情緒判斷
- 分析師端：偏多，買進側約 85%、無賣出評等、近三個月小幅上修。
- 零售端：DATA_UNAVAILABLE。
- 內部人端：中性偏弱，僅一筆小額董事賣出。
- 價格動能：近一個月約 -4.8%。
- 綜合：偏多 (Bullish-leaning)，信心中等，分析師一致性高但零售端缺失，背離旗標無法判定。

## 資料限制
1. Reddit 與 StockTwits 均不可用，零售情緒無量化數據。
2. 目標價與評等家數在不同來源間不一致。
3. institutionsPercentHeld 數值異常 (>100%)，已排除。
4. 機構持股趨勢與 Q3 2026 實際財報結果未取得確認。
5. 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
