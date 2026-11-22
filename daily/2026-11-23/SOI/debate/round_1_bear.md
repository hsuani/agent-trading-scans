# Bear case round 1 — SOI

## Thesis (1 分句)
在連代碼身分、股價、財報數字都無法驗證的狀態下，SOI 的多頭敘事完全建立在單一社群帳號（Serenity）轉述與未具名券商片段之上，風險/回報不可計算，唯一可操作的結論是迴避（avoid），而非建立空頭或多頭倉位。

## Demand / market risks
- 核心成長引擎「Photonics-SOI」的放量時程全靠管理層口頭指引（NPO 本財年底首批量產、CPO 進入 scale-out、TPO 為下一階段），news.md 明確標註為「二手轉述，未核對原始 earnings call」。時程本身即為執行風險，任何一環延後都會打破「$25M 季 → $200M 年 → $400M FY2028」的外推鏈。
- $25M 季度基數與 FY2028 $400M 預測之間的口徑未經核對（fundamentals.md 第19行），意味著目前看多的人用的是不同時間框架、甚至可能重複計算的數字；在口徑未統一前，任何倍數成長故事都無法被獨立驗證。
- UBS 已以「光子樂觀情緒過度」為由降評至 Sell，另一份報告（日期與券商名稱均未確認）指出 Photonics-SOI 要到 2029 年才會加速，發布當日股價跌約 14%（sentiment.md）。這代表至少有機構端聲音認為當前敘事的時間表本身就是錯的，而非僅是斜率問題。
- Citi 被轉述警示「investor expectations for Photonics-SOI growth might be excessive」——即便此警語本身也是二手轉述未核對原文，但它與 UBS 降評方向一致，顯示分歧不是孤例。

## Margin / cashflow risks
- fundamentals.md 的毛利率、營業利益率、ROE、ROIC、FCF/NI 全部 DATA_UNAVAILABLE。沒有任何歷史利潤率數據可用來驗證 Serenity 所稱「Margin expansion has come forward too」，這句話目前只是未附數字來源的口號。
- 「$1.2B 多年期產能承諾」即便存在，也是客戶端的保證金承諾（cash deposits），不是已認列營收；分階段支付的押金比例、違約條款、是否可取消，均無資料。把尚未入帳的客戶承諾當成估值支撐，是典型的敘事超前基本面案例。
- news.md 直接指出：公司公開描述的是「10 餘份產能保留協議」與押金機制，沒有揭露金額；「$1.2B」這個數字在 Reuters、The Star、Cryptobriefing、Blockonomi、Parameter 等所有可查來源中都找不到對應數字，也找不到 Serenity 原文。這是本次多頭論點的核心數字，卻是完全無法溯源的孤證。

## Valuation risk
- 無法建立：市值、股價、trailing/forward P/E、EV/EBITDA、P/FCF、P/S 全數 DATA_UNAVAILABLE（fundamentals.md、market.md）。Bear 目標價、下檔百分比、sector median 比較皆無法計算，不做虛構數字。
- 唯一可引用的分析師目標價為過期快照：S&P Global/StockAnalysis（截至 2026 年 5 月）19 位分析師共識 Hold，均價 €91.82；而 Morgan Stanley 當時喊到 €200，顯示即便在有數據的時點，分析師間的估值分歧本身就超過 2 倍，反映題材的估值錨點極不穩定。
- Worst case：若 $1.2B 承諾與 FY2028 $400M 營收指引任一項被證實為誇大或口徑混淆，且 UBS「2029 年才加速」的時程被證實，則目前建立在社群敘事上的任何溢價評價都沒有基本面支撐，股價修正幅度無上限可估（因無基準價格）。

## Competitive / regulatory
- 產業面有 Marvell–Lumentum 整併與同業（COHR、LITE）同步走強的順風，但這也代表下游客戶集中度上升，議價力可能轉向大型整合後買方，壓縮 Soitec 作為上游供應商的訂價權。
- UBS 估計 Photonics-SOI 市占約 95%（若屬實），高市占同時意味著成長空間遞減與單一客戶/應用集中度風險，一旦 CPO/NPO 放量時程不如預期，缺乏第二成長曲線。

## Tactical (technical)
market.md 明確為 **PRICE_DATA_UNAVAILABLE**：yfinance 連線遭 proxy 403 拒絕，快取 quoteType 為 NONE，repo 內無任何 OHLCV 序列。因此無法提供支撐、壓力、RSI、MACD、停損價位——任何技術面多空判斷在此狀態下都是虛構。這本身就是一個不可忽視的風險訊號：連最基本的可交易價格都取不到的標的，不應該被賦予倉位。

## Rebuttal to bull round 0
目前 `daily/2026-11-23/SOI/debate/` 目錄下尚無 round_0 bull 檔案可供逐點反駁。依現有四份輸入報告可預判的多頭論點與反駁如下：
- 預期 Bull 主張：「$25M→$1.2B LTA，Vindicated」（serenity 原話）。
  反駁：$1.2B 數字在所有專業媒體與公司公告中均查無對應，news.md 明確列為未驗證主張；且即使存在，也是未入帳的客戶保證金承諾，非營收。
- 預期 Bull 主張：FY2027 Q2 營收指引上修至 ~50% YoY，全年 2.5–3 倍基數，股價應聲上漲 15%。
  反駁：這是管理層指引，尚未經財報驗證；指引本身也是「口頭轉述」而非工具端可核對的財報數字，且過去已有一次因「2029 年才加速」的看法導致單日下跌 14% 的先例，說明指引可信度本身存在爭議。
- 預期 Bull 主張：產業順風（COHR、LITE 同步大漲）支持題材。
  反駁：同業上漲反映的是光通訊整體 beta，不能證明 Soitec 個股基本面已兌現；且 Soitec 自身股價、財報數據完全無法驗證，無法區分「題材 beta」與「公司 alpha」。

## Confidence
8/10。並非因為看空基本面確定會惡化，而是因為「完全無法驗證」這個狀態本身就是最強的避險理由：無股價、無財報、無法核對的核心數字（$1.2B）、分析師分歧（Hold 共識 vs Morgan Stanley €200 vs UBS Sell）。在無法建立任何可信倉位基準（進場價、停損、估值錨點）之前，任何多頭倉位的風險都不可控，應判定為 avoid。

BEAR ROUND 1 COMPLETE
