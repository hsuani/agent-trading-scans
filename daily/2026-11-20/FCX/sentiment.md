# Sentiment — FCX as of 2026-11-20

資料來源狀態：
- yf（recommendations / rec_summary / insider / major_holders）：成功
- Reddit r/wallstreetbets、r/stocks：無法存取（WebFetch 回報 blocked），本次無散戶貼文樣本
- StockTwits：api.stocktwits.com DNS 解析失敗，本 session 網路白名單需開放後才能重試
- WebSearch（X / 新聞）：結果多為無日期或舊文章，無法代表 2026-11 當月情緒，僅作背景參考

## Analyst consensus
23 位分析師：6 Strong Buy / 12 Buy / 4 Hold / 1 Sell / 0 Strong Sell（yf rec_summary，約 Buy 比例 78%）。
Recent moves：yf recommendations 四個期間（0m 至 -3m）的評級分布完全相同，代表此來源僅為單一快照，無可用的升降評等時序，無法判定近期升降級或目標價調整。
外部參考（WebSearch，日期不明，可能過時）：Investing.com 顯示 19 Buy / 3 Hold / 1 Sell，目標價區間約 $30 至 $82；Barchart 相關文章提到 JPMorgan 維持 Buy、目標價 $76，平均目標價 $69.80。另有 Morgan Stanley 於 2025-07 由 Overweight 降至 Equal-Weight 的舊聞。
結論：分析師整體偏多，但缺乏近期變動資料，需於上游補充最新評級時序。

## Retail social
- Reddit：本次無法取得 r/wallstreetbets 與 r/stocks 資料，無貼文樣本，無法評估 tilt。
- StockTwits / X：StockTwits 無法連線。X 無直接存取，WebSearch 未找到 2026-11 的具體討論。
- Buzz 量：無法量化（資料缺），無法與典型量比較。
- Themes：無法判定。若需補強，建議於允許 reddit.com 與 api.stocktwits.com 後重跑。

## Insider activity
統計區間：2026-05-20 至 2026-11-20（6 個月）。金額單位 USD M。

Net 6mo：公開市場買入 $0.00M；公開市場賣出約 $8.39M（不含非現金配股）。
非現金配股（Stock Award，屬於例行授予）：董事於 2026-06-01 各獲 2,800 股（$0 價格）；2026-07-01 與 2026-10-01 的董事配股合計約 $0.11M。

| 日期 | 內部人 | 職稱 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-07-30 | HIGGINS STEPHEN T | Officer | 賣出 @ $63.00 | 7,550 | 0.48 |
| 2026-08-05 | HIGGINS STEPHEN T | Officer | 賣出 @ $69.50 | 14,277 | 0.99 |
| 2026-08-05 | MIKES ELLIE L. | Officer | 賣出 @ $70.00 | 4,773 | 0.33 |
| 2026-08-25 | CURRAULT DOUGLAS NICHOLAS II | General Counsel | 選擇權行使 80,000 股後賣出 @ $78.56 | 80,000 | 6.28 |
| 2026-08-27 | KENNARD LYDIA H | Director | 賣出 @ $79.11 | 3,798 | 0.30 |

Notable：最大一筆為 General Counsel CURRAULT 行使選擇權後全數出售 80,000 股，金額約 $6.28M。CFO ROBERTSON 與 CEO QUIRK 在此區間無公開市場交易。Chairman ADKERSON 於 2026-02 有大額賣出，但已超出 6 個月窗口。
注意：賣出集中在 $63 至 $79 區間，股價區間與 2026 年 2 月相近。部分賣出可能屬於 10b5-1 計畫，yf 資料無法判定。

## Ownership shifts
- 機構持股：88.96%（institutionsFloatPercentHeld 89.6%），機構數 2,646。
- 內部人持股：0.72%。
- 趨勢：yf major_holders 僅為單一時點快照，無時序，無法判定機構集中度是增加或減少。

## Net sentiment score
Composite：**中性（信心低）**
- 分析師面：偏多（23 位中 18 位 Buy 以上）。
- 內部人面：偏空訊號。6 個月內 $8.39M 公開市場賣出、零買入，但多數為選擇權行使或例行配股後的賣出，不應直接解讀為看空。
- 散戶面：無資料，無法納入評分。
- 整體因散戶資料缺失與分析師評級無時序，信心低。

Divergence flag：無法判定（散戶資料缺）。若以分析師與內部人對比，兩者方向不一致（分析師偏多、內部人淨賣），但這屬於內部人例行減持的結構性因素，不宜視為明確背離。

SENTIMENT REPORT COMPLETE
