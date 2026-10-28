# Sentiment — SO as of 2026-10-28

資料截止: 2026-10-28。晚於此日期的資料視為未知，未納入。

## Analyst consensus

目前分布 (rec_summary, 0m, 共 24 家): **8 buy / 13 hold / 3 sell**
- Buy 含 strongBuy 1 家；Sell 含 strongSell 1 家。
- Buy 占比約 33%，Sell 占比約 12.5%，多數為 Hold。

近四個月趨勢 (yf rec_summary 各期):

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 |
|---|---|---|---|---|---|---|
| 0m (目前) | 1 | 7 | 13 | 2 | 1 | 24 |
| -1m | 1 | 6 | 14 | 2 | 0 | 23 |
| -2m | 1 | 6 | 13 | 2 | 1 | 23 |
| -3m | 1 | 6 | 14 | 2 | 1 | 24 |

近期變化: 目前 buy 側 (strongBuy + buy) 由 7 增至 8；sell 側 (sell + strongSell) 由 2 增至 3，strongSell 首次出現於目前期。整體仍以 Hold 為主。

限制: yf 的 `recommendations` 指令回傳與 `rec_summary` 相同的彙總計數，無逐家券商的升降評等歷史，故無法列出個別 upgrade/downgrade 紀錄。

目標價 (網頁搜尋，未經 yf 驗證，時間戳不一，僅供參考):
- Scotiabank 由 Outperform 降至 Sector Perform，目標價 $99 (日期 DATA_UNAVAILABLE，來源頁無日期)。
- Mizuho Buy，目標價 $106，資料日期約 2026-07-31 (Investing.com 摘要)。
- Morgan Stanley Underweight，目標價 $92 (2026-04 前後，網頁摘要)。
- 2026-10-13 前後 BofA 與 JPMorgan 下調觀點，理由為成本疑慮與 Q2 營收不及預期 (網頁摘要標示 Tradingpedia 2026-10-15)。**此項無法開啟原文核實，標為未驗證。**
- 市場共識目標價約 $100.93 (Investing.com)；另一來源 $91.48 (Benzinga) 疑為 2025 年資料，已過時。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。兩個 search.json 端點均回傳 "unable to fetch"，本次無法取得貼文、分數、留言數或情緒傾向。
- **StockTwits**: DATA_UNAVAILABLE。`api.stocktwits.com` DNS 解析失敗 (需在 session 網路設定中允許此網域)。
- **X / 新聞聊天**: 網頁搜尋未找到 2026-10 有明確日期的散戶情緒文章。搜尋結果多為自動生成頁或 2026 年 4-5 月舊文，不採用。
- **聲量 (buzz volume)**: DATA_UNAVAILABLE。無法做量化提及數與基準比較。
- **散戶傾向**: DATA_UNAVAILABLE。
- **主題 (Themes)**: 無可靠的散戶主題樣本。從網頁摘要可見的機構側主題為: 成本壓力、Q2 營收不及預期、EPS 展望是否改善 (10 月中旬報導)。這些是分析師與媒體敘述，不是散戶貼文，不可當作散戶情緒。

## Insider activity

視窗: 2026-04-28 至 2026-10-28 (6 個月)。

淨額 (僅計有價格的 Sale 交易，以 USD 計):
- 買入: $0.00M (無公開市場買入紀錄)
- 賣出: 約 $0.87M (9 筆有價格賣出，合計約 870,608 USD)
- 淨額: 約 -$0.87M (淨賣出)

主要交易 (6 個月內):

| 日期 | 申報人 | 職稱 | 交易 | 股數 | 價格 (USD) | 金額 (USD M) |
|---|---|---|---|---|---|---|
| 2026-09-03 | SENA PETER P III | Officer | Sale | 4,266 | 88.59 | 0.378 |
| 2026-08-06 | SPAINHOUR STERLING A. JR. | Officer | Sale | 3,333 | 94.02 | 0.313 |
| 2026-09-03 | KIM MATTHEW M. | Officer | Sale | 1,400 | 88.87 | 0.124 |
| 2026-10-01 | KIM MATTHEW M. | Officer | Sale | 100 | 82.73 | 0.008 |
| 2026-09-01 | KIM MATTHEW M. | Officer | Sale | 100 | 88.45 | 0.009 |
| 2026-08-03 | KIM MATTHEW M. | Officer | Sale | 100 | 94.28 | 0.009 |
| 2026-07-01 | KIM MATTHEW M. | Officer | Sale | 100 | 95.77 | 0.010 |
| 2026-06-01 | KIM MATTHEW M. | Officer | Sale | 100 | 91.16 | 0.009 |
| 2026-05-01 | KIM MATTHEW M. | Officer | Sale | 100 | 96.57 | 0.010 |

其他紀錄 (無價格，性質不明，未計入淨額):
- 2026-05-22 WOMACK CHRISTOPHER C. (Chief Executive Officer) 7,662 股，交易欄位空白 — DATA_UNAVAILABLE (性質不明)。
- 2026-06-26 SENA PETER P III 712 股，無價格 — DATA_UNAVAILABLE。

觀察:
- CEO 本期無公開市場買入，6 個月內僅有上述無價格的一筆紀錄。
- 2026-02-11 有多名高層的 Stock Award (授予)，屬薪酬授予，不計入買賣。
- KIM MATTHEW M. 每月約 100 股的小額賣出呈規律性，可能屬預定計畫式交易，但資料未標示計畫性質，僅為推測。
- 上述 6 個月 (4/28 以前) 另有 2026-03-30 GREENE KIMBERLY S 賣出 25,000 股 (約 $2.42M)，超出本視窗，未計入。

## Ownership shifts

- 機構持股: 74.36%，機構數 2,808 家 (yf major_holders 單一快照)。
- 內部人持股: 0.095%。
- 趨勢: DATA_UNAVAILABLE。yf 僅回傳單一時點，無前期比較，無法判斷集中度變化方向。

## Net sentiment score

**綜合: 中性偏空，信心低。**

依據:
- 分析師 (中性): 8 buy / 13 hold / 3 sell，多數 Hold；buy 側微增、sell 側本期新增 strongSell。權重中等。
- 內部人 (偏空): 6 個月約 $0.87M 淨賣出，無公開市場買入。大型賣出多集中於 2026-08 至 09 月。內部人賣出於公用事業股常見，訊號強度有限。
- 散戶 (DATA_UNAVAILABLE): 無法納入評分。
- 網頁摘要的近期目標價調整偏向下修 (未驗證)。

信心低的原因: 散戶來源全部失效，且分析師評等無逐家歷史，綜合分數的散戶權重為零。

**背離旗標 (divergence flag): 無法判定 (DATA_UNAVAILABLE)**。因散戶傾向缺失，無法確認散戶與分析師方向是否相反。

SENTIMENT REPORT COMPLETE
