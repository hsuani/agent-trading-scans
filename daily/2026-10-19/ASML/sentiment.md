# Sentiment — ASML as of 2026-10-19

資料時點: yfinance 快取 prices/yf/ASML.json 於 2026-10-18 10:53 UTC 更新（live feed 因 Yahoo cookie/crumb 連線失敗而未取得，屬預期降級）。2026-10-19 之後的資料一律視為未知。工具子命令為 rec_summary / recommendations（yf.py 無 ratings 子命令）。

## Analyst consensus
- 最新分布（0m，共 41 家）: strongBuy 7 / buy 31 / hold 2 / sell 1 / strongSell 0。
- **%BUY = 92.7%**（38/41，含 strongBuy）；hold 4.9%，sell 2.4%。
- 趨勢（%BUY）: -3m 90.9%（40/44）→ -2m 88.4%（38/43）→ -1m 90.5%（38/42）→ 0m 92.7%（38/41）。買進比例小幅回升，hold 由 -2m 的 4 家降至 2 家，sell 持平於 1 家。
- 目標價（yf info，17 家給目標價）: 均值 2155.32 / 中位數 2309.31 / 最高 2889.86 / 最低 869.75 USD。以現價 1641.52 USD 計，均值隱含 +31.3%，中位數隱含 +40.7%。recommendationMean 1.37（1 = 強力買進）。
- 近期變動: 快取中的 rec_summary 為彙總數字，無個別券商升降評等明細，無法逐家定日期。WebSearch 提到 New Street Research 由 Buy 降為 Neutral，但日期不明，且在結構化資料中未顯示為 hold 淨增加，故無法確認其時點。
- 外部來源目標價不一致: Benzinga 共識約 1710 USD（[Benzinga](https://kr.benzinga.com/quote/ASML/analyst-ratings)），與 yf 均值 2155 差距大，原因可能是樣本與計價基準不同，未能調和。以 yf 為主。
- 最近一次財報: 2026-10-14，EPS 11.82 對 11.76 估計外的 10.76 估計，超出 +9.86%（yf earnings_dates）。WebSearch 對營收是否低於共識說法互相矛盾（[KuCoin 快訊](https://www.kucoin.com/news/flash/asml-q3-2026-revenue-surpasses-11-6-billion-amid-ai-demand-surge) 稱 Q3 營收約 €11.66B、年增約 55%；另一來源稱小幅未達共識），且股價反應說法不一致。以 yf EPS 超預期為準，營收細節需對照 ASML 官方公告。

## Retail social
- **Reddit**: WebSearch 查 r/wallstreetbets 與一般 Reddit 討論，無可用的 ASML 串文結果，無法取樣或定調。直接抓取 Reddit 主機依規則被阻擋，未嘗試。
- **StockTwits / X**: 無法直接取得 StockTwits 串流。聚合站 AltIndex 給出 ASML 情緒分數 76/100（偏多），並表示近期較 30 日均值轉弱（[AltIndex](https://altindex.com/ticker/asml/sentiment)）。該分數為模型推算、日期不明，只能作低信心參考。另有 2026-02-24 的選擇權與 X 情緒快照（約 70% 偏多）（[historicaloptiondata](https://historicaloptiondata.com/?p=32794)），已過時，不採信。
- **聲量**: 無法量化，資料不足（no measurable buzz data）。
- **主題（從分析文章與聚合來源歸納，非散戶原文）**:
  - 多方: AI 基礎建設需求、High-NA EUV 量產出貨（Intel、TSMC、Samsung）、記憶體（DRAM）資本支出。Bernstein 認為未來 12 個月有超過 30% 上漲空間（[TipRanks](https://www.tipranks.com/stocks/asml)）。
  - 空方: 中國出口管制收緊、半導體關稅與地緣政治、估值偏高（New Street 降評理由之一）、半導體資本支出週期終將反轉（[Walnut Investment](https://walnutinvest.com/stocks/asml/is-it-a-buy-or-sell)）。
- 散戶原文引述: 無可用樣本，不引述。

## Insider activity
- 6 個月內部人交易: live feed 與快取皆為空陣列 []。
- 淨額: **無法判定**（無資料，既非確認淨買亦非淨賣）。
- 解讀限制: ASML 為荷蘭外國私人發行人（foreign private issuer），以 20-F 申報而非美國 Form 4，Yahoo 內部人交易資料通常不完整。insidersPercentHeld 僅 0.008%，此數字不能代表內部人無交易。
- 指定人員（CEO/CFO）買賣: 無資料。

## Institutional / ownership
- 機構持股 20.34%（institutionsCount 2973）；內部人持股 0.008%。
- 前十大機構（2026-06-30 13F，目前最新可得季度）: 10 家中 8 家增持、1 家微減（Capital World Investors，-0.18%）、1 家持平（State Farm，0.0%）。前十大合計持有約 7.95%。
- 主要增持者: FMR（+74%，持股 1.41%）、Capital International（+38%）、Van Eck（+32%）、T. Rowe（+26%）、Invesco（+5.7%）。
- 方向: 機構淨增持（net accumulation），但 Q2 數據屬季度落後。Q3 13F 最晚約 2026-11-14 才會公布，於 2026-10-19 尚不可得。

## Net sentiment score
- **Composite: bullish（信心: 中低）**
  - 分析師（權重最高，資料完整）: 強烈偏多，%BUY 92.7%，目標價隱含 +31%。
  - 散戶（資料薄弱）: 聚合來源偏多（76/100），但無原文佐證、日期不明。
  - 內部人: 無資料，不計入。
  - 機構: 偏多（Q2 淨增持）。
- **Divergence flag: no**。散戶與分析師傾向同向（皆偏多）。但需注意: 散戶端證據薄弱，且 New Street 的估值質疑與中國出口管制風險代表少數反向意見，目標價分散度大（869 至 2889 USD）。

## 資料缺口與限制
1. 無 Reddit / StockTwits 直接樣本，散戶判斷主要依賴聚合來源。
2. 內部人交易不可用（FPI 結構性問題），無法判定內部人流向。
3. 分析師個別升降評等無結構化資料。
4. 財報營收與股價反應來源互相矛盾。
5. 機構持股為 2026-06-30 數據，Q3 13F 尚未公布。

來源（WebSearch 參考）:
- [Benzinga 分析師評等](https://kr.benzinga.com/quote/ASML/analyst-ratings)
- [TipRanks ASML](https://www.tipranks.com/stocks/asml)
- [Walnut Investment 多空論據](https://walnutinvest.com/stocks/asml/is-it-a-buy-or-sell)
- [AltIndex ASML 情緒](https://altindex.com/ticker/asml/sentiment)
- [KuCoin Q3 2026 快訊](https://www.kucoin.com/news/flash/asml-q3-2026-revenue-surpasses-11-6-billion-amid-ai-demand-surge)
- [historicaloptiondata ASML 選擇權情緒](https://historicaloptiondata.com/?p=32794)

SENTIMENT REPORT COMPLETE
