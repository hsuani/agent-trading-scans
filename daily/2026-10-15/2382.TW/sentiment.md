# Sentiment — 2382.TW (廣達 Quanta Computer) as of 2026-10-15

> 注意事項：本次 as-of 日期為 2026-10-15，但執行環境日期為 2026-10-14，因此所有資料實際最多只到 10-14 為止。

## Analyst consensus
目前 rec_summary 共 19 位分析師：5 Strong Buy / 12 Buy / 1 Hold / 0 Sell / 1 Strong Sell，買進方（含強力買進）佔 17/19，約 89%。

近 3 個月變化（-3m 對照 0m）：Strong Buy 由 6 降為 5，Buy 由 11 升為 12，Hold、Sell、Strong Sell 皆未變。總家數不變，屬於「一檔強力買進改列買進」的評等微調，沒有實質調降，也沒有賣方評等變動。

- 個別券商的升降評等 **DATA_UNAVAILABLE**：`recommendations` 指令回傳的仍是彙總計數，沒有逐筆紀錄，無法確認是哪一家券商調整。
- 外部彙整頁（非 yf 工具，未能核對原始來源）提到：Goldman Sachs Hold，目標 299 TWD（2026-06-17）；Nomura/Instinet Buy，目標 524 TWD，CLSA Buy，目標 415 TWD（2026-05-15）。這些都是五月至六月資料，且與 yf 的 19 家計數無法對應，僅供參考。
- 目標價：不同彙整頁數字不一，平均目標價約 375 TWD（26 家）與約 391 TWD（19 家）並存，目標區間為 250–524 TWD 或 240–425 TWD。以 histock 約 10 月初收盤 332 TWD 估算，相對平均目標價約有 +13% 至 +18% 的上行空間，但兩組數字來源不同，僅供參考。

## Retail social
- Reddit：**DATA_UNAVAILABLE**。直接抓取 Reddit 已被封鎖，且 WebSearch 沒有找到 2382 相關的 r/stocks 或 r/wallstreetbets 串文。
- StockTwits：**DATA_UNAVAILABLE**。未取得可用資料。
- PTT Stock / Dcard：**DATA_UNAVAILABLE**。WebSearch 未回傳 PTT 或 Dcard 的討論串，只有 histock 的 YouTuber 影片標題頁（如「後續如何看」「停損停利?」），沒有內文可判讀。
- 因此無法引用代表性的散戶原文，也無法估計討論量。以下散戶傾向是由新聞與籌碼面推論，信心偏低。
- 聲量（定性）：無法判斷與平常相比的水準，DATA_UNAVAILABLE。

新聞與媒體面的主要論述：
- 基本面偏正向：美系外資上調北美五大雲端業者 2027、2028 年資本支出預估約一成，點名廣達等 ODM 受惠。6 月合併營收創單月歷史新高，第二季營收突破一兆元。AI 伺服器訂單能見度延伸至 2027 年。Vera Rubin 預計本季逐步量產。
- 風險點：筆電業務受零組件漲價影響，下半年出貨展望保守。
- 股價面偏弱：histock 數據顯示，自今年高點回落約 36%，近一個月跌約 24%。
- 籌碼面：外資 7 月底單日大賣超約 2.7 萬張；投信自 7 月中旬起連續買超。
- 媒體標題反映多空拉鋸：「廣達除息苦貼息 外資調節 vs AI伺服器新品接棒」。

主要主題（依新聞與社群脈絡）：AI 伺服器需求與 CapEx 上修、Vera Rubin 量產時程、筆電拖累、外資賣壓與股價回檔、增資發行 GDR 的稀釋疑慮（七月公告，發行價約 287 TWD）。

## Insider activity
Net 6mo：**DATA_UNAVAILABLE**。`insider` 回傳空陣列，無法區分「確實無交易」與「資料來源（Yahoo cookie/crumb）取得失敗」。不以 $0 推論。
- 無法確認 CEO、CFO 或其他高階主管的買賣紀錄。
- 注意：林百里相關談話在新聞中被提及（4 月市場期待其談話），但未見內部人交易資料。

