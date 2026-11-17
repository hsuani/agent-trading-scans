# Sentiment — IPGP (IPG Photonics) as of 2026-11-18

資料時點注意：yf 快取於 2026-11-17 15:55 UTC 更新；最新內部人交易日為 2026-11-03；info 欄位（價格、目標價）來自快取。WebSearch 結果多數無明確日期，僅作參考。

## Analyst consensus

rec_summary（單位：家數）

| 評等 | 家數 |
|---|---|
| Strong Buy | 2 |
| Buy | 4 |
| Hold | 2 |
| Sell | 0 |
| Strong Sell | 1 |
| 合計 | 9 |

分布為 6 買進 / 2 持有 / 1 賣出，偏多。注意：info 欄位顯示 numberOfAnalystOpinions = 7，與 rec_summary 合計 9 不一致，需以來源確認。

目標價（USD / 股，info 快取）：平均 106.43、中位數 100.00、最高 135.00、最低 78.00。以現價 61.52 計算，平均目標價相對現價約 +73%。

近期調整：
- `recommendations` 端點回傳的仍是同格式的家數分布（三個期間數字完全相同），無法取得個別升降評等歷史，**升降評等紀錄：DATA_UNAVAILABLE**。
- 以下為二手彙總網站的片段，未經 yf 驗證，僅供參考：Roth/MKM 於 2026-05-06 將目標價下調至 $149；Needham 同日升評至 Buy；Citigroup 於 2026-08-11 維持 Buy 並將目標價由 $150 下調至 $137；MarketBeat 另列 Stifel 於 2026-03-27 重申 Sell。

## Retail social

- Reddit：**DATA_UNAVAILABLE**。依指示未直接抓取 Reddit；WebSearch 未回傳 r/wallstreetbets 或 r/stocks 上的 IPGP 討論串，無法取樣。
- StockTwits / X：StockTwits 直接 API 未使用。WebSearch 找到一則 StockTwits 頁面標示「Bearish Sentiment」，附數值 34，但未註明計算方式與擷取日期，僅能作為弱訊號。X 端無可用結果。
- 選擇權與空單：Benzinga 頁面（日期不明）顯示 put/call 比率 1.08、空單比例 23.8%（略升）。tool 快取的 shortPercentOfFloat 為 23.4%，與之相符。
- 第三方情緒：Equibles 標示整體偏多，主因是機構持續吸納（日期不明）。
- 討論量（buzz volume）：**DATA_UNAVAILABLE**，無可靠提及次數可與平常比較。

Retail tilt：混雜偏空。信心低，樣本僅來自零星網頁，不是直接的社群貼文。

Themes（從 WebSearch 片段歸納）：
1. 價格位置：快取 info 顯示現價 61.52，接近 52 週低點 61.35，較 52 週高點 155.82 下跌約 60%。
2. 獲利與毛利下滑：Simply Wall St 的分析師情緒偏負面，指向銷售與毛利率下滑。
3. 空單比例偏高，約 23%。
4. 大股東與內部人持續賣出，市場關注點放在 Gapontsev 相關信託的減持。
5. 現金充裕、無負債（一篇分析提及約 $870M 現金與短期投資，日期不明）。

## Insider activity

統計區間：2026-05-18 至 2026-11-18（6 個月）。單位：USD M。

| 項目 | 筆數 | 金額 (USD M) |
|---|---|---|
| 公開市場賣出（合計） | 13 | 24.75 |
| 其中：>10% 股東 Gapontsev 信託與 IP Fibre Devices | 7 | 22.72（約 92% 的賣出） |
| 其中：董事 Scherbakov（同時為 >10% 股東）| 3 | 0.55 |
| 其中：CFO Mammen | 1 | 1.20 |
| 其中：董事 Tang、總法律顧問 LoPresti | 2 | 0.29 |
| 公開市場買入 | 1 | 0.20 |
| 淨額 | — | 約 −24.55 |

Net 6mo：$0.20M 買入、$24.75M 賣出，淨賣出約 $24.55M。

Notable：
- 董事 John R. Peeler 於 2026-08-26 以約 $72.84–74.57 買入 2,710 股（USD 0.20M），為區間內唯一公開市場買入。
- CFO Timothy Mammen 於 2026-05-22 以約 $119.60–120.37 賣出 9,975 股（USD 1.20M）。
- CEO Mark Gitin 在區間內無公開市場交易，僅有 2026-02-18 的股票獎勵（不在區間內）。
- Gapontsev 信託於 2026-07-21 以約 $100–103 賣出 56,316 股（USD 5.76M），為區間內單筆最大金額之一。IP Fibre Devices 於 2026-06-29 以約 $100–106 賣出 65,700 股（USD 6.81M）。

單位驗證：Gapontsev 信託 2026-11-03 賣出 20,652 股 × $75.18 = USD 1,552,617，與 tool 回傳的 Value 相符。

## Ownership shifts

- 內部人持股約 39.0%，機構持股約 79.2%，機構數 474 家（yf major_holders）。
- 資料品質旗標：機構佔流通股比例回傳 129.7%（>100%），與定義不符，**此欄位不採用**。
- 前十大機構（多為 2026-09-30 季報，部分為 06-30）：10 家中有 9 家持股增加。
  - Sumitomo Mitsui Trust：+50.9%
  - Westwood：+15.7%（06-30）
  - Vanguard Capital：+7.4%
  - Dimensional：+12.9%
  - Neuberger Berman：−15.8%，為唯一減持者
- 單季快照，尚無足夠時間序列判斷趨勢。整體傾向機構小幅加碼，但需與大股東賣出並看。

## Net sentiment score

- 分析師：**偏多**（信心：中。家數少，且 info 與 rec_summary 家數不一致）
- 零售：**混雜偏空**（信心：低。無 Reddit 資料，StockTwits 數值與 put/call 皆未標日期）
- 內部人：**偏空**（信心：中。賣出約九成來自 >10% 股東信託，非 CEO 或 CFO 的主動減持；唯一公開買入為董事小額買進）
- 機構持股：**小幅偏多**（信心：中。9/10 前十大持股增加）

Composite：**中性偏空**（信心：低至中）。分析師與機構偏多，但內部人與零售偏空，且零售資料薄弱。

Divergence flag：**是**。分析師偏多，與零售及內部人偏空方向相反。依規則，此類背離有參考價值，但本次零售端證據太薄，不應過度解讀。

## Data gaps

- Reddit：DATA_UNAVAILABLE
- 升降評等歷史：DATA_UNAVAILABLE
- 討論量：DATA_UNAVAILABLE
- 機構持股 >100% 之欄位：已排除

SENTIMENT REPORT COMPLETE
