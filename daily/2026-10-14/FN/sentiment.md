# Sentiment — FN (Fabrinet) as of 2026-10-14

資料狀態：Reddit（WebFetch 遭拒）與 StockTwits（DNS 解析失敗）皆無法取得，依規則 soft-fail。散戶面僅能以 WebSearch 的間接資料推估，信心偏低。yf 工具的 Yahoo cookie/crumb 取得失敗，已使用快取回退（屬預期行為）。

## Analyst consensus
yf rec_summary：9 位分析師，3 strong buy / 4 buy / 2 hold / 0 sell，買進評級佔 78%（7/9）。
注意：recommendations 歷史的三個期間（0m、-1m、-2m）數字完全相同，判斷為快取或僅回傳當期快照，無法據此看出評級變化趨勢。

近期評級與目標價變動（StreetInsider 轉引，屬 2026 年春季資料）：
- 2026-04-16 JPMorgan 由 Overweight 降至 Neutral，目標價由 700 調至 680。
- 2026-05-05 Fox Advisors 降至 Equal-Weight。
- 12 個月平均目標價約 668（區間 540 至 800，高點 Needham、低點 Wolfe Research）。
- 其他來源數字分歧：MarketBeat 2026-08 消息稱共識為 "Moderate Buy"，平均目標價約 643；TradingView 平均目標價 550.50（日期不明）。上述數字未能統一為單一時間序列，僅供參考。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 的 search.json 皆無法取得（WebFetch 遭拒）。WebSearch 以 "FN reddit wallstreetbets" 查詢，未找到相關討論串。無可引用的代表性貼文。
- StockTwits / X：StockTwits API DNS 解析失敗，無資料。WebSearch 結果多為低品質聚合頁（同一文章在不同站點、價格與日期互相矛盾），其中含 "Bearish Sentiment" 標題的頁面亦不可信，已排除。Investing.com 頁面列出 2026-07 至 08 的個別使用者看法，立場分歧、樣本過小，不具代表性。
- 討論熱度（volume）：無法量化。以搜尋可見度判斷，FN 的散戶聲量屬低可見度，未見明顯熱度上升。
- 主題（由新聞與搜尋結果推估，非直接散戶貼文）：
  - 基本面：財報 Q4 營收年增約 45%，達創紀錄 13.16 億美元；Q1 FY27 指引高於市場預期（MarketBeat 2026-08-17 快訊）。
  - 估值與波動：2026-08 股價約 572 美元，52 週區間 272.49 至 748.89，波動大。
  - 持股變化：機構減持訊息（Dimensional 2026 Q1 減持約 9.8%）成為質疑點。
- 散戶傾向：無法定論，推估為中性偏多但分歧。信心低。

## Insider activity
Net 6mo（2026-04-14 至 2026-10-14）：$0 buys（公開市場買入），約 $2.74M sells。
- 2026-05-22 BAHRAMI HOMA（Director）賣出 2,500 股，約 $1.78M，均價 711.91。
- 2026-09-03 ARCHER EDWARD T（Officer）賣出 2,500 股，約 $0.96M，均價約 386。
- 2026-08-11 與 2026-08-20 多位高管（GRADY SEAMUS CEO、SVERHA CSABA CFO、GILL HARPAL S. President、ARCHER）大量 Stock Award（Grant），屬授予而非市場買入，不計入淨買賣。
- Notable：CEO GRADY SEAMUS 近 6 個月僅有授予，無公開市場交易。2025-11-26 曾賣出約 22,451 股（約 $10.0M）為 6 個月窗口之外。
- 2026-02-25 KELLY THOMAS F.（Director）賣出約 $1.15M，位於 6 個月窗口之外。
- 解讀：6 個月內無內部人買入，賣出集中於董事與部分高管。授予股票屬例行性質。整體偏中性至略偏空。

## Ownership shifts
- yf major_holders：insidersPercentHeld 0.26%，institutionsCount 1,028。institutionsPercentHeld 回傳 103.7%，明顯為資料異常（超過 100%），不採用其絕對值。
- 13F（WebSearch 轉引 MarketBeat）：Dimensional Fund Advisors 2026 Q1 減持約 9.8% 至約 262,765 股（約 0.73%）；UBS AM 增持約 4.9%；Empowered Funds 與 Ashton Thomas Private Wealth 新建倉。機構與避險基金合計持股約 97%。
- 趨勢：大型被動機構小幅減持、少數主動機構增持，整體無明顯集中化或去集中化結論。來源數字不一致，建議以 SEC EDGAR 13F 覆核。

## Net sentiment score
Composite：**中性（neutral），信心低至中**。
- 分析師面：偏多（bullish）。7/9 買進評級，但春季出現降評，目標價區間寬且來源不一。
- 內部人面：中性偏空。無公開買入，6 個月淨賣出約 $2.74M。
- 散戶面：無法判定（資料缺口）。
- 缺口：Reddit 與 StockTwits 皆未取得，散戶情緒為推估。

Divergence flag：**無法判定**。散戶資料缺失，無法確認散戶傾向是否與分析師傾向相反。若日後取得 Reddit 或 StockTwits 資料，再重新評估。

## 指標摘要
| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師評級（Strong Buy / Buy / Hold / Sell / Strong Sell） | 3 / 4 / 2 / 0 / 0 | yf rec_summary，9 位，當期快照 |
| 買進評級比例 | 78%（7/9） | 由上式推算 |
| 12 個月平均目標價 | 約 668 美元（540–800） | StreetInsider 轉引，2026 春季資料 |
| 其他平均目標價 | MarketBeat 約 643；TradingView 550.50 | 日期不明，數字分歧 |
| 近期評級變動 | JPM 降至 Neutral（4/16，PT 700→680）；Fox Advisors 降至 Equal-Weight（5/5） | StreetInsider 轉引 |
| 6 個月內部人公開買入 | $0 | yf insider |
| 6 個月內部人公開賣出 | 約 $2.74M（BAHRAMI $1.78M、ARCHER $0.96M） | yf insider |
| 6 個月內授予股票（非現金） | 多位高管，數量約 8 萬股 | yf insider，不計入淨額 |
| 內部人持股比例 | 0.26% | yf major_holders |
| 機構持股數 | 1,028 家 | yf major_holders |
| 機構持股比例 | 異常（103.7%） | yf major_holders，資料錯誤，不採用 |
| Dimensional 2026 Q1 變動 | 減持約 9.8%，約 262,765 股（0.73%） | MarketBeat 轉引 |
| 機構與避險基金合計持股 | 約 97% | MarketBeat 轉引 |
| Reddit 討論串數量 | 無法取得 | WebFetch 遭拒 |
| StockTwits 訊息數與多空比 | 無法取得 | DNS 解析失敗 |
| 散戶熱度 | 低可見度（定性） | WebSearch 推估 |
| 綜合情緒 | 中性，信心低至中 | 本報告判斷 |
| 背離旗標 | 無法判定 | 散戶資料缺口 |

SENTIMENT REPORT COMPLETE
