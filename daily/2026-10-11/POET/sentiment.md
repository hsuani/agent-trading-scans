# Sentiment — POET as of 2026-10-11

## Analyst consensus
DATA_UNAVAILABLE（yf rec_summary 與 recommendations 回傳全部為 0，Yahoo cookie/crumb 連線失敗，視為無有效快取）。

WebSearch 補充（非 yf 來源，覆蓋面薄、彼此矛盾，僅供參考）：
- MarketBeat（2026-08-03）：平均評等 "sell"，目標價 $8.00；Weiss Ratings 重申 sell。
- StockAlarm：2 位分析師，Buy 共識，共識目標價 $5.75（低 $3.50、高 $8.00）；其列出的最近動作為 Northland 2025-12 目標 $8、Craig-Hallum 2024-09 目標 $3.50。
- Webull：Buy、平均目標 $5.83，但引用動作皆為 2024 年底，資料過時。
- 24/7 Wall St.（2026-08-12）：BUY、目標 $21.14，為模型估算（自述 50% 信心），非 sell-side 評等，屬離群值。

近期升降評等與目標價變動：DATA_UNAVAILABLE（yf 無資料；WebSearch 只找到上述零散且不一致的來源，無法確認 2026 年內的評等異動）。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。沙箱封鎖直接抓取，依任務規定未重試。改由 WebSearch 間接得知：曾有報導指 POET 在 WSB 24 小時內提及數與正面提及數居首，並與 call options 成交量集中有關，但報導日期不詳，無法確認是否為 2026-10 的狀態。
- StockTwits：DATA_UNAVAILABLE（直接抓取同樣被封鎖）。WebSearch 轉引一則報導：情緒曾由 bearish 翻為 bullish，訊息量單日增逾 58%，但同樣無法確認日期。
- X / 新聞鏈：
  - Seeking Alpha 評論形容情緒在興奮與失望間擺盪，作者仍在等待下一次回檔（日期不詳）。
  - 2026-05 多篇（多為轉載鏡像站）描述股價因獲利了結與商業化時程不確定而大跌。
  - Historical Option Data（2026-06-15）解讀選擇權流為偏多，但當日 put 成交額高於 call；該站為交易喊單站，可信度低。
  - 247wallst（2026-05-28）引述 Cramer 表示「不準備在此追價」，並提及 Reddit 族群看多。
  - 247wallst（2026-08-12 前後）描述股價約由 $7 衝至 $20 後大幅回吐。
  - 德文報導將一波漲勢歸因於 Reddit 交易者，無實質公司新聞。
- 量能：無 2026-10 的提及數快照，相對於典型水準無法定性。
- Themes（由零散來源歸納，時效不一）：
  - 光學中介層（optical interposer）與商業化時程是否兌現。
  - 短期爆量、事件驅動的追價行情，以及漲後的快速回吐。
  - 高隱含波動（有報導 30 日 IV 約 192%，來源品質低，僅供參考）。
  - 對現金部位與稀釋風險的疑慮（僅見於部分評論，來源不足以量化）。
- Tilt：無法在 2026-10 時點定論。過去數月的零散訊號為「爆發性偏多、回落後轉為懷疑」的循環。

## Insider activity
資料來源：yf insider（快取，最新一筆為 2026-08-19，2026-08-19 至 2026-10-11 之間無交易紀錄，需留意快取是否過期）。

6 個月窗口（2026-04-11 至 2026-10-11）：
- 公開市場賣出（Disposition，含 Value 欄位）：18 筆，合計約 $5.10M。
- 公開市場買入：0 筆（未見任何 open-market buy）。
- 淨額：約 -$5.10M（純賣方）。
- 期權行權（Exercise of options）另有多筆，多數與同日或隔日賣出配對，不視為買入信號，未計入淨額。

主要賣出者（依窗口內金額排序，職稱為 yf 欄位原文）：
- Barnes (Kevin)，Senior Officer：2026-05-20 合計約 $1.23M（@$14.22–14.69）；2026-06-05 約 $571K（@$11.25）；2026-08-10 約 $131K（@$8.93）。
- Jinyu (Mo)，Senior Officer：2026-06-05 約 $649K（@$10.82）；2026-06-03 約 $440K（@$14.65）。
- James (Lee)，Director or Senior Officer：2026-06-03 合計約 $495K；2026-06-01 約 $213K（@$14.17）；2026-06-12 約 $367K（@$14.68）。
- Mika (Thomas R)，Senior Officer：2026-08-07 約 $409K（@$8.93）。
- Kankipati (Venkata Rama Raju)，Senior Officer：2026-08-07 約 $208K（@$8.93）；2026-06-16 約 $81K（@$14.73）。
- Riley (Glen)，Director：2026-08-19 約 $103K（@$9.45）；2026-06-30 約 $47K（@$6.71）。
- Khan (Sohail A)，Director：2026-07-08 約 $58K（@$5.84）。
- Tirva、Ende（Director）：2026-06-30 各約 $42K–48K（@$6.71）。

觀察：
- 賣出價位橫跨 $5.84 至 $14.73，多數集中在 $14 區間（2026-05/06）與 $9 區間（2026-08），顯示高位分批了結。
- 2026-08 的賣出價約 $8.93–9.45，與 MarketBeat 報導的 2026-08-03 股價約 $6.97 相比為較高價位，無法確認當時精確股價，以 yf 成交價為準。
- Value 欄位為 null 的列（如 Venkatesan、Malinge 等）為持股或其他異動紀錄，無金額可計，未納入統計。
- 2025-10 有 Malinge、James 的行權後賣出，超出 6 個月窗口，未計入。
- CEO/CFO 身分：yf 只給 Position 原文，未明確標示職稱，DATA_UNAVAILABLE。

## Ownership shifts
- 內部人持股：0.068%（yf insidersPercentHeld）。
- 機構持股：20.48%，機構數 187（yf institutionsPercentHeld / institutionsCount）。
- 趨勢（季度增減）：DATA_UNAVAILABLE（yf 只回傳當前快照，無歷史序列）。

## Net sentiment score
Composite: **neutral 偏 bearish**（信心：低）

依據：
- 內部人：6 個月純賣出約 $5.1M、零買入，為主要偏空訊號，權重最高。
- 分析師：yf 無資料；WebSearch 來源顯示 sell 與 buy 並存，共識不可靠，偏中性。
- 散戶：過去有爆發性偏多，但 2026-10 的快照缺失，且多為事件驅動、短暫；無法作為當前方向依據。
- 整體資料缺口大（分析師、Reddit、StockTwits、季度持股趨勢皆無 2026-10 資料），因此信心低。

Divergence flag: **DATA_UNAVAILABLE**（無法判定）
- 若僅以可得資料比較：散戶過去有偏多爆發，內部人則持續賣出，兩者方向有潛在背離，但 2026-10 的散戶 tilt 未知，不宜作為正式 divergence 判定。
- 分析師 tilt 來源不一（MarketBeat sell vs StockAlarm buy），無法作為比較基準。

注意：本報告不含交易建議。資料缺口與快取時效問題需在使用前複核（yf 連線失敗、insider 快取最新僅到 2026-08-19）。

SENTIMENT REPORT COMPLETE
