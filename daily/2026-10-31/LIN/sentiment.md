# Sentiment — LIN as of 2026-10-31

> 資料時效警示：yfinance 券商評等與內部人交易資料可回溯至 2026-08 前後；Reddit、StockTwits 無法取得；網路新聞多為 7–8 月資料，未找到 10 月的實質輿論。以下結論信心受限。

## Analyst consensus

29 家券商：6 strongBuy + 17 buy = **23 buy** / **5 hold** / **1 sell** (strongSell 0)。買方比例約 79%。

趨勢 (yf rec_summary 四期)：
| 期間 | strongBuy | buy | hold | sell | 買方合計 |
|---|---|---|---|---|---|
| 0m (現在) | 6 | 17 | 5 | 1 | 23 |
| -1m | 5 | 17 | 5 | 1 | 22 |
| -2m | 5 | 16 | 5 | 1 | 21 |
| -3m | 4 | 16 | 6 | 1 | 20 |

評等小幅正向漂移：三個月內買方增加 3 家、hold 減 1 家、無 downgrade 跡象。yfinance recommendations 僅回傳期間彙總，沒有逐家券商的升降評紀錄。

近期目標價異動 (次級來源，未經 yfinance 直接核實)：
- Evercore ISI 目標價升至 $525 (7/10)
- Bernstein 目標價升至 $599 (7/17)
- Walnut Invest 統計：近六個月 12 次上調、0 次下調；平均目標價 $547.08 (8 月資料)，當時股價約 $478.38

Barchart 技術面評等在 Q2 財報前由 100% Buy 降至 64% Buy (次級來源，日期未明)。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：WebFetch 無法連線 reddit.com，無樣本，無法判定 tilt。
- **StockTwits**：api.stocktwits.com 無法解析 (DNS 失敗，不在允許網域清單內)，未重試。需在 session 網路設定中允許此網域才能取得。
- **X / 新聞**：WebSearch 無 10 月相關輿論。可見的新聞標題包括 Barchart「Can Linde Justify Its Premium While Industrial Gas Demand Cools?」，焦點在估值溢價與工業氣體需求降溫。
- **Buzz 量**：無法量化相對於平常的提及次數，記為「未知」。
- **Themes (由新聞標題推論，非 retail 原始貼文)**：
  1. 估值溢價是否合理
  2. 工業氣體需求循環是否放緩
  3. 獲利穩定與指引上修 (次級來源提到 FY2026 EPS 指引 17.70–17.90，且近四季超預期)
  4. Q2 後技術面轉弱

## Insider activity

Net 6mo (2026-05-01 至 2026-10-31)：**$0.05M 買入 / $2.64M 賣出，淨額約 -$2.60M**

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-18 | Reynolds Paula Rosput | Director | 公開市場買入 @ $479.12 | 100 | 0.05 |
| 2026-06-08 | Innocenzi Stefanos | Officer | 無價格資料 (疑似配發) | 4,035 | 不明 |
| 2026-05-15 | Wood Robert L. | Director | 賣出 @ $506.39–508.76 | 5,215 | 2.64 |

重點觀察：
- 窗口內只有兩筆具價格的公開市場交易：董事 Reynolds 小額買入、董事 Wood 賣出。
- 窗口內無 CEO / CFO 公開市場交易。
- 窗口外的背景資料：
  - CEO Sanjiv Lamba 於 2025-12-08 買入 $1.00M (@ $396.68)。
  - 2026-02 至 03 有官員集中賣出，合計約 $10.2M (Bichara、Durbin、Patwari)。此批交易不在 6 個月窗口內，權重較低。

內部人情緒判定：窗口內淨賣但金額小、樣本僅兩筆，偏中性至略偏淡。

## Ownership

- 機構持股 89.39% (float 口徑 89.62%)，機構數 3,363 家。
- 內部人持股 0.25%。
- 僅為單一時點快照，無法判定機構集中度的趨勢方向。

## Net sentiment score

**綜合：偏多 (bullish lean)，信心低至中。**

| 面向 | 判定 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 中 | 23/5/1 分布，三個月內正向漂移；價格資料為 8 月前後 |
| 散戶 | 無資料 | — | Reddit、StockTwits 不可用 |
| 內部人 | 中性偏淡 | 低 | 窗口內淨賣 $2.6M，但只有兩筆可見交易 |
| 技術面 / 新聞 (次級) | 分歧 | 低 | 技術評等轉弱，新聞聚焦估值與需求 |

**Divergence flag：無法判定。** 散戶資料缺失，無法比對散戶與分析師方向。分析師偏多與內部人淡的落差是內部訊號分歧，而非散戶與分析師的分歧。

## Data gaps

1. Reddit (r/wallstreetbets、r/stocks)：連線遭拒
2. StockTwits：api.stocktwits.com DNS 失敗，需加入允許網域
3. yfinance：cookie/crumb 取得失敗，但 rec_summary、insider、major_holders 仍有回傳
4. 10 月份的網路輿論與價格資料未取得；目標價異動來自次級來源

SENTIMENT REPORT COMPLETE
