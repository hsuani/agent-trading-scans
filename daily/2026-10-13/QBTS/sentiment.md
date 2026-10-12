# Sentiment — QBTS as of 2026-10-13

資料截止: yf 數據為工具回傳的最新值，內部人交易最新一筆為 2026-09-08。WebSearch 未找到 2026-10 月的評等變動或社群內容。2026-10-13 之後的資料視為未知。Reddit 與 StockTwits 無法取得，散戶情緒部分為 DATA_UNAVAILABLE。

## Analyst consensus
17 位分析師: 1 strongBuy / 14 buy / 2 hold / 0 sell (當月 yf rec_summary)，買進比例約 88%，無 sell。
近四個月趨勢: 3 個月前為 1/14/1/0 (共 16 家)，約 2 個月前出現一家 buy 轉 hold 或新增 hold，之後維持 1/14/2。方向仍偏多，但 hold 數量小幅增加。
目標價 (WebSearch 彙整，可信度中低):
- Fintel (2026-08-28): 平均 12 個月目標 $35.94，區間 $22.22–$45.15，中位數 $36.72。
- MarketBeat 17 家評等平均目標 $36.47 (日期不明)。
- Feb 2026 (Q4 財報後): Evercore 由 $44 降至 $42 (Outperform)；Mizuho 由 $46 降至 $40 (Outperform)。
- May 2026 (Q1 財報後): Canaccord 由 $43 降至 $41 (Buy)；Mizuho 由 $31 降至 $29 (Outperform)。注意 Mizuho 的兩筆來源基期不一致，可能有誤，未能完全核對。
近期動向: 無 2026-10 的升降評等資料。整體是目標價逐步下修、評等維持買進。

## Retail social
- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 search.json 請求被拒 (WebFetch 無法存取 www.reddit.com)。以 WebSearch 搜尋 Reddit 討論亦無結果。
- StockTwits / X: StockTwits API 無法解析 (ENOTFOUND)，無 bullish/bearish 標記統計。X 端未找到可用的近期貼文摘要。
- Themes (來自新聞而非社群，日期多為 2026 年上半年): 現金約 $10 億的資產負債表支撐研發；Q1 2026 營收 $2.86M，年減約 81%，但每股虧損小幅優於預期；股價年初至今約下跌三分之一；Ken Griffin/Citadel 近期加碼持股。
- Retail buzz volume: DATA_UNAVAILABLE。無法與平常水準比較。
- Retail tilt: DATA_UNAVAILABLE。

## Insider activity
過去 6 個月 (2026-04-13 至 2026-10-13):
- 公開市場買進: $0 (0 筆)。
- 公開市場賣出: 約 $36.88M，共 12 筆。
- 另有 2 筆選擇權行使 (cash cost 約 $0.91M)，行使後隨即賣出，不計入上述淨賣出。
- 獎勵股發放 (無現金交易): 2026-06-04 六位董事各 9,357 股；2026-04-30 CEO Baratz 753,941 股。

主要人員:
- CEO Alan Baratz: 2026-06-08 行使 687,627 股選擇權 (行權價 $0.85–0.91)，同日以 $26.13 賣出，金額約 $17.97M。
- CFO John Markovich: 2026-05-22 以 $27.70 賣出約 $9.11M；2026-06-15 以 $24–26 賣出約 $6.25M；2026-06-09 賣出約 $1.34M；2026-06-02 以 $31 賣出約 $0.09M。合計約 $16.8M。
- 董事 Rohit Ghai (2026-06-15 賣出約 $0.36M)、John DiLullo (2026-09-08 以 $18 賣出約 $20K；2026-06-05 賣出約 $0.19M)。
- GC Diane Nguyen (2026-05-21 以 $25 賣出 $1.0M)。
- Officer Sophie Ames (2026-07-20 賣出約 $52K；2026-05-20 賣出約 $0.44M；2026-04-20 賣出約 $66K)。

12 個月長期趨勢: 2025-10 至 2026-09 期間幾乎全為賣出。唯一的公開市場買進為董事 Steven West 2025-11-18 的 82 股 ($1.8K)，金額極小。2025-10 股價約 $43–44 時 CEO/CFO/GC 也有賣出，屬高價區的獲利了結。
解讀: 大部分賣出與選擇權行使綁定，且多發生在股價 $17–31 區間，無法確認是否為 10b5-1 計畫，需以 SEC Form 4 核對。

## Ownership shifts
- 內部人持股 2.2%；機構持股 54.6%；機構數 700 家 (yf major_holders)。
- 歷史大股東 PSPIB 於 2024-12 至 2025-01 大量減持 (單筆約 1,840 萬股與 4,000 萬股相關紀錄)，其後的持股變化無法從本次資料判斷。
- 機構持股的時間序列 yf 未提供，趨勢: DATA_UNAVAILABLE。

## Net sentiment score
Composite: 中性 (信心: 低)。
- 分析師面: 偏多 (88% 買進，目標價逐步下修但仍高於當前可見的股價區間)。
- 內部人面: 偏空 (6 個月約 $36.9M 賣出，0 筆公開買進)。
- 散戶面: 無資料，無法納入。
- 整體以中性處理，信心低，因為散戶資料缺失，且 analyst 與 insider 的訊號方向相反。

Divergence flag: 無法判定 (散戶資料缺失)。另有 analyst-vs-insider 分歧: 分析師偏多、內部人持續賣出，此訊號需留意。

## Metrics

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師評等 (strongBuy/buy/hold/sell) | 1 / 14 / 2 / 0 | yf rec_summary，當月 |
| 買進比例 | 約 88% (15/17) | 由上表計算 |
| 平均 12 個月目標價 | $35.94 (區間 $22.22–$45.15) | Fintel 2026-08-28，可信度中低 |
| 近期目標價下修 | Evercore $44→$42、Mizuho $46→$40、Canaccord $43→$41、Mizuho $31→$29 | WebSearch，Mizuho 兩筆來源基期待核對 |
| 6 個月內部人公開買進 | $0 (0 筆) | yf insider |
| 6 個月內部人公開賣出 | 約 $36.88M (12 筆) | yf insider，不含行權與獎勵股 |
| 6 個月最大賣家 | CEO Baratz 約 $17.97M；CFO Markovich 約 $16.8M | yf insider |
| 內部人持股比例 | 2.2% | yf major_holders |
| 機構持股比例 | 54.6% (700 家) | yf major_holders |
| Reddit 提及量 / 傾向 | DATA_UNAVAILABLE | 403/拒絕存取 |
| StockTwits 多空標記 | DATA_UNAVAILABLE | ENOTFOUND |
| X / 新聞情緒 | 無可用近期資料 | WebSearch 無 2026-10 結果 |
| 綜合情緒 | 中性 (信心低) | 分析師偏多、內部人偏空、散戶無資料 |
| 分歧旗標 | 無法判定 | 散戶資料缺失；analyst 與 insider 方向相反 |

SENTIMENT REPORT COMPLETE
