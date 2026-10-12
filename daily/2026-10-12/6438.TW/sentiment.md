# Sentiment — 6438.TW (迅得) as of 2026-10-12

**注意: 資料嚴重不足。** 本次查詢沒有取得任何 2026 年 10 月的資料。yfinance 的分析師評等與內部人交易為空, Reddit、StockTwits 無法存取, WebSearch 找到的最新資料停在 2026 年 8 月 11 日。以下各節都只能反映 2026 年 6 月至 8 月的狀況, 不代表 10 月的市場情緒。

## Analyst consensus
0 buy / 0 hold / 0 sell (無資料)。`pipeline/tools/yf 6438.TW rec_summary` 與 `recommendations` 皆回傳空陣列, 未取得任何評等或目標價變動。WebSearch 也找不到 2026 年的券商目標價或評等。唯一相關的研究內容是 CMoney 的一篇 2024 年券商觀點, 提到 CoWoS 市場擴張與毛利率回升預期, 已過時, 且未附評等或目標價。

## Retail social
- **Reddit:** 依規定以 WebSearch 查詢, 未找到 r/wallstreetbets 或 r/stocks 上關於 6438 的討論串。無法判斷情緒傾向。
- **PTT / 中文社群:** 同樣未找到 PTT Stock 板的相關討論。POOR STOCK 有迅得討論區, 但可見留言多為舊文, 另有自動產生的技術分析播報, 不具參考價值。
- **StockTwits / X:** StockTwits 依規定未嘗試抓取 (WebFetch 受阻, 改用 WebSearch)。X 相關搜尋無結果。
- **聲量:** 無法量化。搜尋結果中沒有可辨識的近期輿論熱度。
- **主題:** 無可靠的反覆主題。以資料本身推論, 市場關注點偏向 CoWoS 與半導體設備景氣, 但這是基本面背景, 不是社群情緒的直接證據。

## Insider activity
Net 6mo: 無法計算。`pipeline/tools/yf 6438.TW insider` 回傳空陣列。WebSearch 找到的董監持股數據如下:
- 玩股網: 董監持股比例 2026/06/18 為 12.87%, 4 月中旬約 12.86%, 近幾週幾乎沒有變動。
- 董監申報轉讓頁面 (奇摩股市、中時財經) 抓取內容為空, 沒有可用的申報明細。
- 董事長為王年清, 資本額 8.22 億元。

**未取得**任何具名的 CEO、CFO 或其他董監買賣紀錄。持股比例穩定只能說明近期沒有明顯大額異動, 不能完全排除未被抓到的申報。若需確認, 應查公開資訊觀測站的董監事持股申報。

## Ownership shifts
`pipeline/tools/yf 6438.TW major_holders` 回傳:
- insidersPercentHeld: 25.28%
- institutionsPercentHeld: 1.61%
- institutionsFloatPercentHeld: 2.15%
- institutionsCount: 9

**資料衝突:** yfinance 的內部人持股 25.28% 與玩股網的董監持股 12.87% 差距很大, 原因可能是統計口徑不同 (例如是否含大股東、是否含申報人關係人)。在釐清前, 不建議直接採用其中任何一個數字做判斷。

機構持股比例很低 (約 1.6%), 機構家數 9 家。WebSearch 未找到機構持股的趨勢變化, 因此無法判斷集中度是增加還是減少。

## 價格與基本面背景 (非社群情緒, 僅供脈絡)
- 股價快照 (來源時間不一, 互相有出入): 6 月約 152.5 元; 7/24 約 147.5 元; 8/11 收 145.00 元 (跌 2.00 元)。
- 近 1 個月 -16.4%, 近 1 年 +85.6% (玩股網)。
- 估值: P/E 約 26.65、P/B 約 2.12 (玩股網, 2026/06/26 資料)。Yahoo 另列 P/E 約 27, 同業平均約 34。
- 營收: 2026 年 6 月合併營收 5.93 億元, 年減 3.13%; 2026 年 8 月營收 6.11 億元, 月減 4.19%, 年增 15.54% (nStock, 稱為十年單月同期新高)。年初至今營收約成長 12%。
- 股利: 114 年下半年度現金股利每股 2 元, 除息基準日 2026 年 6 月 26 日。

## Net sentiment score
**Composite: neutral (信心: 低)**

依據: 分析師面無資料, 社群面無資料, 內部人面無交易明細, 僅有持股比例穩定與基本面數據。沒有足夠訊號支持偏多或偏空的判斷。

**Divergence flag: 無法判定 (無資料)。** 因分析師與零售兩側皆缺乏可用資料, 無法比較兩者傾向是否相反。

## 資料缺口與建議
1. 分析師評等: 需取得法人目標價 (如 Goodinfo、CMoney 的法人目標價頁面) 才能評估 consensus。
2. 社群情緒: Reddit 與 StockTwits 在此環境無法存取, 且 PTT 未搜到相關內容。
3. 內部人交易: 需查公開資訊觀測站, 取得 2026 年 4 月至 10 月的申報明細。
4. 時效性: 所有資料最新只到 2026 年 8 月, 未取得 10 月的任何數據。

## 來源
- yfinance 工具輸出: `pipeline/tools/yf 6438.TW` (recommendations, rec_summary, insider, major_holders)
- WebSearch 相關結果: histock.tw/stock/6438, wantgoo.com/stock/6438/major-investors, ww2.money-link.com.tw (SymId=6438), tw.stock.yahoo.com/quote/6438, poorstock.com/board/6438, cmoney.tw 投資快訊 (nid=876328), statementdog.com (6438 相關分析頁), wantrich.chinatimes.com/tw-market/listed/stock/6438, cnyes.com/twstock/directorholder.aspx?code=6438, info.technews.tw (6438 公司資料)

SENTIMENT REPORT COMPLETE
