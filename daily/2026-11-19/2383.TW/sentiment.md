# Sentiment — 2383.TW (台光電 EMC) as of 2026-11-19

資料完整度聲明：Reddit、StockTwits 無法取得（見下方），PTT / Dcard 只找到聚合站的標題而非討論內容，故本報告的散戶面判斷信心低。分析師面資料來自 yfinance 彙整，完整。

## Analyst consensus

目前 18 家（6 strong buy / 12 buy）/ 0 hold / 0 sell，全部為正面評等。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 當期 (0m) | 6 | 12 | 0 | 0 | 0 |
| -1m | 6 | 12 | 0 | 0 | 0 |
| -2m | 6 | 11 | 0 | 0 | 0 |
| -3m | 5 | 11 | 0 | 0 | 0 |

近三個月的變化：買進方向由 16 家增至 18 家（strongBuy 5→6、buy 11→11→12），期間沒有任何 hold 或 sell 出現，也就是沒有降評紀錄。

目標價方面，yfinance rec_summary 不含目標價欄位。搜尋到的券商目標價散見於 2026 年初至年中的報導，數字彼此不一致（摩根大通、統一投顧曾被報為 3,600 元或 3,100 元，高盛 3,200 元，麥格理 2,840 元），且發布日期不明，無法確認為最新版本，因此不列為正式共識。搜尋結果同時提到一則本土投顧目標價 7,200 元與股價盤中曾觸及 6,250 元，這些數字來源品質不一，需以原始報告為準。

## Retail social

- Reddit：WebFetch 遭拒（"unable to fetch from www.reddit.com"），r/wallstreetbets 與 r/stocks 均無資料。標示為無法取得，未推斷散戶傾向。
- StockTwits / X：StockTwits API 無法解析網域（ENOTFOUND api.stocktwits.com），需於 session 網路設定中放行才能取得。X 端只有新聞與券商報告，沒有可辨識的個人散戶貼文。
- PTT：搜尋僅找到 nStock 聚合列表中的一則標題「[情報] 2383 台光電 8月營收」（2026-09-04，Ptt 股市），內文與留言未取得，無法判斷推文傾向。
- Dcard：未找到相關討論串。
- 聲量：無法量化。以新聞密度判斷，媒體報導量在 2026 年中以後明顯增加（營收創高、注意股、高價股波動），但這屬於媒體關注度，不代表散戶留言量。

Themes（只能從新聞端歸納，非散戶原文）：
- 營收動能：2026 年 7 月單月營收約 192.07 億 TWD，年增約 129%，創單月新高（nStock 摘要）。
- 產品題材：M9 材料出貨、NVIDIA 下一代 AI server 材料路線（Rubin Ultra 是否改採 PTFE 的傳聞）。凱基報告指出公司回應「定案仍言之過早」。
- 產能擴張：中國昆山、中山新地，預計 1H28 增加約 180 萬張產能。
- 波動與籌碼：證交所曾將其列為注意股（近 90 個營業日漲幅約 200.6%）；Goodinfo 摘要顯示近 5 日與近一月出現大幅回檔（數字未與原始頁面核對）。

## Insider activity

yfinance insider 回傳空陣列。這可能代表 6 個月內無申報，也可能是 Yahoo cookie/crumb 取得失敗導致資料不完整（工具訊息顯示 crumb 抓取失敗）。因此無法判定淨買賣金額，也無法指出 CEO/CFO 動向。此項結論信心低，建議另以台灣公開資訊觀測站（董監持股申報）核對。

Net 6mo：無法確認（資料缺漏，不以 0 計）。

## Ownership shifts

- 內部人持股比例：約 19.0%
- 機構持股比例：約 48.7%（占流通股約 60.2%）
- 機構家數：379 家
- 目前僅有單一時點快照，無法計算近期集中度趨勢。

## Net sentiment score

Composite：**偏多（信心：中低）**

- 分析師面偏多，評等全數為 buy 以上，近三個月無降評，信心中高。
- 散戶面無有效樣本（Reddit、StockTwits 不可得，PTT / Dcard 僅標題），無法判定方向。
- 內部人面資料不完整，不納入計分。
- 價格動能與情緒高度波動（年內漲幅大、近期回檔），屬於高波動題材股，這會降低單靠情緒判讀的可靠度。

Divergence flag：**無法判定**。分析師傾向為正面，但散戶傾向缺乏可用樣本，不能確認是否背離。若日後取得 PTT 或 StockTwits 資料，應特別檢查「分析師全數買進、散戶轉空」這類背離情形。

資料缺口與來源狀態：
- Reddit（r/wallstreetbets、r/stocks）：WebFetch 被拒，無資料。
- StockTwits：DNS 解析失敗，需放行 api.stocktwits.com。
- PTT / Dcard：僅標題級資料。
- Insider：yfinance 回傳空值，疑為連線問題。
- 日期注意：本報告以 2026-11-19 為 as-of，但執行環境日期為 2026-11-18，部分搜尋結果的日期（如 11/09 數據）為轉述，未逐筆核對。

SENTIMENT REPORT COMPLETE
