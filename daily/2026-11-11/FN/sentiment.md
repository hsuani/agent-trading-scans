# Sentiment — FN as of 2026-11-11

資料完整度: 分析師與內部人資料可用; Reddit、StockTwits 無法取得 (Reddit 連線被拒, StockTwits 因網域無法解析而失敗); 散戶討論量與情緒只能以新聞面間接推估。分析師評級歷史變動工具回傳與 rec_summary 相同的靜態快照, 無法確認近期升降評等事件。

## Analyst consensus

| 評等 | 家數 |
|---|---|
| Strong Buy | 3 |
| Buy | 4 |
| Hold | 2 |
| Sell | 0 |
| Strong Sell | 0 |

合計 9 家, 7 家 Buy 或以上 (約 78%), 0 家 Sell。近 4 個月分佈完全相同, 顯示工具未提供評等變動歷史, 不代表評等沒有變化。

Recent moves (次級來源, 未經原始券商報告核實):
- Barclays 維持 Buy, 目標價 $496 (TIKR 2026-11-03 報導)。同文指出股價本月下跌約 32%, 目前約 17 倍 NTM 預期 EPS, 五年平均約 22 倍。
- MarketBeat (2026-10-28) 描述共識為 "Moderate Buy", 平均目標價 $631.88, 但提到近期多家下調目標價。
- 兩處目標價差距很大 ($496 對 $631.88), 且後者日期較早, 不宜直接比較。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 無法取得, 無樣本、無情緒比例。
- StockTwits: 無法取得 (api.stocktwits.com 無法解析, 需於 session 網路設定中放行)。
- X / 新聞討論 (WebSearch 替代): 找到的多為媒體與評論文章, 未見大量散戶貼文樣本。
  - 正面論述: 季度營收創紀錄 ($1.47B, 年增 51%, 以新聞所載為準), 分析師仍給予 Buy 與高目標價。
  - 負面論述: 估值偏高 (一篇文章稱約 44 倍 FY26E EPS, 為同業中位數兩倍以上), 標題為 "Fabrinet: I Would Sell" 的 Seeking Alpha 文章認為上漲空間已多數用完。
- 整體散戶傾向: 無法量化。以新聞與評論判斷, 討論偏向 "估值與 AI 光學股拋售" 的分歧, 不見一面倒。
- 聲量: 無法與平時基準比較 (缺 Reddit / StockTwits 數據)。
- 主要主題 (依新聞推估): AI 光學股因 AI 融資與超大規模雲端資本支出疑慮被拋售; 估值是否仍合理; 財報時點與指引。

## Insider activity

以 2026-05-11 至 2026-11-11 為 6 個月窗口, 以 Value 欄位 (USD) 計算:

| 日期 | 人員 | 職稱 | 交易 | 股數 | 金額 (M USD) |
|---|---|---|---|---|---|
| 2026-05-22 | BAHRAMI HOMA | Director | 賣出 @ 711.91 | 2,500 | 1.78 |
| 2026-09-03 | ARCHER EDWARD T | Officer | 賣出 @ 385.58–386.34 | 2,500 | 0.96 |

Net 6mo: $0.00M buys, $2.74M sells (公開市場買入為 0)。

其他非現金事件 (不計入買賣淨額): 2026-08-11 與 2026-08-20 的股票授予 (Stock Award, CEO GRADY SEAMUS、President GILL HARPAL S.、CFO SVERHA CSABA、ARCHER EDWARD T 等), 合計約 10 萬股量級, 屬例行薪酬授予。

Notable:
- 6 個月內沒有 CEO 或 CFO 的公開市場交易; CEO GRADY SEAMUS 最近一次賣出為 2025-11-26 (約 $10.0M), 已超出窗口。
- 窗口外的較大賣出: President GILL HARPAL S. (2025-09-04, 約 $5.0M); CFO SVERHA CSABA (2025-08-28, 約 $4.5M); Director KELLY THOMAS F. (2025-12-04, 約 $1.0M)。
- 資料品質注意: GILL HARPAL S. 在 2025-06-04 的交易職稱標為 "Chief Executive Officer", 其他列標為 "President", 職稱欄位可能有誤, 未經核實。

## Ownership shifts

- insidersPercentHeld: 0.00259 (內部人持股比例極低, 以原始小數解讀約 0.26%; 單位需確認)。
- institutionsPercentHeld: 1.01774 (約 101.8%, 超過 100%, 明顯為重複計算或單位問題, 不可直接採信)。
- institutionsCount: 1,010 家。
- 工具未提供季度持股變化趨勢, 無法判斷機構集中度是上升或下降。

## Net sentiment score

Composite: **中性偏多 (信心: 低)**

- 分析師面: 偏多 (7/9 Buy, 無 Sell), 但缺乏評等變動歷史, 且目標價來源不一致。
- 內部人面: 偏空至中性 (6 個月 $2.74M 賣出, 0 買入; 無 CEO/CFO 公開市場交易, 賣出金額相對前一年明顯縮小), 屬小幅訊號。
- 散戶面: 無法量化 (Reddit、StockTwits 不可取得)。
- 新聞面: 分歧 (近期營收新聞正面, 但股價一個月內下跌約 32%, 估值批評與 "I would sell" 論述並存)。
- 信心低的原因: 散戶資料缺失、評等無歷史變動資料、財報日期與目標價來源互相矛盾。

Divergence flag: **無法判定** — 缺乏可靠的散戶情緒資料, 無法確認散戶傾向是否與分析師傾向相反。

Data conflicts to note:
- 財報時點: TIKR 稱 2026-11-02 已公布 (營收 $1.47B), 但 Earnings Whispers 稱預計 2026-11-16 盤後公布。兩者不能同時成立, 需於後續階段核實。
- 目標價: Barclays $496 與 MarketBeat 平均 $631.88 差距約 27%, 來源與日期不同。
- 內部人股權比例 (0.26%) 與機構持股 (101.8%) 數值單位不一致, 僅供參考。

SENTIMENT REPORT COMPLETE
