# Sentiment — 6257.TW (矽格) as of 2026-11-21

本報告引用的最新資料為 2026-11-18，未使用任何晚於 11-21 的資料。

## 資料來源狀態
- `pipeline/tools/yf.py` 可用的 kind 為 rec_summary、recommendations、insider、major_holders、inst_holders。
- Yahoo cookie/crumb 取得失敗（ConnectionError），但 rec_summary、recommendations、major_holders 仍有回傳值。
- insider 與 inst_holders 回傳空陣列，無法區分「沒有內部人交易」與「查詢失敗」，標示為 DATA_UNAVAILABLE。
- Reddit、StockTwits：台股覆蓋度預期極低，標示為 DATA_UNAVAILABLE。PTT、Mobile01 無法直接存取，WebSearch 也未找到相關討論串。

## Analyst consensus
目前可得的分析師樣本極少。rec_summary 與 recommendations 皆顯示：0m 期 1 strongBuy，其餘 buy、hold、sell、strongSell 皆為 0（即樣本數 N=1）。

近期評等與目標價變動（依 WebSearch 新聞彙整）：
- 2025-12（工商時報）：本土法人將評等調升至買進（Buy），並上修 2026 年營運預估。
- 2026-03（時報資訊）：本土法人調升至 Trading Buy，目標價 157 元。
- 2026-03（經濟日報）：法人調高矽格目標價，理由為 AI 等三大訂單動能，數字未確認。
- 約 2026-07（經濟日報）：法人預期隨價格續漲與新產能開出，調升目標價近四成，報導未給出具體數字。

矛盾點：Investing.com 顯示 12 個月平均目標價 328.00 元，但僅來自 1 位分析師且未註明日期，與 157 元目標價明顯不同，不宜直接比較。

## Retail social
- Reddit / StockTwits：DATA_UNAVAILABLE（未查詢，預期覆蓋極低）。
- PTT、Mobile01：無法直接存取，未找到可引用的討論摘要。
- CMoney、HiStock：可見留言多為提問，沒有形成明確多空共識。
- 聲量：無同期基準可比，無法判斷相對於平常的高低。11/17 成交量 7,697 張，11/3 至 11/18 日成交量多在 5,000 至 9,900 張之間。

主要話題（依股價與籌碼報導歸納，非社群原文統計）：
1. 法人目標價調升與 AI、ASIC、矽光子、高速運算訂單動能。
2. 新產能與中興三廠提前完工，客戶包下新產能。
3. 股價在 150 至 160 元區間震盪，11/17 大跌 6.73% 後於 11/18 反彈 2.95%。
4. 外資在 11 月初偏賣超（11/04 賣超 180 張、11/05 賣超 619 張、11/06 賣超 388 張）。

## 量能與基本面交叉檢查（單位：TWD 億）
| 項目 | 數值 | 來源與檢查 |
|---|---|---|
| 2026 年 6 月合併營收 | 19.59 億 | technews 報導；較 5 月約 -0.9% |
| 2026 年 1 至 6 月累計營收 | 111.74 億 | technews 報導，年增 18.1% |
| 2026 年 Q2 營收（推算） | 約 59.4 億 | 與報導「近 59 億、年增 23.06%」吻合 |
| Q2 每股稅後純益 | 2.55 元 | 報導值，淨利率約 21%（偏高，未能獨立驗證） |
| 市值 | 約 771.84 億 | 2026-11-06 快照，股價 159.5 元 |

## Insider activity
Net 6mo：DATA_UNAVAILABLE。yf insider 回傳空陣列，且 Yahoo cookie 失敗，無法區分無交易或查詢失敗。建議查 MOPS 的董監事持股餘額與內部人股權轉讓申報。

## Ownership shifts
- 內部人持股：7.87%（major_holders）
- 機構持股：19.11%；機構浮通股占比 20.74%；機構數 77 家
- 趨勢：DATA_UNAVAILABLE（僅有單一時點快照）。

## 籌碼與融資融券（補充）
- 融資餘額 11/3 至 11/18 約在 10,600 至 11,600 張之間，變動不大。11/17 下跌 6.73% 時融資僅減少約 207 張。
- 融券餘額約 22 張，券資比約 0.19%，空方部位極小。
- 11/17 收盤 152.50 元（-6.73%，成交 7,697 張）；11/18 收盤 157.00 元（+2.95%），本益比約 15.6 至 16.8（依不同來源）。
- 52 週區間 75.5 至 279.5 元（來源為 Investing.com，日期未明，僅供參考）。

## Net sentiment score
- 分析師面：偏多（bullish），但樣本僅 1 位，信心低。
- 散戶社群面：無可靠資料，無法判定傾向。
- 籌碼面：外資 11 月初偏賣，融資平穩，融券極少，整體偏中性。
- 內部人面：DATA_UNAVAILABLE。

綜合：偏多（bullish），信心低。主要依據是單一分析師評等與近期目標價上修方向，並非來自散戶或內部人的確認。

Divergence flag：無法判定（散戶傾向未取得可靠資料）。

SENTIMENT REPORT COMPLETE
