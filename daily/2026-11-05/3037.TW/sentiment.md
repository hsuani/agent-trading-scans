# Sentiment — 3037.TW (欣興) as of 2026-11-05

> 資料時效註記：執行日為 2026-11-04，分析基準日為 2026-11-05。分析師評等快照為工具回傳值；媒體新聞最新僅到 2026-10-12；11 月營收要到下月初才公布。

## Analyst consensus

19 家：6 strongBuy / 12 buy / 1 hold / 0 sell / 0 strongSell（yf `rec_summary`）。 買進類佔 95%，賣出為 0。

| 券商 / 來源 | 評等 | 目標價（TWD 元） | 時間 | 備註 |
|---|---|---|---|---|
| 美銀證券 (BofA) | 買進 | 1,400 → 1,650 | 2026-10 | ASIC 帶動 ABF 稼動率，看好 PCB/HDI 毛利率改善 |
| 日系外資 | 買進 | 1,000 → 1,500 | 2026-07 法說後 | 維持買進 |
| 多家外資 | 維持評等 | 區間 1,000–1,500 → 1,200–1,500 | 2026-07 法說後 | 目標價區間小幅上修 |
| 摩根士丹利 | 優於大盤 | 500 → 550 | 2026 年初 | 舊資料，時效較弱 |

- 近期動向：2026-07 法說後多家上修或維持；2026-10 美銀上調目標價至 1,650 元，是目前最新一筆公開的上修。
- 2025-12 有外資由中立升買進（目標價 150 → 290 元），亞系也上修至 271 元，屬於較舊的訊號。
- 限制：yf `recommendations` 三個期間（0m / -1m / -2m）數字完全相同，疑似為靜態快照，不能當成逐月評等變化來解讀。
- 依 `rec_summary` 與媒體目標價，無法在此確認目前股價，因此無法換算上行空間。來源之一顯示股價約 902 元，另一版約 688 元，數字不一致。

## Retail social

- Reddit (r/wallstreetbets、r/stocks)：**無法取得**。WebFetch 回傳無法連線 www.reddit.com，依規則軟失敗，略過。
- StockTwits：**無法取得**。api.stocktwits.com 在本環境無法解析（DNS 失敗），需由使用者在 session 網路設定中放行。
- X / 新聞鏈：WebSearch 僅找到 2026-10 的外資報導與 2026-07 的法說後報導；11 月的個股論壇討論很少。
  - 11 月初的論壇（histock 籌碼頁）留言以提問為主，例如「能否續抱」「後續走勢」，沒有明確多空共識。此段資料可信度低，是從搜尋摘要看到的，無法直接驗證原文。
  - 較早（7 月）有零星短線賣壓與信心偏弱的留言。

- 散戶量能：無法與基準比較（缺乏 Reddit/StockTwits 計數）。定性來看，11 月初論壇討論量低，未見明顯升溫。
- 散戶傾向：**無法判定**（資料不足，不強行歸類為看多或看空）。

- 主要話題（來自新聞與論壇摘要，非原文引用）：
  - ABF 載板受 AI / ASIC 需求帶動，產品組合與長約售價調升。
  - HDI 業務的獲利與執行風險。
  - 2027 年 EMIB-T 載板量產初期良率。
  - 股價高檔後能否續抱。

## Insider activity

Net 6mo: 無資料。yf `insider` 回傳空陣列，無法確認為零交易或資料缺漏，因此不能視為「無內部人交易」。台灣的董監持股申報（公開資訊觀測站）未在本次範圍內核對。

## Ownership shifts

- 內部人持股約 15.9%（yf `major_holders` insidersPercentHeld = 0.159）。
- 機構持股約 44.0%；占流通股約 52.3%。
- 機構家數 352 家。
- 趨勢：單一時點快照，沒有歷史序列，無法判斷集中度的增減方向。

## Net sentiment score

**Composite: bullish（信心：中等偏低）**

- 分析師面：強烈偏多。19 家中 18 家為買進，無賣出評等，近期目標價上修。信心：高（但快照可能過時）。
- 散戶面：無法判定。Reddit 與 StockTwits 皆無法取得，論壇訊號薄弱。
- 內部人面：無資料。
- 機構面：持股約 44%，無趨勢資料。
- 整體偏多的依據幾乎全部來自分析師端，故整體信心只能算中等偏低。

**Divergence flag: no（無法判定）**
- 目前無法確認散戶傾向，因此無法判斷是否與分析師傾向相反。若日後 StockTwits 或 Reddit 可用，應重新評估此欄位。

## 資料缺口與後續

1. 放行 api.stocktwits.com，補上 StockTwits 量與多空標籤。
2. Reddit 公開 JSON 被擋，需替代來源（或改用 PTT 股票板、Dcard 等中文社群）。
3. 內部人交易需改查公開資訊觀測站董監事持股申報，yf 空陣列不足採信。
4. 分析師評等需以券商最新研究報告或 yf 的逐月快照校正，確認 `recommendations` 是否真有時序變化。
5. 股價需以即時行情確認，目前兩個來源數字不一致（902 元 vs 688 元）。

## 來源（WebSearch 摘要）

- 美銀目標價調升至 1,650 元：https://finance.technews.tw/2026/10/12/unimicron-technologys-medium-to-long-term-profit-outlook-is-promising/
- 2026-07-30 法說後外資報導：https://www.ctee.com.tw/news/20260730701147-430201
- nStock 基本面摘要：https://www.nstock.tw/欣興做什麼.html
- histock 籌碼頁（11 月論壇留言）：https://histock.tw/stock/chips.aspx?no=3037
- 2025-12 外資升評等與目標價：https://ec.ltn.com.tw/article/breakingnews/5273495

SENTIMENT REPORT COMPLETE
