# Sentiment — 6438.TW (迅得) as of 2026-11-23

資料完整度：低。Yahoo 即時呼叫失敗（cookie/crumb 取得失敗），改用 repo cache（prices/yf/6438.TW.json，refreshed 2026-11-22）。insider 與 inst_holders 在 cache 中皆為空陣列。Reddit 與 StockTwits 無法連線（StockTwits 網域未在會話允許清單內）。WebSearch 可找到部分新聞與籌碼資料，但無散戶社群原文，結論置信度低。

## Analyst consensus

| 評等 | 家數 |
|---|---|
| Strong Buy | 1 |
| Buy | 1 |
| Hold | 0 |
| Sell | 0 |
| Strong Sell | 0 |

共 2 家（樣本過少，不具統計意義）。Recent moves: recommendations 只回傳單一當期快照（period 0m），沒有可辨識的升級、降級紀錄，也沒有目標價變動與券商名稱。WebSearch 未找到 2026 年的券商評等報導。

基本面事件（cache earnings_dates，與分析師情緒相關）：2026-11-16 公布的財報 EPS 2.33 元，高於市場預估 2.26 元，超標 3.1%。前幾季為 Q2 2.02 元（未達預估 -5.16%）、Q1 1.76 元（未達預估 -5.38%）。Q3 EPS 與 Q2 股本計算核對：2.33 元 × 約 8,220 萬股 ≈ 1.9 億元稅後純益，與 Q2 的 2.02 元 × 8,220 萬股 ≈ 1.66 億元（新聞報導 1.66 億元）口徑一致。

營收（WebSearch，新聞口徑）：2026 年第三季營收 19.45 億元，季增 6.64%、年增 13.62%，為歷史單季新高。2026 年 1 至 8 月累計營收 48.18 億元，年增約 11.5%。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 無法連線（WebFetch 被擋），無樣本，無法判斷傾向。
- StockTwits: 網域無法解析（不在會話允許網路內），無樣本。依指示不重試。
- PTT / X / 其他社群: WebSearch 未找到 2026 年 11 月的散戶討論串或 X 貼文。搜尋結果以股價、籌碼與新聞頁面為主，無可引用的散戶原文。
- Buzz volume: 無法判斷相對於平常的聲量（無可用計數）。
- Themes（僅依新聞標題與籌碼頁面，非散戶原文）:
  - 先進封裝與台積電、日月光擴廠供應鏈題材（新聞以「台積電供應鏈」「先進封裝業務比重走高」為標題）
  - AI 自動化與機器人零組件漲價循環題材
  - 海外擴廠（PCB 台廠海外擴廠需求）；董事長表示明年海外營收佔比可望達 5% 至 10%
  - 估值偏高與股利下修：2026 年現金股利合計 3 元，低於 2025 年的 5 元
- Retail tilt: 無法判定（bullish / bearish / mixed 皆無直接證據）。

## Insider activity

Net 6mo: 無法確認。yfinance insider 回傳為空陣列，不代表無交易，資料源可能缺漏。
WebSearch 找到的 Goodinfo 股權異動頁面顯示，2026 年 1 月與 3 月有董事本人及其持有之致盛控股有限公司的一般交易紀錄，但搜尋摘要排版混亂，無法確認每筆為增持或減持、股數與金額，因此不計算淨買賣金額。

Notable: 董事（王年清 為董事長，名下相關交易人包含致盛控股）於 2026 年 1、3 月有交易紀錄，方向待確認。CEO 與 CFO 的個別交易無資料。
建議以 MOPS（公開資訊觀測站）董監持股申報原始資料核對。

## Ownership shifts

- 內部人持股比例（insidersPercentHeld）: 25.28%
- 機構持股比例（institutionsPercentHeld）: 1.59%（流通股口徑 2.13%）
- 機構家數（institutionsCount）: 8
- inst_holders 明細為空，無法判斷機構增減趨勢。

內部人持股高、機構持股低，為結構性特徵，不是方向性訊號。機構趨勢需以 MOPS 或 TWSE 籌碼資料補強。

## Market context（僅供參考，非本報告結論）

- 股價參考：WebSearch 所見 2026 年 10 月初約 164.5 元、10/14 收 182 元，7 月約 147.5 元。各來源日期不一，本報告未取得 2026-11-21 或 11-22 收盤價。
- 以 164.5 元與 82,206,325 股估算，市值約 135 億元（口徑為 10 月初股價，非當日市值）。
- 融資餘額（玩股網，6 月）約 4,303 張，融券很少。

## Net sentiment score

Composite: **bullish（置信度低）**。依據：
- 分析師 2 家皆為買進或強力買進，0 家持有或賣出（樣本過少）。
- 最近一季 EPS 超出預估 3.1%，前兩季則未達預估，財報對情緒的正向訊號尚未連續。
- 散戶與內部人訊號皆無法可靠取得，無法互相驗證。

Divergence flag: **無法判定**。散戶傾向無資料，無法比較與分析師傾向是否相反。

## 資料缺口與後續

1. Reddit、StockTwits 無法連線，散戶情緒無直接樣本。若會話允許網域設定，可補抓 r/wallstreetbets、r/stocks 與 api.stocktwits.com。
2. insider 與 inst_holders 在 cache 與即時來源皆為空，需確認 yfinance 對台股的內部人與機構資料覆蓋度，或改以 MOPS 資料補充。
3. 分析師樣本僅 2 家，recommendations 無歷史變動，無法判斷評等趨勢。
4. WebSearch 結果中的 EPS 與營收數字來自多個新聞與統計頁面，日期與口徑不完全一致（例如部分來源的法說會日期指向 2025 年），本報告僅採 cache earnings_dates 的 EPS 與 Q3 營收新聞數字。

SENTIMENT REPORT COMPLETE
