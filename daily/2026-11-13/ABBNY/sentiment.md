# Sentiment — ABBNY (ABB Ltd ADR) as of 2026-11-13

資料截止：2026-11-12 快取（prices/yf/ABBNY.json，_refreshed_at 2026-11-12）。不使用 2026-11-13 之後資料。

## Analyst consensus

快取 rec_summary（0m）：6 位分析師，0 strong buy / 0 buy / 5 hold / 0 sell / 1 strong sell，即 0 買 / 5 持有 / 1 賣。
recommendationKey = hold，recommendationMean = 3.17（1 = strong buy，5 = sell，數值略偏持有偏賣）。

| 項目 | 數值 | 備註 |
|---|---|---|
| 平均目標價 | USD 94.71 | 相對快取現價 USD 84.64 上檔約 +11.9% |
| 最高 / 最低目標價 | USD 114.94 / USD 80.00 | 最低目標價略低於現價（約 -5.5%） |
| 現價（快取） | USD 84.64 | 前收 USD 84.66 |
| 52 週區間 | USD 67.24 – 110.20 | 現價位於區間中上段 |
| 市值 | USD 152.8B | 84.64 × 1,805.6M 股，手算一致 |
| Forward P/E / Trailing P/E | 22.6x / 30.7x | 快取 info 欄位 |

評等分布歷史（rec_summary 快照）：
- 0m：0 買 / 5 持有 / 1 強賣
- -1m：0 買 / 5 持有 / 1 強賣
- -2m：0 買 / 3 持有 / 2 強賣
- -3m：0 買 / 3 持有 / 2 強賣

近 2–3 個月強賣由 2 家降為 1 家，持有由 3 家增至 5 家，評等結構向中性收斂，但仍無買進評等。

近期調整（網路搜尋彙整，個別日期無法確認）：
- 有報導指 SEB Equities、DNB Carnegie、Pareto 曾升至 Buy（Pareto 目標 CHF 96.40）。日期 DATA_UNAVAILABLE。
- Erste Group 降至 Hold（來源時間點不一：部分報導指 2026-08；另有 2026-07-30 Erste 偏正面預估之報導，需以原始評等紀錄核對）。
- Citi 將瑞士掛牌股降至 Neutral，理由為「fully valued」，目標 CHF 76（報導指現價約 CHF 71.10，30% 年初至今漲幅、約 30x P/E）。日期 DATA_UNAVAILABLE。
- Kepler Cheuvreux 因估值因素下調評等（日期 DATA_UNAVAILABLE）。
- Barclays 以 Equal Weight 重新覆蓋（CHF 76）；Deutsche Bank 維持 Hold 並調高目標至 CHF 76；RBC 以 Sector Perform 調高目標至 CHF 83。
- BNP Paribas 曾於 2025-10 首次給予 strong sell（屬一年以上舊資料，僅供參考）。

歷史逐筆評等紀錄（yf recommendations 僅有彙總計數，無逐家分析師日期）：部分 DATA_UNAVAILABLE。

目標價來源分歧：StockAnalysis 平均 USD 85.25（2026-02 更新）；Investing.com 平均 USD 93.32；MarketBeat 共識目標 USD 58.00（"Reduce"）；Zacks 平均 USD 71.50。各來源分析師組合與日期不同，不宜直接合併。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。依指示不直接抓取 Reddit；網路搜尋未找到 ABBNY 相關討論串，無法估計討論量或語氣。
- StockTwits：DATA_UNAVAILABLE。搜尋結果僅為通用 ABB 代號頁，無可見多空比例。
- X / 新聞輿情：搜尋未取得近期散戶意見樣本。可見的散戶相關訊號僅有 TipRanks 自家「Investor Sentiment: Positive」標籤，屬該平台專有指標，非社群原文統計，權重低。
- 討論量（相對常態）：DATA_UNAVAILABLE，無法給出定性評估。
- 主題：無可引用之散戶原文（不引用任何帖文）。新聞與分析師端反覆出現的論點為估值偏高（P/E 約 30x、目標價多數低於或接近現價）與「執行力與營收/訂單強勁、資本配置紀律佳」兩種對立論述。此為機構/分析師端論點，不代表散戶立場。
- 散戶傾向：DATA_UNAVAILABLE（無法判定偏多、偏空或分歧）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。
- yf insider 回傳為空列表。
- major_holders 中 insidersPercentHeld = 0.0，此欄位對 ABB 這類大型瑞士股不具參考價值，不能視為「內部人無持股」的證據。
- 未取得 CEO/CFO 或其他高管交易紀錄。若需判斷，需另查 SIX 內部人申報或 SEC Form 4 之對應資料（DATA_UNAVAILABLE）。

## Ownership shifts

- institutionsCount：85（快取）。
- institutionsPercentHeld：0.2%，此為 ADR 美國 13F 追蹤口徑，數值明顯低估全體機構持股比例，僅能作為「美國 13F 在 ADR 上的部位」參考，不代表 ABB 整體機構持股。
- 前十大 13F 持有人（2026-09-30 或 2026-06-30 申報）以 Northeast Investment Management（680,799 股，-0.9%）與 Kornitzer Capital（283,580 股，-7.0%）居首，其餘多為小型部位。Great Lakes Advisors 增持 34.2%（基數小）。
- 整體趨勢：ADR 層級美國機構部位小幅減碼為主，但樣本極小，方向性結論信心低。全體機構持股趨勢：DATA_UNAVAILABLE。

## Data quality flags

1. 財報資料異常：快取 earnings_dates 顯示 2026-10-20 季報 EPS 估計 1.40、實際 0.65、驚喜 -53.69%。此與前幾季估計約 0.6–0.8 的水準差異極大，疑似估計值或實際值錯誤，未經核實前不採信。
2. 現價分歧：快取現價 USD 84.64（2026-11-12）；網路上 MarketBeat 快照分別為 USD 94.70、107.02、108.47，日期不明。以快取為準，網路數字不作為現價依據。
3. 網路搜尋結果多數無明確日期，僅能作為輔助語境。
4. 下一次財報日期：DATA_UNAVAILABLE。

## Net sentiment score

- 分析師端：中性偏保守（5 持有 / 1 強賣 / 0 買，平均評等 3.17，平均目標較現價高約 12%，但最低目標低於現價，且估值爭議明顯）。
- 散戶端：DATA_UNAVAILABLE。
- 綜合：中性（Neutral），信心低。主因是分析師評等結構偏中性、缺乏可靠散戶與內部人資料，無法形成雙邊共識。

Divergence flag：無法判定（no）。散戶端資料缺失，無法確認散戶傾向是否與分析師傾向相反。

本報告僅整理情緒與共識資料，不構成交易建議。

SENTIMENT REPORT COMPLETE
