# Sentiment — 6510.TWO（中華精測）as of 2026-10-10

> 資料時效聲明：系統今日日期為 2026-10-09，本報告以要求的 as-of 日期 2026-10-10 標註，但實際可取得的最新資料止於 2026 年 9 月初（重訊 2026-09-08、8 月自結 EPS）。未找到 2026 年 10 月的任何散戶討論、券商評等或內部人申報。以下結論應視為「截至最新可取得資料」，而非當日快照。

## Analyst consensus
yf `rec_summary`（期間標示 0m，未附日期）：10 家 — 4 strongBuy / 6 buy / 0 hold / 0 sell，即 **10 買進、0 持有、0 賣出**。
- 近 3 個月趨勢：-3m 為 8 家（4 strongBuy + 4 buy），目前增至 10 家，全部偏多，評等結構無降級。
- yf `recommendations`（個別評等變動明細）回傳空陣列，無法確認近期個別升降評等。
- 目標價：各來源數字互相矛盾，不可直接採用。
  - TradingView 共識（8 家）：平均 1,172.5 TWD，區間 777–2,050 TWD，總體評等 buy，但多數為中性（來源日期不明）。
  - AlphaSpread：平均 4,012 TWD，區間 580.75–5,145 TWD（頁面股價 2,495 TWD，日期不明）。
  - 中信投顧：「買進」，推測合理股價 5,400 元（引自 CMoney 筆記／媒體，日期未明確）。
  - 本土法人 2025 年 8 月調升目標價至 1,050 元，屬舊資料。
- 法人 2026 全年 EPS 預估上修至 65–68 元（媒體引述，非官方數字）。
- Simply Wall St（更新於 2026-02-11）的 DCF 估值 NT$561，低於當時股價，屬估值模型觀點而非分析師評等。

## Retail social
- **Reddit**：本次未以 WebFetch 讀取 r/wallstreetbets、r/stocks 的 JSON 搜尋（依任務指示不使用 WebFetch 抓金融網頁），WebSearch 亦未找到 6510 相關的 Reddit 討論串。**DATA_UNAVAILABLE**（Reddit 面向）。
- **StockTwits**：未取得。本次未存取，亦未找到可引用的資料。**DATA_UNAVAILABLE**。
- **X / PTT / 中文社群**：以 WebSearch 為主，取得 CMoney 股市爆料同學社團（精測版）與部分 PTT 引述摘要，未能取得 PTT 原文。
  - 多空交錯。部分網友看好主力信心與後市；另有大量質疑，認為「主力說法真實性存疑」、擔心被炒作，並預期短線仍需洗盤。
  - 有網友提醒版面上「攻擊性帳號」出現頻率升高，對資訊來源風險有戒心。
  - 有網友指股價已回到年線附近，視為技術面支撐。
  - 代表性言論（引述，≤15 字）：「精測都打到年線」、「精測版面上，這些攻擊帳號出現頻率變超高」。
- **聲量（buzz volume）**：定性判斷。公司曾被列為注意股，且公告有價證券多次達注意交易資訊標準，顯示關注度偏高；但無法取得與歷史基準的提及量比較，只能判定為「高於一般」。
- **主要主題（Themes）**
  1. 主力動向與洗盤／炒作疑慮（散戶最主要分歧點）
  2. 基本面成長：營收連續創高（2026 年 1 月創單月新高，6 月 5.74 億年增 40.2%，7 月 6.15 億年增 49.9%，前 7 月累計年增 30.0%）
  3. 8 月自結 EPS 5.29 元、年增約 94–95%
  4. 先進封裝、MEMS 探針卡技術驗證通過（媒體觀點），AP 測試需求改善
  5. 技術面：年線支撐、短期波動大、近 5 日漲幅明顯
  6. 相對同業的「結構性折價」（單一文章觀點）

## Insider activity
Net 6mo: **DATA_UNAVAILABLE**。
- yf `insider` 回傳空陣列（Cookie／crumb 抓取失敗，回退至快取，仍無資料）。
- WebSearch 未找到 2026 年董監事持股申報增減資料；中時財經頁面的「董監持股」區塊擷取時無數字。
- 已知人員（僅名單，無交易資訊）：董事長洪維國、總經理黃水可（來源：中時財經頁面）。
- 建議直接查詢臺灣證券交易所「公開資訊觀測站」之董監事持股申報與內部人持股轉讓事前申報。

## Ownership shifts
yf `major_holders`（快取，日期未標示）：
- 內部人持股比例（insidersPercentHeld）：36.82%
- 機構持股比例（institutionsPercentHeld）：27.44%
- 機構占浮通股比例（institutionsFloatPercentHeld）：43.43%
- 機構家數（institutionsCount）：74
- 趨勢：**無法判定**。僅有單一時點快照，無法比較機構持股的增減方向。

## Net sentiment score
Composite: **偏多（bullish）**，信心 **低-中（low-to-moderate）**。
- 分析師面：偏多且強。10 家全數買進、無賣出、近 3 個月家數增加。但目標價來源互相矛盾，無法判斷目標價的實際上修幅度。
- 散戶面：中性偏多但分歧大。基本面數字（營收、EPS）強勁，但社群對主力操作存疑、對炒作與洗盤有顧慮。
- 內部人面：DATA_UNAVAILABLE，無法納入評分。
- 資料缺口（Reddit、StockTwits、內部人申報、2026 年 10 月資料）降低整體信心。

Divergence flag: **部分分歧（partial）**。分析師面明確偏多，散戶面以疑慮與觀望為主，方向上並非完全相反，但語氣落差明顯。散戶的疑慮集中在「股價是否被操作」，而非基本面，這類分歧在主力操作型個股上常見，但由於樣本僅來自中文論壇與媒體摘要，參考性有限。

## 資料來源與限制
- yf 工具：rec_summary、recommendations、insider、major_holders（部分為快取回退）。
- WebSearch：CMoney 股市討論區、nStock、MONEY LINK、TechNews 財經、中時財經、TradingView、AlphaSpread、Simply Wall St、GuruFocus、Yahoo 股市。多數結果日期不一，股價快照無法互相對照。
- 未使用 WebFetch 抓取任何金融網頁，依任務規定。

SENTIMENT REPORT COMPLETE
