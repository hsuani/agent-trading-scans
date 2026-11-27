# Sentiment — GLD as of 2026-11-28

> ETF 標的：略過 insider 與 major_holders 分析（不適用）。改以黃金現貨情緒、retail 社群與策略師配置立場代替。
> 資料時效：本次搜尋可取得的最新日期約為 2026-11-18；11-19 至 11-28 之間幾乎沒有可確認的情緒資料。2026-11-28 之後的資料一律視為未知。
> 工具狀況：`pipeline/tools/yf GLD rec_summary` 回傳空值（連線 fc.yahoo.com 失敗），analyst 分佈記為 DATA_UNAVAILABLE。Reddit / StockTwits 直接抓取未執行（依指示僅用 WebSearch），以下為搜尋摘要所見的間接資訊。

## Analyst consensus

- GLD 本身的分析師評等：DATA_UNAVAILABLE（yf rec_summary 無資料）。
- 第三方彙整（Stockchase，時間不明確）：過去 12 個月 5 則評等，2 Buy / 0 Hold / 3 Sell，最近一則為 2026-06-26 的 Sell。樣本少，僅供參考。
- 技術型 AI 訊號（Tickeron，2026-11-10 至 11-12）：Aroon 轉向下降、MACD 轉負，模型給出續跌機率 68%–73%。此類為演算法輸出，非分析師意見。
- 策略師對黃金價格的預測（時間各異，需注意）：
  - Kitco 報導 Goldman Sachs 將 2026 年底目標由 $4,650 下調至 $4,150/oz（日期約 2026 年 11 月，與另一則較舊的 $4,900 目標有出入，以較新者為準）。
  - Deutsche Bank、JPMorgan 據報仍看 $6,000–6,300（年底，來源為二手報導，未直接核實）。
  - 一位分析師將年底目標下修至 $3,500/oz（看空端，來源不明）。
  - 黃金歷史高點為 $5,405/oz（2026-01-29）。
- 配置建議（黃金占組合比重）：
  - State Street（Aakash Doshi，2026 年中展望）：3%–10%，新資金宜 3%–5%。
  - Ned Davis Research（John LaForge，2026-05）：3%–8%。
  - Société Générale（2025-12 前後）：多資產組合中 10%。
  - Orion（Nolan Mauk）：0%–5%。
  - 策略師多半把黃金視為策略性分散工具，而非短線交易標的。
- 近期變動：多數機構在 2026 年 11 月金價跌破 $4,000 後轉趨保守，但未見大規模評等調降的直接證據（DATA_UNAVAILABLE 等級）。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：未能取得 11 月的即時搜尋結果。WebSearch 找到的 WSB 相關資料集中在 2026 年初：
  - 一則 Sherwood 報導指出，2026 年初 WSB 談論白銀（SLV）的次數遠多於 GLD，貴金屬討論偏向白銀。
  - Chart Exchange 快照顯示 GLD 留言兩極，例如「GLD is the only answer」與針對「SLV/GLD 套牢」的嘲諷。屬單次快照，不代表整體情緒。
  - 整體 tilt：無法判定 11 月情況（DATA_UNAVAILABLE）。早期（2026-03）偏多，後來隨金價回落轉弱。
- StockTwits：搜尋摘要顯示兩個快照，一為中性 50 分，一為 72 分看多（後者日期不明）。此數據可信度低，不可當作 11 月的代表值。
- X / 新聞 chatter：未取得 X 貼文。新聞面（Kitco 週報、Forex Peace Army 週更）的情緒以偏空為主，但這屬於專業或論壇評論，不等於 retail 社群。
- 情緒動態（新聞敘事）：
  - Kitco Wall Street 調查（2026-11-13 前後）轉為明顯看空，Main Street 也有轉空的報導（來自搜尋摘要的二手描述）。
  - 媒體出現「1980 年式崩跌」比較（2026-11-18 前後），把美元走強、殖利率上升、升息預期列為主因。
- 主要主題（themes）：
  1. 聯準會偏鷹與升息預期，實質利率與殖利率上升，形成機會成本壓力。
  2. 金價跌破 $4,000 後的「是否崩盤」與「是否抄底」之爭。
  3. 央行買盤仍是多方主要論點（Q2 2026 央行購金 288.9 噸，年增 62%；Q3 約 321 噸，年增 42%）。
  4. 白銀與黃金的 meme 化討論，WSB 注意力偏向白銀。
- 估計聲量：相對一般水準，無法量化（DATA_UNAVAILABLE）。

## Fund flows（ETF 層級背景，非 GLD 單一標的）

