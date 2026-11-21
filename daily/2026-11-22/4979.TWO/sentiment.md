# Sentiment — 4979.TWO (華星光通訊) as of 2026-11-22

資料說明：本報告以 2026-11-22 為基準日，超過該日期的資料一律視為未知。Reddit 與 StockTwits 無法取得（見下方來源狀態）。最新可確認的股價資料為 2026-11-16 收盤。

## Analyst consensus

Yahoo rec_summary 與 recommendations 僅顯示 **2 buy / 0 hold / 0 sell**（strongBuy 1、buy 1），三個期間（0m、-1m、-2m）數字相同，代表覆蓋家數極少，不足以代表市場共識。

| 來源 | 評等 | 目標價 (TWD) | 日期 / 備註 |
|---|---|---|---|
| Yahoo rec_summary（yf） | 2 買入 / 0 持有 / 0 賣出 | 未取得 | 三個期間數字不變 |
| 統一投顧（新聞報導） | 買進（首次給予） | 800 | 2026 年營收預估 60.62 億、2027 年 119.81 億（年增 98%）；EPS 預估 7.69 元 / 15.88 元 |
| Investing.com 彙整 | 2 買入 | 12 個月平均 475 | 同樣只有兩位分析師，樣本極小 |
| 理周投研（舊資料） | 未明 | 210 | 2024 年 3 月，已過時，僅供參考 |

近期變化：未找到外資（摩根士丹利、大摩、野村等）近期評等調升或調降的明確報導。統一投顧初次給予買進評等是目前可見最新的評等動作，但其確切日期未能在搜尋結果中確認。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：無法存取。WebFetch 回報 "Claude Code is unable to fetch from www.reddit.com"，因此未能取得討論串、發文數或情緒傾向。
- **StockTwits / X**：api.stocktwits.com 解析失敗（ENOTFOUND），此網域需在 session 網路設定中允許後才能使用。依規則軟失敗，不列為證據。
- **新聞與網路討論（WebSearch）**：搜尋未找到論壇（PTT、Dcard、股市討論區）的情緒量化數據。Dcard 有個股分析文章（#標的 台股個股分析-華星光(4979)），但內容未能在搜尋摘要中讀取。
- **聲量相對水準**：無法直接量測。以新聞量觀察，近期報導集中在 2026 年 11 月前後的股價急跌與法說題材，可推定討論熱度高於平常，但這是推論，不是計數結果。
- **主要題材（依新聞與分析文章歸納）**：
  - 多方：AI 資料中心與 800G 光模組需求；第三季營收 16.29 億（季增 26.4%、年增 51.4%）；法說會提到 2026 年 800G 成為主流、1.6T 小量出貨；EPS 有機會挑戰 12 元。
  - 空方／風險：客戶集中度高；拉貨節奏；第二供應商導入可能壓縮份額。
  - 短線氣氛：11/16 收盤 341.5 元，單日下跌 37.5 元（-9.89%），前幾日曾觸及 383 元漲停，波幅大，短線獲利了結與震盪賣壓是主要討論點。
- **零售傾向**：以新聞與分析文章看，基本面敘事偏多，但近期價格走勢偏空，屬於混合。無法從社群原文確認散戶實際情緒。

## Insider activity

- **yf insider**：回傳空陣列，過去 6 個月無可取得的內部人交易紀錄。
- **Yahoo 股市 insider-transactions 頁面**：快照停在 2026 年 1 月，董監持股比例顯示約 0.01%。
- **網路搜尋**：未找到 2026 年 11 月的董監事申報轉讓資料。
- **結論**：6 個月淨買賣金額 無法確認（資料缺漏，非「零交易」的證據）。建議到公開資訊觀測站（MOPS）查詢「內部人持股轉讓事前／事後申報」。

注意：yf major_holders 的 insidersPercentHeld 為 12.0%，與 Yahoo 股市頁面的董監持股 0.01% 相差很大，兩者定義不同（前者可能含大股東或法人），本報告不採用其一作為內部人持股的結論。

## Ownership shifts

- yf major_holders：institutionsPercentHeld 24.1%、institutionsFloatPercentHeld 27.4%、機構家數 36。
- 無歷史季度數據，無法判斷機構持股趨勢是增加還是減少。
- 機構持股占比偏低，且家數少，表示法人覆蓋不完整。

## Net sentiment score

**Composite：偏多（neutral-to-bullish），信心低。**

- 分析師面：偏多但樣本過少（2 位買入，無持有、無賣出）。統一投顧給予 800 元目標價，但 12 個月平均目標價 475 元與 11/16 收盤 341.5 元之間有顯著上行空間假設，這本身就是需要保留的前提。
- 散戶面：無法量化，僅能依新聞判斷為混合，短線偏空（急跌）、基本面敘事偏多。
- 內部人面：資料缺漏，無法評分。
- 整體評分因社群與內部人資料缺漏，信心屬低。

**Divergence flag：無法判定。** 散戶傾向無可靠量化數據，無法確認是否與分析師傾向相反。若日後取得 PTT / Dcard 或 StockTwits 資料，應重新檢查此項。

## 資料缺口與來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 成功（樣本僅 2 家） |
| yf insider | 成功但回傳空陣列 |
| yf major_holders | 成功 |
| Yahoo fc.yahoo.com cookie/crumb | 連線失敗（已略過） |
| Reddit r/wallstreetbets、r/stocks | 失敗（WebFetch 無法存取 reddit.com） |
| StockTwits | 失敗（api.stocktwits.com 無法解析，需允許網域） |
| WebSearch 新聞／論壇 | 部分成功，無社群計數 |
| MOPS 內部人申報 | 未查詢（需人工或另一工具） |

SENTIMENT REPORT COMPLETE
