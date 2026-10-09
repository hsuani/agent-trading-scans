# Sentiment — IRM as of 2026-10-10

## Analyst consensus
11 buy（含 4 strongBuy）/ 0 hold / 1 sell（共 12 家，yf rec_summary 當期快照）。與約 3 個月前相比（10 buy / 0 hold / 1 sell），買方家數增加 1 家，賣方家數不變。

近期動態（WebSearch 補充，來源彼此有出入）:
- 2026-09-21：Rothschild & Co Redburn 首次覆蓋，Buy，目標價 $132。
- 2026-08-27：Truist 目標價由 $140 上調至 $155，維持 Buy。
- 2026-08-06：Wells Fargo 目標價由 $135 上調至 $140。
- 2026-05-01：JPMorgan 維持 Overweight，目標價由 $121 上調至 $138。
- RBC（Jonathan Atkin）維持 Buy，目標價 $147（日期未明）。
- 未找到 2026 年 9 月或 10 月的明確降評（downgrade）紀錄。yf recommendations 只提供彙總計數，無個別評等變動明細。

目標價共識（各來源不一致）:
- Bullstory（2026-09-17）：均值 $146.20，區間 $140–$155。
- Barchart（較晚一版）：均值 $134，Street high $153。
- Yahoo 快照（日期未明）：均值 $127.55，high $149，low $44（low 疑為離群值或舊資料）。
- 結論：目標價均值約 $127–$146，取決於來源與日期，無單一可信的 10 月快照。

價格參照：Trade-Ideas 頁面顯示 2026-10-04 收盤 $113.39，9 月份各來源報價約 $112–$117。Yahoo 快照的 $127.19 與此不一致，應視為較舊資料。以 $113 計，均值 $134 約有 18% 上行空間，均值 $146 約有 29%。

## Retail social
- Reddit：DATA_UNAVAILABLE。WebFetch 對 reddit.com 回報無法存取，r/stocks 與 r/wallstreetbets 皆未取得 IRM 貼文。WebSearch 也找不到 2026 年 10 月的 IRM 相關 Reddit 討論。
- StockTwits / X：StockTwits API 無法連線（DNS 解析失敗，soft-fail）。WebSearch 找到的 StockTwits 頁面有 "Bullish" 情緒分數 61，但頁面未標示日期，且其價格資料與 2026 年 10 月不符，僅供參考。SentiSense 給予 "strong bullish" 評分 100，但頁面日期為 2026-06-25。
- 聲量（buzz volume）：DATA_UNAVAILABLE，無法取得提及次數與基準比較。
- 空方部位：Trade-Ideas 頁面（2026-10-04）顯示約 3% 的 IRM 投資人站在空方。這是單一來源的數字，未經交叉驗證。
- 散戶傾向：偏多，但證據薄弱。主要依據為 StockTwits 與 SentiSense 的情緒分數，二者日期或價格基準皆有問題。

Themes（來源：WebSearch 所見的外部觀點）:
- 估值偏貴：Seeking Alpha 文章 "Iron Mountain: Deserves A Downgrade, Overly Expensive Here" 認為估值溢價不合理（日期未明）。
- 槓桿與負債：同一文章與其他來源提及負債依賴度上升的疑慮。
- 利率敏感：REIT 性質使股價對利率預期敏感，May 2026 的自動生成文章提及此風險。
- 股價年初至今漲幅約 37%（Trade-Ideas，2026-10-04），歷史高點 $134.68。

## Insider activity
Net 6mo（2026-04-10 至 2026-10-10）：$0 買入（公開市場買進）/ 約 $35.5M 賣出（不含選擇權行權與股票獎勵）。

- 賣出明細（依 yf insider 資料加總）：
  - CEO William L. Meaney：約 $27.9M，多為每月 1 日或約每月的分批賣出（2026-05 至 2026-10，共 6 筆大額），每次同時伴隨以 $37.00 行權的選擇權轉換（每次約 38,474 股）。
  - Mark Kidd（Officer）：約 $3.7M，每月約 6,000 股。
  - Greg W. McIntosh（Officer）：約 $2.6M（含 2026-08-06 的 11,839 股一筆）。
  - Daniel Borges（Officer）：約 $0.9M（2026-05-21）。
  - Pamela M. Arway（Director）：約 $0.24M（2026-05-12）。
  - Walter C. Rakowich（Director）：約 $0.09M（2026-05-20）。
- 獎勵股（Stock Award）：2026-05-07 九位董事各取得 1,892 股，屬於年度董事薪酬，不計入買入。
- 贈與（Gift）：Rakowich 2026-05-01 贈與 1,600 股，不計入。
- 最近一筆非獎勵買進：Christie Barton Kelly（Director）2025-11-19 買進 33 股（$2,954），已超出 6 個月窗口。

解讀：CEO 的賣出高度規律且與 $37 選擇權行權綁定，較像預先排定的交易計畫（10b5-1）的特徵，但 yf 資料未標示計畫性質，此判斷未經證實。6 個月內無任何公開市場買進，只有賣出。賣出價格區間約 $109–$130，與近期股價相符。

## Ownership shifts
- 機構持股比例：88.28%（institutionsPercentHeld）；流通股口徑 89.06%。
- 機構家數：1,576。
- 內部人持股：0.88%。
- 趨勢：yf major_holders 僅提供單一時點快照，無歷史比較。機構持股變化趨勢：DATA_UNAVAILABLE。

## Net sentiment score
Composite: **偏多但信心低（bullish-leaning, low confidence）**。

- 分析師面：偏多（Buy 佔比約 92%，近期多次目標價上調，唯目標價各來源差異大）。
- 內部人面：偏空或中性（6 個月內無買進，CEO 與多位高層持續賣出，但高度規律，可能為計畫性賣出）。
- 散戶面：偏多但證據不足（StockTwits 與 SentiSense 日期與價格基準有問題，Reddit 與 StockTwits API 無法存取）。
- 信心低的主因：社群資料缺口大，目標價來源差異大，內部人賣出是否為計畫性交易未能驗證。

Divergence flag: **否（無明顯背離）**。分析師與散戶的資料皆偏多，內部人賣出為主要的反向訊號，但其性質（可能為計畫性出售）使其解讀存疑。若後續取得 Reddit 或 StockTwits 的實際當期資料，應重新檢視散戶面。

資料限制摘要：
- Reddit、StockTwits API：無法存取（soft-fail）。
- 聲量與機構持股趨勢：DATA_UNAVAILABLE。
- Yahoo cookie/crumb 取得失敗，yf 資料仍可使用但未附帶 crumb。

SENTIMENT REPORT COMPLETE
