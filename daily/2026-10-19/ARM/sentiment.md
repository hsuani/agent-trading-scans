# Sentiment — ARM as of 2026-10-19

資料基準: 分析師與內部人資料來自 `prices/yf/ARM.json` 快取 (refreshed 2026-10-18); 日線最後一筆為 2026-10-16 收盤 227.8。2026-10-19 之後資料視為未知。社群資料為 WebSearch 結果, Reddit 與 StockTwits 無法直接取得。

## Analyst consensus
43 家 (rec_summary 0m): Strong Buy 8 / Buy 21 / Hold 12 / Sell 1 / Strong Sell 1。
**%BUY = 67.4%** (29/43, Strong Buy 併入 Buy); Hold 27.9%; Sell 4.7%。

近四期趨勢 (%BUY): -3m 67.5% (27/40), -2m 64.3% (27/42), -1m 67.4% (29/43), 0m 67.4%。Hold 數 11→13→12→12。共識結構持平, 無明顯轉向。

目標價 (yf info): 平均 $290.7、最高 $500、最低 $125; 相對 227.8 收盤, 平均目標價有約 +27.6% 空間。yf info 的分析師家數為 40, 與 rec_summary 的 43 略有差異。

近期評等動向 (WebSearch 轉述, 皆為 7 月, 未找到 10 月新評等):
- HSBC 降至 Hold (2026-07 中), 理由為估值與代工產能瓶頸。報導對目標價描述不一致 (一篇稱調升至 $315)。
- UBS 維持 Buy, 目標價 $360 → $320 (7/30 前後)。
- Rosenblatt 維持 Buy, 目標價 $270 → $250 (7/31)。
- TD Cowen 維持 Buy, 認為授權收入與 data center / AI royalty 成長強勁。
- Wealth Awesome (10/9 頁面) 引述 43 家、Buy 為主、12 Hold、2 Sell, 與 yf 數字一致。

價格脈絡 (日線快取):
- 10/2 高點 307.49 → 10/16 收 227.8, 回檔約 -25.9%。
- 10/8 收 275.29 (-6.5%), 報導歸因於 OpenAI 營收報導引發半導體賣壓, 以及 Qualcomm 訴訟。
- 10/13 Delaware 陪審團裁定 Arm 違反與 Qualcomm 的授權協議, 名目賠償僅 $2; 五年權利金停付的裁決仍待 Judge Noreika 決定。當日報導稱股價約 -1%, 日線快取顯示持平 (255.24 → 255.39)。

## Retail social
- **Reddit (r/wallstreetbets, r/stocks)**: 無法取得。WebSearch 不接受 reddit.com 網域, 一般搜尋也未找到 2026 年的 ARM 討論串。無樣本、無傾向判斷。
- **StockTwits / X**: 無法取得。StockTwits 搜尋只回傳無日期的模板頁; X 相關搜尋最新結果停在 2026 年 3 月, 無本週資料。
- **聲量**: 無法量化。MarketBeat 頁面顯示 "this week" 追蹤文章數 29–91, 但頁面日期不一, 不採用。
- **傾向**: 無法判定 (資料不足, 信心低)。
- **主要議題 (取自新聞, 非散戶樣本)**:
  1. Qualcomm 訴訟與五年權利金風險 (10 月判決後仍未定)。
  2. OpenAI 營收與 AI 族群連動, 股票 beta 約 3.77, 波動放大。
  3. 估值爭議: 年中報導指 forward P/E 約 288 倍 (資料已過時)。
  4. AI data center CPU 與 royalty 成長的多方敘事 (3 月報導)。

## Insider activity
窗口: 2026-04-19 至 2026-10-19。
**Open-market 買入: 0 筆 / $0。Open-market 賣出: 16 筆, 約 $62.4M, 6 位內部人。淨額: 約 -$62.4M。**

依人員:
- COLLINS SPENCER (Officer): 2 筆, 約 $19.8M (5/11 @207–214, 5/19 @215)
- CHILD JASON E (CFO): 4 筆, 約 $16.8M (4/22 @180、5/20 @226.5、8/27 @255.3、9/21 @300)
- ABBEY WILLIAM (Officer): 6 筆, 約 $12.0M (5/15 至 6/1, 價格區間 $199–416)
- GRISENTHWAITE RICHARD ROY (Officer): 1 筆, $5.09M (5/18 @209)
- BARTELS LAURA KATHLEEN (Officer): 1 筆, $4.44M (6/2 @392.7)
- EATON CHARLOTTE CLAIRE (Officer): 2 筆, 約 $4.2M (5/21)

