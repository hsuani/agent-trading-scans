# Sentiment — FCX as of 2026-10-16

資料完整度提醒: Reddit 與 StockTwits 本次皆無法取得 (Reddit 回傳 fetch 錯誤, StockTwits DNS 解析失敗), 零售端 (retail) 沒有實際樣本。下列零售段落為資料缺口, 不是中性結論。Yahoo 的 analyst 與 insider 資料由 yf 工具取得, 但 cookie/crumb 取得失敗, 部分欄位可能為快取值。

## Analyst consensus
yf rec_summary (目前, 0m): 23 家 — 6 Strong Buy / 12 Buy / 4 Hold / 1 Sell / 0 Strong Sell。Buy 類占比 78% (18/23), Sell 類 4%。

趨勢 (yf 四期快照): 0m, -1m, -2m 數字完全相同 (6/12/4/1), -3m 為 6/13/3/1。即約 2 至 3 個月前有一家 Buy 轉為 Hold, 之後未變。注意: 0m 與 -1m, -2m 完全一致, 可能是資料未更新, 不能視為近期無評等變動。

近期評等動作 (網路搜尋, 非 yf 原始資料, 日期多為 2026 年 4 至 8 月):
- 2026-02-13: Argus 由 Hold 升為 Buy。
- 2026-04-24: UBS 目標價由 $66 升至 $74, 維持 Buy。同日 Morgan Stanley 由 Overweight 降為 Equal Weight, 目標價由 $70 降至 $66, 理由為 Grasberg 爬坡較慢與近期成本上升。Jefferies 目標價由 $76 降至 $75, 維持 Buy。
- 2026-05-21: Barclays 首次覆蓋, Overweight, 目標價 $77; StreetInsider 所列 7/16 更新目標價為 $80。
- 2026-07: Morgan Stanley 重申 Equal Weight; Barclays, Wells Fargo 維持 Overweight; RBC 維持 Sector Perform。
- 平均目標價: StreetInsider 約 $67.55, Simply Wall St 社群共識約 $67.40, 最高 $85 (Jefferies)。來源日期不一, 最新約 2026 年 8 月。

判讀: 目標價平均約 $67 至 $68, 而 10/1 董事股票獎勵的成交參考價為 $70.00。若此平均目標價仍有效, 股價已略高於平均目標價, 表示分析師共識可能落後市價。需以即時目標價資料確認。

另一筆來源 (Barchart, 2026-03) 稱 21 家中 15 Strong Buy / 3 Moderate Buy / 3 Hold, 與 yf 家數與分布不同, 屬不同資料源與日期, 不宜直接合併。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 本次無法取得 (fetch 錯誤)。無法評估樣本、熱度或語氣。
- StockTwits: 本次無法取得 (DNS 解析失敗)。
- X / 新聞輿情: 網路搜尋未找到 2026 年 10 月的個人投資人觀點, 結果多為 2026 年 3 月至 8 月的分析師與新聞文章, 無法引用零售語錄。
- 零售聲量 (volume): 無法量化, 請勿以此推論熱度高低。
- Themes (由新聞與公司事件推得, 非零售直接觀察): Grasberg 產能與爬坡進度、2026 年銅產量指引下調、銅價與成本、Q1 後分析師目標價調整。
- 零售傾向: 無法判定 (bullish / bearish / mixed 皆不下結論)。

## Insider activity
Net 6mo (2026-04-16 至 2026-10-16, 以 yf insider 紀錄計): 公開市場買入 $0, 公開市場賣出約 $8.39M。

6 個月內主要賣出:
- 2026-08-25: General Counsel Douglas Currault, 賣出 80,000 股, 約 $6.28M (@ $78.56), 同日有 80,000 股選擇權行使 (conversion) 紀錄。
- 2026-08-05: Officer Stephen Higgins (間接持有), 賣出 14,277 股, 約 $0.99M (@ $69.50)。
- 2026-08-05: Officer Ellie Mikes, 賣出 4,773 股, 約 $0.33M (@ $70.00)。
- 2026-07-30: Officer Stephen Higgins, 賣出 7,550 股, 約 $0.48M (@ $63.00)。
- 2026-08-27: Director Lydia Kennard, 賣出 3,798 股, 約 $0.30M (@ $79.11)。

