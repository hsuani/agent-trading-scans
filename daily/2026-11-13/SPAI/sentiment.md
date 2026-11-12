# Sentiment — SPAI (Safe Pro Group Inc.) as of 2026-11-13

資料截止: 2026-11-13。所有數據皆取自該日以前可得來源 (yf 快取 refreshed 2026-11-12)。

## 資料可用性總覽

| 來源 | 狀態 |
|---|---|
| yf rec_summary / recommendations | 可用 (live feed 被擋, 使用 repo 快取 prices/yf/SPAI.json) |
| yf insider | 可用 (僅 11 筆, 交易代碼欄位空白) |
| yf major_holders / inst_holders | 可用 (單期變動, 無多季時間序列) |
| Reddit r/wallstreetbets, r/stocks | DATA_UNAVAILABLE (依指示不直接 WebFetch; WebSearch 未找到 SPAI 相關討論串) |
| StockTwits | DATA_UNAVAILABLE (依指示未抓取) |
| X / 財經新聞 chatter | 部分可用 (WebSearch, 多為舊文或鏡像頁, 可信度低) |
| 分析師升降評等歷史 | DATA_UNAVAILABLE (yf 僅提供期間彙總計數) |
| 下次財報日期 | DATA_UNAVAILABLE |

## 單位與關鍵數值 (USD)

| 指標 | 數值 | 單位 | 備註 |
|---|---|---|---|
| 現價 (快取, 2026-11-12) | 2.98 | USD | 52 週區間 2.75 – 6.70 |
| 流通股數 | 20.98 | M 股 | yf sharesOutstanding |
| 市值 | 0.063 | B USD (約 62.5 M USD) | 交叉驗算: 20.98M × 2.98 ≈ 62.5M, 與 yf marketCap 相符 |
| 近 6 月 CEO 出售金額 | 4.0 | M USD | 1,000,000 股 × $4.00 = $4.0M, 驗算相符 |
| 10 日平均量 vs 平均量 | 159K vs 346K | 股 | 近期成交量明顯低於 yf 平均量 |

## Analyst consensus

3 buy / 0 hold / 0 sell (strongBuy 0)。yf recommendationKey = strong_buy, recommendationMean = 1.0 (1 為最看多)。

- 目標價 (3 家): 平均 $10.67, 最高 $13.00, 最低 $9.00。相對現價 $2.98, 平均目標隱含上行約 258%。
- 期間彙總 0m / -1m / -2m 三列計數完全相同 (3 buy), 表示 yf 的期間資料未顯示任何升降評等, 也可能是欄位未更新。升降評等歷史: DATA_UNAVAILABLE。
- 其他來源 (WebSearch, 日期不一, 多為 2026 年中以前快照): MarketBeat 平均目標 $10, 區間 $8 – $13; Benzinga 3 家 Buy, 平均目標 $10; TipRanks 另列 Hold 評等 (目標 $7.50 與 $4.50, 兩者不一致, 來源日期不明)。
- 另有 Weiss Ratings 於 2026-07-17 將評等由 sell (e+) 上調至 sell (d-)。此為量化評等機構, 不計入分析師家數。

判讀: 分析師一面倒看多, 但只有 3 家、目標價離散且遠高於現價, 與 TipRanks 的 Hold 來源衝突。consensus 可信度低。

Recent moves: 近 6 個月無可確認的升降評等紀錄 (DATA_UNAVAILABLE)。

財報脈絡 (yf earnings_dates): 最近一季 2026-08-14 揭露 EPS -0.15, 低於預估 -0.14 (未達 7%)。前三季 (2025-11-14, 2026-03-31, 2026-05-15) 亦皆低於預估, 近 4 季連續 EPS 未達預期。

## Retail social

- Reddit: DATA_UNAVAILABLE。WebSearch 未回傳 SPAI 相關 r/wallstreetbets 或 r/stocks 討論串, 無法取樣, 無法給出 tilt。
- StockTwits: DATA_UNAVAILABLE。
- StockTwits / X / 社群: WebSearch 僅見 TradingView 社群板少量個人貼文, 內容零散, 無法代表整體。取樣舉例:
  - 「SPAI Army demonstration for 2026 means potential contracts」 (看多, 寄望軍方示範帶來合約)
  - 「Any good news will send this stock to the moon」 (看多, 寄望利多爆發)
- 量能: 近期成交量 (10 日均量約 159K 股) 低於 yf 平均量 (約 346K 股), 社群聲量整體判定為低 (定性判斷, 無實際提及次數可比對)。
- Tilt: 社群輕微偏多但樣本極少, 不具代表性, 信心低。

