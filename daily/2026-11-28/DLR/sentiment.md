# Sentiment — DLR as of 2026-11-28

> 注意: 目前系統日期為 2026-11-27，報告日期 2026-11-28 尚在未來，所有資料以 WebSearch 能找到的最新快照為準，不含 11-28 當日資料。

## 資料來源狀態
- `pipeline/tools/yf DLR rec_summary` 與 `recommendations`: 權限被自動分類器拒絕，未重試。分析師分布改以 WebSearch 聚合資料代替，數字來源彼此不一致，見下。
- `pipeline/tools/yf DLR insider`、`major_holders`: 正常取得（yf 回報 cookie/crumb 失敗，但資料有回傳）。
- Reddit (r/wallstreetbets、r/stocks): 無法取得近期 DLR 討論串，DATA_UNAVAILABLE。
- StockTwits: 無法取得多空比例，DATA_UNAVAILABLE。
- X / 新聞: 僅有 WebSearch 結果，多為分析師與技術面文章，無社群情緒量化數字。

## Analyst consensus
各來源快照日期不同，數字不能直接合併，僅供區間參考:
- Barchart（無明確日期，搜尋結果中最新者）: 34 位分析師，25 Strong Buy / 2 Moderate Buy / 7 Hold，共識 Strong Buy。
- Barchart（較早一篇，約 Apr/May 2026）: 33 位分析師，21 Strong Buy / 2 Moderate Buy / 10 Hold，共識 Moderate Buy。
- 聚合站 11 月 10 日快照: 34 位中 29 位 Buy，平均目標價 224.12 USD，股價約 180.1 USD。
- Benzinga（8 月）: 27 位分析師共識 Buy，平均目標價 210 USD。
- TipRanks（日期不明）: 24 位分析師，平均目標 218.90 USD，最高 250 USD，最低 192 USD。

近期評等動作（日期為搜尋結果標示）:
- HSBC 升至 Buy，目標 240 USD（8/14）。
- Evercore ISI 目標升至 240 USD（8/18）。
- JP Morgan 目標 235 USD（7/24）。
- Truist 目標 220 USD（7/30）。
- Scotiabank 維持 Outperform，目標下調至 189 USD。
- KeyBanc 偏中性（neutral-style）。
- Bernstein 於 3/5 首次給予 Outperform。
- DBS 目標 213 USD（日期不明）。

11 月內未找到明確的新評等變動。

股價背景: 11/6 收盤 174.61 USD（Fox Business）；Weiss Ratings 報導當日下跌約 4.5%，較 4 月 52 週高點 208.14 USD 低約 15%，並將跌幅歸因於市場重新評估未來資料中心建設的監管與許可環境（單一來源，未經交叉驗證）。

## Retail social
- Reddit: 未取得 DLR 近期 WSB 或 r/stocks 討論串。MarketBeat 的 WSB 提及數據為 2024 年舊資料，ChartExchange 的 r/stocks 快照為 2025 年 6 月，皆已過期，不採用。傾向 DATA_UNAVAILABLE。
- StockTwits: 網頁有情緒區塊，但搜尋結果未擷取多空比例。DATA_UNAVAILABLE。
- X / 其他社群: 無可量化資料。TipRanks bloggers 顯示 90% bullish，但僅 10 則意見且日期不明，權重低。Trade-Ideas 指出約 2% 的投資人押注做空，來源與日期不明。
- 聲量: 無法與常態比較，定性判斷為低到中等，缺乏可靠計數。
- 主題（來自新聞與評論，非直接的散戶貼文）:
  - 多頭: AI 基礎設施「房東」定位，供電、散熱、網路連接需求強。
  - 空頭: 估值偏高（有評論指股價不便宜，股息率低）；許可與監管風險。
  - 中性: 股價在 2026 年累計上漲（Barchart 稱 YTD 約 24.5%），但近期動能轉弱。

