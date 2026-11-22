# Sentiment — 2344.TW 華邦電 as of 2026-11-22

## Analyst consensus
目前 (0m) 7 buy (3 strong buy + 4 buy) / 1 hold / 0 sell,來源為 yfinance recommendations 與 rec_summary 工具。
近期趨勢 (各期 strongBuy+buy / hold / sell):
- 0m: 7 / 1 / 0
- -1m: 8 / 0 / 0
- -2m: 8 / 0 / 0
- -3m: 7 / 0 / 0

本月出現 1 檔 hold,表示近一個月內有一家券商由買進轉為持有。工具未標示是哪家。網路資料指 Morgan Stanley 於 2026-03 將評等降為 Hold、目標價 140 元,但兩者日期不同,無法確認是否為同一筆。

目標價 (TWD / 股, 來源為 Investing.com 聚合與新聞):
- 平均約 234 元,最高 360 元 (JPM, 2026-07-15, Buy),最低約 121 元
- 本土券商 218 元 (買進, 7 月)
- 本土投顧 285 元 (強力買進, 2026-07-26)
- 某券商 240 元下修為 205 元 (強力買進維持, 2026-11 法說會後, 確切日期未驗證)

整體結論: 分析師仍以買進為主,但目標價由 7 月高點往下調整。

## Retail social
- Reddit: DATA_UNAVAILABLE。r/stocks 搜尋的 WebFetch 回傳 "unable to fetch from www.reddit.com",未重試。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com 解析失敗 (ENOTFOUND),該域名不在本次 session 允許清單內,未重試。
- X / 新聞與論壇: 以新聞為主,社群原文不足。
  - 2026-11-03 法說會後股價跌停 (新聞)。
  - 2026-11-13 收盤 125 元 (statementdog 報價頁)。
  - 2026-11-16 scoreboard 約 99.90 元。
  - 2026-11-19 盤中一度跌破 100 元,最低 99.9 元,連續 5 個交易日走跌 (LTN 報導)。
  - Investing.com 頁面另顯示 143 元,日期不明,與上列價格矛盾。
- 聲量: 11 月新聞與討論量偏高,集中在 100 元整數關卡與法說會。缺乏可比的基準量,無法給出精確倍數,僅為定性判斷。
- 語氣: 偏空至分歧。
  - 偏空引述 (新聞標題): 「記憶體 is over」(LTN 報導引述股民)。
  - 分歧 (PTT, 時間不明): 一派看好 AI 帶動記憶體需求並持續加碼,另一派認為資金已轉向、短線缺乏動能。
  - 注意: PTT 可驗證的實際貼文為 6 月份 (標題為預測大漲),不屬於 11 月。
- 主要主題:
  1. 記憶體價格 (DDR4 漲勢是否收斂) 能否維持
  2. 100 元關卡能否守住
  3. 法說會後管理層表態 (公司表示 2027、2028 年市況無虞)
  4. 資本支出 731 億元 (董事會通過,主要用於高雄廠)
  5. 前 3 季 EPS 15.32 元 (新聞數字, 未獨立驗證)

## Insider activity
Net 6mo: DATA_UNAVAILABLE。insider 工具回傳空陣列 []。空結果無法確認為零交易或資料缺漏,不應解讀為無內部人交易。
Notable: 無可驗證資料。

## Ownership shifts
- insidersPercentHeld 28.8%
- institutionsPercentHeld 26.4% (float 口徑 37.1%)
- institutionsCount 221
- 趨勢 (時間序列): DATA_UNAVAILABLE。inst_holders 回傳 []。

## Net sentiment score
Composite: 分析師面偏多 (7 buy / 1 hold / 0 sell)、零售與新聞面偏空至分歧。整體為 neutral (偏分歧)。信心: 低至中。
- 信心受限原因: Reddit 與 StockTwits 無資料;股價來源互相矛盾 (125 / 99.9 / 143);52 週區間 52.20–233.50 來自 TipRanks,低點與 2026 價格路徑不一致,未經驗證。

Divergence flag: YES。分析師評等偏多、零售與新聞偏空,兩者方向相反。歷史上這類分歧常見於分析師目標價滯後於股價的情境,但本報告不做交易建議。

## 資料缺口
- DATA_UNAVAILABLE: Reddit、StockTwits、內部人交易、機構持股時間序列、日期可驗證的 11 月分析師評等變動
- 工具說明: pipeline/tools/yf.py 無 ratings 與 holders 子命令,實際使用 recommendations / rec_summary / major_holders / inst_holders

SENTIMENT REPORT COMPLETE
