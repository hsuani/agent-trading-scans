# Sentiment — ANET as of 2026-11-11

## Analyst consensus
29 家: 29 buy（8 Strong Buy + 21 Buy）/ 0 hold / 0 sell（yf rec_summary，0m 期）。
過去三個月趨勢: -1m 與 -2m 為 32 家（7 SB + 24 B + 1 hold）；-3m 為 31 家（8 SB + 23 B）。覆蓋家數略減 2–3 家，評等分布無實質改變，hold 在 -1m 後歸零。
近期評等變動: yf `recommendations` 只回傳月度彙總，沒有逐筆升降評等（upgrade/downgrade）紀錄，無法確認個別券商動作日期。
網路資料點（日期不明，不可直接採信）: Citi 維持 Buy，目標價由 $173 上調至 $215（文中稱 8/7）；Seeking Alpha 有一篇降評文章，主旨為估值過高（約 40x EV/EBITDA、約 39x forward P/E）。
目標價: WebSearch 引用的 Barchart 平均目標價 $179.91 早於 Q2 2026 後的上漲，可能已過時，僅供參考。
資料來源差異: WebSearch 引用的 Barchart 數字為 26 家（22 SB / 3 MB / 1 hold），與 yf 的 29 家（0 hold）不同，本報告以 yf 為主。

## Retail social
- Reddit: 未取得。r/wallstreetbets 與 r/stocks 的 JSON 端點被工具拒絕存取（WebFetch 回報無法從 www.reddit.com 取得），本節無法提供 thread 樣本與多空比例。
- StockTwits / X: StockTwits 無法解析 api.stocktwits.com（DNS 失敗，需於 session 網路設定中允許該網域），略過。X 無直接資料，僅以 WebSearch 結果代替，搜尋結果多為既有文章，未見 2026-11 當月貼文。
- 聲量: 無法量化（無 Reddit / StockTwits 計數），定性判斷為資料不足，無法與歷史基準比較。
- 網路文章的標題語氣（僅供參考，非散戶貼文）: 「is arista networks stock a buy after selloff」，屬於「回檔是否為買點」的討論。
- 多空傾向: 無法直接判定散戶傾向。網路文章偏多（AI 網路需求、Needham 等認為處於「generational investment cycle」），但同時反覆出現估值偏高的疑慮。
- Themes（由文章歸納，非散戶原文）:
  1. AI 資料中心網路需求與成長前景（偏多）。
  2. 估值溢價（40x EV/EBITDA、39x forward P/E）是否已反映於股價（偏空 / 保留）。
  3. 近期回檔約 15%（AskTraders 所述，時間點不確定）後，是否屬於買點（分歧）。

## Price context（由內部人成交價推估，非即時報價）
2026-10-09 成交價約 $217；2026-11-02 約 $164–169；2026-11-05 約 $159–171。10 月初至 11 月初股價約下跌 25%。實際最新報價需另行查證。

## Insider activity
期間: 2026-05-11 至 2026-11-11（6 個月）。
Net 6mo: **$0.00B 買入 / $1.25B 賣出**（淨賣出約 $1.25B，無公開市場買入紀錄）。
| 人員 | 職稱 | 6mo 賣出（USD B） | 備註 |
|---|---|---|---|
| ANDREAS V. BECHTOLSHEIM | >10% 實質持有人 | 0.63 | 2026-05 至 11-05 多次賣出，最近一筆 11-05 約 26 萬股 |
| JAYSHREE ULLAL | CEO | 0.58 | 2026-08-05 約 110 萬股、2026-10-06 與 10-09 合計約 62 萬股，為主要賣方 |
| KENNETH DUDA | President（2025-12 曾列 CEO） | 0.03 | 每月定期賣出並同時行使選擇權，樣式規律 |
| MARK TEMPLETON / CHARLES GIANCARLO | Director | 0.01 / 0.00 | 小額、規律賣出（各約 5,000–8,000 股/次） |
| CHANTELLE BREITHAUPT | CFO | <0.01 | 小額賣出 |
| 其他獨立董事 | Director | <0.01 | 小額 |

Notable: CEO Ullal 與 >10% 持有人 Bechtolsheim 合計占 6mo 賣出 97%以上。
資料說明: 部分批次列（2025-11-20、2026-02-20、2026-05-20、2026-08-20）無金額，屬於非現金配發或授予，已排除於計算之外。無法從資料判斷各筆是否屬於 10b5-1 計畫，此點需另行確認。
資料單位: USD，以 B 表示；本報告無 TWD / KRW 金額。

## Ownership shifts
- 內部人持股 17.2%，機構持股 73.3%（流通股中機構占 88.5%），機構家數 3,256。
- 僅有單一時點快照，無法判斷機構持股的季度趨勢（增持 / 減持）。

## Net sentiment score
- 分析師面: **偏多**（29/29 買進，無 hold / sell，但估值爭議存在）。
- 內部人面: **偏空**（6mo 約 $1.25B 賣出，無買入；CEO 與大股東為主要賣方）。
- 散戶面: **無法判定**（Reddit / StockTwits 無資料，網路文章為正反混合）。
- 綜合: **中性**，信心度 **低**。分析師一面倒看多，與內部人大額賣出形成對照；兩者同時存在時，訊號相互抵消，無法得出明確方向。

Divergence flag: **是**。分析師（全部買進）與內部人（淨賣出）方向相反。散戶傾向因資料缺失無法比較，因此無法確認是否也屬於相反方向。
資料缺口: Reddit、StockTwits 無資料；ownership 無歷史趨勢；analyst 逐筆升降評等無資料；目標價與股價需以即時報價更新。

SENTIMENT REPORT COMPLETE
