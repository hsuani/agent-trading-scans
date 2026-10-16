# Sentiment — ABBNY as of 2026-10-16

本次 yf 工具呼叫說明: `ratings` 與 `holders` 不是合法子命令, 改用 `rec_summary` / `recommendations` / `major_holders` / `inst_holders`。工具輸出為 cache, Yahoo cookie/crumb 失敗, 屬預期。

## Analyst consensus
資料來源有衝突, 需分開看:
- **yfinance cache (rec_summary / recommendations, 0m / -1m / -2m 三期皆相同):** 0 strong buy / 0 buy / 3 hold / 0 sell / 2 strong sell. 共 5 家. 0% BUY. 三期無變動, 代表近三個月沒有評等異動. 但 cache 日期不明, 樣本只有 5 家, 且 strongSell 佔比 40% 與其他來源不一致.
- **MarketBeat 快照 (WebSearch, 日期無法確認):** 13 家, 1 strong buy / 1 buy / 10 hold / 1 sell. 估算 BUY 比例 = 2/13 ≈ **15%**. 平均 12 個月目標價 **$58.00**, 當時股價約 **$94.70**, 目標價低於現價約 39%.
- **Suredividend (2026-07-16 PDF):** Hold, 價格 $103, fair value $56.

**Analyst consensus % BUY: 0% (yfinance cache, n=5) 至 ~15% (MarketBeat, n=13, 日期不明). 兩者均屬 Hold 主導.** 近期 upgrade/downgrade: cache 無近期異動; 其他來源未找到 2026-10 的評等變動.

## Retail social
- **Reddit (r/wallstreetbets, r/stocks):** DATA_UNAVAILABLE. 沙盒封鎖. WebSearch 未回傳任何 Reddit 討論串.
- **StockTwits:** DATA_UNAVAILABLE. 沙盒封鎖.
- **X / 新聞聲量:** 無法量化 mention 次數, buzz volume 定性無法判斷.
- **Retail tilt:** DATA_UNAVAILABLE. 無法判定 bullish / bearish / mixed.
- **Themes (來自新聞, 非散戶):**
  - 多頭敘事: Q2 2026 創紀錄訂單 (約 $12B), 2026 年營收成長指引為低雙位數至低十幾, 資料中心電力需求 (約占營收 9%), 電氣化業務 (約占營收一半且利潤率最高), 2B 股票回購.
  - 空頭 / 風險敘事: 機器人部門出售予 SoftBank (約 $5.4B, 預計 2026 下半年完成), 失去機器人題材曝險; 利率上升可能抑制專案融資; 估值風險 (目標價低於現價).
  - 併購: Rotork 收購案, 管理層稱第二年 EPS 增厚.

## Insider activity
DATA_UNAVAILABLE. `insider` 回傳空陣列, 無法確認是否為真實零交易或資料缺失. ABBNY 為瑞士母公司 ADR, 內部人交易揭露管道與美股 Form 4 不同, 本來源可能不完整.

## Ownership shifts
- `major_holders` 顯示 institutionsPercentHeld 僅 **0.20%**, institutionsCount 88. 此數字對 ABB 這類大型股明顯偏低, 應視為 ADR 美國 13F 覆蓋範圍的局部值, 不代表全球持股結構, 不建議作為集中度依據.
- `inst_holders` 前 10 大 pctChange 方向:
  - 減持: Northeast Investment Mgmt (-1.1%), Kornitzer Capital (-12.6%), Royal Palms (-26.0%), PNC (-8.6%), Front Row (-5.4%)
  - 加持: O'Brien Greene (+6.4%), Rhumbline (+7.9%), Great Lakes (+0.7%)
  - 持平: Cohen Klingenstein (0%)
- **Institutional flow direction: 小幅淨減持 (前 10 大中 5 減 / 3 增 / 1 平 / 1 未知, 且減持幅度大於加持). 樣本小, 信心低.**

## Net sentiment score
- **Analyst 面: 偏中性偏空 (Hold 主導, 目標價低於現價, cache 有 strongSell). 信心中.**
- **Retail 面: DATA_UNAVAILABLE.**
- **Insider 面: DATA_UNAVAILABLE.**
- **機構面: 小幅減持, 信心低.**
- **Composite: neutral-to-bearish, 信心低** (僅分析師與機構兩面有數據, 且來源衝突).

**Divergence flag: 無法判定.** 缺少散戶資料, 無法比較散戶與分析師傾向.

## 資料品質備註
1. yfinance cache 的評等分布與 MarketBeat 快照差距大 (0% vs ~15% BUY), 且日期不明.
2. 價格來源: MarketBeat $94.70, Suredividend $103, 母公司 SEK 961.40 (2026-10-12). 這些不是同一時點.
3. ABB India 與 ABB Ltd 為不同公司, 搜尋結果中 ABB India 的負面評等不適用於 ABBNY.
4. 2026-10-16 之後的資料皆未使用.

SENTIMENT REPORT COMPLETE

Sources (WebSearch): [MarketBeat ABBNY forecast](https://www.marketbeat.com/stocks/OTCMKTS/ABBNY/forecast/), [Suredividend ABBNY 2026-07-16](https://www.suredividend.com/wp-content/uploads/2026/07/ABBNY-2026-07-16.pdf), [Vontobel ABB investment idea](https://markets.vontobel.com/en-se/inspiration/123986/abb-at-the-centre-of-the-electrification-boom), [Stockopedia ABB 2026 outlook](https://www.stockopedia.com/share-prices/abb-SWX:ABBN/news/abb-gives-confident-outlook-for-2026-launches-2-billion-buyback-updated-019e6a08-0290-7d87-9751-1395496534e4/), [Business Reporter ABB 2026](https://www.business-reporter.co.uk/digital-economy/abb-confident-for-2026-as-customers-plan-ahead-despite-political-uncertainty-14034)
