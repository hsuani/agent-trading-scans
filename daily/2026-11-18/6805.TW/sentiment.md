# Sentiment — 6805.TW（富世達）as of 2026-11-18

> 資料限制：今日系統日期為 2026-11-17，任務指定 as-of 2026-11-18，已依任務日期標示，未引用任何舊日期報告。Yahoo cookie/crumb 取得失敗，yf 工具以快取回傳分析師數據。Reddit 與 StockTwits 無法取得（見下方）。

## Analyst consensus

資料來源：`pipeline/tools/yf 6805.TW rec_summary`（快取回傳）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 本月（0m） | 3 | 6 | 0 | 0 | 0 | 9 |
| -1m | 3 | 6 | 0 | 0 | 0 | 9 |
| -2m | 3 | 6 | 0 | 0 | 0 | 9 |
| -3m | 3 | 5 | 0 | 0 | 0 | 8 |

目前 9 家評級：買進 9（Strong Buy 3 / Buy 6）、持有 0、賣出 0。近三個月無評級下調，-3m 至今新增 1 家買進評級。

近期調整：`yf 6805.TW recommendations` 回傳內容與 rec_summary 相同，未提供逐筆升降評等紀錄，無法確認個別券商動向。WebSearch 找到大和資本（Daiwa）維持 Buy，目標價由 NT$2,615 上調至 NT$2,910（上調約 11%），來源為 money.udn.com 報導，報導日期未在搜尋結果中確認。

## Retail social

- Reddit（r/stocks、r/wallstreetbets）：DATA_UNAVAILABLE。WebFetch 回報 `Claude Code is unable to fetch from www.reddit.com`，無法取得貼文樣本、提及次數與多空傾向。
- StockTwits：DATA_UNAVAILABLE。`api.stocktwits.com` DNS 解析失敗（ENOTFOUND），需於 session 網路設定允許該網域後才能重試。
- X / 新聞輿情（WebSearch）：找到的是新聞與法人報導，未找到可量化的散戶貼文或情緒調查。
  - 大和資本維持買進，3Q 財報優於預期，2027 年展望仍正面（money.udn.com）。
  - 3Q 營收約 NT$45.02 億，季增 20.4%、年增 26.2%，創歷史新高；毛利率約 38%；EPS 約 NT$18.11（來源：Yahoo 財經新聞轉載，sourced via WebSearch）。
  - 伺服器業務占 3Q 營收 81.6%；大和預估 2026 年營收年增約 40%，下半年受 GPU 與 ASIC 專案拉動。
  - 10 月營收約 NT$16.5 億，年增 26.46%（nStock 報導）。
- 提及量：無法量化（Reddit、StockTwits 皆無資料），無法與歷史基準比較。

- 主要主題（僅來自新聞與法人報導，非散戶）：
  - AI 伺服器與 GPU/ASIC 出貨動能
  - 毛利率創新高
  - 目標價上調
- 價格資料：nStock 顯示 2026-11-12 約 NT$2,035，其他頁面日期與價位不一致，本報告不以價格做判斷。

**Retail tilt：DATA_UNAVAILABLE（無可用散戶樣本，無法判定多空傾向）**

## Insider activity

`yf 6805.TW insider` 回傳空陣列。工具未回報任何內部人交易，但無法確認是「真無交易」或資料缺漏，依規則記為 DATA_UNAVAILABLE。

Net 6mo：DATA_UNAVAILABLE（無買進金額、無賣出金額、無 CEO/CFO 交易紀錄可引用）

## Ownership shifts

來源：`yf 6805.TW major_holders`（單一快照，無歷史序列，無法判斷趨勢）

| 指標 | 數值 |
|---|---|
| 內部人持股比例 | 21.1% |
| 機構持股比例（占總股本） | 40.3% |
| 機構持股比例（占流通股） | 51.1% |
| 機構家數 | 76 |

趨勢：DATA_UNAVAILABLE（無前期快照可比對）。

## Net sentiment score

Composite: **偏多（confidence：低）**

依據：
- 分析師面：9 家全數買進、0 家持有或賣出，偏多且無近期下調，權重最高，信心中等。
- 法人動向：大和上調目標價，基本面報導正面。
- 散戶面：DATA_UNAVAILABLE，無法納入計分。
- 內部人面：DATA_UNAVAILABLE，無法納入計分。

因散戶與內部人資料皆缺，綜合信心降為低。

Divergence flag: **DATA_UNAVAILABLE（無法判定）**。分析師傾向為偏多，但散戶傾向無資料，無法判斷是否背離。

## 資料缺口與待補

1. Reddit：WebFetch 遭擋，需允許 reddit.com 或改用其他來源。
2. StockTwits：api.stocktwits.com 需加入 session 網路允許清單。
3. 內部人交易：yf insider 回傳空陣列，建議確認 Yahoo cookie/crumb 是否恢復後重抓。
4. 評級逐筆紀錄：yf recommendations 未提供歷史升降評，需 crumb 恢復後重抓。
5. 機構持股趨勢：需第二期 major_holders 快照方可比對。

SENTIMENT REPORT COMPLETE
