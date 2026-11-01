# Sentiment — AMD as of 2026-11-02

## Analyst consensus

rec_summary（0m，本月）：Strong Buy 5 / Buy 39 / Hold 11 / Sell 0 / Strong Sell 0，合計 55 家。Buy 合計 44 家（約 80%），Hold 11 家，Sell 0 家。

| 期間 | Buy（含 Strong Buy） | Hold | Sell |
|---|---|---|---|
| 0m（本月） | 44 | 11 | 0 |
| -1m | 45 | 11 | 0 |
| -2m | 44 | 11 | 0 |

評級分布近三個月幾乎不動，沒有賣出評級。

近期動向（來自 WebSearch，未經主要來源核對）：
- Cantor Fitzgerald（10/4）：維持 Overweight，目標價 $700。
- Citi（10/5）：目標價由 $575 上調至 $800。
- HSBC（5/4）：由 Buy 降為 Hold，目標價 $340（前值 $335），理由為估值與產能限制。
- Northland（4/27）：降為 Market Perform。
- Susquehanna（4/29）：目標價由 $320 上調至 $390，依據為雲端客戶 MI300 訂單增加。
- Daiwa：由 Buy 降為 Outperform，目標價升至 $500，日期無法確認。
- Mizuho、Wedbush 於 7/27 維持買進評級。

目標價共識來源之間互相矛盾：Walnut Invest（資料截至 8 月）平均 $579.11、中位數 $600、47 家；TIKR（7 月）平均 $508。工具未提供目標價歷史，無法以官方數據驗證。Capital.com 文章所載股價區間 $26 至 $580 明顯為資料錯誤，不採用。

## Retail social

- **Reddit**：WebFetch 無法連線 reddit.com，r/wallstreetbets 與 r/stocks 均未取得近期貼文。WebSearch 只找到 2021 至 2023 年的舊報導，無法代表當前情緒。r/AMD_Stock 約 6.8 萬成員（GummySearch，日期不明）。**取樣：0 篇，無法判定 tilt。**
- **StockTwits**：api.stocktwits.com 無法解析（DNS 失敗），需由 session 網路設定允許該網域後才能重試。**取樣：0 則。**
- **X / 新聞聊天**：WebSearch 結果多為 mid-2026 以前的分析文章，未找到 11 月或 10 月的即時討論。
- **Buzz 量能**：無法量化，無法與常態比較。定性判斷為「資料缺口」。
- **Themes（來自新聞與分析文章，非社群原文）**：AI 資料中心與 agentic AI 需求為主要多頭論述；CPU TAM 上修也被提及；估值（HSBC、Daiwa 的降評理由）與股價大幅上漲後的波動為主要空頭論述；產能限制（supply constraint）為反覆出現的風險。

**零售傾向：無法判定（資料不足）。** 無社群樣本可引用。

## Insider activity

6 個月窗口（2026-05-02 至 2026-11-02）內，工具回傳的公開市場賣出共 18 筆，合計約 **$0.26B（USD 2.60 億）**。**公開市場買進：0 筆。** 另有 Stock Gift 與選擇權行使（conversion）各數筆，不計入買賣金額。部分 8 月 7 日、8 月 14 日、6 月 15 日的列項沒有金額欄位，性質不明（可能為稅款扣繳或獎酬歸屬），未計入。

| 人員 | 職稱 | 6mo 賣出（USD M） | 主要交易 |
|---|---|---|---|
| Lisa T. Su | CEO | 約 168.6 | 5/13 約 55.7、6/10 約 57.6、8/18 約 7.2、9/10 約 48.1（每次 15k 至 125k 股） |
| Forrest E. Norrod | Officer | 約 34.4 | 4 次「行使 $84.85 或 $34.19 選擇權後賣出」，最近一次 10/15 約 9.3 |
| Mark D. Papermaster | CTO | 約 23.9 | 6 月與 7 月每月約 3.2 至 3.3；8/14 約 3.8；8/20 約 13.6 |
| Paul D. Grasby | Officer | 約 18.6 | 5/8 約 10.8；8/17 約 7.7 |
| Jean X. Hu | CFO | 約 7.1 | 8/25，15k 股 |
| Nora M. Denzel | Director | 約 5.5 | 6/2，約 10.4k 股 |
| Ava M. Hahn | General Counsel | 約 1.5 | 8/11、8/18 |

Notable：
- CEO Lisa Su 在窗口內 4 次大額賣出，合計約 $168.6M，為淨賣出的最大來源。
- Norrod 與 Papermaster 多次行使低行權價選擇權後立即賣出（exercise-and-sell 模式），需留意是否為 10b5-1 預定計畫，但工具未提供計畫註記，無法確認。
- 窗口內無任何高階主管公開市場買進。

## Ownership shifts

- 機構持股比例 75.4%（institutionsPercentHeld 0.7537），機構數約 5,170 家。
- 內部人持股 0.42%。
- 工具只給單期快照，無法判斷趨勢（增減方向不明）。

## Net sentiment score

**綜合：中性（信心：中低）**

- **分析師面**：偏多。44/55 家給買進，0 家賣出，近三個月評級穩定。目標價共識偏高但來源不一致。
- **內部人面**：偏空。6 個月約 $0.26B 淨賣出，0 筆公開市場買進，CEO 大額賣出。這類賣出可能含計畫性或稅務性質，無法確認，權重應打折。
- **零售面**：無資料。Reddit、StockTwits 均不可用，X 無近期可用樣本。
- 綜合為「分析師偏多、內部人偏空、零售不明」，因零售面缺口，整體判定中性，信心中低。

**Divergence flag：是（分析師與內部人方向相反）。** 分析師評級高度偏多，但內部人在窗口內以持續賣出回應。零售方向無法判定，因此無法確認是否也出現零售與分析師的分歧。

## 資料缺口與待辦
1. Reddit、StockTwits 不可用。StockTwits 需由 session 網路設定允許 api.stocktwits.com 後重試。
2. 目標價歷史與近期目標價變動未取得，建議以主要金融資料源（如 Yahoo Finance、TipRanks）核對。
3. 內部人交易計畫（10b5-1）是否存在，需 SEC Form 4 的計畫註記確認。
4. 機構持股趨勢需第二期快照（13F 比較）。

SENTIMENT REPORT COMPLETE
