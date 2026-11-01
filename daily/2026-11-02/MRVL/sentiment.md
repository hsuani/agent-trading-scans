# Sentiment — MRVL as of 2026-11-02

資料截止原則: 只使用 2026-11-02 當日或之前的資料。WebSearch 結果中標示 11/6 之後的內容已排除。

## Analyst consensus

最新快照 (yf rec_summary, 0m): 47 家中 43 家 Buy 或 Strong Buy (Strong Buy 9、Buy 34)，Hold 4 家，Sell 0 家，Strong Sell 0 家。快照日期未標示，視為最新可得資料。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 (家) | 買方占比 |
|---|---|---|---|---|---|---|
| -2m | 8 | 31 | 5 | 0 | 44 | 88.6% |
| -1m | 8 | 32 | 6 | 0 | 46 | 87.0% |
| 0m (最新) | 9 | 34 | 4 | 0 | 47 | 91.5% |

近期變動: 兩個月內買方家數由 39 增至 43、覆蓋家數由 44 增至 47，Hold 由 5 降至 4，無賣方評級出現。yf recommendations 工具回傳的是月度彙總，沒有個別升評、降評事件與目標價資料，因此無法列出具體 upgrade/downgrade 與目標價變動。

交叉參考 (WebSearch 摘要，權重低): Google Finance 摘要顯示 3 個月內 28 家給予評級，其中 23 家 Buy 或 Strong Buy、5 家 Hold，與 yf 覆蓋數不一致，快照日期亦不明，僅作方向參考。

## Retail social

- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 public JSON 經 WebFetch 回應無法連線，直接以 curl 測試時 proxy 回 403 (CONNECT tunnel failed)。本次沒有貼文樣本，無 tilt 與聲量數據。
- StockTwits: api.stocktwits.com 無法解析 (DNS ENOTFOUND)，需在 session 網路設定中允許該網域後才能重試。本次未重試。
- X 與options 分析站 (WebSearch 樣本，非完整統計):
  - 8 月底 X 樣本多數標示看多，少數中性，樣本中未見看空貼文；內容多半把 MRVL 放在 AI 基礎建設觀察名單中。
  - 6 月中 options 分析站顯示 call dollar volume 占 63.5%，偏多；7 月一篇分析的樣本偏空 (約 60% 看空、30% 看多、10% 中性)；8 月底的 options flow 多數偏多，8/26 一篇例外偏空。
  - 技術面: 有分析指出股價跌破 50 日均線，另有分析提醒超買與壓力位。
- 聲量: 無 Reddit、StockTwits 計數可供比較，無法與歷史基準做量化比較，本節不推定聲量高或低。
- 代表性標題 (SA 文章標題，非散戶貼文): "Marvell: Cheap Today, Critical To Tomorrow's AI Data Centers"，偏多論述。
- 主要主題:
  1. AI 資料中心與客製化晶片題材，多數偏多論述。
  2. 近期股價波動與財測指引疑慮，為短線看空論點。
  3. 技術面超買、均線與壓力位討論，立場分歧。

## Insider activity

Net 6mo (2026-05-02 至 2026-11-02，以 yf 記錄的有價格交易計算): 買入 $0 (6 個月內無公開市場買入)；賣出 12 筆，合計約 19.0M USD。

以下為各人合計 (USD，M):

| 內部人 | 職稱 | 筆數 | 合計賣出 (M USD) | 主要紀錄 |
|---|---|---|---|---|
| Matthew Joseph Murphy | CEO | 5 | 8.59 | 5/13、6/15、7/15、8/17、9/15，每筆 7,500 股，約每月一次 |
| Christopher R. Koopmans | President (間接持有) | 3 | 6.66 | 7/1 10,000 股 @281.92；8/3 @180.50；9/1 @203.27 |
| Sandeep Bharathi | Officer | 2 | 2.46 | 6/16 2,231 股 @299.13；7/16 9,013 股 @199.24 |
| Daniel James Durn | CFO | 1 | 0.63 | 6/23 2,250 股 @281.01 |
| Willem A. Meintjes | CFO (前任，yf 標示) | 1 | 0.70 | 5/15 4,000 股 @175.24 |

核對: 逐筆 Shares × 價格與 yf Value 一致 (例: CEO 9/15 7,500 × 223.39 = 1.675M)，12 筆加總約 19.04M USD。

說明:
- 未列入淨額的紀錄: 2026 年 6 月至 9 月多筆無價格紀錄 (董事 6/10 至 6/12 各 3,940 股；7/15 多位officer 與 CEO 約 2 萬股等)，形式上接近權益獎勵或稅款代扣，未驗證。
- 贈與: 6/15 Mark Casper 1,000 股 (間接)，6/17 Rebecca House 750 股，無金額。
- CEO 的 5 筆賣出頻率規律，可能為 10b5-1 預設計畫，尚未驗證。
- 對照: 2025 年 9 月約 $77-78 時，CEO、CFO、President 與 Officer 曾有一波公開市場買入 (合計約數百萬美元量級，見 yf 紀錄)，2026 年 5 月至 9 月則以賣出為主、價位在 $175-300 區間。
- yf 職稱標示前後不一 (例如 Koopmans 有 COO、President、CEO 三種紀錄)，本報告以最近一筆職稱為準。

## Ownership shifts

機構持股 82.09%，流通股機構持股 82.50%，機構家數 3,001。內部人持股 0.50%。yf 僅提供單一快照，無法判定近期增減趨勢。

## Net sentiment score

- 分析師面: 偏多 (信心: 高)。買方占比 91.5%，無賣方，買方家數 2 個月增加 4 家。
- 內部人面: 偏空 (信心: 中低)。6 個月內 12 筆賣出約 19.0M USD、0 筆公開市場買入；但 CEO 規律賣出可能屬預設計畫，訊號強度有限。
- 散戶面: 無法判定 (信心: 低)。Reddit 與 StockTwits 皆無資料，外部樣本 8 月底偏多、7 月一篇偏空。
- Composite: 中性 (信心: 低)。分析師偏多與內部人賣出互相抵銷，散戶面資料不足以定向。

Divergence flag: 是 (部分)。分析師偏多與內部人持續賣出方向相反，但散戶 tilt 未經確認，不能判定散戶是否與分析師背離。

## 資料缺口

1. Reddit (r/wallstreetbets、r/stocks): proxy 回 403，無樣本。
2. StockTwits: DNS 無法解析，需在 session 網路設定中允許 api.stocktwits.com。
3. 分析師升降評與目標價歷史: yf recommendations 只回傳月度彙總。
4. 機構持股趨勢: 只有單一快照。
5. 股價現況 (11/2 收盤) 未取得，因財經網站被 proxy 阻擋；insider 交易價格僅反映 5 月至 9 月區間。

## 參考來源 (WebSearch)

- [Marvell: Cheap Today, Critical To Tomorrow's AI Data Centers (Seeking Alpha)](https://seekingalpha.com/article/4849753-marvell-cheap-today-critical-to-tomorrows-ai-data-centers)
- [MRVL Trading Analysis 08/31/2026 (Historical Option Data)](https://historicaloptiondata.com/?p=81695)
- [MRVL Trading Analysis 09/01/2026 (Historical Option Data)](https://historicaloptiondata.com/?p=82956)
- [MRVL Trading Analysis 07/07/2026 (Historical Option Data)](https://historicaloptiondata.com/?p=66580)
- [Marvell Technology stock forecast (Capital.com)](https://capital.com/en-eu/analysis/marvell-technology-stock-forecast)

SENTIMENT REPORT COMPLETE
