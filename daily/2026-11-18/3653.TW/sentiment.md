# Sentiment — 3653.TW (健策 Jentech Precision) as of 2026-11-18

資料說明：yfinance 分析師評級可取得；Reddit、StockTwits 無法取得（見下方）；內部人交易回傳空陣列，無法確認是否為真實零交易；搜尋結果未找到 2026 年 11 月的散戶討論。本報告不含任何交易建議。

## Analyst consensus

以 yfinance 最新評級計：**11 buy / 0 hold / 0 sell**（strongBuy 4、buy 7）。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 當期 (0m) | 4 | 7 | 0 | 0 | 0 |
| -1m | 4 | 7 | 0 | 0 | 0 |
| -2m | 4 | 7 | 0 | 0 | 0 |
| -3m | 3 | 7 | 0 | 0 | 0 |

- 近四個月評級分布穩定，無 hold / sell 出現。-3m 時 strongBuy 由 3 變為 4，屬於既有買進評等內部的小幅轉強，並非評等升降。
- yfinance 未提供個別券商的升降級明細與目標價歷史，因此無法列出具名的調升或調降事件。
- 網路搜尋可見的個別報告（數字來源彼此不一致，需以原始報告確認）：
  - 大和：重申「買進」，12 個月目標價由 9,420 元上調至 10,000 元（報導以約 73 倍本益比估算，並提到 AI 伺服器需求不如預期、散熱規格升級落後為風險）。
  - 美系外資（約 7 月底）：上調 2026 年 EPS 預估 7%，維持「買進」；但同一則來源提到目標價 4,000 元，與當時約 6,000 至 7,000 元的股價明顯不符，疑為誤報或數字有誤，本報告不採用。
  - 里昂（日期不明，應早於大和）：目標價由 5,480 元上調至 5,700 元，維持「優於大盤」。
  - Investing.com 顯示的最新列示目標價為摩根大通 8,800 元（2026 年 9 月 3 日）。
- 目標價散布很大（約 5,700 至 10,000 元）；目前能確認的只有評等全數偏多，目標價細節無法完整整合。

## Retail social

- Reddit：DATA_UNAVAILABLE。r/stocks 搜尋端點回傳 "unable to fetch"，無法取得貼文樣本、聲量或傾向。r/wallstreetbets 未嘗試（同一網域，預期相同）。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 在此環境無法解析（非允許網域），需由使用者於 session 網路設定中開放後才能重試。
- X / 新聞與論壇搜尋：WebSearch 僅回傳股價與評等快照，未找到 2026 年 11 月的散戶留言。CMoney 個股討論區有入口但抓取內容無留言，無法判斷情緒。Investing.com 的散戶情緒頁無可用數據。
- 聲量（相對一般水準）：無法量化，標記為 DATA_UNAVAILABLE。
- 主題：無可用樣本，無法歸納。已知的基本面敘事（僅供背景，非散戶原文）：2026 年 8 月單月營收 32.26 億元（年增 90.9%，單月歷史新高）、2026 Q2 EPS 15.8 元（年增 101%）；股價於 2026 年夏季大幅上漲，8 月初出現單日約 10% 漲幅，之後有回檔紀錄。

## Insider activity

yfinance `insider` 回傳空陣列。在無法確認是否為工具缺漏或真實零交易的情況下，本節標記為 **DATA_UNAVAILABLE**，不推論為「無內部人交易」。台灣董監持股申報（公開資訊觀測站）未在本次資料來源中取得。

Net 6mo：DATA_UNAVAILABLE（無買賣金額、無職稱或姓名可列）。

## Ownership shifts

yfinance `major_holders`（快照，未附日期）：
- 內部人持股比例：37.66%
- 機構持股比例：40.36%
- 機構佔流通股比例：64.74%
- 機構家數：256

機構持股的時間趨勢（季度變化）工具未提供，標記為 DATA_UNAVAILABLE。目前僅能確認集中度屬高水準（內部人加機構合計約 78%，此為相對高的持股集中度，但與 float 口徑不同，需謹慎解讀）。

## Net sentiment score

- **Composite：偏多（bullish），信心低。** 依據僅為分析師評級（全數買進）；散戶社群面與內部人面均無可用資料，無法形成完整的綜合判斷。
- **Divergence flag：無法判定。** 散戶傾向資料缺失，無法確認是否與分析師傾向相反。

資料缺口清單：Reddit（DATA_UNAVAILABLE）、StockTwits（DATA_UNAVAILABLE，網路限制）、內部人交易（DATA_UNAVAILABLE）、機構持股趨勢（DATA_UNAVAILABLE）、聲量量化（DATA_UNAVAILABLE）。

注意：本次執行日期依使用者指定為 2026-11-18，系統環境日期為 2026-11-17；本報告以 2026-11-18 為 as-of 日期，但實際抓取的資料時點多為 2026 年 9 月前後，未取得 11 月資料。

SENTIMENT REPORT COMPLETE