非市場交易 (不計入淨額): 董事與高管的例行股票獎勵 (2026-06-01, 07-01, 10-01), CEO Kathleen Quirk 與 Chairman Richard Adkerson 的年度獎勵於 2026-02 發放。

6 個月外脈絡 (僅供參考, 不計入淨額): 2026-02 Chairman Richard Adkerson 賣出約 400,991 股 (約 $25.5M), CFO Maree Robertson 賣出約 48,500 股 (約 $3.0M), General Counsel Currault 賣出約 75,000 股 (約 $4.8M)。另 2026-03 與 2025-11 有 Adkerson 的贈與紀錄。

判讀: 6 個月內無公開市場買入, 賣出集中於 GC 與部分高管, 且多數發生在股價由 2025 年底約 $48 上漲至 $63 至 $79 區間的期間。CEO 在此期間無公開市場交易紀錄。這類賣出較像獲利了結, 不必然代表對基本面的負面判斷, 但仍是與分析師偏多方向相反的訊號。

## Ownership shifts
- 機構持股: 89.4% (institutionsPercentHeld), 機構家數 2,524。
- 內部人持股: 0.72%。
- 趨勢: yf major_holders 僅提供目前快照, 無歷史比較, 無法判斷機構集中度趨勢。

## Net sentiment score
Composite: **中性偏多 (neutral-to-bullish), 信心中低**

依據:
- 分析師 (權重高, 資料較完整): 偏多 (78% Buy 類), 但目標價平均可能落後市價, 且 Morgan Stanley 在 4 月降評。
- Insider: 偏中性至偏空 (6 個月淨賣出 $8.4M, 無公開市場買入, 屬獲利了結型態)。
- 零售: 無資料, 不納入計分。
- 機構持股高 (89%), 內部人持股低, 無趨勢資料。

信心偏低的原因: 零售端完全缺失, 分析師評等快照的 0m 與 -1m, -2m 數字相同, 且目標價均為 2026 年 8 月以前資料。

Divergence flag: **無法判定 (零售資料缺失)**。
- 分析師與 insider 之間存在部分分歧: 分析師偏多, 內部人在股價高點區間賣出。
- 若取得 Reddit 或 StockTwits 資料後, 再判斷零售是否與分析師方向相反。

補抓建議: 下次報告前, 優先取得 (1) 即時股價與 rec 的日期化評等變動, (2) 最新 consensus 目標價, (3) 零售資料 (Reddit 可嘗試其他端點或改用 PullPush 類替代來源, StockTwits 需確認 DNS 與 API key 狀況)。

## Sources (網路搜尋)
- [UBS raises PT on FCX to $74 (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/ubs-raises-price-target-freeport-173240543.html)
- [Morgan Stanley, UBS, JPMorgan raise PT on FCX (Yahoo Finance)](https://finance.yahoo.com/news/morgan-stanley-ubs-jpmorgan-raise-215607470.html)
- [FCX analyst ratings history (StreetInsider)](https://www.streetinsider.com/rating_history.php?q=FCX)
- [FCX analyst consensus (FN2)](https://cdn.fn2.ai/earnings/fcx/analysts)
- [Argus upgrades FCX (Nasdaq)](https://www.nasdaq.com/articles/argus-research-upgrades-freeport-mcmoran-fcx)
- [Freeport-McMoRan analyst estimates & ratings (Nasdaq)](https://www.nasdaq.com/articles/freeport-mcmoran-stock-analyst-estimates-ratings)
- [Analysts' opinion on FCX, Barchart (2026-03)](https://www.barchart.com/story/news/1057840/here-s-what-to-expect-from-freeport-mcmorans-next-earnings-report)

SENTIMENT REPORT COMPLETE
