# Sentiment — 2383.TW 台光電 as of 2026-10-29

資料時點說明: 分析師評級為執行當下 yfinance 彙總數據；散戶與社群來源 (Reddit、StockTwits) 本次皆無法取得；價格引用為第三方網站 2026-10-16 快照。

## Analyst consensus
目前 18 家 buy (6 Strong Buy + 12 Buy) / 0 家 hold / 0 家 sell。

| 時間點 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 目前 (0m) | 6 | 12 | 0 | 0 | 18 |
| 1 個月前 (-1m) | 6 | 11 | 0 | 0 | 17 |
| 2 個月前 (-2m) | 5 | 11 | 0 | 0 | 16 |
| 3 個月前 (-3m) | 5 | 11 | 0 | 0 | 16 |

Recent moves: 近三個月覆蓋家數由 16 增至 18，新增皆為 buy 評級，期間無 hold 或 sell 出現，也無降評紀錄。工具僅回傳月度彙總計數，無法列出個別券商的升降評名稱。目標價資料未提供，無法判斷目標價調整方向。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆回傳 "Claude Code is unable to fetch from www.reddit.com"，兩個來源均略過。台股個股在這兩個版的討論量本身可能就很少，即使可取得，樣本也可能不足以代表散戶看法。
- StockTwits: 無法取得。api.stocktwits.com 解析失敗 (getaddrinfo ENOTFOUND)，此 session 網路設定未允許該網域。依規定未重試，需由使用者於 session 網路設定中開放該網域後才會重新抓取。
- X: 本次未取得 X 貼文資料。
- 網路可見討論 (WebSearch 結果，樣本有限): CMoney 個股討論區內容立場混合。一則偏多，留言者形容股價走勢強勁並提出長期價格區間看法；另一則偏保守，提醒大盤可能回測近期低點，應注意風險控管。頁面未顯示發文日期，無法確認是否為 10 月內容。
- 討論量: 無可靠的提及次數來源，無法與歷史基準比較，僅能定性為「無法量化」。
- Themes:
  1. 營收與獲利成長: 第三方公司簡介指出 2026 年 7 月營收創單月歷史新高，Q2 EPS 年增幅度大。這是偏多論述的主要依據。
  2. 大盤回檔風險: 保守論述的核心，認為整體市場可能重新測試近期低點。
  3. 三大法人籌碼: 第三方籌碼頁顯示 10 月中旬外資多日淨賣超 (含 10/15 大額賣超)，投信則多數買超。
- Retail tilt: 混合 (mixed)，樣本不足，信心低。

## Insider activity
Net 6mo: 無法確認。insider 工具回傳空陣列 `[]`，此結果無法區分「6 個月內無申報」與「資料來源未涵蓋台股董監事申報」。因此不能推論為零買零賣。Notable: 無可辨識的個人交易紀錄。建議以公開資訊觀測站 (MOPS) 的董監事持股申報資料核實。

Ownership shifts (單一快照，無歷史趨勢):
- 內部人持股比例 (insidersPercentHeld): 19.0%
- 機構持股比例 (institutionsPercentHeld): 48.7%，機構家數 368
- 以流通股計的機構持股比例 (institutionsFloatPercentHeld): 60.1%
- 無前期快照，無法判斷集中度增減方向。

## Net sentiment score
Composite: 偏多 (bullish)，信心中低 (low-to-moderate)。
- 偏多依據: 分析師 18 家全數為 buy 評級，且近三個月家數穩定增加，為目前唯一可量化的訊號。
- 限制: 散戶面無可靠樣本，內部人交易無法確認，兩者皆無法納入加權。
- 反向因素: 10 月中旬外資淨賣超，以及大盤回檔風險論述，屬於需要持續觀察的變數。
- 價格脈絡 (第三方): 2026-10-16 收盤約 5,165 TWD；8 月公開快照為 5,490 TWD。兩者為不同日期，僅供參考。

Divergence flag: 否 (資料不足，無法確認分歧)。分析師面為偏多，散戶面為混合，兩者目前沒有明確反向訊號。待 Reddit 或 StockTwits 可取得後應重新評估。

## Data gaps
- Reddit (r/wallstreetbets、r/stocks): 無法取得
- StockTwits: 網域未允許，無法取得
- insider 工具: 回傳空陣列，無法確認
- 目標價與個別升降評明細: 工具未提供

## 來源
- [nStock 2383 股價與籌碼](https://www.nstock.tw/2383?status=8)
- [nStock 公司簡介 (2026-08-29)](https://www.nstock.tw/台光電做什麼.html)
- [CMoney 台光電個股討論區](https://www.cmoney.tw/forum/stock/2383?tab=column)

SENTIMENT REPORT COMPLETE
