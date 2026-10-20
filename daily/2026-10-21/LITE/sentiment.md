# Sentiment — LITE as of 2026-10-21

> 註：`yf.py` 沒有 `ratings` 子命令，改用 `rec_summary` 與 `recommendations`（兩者回傳相同彙總資料）。
> 註：Reddit（WebFetch 無法連線）與 StockTwits（DNS 解析失敗）皆不可用。近期 10 月的市場情緒與分析師動態在公開來源中找不到，多數資料停留在 8 至 9 月。

## Analyst consensus

yf 彙總（期間 0m，即目前）：5 strongBuy / 17 buy / 4 hold / 0 sell / 0 strongSell，共 26 家。

近四期趨勢（買進含 strongBuy）：
- -3m：21（5+16），hold 4
- -2m：22（5+17），hold 4
- -1m：23（5+18），hold 4
- 0m：22（5+17），hold 4

最近一期買進減少 1 家，hold 與 sell 維持不變，整體仍偏多。

網路來源（時間較舊，與 yf 數字不一致）：
- MarketBeat（2026-09-04）：22 家，15 buy / 1 strong buy / 5 hold / 1 sell，平均目標價約 $1,054，當時股價約 $881。
- MarketBeat 同一頁：過去 90 天 3 次降評、1 次升評。
- Benzinga：TD Cowen 於 7 月將目標價下調至 $800，維持 Hold。
- Benzinga：Barclays 升評 Overweight，目標價 $1,000（日期未確認）。
- Barchart（日期未確認）：共識為 Strong Buy，市值約 $72.1B，2026 年初至今漲幅約 157.9%。

逐家評等變動（升降評明細）：yf 工具只回傳彙總，無逐家明細，以上以網路來源為準，標示為部分資料。

## Retail social

- Reddit：DATA_UNAVAILABLE。WebFetch 無法連線 www.reddit.com，r/wallstreetbets 與 r/stocks 皆無法讀取。WebSearch 也找不到 2026 年 10 月的 LITE 相關討論串。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗。
- X / 新聞：未找到 2026 年 10 月的 LITE 情緒專文。唯一的近期資料為 2026-10-06 的成交額報導（約 $4.76B，當日美股排名第 18），顯示交易熱度高。
- 聲量（定性）：無法與歷史基準比較。成交額排名高顯示市場關注度高，但無法區分散戶或機構。
- LunarCrush 有 LITE 社群情緒頁面，但本次無法讀取其當前數值。
- 傾向：DATA_UNAVAILABLE（無法判定多空）。
- 主題：無法從可取得來源歸納。網路上既有的多方論點包括 AI 資料中心與資料通訊需求（TipRanks 列為看多要點），空方論點包括估值偏高（P/E 約 189，MarketBeat 所載）與供給限制（TipRanks 列出）。這些是分析來源的觀點，不是散戶貼文。

## Insider activity

查詢區間：2026-04-21 至 2026-10-21，資料中最早一筆為 2026-05-08。

整體：
- 交易總數 49 筆，其中 28 筆為賣出，21 筆為股票獎勵（Stock Award，無現金價值）。
- 公開市場買進：0 筆。
- 賣出金額合計約 $101.4M。
- 淨額：約 -$101.4M（全為賣出）。

依人員彙整（賣出金額與筆數）：

| 人員 | 職稱 | 賣出金額 | 筆數 |
|---|---|---|---|
| Vincent D. Retort | Officer | 約 $41.0M | 4 |
| Jae Kim | General Counsel | 約 $16.2M | 5 |
| Wupen Yuen | Officer | 約 $14.1M | 10 |
| Brian J. Lillie | Director | 約 $11.8M | 2 |
| Ian Seymour Small | Director | 約 $7.5M | 2 |
| Isaac Hosojiro Harris | Director | 約 $4.9M | 2 |
| Pamela Fletcher | Director | 約 $3.1M | 1 |
| Wajid Ali | CFO | 約 $2.4M | 1 |
| Michael E. Hurlston | CEO | 約 $0.5M | 1 |

