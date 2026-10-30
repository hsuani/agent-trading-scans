# Sentiment — GLD as of 2026-10-31

## Executive summary

GLD 是 SPDR Gold Shares 的實物黃金信託 ETF，不是公司，因此內部人交易與機構持股分析不適用。本次可取得的資料有三類：(1) 銀行與市場對金價的目標價變動（2026 年 6 月至 7 月），(2) 零散的散戶情緒指標（多為 2026 年 2 至 3 月的快照，或來源可信度偏低的自動生成頁面），(3) 基金資金流的季報與彙總數字（最新為 2026 年 Q2，10 月份資金流數據未取得）。

整體判斷：銀行目標價在年中被普遍下修，但仍維持正向長線觀點；散戶情緒在 2 月高點後降溫，情緒指標顯示的偏多結論缺乏 10 月當月的可驗證數據；資金流在 Q2 出現淨贖回。綜合為「中性偏多、信心低」。詳見文末結論。

## Data availability

| 項目 | 狀態 | 說明 |
|---|---|---|
| yf `recommendations` / `rec_summary` | DATA_UNAVAILABLE | 工具回傳空陣列，Yahoo cookie/crumb 連線失敗 |
| yf `insider` | DATA_UNAVAILABLE | 同上，且 ETF 不適用 |
| yf `major_holders` / `inst_holders` | 不適用 | ETF 不做此分析，依任務規定略過 |
| yf `ratings` | 工具不支援 | 本 CLI 無此 kind，改以 WebSearch 補充 |
| Reddit（WSB / stocks） | 未直接抓取 | 依任務規定，由 WebSearch 間接取得 |
| StockTwits | 未直接抓取 | 同上，未取得可引用的即時數據 |

## Retail / social sentiment read

- 數據來源與限制：直接的 r/wallstreetbets 提及次數與 StockTwits 貼文流本次都無法取得。以下是透過 WebSearch 找到的間接證據。
- 2 月高點後降溫：一篇 AOL 文章引用某情緒指數，指出 Reddit 情緒分數於 2 月 23 日達到 78，當時 r/stocks 討論黃金八個月連漲；到 3 月 3 日回落至 60.93（仍屬偏多區間）。文章提到散戶討論重心從「買 GLD」轉向「如何買實體金幣」，顯示部分散戶偏好實物而非 ETF。
- AltIndex 情緒評分：AltIndex 對 GLD 給出 78/100（偏多）的 NLP 評分，但頁面未標示讀數日期，且其資料來源包含 Reddit、StockTwits 等論壇，無法拆分個別平台的 tilt，因此只能作為弱參考。
- 來源可信度警示：historicaloptiondata.com 類頁面宣稱的 55–80% 看多比例，來自少數 X 貼文，且引用的 GLD 價格前後不一致，本報告不採用其百分比作為散戶情緒的量化依據。
- 主要主題（依搜尋結果歸納）：
  - 避險需求：黃金作為股市波動時的避險資產，其角色在權益市場震盪時被重新提及。
  - 利率敏感度：有來源提到聯準會對升息的訊號對金價形成壓力（10 月的一篇頁面，但該頁數字未獲其他來源證實）。
  - 實物 vs ETF：散戶討論轉向實體金幣與金礦股，而非 GLD 本身。
- 聲量相對基準：無法量化與歷史平均的比較；定性判斷為 2 月前後討論熱度高、近期不明顯。

## Analyst consensus（市場與銀行觀點）

ETF 本身沒有評級分布，因此以大型銀行對金價的目標價作為代理指標。來源為 2026 年 7 月的彙整報導，為本次能取得的最新資料：

| 機構 | 目標（USD/oz） | 時點 | 變動 |
|---|---|---|---|
| Goldman Sachs | 4,900 | 2026 年底 | 6 月自 5,400 下修，7 月維持 |
| UBS | 約 5,200（12 個月）| 近一年 | 5 月自 5,500 下修；較 1 月的 6,200 更低 |
| Morgan Stanley | 約 5,200（H2 2026 bull case）| 2026 下半年 | 持有評等，上行情境需 ETF 流入配合 |
| Bank of America | 4,800 | 近期 | 下修；7 月彙整中的數字 |
| JPMorgan | 6,000 | 2026 年 Q4 | 7 月彙整中的數字；另一表格顯示 Q3 均價 4,300、Q4 均價 4,500，兩者指標不同 |
| Deutsche Bank / Wells Fargo | 約 6,000 / 6,100–6,300 | 2026 年初 | 舊資料，已可能過時 |

