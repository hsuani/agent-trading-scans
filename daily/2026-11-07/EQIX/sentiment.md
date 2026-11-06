# Sentiment — EQIX (Equinix Inc) as of 2026-11-07

## Executive summary

- 分析師共識明顯偏多：yf rec_summary 顯示 30 buy / 5 hold / 0 sell（共 35 家），近三個月 buy 家數由 27 增至 30，hold 由 6 降至 5，無任何 sell 評等。
- 散戶社群情緒無法量化：Reddit（WallStreetBets、r/stocks）與 StockTwits 在本次執行環境皆無法連線，WebSearch 找到的 Reddit 相關資料僅為 2025 年 5 月的快照，不可作為當前依據。
- 內部人交易資料為空（yf insider 回傳空陣列），無法確認為「零交易」或「資料缺漏」，本報告視為「資料不可得」，不作為偏多或偏空證據。
- 機構持股僅有單一時點快照（institutionsCount 2006、機構持股比例約 100.4%，超過 100% 顯示資料口徑有問題），無法判斷機構集中度趨勢。
- 綜合判斷：偏多（信心低），主要依據單一來源的分析師評等，其他三個維度皆資料不足。

## Data availability

| 資料來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations | 部分可用 | 回傳為四個時間點的評等彙總（0m / -1m / -2m / -3m），非逐筆升降評等歷史，無法列出具體 upgrade / downgrade 事件與目標價變動 |
| yf rec_summary | 可用 | 當期 35 家分析師分布 |
| yf insider | 空陣列 | 回傳 []，Yahoo cookie / crumb 取得失敗，無法確認是否為真實零交易 |
| yf major_holders | 部分可用 | 有 insidersPercentHeld、institutionsPercentHeld、institutionsCount，無歷史序列 |
| Reddit r/wallstreetbets | 不可用 | WebFetch 無法連線 www.reddit.com |
| Reddit r/stocks | 不可用 | 同上 |
| StockTwits | 不可用 | api.stocktwits.com DNS 解析失敗（ENOTFOUND），需於 session 網路設定中允許該網域 |
| WebSearch（新聞 / 意見） | 部分可用 | 多數結果無日期或為模板化頁面，可信度有限；僅引用可辨識來源 |

依任務規則，yf 與 WebSearch 之外未使用其他金融網站資料。

## Retail / social sentiment read

- 散戶聲量（buzz volume）：無法評估。Reddit 與 StockTwits 皆未取得資料，不提供「高於或低於平常」的定性判斷。
- 散戶傾向（tilt）：無法判定。
- 唯一找到的 Reddit 相關資料為 ChartExchange 的 EQIX 提及追蹤頁（快照時間為 2025 年 5 月，已過時），其中有一則 r/stocks 留言把 EQIX 與 AI 基礎設施股在財報後的上漲連結起來。此資料僅供參考，不反映 2026-11 的散戶情緒。
- 次要敘述（WebSearch 來源，非社群原文）：部分文章提到 EQIX 的 P/FFO 倍數偏高可能限制短期上漲空間，另有文章指出資本密集、利率上升時融資成本可能增加。這些是媒體或分析性文章的觀點，不代表散戶立場。
- 主要主題（僅就可取得的非社群資料歸納）：AI 資料中心需求、估值（P/FFO）、利率敏感度。

## Analyst consensus

當期分布（yf rec_summary，0m）：

| 評等 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 6 | 17.1% |
| Buy | 24 | 68.6% |
| Hold | 5 | 14.3% |
| Sell | 0 | 0% |
| Strong Sell | 0 | 0% |
| 合計 | 35 | 100% |

近期趨勢（yf recommendations，四個時間點）：

| 時間點 | Buy（SB + B） | Hold | Sell | 合計 |
|---|---|---|---|---|
| 0m（當期） | 30 | 5 | 0 | 35 |
| -1m | 30 | 5 | 0 | 35 |
| -2m | 28 | 6 | 0 | 34 |
| -3m | 27 | 6 | 0 | 33 |

