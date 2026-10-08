# Sentiment — APD as of 2026-10-09

資料覆蓋不完整，Reddit 與 StockTwits 皆無法取得 (見下方)。

## Analyst consensus
yf rec_summary: 4 Strong Buy / 11 Buy / 7 Hold / 0 Sell / 0 Strong Sell，合計 22 家。買進類佔 15/22 (約 68%)，無賣出評級。
- 近四個月趨勢: 總家數由 21 增至 22 (Strong Buy 由 3 增至 4)，Buy 與 Hold 皆無變動，整體偏多且穩定。
- yf recommendations 僅提供月度彙總計數，無逐家券商的升降評等明細，故無法從工具確認具體 upgrade/downgrade 事件。
- 新聞面 (WebSearch，截至 2026-09-18 左右): Argus 於 9/9 將目標價上調至 $329；Keybanc 於 9/11 以 Sector Weight (中性等級) 首次評級；Benzinga 9/18 快照為 18 家 (12 Buy / 6 Hold)，平均目標價 $329，當日收盤 $279.46，隱含上行約 17%。
- 來源數字不一致: yf 為 22 家，Benzinga 為 18 家，可能是統計口徑或時點差異，未調和。
- 其他聚合站 (Nemo Money) 目標價約 $333.38；Nemo 預估下次財報 2026-11-05 (FQ4 2026)。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無資料。WebFetch 回報 "unable to fetch from www.reddit.com"，兩個子版皆失敗，soft-fail。
- StockTwits: 無資料。api.stocktwits.com DNS 解析失敗 (ENOTFOUND)，soft-fail。
- X / 新聞散戶討論: WebSearch 未找到 2026-10 的散戶情緒文章，最新相關內容僅為 9 月分析師動態與聚合站頁面，不足以判定散戶情緒。
- 討論量: 無法量化，無相對基準，不做判斷。
- 主題: 無可靠樣本，無法列出重複出現的主題。
- 散戶傾向: 無法判定 (無資料)。

## Insider activity
以 2026-10-09 回推 6 個月 (約 2026-04-09 起) 計算:
- 買入: $0。
- 賣出: $0.82M，單筆。CFO Melissa Schaeffer 於 2026-05-01 以 $303.76 賣出 2,714 股，約 $824K，直接持有 (D)。
- 淨額: 約 -$0.82M (淨賣)。
- 6 個月外但值得注意: Mantle Ridge, L.P. (>10% 持股者) 於 2026-02-12 以 $284.21 賣出 70,175 股，約 $19.9M，另有 1,759 股贈與。
- 近 18 個月趨勢: 2025 年 2 月出現集中賣出 (約 $11M+)，2025 年 8 月另有小額賣出；唯一近期買入為董事 EVANS ANDREW W 於 2025-04-02 買入 5 股 (約 $1.5K)，屬象徵性交易。
- 資料缺口: 最新一筆 Form 4 日期為 2026-05-01，2026-05 之後無記錄。可能為工具資料延遲，或實際無交易，需以 SEC EDGAR 核對。

## Ownership shifts
- 機構持股 92.98%，機構數 2,253 家。
- 內部人持股 1.89%。
- 僅有單一時點快照，無法判定機構集中度的趨勢方向。

## Net sentiment score
- 分析師: 偏多 (Buy 類佔 68%，無 Sell，近期目標價上修)。
- 內部人: 中性偏空 (6 個月淨賣約 $0.82M，無買入；但金額相對 APD 市值不大，且多為例行 10b5-1 性質的可能性待查)。
- 散戶: 無資料。
- 綜合: 中性偏多，信心低。主要原因是散戶端完全缺資料，且內部人與分析師方向不一，加上 yf 與 Benzinga 家數不一致。

Divergence flag: 無法判定。散戶端無資料，無法比較其傾向與分析師傾向是否相反。

SENTIMENT REPORT COMPLETE
