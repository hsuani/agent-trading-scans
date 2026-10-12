# Sentiment — TLN as of 2026-10-13

資料基準: 價格與 yf 快取更新於 2026-10-12 (收盤 $386.36)。Reddit / StockTwits 直連遭阻擋，零售情緒改以 WebSearch 間接取得，樣本量不足。

## Analyst consensus
17 家分析師: 6 Strong Buy / 9 Buy / 2 Hold / 0 Sell / 0 Strong Sell (yfinance rec_summary, 0m 期)。recommendationMean 1.59 (1 = Strong Buy, 5 = Sell)，recommendationKey = buy。近三個月結構穩定 (-1m: 6/10/2/0/0；-2m: 6/9/2/0/0)，無賣方評級。

目標價 (yf 快取 info): 平均 $455.65、中位數 $449、最高 $560、最低 $307，相對現價約 +18%。

近期評等變動 (來自 WebSearch 之 MarketBeat / Benzinga 摘要，yf 未提供歷史升降評明細):
- Morgan Stanley: 目標價 $503 -> $514，維持 Overweight (2026-09-18 前後)
- Jefferies: 目標價 $453 -> $422，Hold (2026-07)
- Mizuho: 首次覆蓋 Outperform (2026-09 初)

資料不一致: MarketBeat (2026-10-06) 列 8 Buy / 3 Hold / 1 Sell、平均目標 $460.08；Benzinga 列 20 家 Buy、平均目標 $386。與 yf 的 17 家 (0 Sell) 口徑不同，分析師家數與目標價以 yf 為主，其餘僅作參考。

## Retail social
- Reddit: DATA_UNAVAILABLE。直連 r/wallstreetbets、r/stocks 遭阻擋，WebSearch 未回傳任何 TLN 相關 Reddit 討論串。
- StockTwits / X: 部分。StockTwits 個股頁可開啟但情緒多空比例未出現在擷取文字中，無法量化。WebSearch 未找到具代表性的 X 貼文。
- Benzinga sentiment 頁 (約 2026-09 初) 標示 put/call ratio 3.00 為 bearish 選擇權流向，屬期權市場訊號，不等同散戶情緒，僅作旁註。
- MarketBeat 新聞情緒分數 1.43 (範圍 -2 到 2)，偏正面，但日期不明確。
- 零售聲量: 無可靠次數資料，無法與基準比較，判定為 DATA_UNAVAILABLE。
- 零售多空傾向: 無法判定。

主要敘事主題 (來自新聞與分析師摘要，非散戶貼文):
- 多方: 2 座 CCGT 收購約增 $520M 2026 EBITDA、PJM 容量價格上升、AI / 資料中心電力需求。
- 空方: 夏季天氣溫和導致 EBITDA 落在先前指引下半段、GAAP 虧損、本益比偏高 (trailing P/E 約 77，forward P/E 約 19.5)。
- 質疑: Jim Cramer 稱其為「沒有好殖利率的電力基建題材，不適合我」。
- 2026-08-05 季報 EPS 2.37，低於預估 3.39 (-29.98%)。下次財報 2026-11-04 (預估 EPS 7.37)。

## Insider activity
資料窗口: 2026-04-13 至 2026-10-13 (6 個月)。

已明確標示金額之公開市場交易:
- 2026-06-15 ABBAS GIZMAN I. (Director) 賣出 2,600 股，$380.00/股，約 $988K。

其他 Form 4 紀錄交易類型與金額皆空白，無法判定買或賣:
- 2026-07-15 NUTT TERRY L. (President) 8,312 股，類型未揭露。若為賣出，金額約 $3.2M (以 $380 估算，僅供量級參考，非資料內容)。
- 2026-05-22 多位董事與高管 (MCFARLAND 354,865 股、BERRYMAN 99,138 股、NUTT 90,826 股、MULLER 62,862 股等) 股數高度相似，較像股權授予或歸屬，非市場買賣。

Net 6mo: 明確買入 $0 / 明確賣出約 $988K。另有 NUTT 8,312 股 (類型不明) 未計入。
Notable: 唯一明確的近期市場交易為 Director ABBAS GIZMAN 賣出。CEO MCFARLAND、CFO MULLER 近六個月無明確買賣紀錄。
大股東: RUBRIC CAPITAL 於 2024-12 ($204.35) 與 2025-06 ($288-298) 有大額賣出，皆超過 6 個月窗口。

## Ownership shifts
- 機構持股: yf 顯示 institutionsPercentHeld 102.8%，超過 100%，屬資料異常 (多重計算)，不能直接解讀為集中度。機構數 809。
- 內部人持股: 1.38%。
- 13F (2026-06-30) 主要變動: Fred Alger +30.4%、BlackRock +6.5%、ECP ControlCo 2.4M 股 (+100%，應為新增或重組部位)、Reaves -2.3%。
- Rubric Capital 持有 6.1%，本期未變動。
- 僅單期快照，無法判斷多季趨勢。

## Net sentiment score
Composite: **BULLISH (信心中等偏低)**
- 分析師面 (權重最高): 強烈偏多。17 家中 15 家 Buy 以上、0 Sell，目標價隱含約 +18%。
- 內部人面: 偏中性至輕度偏空。明確交易僅一筆小額賣出，其餘多為授予性質。
- 零售面: 無法量化，不納入加權。
- 信心受限因素: 散戶資料缺失、分析師來源數字不一致、機構持股資料異常、最近財報未達預估。

Divergence flag: **無法判定**。零售傾向無法量測，無法與分析師傾向做背離比較。若日後取得 StockTwits 多空比或 Reddit 樣本，應再檢視。

## Metrics

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師總數 | 17 | yf rec_summary (0m) |
| Strong Buy / Buy | 6 / 9 | yf rec_summary |
| Hold / Sell / Strong Sell | 2 / 0 / 0 | yf rec_summary |
| recommendationMean | 1.59 | yf 快取 info |
| 目標價 平均 / 中位 | $455.65 / $449 | yf 快取 info |
| 目標價 高 / 低 | $560 / $307 | yf 快取 info |
| 現價 (2026-10-12) | $386.36 | yf 快取 |
| 隱含上行空間 (平均目標) | 約 +18% | 計算值 |
| 52 週高 / 低 | $449.84 / $279.77 | yf 快取 |
| 6mo 明確買入金額 | $0 | yf insider |
| 6mo 明確賣出金額 | 約 $988K | yf insider (ABBAS GIZMAN) |
| 6mo 類型不明交易 | 1 筆 (NUTT 8,312 股) | yf insider |
| 內部人持股比例 | 1.38% | yf major_holders |
| 機構持股比例 | 102.8% (異常) | yf major_holders |
| 機構數 | 809 | yf major_holders |
| Reddit 樣本 | DATA_UNAVAILABLE | 直連遭阻擋，WebSearch 無結果 |
| StockTwits 多空比 | DATA_UNAVAILABLE | 頁面已開啟，比例未擷取 |
| 零售聲量 / 多空傾向 | DATA_UNAVAILABLE | 無可靠來源 |
| Benzinga put/call | 3.00 | 期權流向，非散戶情緒 |
| MarketBeat 新聞情緒 | 1.43 | 範圍 -2 到 2，日期不明 |
| 綜合情緒 | BULLISH (信心中等偏低) | 分析師為主 |
| 背離旗標 | 無法判定 | 零售資料不足 |

SENTIMENT REPORT COMPLETE
