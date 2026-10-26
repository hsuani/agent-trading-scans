# Sentiment — ABBNY as of 2026-10-26

**資料完整度: 低.** Reddit 與 StockTwits 皆無法取得 (見下方), yf 的 recommendations 與 rec_summary 回傳相同數值 (非歷史評級變動), insider 回傳空陣列, 網路搜尋來源之間數字互相矛盾. 以下結論信心偏低.

## Analyst consensus

**yf rec_summary (當期, 0m): 0 buy / 5 hold / 0 sell, strongSell 1 (共 6 家).**

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (當期) | 0 | 0 | 5 | 0 | 1 |
| -1m | 0 | 0 | 3 | 0 | 2 |
| -2m | 0 | 0 | 3 | 0 | 2 |
| -3m | 0 | 0 | 3 | 0 | 2 |

趨勢: 過去一個月 strongSell 由 2 降為 1, hold 由 3 升為 5, 整體偏空成分減少. 但 yf 的 recommendations 工具未給出逐筆評級變動, 無法核對是哪幾家調整.

**網路來源 (家數與分布不一致, 僅供參考):**
- Walnut Invest 頁面: 0 buy / 3 hold / 2 sell (5 家), 平均目標價約 USD 93.32, 約高於其頁面價格 2.5%.
- MarketBeat 頁面: 1 strong buy / 1 buy / 10 hold / 1 sell (13 家), 共識 Hold, 平均目標價 USD 58.00 (所有分析師目標價皆列 58.00, 疑為過期或異常值, 與當時股價約 USD 94.70 相比隱含約 39% 下檔, 不宜直接採信).

**近期評級動作 (網路搜尋, 多數無明確日期, 需核實):**
- Pareto 與 DNB Carnegie 疑於 2026-07-16 升評為 Buy (Pareto 目標 CHF 96.40). 另一頁面亦提及 Pareto 由 Buy 降為 Hold, 兩者矛盾, 日期不明.
- Handelsbanken 降評為 Underperform, 目標 USD 67 (無日期).
- JPMorgan Neutral, 目標 CHF 80 (由 70 上調); Citi Neutral, 目標 CHF 85 (由 78 上調); Barclays Equal Weight, 目標 CHF 76 (重新覆蓋). 日期皆未標示.
- 搜尋未找到 2026-10 月內的明確評級變動.

**目標價單位:** 瑞士上市 ABBN 目標價為 CHF, MarketBeat/Walnut 以 USD 呈現. 兩者不可直接混比.

## Retail social

- **Reddit (r/wallstreetbets, r/stocks):** 兩個 JSON 端點皆被 WebFetch 拒絕 (無法連線). 無法取得討論串, 無法估計 tilt. 無引用.
- **StockTwits:** `api.stocktwits.com` DNS 解析失敗 (ENOTFOUND). 無法取得訊息量或 Bullish/Bearish 標籤.
- **X / 新聞論壇:** 一般搜尋未找到 ABBNY 相關散戶討論串, 無法判定近期散戶熱度. 目前只能回報「buzz volume 未能量化」, 不能說是低或高.
- **Themes (取自財經敘事與分析師文字, 非散戶貼文):**
  - 全球保護主義與成本上升侵蝕利潤率 (Simply Wall St narrative 標題: "global protectionism and rising cost burdens will erode margins").
  - 估值疑慮是部分降評理由 (Simply Wall St 2026-05 摘要).
  - 機器人與離散自動化業務 (Robotics & Discrete Automation) 為市場關注點.
  - 第三方資料指 FY2026 EPS 預估約 USD 3.73, 年增約 43%, 但來源僅單一頁面, 未驗證.
- **Retail tilt:** 無法判定 (bullish / bearish / mixed 皆無足夠樣本).

## Insider activity

- **yf insider: 空陣列.** 不能據此推定無交易, 可能是 Yahoo 資料抓取失敗 (cookie/crumb 取得失敗).
- **網路來源, 互相矛盾:**
  - Simply Wall St: 董事長 Peter Voser 於 2026-02-12 賣出 30,000 股, 最高價 EUR 76.98 (毛額約 EUR 2.3M = 30,000 × 76.98). 另稱近 3 個月內部人僅賣出, 無買入.
  - Sami Atiyeh (Robotics & Discrete Automation 總裁) 有賣出股票的報導, 日期與股數未確認.
  - InsiderScreener: 近 90 天淨買入約 CHF 2M+ (10 位內部人, 皆為董事會成員, 無執行長/CFO 交易), 其中 2026-05 約 CHF 1.4M 買入. 但其列出之成交價 (例: 466.22, 197.41) 明顯偏離其他來源的股價區間, 數據品質存疑.
