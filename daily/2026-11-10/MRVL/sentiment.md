# Sentiment — MRVL (Marvell Technology) as of 2026-11-10

資料來源狀態：yf 工具走快取（Yahoo cookie/crumb 失敗，屬預期），數據可用。Reddit 直接抓取被封鎖（WebFetch 失敗），StockTwits API 無法解析網域（DNS 失敗，需於 session 網路設定放行 api.stocktwits.com），故散戶情緒改以 WebSearch 的二手報導取得。

## Analyst consensus

rec_summary（yf，0m）：**7 Strong Buy / 31 Buy / 5 Hold / 0 Sell**（共 43 家，買進評等占 88%，無賣出評等）。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 0m（最新） | 7 | 31 | 5 | 0 | 43 |
| -1m | 8 | 35 | 4 | 0 | 47 |
| -2m | 8 | 32 | 6 | 0 | 46 |
| -3m | 8 | 31 | 5 | 0 | 44 |

觀察：最新月 Strong Buy 與 Buy 合計由 43 降至 39 附近（Buy 系列減少 4 家，Hold 增加 1 家），與近期評等下修方向一致，但 yf 工具未提供逐筆評等異動事件，無法逐家確認。

近期評等異動（WebSearch 二手來源，未全部直接核對原文）：
- **TD Cowen（2026-11-03 前後）**：由 Buy 降為 Hold，目標價由 $350 降至 $175；兩個獨立來源（StockTwits 轉載、German 報導）都提到 $175。另一份 Barchart 摘要寫 $245，日期不明，列為衝突。TD Cowen 理由：收購 Lumentum 後的「material headwinds」，並預估 2028 年約中個位數百分比稀釋；亦提及定價時點可能接近光學元件短週期高點。
- **B. Riley**：目標價下修至 $275（稀釋與整合風險）。
- **Oppenheimer**：重申 Buy，目標 $325（Barchart 引述，日期未確認）。
- 2026 年 5 月的上修（BofA $200、Citi $215、Stifel $230、KeyBanc $260、Morgan Stanley $195）已屬舊資料，僅作背景，不代表當前目標價。

目標價中位數無可靠 2026-11 數值，請勿直接引用舊目標價。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：WebFetch 被封鎖，無法取得貼文樣本、分數與留言數。WebSearch 亦未找到 MRVL 相關 Reddit 討論串。**DATA_UNAVAILABLE**。
- **StockTwits / X / 新聞論壇**：StockTwits API 無法解析（DNS 失敗）。依 WebSearch 摘要的二手報導，StockTwits 情緒於近期偏多（bullish），訊息量來到「extremely high」等級。此為二手轉述，未能直接核對原始訊息數與多空標籤比例。
- **聲量（相對量）**：定性判斷為近期高於平常。Lumentum 併購與 TD Cowen 下評後討論量上升，但無精確計數。
- **散戶傾向**：偏多（mixed-to-bullish），信心低（僅單一二手來源）。
- **主要主題**（依新聞與論壇摘要歸納，非直接取自貼文）：
  1. Lumentum 併購的稀釋與估值爭議（約 $115B 全股票交易，Lumentum 股東換股比 4.5:1，MRVL 股東約持有合併後公司 67%，預計 2028 年上半年完成）。
  2. AI 光學與資料中心連接的長期成長敘事（「AI connectivity platform」轉型）。
  3. 定製 ASIC 能見度與雲端客戶集中度（TD Cowen 舊有評論延伸）。
  4. 近期股價大跌（據報導單日最大約 -12.7%，週跌近 30%）後的逢低買進與停損討論。

## Insider activity

yf insider 紀錄，**近 6 個月（2026-05-10 至 2026-11-10）**，只計有成交金額之公開市場交易：

- **買進：$0**（6 個月內無任何公開市場買進）
- **賣出：約 $20.9M**（13 筆有金額交易）

| 日期 | 內部人 | 職稱 | 股數 | 金額 (USD M) |
|---|---|---|---|---|
| 2026-11-02 | Christopher R. Koopmans | President | 10,000 | 1.87 |
| 2026-09-15 | Matthew J. Murphy | CEO | 7,500 | 1.68 |
| 2026-09-01 | Christopher R. Koopmans | President | 10,000 | 2.03 |
| 2026-08-17 | Matthew J. Murphy | CEO | 7,500 | 1.77 |
| 2026-08-03 | Christopher R. Koopmans | President | 10,000 | 1.81 |
| 2026-07-16 | Sandeep Bharathi | Officer | 9,013 | 1.80 |
| 2026-07-15 | Matthew J. Murphy | CEO | 7,500 | 1.57 |
| 2026-07-01 | Christopher R. Koopmans | President | 10,000 | 2.82 |
| 2026-06-23 | Daniel J. Durn | CFO | 2,250 | 0.63 |
| 2026-06-16 | Sandeep Bharathi | Officer | 2,231 | 0.67 |
| 2026-06-15 | Matthew J. Murphy | CEO | 7,500 | 2.24 |
| 2026-05-15 | Willem A. Meintjes | CFO（前任） | 4,000 | 0.70 |
| 2026-05-13 | Matthew J. Murphy | CEO | 7,500 | 1.33 |

注意：
- 大量 CEO / President 固定股數定期賣出（每月約 7,500 或 10,000 股），形態接近預先排程（10b5-1）型態，但工具資料未標示計畫旗標，無法確認。
- 另有數十筆無金額的交易（多為 RSU 歸屬、稅務代扣或 Form 4 其他代碼），已排除於上列統計之外。
- 2026-05 以前的 Murphy / Meintjes / Koopmans 亦有大量無金額交易，未納入計算。
- 2026-11-02 Koopmans 以約 $186.97 賣出，為最新交易，距 TD Cowen 下評與股價大跌時點接近。

Ownership（yf major_holders）：機構持股約 81.9%（3,038 家機構），內部人持股約 0.50%。機構持股比例的時序變化本次未取得，**趨勢無法判斷**。

## Net sentiment score

- **分析師**：偏多（88% 買進以上，但最新一週有評等下修，TD Cowen 轉 Hold）。
- **散戶**：偏多，信心低（僅單一二手來源 StockTwits 摘要；Reddit 無資料）。
- **內部人**：偏空（6 個月約 $20.9M 賣出、0 買進，主要為 CEO 與 President 固定排程賣出）。
- **綜合評分：偏多（中性偏多），信心：中低**。主因為分析師共識仍強，但近期 TD Cowen 下評、Lumentum 併購稀釋與持續內部人賣出，削弱信心。

**Divergence flag：否**（散戶與分析師傾向同向偏多）。另須注意：內部人淨賣出與分析師及散戶偏多方向相反，屬獨立警示訊號，但多數為排程型態，解讀上不宜等同於看空。

## 資料缺口與衝突

1. Reddit 與 StockTwits 直接資料缺失（DATA_UNAVAILABLE），散戶判斷依賴二手報導。
2. TD Cowen 目標價有 $175 與 $245 兩個版本，以 $175（兩個獨立來源一致）為準，但仍非一手確認。
3. 2026-11-03 以後的股價與評等數據未能與 yf 0m 快照逐一對照，yf 快照是否已反映 TD Cowen 下評未能確認。
4. 機構持股趨勢無時序資料。

SENTIMENT REPORT COMPLETE
