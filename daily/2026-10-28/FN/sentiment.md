# Sentiment — FN (Fabrinet) as of 2026-10-28

資料來源狀態：Yahoo 即時 API 連線失敗（ConnectionError），`pipeline/tools/yf.py` 改用 repo 快取 `prices/yf/FN.json`（refreshed 2026-10-27 12:03 UTC，未超過 14 天上限）。Reddit 與 StockTwits 本次皆無法取得（見下方）。報告依可取得資料撰寫，標示資料缺口。

## Analyst consensus

分析師覆蓋 9 位（yf `numberOfAnalystOpinions`）：**3 Strong Buy / 4 Buy / 2 Hold / 0 Sell**。
BUY 比例（Strong Buy + Buy）= 7 / 9 ≈ **77.8%**，Hold 22.2%，Sell 0%。

| 項目 | 數值 | 備註 |
|---|---|---|
| 評級分布 (0m / -1m / -2m / -3m) | 皆為 3 SB / 4 B / 2 H / 0 S | 四個月快照完全相同，代表快取期間無評級數字變動 |
| 目標價均值 | 687.78 USD | 快取 `info.targetMeanPrice` |
| 目標價中位 / 最高 / 最低 | 739 / 800 / 431 USD | |
| 現價（cnyes 快取報價） | 325.24 USD | 前收 314.94 USD |
| 均值目標相對現價 | 約 +111% | 目標價明顯落後於股價下跌，需留意 |
| 市值 | 11.65B USD | 35.83M 股 × 325.24 USD 反算吻合 |
| forward P/E / trailing P/E | 14.8x / 24.9x | yf info |

**近期評級動向（需標註）**：
- yf `recommendations` 並非逐筆升降評等紀錄，而是月度彙總快照，無法從中看出具體 upgrade / downgrade 事件。
- 網路搜尋摘要（未經 yf 驗證，來源為聚合站點）提到：2026-07-22 Needham 維持 Buy 並將目標價由 800 下調至 650；2026-10-15 有目標價下調至 431；2026-10-21 有目標價下調至 600。若屬實，目標價正隨股價下跌而下修，與 yf 快取的 688 均值存在落差，代表快取目標價可能偏舊。
- 同一搜尋摘要另指 Google Finance 統計為 8 位分析師（6 Buy / 2 Hold），與 yf 的 9 位略有出入，以 yf 為準。
- 下一個催化事件：財報（FQ1 FY2027）預計 2026-11-02 盤後公布（網路摘要，未經官方確認）。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：WebFetch 回傳 "unable to fetch from www.reddit.com"，本次無法取得貼文樣本、分數與留言數。soft-fail。無法判定 tilt。
- **StockTwits**：`api.stocktwits.com` DNS 解析失敗（ENOTFOUND），本次無法取得訊息流。soft-fail。
- **X / 新聞聊天**：WebSearch 未找到 2026-10 月 FN 的 Reddit 或 StockTwits 貼文內容。唯一可用的聚合器數據為 SentiSense（快照日期 2026-08-09，已過時）：30 日情緒分數 2.94（Neutral，回升中），Reddit 看多提及占比 14%、X 看多占比 21%，每日提及約 6 則。此數據過舊，僅供參考，不作為當日 tilt 依據。
- **聲量（buzz volume）**：無法與基準比較，定性判斷為低。依 SentiSense 快照每日約 6 則提及，可視為低聲量標的（數據為 8 月）。
- **Themes（由網路摘要歸納，非直接取自社群貼文）**：
  - 股價一個月內跌約 21%（網路摘要：10-23 收 314.94 USD，月跌 -20.94%），搜尋摘要未找到直接原因。
  - 財報前情緒偏弱（一則摘要稱單日跌 10.7%，歸因「財報前情緒偏弱」，未經驗證）。
  - 同業（TTMI、AAOI）10 月亦有分析師動作，產業面情緒可能連帶影響。

**Retail tilt**：無可靠社群樣本，**無法判定**。不引用任何社群貼文原文。

## Insider activity

6 個月窗口（2026-04-28 至 2026-10-28）：

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-09-03 | ARCHER EDWARD T | Officer | 公開市場賣出 @385.58–386.34 | 2,500 | 0.96 |
| 2026-05-22 | BAHRAMI HOMA | Director | 公開市場賣出 @711.91 | 2,500 | 1.78 |

