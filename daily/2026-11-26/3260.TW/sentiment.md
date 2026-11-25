# Sentiment — 3260.TW (威剛 ADATA) as of 2026-11-26

資料完整度：低。yfinance 全部端點（rec_summary / recommendations / insider / major_holders）在本次執行皆因 Yahoo cookie/crumb 連線失敗而回傳空值；Reddit 與 StockTwits 無法連線。以下結論主要依據新聞搜尋結果，信心受限。

## Analyst consensus
資料缺口：yf rec_summary 回傳空值，無法取得目前 買進 / 持有 / 賣出 家數。以下為新聞彙整可辨識的券商評等（非完整統計）。

| 券商 | 評等 | 目標價 (TWD) | 日期 | 備註 |
|---|---|---|---|---|
| 玉山投顧 | 增持 | 420 | 2026-11 初 | 預估 2027 EPS 84.15 元；毛利率回落至 28.64% |
| 國票 | 買進（由強力買進下調） | 未取得 | 2026-11 | 因營收與獲利再次下修，短期評價下調 |
| 某投顧 | 買進 | 556 | 2026-05-08 | 舊資料，僅供參考 |

Recent moves: 2026-11-06 法說後，公司表示 Q4 營收將較 Q3 略減（年底客戶庫存結算），但對 DRAM 明年缺貨程度維持正向看法。國票下調評等屬本季最明確的負向動作；玉山維持增持。

注意：常被引用的「降評、目標價 200 元」報導發布於 2025-11-21，屬舊聞，不列入本季判斷。

## Retail social
- Reddit (r/wallstreetbets, r/stocks)：無法連線（WebFetch 失敗），無樣本。Tilt：未知。
- StockTwits：無法連線（DNS 解析失敗，api.stocktwits.com 不在允許網域內），無樣本。
- X / 新聞散戶言論：本次 WebSearch 未找到散戶論壇或社群的具體貼文，僅有媒體與法人報導。Buzz 量：無法量化，以定性判斷屬一般（相較記憶體族群的高關注度，個股單獨討論度未見明顯放大）。
- 參考股價走勢：最近可查紀錄為 2026-10-30 收 346.5 元，當日下跌逾 4%，記憶體族群同步走弱；11 月下旬股價未取得。

Themes (從媒體與法人報導歸納):
1. 記憶體缺貨週期：DRAM 明年缺貨可能更嚴重，NAND 價格維持高檔（外資估今年 NAND 價格漲約 40%）。偏多主軸。
2. Q4 季減與毛利率壓力：Q4 營收季減、Q3 表現低於預期被認為受成本推升影響毛利，是主要疑慮。
3. 獲利創高但評價受質疑：前三季營收、營業利益、稅後淨利與 EPS 皆創歷史新高，但市場關注獲利成長是否更依賴價格而非毛利擴張。

## Insider activity
資料缺口：yf insider 回傳空值，無法計算近 6 個月淨買賣金額。
Net 6mo: 未取得（無法判斷 CEO / CFO / 其他人員買賣方向）。

## Ownership shifts
資料缺口：yf major_holders 與 inst_holders 未取得，無法判斷機構持股集中度趨勢。

## Fundamentals reference (供交叉核對，非情緒來源)
| 指標 | 數值 | 單位 |
|---|---|---|
| 2026-10 單月營收 | 170.63 | 億 TWD（較 9 月 +8.5%，年增 +282.3%） |
| 2026 年 1-10 月累計營收 | 1,343.69 | 億 TWD（年增 +222.7%） |

Money unit check: 單月 170.63 億 TWD 對 1-10 月累計 1,343.69 億 TWD，約為 10 個月平均 134.4 億，與 10 月單月 170.6 億的高點走勢相符，單位一致（皆為億 TWD，未混用 B）。

## Net sentiment score
Composite: **neutral（偏多但信心低）**。
- 偏多訊號：記憶體缺貨敘事、玉山維持增持且目標價 420 元、前三季獲利創高。
- 偏空訊號：國票下調評等、Q4 營收季減、毛利率壓力疑慮。
- 信心：低。散戶端與內部人、機構持股端皆無資料，僅能由媒體與券商報導推估。

Divergence flag: **無法判定**。散戶端無樣本，無法與分析師端比較是否反向。以已知券商端看，評等分歧（增持 vs 買進下調）而非一致偏多或偏空。

## Data gaps / follow-up
- yfinance cookie/crumb 連線失敗：待網路恢復後重跑 rec_summary、recommendations、insider、major_holders、inst_holders。
- api.stocktwits.com 需於 session 網路設定中允許後才能重試。
- Reddit 連線失敗，需確認 www.reddit.com 網域可達。
- 日期提醒：系統當日為 2026-11-25，本報告依任務指定之 as-of 2026-11-26 撰寫，部分資料為 11-25 前的最新可得資訊。

SENTIMENT REPORT COMPLETE
