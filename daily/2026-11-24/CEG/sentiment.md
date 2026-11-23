# Sentiment — CEG as of 2026-11-24

資料說明：yfinance 即時連線失敗 (Cookie/crumb 取得失敗)，rec_summary、major_holders、inst_holders、insider 皆使用快取資料，屬預期情況，非錯誤。13F 持股資料截至 2026-09-30。社群資料以 WebSearch 取得，多數來源未標示日期，可信度低。

## Analyst consensus
20 buy (含 6 strongBuy) / 5 hold / 0 sell，共 25 位分析師。

近三個月變化 (rec_summary 快照)：

| 期間 | strongBuy | buy | hold | sell | 合計 |
|---|---|---|---|---|---|
| 目前 (0m) | 6 | 14 | 5 | 0 | 25 |
| -1m | 6 | 14 | 5 | 0 | 25 |
| -2m | 6 | 12 | 4 | 0 | 22 |
| -3m | 6 | 12 | 4 | 0 | 22 |

評級結構偏多，沒有 sell 評級，近三個月 buy 增加 2 家、hold 增加 1 家，覆蓋家數增加 3 家。recommendations 工具回傳內容與 rec_summary 相同，為彙總快照而非逐家升降評等紀錄，因此無法從工具確認個別券商的升降評等動作。

近期目標價與評級動向 (WebSearch，來源：TIKR、Stocktwits)：
- Bernstein：目標價由 $296 降至 $293，維持 Outperform，2026-11-17 報導，隱含上行空間約 5%。
- BMO：目標價由 $316 升至 $335，維持 Outperform，隱含上行空間約 23%。
- Citi：目標價由 $348 降至 $297，維持 Neutral，報導未標日期，需再確認時間。
- Mizuho：目標價 $390 降至 $330，Neutral，約為 2026 年 3 月資料。
- CIBC：目標價 $346，Outperform，日期不明。
- 共識目標價約 $339，較一年前的 $404 下降約 16%，仍高於當時股價約 22%。

股價參考：由 Bernstein 與 BMO 的上行空間推算，2026-11-17 股價約在 $272 至 $279 區間。同一來源指出，股價較 52 週收盤高點低約 28%。

## Retail social
- Reddit：WebSearch 未找到 2026 年 11 月的具體討論串。AltIndex 顯示近期 r/wallstreetbets、r/stocks、r/investing 提及數為 0，但頁面未標日期。2026 年 2 月的報導指出，討論由 1 月的 r/stocks、r/options 偏多期權討論，轉為 r/stockmarket 的正反分歧辯論。傾向：近期不明，早期偏多後轉為分歧。
- StockTwits / X：StockTwits 最後一筆有日期的情緒讀數為 2026 年 3 月 5 日，為 bearish (43/100)。一篇未標日期的 2026 年文章寫到，當時情緒轉為 bullish、訊息量增加 311%。AltIndex 顯示 100/100 bullish，同樣未標日期。直接取用 StockTwits 即時頁面未成功，soft-fail 處理。
- 社群提及量：整體屬低 (qualitative)，但缺乏可靠的 2026 年 11 月基準，無法量化與平時相比的倍數。
- 主要話題：
  - 核能與無碳資產、AI 與資料中心用電需求 (多數偏多論述)
  - Calpine 收購案的整合與效益 (有人認為被低估，也有人認為散戶不買帳；可引用標題：「Retail Investors Lose Faith」)
  - 估值：2026 年 2 月時 P/E 約 30x，產業平均約 19x (偏空論述)
  - 政策與監管：FERC 相關風險；德州州長人選變動可能影響 Calpine 併入的天然氣電廠 (偏空風險)
  - 股價下跌時的逢低接手論述 (可引用標題：「Retail Is Already Diving In To Buy The Dip」)
- 散戶語氣：無法可靠判定。近期有效資料不足，早期 (2024–2025) 以偏多為主，2026 年 3 月轉為偏空，近期資料缺失。

## Insider activity
統計區間：2026-05-24 至 2026-11-24 (近 6 個月)。

Net 6mo：$0.42M 買入 (公開市場)，$0 賣出。

| 日期 | 人員 | 職位 | 交易 | 股數 | 金額 (USD) |
|---|---|---|---|---|---|
| 2026-08-11 | CRANDALL ROGER W | Director | 公開市場買入，約 $278.62/股 | 1,500 | $0.42M |
| 2026-08-04 | CRANDALL ROGER W | Director | 股票獎勵 (Grant) | 462 | $0.12M (非公開市場) |

