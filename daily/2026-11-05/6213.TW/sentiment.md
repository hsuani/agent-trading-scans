# Sentiment — 6213.TW (聯茂 ITEQ, CCL) as of 2026-11-05

> 資料時點注意：本次執行環境日期為 2026-11-04，2026-11-05 尚無收盤與新聞資料。以下為 2026-11-04 前可取得的最新資料，視為 11-05 的近似值。
> 整體資料可信度：低。Yahoo 端點 cookie/crumb 取得失敗，Reddit/StockTwits 無法連線，多數分析師數據與新聞目標價互相矛盾。

## Analyst consensus

rec_summary（yf，當期 0m）：9 家分析師，7 買進（含強力買進 3）/ 1 持有 / 1 賣出。
- 注意：0m、-1m、-2m 三期數字完全相同，且 yf 認證失敗，疑似快取或預設值，不能當作近期變化的證據。
- `recommendations` 歷史評等變動：DATA_UNAVAILABLE（三期無差異，無法辨識 upgrade/downgrade 時點）。

近期新聞中的評等與目標價（WebSearch，來源時點不一、彼此衝突）：
- 2026-08-25：一家民營金控投顧將評等升為「買進」，目標價 785 元（本益比 15 倍），報導稱與當時收盤價相比仍有約 48% 上行空間。
- 多家本國投顧調高獲利預估與目標價，理由包括產品漲價、稼動率提升與產能擴充。
- 另一則報導引述大華資本（Daiwa）給予「中立」評等、目標價 123 元，與上述 785 元差距極大，日期不明，可能為較舊報告。
- FactSet 共識目標價 105.5 元，報導標示為 2025 年調查，已過時，僅供參考。
- 同一批新聞提及 2026 年 EPS 預估約 20.01 元，但另一份 FactSet 資料為 EPS 4.58 元，單位與年度不一致，不採用。

Recent moves：近期評等朝上調整為主（多家調升目標價），但目標價分散度極大，無法形成可靠共識。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（主機於本沙盒被封鎖，未重試）。
- StockTwits：DATA_UNAVAILABLE（主機被封鎖）。
- X / 新聞討論：WebSearch 未找到 2026 年 11 月的散戶討論。可辨識的市場敘事如下：
  - 2026 年 7 月，聯茂在大陸 CCL 龍頭調漲通知後帶頭大漲，股價創紀錄高點約 424.5 元（新聞標示）。
  - 2026 年 9 月 17 日，股價收於跌停 495 元，原因為 CPO 技術可能降低部分應用所需的 CCL 規格，市場對規格替代風險有疑慮（新聞標示）。
  - 族群層級：CCL 三雄（台光電、台燿、聯茂）同步走強或回檔，題材為 AI 伺服器與網通高階規格升級、ASIC 需求（特別是 AWS 相關）。
- 聲量相對基準：DATA_UNAVAILABLE（無法取得提及次數，無法做量化比較）。

- Themes（有依據者）：
  1. 漲價循環：CCL 上游成本與終端售價同步上調，帶動獲利預估上修。
  2. AI 伺服器與 ASIC 需求：高階 CCL 規格升級是主要多方論點。
  3. 技術替代風險：CPO 與規格變化被視為空方主因，且曾引發單日重挫。
  4. 追高與獲利了結：大漲後的回檔被歸因於獲利了結，而非基本面轉弱。

- Retail tilt：DATA_UNAVAILABLE（無散戶原始貼文可直接判讀）。依新聞敘事推測偏多，但證據薄弱，不列為結論。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。
- yf `insider` 回傳空陣列，但 yf 認證已失敗，無法區分「確實無交易」與「取得失敗」。
- WebSearch 未找到 2026 年 10 月前後的董監持股轉讓申報內容。奇摩股市與公開資訊觀測站有相關頁面，但本次未能讀取實際內容。
- Notable：無法列出 CEO/CFO 或其他人員的買賣紀錄。

## Ownership shifts

- insidersPercentHeld：37.6%（yf major_holders，單一快照）。
- institutionsPercentHeld：7.8%；institutionsFloatPercentHeld：12.5%；institutionsCount：48。
- 趨勢（季度變化）：DATA_UNAVAILABLE（只有單期快照）。
- 解讀：內部人持股比例高，且機構持股占流通股比例偏低，代表籌碼主要集中在內部人與散戶，機構參與度有限。數字來自快照，不能判斷近期變化方向。

## Net sentiment score

- Composite：偏多（信心：低）。
  - 分析師端：7 買進 / 1 持有 / 1 賣出，偏多，但數據疑似過時，且新聞目標價分散。
  - 散戶端：DATA_UNAVAILABLE。
  - 內部人端：DATA_UNAVAILABLE。
  - 新聞敘事：漲價與 AI 需求偏多，CPO 規格替代風險偏空，兩者並存。
- Divergence flag：無法判定（散戶資料缺失）。若散戶確實偏空、分析師偏多，才會構成有資訊量的背離，目前無法驗證。

## Data gaps summary

| 項目 | 狀態 | 原因 |
|---|---|---|
| 分析師歷史評等變動 | DATA_UNAVAILABLE | 三期數據相同，疑似快取 |
| Reddit | DATA_UNAVAILABLE | 主機被封鎖 |
| StockTwits | DATA_UNAVAILABLE | 主機被封鎖 |
| 散戶聲量基準 | DATA_UNAVAILABLE | 無原始數據 |
| 6 個月內部人交易 | DATA_UNAVAILABLE | yf 認證失敗，網頁無內容 |
| 機構持股趨勢 | DATA_UNAVAILABLE | 僅單期快照 |
| 2026-11-05 當日資料 | DATA_UNAVAILABLE | 執行日為 11-04 |

SENTIMENT REPORT COMPLETE
