# Sentiment — 6217.TWO 中探針 as of 2026-11-28

**注意事項**
- 系統環境日期為 2026-11-27，任務指定 DATE 為 2026-11-28。本報告只採用 2026-11-28 以前的資料，之後的資料一律視為未知。
- 本次未使用任何舊的 `daily/<date>/` 報告數據。

## 資料來源可用性

| 來源 | 狀態 | 說明 |
|---|---|---|
| yfinance recommendations / rec_summary / insider | DATA_UNAVAILABLE | Yahoo cookie/crumb 取得失敗，三個指令皆回傳空陣列 |
| yfinance major_holders | 部分可用 | 回傳值見下表，可信度低（見說明） |
| Reddit r/wallstreetbets、r/stocks | DATA_UNAVAILABLE | WebFetch 無法連線 www.reddit.com |
| StockTwits | DATA_UNAVAILABLE | api.stocktwits.com DNS 解析失敗 |
| X / PTT | 未取得 | 搜尋結果沒有可用的討論串或留言內容 |
| WebSearch（新聞、法人、申報轉讓） | 部分可用 | 多數來源為 2026-10 至 2026-11 初，部分價格資料日期不一致 |

## Analyst consensus

DATA_UNAVAILABLE：無法取得 buy / hold / sell 家數與評等變動。
目標價：未找到 2026 年券商目標價。搜尋到的「目標價 250 至 270 元」來自技術分析網站，資料日期為 2026-01，不是券商目標價，不採用。
法人觀點（新聞轉述，非評等）：經濟日報與鉅亨網報導指出，法人預期 2026 年半導體測試針營收占比由約 20% 提升至約 30%，外資與自營商近期積極買進。這是較早期的看法，與近期營收下滑有落差。

## Retail social

- **Reddit**：DATA_UNAVAILABLE。
- **StockTwits / X**：DATA_UNAVAILABLE（StockTwits 網路受限；X 無可用結果）。
- **PTT**：未取得討論串內容。nStock 雖有 PTT 討論分頁，但搜尋結果未擷取內文。
- **可觀察到的 Ptt 標題**：2026-10-16 有一則「9 月自結 EPS -0.30、年增 -1,600%」的發文，顯示該月仍為虧損。這是新聞性質的貼文，不代表散戶整體情緒。
- **聲量（相對）**：無法量化。
- **Tilt**：無法判定（資料不足）。
- **主要題材（由新聞與公告歸納，非散戶原話）**：
  1. 半導體測試針（探針卡）營收占比提升的長期故事
  2. 短線劇烈波動：近 5 日跌約 28%（2026-11-09 前後），被列為「注意股」
  3. 過去曾因股價急漲急跌被列為處置股（2025 年下半年與 2026 年 3 月前後各有紀錄）
  4. 營收與獲利轉弱（10 月營收年減 11%，9 月單月仍虧損）

## Insider activity

Net 6mo：DATA_UNAVAILABLE（yfinance insider 空回傳，無法取得 6 個月淨買賣金額）。

間接線索（均為舊資料，不足以判斷近期趨勢）：
- Yahoo 申報轉讓頁面最新一筆約為 2024-07，之後無更新紀錄。
- 玩股網董監持股比例在 2026-05 底至 2026-07-24 間約維持 6.84%，無明顯增減，但資料未涵蓋 11 月。
- 無法確認是否有 CEO / CFO 買賣。

## Ownership shifts

- yfinance major_holders：insidersPercentHeld 17.23%、institutionsPercentHeld 3.77%、institutionsFloatPercentHeld 4.55%、institutionsCount 8。
  - 注意：機構持股 3.77% 與台股上櫃公司的一般水準差距很大，此數值可能有統計口徑問題，**不建議直接用於結論**。
- 外資動向（goodinfo 搜尋摘要，2026-11-09）：外資單日賣超 16 張，持股 32,904 張，持股比 28.07%。投信當日無買賣。
- 趨勢（多個月）：無法確認。

## 價格與基本面背景（僅作為情緒判讀背景）

| 項目 | 數值 | 日期 / 來源 |
|---|---|---|
| 股價（近期兩個值） | 168 元（10/08）、131 元（11/10，單日 +9.62%） | statementdog、nStock |
| 近 5 日漲跌 | -28.29%（被列注意股） | nStock 新聞，2026-11-09 |
| 10 月營收 | 2.80 億元，年減 11.03% | nStock 快訊 |
| 2026 上半年營收 | 22.72 億元，年增 37.69% | 新聞摘要 |
| 9 月自結 EPS | -0.30 元，年增 -1,600% | Ptt 發文，2026-10-16 |
| 近 4 季 EPS | -0.37 元 | statementdog |
| 股價淨值比 | 6.54 倍 | statementdog |

資料衝突：部分來源指 2026 年 5 月營收年增 51.18%，2026 年 Q1 EPS 0.11 元，但 2025 全年 EPS 為 -1.65 元。另有頁面顯示一年內最高 371 元、最低 41.2 元，波動劇烈，且各來源股價不一致。以上數值未經交叉驗證，請以 MOPS 或證交所資料為準。

## Net sentiment score

- **Composite：neutral，信心低（low）**
- 理由：
  - 分析師端無數據，無法判斷評等傾向。
  - 散戶端（Reddit、StockTwits、PTT）皆無法取得，無法判斷傾向。
  - 可觀察的新聞與價格面偏弱：短線大跌、注意股、營收年減、獲利為負；另有法人買超與半導體測試針長期故事作為支撐。兩者並存，合計偏中性。
- **Divergence flag：無法判定（no）**
  - 因分析師與散戶兩端皆缺資料，無法判斷兩者是否背離。

## 指標表

| 指標 | 數值 | 狀態 |
|---|---|---|
| 買 / 持有 / 賣家數 | DATA_UNAVAILABLE | 無資料 |
| 近期評等變動 | DATA_UNAVAILABLE | 無資料 |
| 目標價（券商） | DATA_UNAVAILABLE | 無資料 |
| Reddit 討論量與傾向 | DATA_UNAVAILABLE | 來源受限 |
| StockTwits 訊息量與傾向 | DATA_UNAVAILABLE | 來源受限 |
| PTT / X 傾向 | DATA_UNAVAILABLE | 無可用內容 |
| 6 個月內部人淨買賣（TWD） | DATA_UNAVAILABLE | 無資料 |
| 董監持股比例 | 約 6.84%（至 2026-07-24） | 舊資料，11 月未確認 |
| insidersPercentHeld（yfinance） | 17.23% | 可信度低 |
| institutionsPercentHeld（yfinance） | 3.77% | 可信度低，疑似口徑問題 |
| 外資持股比（2026-11-09） | 28.07%（32,904 張） | 來源：goodinfo 摘要 |
| 10 月營收 | 2.80 億元（年減 11.03%） | 新聞 |
| 上半年營收 | 22.72 億元（年增 37.69%） | 新聞 |
| 近 5 日股價變動 | -28.29% | 新聞，2026-11-09 |
| 綜合情緒 | neutral（信心低） | 本報告判定 |
| 背離旗標 | 無法判定 | 資料不足 |

SENTIMENT REPORT COMPLETE
