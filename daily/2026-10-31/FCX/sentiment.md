# Sentiment — FCX as of 2026-10-31

> Reddit 與 StockTwits 皆無法取得，散戶面為空白。

## Analyst consensus
目前 23 家 (yfinance rec_summary): 18 buy (strongBuy 6 + buy 12) / 4 hold / 1 sell / 0 strongSell，約 78% 為買進評級。

近 3 個月變化 (yfinance 彙總，非逐筆紀錄): 約 3 個月前為 19 buy / 3 hold / 1 sell，目前 18 buy / 4 hold / 1 sell，淨變化為 1 家由買進轉為持有，整體仍偏多。yfinance `recommendations` 只回傳彙總計數，無法列出個別券商的升降評與目標價變動明細。

次要來源 (搜尋結果，日期不一，僅供參考):
- 一則 2026-10-17 彙總頁顯示共識為 Buy，平均 6 個月目標價約 $78.7，較當時約 $69.7 股價高約 13%。
- Barclays 於 2026-07-27 將目標價由 $80 上調至 $82 (Overweight)，另有 Wells Fargo、RBC 亦上調目標價。
- Benzinga 顯示做空比率約 1.9% of float。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無法取得。WebFetch 回傳 "unable to fetch from www.reddit.com"，依規則軟失敗，無貼文樣本、無情緒分數。
- StockTwits: 無法取得。`api.stocktwits.com` DNS 無法解析 (ENOTFOUND)，判定為 session 網路白名單未開放。
- X / 新聞搜尋: 搜尋結果未出現可辨識的散戶貼文，只有分析師彙總頁與財經媒體。未找到可引用的散戶語句。
- 聲量: 無法量化。
- 主要議題 (由新聞面而非散戶面推得): 銅、金價高檔是 2026 年股價主要驅動 (Barchart 報導)；分析師多以此作為買進論據。
- 散戶傾向: 無法判定 (資料缺漏)。

## Insider activity
區間: 2026-05-01 至 2026-10-31 (6 個月)。

| 項目 | 金額 (USD M) | 筆數 | 說明 |
|---|---|---|---|
| 公開市場買入 | 0.0 | 0 | 區間內無 open-market buy |
| 公開市場賣出 | 約 8.4 | 5 | 見下表 |
| 股票獎勵 / 授予 | 約 0.1 (折算) | 多筆 | 董事與高管例行授予，不計入買賣 |

主要賣出 (USD):
| 日期 | 人員 | 職稱 | 股數 | 價格 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-25 | Douglas N. Currault II | General Counsel | 80,000 | $78.56 | 6.28 |
| 2026-08-05 | Stephen T. Higgins | Officer | 14,277 | $69.50 | 0.99 |
| 2026-08-05 | Ellie L. Mikes | Officer | 4,773 | $70.00 | 0.33 |
| 2026-08-27 | Lydia H. Kennard | Director | 3,798 | $79.11 | 0.30 |
| 2026-07-30 | Stephen T. Higgins | Officer | 7,550 | $63.00 | 0.48 |

備註:
- Currault 於 2026-08-25 有 80,000 股衍生性證券轉換後賣出，屬執行選擇權後賣出，與一般市場拋售性質不同。
- 所有賣出集中於 2026-07 至 2026-08，股價約 $63–$79 區間。2026-10 僅見董事例行授予，無 CEO/CFO 交易。CEO Kathleen Quirk 與 CFO Maree Robertson 於區間內無公開市場交易。
- 區間外 (供參考): 2026-02 Chairman Richard Adkerson 出售約 40.1 萬股 (約 $25.5M)，CFO Robertson 出售 48,500 股 (約 $3.0M)。2026-02 另有 Higgins 出售約 $1.9M。
- 是否為 10b5-1 計畫: 工具資料未標示，無法判定。

淨額: 6 個月淨買入 $0.0M，淨賣出約 $8.4M。

## Ownership shifts
- 內部人持股: 0.73%
- 機構持股: 91.9% (流通股 92.6%)
- 機構家數: 2,571
- yfinance `major_holders` 只提供單一時點快照，無法判斷機構集中度的時間趨勢。

## Net sentiment score
- 分析師面: 偏多 (約 78% 買進，目標價高於現價)。信心: 高。
- 內部人面: 偏空 (無公開買入，約 $8.4M 賣出，集中於 2026-07/08；多為高階主管與獨立董事)。信心: 中。內部人賣出常見分散或計畫性原因，單看金額不足以推論看法。
- 散戶面: 無資料。
- 綜合: 中性偏多 (信心: 低至中)。分析師面為主要正向訊號，內部人面為溫和負向，但缺少散戶面，整體評估不完整。

Divergence flag: 無法判定。散戶語氣無資料，無法與分析師傾向比對。

## 資料來源與缺口
- 成功: yfinance (rec_summary、recommendations、insider、major_holders)。
- 失敗: Reddit (WebFetch 無法連線)；StockTwits (DNS 解析失敗)。
- 次要 (搜尋): Barchart 分析師觀點、Benzinga FCX 情緒頁、Investing.com FCX 共識頁。部分搜尋結果日期不一致，已排除明顯過時的 2025 年資料。

SENTIMENT REPORT COMPLETE
