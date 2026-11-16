# Sentiment — ARQQ (Arqit Quantum) as of 2026-11-17

資料完整度偏低: yf 分析師評等欄位為空, Reddit 與 StockTwits 無法取得, 僅有內部人交易、持股結構與少量網路搜尋結果。以下結論信心有限。

## Analyst consensus
yf `recommendations` 與 `rec_summary` 皆回傳空值, 無法取得最新 buy / hold / sell 分布。

次級來源 (MarketBeat 2026-09-28 快訊, 與 TipRanks AI 分析): 共識評等 Hold, 目標價約 $60, 樣本極少 (約 1 Buy / 1 Sell)。TipRanks 技術面評級為 Neutral, 並給出 Hold。這些資料落後報告日約 7 週, 且與 yf 內部人交易顯示的價格區間不一致 (見下方備註), 只能作為方向參考。

近期評等調整 (upgrade / downgrade / 目標價變動): 無可靠資料。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法存取 (WebFetch 回傳錯誤, 來源不可用)。
- StockTwits: 無法存取 (api.stocktwits.com 無法解析, 需於 session 網路設定允許該網域)。
- X / 新聞搜尋: 單次搜尋結果品質低, 多為爬蟲頁面, 且部分內容指向 ARQQW 認股權證而非普通股。可辨識的標題包括「股價單日大漲」與「TipRanks 認為 Hold」等, 但無法確認日期與情緒量能。
- 提及量 (buzz volume): 無法量化, 無法與歷史基準比較。
- 散戶傾向: 無法判定 (bullish / bearish / mixed 皆無足夠樣本)。
- 主題: 無可靠樣本, 不作推論。

## Insider activity
Net 6mo (2026-05-17 至 2026-11-17): 公開市場買入 $0, 賣出約 $2.68M (以 yf 交易金額加總)。

| 期間 | 主要賣方 (職稱) | 交易金額 (USD M) | 備註 |
|---|---|---|---|
| 2026-06-22 | Jennifer Bers (Officer) | 0.18 | 賣出 8,288 股, 單價 $21.42 |
| 2026-06-30 | Patrick Willcocks (General Counsel) | 0.12 | 賣出 4,000 股, 單價 $29.48 |
| 2026-07-01 | Manfredi Lefebvre d'Ovidio (Director, 間接持有) | 1.64 | 賣出 54,444 股, 單價 $30.07–30.24 |
| 2026-07-02 | Andrew Leaver (CEO) 等多人 | 0.38 | CEO 賣出 9,893 股, 單價 $25.20; 另有 CFO 以外高管與董事同步賣出 |
| 2026-10-02 至 10-13 | Andrew Leaver (CEO) 及其他高管、董事 | 0.37 | 多日連續小額賣出, CEO 最大單 2,818 股 @ $24.47 (10/2); 10/13 CEO 另賣 2,573 股 @ $16.40 |

關鍵觀察:
- 賣方以 CEO Andrew Leaver 與 General Counsel Patrick Willcocks 為主, 幾乎每批次都有 CEO 參與, 呈現系統性 (可能為 10b5-1 計畫或稅務相關) 的賣出節奏, 但資料無法確認計畫性質。
- 交易單價從 2026-07 的約 $25–30 下滑至 2026-10 的約 $16–24, 高管在股價下跌過程中仍持續賣出。
- 無任何 CEO / CFO 公開市場買入紀錄。
- 非公開市場的權證 / 選擇權轉換 (strike $2.50) 不計入買賣: 2026-06 Calabria、Ritchie 轉換, 2026-09-22 Lefebvre d'Ovidio 轉換 4.6M 股 (yf 顯示金額 $11.5M 為行權價 × 股數, 非市價成交額)。若將轉換視為「持有者變現」訊號需保留, 但不應當成買入。
- 2026-04 另有 CFO 與 CEO 等多人賣出 (合計約 $0.2M), 超出 6 個月窗口, 不計入。

## Ownership shifts
- 機構持股比例: 80.6% (機構持股計 97 家)。
- 內部人持股比例: 4.3%。
- 僅有單一時點快照, 無法判斷機構集中度趨勢 (增持或減持)。

## Net sentiment score
Composite: **bearish (信心低)**

依據:
- 內部人淨賣出 (約 $2.68M, 無公開市場買入) 為主要偏空訊號。
- 分析師端僅有落後數週的 Hold 共識, 不構成明確偏多或偏空。
- 散戶端無資料, 無法納入加權。
- 機構持股高 (80.6%) 屬中性偏穩定指標, 不足以翻轉偏空結論。

Divergence flag: **無法判定** — 散戶傾向無資料, 無法比較與分析師傾向是否相反。

## 資料缺口與來源衝突
1. yf `recommendations` / `rec_summary` 為空, 分析師資料需以次級來源補足, 且時效不足。
2. Reddit 與 StockTwits 不可用, 散戶面向完全缺失。
3. 價格資料衝突: TipRanks 搜尋摘要顯示最近價格約 $40.73, 但 yf 內部人交易顯示 2026-10 成交價約 $16–24, 兩者無法調和。本報告以 yf 交易單價為準, 不引用搜尋摘要中的現價。
4. MarketBeat 摘要稱 90 天內內部人賣出 70,785 股 / $2.07M, 與本報告以 yf 加總的 6 個月窗口數字不同 (窗口與來源計算基準不同), 未採用其數字。
5. 搜尋結果中的「單日上漲 131%」等標題日期不明, 未納入判斷。

## 建議後續補件
- 於 session 網路設定允許 reddit.com 與 api.stocktwits.com 後重新抓取散戶資料。
- 以可靠來源 (如 yf 可用時重試) 補抓 `recommendations` 與 `rec_summary`, 確認 2026-11 的評等分布與目標價。

SENTIMENT REPORT COMPLETE
