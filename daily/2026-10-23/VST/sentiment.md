# Sentiment — VST (Vistra Corp) as of 2026-10-23

## Analyst consensus
yf rec_summary（當期 0m）：4 strongBuy / 18 buy / 0 hold / 0 sell / 1 strongSell，共 23 家，合計約 87% 買進評等。

- 近四個月趨勢：strongBuy 維持 4、strongSell 維持 1，buy 由 15 增至 18，hold 與 sell 皆為 0。Analyst 端沒有出現降評，最近一期的變化是買進家數增加。
- 注意：yf `recommendations` 只回傳與 rec_summary 同格式的月度快照，沒有逐筆 upgrade / downgrade 紀錄，因此個別調評與目標價變動列為 DATA_UNAVAILABLE（工具未提供）。
- 目標價：TIKR（2026-10-18 前後）引用平均目標價約 $210.10；BMO 將目標價由 $236 上調至 $245，維持 Outperform（來源文章未標明確切日期）。
- 來源不一致：WebSearch 引用的 TIKR 數字為 17 buy / 4 outperform / 1 underperform（合計 22 家），與 yf 的 23 家略有差異；Barchart（2026-08-24）則為 16 strong buy / 1 hold，與 yf 的 0 hold 不一致。以 yf 為主，但家數與分類以不同來源為準的差異需留意。
- 盈餘預估下修：TIKR 指出自 2026-06-30 起，市場一致預估 2027 營收下修約 4%、2028 營收下修約 3%。評等仍偏多，但預估數字在走弱，兩者出現分歧。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 對 Reddit 的 search.json 被阻擋，以 WebSearch 搜尋 Reddit 亦未回傳 VST 相關討論串（搜尋 reddit.com 網域也被拒絕）。無法取得樣本貼文，也無法判斷 Reddit 上的多空傾向。
- StockTwits：DATA_UNAVAILABLE（直接 API 未取得，搜尋亦無 StockTwits 頁面結果）。
- X / 社群聚合站（LunarCrush 快照，僅作代理參考）：
  - 正面情緒占比在不同快照間為 81% 至 96%。
  - 24 小時貼文數約 168 至 334 篇；互動量在不同快照間差距很大（約 76K 與約 550K 以上），看不出穩定的熱度基準，因此「聲量相對常態」只能定性判斷為「偏高但不穩定」。
  - 各快照的股價落在約 $135 至 $158，代表它們的抓取時間不同，不能當成同一時點的數據使用。
  - 其中的 AI 生成摘要把下跌歸因於 Q2 GAAP 未達預期與非現金避險損失，這是自動摘要，只能當作線索。
- 選擇權代理指標（Benzinga，約 2026-08-28 快照）：put/call ratio 0.51，偏向買權，short float 約 3.3%。日期偏舊，僅供參考。
- 散戶總體傾向：聚合站顯示偏多，但樣本來源與時點不一致，信心低。

- Themes（從新聞與聚合站摘要歸納）：
  1. 避險（hedge）損失：Q2 GAAP 未達預期，市場擔心避險部位限制上行空間，BMO 也將此列為投資人關注點。
  2. 德州電價與資料中心併網：TIKR 指出德州電價走弱，以及州層級暫停資料中心併網申請，壓抑估值。
  3. AI / 資料中心電力需求：仍是多方主要論述；Helix 產能擴充被視為中長期支撐。
  4. 政策利多：2026-10-05 能源部（DOE）提供最高 $4.2B 的有條件貸款，用於核電機組 uprate。
  5. 近期催化劑：Q3 財報預定 2026-11-06，為下一個明確事件。

## Insider activity
統計區間：2026-04-23 至 2026-10-23（6 個月）。金額為 USD，單位 M。排除 Stock Award（Grant）與 Stock Gift 等零現金流交易。

| 項目 | 金額（USD M） | 筆數 |
|---|---|---|
| 公開市場買進 | 1.2 | 2 |
| 賣出 | 25.9 | 10 |
| 淨額 | -24.7 | — |

