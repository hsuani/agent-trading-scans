# Sentiment — 3260.TW (威剛 ADATA Technology) as of 2026-11-22

## 資料來源狀態
- yf 工具：`insider`、`major_holders`、`inst_holders`、`recommendations`、`rec_summary` 皆回傳空陣列；`news` 回傳 403。Yahoo cookie/crumb 取得失敗（ConnectionError）。重試後仍不可用，快取也無資料，記為 DATA_UNAVAILABLE。`ratings` 不是合法子命令，以 `rec_summary` 代替，同樣不可用。
- Reddit（r/stocks）WebFetch 被阻擋，r/wallstreetbets 未嘗試（同一網域已阻擋）。記為 DATA_UNAVAILABLE。
- StockTwits：api.stocktwits.com DNS 解析失敗（網域不在允許清單），記為 DATA_UNAVAILABLE。需在工作階段網路設定允許此網域後才能重試。
- WebSearch 可用，以下為主要依據（多為新聞與論壇摘要，非原始資料）。

## Analyst consensus
- 買進／持有／賣出家數：DATA_UNAVAILABLE（yf rec_summary 無資料）。
- 近期評等變動：未找到 2026 年 11 月的個股評等調整。唯一找到的評等變動為 2025 年 11 月：法人將威剛由 BUY 下調為 Trading BUY，目標價由 297.5 元下調至 200 元（資料較舊）。
- 玉山投顧：有報導給予買進、目標價 556 元，但報導日期不明，無法確認是否為最新，標記為未驗證。
- 國票：搜尋結果中「由強力買進降為買進、目標價 160 元調降至 140 元」的內容，其實是旺宏（2345）的評等，與威剛無關，已排除。
- 公司端（11/6 法說）：預估 Q4 營收較 Q3 略減，主因年底客戶庫存結算與 12 月備貨保守；仍認為 2027 年 DRAM 缺貨將比今年更嚴重。

## Retail social
- Reddit：DATA_UNAVAILABLE（r/stocks 被阻擋）。
- StockTwits / X：StockTwits DATA_UNAVAILABLE。X 未搜尋到可用的社群貼文。
- PTT Stock 版：找到 2026 年 8 月的一篇威剛七月營收討論（七月營收年增 331.29%）。留言多空對立，有人宣稱放空，有人質疑本益比過高，也有人認為「低價庫存」說法已講了半年。樣本僅一篇，無法量化討論量。
- 聲量：無法量化與一般水準相比。搜尋結果顯示相關報導與論壇討論存在，但規模為定性判斷，無具體提及次數。
- 代表性說法（短引）：「股價仍跌逾4%」（新聞標題引述）；「利多不漲就算了」（專欄語）。

## Retail tilt
- 偏中性，多空分歧。
- 看多主題：記憶體供給緊、原廠庫存降至約 3–5 週（董事長表示已轉為賣方市場）、2027 年 DRAM 缺貨加劇、獲利大增（10 月營收約 170.63 億 TWD，年增約 282%；1–10 月累計約 1,343.69 億 TWD，年增約 222.7%；前三季 EPS 約 101.47 元）。
- 看空主題：本益比過高（有文章稱不到 5 倍，也有文章稱約 16 倍，兩者不一致，且來源日期不明）、Q3 毛利率 35.88% 低於預期（成本上升壓縮毛利）、Q4 營收可能季減、股價在獲利公布後反而下跌（10/30 收 346.5 元，單日跌 4.28%）、週期反轉與毛利率高點疑慮。
- 單位註記：營收以 TWD 億元表示，未與 B 混用。

## Insider activity
Net 6mo: DATA_UNAVAILABLE（yf insider 無資料）。
- WebSearch 未找到威剛個別董監持股申報明細。金管會 2026 年 6 月新聞稿僅有全市場彙總，未列個股。
- 建議查詢公開資訊觀測站（mops.twse.com.tw），公司代號 3260，「董事、監察人持股變動」。

## Ownership shifts
- major_holders / inst_holders：DATA_UNAVAILABLE。無法判斷機構持股集中度趨勢。

## Net sentiment score
Composite: **neutral（信心：低）**。
- 分析師面：可取得的資料不足，無法形成可靠的共識結論。現有零星資料偏向基本面看好（公司與部分投顧對 DRAM 供需樂觀），但有 2025 年評等下調紀錄，且 2026 年 11 月無新評等可比對。
- 散戶面：僅一篇 PTT 樣本，多空對立，偏中性。
- 股價反應面：獲利大增但股價未跟漲，市場對估值與毛利率存疑，偏保守。
- 內部人面：DATA_UNAVAILABLE。

Divergence flag: **無法判定（資料不足）**。目前無可靠的分析師多空分布可與散戶傾向比較。若後續取得 2026 年 11 月的評等分布，且 StockTwits／Reddit 可用，應再檢視是否出現分析師偏多、散戶偏空的背離。

## 資料缺口與後續
1. yf 的 insider、holders、recommendations、rec_summary 全部不可用，需確認 Yahoo 連線與 cookie/crumb 機制。
2. StockTwits 需在工作階段網路設定允許 api.stocktwits.com。
3. Reddit 目前被阻擋，需確認是否可用。
4. 玉山 556 元目標價、Substack 股價 372 元與本益比 16.18 倍等數據來源與日期不明，未採信為定論。

SENTIMENT REPORT COMPLETE
