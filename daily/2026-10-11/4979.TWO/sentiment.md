# Sentiment — 4979.TWO (華星光) as of 2026-10-11

> 資料說明：2026-10-11 為週日，市場資料以 2026-10-08 為準。Reddit、StockTwits 無法連線，X 無可用結果，散戶社群資料全部標示 DATA_UNAVAILABLE。yf 內部人交易回傳空陣列，視為 DATA_UNAVAILABLE。

## Analyst consensus
2 buy / 0 hold / 0 sell（strongBuy 1、buy 1；yf rec_summary，0m 與 -1m 期間相同）。
- 近期升降評（recommendations 歷史）：DATA_UNAVAILABLE。yf recommendations 回傳內容與 rec_summary 相同，無個別券商的評等變動紀錄。
- 目標價：DATA_UNAVAILABLE（可靠來源）。Investing.com 頁面顯示 12 個月平均目標價 475 元，但頁面未標註擷取日期，且其股價 340 元與其他來源明顯不符，僅供參考，不採信。
- 歷史評等（已過時）：2024-05 某券商「增加持股」目標價 210 元；2024-11 至 12 下調「降低持股」目標價 98 元；2025-06 報告仍維持 210 元。2024 至 2025 資料不代表目前看法。
- 覆蓋度薄：可見分析師僅 2 位，樣本過小，分布統計意義有限。

## Retail social
- Reddit（r/stocks、r/wallstreetbets）：DATA_UNAVAILABLE。連線遭拒（Claude Code 無法存取 www.reddit.com）。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（ENOTFOUND）。
- X / 新聞討論：WebSearch 無法找到 2026 年 10 月的英文社群討論；英文搜尋只回傳無關公司（LPTH、LITE）。
- 中文財經平台（CMoney 投資快訊）：可見多篇 2026 年股價上漲的快訊，標題語氣偏多，例如「光通訊市場回暖助推股價上漲」、「光通訊市場中的新星，股價漲幅達8.71%」。這些是自動生成的快訊摘要，不是散戶貼文，不計入散戶情緒量化。
- 提醒風險事件：一則 2026 年 7 月底新聞標題提到「爆今年第2度違約交割」，屬於搜尋摘要內容，未核實原文，列為待確認事項。
- 討論量（相對常態）：DATA_UNAVAILABLE。
- 主要主題（僅由中文快訊標題歸納）：光通訊 / 矽光子需求、股價突破、估值偏高的質疑。估值面：StatementDog 顯示本益比約 100 倍、股價淨值比約 18.8 倍，明顯高於產業平均（約 50.8 倍），屬於多方題材與估值風險並存。

## Price context（來自同日 market.md）
收盤 565 元（10/08），MA20 572.3、MA50 550.3、MA200 465.6，RSI14 49.0，MACD histogram -3.02。距 9/09 高點 658 回落約 14%，距 52 週高點 762（5/06）約 26%。股價仍在多頭排列，短線盤整。

## Insider activity
Net 6mo: DATA_UNAVAILABLE（yf insider 回傳空陣列）。
- 網路補充（Yahoo 股市內部人交易頁）：最近申報紀錄為 2025/03/03，申報人為誼虹科技股份有限公司（大股東，非董監個人），張數 500 張。2025 年 3 月之後無 2026 年申報紀錄，但搜尋結果無法證實是否真的沒有申報。
- 董監持股比例：0.01%（資料時間 2026/01/23，公司基本資料頁）。
- 注意：yf major_holders 的 insidersPercentHeld 為 12.0%，與台灣董監持股 0.01% 口徑不一致，推測 12% 包含大股東或定義不同，未確認。
- 買賣方向與職位（CEO/CFO）：DATA_UNAVAILABLE。

## Ownership shifts
- 內部人持股（yf）：12.0%
- 機構持股（yf）：23.7%（float 口徑 27.0%），機構家數 35
- 持股趨勢（季度變化）：DATA_UNAVAILABLE。yf 僅回傳當期快照，無歷史比較。inst_holders 未取得。

## Net sentiment score
Composite: **neutral（信心：低）**
- 分析師面：偏多但樣本極少（2 buy / 0 sell），且目標價數據不可靠，權重低。
- 散戶面：無可用直接數據，只能由中文快訊標題推斷偏多，權重低。
- 內部人面：無近期交易資料，無法判斷，且持股比例極低（0.01% 董監）。
- 估值與價格面：估值明顯偏高（PE 約 100 倍），股價距高點仍有回檔空間，技術面中性偏弱。

Divergence flag: **無法判定**。散戶資料缺失，無法與分析師傾向比較。若日後取得 Reddit 或 StockTwits 資料，優先確認散戶是否仍偏多而分析師樣本過少，這種落差需要留意。

## 待補資料
1. 2026 年券商個別評等與目標價（建議查 Anue 鉅亨、MoneyDJ 研究報告）。
2. 2026 年內部人申報轉讓紀錄（TPEx 公開資訊觀測站）。
3. 「違約交割」事件之原文與日期確認。
4. 散戶社群資料（Reddit、StockTwits 不可用時，改用 PTT 股版或 Dcard 股票版人工抽查）。

SENTIMENT REPORT COMPLETE