- **6 個月淨額：買入 $0 M；賣出 $2.74 M（0.96 + 1.78），淨賣出 $2.74 M。**
- 另有 2026-08-11 與 2026-08-20 的股票獎勵（Stock Award / Grant，無現金價值），涉及 CEO Seamus Grady（合計 42,508 股）、President Harpal Gill（合計 17,120 股）、CFO Csaba Sverha（合計 10,257 股）、Officer Edward Archer（合計 8,071 股）及其他人員。獎勵屬例行薪酬，不計入買賣淨額。
- **CEO / CFO 動向**：CEO Grady 在窗口內無公開市場交易，最近一次賣出為 2025-11-26（約 1,003 萬 USD）。CFO Sverha 最近一次賣出為 2025-08-28（約 455 萬 USD）。窗口內 CEO / CFO 無買入。
- **President Gill**：最近一次賣出為 2025-09-04（約 504 萬 USD），窗口內無賣出。
- **董事會**：2026-02-25 Thomas Kelly 賣出約 115 萬 USD；窗口內僅 Bahrami 一筆大額賣出。
- **觀察**：窗口內公開市場賣出金額小（約 $2.7M），主要來自 Officer 與 Director，無 CEO / CFO 出售。相較 2025 年 8–9 月的大量賣出（數百萬 USD 級，多筆），賣壓已明顯降低。無內部人公開市場買入紀錄。
- 注意：yf 將獎勵與授予標示為 "D"（direct ownership），交易碼無法從快取判定是否為稅務代扣等例行交易。

## Ownership shifts

yf `inst_holders`（資料日 2026-06-30，即 Q2 13F 數據，非最新）：

| 機構 | 持股比 | 股數 | 季度股數變動 |
|---|---|---|---|
| BlackRock | 13.46% | 4.82M | -13.8% |
| T. Rowe Price Associates | 5.42% | 1.94M | -49.5% |
| Vanguard Portfolio Mgmt | 5.30% | 1.90M | -11.0% |
| FMR LLC | 5.14% | 1.84M | -13.1% |
| Vanguard Capital Mgmt | 4.51% | 1.62M | +0.6% |
| JPMorgan Chase | 4.40% | 1.58M | +42.8% |
| State Street | 3.66% | 1.31M | +0.9% |
| Geode Capital | 2.99% | 1.07M | -13.1% |
| Invesco | 2.50% | 0.90M | -16.4% |
| T. Rowe Price Investment Mgmt | 2.37% | 0.85M | +278.6% |

- 前十大機構合計持股約 17.83M 股，依 `pctChange` 反推上季約 20.24M 股，**淨減持約 11.9%**（10 家中 6 家減、4 家增）。
- 機構持有家數 1,027 家（`institutionsCount`）。
- **資料品質警示**：`major_holders` 回傳 `institutionsPercentHeld = 1.037`（即 103.7%），數值不可能成立（機構持股比不應超過 100%），可能為 Yahoo 欄位重複計算或單位問題。本報告不採用該欄位作為結論依據。`insidersPercentHeld = 0.26%`，數值合理。
- **方向**：季度數據顯示機構淨減持（T. Rowe Price Associates 大幅減碼為主因之一），但 JPMorgan 與 T. Rowe Price Investment Management 增持。資料為 6 月底快照，與近期 21% 月跌之間的機構動向無法驗證。

## Net sentiment score

- **分析師（看多側）**：BUY 77.8%、無 Sell，但目標價隨股價下修，均值目標相對現價仍有大幅空間，代表分析師評等偏多，價格與目標之間落差大。
- **內部人（偏弱）**：6 個月淨賣出約 $2.74M，無買入，但無 CEO / CFO 出售，規模小於 2025 年。
- **機構（偏弱）**：前十大淨減持約 11.9%（6 月快照）。
- **散戶（無資料）**：Reddit / StockTwits 皆未取得，SentiSense 快照（8 月）情緒中性偏溫。
- **股價動能（作為情緒代理）**：近一個月約 -21%，為偏弱訊號。

**Composite：中性（Neutral）偏弱，信心低（low confidence）。**
理由：分析師評等仍偏多，但內部人與機構流向偏淨流出，股價月跌，散戶面無可用樣本，無法形成完整交叉驗證。

**Divergence flag：無法判定（no）**。缺乏可靠散戶 tilt 數據，無法判斷散戶與分析師是否方向相反。若後續補到散戶資料，需特別檢查 Reddit / StockTwits 是否看空，以判斷是否形成分歧。

## 資料缺口與後續

1. Reddit、StockTwits 皆失敗，建議次日重試或以其他來源補足散戶面。
2. yf 即時 API 失敗，本報告全部依快取（2026-10-27 12:03 UTC）。目標價與評級可能落後於近期的目標價下修。
3. `institutionsPercentHeld` 數值異常（103.7%），已排除。
4. 網路摘要（分析師動作、財報日、月跌原因）未經一手來源確認，僅作為背景參考。

SENTIMENT REPORT COMPLETE
