# Sentiment — 000660.KS (SK hynix) as of 2026-11-18

資料狀態總覽：分析師評等來自 yf（cookie/crumb 失敗後仍回傳資料，屬快取/降級路徑）。Reddit 與 X 社群內容無法取得，StockTwits 無法解析網域，內部人交易回傳空陣列，視為 DATA_UNAVAILABLE。

## Analyst consensus

截至 yf rec_summary（0m）：**41 家券商 = 12 Strong Buy / 28 Buy / 1 Hold / 0 Sell / 0 Strong Sell**，買進評等占 97.6%。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（目前） | 12 | 28 | 1 | 0 | 0 |
| -1m | 12 | 28 | 1 | 0 | 0 |
| -2m | 11 | 28 | 1 | 0 | 0 |
| -3m | 11 | 27 | 1 | 0 | 0 |

近三個月評等結構幾乎沒變，Strong Buy 由 11 增至 12，Buy 由 27 增至 28，沒有任何 Sell 評等。

- 評等變動明細（upgrade / downgrade 日期與機構）：DATA_UNAVAILABLE。`recommendations` 指令回傳的仍是同一組月度彙總，並非個別評等變動紀錄。
- 目標價變動：DATA_UNAVAILABLE（yf 未回傳）。WebSearch 找到的目標價數字來源時間偏早或互相矛盾，未採用：StockAnalysis 標示資料日期為 2026-06-05，平均目標價約 208 萬韓元/股；Edaily 報導 Hanwha 於 6 月將目標價調至 430 萬韓元/股，該數字與平均值差距過大，未能驗證。
- 市場報導中的股價水準（非 yf 來源，僅供參考）：11 月 6 日收盤約 118.2 萬韓元/股，盤中低點約 108.9 萬韓元/股；11 月初一週內約下跌 23.1%。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：DATA_UNAVAILABLE。WebFetch 對 www.reddit.com 回報無法存取，本次未取得任何貼文樣本，因此無法給出討論聲量與多空傾向。
- **StockTwits**：DATA_UNAVAILABLE。api.stocktwits.com 無法解析，目前網路設定未允許該網域。
- **X / 韓國社群（종목토론방等）**：未取得。WebSearch 只找到證券與媒體文章，沒有可引用的社群貼文。
- **聲量相對基準**：DATA_UNAVAILABLE，無法判斷相對於平常的水準。
- **多空傾向**：無法判定（DATA_UNAVAILABLE）。
- **媒體敘事（代理指標，非散戶情緒直接量測）**：近期報導主軸是「基本面與情緒面背離」。報導指出公司有創紀錄季報與大規模股東回饋，但股價仍大幅下跌，部分文章將其歸因於情緒性賣壓。此為媒體觀察，不能視為散戶多空結論。
- **主要主題（來自新聞/媒體，非社群直接取得）**：
  - 記憶體供需：KB 證券認為供給增幅有限、需求快速成長，缺貨可能比 2026 年更嚴重。
  - 長期合約：報導稱 2027、2028 年產能約過半已與大客戶簽署長期協議（數字來自二手報導，未經原始公告核對）。
  - ADR / 那斯達克掛牌：BNK 投資證券認為 ADR 上市後本股重估空間有限。
  - 股東回饋：報導提及年度回饋規模約 40 兆韓元（約 400,000 億韓元）的自家股買回與註銷，未經原始公告核對。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。`insider` 指令回傳空陣列，無法區分「確實無交易」與「資料源遺漏」，因此不視為零交易。未取得 CEO / CFO 或其他董監事的買賣紀錄。若需判斷，應改查韓國金融監督院 DART 電子申報系統的內部人持股變動公告。

## Ownership shifts

yf major_holders 單一快照（無時間序列，趨勢 DATA_UNAVAILABLE）：

| 指標 | 數值 |
|---|---|
| 內部人持股比例 | 20.17% |
| 機構持股比例 | 38.79% |
| 機構占流通股比例 | 48.59% |
| 機構家數 | 735 |

機構持股集中度目前屬中等水準，但缺少前後期比較，無法判斷是增持或減持。

## Net sentiment score

**綜合：偏多（信心：低）**

- 分析師面：偏多（信心：高）。41 家中 40 家為 Buy 或 Strong Buy，且近三個月未見降評，評等結構穩定。
- 散戶面：無法判定（DATA_UNAVAILABLE），無社群樣本可用。
- 內部人面：無法判定（DATA_UNAVAILABLE）。
- 股東結構：中性，僅有單一快照。
- 綜合信心偏低，原因是散戶與內部人兩個維度缺資料，且分析師評等在某些期間與近期股價走勢明顯背離，無法單靠評等判斷市場共識。

**背離旗標：無法判定（DATA_UNAVAILABLE）**。分析師端偏多，散戶端無資料，因此不能確認是否出現方向相反的背離。

資料限制摘要：
- Reddit、StockTwits、X 社群：未取得。
- 評等變動明細、目標價歷史：未取得。
- 內部人交易：yf 回傳空陣列，視為 DATA_UNAVAILABLE。
- 股東持股趨勢：只有單期快照。
- 媒體來源時效：多數文章早於 11 月，未找到權威性的 2026 年 11 月共識報告。

本報告僅描述市場情緒與分析師評等，不提供交易建議。

SENTIMENT REPORT COMPLETE