CEO HAAS RENE A:
- 窗口內無公開市場賣出。8/31 為 64 股 award (非市場交易)。
- 窗口外的前次賣出為 4/14 ($1.50M) 與 3/26 ($5.13M)。

其他:
- 5/15 多筆 Stock Award (CEO 265,643 股等) 為 $0 授予, 非市場買入。
- 5/15 有多筆無金額申報 (多為董事與高管股權歸屬), 需進一步確認性質。
- 董事 SINE JEFFREY A. 8/7 贈與 9,572 股 (價值 0)。

解讀: 賣出集中在 5 月 (股價約 200–290) 與 6 月 (約 384–416)。CFO 8 月與 9 月的 10,400 股賣出間隔約 25 天, 節奏可能屬於預定交易計畫, 但 yf 資料未確認 10b5-1 標記。內部人持股僅約 0.07%, 賣出對流通股比例的影響有限。

## Ownership shifts
- 機構持股 96.25% (1,311 家), 持股高度集中於機構。
- 前十大機構 (13F, 報告日 2026-06-30): 增持 7 家、減持 3 家。
  - 增持: Invesco +118% (12.8M 股, 1.2%)、Arrowstreet +333% (4.1M)、FMR +66% (4.1M)、Goldman Sachs +79% (2.9M)、Capital International +76%。
  - 減持: Morgan Stanley -52%、Capital Research Global -43%、DZ Bank -31%。
- 方向: 第二季機構淨增持, 偏多。資料為 6/30 報告, 尚未反映 Q3 13F。
- 空方持股 (short % float): 約 11.1%。

## Net sentiment score
**Composite: 中性 (信心: 低至中)**

| 面向 | 傾向 | 權重與說明 |
|---|---|---|
| 分析師 | 偏多 | 67% Buy, 平均目標價高於現價; 結構持平 |
| 內部人 | 偏空 | 16 筆、約 $62M 賣出, 0 筆買入; 部分可能為計畫性出售 |
| 機構 (13F) | 偏多 | 前十大 7 增 3 減, 資料滯後一期 |
| 價格與新聞動能 | 偏空 | 10/2 高點後回檔 -26%; Qualcomm 權利金風險未解 |
| 散戶社群 | 無法判定 | Reddit / StockTwits / X 皆無可用樣本 |

**Divergence flag: 是** (分析師與機構偏多, 與內部人賣出及價格動能偏空相反)。散戶 vs 分析師的分歧無法判定, 因為缺乏散戶資料。

## Data gaps and next checks
- 社群資料缺口: Reddit 與 StockTwits 需直接查看或改用可接受的資料源; 若要判定散戶傾向, 應補抓 10/17 至 10/19 的社群樣本。
- 價格快取最後一筆為 10/16, 10/17 與 10/18 未在快取中。
- 下一次財報: 2026-11-04 (yf, EPS 預估 $0.47), 在本報告資料基準之後。
- 上一次財報 (7/29) EPS $0.45 對 $0.40 預估, 超預期 11.4%。

## Sources
- yf 快取: `prices/yf/ARM.json`、`prices/ARM.csv`
- [Wealth Awesome, ARM 10/9 頁面](https://wealthawesome.com/why-arm-holdings-stock-plummeted-yesterday-10092026)
- [TIKR, ARM 10/8 下跌與 OpenAI 報導](https://www.tikr.com/de/blog/arm-holdings-stock-fell-6-in-a-day-as-an-openai-revenue-report-hit-chip-stocks-heres-where-openai-touches-arms-business)
- [The Star, Qualcomm 陪審團裁定 (2026-10-14)](https://www.thestar.com.my/tech/tech-news/2026/10/14/qualcomm-says-jury-found-arm-breached-license-agreement)
- [Simply Wall St, 分析師評等彙整](https://simplywall.st/community/narratives/us/semiconductors/nasdaq-arm/arm-holdings/dqgcwlk1-ai-data-centers-and-iot-will-transform-markets-3jyt/updates/12-analysts-remain-divided-on-arm-holdings-with-bulls-citing-s)
- [Benzinga, ARM sentiment 頁面](https://jp.benzinga.com/quote/ARM/sentiment)

SENTIMENT REPORT COMPLETE