觀察：
- 多數銀行在 2026 年年中下修金價目標，但仍普遍高於 4,500 的區間，顯示長線偏多。
- 來源之間的數字存在指標差異（年底目標 vs 年均價 vs 季均價），無法將其直接平均。
- 缺少 10 月的銀行更新，本報告無法確認是否有進一步調整。
- 網路上另有一篇 10 月頁面稱「無分析師目標價」，但該頁同時引用的 GLD 價格與其他來源不符，可信度低，未採納。

## Institutional / fund flow signal

- 2026 年 Q2 季報（10-Q，截至 6 月 30 日）：贖回 32.9M 股，申購 18.5M 股，淨減約 14.4M 股（申購對應約 170 萬盎司黃金入庫，贖回對應的黃金數量未在搜尋結果中取得）。方向為淨流出。
- 資產規模：TradingView 頁面列 AUM 約 141.36B USD（日期標示 10 月 16 日），另一頁面列 172.71B USD（未標日期）。兩者差距大，本報告不採用單一數字，僅記錄為「介於 1,400 億至 1,700 億美元區間，無法確認」。
- 一年期淨流入：TradingView 頁面列約 3.55B USD，時點與計算基準未明。
- 其他參考：3 月 9 日 etfcentral 快照顯示一個月淨流出約 1.33B USD，年初至當日淨流入約 0.83B USD；一篇 5 月文章引用 State Street 數據，指實體金 ETF（含 GLD）在截至 2026 年 4 月的 12 個月內淨流入約 30B USD（次要來源）。
- 10 月份的單月資金流：DATA_UNAVAILABLE。搜尋結果中僅有 9 月初的定性描述（資金流入，逢低買盤），未有可核對的數字。

## Overall sentiment verdict

| 面向 | 判讀 | 信心 |
|---|---|---|
| 銀行 / 分析師觀點 | 偏多（長線），年中下修 | 中 |
| 散戶情緒 | 2 月高點後降溫，近期無可靠量化數據 | 低 |
| 資金流 | Q2 淨流出；10 月數據缺失 | 低至中 |
| 綜合 | 中性偏多 | 低 |

- 綜合看法：銀行長線觀點仍維持正向，但目標價在 2026 年年中普遍下修，資金流在 Q2 轉為淨贖回，散戶熱度自 2 月後降溫。目前缺乏可核對的 10 月數據，因此信心偏低。
- 分歧提示：目前無法確認散戶與分析師之間是否存在方向分歧。若 10 月的散戶情緒偏多而銀行維持下修，才會構成分歧訊號，但本次資料不足以判定。
- 資料可信度注意：本次多數來源為自動生成或二手彙整頁面，GLD 價格、AUM 與目標價數字在不同來源間有明顯出入。在引用任何單一數字前，應先與 SPDR 官網或市場資料供應商核對。
- 本報告僅呈現情緒與共識狀態，不構成交易建議。

## Sources (WebSearch, accessed for 2026-10-31 analysis)

- [Goldman / UBS / BofA / JPM 彙整（investinglive，2026-07-06）](https://images.investinglive.com/commodities/wall-street-splits-on-gold-as-forecasts-range-from-4800-to-6000-20260706/)
- [BofA 與 JPM 目標調整（BNN Bloomberg，2026-07-08）](https://www.bnnbloomberg.ca/markets/gold/2026/07/08/bofa-cuts-2026-average-gold-forecast-sees-long-term-upside/)
- [Reddit 情緒降溫（AOL）](https://www.aol.com/articles/gold-17-reddit-just-shifted-184111680.html)
- [GLD Q2 2026 10-Q（SEC）](https://www.sec.gov/Archives/edgar/data/0001222333/000143774926025680/gld20260630_10q.htm)
- [GLD 基金資料（TradingView）](https://www.tradingview.com/symbols/AMEX-GLD/profile/)
- [GLD 基金資料（etfcentral）](https://www.etfcentral.com/fund/GLD)

SENTIMENT REPORT COMPLETE
