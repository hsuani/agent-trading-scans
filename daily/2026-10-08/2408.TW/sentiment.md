# Sentiment — 2408.TW (南亞科 Nanya Technology) as of 2026-10-08

## 資料來源與品質說明
- Yahoo 即時呼叫失敗（ConnectionError），所有 yf 數據取自 repo 快取 `prices/yf/2408.TW.json`，快取刷新時間為 2026-10-07 13:09 UTC。
- Reddit 無法連線（soft-fail）；StockTwits 被 egress proxy 阻擋（EGRESS_BLOCKED，soft-fail）。
- 中文與英文網路搜尋結果為摘要，未逐筆驗證原始報導；年份與數字不一致之處已註明。
- 未使用任何舊日期 `daily/` 目錄的數字。

## 分析師共識
目前 12 位分析師：**11 buy（strong buy 4 + buy 7）/ 0 hold / 1 sell**。Buy 佔 91.7%、Hold 0%、Sell 8.3%。Yahoo recommendationMean 為 1.67（1 = strong buy，5 = sell）。

目標價：平均 581 TWD（相對快取收盤價 514 TWD，上行空間約 13.0%），最高 850 TWD，最低 150 TWD。

近期評等與目標價變動（搜尋彙整，非 Yahoo 歷史資料）：
- 大和：6 月前後目標價由 292 調至 650 TWD，維持買進。
- Macquarie：7 月 13 日買進，目標價 552 TWD。
- JPMorgan：8 月 10 日維持買進，目標價 850 TWD（來源為 investing.com 摘要）。
- 摩根士丹利：4 月中立，目標價由 298 降至 278 TWD，認為股淨比與獲利修正後上行空間有限。
- 日系外資：4 月買進，目標價 292 TWD；本土法人 4 月目標價由 318 下修至 267 TWD。
- Citi：1 月賣出，目標價 41 TWD。此數字與當時股價差距異常，疑為報導錯誤或舊資料，未計入共識。
- FactSet 彙整 16 位分析師 EPS 中位數 41.76 元、目標價 317.5 元，報導未標日期，未採計。

注意：`rec_summary` 與 `recommendations` 的 0m、-1m、-2m、-3m 四個期間數字完全相同，快取內沒有真正的月度歷史，因此無法從 Yahoo 推算近期評等升降趨勢，上表的評等變動僅來自搜尋摘要。

## 機構資金流向
- Yahoo 持股結構：institutionsPercentHeld 14.2%，institutionsFloatPercentHeld 31.2%，機構家數 216。
- `inst_holders` 即時與快取皆為空陣列，無法取得個別機構持股名單與季度增減趨勢。
- insidersPercentHeld 54.4%：屬結構性大股東持股比重，並非交易訊號，持股變動需以 MOPS 公開資訊觀測站核對。
- 三大法人（搜尋摘要，年份與金額未經 TWSE 驗證）：8 月 4 日與 8 月 10 日南亞科皆位居外資買超金額前列，8 月 10 日摘要數字為外資買超約 517 億元；8 月 31 日與 9 月 16 日南亞科仍在外資買超前二，但當日三大法人合計皆為賣超（9 月 16 日合計賣超約 213.8 億元）。10 月交易日資料未取得。

## 內部人交易
Net 6mo：**無資料**。`yf insider` 即時與快取皆回傳空陣列，無法計算淨買賣金額，也無法辨識 CEO / CFO 等個別交易人。空陣列不等於「無內部人交易」，應以 MOPS 內部人持股申報核對。

## 散戶情緒
- Reddit：未取得（無法連線）。
- StockTwits：未取得（egress 阻擋）。
- X / 網路搜尋：找不到 2026 年 10 月的討論貼文；英文來源以投資平台與機構評等摘要為主。
- 中文社群：PTT 股版未找到直接討論串。CMoney 股市爆料同學會南亞科版摘要顯示整體偏謹慎但不悲觀，有人提出「空頭對南亞科會怎樣」，顯示對季線與外資動向的擔憂。
- 討論量（buzz volume）：無法量化。中文財經媒體報導頻繁，英文社群可見度低，定性判斷為中等偏低。
- 主要議題（主題排序）：
  1. DRAM 價格與 DDR4 漲勢能否延續，下半年是否轉弱。
  2. 泰山新廠 2027 年第一季開始裝機的時程。
  3. 美光等同業走弱的傳導風險。
  4. 股價漲幅大後的獲利了結賣壓與季線支撐。
  5. 美國對境外生產記憶體的關稅政策風險。
- 散戶傾向：mixed，偏謹慎。

## 排程事件
- 2026-10-12 為 Q3 財報預定日，Yahoo 快取 EPS 預估 24.02 元（Q2 實際 EPS 14.66 元，Q2 營收約 825.5 億元）。此為排程資料，財報結果不在本報告時點範圍內。

## 綜合情緒評分
- 分析師：**偏多（bullish）**，信心高。11/12 買進，但樣本僅 12 位，且目標價分歧大（150 至 850 TWD）。
- 散戶：**中性偏謹慎（neutral-to-cautious）**，信心低。中文社群樣本少，無 Reddit / StockTwits 數據。
- 機構資金：**分歧（mixed）**，信心低。8 月為外資主力買超，9 月多日合計賣超，10 月無資料。
- 綜合：**偏多但信心中低（bullish-leaning, low-medium confidence）**。

**分歧旗標（Divergence flag）：是（輕度）**。分析師評等高度正面，但散戶社群與近期法人買賣節奏偏謹慎，主要疑慮為股價高檔獲利了結與 DRAM 漲價是否可持續。

## 指標表

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 評等分布（Buy / Hold / Sell） | 11 / 0 / 1（12 位） | yf 快取 rec_summary |
| Buy 比例 / Hold / Sell | 91.7% / 0% / 8.3% | 由上表計算 |
| recommendationMean | 1.67 | yf 快取 info（1 = strong buy） |
| 目標價平均 / 最高 / 最低 | 581 / 850 / 150 TWD | yf 快取 info |
| 快取收盤價 | 514 TWD | yf 快取 info（2026-10-07 刷新） |
| 目標價隱含上行空間 | 約 +13.0% | 581 / 514 - 1 |
| 其他摘要目標價（investing.com） | 559.83 TWD | 搜尋摘要，快照時點不明 |
| 52 週高 / 低 | 569 / 85 TWD | yf 快取 info |
| Trailing P/E | 19.4x | yf 快取 info |
| 市值 | 約 1.77 兆 TWD | yf 快取 info（marketCap） |
| 內部人持股 | 54.4% | yf major_holders，結構性持股 |
| 機構持股 / 流通股機構持股 | 14.2% / 31.2% | yf major_holders |
| 機構家數 | 216 | yf major_holders |
| 內部人 6 個月淨買賣 | 無資料 | yf insider 空陣列 |
| 機構個別持股變動 | 無資料 | yf inst_holders 空陣列 |
| 下次財報 | 2026-10-12 | yf 快取 earnings_dates |
| Q3 EPS 預估 | 24.02 元 | yf 快取 earnings_dates |
| Beta | 約 1.95 | 搜尋摘要（Simply Wall St），未經 yf 驗證 |
| Reddit / StockTwits | 未取得 | 網路受限 |
| 綜合情緒 | 偏多，信心中低 | 本報告評分 |
| 分歧旗標 | 是（輕度） | 分析師正面 vs 散戶 / 資金謹慎 |

SENTIMENT REPORT COMPLETE
