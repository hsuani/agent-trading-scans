# Sentiment — AXTI as of 2026-11-16

## Analyst consensus
yf `rec_summary`（最新一期 0m）：6 位分析師，5 buy（2 strong buy + 3 buy）/ 1 hold / 0 sell。過去 3 個月（-1m 至 -3m）維持 4 buy + 1 hold 左右，無 sell，評級結構幾乎沒有變化。

| 項目 | 數值 | 來源 |
|---|---|---|
| 最新分布 | 5 buy / 1 hold / 0 sell | yf rec_summary |
| 共識標籤 | Hold | MarketBeat（WebSearch） |
| 共識目標價 | US$77.80（8 月時為 US$77.00） | MarketBeat（WebSearch） |
| 個別目標價 | Wedbush US$93 | TIKR 標題（WebSearch，僅標題可見） |

近期動向：
- Needham 於 7 月由 hold 升為 buy（MarketBeat 轉述）。
- Northland 將 FY2026 EPS 預估上修至 US$1.15（原 US$0.81）（MarketBeat 轉述）。
- 業績後股價急跌：TIKR 報導一週內下跌 14%，MarketBeat 11/5 快訊提到單日下跌 16%、盤中最低 US$40.42。
- 注意：yf 的 buy 計數與 MarketBeat 的 "Hold" 標籤不一致，可能是資料來源或更新時點不同，未能釐清。
- `recommendations` 工具只回傳月度計數，沒有逐家券商的升降評等紀錄，因此無法列出個別調評事件的日期與方向。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：**不可用**。WebFetch 回傳 "unable to fetch from www.reddit.com"，依規定未重試。
- StockTwits：**不可用**。api.stocktwits.com DNS 解析失敗（ENOTFOUND），顯示該網域未列入本次 session 允許清單，依規定未重試。需在 session 網路設定中放行後才能補查。
- X / 新聞：WebSearch 兩次搜尋，未找到當期散戶貼文或聲量數據。可用線索如下：
  - 4 月 IBD 報導提到 AXTI 單日大漲 19% 時成交量暴增，社群與論壇以「AI sleeper」形容。此為 4 月資料，不代表現在。
  - Simply Wall St 敘事（無日期）聚焦出口許可不確定性，認為市場可能已反映過於樂觀的情境。
- 聲量（buzz volume）：無法量化，無法與平常水準比較。
- 散戶傾向：**無法判定**（資料缺口）。

主要題材（依可取得來源歸納）：
1. 中國出口許可（export permit）與磷化銦、鎵、鍺等受管制材料的供應限制，是最常被提及的風險。
2. 業績後的估值與獲利能見度：11 月股價大跌，市場關心毛利率與出口許可能否持續。
3. AI 光通訊需求（磷化銦基板）帶來的成長敘事。

## Insider activity
統計區間：2026-05-16 至 2026-11-16（過去 6 個月）。金額來源為 yf insider 的 Value 欄位（USD）。

| 日期 | 內部人 | 職稱 | 類型 | 股數 | 金額（M USD） |
|---|---|---|---|---|---|
| 2026-06-02 | YOUNG MORRIS S | CEO | 公開市場賣出（直接持有） | 197,498 | 22.31 |
| 2026-06-15 | CHANG DAVID C | 董事 | 賣出 | 8,333 | 0.93 |
| 2026-06-15 | CHEN JESSE | 董事 | 賣出 | 6,172 | 0.71 |
| 2026-06-12 | CHEN JESSE | 董事 | 賣出 | 22,000 | 2.04 |
| 2026-06-10 | CHEN JESSE | 董事 | 賣出 | 16,500 | 1.48 |
| 2026-06-04 | CHEN JESSE | 董事 | 賣出 | 10,133 | 1.11 |
| 2026-06-02 | CHEN JESSE | 董事 | 賣出 | 5,200 | 0.58 |
| 2026-08-07 | LEBLANC LEONARD J | 董事 | 賣出 | 2,500 | 0.22 |
| 2026-08-17 | LEBLANC LEONARD J | 董事 | 賣出 | 4,000 | 0.38 |

- 買進：0 筆（區間內無公開市場買進；上一筆買進為 2025-02-25 CEO 買進 30,000 股，已超出區間）。
- 賣出合計：約 **US$29.8M**（約 M USD 29.77）。
- 淨額：**約 -US$29.8M**（淨賣出）。
- 排除項目（非市場買賣）：CEO 6/2 的選擇權行使 85,703 股（US$0.45M，行使價 5.21，與同日 197,498 股賣出分屬不同交易，未計入賣出金額）；CEO 與 CFO 的股票獎勵（Grant）與贈與（Gift，金額 0）；董事獎勵股。
- 重點：CEO Morris S. Young 6/2 賣出約 US$22.3M，為區間內最大單筆；CFO Gary L. Fischer 在區間內無交易紀錄（其最近賣出為 2026 年 3 月，已超出區間）。
- 限制：yf 最新內部人交易日期為 2026-08-17，8 月中至 11/16 之間無資料，可能有延遲揭露或工具覆蓋不全。是否屬 10b5-1 預定計畫無法從資料判定。

## Ownership shifts
- 內部人持股：7.21%（yf major_holders）。
- 機構持股：88.01%，佔流通股 94.85%；機構數 435 家。
- 趨勢：工具只回傳單一時點快照，無法判定機構持股的增減方向。MarketBeat 或 13F 資料可補足，本次未取得。

## Net sentiment score
**綜合：偏空（neutral-to-bearish），信心度低。**

依據：
- 分析師：偏多（5 buy / 1 hold / 0 sell，評級結構穩定，目標價區間 US$77.80 至 US$93 高於 11 月低點 US$40.42）。權重中等，因為共識標籤已由 Buy 轉為 Hold，且 yf 與 MarketBeat 數字不一致。
- 內部人：偏空（區間內僅賣出，無買進，CEO 單筆 US$22.3M）。權重高，但需考量可能為預定計畫。
- 散戶：無資料（Reddit、StockTwits 不可用）。
- 新聞面：偏空至中性（業績後大跌、出口許可不確定性）。

信心度低的原因：散戶面完全缺失，且分析師與共識標籤來源不一致。

**Divergence flag：是**（分析師偏多、內部人偏空）。散戶端因資料缺失無法判定是否與分析師反向。內部人與分析師方向相反，屬於值得注意的訊號，但內部人賣出可能與個人資產配置或預定計畫有關，不能單獨解讀為看空。

資料缺口與後續建議：
- 放行 api.stocktwits.com 後可補查 StockTwits 散戶情緒。
- Reddit 無法存取，可改用其他來源補查 r/stocks、r/investing 近期 AXTI 討論。
- 出口許可現況需以 AXT 最新 10-Q 或財報為準。WebSearch 顯示 2026 年 8 月有關於 11/10 中國出口管制暫停期限的報導，但未能確認後續結果，這一點對本檔判讀影響很大。

SENTIMENT REPORT COMPLETE
