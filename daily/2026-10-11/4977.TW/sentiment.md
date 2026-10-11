# Sentiment — 4977.TW (眾達-KY) as of 2026-10-11

## Analyst consensus
**0 buy / 1 hold / 0 sell**（yf rec_summary，僅 1 位分析師樣本）。
- Recent moves: `recommendations` 歷史評等變動為空，DATA_UNAVAILABLE（無可確認的升降評紀錄）。
- 目標價：Investing.com（香港頁）列 12 個月平均目標價 132.00 元，頁面未標示日期，屬快照，時效不明。
- 同一頁面顯示最近一次財報（2026-05-15）EPS -1.00，低於預估 0.67。
- 樣本極少（單一分析師），不足以代表市場共識。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。Reddit 直接抓取被擋（WebFetch 無法連線），無法計算提及數與情緒。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗。
- PTT 股票版：僅能取得標題層級資料（搜尋摘要，未抓到內文與留言）。可見標題包括「[標的] 4977 眾達-KY 司馬懿概念股」、「[情報] 4977 眾達-KY 決議買回庫藏股」、「[新聞] 4977眾達-KY10月自結0.7」。標題傾向中性偏正面（概念題材與買回），但無法量化。
- CMoney 討論區：搜尋摘要顯示多空意見分歧，有人擔憂跌停後賣壓，也有人看好中長期，整體偏向提醒風險控管。
- 聲量：無法取得量化提及數，DATA_UNAVAILABLE。定性上，PTT 與 CMoney 有持續討論，但未見爆量跡象。
- Themes（自搜尋摘要歸納，非原文抽樣）：
  1. CPO / 雷射光源題材：董事長於股東會表示馬來西亞新廠布建高功率雷射光源 Flip Chip 產能，有機會於 2026 年底通過認證；另有文章提及與 Broadcom 合作 CPO 雷射光學封裝。屬題材敘述，實際出貨時程未獲證實。
  2. 買回庫藏股：PTT 標題顯示公司已決議買回，屬正面訊號，決議日期與執行進度未確認。
  3. 營收與獲利落差：8 月合併營收年增 106.22%，但 1~5 月累計營收年減 25.49%，2026Q1 EPS -1.18 元，市場在「單月爆發 vs 基本面仍弱」之間拉扯。
  4. 股價波動大：2026-02 曾因異常交易被交易所處置，2026-05 有短期大漲後跌停的紀錄。
  5. 併購擴張：2026-05 宣布收購品固集團 100% 股權，擴大精密機構件布局。
- 代表性觀點（搜尋摘要改寫，非原文）：「CPO 量產潮是 2026、2027 年主軸」（投顧文章）；「怕跌停後的賣壓」（CMoney 討論）。

## Insider activity
DATA_UNAVAILABLE。`yf insider` 回傳空陣列；Yahoo cookie/crumb 取得失敗，無法確認是否為真實無申報或資料缺漏。
- 無法計算 6 個月淨買賣金額，也無法判斷 CEO/CFO 或其他人員的交易。
- 建議以台灣公開資訊觀測站（MOPS）的董監事持股申報補查。

## Ownership shifts
- `yf major_holders`：insidersPercentHeld 9.13%；institutionsPercentHeld 1.64%；institutionsCount 6。此為 Yahoo 美股口徑，對台股的法人持股統計可能不完整，僅供參考。
- 外資持股：玩股網顯示 2026/07/03 外資持股 16.74%。（來源為搜尋摘要，未取得時間序列。）
- 三大法人買賣超：
  - 2026-04 末近五日：外資合計賣超 2,651 張、投信買超 122 張（時報報導）。
  - 2026-08-03 外資賣超 49 張；2026-08-04 外資買超 113 張，投信為 0。
  - 9 月與 10 月的逐日數據未取得，DATA_UNAVAILABLE。
- 趨勢判讀：外資在 4 月大幅賣超，之後進出互有，無法確認 9–10 月方向。

## Price reference（資料時點不一致，需注意）
- statementdog：2026-10-07 收盤 175 元，每股淨值 51.99 元，股價淨值比 3.37 倍。
- nStock：2026-09-16 收 176.5 元。
- MONEY LINK：2026-08-04 收 131 元（當日 +7.82%）。
- Investing.com：股價 134 元（無日期）。
- 上述價格來源時點不同，且 Investing 頁面的 134 元與 10/07 的 175 元差距大，無法確認 10/11 當日價格。

## Net sentiment score
- **Composite：neutral（信心：低）**
  - 分析師面：偏中性。僅 1 位分析師、評等 hold、目標價 132 元，且目標價參照的股價與近期報價不一致，時效不明。
  - 散戶面：偏中性，略偏正面題材。CPO 與買回為正面敘事，但 PTT/CMoney 同時出現風險提醒，無量化數據。
  - 內部人與籌碼面：資料不足。內部人 DATA_UNAVAILABLE；外資 4 月大幅賣超後方向不明。
- **Divergence flag：no（無法判定）**
  - 分析師 hold 與散戶中性偏正面題材，並非明確反向。但因散戶量化數據缺失，此判定信心低。

## Data gaps summary
| 項目 | 狀態 |
|---|---|
| Analyst rec_summary | 可用（1 位分析師，0/1/0） |
| Analyst 歷史評等變動 | DATA_UNAVAILABLE |
| 目標價 | 快照可用，日期不明 |
| Reddit | DATA_UNAVAILABLE（連線被擋） |
| StockTwits | DATA_UNAVAILABLE（DNS 失敗） |
| PTT / CMoney | 僅標題與摘要，無量化 |
| Insider 6mo | DATA_UNAVAILABLE |
| 大股東 / 法人持股 | 部分可用（Yahoo 口徑與外資 16.74%） |
| 9–10 月三大法人 | DATA_UNAVAILABLE |

SENTIMENT REPORT COMPLETE
