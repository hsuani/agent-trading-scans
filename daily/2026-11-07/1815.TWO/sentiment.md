# Sentiment — 1815.TWO (富喬工業 Fulltech Fiber Glass) as of 2026-11-07

> 資料完整度低: 本次多數來源失敗, 以下結論僅供參考, 不構成可靠情緒判斷。

## Analyst consensus
資料無法確認。yfinance `rec_summary` / `recommendations` 回傳 0 buy / 0 hold / 0 sell, 但同一次呼叫伴隨 Yahoo cookie/crumb 取得失敗 (ConnectionError), 0 值應視為「未取得」而非「無評等」。
- 網路搜尋得到的 TradingView 快照僅顯示單一目標價 128 TWD, 未提供完整評等分布。
- 快照股價約 91.8 TWD (一週跌約 10%) 與另一快照約 96.6 TWD (記錄高點 117.5 TWD, 日期 2026-01-20) 互相矛盾, 日期不明, 視為過時。
- 近期升級/降級與目標價變動: 無可靠資料。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得, 請求被網站封鎖 (WebFetch 無法連線 www.reddit.com)。無法評估討論量或多空傾向。
- StockTwits: 無法取得, api.stocktwits.com 無法解析 (DNS 失敗), 需在 session 網路設定中允許該網域。
- X / 新聞: 一般搜尋未找到 2026-11 的相關意見文章, 僅有無日期的行情與資料頁面。
- 討論量 vs 一般水準: 無法判定。
- 主題: 無可靠樣本。公司主要業務為電子級與工業級玻璃纖維紗及布, 主要應用於印刷電路板 (PCB) 材料, 這是可辨識的基本面背景, 但不是散戶情緒的直接證據。

## Insider activity
Net 6mo: 無法確認。yfinance `insider` 回傳空陣列, 同樣伴隨 Yahoo 連線失敗, 不能判定為「零交易」。
Notable: 無。
持股背景 (yfinance `major_holders`, 可能受同一連線問題影響, 僅供參考): 內部人持股約 23.9%, 機構持股約 10.3% (占已發行股數), 機構家數 22 家。

## Ownership shifts
無歷史時間序列, 無法判斷機構集中度趨勢。目前快照顯示內部人持股比例偏高、機構持股比例偏低, 屬於結構性特徵, 不代表近期變動方向。

## Net sentiment score
Composite: **無法判定 (neutral by default, confidence: 低)**。
- 分析師面: 資料缺失, 不可用。
- 散戶面: Reddit 與 StockTwits 皆未取得, 不可用。
- 內部人面: 資料缺失, 不可用。

Divergence flag: **無法評估** — 缺少散戶與分析師兩端的有效資料, 無法判斷兩者是否背離。

### 後續補件建議
1. 允許 api.stocktwits.com 網域後重抓 StockTwits。
2. 重新執行 `pipeline/tools/yf 1815.TWO rec_summary`、`recommendations`、`insider`, 確認 Yahoo cookie/crumb 能否取得。
3. Reddit 若持續被封鎖, 改用其他可接受的公開來源或保留空白欄位。

SENTIMENT REPORT COMPLETE
