# Sentiment — 6257.TW (矽格) as of 2026-11-07

## Executive summary
6257.TW 的情緒資料很不完整。yf 工具的 Yahoo cookie/crumb 取得失敗，內部人交易回傳空陣列，分析師資料只有 1 位分析師。散戶討論的 WebSearch 沒有找到 PTT、Dcard 或論壇內容，也沒有 11 月的評等或目標價。綜合判斷為中性，信心低。2026 年股價大幅上漲（約 130 元漲到 200 元以上），這是價格脈絡，不能當成情緒訊號。

## Data availability
| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations | 部分可用 | 回傳的只有 0m 與 -1m 的彙總，沒有歷史評等變動明細 |
| yf rec_summary | 可用 | 0m 與 -1m 各為 1 strongBuy，其餘為 0 |
| yf insider | 空 | 回傳 []，無法區分「真的沒有交易」與「資料抓取失敗」 |
| yf major_holders | 可用 | 單一時點快照，沒有季度趨勢 |
| Reddit (r/stocks, r/wallstreetbets) | 未查詢 | 依任務限制只用 WebSearch 查散戶情緒；這兩個版主要討論美股，對台股覆蓋很少 |
| StockTwits | 未查詢 | 屬於財經網站，依規則不以 WebFetch 存取 |
| WebSearch（散戶與新聞） | 部分可用 | 找到 2025 年底至 2026 年 8 月的新聞與股價；沒有 PTT/Dcard 結果，沒有 11 月資料 |

Yahoo 的 cookie/crumb 取得失敗，因此 insider 結果可能不完整。

## Retail / social sentiment read
- 聲量：無法量化。WebSearch 沒有找到 PTT 股板或 Dcard 的相關討論，也沒有可計算的提及次數。
- 傾向：無法判定（bullish / bearish / mixed 都無資料支持）。
- 主題（來自新聞，不是散戶貼文）：營運與 AI、矽光子、高速網通與 HPC 測試需求；產能擴充（湖口廠部分廠區 7 月量產，竹東中興新廠預計 2027 年第一季量產）。
- 代表性散戶觀點：無可引用樣本。
- 結論：無法判斷散戶與分析師是否背離，因此不做 divergence 判定。

## Analyst consensus
目前 1 buy / 0 hold / 0 sell（rec_summary，strongBuy 計 1）。覆蓋極薄，只有 1 位分析師。
近期變動：
- 2025 年 12 月的新聞提到，本土法人將評等調升為買進，並上修 2026 年營運數據。這是 2025 年底的資料，無法確認目前是否仍有效。
- 2026 年 7 月營收約新台幣 20.1 億元，年增約 27%，1–7 月累計約 131.9 億元，年增逾 19%（新聞來源，未經 yf 驗證）。
- 2026 年資本支出預算約 59.3 億元，年增約 25%（2025 年底新聞）。
- 目標價：無資料。

## Institutional / insider signal
- 內部人：yf insider 回傳空陣列，6 個月淨買賣金額無法計算。無法確認 CEO/CFO 是否有交易。
- 內部人持股：約 7.87%（major_holders insidersPercentHeld）。
- 法人持股：約 18.7%（institutionsPercentHeld），占流通股約 20.3%，機構數 77。
- 趨勢：只有單一快照，無法判斷機構集中度是上升或下降。

## Overall sentiment verdict
- 分析師面：偏多但樣本極小（1 buy），且最近的評等資料可能已過時。
- 散戶面：無資料。
- 內部人面：無資料（工具回傳不可靠）。
- 綜合：中性，信心低。
- Divergence flag：無法判定（no）。散戶資料缺失，無法比較兩者傾向。

建議後續補充：Yahoo cookie 恢復後重跑 insider 與 recommendations；PTT 股板或 Dcard 關鍵字搜尋；11 月法說會與券商報告。

## Sources
- yf 工具輸出：`pipeline/tools/yf.py 6257.TW recommendations | rec_summary | insider | major_holders`（2026-11-07 執行）
- WebSearch（工商時報、中時財經等 2025 年底新聞）：https://www.ctee.com.tw/news/20251226700828-430201 ； https://wantrich.chinatimes.com/news/20251226900303-420101
- WebSearch（Yahoo 股市、MONEY LINK、統計狗等股價頁面）：https://tw.stock.yahoo.com/quote/6257/profile ； https://ww2.money-link.com.tw/TWStock/StockChart.aspx?SymId=6257 ； https://statementdog.com/analysis/6257
- 注意：統計狗頁面的「10/16 收盤價 252 元」未標明年份，無法確認是否為 2026 年資料，因此未採用為當前價格。

SENTIMENT REPORT COMPLETE
