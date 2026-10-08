# Sentiment — ZS as of 2026-10-09

> 資料時點注意：本次 DATE 為 2026-10-09，但系統當日為 2026-10-08；內部人交易最新一筆為 2026-09-25，分析師 rec_summary 為當前快照。實際資料截止於 2026-10-08。

## Analyst consensus
45 家覆蓋：6 strongBuy / 29 buy / 10 hold / 0 sell / 0 strongSell（Buy 類佔約 78%，Sell 為 0）。
近 3 個月趨勢（0m → -3m）：strongBuy 8 → 6，buy 30 → 29，hold 8 → 10。整體評等略往 hold 移動，但仍無任何 sell。
Recent moves：yf recommendations 工具僅回傳彙總計數，無個別升降評等的日期紀錄，無法列出具體 upgrade/downgrade 事件。
目標價：未從主數據源取得。次要網站（非官方，日期不一）提到 2026-09 平均目標約 $192.55，中位數約 $190；此為聚合站資料，僅供參考，未交叉驗證。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 的 search.json 皆無法存取（Claude Code 無法抓取 www.reddit.com），本節無直接樣本。以網路搜尋（WebSearch）查詢 Reddit 相關討論，也未找到 ZS 的近期 Reddit 討論串，無法判斷散戶論調與聲量。
- StockTwits：api.stocktwits.com 解析失敗（DNS ENOTFOUND），無法取得訊息流與多空標記。
- X / 新聞聲量：網路搜尋僅回傳聚合站與自動生成頁面，缺乏可信的近期文章。可辨識的敘事包括：2026 年初股價自 $224.92 回檔約 37%（至 $142.32）、後續反彈；9 月的檔案提及 short interest 偏高、競爭壓力，以及營收仍維持成長。這些屬於二手整理，非散戶原文。
- 聲量相對基準：無法量化。
- Retail tilt：無法判定（資料缺口）。
- Themes（由二手來源推得，信心低）：SaaS 估值壓縮、季度財報後的反應、空單比例、與競爭者（網路安全平台）的份額爭奪。

## Insider activity
過去 6 個月（2026-04-08 ~ 2026-10-08）公開市場交易：買入 0 筆 / $0；賣出 20 筆 / 約 $8.91M。
不計入：2026-09-15 的股票獎勵（RUBIN $0 與 GELLER $0 之 grant）、2026-09-15 前的 gift 與 option conversion。

依人員彙總的賣出金額（6 個月）：
- GELLER ADAM（Officer）：約 $2.68M
- RUBIN KEVIN E（CFO）：約 $2.00M
- SCHLOSSMAN ROBERT S（Officer）：約 $1.94M
- RICH MICHAEL J（Officer）：約 $1.32M
- CHAUDHRY JAGTAR SINGH（CEO）：約 $0.91M
- BEER JAMES ALEXANDER（Director）：約 $0.06M

Notable：
- CEO Chaudhry 於 2026-09-16 賣出 2,852 股（約 $550K，$192.76），2026-06-16 另賣 2,878 股（約 $364K）。
- CFO Rubin 於 2026-09-16 賣出 5,957 股（約 $1.15M），2026-09-25 再賣 519 股；另有 2026-07-27、08-25 各約 503 股的小額固定頻率賣出，形態可能屬 10b5-1 計畫，但資料中未確認。
- 2026-09-17 GELLER ADAM 賣出 10,162 股（約 $1.96M，$192.01–192.76），為期間最大單筆。
- 賣出價格區間：2026 年 3 月約 $153–157，6 月約 $122–127，9 月約 $192–200。賣出集中在股價反彈後，與 2025 年 12 月（約 $230）與 2025 年 6–9 月（約 $280–308）的情況相似，大量賣出似與交易窗口開放有關，尚未確認。
- 2025 年 10 月以來沒有任何公開市場買入紀錄（過去 12 個月僅見 grant 與賣出）。

## Ownership shifts
- 內部人持股約 34.7%（數字偏高，可能含創辦人等大股東，需確認）。
- 機構持股約 53.2%（占總股本），占流通股約 81.5%，機構數 1,142 家。
- 只有單一快照，無法判斷機構加減碼趨勢。

## Net sentiment score
Composite：**neutral（信心：低）**
- 分析師面：偏多。45 家中約 78% 為 buy 類，無 sell，但近 3 個月 strongBuy 略減、hold 略增，動能微降。
- 內部人面：偏空。6 個月 $8.9M 賣出、0 買入；不過高管在股價回升時賣出屬常見現象，其訊號強度有限，且無法排除計畫性交易。
- 散戶面：無資料，無法評估。
- 綜合：分析師偏多與內部人持續賣出相互抵消，整體中性。資料缺口（Reddit、StockTwits 皆無法取得）大幅降低結論的信心。

Divergence flag：**無法判定（散戶資料缺）**。
另有一項分析師與內部人之間的分歧：分析師評等偏多，但內部人在 6 個月內只賣不買，兩者方向相反，值得後續追蹤。

## 資料缺口與後續建議
1. Reddit（wallstreetbets、stocks）與 StockTwits 皆無法存取，散戶 tilt、聲量與樣本引述均缺。可於 Reddit 與 StockTwits 可用時重跑。
2. yf recommendations 未提供個別評等變動日期，無法列出 upgrade/downgrade；需改用其他來源（如 MarketBeat、券商研究彙整）確認近期動作。
3. 內部人交易的 10b5-1 性質需從 SEC Form 4 附註確認。

SENTIMENT REPORT COMPLETE
