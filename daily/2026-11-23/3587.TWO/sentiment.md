# Sentiment — 3587.TWO 閎康科技 as of 2026-11-23

資料覆蓋嚴重不足，以下結論可信度低。

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary / insider | 回傳空陣列 `[]`，Yahoo 端點被 proxy 403 拒絕（guce / fc / query1,2.finance.yahoo.com），非「無交易」而是「無資料」 |
| yf major_holders | 成功，但只有單一快照，無歷史趨勢 |
| Reddit r/wallstreetbets、r/stocks | WebFetch 被拒（無法連線 www.reddit.com），無法取得 |
| StockTwits | DNS 解析失敗（api.stocktwits.com 不在允許網域內），需在 session 網路設定中允許後才能重試 |
| WebSearch（中文/英文） | 有零星資料，無 2026 年 11 月的散戶討論 |

## Analyst consensus

依 Investing.com 彙整頁（日期不明）：3 位分析師，共識「買入」（3 buy / 0 hold / 0 sell，僅能視為參考）。12 個月平均目標價約 365.67 TWD，區間 300–450 TWD。同頁另一版本股價約 249.5 TWD。52 週區間約 178–399 TWD。

- 最近一次財報（2026-05-19 公布）EPS 2.24 TWD（來源未標示是哪一季）。
- 聯合報報導估計 2026 年 EPS 有機會上看 12 TWD，本益比約 18 倍（文章日期不明）。
- 另一估值頁顯示本益比約 34.7 倍、股價淨值比約 2.76 倍。兩者估值差距大，需以實際財報重算。
- 無法確認 2026 年 11 月內是否有個別券商升降評等或調整目標價。

## Retail social

- **Reddit**：無法取得。Reddit 端點被拒，無法給出討論量或多空傾向。
- **StockTwits / X**：StockTwits 無法連線。X 無可用結果。
- **Buzz 量**：無法量化。
- **可用的 news 與媒體面**：2026-08-04 報導閎康宣布處分中國子公司 80% 股權後，股價連續兩日漲停，法人認為資源將轉向日本與美國市場。另有媒體提到閎康曾被列為注意股，並以 TEM 原子級解析、先進製程（台積電 2nm、Rapidus）與矽光子作為題材。
- **Themes（來自媒體而非散戶）**：先進製程failure analysis 需求、海外布局、AI 晶片分析題材、估值偏高與股價波動大。

## Insider activity

yf insider 無資料（Yahoo 端點被拒），**無法判斷 6 個月內的淨買賣金額與買賣人身分**。目前只能看到持股結構：

## Ownership shifts

依 yf major_holders（單一快照）：內部人持股 27.2%，機構持股 8.5%（占流通股約 11.7%），機構家數 16 家。沒有前後期比較，無法判斷集中度趨勢。

另有一則 Goodinfo 片段提到 11/17 外資買超約 68 張、投信無買賣、自營商買超 1 張。內容格式破碎，只能視為未驗證數字。

## Net sentiment score

**Composite: neutral（信心：低）**

- 分析師面：偏多（3 買，但資料日期不明，平均目標價高於多數來源的股價）。
- 散戶面：無資料。
- 內部人面：無資料。
- 媒體面：近期偏正面（處分中國子公司、先進製程與海外題材），但估值與波動風險並存。

**Divergence flag: 無法判斷**（缺少散戶資料，無法比較與分析師的傾向是否相反）。

## 資料品質警示

1. WebSearch 曾回傳同名但不同公司的資料（6515 穎崴科技），已全部排除，未納入本報告。
2. 多數 Investing.com、Goodinfo 數字日期不明，不可視為 2026 年 11 月的即時資料。
3. 本報告未包含市值金額，因此無需 億 / B 換算。目標價與股價皆為 TWD/股。

SENTIMENT REPORT COMPLETE
