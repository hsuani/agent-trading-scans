# Sentiment — FANUY as of 2026-10-23

資料品質提醒：本次取得的 yf 資料有多項欄位缺漏（Yahoo cookie/crumb 取得失敗），Reddit 與 StockTwits 皆無法取得，零售情緒部分僅能以搜尋摘要替代，置信度偏低。

## Analyst consensus
目前 rec_summary 為 0 buy / 2 hold / 0 sell（BUY 比例 0%）。前一期（-1m）分布相同，近期無評等變動紀錄。recommendations 歷史表回傳與 rec_summary 相同的兩筆快照，無法看出升降評等或目標價調整歷程。

搜尋摘要提到的其他分析師資料均為較舊資訊：MarketBeat 2025 年有 UBS 由 hold 升為 strong-buy 的紀錄（2025-05），且有 consensus target 23.00 USD 的聚合頁面，但樣本數少，且不屬於 2026 年資料，不能當作現況。

| 項目 | 數值 |
|---|---|
| Strong Buy / Buy | 0 / 0 |
| Hold | 2 |
| Sell / Strong Sell | 0 / 0 |
| BUY 比例 | 0% |
| 近期評等變動 | 無可辨識紀錄 |

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得，兩個 search.json 端點皆被封鎖（WebFetch 回報無法連線）。WebSearch 也未找到相關討論串，無法判斷發文量與多空傾向。
- StockTwits：無法解析 api.stocktwits.com 網域，資料缺失。
- StockTwits / X / 新聞：WebSearch 僅找到 Investing.com 的技術面訊號頁，顯示日線技術指標為 Strong Sell（價格 19.02 USD，標註日期為 2026-08-21，已過時）；另一篇 Seeking Alpha 文章認為股價距近期高點約 43% 折價、成長預期存疑，且作者偏好產業 ETF 而非直接持有，屬於偏謹慎的意見。
- 聲量：無法量化，定性判斷為低。FANUY 為 OTC ADR，流動性與討論度本來就較低。
- Themes（由有限來源歸納）：估值與波動偏高、成長預期疑慮、即將公布的財報（搜尋摘要標示為 2026-10-22）。

Representative take（來自 Seeking Alpha 標題，≤15 字）：「too volatile for my preference」。

## Insider activity
yf insider 回傳空陣列，過去 6 個月無可見的內部人交易紀錄，淨買賣金額為 0。由於資料源可能不完整，此結論僅代表 yf 可取得的資料範圍，不代表實際無交易。

## Ownership shifts
- 機構持股 (institutionsPercentHeld): 0.00229（原始值，數值為比例格式，解讀上需保守）
- 機構家數 (institutionsCount): 27
- 內部人持股 (insidersPercentHeld): 0.0
- 時間序列：無，無法判斷機構持股是增加或減少。
- 機構資金流向結論：無法判定淨流入或淨流出。

## Net sentiment score
Composite: **中性偏謹慎（neutral-to-bearish lean）**，置信度：**低**。
- 分析師端：0 buy / 2 hold，無買進評等，偏中性；缺乏正面共識。
- 零售端：無可用的 Reddit / StockTwits 資料，只有少量偏空的技術面與估值論述，不足以構成可靠的零售傾向。
- 內部人端：無交易紀錄，中性。
- 機構端：無時間序列，無法判斷流向。

Divergence flag: **無法判定**。零售端資料缺失，無法與分析師端比較。另外，搜尋摘要標示財報日為 2026-10-22（DATE 前一日），財報後的分析師調整與市場反應未納入本次資料，建議於 DATE 後複查 rec_summary 與新聞。

SENTIMENT REPORT COMPLETE
