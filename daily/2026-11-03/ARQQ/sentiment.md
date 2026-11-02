# Sentiment — ARQQ as of 2026-11-03

資料截止注意: 執行日為 2026-11-02, 報告依指定日期 2026-11-03 標示。內部交易資料最新一筆為 2026-10-16。

## Analyst consensus
**無法取得。** `pipeline/tools/yf ARQQ recommendations` 與 `rec_summary` 皆回傳空陣列, 原因是 cookie/crumb 取得失敗。代理伺服器日誌顯示 `query2.finance.yahoo.com:443` 遭 403 CONNECT 拒絕 (policy denial), 屬於代理政策層級阻擋, 本次未嘗試繞過。
- 買進 / 持有 / 賣出分布: N/A
- 近期升降評與目標價變動: N/A
- 可得的持股結構 (yf `major_holders`, 可正常回傳):

| 指標 | 數值 |
|---|---|
| 機構持股比例 (institutionsPercentHeld) | 82.6% |
| 機構持股占浮動股比例 (institutionsFloatPercentHeld) | 85.0% |
| 機構持有家數 (institutionsCount) | 93 |
| 內部人持股比例 (insidersPercentHeld) | 2.8% |

持股趨勢需要多期快照比較, 目前只有單期資料, 無法判斷機構集中度是上升或下降。

## Retail social
- **Reddit (r/wallstreetbets, r/stocks)**: 本次未取得資料。WebSearch 未索引到相關討論串, 檢索結果多為自動生成的股價頁面。依任務規定, 未對 Reddit 直接發出 WebFetch。
- **StockTwits / X**: 同樣無可用資料。WebSearch 只找到 TradingView 的一則 idea 頁面, 不具代表性。
- **聲量 (mention volume)**: 無法量化, 與常態比較無依據。
- **多空傾向**: 無法判定。
- **主要題材**: 無可靠樣本, 無法歸納。

WebSearch 找到的股價頁面品質低、日期互相矛盾 (2026-04-07 約 $12.55; 2026-05-27 約 $16.10; 2026-07-31 頁面標示一年期跌幅 -45.6%), 不作為情緒依據。

## Insider activity
資料區間: 2026-05-02 至 2026-11-02 (近 6 個月)。金額單位: USD M。

**淨額 (6 個月)**: 公開市場賣出約 **$2.68M**; 公開市場買進 **$0**。

| 內部人 | 職稱 | 交易日 | 股數 | 均價 (USD) | 金額 (USD M) |
|---|---|---|---|---|---|
| LEFEBVRE D'OVIDIO MANFREDI | Director (間接持有) | 2026-07-01 | 54,444 | 30.07–30.24 | 1.64 |
| LEAVER ANDREW | CEO | 2026-07-02 | 9,893 | 25.20 | 0.25 |
| LEAVER ANDREW | CEO | 2026-10-02 / 05 / 06 / 13 | 10,324 | 23.78–24.47 (10-13 為 16.40) | 0.23 |
| BERS JENNIFER | Officer | 2026-06-22 | 8,288 | 21.42 | 0.18 |
| WILLCOCKS PATRICK | General Counsel | 2026-06-30, 07-02, 10-02/05/06 | 約 8,300 | 25.20–29.48 | 0.21 |
| FEENAN PAUL | Officer | 2026-07-02, 10-02/05/06 | 約 5,100 | 約 24–25 | 0.08 |
| NILAN NICHOLAS WILLIAM | Officer | 2026-10-02/05/06 | 約 1,500 | 約 24 | 0.04 |
| WILDER BEN SIMON | COO | 2026-07-02, 10-02/05/06 | 約 1,800 | 約 24–25 | 0.04 |
| RITCHIE GARTH | Director | 2026-07-02, 10-02/05/06 | 約 1,000 | 約 24–25 | 0.02 |

**重點觀察**:
- 公開市場賣出高度集中於 CEO、General Counsel、Officer 等管理層, 包括 2026-10-02、10-05、10-06 三個交易日的多人同步小額賣出。金額與股數結構相近, 符合預先排程賣出 (10b5-1) 的特徵, 但資料本身無法確認是否為計畫性交易。
- 最大單筆為 Director LEFEBVRE D'OVIDIO MANFREDI 間接持有的賣出, 2026-07-01 約 $1.64M, 占區間賣出總額約六成。
- 價格脈絡: 2026-04 CEO 與 CFO 的賣出價約 $13–16 (區間外); 2026-07 約 $25–30; 2026-10 約 $24。內部人在 7 月高點與 10 月反彈時段持續賣出。
- **不列入賣出的項目**: 三筆選擇權行權 (conversion) 不屬於買進, 包括 2026-06-03 CALABRIA CARLO (120,000 股, 行權價 $2.50)、2026-06-05 RITCHIE GARTH (73,562 股)、2026-09-22 LEFEBVRE D'OVIDIO MANFREDI 間接持有 (4.6M 股, 工具欄位顯示金額 $11.5M, 即行權價 × 股數, 非實際現金流)。2026-09-22 的行權後是否賣出, 資料中未見對應紀錄。
- 另有 2026-10-01 至 10-16 多筆無價格、無金額的小額 "D" 紀錄, 性質不明 (可能為非現金交易), 未計入。

## Ownership shifts
- 機構持股 82.6%, 機構數 93 家, 內部人 2.8%。
- 無歷史快照, 無法判斷趨勢。
- 持股結構本身不顯示明顯集中風險, 但單一間接持股的董事 (LEFEBVRE D'OVIDIO MANFREDI) 在區間內兼具大量行權與賣出, 值得在後續追蹤。

## Net sentiment score
**綜合判定: 偏空 (bearish-leaning), 信心: 低。**

- 內部人面: 偏空。6 個月內零公開市場買進, 有持續性賣出, 且賣出集中於管理層與一名董事的大額間接持股。
- 散戶面: 無資料, 無法評分。
- 分析師面: 無資料, 無法評分。
- 信心偏低的原因: 兩個主要來源 (analyst ratings 與 retail social) 皆無法取得, 綜合判定只能依內部人交易單一來源。

**背離旗標 (divergence flag)**: **無法判定。** 缺乏分析師與散戶資料, 無法比較兩者傾向是否相反。

**待補資料**:
1. Yahoo Finance 相關端點恢復後重新抓取 `recommendations` 與 `rec_summary`。
2. 在可用環境下補抓 Reddit `r/wallstreetbets` 與 `r/stocks` 搜尋結果, 以及 StockTwits 串流。
3. 追蹤 LEFEBVRE D'OVIDIO MANFREDI 2026-09-22 大額行權後的後續交易。

SENTIMENT REPORT COMPLETE
