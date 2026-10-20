# Sentiment — 3017.TW（奇鋐 / AVC）as of 2026-10-21

> 資料時效注意：yf 工具的評等計數可取得，但網路搜尋結果最新只到 2026 年 8 月中旬，10 月的券商評論與股價未能取得。Reddit 與 StockTwits 皆無法存取。以下結論的信心度因此偏低。另外，系統日期為 2026-10-20，本報告依指定的 as-of 日期 2026-10-21 撰寫。

## Analyst consensus

目前 17 家（6 strongBuy / 11 buy / 0 hold / 0 sell / 0 strongSell）。與 -1m、-2m 相同；-3m 為 15 家（6 strongBuy / 9 buy），顯示近 3 個月新增 2 家買進評等，沒有任何降評或持有評等。

Recent moves（以 WebSearch 找到的外資與本土法人報告，發布日期多為 2026 年 7 至 8 月，**10 月的調整未能確認**）:
- 花旗：目標價由 3,800 上修至 4,350 元，維持買進；預估 2027 年營收年增 50%，並預估 3Q26 營收季增 16%。
- 美銀（BofA）：目標價由 2,225 大幅上調 59% 至 3,540 元，本益比倍數由 24 倍調至 27 倍，維持買進；預估 2026 年 EPS 99.23 元。
- 摩根士丹利（大摩）：目標價由 2,950 上調至 3,333 元，評等優於大盤。
- 麥格理：目標價 4,600 元，為外資中最高（來源未註明日期）。
- 日系外資：目標價 3,155 元，維持買進。
- 本土法人：目標價最高 4,145 元，看好 ASIC 與液冷成長。
- 參考股價：8 月 9 日約 2,785 元（nStock 顯示），另有報導提及一日收 3,430 元，日期不明。目標價與股價落差大，屬於偏多的分析師傾向。

## Retail social

- Reddit：DATA_UNAVAILABLE。r/stocks 與 r/wallstreetbets 搜尋均回傳 "Claude Code is unable to fetch from www.reddit.com"，無法取得貼文與分數。
- StockTwits / X：StockTwits 回傳 `getaddrinfo ENOTFOUND api.stocktwits.com`，DATA_UNAVAILABLE。X 端無可用的 2026 年 10 月搜尋結果。
- 華文社群（CMoney 股市爆料同學會）：搜尋摘要顯示少量貼文，內容偏保守。有人認為股價短線回檔、被高估，引用本益比約 46.71 倍；另有樂觀看法，認為 AI 需求可見度看到 2028 至 2029 年。貼文日期無法確認（頁面標示近 7 天，但內文財務數字為 5 月資料），樣本量不足以代表整體。
- PTT Stock 板：搜尋未找到相關討論，DATA_UNAVAILABLE。
- 討論量（相對常態）：無法量化。只能定性判斷，華文財經新聞對 2026 年 6 月股東會與 7 月營收創高的報導密度高，但這是媒體量，不等於散戶聲量。

## Retail tilt

整體：**mixed，偏多頭基本面、偏保守估值**（信心度低，樣本少）。

Top recurring themes（依搜尋摘要歸納）:
1. 估值擔憂：本益比偏高、短線回檔、股價被高估（CMoney 貼文）。
2. AI 伺服器與液冷長線需求：訂單能見度至 2028 至 2029 年（股東會上董事長沈慶行的說法，並被散戶轉述）。
3. 營運創高：2026 年 2Q 毛利率約 32.6%，單季 EPS 24.37 元；7 月營收 185.9 億元，年增 57.4%。
4. 風險提示：零組件短缺、客戶平台世代交替（法人報告提及）。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。`yf insider` 回傳空陣列（可能是 Yahoo 端無資料，或 Cookie/crumb 取得失敗；該工具 log 有 ConnectionError）。網路搜尋未找到董監持股變動、申報轉讓或減持資料。建議查詢公開資訊觀測站的董監事持股申報紀錄以確認。

## Ownership shifts

- insidersPercentHeld: 17.35%
- institutionsPercentHeld: 43.77%（float 持有 52.96%）
- institutionsCount: 358
- inst_holders 僅回傳一筆：Stanley-Laman Group, Ltd.，持股 12,800 股，報告日 2026-06-30，變動 +100%（此為單一機構的小額變化，不足以判斷整體趨勢）。
- 歷史機構持股趨勢：DATA_UNAVAILABLE（僅有單一時點快照）。

## Net sentiment score

Composite: **bullish（信心度：中低）**

- 分析師面：bullish（信心度中高）。17 家全數買進，無賣出或持有，近 3 個月多家上修目標價；但目標價的報導日期多在 8 月，10 月是否有變化未知。
- 零售面：mixed 偏保守（信心度低）。樣本只有單一華文論壇摘要，時間不明，無 Reddit / StockTwits 資料。
- 內部人面：DATA_UNAVAILABLE，無法納入評分。
- 機構面：中性偏穩（機構持股 43.8%，358 家，無趨勢資料）。

Divergence flag: **yes（部分分歧，信心度低）**。分析師一面倒看多並上修目標價，而零售端的可取得樣本偏向估值擔憂。這種分歧常見於高估值的題材股，但本次樣本太少，不能視為確定訊號。

## 資料缺口與後續建議

1. Reddit、StockTwits、PTT 需在可存取的環境或手動搜尋 2026 年 10 月的貼文，以補足散戶情緒。
2. 內部人交易需查 MOPS（公開資訊觀測站）的董監持股申報。
3. 10 月的券商評等與目標價需重新搜尋，確認 8 月後是否有調整。

SENTIMENT REPORT COMPLETE
