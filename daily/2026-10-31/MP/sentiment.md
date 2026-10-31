# Sentiment — MP as of 2026-10-31

**資料完整度警示**: Reddit (r/wallstreetbets, r/stocks) 抓取失敗。StockTwits 無法解析 api.stocktwits.com (DNS ENOTFOUND)。X / 社群零星內容僅能從一般網頁搜尋取得，無法量化。因此本報告的散戶面向為**資料缺失**，不是「散戶中性」。

## Analyst consensus

資料來源: `yf MP rec_summary` (本期 0m)。Strong Buy 5 / Buy 13 / Hold 1 / Sell 0 / Strong Sell 0，共 19 家。即 18 買 (95%)、1 持有、0 賣。

- 近 3 個月 (-1m 至 -3m) 分布幾乎不變，唯 -2m 起 Hold 由 1 變 0，其餘無明顯變化。
- `yf MP recommendations` 歷史評等變動回傳空陣列，無法確認個別升降評紀錄。
- 網頁搜尋可見的目標價調整 (未經 yf 驗證): Baird 由 $80 降至 $65 (維持 outperform, 10/1)；Morgan Stanley 由 $73 降至 $66 (維持 overweight, 10/7)；Deutsche Bank 於 7 月降低目標價。
- **衝突**: MarketBeat 文章提到「一家 Strong Sell、兩家 sell」並給出平均目標價 $75，與 yf 的 0 賣家數不一致。平均目標價 $75 明顯高於 10 月中後段的股價區間 (約 $37–$46)，可能是過期數字。以 yf 分布為準，但需留意來源不一致。

## Retail social

- **Reddit**: 抓取失敗，無樣本串文，無法給出 tilt。
- **StockTwits / X**: StockTwits 無法連線。網頁搜尋未找到 r/wallstreetbets、StockTwits 或 X 上對 MP 的近期具體討論，無法引用代表性言論。
- **Buzz 量**: 無法量化，無法與平時基準比較。
- **Themes (從新聞標題推斷，非散戶原文)**: 分析師降目標價；中國相關的供應鏈與稀土貿易降溫疑慮；股價跌破 50 日與 200 日均線。
- **Tilt**: 無法判定 (資料缺失)。

## Insider activity

`yf MP insider` 回傳空陣列，無法取得 6 個月內部人交易金額。網頁搜尋提及 CEO James Litinsky 透過其可撤銷信託出售股份，據稱依 10b5-1 計畫執行，但未取得交易日期與股數，無法換算金額，僅作為待核實線索。

**Net 6mo: 無法計算 (資料缺失)。**

## Ownership shifts

`yf MP major_holders`:
- 內部人持股 19.6%
- 機構持股 78.4% (佔流通股 97.5%)
- 機構數 964 家

僅為單一時點快照，無法判定季度趨勢。機構持股高 (佔流通 97.5%) 代表籌碼以機構為主，散戶影響力相對較低。

## 其他參考 (非 yf，來源為網頁)
- 空單比例: Benzinga 9 月快照顯示 19.6% of float，標示「上升 — 偏空」(8 月為 17.3%)。
- 股價: 10 月區間高點 $48.65、低點 $37.11；10/22 約 $38.56。10/31 即時價未取得。
- 下一個催化劑: MP 宣布將於 2026-11-05 公布 Q3 財報。
- 近期跌幅原因: 未找到單一明確原因，主要歸因於分析師降目標價與中國相關疑慮，證據強度弱。

## Net sentiment score

**Composite: 分析師面偏多 (中高信心)、散戶面無法評估 (低信心)、價格與籌碼面偏弱。綜合: 中性偏多，信心低。**

- 分析師面: 偏多，信心中高 (19 家中 18 買，但近期多家降目標價，且目標價與股價差距大，表示分析師共識可能落後價格)。
- 散戶面: 無資料，不納入加權。
- 價格/籌碼面: 偏弱 (股價自 10 月高點回落約 20%，空單比例上升，跌破主要均線)。這些不是情緒指標本身，僅作背景。

**Divergence flag: 無法判定 (no)。** 因缺乏散戶資料，無法確認散戶是否與分析師方向相反。

## 待補項目
1. 允許 api.stocktwits.com 與 www.reddit.com 網域後重跑散戶面。
2. 核實 CEO 出售的日期、股數與金額 (需要 SEC Form 4 資料)。
3. 取得 10/31 即時股價與 MarketBeat 最新目標價平均值，以校正 $75 的過期數字。
4. 11/05 財報後重跑分析師評等與內部人交易。

SENTIMENT REPORT COMPLETE
