# Sentiment — SPAI as of 2026-10-09

> 注意事項: 目前系統日期為 2026-10-08, 報告 as-of 日期 2026-10-09 晚於系統日期。本報告所用資料為 2026-10-08 當下可取得的最新資料, 不含 10-09 之後的任何資訊。

## Analyst consensus
3 buy / 0 hold / 0 sell (strongBuy 0, strongSell 0)。三個期間 (0m、-1m、-2m) 皆為 3 buy, 無變化。近期升評、降評與目標價調整資料, 本次 yf 工具未提供 (recommendations 僅回傳計數, 無逐筆變動, 無 price target 欄位)。覆蓋家數僅 3 家, 樣本偏少, 共識強度的參考價值有限。

Recent moves: 無可驗證的升降評紀錄。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 search.json 皆被代理伺服器拒絕 (CONNECT tunnel 403), 無法取得貼文數、分數與語氣。soft-fail, 未取得樣本。
- StockTwits / X: StockTwits API 無法解析 (DNS 查詢失敗 `api.stocktwits.com`), 未取得訊息流。
- 補充搜尋 (非 Reddit / StockTwits): 找到一個 Investing.com 的使用者多空紀錄頁 ([Safe Pro Scoreboard](https://www.investing.com/equities/safe-pro-scoreboard)), 記錄 2026-05 至 2026-08 的個人多空喊單。其中多數 6 月喊單在 6 月底前跌幅約 30% 以上, 一筆 7 月做多在 8 月中約漲 65%。此為散戶自行登錄的紀錄, 樣本少、非系統性調查, 不代表整體散戶情緒。
- 另有數個 2026-04 的 "Strong Buy" 網頁 (標題含 SPAI), 內容模板相同、散布於不相關網域, 評論區疑似自動生成, 可信度低, 未納入判斷。
- Buzz volume: 無法量化 (無可用提及數資料)。
- Tilt: 無法判定。
- Themes: 無可靠主題樣本。可見的使用者紀錄顯示 6 月以後多空分歧大、停損與回撤是討論焦點 (依有限樣本推測, 信心低)。

## Insider activity
查詢區間: 2026-04-09 至 2026-10-09 (6 個月)。

Net 6mo: $0 buys (公開市場買入), $4.0M sells (公開市場賣出)。

Notable:
- **Daniyel Erdberg, CEO**, 2026-09-09, 公開市場賣出 1,000,000 股, 約 $4.00/股, 總值約 $4.0M。yf 標示為 Ownership D (直接持有)。次要來源 (Quiver Quantitative) 估計約佔其持股 21.1%, 剩餘直接持股約 3,749,058 股。Webull 報導指稱為該公司近一年最大一筆內部人賣出。
- 公司未發布說明, 找不到出售理由的公開聲明。
- 其他 6 個月內紀錄多為授予或贈與, 非公開市場交易:
  - Brian William Mack (Officer), 2026-05-01, 授予 300,000 股 (價格 0)
  - Daniyel Erdberg (CEO), 2026-03-06 贈與 9,000 股 (已超出 6 個月窗口, 僅供參考; 2025-12-23 另有 24,000 股贈與, 亦超出窗口)
  - Jarret Daniel Mathews (COO), 2026-04-01 授予 20,000 股 (已超出 6 個月窗口)
- CFO Theresa Carlise 的 2025-08-22 授予 40,000 股在窗口外。次要來源提及 CFO 持股因 RSU 歸屬被扣繳稅款, 非公開市場賣出, yf 清單中未見對應紀錄。
- 解讀: 唯一的公開市場交易為 CEO 賣出。此為單一大額賣出, 不足以判定整體內部人態度。授予與贈與不構成買賣訊號。

Ownership (yf major_holders, 單一時點快照):
- Insiders 持股 45.47%
- Institutions 持股 12.06% (佔流通股 22.13%), 機構數 31 家
- 無歷史時序資料, 無法判斷機構集中度趨勢。

## Net sentiment score
Composite: **neutral 偏空 (mixed-to-bearish), 信心低**。

依據:
- 分析師: 偏多 (3/3 buy), 但覆蓋家數少, 且無逐筆升降評可驗證其動向。
- 內部人: 偏空傾向 (6 個月內 CEO 單筆約 $4.0M 公開市場賣出, 無公開市場買入)。
- 散戶: 無足夠資料, 不納入權重。僅有少量個人喊單紀錄, 方向分歧, 不具代表性。

Divergence flag: **無法判定 (no)**。散戶端資料缺失, 無法與分析師比較。若以分析師與內部人對照, 則存在明顯張力: 分析師全數 buy, 而 CEO 同期公開市場賣出。此張力值得追蹤, 但單一賣出的解讀不宜過度。

資料缺口 (建議下次補強):
- Reddit 與 StockTwits 在本環境無法存取, 散戶情緒為空白。
- 分析師逐筆升降評與目標價變動未取得。
- 機構持股無時序資料。
- CEO 9/9 賣出之 Form 4 原件未直接核對 (目前依 Quiver、Webull、Stock Titan 等次要來源交叉比對), 建議於 EDGAR 驗證價格與股數。

## Sources
- [Investing.com Safe Pro Scoreboard](https://www.investing.com/equities/safe-pro-scoreboard)
- [Quiver Quantitative: CEO sells 1,000,000 SPAI shares](https://www.quiverquant.com/news/Insider+Sale%3A+Chairman+and+CEO+of+%24SPAI+Sells+1%2C000%2C000+Shares)
- [Webull news on SPAI CEO sale](https://www.webull.com/news/15576523173086208)
- [Stock Titan SPAI SEC filings](https://www.stocktitan.net/sec-filings/SPAI)

SENTIMENT REPORT COMPLETE
