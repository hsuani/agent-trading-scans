# Sentiment — 6515.TW（穎崴）as of 2026-10-10

> 資料時效注意：系統當日為 2026-10-09，本報告以 2026-10-10 為目標日期，但 10/10 當日資料尚未產生，所有數字以 10/09 前可取得的最新資料為準。部分來源未標示日期，已逐項註明。

## Analyst consensus

yf `rec_summary` 回傳 12 家券商：Strong Buy 4 / Buy 8 / Hold 0 / Sell 0 / Strong Sell 0。過去 3 個月分布穩定（-3m 為 4 Strong Buy / 6 Buy），無 Hold 或 Sell。

Recent moves（新聞來源，未標日期者已註明）:
- 花旗：目標價由 6,000 升至 10,000 元，之後 Investing.com 紀錄顯示 2026/05/28 再升至 13,000 元。
- 高盛：目標價由 6,300 升至 15,000 元，為報導中的最高目標價，評等買進，5 月維持不變。
- 野村/Instinet：2026/07/24 首次給予買進，目標價 8,315 元，為報導中的最低目標價。
- 12 個月平均目標價約 12,012 元（來源：Investing.com 彙整，時點不明）。
- 上述目標價與近期股價落差大，需以券商原始報告為準。

限制：yf `recommendations` 只回傳與 `rec_summary` 相同的月度計數，無個別評等變動明細（upgrade/downgrade 逐筆），因此無法確認 2026/10 的評等異動。新聞彙整的 10 家與 yf 的 12 家數量不一致，屬來源口徑差異。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 回報無法連線至 www.reddit.com，本次未取得任何貼文。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 連線失敗（DNS 解析失敗），本次未取得訊息量或多空標籤。
- PTT / Dcard：本次搜尋未找到可用的股市討論串，DATA_UNAVAILABLE。
- CMoney 股市爆料同學會（搜尋摘要，未標日期，約 9 月中旬前後）：多空意見分歧。部分網友對近期跌幅悲觀，部分認為後市被看好；整體以觀望為主。此為論壇摘要，非全體散戶的量化結果。
- 聲量：無可量化的提及次數，無法與歷史基準比較，標記為 DATA_UNAVAILABLE。

Themes（依新聞與論壇摘要歸納）:
- AI 與 HPC 需求帶動營收：公司 2026/05 自結營收年增 119.79%，2026/09 營收 12.5 億元、年增 87.72%，為十年同期單月新高（來源：nStock，截至 10/07）。
- 股東會與股利：2026/06 股東會後股價一度重返萬元關卡；董事會決議每股現金股利 50 元（盈餘分配 25 元加資本公積 25 元），為掛牌以來新高。
- 籌碼分歧：有網友指外資持續買進、投信持續賣出，法人買賣方向不一致（來源：CMoney 論壇摘要）。
- 短線波動：2026/07/17 單日下跌約 9.42%；9 月初起股價自低檔回升（來源：玩股網）。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。

- yf `insider` 回傳空陣列，但同次呼叫的 Cookie/crumb 取得失敗（ConnectionError），無法判斷是「無交易」還是「資料抓取失敗」，因此不能視為零交易。
- 新聞搜尋未找到 2026 年董監事持股轉讓或申報的具體股數與金額。
- 已知治理事件：2026/06/17 股東常會完成董事全面改選，董事長暨總經理為王嘉煌，財務長為李振昆，另有 4 席獨立董事（來源：CTEE）。
- Notable: 無可確認的 CEO/CFO 買賣紀錄。需至公開資訊觀測站（MOPS）查詢「內部人持股轉讓事前申報」與「持股異動」以確認。

## Ownership shifts

yf `major_holders`（時點不明）:
- 內部人持股 29.48%
- 機構持股 30.32%（佔流通股 43.0%）
- 機構家數 114 家

趨勢：本次工具僅回傳單一時點快照，無歷史序列，無法判斷集中度是升或降。外資與投信買賣方向不一致（見上方論壇摘要），機構集中度趨勢標記為 INCONCLUSIVE。

## Price reference（用於交叉比對，非情緒來源）

來源之間價位不一致，需以交易所當日收盤核對：
- nStock（截至 2026/10/07）：約 5,530 元，近一周均價約 5,941 元。
- 玩股網（未標日期）：6,055 元，單日跌 630 元（-9.42%）。
- 其他新聞：2026/08/05 成交價 6,885 元；2026/09/09 收盤 7,280 元；2026/09/11 收盤 6,890 元。
- 52 週區間：約 1,065 至 11,490 元（來源：Investing.com，時點不明，低點數字可能為資料錯誤）。

## Net sentiment score

- 分析師面：偏多。12 家全數買進或強力買進，無 Hold 或 Sell；目標價區間 8,315 至 15,000 元，遠高於近期股價（信心：高，但來源為計數與新聞彙整）。
- 散戶面：分歧，偏中性。論壇摘要顯示多空並存，缺乏 Reddit、StockTwits、PTT 量化資料（信心：低）。
- 內部人面：DATA_UNAVAILABLE，無法納入評分。
- 綜合：偏多（Bullish lean），信心中等。依據主要來自分析師一致性與基本面成長數據，散戶面資料不足。

Divergence flag: 目前無法判定。散戶面資料缺漏，且論壇摘要未標日期，無法可靠比較散戶與分析師方向。若後續取得 Reddit、StockTwits 或 PTT 量化資料，再重新評估。

## Data gaps summary

| 來源 | 狀態 |
|---|---|
| yf rec_summary | 取得（12 家，月度計數） |
| yf recommendations | 僅有計數，無逐筆評等變動 |
| yf insider | 空陣列，Cookie 失敗，無法確認 |
| yf major_holders | 取得（單一時點） |
| Reddit | DATA_UNAVAILABLE（連線被拒） |
| StockTwits | DATA_UNAVAILABLE（DNS 失敗） |
| PTT / Dcard | DATA_UNAVAILABLE（無可用結果） |
| WebSearch 新聞與論壇 | 部分取得，多數未標日期 |

SENTIMENT REPORT COMPLETE
