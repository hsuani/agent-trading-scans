# Sentiment — 1513.TW (中興電工) as of 2026-11-24

> 資料來源狀態：yf rec_summary / recommendations 有回傳；inst_holders 與 insider 回傳空陣列（Yahoo cookie/crumb 取得失敗，未取得快取）；零售社群（Reddit / PTT / StockTwits）搜尋無實質討論串，判定為 DATA_UNAVAILABLE。

## Analyst consensus

yf rec_summary（當期 0m）：**1 strongBuy / 6 buy / 1 hold / 0 sell / 0 strongSell**，合計 8 家。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m（當期） | 1 | 6 | 1 | 0 | 0 |
| -1m | 1 | 6 | 1 | 0 | 0 |
| -2m | 1 | 6 | 1 | 0 | 0 |
| -3m | 1 | 6 | 1 | 0 | 0 |

- 近四個月彙總評等分布完全相同，沒有可辨識的升評或降評事件。yf `recommendations` 回傳的也是同一組彙總期間資料，並非逐筆 upgrade / downgrade 紀錄，因此無法列出個別券商的評等變動。
- 目標價：外部彙整網站（Investing.com 搜尋摘要）列示 12 個月平均目標價 **TWD 185.50**，買進 7 家、賣出 0 家。此數字與 yf 的 8 家分布略有差異（口徑或更新時點不同），以外部來源為準，未經 yf 交叉驗證。
- 股價參考：來源之間股價不一致（約 TWD 138.5 至 153.5，52 週區間 TWD 142.5 至 201.0），無法確認當日收盤價，目標價空間計算需等確認收盤價後再做。

## Retail social

- Reddit：WebSearch 未找到 r/wallstreetbets 或 r/stocks 上關於 1513.TW 的討論串。依指示未使用 WebFetch 直接抓取。**DATA_UNAVAILABLE**。
- PTT / Dcard：WebSearch 僅回傳財經網站（statementdog、goodinfo、nstock 等），沒有 PTT Stock 板或 Dcard 的相關貼文。**DATA_UNAVAILABLE**。
- StockTwits / X：未找到可靠的貼文樣本。Investing.com 技術面訊號在不同頁面互相矛盾（一頁為 Strong Sell，另一頁 RSI 14 日為 58.99 偏多），屬於行情頁面彙整，不是零售情緒。
- 聲量（相對一般水準）：無法量化，搜尋結果中沒有可辨識的社群提及量。Goodinfo 顯示 11 月中旬當沖比率約 35% 至 40%，代表短線交易活躍，但方向性不明，不能視為看多或看空訊號。
- 主要題材（來自財經媒體與公司資料，非網友原話）：
  - 台電體系電網與變電工程（345kV GIS 認證、EPC 統包），受惠台電強韌電網計畫。
  - AI 資料中心供電與配電設備，但 AIDC 統包仍在效益評估階段。
  - 在手訂單約 TWD 431 億（截至 2026/03 底）。
  - 10 月營收年增約 18%，今年累計營收約 TWD 239.75 億（Winvest 摘要）。
- 零售語氣判定：**無法判定（DATA_UNAVAILABLE）**。

## Insider activity

- yf insider：回傳空陣列，無法取得逐筆申報。
- WebSearch 與 Goodinfo 統計：截至 2026/09，非獨立董監合計約 5.32 萬張、持股比例 10.6%，當月無增減。HiStock 顯示 2026/05 至 07 董監持股比例維持 10.58%。
- 2026/08 起的公告為設置永續發展委員會與副總經理屆齡退休，未見董監或經理人買賣申報。
- **Net 6mo：無法確認（DATA_UNAVAILABLE）。** 沒有找到 2026 年內的買進或賣出明細，不能宣稱淨買或淨賣。
- 質押風險：Goodinfo 顯示董監質押約 1.22 萬張，質押比例 22.9%。這是需要留意的結構性風險，與買賣申報不同，不代表近期有賣出。
- 建議查證：公開資訊觀測站「董監事持股查詢」與「內部人申報」，以 1513 搜尋。

## Ownership shifts

- yf major_holders：
  - insidersPercentHeld：19.94%
  - institutionsPercentHeld：14.19%
  - institutionsFloatPercentHeld：17.72%
  - institutionsCount：58
- yf inst_holders：回傳空陣列，無法取得前幾大機構持股明細與季度變化。
- 趨勢判定：**無法判定**。目前只有單一時點快照，沒有前期對照，不能判斷機構持股是增加還是減少。
- 口徑注意：yf 的 insidersPercentHeld（19.94%）與 Goodinfo 的董監持股比例（10.6%）差距大，應是定義不同（yf 可能包含大股東或其他口徑），不宜直接比較。

## Net sentiment score

- 分析師面：**偏多（bullish）**。8 家中 7 家為 buy 或 strongBuy，0 家賣出，四個月無變化。
- 零售面：**無資料（DATA_UNAVAILABLE）**。
- 內部人面：**無法判定**，但無證據顯示近期有大股東或董監大量賣出；質押比例偏高為風險因子。
- 綜合：**偏多（bullish），信心低**。判斷只根據分析師面，零售與內部人資料缺失，且分析師評等四個月未變動，可能只是陳舊彙總。

**Divergence flag：無法判定（no）**。零售情緒資料缺失，無法比較零售與分析師方向是否相反。

## 摘要表

| 項目 | 結果 | 信心 | 備註 |
|---|---|---|---|
| 分析師評等（yf 0m） | 1 SB / 6 B / 1 H / 0 S / 0 SS | 中 | 四個月無變化，無逐筆升降評紀錄 |
| 目標價（外部彙整） | 平均 TWD 185.50 | 低 | 外部來源，未經 yf 驗證 |
| 零售聲量與語氣 | DATA_UNAVAILABLE | — | Reddit / PTT / StockTwits 無實質討論 |
| 內部人買賣（6mo） | 無法確認 | — | yf insider 空陣列；Goodinfo 9 月無增減 |
| 董監質押 | 22.9%（約 1.22 萬張） | 中 | 結構性風險，非近期賣出 |
| 機構持股 | 14.19%，58 家，趨勢無法判定 | 低 | inst_holders 空陣列，無時間序列 |
| 綜合情緒 | 偏多，信心低 | 低 | 僅分析師面有資料 |
| 背離訊號 | 無法判定 | — | 零售資料缺失 |

SENTIMENT REPORT COMPLETE
