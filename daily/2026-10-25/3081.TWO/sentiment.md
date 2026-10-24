# Sentiment — 3081.TWO (聯亞) as of 2026-10-25

注意: 資料時點以工具抓取時為準（今日 2026-10-24），部分來源已失效。

## 資料可得性

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 成功（Yahoo cookie/crumb 取得失敗，但資料仍回傳） |
| yf insider | 回傳空陣列，無法確認是否真的零交易（同一 Yahoo 通道有異常，見下方限制） |
| yf major_holders | 成功 |
| Reddit r/wallstreetbets、r/stocks | 失敗，WebFetch 無法連線 www.reddit.com，未取得任何貼文 |
| StockTwits | 失敗，api.stocktwits.com DNS 解析失敗 |
| 網路搜尋（X / 新聞 / 論壇） | 成功，但最新一筆相關內容約為 2026 年 7 至 8 月，搜尋無 2026 年 10 月的情緒資料 |

## Analyst consensus

目前 8 buy（含 1 strongBuy）/ 1 hold / 1 sell，共 10 家。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當期 (0m) | 1 | 7 | 1 | 1 | 0 |
| -1m | 1 | 7 | 1 | 1 | 0 |
| -2m | 1 | 7 | 1 | 1 | 0 |
| -3m | 1 | 5 | 1 | 1 | 0 |

- 近三個月買進評等由 6 家增至 8 家（+2），hold 與 sell 數量未變。
- 網路搜尋提到某外資調高目標價至 NT$1,505 並將評等下調為中性，認為估值已反映多數利多（上半年營運優於預期）。但 yf 的 hold 數在四個期間都是 1，與「下調為中性」不吻合，兩者無法互相印證。
- 目標價與當時股價存在落差：搜尋結果提到股價約 NT$3,430，高於 NT$1,505 的目標價。這代表目標價、股價或報導日期中至少一項有誤，或該目標價為舊資料，需人工核對原始券商報告後再採用。
- 無法確認目標價的完整分布（yf 未提供），也無法確認近期是否有新的調級。

## Retail social

- Reddit：無資料（連線被擋）。無法給出貼文樣本或正負比例。
- StockTwits / X：StockTwits 無資料。X 無直接取得，僅能從搜尋結果間接推論。
- 論壇（CMoney 股市爆料、個股討論區）：搜尋摘要顯示，多數發言偏樂觀看長期（AI 資料中心光通訊需求、InP 基板價格上升），但對短期動能有保留，同時有討論指出近期股價下跌後賣壓可能回潮、部分技術指標收斂、上漲動能減弱。整體屬於「長多、短線分歧」。
- 交易熱度：櫃買中心曾將該股列為注意股（搜尋結果僅見標題「近5日漲11.30%」，發布日期不明）。這代表短期投機交易活躍，但不能直接解讀為看多或看空。
- 聲量：無法量化與平常相比的提及次數（Reddit、StockTwits 皆無法取得），只能定性判斷為「中等，以台股論壇為主」，證據不足。
- 主要主題（依搜尋結果歸納，非逐篇閱讀）：
  1. AI 資料中心光通訊需求帶動
  2. InP 基板與 MOCVD 產能擴充（摘要提到 2026 年底至 2027 年底產能預期倍增）
  3. 短線動能是否延續、是否有追高風險
  4. 營收爆發（摘要：2026 年 7 月月營收約 NT$5.01 億，年增 176.5%）

## Insider activity

Net 6mo: 無資料（yf insider 回傳空陣列，無法確認是否真的沒有交易）。
- 不認定為零交易，因為同一 Yahoo 通道在本次查詢中有 cookie/crumb 失敗的紀錄。
- 未找到 CEO、CFO 或其他內部人的具體交易紀錄。
- 建議到 TWSE/TPEx 公開資訊觀測站（董監事持股異動、內部人申報）人工核對。

## Ownership shifts

- 內部人持股 13.95%
- 機構持股 26.46%（占流通股 30.75%）
- 機構家數 84 家
- yf 只提供單一時點快照，無法判斷機構持股的增減趨勢。

## Net sentiment score

綜合判斷：偏多（bullish），信心：低至中。
- 分析師面：偏多，信心中。買進評等 8/10，近三個月增加 2 家；但數據時點不明，且與搜尋結果的「下調為中性」有矛盾。
- 散戶面：偏多但分歧，信心低。只有論壇摘要，沒有 Reddit、StockTwits 的實際樣本，無法量化。
- 內部人面：無資料，不納入計分。
- 扣分因素：短線動能轉弱的討論、股價高於已知目標價、注意股身分帶來的波動風險。

Divergence flag: 否。散戶與分析師方向大致同向（都偏多），僅在「長期偏多、短線保留」的程度上有差異。但若最新的中性評等與目標價數據屬實，分析師內部的估值分歧仍值得追蹤。

## 限制與建議後續查證

1. Reddit、StockTwits 無法連線，散戶面證據不完整。
2. 搜尋結果的最新日期約為 2026-08，與報告日期 2026-10-25 相隔約兩個月，情緒可能已改變。
3. yf 的 insider 與 Yahoo 通道異常，需以 TWSE/TPEx 公開資料交叉確認。
4. 目標價與股價數字不一致，需核對原始券商報告。

## 來源

- [CMoney 股市 3081 論壇](https://www.cmoney.tw/forum/stock/3081?tab=column)
- [CMoney 股市 3081 新聞](https://www.cmoney.tw/forum/stock/3081?tab=news)
- [Histock 3081 財務報表](https://histock.tw/stock/3081/%E8%B2%A1%E5%8B%99%E5%A0%B1%E8%A1%A8)
- [Ctee 新聞 2026-03-26](https://www.ctee.com.tw/news/20260326700837-430201)
- [China Times 2026-07-15](https://wantrich.chinatimes.com/news/20260715900297-420101)
- [Yahoo 股市 注意股：聯亞 近5日漲11.30%](https://tw.stock.yahoo.com/news/%E9%80%9A%E7%B6%B2%E8%82%A1-%E6%B3%A8%E6%84%8F%E8%82%A1-%E8%81%AF%E4%BA%9E-%E8%BF%915%E6%97%A5%E6%BC%B211-30-235118852.html)
- [Wantgoo 三大法人趨勢（未讀取）](https://www.wantgoo.com/stock/3081/institutional-investors/trend)

SENTIMENT REPORT COMPLETE