## Ownership shifts
- 內部人持股：約 29.7%
- 機構持股：約 33.9%（佔流通股約 48.2%）
- 機構家數：304
- `inst_holders` 回傳空陣列，**DATA_UNAVAILABLE**，無法看到個別機構的增減。
- 只有單一時點快照，無法判斷趨勢。新聞顯示外資七月大賣、投信七月中起買超，方向相反，但無法量化至季度層級。

## Net sentiment score
- 分析師面：**偏多（信心：中高）**。17/19 買進方，近三個月無賣方評等變動，僅有一檔強力買進改列買進。
- 散戶面：**無法可靠判斷（信心：低）**。Reddit、StockTwits、PTT、Dcard 皆無資料，只能由新聞與籌碼推論，偏謹慎。
- 內部人面：**DATA_UNAVAILABLE**。
- 籌碼與股價面：**偏弱**（外資賣超、股價較高點回落約 36%，投信買超）。
- 綜合：**中性偏多（信心：低至中）**。分析師評等偏多，但缺少散戶與內部人資料，股價動能偏弱，綜合判斷只能保守。

Divergence flag：**部分**。分析師傾向偏多，但股價動能與外資籌碼偏空，兩者方向相反。散戶傾向因資料缺失無法判定，因此無法確認是否與分析師相反，此旗標信心低。

## 結構化指標表

| 指標 | 數值 | 狀態 / 備註 |
|---|---|---|
| 分析師家數 | 19 | rec_summary 0m |
| 買進方（Strong Buy + Buy） | 17 | 約 89% |
| 持有（Hold） | 1 | 3 個月未變 |
| 賣出方（Sell + Strong Sell） | 1 | Strong Sell 1，Sell 0 |
| 近 3 個月評等變動 | Strong Buy -1、Buy +1 | 無降級至 Hold 或 Sell |
| 平均目標價 | 約 375 至 391 TWD | 來源不一，未核實 |
| 目標區間 | 250–524 或 240–425 TWD | 來源不一 |
| 內部人 6 個月淨買賣 | DATA_UNAVAILABLE | insider 回傳空值 |
| 內部人持股 | 29.7% | 單一快照 |
| 機構持股 | 33.9%（流通股 48.2%） | 機構 304 家 |
| 機構個別增減 | DATA_UNAVAILABLE | inst_holders 空值 |
| Reddit | DATA_UNAVAILABLE | 封鎖 / 無結果 |
| StockTwits | DATA_UNAVAILABLE | 未取得 |
| PTT / Dcard | DATA_UNAVAILABLE | 無討論串 |
| 散戶聲量 | DATA_UNAVAILABLE | 無法定性比較 |
| 股價相對今年高點 | 約 -36% | histock 數據 |
| 近一個月股價變動 | 約 -24% | histock 數據 |
| 外資 7 月大賣超 | 約 2.7 萬張（單日） | 新聞 |
| 投信買超 | 7 月中起連續買超 | 新聞 |
| 綜合情緒 | 中性偏多 | 信心低至中 |
| 背離旗標 | 部分 | 信心低 |

## 資料來源與限制
- yf 工具：recommendations、rec_summary、insider、major_holders、inst_holders。Yahoo cookie/crumb 取得失敗，已回退至 repo 快取。insider 與 inst_holders 為空值，recommendations 僅有彙總數字。
- WebSearch（非原始來源，多為彙整頁）：histock 籌碼與新聞、ltn 焦點股報導（4 月）、udn 除息與 AI 伺服器報導、kgi 研究報告（2026-08-13）、simplywall.st、investing.com、fintel、tradingview、valueinvesting.io。多數日期落在 4 月至 8 月，只有 histock 頁面與 udn 報導接近 10 月初。
- 彙整頁之間的目標價與價格互相矛盾，已如上標註，建議以即時行情與原始券商報告核對。
- 本報告不構成交易建議。

SENTIMENT REPORT COMPLETE
