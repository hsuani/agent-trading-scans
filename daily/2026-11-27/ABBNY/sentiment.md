# Sentiment — ABBNY (ABB Ltd ADR) as of 2026-11-27

資料時效註記：yf 數據來自 `prices/yf/ABBNY.json` cache（refreshed 2026-11-26 16:47 UTC，live 呼叫失敗後改用 cache，屬正常情況）。系統當日為 2026-11-26，本報告以使用者指定的 as-of 日期 2026-11-27 標示，實際資料為 11-26 盤後快照。

## Analyst consensus

ADR 覆蓋（yf rec_summary，當期 0m）：0 strong buy / 0 buy / 5 hold / 0 sell / 1 strong sell，共 6 家。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當期） | 0 | 0 | 5 | 0 | 1 | 6 |
| -1m | 0 | 0 | 5 | 0 | 1 | 6 |
| -2m | 0 | 0 | 3 | 0 | 2 | 5 |
| -3m | 0 | 0 | 3 | 0 | 2 | 5 |

- 近三個月：覆蓋家數由 5 增至 6，無任何 Buy 或 Strong Buy 評級，評級結構為 Hold 為主、少數強烈賣出。
- 近期升降評等（個別機構名稱與日期）：DATA_UNAVAILABLE（yf 僅提供彙總計數，無逐筆 upgrade / downgrade 明細）。
- 目標價變動：無可靠的時序數據。網路來源資料互相矛盾且日期不明：Investing.com ADR 頁顯示 5 家分析師、0 buy / 3 hold / 2 sell，平均 12 個月目標價 93.20 USD（另一頁為 92.60 USD）；TipRanks 平均目標價 52.58 USD，與其他來源差距過大，疑為過時數據。
- 瑞士本地 ABBN 覆蓋（非 ADR，僅供參考）：據 cash.ch 引述 Bloomberg 資料為 14 buy / 23 hold / 2 sell，平均目標價 82.60 CHF；Goldman Sachs 將目標價下調至 79 CHF 並維持 Neutral。此覆蓋宇宙與 ADR 不同，不應直接混用。
- 來源差異註記：yf 顯示 1 家 strong sell，Investing.com 顯示 2 家 sell，計數口徑不一致。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。沙箱封鎖 reddit.com 直接存取，改用 WebSearch 查詢，未找到任何針對 ABBNY 的 Reddit 討論串。
- StockTwits：DATA_UNAVAILABLE。直接 API 呼叫未執行（依指示 host 受阻），WebSearch 僅回傳 stocktwits.com 的 symbol 頁面殼，無實質貼文內容。
- X / 新聞聊天：WebSearch 結果以新聞與分析師摘要為主，無可辨識的散戶貼文樣本。無可直接引用的散戶原話（無樣本可引）。
- 討論量（相對典型）：無法量化，定性判斷為低。搜尋結果中僅見第三方報價頁的小型投票（Investing.com 的 ABBN 多空投票僅有 2026 年 4 至 5 月的留言）與 Simply Wall St 社群敘事（4 位追蹤者），量能偏低。
- 散戶傾向：DATA_UNAVAILABLE（樣本不足，不做方向性判定）。
- 主要主題（來自新聞與社群敘事，非散戶貼文直接抽樣）：
  1. AI 資料中心需求與估值可持續性：2026 年夏季市場出現對龐大 AI 投資與估值是否可持續的疑慮，股價自 6 月高點回落約 24%（cash.ch 引述）。
  2. 估值分歧：Simply Wall St 社群敘事給出約 78.4 CHF 的公允價值，並稱股價低於該值約 10.7%（日期不明，屬單一社群觀點）。
  3. 分析師分歧：部分券商調升目標價、部分調降或提出更保守假設（Simply Wall St 敘事描述為「split view」）。

## Insider activity

Net 6mo（2026-05-27 至 2026-11-27）：DATA_UNAVAILABLE（無法確認淨買賣金額）。

