# Sentiment — 1815.TWO (富喬 Fuchuang) as of 2026-11-19

資料可得性總結：Reddit 與 StockTwits 無法取得，分析師評級與內部人交易資料為空，社群情緒資料實質缺漏。本報告的情緒判斷主要依據媒體報導的基本面敘事，信心偏低。

## Analyst consensus
0 buy / 0 hold / 0 sell（`yf rec_summary` 回傳全為 0，`yf recommendations` 無歷史評級紀錄）。
Recent moves：無可查詢之升降評等紀錄。
補充：單一網路快照（TradingView）顯示一筆分析師目標價 128.00 TWD，最高與最低皆為同一數字，且快照日期不明，覆蓋度極薄，無法視為共識。

## Retail social
- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 public JSON 端點均回報 "unable to fetch"，無法統計提及數或語氣。
- StockTwits / X：StockTwits API 因 `api.stocktwits.com` DNS 無法解析而失敗（需於 session 網路設定中允許該網域）。X 端未找到以 1815 為主題的近期社群討論，僅有媒體與研究機構的個股評論。
- 提及量：無法量化，無法與歷史基準比較。
- 情緒傾向：無社群樣本，無法判定 bullish / bearish 比例。
- Themes（僅依媒體報導歸納，非社群原文）：
  - 獲利大幅改善：2026 前三季稅後純益 20.82億 TWD，年增約 3.95 倍，9 個月 EPS 3.41 TWD（與淨利 ÷ EPS 反推股本約 6.1億 股，量級一致）。
  - 營收高成長：2026 年 10 月合併營收 10.49億 TWD，年增 85.62%；前 10 個月累計 77.67億 TWD，年增 58.42%。
  - 第三季毛利率 49.1%。
  - 泰國新廠規劃導入先進製程生產高階玻纖布，預計 2027 年第三季量產，題材指向 AI 伺服器、低軌衛星、IC 載板。
  - 估值與波動風險：有評論提及高本益比與股價波動，建議分批布局。
  - 技術面：媒體提到前波高點約 161.5 TWD 後回檔，11 月 9 日收盤約 129 TWD，前高壓力 141.5 TWD，風險控制區 120–122 TWD。
- 資料時效注意：搜尋結果中另有 TradingView 顯示約 91.8 TWD、Simply Wall St 顯示 54.00 TWD、Alpha Lenz 顯示 95.00 USD 等不一致價位，皆來源不明或明顯過時，本報告不採用。

## Insider activity
Net 6mo: 無資料。`yf insider` 回傳空陣列，無法判定 CEO / CFO 或其他董監事的買賣方向與金額。
Notable: 無可引用之交易紀錄。此為資料缺漏，不代表無內部人交易。

Ownership 補充（`yf major_holders`）：
| 項目 | 比例 |
|---|---|
| Insiders % held | 23.94% |
| Institutions % held | 10.36% |
| Institutions % of float | 13.62% |
| Institutional holder count | 23 |

持股趨勢（逐季變化）無資料，無法判斷機構集中度是上升或下降。

## Net sentiment score
Composite: **neutral（信心低）**

依據：
- 分析師面：無有效評級，無法給分。
- 社群面：Reddit、StockTwits、X 皆無可用樣本，無法給分。
- 內部人面：無交易紀錄，無法給分。
- 媒體敘事面：基本面（營收、獲利、毛利）與新產能題材偏正面，但同時出現估值與技術面分歧的提醒。媒體語氣整體偏正面，屬於基本面敘事而非市場情緒的直接量測。

綜合上述，以媒體正向基本面敘事為唯一可用訊號，且無社群與分析師佐證，因此判定為 neutral，信心低。

Divergence flag: **無法判定（no data）**。目前缺乏零售語氣樣本，無法與分析師傾向做對照，因此既不能確認也不能排除背離。

## 資料缺口與後續建議
1. Reddit JSON 端點被阻擋，需於 session 網路設定允許 reddit.com 或改用其他來源。
2. `api.stocktwits.com` 需加入 session 允許網域清單，才能取得 StockTwits 樣本。
3. `yf` 的 Yahoo cookie/crumb 取得失敗（ConnectionError），導致 `recommendations`、`rec_summary`、`insider` 可能是資料不完整而非真的沒有，建議於網路恢復後重跑。
4. 台灣市場的分析師覆蓋與內部人申報可參考 TPEx 公開資訊觀測站（重大訊息、董監事持股申報）以補足。

SENTIMENT REPORT COMPLETE
