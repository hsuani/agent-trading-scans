# Sentiment — FANUY as of 2026-10-25

**資料完整度: 低。** Reddit 與 StockTwits 皆無法取得,且分析師與內部人資料樣本極少。以下結論信心偏低。

## Analyst consensus
2 hold / 0 buy / 0 sell(yf rec_summary,0m 與近 1–2 個月皆相同)。近期升降評等: yf 歷史評等表僅回傳彙總計數,沒有逐筆升降評等紀錄,也沒有目標價變動資料。Yahoo cookie/crumb 取得失敗,但仍回傳資料,可信度需保留。

外部線索: 2026-10-08 有一則 Seeking Alpha 分析師 note 評為 "Buy",理由是 Factory Automation 成長與日本工具機訂單回升,robot 部門北美銷售年增 21%(依 Pluang 轉載)。這與 yf 的 2 hold 彙總不一致,可能是樣本期間或資料來源不同所致,未能釐清。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 回報 "unable to fetch from www.reddit.com"。
- StockTwits: 無法取得。DNS 解析失敗 (api.stocktwits.com ENOTFOUND)。
- X / 新聞: 搜尋未找到 2026-10 的散戶討論。找到的 MarketBeat 情緒分數日期不明且不一致,不採用。
- 聲量: 無法判斷,無樣本可比對。
- 傾向: 無法判斷(不是中性,是沒有資料)。
- 主題: 無可靠主題。

## Insider activity
Net 6mo: 無資料(yf insider 回傳空陣列)。空陣列也可能是資料缺漏而非真的沒有交易,不能當作「無內部人交易」的證據。FANUY 為 OTC ADR,內部人申報可能不在此來源內。

## Ownership shifts
- institutionsCount: 27
- institutionsPercentHeld: 0.229%(原始值 0.00229 為小數格式)
- insidersPercentHeld: 0%(原始值 0.0)

這些數字對 Fanuc 母公司而言明顯偏低,更像是 ADR 本身的持股統計,而非整體股權結構。趨勢: 無歷史序列,無法判斷增減。

## Net sentiment score
**綜合: 中性 (neutral),信心低。**
- 分析師面: 2 hold,0 buy,0 sell,偏中性;外部 2026-10-08 一則 Buy 偏多。
- 散戶面: 無資料。
- 內部人面: 無資料。
- 技術面 (非本 agent 範圍,僅作背景): 2026-08 Investing.com 日線訊號為 Strong Sell,資料已過時約兩個月。
- 近期事件: Investing.com 列出 2026-10-22 為財報日,但今日 (10-25) 未搜尋到財報結果或市場反應報導,是最大缺口。

**分歧旗標: 無法判定。** 沒有可靠的散戶傾向可與分析師比較,故不標記分歧。

## 建議後續補查
1. 補查 2026-10-22 財報結果與股價反應(Fanuc 官方 IR 或日文財經媒體)。
2. 補查 Reddit / StockTwits 替代來源(若代理環境允許)。
3. 確認 yf 的 2 hold 彙總與 Seeking Alpha Buy 評等的差異。

## Sources
- [Pluang: Fanuc 近期發展 (Seeking Alpha Buy 引述)](https://pluang.com/en/news-feed/perkembangan-terkini-fanuc-dan-data-menjanjikan)
- [Investing.com: Fanuc Corporation (FANUY)](https://www.investing.com/equities/fanuc-corporation)
- [MarketBeat FANUY](https://www.marketbeat.com/stocks/OTCMKTS/FANUY)

SENTIMENT REPORT COMPLETE