- yf insider（live 與 cache 皆為空陣列 `[]`）：無資料可用，不能視為「無交易」。
- 網路來源（未能核對原始 Form 4 或瑞士 SIX 申報）：
  - Simply Wall St 與 InsiderScreener 皆提及 2026-05-04 董事集中買進，由董事長 Peter Voser 領銜，另有 6 位董事參與，價格約 85.61 EUR（Simply Wall St 列示）。
  - 同一批來源提到 Voser 於 2026-02 出售 30,000 股，以及 Timo Ihamuotila 於 2025-11 賣出，早於 6 個月窗口。
  - InsiderScreener 稱近 90 天淨買入超過 2 百萬 CHF、涉及 10 位內部人、無執行長或 CFO 交易。但其所列交易日期（2026-05-04）已超出 90 天窗口，且其中 Voser 條目的單價 466.22 與 197.41 CHF 與同日 78.42 CHF 明顯矛盾，數據品質存疑。
- 結論：5 月董事買進為最明確的內部人正向訊號，但落在 6 個月窗口的邊界外（約 6.8 個月前），且來源數據互相矛盾，不應作為 6 個月淨買賣的依據。
- Notable：Peter Voser（董事長）— 2026-05 買進（未驗證）；Voser — 2026-02 賣出 30,000 股（未驗證）。

## Ownership shifts

- 機構持股家數：84（yf major_holders，institutionsCount）。
- `institutionsPercentHeld` 回報 0.0015、`insidersPercentHeld` 回報 0.0，數值明顯不合理（ABB 作為大型股，機構持股比例不可能僅 0.15%），判定為 DATA_UNAVAILABLE，不採用。
- 2026-09-30 13F 前幾大持股變動（yf inst_holders，樣本 8 筆，非完整名單）：
  - Northeast Investment Management：680,799 股，-0.9%
  - Kornitzer Capital Management：283,580 股，-7.0%
  - Great Lakes Advisors：53,074 股，+34.2%
  - 其餘小型持有人變動多為 0 或 -1% 至 -3%
- 集中度趨勢：DATA_UNAVAILABLE（僅單期快照，無前期比較，無法判定集中或分散趨勢）。樣本顯示無明顯大規模加碼或撤出，但證據薄弱。

## Net sentiment score

- **Composite：neutral（信心：低）**
  - 分析師面（偏中性至偏空）：ADR 覆蓋 0 buy，多數 hold，少數 strong sell；瑞士本地覆蓋則偏正面（14 buy），兩者口徑不同。
  - 散戶面：DATA_UNAVAILABLE，無法納入評分。
  - 內部人面（不確定，偏正）：5 月董事集中買進為正向訊號，但窗口與數據品質存疑。
  - 媒體敘事（中性）：AI 估值疑慮與股價自高點回落，同時仍有分析師調升目標價。
- **Divergence flag：無法判定**。因散戶傾向為 DATA_UNAVAILABLE，無法確認散戶與分析師是否方向相反。若僅以可得資訊比較，分析師面偏中性至偏空、內部人面偏正，兩者方向不一致，但此差異不足以構成散戶背離的證據。

## 資料缺口彙整

| 項目 | 狀態 | 說明 |
|---|---|---|
| Reddit 討論 | DATA_UNAVAILABLE | 直接 host 被封鎖，WebSearch 無結果 |
| StockTwits | DATA_UNAVAILABLE | 直接 API 未執行，搜尋僅見殼頁 |
| 逐筆評等變動 | DATA_UNAVAILABLE | yf 僅提供彙總計數 |
| 目標價變動 | DATA_UNAVAILABLE | 來源互相矛盾、日期不明 |
| 6 個月內部人淨買賣 | DATA_UNAVAILABLE | yf 為空，網路數據矛盾 |
| 機構持股比例 | DATA_UNAVAILABLE | yf 數值不合理 |
| 機構集中度趨勢 | DATA_UNAVAILABLE | 僅單期快照 |

SENTIMENT REPORT COMPLETE
