# Sentiment — 1815.TWO (富喬工業) as of 2026-11-06

資料狀態：DATA_UNAVAILABLE（分析師評等與散戶社群來源皆無法取得最新資料，以下僅為部分替代資訊，時效性不足）。

## Analyst consensus
資料狀態：無法取得。`yf rec_summary` 與 `yf recommendations` 回傳全部為 0 或空陣列，原因是 Yahoo cookie/crumb 取得失敗（ConnectionError），不代表該股無券商覆蓋。
- 券商目標價與評等（buy / hold / sell）：本次無法確認，搜尋結果也未找到 2026 年的券商目標價區間。
- 近期升降評：無資料。
- 替代參考：2026 年第一季合併營收 18.81 億元（TWD）、稅後純益 4.58 億元、EPS 0.79 元、毛利率約 36%、營益率約 21%。上半年 EPS 約 2.24 元（來源為 goodinfo 新聞列表標題）。股東會通過每股 1 元股利（現金 0.5 元加股票股利 0.5 元）。這些是基本面資料，不是分析師評等。

## Retail social
- Reddit: 無法取得。r/stocks 與 r/wallstreetbets 的 public JSON 被阻擋（WebFetch 回傳無法連線），本次無樣本，無法判定散戶語氣。
- StockTwits / X: StockTwits API 因網路設定無法解析主機（api.stocktwits.com 需在 session 網路白名單中開放）。X 與新聞搜尋僅找到股價與財報類頁面，沒有可辨識的散戶情緒文章，無法引用代表性言論。
- Themes（由新聞與產業報導歸納，非社群樣本）：
  - 高階玻纖布供需：報導指出全球高階玻纖布市場供不應求，供給端主要由日東紡主導，市場預期供需吃緊可延續二至三年。
  - 2026 年 1 月納入 MSCI 全球小型指數成份股。
  - 股價資料來源彼此不一致（有頁面顯示 147 元，日期為 10/21；另一頁顯示 95.00，日期為 07/09），無法確認最新價位，此處不據以判斷情緒。
- 散戶語氣（推定）：無直接樣本，暫定為中性，信心低。

## Insider activity
資料狀態：無法取得。`yf insider` 回傳空陣列，且 Yahoo 認證失敗，無法確認。本次不提供 6 個月淨買賣金額，也不列出 CEO / CFO 交易紀錄。
- 注意：Yahoo 的 insidersPercentHeld 為 23.94%，這是持股比例，不是交易資料。

## Ownership shifts
- 機構持股比例（Yahoo major_holders）：institutionsPercentHeld 約 10.31%，institutionsFloatPercentHeld 約 13.56%，機構數量 22 家。此為單一時點快照，無趨勢比較。
- 外資與投信持股（nstock，2026 年 9 月中旬）：外資約 27.11%，投信約 13.35%。
- 法人買賣超軌跡（時序，由搜尋結果彙整）：
  - 2026 年 4 月 9 日前後：外資買超金額位列前幾名，投信未列前幾名。
  - 2026 年 7 月初：外資賣超（wantgoo 欄位對應不完整，投信數字無法確認）。
  - 2026 年 8 月中旬：外資單周買超約 4.56 萬張，股價漲幅約 22%（goodinfo 新聞標題）。
  - 2026 年 9 月中旬：外資與投信同日皆賣超，外資賣超約 1.04 萬張，投信賣超約 0.15 萬張（nstock 近 10 日明細）。9 月 11 日投信曾買超約 0.76 萬張。
- 2026 年 11 月的法人買賣超：無資料。最新可得資料停在 9 月中旬，距本報告日約 7 週，時效不足。

## Net sentiment score
Composite: neutral（信心：低）。
- 分析師面：無資料，無法評分。
- 散戶面：無直接樣本，暫定中性。
- 法人面：外資在 8 月大幅買進後於 9 月轉為賣超，方向不穩定，但資料距今已久。
- 基本面與產業新聞偏正面（EPS 成長、股利、高階玻纖布供需），但這不等同於情緒指標。

Divergence flag: no（無法判定）。因分析師與散戶兩端皆無有效資料，無法確認兩者是否背離。

## 摘要
analyst % BUY：無資料（Yahoo 認證失敗，無法計算）；institutional flow：外資 9 月中旬轉為賣超，最新資料停在 9 月，11 月無資料；retail tone：無法取得 Reddit / StockTwits 樣本，暫定中性（信心低）。

## Data gaps（待補）
1. Yahoo cookie/crumb 認證失敗：需修復 yf 工具後重跑 rec_summary、recommendations、insider。
2. Reddit public JSON 被阻擋：需在網路白名單開放 www.reddit.com，或改用其他來源。
3. StockTwits 主機無法解析：需在 session 網路設定中允許 api.stocktwits.com。
4. 11 月法人買賣超：建議直接查台灣櫃買中心法人資料，或 nstock、goodinfo、玩股網的 1815 籌碼明細。

SENTIMENT REPORT COMPLETE
