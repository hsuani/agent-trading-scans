# Sentiment — DLR as of 2026-11-21

資料說明：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 直接抓取皆失敗（WebFetch 無法連線、api.stocktwits.com DNS 無法解析），以 WebSearch 補查亦無可用的散戶貼文或情緒比例。X 類討論搜尋無結果。散戶面向資料以 DATA_UNAVAILABLE 標示，不以新聞或分析師報導代替散戶情緒。yf 工具的 Yahoo 連線亦有 403 警告，結構化資料可能來自 repo cache，各欄位日期皆早於 2026-11-21。

## Analyst consensus

截至 yf rec_summary（0m）：34 家覆蓋，5 Strong Buy / 24 Buy / 5 Hold / 0 Sell / 0 Strong Sell，買進評等占 85%（29/34）。3 個月前為 5 SB / 23 Buy / 5 Hold，近 3 個月僅 Buy 增加 1 家，評等結構穩定。

- 近期評等變動（WebSearch 彙整，日期以各來源為準，部分未能交叉驗證）：
  - 2026-07-15：Guggenheim 升至 Buy。
  - 2026-07-24：TD Cowen 由 Hold 升至 Buy，目標價上調至 $222。
  - 2026-04-27：HSBC 由 Buy 降至 Hold。
  - 2026-01：Barclays 由 Underweight 調至 Equal-Weight；Bank of America 由 Buy 降至 Neutral。
  - 日期不明：Scotiabank 目標價由 $195 上調至 $222，維持 Sector Outperform；UBS 由 Neutral 升至 Buy（來源未標日期，未能確認）。
- yf recommendations 工具只回傳彙總計數，未提供逐筆升降評等紀錄，故上述事件僅來自 WebSearch。
- 目標價分歧：Barchart 平均約 $218.56、TipRanks 平均約 $218.90（24 家）、一則 2026-11-10 印尼站點顯示平均約 $224。各來源計算基準不同，且 Nasdaq/MarketBeat 將其列為 Moderate Buy，與 Barchart/TipRanks 的 Strong Buy 描述不一致。
- 股價參考：Fox Business 顯示 2026-11-06 收盤 $174.61；2026-11-10 站點顯示約 $180。2026-11-21 當日股價未能取得（DATA_UNAVAILABLE）。

## Retail social

- Reddit：r/wallstreetbets 與 r/stocks 搜尋皆無法連線（WebFetch 被拒）；WebSearch 亦未找到 DLR 相關近期討論串。篇數、情緒傾向、代表貼文：DATA_UNAVAILABLE。
- StockTwits / X：StockTwits API 無法解析；WebSearch 找到的 StockTwits DLR 頁面未載入多空比例，僅見新聞標題（Zacks 報導 Q2 FFO 優於預期並上修 2026 展望）。X 無可用結果。多空比例、訊息量：DATA_UNAVAILABLE。
- 散戶聲量（相對常態）：DATA_UNAVAILABLE，無法判定。
- 第三方代理指標：TipRanks 將投資人情緒標示為 Very Positive，但該數值來自其平台投資組合追蹤資料，並非散戶貼文，僅作參考。
- 主題（取自新聞與分析文章，非散戶原文）：
  - 多頭：AI 資料中心需求帶動出租與託管業務，媒體報導 colocation 預訂創紀錄、backlog 約 $1.4B（TIKR 標題）。
  - 空頭／風險：競爭、市場集中度、高負債（Zacks 列為主要風險）；另有評論認為其他 AI 題材股上檔空間更大。
- 整體散戶傾向：無可靠資料，無法判定 bullish / bearish / mixed。

## Insider activity

6 個月窗口（2026-05-21 至 2026-11-21）內：
- 公開市場買入：0 筆，$0.00M。
- 公開市場賣出：1 筆，$0.039M。
- 其他：Mandeville（董事）2026-05-29 股票授予 1,289 股（非公開市場交易，申報價 $0）。

主要紀錄：
- Mark R. Patterson（Director），2026-08-27，賣出 200 股，約 $0.039M，申報價 $193.96。

窗口外的重要紀錄（僅供脈絡）：
- Andrew P. Power（CEO），2025-09-15，賣出 58,000 股，約 $10.16M（價格區間 $175.10–$175.16）。
- Mary Hogan Preusse（Director），2025-12-01，賣出 4,166 股，約 $0.66M。
- Matt Mercier（CFO），2024-12-12，賣出 2,518 股，約 $0.47M。
- 資料提醒：部分列資料 Value 為空白，無法核對金額；Yahoo 連線異常，清單可能不完整。

判讀：6 個月內無 CEO/CFO 公開市場交易，內部人淨交易為小幅賣出（約 $0.04M），規模極小。但 CEO 於 2025 年 9 月有大額賣出，屬窗口外。

## Ownership shifts

- 機構持股占比約 100.4%（yf 數值，超過 100% 屬資料口徑問題，僅作方向參考）；機構數 1,823 家；內部人持股約 0.03%。
- 2026-09-30 前十大持股（13F 口徑）：

| 機構 | 持股數（百萬股） | 市值（B USD） | 占比 | 季度變化 |
|---|---|---|---|---|
| BlackRock | 43.19 | 7.31 | 11.42% | +6.6% |
| Vanguard Portfolio Mgmt | 31.93 | 5.41 | 8.44% | +5.9% |
| Cohen & Steers | 26.69 | 4.52 | 7.05% | -8.7% |
| Vanguard Capital Mgmt | 23.64 | 4.00 | 6.25% | +6.1% |
| State Street | 21.98 | 3.72 | 5.81% | +5.5% |
| Norges Bank（資料日 2026-06-30） | 19.29 | 3.27 | 5.10% | -12.3% |
| Geode Capital | 10.45 | 1.77 | 2.76% | +7.1% |
| Bank of America | 8.76 | 1.48 | 2.32% | -2.0% |
| APG Asset Mgmt US | 8.67 | 1.47 | 2.29% | +0.5% |
| Morgan Stanley | 7.56 | 1.28 | 2.00% | +16.1% |

- 趨勢：前十大中 7 家季度增持，Cohen & Steers 與 Norges Bank 減持幅度較大。整體偏向被動與大型機構持續加碼，主動基金方向分歧。

## Net sentiment score

綜合判定：**偏多（bullish），信心中等偏低**。

- 分析師面（權重高，資料完整）：偏多。85% Buy、0 Sell，近期有 Buy 升評與目標價上修，但 HSBC 曾降評，評等並非全面一致。
- 內部人面（權重中）：中性偏弱。6 個月無買入，僅一筆小額董事賣出；2025 年 CEO 大額賣出為窗口外舊資料。
- 機構持股面（權重中）：偏多。多數前十大持股季度增持。
- 散戶與社群面（權重高，但資料缺失）：DATA_UNAVAILABLE。無法評估訊息量與多空比例，綜合判定信心因此受限。

信心降低原因：Reddit、StockTwits、X 皆無法取得，散戶面為空白；目標價與評等來源互相矛盾；部分 WebSearch 結果日期不明。

Divergence flag：**無法判定（DATA_UNAVAILABLE）**。分析師偏多，但散戶面無資料，無法確認是否存在散戶與分析師方向相反的情況。若日後取得 StockTwits 或 Reddit 資料，應優先比對散戶傾向與分析師 85% Buy 是否一致。

SENTIMENT REPORT COMPLETE
