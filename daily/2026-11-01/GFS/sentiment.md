# Sentiment — GFS as of 2026-11-01

資料截止: 分析師評級為 yf rec_summary 最新快照 (0m); 內部人交易至 2026-09-28; 零售端 Reddit 與 StockTwits 本次無法取得, 改用 WebSearch 片段 (多為 2026-07 至 2026-08 快照)。

注意: 本次 DATE 為 2026-11-01, 但系統日期為 2026-10-31, 所有數據皆為最近可得快照, 並非 11/01 盤中資料。

## Analyst consensus (yf rec_summary, 單位: 家數)

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買方側 (SB+B) | 持有 | 賣方側 (S+SS) |
|---|---|---|---|---|---|---|---|---|---|
| 0m (最新) | 3 | 10 | 9 | 0 | 1 | 23 | 13 (57%) | 9 (39%) | 1 (4%) |
| -1m | 4 | 10 | 8 | 0 | 1 | 23 | 14 | 8 | 1 |
| -2m | 4 | 9 | 8 | 0 | 1 | 22 | 13 | 8 | 1 |
| -3m | 3 | 9 | 9 | 0 | 1 | 22 | 12 | 9 | 1 |

評級分布近三個月基本穩定, 買方側在 -1m 到 0m 減 1 家, 無明顯轉向。yf recommendations 工具未回傳個別升降評等事件, 故「近期調整」以外部來源補充:

- 外部來源 (2026-05, Benzinga 評等歷史): Susquehanna 目標價由 $100 升至 $125; Evercore ISI 由 $58 升至 $85; Needham 由 $55 升至 $80。
- 目標價 (外部快照, 日期不一, 彼此有出入): Walnut 2026-07 平均 $80.24 (區間 $60–$125, 21 家); 2026-08 快照 $68.69; Fintel 2026-08-28 中位數 $76.50。Investing.com 的評級為 12 買 / 9 持有 / 1 賣 (21 家)。
- 目標價資料偏舊且不一致, 應以券商終端或 Yahoo Finance 的 10 月數據為準。

## Retail social

- Reddit: 本次無法取得。r/wallstreetbets 與 r/stocks 的 search.json 回傳 fetch 錯誤 (無法連線), 未能抽樣 threads。搜尋結果中僅見垃圾或轉載頁面, 不予採用。
- StockTwits: API 因網域無法解析 (ENOTFOUND) 失敗, 需於 session 網路設定允許 api.stocktwits.com。外部快照 (2026-08 前後) 顯示 "Bearish Sentiment" 標籤, 樣本約 28 票, 時效性存疑。
- X / 新聞與部落格:
  - TipRanks 部落客觀點: 看空 60% (樣本 5 則), 偏空。
  - 24/7 Wall St. 社群情緒模型: 0/100, 標示 Bearish, 討論熱度 Low。
  - Benzinga: put/call 比率 0.31–0.51 (偏多解讀), 空單比率 13.6% (描述為下降)。市場觀點與分析師共識 (Neutral) 不一致。
- 討論量 (buzz volume): 定性判斷為低於一般水準 (24/7 標示 Low), 但樣本薄弱, 無法量化與基準比較。
- 主要論點 (由片段歸納, 非原文轉錄): 股價自 2026-05 高點 (約 $87 附近的內部人成交價) 回落至 $44–49 區間, 多方關注產能擴張與需求, 空方關注估值拉回與內部人持續賣出。
- 零售傾向: 偏空, 信心低 (樣本少、時效舊、來源互相矛盾)。

## Insider activity

6 個月區間 (2026-05-01 至 2026-10-31), 以 yf insider 逐筆計算:

| 指標 | 數值 |
|---|---|
| 買進 (open-market) | 0 筆 / USD 0.00M |
| 賣出 | 30 筆 / USD 2.92M / 約 43,400 股 |
| 淨額 | 淨賣出 USD 2.92M |

各人賣出金額 (USD M, 6 個月區間內):

| 姓名 | 職稱 | 賣出金額 | 備註 |
|---|---|---|---|
| HOGAN MICHAEL JAMES | Officer | 1.14 | 2026-05 至 2026-07 多筆, 最後一筆 2026-07-22; 另有數筆贈與 (0 價值) |
| AZAR SAMAK L | Officer | 0.44 | 約每週或兩週一次, 每次 335–500 股, 持續至 2026-09-10; 規律性強, 疑似排程性 (未經證實) |
| VICARI SAMUEL | Officer | 0.66 | 2026-05-11, 8,692 股 |
| RAMAN PRADHEEPA | Officer | 0.45 | 2026-08-18 (6,760 股, $0.35M) 與 2026-09-28 (2,145 股, $0.10M) |
| DORCHAK GLENDA MARY | Director | 0.23 | 2026-07-20, 4,000 股 |

- 董事 (Rao, Halawa, Obeid, Languille, Antaki) 於 2026-07-28 有股票獎勵 (grant), 無現金買入。
- 解讀: 6 個月內無公開市場買進, 賣出由多位 Officer 與一位 Director 執行, 偏空訊號。但賣出為獎勵股變現, 且部分為規律性小量賣出, 訊號強度中等偏低。

## Ownership shifts

- insidersPercentHeld: 0.12% (內部人持股極低)。
- institutionsPercentHeld: 100.48%, institutionsCount: 599。機構持股比率超過 100%, 屬資料異常 (疑為重複計算或 float 基準不一), 不可直接用於判讀集中度趨勢。
- 本次僅為單期快照, 無歷史機構持股變化可比。

## Net sentiment score

- 分析師: 偏多 (買方側 57%, 賣方側僅 1 家), 信心中等。
- 內部人: 偏空 (6 個月淨賣出 USD 2.92M, 0 買進), 信心中等偏低。
- 零售: 偏空, 信心低 (Reddit、StockTwits 無法直接取得, 外部片段互相矛盾)。
- 綜合: 中性 (Neutral), 信心低。分析師偏多與內部人及零售偏空並存, 整體無明確方向。

Divergence flag: 是。零售與內部人傾向 (偏空) 與分析師傾向 (偏多) 相反, 此分歧本身具資訊價值, 但因零售樣本薄弱, 解讀時需保守。

資料品質警示:
1. Reddit 與 StockTwits 未取得, 零售面為間接證據。
2. yf 的 cookie/crumb 取得失敗 (ConnectionError), 但回傳資料完整; 機構持股比率 >100% 屬異常。
3. 外部目標價與股價快照時間不一, 且 WebSearch 內某些 July 股價 (約 $47) 與 yf 內部人成交價 (July 約 $57–70) 不一致, 以 yf 成交價為準。

## Sources

- [Benzinga GFS rating history / sentiment](https://www.benzinga.com/quote/GFS/sentiment)
- [Walnut Invest GFS forecast](https://walnutinvest.com/stocks/gfs/forecast)
- [Investing.com GFS consensus](https://uk.investing.com/equities/globalfoundries-consensus-estimates)
- [Fintel GFS](https://fintel.io/s/us/GFS)
- [Stocktwits GFS](https://stocktwits.com/symbol/GFS)
- [TipRanks GFS bloggers](https://www.tipranks.com/stocks/gfs/bloggers)
- [Nasdaq: Susquehanna upgrades GFS](https://www.nasdaq.com/articles/susquehanna-upgrades-globalfoundries-gfs)
- [StreetInsider GFS rating history](https://www.streetinsider.com/rating_history.php?q=GFS)
