# Sentiment — RKLB (Rocket Lab USA) as of 2026-11-09

資料時點截至 2026-11-08 盤後，未使用 2026-11-09 之後的資料。

資料來源狀態：
- yfinance（`pipeline/tools/yf`）可用，但 Yahoo cookie/crumb 取得失敗，資料可能為快取。`recommendations` 與 `rec_summary` 回傳完全相同，實質上只有一組來源。
- Reddit（r/wallstreetbets、r/stocks）直接抓取被擋（WebFetch 無法連線），無法取得原始貼文。
- StockTwits API 因 DNS 解析失敗無法連線（`api.stocktwits.com` 不在允許網域內），無法取得即時訊息流。
- 以下散戶資訊全部來自 WebSearch 的二手摘要，時效與可信度低，已標示。

## Analyst consensus

目前 22 位分析師：5 Strong Buy / 13 Buy / 4 Hold / 0 Sell / 0 Strong Sell。Buy 側 18 位（約 82%）。

近期趨勢（yf 快照，單位：位）：

| 期間 | Strong Buy | Buy | Hold | Sell | 覆蓋合計 | Buy 側占比 |
|---|---|---|---|---|---|---|
| 0m（目前） | 5 | 13 | 4 | 0 | 22 | 82% |
| -1m | 5 | 13 | 4 | 0 | 22 | 82% |
| -2m | 4 | 12 | 4 | 0 | 20 | 80% |
| -3m | 3 | 11 | 4 | 0 | 18 | 78% |

過去三個月覆蓋由 18 位增至 22 位，Buy 側由 14 位增至 18 位，Hold 持平，Sell 始終為 0。近一個月無評等變動。

近期動向（二手來源）：Cantor Fitzgerald 於 11/4 維持 Buy，目標價 $122（來源：tikr，約隱含 136% 上檔，對應當日股價約 $52）。未取得完整目標價分布，無法計算 consensus target。

注意衝突：一則 2026-10 的 MarketBeat 摘要稱共 22 位中有 1 位 Sell，與 yf 的 0 Sell 不一致。以 yf 為主，此差異未解決。

## Retail social

- **Reddit**：直接抓取失敗，無法取得樣本貼文與計數。二手來源（247wallst，2026-07-20）報導：股價於一個月內重挫逾 37% 期間，r/wallstreetbets 同時出現「低點抄底」與認賠的留言，文章引用的 Reddit 情緒分數由約 85（Iridium 收購案宣布前後高點）跌至 18–24（7 月中）。此為單一媒體轉述，未經原始資料驗證，且停在 7 月，不代表 11 月狀況。
- **StockTwits**：API 無法連線。二手彙整（stocktwits.com 文章，2026-07-14）記錄當時散戶情緒為 bearish；較早（2026 年 5 月）曾多次為 bullish 或 extremely bullish。Blog 站（blog.jingtea.com）宣稱 8/11 有 78% bullish，但無法對照原站，視為不可靠。
- **X / 其他**：AltIndex 的 X 提及情緒評分為中性（66/100），時點不明，僅供參考。
- **聲量**：無法量化提及數。二手來源顯示 2026 年 Q2 有明顯討論升溫（Q1 財報後、股價大漲期間），11 月的聲量數據未取得。

主要討論主題（依二手來源歸納）：
1. Neutron 首發延遲：多次被列為股價下修的主因，市場將其視為單一關鍵催化劑。
2. Iridium 收購案（二手來源，約 $54/股、約 $8B EV）：為 7 月股價劇烈波動的主要話題，散戶對其估值與資金壓力意見分歧。
3. 太空股與 AI 股連動拋售：11 月初下跌被歸因於板塊情緒，而非公司本身新聞（tikr，標題語「Absolute Slaughter」）。
4. 估值與獲利：散戶常提到公司仍未獲利、beta 約 2.9，波動大。
5. 11/9 為次要來源提及的 Neutron 相關待觀察日期，未能驗證是否有官方公告。

## Insider activity

6 個月窗口：2026-05-09 至 2026-11-08。

