# Sentiment — 3289.TWO (宜特) as of 2026-10-25

> 資料完整度低。analyst、insider 與 Reddit/StockTwits 來源皆無法取得，本報告的情緒判定信心低。
> 注意：今日實際日期為 2026-10-24，DATE 為 2026-10-25，最新價格資料止於 10/16，最新營收止於 9 月（10/8 公布）。

## Analyst consensus
資料無法取得。yfinance 的 recommendations、rec_summary 皆回傳空值，原因是 fc.yahoo.com 的 CONNECT 被 egress proxy 以 403 拒絕（政策阻擋，未重試）。目前無法給出 買進/持有/賣出 的家數。

最近可查到的券商評等資料都已過時，不能代表現在：
- 2024 年 8 月：買進評等，目標價上調至 165 元。
- 2025 年 7 月：目標價上調至 135 元，並預估 2025 年營收 48.02 億、2026 年營收 54.62 億。
- 2026 年 10 月的評等與目標價：搜尋找不到。

對照基本面：股價 10/16 收 135.5 元（另一來源 9/18 收 136.5 元，年份標示不一致）。若以 135.5 元對照 2025 年 7 月的 135 元目標價，股價已接近當時目標價，但這不是 2026 年的券商看法。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：無法取得。WebFetch 回傳 "unable to fetch from www.reddit.com"，視為政策阻擋，未重試。
- StockTwits：無法取得。api.stocktwits.com 解析失敗（ENOTFOUND），視為網路政策阻擋。
- X / 新聞與論壇：WebSearch 找不到 2026 年 10 月的個股意見。HiStock 論壇 7 月的貼文偏向提問（能否突破壓力、漲勢是否延續），沒有明確多空共識。
- 討論量：無法量化，無法與平常量比較。
- 主題（僅依 7 月論壇摘要，時效低）：壓力位突破、與 CPO / 矽光子的題材關聯。
- 整體傾向：無法判定（mixed / unknown）。

## Insider activity
資料無法取得。yfinance insider 回傳空值（同上，proxy 阻擋）。

Yahoo 股市「申報轉讓」頁面最新一筆為 2025-04-17，經理人林榆桑 贈與 10 張。6 個月窗口（2026-04-25 至 2026-10-25）內，此來源未見記錄。不過該頁面快照日期為 2026-01-23，不排除之後有未收錄的申報。

Net 6mo: 無法計算（$0 buys / $0 sells 僅代表資料缺漏，不代表沒有交易）。
- 需以 MOPS 公開資訊觀測站「內部人持股轉讓事前／事後申報」查詢 3289，篩選董事與經理人。
- 2025 年 8 月董事會決議現金增資 1,200 萬股，其中 960 萬股由原股東依持股比例認購（時報資訊報導）。這屬於公司層面的資本行動，不是內部人買賣。
- 2026 年 6 月 12 日股東會改選董監事（MONEY LINK 基本資料），新任董監持股變化需另查。

## Ownership shifts
- yfinance major_holders：insidersPercentHeld 17.55%、institutionsPercentHeld 2.74%、institutionsFloatPercentHeld 3.32%、機構家數 7。
- 機構持股比例偏低，且資料來源為 yfinance 的快照，日期不明，趨勢（增持或減持）無法判定。
- 外資買賣超：搜尋到的 MONEY LINK 法人資料只到 2025 年 9 月前後；HiStock 顯示 8/3–8/4 外資買超、8/5 外資賣超，時效已過。

## Fundamental context（用於判讀情緒，非情緒本身）
- 9 月合併營收 3.59 億 TWD，月增 -3.1%，年增 -21.5%。
- 2026 年 1–9 月累計營收 33.97 億 TWD，年增 -5.9%。
- 2025 年全年歸屬母公司淨利年減約 24%，但仍為歷史第三高（時報資訊報導）。
- 管理層 4 月表示 Q2 起毛利率可望改善，並聚焦矽光子與 co-packaged optics。
- 本益比約 29.7，殖利率約 4.1%（Statementdog）。

## Net sentiment score
Composite: **neutral（信心：低）**。
- 基本面動能偏弱：9 月年增 -21.5%、YTD 年減 5.9%，與管理層「毛利率改善」的說法有落差。
- 分析師面：無當前數據，最近可查資料已過時，無法判斷。
- 零售面：無法取得 Reddit / StockTwits，論壇摘要為中性偏觀望。
- 內部人面：6 個月內無可查到的記錄，但資料不完整。

Divergence flag: **無法判定**。缺少 2026 年的分析師評等與零售貼文量化資料，無法檢驗零售與分析師是否背離。

## 資料缺口與後續
1. yfinance（fc.yahoo.com）與 Reddit、StockTwits 皆被政策阻擋（403 / 解析失敗），不建議重試。
2. 建議由人工補查：MOPS 內部人申報、券商 2026 年 10 月的評等與目標價（CMoney、MONEY LINK 法人資料）、PTT 股票板與 HiStock 論壇近 30 天貼文。

SENTIMENT REPORT COMPLETE