值得注意的事項：
- CEO Hurlston 的單筆賣出為 548 股，價格 $958.66（2026-08-27），金額不大。
- Wupen Yuen 在 2026-08-26 至 2026-09-29 間約每週賣出約 1,500 股，價格 $824 至 $988。此模式可能是預定交易計畫，但資料中未驗證。
- 董事（Lillie、Small、Harris、Fletcher）在區間內也有賣出，屬於較廣泛的內部人減持。

## Ownership shifts

- 機構持股：94.1%（1,851 家機構）。內部人持股：0.31%。
- 資料日期：2026-06-30（Q2 13F）。
- 前十大持股（合計約 42.0%）與季度變化：

| 機構 | 持股比例 | 季度變化 |
|---|---|---|
| BlackRock | 10.13% | +17.1% |
| Vanguard Capital | 5.61% | +9.5% |
| Vanguard Portfolio Mgmt | 4.52% | +10.6% |
| JPMorgan | 4.48% | +38.0% |
| FMR | 3.89% | -51.0% |
| State Street | 3.81% | +13.7% |
| Invesco | 3.51% | +170% |
| Geode | 2.48% | +5.5% |
| Jupiter Topco | 2.09% | +100% |
| Arrowstreet | 1.51% | +239% |

- 前十大中 9 家增持，FMR 為主要減持方。
- 集中度趨勢：DATA_UNAVAILABLE（僅一期快照，無法比較多期）。

## Price context

- 內部人交易價格區間：2026-08 至 2026-09 約 $824 至 $988。
- 2026-09-04 股價約 $881（MarketBeat）。
- 2026-10 股價：DATA_UNAVAILABLE。

## Net sentiment score

- 分析師：偏多（高信心）。26 家中 22 家為買進，無賣出評等，但近一個月買進數略減。
- 內部人：偏空（中信心）。區間內無公開市場買進，賣出金額約 $101M 且分布廣。不過高價後的賣出在高估值股票常見，訊號強度低於買進。
- 機構：偏多（中信心）。前十大多數增持，僅 FMR 明顯減持。
- 散戶：DATA_UNAVAILABLE。
- 綜合：中性偏多，信心低至中。分析師與機構偏多，內部人偏空，散戶資料缺失，且 10 月資料不足。

Divergence flag：
- 散戶 vs 分析師：DATA_UNAVAILABLE，無法判定。
- 內部人 vs 分析師：是。分析師以買進為主，內部人則全為賣出，兩者方向相反。

## Data gaps

1. Reddit 與 StockTwits 不可用，散戶情緒無法量化。
2. 2026-10 的分析師動態與股價資料未取得，網路來源最新約為 2026-09。
3. yf 評等彙總（26 家，0 賣出）與 MarketBeat（22 家，含 1 賣出）數字不一致，本報告以 yf 為主、MarketBeat 為輔。
4. 逐家升降評明細僅能從網路來源取得，且日期不完整。

## Sources

- [MarketBeat LITE forecast](https://www.marketbeat.com/stocks/NASDAQ/LITE/forecast/)
- [Barchart LITE analyst estimates](https://www.barchart.com/story/news/1995337/lumentum-holdings-stock-analyst-estimates-ratings)
- [Benzinga LITE price targets](https://www.benzinga.com/quote/LITE/price-targets)
- [10jqka 2026-10-07 成交額報導](https://stock.10jqka.com.cn/usstock/20261007/c680445416.shtml)
- [LunarCrush LITE social sentiment](https://lunarcrush.com/en/stock/lumentum-holdings-inc-common-stock-lite)
- [TipRanks LITE price target](https://www.tipranks.com/stocks/lite/price-target)

SENTIMENT REPORT COMPLETE
