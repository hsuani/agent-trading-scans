# Sentiment — TSLA as of 2026-11-27

資料來源狀態：yf 資料為 cache 回補（屬正常）；Reddit / StockTwits 直連主機在此沙箱被封鎖，改以 WebSearch 取得間接資料，時效與可信度偏低。

## Analyst consensus

yf rec_summary（當前，USD 不適用，單位為家數）：

| 評等 | 家數 | 佔比 |
|---|---|---|
| Strong Buy | 6 | 13.3% |
| Buy | 16 | 35.6% |
| Hold | 22 | 48.9% |
| Sell | 1 | 2.2% |
| Strong Sell | 0 | 0.0% |
| 合計 | 45 | 100% |

即 **22 buy / 22 hold / 1 sell**（strong buy 併入 buy 計算）。

近 3 個月趨勢（家數）：

| 期間 | Buy（含 Strong Buy） | Hold | Sell（含 Strong Sell） |
|---|---|---|---|
| 當前 (0m) | 22 | 22 | 1 |
| 前 1 月 (-1m) | 20 | 22 | 2 |
| 前 2 月 (-2m) | 19 | 21 | 4 |
| 前 3 月 (-3m) | 22 | 20 | 5 |

Recent moves：
- 賣方評等由 5 家降到 1 家，3 個月內明顯收斂；買方評等在 2 個月內由 19 回升到 22。整體偏向「Hold 為主、賣方退場」。
- WebSearch 所見：Bloomberg 資料經 Benzinga 於 2026-10 報導，賣方評等占 61 家中的 13.1%，為 2023-04 以來最低，較 2026-01 的 23.3% 下降。報導指出部分降幅來自 Wells Fargo 分析師 Colin Langan 離職，而非升評。TD Cowen 曾重申 Buy（日期不明）。
- 不同來源家數不一致：yf 為 45 家、Bloomberg 為 61 家，Barchart 摘要（日期不明）為 16 Strong Buy、2 Moderate Buy、20 Hold、3 Strong Sell。以 yf 為主要數字，其餘僅供參考。
- 個別升降評與目標價變動：DATA_UNAVAILABLE（yf 工具僅回傳彙總計數，未提供逐筆評等變動與目標價）。

## Retail social

- Reddit：直連 JSON 被封鎖（DATA_UNAVAILABLE）。WebSearch 找到 24/7 Wall St 2026-02 文章，引述 Reddit 社群情緒分數 38.0（bearish），趨勢由中性轉偏空。另有 r/wallstreetbets 一則大額短天期 put 貼文，約 1,549 upvotes，日期不明。2026-11 的 Reddit 討論量與傾向：DATA_UNAVAILABLE。
- StockTwits：直連 API 被封鎖（DATA_UNAVAILABLE）。WebSearch 摘要稱 2026-11-13 至 11-17 期間 StockTwits 情緒轉為 bearish，主因機器人計程車（Robotaxi）撞車事件與 Peter Thiel 相關基金減持。此為 AI 生成摘要，可信度低。訊息量數據：DATA_UNAVAILABLE。
- X：WebSearch 未取得 2026-11 有效結果（DATA_UNAVAILABLE）。
- 討論量（相對常態）：DATA_UNAVAILABLE（無提及次數資料，無法做定量比較）。
- 傾向：偏空（bearish-leaning）。早期 2026 與 11 月中的摘要一致指向看空情緒，多頭論述集中於「守住支撐、情緒未崩」。
- 主要主題：
  1. Robotaxi 安全疑慮：奧斯汀路測撞車事件，摘要稱累計 7 起（未驗證）。
  2. 大股東減持：Peter Thiel 相關基金大幅減持。
  3. 銷售與基本面：美國 11 月銷量疑似年減約 23%（單一德文報導，未經英文來源驗證）；Q3 FY2026 財報淨利下滑（Trefis 摘要，數字需驗證）。
  4. 估值與公司轉型：市場對機器人、能源業務能否支撐估值有分歧。
  5. 支撐位：多空都以中段 $380 附近、下探 $350 為關鍵價位討論。
- 代表性 crowd 觀點：無法取得原文 post，僅能依 WebSearch 摘要轉述。摘要指出多頭認為守住支撐即是韌性，空頭則認為同一測試顯示情緒脆弱。未引用原文。

## Insider activity

6 個月窗口：2026-05-27 至 2026-11-27。

| 類別 | 筆數 | 金額（USD） | 說明 |
|---|---|---|---|
| 公開市場買入 | 0 | $0 | 窗口內無 open-market buy |
| 公開市場賣出 | 2 | $1.99M | 全數為 CFO Vaibhav Taneja（2026-06-08 $1.05M；2026-09-08 $0.94M） |
| 選擇權行使（Conversion） | 1 | 名目 $7.09B | CEO Elon Musk 2026-06-16 行使 303.96M 股，行使價 $23.34；非市場交易，不計入買賣 |
| 無價格紀錄之處分 | 2 | — | Taneja 2026-06-05、2026-09-04 各約 6.5K 股，性質不明（疑為稅務扣繳），未計入 |

- 淨額：6 個月內 $0 買入、$1.99M 賣出，淨賣 $1.99M，規模極小。
- 窗口外參考：CEO Musk 2025-09-12 於 $371.90–396.36 公開買入約 2.57M 股，金額約 $1.00B，為近一年最大的內部人買盤；窗口外董事 Wilson-Thompson 2026-02 至 04 期間多次賣出（合計約 $30M）。
- 資料時效注意：最新一筆內部人交易為 2026-09-08，距 as-of 日約 80 天，無法確認 2026-09-09 至 11-27 之間是否有未揭露或未同步的申報。
- 角色分布：CEO 僅有選擇權行使與窗口外的大額買入；CFO 為窗口內唯一賣方；董事方面窗口內無交易。

## Ownership shifts

- 內部人持股：17.8%；機構持股：44.8%（占總股本），占流通股 54.5%；機構家數 5,298。
- 趨勢（季度間變化）：DATA_UNAVAILABLE（工具僅提供單一時點快照，無法判斷集中度的方向）。

## Net sentiment score

綜合判定：**中性偏空（neutral-to-bearish），信心：低**

- 分析師側：中性偏多。Buy 占約 49%，Sell 由 5 家降到 1 家，目前評等結構為 Hold 主導。
- 散戶側：偏空。早期 2026 Reddit 指標為 bearish，11 月中旬 StockTwits 摘要亦為 bearish，主題集中於 Robotaxi 安全與減持。
- 內部人側：輕度偏空。窗口內僅 CFO 小額賣出 $1.99M，無公開買入；但 CEO 於窗口外有 $1.00B 買盤，訊號相互矛盾。
- 信心受限原因：Reddit / StockTwits / X 2026-11 原始數據皆為 DATA_UNAVAILABLE；多數散戶結論來自 AI 生成的聚合摘要；分析師家數在不同來源間不一致；內部人資料有約 80 天時效缺口。

Divergence flag：**是**。散戶傾向偏空，但分析師賣方評等持續下降、買方評等回升，兩者方向相反。此背離在過去具有參考價值，但本次因散戶數據缺失，無法確認散戶端的最新強度。

SENTIMENT REPORT COMPLETE