- 全球黃金 ETF 2026-09 淨流入約 US$10B，2026-Q3 累計約 US$31B（創紀錄）。
- 全球黃金 ETF 2026-10 淨流入約 US$2.7B，淨增持約 19 噸，總持有量達 4,275 噸（紀錄高）。北美基金出現流出，歐洲與亞洲為主要流入來源。
- GLD 單日流量（約 $550M、$950M 等）來自無日期的新聞頁，無法定位時間，不採用。
- 2026-11 全月流量：DATA_UNAVAILABLE（WGC 11 月報告預計 12 月初才出）。

## Insider activity

不適用（ETF 無內部人交易申報）。

## Ownership shifts

不適用（ETF）。機構持倉變化僅有零星個案（Greenlight 於 Q1 2026 減持 GLD 至 99,611 股；Third Point 於同期新開 95,000 股），屬單一基金個案，不具趨勢意義。

## Net sentiment score

- 綜合判斷：**偏空（bearish），信心低至中**。
  - 偏空依據：金價自 2026-01 高點 $5,405 大幅回落，11-16 至 11-18 創 14 個月新低（盤中低點約 $3,660–3,852，來源數字不一致）；技術指標轉弱；利率與美元走強；Wall Street 情緒轉空；2026-Q1 以來的 GLD 單一股票分析評等偏賣。
  - 偏多或抵銷因素：央行持續買入；全球黃金 ETF 持有量仍創紀錄（截至 2026-10）；長線策略師仍維持 3%–10% 配置建議，多數並未因短期下跌而撤回。
  - 信心低的原因：11-19 至 11-28 的資料缺失；retail 社群在 11 月無可用資料；分析師評等樣本少且時間不一。
- 背離旗標（Divergence flag）：**無法判定（DATA_UNAVAILABLE）**。Retail 在 11 月的 tilt 無可靠資料，因此無法確認 retail 與分析師是否背離。若以新聞面的 Main Street vs Wall Street 描述來看，兩者都轉空，未見明顯背離。

## 資料缺口與可信度

- 11-19 至 11-28 的 Reddit、StockTwits、X 與 analyst rating 更新：DATA_UNAVAILABLE。
- 金價水準來源不一致（$3,660–3,900 區間），本報告只用方向性描述，不採用單一價位。
- 策略師目標價與配置建議多數為 2025-12 至 2026-05 的舊資料，已在條目中標註日期，應視為背景而非即時共識。

## Metrics table

| 指標 | 數值 | 日期 / 來源 | 備註 |
|---|---|---|---|
| GLD 分析師評等（yf rec_summary） | DATA_UNAVAILABLE | yf 連線失敗 | 無法取得 |
| 第三方 GLD 評等（12 個月） | 2 Buy / 0 Hold / 3 Sell | Stockchase，最近 2026-06-26 | 樣本少 |
| Tickeron 技術訊號 | Aroon 下行，續跌機率 73%；MACD 轉負，續跌機率 68% | 2026-11-10 至 11-12 | 演算法輸出 |
| Goldman Sachs 2026 年底金價目標 | $4,150/oz（由 $4,650 下調） | Kitco，2026-11 | 以較新者為準 |
| 策略師配置建議（黃金占比） | 0%–10%（多數 3%–8%） | State Street、NDR、SocGen、Orion | 日期 2025-12 至 2026-05 |
| 金價區間（近期） | 盤中低點約 $3,660–3,852/oz | 2026-11-16 至 11-18 | 來源數字不一，方向參考 |
| 歷史高點 | $5,405/oz | 2026-01-29 | 背景 |
| 全球黃金 ETF 流入（Sep 2026） | +US$10B | WGC | 全球層級，非 GLD |
| 全球黃金 ETF 流入（Q3 2026） | +US$31B（創紀錄） | WGC | 全球層級 |
| 全球黃金 ETF 流入（Oct 2026） | +US$2.7B；持有 4,275 噸 | WGC | 北美流出 |
| 央行購金（Q2 2026） | 288.9 噸（年增 62%） | 搜尋摘要 | 二手來源 |
| 央行購金（Q3 2026） | 約 321 噸（年增 42%） | WGC 摘要 | 二手來源 |
| Reddit 情緒 | DATA_UNAVAILABLE（11 月） | WSB 最近可得資料為 2026 年初 | 無即時樣本 |
| StockTwits 情緒 | 50（中性）或 72（看多），日期不明 | 搜尋快照 | 低可信度 |
| Insider 淨買賣（6 個月） | 不適用 | ETF | — |
| 機構持倉趨勢 | 不適用（ETF）；個案 Greenlight 減、Third Point 增 | 2026-Q1 | 無趨勢意義 |
| 綜合情緒 | 偏空（信心低至中） | 本報告判斷 | — |
| 背離旗標 | DATA_UNAVAILABLE | — | — |

SENTIMENT REPORT COMPLETE
