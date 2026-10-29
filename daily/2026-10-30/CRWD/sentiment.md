# Sentiment — CRWD as of 2026-10-30 (資料截至 2026-10-26; 執行日 2026-10-29)

## 資料可得性與限制
- **日期**: 本次執行日為 2026-10-29，指定 DATE 為 2026-10-30。最新可得資料為 2026-10-26，2026-10-30 當日資料不在範圍內。
- **Reddit (r/wallstreetbets, r/stocks)**: WebFetch 回報無法連線 (Claude Code is unable to fetch from www.reddit.com)，已 soft-fail。
- **StockTwits**: `api.stocktwits.com` DNS 解析失敗 (getaddrinfo ENOTFOUND)，需於 session 網路設定允許此網域後才能重試。本次未重試。
- **X / 新聞**: 以 WebSearch 取代，結果多為 TIKR、Trefis、Bullstory 等聚合站，權威性有限。

## Analyst consensus
yf `rec_summary` (0m)：Strong Buy 10 / Buy 30 / Hold 12 / Sell 0 / Strong Sell 1，合計 53 家。買方 40 家 (約 75%)、持有 12 家 (約 23%)、賣方 1 家 (約 2%)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m (當期) | 10 | 30 | 12 | 0 | 1 |
| -1m | 10 | 30 | 12 | 0 | 1 |
| -2m | 10 | 30 | 12 | 0 | 1 |
| -3m | 10 | 31 | 11 | 0 | 1 |

近三個月評等結構幾乎不變，僅 Buy 減 1、Hold 增 1。

**近期目標價變動** (來源為網路搜尋彙整，未逐一核對原始研報):

| 日期 | 機構 | 動作 | 來源性質 |
|---|---|---|---|
| 2026-10-15 | Citigroup | 目標價 $260 → $295 | TIKR 彙整 |
| 2026-10-16 | KeyBanc | 目標價 $245 → $265，引用 33 家渠道商訪談 | TIKR 彙整 |
| 未標日期 | BTIG | 目標價上調至 $312 (前值 $245) | TIKR 彙整 |
| 未標日期 | Bank of America | 目標價 $535，維持 Neutral | MarketBeat 條目 |
| 2026-05-20 | Morgan Stanley | 目標價 $510 → $610，維持 Overweight | 標題來源，與 7 月另一來源的 $227 衝突 |
| 未標日期 | Piper Sandler / RBC / Stifel | 分別為 $375、$365、$435 | 無日期，無法定位時間 |

Bullstory (2026-10-02) 顯示 50 家分析師、平均目標價 $235.67、區間 $132–$300、共識 Buy。Walnut (資料截至 2026-08) 顯示 41 買 / 11 持有 / 1 賣。與 yf 合計 53 家的結構大致一致。

## Retail social
- **Reddit**: 無法取得樣本，無法判斷討論量與傾向。
- **StockTwits / X**: StockTwits 無法連線。網路搜尋未找到 2026-10 的 X 或 Reddit 具體貼文，無法引用代表性言論。
- **聲量**: 無法量化，不做「高於或低於常態」的判斷。
- **傾向**: 無法判定。新聞端語氣呈現混合。
- **新聞主題 (可作為 retail 討論的替代參考)**:
  - 估值: TIKR (10-14) 指平均目標價 $241 低於當時股價約 8%；另一篇指股價漲幅已超過一倍，但華爾街營收預估上修有限。
  - 催化劑: Trefis (10-26) 指 10-23 股價上漲 8.2%，主因為 Evercore ISI 渠道調查顯示網安預算偏向樂觀。
  - 區間: Trefis 指 2026-02-24 低收 $87.56、2026-10-06 高收 $278.86；12 個月報酬約 106%。
  - 下一個財報: Trefis 指 2026 年 12 月公布 FY2027 Q3 財報。

## Insider activity
**6 個月 (2026-04-30 至 2026-10-26)**: 買入 0 筆 (公開市場)；賣出 115 筆，約 **$483M**。扣除獎勵股與贈與，僅計 Sale。

| 內部人 | 職位 | 6 個月賣出金額 (USD M) |
|---|---|---|
| George Robert Kurtz | CEO | ~289 |
| Sameer K. Gandhi | Director | ~58 |
| Michael Sentonas | President | ~49 |
| Gerhard Watzinger | Director | ~36 |
| Burt W. Podbere | CFO | ~16 |
| Roxanne Schuh Austin | Director | ~12 |
| Anurag Saha | Officer | ~10 |

- **Notable**: CEO Kurtz 近 6 個月幾乎每 2 至 3 個交易日賣出約 20,000 股，最近一筆為 2026-10-26，約 $5.1M。此規律性可能為預定交易計畫 (10b5-1)，但本次資料未能驗證。
- **資料品質警示**: 2026-06/07 部分列的成交價出現 $3,090.96、$189–$776 等數值，與同期其他列及 Trefis 價位不一致。因此 USD 總額可能有誤，**金額僅供量級參考**；「賣出筆數遠多於買入、無公開市場買入」的方向性結論較為可靠。
- **持股結構 (yf major_holders)**: 內部人持股 1.35%；機構持股 77.9% (float 基準 78.9%)；機構數 3,309 家。僅有單期快照，無法判定趨勢。

## Net sentiment score
- **分析師**: 偏多 (中度)。約 75% 買方評等，近期目標價多為上調。
- **內部人**: 賣出流量大、無公開市場買入，流量面偏空，但規律性賣出可能為計畫性，資訊量偏低。
- **散戶**: 無法判定。
- **綜合**: **中性** (信心低)。分析師偏多與內部人淨賣出並存，散戶端缺資料，無法完整評估。

**背離旗標**: **無法判定** (缺散戶資料，無法比較散戶與分析師傾向)。但分析師偏多與內部人大量賣出之間存在方向差異，值得在後續研究中留意。

本報告僅為情緒面資料彙整，不含交易建議。

## 來源
- [Trefis: What Is Behind The Move In CrowdStrike Stock? (2026-10-26)](https://www.trefis.com/stock/crwd/articles/620538/what-is-behind-the-move-in-crowdstrike-stock/2026-10-26)
- [TIKR: CrowdStrike has more than doubled in 2026 but Wall Street has barely raised its revenue estimates](https://www.tikr.com/zh/blog/crowdstrike-has-more-than-doubled-in-2026-but-wall-street-has-barely-raised-its-revenue-estimates-heres-what-could-move-them)
- [TIKR: CrowdStrike stock fell 7% on Friday](https://www.tikr.com/blog/crowdstrike-stock-fell-7-on-friday-heres-what-could-drive-shares-through-2026)
- [Bullstory: CRWD analyst price target range](https://bullstory.io/en/stocks/crwd/forecast/price-target)
- [Walnut: CRWD Stock Forecast and Price Target (2026)](https://walnutinvest.com/stocks/crwd/forecast)
- [MarketBeat: BMO / Morgan Stanley / BofA 相關條目](https://www.marketbeat.com/instant-alerts/bmo-capital-markets-forecasts-strong-price-appreciation-for-crowdstrike-nasdaqcrwd-stock-2025-09-18)
- [Placera: Morgan Stanley boosts price target to $610 (2026-05-20)](https://www.placera.se/telegram/morgan-stanley-boosts-price-target-on-crowdstrike-holdings-to-610-from-510-keeps-overweight-rating-20260520)
- [TipRanks/The Fly: CrowdStrike price target raised to $375 at Piper Sandler](https://www.tipranks.com/news/the-fly/crowdstrike-price-target-raised-to-375-from-290-at-piper-sandler)

SENTIMENT REPORT COMPLETE
