# Sentiment — LAES (SEALSQ) as of 2026-10-27

> 資料可用性：Reddit (r/wallstreetbets, r/stocks) 經 agent proxy 封鎖 (403 / connect_rejected)；StockTwits DNS 無法解析；僅 yf 內部資料與網路搜尋可用。零售情緒部分為**資料缺口**，非正面或負面結論。最新 yf 交易紀錄為 2026-10-06，10-07 至 10-27 間無資料。

## Analyst consensus

2 buy / 0 hold / 0 sell (yf `rec_summary`，其中 1 strongBuy + 1 buy)。覆蓋家數極少，屬於薄樣本。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (當期) | 1 | 1 | 0 | 0 | 0 |
| -1m | 1 | 1 | 0 | 0 | 0 |
| -2m | 1 | 1 | 0 | 0 | 0 |

- 近三個月 yf 評等分布無變化，`recommendations` 未出現升評或降評紀錄。
- 網路搜尋的聚合資料 (Benzinga 8 月快照) 指 Cantor Fitzgerald 維持 Overweight，但 2026-04-02 將目標價由 $7 降至 $4；Benzinga 平均目標價約 $5。MarketBeat 平均評等 3.00 與 yf 的 2 buy 不一致，且可信度較低，僅列為參考。
- 目標價變動：Cantor 4 月降目標價為唯一可見的近期變動，yf 本身未提供目標價欄位。

## Retail social

- **Reddit**：無法取得。r/wallstreetbets 與 r/stocks 搜尋均被 proxy 擋下，無法計算提及數、樣本帖文或多空傾向。
- **StockTwits / X**：StockTwits 無法連線。X 無直接抓取，網路搜尋僅找到 Benzinga、MarketBeat、Tradersunion、Stockscan 等聚合頁，沒有可引用的散戶貼文。
- **聲量 (定性)**：搜尋結果反映「覆蓋與搜尋熱度稀薄」，零售聲量推估為**偏低**，但缺乏量化基準，此判斷信心低。
- **Themes**：無法從原始貼文歸納。聚合頁提及的議題為 H1 每股虧損 $(0.13) 低於預期、技術面偏弱、以及一則未經證實的 GigCapital8 合併消息。

## Insider activity

Net 6mo (2026-04-27 至 2026-10-27)：**$0 open-market buys，約 $0.58M sells** (USD)。

| 內部人 | 職稱 | 期間內主要交易 | 金額 (USD, 約) |
|---|---|---|---|
| ENGUENT JEAN-PIERRE | Officer | 5 月至 10 月多次出售 (每月約 15,000 股，7/8、8/5、9/3、10/6 為主) | 約 $0.27M，含 10/6 出售 35,000 股 @ $2.46 |
| MOREIRA CARLOS CREUS | CEO | 5/29、6/3、6/5 出售，合計約 $0.11M | 約 $0.11M |
| O'HARA JOHN CHARLES | CFO | 5/29、6/3、6/5 出售 | 約 $0.11M |
| BUONANNO FRANCK JEAN | Officer | 5/14 出售 20,000 股 @ $2.90 | 約 $0.06M |
| FEUARDENT MOREIRA ANDREAS | Officer (間接持有) | 期間內無出售紀錄 (4/7 出售在窗口外) | — |
| WARD PETER | Director | 6/16 行使衍生性證券 366,746 股，行使價 $0.01，無對應出售紀錄 | 行使成本 $3,667 |

- 期間內的 derivative 行使 (價格 $0.01) 多與後續出售配對，屬於選擇權或 RSU 行使後出售，不計為公開市場買進。
- 期間內 CEO 與 CFO 的出售集中於 5 月底至 6 月初，之後無紀錄。
- 出售價格區間約 $2.46 至 $3.69，最近一筆 10/6 為 $2.46。
- 無法確認這些出售是否屬於 10b5-1 預定交易計畫，yf 未提供此欄位。

## Ownership shifts

- 內部人持股 3.19%，機構持股 6.65%，機構家數 127。
- yf `major_holders` 僅為單一快照，無法判斷趨勢。機構集中度偏低，屬於小型外國發行人常見結構，不能視為機構背書的訊號。

## Net sentiment score

- **Analyst tilt**：偏多 (bullish)，但僅 2 家且近三個月無變化，信心低。
- **Retail tilt**：無法判定 (Reddit、StockTwits 不可用)，僅能推估聲量偏低。
- **Insider tilt**：偏空 (bearish)，6 個月內無公開市場買進，約 $0.58M 出售，主要為高階主管與 officer 的持續性出售。
- **Composite**：**偏空至中性 (bearish-leaning neutral)，信心低**。主因是內部人淨賣出與價格走弱，而非散戶訊號。分析師樣本過少，且零售資料缺失，無法形成完整判斷。

**Divergence flag：無法完整判定。**
- 分析師 (偏多) 與內部人 (淨賣出) 方向相反，這是一個值得注意的分歧訊號。
- 散戶方向因資料缺失無法比對，因此不能確認零售與分析師是否相反。
- 建議在 Reddit 或 StockTwits 可用時補查，並以更即時的股價資料確認 10/7 至 10/27 之間的價格變化與是否有新增內部人交易。

## 資料註記
- 網路聚合來源 (Benzinga、MarketBeat、Tradersunion、Stockscan) 彼此不一致，且多為非官方快照，只作為輔助參考。
- 網路搜尋提到「SEALSQ 將與 GigCapital8 (GIW) 合併，宣布日為 2026-10-09」，僅來自單一聚合頁，未獲其他來源證實，本報告不採用此說法作為結論。
- Benzinga 顯示 2026-10-09 股價約 $2.11，與 yf 最近內部人出售價 $2.46 (10/6) 相近，但非同一日的確認報價。

SENTIMENT REPORT COMPLETE
