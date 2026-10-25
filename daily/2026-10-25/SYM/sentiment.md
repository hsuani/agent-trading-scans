# Sentiment — SYM as of 2026-10-25

資料完整度: 分析師與內部人交易為本次主要來源 (yf 工具)。Reddit 與 StockTwits 無法取得 (見下方)，散戶情緒為 N/A，綜合評分信心偏低。

## Analyst consensus

目前分布 (yf rec_summary，單位為家數):

| 評級 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 1 | 6% |
| Buy | 8 | 47% |
| Hold | 5 | 29% |
| Sell | 2 | 12% |
| Strong Sell | 1 | 6% |
| 合計 | 17 | 100% |

即 9 buy / 5 hold / 3 sell。近四個月走勢: Buy 由 8 → 8 → 9 → 9，Hold 與 Sell 無變化，整體為持平至微偏多。

近期動向:
- yf recommendations 端點回傳的仍是同一組彙總數字，無個別升降評等明細，無法確認近期 upgrade / downgrade 事件。
- 網路搜尋摘要 (Benzinga, 2026-09，未經原始頁面核對): 平均目標價約 $55，最高 $82，最低 $10。Needham 下調目標價至 $60 但維持 Buy；Barclays 維持 Underweight，目標價 $38。
- Weiss Ratings 於 2026-05-11 由 hold 下調至 sell (Trefis, 2026-05)。Weiss 非典型券商研究，權重應低於 sell-side。
- 家數落差: 搜尋摘要稱 21 位分析師給 Buy，與 yf 的 17 家總數不一致，以 yf 為準。

## Retail social

- Reddit (r/wallstreetbets、r/stocks): 無法取得。WebFetch 回傳 "unable to fetch from www.reddit.com"，依規則軟失敗，未取得貼文樣本、分數或留言數。
- StockTwits: 無法取得。api.stocktwits.com 解析失敗 (ENOTFOUND)，未取得訊息量與多空標籤。
- X / 新聞搜尋: 僅得到零散的 aggregator 頁面，無 2026-10 月的 SYM 個股評論。最新可用的情緒資料為 2026-09 的 Benzinga 頁面，內容包括:
  - 空單比例 (short interest) 約佔流通股 31.7%，頁面標示為偏空。此數字來自搜尋摘要，未經原始頁面核對，且兩個 Benzinga 頁面對選擇權流量與內部人資料的描述互相矛盾。
  - 2026-05 財報: 營收 $676M 優於預期，但 EPS $0.01 低於 $0.12 的共識，屬於失望的盈餘反應 (Trefis)。
  - GuruFocus 提到年初至今跌幅約 29.9%，trailing P/E 約 463x (GAAP 雜訊可能很大)，文章日期不明。
- 股價參考: 內部人 2026-10-01 至 10-05 的成交價約 $42.67–$43.72，為目前可用的最新價格錨點。stockscan 的 $41.49 與泰國掛牌 BKK:SYM23 (7.25) 不是同一標的，不採用。
- 買賣量級: 無法量化，未取得相對於平常的提及次數，僅能定性。
- 散戶多空傾向: N/A (資料不足)。
- 主要主題 (僅由搜尋摘要推斷，證據弱): 高空單比例與逼空可能性、盈餘品質與 GAAP 獲利不足、估值過高、分析師目標價分歧。

## Insider activity

6 個月區間 2026-04-25 至 2026-10-25 (共 25 筆有金額的交易):

| 項目 | 金額 (USD M) | 筆數 |
|---|---|---|
| 公開市場買入 | 0.0 | 0 |
| 高階主管與董事賣出 | 約 8.0 | 24 |
| SoftBank (10% 以上大股東) 賣出 | 281.8 | 1 |
| 合計賣出 | 289.9 | 25 |

淨額: 6 個月內無任何公開市場買入。內部人 (CEO、CFO、CTO、董事、其他主管) 合計賣出約 $8.0M；若計入 SoftBank 則合計約 $289.9M。

主要交易:
- SoftBank Group (Beneficial Owner >10%)，2026-05-27: 賣出約 559 萬股，成交價 $50.42，約 $281.8M。為本區間最大單筆，屬大股東減持，性質與董監事個人賣出不同。
- Todd Krasnow (Director)，2026-05 至 2026-10 多次小額賣出，合計約 $3.5M，為賣出最頻繁者。
- Izilda Martins (CFO)，2026-07-27，賣出 27,463 股，成交價 $40.80，約 $1.12M。
- James Kuffner (CTO)，2026-07-24，賣出 18,987 股，成交價 $40.38，約 $0.77M；同區間另有多筆賣出。
- William Boyd (Officer)，2026-07-27，賣出 9,194 股，成交價約 $40.8，約 $0.38M。
- Charles Kane (Director)，2026-10-01，賣出 2,000 股，成交價約 $42.7，約 $0.09M。

觀察:
- 2026-07-23 附近有 5 筆無金額的大量申報 (例如 Kuffner 47,923 股、Martins 59,134 股)。推測為 RSU / PSU 歸屬或稅款扣繳，之後 07-24 至 07-27 出現的市場賣出可能與之相關，但資料無法確認，不應直接視為主動賣出。
- 2025-12-11 CEO Richard Cohen 有一筆 1,000,000 股的 stock gift (非市場交易)，不計入金額。
- 賣出價格區間由 2026-04 約 $57–60 下滑至 2026-07/08 約 $40，之後回升至 $42–46。

## Ownership shifts

- 機構持股占已發行股數 79.4%，機構占流通股 91.9%，機構家數 555 家。
- 內部人持股占 13.6%。
- yf major_holders 只提供目前快照，無歷史序列，無法判斷機構集中度趨勢。SoftBank 5.59M 股的減持若屬實，代表大股東持股比例下降，值得後續追蹤 13F 資料確認。

## Net sentiment score

- 分析師: 偏多 (Buy 占 53%，四個月 Buy 家數微增，sell 家數穩定)。信心: 中。
- 內部人: 偏空 (6 個月零公開買入，合計賣出逾 $8M，不含 SoftBank；加上 SoftBank 約 $290M)。信心: 中高，但 SoftBank 單筆性質不同，需分開解讀。
- 散戶: N/A。Reddit、StockTwits 皆無法取得。
- 綜合: 中性 (分析師偏多與內部人偏空相抵)。信心: 低，因為散戶資料缺失，且搜尋來源的目標價與空單數字未經原始頁面核對。

Divergence flag: 無法判定 (散戶資料缺失)。
附註: 分析師偏多與內部人持續賣出存在方向分歧，此分歧是聰明錢內部的分歧，不是散戶與分析師的分歧。若後續能取得 Reddit 或 StockTwits 資料，應重新判定。

## 資料缺口與後續

1. Reddit 與 StockTwits 需替代來源或稍後重試。
2. yf recommendations 無個別升降評等明細，目標價歷史需另取。
3. 內部人交易中 9 筆無金額的紀錄未計入金額，性質待確認。
4. 空單比例 31.7%、Needham / Barclays 目標價、GuruFocus 數字皆來自搜尋摘要，需以原始來源核對。

SENTIMENT REPORT COMPLETE