Themes (定性):
1. 軍方示範與合約期待 (國防 / 無人機影像 AI 題材)
2. 股價接近 52 週低點, 「低價等利多」心態
3. 連續財報未達預期, 基本面疑慮
4. 技術面: WebSearch 節錄之 2026-07-28 MarketBeat 快照顯示股價 $3.79, 低於 50 日與 200 日均線 (屬價格資料, 非社群觀點)

## Insider activity

6 個月窗口: 2026-05-13 至 2026-11-13。

Net 6mo: $0 公開市場買入, $4.0M 賣出 (僅一筆)。

| 日期 | 人員 | 職位 | 交易 | 股數 | 金額 (USD) | 備註 |
|---|---|---|---|---|---|---|
| 2026-09-09 | ERDBERG DANIYEL | Chief Executive Officer | 出售 (Sale) | 1,000,000 | 4.0M | 持股性質 D (直接); 交易代碼空白, 無法判定是否為 10b5-1 計畫 (DATA_UNAVAILABLE) |
| 2026-05-01 | MACK BRIAN WILLIAM | Officer | 股票獎勵 (Grant) | 300,000 | 0 | 非市場交易, 不計入淨買賣 |

窗口外參考: 2026-04-01 COO MATHEWS JARRET DANIEL 獎勵 20,000 股; 2026-03-06 CEO 贈與 9,000 股; 2025-12-23 CEO 贈與 24,000 股。

CEO 售價 $4.00, 高於現價 $2.98 約 34%; 以現價計, 該筆賣出後股價下跌約 25%。

判讀: 窗口內唯一的實質交易是 CEO 出售, 無高階主管公開市場買入紀錄。獎勵與贈與不計入淨買賣。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 42.8%
- 機構持股 (institutionsPercentHeld): 11.6%, 浮動股比例 20.3%, 機構家數 31
- 前十大機構合計約 9.5% 股份 (依 inst_holders 加總)
- 近期持股變動 (單期, 非時間序列):
  - Vanguard Capital Management LLC: 563,837 股, 較前期 +24.5% (2026-06-30)
  - Themes Management Co LLC: 222,279 股, +100% (2026-09-30)
  - Jane Street Group, LLC: 139,551 股, +100% (2026-06-30)
  - Perkins Capital Management, Inc.: 223,000 股, -3.3% (2026-09-30)
  - Tudor Investment Corp Et Al: 129,459 股, -42.6% (2026-06-30)
- 多季機構持股趨勢: DATA_UNAVAILABLE。2026-09-30 的 13F 申報在 2026-11-13 前可能尚未全數公布, 最新季度資料可能不完整。

判讀: 機構持股比例偏低, 變動方向分歧, 無法得出一致的集中度趨勢。

## Net sentiment score

- 分析師 (偏多, 信心: 低): 3 家全 Buy, 但樣本少, 目標價離散, 來源衝突。
- 散戶社群 (不明確, 信心: 低): 樣本極少, 量能低, 僅見零星看多寄望。
- 內部人 (偏空, 信心: 中): 6 個月內 CEO 出售 $4.0M, 無公開市場買入。
- 量化與價格面 (偏空, 信心: 中): Weiss sell (d-), 股價低於長期均線, 接近 52 週低點, 近期財報連續未達預期。

Composite: 中性偏空 (信心: 低到中)。

Divergence flag: 是。分析師傾向 (3 Buy) 與內部人出售 / 量化評等 / 價格走勢方向相反。此背離值得在後續討論中追蹤, 但本報告不構成交易建議。

## 來源

- yf 快取: /home/user/agent-trading-scans/prices/yf/SPAI.json (refreshed 2026-11-12)
- WebSearch: [TipRanks SPAI analysis](https://www.tipranks.com/stocks/spai/stock-analysis), [MarketBeat SPAI forecast](https://www.marketbeat.com/stocks/NASDAQ/SPAI/forecast), [MarketBeat 2026-07-28 alert](https://www.marketbeat.com/instant-alerts/safe-pro-group-nasdaqspai-shares-down-13-time-to-sell-2026-07-28/), [AAII 2026-10 piece](https://www.aaii.com/investingideas/article/551740-why-safe-pro-group-inc8217s-spai-stock-is-down-567), [TradingView SPAI minds](https://www.tradingview.com/symbols/NASDAQ-SPAI/minds)
- 注意: WebSearch 部分結果為鏡像或自動生成頁面 (日期多為 2026-04 或 2025), 已排除不採用。

SENTIMENT REPORT COMPLETE
