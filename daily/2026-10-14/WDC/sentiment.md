# Sentiment — WDC as of 2026-10-14

## Analyst consensus
yfinance 目前分布為 4 Strong Buy / 17 Buy / 5 Hold / 0 Sell / 0 Strong Sell（共 26 位）。近四個期間中，Hold 由 3 增至 5，Strong Sell 由 1 降至 0，評等整體維持高度偏多，但邊際有轉趨保守的跡象。

Recent moves（來源為 2026-08 前後的公開報導，未查到 2026-10 月內的評等變動）:
- Citigroup 目標價 $800 → $740，維持 Buy（2026-08-07）
- TD Cowen 目標價 $500 → $540，維持 Buy（2026-08-06）
- Benzinga 彙整之平均目標價約 $483，高於 2026-09-28 股價 $453.23 約 7%

注意: 分析師人數來源不一致。yfinance 為 26 人，Benzinga 頁面為 20 人（16 Buy / 4 Hold），另一頁面為 22 人，Barchart（2026-01）為 25 人。StockScan 顯示平均目標價約 $103，與股價嚴重不符，判定為過時或錯誤資料，不採用。

## Retail social
- Reddit: r/wallstreetbets 與 r/stocks 的 JSON 搜尋皆被工具拒絕存取（WebFetch 回報無法連線 www.reddit.com），本次無法取得貼文樣本、分數或留言語氣。Tilt: 無資料。
- StockTwits / X: StockTwits API 回報 DNS 解析失敗（api.stocktwits.com），本次無法取得訊息流。X 端 WebSearch 未找到 2026-10 的散戶意見文章。
- 間接指標（2026-08-07 前後，Benzinga 頁面，資料已過時）: 空頭持倉約佔流通股 7.8%；Put/Call 比 0.81。
- 聲量（Buzz volume）: 無法量化，未取得提及次數。
- Themes: 無可靠的 2026-10 主題資料。從 2026-08 至 09 的公開報導來看，討論焦點偏向 Q4 FY2026 財報後的估值與目標價調整，屬推論，未經貼文樣本驗證。

## Insider activity
Net 6mo（2026-04-14 至 2026-10-14）: $0 買入 / 約 $35.6M 賣出（共 20 筆公開市場賣出）。無公開市場買入紀錄。另有 8 筆 Grant、2 筆 Gift，無現金價值。

Notable:
- CEO Irving Tan: 2026-05-01 賣出 20,000 股，約 $8.2M（$406–415）；2026-08-11 賣出 20,000 股，約 $8.9M（$441–447）。兩次皆為固定股數，是否屬 10b5-1 計畫無法從資料確認。
- Director Stephanie Streeter: 2026-09-01 賣出 5,600 股，約 $2.5M（$447–455），間接持有。
- Director Martin Cole: 2026-06-09 與 2026-07-28 合計賣出約 $3.8M。
- Director Brian Davis (Officer): 2026-05-11 賣出 10,000 股，約 $5.0M。
- Vidyadhara Gubbi (Officer): 2026-05-04 與 2026-06-01 合計約 $3.4M；2026-09-04 再賣 1,795 股，約 $0.8M。
- Cynthia Tregillis (Officer): 2026-04 至 09 多筆小額賣出，合計約 $2.0M。
- 賣出價格區間: 約 $377 至 $556。6 月高點附近（$545–556）有賣出，9 月起價位回落至 $447–460 區間仍有賣出。

解讀: 核心管理層（CEO 與多位 Officer）持續減持，且完全沒有公開市場買入，屬偏空的內部人訊號。但賣出規模在多位高層間分散，且含固定排程樣式，不必然反映對基本面的看法。

## Ownership shifts
- 機構持股約 88.9%（2,474 家機構）；內部人持股約 0.27%。
- 工具僅提供單一時點快照，無法判定機構持股的季度變化趨勢。需另行取得 13F 資料才能判斷是否有集中或分散。

## Net sentiment score
Composite: **中性（偏多的分析師 vs. 偏空的內部人賣出），信心低**。
- 分析師面: 偏多（約 85% Buy 或 Strong Buy），但 Hold 增加。
- 內部人面: 偏空（6 個月約 $35.6M 賣出，零買入）。
- 散戶面: 無資料，無法判定。
- 評分的信心受限於: 散戶資料完全缺失、分析師人數來源不一、部分資料為 2026-08 前後的快照。

Divergence flag: **無法判定**。散戶端資料缺失，無法比較散戶與分析師的傾向是否相反。若後續取得散戶資料，應以「分析師偏多 + 內部人減持」的組合作為主要比較對象。

資料品質註記: yfinance 的 cookie/crumb 取得失敗，但仍回傳 JSON（推測為快取回退）；代理層亦拒絕部分 Yahoo 端點的連線，資料的實際擷取時間無法確認。

## Metrics

| 指標 | 數值 | 日期/來源 | 備註 |
|---|---|---|---|
| 分析師評等（Strong Buy / Buy / Hold / Sell / Strong Sell） | 4 / 17 / 5 / 0 / 0 | yfinance，目前期間 | 共 26 位 |
| Buy 以上佔比 | 約 81%（21/26） | 由上式計算 | 以 26 位為基準 |
| 平均目標價 | 約 $483 | Benzinga，2026-08 | 來源非當日 |
| 股價參考 | $453.23 | 2026-09-28 | 目標價隱含上行約 7% |
| 近期目標價調整 | Citi $800→$740；TD Cowen $500→$540 | 2026-08-06/07 | 皆維持 Buy |
| 6 個月內部人淨買入 | $0 | yfinance insider，2026-04-14 起 | 無公開市場買入 |
| 6 個月內部人賣出總額 | 約 $35.6M（20 筆） | yfinance insider | 含 CEO 兩筆約 $17.1M |
| 6 個月內部人賣出 / 買入比 | 無法計算（分母為 0） | — | 偏空訊號 |
| 內部人持股比例 | 0.27% | yfinance major_holders | 單一快照 |
| 機構持股比例 | 88.9%（2,474 家） | yfinance major_holders | 無趨勢資料 |
| 空頭持倉（佔流通股） | 7.8% | Benzinga，2026-08 | 過時 |
| Put/Call 比 | 0.81 | Benzinga，2026-08 | 過時 |
| Reddit 貼文樣本數 | 無資料 | 存取被拒 | — |
| StockTwits 多空標記 | 無資料 | DNS 失敗 | — |
| 散戶情緒綜合判定 | 無資料 | — | 無法比較 |
| 綜合情緒 | 中性，信心低 | 本報告 | 無交易建議 |

SENTIMENT REPORT COMPLETE
