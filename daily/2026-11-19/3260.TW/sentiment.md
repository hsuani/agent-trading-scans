# Sentiment — 3260.TW 威剛 ADATA Technology as of 2026-11-19

資料說明：本次情緒資料大多無法取得。Yahoo Finance 在此環境遭 proxy 阻擋（curl 403），`pipeline/tools/yf` 對 3260.TW 的 rec_summary、recommendations、insider、major_holders 皆回傳空值，快取檔 `prices/yf/3260.TW.json`（2026-11-18 15:32 UTC 更新）同樣全部為空。威剛在 TPEx 上市，Yahoo 代碼較可能為 3260.TWO，直接以 3260.TWO 重試仍被阻擋。Reddit 公開 JSON 與 api.stocktwits.com 皆無法連線（後者為 DNS 無法解析，需於 session 網路設定中放行）。以下以網路搜尋結果補充，但多為新聞與券商彙整頁，樣本極少。

## Analyst consensus

無法建立可靠的 buy / hold / sell 分布。目前可見的資料來源彼此不一致，且都只涵蓋一至兩位分析師：

| 來源 | 評等 | 目標價 | 時間點 | 備註 |
|---|---|---|---|---|
| Investing.com 彙整 | 1 Buy / 0 Hold / 0 Sell | 平均 NT$455 | 頁面最新財報引用 2026-05-13 | 僅 1 位分析師，無法確認券商 |
| Simply Wall St | 未註明 | NT$316（由 NT$200 上調） | 2026-03 | 單一分析師 |
| Oninvest | Hold（發行人評等） | 平均 NT$194 | 2026-03-31 更新 | 隱含下檔空間，與 Investing.com 方向相反 |
| 工商時報報導 | Trading BUY（由 BUY 下調） | NT$297.5 下修至 NT$200 | 2025-11 | 已明顯過時 |

近期動向：2025-11 的下調是最明確的評等變動，理由是短線記憶體報價漲幅趨緩。2026 年以後的目標價上修（NT$316，以及 Investing.com 的 NT$455）與基本面改善方向一致，但都無法確認是否為最新報告。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：無法取得。WebFetch 回傳 blocked，本次沒有任何樣本可判斷 tilt。
- StockTwits：無法取得。DNS 解析失敗，需於 session 網路設定中放行 api.stocktwits.com 後才能重試。
- X / 論壇：WebSearch 以繁體中文查詢網友看法，結果全部是新聞、法說會內容與券商觀點，未找到 PTT、Dcard、Threads 等論壇或社群的留言。**本次無可用的社群情緒資料。** 建議人工查詢 PTT 股板或 Dcard 股票版。
- 討論量（buzz volume）：無法量化，因此無法與平常水準比較。
- 主題（僅依新聞報導歸納，非網友發言）：
  - 記憶體（DRAM / NAND）缺貨與合約價走勢，為公司與媒體的主要敘事。
  - 高庫存在漲價循環中被視為優勢，但價格反轉時會變成風險。
  - 第四季年底客戶庫存結算造成營收可能略降，是法說會後的主要討論點。

## Insider activity

Net 6mo：無法取得。yf 的 insider 資料為空，WebSearch 也未找到 2026 年下半年董監事個人持股申報的明細。

公司層級的訊號：威剛董事會於 2026-11-09 公告買回庫藏股 600 萬股（約占已發行股份 1.68%），目的是轉讓予員工，買回期間為 115/11/10 至 116/1/8（民國年），價格區間 NT$213.5 至 NT$532.2。公告時公司已持有約 996 萬股。這屬公司買回，不等同董監事買賣，不應計入 insider net 數字。前一次買回（去年 4 月至 6 月）執行率為 97%（實買 7,763 張，上限 8,000 張）。

個人申報的確認路徑：公開資訊觀測站「董監持股及質押」與「內部人持股轉讓事前申報」。

## Ownership shifts

無法取得。major_holders 與 inst_holders 皆為空值，無法判斷機構持股集中度趨勢。

## 基本面背景（供交叉檢查，非情緒指標）

| 項目 | 數值 | 來源性質 |
|---|---|---|
| 2026 Q1 EPS | NT$30.05 | 新聞報導 |
| 2026 Q2 EPS | NT$32.39 | 新聞報導 |
| 2026 上半年 EPS | NT$62.46（30.05 + 32.39 ≈ 62.44，四捨五入差異可接受） | 新聞報導 |
| 2025 全年 EPS | NT$23.18 | 新聞報導 |
| 2026 年 5 月合併營收 | 129.4 億元 | 新聞報導 |
| 2026 年 10 月營收 | 170.6 億元（月增 8.5%，年增 28.2%） | 新聞報導 |
| 2026 年 1–5 月累計營收 | 496.1 億元 | 新聞報導 |
| 2026-10-30 收盤（盤中） | NT$346.5（跌 NT$15.5，-4.28%） | nStock 頁面，價格時效需注意 |

Q4 展望（2026-11-06 法說會，公司自述）：第四季營收預期較第三季略降，原因是年底客戶庫存結算，12 月備貨可能保守。公司表示 DRAM 目前仍全年缺貨，2027 年缺貨將較 2026 年更嚴重，且記憶體產業已進入賣方市場。

注意：搜尋結果中有一篇報導聲稱 11 月營收創新高，但截至 2026-11-18 11 月營收尚未公布，無法確認，本報告不採用。

## Net sentiment score

Composite：**neutral（信心：低）**

- 分析師面：樣本過少且彼此矛盾。Investing.com 的單一 Buy 與目標價上修偏多，Oninvest 的 Hold 與 NT$194 平均目標價偏空，整體落在中性。
- 散戶面：無資料，不評分。
- Insider 面：無個人申報資料。公司買回庫藏股供員工使用，屬輕度正向的公司行為，但不計入 insider 分數。
- 公司法說的基調（DRAM 缺貨延續至 2027）偏多，但 Q4 季減預期偏保守，兩者相抵。

Divergence flag：**無法判定**。因缺少散戶 tilt，無法確認是否與分析師方向相反。待 Reddit 或 StockTwits 放行後再重新評估。

## 資料缺口與後續

1. Yahoo Finance 被 proxy 阻擋，rec_summary、insider、major_holders 需待網路放行後重跑，或改由公開資訊觀測站人工取得。
2. 3260 在 TPEx 上市，建議確認 yf 代碼應為 3260.TWO 而非 3260.TW。
3. Reddit 與 StockTwits 皆需放行，否則散戶情緒面永遠空白。
4. 目標價資料需以券商原始報告為準，本報告所列數字僅供參考。

來源（網路搜尋，供交叉檢查）：
- https://uanalyze.com.tw/articles/3527858570
- https://www.ctee.com.tw/news/20251121700950-430201
- https://www.investing.com/equities/adata-technology-co-ltd
- https://simplywall.st/stocks/tw/semiconductors/tpex-3260/adata-technology-shares/valuation
- https://en.oninvest.com/issuers/3260-two
- https://finance.technews.tw/2026/07/28/adatas-eps-reached-62-46-yuan-in-the-first-half-of-2026/
- https://finance.technews.tw/2026/04/28/adatas-first-quarter-eps-reached-a-record-high-of-nt30-05/
- https://finance.technews.tw/2026/06/08/adatas-may-revenue-reached-a-record-high-of-nt12-94-billion/

SENTIMENT REPORT COMPLETE
