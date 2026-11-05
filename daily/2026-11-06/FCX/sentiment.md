# Sentiment — FCX as of 2026-11-06

資料完整度: 分析師評等與內部人交易完整; 散戶社群 (Reddit, StockTwits) 全部無法取得, 散戶面只能用聚合網頁的二手資訊, 信心度因此下調。

## Analyst consensus
23 位分析師: 6 strongBuy / 12 buy / 4 hold / 1 sell / 0 strongSell (Buy 側 18 家, 占 78%; Hold 17%; Sell 4%)。`recommendations` 工具回傳的 4 個期間 (0m 至 -3m) 數字完全相同, 代表沒有抓到評等變動事件, 因此無法確認近期升評或降評的具體日期。

近期目標價動向 (來自網路聚合資料, 日期未驗證):
| 券商 | 動作 | 評等 |
|---|---|---|
| Wells Fargo | 目標價 87 → 79 USD | Overweight (維持) |
| Freedom Broker | 目標價 75 → 68 USD | Hold (維持) |
| Barclays | 目標價 83 → 84 USD | Overweight (維持) |

整體趨勢: 評等結構穩定偏多, 但目標價有小幅下修跡象, 主要受能源成本壓力影響 (單一摘要指出較 2025 年增加約 500M USD 成本)。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 被拒, 直接 curl 也遭代理 403, 無樣本、無貼文數、無傾向判讀。
- StockTwits: 無法取得。`api.stocktwits.com` 無法解析 (DNS 失敗), 需在 session 網路設定中允許該網域後才能重試; 本次未重試。
- X / 新聞聚合 (WebSearch): 多為分析師觀點與價格目標文章, 日期混雜, 不具散戶情緒代表性。可見的 bullish 論點: 銅金價格高檔, 實現價格全面改善; bearish 論點: 能源通膨壓縮利潤, 目標價下修。
- 聲量 (buzz volume): 無法量化, 無法與平常水準比較。
- 主要主題 (僅從聚合來源推得, 非散戶原文): 銅金價格循環、能源成本、目標價下修。
- 散戶傾向: 無法判定 (bullish / bearish / mixed 皆不下結論)。

## Insider activity
統計區間: 2026-05-06 至 2026-11-06 (6 個月)。金額單位: USD M。

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-27 | Lydia H. Kennard | Director | 賣出 @79.11 | 3,798 | 0.30 |
| 2026-08-25 | Douglas N. Currault II | General Counsel | 選擇權行使 (80,000 股, 履約價 12.04–28.14) | 80,000 | 1.20 (行使價值) |
| 2026-08-25 | Douglas N. Currault II | General Counsel | 賣出 @78.56 | 80,000 | 6.28 |
| 2026-08-05 | Stephen T. Higgins | Officer (間接持有) | 賣出 @69.50 | 14,277 | 0.99 |
| 2026-08-05 | Ellie L. Mikes | Officer | 賣出 @70.00 | 4,773 | 0.33 |
| 2026-07-30 | Stephen T. Higgins | Officer (間接持有) | 賣出 @63.00 | 7,550 | 0.48 |

- 6 個月公開市場賣出合計: 約 8.39 M USD; 公開市場買入: 0。
- 淨額: 約 -8.39 M USD (純賣出)。選擇權行使 (Currault) 的 1.20 M USD 行使價值不計入買入, 因為隨即全數賣出。
- 例行授予 (非市場交易, 不計入淨額): 2026-06-01 九位董事各 2,800 股 (零成本, 共 25,200 股); 2026-07-01 Stephens 與 Grant 董事授予約 0.054 M USD; 2026-10-01 同兩位董事授予約 0.054 M USD。
- 執行長 Kathleen L. Quirk 在 6 個月區間內無公開市場交易。
- 區間外參考 (2026-02): 董事長 Richard C. Adkerson 賣出 400,991 股, 約 25.46 M USD; CFO Maree E. Robertson 賣出 48,500 股, 約 2.99 M USD。不計入本區間淨額, 僅供脈絡。
- 解讀: 主要賣出集中在 7–8 月 (價位約 63–79), 且多為 GC 與高階主管; 沒有任何公開市場買入。8 月賣壓集中於 78–79 USD, 接近 52 週高點 80.24 USD。

## Ownership shifts
- 內部人持股 0.73%; 機構持股 92.12%; 機構數 2,599 家 (float 機構占比 92.81%)。
- 只有單一時點快照, 無法判定機構集中度的趨勢。

## Net sentiment score
- 分析師面: 偏多 (Buy 側 78%), 但目標價有小幅下修。
- 內部人面: 偏空 (6 個月約 8.4 M USD 純賣出, 無公開市場買入)。屬於輕度偏空, 多為獲利了結式賣出。
- 散戶面: 無資料。
- 綜合: 中性偏多 (信心度: 低)。

Divergence flag: 是 (分析師偏多 vs 內部人純賣出)。散戶與分析師的背離無法判定, 因為散戶資料缺失。

SENTIMENT REPORT COMPLETE