- 公開市場買入（Purchase）：0 筆、$0。
- 公開市場賣出（Sale）：合計約 $387.8M（約 0.39B USD）。
- 扣除 CEO Peter Beck 單筆 7/8 之 $286.4M，其餘賣出約 $101.4M。

依人員（賣出，單位：USD M）：

| 人員 | 職稱 | 賣出股數 | 賣出金額 |
|---|---|---|---|
| Peter Beck | CEO | 3,275,779 | 286.4 |
| Arjun Kampani | General Counsel | 224,260 | 28.2 |
| Adam Spice | CFO | 352,735 | 25.8 |
| Alexander Slusky | Director | 200,000 | 25.7 |
| Frank Klein | COO | 162,500 | 17.3 |
| Marvin Clevenger | Officer | 34,100 | 3.8 |
| Nina Armagno | Director | 10,926 | 0.6 |
| Agostino Ricupati | Officer | 669 | 0.05 |

重點觀察：
- **CEO Peter Beck**（7/8，$81.59–$101.57，3.28M 股，$286.4M）為窗口內最大單筆。5/26 另有一筆 5,000,000 股但無價格與金額欄位（性質待確認，可能為選擇權行使），需查 Form 4 確認。
- **CFO Adam Spice** 呈規律樣式：每約兩個月一次「選擇權行使（$1.09）+ 賣出」（9/2、11/2；另有 2026-01-05），可能為預排計畫（10b5-1），待查證。
- **Director Alexander Slusky** 於 5 月連續三次賣出（$115–$150），5 月共 200,000 股。
- **賣出價格走勢**：5 月約 $139–$150，8 月約 $66–$71，11 月初約 $51–$55，較 5 月高點跌幅逾 60%。多數賣出發生於財報後窗口期（3 月、5 月、8 月、11 月），與窗口期慣例一致。
- 另有非市場交易：多筆 Stock Gift（Slusky、Frank、Spice、Saintil）與 5/20、6/3 之獎勵授予，不計入買賣淨額。
- 內部人持股比例約 0.79%（yf），持股少，賣出對流通股影響有限，但方向性仍偏空。

## Ownership shifts

- 機構持股約 62.5%（流通股口徑 63.0%），機構數 1,462 家（yf 快照）。
- 內部人持股約 0.79%。
- 無歷史季度變化數據，無法判斷機構集中度趨勢。本次無法出具「增持或減持」結論，需下一輪補抓 13F 資料。

## Net sentiment score

| 受眾 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多（bullish） | 中高 | 18/22 Buy，0 Sell，覆蓋與 Buy 側三個月持續增加；目標價細節未取得 |
| 散戶（社群） | 偏空至中性（bearish-leaning / mixed） | 低 | 7 月 StockTwits 為 bearish，Reddit 情緒自高點大幅下滑；11 月資料缺失，僅有二手描述 |
| 內部人 | 偏空（bearish-leaning） | 中 | 6 個月內 0 筆公開買入、約 $387.8M 賣出；部分為規律計畫，賣出金額仍高於買入 |

綜合分數：**中性偏空（neutral-to-bearish）**，信心 **低至中**。分析師與內部人方向相反，散戶資料最弱，僅能作為輔助參考。

**背離旗標：是**。分析師 consensus 偏多，而內部人淨賣出與散戶 7 月後轉弱偏空，兩者方向相反。此背離具參考價值，但因散戶數據缺失，無法確認 11 月的散戶傾向是否與分析師持續背離。

資料缺口與待補項目：
1. Reddit 與 StockTwits 直連失敗，11/1–11/8 的散戶情緒、聲量與樣本貼文均未取得。
2. yfinance 之 Yahoo cookie/crumb 失敗，數據可能為快取，建議重跑確認。
3. 分析師目標價分布未取得。
4. 機構持股趨勢缺少歷史資料。
5. 5/26 之 5,000,000 股無價格交易，性質待確認。
6. Iridium 收購案與 Neutron 狀態僅見二手來源，需查一手公告（SEC 8-K、公司新聞稿）。

SENTIMENT REPORT COMPLETE
