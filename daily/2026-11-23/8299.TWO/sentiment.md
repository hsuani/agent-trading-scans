# Sentiment — 8299.TWO (群聯 Phison Electronics) as of 2026-11-23

資料狀態說明：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 無法連線，散戶社群面無有效樣本；PTT/Dcard 搜尋未找到 2026 年 11 月的討論串。本報告的「散戶」結論全部缺證據，不應被解讀為散戶偏多或偏空。

## Analyst consensus

依 yfinance rec_summary（0m 期，共 13 家）：4 strongBuy + 7 buy = 買進 11 家，hold 0 家，sell 2 家（strongSell 0）。
過去三期（-1m 至 -3m）為 11 買 / 1 hold / 1 sell，故最新一期 hold 歸零、sell 增至 2。

| 券商 / 來源 | 評等 | 目標價（TWD） | 日期 / 備註 |
|---|---|---|---|
| 外資（未具名） | 減碼 | 2,588 → 1,357（-48%） | 2026 年 11 月；承認先前估值模型計算錯誤 |
| 統一投顧 | 買進 → 中立 | 未取得 | 2026 年 11 月；理由為 PC 市場疲弱、2027 下半年 NAND 可能供過於求 |
| 凱基投顧 | 增加持股（維持） | 2,900 → 2,700 | 2026 年 11 月；看好 eSSD 高附加價值 |
| 永豐投顧 | 買進（維持） | 2,998 → 2,070 | 2026 年 11 月；NAND 供給仍緊 |
| CLSA | 買進 | 2,600 → 3,000 | 日期格式不明（可能 2026-05-11 或 2026-11-05） |

Recent moves：目標價修訂以下修為主（已知 3 筆下修、1 筆上修且日期不明）。yfinance 的 hold 為 0，與統一投顧降為中立的新聞不符，顯示 yfinance 對台灣券商覆蓋不完整或有延遲，評等計數應視為下限參考。聚合網站的共識目標價互相矛盾（約 2,356 至 2,977 TWD），不採用。

股價參考：2026-11-09 公告 Q3 財報與庫藏股後，股價一度漲停至 1,650 TWD（statementdog 報導）。11/23 的收盤價未取得。外資目標價 1,357 低於該參考價，屬明確偏空。

## Retail social

- Reddit：WebFetch 無法存取 www.reddit.com，無樣本，tilt 不明。
- StockTwits：api.stocktwits.com DNS 解析失敗（需於 session 網路設定允許該主機），無樣本。
- PTT / Dcard / X：搜尋只找到 2025 年 12 月的 PTT 轉述（當時多為看多留言，但也有酸言），非近期資料。2026 年 11 月的 X 與論壇聲量無法量化。
- 聲量：無法與基準比較，標為「未知」。

Themes（取自新聞與媒體轉述，非散戶原文，僅供參考）：
- 業績與回購：Q3 EPS 138 元創高、董事會通過買回 2,000 張（約 200 萬股，預算 45.6 億 TWD）。
- 核心爭議：公司認為缺貨延續多年；研調機構預估 2027 年 NAND 反轉。
- 毛利率回落：Q3 毛利率 59.7%（前一季約 65.3%），外資認為低於預期 60.3%；低價庫存將於下半年消化。
- 庫存風險：存貨約 1,110 億 TWD、週轉天數近 300 天，反轉時跌價與毛利率壓力會同時出現。

## Insider activity

yfinance insider 回傳空陣列，無法判定近 6 個月董監或經理人買賣。此為資料缺漏，不代表無交易。需至 MOPS 董監事持股異動查詢確認。
唯一可確認的資金面訊號是公司層級回購（2,000 張），屬公司行為，不計入內部人買賣。除息基準日為 11/17（來源：Goodinfo 頁面）。

Net 6mo: 數據不足，無法計算 $ buys / $ sells。

## Ownership shifts

yfinance major_holders 快照（僅單期，無趨勢）：
- 內部人持股 15.85%
- 機構持股 20.75%（佔流通股 24.66%）
- 持有機構數 183 家

機構集中度趨勢無法判定。

## Unit check（億 / B 一致性）

- Q3 合併營收 860.76 億 TWD；10 月單月營收 315.30 億 TWD（累計前 10 月 2,264.62 億 TWD）。
- 數字衝突：新聞標題「Q3 狂賺 305 億」與「EPS 138 元」無法同時成立。以公司流通股數約 2,330 萬股（依資本額推算，未經工具驗證）反推，EPS 138 對應淨利約 32 億 TWD（138 × 2,330 萬）；305 億則對應 EPS 約 1,309。兩者相差 10 倍，且 305 億 / 營收 860.76 億 約 35% 淨利率，與 EPS 推得的約 0.4% 淨利率矛盾。此數字需於 MOPS 財報核對，本報告不採用 305 億，也不以其做估值判斷。
- 以 1,650 TWD × 約 2,330 萬股 推算市值約 384 億 TWD（股數為推算值）。

## Net sentiment score

Composite：**neutral（信心：低）**，略偏空於目標價修訂動能。
- 分析師面：評等計數仍偏多（11/13 買進），但最近的修訂方向為下修，外資評等降至減碼，統一降至中立。
- 散戶面：無有效資料，不計分。
- 新聞面：基本面強與估值、毛利率回落、2027 景氣爭議並存，多空對立。

Divergence flag：**無法判定**。散戶 tilt 缺資料，無法檢驗是否與分析師方向相反。若日後取得 PTT / Reddit / StockTwits 樣本，優先檢查散戶是否仍偏多而分析師下修，此組合通常具參考價值。

## Data gaps（供上游參考）
1. Reddit、StockTwits 不可用（網路限制）。
2. PTT/Dcard 2026 年 11 月樣本缺失。
3. 內部人交易需以 MOPS 補查。
4. Q3 EPS 與淨利數字衝突，需核對財報原文。
5. 11/23 股價與盤中情緒未取得。

Sources（新聞轉述）：
- [統計狗：群聯 Q3 EPS 138 元與庫藏股](https://statementdog.com/news/18015)
- [TechNews：群聯 2026 年 10 月營收](https://finance.technews.tw/2026/11/06/phison-8299-202610-financial-report/)
- [中時旺得富（2026-11-11）](https://wantrich.chinatimes.com/news/20261111900103-420101)
- [Investing.com 共識頁（CLSA 目標價）](https://au.investing.com/equities/phison-electronics-consensus-estimates)

SENTIMENT REPORT COMPLETE
