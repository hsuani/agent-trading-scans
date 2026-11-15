# Sentiment — AMD as of 2026-11-16

資料截止說明：環境日期為 2026-11-15，本報告以 2026-11-16 為 as-of。yf 工具回傳的最新內部人交易為 2026-10-15，Oppenheimer 升評為 2026-11-09；2026-11-16 當日的價格與新增資料未納入。

## Analyst consensus

最新月（0m）共 54 位分析師：5 strongBuy / 42 buy / 7 hold / 0 sell / 0 strongSell，買進或以上佔 87%（47/54）。

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 | 買進以上占比 |
|---|---|---|---|---|---|---|---|
| 0m（當前） | 5 | 42 | 7 | 0 | 0 | 54 | 87.0% |
| -1m | 5 | 39 | 11 | 0 | 0 | 55 | 80.0% |
| -2m | 5 | 40 | 11 | 0 | 0 | 56 | 80.4% |
| -3m | 4 | 40 | 11 | 0 | 0 | 55 | 80.0% |

近期動作：
- 最近一個月 hold 由 11 降至 7，買進以上由 44 增至 47，表示約 4 位持 hold 者轉向偏多（yf 僅提供月度彙總，無個別券商的升降評等明細，無法逐家確認）。
- Oppenheimer 於 2026-11-09 由 Perform 升至 Outperform，目標價 $600（對照 2026-11-06 收盤 $449.04，約 +34%）。
- DA Davidson 將目標價升至 $600 並維持 Buy；StoneX 重申 Buy，目標價 $685（二手來源，見 WebSearch）。
- 目標價的完整歷史變動 yf 工具未提供，無法列出中位數或變動幅度。
- 賣出評等數量四個期間皆為 0。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 的 search.json 皆無法存取（WebFetch 回報 unable to fetch reddit.com），本節無直接樣本，soft-fail。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，疑為 session 網路白名單未開放），soft-fail。需在 session 網路設定中允許該網域後才能重試。
- X / 新聞二手摘要（WebSearch，搜尋摘要非原文）：
  - 有摘要指出 StockTwits 的散戶情緒在 11/4 與 11/9 來到當期偏多高點，訊息量高，但該數字僅見於二手摘要，未能直接核實。
  - 財經媒體標題仍寫 "Wall Street Remains Split On The Stock"，顯示市場觀點分歧。
- 聲量（buzz）：無可量化的提及次數。以二手摘要判斷，11/4 與 11/9 前後聲量偏高；其餘時段無法評估。
- 散戶傾向：二手來源偏多（bullish）、信心低，原因是無直接社群樣本可驗證。
- 主要議題（Themes）：
  1. 資料中心成長：Oppenheimer 預估 2027 資料中心營收年增 135%，佔營收約 85%，並預估 2027 年約 3 GW、2028 年約 4 GW 產能。
  2. 估值偏高：Trefis 指 AMD 約為 FY2026 調整後 EPS 預估的 61.3 倍，有人認為獲利了結壓力大。
  3. 內部人賣出：Trefis 認為 8、9 月的內部人賣出可能拖累情緒（見下節）。
  4. 財報反應：FQ3（11/3 公布）營收與 EPS 優於預期，但市場反應保守，11/5 股價隨 AI/晶片類股拋售下跌。
  5. 長期風險：MarketBeat 提及 Meta 自研 AI 晶片為長期競爭壓力。
- 代表性觀點（標題原句，非原文轉貼）：「Server And Data Center Success Is 'Undeniable'」（Oppenheimer 升評相關標題）；「Wall Street Remains Split On The Stock」。

## Insider activity

回溯期間 2026-05-16 至 2026-11-15（6 個月）：

- 公開市場買進（Purchase）：0 筆、$0。
- 公開市場賣出（Sale，附成交價）：16 筆，合計約 $193.1M。

