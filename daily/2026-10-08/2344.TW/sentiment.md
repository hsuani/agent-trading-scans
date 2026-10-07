# Sentiment — 2344.TW 華邦電電子 (Winbond Electronics) as of 2026-10-08

資料時點聲明：yf 工具的 live 呼叫因 cookie/crumb 取得失敗，實際回傳內容來自 repo 快取 `prices/yf/2344.TW.json`（`_refreshed_at` = 2026-10-07T13:08:58Z）。Reddit 與 StockTwits 無法連線，CMoney 亦被 egress proxy 阻擋。網路新聞搜尋結果最新僅到 2026-08 中旬，未找到 9 月、10 月的法人評等或股價資料。以下數字均未沿用過去 daily 目錄的數值。

## Analyst consensus

yf `rec_summary` / `recommendations`（0m 期間）：strongBuy 4、buy 4、hold 0、sell 0、strongSell 0，合計 8 家，買進側 100%。

評等變化（與 -3m 比較）：覆蓋家數由 6 家增至 8 家；hold 由 1 家降為 0；買進側（strongBuy + buy）由 5 家增至 8 家。-2m 為 7 家，-1m 與 0m 均為 8 家，變化主要發生在 -3m 至 -2m 之間。

目標價（yf 無此欄位，以下來自網路新聞，未能交叉驗證）：
- 本土券商（2026-08-18）：維持買進，目標價 218 元（新聞搜尋彙整，原始出處未逐一核對）。
- 官股投顧（2026-07-26）：強力買進，目標價由 200 元上調至 285 元（依 2 年平均 EPS 63.26 元、4.5 倍本益比推算）。
- 摩根大通（2026-06-15）：加碼，目標價 255 元。英文搜尋結果另有一筆 7 月中旬 JPM 目標價 360 元的摘要，與此不一致，未採用。
- 摩根士丹利（2026-05）：中立，目標價 100 元，理由是股價上漲空間可能受限。為目前已知唯一明確偏保守的外資。
- 基本面背景：2026 年第 2 季合併營收 598.43 億元（季增 56.4%、年增 184.7%），第 2 季 EPS 5.4 元，財報後股價反跌，8/7 開盤約下挫 3% 至 166 元。法人表示報價基期已高、下半年漲幅可能不及上半年，但目標價仍維持 200 元以上。

## Institutional flow

yf `major_holders`（單一時點快照，無時間序列）：
- insidersPercentHeld：30.26%
- institutionsPercentHeld：24.61%（占流通股 35.28%）
- institutionsCount：196 家

機構持股的「集中度趨勢」無法由現有資料判定（缺少歷史快照）。yf `inst_holders` 快取為空。外資買賣超日資料本次未取得。

## Insider activity

yf `insider` 回傳空陣列。這可能代表近 6 個月無申報交易，也可能是資料源缺漏，目前無法區分。Net 6mo：資料不足，不宣告為零。台灣董監持股申報（MOPS）本次無法存取，建議後續補查。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 搜尋皆因 WebFetch 無法連線而失敗（403/連線阻擋），未取得樣本。
- StockTwits：api.stocktwits.com 被 egress proxy 阻擋（EGRESS_BLOCKED），未取得訊息流。
- CMoney 股市爆料/討論區：本次 WebFetch 被阻擋；僅能從搜尋摘要得知，討論呈分歧，部分投資人擔心波動，另一部分期待外資買超後反彈，有聲音指出悲觀情緒擴散。此為自動摘要，權重低。
- 新聞與散戶投票：Investing.com 使用者投票（「2344 股價會漲或跌」）近期多數選項為看跌，樣本少且為自選，僅供參考。
- 聲量（buzz volume）：無法量化，無法與歷史基準比較，標記為「未能評估」。
- 相關新聞報導：多篇 7 月底至 8 月中旬的新聞提到「股價連日走弱、部分投資人調節持股、對法人目標價保留態度」，與分析師側的積極評等形成對照。

主要討論主題（依搜尋結果整理）：
1. 利基型 DRAM 與 SLC NAND 供需吃緊、記憶體價格上漲（看多主軸）。
2. 矽電容（silicon capacitor）預計 2027 年上半年量產，被視為第三成長動能（看多）。
3. 高基期與估值疑慮，認為下半年漲幅可能不如上半年（看空或保守）。
4. 法人目標價偏高、散戶質疑（保守）。

