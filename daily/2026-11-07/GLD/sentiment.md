# Sentiment — GLD (SPDR Gold Shares) as of 2026-11-07

## Executive summary

GLD 是 ETF，沒有分析師評級，yf 工具對 `recommendations` 與 `rec_summary` 皆回傳空值。因此「分析師共識」改以銀行與調查機構的金價目標代替。可取得的資料大多停在 2026 年 3 月至 7 月，沒有 2026-11-07 當日的價格、情緒或資金流數據。

- 零售情緒：2026 年初偏多（Stocktwits 形容為 "extremely bullish"），2 月底後 Reddit 熱度轉向「如何買實體金」。10 月至 11 月的情緒數據找不到。
- 銀行與調查金價目標：2026 年平均價約落在 $4,450–$4,750/oz，2027 年 Deutsche Bank 預估約 $5,150/oz。目標價偏多，但寫作時間多在 2025 年底至 2026 年初。
- 資金流：最新一筆可用資料（10 月下旬）顯示 GLD 年初至今淨流出約 -$2.8B 至 -$2.9B，兩個來源數字不一致。另一追蹤器於 10 月 5 日的數字卻顯示美國金 ETF 年初至今淨流入 +$5.0B，方向相反。
- 綜合：零售情緒（舊資料）偏多，資金流（較新資料）偏空，方向分歧。整體信心低。

## Data availability

| 項目 | 狀態 | 最新可用日期 | 備註 |
|---|---|---|---|
| 分析師評級（yf rec_summary / recommendations） | 無資料（空陣列） | — | GLD 為 ETF，無個股式評級 |
| 銀行 / 調查金價目標 | 部分可得 | 2025 年 11 月至 2026 年 中 | 來源品質參差，部分為自動生成頁面 |
| Reddit / Stocktwits 情緒 | 部分可得 | 2026 年 3 月前後 | 2026-11 無資料；Reddit 與 Stocktwits 直接抓取未執行（依任務要求以 WebSearch 為主） |
| 資金流（creations / redemptions, AUM） | 部分可得、來源衝突 | 2026 年 10 月下旬 | 無 GLD 官方 AUM 或 2026-11 數據 |
| GLD 價格 | 部分可得 | 2026 年 7 月 29 日 $371.08（Market Chameleon 頁面） | 2026-11-07 收盤價未取得 |
| 金現貨價 | 部分可得 | 2026 年 5 月 28 日約 $4,457/oz（低品質來源）；2 月 27 日 $5,221.30/oz | 2026-11-06 至 11-07 無可靠報價 |
| 內部 daily/2026-11-07/GLD 資料 | 未借用 | — | 依指示不借用舊日期報告數字 |

資料限制：所有數據都超過 2026-11-07 之前的有效窗口或來源日期不明，全部視為過去數據。GLD 價格與金價之間的換算無法對齊：$371（7 月）與 52 週高點 $509.70 的比例，對應的金價推算與 5 月 $4,457 的報價不一致。因此本報告不以價格比率作結論。

## Retail / social sentiment read

- 量級：無法取得 2026-11 的提及次數。2026 年初 Stocktwits 上 GLD 訊息量被描述為 "extremely high"，屬於高於平常的水準。
- 語調（2026 年初）：Stocktwits 上 GLD 情緒在 1–2 月被標示為 "extremely bullish"，即使金價從高點回落，仍有人把跌勢視為買點，例如「buying opportunity」這類說法。
- 語調（2026 年 3 月）：Reddit 情緒於 2 月 23 日達到高點（約 78 分），之後轉向「如何買實體金」，即從買 GLD 轉向買金幣或實體金。來源為 247wallst 報導，並引用 AltIndex 式的 NLP 分數（60.93，標示 bullish）。
- 領先指標觀察：ICE 分析指出，1 月下旬 Reddit 上金與銀 ETF 的情緒急速惡化，且 Reddit 討論可能早於重大價格下跌。這是單一來源觀察，未經獨立驗證。
- 金礦股情緒：3 月 Stocktwits 報導指出，Newmont、Barrick 的情緒降溫至中性，原因是金價獲利了結。
- 主題（可見的重複主題）：(1) 逢低買進的敘事（"buying opportunity"）；(2) 從 GLD 轉向實體金與金幣的敘事；(3) 獲利了結與金價高檔回檔的擔憂。
- 不確定性：AltIndex 的 GLD 情緒分數 78/100（Bullish）沒有標示日期，無法確定是否為 2026-11 的數值，故不採用。

## Analyst consensus（市場與銀行觀點）

GLD 無分析師評級，以下為金價目標代理指標：

