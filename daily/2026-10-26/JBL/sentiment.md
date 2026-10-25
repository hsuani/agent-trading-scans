# Sentiment — JBL (Jabil Inc.) as of 2026-10-26

> 資料時點注意：今日為 2026-10-25，本報告以 2026-10-26 為 as-of 日期。yf 工具回傳的價格為 2026-10-25 11:11 UTC 的快取值（last_price 273.97 USD）；內部人交易最新一筆為 2026-10-20。WebSearch 結果日期標示混亂，已標註來源與不確定性。

## Analyst consensus

**10 家分析師：2 strongBuy / 7 buy / 1 hold / 0 sell / 0 strongSell**（來源：yf rec_summary，0m 期間）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（當前） | 2 | 7 | 1 | 0 | 0 |
| -1m | 2 | 7 | 1 | 0 | 0 |
| -2m | 2 | 7 | 1 | 0 | 0 |
| -3m | 2 | 6 | 2 | 0 | 0 |

- 近三個月評等幾乎不變，唯一變動是一家 Hold 轉 Buy（-3m 的 2 Hold 降為 1 Hold）。
- yf 工具未提供個別券商的升降評等明細，無法逐筆確認 upgrade/downgrade 事件。
- **目標價 (PT)：primary 來源 DATA_UNAVAILABLE。** WebSearch 聚合站的數字互相矛盾，僅供參考、不採信為確定值：
  - Fintel 平均 PT 約 435.07 USD（最高 506.10）。
  - Barchart 平均 PT 約 447.73 USD。
  - 個別事件（聚合站，日期未經驗證）：Goldman Sachs 由 482 下修至 375 USD（標示 2026-09-08）；Stifel 上修至 460 USD（標示 2026-06）；UBS 由 Neutral 升 Buy、PT 430 USD（標示 2026-08-11）；Zacks Research 降至 Hold。
- 若以 274 USD 現價對照上述平均 PT，隱含上漲空間約 59%，但 PT 來源品質不足以作為決策依據，僅表示分析師整體偏多。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)：DATA_UNAVAILABLE。** WebFetch 被拒絕（無法存取 reddit.com）；curl 經代理回傳 403（CONNECT tunnel failed）。未取得任何樣本討論串，無法計算 tilt。
- **StockTwits：DATA_UNAVAILABLE。** api.stocktwits.com 解析失敗（ENOTFOUND），無法取得 bullish/bearish 標籤統計。
- **X / 新聞與社群聚合：** WebSearch 找到 LunarCrush 頁面，快照顯示 24 小時內約 10K engagements、41 則貼文、社群情緒 100% 正向（樣本量小，發布日期與平台拆分不明）。另有 StockTwits 新聞稿（標示 2026-03）指出財報與買回計畫後情緒升至 "extremely bullish"（95/100），但屬歷史事件。
- **Buzz 量能：** 無可靠的提及數量或與常態比較，判定 DATA_UNAVAILABLE。
- **Retail tilt：** 無法判定（僅有少量聚合站正向快照，不足以構成 tilt）。
- **Themes（聚合站 TipRanks 等整理，非原始貼文）：**
  - 多頭：AI 資料中心相關需求。
  - 空頭：FY26 指引低於投資人預期的疑慮；部分財報後股價下跌（一則聚合站提及 Q4 公布後下跌約 6.7%，日期未驗證）。

## Insider activity

**Net 6mo（2026-04-26 至 2026-10-26）：$0.15M 買進 / $0.97M 賣出，淨賣出約 $0.82M（USD）**

| 日期 | 內部人 | 職位 | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-10-20 | Gary K. Schick | Officer | 賣出 @ 274.20–280.43 | 1,000 | 0.28 |
| 2026-07-17 | Nallicheri V. Tyagarajan | Director | 買進 @ 299.63 | 500 | 0.15 |
| 2026-07-15 | Gary K. Schick | Officer | 賣出 @ 315.05–330.00 | 1,000 | 0.32 |
| 2026-07-06 | Matthew Crowley | Officer | 賣出 @ 345.00 | 94 | 0.03 |
| 2026-04-30 | Gary K. Schick | Officer | 賣出 @ 340.00 | 1,000 | 0.34 |

