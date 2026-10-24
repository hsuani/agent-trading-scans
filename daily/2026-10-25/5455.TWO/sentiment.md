# 情感分析 — 5455.TWO (昇益開發 SHENG YI DEVELOPMENT) 截至 2026-10-25

**注意事項（先讀）**
1. **公司身分與舊報告不符**：yfinance 回傳的公司為 Sheng Yi Development Co.,Ltd（昇益開發，新竹，營建/不動產開發，員工約 20 人）。搜尋結果 poorstock.com 也將 5455 對應為「昇益」。但 2026-07-21 既有的 `daily/2026-07-21/5455.TWO/sentiment.md` 描述的是「英特磊 (IET-KY)」，股價約 365 至 537 TWD、分析師目標價 854 TWD、EPS 7.22 元等。這些數字與 yfinance 的 31 TWD 收盤價及市值差距約一個數量級，**兩者無法同時成立**。本次報告不沿用該檔任何數字或結論，建議上游核對 July 報告的 ticker 對應是否錯誤。
2. **日期**：任務指定 DATE 為 2026-10-25，但本機系統日期為 2026-10-24。本報告以指定日期標註，資料實際截至工具可取得的最新值。

---

## 分析師共識
**0 買進 / 0 持有 / 0 賣出**（資料不足）。
- `yf rec_summary` 與 `yf recommendations` 皆回傳空陣列，無評等分佈、無升降評等紀錄。
- `yf info` 顯示 `recommendationKey: none`，無 `targetMeanPrice`，`numberOfAnalystOpinions` 未提供。
- 判讀：此股缺乏可得的券商覆蓋資料，無法判定分析師方向。不應解讀為「無人看好」或「無人看壞」，僅代表資料源無紀錄。

## 零售社群
- **Reddit (r/wallstreetbets, r/stocks)**：WebFetch 遭拒（無法連線 www.reddit.com），本次無資料。
- **StockTwits**：DNS 解析失敗（api.stocktwits.com 無法解析），本次無資料。
- **X / 新聞搜尋**：中文搜尋僅找到一則 poorstock.com 的 AI 生成技術頁（資料止於 2026/07/31，收盤約 28.3 元，成交量低、部分交易日無成交），以及與本公司無關的 2455 全新、TWO (Two Harbors) 內容。**未找到 5455 的論壇或社群討論串。**
- **討論量**：極低（無可辨識的討論樣本）。
- **零售傾向**：無法判定（資料不足）。
- **主題**：無可歸納的重複主題。
- 注意：July 報告引用的 CMoney、PTT、玩股網等討論內容，因上述公司身分問題，本次不予採計。

## 內部人交易
**6 個月淨買賣：無資料。**
- `yf insider` 回傳空陣列。空陣列不等於「無交易」，可能是資料源未覆蓋 TPEx 公司的董監事申報。
- `yf info` 列出的 officers 僅有董事長兼總經理 Wenchi Chen（陳文吉）與會計主管 Yanyin Yang，無交易紀錄欄位可用。
- 建議查核 MOPS（公開資訊觀測站）的董監事持股異動申報，以取得實際淨買賣金額。

## 持股結構
- `insidersPercentHeld`: 70.3%（內部人持股比重高，表示浮通股數有限）。
- `institutionsPercentHeld` / `institutionsCount`: 回傳 0，資料源不可用，**無法判斷機構持股趨勢**。
- 市值與股本：股本 65,502,000 股，收盤 31.0 TWD，市值約 **20.3 億 TWD**（2,030,562,048 TWD）。換算驗算：65.5M × 31.0 ≈ 2.03B，一致。

## 綜合情感評分
**Composite: 中性（neutral），信心：低。**
| 面向 | 狀態 | 評分 |
|---|---|---|
| 分析師共識 | 無資料 | 不計分 |
| 零售社群 | 無資料，討論量極低 | 不計分 |
| 內部人交易 | 無資料 | 不計分 |
| 持股結構 | 內部人 70.3%，機構資料缺 | 中性（僅供參考） |

有效資料面僅一項（持股集中），不足以形成方向性判斷。綜合評分不應被視為看多或看空訊號。

**Divergence flag: 無法判定（NO）。** 分析師與零售兩側均無有效樣本，不存在可比較的傾斜方向。

## 資料缺口與後續建議
1. 以 MOPS 核對董監事申報（內部人淨買賣）與重大訊息。
2. 以 TPEx 個股頁與昇益開發法說會資料，確認營運與基本面，並核對 July 報告是否誤植。
3. 若需社群面，可改用中文財經社群（CMoney、Goodinfo 討論區）直接人工查詢；Reddit 與 StockTwits 在目前網路條件下不可用。

**Sources (搜尋結果)**
- [poorstock.com - 5455](https://poorstock.com/stock/5455)
- 既有報告：`daily/2026-07-21/5455.TWO/sentiment.md`（身分不一致，僅供比對）

SENTIMENT REPORT COMPLETE