| 機構 / 來源 | 目標 / 預估 | 發布時間 | 備註 |
|---|---|---|---|
| Deutsche Bank | 2026 年均價約 $4,450/oz；2027 年均價約 $5,150/oz（前次預估 $4,000） | 2025 年 11 月底 | 另有媒體標題寫「接近 $5,000」，與本段數字略有出入，以原報告為準 |
| LBMA 2026 Precious Metals Forecast Survey | 2026 年平均 $4,741.97/oz | 2026 年初 | 描述為比銀的預估保守 |
| Reuters 分析師民調（30 位） | 2026 年中位數 $4,746.50/oz | 2026 年初 | 為該調查自 2012 年以來最高的年度預估 |
| 綜合摘要 | 多數主要機構預估區間 $4,000–$5,300/oz | 2026 年中 | 來源為二手彙整 |

解讀：銀行與調查的 2026 年目標集中在 $4,450–$4,750，2027 年目標約 $5,150。上述目標多為 2025 年底至 2026 年初發布。近期（2026 年中後）是否有目標上修或下修，本次搜尋未找到。

## Institutional / fund flow signal

- 2026 年 7 月 WGC 相關報導：全球金 ETF 6 月淨流出約 $8.9B，北美占比最大，上半年總量被描述為 2013 年以來最弱（另一篇同期報導標題寫上半年流量「仍為正」，兩者衝突，須以原報告為準）。6 月的流出多來自中國基金。
- 2026 年 10 月下旬（追蹤器 A，約 10 月 26 日）：GLD 過去一個月淨流出約 -$1.72B，年初至今約 -$2.94B。
- 2026 年 10 月下旬（追蹤器 B，約 10 月 27 日）：年初至今約 -$2.82B。
- 2026 年 10 月 5 日（追蹤器 C，thetrading.tools）：美國金 ETF 年初至今淨流入約 +$5.0B。這與追蹤器 A、B 的方向相反，三者計算口徑不同，不宜直接合併。
- 未取得：GLD 官方 AUM 趨勢、2026-11 的 creations / redemptions 數據，以及 SPDR 官網的每日持股量。
- 結論：可用的最新資料（10 月下旬）偏向淨流出；10 月初的一筆數據偏向淨流入。資金流方向在 2026 年 10 月前後存在不確定性。

## Overall sentiment verdict

| 面向 | 判讀 | 信心 |
|---|---|---|
| 分析師（金價目標代理） | 偏多（中長期目標約 $4,450–$5,150） | 中（資料為 2025 年底至 2026 年中，已過時） |
| 零售情緒 | 2026 年初偏多，3 月後轉為「實體金」與逢低買的混合敘事；2026-11 無資料 | 低 |
| 資金流 | 最新資料（10 月下旬）偏空，年初至今淨流出約 -$2.8B 至 -$2.9B；但另一份 10 月初資料為淨流入 | 低 |
| 綜合 | 中性（分歧） | 低 |

- 綜合看法：以目標價看偏多，以資金流看偏空，以零售舊資料看偏多，方向分歧。
- 分歧旗標：是。零售（舊資料）偏多與近期資金流偏空方向相反，但兩者的資料時間差異很大，不能當作同一時點的訊號。
- 本報告僅呈現情緒與共識狀態，不構成交易建議。

## Sources

- [Stocktwits: Gold down from record high, retail calls it a buying opportunity](https://stocktwits.com/news-articles/markets/equity/gold-down-after-record-highs-retail-investors-are-calling-it-a-buying-opportunity/cmyi1nGR412)
- [Stocktwits: Newmont, Barrick, do miners still shine for retail investors?](https://stocktwits.com/news-articles/markets/equity/newmont-barrick-gold-miners-retail-turns-neutral/c7rfklCRbk)
- [247wallst: Gold is up 17% this year but Reddit just shifted from buying GLD to googling coins (2026-03-04)](https://247wallst.com/investing/2026/03/04/gold-is-up-17-this-year-but-reddit-just-shifted-from-buying-gld-to-googling-coins/)
- [AltIndex GLD sentiment page (undated score, not used)](https://altindex.com/ticker/gld/sentiment)
- [ICE: Reddit new signals and sentiment insights](https://www.ice.com/insights/reddit-new-signals-and-sentiment-insights)
- [Market Chameleon GLD overview (price $371.08, 2026-07-29)](https://marketchameleon.com/Overview/GLD/SingleLegOptionTradesNew/)
- [The Trading Tools: Gold ETF flows (Oct 5, 2026 tracker, YTD +$5.0B)](https://www.thetrading.tools/gold-etf-flows)
- [Engineering News: First-half gold ETF flows remained positive, WGC (2026-07-08)](https://www.engineeringnews.co.za/article/first-half-gold-etf-flows-remained-positive-world-gold-council-2026-07-08)
- [Deutsche Bank gold forecast via OnInvest](https://en.oninvest.com/article/gold-may-rise-by-another-20-deutsche-bank-expects-a-rise-to-almost-5000-per-ounce)
- [LBMA 2026 Precious Metals Forecast Survey](https://www.lbma.org.uk/forecast-survey-2026/at-a-glance)

本報告未使用 WebFetch 存取任何財經網站。yf 的 Yahoo 端點於執行期間被代理拒絕連線，因此 GLD 的 yf 資料空值可能來自連線失敗，而非確認 GLD 無評級。

SENTIMENT REPORT COMPLETE
