# Sentiment — ANET as of 2026-10-21

注意事項：
- yf 工具子命令與任務描述不符：`ratings` 實際為 `recommendations`，`holders` 實際為 `major_holders` / `inst_holders`。
- 所有 yf 呼叫顯示 Yahoo cookie/crumb 取得失敗，但資料仍正常回傳（`cache` 來源），視為可用。
- 最新內部人交易日為 2026-10-09，最新公開股價快照為 2026-10-08。

## Analyst consensus

rec_summary（yf, 當期）：32 家分析師，7 strongBuy / 24 buy / 1 hold / 0 sell / 0 strongSell。約 97% 為買進評等。

近四個月趨勢：
- 當期與前一期（-1m）相同：7 / 24 / 1。
- -2m：8 / 23 / 0。
- -3m：7 / 22 / 1。
- 評等結構穩定，無明顯降級跡象。

近期升降評等與目標價調整：yf `recommendations` 僅回傳彙總計數，未提供逐筆升降評明細，此部分為 DATA_UNAVAILABLE。

WebSearch 補充（非 yf，時點不一）：
- Barchart 報導（Q2 2026 財報後）：26 家分析師，22 Strong Buy / 3 Moderate Buy / 1 Hold，共識 Strong Buy。與 yf 的 32 家數量不一致，可能來自不同資料源或不同時點。
- StockAnalysis（2026-08-05 快照）：12 個月目標價 $228.61。
- Evercore ISI 將目標價由 $200 上調至 $250，維持 Outperform（StockAnalysis 引述）。發布日期未確認。

## Retail social

- Reddit：依任務規定跳過 Reddit 域名。WebSearch 另查 r/wallstreetbets 相關內容，未找到 ANET 近期討論串，無法判斷 buzz 量與語氣。
- StockTwits：依任務規定跳過，DATA_UNAVAILABLE。
- X / 新聞輿情：WebSearch 未找到 2026-10 的散戶情緒文章，DATA_UNAVAILABLE。
- 聲量（buzz volume）：DATA_UNAVAILABLE。
- 語氣傾向：DATA_UNAVAILABLE。
- 主題：無可靠樣本。近期可確認的公開事件僅有：
  - 2026-10-06 公告 Q3 財報將於 2026-11-03 盤後發布（[Arista 新聞稿](https://www.arista.com/zh/company/news/press-release/24817-pr-20261006)）。
  - Q2 2026 營收約 $30 億，年增 37.7%，上調全年營收指引至約 $126 億，Q3 指引約 $33 億（[Nasdaq 財報會議摘要](https://www.nasdaq.com/articles/arista-networks-q2-earnings-call-highlights)）。
  - 空方論點（早期 2026 報導）：記憶體成本上漲壓縮毛利（[Tikr](https://www.tikr.com/blog/arista-networks-has-tripled-from-its-52-week-low-heres-why-analysts-still-signal-a-buy)）。此為機構分析觀點，非散戶討論。
- 代表性散戶語句：無可引用樣本。

## Insider activity

以 2026-04-21 至 2026-10-21 計算（近 6 個月），依 yf `insider` 逐筆加總（金額為工具回傳之 Value，近似值）：

- 公開市場買入：未見任何 Purchase 紀錄，淨買入為 $0。
- 公開市場賣出：約 $12.5 億（$1.25B）。
  - CEO Jayshree Ullal：約 $6.72 億，為最大賣方。最近一筆為 2026-10-09，以約 $217.05 賣出 158,543 股，金額約 $3,440 萬。
  - 10% 大股東 Andreas Bechtolsheim（非內部人職位，但列為內部人申報）：約 $5.45 億。
  - President Kenneth Duda：約 $2,420 萬，多為 10b5-1 式定期賣出（規律性，但本工具未確認計畫類型）。
  - CFO Chantelle Breithaupt：約 $77 萬。
  - 董事 Charles Giancarlo：約 $409 萬。Mark Templeton：約 $201 萬。其餘董事（Battles、Wassenaar）合計約 $14 萬。
- 其他申報（未計入賣出）：選擇權行使轉換、股票贈與（0 價）、董事年度股權授予（金額為 null）。
- 解讀：賣出集中於 CEO 與 10% 大股東，且股價區間約 $150 至 $217 間持續出售，屬於大額、持續性減持。非內部人買入，屬偏空的內部人訊號，但多數 CEO 賣出可能屬預先排程或稅務相關，本工具無法確認。

## Ownership shifts

yf `major_holders` 摘要：
- 內部人持股：17.2%。
- 機構持股：73.4%；占浮動股數 88.7%；機構家數 3,157。

前十大機構（13F 日期 2026-06-30，最新可得季度，Q3 13F 尚未公布）：

| 機構 | 持股比例 | 季度股數變化 |
|---|---|---|
| BlackRock | 7.25% | -0.6% |
| Vanguard Capital Management | 5.45% | +0.6% |
| State Street | 3.82% | +3.0% |
| FMR | 3.75% | -9.5% |
| Geode | 2.18% | +1.0% |
| Vanguard Portfolio Management | 2.05% | -0.1% |
| T. Rowe Price | 1.84% | -20.8% |
| Morgan Stanley | 1.56% | +6.4% |
| Cresset | 1.54% | -6.4% |
| Capital Research Global Investors | 1.04% | -10.8% |

趨勢：前十大中減持者（FMR、T. Rowe、Capital Research 等主動型基金）減碼幅度較大，被動指數資金（BlackRock、Vanguard、State Street、Geode）持平或增持。機構集中度整體穩定，主動基金有獲利了結跡象。

## Net sentiment score

綜合判斷：偏多（分析師面）與偏空（內部人面）分歧。
- 分析師：強烈買進，評等穩定，目標價高於近期股價（約 $215 至 $217）。信心：中高。
- 內部人：大額持續賣出，無買入，偏空。信心：中（需考慮 10b5-1 與稅務因素）。
- 機構：主動基金減碼，被動資金持平。中性。
- 散戶：DATA_UNAVAILABLE，無法評估。

整體：分析師偏多、內部人偏空，綜合為中性偏多，信心中等。

Divergence flag：部分。分析師與內部人之間出現分歧（分析師買進、內部人大額賣出）。散戶面無資料，無法判斷是否與分析師反向。

## Data gaps
- Reddit、StockTwits、X：DATA_UNAVAILABLE。
- 逐筆分析師升降評與目標價變動：DATA_UNAVAILABLE（yf 僅提供彙總，WebSearch 只有 8 月前後的零散資料）。
- 2026-06-30 以後的機構持股變動（Q3 13F）：DATA_UNAVAILABLE（尚未公布）。

Sources:
- [Arista Q3 2026 earnings date press release](https://www.arista.com/zh/company/news/press-release/24817-pr-20261006)
- [Nasdaq Q2 earnings call highlights](https://www.nasdaq.com/articles/arista-networks-q2-earnings-call-highlights)
- [Tikr: Arista tripled from 52-week low](https://www.tikr.com/blog/arista-networks-has-tripled-from-its-52-week-low-heres-why-analysts-still-signal-a-buy)
- [StockAnalysis ANET](https://stockanalysis.com/stocks/ANET/)
- [Barchart analyst estimates](https://www.barchart.com/story/news/3755970/arista-networks-stock-analyst-estimates-ratings)

SENTIMENT REPORT COMPLETE
