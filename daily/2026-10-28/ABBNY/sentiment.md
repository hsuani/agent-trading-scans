# Sentiment — ABBNY as of 2026-10-28

## Analyst consensus
目前 (period 0m) 共 6 位分析師: 0 buy / 0 strong buy / 5 hold / 0 sell / 1 strong sell，共識偏中性偏保守。

近月 (-1m) 為 0 buy / 3 hold / 2 strong sell，本月 strong sell 由 2 降至 1、hold 由 3 增至 5，評級有小幅向中性移動的跡象。近三個月 (-2m、-3m) 結構相同 (3 hold / 2 strong sell)，未見新增買進評級。

目標價 (第三方彙整，非 yf 工具輸出，來源時間不一):
- Walnut Invest 平均目標價約 $93.32，該站引用價格 $91.05 (日期未標示)。
- MarketBeat 2026 年 7 月項目列出 $58 目標價與 Hold 共識，與上述數字不一致，列為低可信度。

**限制**: yf 工具回傳的評級為快取或部分快取資料，回傳內容未附抓取時間戳，無法確認是否為 2026-10-28 當日數值。目標價變動歷史 DATA_UNAVAILABLE。

## Retail social
- Reddit (r/wallstreetbets、r/stocks): DATA_UNAVAILABLE。WebFetch 回傳 "unable to fetch from www.reddit.com"，無法取得貼文樣本、提及數或情緒傾向。
- StockTwits: DATA_UNAVAILABLE。api.stocktwits.com DNS 解析失敗 (session 網路白名單未包含此網域)，需由使用者於 session 設定中允許後才能重試。
- X / 新聞聊天: WebSearch 僅回傳彙整站與舊資料，未找到可引用的 2026-10 當月社群貼文。
  - 網站: Walnut Invest 將 ABBNY 列為 0 buy / 3 hold / 2 sell；Equibles 標示情緒中性、動能強、機構資金流為 Accumulating；Investing.com 總評 Neutral。
  - 多頭敘述 (Stockchase): 股價有明顯漲幅，市場寄望歐洲景氣回升與工業機器人前景改善。
  - 空頭敘述 (suredividend, 2026-04): 股價在大盤回檔時傾向跌幅較大。
  - Earnings Whispers 標示財報日為 2026-10-19 (盤前)，該日後的實際財報內容未驗證。
- 聲量 (buzz volume) 相對一般水準: DATA_UNAVAILABLE。
- 主要主題 (僅由彙整站推得，非社群原文): 估值偏高 (trailing P/E 約 33x、forward 約 25x)、財報後動能、歐洲景氣、工業機器人題材。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。yf insider 回傳空陣列 `[]`，無法區分「無交易」與「資料缺漏」，不應解讀為零內部人交易。

Notable: DATA_UNAVAILABLE。

## Ownership shifts
- institutionsCount: 88 (機構家數)。
- institutionsPercentHeld: 0.00202，insidersPercentHeld: 0.0。這兩個百分比數值明顯偏低且與機構家數不成比例，判定為資料品質問題 (ADR 持股比例未正確換算)，不採用。
- 機構持股集中度趨勢 (多期比較): DATA_UNAVAILABLE。
- Equibles 提及機構資金流為 Accumulating，屬第三方敘述，未能以 yf 數據驗證。

## Net sentiment score
Composite: **中性 (neutral)**，信心 **低**。

- 分析師面: 偏中性偏保守 (0 buy、5 hold、1 strong sell，近月賣方評級略有緩和)。
- 散戶面: DATA_UNAVAILABLE (Reddit、StockTwits 皆無法取得)。
- 內部人面: DATA_UNAVAILABLE。
- 第三方彙整站敘述: 中性，動能偏多，估值偏高。

信心低的原因: 散戶與內部人兩個關鍵來源皆缺，分析師資料時間戳不明，且目標價來源互相矛盾。

Divergence flag: **無法判定 (DATA_UNAVAILABLE)**。散戶傾向資料缺漏，無法與分析師傾向比較。

## 資料來源與缺漏清單
| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 取得 (快取或部分快取，時間戳不明) |
| yf insider | 空陣列，視為 DATA_UNAVAILABLE |
| yf major_holders | 取得，但百分比欄位疑似換算錯誤，僅採機構家數 88 |
| Reddit r/wallstreetbets、r/stocks | DATA_UNAVAILABLE (WebFetch 無法連線) |
| StockTwits | DATA_UNAVAILABLE (DNS 解析失敗，網域未允許) |
| WebSearch | 部分取得，多為彙整站與舊資料 |

Sources (WebSearch):
- [Walnut Invest ABBNY forecast](https://walnutinvest.com/stocks/abbny/forecast)
- [Equibles ABBNY](https://equibles.com/stocks/abbny)
- [Investing.com ABB Ltd ADR](https://www.investing.com/equities/abb-ltd-adr)
- [Earnings Whispers ABBNY](https://beta.earningswhispers.com/go/x/ABBNY)
- [MarketBeat ABB Erste Group 2026-07-30](https://www.marketbeat.com/instant-alerts/erste-group-bank-has-strong-forecast-for-abb-fy2026-earnings-2026-07-30/)
- [suredividend ABBNY 2026-04-22](https://www.suredividend.com/wp-content/uploads/2026/04/ABBNY-2026-04-22.pdf)

SENTIMENT REPORT COMPLETE