## Insider activity
查詢區間: 2026-05-28 至 2026-11-28（6 個月）。
- 公開市場買入: 0 筆，約 $0.000M。
- 公開市場賣出: 1 筆，約 $0.039M。董事 Mark R. Patterson，2026-08-27，200 股，均價 193.96 USD。
- 不計入的項目: 2026-05-29 董事 Jean Mandeville 股票獎勵 1,289 股（無現金交易）。
- 6 個月內 CEO/CFO 無交易紀錄。
- 背景（超出 6 個月，僅供參考）: CEO Andrew Power 於 2025-09-15 賣出 58,000 股，約 $10.16M；CFO Matt Mercier 於 2024-12-12 賣出 2,518 股，約 $0.47M。

6 個月淨額: 買入 $0.000M，賣出 $0.039M，淨賣出約 $0.039M，規模小，且僅一位董事。

## Ownership
- 機構持股（yf major_holders）: 機構持股比例回傳 100.33%，超過 100%，應為資料重複計算，不可直接使用。機構數量 1,824 家。
- 內部人持股: 0.031%。
- 機構持股趨勢（季度時間序列）: DATA_UNAVAILABLE。

## Net sentiment score
- 分析師: 偏多（Buy 比例高，多數目標價高於 11 月股價約 180 USD）。信心: 中高，但來源數字不一致。
- 散戶/社群: 無法判定（DATA_UNAVAILABLE）。
- 內部人: 輕微偏空（單筆小額董事賣出，無 CEO/CFO 買入）。信心: 低，樣本少。
- 綜合: 偏多（bullish-leaning），信心低到中等。主要依據為分析師。

Divergence flag: 無法判定。散戶側資料不足，無法比較與分析師傾向是否相反。

## Metrics table

| 指標 | 數值 | 單位 | 來源 / 日期 | 狀態 |
|---|---|---|---|---|
| 分析師家數（最新 Barchart） | 34 | 位 | Barchart，日期不明 | 可用 |
| Strong Buy / Moderate Buy / Hold | 25 / 2 / 7 | 位 | Barchart，日期不明 | 可用 |
| 分析師家數（11/10 快照） | 34（Buy 29） | 位 | 聚合站，11/10 | 可用 |
| 平均目標價（11/10 快照） | 224.12 | USD | 聚合站，11/10 | 可用 |
| 平均目標價（TipRanks） | 218.90 | USD | TipRanks，日期不明 | 可用 |
| 目標價區間 | 192 – 250 | USD | TipRanks，日期不明 | 可用 |
| 股價（11/6 收盤） | 174.61 | USD | Fox Business，11/6 | 可用 |
| 股價（11/10 附近） | ~180.1 | USD | 聚合站，11/10 | 可用 |
| 6 個月公開市場買入 | 0.000 | M USD | yf insider | 可用 |
| 6 個月公開市場賣出 | 0.039 | M USD | yf insider | 可用 |
| 6 個月淨額 | -0.039 | M USD | 計算 | 可用 |
| 6 個月內 CEO/CFO 交易 | 0 | 筆 | yf insider | 可用 |
| 機構持股比例 | 100.33 | % | yf major_holders | 資料異常（>100%） |
| 機構家數 | 1,824 | 家 | yf major_holders | 可用 |
| 內部人持股比例 | 0.031 | % | yf major_holders | 可用 |
| Reddit 提及量 / 多空 | — | — | — | DATA_UNAVAILABLE |
| StockTwits 多空比例 | — | — | — | DATA_UNAVAILABLE |
| 機構持股季度趨勢 | — | — | — | DATA_UNAVAILABLE |
| rec_summary / recommendations 原始數據 | — | — | 權限被拒 | DATA_UNAVAILABLE |

## 結論
DLR 的分析師傾向偏多，內部人 6 個月內僅有一筆小額董事賣出。散戶社群情緒因缺乏可取得的 Reddit、StockTwits 數據而無法判定。綜合評分: 偏多，信心低到中等。本報告不含交易建議。

SENTIMENT REPORT COMPLETE
