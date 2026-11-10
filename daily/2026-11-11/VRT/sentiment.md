# Sentiment — VRT as of 2026-11-11

## Analyst consensus
資料單位: 分析師家數 (tool: yf rec_summary, 0m 期)

| 評級 | 家數 |
|---|---|
| Strong Buy | 4 |
| Buy | 23 |
| Hold | 3 |
| Sell | 0 |
| Strong Sell | 0 |

合計 30 家: 27 buy (含 4 strong buy) / 3 hold / 0 sell。

趨勢 (近 4 個月, 同工具): 4 個月前為 3 SB / 21 B / 4 H (合計 28 家)。現在 Hold 減 1、Buy 增 2、Strong Buy 增 1, 整體評級小幅上移。

Recent moves (次級來源, 日期不一, 未經 yf 逐筆驗證):
- Wells Fargo 升評 (2026-09-26, MarketBeat)。
- Vertical Research 首次覆蓋給 Buy (2026-10 月)。
- RBC 目標價由 $323 升至 $351, 維持 moderate buy。
- Jefferies 降評至 Hold, 理由為估值偏高與 hyperscaler capex 長期放緩風險 (日期未明)。
- Wall Street Zen 升評 (2026-10-31, MarketBeat)。
- GLJ Research 首次覆蓋給 Sell, 目標價 $188, 11 月初再下修至 $187。
- MarketBeat 平均評級 "Moderate Buy", 平均目標價約 $338 (Bullstory 約 $339)。

資料缺口: yf rec_summary 的 sell 欄為 0, 未反映 GLJ 的 Sell, 疑似工具未納入該家; 另有 StreetInsider 單筆 JPMorgan 目標價 $51, 明顯為異常值, 未採用。

## Retail social
- Reddit: 不可用。r/wallstreetbets 與 r/stocks 搜尋的 WebFetch 皆回報無法連線 (soft-fail), 無法取得貼文樣本、熱度或多空傾向。
- StockTwits / X: StockTwits API 因網域無法解析 (ENOTFOUND) 失敗 (soft-fail); 須於 session 網路設定中允許 api.stocktwits.com 才能重試。X 端未取得社群貼文, 僅有下述新聞標題。
- 新聞標題傾向 (非散戶原文, 僅作參考): 9/01 "shares up 21, still a buy"; 10/08 "shares down 1, should you sell"; 11/06 "stock jumps 3.3%, time to buy" (MarketBeat 系列標題, 多為自動生成)。標題偏向交替看多看空, 無明確散戶結論。
- 散戶聲量 (buzz volume): 無法量化 (無 Reddit/StockTwits 數據), 不作推斷。
- Themes (由新聞與分析師觀點歸納, 非散戶原文): (1) 估值 (約 50x trailing adjusted earnings) 是主要多空分歧點; (2) hyperscaler capex 是否放緩; (3) S&P 500 納入的市場傳聞; (4) beta 超過 2, 對大盤情緒敏感。
- Retail tilt: 無法判定 (mixed / 資料不足)。

## Insider activity
區間: 2026-05-11 至 2026-11-10 (6 個月)。單位: USD M。

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-09-01 | Monser Edward L | Director | 公開市場賣出 (價格 $249–256) | 15,287 | 3.88 |
| 2026-09-01 | Monser Edward L | Director | 選擇權行使 (行使價 $11.50) | 15,287 | 0.18 (行使價值, 非賣出) |
| 2026-09-08 | Albertazzi Giordano | CEO | 贈與 (gift) | 118,523 | 0 |
| 2026-10-05 | Resha Michael | Officer | 獎勵股 (grant, 價格 $253.62) | 3,193 | 0.81 (授予價值, 非買入) |
| 2026-06-25 / 03-26 | 多位高管 (含 CEO, CFO) | 各職位 | 獎勵股 (grant) | 0–11 股/人 | 0 |

- 6 個月公開市場買入: $0 (無)。
- 6 個月公開市場賣出: $3.88M (僅 Monser, 1 筆)。
- 淨值: 約 -$3.88M (淨賣出)。
- 高管 (CEO Albertazzi, CFO Chamberlin) 6 個月內僅見獎勵與贈與, 無公開市場買賣。
- 6 個月前的較大賣出 (2026-02-26/27, Fradin, Reinemund, Cote, Karlborg 等合計約 $100M+) 不計入本區間, 但顯示 2 月高點附近有密集減持。
- 解讀: 無內部人買入, 近期唯一的公開市場交易為董事減持; 高管無買賣。

## Ownership shifts
- 機構持股比例 84.2% (institutionsPercentHeld 0.842), 機構家數 2,683。
- 內部人持股 0.24%。
- 趨勢 (逐季變化) 工具未提供, 無法判斷機構集中度是增加或減少。

## Net sentiment score
- Analyst 面: 偏多 (27/30 buy, 0 sell, 近期評級小幅上移; 有 GLJ 單一 Sell 為明顯少數意見)。
- Insider 面: 中性偏空 (6 個月無買入、有 $3.88M 董事減持, 高管僅獎勵無買賣)。
- Retail 面: 無法判定 (Reddit、StockTwits 皆不可用)。
- 股價背景 (次級來源): 約 $203 (2026-11-05, Trefis), 較 9 月內部人賣出價 $250 前後下跌約 19%; 11/06 單日 +3.3%。

Composite: **偏多, 信心低** (分析師多數偏多, 但內部人無買入、散戶資料缺漏, 且股價較近期高點回落, 估值分歧明顯)。

Divergence flag: **無法判定** 於散戶 vs 分析師 (缺散戶資料)。內部人 vs 分析師: 輕度分歧 (分析師偏多, 內部人未買入且有董事減持)。

資料來源限制: 分析師數字來自 yf 工具 (可信度高); 近期評級事件與目標價為次級新聞來源 (MarketBeat, Trefis, Bullstory, rallies.ai 等彙整), 日期與數字未逐一核對, 部分不一致。Reddit 與 StockTwits 不可用, 散戶面為空白。本報告不含交易建議。

SENTIMENT REPORT COMPLETE
