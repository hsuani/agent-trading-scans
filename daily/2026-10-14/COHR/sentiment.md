# Sentiment — COHR as of 2026-10-14

## Analyst consensus
yf rec_summary（0m）：4 Strong Buy / 15 Buy / 5 Hold / 0 Sell / 0 Strong Sell，共 24 家，Buy 類佔 79%（19/24）。近四個月（-1m 至 -3m）評級分布幾乎不變，僅 -2m 與 -3m 的 Buy 少一家（14 vs 15），沒有賣方評級。

- 近期升降評級：yf `recommendations` 回傳的仍是各月份評級計數，而非個別升降評等事件，因此無法從 yf 取得逐筆 upgrade/downgrade。
- 網路搜尋：找不到 2026 年的個別升降評等新聞。可見的最新條目為 2026-08-13 前後：Jefferies 維持 Buy 並將目標價由 $375 調至 $420；Morgan Stanley 維持 Equal-Weight 並將目標價由 $330 調至 $375。這些來自搜尋摘要，未經原始頁面驗證。
- 目標價：聚合站顯示共識目標價約 $307（最高 $500），但該站的分析師家數為 20，與 yf 的 24 家不一致，兩者口徑可能不同。
- 其他搜尋結果多為 2023 至 2024 年資料（如 B. Riley、Rosenblatt、Northland 降評），已判定為過時，不納入判斷。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 的搜尋請求皆被擋（無法存取 www.reddit.com），本次無貼文樣本，無法判定散戶語氣。
- StockTwits：api.stocktwits.com 無法解析網域（DNS 失敗），依規則軟失敗，略過。
- X / 新聞搜尋：一則聚合頁顯示 Google Finance 的 outlook widget 為 55.6% bullish / 5.6% bearish（約 2026-10-05，COHR 收於 ~$333.64，52 週區間 $108.19 至 $440.00，P/E 約 80.98）。另一頁顯示 short float 約 6.0%、put/call ratio 約 1.17（該頁標示為 bearish）。這些是機構或聚合數據，不代表散戶語氣。
- 聲量（buzz volume）：無法量化，因為缺少 Reddit 與 StockTwits 資料。
- 主要主題（僅能由搜尋摘要推斷）：估值偏高（P/E 約 81）、股價在 52 週高點附近、短部位約 6%。這些屬於市場討論的常見論點，不是逐篇貼文的引述。

## Insider activity
過去 6 個月（2026-04-14 至 2026-10-14）yf 共 11 筆公開市場賣出、0 筆買入。
- 淨額：買入 $0；賣出約 $10.65M（11 筆）。
- 賣出主力：
  - Sherri R. Luther（CFO）：4 次賣出，4/22 @ $351（2,000 股）、5/12 @ $372.96（2,000 股）、7/22 @ $306.68（1,000 股）、8/18 @ $324（3,000 股，約 $972K）。
  - Julie Sheridan Eng（CTO）：9/01 @ $270.69–276.83，13,077 股，約 $3.58M，為單筆最大的管理層賣出。
  - Enrico DiRolomo（董事）：9/11 @ $305.98，5,315 股，約 $1.63M；8/31 另有 2,272 股（約 $0.63M）。
  - Robert P. Beard（高管）：9/09 @ $309.32，500 股，約 $155K。
  - 其他董事：Lisa Neal-Graves（9/02，約 $0.59M）、Stephen Skaggs（8/31，約 $0.63M）、Howard Xia（5/11，約 $0.71M，含 derivative 轉換）。
- CEO James R. Anderson：沒有公開市場賣出，只有 8/28 的股票獎勵（30,564 股）。
- 其他 8/28 的 Stock Award（獎勵）不計入買賣，包括 CFO、CTO 與多位高管。
- 注意：yf 資料未標示賣出是否屬 10b5-1 計畫，因此無法判斷是否為預定性質的賣出，也無法排除其他解釋。

## Ownership shifts
- insidersPercentHeld：4.42%
- institutionsPercentHeld：87.25%（float 口徑 91.29%）
- institutionsCount：1,779
- 沒有時間序列資料，無法判斷機構集中度是上升還是下降。

## Net sentiment score
- 分析師面：偏多（bullish），信心高。24 家中 79% 為 Buy，無 Sell。
- 內部人面：偏空（bearish 傾向），信心中等。6 個月內 0 買入、約 $10.65M 賣出，但多為高階管理層與董事的例行或計畫性賣出，屬常見情況，不能直接視為看空訊號。
- 散戶面：無法判定。Reddit 與 StockTwits 皆無資料，搜尋僅有聚合 outlook 與 short/put-call 數據。
- 綜合：中性偏多（neutral-to-bullish），信心低至中等。主要因散戶資料缺漏，且內部人賣出的性質不明。

Divergence flag：無法判定（散戶資料缺漏）。若日後取得散戶資料，需比較其語氣與分析師的偏多傾向。

## 資料缺口與來源狀態
- yf `recommendations`：回傳的是月度評級計數，而非逐筆升降評等事件。
- Reddit（r/wallstreetbets、r/stocks）：HTTP 存取被擋，無資料。
- StockTwits：DNS 解析失敗，無資料。
- 網路搜尋：2026 年個別升降評等資料不足，部分來源過時或口徑不一。
- 本次快取回退未觸發：yf 的 cookie/crumb 取得失敗（ConnectionError），但仍回傳資料，已依 yf 輸出使用。

## Metrics table

| 指標 | 數值 | 說明 |
|---|---|---|
| 分析師評級（0m） | 4 SB / 15 B / 5 H / 0 S / 0 SS | 共 24 家，Buy 類 79% |
| 近 4 個月評級變化 | Buy 15 → 14（-2m 起） | 無賣方評級 |
| 共識目標價（聚合站） | 約 $307（高 $500） | 分析師家數口徑不一（20 vs 24） |
| 內部人 6 個月淨買賣 | 淨賣出約 $10.65M | 買入 $0，賣出 11 筆 |
| CEO 6 個月公開市場交易 | 0 | 僅 8/28 股票獎勵 |
| CFO 6 個月賣出 | 4 筆，約 $2.40M | Luther，多次分批賣出 |
| 內部人持股比例 | 4.42% | yf major_holders |
| 機構持股比例 | 87.25%（float 91.29%） | yf major_holders |
| 機構家數 | 1,779 | yf major_holders |
| Short float | 約 6.0% | 搜尋聚合，未驗證 |
| Put/Call ratio | 約 1.17 | 搜尋聚合（標示 bearish），未驗證 |
| Google outlook | 55.6% bullish / 5.6% bearish | 約 2026-10-05，搜尋摘要 |
| Reddit 貼文樣本 | 0 | 存取被擋 |
| StockTwits 訊息 | 0 | DNS 失敗 |

Sources: yf 工具輸出（rec_summary、recommendations、insider、major_holders）；網路搜尋摘要（Google Finance 與聚合站點，未逐一開啟原始頁面）。

SENTIMENT REPORT COMPLETE
