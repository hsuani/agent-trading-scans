# Sentiment — 6805.TW (富世達 Fositek) as of 2026-10-14

## Analyst consensus
9 家覆蓋：3 strongBuy / 6 buy / 0 hold / 0 sell（100% 買進傾向）。
近四個月結構：-3m 為 3 strongBuy / 5 buy（8 家），目前增加 1 家 buy，未見降評。yf recommendations 僅回傳彙總計數，無逐筆升降評紀錄。
目標價：cnyes 引述 FactSet 最新一次調查，9 家平均目標價 2600，中位數 2026 EPS 預估 66.17；較早一次 11 家調查目標價 2080。兩者發布日期未標示，無法精確排序，僅能定性為「目標價區間上修」。

## Retail social
- Reddit：r/stocks 與 r/wallstreetbets 搜尋皆回傳 "Claude Code is unable to fetch from www.reddit.com"，本次無法取樣貼文，soft-fail。
- StockTwits / X：StockTwits API 解析失敗（getaddrinfo ENOTFOUND api.stocktwits.com），soft-fail。X 端未取得可用貼文。
- 替代來源（CMoney 股市爆料同學論壇，日期未標示）：多空分歧。偏多者提到機構與 ETF 部位變動的題材；偏保守者擔心 ETF 輪動風險、成交量偏低，認為需要正面催化劑。此為使用者貼文，屬弱訊號。
- 外部題材：一則 Yahoo 台灣標題將富世達連結至 AI 伺服器供應鏈，並提及高盛將其列入 AI 液冷概念買進名單（日期與內容未能驗證）。
- 聲量：無法量化提及數。論壇與新聞層級可見討論，但未見明顯爆量訊號，定性為低至中等。
- 主要議題（重複出現）：AI 液冷與伺服器題材、ETF 持股變動、股價波動後的回檔風險、成交量是否足以支撐。

## Insider activity
Net 6mo：無法確認淨額。yf insider 回傳空陣列（無交易紀錄），但 Yahoo cookie/crumb 取得失敗，無法區分「確實無交易」與「資料缺失」，兩者目前無法區分。
- 背景（網路搜尋，次要來源）：玩股網週資料顯示董監持股比例於 2026-05 至 2026-07 維持 19.99%，無變動。
- 董事會：2026-05-26 股東常會改補選董監，目前董事 9 席；董事長黃祖模，總經理徐安賜（MONEY LINK 基本資料）。
- 未找到 2026 年董監事持股轉讓申報的具體公告。
- Notable：無。建議直接查公開資訊觀測站「董監事持股轉讓申報」與「內部人持股轉讓事前申報」以補足。

## Ownership shifts
- 內部人持股 21.12%（yf insidersPercentHeld，與玩股網 19.99% 口徑不同，屬正常差異）。
- 機構持股 39.96%（占已發行股數），占流通股數 50.66%，機構家數 83。
- 趨勢：yf 僅提供單一時點快照，無法判斷機構集中度的時間變化，趨勢標示為 N/A。
- 股價事件：時報新聞提及 2026 年 7 月初曾被證交所列為注意股（收盤價 1490.00）。

## Net sentiment score
Composite：**偏多（bullish lean）**，信心度 **低至中**。
- 分析師：強偏多（9 買 / 0 持有 / 0 賣，目標價上修）。
- 零售：分歧，無 Reddit 與 StockTwits 資料，僅有論壇弱訊號，無法作為強依據。
- 內部人：無法判定，資料缺失。
- 扣分理由：零售與內部人兩個維度缺資料，且目標價與股價日期不一致，無法與當前股價對照估值空間。

Divergence flag：**否**。零售傾向為分歧而非明顯看空，與分析師的偏多方向未呈現反向背離。惟零售資料不足，此判斷信心有限。

## 指標表

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 覆蓋分析師家數 | 9 | yf rec_summary（0m） |
| strongBuy / buy / hold / sell | 3 / 6 / 0 / 0 | yf rec_summary（0m） |
| 近三個月買進家數變化 | 8 → 9（+1 buy） | yf rec_summary（-3m 對比 0m） |
| 平均目標價 | 2600（9 家，FactSet） | cnyes 引述，日期未標示 |
| 前次目標價 | 2080（11 家） | cnyes 引述，日期未標示 |
| 中位數 2026 EPS 預估 | 66.17 | cnyes 引述 |
| 最近可得股價 | 1835.00（2026-08-13） | MONEY LINK，非 10-14 即時價 |
| 內部人 6 個月淨買賣 | N/A（資料缺失） | yf insider 回傳空陣列，無法確認 |
| 董監持股比例 | 19.99%（穩定） | 玩股網週資料（次要來源） |
| 內部人持股（yf） | 21.12% | yf major_holders |
| 機構持股（占已發行） | 39.96% | yf major_holders |
| 機構持股（占流通） | 50.66% | yf major_holders |
| 機構家數 | 83 | yf major_holders |
| 機構持股趨勢 | N/A | 僅單一快照 |
| Reddit 樣本數 | 0（抓取失敗） | WebFetch 被拒 |
| StockTwits 樣本數 | 0（連線失敗） | DNS 解析失敗 |
| 零售聲量 | 低至中（定性） | 論壇與新聞可見，無量化 |
| 綜合情緒 | 偏多，信心低至中 | 本報告判斷 |
| 背離旗標 | 否 | 零售分歧，非反向 |

## 資料限制
- yf 的 cookie/crumb 取得失敗，已降級執行，資料是否來自快取未能確認。
- Reddit 與 StockTwits 本次均不可用。
- 網路搜尋結果的日期多數未標示，數字應視為參考，並非當日即時數據。
- 本報告為情緒觀察，不構成交易建議。

## Sources
- [CMoney 股市 6805 研究報告](https://www.cmoney.tw/forum/stock/6805?tab=report)
- [CMoney 股市 6805 專欄](https://www.cmoney.tw/forum/stock/6805?tab=column)
- [MONEY LINK 6805 基本資料](https://ww2.money-link.com.tw/TWStock/StockBasic.aspx?SymId=6805)
- [MONEY LINK 6805 股價走勢](https://ww2.money-link.com.tw/TWStock/StockChart.aspx?symid=6805)
- [cnyes 新聞 6368768](https://news.cnyes.com/news/id/6368768)
- [cnyes 新聞 6535038](https://news.cnyes.com/news/id/6535038)
- [Yahoo 台灣股市 富世達 10 月營收新聞](https://tw.stock.yahoo.com/news/%E6%A5%AD%E7%B8%BE-%E9%9B%BB%E9%9B%B6%E7%B5%84-%E5%AF%8C%E4%B8%96%E9%81%9410%E6%9C%88%E7%87%9F%E6%94%B6%E7%82%BA13-05%E5%84%84%E5%85%83-%E5%B9%B4%E5%A2%9E43-062528783.html)
- [玩股網 6805 股東結構](https://www.wantgoo.com/stock/6805/major-investors/concentration)
- [時報資訊 6805 個股頁](https://wantrich.chinatimes.com/tw-market/listed/stock/6805)
- [時報資訊 2026-04-28 新聞](https://wantrich.chinatimes.com/news/20260428900151-420101)
- [時報資訊 2026-07-08 新聞](https://wantrich.chinatimes.com/news/20260708900127-420101)

SENTIMENT REPORT COMPLETE