- 近三個月 buy 家數淨增 3 家，hold 淨減 1 家，無 sell 評等出現。
- 近一個月評等分布未變動。
- 逐筆升降評等與目標價變動：yf 工具未回傳具體事件，無法列出。
- 交叉驗證：WebSearch 引用的 Barchart 文章寫為 31 家（21 Strong Buy、3 Moderate Buy、7 Hold），與 yf 的 35 家（6 SB、24 B、5 H）數字不一致，且該文章日期不明。本報告以 yf 當期數據為準，並註記此差異。PriceTargets.com 的 consensus 描述為 Moderate Buy（28 家），亦與 yf 的分布存在口徑差異。
- 目標價：未取得可驗證的目標價數字，不予引用。

## Institutional / insider signal

內部人交易（insider）：
- 6 個月淨買賣：無法判定。yf insider 回傳空陣列，無法區分「無交易」與「取數失敗」。
- 本報告不列出任何具體 CEO / CFO 交易，因無可驗證資料。

機構與持股結構（yf major_holders，單一時點）：
- insidersPercentHeld：約 0.27%（內部人持股比例極低，對內部人情緒的解讀受限）。
- institutionsPercentHeld：約 100.4%，超過 100%，屬 Yahoo 持股口徑的資料異常（機構持股與內部人持股可能重複計算），不可直接解讀為機構持股過度集中。
- institutionsCount：2006 家。
- 機構持股趨勢：無歷史序列，無法判斷增持或減持方向。

## Overall sentiment verdict

- 分析師面：偏多（信心：中高，單一來源，且當期數據與媒體引用數字不一致）。
- 散戶面：無法判定（Reddit / StockTwits 皆不可用，僅有過時資料）。
- 內部人面：無法判定（insider 資料為空陣列）。
- 機構面：無法判定（僅有單一快照，且持股比例數值有口徑問題）。

綜合情緒分數：**偏多（信心低）**。判斷主要基於分析師評等結構（0 sell、30 buy），其餘三個維度皆資料不足，因此綜合信心受限。

背離旗標（retail vs analyst）：**無法判定**。散戶傾向不可得，無法檢驗是否與分析師方向相反。若日後取得散戶資料，建議優先比對 StockTwits 與 Reddit 的當期 tilt 與分析師偏多之間是否背離。

資料缺口與補充建議：
1. 允許 api.stocktwits.com 與 www.reddit.com 網域後重跑散戶面。
2. 重新取得 yf insider（需解決 Yahoo cookie / crumb 問題），以確認內部人交易是否為零。
3. 若需要升降評等與目標價歷史，需確認 yf recommendations 是否有逐筆模式可用。

## Sources

- yf 工具（本地）：`pipeline/tools/yf.py EQIX recommendations`、`rec_summary`、`insider`、`major_holders`，執行日期 2026-11-06 / 2026-11-07 環境
- WebSearch 結果（僅引用可辨識的來源，數字已與 yf 交叉比對，未直接採用其數字）：
  - [Barchart: Are Wall Street analysts predicting Equinix stock will climb or sink](https://www.barchart.com/story/news/277289/are-wall-street-analysts-predicting-equinix-stock-will-climb-or-sink)
  - [PriceTargets.com: NASDAQ EQIX consensus](https://www.pricetargets.com/NASDAQ/EQIX)
  - [TipRanks: EQIX stock analysis](https://www.tipranks.com/stocks/eqix/stock-analysis)
  - [ChartExchange: NASDAQ EQIX Reddit trends（2025 年 5 月快照）](https://chartexchange.com/symbol/nasdaq-eqix/trends/reddit)
- 未能取得：Reddit（r/wallstreetbets、r/stocks）、StockTwits（api.stocktwits.com）

SENTIMENT REPORT COMPLETE
