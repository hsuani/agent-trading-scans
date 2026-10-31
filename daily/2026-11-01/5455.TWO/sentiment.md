# Sentiment — 5455.TWO as of 2026-11-01

資料時點：本機 yf 快取寫入於 2026-10-31 12:08 UTC；系統日期為 2026-10-31，報告以指定的 2026-11-01 標示。

**資料可信度警示：本次資料大部分不可用，無法給出可靠的情緒評分。** 以下說明缺口與矛盾，請勿把本報告當成有效的情緒判斷。

## 資料取得狀況

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary / insider | 回傳空陣列（Yahoo cookie/crumb 取得失敗，疑為網路限制） |
| yf major_holders | 部分回傳：insidersPercentHeld 70.3%，institutions 欄位皆為 0（不可信） |
| yf info（快取） | 有回傳，但與既有筆記矛盾，見下方「身分與價格矛盾」 |
| Reddit r/wallstreetbets、r/stocks | WebFetch 失敗（無法連線 www.reddit.com），無資料 |
| StockTwits | DNS 解析失敗（api.stocktwits.com 不在允許網域內），無資料 |
| WebSearch（中文、英文，共三次） | 結果皆為其他公司或其他 .TWO 代號，無 5455 相關內容，未採用 |

## 身分與價格矛盾（需先核對 — 重大資料品質警示）

- 既有筆記 `daily/2026-07-21/5455.TWO/sentiment.md` 記錄公司為「英特磊」，價格區間 365–537 TWD，EPS 預估 7.22 元，Q1 2026 稅後淨利年增 231.8%。
- 本次 yf info 回傳 longName 為 **Sheng Yi Development Co., Ltd**（聖億建設，房地產開發商），currentPrice 30.35 TWD，trailingEps -0.63，市值約 19.9 億 TWD。
- 兩組資料的價格、獲利方向與公司名稱都對不上，無法判斷哪一組正確。**universe.py taxonomy 將 5455.TWO 定義為「英特磊」（矽光子磊晶供應鏈上游），但本次 yfinance 回傳的是聖億建設（建設公司），兩者業務完全不相關。** 在核對前，以下所有數字都應視為未驗證，且不應用於本股的 photonics 同業比較。

## 分析師共識

本次工具回傳 0 buy / 0 hold / 0 sell（資料為空，不代表無覆蓋）。

- 上一期（2026-07-21）筆記記錄 2 buy / 0 hold / 0 sell，平均目標價 854 TWD。此為舊資料，且在上述身分矛盾下無法確認，不應直接沿用。
- 近期升降級：本次無資料，無法判斷。

## 零售社群

- Reddit：無法取得（連線失敗）。
- StockTwits / X：StockTwits 無法連線；WebSearch 無相關結果。
- 討論量：無法量化。
- 情緒傾向：無法判定。

## 內部人交易

- 6 個月淨買賣：無資料（yf insider 回傳空陣列）。
- insidersPercentHeld 70.3% 的數字異常高，且與公司身分矛盾，未納入判斷。

## 持股結構

- 機構持股欄位全為 0，不可信，無法判斷機構集中度趨勢。
- 內部人/大股東持股 70.3%（來源待核對）。

## 綜合情緒評分

**無法判定，信心：極低（資料身分矛盾 + 資料不足）。**

- 分析師面：無有效本期資料，無法評估。
- 零售面：無有效本期資料，無法評估。
- 內部人面：無資料。
- 背離旗標：**無法判定**（缺少分析師或零售任一側的有效資料，且公司身分本身存疑）。

## 建議後續動作（供上游判斷，不構成交易建議）

1. **優先事項：核對 5455.TWO 的正確公司名稱與現價**（英特磊 vs Sheng Yi Development；365–537 TWD vs 30.35 TWD）。此為本股本次 Phase-1 全部報告（fundamentals/market/sentiment）共同的資料完整性問題，建議下游（evidence-shadow、research-manager、sector-comparator）不要將本股數字當作 tw_photonics 同業的正常數據使用。
2. 在網路允許清單中加入 api.stocktwits.com，並確認 Yahoo（fc.yahoo.com）可連線，以恢復 yf 的 recommendations 與 insider 資料。
3. 改用台灣來源補充分析師評等與內部人申報，取代空白欄位。
