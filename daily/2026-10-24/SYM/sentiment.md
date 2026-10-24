# Sentiment — SYM as of 2026-10-24

資料來源狀態: yf 工具 (rec_summary、recommendations、insider、major_holders) 可用。Reddit (r/wallstreetbets、r/stocks) 與 StockTwits 無法取得即時資料, 本次社群情緒為缺漏。WebSearch 找到的社群與新聞資料多為 2024–2026 年初, 不代表當前情緒。

## Analyst consensus

9 buy (1 strong buy + 8 buy) / 5 hold / 3 sell (2 sell + 1 strong sell), 共 17 家券商。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 目前 (0m) | 1 | 8 | 5 | 2 | 1 | 17 |
| 1 個月前 (-1m) | 1 | 8 | 5 | 2 | 1 | 17 |
| 2 個月前 (-2m) | 1 | 9 | 5 | 2 | 1 | 18 |
| 3 個月前 (-3m) | 1 | 9 | 5 | 2 | 1 | 18 |

近期變動: 過去約 2 個月, 買進側 (strong buy + buy) 由 10 家降至 9 家, 持有與賣出家數未變, 總家數由 18 降為 17。工具只提供彙總計數, 無法確認是評等下調、還是覆蓋中止 (coverage drop)。`recommendations` 工具回傳的也是同一組彙總計數, 沒有逐筆升降評等紀錄。

目標價: yf 工具未提供目標價。WebSearch 找到的彙總頁為 2026 年初資料, 共識目標價約 US$65.56 (區間 US$42–83), 且 Goldman Sachs 於 2026 年 1 月上調至 US$50。此資料已過時, 且與本報告內部人成交價推算的現價區間 (約 US$43) 相差很大, 僅供參考, 不應作為當前目標價依據。

## Retail social

- Reddit: 無法取得。WebFetch 對 r/wallstreetbets 與 r/stocks 的搜尋 JSON 皆回傳錯誤 (無法連線 reddit.com)。以 WebSearch 查 r/wallstreetbets 相關討論, 也找不到 2026 年的 SYM 討論串。討論量與傾向: 無法判斷。
- StockTwits / X: StockTwits 回傳 DNS 解析失敗 (api.stocktwits.com), 無法取得訊息流。X 上無 2026 年 10 月的相關可用結果。
- 聲量 (mention volume): 無法量化, 不寫出假定數字。
- 引言樣本: 無 (無 2026 年貼文可引用)。
- 傾向: 無法判定 (bullish / bearish / mixed 皆無足夠證據)。

Themes (歷史背景, 來自 WebSearch 的 2023–2025 文章, 非當前資料):
- 估值: 2024 年有分析師指出前瞻 P/S 超過 7 是主要疑慮。
- 客戶集中: 2023 年文章指出單一客戶在某季佔營收約 89%。
- 營運: 長交期 (約 24 個月) 與 CFO 多次更替, 常被列為空方論點。
- 空單: 2025 年多個快照顯示 short interest 約佔流通股 28%–37%。

## Insider activity

資料期間: 2026-04-24 至 2026-10-24 (6 個月)。金額為 USD, 以工具回傳的成交價值加總。

淨額 6mo: 買入 US$0 / 賣出 約 US$293.9M (其中 US$281.8M 為 SoftBank 單筆; 不含 SoftBank 約 US$12.1M)。淨流出 約 US$293.9M。
資料範圍 (2025-01 至 2026-10) 內, 未見任何公開市場買入 (Purchase) 紀錄, 只見獎勵 (Stock Award)、贈與 (Stock Gift) 等非交易類紀錄。

| 人員 | 職稱 | 有價賣出筆數 | 賣出金額 (USD M) | 未定價筆數 | 備註 |
|---|---|---|---|---|---|
| SoftBank Group Corp | 10% 以上持股者 | 1 | 281.8 | 0 | 2026-05-27 以 US$50.42 賣出 5,590,000 股 |
| Todd J. Krasnow | Director | 9 | 3.59 | 0 | 2026-05 單日兩筆合計約 US$2.75M |
| Charles F. Kane | Director | 7 | 0.66 | 0 | 定期小額賣出 |
| James J. Kuffner Jr. | CTO | 4 | 2.31 | 3 | 2026-04 至 08 持續賣出 |
| Brian D. Alexander | Officer | 2 | 2.64 | 1 | 2026-04-24 單筆 37,860 股 (約 US$2.27M) |
| William M. Boyd III | Officer | 4 | 1.43 | 1 | 2026-04 與 07 皆有賣出 |
| Izilda P. Martins | CFO | 1 | 1.12 | 1 | 2026-07-27 賣出 27,463 股 (US$40.80) |
| Maria G. Freve | Officer | 3 | 0.36 | 1 | 小額 |
| Andrew D. Ross / Eric Branderiz | Director | 0 | 0 | 2 | 僅未定價紀錄 (推測為權利股或行權相關, 無法確認) |

Notable:
- CFO Izilda P. Martins 於 2026-07-27 賣出 27,463 股, 約 US$1.12M。
- CEO Richard B. Cohen 在窗口內無交易。上一筆為 2025-12-11 贈與 1,000,000 股 (非賣出)。
- 多筆 Krasnow、Kane 的小額賣出以固定股數重複出現, 可能為預定交易計畫 (10b5-1), 但工具資料無法確認。
- 未定價紀錄集中於同日多人 (如 2026-07-23 共 5 人), 通常屬於權利股歸屬或稅款預扣類型, 不計入金額。

成交價推算 (內部人成交價, 非即時報價): 2026-01 約 US$60–69; 2026-04 至 05 約 US$50–60; 2026-07 至 08 約 US$40–46; 2026-09 至 10 約 US$39–44。顯示股價於 2026 年下半年明顯回落。

## Ownership shifts

- 內部人持股: 13.6%
- 機構持股: 79.4% (流通股中佔 91.9%), 機構數 555 家
- 大股東: SoftBank 為 10% 以上持股者, 在 2025-12 與 2026-05 皆有大額賣出; RBC Millennium GST Non-Exempt Trust 在 2025-08 有 220,000 股賣出; David A. Ladensohn 為 10% 以上持股者, 2025 年有多筆賣出。
- 趨勢: yf 工具只提供當前快照, 無法判斷機構集中度的變化方向。持股變動趨勢: 無法判斷。

## Net sentiment score

Composite: **中性偏空 (信心低)**

- 分析師面: 中性偏多。9 買 / 5 持有 / 3 賣, 近期買進側由 10 降為 9。
- 內部人面: 偏空。6 個月內零買入, 賣出約 US$293.9M, 含 SoftBank 單筆 US$281.8M; 不含 SoftBank 也有約 US$12.1M, 且多為高階主管與董事的連續賣出。
- 散戶面: 無有效資料, 不計入評分。
- 信心低的原因: 社群資料缺漏, 目標價資料過時, 且內部人賣出無法區分是否為預定交易計畫。

Divergence flag: **無法判定 (散戶資料缺漏)**。分析師偏多與內部人淨賣出之間存在分歧, 這是「分析師 vs. 內部人」的分歧, 並非「散戶 vs. 分析師」的分歧, 後者因缺少 Reddit 與 StockTwits 資料而無法評估。

資料缺口與後續建議:
- Reddit、StockTwits 恢復後應重跑散戶部分。
- 目標價需要即時來源 (例如 yf 目標價欄位或券商報告) 補足。
- 機構持股的季度變化需要 13F 比對才能判斷趨勢。

SENTIMENT REPORT COMPLETE
