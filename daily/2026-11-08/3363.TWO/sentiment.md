# Sentiment — 3363.TWO (上詮) as of 2026-11-08

> 資料完整度: 低。yfinance 即時 feed 無法連線 (fc.yahoo.com ConnectionError)，analyst 數字取自 repo 快取；Reddit / StockTwits 未取得有效內容；散戶面主要依 WebSearch 找到的財經站標題與新聞，無法量化討論量。

## Analyst consensus

目前 rec_summary 為 **2 buy / 1 hold / 0 sell** (含 1 strongBuy，共 3 家)。歷史 recommendations 顯示: -1m 為 2 strongBuy + 1 buy; -2m 為 1 strongBuy + 1 buy，無 hold / sell 紀錄。

近期重要動態 (來自新聞，yf 快取未反映):
- **摩根士丹利 (大摩) 降評**: 由 Overweight 降為 Equal Weight，目標價由 708 元下修至 688 元 (約 2026-09 前後，來源為報導轉述，未見原始報告)。主要疑慮為產能擴充與量產規模是否跟得上 CPO 市場成長，並點名 Corning、Coherent 等競爭者規模較大。若大摩已改為 hold，yf 快取的 1 hold 與此相符，但 yf 日期不明，無法確認。
- **高盛**: 初評 Buy，目標價 864 元 (日期未確認)。
- **統一**: 中立。**中信**: 認為不便宜、需留意風險。

目標價: 僅上述券商的零星報導數字，沒有完整的共識目標價。

## Retail social

- **PTT / 股市版**: nStock 頁面列出的標題多為財報與營收情報，例如 "[情報] 3363 上詮 115年Q1:-0.98 及4月營收" 與 "[情報] 3363上詮 8月營收"。標題偏中性偏事實性，正文內容無法取得，無法判定多空。
- **Reddit (r/wallstreetbets, r/stocks)**: 未取得搜尋結果。以 WebSearch 查詢未命中任何討論串。依指示未以 WebFetch 直接請求 Reddit 公開 JSON。
- **StockTwits / X**: 未取得可用內容。StockTwits 未嘗試 (依指示改用 WebSearch)。
- **Dcard / CMoney 股市爆料同學會**: 搜尋結果只有頁面入口，沒有 2026-11 的貼文內容。
- **討論量 (定性)**: 搜尋可見的 PTT 情報標題與財經媒體報導有一定量，但無法做有意義的 mention count 與 typical 比較，**buzz 量判定: 無法評估 (資料不足)**。
- **主要主題 (從標題與媒體可見)**:
  1. CPO / FAU 量產故事 (1.6T 於 2026Q3 量產目標，3.2T 於 Q4 放量)。市場正面看待的核心。
  2. 虧損收斂但仍虧: 2026Q3 單季淨損約 700 萬元、EPS -0.06，較去年同期由盈轉虧。
  3. 擴產與資本支出: 董事會通過新增約 21.9 億元資本支出，加計原有約 11.4 億元，總預算約 33.3 億元。
  4. 股價波動與注意股: 「通網股注意股」「近 5 日跌 7.75%」一類標題。
  5. 大摩的產能疑慮。

## Insider activity

Net 6mo: **資料無法取得**。insider 查詢回傳空陣列 `[]`，無法確認是「6 個月內無申報」還是 feed 未涵蓋。在未確認前，不應將空陣列解讀為零交易。

Ownership 快照 (major_holders): 內部人持股約 26.4%，法人持股約 11.4% (占流通股約 15.5%)，法人家數 35。屬單一時點快照，無法判斷持股集中度趨勢。

## Ownership shifts

- 內部人 26.4%、法人 11.4%，法人家數 35。
- 趨勢: 無歷史資料可比較，**判定無法評估**。
- 新聞提及「擬辦現增 1 萬張新股」(來源 uanalyze 文章，日期未明，可能為較早期事件)，若屬實，對股本稀釋與籌碼面有影響，需另行確認。

## Net sentiment score

**Composite: neutral (信心: 低)**

- 分析師面: 偏正向但有分歧。yf 快取 2 buy / 1 hold / 0 sell，但大摩已從加碼降為中立，高盛 buy，統一中立，中信保守。整體屬「偏多但有保留」。
- 散戶面: 無法有效量化。可見的主題 (CPO 題材 vs 虧損、擴產、大摩疑慮) 呈正負並存，沒有明確一致的多空傾向。
- 內部人面: 資料缺失，不計入評分。

**Divergence flag: no (資料不足，無法判定)**。分析師整體仍偏多、散戶面無明確傾向，兩邊未形成清楚的反向訊號。若日後取得 PTT / Dcard 正文，應再次檢視。

### 資料品質與注意事項

- 股價快照來源日期不一致: 約 600 元 (2026-08-14)、652 元 (2026-09-24)、531 元 (2026-10-16)。目前無可靠的 2026-11-07 收盤價，請以交易所行情為準。
- 獲利數字在不同來源之間有出入: 一處報導寫前三季每股虧 1.24 元，另一股務站寫 2026Q2 EPS -0.22 元。各來源口徑不同，建議以公開資訊觀測站正式公告為準。
- 資本支出數字: 第一則搜尋結果寫 "NT$2.19 billion"，但原文報導標題為新增 21.9 億元。以 21.9 億 (約 21.9 億元 NT，即 2.19 億的 10 倍) 為準，已統一採用原文數字。
- 2026 年 10 月營收尚未公告 (預計於 11 月 10 日前後公布)，本報告不含該數字。
- 本報告為情緒與分析師面彙整，不構成交易建議。

### 來源

- [上詮自結Q3每股虧0.06元 新增21.9億元資本支出擴充FAU產線](https://uanalyze.com.tw/articles/6648458480)
- [上詮斥資15.38億擴產FAU生產線 Q3起依客戶需求交貨3.2T產品](https://uanalyze.com.tw/articles/6955154609)
- [CPO量產帶動FAU需求升溫 上詮產能效率受考驗,大摩降評示警](https://uanalyze.com.tw/articles/8277656872)
- [上詮將全力投入矽光產線 FAU出貨逐步放大推升明年業績](https://uanalyze.com.tw/articles/7027639885)
- [上詮自結11月虧損2200萬元 擬辦現增1萬張新股增加光通訊CPO產線 (日期未明)](https://uanalyze.com.tw/articles/7554544343)
- [nStock 上詮做什麼 (PTT 標題與公司概況)](https://www.nstock.tw/上詮做什麼.html)
- [CMoney 股市爆料同學會 3363](https://www.cmoney.tw/forum/stock/3363)
- [Yahoo 股市 3363.TWO 營收](https://tw.stock.yahoo.com/quote/3363/revenue)

SENTIMENT REPORT COMPLETE
