# Sentiment — MP as of 2026-10-23

> 資料時點注意：本報告以 DATE=2026-10-23 標示，但執行當日系統日期為 2026-10-22。價格與新聞資料最晚僅到 2026-10-19，請以收盤後資料再次核對。

## Analyst consensus
19 位分析師：5 strongBuy / 13 buy / 1 hold / 0 sell / 0 strongSell（資料來源：yf rec_summary）。
BUY 比例 = 18/19 ≈ **94.7%**，HOLD 約 5.3%，SELL 0%。

近期變動（yf recommendations 的月度快照）：
- 0m、-1m 皆為 5 strongBuy / 13 buy / 1 hold；-2m、-3m 為 5 strongBuy / 13 buy / 0 hold。即約 2 個月前新增 1 筆 hold，評等數量其餘期間持平，未見大量評等調整。
- 目標價下修（來源為 MarketBeat / Nasdaq 的二手彙整，未能於 yf 直接驗證）：
  - Morgan Stanley：目標價 $73 → $66，維持 Overweight。
  - Robert W. Baird：目標價 $80 → $65，維持 Outperform。
  - Zacks Research：由 hold 降為 strong sell（報導日期 2026-08-26）。
  - Wall Street Zen：由 hold 降為 sell。
- MarketBeat 共識目標價約 $75（10 月報導），Fintel 平均目標價約 $78（2026-08）。

**一致性提醒**：yf 的 0 sell 與第三方（Zacks、Wall Street Zen）的 sell 評等口徑不同，MarketBeat 亦稱「2 筆 sell」。實際計算採用 yf 數字，但第三方 sell 評等應視為獨立訊號。

## Retail social
- **Reddit**：r/wallstreetbets 與 r/stocks 搜尋皆被封鎖（WebFetch 回傳 "unable to fetch"），無法取得討論串數量、分數或語氣。依規則 soft-fail，未納入評分。
- **StockTwits / X**：StockTwits API DNS 解析失敗（ENOTFOUND），無法取得訊息標籤比例。X 端僅能以 WebSearch 取得新聞轉載，無法判讀真正的社群語氣。
- **Buzz 量**：無法量化。以新聞覆蓋度判斷，10 月多為 MarketBeat 自動化的股價警示與分析師評等更新，並無明顯的散戶熱議事件。
- **Tilt**：無社群樣本，無法判定散戶多空傾向。
- **Themes（僅來自新聞，非社群樣本）**：
  - 稀土題材降溫：Quiver Quant 認為投資人正在減少對稀土主題的押注，供給緊俏與地緣溢價消退。
  - 缺乏公司層級催化：該文指出 MP 近期沒有新的公司層面消息，同業股表現也偏弱。
  - 技術面轉弱：股價低於 50 日與 200 日均線（$51.86 與 $54.96）。
  - 基本面：最近一季營收約 $108.49M（年增約 89%），但仍有負毛利率，分析師預期全年虧損。

## Insider activity
yf insider 回傳空清單，無法確認 6 個月內是否有內部人交易，也不能推論「無交易」。**Net 6mo：資料缺漏（不計入分數）**。
內部人持股比例約 19.6%（yf major_holders），但這是持有比例，不代表交易方向。

## Ownership shifts
- 機構持股比例約 78.4%，流通股機構持股約 97.6%，機構家數 966。
- yf 僅提供當前快照，沒有季度趨勢，**無法判斷機構淨流入或淨流出方向**。

## Net sentiment score
- **分析師面**：偏多（bullish）。高比例買進評等，但目標價連續下修，信心中等偏高。
- **散戶 / 社群面**：無資料（Reddit、StockTwits 皆不可得）。
- **價格動能面（新聞推導）**：偏空。10 月股價由約 $48.79（9 月底）跌至約 $39.82（10/14），之後約在 $40 附近，跌幅明確，但未找到直接的公司層面原因。
- **綜合**：分析師偏多、價格動能偏空，整體為 **neutral（中性偏多，信心低）**。原因是社群資料缺失，無法補足散戶端。

**Divergence flag：無法判定（no）**。缺乏散戶語氣資料，無法確認散戶傾向是否與分析師相反。若補足 Reddit 或 StockTwits 資料後再評估。

## 資料缺口與後續
1. Reddit JSON 被封鎖；StockTwits DNS 失敗。需要替代來源（例如付費社群 API 或其他可用的 Reddit 查詢方式）。
2. yf insider 為空，需以 SEC Form 4 直接核對 6 個月內交易。
3. 機構持股需要多季 13F 比較才能判斷流向。
4. 分析師評等口徑需統一（yf 與 MarketBeat / Zacks 不一致）。
5. 下一個催化劑：2026-11-05 第三季財報。

SENTIMENT REPORT COMPLETE
