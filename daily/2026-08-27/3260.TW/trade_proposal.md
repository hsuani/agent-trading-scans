FINAL TRANSACTION PROPOSAL: **HOLD**

# Trade proposal — 3260.TW as of 2026-08-27

## Direction
AVOID（不建立新方向性部位；若已持有現股，維持極輕倉觀察，不加碼）

## Setup
不提供進場區間、停損、Target 1/2、R:R。

理由：research manager 的 investment_plan.md 明確判定 NEUTRAL / 信心 LOW，核心原因是**輸入資料本身不可信**，而非單純方向不明：
- fundamentals.md 內部 Trailing P/E 出現三種矛盾算法（表格 8-9x vs H1 EPS 年化反推 ~3.3x vs sentiment.md 另給 5.38x），差距達 2-3 倍。
- fundamentals.md 的 Q2 淨利 NT$1.04B 與 news.md 引用公司法說會官方公告 NT$107.68 億（NT$10.768B）相差近 10 倍量級，後者來源可信度明顯更高，代表 fundamentals.md 至少有一處基礎輸入錯誤。
- market.md 因 yfinance 對 3260.TW 無資料覆蓋，MA/RSI/MACD/ATR/52 週高低全數缺失（PRICE_DATA_UNAVAILABLE），僅剩 cnyes 現貨價；sentiment.md 卻聲稱「日線 Strong Sell」，來源與計算方式不明，兩份 Phase-1 報告對「是否存在可用技術訊號」互相矛盾。

在沒有可靠 P/E、沒有可靠 K 線/ATR 的情況下，任何進場價、停損價、目標價都只能是編造數字，不採用。

## Sizing
不建立新倉。若已持有，維持觀察倉位或降至輕倉（quantitative 不適用——無可靠 ATR/波動率數字可供計算部位大小）。

## Time horizon
數週至一季——待 Q3 財報（10 月下旬）與資料校正後重新評估。非適合立即依現有資料做方向性建倉的時點。

## Trigger
Wait for（以下兩項資料修正/催化事件同時或分別出現，才重新評估方向）：
1. 取得公開資訊觀測站/公司官方財報，核實正確 Q2/H1 淨利與 EPS 數字，消除三種 P/E 矛盾，重新計算 Trailing/Forward P/E。
2. 取得可靠的日/週 K 線與 RSI/MACD/ATR 資料源（例如台灣證交所或其他技術分析平台），補足 market.md 資料缺口，才可能設定客觀進場價、停損位與 R:R。
3. Q3 法說會（10 月下旬）確認記憶體漲價指引是否兌現。

## Invalidation
本提案本身即為「不進場」，故無傳統停損；若在資料修正前有人已持有部位，應在以下任一情況發生時降低曝險：
- TrendForce/DRAMeXchange 週度報價出現 DRAM/NAND 合約價轉跌訊號（驗證空方「周期見頂」假說）。
- 內部人（董監事）出現實際減持紀錄。
- 公司財報校正後 Trailing P/E 高於同業（代表「估值便宜」論點不成立）。

## Catalyst calendar
- 2026-10（下旬）— Q3 法說會，公司公布正確 Q2/H1/Q3 財務數字並更新漲價指引
- 持續追蹤 — 公開資訊觀測站官方財報公告，用以校正 fundamentals.md 的淨利/EPS 數量級錯誤
- 持續追蹤 — TrendForce/DRAMeXchange DRAM/NAND 週度合約價，判斷記憶體漲價周期是否持續至 2027 年

TRADE PROPOSAL COMPLETE
