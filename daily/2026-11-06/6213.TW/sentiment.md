# Sentiment — 6213.TW (聯茂 ITEQ, CCL) as of 2026-11-06

> 資料時點注意：DATE 為 2026-11-06。本次可取得的最新新聞與股價資料約到 2026-10 中下旬，2026-10 下旬至 11-06 之間的散戶討論、法人買賣超與股價均無法取得，以下不做推估。
> 整體資料可信度：低。yf 認證失敗（fc.yahoo.com / query2.finance.yahoo.com 被 proxy 拒絕），`recommendations` 與 `rec_summary` 三期數字完全相同，疑似快取；Reddit / StockTwits 主機無法連線，本次未重試。

## Analyst consensus

rec_summary（yf，0m）：9 家分析師，7 買進（強力買進 3 + 買進 4）/ 1 持有 / 1 賣出。買進占比約 78%（7/9）。
- 注意：0m、-1m、-2m 三期完全相同（3 / 4 / 1 / 1 / 0），與 2026-11-05 檔案中的數字一致，無法判讀近期 upgrade / downgrade 節奏，視為快取值。
- `recommendations` 歷史評等變動：DATA_UNAVAILABLE（沒有日期欄位，無法辨識評等變動時點）。

WebSearch 可見的其他評等與目標價（來源時點不一、彼此衝突，僅供參考）：
- 2026-08 前後：一家民營金控投顧評等「買進」，目標價 785 元。
- 日系外資上調目標價至 1,110 元，理由為 CCL 漲價（報導日期不明，應為 2026 年中前後）。
- 大華資本（Daiwa）「中立」，目標價 123 元，日期不明，可能為較舊報告。
- stockanalysis（2026-08-05 快照）：8 家 S&P Global 追蹤分析師，共識「Hold」，平均目標價低於當時股價約 12%。
- valueinvesting.io（日期不明）：16 家分析師，共識 HOLD，平均目標價約 230.75 元。
- FactSet 共識目標價 105.5 元，報導標示為 2025 年調查，已過時。

解讀：yf 的 rec_summary 偏多（78% 買進），但 WebSearch 來源的共識在 Hold 與 Buy 之間分歧，目標價從 105.5 元到 1,110 元不等。這種分歧來自不同日期與不同資料商的 snapshot，無法合成為單一可信的共識。

Recent moves：DATA_UNAVAILABLE（無可辨識日期的評等變動）。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（主機無法連線，本次未重試）。
- StockTwits：DATA_UNAVAILABLE（主機無法連線）。
- 聲量相對基準：DATA_UNAVAILABLE（無提及次數，無法做量化比較）。
- CMoney 股市爐主（股吧）：摘要頁無日期，多空並陳。偏多的一方認為主力仍會拉抬；偏空的一方則主張換股、認為信心受挫，另有人提醒追高風險。此為搜尋摘要的轉述，非原始貼文，且時間點不明。
- X / PTT / Dcard：本次搜尋未找到 2026-10 下旬至 11-06 的討論串，無法判讀。

Retail tilt：MIXED（低信心）。僅能依據無日期的股吧摘要判斷多空並存，無法確認 2026-11-06 當下的散戶傾向。

Themes（有依據者，來自新聞與搜尋摘要）：
1. 漲價循環：CCL 上游與終端售價同步上調，帶動獲利預估上修（2026-06 營收 42.14億，年增 47.94%；2026-07 營收 47.49億，年增 96.88%，皆為新聞轉述的歷史單月新高）。
2. AI 伺服器與 ASIC 需求：高階 CCL 規格升級為主要多方論點。
3. 技術替代風險：CPO 技術被視為可能降低部分應用的 CCL 規格需求，2026-09-17 曾因此收跌停（新聞標示），是主要空方論點。
4. 追高與獲利了結：大漲後回檔常被歸因於獲利了結，而非基本面轉弱。
5. 產能瓶頸：新伺服器平台受上游封裝瓶頸影響，放量進度可能不如預期（法人提醒的風險）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。
- yf `insider` 回傳空陣列，但 yf 認證已失敗，無法區分「確實無交易」與「取得失敗」。
- WebSearch 未找到 2026-05 至 2026-11 的董監持股轉讓申報內容。
- Notable：無法列出 CEO / CFO 或其他人員的買賣紀錄。

## Ownership shifts

- yf major_holders 單期快照：insidersPercentHeld 37.6%；institutionsPercentHeld 7.8%；institutionsFloatPercentHeld 12.6%；institutionsCount 48。
- yf inst_holders：空陣列（DATA_UNAVAILABLE）。
- 外資持股（wantgoo，2026-07-03）：74,895 張、持股比重 20.6%；三大法人合計持股比重 23.83%。7 月 2 日外資買賣超 -44 張，投信 0。
- 注意：yf 的 institutionsPercentHeld（7.8%）與 wantgoo 的外資 + 三大法人比重（23.83%）定義不同，不能直接比較。
- 趨勢方向：DATA_UNAVAILABLE。2026-07 之後的法人買賣超與持股比重無資料，無法判定 10 月至 11 月的資金流向。
- Yahoo 與 MONEY LINK 的法人表分別停在 2025-12 與 2025-09，已過期，不採用。

## Net sentiment score

- Composite：偏多（信心：低）。
  - 分析師端：rec_summary 7 買進 / 1 持有 / 1 賣出，偏多；但數據疑似快取，且目標價分歧極大。
  - 散戶端：MIXED，僅有無日期的股吧摘要，無法確認當下傾向。
  - 內部人端：DATA_UNAVAILABLE。
  - 法人籌碼端：DATA_UNAVAILABLE（僅 2026-07 快照，方向不明）。
  - 新聞敘事：漲價與 AI 需求偏多，CPO 規格替代風險偏空，兩者並存。
- Divergence flag：無法判定。分析師端偏多，散戶端 MIXED，若後續取得 2026-10 下旬至 11-06 的股吧或 PTT 原始貼文，再重新評估背離。

## Data gaps summary

| 項目 | 狀態 | 原因 |
|---|---|---|
| 分析師歷史評等變動 | DATA_UNAVAILABLE | 無日期欄位，三期數字相同 |
| 分析師 rec_summary | 有值但疑似快取 | yf 認證失敗，三期相同 |
| Reddit | DATA_UNAVAILABLE | 主機無法連線 |
| StockTwits | DATA_UNAVAILABLE | 主機無法連線 |
| 散戶聲量基準 | DATA_UNAVAILABLE | 無原始提及數 |
| 6 個月內部人交易 | DATA_UNAVAILABLE | yf 認證失敗，網頁無內容 |
| inst_holders | DATA_UNAVAILABLE | yf 回傳空陣列 |
| 法人買賣超 2026-10 至 11-06 | DATA_UNAVAILABLE | 搜尋無資料，最新為 2026-07 |
| 2026-10 下旬至 11-06 股價 | DATA_UNAVAILABLE | 搜尋無資料 |

## Summary

- analyst consensus：77.8% BUY（7/9，yf rec_summary，疑似快取）
- institutional flow direction：UNKNOWN（無 2026-10 至 11-06 資料；最後快照 2026-07 外資持股 20.6%）
- retail sentiment tone：MIXED（低信心）

SENTIMENT REPORT COMPLETE