代表性觀點（引述不超過 15 字，來源為新聞彙整，非原始貼文）：
- 「股價連日走弱，部分投資人信心動搖並陸續調節持股」（新聞描述）。

## Net sentiment score

- 分析師側：偏多（8/8 買進側，目標價區間 200 至 285 元，唯一中立評等為大摩 100 元）。信心：中（評等數據來自快取，目標價資料多停留在 8 月中旬）。
- 散戶側：中性偏謹慎。信心：低（Reddit、StockTwits 皆無法取得，僅有新聞彙整與小樣本投票）。
- 內部人側：無資料。信心：無。
- 機構側：持股比例穩定但無趨勢資料，無法判斷方向。

Composite：偏多（中等偏低信心）。主要依據是分析師評等一致偏多，散戶端證據不足以抵消。

Divergence flag：有限度是（弱訊號）。分析師評等積極，散戶與新聞側轉為謹慎，但散戶樣本只有新聞彙整與小樣本投票，不足以構成可靠的分歧判斷。若取得 Reddit 或 StockTwits 資料後，應重新評估此旗標。

## 資料缺口與後續建議

1. 9 月、10 月的法人評等與目標價調整未取得，需以 MoneyDJ、公開資訊觀測站或券商報告補查。
2. 內部人申報（董監持股增減）需查 MOPS，yf 空陣列不足以作為結論。
3. Reddit 與 StockTwits 在本環境無法存取，散戶訊號目前不完整。
4. 機構持股趨勢需要至少兩個時點的快照才能判斷方向。

## Metrics table

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 買進側評等（strongBuy + buy，0m） | 8 家 | yf rec_summary（快取，2026-10-07 刷新） |
| 持有 / 賣出 | 0 / 0 | 同上 |
| 覆蓋家數變化（-3m → 0m） | 6 → 8 | yf recommendations |
| 買進比例（0m） | 100% | 計算值 |
| 目標價區間（網路新聞） | 100（大摩中立）至 285 元 | 新聞彙整，8 月中旬為最新，未驗證 |
| 本土券商目標價（2026-08-18） | 218 元 | 新聞 |
| 內部人 6 個月淨買賣 | 無資料 | yf insider 回傳空陣列 |
| insidersPercentHeld | 30.26% | yf major_holders 快照 |
| institutionsPercentHeld | 24.61% | yf major_holders 快照 |
| institutionsFloatPercentHeld | 35.28% | yf major_holders 快照 |
| institutionsCount | 196 | yf major_holders 快照 |
| Reddit 樣本 | 無法存取 | WebFetch 失敗 |
| StockTwits 樣本 | 無法存取 | EGRESS_BLOCKED |
| 散戶傾向 | 中性偏謹慎（低信心） | 新聞彙整、Investing.com 小樣本投票 |
| 聲量（buzz volume） | 未能評估 | 無歷史基準 |
| 綜合情緒 | 偏多（中等偏低信心） | 分析師主導 |
| 分歧旗標 | 有限度是（弱） | 散戶證據不足 |

## Sources

- [Winbond 2344 consensus (Investing.com)](https://www.investing.com/equities/winbond-consensus-estimates)
- [valueinvesting.io 2344.TW estimates](https://valueinvesting.io/2344.TW/estimates)
- [Simply Wall St Winbond](https://simplywall.st/stocks/tw/semiconductors/twse-2344/winbond-electronics-shares)
- [CMoney 2344 討論區](https://www.cmoney.tw/follow/channel/stock-2344)
- [技術新報 外資關注華邦電營運](https://finance.technews.tw/2026/05/06/foreign-investors-are-watching-winbond-electronics-operations/)
- [UDN 小摩目標價（新聞）](https://money.udn.com/money/amp/story/5607/9239425)
- [SETN 跌慘了也不降評 華邦電目標價](https://www.setn.com/news/1881355)
- [CTEE 2026-06-15 報導](https://www.ctee.com.tw/news/20260615700736-430201)

SENTIMENT REPORT COMPLETE
