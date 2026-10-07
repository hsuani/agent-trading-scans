# Sentiment — 3231.TW (緯創 Wistron) as of 2026-10-08

資料時點注意：本機系統日期為 2026-10-07，最新可查到的市場數據停在 2026-10-01 收盤。以下「截至 10-08」指報告基準日，實際資料多為 10-01 或更早。

## Analyst consensus
yf `rec_summary`（當期）：17 buy（6 strongBuy + 11 buy）/ 0 hold / 0 sell。前一期（-1m）同為 17 buy / 0 hold / 0 sell；再前一期（-2m）為 14 buy（5 strongBuy + 9 buy）/ 2 hold / 0 sell。

近期評等與目標價（來自 WebSearch 新聞彙整，券商與日期未逐一核對）：
- 2026-08-04：美系外資在法說會後將目標價由 210 上調至 275 元，維持買進，認為 ODM 附加價值與 AI 伺服器毛利率有望續擴。
- 2026-06-15 前後：高盛維持買進，12 個月目標價 246 元。
- 2026-06-03：一家投顧維持買進，2027 年目標價由 190 上修至 240 元。
- 未註明日期：一家外資目標價由 215 上調至 225 元，維持買進。
- 2026-01：摩根士丹利維持加碼，目標價 215 元。
- 聚合網站單點數據：Macquarie 買進目標 400 元；JPMorgan 持有目標 165 元（日期不明，與其他來源差距大，僅供參考）。
- FactSet 共識：EPS 預估上修至 8.98 元，預估目標價 190 元（cnyes 報導，日期未確認）。

目前可查到的目標價多落在 225 至 275 元之間。以 10-01 收盤 190.50 元計，多數目標價仍有上行空間。

## Retail social
- Reddit：DATA_UNAVAILABLE。以 WebSearch 查 "reddit wistron 3231" 無相關討論串。台股散戶討論以 PTT、Dcard、CMoney 為主，Reddit 樣本不具代表性。
- PTT / Dcard：DATA_UNAVAILABLE（未能直接取得近期串文，僅搜尋到 PTT Stock 板舊文，2023-08 看多文，已過期）。
- CMoney 股市社群（近期彙整，樣本少）：偏樂觀的長線看法占多數，主軸為 AI 伺服器客戶與 EPS 上修預期；短線情緒中性，多數人在問關鍵價位。
  - 代表性觀點（摘要）：多名同學認為緯創每股收益展望樂觀、投資機會穩健提升。
  - 代表性觀點（摘要）：也有人提醒 AI 題材可能造成股價過度反應與短期修正。
- StockTwits / X：DATA_UNAVAILABLE（StockTwits 依任務規定未以 WebFetch 存取；WebSearch 無 X 上可用的近期樣本）。
- 聲量：DATA_UNAVAILABLE（無可靠提及次數）。定性觀察：2025-10 與 2025-12 法人消息曾引發熱議，近期無明顯爆量訊號可確認。
- 散戶傾向：中性偏多（樣本極少，信心低）。
- 主要主題：
  1. AI 伺服器與雲端客戶（Dell、ASIC 相關）帶動的獲利預期
  2. 每股盈餘上修與估值是否合理
  3. 追價風險與籌碼面波動（量大、價漲後的震盪）
  4. 2025-12 營收大增但股價反應不如預期後的失望情緒

## Institutional flow（補充，非任務必要項目）
- 2026-10-01：外資買超 29,330 張（約 55.87 億元），為當日外資買超第一名，前一交易日為賣超 1,846 張。投信當日個股買賣超未確認。
- 2026-07-23：外資買超 79,016 張，媒體同時提及投信賣超 16,731 張（兩數字的日期與歸屬需交易所資料再確認）。
- 2026-10-02 至 10-07 三大法人個股數據：DATA_UNAVAILABLE。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。
- yf `insider`：回傳空陣列，無交易紀錄可用。
- 快取 / 新聞備援（非 2026 資料）：董事長林憲銘於 2024-08 至 2024-09 連續買進，共 2,020 張（約 2 億元），累計持股約 44,619 張。
- 2026 年內部人申報轉讓：未查到。
- 持股比例（yf `major_holders`）：insidersPercentHeld 約 5.14%。

## Ownership shifts
- yf `inst_holders`：空陣列，無機構明細。
- yf `major_holders` 快照：institutionsPercentHeld 約 34.96%（float 口徑約 36.86%），institutionsCount 245。快照日期未標示。
- 持股變動趨勢（季度對比）：DATA_UNAVAILABLE。

## Net sentiment score
Composite: **bullish（信心：中等偏低）**
- 分析師面：強烈偏多。17 buy / 0 sell，且 2026-08 後仍有目標價上調。權重高。
- 籌碼面：外資近期持續買超（10-01 為大買超），偏多但單日數據不足以定論。
- 散戶面：中性偏多，樣本極少，權重低。
- 內部人面：無 2026 資料，不納入計分。
- 扣分因素：股價多個來源價格不一致（136 至 195 元），趨勢判斷有不確定性；多數目標價為 2026 年中以前的預估，時效性有限。

Divergence flag: **no**。散戶傾向未與分析師傾向相反，兩者大致同向偏多。但散戶樣本不足，此判斷可靠度低。若補得到 PTT 或 Dcard 近期串文，需重新檢視。

## Data gaps（DATA_UNAVAILABLE 彙整）
- Reddit 近期討論
- PTT / Dcard 近期串文
- StockTwits 與 X 近期貼文量與情緒
- 散戶聲量（提及次數）
- 2026 年內部人交易（yf insider 空，無法驗證）
- 機構持股季度趨勢與 inst_holders 明細
- 10-02 至 10-07 個股三大法人買賣超

SENTIMENT REPORT COMPLETE
