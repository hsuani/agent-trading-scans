# Sentiment — SNDK as of 2026-11-25

> 資料注意: 系統時鐘為 2026-11-24, 本報告以 2026-11-25 標示; 內部人與分析師資料取 yf 最新可得值。SNDK 已於 2026-11-20 完成 8:1 股票分割, yf 內部人股數與價格為分割前口徑 (金額不受影響), 目標價亦多為分割前數字。

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf rec_summary | 可用 (cookie/crumb 失敗, 以無 crumb 模式回傳) |
| yf recommendations | 回傳內容與 rec_summary 相同 (月度分佈), 無個別升降評事件, 升降評明細 DATA_UNAVAILABLE |
| yf insider | 可用 (6 個月交易紀錄完整) |
| yf major_holders | 可用, 僅最新快照, 無時間序列 |
| Reddit (r/wallstreetbets, r/stocks) | 失敗: WebFetch 無法連線 reddit.com, 此次無法評估 |
| StockTwits API | 失敗: DNS 解析失敗, 需於 session 網路設定允許 api.stocktwits.com, 未重試 |
| WebSearch (X/新聞/聚合站) | 可用, 但來源日期混雜 (多為 7 月至 11 月), 部分為 AI 摘要 |

## Analyst consensus

| 評等 | 目前 (0m) | 1 個月前 | 2 個月前 | 3 個月前 |
|---|---|---|---|---|
| Strong Buy | 5 (20%) | 4 | 4 | 4 |
| Buy | 17 (68%) | 17 | 17 | 16 |
| Hold | 3 (12%) | 3 | 3 | 3 |
| Sell | 0 (0%) | 0 | 0 | 0 |
| Strong Sell | 0 (0%) | 1 | 1 | 1 |
| 合計 | 25 | 25 | 25 | 24 |

目前 25 家分析師中 22 家買進 (88%), 0 家賣出。近 1 個月的變化: Strong Sell 由 1 降為 0, Strong Buy 由 4 升為 5, 整體偏多且略為改善。

近期評等與目標價 (來源為 WebSearch 聚合站, 未經券商原文核對, 日期標示為來源所示):
- Bernstein (Mark Newman): Buy 維持, 目標價由 1,700 上調至 3,000 (約 11/12)。
- Evercore ISI: Outperform 維持, 目標價 2,500 (11/11)。
- Fox Advisors: 由 Overweight 降為 Equal-Weight (11/2, Benzinga 追蹤器)。唯一可見的降評, 且日期與 11/5 大跌接近。
- Argus (Kelleher): 升為 Buy, 目標價 1,600 (日期不明)。
- Zacks: Hold, 目標價 1,881 (Zacks 為量化評級機構, 非傳統券商, 日期不明)。
- 平均目標價: Benzinga 1,636.83 (更新於 11/5); Barchart 平均 2,245, 共識 Strong Buy。兩者差距大, 反映樣本與日期不同。
- Benzinga 的樣本為 18 家 (17 買, 1 持有), 與 yf 25 家不同, 以 yf 為準。

## Retail social

- **Reddit**: 無法取得 (連線失敗)。r/wallstreetbets 與 r/stocks 的聲量與語氣 DATA_UNAVAILABLE。
- **StockTwits**: API 失敗。聚合摘要 (日期不明) 指 StockTwits 情緒由「看空」轉為「中性」, 討論熱度由「低」升至「高」; 另一則指暴跌期間 24 小時訊息量增約 900%。兩則皆無絕對基準, 聲量僅能定性為「暴跌期間高於平常」。
- **X / 新聞與聚合站**: 
  - 247wallst (7 月) 標題為「Wall Street Loves SanDisk, but Retail Is Strangely Silent」, 顯示散戶參與度低於分析師熱度。
  - AltIndex 綜合評分 65/100 偏多 (無時間戳)。
  - LunarCrush 兩次快照分別為 78% 與 92% 正面 (無日期, 且彼此不一致)。
  - 結論: 聚合站數值互相矛盾且無法對齊到 11/25, 不納入評分。
- **Retail tilt**: 無可靠讀數, 僅能說「看多與看空敘事並存, 方向無法判定」。

主要敘事 (由 WebSearch 摘要歸納):

多方:
1. AI 儲存需求帶動 NAND 結構性成長, Evercore 與 Bernstein 的論點均圍繞此點。
2. 以峰值獲利計算的估值偏低, 下跌屬情緒性拋售, 基本面未惡化 (Zacks 觀點)。
3. 分析師目標價仍在 1,600 至 3,000 之間, 遠高於 11 月的成交價 (分割前口徑)。

空方:
1. 記憶體景氣循環未改變, 「NAND is still NAND」, 價格與需求於下半年轉弱 (Edgewater 警告)。
2. 中國 CXMT 於上海上市, 增加供給與競爭憂慮。
3. 美國資料中心監管擔憂, 11/5 單日跌約 22% (Simply Wall St 摘要歸因)。
4. 內部人於 6 至 11 月持續賣出 (見下節)。
5. 選擇權偏空: 11 月到期 put/call 約 2.08 (來源與日期不明, 低可信度)。

熱門標題 (主題參考): 「Sandisk Drops 5%: AI Breakout or Speculative Bubble?」、「Retail Traders Debate Whether $1,000 Will Hold」。

## Insider activity

Net 6mo (2026-05-25 至 2026-11-25): **買進 $0** (無公開市場買進紀錄); **賣出約 $126.6M** (USD M)。授予股 (grant) 與贈與 (gift) 未計入。