| 內部人 | 職稱 | 賣出筆數 | 賣出股數 | 賣出金額（USD M） |
|---|---|---|---|---|
| Lisa T. Su | CEO | 3 | 235,000 | 112.95 |
| Forrest E. Norrod | Officer | 4 | 71,271 | 34.36 |
| Mark D. Papermaster | CTO | 4 | 48,180 | 23.94 |
| Paul D. Grasby | Officer | 1 | 15,000 | 7.72 |
| Jean X. Hu | CFO | 1 | 15,000 | 7.11 |
| Nora M. Denzel | Director | 1 | 10,447 | 5.45 |
| Ava M. Hahn | General Counsel | 2 | 3,136 | 1.53 |

驗算：Su 3 筆合計 235,000 股，以約 $480 均價估算約 $113M，與工具回傳的 $112.95M 相符。

重點觀察：
- 賣出金額最大者為 CEO Su：2026-06-10（約 $57.6M）與 2026-09-10（約 $48.1M），另 2026-08-18 約 $7.2M。
- Norrod 與 Papermaster 的賣出多集中在月中（如 8/14、9/15、10/15），且同時伴隨期權行權（conversion，價格 $84.85），pattern 可能屬預先排定的交易計畫，但工具未標示 10b5-1，無法確認。
- 另有 16 筆無成交金額的紀錄（合計約 86 萬股，多為 8/7 與 8/14 前後），性質不明，可能為稅款預扣或歸屬相關處分，本報告不計入賣出。
- 贈與（gift）4 筆、行權（conversion）7 筆，未計入賣出。
- 董事會成員有 2026-05-14 之限制性股票（三人各 2,613 股）紀錄，無成交金額，不計入。
- 內部人持股比例約 0.63%（yf major_holders）。

## Ownership shifts

- 機構持股比例約 76.7%，機構數約 5,234 家（yf major_holders）。
- 前十大機構合計約 37.6%（依 yf inst_holders）：

| 機構 | 持股比例 | 股數（M） | 持股變動（pctChange） | 報告期 |
|---|---|---|---|---|
| BlackRock | 9.16% | 150.3 | +3.3% | 2026-06-30 |
| Vanguard Capital Mgmt | 6.49% | 106.5 | +0.5% | 2026-06-30 |
| State Street | 4.60% | 75.4 | +1.5% | 2026-09-30 |
| Invesco | 3.29% | 54.0 | +1.6% | 2026-09-30 |
| FMR | 3.25% | 53.3 | +108.5% | 2026-09-30 |
| Geode | 2.46% | 40.4 | +2.1% | 2026-09-30 |
| JPMorgan | 2.32% | 38.0 | -5.7% | 2026-09-30 |
| Vanguard PM | 2.31% | 37.9 | +0.9% | 2026-06-30 |
| T. Rowe Price | 2.19% | 35.9 | +24.6% | 2026-06-30 |
| Morgan Stanley | 1.48% | 24.3 | +2.1% | 2026-06-30 |

- 趨勢：多數前十大機構為加碼，FMR 大幅加碼（約 +108%）與 T. Rowe 加碼（約 +25%）最為明顯；JPMorgan 為唯一明顯減碼者。
- 注意：機構 pctChange 來自 13F，報告期滯後約 1–3 個月，無法反映 11 月的即時部位。

## Net sentiment score

- 分析師面：偏多（bullish），信心高。買進以上 87%、零賣出評等，近一月趨勢向上。
- 散戶面：偏多（二手摘要），信心低。Reddit 與 StockTwits 皆未取得，僅有 WebSearch 摘要。
- 內部人面：偏空（以金額計），信心中。6 個月內 $193M 公開市場賣出、零買進；但多數屬例行或排程性質，不能直接解讀為看空。
- 機構面：中性偏多，前十大多數加碼，信心中（13F 有滯後）。

綜合：**偏多（bullish），信心中低**。主要支撐來自分析師共識與機構加碼；主要拖累是內部人持續賣出與估值偏高（約 61 倍 FY26 調整 EPS）。

Divergence flag：**部分（是）**。
- 分析師與散戶（二手來源）同向偏多，無整體背離。
- 內部人賣出與分析師偏多傾向相反，為值得留意的分歧。此為情緒面的觀察，不構成交易建議。

SENTIMENT REPORT COMPLETE
