# Sentiment — ALB as of 2026-10-30

> 資料時點注意：本報告的 as-of 日期為 2026-10-30，但執行當日為 2026-10-29。yfinance 資料為執行當下快照。Reddit 與 StockTwits 無法取得，零售情緒部分為缺口。

## Analyst consensus
23 位分析師（yfinance 0m）：2 strong buy / 12 buy / 9 hold / 0 sell / 0 strong sell，即 14 buy、9 hold、0 sell。
近三個月趨勢：
- -1m：13 buy（3 strong buy + 10 buy）、9 hold、0 sell
- -3m：13 buy、9 hold、0 sell
- 本月評級由 strong buy 轉為一般 buy 的比例增加，整體買方家數 13 → 14，無賣方評級。

近期評等與目標價變動（來自次級來源 WebSearch，日期與數字在來源間不一致，需以 live 資料核對）：
- Citigroup：neutral 升 buy，目標價 $225（6/18）
- Vertical Research：hold 升 buy，目標價 $224（5/26）
- Truist：目標價由 $260 下調至 $245（7/20）
- Scotiabank：目標價由 $215 下調至 $200（7/28）
- Mizuho：目標價下調至 $185（6–7 月）
- Zacks Research：strong-buy 降為 hold（7/20）
- Weiss：維持 sell（8/4）
- 一則德文來源提及有分析師由 buy 降為 neutral，理由為 2027 年起的鋰供給過剩；日期不明。

目標價共識分歧大：Benzinga 快照 $181（19 位分析師，12 buy / 6 hold / 1 sell）；MarketBeat $199.22（Moderate Buy）；Walnut（8 月）$187.16。以上皆早於 9 月，未能取得 10 月後的評等異動。

## Retail social
- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 JSON 端點回傳無法存取（WebFetch 錯誤），本次未取得樣本貼文與情緒傾向。
- StockTwits / X：StockTwits API 因網路白名單限制無法解析（api.stocktwits.com 未開放），需於 session 網路設定中允許後才能重試。X / 新聞搜尋未找到可引用的零售討論貼文，只找到鏡像站與自動生成內容，可信度低。
- 零售聲量（定性）：無法量化，無法與平常基準比較，標註為資料缺口。
- 零售傾向：無法判定（bullish / bearish / mixed 皆無足夠樣本）。
- 主要主題（僅由新聞與分析師文字歸納，非零售貼文）：
  - 鋰價是否穩定，以及 2027 年後供給過剩的疑慮
  - EV 需求能否支撐鋰價反彈
  - 股價區間震盪，對鋰價與同業（如鋰相關股）連動性高
  - 下一次財報 11/4（次級來源），市場關注 Q1 之後的獲利與展望

## Insider activity
追蹤期間：2026-04-29 至 2026-10-29（6 個月）。
淨額 6mo：買入 $0M，賣出 $3.01M（約 16,393 股，單價 $183.12–$184.52，交易日 2026-05-15）。
- 唯一公開市場交易：CEO Jerry Kent Masters Jr.，5/15 賣出 16,393 股，約 $3.01M。
- 其餘為董事與高階主管的股票授予（Stock Award，單價 0），包含 9/14 的 COO、Officer 等，屬例行薪酬，不計入買賣淨額。
- 3 月 CEO 另有 30,716 股贈與（3/12，約 $5.00M）與 3/10 賣出 11,783 股（約 $2.01M），均在 6 個月窗口之外，僅作背景參考。
- 過去 6 個月內無高階主管或董事公開市場買入。

## Ownership shifts
- 內部人持股 0.21%（yfinance insidersPercentHeld）。
- 機構持股 101.8%，明顯超過 100%，屬資料異常（可能為流通股數或重複計算），不應直接解讀為集中度。
- 機構家數 1,283 家。本次僅有單一快照，無法判定季度趨勢。

## Net sentiment score
Composite：**中性偏多（信心度：低）**
- 分析師面：偏多（14 buy / 9 hold / 0 sell，無賣方評級，但目標價近期多數遭下調）。
- 內部人面：中性偏空（6 個月內僅 CEO 一筆 $3.01M 賣出，無買入）。
- 零售面：無資料。
- 信心度低的原因：零售樣本完全缺失，媒體與次級來源的日期與價格互相矛盾，且機構持股數據異常。

Divergence flag：**無法判定**。分析師偏多，但零售傾向缺失，無法與分析師比較。若之後取得 Reddit / StockTwits 資料，應再檢查零售是否與分析師方向相反。

SENTIMENT REPORT COMPLETE
