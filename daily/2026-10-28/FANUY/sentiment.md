# Sentiment — FANUY (Fanuc ADR) as of 2026-10-28

資料狀態總覽: 分析師評等部分可用 (樣本極少); 內部人交易 DATA_UNAVAILABLE (空結果); 散戶社群 DATA_UNAVAILABLE (Reddit 與 StockTwits 皆無法存取); 機構持股僅單一快照。

## Analyst consensus

Yahoo rec_summary (當期 0m) 統計: **1 strong buy / 0 buy / 1 hold / 0 sell / 0 strong sell**, 共 2 位分析師, 樣本極小, 統計可信度低。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (當期) | 1 | 0 | 1 | 0 | 0 |
| -1m | 0 | 0 | 2 | 0 | 0 |
| -2m | 0 | 0 | 2 | 0 | 0 |

- 近期變化: 評等分布由 -1m 的 2 hold 轉為當期 1 strong buy + 1 hold, 代表一位分析師評等上調至 strong buy。**DATA_UNAVAILABLE**: 無法取得具體升降評等事件、日期與券商名稱。`yf recommendations` 回傳內容與 rec_summary 完全相同 (只有月度計數, 無事件清單)。
- 目標價: Yahoo 1 年目標價估計 $21.72 (來源為 WebSearch 摘錄, 日期不明, 非 yf 工具直接輸出)。**DATA_UNAVAILABLE**: 目標價變動歷史。
- 次要引用: Pluang 轉引 Seeking Alpha (2026-10-08) 維持 Buy 評等, 理由為工廠自動化與機器人銷售受美國回流與日本需求帶動。此為二手轉述, 未核對原文。

## Retail social

- **Reddit** (r/wallstreetbets, r/stocks): **DATA_UNAVAILABLE**。WebFetch 回報無法存取 www.reddit.com, 無法取得 FANUY 相關串文、分數或留言語氣。
- **StockTwits**: **DATA_UNAVAILABLE**。api.stocktwits.com DNS 解析失敗, 目前雲端 session 網路白名單未允許此網域。需於 session 網路設定中允許後才能重試。
- **X / 新聞聲量 (WebSearch 兩次)**: 未找到任何散戶論壇或 Reddit 討論串。搜尋結果以市場資料頁與分析師摘要為主, 無法判斷聲量相對於平常水準的高低。
- **Retail 語氣**: DATA_UNAVAILABLE (無樣本可分類為偏多 / 偏空 / 混合)。
- **Themes (僅來自分析師與新聞來源, 非散戶)**: 工廠自動化需求、美國製造回流、日本需求、機器人銷售成長、AI / physical AI 題材 (roic.ai 有一則未標日期的升評等摘要提及此項)。
- **引述 (新聞來源, 非散戶)**: 「factory automation and robot sales grow strongly」 (Pluang 轉引 Seeking Alpha, 2026-10-08)。

## Insider activity

Net 6mo: **DATA_UNAVAILABLE**。`yf insider` 回傳空陣列 `[]`, 無法區分「期間內無交易」與「抓取失敗 (Yahoo cookie/crumb 取得失敗, 僅靠 cache 回應)」。不應解讀為零內部人交易。
- Notable: 無。

## Ownership shifts

`yf major_holders` 單一快照 (無時間序列, 趨勢 DATA_UNAVAILABLE):
- insidersPercentHeld: 0.0
- institutionsPercentHeld: 0.00229 (約 0.23%; 此數值對 Fanuc 這類大型日股 ADR 偏低, 疑為 Yahoo 對 OTC ADR 的資料缺漏或單位問題, 不建議採信)
- institutionsCount: 27

機構集中度趨勢: DATA_UNAVAILABLE (無前期比較)。

## Other reference points (低可信度, 僅作背景)

- 基本面 (Webull 引述 FY Q1 截至 2026-06-30): 營收 ¥231,035 百萬, 淨利 ¥50,981 百萬, 皆年增。本益比約 40x, 被評為偏貴。
- 價格: investing.com 報 $19.02 (日期 2026-08-21), roic.ai 報 $20.91 (日期不明)。兩者皆非 2026-10-28 當日價格, 不採用。
- 財報日: Yahoo 顯示 2026-10-23, investing.com 顯示 2026-10-22, 兩者不一致。財報結果本身未核實。
- MarketBeat 的 days-to-cover 數字 (267 與 780 天) 明顯不合理, 已排除。

## Net sentiment score

**Composite: NEUTRAL (信心度: 低)**

- 分析師面: 偏正向但樣本僅 2 人 (1 strong buy + 1 hold), 且無升降事件細節, 權重低。
- 散戶面: 無資料 (DATA_UNAVAILABLE), 不計入評分。
- 內部人面: 無資料 (DATA_UNAVAILABLE), 不計入評分。
- 機構面: 僅 27 家機構的單一快照, 無趨勢, 不計入評分。

**Divergence flag: 無法判定** (散戶語氣缺失, 無法比較與分析師傾向的方向是否相反)。

## Data gaps

1. StockTwits/Reddit 皆無法存取。
2. `yf insider` 回傳空值。
3. `yf recommendations` 未提供事件級升降評等紀錄。
4. Yahoo cookie/crumb 失敗, 所有 yf 數值應視為待核實。

SENTIMENT REPORT COMPLETE
