# Sentiment — 1815.TWO (富喬) as of 2026-11-20

資料可得性很低，結論信心偏低。

## Analyst consensus
yf rec_summary 與 recommendations 皆回傳 0 buy / 0 hold / 0 sell，無歷史評等變動。Yahoo cookie/crumb 取得失敗，因此這個「零」可能是資料缺漏，不一定代表真的沒有券商覆蓋。

網路搜尋找到的是媒體或投研單位的觀點，不是正式券商評等：
- 理周投研部：中長線目標價 135 元，理由是 800G 交換器與 AI 伺服器對 Low Dk/Df 材料需求強，認為營運進入「超級週期」。文中提到 2025 年 EPS 1.64 元，較前一年增逾 11 倍。
- UDN 報導標題提到 9 月瞄準 141.5 元，但未取得內文，無法確認來源與評等。
- StatementDog 頁面顯示 10/21 收盤價 147 元。若年份為 2026，目標價 135 元低於此價位。年份未經確認。
- 近期 revenue/EPS 上修：2026 年上半年營收約 40.13 億 NT$，年增 43%，毛利率 38.1%，今年 EPS 估 5 元、明年再增 40% 以上（未註明預估機構）。

Recent moves: 無正式升降評等紀錄，無法判斷近期目標價調整方向。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): 無法取得，WebFetch 被拒（無法連線 www.reddit.com）。無樣本、無 tilt。
- StockTwits: 無法取得，api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許此網域。
- X / 新聞討論: 網路搜尋未找到 11 月的散戶討論。已知的 8 月研究摘要提到外資連續買超，以及 AI 伺服器高階布料需求受市場關注。
- Buzz 量: 無法量化，無資料。
- Themes（從媒體與研究文字推得，非散戶原文）: AI 伺服器與 800G 交換器帶動 Low Dk 材料；E-glass 轉型至 M9 石英布；低軌衛星、高速交換器等新應用；玻纖紗與玻纖布垂直整合。

## Insider activity
yf insider 回傳空陣列，無 6 個月內申報交易紀錄。此為 Yahoo 抓取失敗後的結果，不能視為確定無交易。
- 內部人持股約 23.9%（yf major_holders），屬高集中度，代表大股東結構穩定，但不代表近期買賣方向。
- 另有 2026 年 6 月董事會通過註銷員工限制型股票，資本減少約 3.5 千萬 NT$（約 0.35 億 NT$），屬於股本調整，不是市場買賣。

Net 6mo: 無資料（$0 buys / $0 sells 僅代表工具無回傳）。

## Ownership shifts
- 機構持股約 10.4%（institutionsCount 23 家），浮動股權中機構占約 13.6%。
- 無歷史時間序列，無法判斷機構集中度趨勢。

## Net sentiment score
Composite: **neutral（信心低）**。
- 分析師面：無正式覆蓋；僅有的媒體目標價（135 至 141.5 元）與基本面成長敘事偏多，但未確認日期與來源。
- 散戶面：無資料。
- 內部人面：無資料。
- 資料缺口大，綜合評分只能視為「基本面敘事偏多、市場情緒未知」。

Divergence flag: **無法判斷**。缺乏散戶資料，無法比較散戶與分析師方向。

## 資料來源與缺漏摘要
- 失敗：Reddit 兩個 subreddit（拒絕）、StockTwits（DNS 失敗）、yf 的 recommendations / rec_summary / insider（Yahoo cookie/crumb 失敗，回傳空或零）。
- 成功：yf major_holders（持股結構）、網路搜尋（媒體與研究文字）。
- 建議補抓：Reddit 與 StockTwits 網域放行後重跑；另查 MoneyDJ 或 Goodinfo 券商目標價頁，確認 135 與 141.5 元目標價的日期與券商。

SENTIMENT REPORT COMPLETE
