# Sentiment — IONQ as of 2026-11-17

資料完整度：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 無法連線（Reddit 回傳無法存取，StockTwits 網域解析失敗，需於 session 網路設定允許 api.stocktwits.com）。零售情緒部分僅能以新聞與評論文章做間接判讀，無法量化提及量與原始貼文樣本。

## Analyst consensus

| 評級 | 家數 | 說明 |
|---|---|---|
| Strong Buy | 1 | yf 當期快照 |
| Buy | 11 | 含 B. Riley、Cantor Fitzgerald、Mizuho（Outperform） |
| Hold | 2 | 含 Morgan Stanley（Equal Weight）、DA Davidson（Neutral）為推測對應 |
| Sell | 0 | |
| Strong Sell | 0 | |

合計 14 家，買進相關評級占 12/14（約 86%）。過去 4 個月（0m 至 -3m）評級結構幾乎不變，僅 -3m 時 Buy 少 1 家，評級面無明顯轉向。

Recent moves（以 Q3 財報 2026-11-05 為中心，多為目標價下調而非評級變更）：
- B. Riley（11/02）：目標價 $100 → $75，維持 Buy。
- Cantor Fitzgerald（11/06）：目標價 $70 → $60，仍示有上行空間。
- Mizuho：目標價 $80 → $61，維持 Outperform（發布日期來源不明確）。
- Morgan Stanley（Joseph Moore）：目標價 $32 → $58，維持 Equal Weight，為財報前動作（來源日期有衝突，需再確認）。
- DA Davidson：目標價 $55，維持 Neutral（來源單一）。
- 未查得 11 月內確認的評級升級或降級。

共識目標價約 $64–70（來源間差異大，僅供參考）。方向上是「評級維持偏多、目標價普遍下修」。

## Retail social

- Reddit：無法取得 r/wallstreetbets 與 r/stocks 貼文，無法計算提及量與語氣分布。
- StockTwits / X：StockTwits 無法連線。X 無直接資料，僅透過新聞搜尋間接觀察。
- 新聞與評論流（非零售原始樣本）：11 月初因 Q3 前股價下跌約 32%（一個月內），評論多聚焦虧損與稀釋疑慮。財報後 11/06 股價大漲約 21–23%，情緒轉為正向，多篇文章以「beat and raise」為主軸。
- 疑慮：約 $2B 股權募資被視為稀釋風險，也被多篇文章提及。

Retail tilt：無法直接判定。間接觀察為「財報後偏多、前期偏空」，屬於混合。

Themes（依新聞與評論歸納）：
1. Q3 營收 $173.8M，年增 336%，2026 營收指引上修至 $505–515M（前值 $450–460M）。
2. 持續虧損與稀釋風險（$2B 募資）。
3. 量子股板塊情緒連動（RGTI、QBTS 同步大幅波動）。
4. 估值爭議（目標價下修與高波動並存）。

## Insider activity

6 個月窗口（2026-05-17 至 2026-11-17）：
- 買進：$0（無公開市場買進）
- 賣出：約 $0.60M（4 筆，皆為董事）
- 獎勵股（Stock Award）與衍生性證券轉換另計，不計入淨買賣金額

Notable：
- 2026-09-10，Director John W. Raymond，賣出 2,407 股，約 $0.09M，@ $37.21
- 2026-06-18，Director Kathryn K. Chou，賣出 2,757 股，約 $0.15M，@ $55.02
- 2026-06-18，Director Gabrielle B. Toledano，賣出 2,757 股，約 $0.15M，@ $55.01
- 2026-06-18，Director John W. Raymond，賣出 3,815 股，約 $0.21M，@ $55.01

CEO（Niccolo M. De Masi）與 CFO（Thomas G. Kramer）在 6 個月窗口內無交易紀錄（僅 2026-02-20 有 CEO 獎勵股）。最近一次董事公開市場買進為 2026-02-27 Director William J. Teuber Jr.，$0.12M，@ $38.38，已超出 6 個月窗口。

判讀：6 個月內無內部人買進，賣出集中於董事，金額相對小，屬輕度偏空訊號。獎勵股為常態薪酬發放，不視為看多或看空。

## Ownership shifts

- 機構持股：40.85%（institutionsPercentHeld）；流通股中機構占比 41.61%；機構家數 1,017。
- 內部人持股：1.83%。
- 限制：目前為單一時點快照，無法計算趨勢。機構集中度變化需跨期資料才能判定。

## Net sentiment score

- 分析師面：偏多（評級 86% 買進相關），但目標價普遍下修，價格面動能偏弱，判為「偏多但降溫」。
- 內部人面：輕度偏空（6 個月無買進，董事小額賣出）。
- 零售面：無法量化，間接資料為財報後轉正、前期偏空，混合。
- 綜合：**中性（信心：低）**。分析師評級偏多與內部人賣出相抵，零售面缺資料無法確認方向。

Divergence flag: **無法判定**。零售樣本缺失，無法確認零售傾向是否與分析師傾向相反。若日後取得 Reddit 或 StockTwits 資料，應優先重新評估此欄。

SENTIMENT REPORT COMPLETE
