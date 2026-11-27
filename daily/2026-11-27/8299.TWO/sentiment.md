# Sentiment — 8299.TWO (群聯 Phison) as of 2026-11-27

## 資料限制
- Reddit (r/wallstreetbets, r/stocks): WebFetch 被拒 ("unable to fetch")，無資料。台股本身與此來源相關性就低。
- StockTwits: api.stocktwits.com DNS 解析失敗，需於 session 網路設定允許該網域後才能重試。
- yf insider: 回傳空陣列，無資料。
- PTT Stock 板: 搜尋未找到 2026 年 11 月的討論原文。
- 新聞類內容取自搜尋摘要，未逐篇開啟原文。

## Analyst consensus
yf rec_summary (0m, 13 家): Strong Buy 4 / Buy 7 / Hold 0 / Sell 2 / Strong Sell 0。買進類 11/13 (約 85%)。
前三期 (-1m 至 -3m) 皆為 4/7/1/1，最近一期 Hold 由 1 降為 0，Sell 由 1 升為 2，即一家券商由中性轉向賣出 (yf 未標示券商名稱)。

近期評等與目標價變動 (新聞摘要，11 月初至 11/9):

| 券商 | 動作 | 目標價 (TWD) |
|---|---|---|
| 外資 | 調降至減碼 (Underweight) | 2,588 → 1,357 (-48%)，報導稱部分來自估值模型計算錯誤 |
| 統一投顧 | 買進 → 中立 | 未提供 |
| 凱基投顧 | 維持增加持股 | 2,900 → 2,700 (-6.9%) |
| 永豐投顧 | 維持買進 | 2,998 → 2,070 (-31%) |
| 中信、國票 | 目標價下修逾 30% | 未細列 |

較早正面案例：9 月下旬某投顧目標價 2,750 → 2,900，評等增加持股。Macquarie 10/13 維持 2,564 (單一搜尋摘要)。Investing.com 顯示的平均目標價約 2,977 為過時快照，與近期下修不一致，不採用。

解讀：評等數量仍偏多，但目標價大幅下修，評等與目標價之間的分歧擴大。

## Retail social
- Reddit: 無法存取。
- StockTwits: 無法存取。
- PTT Stock 板: 找到的是 2025 年 12 月的新聞轉貼，留言有喊漲與反向酸言，時間過舊，不計入當期判斷。
- 新聞與 X 類敘事: 11/9 Q3 財報與庫藏股公告後股價漲停 (報導)。但同日大盤自跌破 4 萬大幅反彈，漲停部分與大盤及記憶體族群連動，無法分離個股情緒。
- 討論量: 無法量化。新聞曝光在 11 月高於平常，社群討論量無資料。
- 散戶傾向: 無法判定 (低信心)。

主要主題 (取自新聞):
- 多方: Q3 EPS 約 138 元創高，Q3 營收約 860.76 億 TWD，毛利率約 59.7%；董事會通過買回 2,000 張庫藏股 (11/6 至 2027/1/5，轉讓員工)；管理層預期 NAND 供給偏緊至 2027。
- 空方: 毛利率較前季回落，外資認為 Q3 毛利率 59% 低於市場預期 60.3%；NAND 漲勢趨緩；部分研調預估 2027 下半年可能供過於求；外資目標價下修。

## Insider activity
- 6 個月窗口 (2026-05-27 至 2026-11-27): 買進 0 億 / 賣出 0 億 TWD，但這是「未找到公開報導」，不等於確定為零 (yf 無資料)。
- 非董監事交易，不計入內部人情緒:
  - 2,000 張庫藏股買回 (公司層級，2026/11/6 起)。報導金額 45.6 億 TWD，但以張數 × 約 1,650 TWD 推算約 33 億，金額不一致，未能核實。
  - 宇瞻 (8271) 股票處分 (2026/05)，為公司持有子公司股票。
- 超出窗口的 CEO 紀錄 (僅供參考):
  - 潘健成 2026/01 贈與 102 張予 3 名子女，報導稱為家族贈與，非出售。
  - 潘健成 2025/12 增持約 4 萬股。

## Ownership
yf major_holders (單一快照): 內部人持股 15.83%，機構持股 20.67% (流通股比 24.56%)，機構家數 182。無時間序列，無法判斷集中度趨勢。

## Net sentiment score
- 分析師面: 偏中性偏多。評等多數仍為買進類，但目標價大幅下修，且近期有一家轉為賣出。信心: 中。
- 散戶面: 無法量化。新聞敘事偏多 (財報與買回)。信心: 低。
- 內部人面: 無可查交易，無法判斷。公司層級買回屬正向訊號，但不是內部人交易。信心: 低。
- **Composite: neutral (信心: 低)**。主要受資料缺口影響。

Divergence flag: **無法判定**。散戶資料缺失，無法與分析師比較。分析師內部存在分歧：評等偏多但目標價與近期評等偏空。

## 資料衝突注意
1. 外資目標價下修部分來自模型錯誤修正，並非純基本面轉弱。
2. 股價來源互相矛盾: MarketScreener 11/11 為 1,730 TWD，Investing.com 11/7 為 1,500 TWD，報導 11/9 漲停至 1,650 TWD。未採用。
3. 買回金額 45.6 億與張數推算不符 (約 33 億)。
4. yf 顯示 Hold 減 1，但新聞稱統一由買進降為中立，方向上應增加 Hold。yf 資料可能落後或統計口徑不同。
5. 2026/11 月營收 (年增 62%) 報導可能晚於 2026-11-27 發布，依指示視為未知，不採用。

## 來源 (搜尋摘要，未逐篇開啟)
- https://wantrich.chinatimes.com/news/20261111900103-420101
- https://wantrich.chinatimes.com/news/20261109900160-420101
- https://wantrich.chinatimes.com/news/20261109900002-420101
- https://wantrich.chinatimes.com/news/20261111900384-420101
- https://statementdog.com/news/18015
- https://finance.technews.tw/2026/11/09/phisons-third-quarter-gross-margin-declined-as-low-priced-inventory-ran-out/
- https://finance.technews.tw/2026/11/06/phison-releases-third-quarter-financial-results-and-october-revenue/
- https://www.nasdaq.com/articles/phison-electronics-tpex-8299-price-target-increased-2488-110466
- https://ca.marketscreener.com/index.php/quote/stock/PHISON-ELECTRONICS-CORP-6497570/

SENTIMENT REPORT COMPLETE
