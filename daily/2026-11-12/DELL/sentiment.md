# Sentiment — DELL as of 2026-11-12

> 資料時點注意: 執行環境日期為 2026-11-11, 本報告以要求的 2026-11-12 為 as-of 日期。yf 資料為工具當下回傳值, 最新一筆內部人交易為 2026-10-22。

## Analyst consensus

29 家覆蓋: 6 strong buy / 14 buy / 9 hold / 0 sell / 0 strong sell (當期 0m)。買進系 20 家 (約 69%), 持有 9 家 (約 31%), 無賣出評等。

近四期趨勢 (買進系 / 持有):
| 期間 | 買進系 | 持有 | 賣出 |
|---|---|---|---|
| 0m (當期) | 20 | 9 | 0 |
| -1m | 19 | 10 | 0 |
| -2m | 20 | 9 | 0 |
| -3m | 19 | 9 | 0 |

Recent moves: yf `recommendations` 只回傳彙總分佈, 未提供個別券商升降評與目標價變動清單, 無法逐家確認近期 upgrade / downgrade。結構上穩定, 月度間僅 ±1 家在買進與持有間移動。網路搜尋結果中有數則關於單一券商降評的報導, 但日期互相矛盾 (部分為 2025 年內容), 無法確認為本期事件, 本報告不採用。

## Retail social

- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 JSON 端點 (WebFetch 與 curl 皆失敗, 連線回傳 000 / 被擋)。Soft-fail, 無貼文樣本與情緒比例。
- StockTwits / X: StockTwits 端點 DNS 解析失敗 (api.stocktwits.com 不在本 session 允許網域內), 無法取得訊息流。須於 session 網路設定允許該主機後才能補抓。
- X / 新聞搜尋: 一則彙整型搜尋摘要 (Quiver Quantitative 引述) 描述社群情緒為「mixed」, 近期有下滑但仍有長期成長敘事。來源時間戳不一致, 僅作為定性參考, 不計入量化分數。
- 聲量相對基準: 無法量化 (缺 Reddit / StockTwits 數據)。
- 情緒傾向: 無法判定, 信心低。
- Themes (僅來自搜尋摘要的定性描述, 未經貼文直接驗證): AI 伺服器需求與營收指引、記憶體成本與毛利率壓力、估值與回檔買點討論。

## Insider activity

資料窗口: yf `insider` 回傳 150 筆, 日期範圍僅 2026-07-06 至 2026-10-22。6 個月窗口 (2026-05-12 至 2026-11-12) 中 2026-05-12 至 2026-07-05 的交易未出現在回傳資料中, 故下列數字為「可見期間」的下限估計。

Net 6mo (可見期間, USD): 買進 $0M, 賣出約 $1,054M (約 $1.05B)。非公開市場交易 (配股、授予、轉換) 另計 73 筆, 不計入買賣金額。

| 申報人 | 角色 | 筆數 | 淨額 (USD M) |
|---|---|---|---|
| Silver Lake Partners IV, LP. | 10% 以上持股人 (部分申報為 Director) | 13 | -400.2 |
| SL SPV-2, L.P. | 10% 以上持股人 / Director | 13 | -368.0 |
| Silver Lake Partners V DE AIV, L.P. | 10% 以上持股人 (部分申報為 Director) | 13 | -212.6 |
| Silver Lake Technology Investors IV / V | 10% 以上持股人 | 28 | -12.8 |
| Peter Trizzino | Officer | 1 | -21.1 |
| David Alan Kennedy | Chief Financial Officer (CFO) | 1 | -14.0 |
| Jennifer D. Saavedra | Officer | 1 | -13.1 |
| Richard Jay Rothberg | General Counsel | 2 | -5.6 |
| Lynn Vojvodich Radakovich | Director | 4 | -3.8 |
| Jane Tunnell | Officer | 1 | -2.8 |

Notable: Silver Lake 相關實體 (10% 以上持股人) 自 2026-07 起分批出售, 單筆價格區間約 $405 至 $591 (2026-07-06 至 2026-10-09), 2026-10-22 Director Radakovich 以 $460 出售。全數為賣出, 無任何公開市場買進。高階主管賣出包括 CFO David Alan Kennedy (2026-09-17, 約 $585 每股, 約 $14.0M) 與 General Counsel Richard Jay Rothberg (2026-09 兩筆)。工具資料未見 CEO 的公開市場交易。Silver Lake 的賣出規模大, 但其持股人身分與分批執行特徵 (多日、固定區間) 顯示較可能是基金退出 / 流動性安排, 而非對公司前景的方向性判斷。

資料驗算: Silver Lake Partners IV 2026-10-06 單筆 54,236 股 / $31,198,621 ≈ $575 每股, 與申報價格區間相符。

## Ownership shifts

- 內部人持股: 7.7%
- 機構持股: 77.7% (流通股中約 84.2%)
- 機構家數: 2,943
- 趨勢: 工具僅回傳單一時點快照, 無法判定機構集中度變化方向。Silver Lake 的減持若持續, 會影響 10% 持股人結構, 值得後續追蹤。

## Net sentiment score

Composite: **中性 (信心低)**

- 分析師面: 偏多。買進系 20 / 29 (約 69%), 零賣出評等, 結構連續數月穩定。
- 內部人面: 偏空 (但以基金退出為主)。可見期間 $1.05B 賣出、零買進, 主要來自 Silver Lake 相關實體。
- 散戶面: 無資料, 不計分。定性描述為 mixed。

Divergence flag: **無法判定 (散戶資料缺失)**。但分析師與內部人方向相反已成立: 分析師偏多, 內部人持續賣出 (主要為大股東退出)。此分歧需以持股人身分與交易結構解讀, 不宜直接視為看空訊號。

資料缺口清單 (補抓後可更新本報告):
1. Reddit (r/wallstreetbets, r/stocks) 網路封鎖, 需 session 網路允許或改用其他來源。
2. api.stocktwits.com DNS 解析失敗, 需加入 session 允許網域。
3. yf `insider` 僅覆蓋 2026-07 起, 5 月至 6 月交易需補抓。
4. yf `recommendations` 無個別券商評等變動明細, 需其他來源確認近期升降評與目標價。

SENTIMENT REPORT COMPLETE
