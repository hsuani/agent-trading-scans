# Sentiment — SPAI as of 2026-11-27

> 資料時效註記：本報告要求的基準日為 2026-11-27，但執行當下系統日期為 2026-11-26，且 yf 工具在本沙盒中走 cache fallback（Yahoo cookie/crumb 連線失敗）。下列數據為可取得的最新快照，多數帶有日期落差（最新可確認價格為 2026-11-17），請視為近似值。

## Analyst consensus

| 評級 | 家數 |
|---|---|
| Strong Buy | 0 |
| Buy | 3 |
| Hold | 0 |
| Sell | 0 |
| Strong Sell | 0 |

（來源：yf `rec_summary` / `recommendations`，近 3 個期間皆為 3 Buy / 0 Hold / 0 Sell，代表評級分布近期未變動。）

- 近期動態：本次無法取得 2026 年內的升降評等紀錄（DATA_UNAVAILABLE）。搜尋結果提到 Lake Street 新覆蓋 Buy（目標價 $9，日期 2025-11-18）、Northland Buy（目標價 $13，2025-09-09）、Litchfield Hills Buy（目標價 $12，2025-09-17，另有 $8 低標紀錄）。這些都是 2025 年的紀錄，不是 2026 年最新動態。
- 目標價：聚合站顯示平均目標價約 $10.00–$11.00（高 $13、低 $8–$9），來源彼此不一致，且多數日期不明。若以目標價對照最新可確認價格 $3.04（2026-11-17，AAII 資料），隱含上行空間極大，但這正說明此類目標價可能已過時，不宜單獨引用。
- 注意：有一則聚合站寫 5 家分析師含 2 Sell（Moderate Buy），與 yf 的 3 Buy 0 Sell 衝突，判定為舊資料或不同口徑，本報告以 yf 為準。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 的 Reddit 主機在本沙盒被封鎖，WebSearch 也未索引到 SPAI 相關 Reddit 討論串。
- StockTwits：DATA_UNAVAILABLE（當期情緒分數未取得）。WebSearch 只抓到 SPAI 頁面快照，顯示價格 $3.92，但情緒 gauge 未被擷取。另有一則 2025-12 的報導指當日情緒為「極度看多」（當日股價大漲超過 15%），但日期久遠，不代表現況。
- X / 論壇 / 新聞：TradingView 社群留言偏多，多圍繞「SPAI Army」與政府合約題材，例如「任何好消息都會讓股價飆上去」。Investing.com 留言「Its going to $12」屬無依據喊單。單一留言不足以代表整體情緒。
- 量級判定：無法與歷史基準比較（DATA_UNAVAILABLE）。
- 主要論述與題材（依可取得來源歸納）：
  1. 政府 / 國防 AI 合約消息是最常被討論的催化題材。
  2. 股價回落後，多數討論轉向「是否止跌」與「籌碼是否還在賣」。
  3. 價格趨勢負面（Quiver 顯示近 1 個月約 -27.8%、近 3 個月約 -37.8%，日期不明；AAII 顯示四季加權相對強弱 -15.4%，動能分數 21，屬 Weak）。
- 整體傾向：零散資料偏多頭喊單，但價格與動能偏弱。Retail 傾向無法以可靠數據確認，暫判為「混合」。

## Insider activity

以 2026-05-27 至 2026-11-27 為 6 個月窗口，yf `insider` 紀錄如下：

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額（USD） |
|---|---|---|---|---|---|
| 2026-09-09 | ERDBERG DANIYEL | CEO | 賣出，價格 $4.00 | 1,000,000 | $4.0M |
| 2026-05-01 | MACK BRIAN WILLIAM | Officer | 股票獎勵（Grant） | 300,000 | $0（非公開市場買入） |
| 2026-04-01 | MATHEWS JARRET DANIEL | COO | 股票獎勵（Grant） | 20,000 | $0（窗口外） |

- 6 個月淨額：公開市場買入 $0；公開市場賣出約 $4.0M（僅 CEO 一筆）。
- 注意：Mack 的 2026-05-01 獎勵，若以 6 個月窗口計算，已接近窗口邊界，且屬獎勵而非買入。
- 歷史紀錄中的贈與（Gift）與 2025 年董事獎勵，不屬於市場買賣，未計入淨額。
- 解讀：CEO 於 2026-09-09 以 $4.00 賣出約 100 萬股，為本期最重要的內部人訊號，屬偏空訊號。股價 $4.00 高於最新可確認價 $3.04，故該賣出價位在當時高於現價。

## Ownership shifts

- 內部人持股：44.2%（yf `major_holders`）。
- 機構持股：11.2%（佔總股本）；佔流通股（float）20.1%；機構家數 33。
- 趨勢：本次工具僅回傳當期快照，無歷史季度變化，機構持股「增減趨勢」為 DATA_UNAVAILABLE。
- 解讀：內部人持股比例偏高，流通股結構集中，機構覆蓋度相對有限，股價波動可能被少數持股放大。

## Net sentiment score

- 分析師面：偏多（3 Buy / 0 Sell），但樣本僅 3 家，且缺乏 2026 年最新評等動態，可信度中等偏低。
- 內部人面：偏空（CEO 2026-09 賣出約 $4.0M，6 個月內無公開市場買入）。
- 零售面：混合（Reddit / StockTwits 數據缺失，僅有零散喊單與合約題材討論）。
- 價格動能：偏弱（近 1–3 個月下跌，相對強弱為 Weak）。

**Composite：中性偏空（neutral-to-bearish），信心：低（low）。** 主要原因是資料時效落差大，且 Reddit / StockTwits 缺失，無法做出可靠的零售情緒判定。

**Divergence flag：無法判定（DATA_UNAVAILABLE）。** 分析師面偏多，但零售面缺少可比對的量化數據，無法確認兩者是否背離。若補齊 StockTwits 情緒分數與近期 Reddit 討論，可再判定此旗標。

## 資料缺口與後續建議

- Reddit 直接查詢（WebFetch 被封鎖）：DATA_UNAVAILABLE。
- StockTwits 當期情緒分數：DATA_UNAVAILABLE。
- 2026 年分析師升降評等與目標價變動：DATA_UNAVAILABLE。
- 機構持股歷史趨勢：DATA_UNAVAILABLE。
- 建議：於可連線環境補抓 StockTwits symbol 頁面的情緒分數，並以 yf 即時資料重跑 `insider` 與 `rec_summary` 以確認 cache 內容未過期。

SENTIMENT REPORT COMPLETE
