# Final decision — 3260.TW as of 2026-10-22

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
Phase-1-only stub(非 positive pick,未進入 Phase 2-4 完整辯論)

## Phase-1 positive-pick 訊號評分
| 訊號 | 條件 | 結果 | 判定 |
|---|---|---|---|
| Fundamentals | Revenue YoY>15% 且 FCF/NI > -1 | yfinance `financials` / `cashflow` / `balance_sheet` 全數回傳空值或 404,營收成長與 FCF/NI 無法以標準化工具驗證(fundamentals.md 標記 DATA_UNAVAILABLE);公開月營收公告顯示 Q3 合併營收 NT$530.3 億、年增 266%,但 9 月營收環比 -16.88% | **FAIL(無法驗證)** |
| Market(技術) | RSI14<72 且 MACD hist 非深度負值 且 價格>MA50 | RSI14 = 26.97(過)但 MACD 柱 -3.46 持續負值,且價格 328.00 < MA50 389.16(-15.7%),同時低於 MA20 / MA200,空頭排列 | **FAIL** |
| News | 淨頭條情緒偏多 | Q4 DRAM/NAND 合約價預期再漲 15–20%、Q3 營收創高;惟 9 月營收環比下滑反映出貨調整。news.md 淨讀:正面至混合、幅度中等 | **PASS** |
| Sentiment | 分析師共識≥60% buy 或機構資金淨流入 | 3 家法人全數買進(目標價 780–1,000 元)、投信連 5 日買超;但 10 月三大法人合計賣超 553 張,外資持股僅 13.34% | **PASS** |
| Valuation | Forward P/E<35x 或明確 EPS 成長催化 | 工具無 P/E 資料;法人預估 2026 EPS 111.5–136.82 元對應現價 328 元為 2.4–2.9x,但目標價分歧 200–1,000 元,預估口徑無法驗證 | **FAIL(無法驗證)** |

**合格訊號數: 2/5(門檻為≥3)→ 不符合 positive-pick 標準,僅完成 Phase 1(+ Phase 1.5 evidence shadow),未進入 Bull/Bear 辯論、交易員規劃與風險委員會。**

## 為何不予完整分析
威剛是本次 tw_memory 四檔中唯一 yfinance 財務資料幾乎全缺的名字(`info` 404、三表空值),基本面與估值兩個訊號都停在「無法驗證」而非「不及格」;可驗證的技術面則明確空頭 —— 股價自 8 月 459.5 元高點回檔 28%,跌破三條均線,RSI 26.97 深度超賣但無量能背離。新聞與法人評等偏多,但法人目標價 200 到 1,000 元的 5 倍分歧本身就是訊號:市場對週期高峰後的獲利延續性沒有共識。在沒有可驗證財報數據的情況下進入完整辯論,只會把法說與媒體數字當成事實來辯,違反本 pipeline 的 PRICE-DATA / 數據完整性紀律。

## 監控觸發(若未來重新評估)
- 11 月初 10 月營收公告:若環比由 -16.88% 轉正且年增維持三位數,News 訊號強化、基本面可用公開數據補證。
- 技術面:收復 MA20(363.80)並站穩,或 RSI 自 <30 區回升且 MACD 柱狀圖收斂轉正,為反彈確認;跌破 334 元支撐則下一支撐區看 7 月低檔。
- 資料面:若 `prices/yf/3260.TW.json` 快取或 yfinance 開始提供財報欄位,Fundamentals / Valuation 兩個訊號可重新判定,屆時最多達 4/5。

## 資料限制聲明
本報告僅使用 2026-10-22 當日工具輸出(pipeline/tools/yf、ta;價格來源 cnyes 即時 + Yahoo 日 K)與同日 WebSearch 結果,未借用歷史 daily/<date>/ 報告的任何數字。

FINAL DECISION COMPLETE