- 賣出者與金額（USD M）：Hudson, Scott A.（Officer）約 10.3；Moldovan, Kristopher E.（CFO）約 6.3；Helm, Scott Bradford（Director）4.0；Acosta, Arcilia C.（Director）2.5；Montemayor, Margaret M.（Officer）約 1.6；Sult, John R.（Director）1.1；Barbas, Paul M.（Director）0.07。
- 買進者：CEO Burke, James A.（2026-08-24 買進 2,000 股，約 $135.00；2026-09-01 買進 6,665 股，約 $135.25 至 $135.99），合計約 $1.2M。
- 重點觀察：
  - 本區間內唯一的公開市場買進來自 CEO，價位在 $135 附近，低於其後的多數賣出價（$150 至 $170）。
  - CFO 與 Hudson 在 2026-09 至 10 月的賣出價位集中在 $150 至 $165，屬於高價區的減持。
  - 2026-02-24 有大規模 Stock Award（$171.62 計價，CEO 320,000 股），屬於授予而非市場交易，不計入淨額。
  - 這些賣出是否屬於 10b5-1 預定計畫，工具資料無法判定，列為未驗證。
- 較長期背景：2025 年 9 月至 10 月，CEO 以期權行權後賣出的規模很大（單筆多為 4,000 萬至 1,000 萬美元級別，價位 $186 至 $216），在 2025 年 12 月後無對應大量賣出。

## Ownership shifts
- 機構持股比例 92.1%（institutionsFloatPercentHeld 92.9%），機構家數 1,882；內部人持股比例 0.77%（yf major_holders）。
- 機構趨勢：DATA_UNAVAILABLE（無彙總的季度變化數字）。Fintel 個別申報人的 13F 變化參考如下：
  - Morgan Stanley：2026-03-31 持股約 8.26M 股，較前期增加約 4.3%。
  - Legal & General：2026-03-31 持股約 1.74M 股，減少約 1.9%。
  - Nomura：2026-03-31 持股約 3.4 萬股，減少約 63%（同時有選擇權部位）。
  - Exchange Traded Concepts：2026-06-30 持股約 18.9 萬股，增加約 11.7%。
  - Viking Fund Management：2026-06-30 持股 3.5 萬股，增加約 75%（基數小）。
- 結論：個別申報人方向不一，無法判定整體機構淨增減。

## Net sentiment score
- 分析師（高信心）：偏多。23 家中 22 家買進或強力買進，無 hold 與 sell 增加，平均目標價高於近期股價（約 $152）。但盈餘預估下修，評等與預估走向有落差。
- 散戶（低信心）：偏多（聚合站正面情緒高），但缺乏 Reddit 與 StockTwits 直接數據，時點與樣本不一致，不足以作為強訊號。
- 內部人（中信心）：偏空。6 個月淨賣約 $24.7M，主要為高價區減持；僅 CEO 於 $135 附近有小額公開買進。
- 綜合：中性偏多（信心中等）。分析師與聚合站偏多，內部人淨賣與預估下修構成主要反向訊號。

Divergence flag: 是（部分）。
- 散戶與分析師方向一致（皆偏多），但信心都不高，因為散戶資料不完整。
- 內部人淨賣與分析師買進評等方向相反，這是本報告最明顯的分歧點。
- 盈餘預估下修與買進評等也不一致，值得留意。

## 資料缺口
- Reddit：DATA_UNAVAILABLE
- StockTwits：DATA_UNAVAILABLE
- 逐筆評等調整（upgrade / downgrade）：DATA_UNAVAILABLE
- 機構持股彙總趨勢：DATA_UNAVAILABLE
- yf 與 WebSearch 之間的分析師家數與分類不一致，已於上文標註。

## 資料來源
- yf rec_summary、recommendations、insider、major_holders（pipeline/tools/yf VST）
- TIKR 文章（2026-10-18 前後）：https://www.tikr.com/blog/vistra-stock-is-down-28-over-the-past-year-discount-or-warning-sign
- BMO 目標價上調：https://www.tipranks.com/news/the-fly/vistra-price-target-raised-to-245-from-236-at-bmo-capital-thefly
- Barchart 共識評等：https://www.barchart.com/story/news/3999453/vistra-corp-stock-is-wall-street-bullish-or-bearish
- LunarCrush 社群情緒快照：https://lunarcrush.com/en/stock/vistra-corp-vst
- Benzinga 選擇權與分析師頁：https://kr.benzinga.com/quote/VST/price-targets
- Fintel 13F 個別申報人頁：https://fintel.io/so/us/vst/morgan-stanley

SENTIMENT REPORT COMPLETE
