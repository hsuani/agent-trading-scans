# Sentiment — 2344.TW (華邦電 Winbond Electronics) as of 2026-10-29

資料完整度: 低。Reddit 與 StockTwits 無法取得，X/新聞搜尋找不到 2026 年 10 月的內容，內部交易資料為空。以下結論主要依賴 yf 分析師評等快照，其餘面向只能標示為資料缺口。

## Analyst consensus

yf 快照 (0m): 8 buy (strongBuy 4 / buy 4) / 0 hold / 0 sell。

近三個月趨勢 (yf 月度快照):

| 期間 | strongBuy | buy | hold | sell | 合計 |
|---|---|---|---|---|---|
| 0m (當前) | 4 | 4 | 0 | 0 | 8 |
| -1m | 4 | 4 | 0 | 0 | 8 |
| -2m | 4 | 3 | 0 | 0 | 7 |
| -3m | 3 | 2 | 1 | 0 | 6 |

Recent moves: 過去三個月買方評等由 6 家增至 8 家，hold 由 1 家降至 0，未見 sell 評等。yf 的 `recommendations` 指令回傳的仍是上述月度彙總，沒有逐筆升降評等紀錄，因此無法確認是哪家券商升評或降評。

Target price: 網路搜尋找到的目標價資料彼此不一致且日期不一。JPMorgan 2026-07-15 的 Buy 評等目標價 360 TWD 為其中唯一有明確日期與券商歸屬的一筆；其他聚合來源的平均目標價落在約 183.6 至 234 TWD 之間，且股價快照差異很大 (最近一筆 171.5 TWD，日期格式不明)。這些數字無法確認為 2026-10-29 當時的狀態，只能作為參考。

Coverage 規模衝突: yf 快照顯示 8 家；另一聚合來源列出 15 家 (6 buy、8 strong buy、1 hold)；Simply Wall St 記載 2026-04 時為 9 家。三者口徑不同，此處以 yf 為主，並標示差異。

## Retail social

- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 search.json 回傳 "Claude Code is unable to fetch from www.reddit.com"，本報告無法評估討論量或帖文傾向。
- StockTwits / X: StockTwits 因 api.stocktwits.com DNS 解析失敗無法連線，需於 session 網路設定中放行該網域後才能重試。X 端只有一般 WebSearch，未找到 2026 年 10 月的個股討論。
- 聲量 (buzz volume): 無法與歷史基準比較，標示為未知。
- Tilt: 無法判定 (bullish / bearish / mixed 均無樣本)。
- Themes: 無可引用之主題。搜尋結果中僅有 Winbond 的公司簡介與價格歷史頁面，不屬於散戶討論。

## Insider activity

Net 6mo: 資料缺口。`insider` 指令回傳空陣列，無法區分「六個月內無申報交易」與「資料源未涵蓋」。目前沒有可引用的買賣金額或職位。

Ownership (yf major_holders): insiders 持股 30.26%，institutions 持股 26.51% (佔 float 38.01%)，機構家數 209。`inst_holders` 回傳空陣列，無法判斷機構持股近期是增加或減少，因此「ownership shifts」只能呈現單一時點數字，趨勢未知。

## Net sentiment score

Composite: 偏多 (bullish)，信心低。

- 分析師面: 偏多。8 buy / 0 sell，且買方家數三個月內增加。
- 散戶面: 無資料。
- 內部人面: 無資料 (空陣列)。
- 機構面: 持股比重 26.5% 為中等，但無時間序列，不予加權。

Divergence flag: 無法判定 (no) — 散戶資料缺席，無法檢驗散戶傾向是否與分析師相反。若後續補上 Reddit 或 StockTwits 資料，才能執行此項比對。

資料缺口與後續:
1. 開放 api.stocktwits.com 網域後重新抓取。
2. Reddit 需以其他途徑取得 (官方 API 或代理)。
3. 內部交易需確認 yf insider 來源是否涵蓋台灣上市公司；若不涵蓋，應改用 MOPS 董監事持股申報。
4. 網路搜尋中 2337 (旺宏 Macronix) 的結果與本股無關，已排除，未納入任何數字。

SENTIMENT REPORT COMPLETE