- **Net 6mo: 無法可靠計算.** 已知賣出一筆約 EUR 2.3M (Voser, 2026-02). 若 InsiderScreener 數字屬實, 5 月有董事會淨買入約 CHF 1.4M, 但未經核實.
- **CEO/CFO 交易:** 未在可靠來源中確認.

## Ownership shifts

- yf major_holders: `institutionsPercentHeld` = 0.2% (0.00202), `institutionsCount` = 88, `insidersPercentHeld` = 0.0.
- 0.2% 明顯不合理 (ABB 為大型股), 推測是 OTC ADR 持股登記的侷限, 未反映瑞士本地法人持股. 此數字不具參考價值.
- 持股變動趨勢: 無可用資料.

## Net sentiment score

- **Analyst tilt:** 中性 (neutral). yf 當期 6 家中 5 hold, 1 strongSell, 近一月偏空減弱. MarketBeat 13 家略偏多 (2 buy vs 1 sell), Walnut 5 家略偏空. 各來源結論不一致.
- **Retail tilt:** 無資料.
- **Insider tilt:** 不確定. 已知一筆大額賣出 (Voser) 與一組董事會買入 (數據存疑).
- **Composite: neutral (信心: 低).** 主要原因是散戶端完全缺席, 分析師與內部人資料又互相矛盾.
- **Divergence flag: 無法判定.** 缺乏散戶 tilt, 不能判斷是否與分析師方向相反.

## Data gaps and next steps

1. Reddit 與 StockTwits 需替代來源 (例如付費社群 API 或手動抽樣) 才能補足散戶面.
2. yf 的 cookie/crumb 失敗需修復, 以取得真正的 recommendations 歷史與 insider 交易.
3. 建議核實 ABB 官方 investor relations 或 SIX 揭露的內部人交易, 並確認 2026-10-20 財報 (Digrin 所列日期) 是否已公布, 以及其市場反應. 本次未取得財報內容, 不應把其影響納入判斷.
4. 分析師目標價與家數需以單一可靠來源 (如 TipRanks 或 Refinitiv) 重新核對.

## Sources (網路搜尋)

- [Walnut Invest, ABB Ltd (ABBNY) Forecast](https://walnutinvest.com/stocks/abbny/forecast)
- [MarketBeat, ABBNY Forecast](https://www.marketbeat.com/stocks/OTCMKTS/ABBNY/forecast/)
- [Simply Wall St, ABB 全球保護主義敘事](https://www.simplywall.st/narratives/fqlz0u7x-global-protectionism-and-rising-cost-burdens-will-erode-margins)
- [Simply Wall St, ABBN 營運與市場觀察](https://www.simplywall.st/narratives/ndf3nx4v-abbn-operational-strength-and-market-caution-will-shape-near-term-performance)
- [StockAnalysis, ABB Ltd (ABBNY)](https://stockanalysis.com/quote/otc/ABBNY/)
- [TipRanks/The Fly, Handelsbanken 降評 ABB](https://www.tipranks.com/news/the-fly/abb-downgraded-to-underperform-from-market-perform-at-handelsbanken)
- [TipRanks/The Fly, Barclays 目標價](https://www.tipranks.com/news/the-fly/abb-price-target-lowered-to-chf-36-from-chf-38-at-barclays-thefly)
- [Simply Wall St, ABB 股權與內部人交易](https://simplywall.st/stocks/it/capital-goods/bit-1abb/abb-shares/ownership)
- [Simply Wall St, Sami Atiyeh 賣出股票報導](https://simplywall.st/stocks/ch/capital-goods/vtx-abbn/abb-shares/news/president-of-robotics-discrete-automation-business-sami-atiy-1)
- [InsiderScreener, Abb Ltd](https://www.insiderscreener.com/en/company/abb-ltd)
- [Digrin, ABB Ltd (ABBN.SW) 財報](https://www.digrin.com/stocks/detail/ABBN.SW/earnings)

SENTIMENT REPORT COMPLETE
