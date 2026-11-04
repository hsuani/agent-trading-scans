# Sentiment — 5475.TWO (德宏) as of 2026-11-05

> 資料時效注意：執行日為 2026-11-04，報告基準日為 2026-11-05（尚未收盤）。本報告所有資料皆為基準日之前已公開者，最新可查到的價格與新聞約為 2026-10-20 前後，無 2026-11 月內之資料。

## 資料來源狀態

| 來源 | 狀態 | 說明 |
|---|---|---|
| Reddit (r/wallstreetbets, r/stocks) | DATA_UNAVAILABLE | 本沙箱封鎖 reddit.com，依指示未重試 |
| StockTwits | DATA_UNAVAILABLE | 本沙箱封鎖，依指示未重試 |
| yfinance 分析師評等 (rec_summary) | DATA_UNAVAILABLE | yf 工具 cookie/crumb 取得失敗，回傳空陣列 |
| yfinance 評等歷史 (recommendations) | DATA_UNAVAILABLE | 同上，回傳空陣列 |
| yfinance 內部人交易 (insider) | DATA_UNAVAILABLE | 同上，回傳空陣列 |
| yfinance 大股東 (major_holders) | 部分可用 | 取得持股結構，見下文 |
| WebSearch 新聞與報導 | 部分可用 | 新聞與媒體報導可查，未找到券商目標價 |
| 散戶論壇 (PTT / Dcard / 股市社群) | DATA_UNAVAILABLE | 搜尋未回傳相關討論內容 |

## Analyst consensus

- 買進 / 持有 / 賣出分布：DATA_UNAVAILABLE（yf rec_summary 無資料，WebSearch 未找到券商評等彙整）
- 近期升降評等：DATA_UNAVAILABLE
- 目標價變動：DATA_UNAVAILABLE（搜尋結果僅提示「需查券商研究報告」，未取得具體目標價）

補充：媒體報導中多次提及產業景氣回溫，但並非券商評等，不計入共識統計。

## Retail social

- Reddit：DATA_UNAVAILABLE（沙箱封鎖）
- StockTwits / X：StockTwits DATA_UNAVAILABLE（沙箱封鎖）；X 無可用搜尋結果
- 媒體與新聞情緒（替代指標）：近期報導偏多方。報導標題多以「漲停」「缺貨」「創新高」描述，例如 2026 年 10 月 20 日盤中漲停 228.5 元（漲幅約 9.86%）。
- 散戶論壇討論量：DATA_UNAVAILABLE，無法估算提及次數相對於平常的倍數。

### 主要主題（依媒體報導歸納）

1. 玻纖布供需缺口：中國 CCL 大廠（建滔等）多次調價，業界預期缺口可能延續至 2027 年。
2. 獲利回升：2026 年前 9 月累計營收約 16.42 億元，年增約 176.92%；9 月單月營收約 3.24 億元，年增約 227.61%；9 月單月歸屬母公司淨利約 1.24 億元，EPS 約 0.97 元。
3. 毛利率回升：2026 年上半年毛利率約 33.43%，其中第二季單季約 36.62%。
4. AI 題材：布局石英纖維布（Q 布），應用於 AI 高速傳輸。
5. 銅價與產業政策：報導提及銅價上漲與中國「反內捲」政策。

注意：上述數字取自媒體轉述，未經公開資訊觀測站核對。以 9 月淨利 1.24 億元與 EPS 0.97 元反推，約對應 1.28 億股，屬合理範圍，但仍建議以 MOPS 申報數字為準。

## Insider activity

Net 6mo：DATA_UNAVAILABLE（yf insider 無資料）。

- 公開資訊觀測站 (MOPS) 董監申報轉讓資料未在搜尋結果中取得。
- 玩股網資料顯示董監持股比例 2026 年 5 月至 7 月維持 10.17%，無明顯增減；資料僅到 7 月，之後變化無法確認。
- Notable：DATA_UNAVAILABLE

## Ownership shifts

來源：yfinance major_holders（僅提供彙總值）

| 指標 | 數值 |
|---|---|
| 內部人持股比例 (insidersPercentHeld) | 27.93% |
| 機構持股比例 (institutionsPercentHeld) | 2.73% |
| 機構佔流通股比例 (institutionsFloatPercentHeld) | 3.78% |
| 機構數量 (institutionsCount) | 7 |

- 解讀：內部人（含大股東）佔比高，機構持股比例偏低，流通股的機構覆蓋度有限。
- 趨勢：DATA_UNAVAILABLE（僅單一時點快照，無法判斷增減）。
- 玩股網參考：400 張以上大股東比例 2026/07/17 為 41.29%，為同一來源可見的最近一期數字。

## Net sentiment score

- **Composite：偏多（neutral-to-bullish）**，信心度：低。
- 理由：唯一可用的正面訊號來自媒體與新聞（營收、毛利率、股價漲停）；分析師評等、內部人交易、散戶社群三大維度皆無資料，無法形成多來源共識。
- 風險：媒體報導偏向正面敘事，可能有選擇性偏誤；產業景氣是否持續未知；內部人持股高但近期申報資料缺失。

**Divergence flag：無法判定（no）**。缺少分析師評等與散戶社群資料，無法比較兩者方向是否相反。

## 資料缺口與後續建議

1. 重新執行 yf 工具，待 cookie/crumb 恢復後補抓 rec_summary、recommendations、insider。
2. 至 MOPS 查詢董監事持股與內部人申報轉讓明細（2026 年 5 月至 11 月）。
3. 至券商研究報告（如元大、凱基、群益）查詢最新目標價與評等。
4. 若 Reddit/StockTwits 恢復可用，補抓社群資料；若無法恢復，建議以 PTT 股版等替代來源補充。

SENTIMENT REPORT COMPLETE
