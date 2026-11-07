# Sentiment — ALAB as of 2026-11-08

資料截止點以 2026-11-08 為準; 本環境時間為 2026-11-07, 11/7–11/8 的盤中與社群資料未能驗證。

## Analyst consensus

25 位分析師: 6 Strong Buy / 12 Buy / 7 Hold / 0 Sell / 0 Strong Sell。Buy 以上占 72% (18/25), 無賣出評等。

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| 當期 (0m) | 6 | 12 | 7 | 0 | 25 |
| -1m | 7 | 11 | 8 | 0 | 26 |
| -2m | 7 | 12 | 7 | 0 | 26 |
| -3m | 7 | 12 | 7 | 0 | 26 |

近一個月: Strong Buy 減 1、Buy 加 1、Hold 減 1, 合計由 26 降為 25 (疑為一位分析師未計入或撤除評等, 原因未明)。三個月內評等結構穩定, 無賣出評等出現。

近期目標價與評等變動 (來自網路摘要, 日期與季度不明, 需以原始來源再核):
- Needham: 目標價 $260 → $425, 維持 Buy。
- TD Cowen: 目標價 $425 → $375, 維持 Hold。
- Citigroup: 目標價 $275 → $250, 維持 Buy (對應 Q4 2025 財報後, 約 2026-02)。
- Morgan Stanley: 媒體標題稱其認為有 75% 上行空間 (評等與目標價未驗證)。
- Quiver 統計 6 個月內 15 位分析師中位數目標價 $250, 但此數字與 2026-07 之後的成交價區間 (約 $274–468) 明顯不一致, 判定為過時資料, 不採信。

yf 工具本次只回傳月度彙總, 未提供逐筆升降評紀錄, 故無法列出完整的 upgrade/downgrade 時間線。

## Retail social

- Reddit: 本次未能直接抓取 r/wallstreetbets 或 r/stocks 搜尋結果 (依指示改用 WebSearch)。唯一可得的聚合數據來自 AltIndex, 最後更新為 2026-09-08: 每日約 5 則提及 (低量), 月提及量 2–10 則, Reddit 情緒分數 66/100 (中性偏多)。此資料距今約兩個月, 僅供背景參考, 不代表本週情緒。
- StockTwits / X: StockTwits API 直接呼叫失敗 (DNS 解析失敗, api.stocktwits.com 未列入本 session 允許網域), 軟失敗處理, 需於 session 網路設定中放行才能重試。網路摘要提到 StockTwits 日均約 192 則提及, 並有一篇標題為 "Retail Sentiment Hits Year-High" 的文章, 描述財報後散戶情緒創年內新高 (日期未明, 疑為近期)。另一摘要稱散戶情緒指數 95/100 屬 "extremely bullish", 但原始來源無法核對, 僅作參考。
- 聚合情緒: AltIndex 綜合 (Reddit + StockTwits + 論壇) 為 76/100 偏多, 但註明已較 30 日均值降溫。
- 散戶聲量判定: 相對於 ALAB 過去平均, 本次無法量化為確定數字。目前證據顯示聲量屬中等偏高 (StockTwits 量高於 Reddit), 但缺乏同期基準。

Themes (主要主題):
1. AI 連接需求與 Amazon–Anthropic Trainium 合作被視為長期順風 (Quiver 摘要中提及 Reddit 討論)。
2. 財報超預期後股價仍跌, 市場焦點移至毛利與支出展望及高估值 (Tikr 摘要, 2026-11-04 前後)。
3. 內部人持續出售, 被視為偏空訊號 (見下節)。
4. 與 NVDA Spectrum-X 及 UEC 開放標準的競爭風險 (論壇討論, 日期不明)。

Retail tilt: 偏多但降溫, 信心低 (資料多為過時或無日期)。

## Insider activity

Window: 2026-05-08 至 2026-11-08 (6 個月)。數據來源: yf insider (2026-09-02 為最近一筆公開市場賣出)。

| 內部人 | 職稱 | 賣出筆數 | 賣出金額 (USD M) |
|---|---|---|---|
| Gajendra Sanjay | President | 4 | 238.2 |
| Alba Manuel | Director | 4 | 132.5 |
| Mohan Jitendra | CEO | 3 | 83.6 |
| Dyckerhoff Stefan A | Director | 4 | 17.5 |
| Mazzara Philip | General Counsel | 3 | 5.8 |
| Lazar Jack R | Director | 1 | 3.6 |
| Mayer Bethany J | Director | 1 | 0.3 |
| 合計 | | 20 | 481.5 |

- 公開市場買入: 0 筆、0 USD。
- 賣出股數合計約 1,640,454 股, 平均成交價約 $293 (與金額換算一致)。
- 非公開市場交易: 股權獎勵 (Hurlston、Barratt、Cota、Lazar、Mayer、Dyckerhoff 等董事, 以及 Mazzara) 與股票贈與 (Gajendra 約 226,189 股, 2026-05-22)。獎勵與贈與不計入淨買賣。
- 主要人士: Gajendra (President) 與 Mohan (CEO) 合計約 USD 322M, 占總賣出額約 67%。
- 價格脈絡: 5 月賣出價約 $190–293, 7 月約 $430–468 (高點), 8 月約 $310–352, 9 月約 $274–289。自 7 月高點到 9 月, 成交價下跌約四成。目前 (11/8) 股價未能驗證。
- 10b5-1 交易計畫與否, 本資料無法判定, 不應直接解讀為主觀看空。
- 網路摘要 Quiver 稱 6 個月內內部人 135 筆賣出、0 筆買入, 與本地彙總方向一致 (筆數定義不同)。

Net 6mo: USD 0 買入 / USD 481.5M 賣出 (約 0.48B), 淨賣出。Notable: Gajendra (President) 4 筆共約 USD 238M; Mohan (CEO) 3 筆約 USD 84M。

## Ownership shifts

- 內部人持股: 10.24%。
- 機構持股 (占流通股): 75.25%; 占流通股 (float) 83.84%; 機構數 1,342 家。
- 僅有單期快照, 無時間序列, 無法判定集中度趨勢。

## Net sentiment score

Composite: 中性 (信心: 中低)。

- 分析師面: 偏多 (信心: 中)。72% Buy 以上, 0 Sell, 三個月結構穩定。但目標價數據多為非當期, 需核實。
- 散戶面: 偏多但降溫, 聲量中等 (信心: 低)。主要資料為過時或無日期。
- 內部人面: 偏空 (信心: 高, 數據明確)。6 個月淨賣 USD 481.5M, 零買入。但須考慮 10b5-1 計畫與持股分散等因素。

Divergence flag: 是 (內部人與分析師方向相反)。散戶與分析師方向並不相反 (兩者皆偏多), 故不構成「散戶與分析師背離」的典型訊號。內部人賣出與分析師買入之背離值得後續追蹤。

本報告不含交易建議。

SENTIMENT REPORT COMPLETE
