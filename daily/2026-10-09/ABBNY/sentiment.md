# Sentiment — ABBNY as of 2026-10-09

資料截止日: 2026-10-08 (與 news.md 一致)。Reddit、StockTwits 本次皆無法取得 (見下方資料缺口)。

## Analyst consensus
5 家覆蓋 (yf rec_summary, 當期): 0 buy / 3 hold / 0 sell，另 2 家 strong sell (共 0 strong buy)。
- 近三個月 (0m / -1m / -2m) 分布完全相同，代表期間內無評等數量變化，但也可能是快取未更新，需以來源時間戳核對。
- `yf recommendations` 回傳內容與 rec_summary 相同，為月度彙總，不含逐筆升降評等事件，因此「近期 upgrade / downgrade」無法從此工具確認。
- 已知事件 (WebSearch 二手來源): 2025-10-03 BNP Paribas 將評等列為 strong sell (MarketBeat 標題)。
- 目標價: yf 未提供。WebSearch 引用的 MarketBeat 數字為 2026-04 之共識目標價 $58.00 (平均評等 Hold，當時 3 Strong Buy / 3 Hold / 3 Sell)。此數字已超過半年、且與目前 yf 分布不一致，僅供參考，不可當作現行目標價。
- 估值參考 (Yahoo 摘要, 經 WebSearch): trailing P/E 38.16、forward P/E 31.06。news.md 另引 forward P/E 約 26 倍，兩者口徑或時點不一，需注意。
- 方向判讀: 目前分析師端偏保守 (無 Buy，兩家 strong sell)，與 96.20 美元附近價位、偏高估值的組合一致。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): 無法取得。代理端對 reddit.com 回傳 CONNECT 403 (curl 與 WebFetch 皆失敗)，soft-fail。本次無樣本貼文、無法估算提及量。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND)，soft-fail。
- X / 新聞討論 (WebSearch, 2026-09 前後資料為主，無 10 月直接貼文): 
  - 一家瑞士交易台認為股價接近修正尾聲，稱為短線偏多但屬投機性操作，並警告若再轉弱將有重大損失。
  - Stockchase 使用者意見多數偏多，主軸為 ABB 位於電氣化與 AI 資料中心供電題材。
  - 少數意見認為公司因州級專案而成長緩慢。
- 提及量: 無法量化。以可得來源判斷，ABBNY 為 OTC 掛牌之低流動性 ADR (10 日均量約 185k 股，見 news.md)，散戶討論量預期偏低，此為推論，非實測。
- 主要主題 (可得來源歸納):
  1. AI 資料中心與電網 / 直流 (DC) 電力題材 (偏多)
  2. 2026-07 Q2 訂單與指引上調 (偏多)
  3. Rotork 收購 (約 55 億美元) 估值與整合疑慮 (偏空或中性)
  4. 利率上升與高估值壓力 (偏空)
  5. 2026-10-20 Q3 財報前的期待與不確定性
- 散戶傾向: 無法判定。僅有可得來源偏多，樣本不足，不足以形成可靠結論。

## Insider activity
yf insider 回傳空清單。近 6 個月無可查詢的內部人交易紀錄。
- 注意: ABB 為瑞士公司，內部人申報依瑞士與 SEC 外國私人發行人規則，未必以 Form 4 形式出現於 yf，因此空清單可能是結構性缺口，不能直接解讀為「無內部人交易」。
- Net 6mo: $0 buys, $0 sells (資料不足，無法確認)。
- Notable: 無。
- 另見 news.md 所列之人事變動: Sami Atiya (Robotics 與 Discrete Automation 總裁) 預計 2026 年底前離任，屬人事訊號，非內部人買賣。

## Ownership shifts
yf major_holders:
- insidersPercentHeld: 0.0
- institutionsPercentHeld: 0.00226
- institutionsCount: 89
- 可信度低: 機構持股比例 0.226% 不符合大型工業股之常態，疑為 ADR 口徑或單位問題。僅能確認機構家數約 89 家。
- 趨勢: 無歷史資料，無法判定集中度變化方向。

## Net sentiment score
Composite: **neutral (偏空傾向, 信心低)**

- 分析師端: 偏空 (0 buy / 3 hold / 2 strong sell)，信心中等，因樣本僅 5 家且目標價資料過時。
- 新聞端 (見 news.md): 偏多，mild to moderate bullish，主因 Q2 訂單與指引上調、資料中心題材、回購持續。但 10-08 單日下跌 2.88% 原因不明。
- 散戶端: 無法評估。可得來源樣本不足。
- 內部人端: 無資料。
- 綜合: 分析師偏空與新聞偏多並存，散戶端無資料，整體判為 neutral，偏空傾向，信心低。

Divergence flag: **無法判定 (no data)**。散戶端資料缺失，無法比較散戶與分析師方向是否相反。若以新聞面為代理，新聞偏多與分析師偏空之間存在落差，但這是新聞與分析師之間的差異，不等同於散戶與分析師之間的背離。

## 資料缺口與可靠度
- Reddit: 代理 403，無資料。
- StockTwits: DNS 失敗，無資料。
- yf recommendations: 僅月度彙總，無逐筆評等事件。
- yf insider: 空清單，需人工確認 (瑞士申報規則可能造成缺口)。
- yf major_holders: 機構持股比例數值疑似錯誤。
- Yahoo cookie / crumb 取得失敗 (ConnectionError)，但數據仍回傳，時效性無法確認。
- 目標價: 僅有 2026-04 之二手數字，不可作為現行參考。
- 日期: 任務指定 DATE=2026-10-09，系統當日為 2026-10-08，資料截止日以 2026-10-08 為準，未納入之後資訊。

SENTIMENT REPORT COMPLETE
