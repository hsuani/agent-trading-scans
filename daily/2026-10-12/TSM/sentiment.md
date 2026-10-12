# Sentiment — TSM as of 2026-10-12

## Analyst consensus
21 家分析師：6 strongBuy / 14 buy / 1 hold / 0 sell（rec_summary 當期，與 recommendations 最新一筆一致）。Buy 系（含 strongBuy）佔 20/21，約 95%。

評級分布走勢（yf recommendations，近四個月）：

| 期間 | strongBuy | buy | hold | sell |
|---|---|---|---|---|
| 當期 (0m) | 6 | 14 | 1 | 0 |
| -1m | 6 | 14 | 1 | 0 |
| -2m | 6 | 12 | 1 | 0 |
| -3m | 6 | 12 | 1 | 0 |

評級結構近四個月沒有降級跡象，Buy 家數由 12 增至 14。yf 工具只回傳彙總計數，沒有個別升降評等明細，因此無法列出具體 upgrade / downgrade 事件。

目標價（WebSearch 取得，來源品質參差，均非官方數據）：
- Needham：目標價上調至 $530，維持 Buy（約 2026-07 底，Benzinga 轉述）。
- Stifel：首次覆蓋，Buy，目標價 $515（2026-09-02）。
- Barclays：目標價 $355，Overweight。此為 2025 年舊數據，已過時，不採用。
- 共識目標價各來源不一：TradersUnion（2026-07）平均 $490；Walnut Invest（資料約 2026-08）平均 $540，中位數 $534.5，區間 $430–$700，18 buy / 1 hold / 0 sell。
- 股價參考：MarketBeat 2026-10-06 收於 $482.61；AltIndex 2026-09-13 為 $433.24；Alphasquare 2026-07-24 為 $403.41。各來源時點不同，當前價位需以即時報價確認。

## Retail social
- Reddit：本次 WebFetch 對 r/wallstreetbets 與 r/stocks 的 search.json 被擋（依任務規定改用 WebSearch）。WebSearch 找不到 2026-10 的 WSB 或 r/stocks 討論串，只找到 2024 年的 WSB 舊文（比較 TSMC 與 NVDA、SMCI、ASML、INTC，論點為良率、全球布局、對中國地緣風險較低；留言反駁其「西方公司」定位，強調台灣國防角色）。**近期 Reddit 樣本：無資料。**
- StockTwits：api.stocktwits.com 依規定視為受限，未取得資料。**無資料。**
- X / 論壇：TradingView 社群討論串指出 TSMC 三率齊升且指引強，但股價盤整未突破（日期不明）。TipRanks 轉載於 Naga 的情緒分數標示為 POSITIVE，但頁面無日期。
- 聲量（buzz volume）：無法量化，缺乏可比的提及次數基準，不做高低判斷。
- 主要主題（僅依有限的 WebSearch 摘要）：
  1. AI / HPC 資本支出：MarketBeat 轉述 TSMC 2026 資本支出上修至最高 $64B，市場視為 AI 需求的正面訊號。
  2. 成長速度相對性：看空論點為 TSM 成長不如部分 AI 相關股，屬於估值與相對強弱的討論。
  3. 地緣政治：舊有討論中的主要風險因子，本期無新資料。
- 零售傾向：**無法判定**（樣本不足，僅有零星正面的聚合分數）。

## Insider activity
資料來源為 yf insider。注意：TSM 為外國私人發行人（20-F 申報），通常不適用美國 Form 4 規定，此資料的完整性與口徑需自行確認。

過去 6 個月（2026-04-12 至 2026-10-12）：
- 買入：約 $24,378（4 筆，合計 42 股）
- 賣出：$0

明細：
- TIEN BOR-ZEN（職位標示 Officer）：2026-04-28 買入 20 股，約 $7,760（$386–390）；2026-05-20 買入 17 股，約 $6,718（$391.81–400）；2026-07-20 買入 10 股，約 $4,050（$405）；2026-07-28 買入 15 股，約 $5,850（$390）。

6 個月以外（僅供參考）：
- BURNS URSULA M（Director）：2026-03-31 買入 1,000 股，約 $322,050（$322.05）。

與 MarketBeat 轉述一致的「兩位副總裁小額買進」訊號，金額不大，但方向一致。內部人無賣出紀錄。

## Ownership shifts
- 機構持股：15.49%（機構數 4,658 家）。
- 內部人持股：0.013%。
- 機構持股趨勢：yf major_holders 只有單一時點快照，無法判斷 13F 集中度的變化方向，此項標示為**無法判定**。

## Net sentiment score
Composite：**bullish（信心：中等偏低）**

依據：
- 分析師面（權重最高）：bullish，信心高。21 家中 20 家為 Buy 系，無 sell，Buy 家數近期增加，目標價區間約 $490–$540 平均，高於 MarketBeat 2026-10-06 的 $482.61 參考價。
- 內部人面：小幅 bullish。6 個月內無賣出，總買入金額低，且 $322k 的 Burns 買進落在 6 個月窗外。
- 零售面：無資料，不納入評分。所有 Reddit、StockTwits 來源均未取得 2026-10 的數據，僅有零星正面的聚合情緒分數。

信心偏低的原因：零售端完全缺資料；目標價來源彼此差距大（$355 至 $700）；股價參考值分散在 $403–$483，不同來源時點不一致，無法確認當前價位；insider 資料的申報制度存疑。

Divergence flag：**無法判定**。因零售傾向不可得，無法判斷零售是否與分析師反向。若日後取得 WSB / StockTwits 數據，應重新檢查是否背離。

## 資料缺口與待補項目
1. Reddit（r/wallstreetbets、r/stocks）與 StockTwits 在本次執行中無法取得 2026-10 的樣本。
2. yf 工具 cookie / crumb 取得失敗（連線錯誤），回傳內容的即時性無法確認，應視為 repo 快取或彙總資料。
3. 個別分析師評等變動與目標價變動明細缺失，只有 WebSearch 的零星摘要。
4. 目標價與股價來源未對齊，建議以即時報價與分析師資料庫（如 MarketBeat、Yahoo Finance 或 TSMC IR）覆核。

SENTIMENT REPORT COMPLETE