| 內部人 | 職務 | 賣出股數 (分割前) | 金額 (USD M) | 主要交易日 |
|---|---|---|---|---|
| GOECKELER DAVID V | CEO | 67,679 | 104.97 | 9/14 (33,838 股), 9/17 (33,841 股) |
| ILKBAHAR ALPER | CTO | 7,112 | 11.40 | 6/1, 9/3 (另 8/20 有 276 股, 金額欄空白, 性質不明) |
| SHEK BERNARD | Officer | 5,308 | 8.68 | 6/3, 7/1, 8/3, 9/1, 9/8, 11/2 (共 6 筆) |
| VISOSO LOMELIN LUIS FELIPE | CFO | 1,000 | 1.57 | 9/15 |
| **合計** | | **81,099** | **126.62** | |

單位換算驗算: CEO 33,838 股 × 約 1,532 美元 (9/14 價格區間中位數) ≈ 51.8M, 與回報值 51.70M 相符。

重點:
- **注意: GOECKELER DAVID V (CEO)**, 兩筆合計約 $105.0M, 佔 6 個月賣出總額約 83%。成交價約 1,523 至 1,587 (分割前), 較 7 月個別成交高點 (約 2,088, 見 SHEK 7/1 交易) 低約 24%。交易是否屬 10b5-1 計畫無法由 yf 判定。
- CFO 與 CTO 於 9 月亦有賣出。SHEK BERNARD 於 11/2 以約 1,158 (分割前) 賣出, 為最近一筆, 時點在 11 月大跌期間。
- 大型授予股 (CEO 2025-09 與 2026-09) 與董事授予股 (2026-11-17, 每人 326 股) 均屬薪酬性質, 不計入買進。
- 6 個月窗口外: POKORNY MICHAEL (5/12, 約 $3.49M) 與 SAYINER NECIP (5/8, 約 $0.87M) 亦為賣出, 未計入上述總額。

## Ownership shifts

- yf major_holders (快照): 內部人持股 1.10%, 機構持股 76.86%, 流通股機構持股 77.71%, 機構數 2,425。
- 機構持股的時間趨勢: DATA_UNAVAILABLE (工具僅提供快照)。
- 10% 以上大股東 Western Digital Corp 持股 29.86M 股, 申報日 2025-02-13。此數字可能已過時, 不可視為現況。

## Net sentiment score

- 分析師: **偏多** (信心: 高。88% 買進、0% 賣出、近期多數重申或上調目標)。
- 內部人: **偏空** (信心: 中高。6 個月賣出約 $126.6M、零買進, 但賣出動機未知, 可能含計畫性或薪酬性賣出)。
- 散戶: **無法判定** (信心: 低。Reddit 與 StockTwits 無資料, 聚合站矛盾)。

**Composite: 中性偏多 (信心: 低至中)**。分析師面明確偏多, 內部人面偏空, 散戶面缺資料, 綜合僅能給出中性偏多。

**Divergence flag: 是**。分析師 (88% 買進) 與內部人 (淨賣出、零買進) 方向相反。散戶與分析師的背離無法判定, 因為散戶讀數不足。

注意: 本節僅為情緒讀數, 不構成交易建議。

## 來源

- [yf rec_summary / insider / major_holders (pipeline/tools/yf)](pipeline/tools/yf)
- [Nasdaq: Why Sandisk stock crashed today](https://www.nasdaq.com/articles/why-sandisk-stock-crashed-today)
- [Nasdaq: Why Sandisk stock keeps crashing](https://www.nasdaq.com/articles/why-sandisk-stock-keeps-crashing)
- [StockTwits: SNDK plunges over 30% in 3 days, retail debates $1,000](https://stocktwits.com/news-articles/markets/equity/sndk-stock-sandisk-drop-30-percent-loss-3-days-1000-retail-debate/cZZCrYiRJbB?.tsrc=rss)
- [247wallst: Wall Street Loves SanDisk, but Retail Is Strangely Silent](https://247wallst.com/investing/2026/07/22/wall-street-loves-sandisk-but-retail-is-strangely-silent/)
- [247wallst: SanDisk Cratered Again But One Analyst Believes 200% Returns Are Coming](https://247wallst.com/investing/2026/07/29/sandisk-cratered-again-but-one-analyst-believes-200-returns-are-coming/)
- [AltIndex SNDK sentiment](https://altindex.com/ticker/sndk/sentiment)
- [LunarCrush SNDK social sentiment](https://lunarcrush.com/de/stock/sandisk-corporation-sndk)
- [Benzinga SNDK price targets](https://www.benzinga.com/quote/sndk/price-targets)
- [Benzinga SNDK analyst ratings](https://www.benzinga.com/quote/SNDK/analyst-ratings)
- [Barchart: SanDisk new buy rating](https://www.barchart.com/story/news/3776513/what-to-know-as-sandisk-stock-scores-a-new-buy-rating)
- [Simply Wall St: SanDisk narrative update](https://simplywall.st/narratives/w6k7ht81-update-for-sandisk?blueprint=4732317)
- [Finimize: Sandisk AI storage boom meets 42% selloff](https://finimize.com/content/sndk-asset-snapshot)
- [TipRanks: Sandisk shares tumble amid bearish sentiment](https://www.tipranks.com/news/catalyst/sandisk-corp-shares-tumble-amid-bearish-sentiment)
- [TIKR: Sandisk lost 51% in a month, Bernstein sees 259% upside](https://www.tikr.com/blog/sandisk-lost-51-in-a-month-bernstein-sees-259-upside-from-here)
- [nai500: SanDisk 8-for-1 split arrives with stock down 60% from July highs](https://nai500.com/blog/2026/11/sandisks-8-for-1-split-arrives-with-stock-down-60-from-july-highs/)
- [SEC: Sandisk Form 8-K (2026-10-29)](https://www.sec.gov/Archives/edgar/data/0002023554/000162828026068243/sndk-20261029.htm)

SENTIMENT REPORT COMPLETE
