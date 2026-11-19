# Sentiment — FANUY as of 2026-11-20

資料來源狀態：yf 工具可用（analyst / insider / ownership）；Reddit 無法連線；StockTwits 因網域未允許而無法解析；X/新聞僅有過時資料。整體覆蓋不足，本報告信心偏低。

## Analyst consensus
ADR 覆蓋極薄，僅 2 位分析師。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當期 (0m) | 1 | 0 | 1 | 0 | 0 |
| 一個月前 (-1m) | 0 | 0 | 2 | 0 | 0 |

近期變動：合計家數不變，由 2 Hold 變為 1 Strong Buy + 1 Hold，推斷為一位分析師由 Hold 升評為 Strong Buy（由彙總數字推論，未能確認券商與日期）。`recommendations` 端點未回傳個別評等變動事件，無法列出逐筆升降評。ADR 層級的目標價資料未取得。

母公司線（TSE 6954，僅供背景參考，不等同 ADR）：
- stockanalysis.com 彙整約 20 位分析師 Buy 評等，平均目標價約 ¥7,380（頁面日期 2026-06-16）。
- Investing.com 彙整為 8 Buy / 10 Hold / 2 Sell（頁面未標日期）。
- PriceTargets.com 對 FANUY 顯示 "Strong Buy"，但僅 2 位分析師，自 2025-10 起未更新。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：抓取失敗，無法連線 www.reddit.com。無樣本討論串，無法判定聲量與傾向。
- StockTwits：api.stocktwits.com 無法解析，未取得資料。需在工作階段網路設定中允許該網域後才能重試。
- X / 新聞：網路搜尋未找到 2026-11 的散戶討論，搜得的結果多為 2025 年財報與未標日期的技術面頁面，不可作為當期散戶情緒證據。
- 聲量：無法量測。以 ADR 覆蓋規模推斷，散戶討論量應偏低，但這只是推論，非實測。
- 主題（僅見於分析師端與彙整來源）：
  - 財報優於預期後的 EPS 上修（2025-11 的報導）。
  - TipRanks 指出估值偏高、短期動能偏弱。
  - Investing.com 技術面訊號為 "Strong Sell"（日期不明，可能已過時）。

## Insider activity
Net 6mo：$0 buys / $0 sells（`insider` 端點回傳空清單，無可用交易紀錄）。
Notable：無。
注意：FANUC 為日本上市公司，不適用美國 Form 4 申報制度，空結果不代表內部人士無交易，僅表示此工具無資料。

## Ownership shifts
- 機構持股比例：0.186%（yf 欄位值 0.00186），機構家數 27。
- 內部人持股：0.0%（同樣受資料來源限制，不代表實際持股為零）。
- 此持股比例明顯偏低，推測 yf 僅涵蓋美國申報可見的持股，未涵蓋東京上市股的完整股東結構。
- 無時間序列資料，無法判定集中度趨勢。

## Net sentiment score
Composite：**中性（neutral）**，信心：**低**。
- 分析師端：輕度偏多（1 Strong Buy、1 Hold、0 Sell，且有升評跡象），但樣本僅 2 人。
- 散戶端：無資料。
- 內部人端：無資料。
- 持股端：無趨勢資料。

Divergence flag：**無法判定**。散戶傾向無法量測，因此無法確認是否與分析師傾向相反。

資料缺口清單：
1. Reddit 兩個子版無法存取。
2. StockTwits 網域未允許。
3. ADR 目標價與逐筆評等變動缺失。
4. 內部人交易資料對日股不適用或為空。
5. 機構持股趨勢缺失。

日期註記：執行環境當日為 2026-11-19，本報告依指示標示為 2026-11-20 的 as-of 日期，資料實際取得於執行當日。

SENTIMENT REPORT COMPLETE
