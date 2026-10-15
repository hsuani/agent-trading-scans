# Sentiment — ALB as of 2026-10-16

## Analyst consensus
yf rec_summary 目前為 3 strong buy / 11 buy / 9 hold / 0 sell / 0 strong sell（共 23 家）。本工具回傳的過去三個月計數完全相同，疑似資料未更新，不能視為最新快照。

近期動向（以網路搜尋為主，未能用結構化來源逐筆核對）:
- BMO Capital (10/6): 目標價由 $200 降至 $175，維持 Outperform。原因是第三季儲能業務指引下修（銷量與價格）。
- UBS (10/上旬): 目標價降至 $150。
- Argus (10/上旬): 目標價由 $230 降至 $135。
- Mizuho (10/1): 目標價由 $140 降至 $130。
- Vertical Research: 評等由 Buy 降為 Hold，目標價 $145。來源未註明日期，無法確認是否在 10 月內。
- 本期未找到新的評等調升。
- 股價參考: 10/7 收於約 $102.75。前一次內部人大額賣出價約 $184（5 月），顯示股價自高點已大幅回落。
- 下次財報: 11/4（依 Tikr 報導）。

整體判讀: 評等分布仍偏多（0 sell），但 10 月出現集中的目標價下修，分析師端語氣轉弱。與 yf 計數不一致的部分，需以 MarketBeat / TipRanks 即時資料再核對。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 抓取失敗（WebFetch 回傳 Claude Code 無法存取 www.reddit.com）。Soft-fail，無樣本。
- 網路搜尋 "ALB reddit" 未找到相關 Reddit 討論串，無法判斷散戶語氣。
- StockTwits: DNS 解析失敗 (api.stocktwits.com ENOTFOUND)。Soft-fail，無樣本。
- X / 新聞: 未取得 X 原始貼文。可見的網路內容多為機構評論與目標價調整新聞，屬於專業投資人論述，不屬於散戶情緒。
- 討論量: 無法量化（無資料），不做「高於或低於平常」的判斷。
- 散戶傾向: 無法判定（bullish / bearish / mixed 皆無依據）。
- 主題: 無法從本次資料歸納。從機構報告可見的主要論點為鋰價與儲能需求、第三季指引下修、以及股價自 4 月高點回落後的估值重估。這些是分析師論述，不是散戶主題。

## Insider activity
統計區間 2026-04-16 至 2026-10-16（6 個月）:
- 公開市場買入: $0（無）
- 公開市場賣出: 約 $3.01M（CEO Jerry Kent Masters，2026-05-15，16,393 股，價格 $183.12–184.52）
- 淨額: 約 -$3.0M（以賣出為主，無買入）
- 其他交易（非買賣，不計入淨額）: 2026-07 至 2026-09 董事與高階主管股票獎勵（Stock Award），無現金金額

區間外參考:
- 2026-03: CEO 賣出約 $2.01M（$170–172）；另有 $5.0M 股票贈與（Stock Gift，非市場交易）
- 2025-10: 董事 Alejandro Wolff 買入約 $17.9K；GC Krupa 小額賣出（$95–105）

Notable: Jerry Kent Masters（CEO）— 5 月大額賣出為近期最明確的內部人負面訊號。無內部人公開市場買入紀錄，本區間內無逆勢承接。

## Ownership shifts
- 內部人持股: 約 0.22%
- 機構持股: 約 101.8%（超過 100%，為資料來源常見的重複計算現象，僅供參考）
- 機構家數: 1,303
- 趨勢: 本次只有單一時點快照，無法判斷集中度的增減方向。需要下一期快照比較。

## Net sentiment score
- 分析師端: 中性偏多（多數 Buy，0 Sell），但 10 月目標價集中下修，動能轉弱。
- 內部人端: 偏空（6 個月內僅有 CEO 大額賣出，無買入）。
- 散戶端: 無資料，無法評分。
- 綜合: **中性偏空，信心度低**。信心受限於散戶資料完全缺失，且 yf 分析師計數疑似過期。

Divergence flag: **無法判定**。散戶端沒有可比對的資料，因此不能確認散戶與分析師方向是否相反。若要判定，需補 Reddit 或 StockTwits 資料（需從其他來源或可用的代理服務取得）。

## 資料來源狀態
- yf recommendations / rec_summary / insider / major_holders: 成功（回傳內容中含 Yahoo cookie/crumb 失敗警告，資料仍有回傳）
- Reddit (wallstreetbets, stocks): 失敗（存取受限）
- StockTwits: 失敗（DNS 解析）
- WebSearch: 成功，結果多為 2026-05 至 2026-10 的新聞彙整，部分條目日期不明

SENTIMENT REPORT COMPLETE