- **Notable：** 6 個月內唯一的買進來自董事 Tyagarajan（500 股，約 $0.15M），是獨立董事的小額買進。
- CEO Michael Dastoor 在 6 個月窗口內無交易。前次紀錄為 2026-04-08 賣出 9,467 股（約 $2.71M）及 2026-01-22 賣出 15,000 股（約 $3.70M）。
- 12 個月脈絡：2025-10 至 2026-04 期間，CEO、COO、CTO、CFO、Director 等多人集中賣出，賣出價約 200–340 USD。此段期間賣出金額遠大於 6 個月窗口。
- 規模判讀：6 個月淨賣出 $0.82M 相對市值約 $28.7B（見下方 Ownership）屬很小比例。
- **DATA_UNAVAILABLE：** 10b5-1 計畫標記、是否為選擇權行使後賣出、以及部分交易之 Transaction 欄位（yf 回傳為空）。

## Ownership shifts

- **機構持股比例：** 99.5%（institutionsPercentHeld）；機構數量 1,529 家。內部人持股 1.16%。
- **市值估算（推導值，非工具直接回傳）：** BlackRock 持股 10,132,052 股、佔比 9.67%，推得流通股數約 104.8M 股；以 274 USD 計算，市值約 28.7B USD。
- **前十大機構（2026-06-30 季報）：**

| 機構 | 持股比例 | 持股數 (M 股) | 市值 (USD B) | 季度持股變化 |
|---|---|---|---|---|
| BlackRock | 9.67% | 10.13 | 2.78 | +4.7% |
| Vanguard Capital Mgmt | 6.58% | 6.89 | 1.89 | +3.0% |
| Texas Yale Capital | 6.00% | 6.29 | 1.72 | -0.0% |
| Vanguard Portfolio Mgmt | 5.19% | 5.43 | 1.49 | +1.5% |
| State Street | 4.70% | 4.93 | 1.35 | -0.1% |
| Wellington Mgmt | 4.10% | 4.30 | 1.18 | -4.9% |
| Primecap Mgmt | 3.02% | 3.17 | 0.87 | -3.5% |
| UBS Group | 2.89% | 3.03 | 0.83 | +79.4% |
| Geode Capital | 2.85% | 2.99 | 0.82 | +3.1% |
| JPMorgan Chase | 2.60% | 2.72 | 0.75 | +52.0% |

- 前十大合計約 47.6%。集中度中等偏高，但以指數型基金（BlackRock、Vanguard、State Street、Geode）為主。
- 趨勢：指數與被動持股多為小幅增加；主動型基金中 Wellington、Primecap 減持，UBS、JPMorgan 大幅加碼（相對變化，絕對股數仍小）。
- 持股變化欄位 `pctChange` 的計算基準未在工具輸出中說明，以上為相對變動的粗略解讀。

## Net sentiment score

**Composite：偏多（bullish lean），信心 中低**

| 面向 | 判讀 | 信心 | 依據 |
|---|---|---|---|
| 分析師評等 | 偏多 | 中 | 9/10 為 Buy 以上，評等近三月穩定；樣本僅 10 家 |
| 內部人交易 | 中性偏空（輕度） | 中 | 6 個月淨賣出 $0.82M，僅一筆董事小額買進；CEO 無交易 |
| 散戶社群 | 無法判定 | 低 | Reddit、StockTwits 皆 DATA_UNAVAILABLE；聚合站正向快照樣本小 |
| 機構持股 | 中性偏多 | 中 | 指數型持股穩定增加；部分主動基金減持 |

- 信心偏低的主因：(1) 散戶資料完全缺失；(2) 目標價來源互相矛盾，無法確認；(3) 內部人交易資料的 10b5-1 標記缺失。
- 價格面脈絡：現價 273.97 USD，低於 Apr–Jul 內部人賣出價區間（約 300–345 USD），亦低於聚合站提及的 Aug 快照價（約 308 USD，未驗證）。股價相對近期高點已回落，但 52 週高低價欄位為 NaN，無法精確計算。

**Divergence flag：是（有限度）。** 分析師偏多，內部人於 6 個月內以小額淨賣出為主。散戶 tilt 無法判定，故無法確認是否形成三方背離。

SENTIMENT REPORT COMPLETE