說明：
- 唯一公開市場交易為董事 Roger Crandall 的買入，金額與股數 × 價格核對一致 (1,500 × $278.62 ≈ $0.42M)。
- 6 個月內沒有偵測到內部人賣出。
- 2026-04-28 的董事股票獎勵 (每人 556 股) 與 2026-02-09 的管理層列表 (CEO Joseph Dominguez 等人，無金額欄位) 不在區間內，或屬於獎勵與扣繳性質，不計入淨買賣。2026-02 列表中，CFO 職稱出現兩位 (Daniel Eggers、Shane Smith)，需以 SEC Form 4 核對。
- 高層 (CEO/CFO) 在區間內無公開市場買賣。內部人持股比例約 0.35%。

## Ownership shifts
- 機構持股比例：約 85.0%，機構家數 2,534 家。
- 13F 截至 2026-09-30 的前十大持股合計約 41.9%。前十大中 8 家較上期增持，2 家減持：
  - Blackrock：7.36%，較上期 +5.4%，約 $6.49B
  - Vanguard Capital Management：6.20%，+3.6%，約 $5.47B
  - State Street：5.80%，+5.1%，約 $5.12B
  - Vanguard Portfolio Management：4.66%，+3.5%，約 $4.11B
  - Capital International Investors：4.10%，+13.9% (最大增持)，約 $3.62B
  - ECP ControlCo, LLC：4.03%，持平，約 $3.56B (推測為 Calpine 交易取得股份之相關實體，未經確認)
  - Invesco：3.08%，-2.4%，約 $2.72B
  - Morgan Stanley：2.69%，+4.7%，約 $2.38B
  - Geode Capital：2.22%，+4.0%，約 $1.96B
  - FMR：1.79%，-3.6%，約 $1.58B
- 趨勢判讀：機構整體呈淨增持，主動型基金 (Capital International) 加碼較明顯，FMR 與 Invesco 小幅減持。

## Net sentiment score
Composite：**偏多 (bullish)，信心中低 (medium-low)**。

- 分析師面：偏多。20/25 buy，無 sell，共識目標價約 $339，高於隱含股價約 22%。但目標價趨勢向下 (由 $404 降至 $339)，且 Citi、Mizuho 近期降目標價，偏多的強度有所減弱。
- 內部人面：小幅偏多。董事公開市場買入 $0.42M，無內部人賣出。樣本量小，僅一筆。
- 機構面：偏多。前十大多數加碼，機構持股約 85%。
- 散戶面：中性偏不明 (信心低)。最後有日期的 StockTwits 讀數為偏空 (2026-03)，其餘資料皆未標日期，無法確認 2026 年 11 月的散戶語氣。

Divergence flag：**無法判定 (資料不足)**。分析師與機構偏多，但散戶近期資料缺失，無法確認兩者是否背離。若未來取得可靠的 11 月散戶資料，應再檢視是否出現與分析師相反的傾向。

## 摘要表

| 面向 | 指標 | 讀數 | 判讀 | 信心 |
|---|---|---|---|---|
| 分析師共識 | 評級分布 (buy/hold/sell) | 20 / 5 / 0 | 偏多 | 中高 |
| 分析師動向 | 共識目標價 (一年前 → 現在) | $404 → $339 | 目標價下修 | 中 |
| 內部人 | 6 個月淨額 (公開市場) | 買 $0.42M / 賣 $0 | 小幅偏多 | 低 (樣本少) |
| 機構持股 | 前十大 QoQ 方向 | 8 增 / 2 減，合計 41.9% | 偏多 | 中 |
| 機構持股 | 機構持股比例 | 約 85.0% | 高度機構化 | 高 |
| 散戶 (Reddit) | 近期提及與語氣 | 近期資料不足，2 月起分歧 | 不明 | 低 |
| 散戶 (StockTwits) | 最近有日期讀數 | 2026-03 bearish (43/100) | 偏空 (過時) | 低 |
| 綜合 | 情緒綜合判斷 | 偏多 | 信心中低 | 中低 |
| 背離旗標 | 散戶 vs 分析師 | 無法判定 | 資料不足 | - |

SENTIMENT REPORT COMPLETE
