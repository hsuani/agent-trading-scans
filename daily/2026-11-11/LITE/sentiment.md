# Sentiment — LITE as of 2026-11-11

資料來源狀態:
- yfinance 工具 (recommendations / rec_summary / insider / major_holders): 正常。
- Reddit (r/wallstreetbets, r/stocks): WebFetch 遭拒, 無法取樣貼文。
- StockTwits: api.stocktwits.com DNS 解析失敗, 需在 session 網路設定允許此網域後才能重試。
- WebSearch 聚合站與 AI 摘要 (AltIndex、Quiver、MarketBeat 等): 可用但日期混雜、數字互相衝突, 下文已標示。

## Analyst consensus

目前 (0m) rec_summary: 25 家, Strong Buy 3 / Buy 16 / Hold 6 / Sell 0 / Strong Sell 0。買方合計 19 家 (約 76%)。

趨勢 (yfinance 月度序列, 買方占比):
| 期間 | Strong Buy | Buy | Hold | 合計 | 買方占比 |
|---|---|---|---|---|---|
| -3m | 5 | 17 | 4 | 26 | 约 85% |
| -2m | 5 | 18 | 4 | 27 | 约 85% |
| -1m | 5 | 18 | 5 | 28 | 约 82% |
| 0m | 3 | 16 | 6 | 25 | 约 76% |

解讀: 買方家數連續下滑, 持有家數由 5 升至 6, 無賣方評等。屬於漸進式降評, 非集體轉空。

Recent moves (二手摘要, 日期未確認):
- Barclays 由 Overweight 下調至 Equal Weight。
- StoneX 首次評等 Buy, 目標價 $1,200。
- MarketBeat 共識為 "Moderate Buy", 平均目標價約 $1,078.75。
- 不同來源的分析師家數與共識標籤不一致 (另一來源稱 22 家、15 Strong Buy), 以 yfinance 25 家為準。

股價脈絡 (二手摘要, 未能與工具數據對齊): 摘要稱 2026-11-02 財報後單日下跌 18.59%, 收於 $684.40; 此價位與 2026 年 9 月內部人成交價 (約 $840 至 $990) 有明顯落差, 需由價格資料源另行確認, 本報告不採用。

## Retail social

- Reddit: 無法取得原始貼文。聚合站 AltIndex 顯示 Reddit 提及量近期趨近於 0/日, 5-9 月月度約 5-10 次提及, 屬低討論量。該站情緒分數偏中性至偏多, 僅供參考。
- StockTwits / X: StockTwits 未取得。X 端由 Quiver 的 AI 摘要反映: 偏多一派稱訂單 "sold out through 2028"；保守一派建議暫不加碼。
- 聲量: 整體低, 無法給出可靠的相對倍數。

Retail tilt: 混合偏多 (低信心)。聚合站整體偏多, 但樣本薄弱、來源非原始貼文。

Themes:
- 供給瓶頸: indium phosphide 與 EML 雷射供應吃緊。
- AI 光通訊需求與資料中心擴產。
- 估值爭議: 倍數高於產業與自身五年均值。
- 財報後急跌與內部人大量賣出, 為主要負面敘事。

## Insider activity

Net 6mo (2026-05-11 至 2026-11-11, 僅計公開市場 "Sale", 排除 Stock Award 授予):
- 買入: 0 筆 (無公開市場買入)。
- 賣出: 27 筆, 共 110,214 股, 約 $98.2M (USD)。
- 近 3 個月 (2026-08-11 起): 72,454 股, 約 $62.5M。

6 個月賣出明細 (USD M):
| 內部人 | 職位 | 筆數 | 股數 | 金額 (USD M) |
|---|---|---|---|---|
| Vincent D. Retort | Officer | 4 | 47,512 | 40.95 |
| Jae Kim | General Counsel | 5 | 18,625 | 16.24 |
| Yuen Wupen | Officer | 10 | 15,517 | 14.10 |
| Brian J. Lillie | Director | 2 | 12,000 | 11.78 |
| Isaac H. Harris | Director | 2 | 5,416 | 4.86 |
| Ian S. Small | Director | 1 | 4,954 | 4.30 |
| Pamela Fletcher | Director | 1 | 3,155 | 3.07 |
| Wajid Ali | CFO | 1 | 2,487 | 2.37 |
| Michael E. Hurlston | CEO | 1 | 548 | 0.53 |

Notable: CEO 僅一筆小額賣出 (約 $0.53M), CFO 一筆約 $2.37M。金額最大者為 Retort (Officer) 單筆約 $33.0M。多數交易為連續小額, 無法由工具確認是否有預定交易計畫 (10b5-1)。

## Ownership shifts

- 機構持股 95.25%, 機構數 1,926 家; 內部人持股 0.31%。
- 工具只提供單一時點快照, 無時間序列, 無法判斷集中度趨勢。

## Net sentiment score

Composite: 中性 (信心低至中)。
- 分析師: 偏多 (76% 買方, 0 賣方), 但買方占比近三個月連續下滑。
- 內部人: 偏空 (6 個月約 $98M 賣出、0 買入)。
- 零售: 混合偏多, 但樣本不足, 信心低。

Divergence flag: 是 (部分)。分析師整體偏多, 與內部人大量賣出方向相反; 但內部人賣出可能屬例行或計畫性交易, 解讀需保守。

SENTIMENT REPORT COMPLETE
