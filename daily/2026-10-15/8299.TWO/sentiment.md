# Sentiment — 8299.TWO (群聯電子 Phison Electronics) as of 2026-10-15

資料截止：2026-10-15。本報告未使用 2026-10-15 之後的資料。

整體狀態：分析師共識資料可取得但日期不明；散戶社群來源（Reddit、StockTwits、PTT）全部無法取得，標記為 DATA_UNAVAILABLE；內部人交易資料無法取得，標記為 DATA_UNAVAILABLE。整體信心偏低。

## Analyst consensus
yfinance 快照（日期未標示，Yahoo cookie/crumb 取得失敗，資料可能是快取）：4 strongBuy / 7 buy / 1 hold / 1 sell / 0 strongSell，合計 13 家。即 11 買進（含強力買進）、1 持有、1 賣出。

近 3 個月歷史快照（period -1m 至 -3m）：多數為 4 strongBuy / 7 buy / 1 hold / 1 sell，-3m 時為 4 / 6 / 1 / 0 / 0，賣出評等在 -3m 時為 0，之後出現 1 家賣出。評等結構整體穩定，未見明顯集中下修。

Investing.com 共識（日期約 2026-05 至 2026-07，來源日期不一）：平均目標價約 2,942 至 2,977 TWD，範圍 2,240 至 4,130 TWD；7 月頁面列 10 買進 / 1 持有 / 0 賣出。

近期目標價調整（新聞來源，2026 年 8 月中旬，財報後）：
- 下修：富邦投顧、國泰證期分別由三字頭降至 2,730 元與 2,900 元；統一投顧下修至 2,700 元。
- 上修或維持正面：國票投顧上調 600 元至 3,000 元；宏遠 3,725 元；中信投顧、群益投顧分別調高至 2,785 元、2,730 元；凱基投顧持平。
- FactSet 調查：2026 年 EPS 預估中位數由 395.87 元升至 402.74 元，但目標價中位數降至 2,750 元。

資料缺口：2026 年 9 月與 10 月的目標價變動未在搜尋中找到明確報導。Investing.com 價格與日期標示不一致（同頁 1,650 TWD 與前收 564 TWD 矛盾），此處不採用其價格數字。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。兩個 search.json 端點皆被拒絕（"Claude Code is unable to fetch from www.reddit.com"）。無法計算討論量、無法引用代表性貼文，散戶傾向未知。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 解析失敗（getaddrinfo ENOTFOUND），無法取得訊息與 Bullish/Bearish 標籤。
- PTT（股票板）：DATA_UNAVAILABLE。搜尋未找到 2026 年 10 月的群聯相關討論串，無法評估。
- 討論量（相對常態）：無法評估（DATA_UNAVAILABLE）。
- 新聞與媒體語氣（替代參考，非散戶原文）：8 月 14 日股價單日下跌 8.77% 至 2,080 元，評論稱為「利多出盡」與短線獲利了結賣壓；多家媒體以「記憶體賺爛」、「每股豪配 60 元」等形容獲利表現，偏正面。
- 主要主題（來自新聞，非散戶貼文）：
  1. 獲利創高與毛利率高峰是否已過（偏空論點：毛利率高峰、本益比可能壓縮）。
  2. NAND 供給在 2027 年前仍吃緊，獲利可維持高檔（偏多論點）。
  3. 高層持股動向與股價關聯（見下方內部人段落）。

代表性原文引述：無（散戶來源全部不可得）。

## Insider activity
yfinance insider 資料：回傳空陣列，無法確認是否為真實無交易或取值失敗。因 Yahoo 認證失敗，視為 DATA_UNAVAILABLE，不推定為零交易。

新聞補充（非完整申報清單）：
- 2026-01-13：執行長潘健成依法申報贈與持股，贈與 3 名子女，每人 34 張，合計 102 張。據報導本人表示屬家族贈與安排，非出售。該事件距今超過 6 個月，不計入近 6 個月淨額。
- 未找到 2026 年 4 月 15 日後的董監事買賣申報。

淨額（近 6 個月，2026-04-15 至 2026-10-15）：DATA_UNAVAILABLE。無法計算 $ 買入與 $ 賣出。

## Ownership shifts
yfinance major_holders（日期未標示）：
- 內部人持股：15.87%
- 機構持股：17.16%（浮動股比例 20.40%）
- 機構家數：164

趨勢：無歷史時間序列，無法判斷增減。僅能記錄當前集中度為中等偏低（機構占比不高），屬一次性快照。

## Net sentiment score
Composite: 中性偏多（信心：低）

依據：
- 分析師面（權重較高）：評等結構偏多，11 買進 / 1 持有 / 1 賣出，近期目標價有上有下，財報後共識未明顯轉向。
- 散戶面：無資料（DATA_UNAVAILABLE），不納入計分。
- 內部人面：無近 6 個月資料，不納入計分。
- 新聞語氣：獲利創高但股價財報後回落，市場對高點的分歧明顯。

信心偏低的原因：散戶來源全部缺失，分析師資料日期不明，內部人資料無法驗證。

Divergence flag: 無法判定（DATA_UNAVAILABLE）。散戶傾向缺失，無法比較是否與分析師傾向相反。若日後取得 PTT 或 Reddit 資料，應重新評估此欄。

## 資料來源狀態
| 來源 | 狀態 | 備註 |
|---|---|---|
| yf recommendations / rec_summary | 可取得（日期未明） | Yahoo cookie/crumb 失敗，可能為快取 |
| yf insider | DATA_UNAVAILABLE | 回傳空陣列，原因不明 |
| yf major_holders | 可取得（日期未明） | 單一快照 |
| Reddit r/wallstreetbets、r/stocks | DATA_UNAVAILABLE | 403 類拒絕 |
| StockTwits | DATA_UNAVAILABLE | DNS 解析失敗 |
| PTT | DATA_UNAVAILABLE | 搜尋無 2026 年 10 月討論 |
| WebSearch 新聞與法人 | 部分可用 | 最新具日期資料約 2026-10-08（9 月營收） |

SENTIMENT REPORT COMPLETE
