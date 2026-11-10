# Sentiment — WDC as of 2026-11-11

資料來源狀態：yf 分析師與內部人資料可用；Reddit（r/wallstreetbets、r/stocks）抓取失敗（WebFetch 無法連線 www.reddit.com）；StockTwits 無法解析 api.stocktwits.com（網路白名單未開放，需於 session 網路設定允許該網域後再試）；僅 WebSearch 提供新聞與選擇權情緒的間接資料。散戶情緒為缺資料狀態。

## Analyst consensus

26 位分析師：5 strongBuy / 17 buy / 4 hold / 0 sell / 0 strongSell（買進系 22 位，占 84.6%；持有 4 位，占 15.4%；賣出 0 位）。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 當月（0m） | 5 | 17 | 4 | 0 | 0 |
| 上月（-1m） | 4 | 17 | 5 | 0 | 0 |
| -2m | 4 | 17 | 5 | 0 | 0 |
| -3m | 4 | 17 | 5 | 0 | 0 |

- 近期動向：本月 strongBuy 多 1 位、hold 少 1 位，其餘穩定；過去三個月評等分布幾乎沒有變動。
- 逐筆升降評等：yf 僅回傳彙總計數，無法列出個別券商的升級或降級紀錄，此項待補。
- 目標價：yf 工具未提供。WebSearch 找到的 Benzinga 目標價 149.17 USD（24 位分析師）標示為 2025 年底資料，已明顯過時，不採用。
- 股價參考：WebSearch 所引用的 2026-11-06 收盤價為 263.78 USD。

## Retail social

- Reddit：抓取失敗，無樣本。
- StockTwits：無法連線，無樣本。
- X / 新聞與選擇權情緒（WebSearch，來源日期不一，部分為 2026 年 7–8 月）：
  - Benzinga 情緒頁顯示空單佔流通股約 7.8%；近期選擇權成交偏負面（頁面日期不明）。
  - MarketBeat 8 月多篇快訊以股價大幅震盪為主（單日跌幅約 6.9%–7.4%，另有一日漲 3.7%）。
  - 一則 Motley Fool 標題引述 WDC 自 6 月起跌約 53%（經 MarketBeat 轉載）。
- 聲量估計：無法量化與基準比較，定性判斷為「缺資料」。
- 散戶傾向：無直接樣本，無法判定；僅能以選擇權成交與新聞標題作間接代理，傾向偏空。
- 主要題材（來自新聞，非散戶原文）：
  - 多方：硬碟需求強、全球供給趨緊，支撐營收與毛利展望。
  - 空方：中國 CXMT（長鑫存儲）競爭疑慮；股價自高點大幅回落。

## Insider activity

Net 6mo（2026-05-11 至 2026-11-11）：$0 買進（公開市場買入）／約 $25.5M 賣出（18 筆）。
- 無任何公開市場買進紀錄；其餘為獎勵授予（Stock Award）、贈與（Stock Gift），金額為 0，不計入資金流。
- 6 個月內賣出金額依人員加總（M USD）：

| 內部人 | 職稱 | 賣出金額（M USD） | 筆數 | 備註 |
|---|---|---|---|---|
| Tan Irving | CEO | 8.90 | 1 | 2026-08-11，20,000 股，約 441–447 USD |
| Brian Scott Davis | Officer | 5.01 | 1 | 2026-05-11，10,000 股，約 490–510 USD |
| Martin I. Cole | Director | 3.86 | 4 | 6 月與 7 月多次出售 |
| Stephanie A. Streeter | Director（間接） | 2.52 | 1 | 2026-09-01，5,600 股 |
| Vidyadhara K. Gubbi | Officer | 2.20 | 2 | 6 月與 9 月 |
| Cynthia Lock Tregillis | Officer | 2.59 | 8 | 持續性小額出售 |
| Bruce E. Kiddoo | Director | 0.40 | 1 | 2026-05-28 |

- 最大單筆：CEO Tan Irving 2026-08-11 出售 20,000 股，約 8.90M USD。
- CFO Kris Sennesael 在此窗口內無賣出紀錄（僅有 2025 年股票授予）。
- 數字驗算：CEO 20,000 股 × 約 444.7 USD ≈ 8.9M USD，與工具回傳吻合，單位正確（USD，以 M 表示）。
- 最近一筆交易為 2026-10-21（Tregillis，約 0.31M USD），資料有時間落差，10 月下旬至今的交易可能尚未反映。
- 留意：此期間股價由約 380–545 USD 區間回落至約 264 USD（依 yf 出售價與 WebSearch 2026-11-06 收盤價對照），內部人在高價區大量出售，且無買進。出售可能屬預先安排的交易計畫，工具無法確認。

## Ownership shifts

- 機構持股 88.9%（institutionsPercentHeld 0.889），機構數 2,433 家，內部人持股 0.27%。
- 機構持股趨勢：工具僅提供單一時點快照，無歷史比較，無法判定增減方向。此項待補。

## Net sentiment score

Composite：中性（信心：低）。
- 分析師：偏多（84.6% 買進，評等近三個月穩定，無賣出）。
- 內部人：偏空（6 個月約 25.5M USD 賣出、零公開市場買進）。
- 選擇權與價格動向（間接）：偏空（空方占流通股約 7.8%，近期選擇權偏負面，股價大幅回落）。
- 散戶：無資料。

信心低的原因：散戶兩個來源皆失敗，目標價過時，機構趨勢缺資料；分析師與內部人方向相反，綜合後落在中性。

Divergence flag：是（低信心）。分析師傾向偏多，而內部人交易與選擇權動向偏空，兩者方向相反。散戶傾向無法驗證，因此無法確認是否為「散戶與分析師背離」。建議後續補抓 Reddit 或 StockTwits（需先開放網域）、個別升降評等紀錄與目標價，再重新評估此旗標。

SENTIMENT REPORT COMPLETE
