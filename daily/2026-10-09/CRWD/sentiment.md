## CRWD 情緒報告，截至 2026-10-09

**資料完整度警告:** Reddit 與 StockTwits 皆無法取得 (見下方 Retail social)，散戶情緒維度為缺口。另外 DATE 為 2026-10-09，但執行環境日期為 2026-10-08，最新可得 insider 交易為 2026-10-05，請上游確認日期是否正確。

## Analyst consensus

截至 `rec_summary` 0m: **53 位分析師 = 10 Strong Buy / 30 Buy / 12 Hold / 1 Sell / 0 Strong Sell**。買方傾向約 75%，持有約 23%，賣方約 2%。

近 3 個月趨勢:
- -3m 為 31 Buy / 11 Hold，目前 30 Buy / 12 Hold，約 1 檔從 Buy 降為 Hold。
- 0m 出現 1 檔 Sell，同時 Strong Sell 減為 0，屬於評等分布微幅轉向，但整體仍偏多。
- 工具只提供評等計數，未提供個別券商的升降評等明細與目標價變動，因此無法列出具名 upgrade/downgrade 與 PT 變化。`recommendations` 與 `rec_summary` 回傳內容相同。
- 交叉參考 (時效較舊，僅供參考): Barchart 2026-02 報導 48 位分析師中 Moderate Buy，Berenberg 於 2026-02 升至 Buy，來源為 [Barchart 轉載](https://business.mammothtimes.com/mammothtimes/article/barchart-2026-2-2-do-wall-street-analysts-like-crowdstrike-stock)。

## Retail social

- **Reddit:** 無法取得。r/wallstreetbets 與 r/stocks 的搜尋皆被 WebFetch 封鎖 (reddit.com 無法存取)，本次無樣本。Buzz 量與多空傾向均無法判定。
- **StockTwits / X:** StockTwits 回報 DNS 解析失敗 (`api.stocktwits.com` ENOTFOUND)，未取得訊息量與多空標籤。
- **WebSearch 補充:** 僅找到一則低可信度來源提到散戶情緒「極度看多」，無平台、無數量、無法驗證，不列為依據。搜尋結果也未提供 2026-10 的近期散戶討論。
- **Buzz volume:** 無法量化，無法與常態比較。
- **Retail tilt:** 無法判定。
- **Themes:** 無可靠資料。

## Insider activity

6 個月窗口 (2026-04-09 至 2026-10-09):
- **買入:** 0 筆、$0。
- **賣出:** 共 115 筆 Sale 紀錄，總額約 **$463M** (as-reported)。其中約 $68M 位於 2026-06-22 至 2026-07-06 區間，價格欄位在同一時間點出現約 4 倍的尺度不一致 (約 $190、$700、$775、$3,090 混雜)，可能與 2026-07-02 的 4-for-1 分割有關。排除這些異常列後，乾淨口徑約 **$395M**。
- **方向:** 無論口徑為何，皆為單邊賣出。

主要賣方 (乾淨口徑):
- **George Kurtz (CEO):** 約 $222M，為最大賣方。近 30 天多為每筆 20,000 股、約每 2 至 5 個交易日一次，最近一筆為 2026-10-05，20,000 股、$5.4M，價格區間約 $268–274。Feed 未標示是否為 10b5-1 預定計畫，無法判定。
- **Sameer Gandhi (Director):** 約 $54M，最近一筆 2026-10-01，54,000 股、$14.3M。
- **Michael Sentonas (President):** 約 $41M，最近一筆 2026-09-21，49,863 股、$11.6M。
- **Gerhard Watzinger (Director):** 約 $36M，2026-09-16 賣出 120,000 股。
- **Roxanne Austin (Director):** 約 $12M，2026-09-14 賣出 50,000 股。
- **Burt Podbere (CFO):** 約 $10M，2026-09-21 賣出 33,882 股。
- **Anurag Saha (Officer):** 約 $9M。
- **Cary Davis (Director):** 約 $7M。
- **Denis O'Leary (Director):** 約 $3M。

其餘為董事與管理層的例行股票獎勵 (Stock Award) 及少量贈與，非市場交易。

重點觀察: 近 30 天的賣出價格多落在接近近期高點的區間 (約 $230–274)，且 CEO、CFO、President、多位董事同步賣出。這與 insider 常見的獲利了結或分散持股相符，但單靠此資料無法區分是預定計畫或主動決策。

## Ownership shifts

- 機構持股約 **77.8%**，機構數 **3,162** 家。
- 內部人持股約 **1.4%**。
- 工具只提供單一時點快照，無法判定機構集中度的趨勢。

## Net sentiment score

- **分析師:** 偏多，信心中高 (以評等計數判斷)。
- **Insider:** 偏空或中性，信心中等。賣出規模與頻率明顯，但無買入，且可能包含預定交易。
- **散戶:** 無資料，不納入計分。
- **綜合:** **中性偏多，信心低**。主要受限於散戶資料缺失，以及 insider 資料的價格尺度問題。

**Divergence flag: 部分是。** 分析師端偏多，內部人端單邊賣出，兩者方向不一致。散戶與分析師的偏離則無法判定，因為缺乏散戶資料。

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| `yf rec_summary` / `recommendations` | 成功，回傳相同的趨勢計數，無個別券商明細 |
| `yf insider` | 成功，但 2026-06-22 至 2026-07-06 區間價格尺度不一致，已標註 |
| `yf major_holders` | 成功，單一快照 |
| Reddit (r/wallstreetbets, r/stocks) | 失敗，無法存取 |
| StockTwits | 失敗，DNS 解析錯誤 |
| WebSearch | 部分成功，近期資料稀少，多為低可信度來源 |

SENTIMENT REPORT COMPLETE

Sources:
- [Barchart 轉載，2026-02 分析師評等報導](https://business.mammothtimes.com/mammothtimes/article/barchart-2026-2-2-do-wall-street-analysts-like-crowdstrike-stock)
- [WebSearch 結果: StockAlarm 分析師頁](https://pro.stockalarm.io/quote/CRWD/analysts) (未註明日期，未採用為依據)
