# Sentiment — AVGO (Broadcom) as of 2026-11-10

資料品質: 分析師評級與內部人交易來自 yf 工具（cache fallback，屬預期狀況）；散戶輿情僅能透過 WebSearch 取得彙整頁面，Reddit 直接抓取與 StockTwits 皆無法存取（見下方 DATA_UNAVAILABLE 標記）。整體信心偏低。

## Analyst consensus

評級分布（yf rec_summary，N = 51）:

| 評級 | 0m（目前） | -3m | 變化 |
|------|-----------|-----|------|
| Strong Buy | 8 | 8 | 0 |
| Buy | 41 | 37 | +4 |
| Hold | 2 | 4 | -2 |
| Sell | 0 | 0 | 0 |
| Strong Sell | 0 | 0 | 0 |

- 買進方（Strong Buy + Buy）佔 96%，無賣出評級。
- 注意: yf 的 `0m` 與 `-1m` 數值完全相同，可能是 cache 未更新，目前分布僅作參考。
- 另一來源 MarketBeat 顯示 "Moderate Buy"、約 45 位分析師、平均目標價 $530.52，與 yf 的 N 不一致，需以主來源核對。

近期評級動作（yf `recommendations` 端點未回傳逐筆升降評等紀錄，以下來自次要來源，未能完全核實）:

| 日期（來源所述） | 機構 | 動作 | 內容 |
|------|------|------|------|
| 2026-10-27 | William Blair | 降評 | Outperform → Market Perform |
| 2026-10 下旬（日期不確定） | DA Davidson | 升評 | Neutral → Buy，目標價 $350 → $400 |
| 日期不明 | BofA | 降目標價 | $530 → $460，維持 Buy |
| 2026-07-07 | Erste Group | 降評 | Hold |
| 2026-06-04 | Macquarie | 降評 | Outperform → Neutral，目標價 $437 |
| 後續（日期未確認） | Macquarie | 升評（來源衝突） | Outperform，目標價 $490 |

目標價共識（來源不一）:
- MarketBeat 平均目標價 $530.52；24/7 Wall St. 約 $530.14。
- Quiver Quantitative 統計 6 個月內 22 位分析師中位數 $450。
- 股價參考: 2026-11-05 收盤約 $291.53（兩個來源一致），為一年來最低收盤；2026-10-30 約 $326。目標價中位數約為收盤價的 1.5 倍以上，分析師目標與市價落差大，屬於評級偏多但價格動能弱的分歧。

## Retail social

- **Reddit**: DATA_UNAVAILABLE（www.reddit.com 無法直接存取）。改以 WebSearch 摘要: AltIndex 估計約 30 則/日提及（相對 investing subreddit 屬正常水準，非熱門也非冷清），Reddit 情緒分數 71/100 判定為中性。WSB 中 AVGO 多為半導體上漲時的帶過式提及，非主題討論。
  - 代表性觀點（來源為搜尋摘要，非原文直接核對）: 估值比較爭論，「AVGO 與 NVDA 估值必有一方不合理」。
  - 多方論點: Q1 FY2026 財報「beat and raise」、與 Google 長期 TPU 供應協議延續至 2031。
  - 注意: 搜尋結果多為 2025 年底至 2026 年中的貼文，時效性不足。
- **StockTwits**: DATA_UNAVAILABLE（api.stocktwits.com 無法解析，需於 session 網路設定中放行）。
- **X / 新聞輿情（WebSearch）**:
  - 偏多敘事: Anthropic 相關 AI 客戶與擬議中約 $63B 的融資結構，被視為 AI 客製晶片的資金後盾。
  - 偏空敘事: 估值與利率、超大規模雲端業者資本支出能否持續、Meta 等客戶轉向自研 AI 晶片可能降低對外部供應商的依賴。
  - 情緒指標（無日期，僅作快照）: 看多比例由 12.6% 降至 1.9%，已轉為略偏空。
  - 近期價格新聞: 2026-11-05 跌約 10.4%（Trefis），該日半導體族群普跌，媒體未找到公司專屬利空；TIKR 報導一週跌幅約 15.5%。兩者幅度來源不一，需以交易所收盤資料核實。
  - 代表性標題（非觀點原文）: 「Broadcom Just Dropped 15% in a Week. Is It Time to Sell, or Load Up?」
- **Buzz 量能**: 相對常態屬正常水準（AltIndex 估計約 30 則/日），未見異常放量。
- **Themes**: AI 客戶集中度與 Anthropic 題材 / 估值與 NVDA 比較 / 半導體族群拋售 / 自研晶片替代風險 / 資本支出週期。

