# Sentiment — ASML as of 2026-11-16

> 資料時效注意: 今日實際日期為 2026-11-15, 報告以 2026-11-16 為標示日期。yf 工具回傳的分析師數據為當前快照 (無明確日期戳記); 新聞來源最新僅到 11/9 收盤價附近。Reddit 與 StockTwits 無法存取, 散戶情緒部分資料不足。

## Analyst consensus

41 位分析師: **7 strongBuy / 31 buy / 2 hold / 1 sell / 0 strongSell**。買進及以上占比約 93% (38/41)。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 當前 (0m) | 7 | 31 | 2 | 1 | 0 |
| -1m | 7 | 31 | 2 | 1 | 0 |
| -2m | 7 | 31 | 3 | 1 | 0 |
| -3m | 6 | 32 | 4 | 1 | 0 |

- 近三個月趨勢: hold 由 4 降至 2, 方向偏正面; 但 -3m 時 hold 為 4, 近期有小幅回收, 整體評級分布穩定。
- 近期升降評等事件: yf `recommendations` 回傳為月度彙總, 未列出個別升降評等事件, 無法確認具體 upgrade / downgrade 名單。
- 目標價變動: yf 工具未提供目標價欄位。次級新聞 (MarketBeat, 未直接驗證) 提到 JPMorgan 維持 Overweight 並將目標價調降至 $2,350, 但此為單一來源, 僅供參考。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 無法存取 (WebFetch 遭擋, 來源不可達)。本次無樣本, 無法判定散戶傾向。
- **StockTwits**: 無法解析 api.stocktwits.com (網路白名單未開放)。需於 session 網路設定中允許該網域後才能重試。
- **X / 新聞與評論 (WebSearch 替代)**: 近期評論偏向中性, 正負並陳:
  - 正面: Q3 營收約 €11.7B、年增約 55%, 毛利率約 57.5%; 管理層表示供給至少到 2028 年前接近售罄 (次級來源 MarketBeat, 2026-10-17)。Zacks 指出 2026 / 2027 EPS 預估過去一年分別上修約 45% / 51%。
  - 負面: 估值偏高是主要批評 (MarketBeat, 2026-10-28 引述分析師觀點: 業務出色但估值昂貴)。中國風險: 有報導指中國國有背景廠商開始量產浸潤式 DUV 設備, 引發對中國銷售流失的擔憂; BofA 認為此次拋售為過度反應 (MarketBeat, 2026-07-30)。
  - 總體: 宏觀通膨與利率預期升高, 資金撤出高估值科技股 (MarketBeat, 2026-10-17)。
- 價格參考: 次級來源 Stockchase 列出 2026-11-09 收盤約 $1,501.74, 較 10 月初提及的約 $1,800 水位有明顯回檔 (未經行情工具交叉驗證)。

### 主要主題 (Themes)
1. 需求能見度高 (AI / DRAM 擴產), 訂單與營收動能受肯定。
2. 估值擔憂: 股價回檔後仍被視為高估值 (視角分歧)。
3. 中國出口管制與本土替代風險。
4. 宏觀利率與通膨對高估值半導體的壓力。

### 聲量 (Buzz volume)
無法量化 (社群來源不可用)。新聞層面報導頻率在 10 月至 11 月間屬正常水準, 無明顯異常放量跡象 (定性判斷, 信心低)。

## Insider activity

Net 6mo: 資料不足。yf `insider` 回傳空陣列, 無任何交易紀錄可計算。
- 注意: ASML 為荷蘭上市公司 (NYSE/Nasdaq 同步掛牌, 屬 foreign private issuer 性質), 內部人申報制度與美股 Form 4 不同, 空結果不代表「無內部人交易」, 僅表示工具無法取得資料。
- Notable: 無。

## Ownership shifts

- 機構持股比例 (yf `major_holders`): institutionsPercentHeld 約 19.9%, insidersPercentHeld 約 0.06%, 機構家數約 2,996。
- 機構持股大戶 (yf `inst_holders`, 最新申報日 2026-09-30 為主):

| 機構 | 持股比例 | 持股數 (M 股) | 市值 (USD B) | 季度變動 |
|---|---|---|---|---|
| FMR, LLC | 1.54% | 5.98 | 8.95 | +9.2% |
| Fisher Asset Management | 1.25% | 4.84 | 7.24 | +2.1% |
| Capital World Investors | 0.88% | 3.43 | 5.12 | -8.1% |
| Invesco Ltd. | 0.72% | 2.79 | 4.17 | -11.1% |
| State Farm Mutual | 0.71% | 2.74 | 4.10 | -0.5% |
| Van Eck Associates (6/30) | 0.63% | 2.46 | 3.68 | +31.7% |
| Capital International | 0.61% | 2.38 | 3.55 | -2.5% |
| JPMorgan Chase | 0.54% | 2.10 | 3.15 | -12.2% |
| T. Rowe Price (6/30) | 0.50% | 1.93 | 2.89 | +25.7% |
| Morgan Stanley (6/30) | 0.46% | 1.79 | 2.67 | +0.2% |

- 趨勢: 前十大持股中, 增持者 (FMR、Fisher、Van Eck、T. Rowe) 與減持者 (Capital World、Invesco、JPMorgan) 大致各半, 集中度變化不明顯。Van Eck 與 T. Rowe 為 6/30 申報, 資料較舊。
- 單位換算: 市值以 USD B 表示 (原始數值 8,947,308,268 USD ≈ 8.95B)。

## Net sentiment score

- **Composite: 偏多 (bullish), 信心中等偏低。**
  - 分析師面: 偏多, 信心高 (93% 買進及以上, 評級分布穩定)。
  - 散戶面: 無法判定 (Reddit / StockTwits 不可用; 新聞評論中性偏多但估值與中國風險為明顯保留意見)。
  - 內部人面: 無資料, 不計入。
  - 機構面: 持股比例穩定, 增減持互見, 中性。
- **Divergence flag: 無法判定 (no-data)。** 因缺乏散戶樣本, 無法確認散戶與分析師傾向是否相反。新聞評論的保留意見 (估值、中國) 與分析師整體偏多並非明顯對立, 故暫不標記背離。

## Data gaps / follow-up

1. Reddit 與 StockTwits 需於網路設定開放後重試。
2. yf `insider` 空結果需另以 SEC / AFM 或其他來源交叉確認。
3. 目標價與個別升降評等事件 yf 未提供, 需另尋來源。
4. 缺少 2026-11-16 當日資料, 報告為 11/9 前後可取得資訊的延伸。

SENTIMENT REPORT COMPLETE
