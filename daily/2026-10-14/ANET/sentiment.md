# Sentiment — ANET as of 2026-10-14

## Analyst consensus
31 buy（含 7 Strong Buy）/ 1 hold / 0 sell（yf rec_summary，期間 0m）。
近三個月趨勢：buy 由 22 升至 24，hold 由 1 降至 0 再回到 1，整體結構穩定，無明顯評等轉向。
Recent moves（升降評等明細）：DATA_UNAVAILABLE（yf recommendations 只回傳彙總計數，無逐筆 upgrade / downgrade 紀錄）。
目標價：DATA_UNAVAILABLE 於 yf 工具內。外部來源（StockAnalysis，2026-08-05 快照）顯示 12 個月平均目標價約 228.61 美元，共 30 家分析師。另有網路摘要提及 Evercore ISI 將目標價由 200 上調至 250 美元，日期未確認。

## Retail social
- Reddit: DATA_UNAVAILABLE。r/wallstreetbets 與 r/stocks 的 public JSON 抓取遭封鎖（回傳無法存取）。以搜尋引擎補查亦未找到 ANET 相關的 Reddit 討論串，故無法判斷樣本與語氣傾向。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 解析失敗（ENOTFOUND），依規則軟性失敗、略過。
- X / 新聞輿論: 以 WebSearch 搜尋僅得到財經新聞與資料聚合站，未取得可辨識的 X 貼文樣本。
- 聲量（buzz volume）: DATA_UNAVAILABLE，無法給出與常態相比的提及次數。
- 近期價格背景: 依 2026-10-08 快照，Google Finance 收盤價約 210.97 美元（單日跌 2.25%），52 週區間約 114.52 至 217.32 美元。此為 10-08 資料，非 10-14 即時報價。
- Themes（由新聞與分析文章歸納，非零售貼文本身）:
  - AI 資料中心需求帶動的成長敘事，為最常見的多方論點。
  - 毛利率承壓，記憶體成本上升為主要空方論點（TIKR 等文章提及）。
  - FY26 指引是否只是符合共識、出貨與營收認列時點波動，為次要疑慮。
- 零售語氣（bullish / bearish / mixed）: DATA_UNAVAILABLE。

## Insider activity
統計區間：2026-04-14 至 2026-10-14（yf insider，資料最新至 2026-10-09）。
Net 6mo: $0 buys、約 $1,366M sells（Sale 類交易，約 43 筆）。
以 Form 4 「Sale at price」計，不含 「Conversion of Exercise」（選擇權行使，共數筆、金額小）與無金額之獎勵股登記。

Notable:
- Jayshree Ullal，CEO：6 個月內 15 筆賣出，約 403 萬股，約 7.79 億美元（最近一筆 2026-10-09，約 217 美元）。
- Andreas Bechtolsheim，10% 以上實質持有人：11 筆賣出，約 304 萬股，約 5.45 億美元（最近一筆 2026-09-17）。
- Kenneth Duda，President：4 筆賣出，約 18.8 萬股，約 3,371 萬美元，另有多筆選擇權轉換。
- Chantelle Breithaupt，CFO：4 筆賣出，約 1.3 萬股，約 215 萬美元。
- 董事（Mark Templeton、Charles Giancarlo、Yvonne Wassenaar、Kelly Battles）：小額賣出，合計約 650 萬美元以下。
- 解讀注意: 資料未標示 10b5-1 計畫，無法判斷賣出是否屬預先排定。Insider 賣出在股價高檔時常見，訊號強度有限。6 個月內無任何公開市場買入。

## Ownership shifts
- 內部人持股比例: 17.25%
- 機構持股比例: 73.33%；機構流通股佔比: 88.62%
- 機構家數: 3,133
- 趨勢（季度間變化）: DATA_UNAVAILABLE。yf major_holders 僅回傳當期快照，無法比較前期。

## Net sentiment score
Composite: 中性（neutral），信心度低至中。
- 分析師：偏多，信心度高（31 買 / 1 持有 / 0 賣，結構穩定）。
- 內部人：淨賣出規模大（約 13.7 億美元，零買入），偏空訊號，但需扣除常態性賣出與 10b5-1 可能性，信心度中。
- 零售：無資料，無法納入加權。

Divergence flag: 無法判定（零售資料缺失，DATA_UNAVAILABLE）。
需注意的是機構分析師與內部人方向不一致：分析師普遍看多，而 CEO 與大股東在近期高點持續賣出。此為機構內部的分歧，而非零售與機構之間的分歧。

## 指標表

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師 Buy（含 Strong Buy） | 31（7 Strong Buy + 24 Buy） | yf rec_summary，0m |
| 分析師 Hold | 1 | yf rec_summary，較 3 個月前 1 持平，較 2 個月前減 1 |
| 分析師 Sell / Strong Sell | 0 / 0 | yf rec_summary |
| 平均目標價 | 約 228.61 美元（2026-08-05 快照） | 外部來源（StockAnalysis），yf 內 DATA_UNAVAILABLE |
| 近期升降評等明細 | DATA_UNAVAILABLE | yf recommendations 僅回傳彙總 |
| 6 個月內內部人買入金額 | 0 美元 | yf insider，2026-04-14 起 |
| 6 個月內內部人賣出金額 | 約 13.66 億美元（約 43 筆 Sale） | yf insider，不含選擇權轉換 |
| CEO 6 個月賣出金額 | 約 7.79 億美元 | yf insider，Jayshree Ullal |
| CFO 6 個月賣出金額 | 約 215 萬美元 | yf insider，Chantelle Breithaupt |
| 10% 以上持有人賣出金額 | 約 5.45 億美元 | yf insider，Andreas Bechtolsheim |
| 內部人持股比例 | 17.25% | yf major_holders |
| 機構持股比例 | 73.33% | yf major_holders |
| 機構流通股佔比 | 88.62% | yf major_holders |
| 機構家數 | 3,133 | yf major_holders |
| 機構持股季度變化 | DATA_UNAVAILABLE | 無歷史快照 |
| Reddit 提及數 / 語氣 | DATA_UNAVAILABLE | 抓取遭封鎖，搜尋無結果 |
| StockTwits 訊息與多空比 | DATA_UNAVAILABLE | DNS 解析失敗 |
| X 貼文聲量 | DATA_UNAVAILABLE | 僅新聞類結果 |
| 最近收盤價（參考） | 約 210.97 美元（2026-10-08） | 外部來源（Google Finance），非 10-14 報價 |
| 52 週區間（參考） | 約 114.52 至 217.32 美元 | 外部來源，2026-10-08 |
| 綜合情緒 | 中性（信心度低至中） | 本報告判定 |
| 分歧旗標 | 無法判定 | 零售資料缺失 |

## 資料來源與限制
- yf（ANET rec_summary / recommendations / insider / major_holders）：Yahoo cookie 與 crumb 取得失敗，改以快取或無 crumb 模式回傳，屬正常降級流程。
- Reddit：WebFetch 無法存取 www.reddit.com，軟性失敗。
- StockTwits：api.stocktwits.com DNS 解析失敗，軟性失敗。
- X / 新聞：WebSearch 結果多為 2026 年 8 月前後的快照，未找到 2026-10-14 當日的新聞或輿論，時效性有限。

SENTIMENT REPORT COMPLETE
