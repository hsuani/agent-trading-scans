# Sentiment — FANUY (FANUC Corp ADR) as of 2026-11-13

資料截止：2026-11-12（yf cache 更新時間 2026-11-12 15:05 UTC，價格快照 2026-11-12 14:49）。未使用 2026-11-13 之後資料。
價格基準：FANUY 約 17.19 USD（OTC Markets OTCPK，日內 -3.75%，前收 17.86 USD）。

## Analyst consensus

資料來源：`pipeline/tools/yf FANUY rec_summary`（cache 回退 `prices/yf/FANUY.json`）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當前 (0m) | 1 | 0 | 1 | 0 | 0 |
| 一個月前 (-1m) | 0 | 0 | 2 | 0 | 0 |

目前 2 位分析師：1 買進 (Strong Buy) / 1 持有 (Hold) / 0 賣出。覆蓋家數僅 2，樣本過小，統計意義有限。

- 近期動向：一個月前為 2 Hold，目前出現 1 家升至 Strong Buy，屬於單邊上調，但 yf 歷史評等明細 (`recommendations`) 只有兩個期間彙總，無法列出具體券商與日期。
- 目標價 (yf info)：平均 22.70 USD、最高 22.81 USD、最低 22.58 USD。三者幾乎相同，代表兩位分析師目標價高度接近。相對 17.19 USD 約有 +32% 上行空間（以 2 家平均計）。
- 目標價變動歷史：DATA_UNAVAILABLE（cache 無歷史目標價序列）。
- 外部搜尋交叉驗證：WebSearch 結果顯示 MarketBeat 為 Strong Buy (1 Buy)、pricetargets.com 為 2 Strong Buy，與 cache 的 1 Strong Buy + 1 Hold 不一致，且頁面多為 2026 年中以前快照，以 cache 為準。另一組「8 買 / 10 持有 / 2 賣（20 家）」數據屬於東京上市 6954 的日圓語境，非本 ADR 覆蓋，未採用。

## Retail social

- Reddit：DATA_UNAVAILABLE。依規定不直接抓取 Reddit/StockTwits，WebSearch 也未找到 r/wallstreetbets、r/stocks 相關 FANUY 討論串。
- StockTwits / X：DATA_UNAVAILABLE。WebSearch 未回傳 2026-11 期間 X 貼文或論壇討論。
- 討論量：無法量化（DATA_UNAVAILABLE）。FANUY 為 OTC 粉單 ADR，流動性低（10 日均量約 127 萬股、但 2026-11-12 盤中僅 3,214 股），散戶社群討論度預期偏低，屬推論，非實測數據。
- retail tilt：無法判定（DATA_UNAVAILABLE）。
- 可得的替代情緒訊號：TipRanks 自動化情緒標籤為 Positive、動能指標為負（WebSearch 摘要，2026 年快照，日期不明）；MarketBeat 新聞情緒分數 0.86（2025-10 快照，已過時，僅作背景）。這些是自動化或過時資料，不代表散戶看法。
- 主題（僅能從 WebSearch 與 cache 歸納，無法確認是否為散戶主流看法）：
  - 估值偏高：trailing P/E 約 25.3、forward P/E 約 25.7（yf）；另有來源給出 P/E 45.31，口徑不一。
  - 日股 6954 價格與 ADR 價格的換算與匯率影響，可能是非專業讀者的主要疑問點。
  - 公司為工業自動化（CNC、機器人）龍頭，市場討論多連結 AI / 機器人需求（屬一般產業敘事，缺乏 2026-11 具體引述）。
- 代表性引述：DATA_UNAVAILABLE（無可引用之 2026-11 散戶貼文）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。
- `pipeline/tools/yf FANUY insider` 與 cache `insider` 皆回傳空陣列，無法判定 6 個月內買賣金額。
- 注意：yf `companyOfficers` 列出 CEO Kenji Yamaguchi、CFO Ryuji Sasuga 等，其 `exercisedValue` 與 `unexercisedValue` 皆為 0，此欄位不代表交易，不可解讀為無交易的證據。
- `major_holders` 顯示 insidersPercentHeld = 0.0%（以 ADR 口徑計，參考價值有限）。

## Ownership shifts

- 機構持股比例：0.23%（institutionsPercentHeld 0.00232）；機構家數 27 家（yf major_holders）。
- 最大持有人：Aristotle Capital Management，2026-06-30 持 3,559,342 股，季增 -5.8%。其餘多為小型持股（數千至數萬股）。
- 2026-09-30 季報中，多數小型持有人呈小幅增減，無明顯集中或撤離趨勢。例如 Hantz Financial 持 71,936 股（-12.8%）、Sankala Group 持 43,836 股（+15.8%）。
- 判讀：ADR 機構持股比例極低，可能因為 ADR 口徑與母公司 6954 (TSE) 持股分開計算。以本 ADR 口徑，無法判斷機構集中度趨勢是否有意義。

## Net sentiment score

- 分析師面：偏多（Buy / Strong Buy 1 家、Hold 1 家，平均目標價高於現價約 32%），但樣本僅 2 家，信心度低。
- 散戶面：無法評估（DATA_UNAVAILABLE）。
- 內部人面：無法評估（DATA_UNAVAILABLE）。
- 機構面：中性偏弱，持股極少，無明顯方向。
- 綜合：**中性（偏多，信心：低）**。主要依據為分析師評等與目標價，其他維度缺乏資料，不足以構成完整情緒判斷。

Divergence flag：無法判定（retail tilt 為 DATA_UNAVAILABLE，無法與分析師面比較）。

資料缺口摘要：
1. Reddit / StockTwits / X 2026-11 討論：DATA_UNAVAILABLE。
2. 內部人交易（6 個月）：DATA_UNAVAILABLE（yf 回傳空）。
3. 分析師評等歷史與目標價變動序列：DATA_UNAVAILABLE（僅有兩期彙總）。
4. 覆蓋樣本：僅 2 家分析師，結論需保守解讀。

SENTIMENT REPORT COMPLETE