- **Retail tilt**: 中性偏弱（mixed），低信心。

## Insider activity

以 yf `insider` 近 6 個月（2026-05-10 至 2026-11-10）統計，金額單位 USD:

| 日期 | 內部人 | 職位 | 交易 | 股數 | 金額 (USD M) |
|------|-------|------|------|------|------|
| 2026-06-11 | YOU HARRY L | Director | 公開市場買進 | 1,000 | 0.37 |
| 2026-06-15 | O'TOOLE AMIE THUENER | CFO | 股票獎勵 | 50,000 | 0 |
| 2026-06-17 | BRAZEAL MARK DAVID | Officer | 賣出 | 8,152 | 3.18 |
| 2026-06-24 | SAMUELI HENRY | Director | 賣出 | 654,241 | 250.01 |
| 2026-06-25 | BRAZEAL MARK DAVID | Officer | 賣出 | 25,000 | 9.68 |
| 2026-06-29 | PAGE JUSTINE F. | Director | 賣出 | 1,602 | 0.60 |
| 2026-07-08 | BRAZEAL MARK DAVID | Officer | 賣出 | 25,000 | 9.48 |
| 2026-07-08 | DELLY GAYLA J | Director | 賣出 | 1,890 | 0.73 |
| 2026-07-10 | BRAZEAL MARK DAVID | Officer | 賣出 | 25,000 | 10.03 |

- 6 個月淨額: 買進 約 $0.37M（1 筆）；賣出 約 $283.7M（含單一董事大宗賣出 $250.0M）；淨賣出約 $283.3M。
- 買進方僅 1 位董事（YOU HARRY L，1,000 股）。CEO TAN HOCK E 於本視窗內無公開市場交易（最近一筆為 2026-04-08 贈與）。
- 資料時效: 最新一筆交易為 2026-07-10，7 月中至 11 月初無任何紀錄，可能為實際無申報或 cache 落後，需向 SEC EDGAR Form 4 核對。
- 需注意: Quiver Quantitative 在次要來源中稱 6 個月內有 212 筆交易（1 買 / 211 賣），與 yf 列表筆數差異極大，可能為統計口徑（含選擇權、獎勵、不同視窗）不同，以 yf 為主、Quiver 僅供參考。
- 解讀: 大量賣出集中於 6 至 7 月股價約 $370–400 區間，當前股價約 $291，內部人賣出時點高於現價。此為訊號之一，不代表內部人對後市的必然判斷（可能含預先排程計畫，無法由資料確認）。

## Ownership shifts

- 機構持股比例 79.9%（institutionsPercentHeld），機構數 6,290；內部人持股 1.9%。
- DATA_UNAVAILABLE: 機構持股季度變化趨勢（僅單一快照，無法判斷增減）。

## Net sentiment score

- **分析師**: 偏多（買進方佔 96%，無賣出評級；但 2026-10 起出現降評與降目標價）。信心: 高。
- **散戶 / 社群**: 中性偏弱（mixed），以 AI 題材為主、Reddit 量能正常、情緒分數中性；情緒指標快照顯示看多比例大幅下降。信心: 低（Reddit、StockTwits 無直接資料）。
- **內部人**: 偏空（6 個月淨賣出約 $283M，主要為單一董事大宗賣出；買進極少）。信心: 中。
- **股價動能**: 偏弱（3 個月跌約 31.7%，2026-11-05 創一年新低收盤）。
- **綜合**: 中性（neutral），信心: 低至中。分析師偏多與內部人及價格動能偏弱並存。

**Divergence flag: 是（中度）**。分析師評級偏多，而內部人淨賣出與散戶情緒轉弱方向相反。散戶資料不完整，此判斷需於 Reddit / StockTwits 可存取後覆核。

## 資料缺口 (DATA_UNAVAILABLE)

- Reddit 直接貼文與 subreddit JSON: DATA_UNAVAILABLE（403 / 無法連線）
- StockTwits 串流: DATA_UNAVAILABLE（DNS 無法解析）
- X 貼文量化統計: DATA_UNAVAILABLE（僅有 WebSearch 摘要）
- 機構持股趨勢: DATA_UNAVAILABLE（單一快照）
- 逐筆評級升降歷史: DATA_UNAVAILABLE（yf recommendations 未回傳，僅有次要來源）

SENTIMENT REPORT COMPLETE
