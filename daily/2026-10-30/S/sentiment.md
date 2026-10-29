# Sentiment — S (SentinelOne, NYSE) as of 2026-10-30

> 資料擷取時點為 2026-10-29（系統日期）；報告日期依任務設定為 2026-10-30。Reddit 與 StockTwits 本次無法取得，散戶面為資料缺口。

## Analyst consensus
目前 34 位分析師（yfinance rec_summary, 0m）：**18 Buy**（含 Strong Buy 3）/ **15 Hold** / **1 Sell**（含 Strong Sell 1）。
近三個月走勢（-3m → 0m）：Buy 22 → 18（-4）、Hold 13 → 15（+2）、Sell 0 → 1（+1），評級有向 Hold 漂移的跡象。

近期動作（WebSearch 彙整，為第三方聚合資料，未逐篇核對原始券商報告）：
- Needham 維持 Buy，目標價 31 USD（2026-10-13）
- Yorkville Ives 首次給予 Buy，目標價 32 USD（2026-10-06）
- FBN Securities 降評至 Hold，目標價 24 USD（2026-10-06）
- TD Cowen 目標價由 26 USD 上調至 29 USD，維持 Buy（2026-10-02）
- Raymond James 降至 Hold（2026-05-29）；Scotiabank 升至 Buy，目標價 23.50 USD（2026-07-06）

平均目標價因聚合來源與時間窗不同而分歧：MarketBeat 23.92 USD（2026-10-13）、Google Finance 24.25 USD（近三月）、StockAnalysis 19.50 USD、Investing.com 19.45 USD（後兩者日期不明，可能偏舊）。
參考價位：2026-10 初內部人售股價約 25.26–25.33 USD；MarketBeat 2026-10-13 報導開盤約 25.71 USD。

## Retail social
- **Reddit（r/wallstreetbets, r/stocks）**：WebFetch 遭拒（無法連線 reddit.com），本次未取得任何貼文，無法判斷散戶語氣。
- **StockTwits**：api.stocktwits.com 解析失敗（DNS 無法解析，需於 session 網路設定中允許該網域）。依規則未重試，本次不納入。
- **X / 新聞聊天**：WebSearch 結果以券商評等與內部人交易的新聞稿為主，未找到可辨識的散戶個人觀點貼文，無可引用樣本。
- **Retail buzz 量**：無法量化，資料不足。
- **Retail tilt**：無法判定（bullish / bearish / mixed 皆不下結論）。
- **Themes**：無可靠主題歸納。僅能從公開資料看到的市場結構面：空頭部位約 5.1% float、Put/Call 約 1.04（Benzinga 頁面，日期不明，僅供參考）。
- 基本面背景（非散戶言論）：MarketBeat 9 月報導指公司仍未獲利，淨利率約 -30.95%。

## Insider activity
統計區間：2026-04-30 至 2026-10-29，以 yfinance insider 之 "Sale" 列計（排除選擇權行使、股票獎勵、贈與與無金額列）。
Net 6mo: **$0 buys, 約 31.97M USD sells**（淨賣出約 31.97M USD，30 筆）。買入交易為 0。

依人員分組（USD）：
| 人員 | 職稱 | 6mo 賣出（M USD） |
|---|---|---|
| Tomer Weingarten | CEO | 約 25.79 |
| Sonalee Parekh | CFO | 約 2.57 |
| Robin Tomasello | Officer | 約 1.02 |
| Keenan Conder | Officer | 約 0.90 |
| Barry Padgett | President | 約 0.86 |
| Ana Pinczuk | Officer & Director | 約 0.82 |

Notable：
- CEO Tomer Weingarten 於 2026-10-05 以約 25.26 USD 賣出 527,368 股（約 13.32M USD），同日行使 500,000 股選擇權（行使價 9.74 USD）。
- 2026-09 至 2026-10 初，多名高階主管集中在約 19.4–25.3 USD 區間出售（CFO、President、CEO）。
- 6 月下旬有董事會成員的股票獎勵（Stock Award），非市場買入。
- 2025-12-16 董事 Mark Peek 有一筆公開市場買入（約 0.60M USD），為 6 個月窗外的唯一買入。
- 留意：CEO 多數賣出呈月度、規律節奏，是否屬 10b5-1 計畫需回查 Form 4 附註，本報告無法確認。

## Ownership shifts
- 機構持股約 86.4%（流通股約 87.2%），機構數 656 家。
- 內部人持股約 0.89%。
- 本工具僅提供當前快照，無歷史季度變化，**機構集中度趨勢無法判定**。

## Net sentiment score
- **分析師面**：偏多但降溫。多數為 Buy（18/34），但近三月 Buy 減少、Hold 與 1 筆 Sell 增加。傾向：**bullish-lite**（信心：中）。
- **內部人面**：偏空。6 個月內部人淨賣出約 31.97M USD，無買入。解讀需留意多數為行權與售股的例行模式（信心：中）。
- **散戶面**：資料缺口，無法評分（信心：無）。
- **綜合**：**neutral**（信心：低至中）。分析師與內部人方向相反，但散戶端缺失，無法做完整三方比對。

Divergence flag: **無法判定**（散戶 tilt 缺失）。
補充：分析師多數偏多與內部人淨賣出之間存在方向背離，屬於需追蹤的訊號，但這不是散戶與分析師之間的背離。
後續若 Reddit 或 StockTwits 可連線，應補抓後再評估散戶面。

SENTIMENT REPORT COMPLETE
