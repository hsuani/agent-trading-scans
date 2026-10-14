# Sentiment — IPGP (IPG Photonics) as of 2026-10-14

資料狀態提醒：Reddit (r/wallstreetbets, r/stocks) 直接抓取被拒 (WebFetch 無法存取)，StockTwits API 無法解析網域 (DNS 失敗)，兩者皆 soft-fail。yf rec_summary 三個期間 (0m / -1m / -2m) 數字完全相同，疑為快取或未更新資料。WebSearch 找到的分析師與空方數據多為 2026 年 8 月前後快照，並非 10 月當日資料。以下結論信心已相應下調。

## Analyst consensus
9 家覆蓋：6 buy (強買 2 + 買 4) / 2 hold / 1 sell (強賣 1)，無一般 sell 評等。Buy 比例約 67%。

近期動向 (WebSearch 摘要，日期為 2026 年 8 月前後)：
- Citigroup 於 2026-08-11 將目標價由 150 下調至 137，維持 Buy。
- Roth 上調目標價 2 美元至 151 (確切日期未確認)。
- 平均目標價約 121–136 美元 (各來源不一：Investing.com 約 126.21，MarketBeat 約 135.50)。
- yf recommendations 工具僅回傳彙總計數，未提供個別券商升降評等明細，無法判定 10 月內是否有新的 upgrade / downgrade。

## Retail social
- Reddit: 無法取得。WebFetch 對 r/wallstreetbets 與 r/stocks 的搜尋端點皆被拒，WebSearch 亦未找到相關串文。無法估計討論量與多空傾向。
- StockTwits / X: StockTwits API 無法存取。WebSearch 摘要提到一個 StockTwits 頁面的情緒標記為 "Bearish"，情緒分數 34，但該頁面日期不明，且另一快照價位不同，可信度低。未取得 X 相關貼文。
- 聲量 (buzz volume)：無可靠數據，無法與常態比較。
- 多空傾向：無法直接判定。唯一可用的散戶代理指標 (StockTwits 快照) 偏空，信心低。
- 主要主題 (由新聞與選擇權數據推論，非社群原文)：
  - 空方部位偏重：Benzinga 頁面引用的做空比率約 22% float、put/call 比率 2.33 至 3.27 (兩版本數字不同)。
  - 估值與成長持續性的分歧：部分評論認為分析師目標價遠高於交易價位，成長能否延續仍有爭議。
  - 內部人大額賣出的解讀：多數賣方為 10% 大股東實體，市場關注其是否為被動分散。
- 引述樣本：無可引用的社群原文。

## Insider activity
統計區間：2026-04-14 至 2026-10-14 (6 個月)。

Net 6mo: 買入約 $0.20M，賣出約 $23.38M，淨賣出約 $23.18M。

- 賣方結構：
  - 10% 大股東實體 (IP Fibre Devices Ltd 約 $13.34M；Valentin Gapontsev Trust I 約 $7.83M)，合計約 $21.17M，佔賣出總額約 90%。
  - 董事與高層合計約 $2.21M：Mammen (CFO) 約 $1.20M (2026-05-22，約 119.60–120.37 美元)；Scherbakov (董事，同時為 10% 持有人) 約 $0.55M；Tang (董事) 約 $0.18M；Desmond (董事) 約 $0.18M；LoPresti (General Counsel) 約 $0.11M；Ness、Meurice、Buttarazzi 等零星賣出未計入以上 6 個月總額 (日期多在區間外或金額小)。
- 買方：
  - Peeler John R (董事) 2026-08-26 買入 2,710 股，約 $0.20M (約 72.84–74.57 美元)，為區間內唯一公開市場買入。
  - Notable：CEO Gitin 於區間內無公開市場交易，僅 2026-02 的股票授予 (Stock Award)。
- 說明：大股東實體賣出的規模與頻率 (近 6 個月多次出售)，對市場解讀影響最大；高層的小額賣出多為既有選擇權行使後的部分變現，屬常見模式，但 CFO 單筆約 $1.2M 值得留意。

## Ownership shifts
- 內部人持股比例：38.98% (yf major_holders)。
- 機構持股比例：75.13%，機構數 491 家。
- 資料異常：institutionsFloatPercentHeld 值為 1.23 (超過 100%)，應為資料源錯誤，不採信。
- 機構持股趨勢：工具僅提供單一時點快照，無法判定增減趨勢，需以 13F 季度資料補充。

## Net sentiment score
Composite: 中性偏空 (信心：低)

依據：
- 分析師層面偏多 (6/9 buy，目標價平均高於近期交易價)。
- 內部人層面偏空：6 個月淨賣出約 $23M，但約 90% 來自大股東實體，高層與董事淨賣出約 $2.2M，另有董事 Peeler 小額買入，訊號較為混雜。
- 選擇權與空方層面偏空：put/call 比率偏高、做空比率約 22%。
- 散戶層面：無可靠數據，唯一代理指標偏空，但時效與來源不足。

信心偏低的主因：Reddit 與 StockTwits 皆無法取得，分析師與空方數據多為 8 月前後快照，且 yf 評等數據疑似未更新。

Divergence flag: 是 (有限度)。分析師傾向偏多，而選擇權、空方與內部人大額賣出 (即使多為大股東) 指向偏空，兩者方向相反。因散戶端資料缺失，此分歧無法確認是否為「散戶偏空 vs 分析師偏多」的典型背離，應視為待補充驗證的訊號。

## 核心指標表

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 覆蓋分析師數 | 9 | yf rec_summary |
| Buy 評等數 (強買 + 買) | 6 (2 + 4) | yf rec_summary |
| Hold 評等數 | 2 | yf rec_summary |
| Sell 評等數 (強賣 + 賣) | 1 (1 + 0) | yf rec_summary |
| Buy 比例 | 約 67% | 6 / 9 |
| 平均目標價 | 約 121–136 美元 | WebSearch，各來源不一，日期約 2026-08 |
| 近期目標價變動 | Citi 150 → 137 (2026-08-11)；Roth 上調 2 美元至 151 | WebSearch，未直接驗證 |
| 6 個月內部人買入 | 約 $0.20M | yf insider (Peeler) |
| 6 個月內部人賣出 | 約 $23.38M | yf insider |
| 6 個月淨賣出 | 約 $23.18M | 計算值 |
| 大股東實體賣出 | 約 $21.17M (約 90% of 賣出) | yf insider |
| 董事與高層賣出 | 約 $2.21M | yf insider |
| 內部人持股比例 | 38.98% | yf major_holders |
| 機構持股比例 | 75.13% | yf major_holders |
| 機構數 | 491 | yf major_holders |
| 做空比率 (float) | 約 22% | WebSearch (Benzinga)，日期約 2026-08，兩版本 22.2%–22.3% |
| Put/call 比率 | 2.33–3.27 | WebSearch (Benzinga)，版本不一 |
| Reddit 討論量 | 無法取得 | 抓取被拒 |
| StockTwits 情緒 | 無法取得 (API 失敗)；代理快照偏空 (分數 34)，日期不明 | WebSearch |
| 綜合情緒 | 中性偏空 | 信心低 |
| 背離旗標 | 是 (有限度) | 分析師偏多 vs 選擇權與內部人偏空 |

SENTIMENT REPORT COMPLETE
