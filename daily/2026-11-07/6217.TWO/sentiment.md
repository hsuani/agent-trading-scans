# Sentiment — 6217.TWO (中探針 Chung Hsin Probe) as of 2026-11-07

## Executive summary

本報告資料覆蓋嚴重不足。Yahoo 分析師評等、內部人交易兩組 yf 查詢皆因 fc.yahoo.com 連線失敗而回傳空陣列，無法判讀分析師共識與內部人淨買賣。僅取得股東結構快照（內部人持股約 17.2%、法人持股約 1.8%）。WebSearch 結果最新只到 2026 年 10 月左右，未找到 2026 年 11 月的散戶討論、新聞或評等變動。整體判定為「中性，低信心」，無法形成有效的散戶與分析師背離判斷。

## Data availability

| 來源 | 狀態 | 說明 |
|---|---|---|
| yf `recommendations` | 失敗（回傳空） | fc.yahoo.com cookie/crumb 連線失敗，重試一次仍失敗 |
| yf `rec_summary` | 失敗（回傳空） | 同上 |
| yf `insider` | 失敗（回傳空） | 同上；空陣列不代表無內部人交易 |
| yf `major_holders` | 成功 | 僅四項彙總指標，見下文 |
| WebSearch 散戶討論 | 部分可用 | 結果多為網站首頁與月資料頁，日期零散，最新約 2026 年 10 月 |
| Reddit（r/wallstreetbets, r/stocks） | 未查詢 | 本次任務限定以 WebSearch 取得散戶情緒，且台股個股在該社群樣本通常極少，未另行抓取 |
| StockTwits | 未查詢 | 同上，本次未以 WebFetch 存取財經站點 |
| 日期一致性 | 注意 | 報告日期為 2026-11-07，本機日期為 2026-11-06，當日收盤後資料可能尚未公布；所有 2026-11-07 之後的資料視為未知 |

## Retail / social sentiment read

- **聲量**：無法量化。搜尋結果未出現 2026 年 11 月的社群討論，無法與歷史基準比較。
- **既有可見討論（日期不明或非 11 月）**：
  - CMoney 股市討論頁提及資金動向與融資風險，並有人提醒股價在 170 元關卡附近不穩。該頁未標示發文日期，無法確認為近期內容，語氣偏謹慎。
  - 無法取得可核實的原始貼文，因此不引用具體引言。
- **主要主題（依搜尋摘要歸納，樣本有限）**：
  1. 股價劇烈波動與投機性質（2026 年多次被證交所列為注意股）。
  2. 融資餘額變化與資金追價風險。
  3. 營收年增仍有成長，但季度 EPS 為負，獲利面有爭議。
- **散戶傾向**：中性偏謹慎。依現有樣本無法區分多空比例，信心低。

## Analyst consensus

- **分析師買進 / 持有 / 賣出分布**：無資料（yf `rec_summary` 失敗）。
- **近期升降評等與目標價變動**：無資料（yf `recommendations` 失敗）。
- **基本面背景（非評等，僅供對照）**：
  - 2026 年 6 月營收約 4.29 億元（月增 5.8%，年增 43.91%）。
  - 2026 年 7 月營收約 4.22 億元（月減 1.73%，年增 27.8%）。
  - 2026 年 9 月營收約 3.52 億元（月減 16.09%，年增 0.7%）。
  - 2026 年前三季累計營收約 34.62 億元（年增 29.65%）。
  - Q2 2026 EPS 為 -0.3，累計至 Q2 為 -0.19；Q1 2026 EPS 約 0.11。
  - 以上為搜尋摘要所示數字，未經 yf 或公司公告逐筆核對。
- 因缺乏評等資料，無法判定分析師與散戶是否背離。

## Institutional / insider signal

### 內部人交易（6 個月）
- yf `insider` 查詢失敗，無法計算 6 個月淨買賣金額，亦無法確認 CEO / CFO 等身分的交易。
- 不得將空結果解讀為「無內部人交易」。

### 股東結構（yf `major_holders`）

| 指標 | 數值 | 備註 |
|---|---|---|
| 內部人持股比例 (insidersPercentHeld) | 17.23% | 可能包含大股東與董監，定義未確認 |
| 法人持股比例 (institutionsPercentHeld) | 1.84% | 相對於已發行股數 |
| 法人持股比例（流通股） (institutionsFloatPercentHeld) | 2.22% | 相對於流通股數 |
| 法人機構數 (institutionsCount) | 8 | 數量少 |

- 法人持股比例偏低，但 Yahoo 對台股法人資料覆蓋可能不完整，不宜直接推論法人撤出。
- 單一搜尋摘要（玩股網相關頁面）提到外資持股約 17% 至 21%（2026 年 5 月至 7 月）、投信持股為 0，數字未經原頁核實，僅列為待確認線索。
- 2026 年 7 月 31 日外資曾有小幅淨買超（約 307 張），融資餘額同期下降，屬短期籌碼訊號，無法延伸至 11 月。
- **趨勢判定**：無法確認 2026 年 11 月的持股變化趨勢。

## Overall sentiment verdict

- **分析師面**：無資料，無法判定。
- **散戶面**：中性偏謹慎，樣本少、日期不明，信心低。
- **內部人 / 法人面**：無法判定（內部人資料缺失；法人資料僅靜態快照）。
- **綜合**：**中性（Neutral），信心低**。
- **背離旗標**：**否（無法判定）**。因分析師評等缺失，無法判斷散戶與分析師是否方向相反。
- **對後續工作的建議**：需重新取得 yf `recommendations`、`rec_summary`、`insider` 資料（連線恢復後），並以 2026 年 11 月的 CMoney、PTT 股票板或新聞資料補足散戶面。本報告不提供交易建議。

## Sources

- [玩股網 6217 本益比 / 公司概況](https://www.wantgoo.com/stock/6217/enterprise-value/price-to-earning-ratio)
- [玩股網 6217 股東集中度](https://www.wantgoo.com/stock/6217/major-investors/concentration)
- [玩股網 6217 新聞](https://www.wantgoo.com/stock/6217/news)
- [CMoney 6217 股市討論](https://www.cmoney.tw/forum/stock/6217?tab=column)
- [Yahoo 股市 6217 融資頁](https://tw.stock.yahoo.com/quote/6217.TWO/margin)
- [winvest 中探針 2026 年 7 月營收快訊](https://winvest.tw/News/Detail/91459)
- [winvest 中探針 2026 年 6 月營收快訊](https://winvest.tw/en/News/Detail/90182)
- [HiStock 6217 券商分點績效](https://histock.tw/stock/mainprofit.aspx?no=6217)
- 本地工具：`pipeline/tools/yf.py 6217.TWO {recommendations, rec_summary, insider, major_holders}`（前三者因連線失敗回傳空陣列）

SENTIMENT REPORT COMPLETE
