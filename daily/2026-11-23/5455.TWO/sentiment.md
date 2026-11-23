# Sentiment — 5455.TWO (英特磊) as of 2026-11-23

**重要警示: 股票代號可能有誤。** 本次所有工具都回傳空值, 而網路搜尋結果把英特磊 (IntelliEPI / IET-KY) 對應到代號 4971, 而非 5455。搜尋頁面上的 5455 只出現在五檔報價中, 不是該公司的代號 ([鉅亨網 4971 頁面](https://www.cnyes.com/twstock/4971))。請先確認代號, 再解讀本報告。下列空值可能是代號錯誤造成, 不一定代表該股沒有覆蓋。

## Analyst consensus
- 0 buy / 0 hold / 0 sell。`rec_summary` 與 `recommendations` 皆回傳空陣列。
- 近期升降評與目標價變動: 無資料。
- 網路搜尋未找到 2026 年 11 月的評等或目標價。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 抓取失敗 (`www.reddit.com` 無法存取), 無資料。
- StockTwits: 抓取失敗 (`api.stocktwits.com` DNS 無法解析)。需要在工作階段網路設定中允許此網域, 才能重試。
- X / 新聞: 搜尋結果沒有 2026 年的討論。最新可見資料約為 2025 年底, 內容如下:
  - 營收創高、股價漲停並創歷史新高 ([uanalyze 焦點股](https://uanalyze.com.tw/articles/6595341786))。
  - 外資連續買超 ([uanalyze](https://uanalyze.com.tw/articles/7321543358))。
  - 磷化銦 (InP) 產品被視為明年成長主力, 業績有望翻倍 ([Yahoo 股市](https://tw.stock.yahoo.com/news/))。
  - 美國政府停擺可能使 CHIPS 法案補助與審查延後 3 至 6 個月。
  - 與光聖 (6442) 的股份交換, 用以加深 CPO 與矽光子合作。
  - 曾被列為處置股, 期限至 2026 年 1 月 6 日。
- 注意: 這些資料都早於 2026 年 11 月, 不能代表現在的情緒。
- 聲量 (相對常態): 無法判斷。
- 主要主題 (僅限 2025 年底資料): 磷化銦成長、CPO / 矽光子、外資買盤、高檔震盪風險。

## Insider activity
- 6 個月淨買賣: 無資料 (`insider` 回傳空陣列)。
- 無法確認 CEO、CFO 或其他董監事的交易。

## Ownership shifts
- `major_holders`: 內部人持股約 70.3%。
- 法人持股與法人家數顯示 0, 這很可能是資料源缺漏, 不是實際數字。法人持股趨勢: 無法判斷。

## Net sentiment score
- Composite: **neutral (信心低)**。原因是分析師、散戶、內部人三方面皆無 2026 年資料, 且代號有疑慮。
- Divergence flag: **無法判定**。沒有分析師傾向可供比較。

## 資料缺口與後續
1. 先確認代號是 5455 還是 4971 (英特磊), 並確認台灣交易所或櫃買中心上的正確掛牌。
2. 在工作階段網路設定中允許 `www.reddit.com` 與 `api.stocktwits.com`。
3. 確認 `yf` 工具是否支援台灣櫃買 (.TWO) 代號的分析師資料。
4. 補查 2026 年的法人評等、外資買賣超與營收公告, 再重跑本報告。

SENTIMENT REPORT COMPLETE
