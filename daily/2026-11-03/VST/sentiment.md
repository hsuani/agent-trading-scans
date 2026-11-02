# Sentiment — VST as of 2026-11-03

資料截至 2026-11-02 可取得的來源。Q3 2026 財報預定 2026-11-06 盤前公布，尚未公布。

## Analyst consensus

| 評級 | 家數 | 占比 |
|---|---|---|
| Strong Buy | 4 | 17.4% |
| Buy | 18 | 78.3% |
| Hold | 0 | 0% |
| Sell | 0 | 0% |
| Strong Sell | 1 | 4.3% |

合計 23 家。yf `rec_summary` 回傳 22 家偏多（Strong Buy + Buy），1 家 Strong Sell，無 Hold。來源間家數不一致：WebSearch 引用的 MarketBeat / Barchart 數字為 1 Strong Buy / 17 Buy / 1 Hold / 1 Sell，或 16 Strong Buy / 1 Hold，口徑不同，本報告以 yf 為準。

近期變化：
- 近一個月（`-1m` 至 `0m`）Buy 由 15 增至 18，合計由 20 家增至 23 家，代表近期新增約 3 筆偏多評級（可能為首次覆蓋）。Strong Buy 家數四個期間皆為 4。
- yf `recommendations` 工具只回傳期間彙總，無個別 upgrade / downgrade 明細，無法列出具體券商動作。
- 目標價：MarketBeat 7 月約 $230.63；9 月 Tikr 引用平均 $217.42；10 月底 MarketBeat preview 為 $202.43。目標價呈下修趨勢。
- 7 月 30 日 MarketBeat 報導提及 TD Cowen 降評後股價大跌，屬於少數負面動作。
- BMO 將目標價由 $236 調高至 $245（維持 Outperform）的報導，WebSearch 顯示屬於前一年的 Q3 更新，不採為近期訊號。

## Retail social

- **Reddit（r/wallstreetbets、r/stocks）**：本次無法取得。依任務規定，未對社群主機使用 WebFetch；WebSearch 未返回任何 VST 相關 Reddit 討論串。軟性失敗，此來源缺席。
- **StockTwits**：WebSearch 僅取得頁面快照（市值 $49.97B、52 週區間 $132.66–$219.82、P/E 24.74），無 bullish / bearish 比例。須直接查 stocktwits.com/symbol/vst 才能取得。
- **LunarCrush 聚合頁**：多個語系快照顯示社群情緒 85%–95% 正向（一則為 339 篇 / 24 小時），但頁面無日期，可信度低，僅作參考。
- **SentiSense**：2026-08-09 快照評為 slightly bullish（30 日分數 6），並呈降溫趨勢。日期偏舊。
- **Benzinga**：2026-08-28 快照 P/C ratio 0.51、short float 3.3%。日期偏舊。
- **X**：WebSearch 未取得可用的貼文層級情緒資料。
- **Buzz 量**：無法量化。以 LunarCrush 單一快照的 339 篇 / 24 小時推估屬中等，但無歷史基準可比，只能定性為「無法量化，定性判斷為中等」。

**Retail tilt**：偏多（低可信度）。主要依據為 LunarCrush 聚合正向比例與 SentiSense 偏多快照，兩者皆非當日、非原始貼文。

**Themes（由新聞與預覽歸納）**：
1. 資料中心電力需求與 AI 題材：Meta 20 年核能合約、Helix 資料中心平台（最多 $1B 承諾）。
2. 管理層對資料中心規模的保守口徑：CEO 表示 ERCOT 佇列曾被描述超過 400 GW，但公司預期 2030 年約 12–15 GW。這是市場討論的爭議點。
3. Texas 電價（ERCOT pricing）為空方論點的核心，認為股價走勢取決於電價而非資料中心需求。
4. 2026 年股價落後大盤（Barchart：YTD 約 -15.6%，SPX 約 +12.1%）。
5. 11/6 財報與 2027 預測更新為近期催化劑。

代表性市場口吻（WebSearch 預覽文章摘要）：「sentiment has turned from mildly bullish to mildly bearish」（前述預覽之描述，非原始貼文）。

## Insider activity

統計區間：2026-05-03 至 2026-11-03（6 個月）。金額以 USD 計，單位 M。僅計 Purchase 與 Sale；Stock Award、Stock Gift、Conversion of derivative 不計入買賣淨額。

Net 6mo：**$1.17M 買入**（2 筆）、**$25.88M 賣出**（10 筆），淨賣出 **$24.71M**。

| 日期 | 人員 | 職稱 | 交易 | 金額 (M USD) |
|---|---|---|---|---|
| 2026-08-24 | BURKE JAMES A. | CEO | Purchase @ $135.00 | 0.27 |
| 2026-09-01 | BURKE JAMES A. | CEO | Purchase @ $135.25–135.99 | 0.90 |
| 2026-09-08 | HUDSON SCOTT A | Officer | Sale @ $150.97–152.56 | 6.75 |
| 2026-09-08 | MOLDOVAN KRISTOPHER E. | CFO | Sale @ $151.03 | 3.02 |
| 2026-10-06 | HUDSON SCOTT A | Officer | Sale @ $160.14 | 3.56 |
| 2026-10-07 | MOLDOVAN KRISTOPHER E. | Officer（間接持股） | Sale @ $165.00 | 3.30 |
| 2026-05-27 至 06-18 | 多位董事 / 高管（HELM、ACOSTA、SULT、BARBAS、MONTEMAYOR） | Director / Officer | Sale | 合計約 9.2 |

依人員彙總（M USD）：Hudson 10.31、Helm 4.00、Moldovan 6.32（CFO 3.02 + 間接 3.30）、Acosta 2.51、Montemayor 1.56、Sult 1.10、Barbas 0.07。

重點觀察：
- CEO Burke 在股價約 $135 時於 8 月底至 9 月初兩度以公開市場買入，是區間內唯一的 open-market 買入，金額約 $1.17M。
- 9 月至 10 月的大額賣出集中於 Hudson 與 Moldovan，價位在 $150–165 之間。
- 區間外（2025 年下半）CEO Burke 有大量 option 轉換後賣出的紀錄，屬於 10b5-1 或例行變現型態的可能，但本工具無法驗證計畫性質，僅作記錄。
- 數字驗算：Burke 6,665 股 × 約 $135.6 ≈ $0.90M，與工具回傳一致。Hudson 22,222 × $160.14 ≈ $3.56M，一致。

## Ownership shifts

- 機構持股：92.5%（institutionsPercentHeld），float 內機構持股 93.2%，機構家數 1,897。
- 內部人持股：0.77%。
- 趨勢：工具僅提供單一時點快照，無歷史比較，無法判斷集中度是增加或減少。

## Net sentiment score

**Composite：中性偏多（neutral-to-bullish），信心：中低。**

分項判斷：
- 分析師：偏多，信心高。22 / 23 家偏多、無 Hold，但目標價近幾個月下修。
- 內部人：偏空，信心中。6 個月淨賣 $24.7M，但 CEO 在 $135 有公開買入，屬於混合訊號。
- 散戶：偏多（低可信度）。聚合器正向比例高，但來源皆非當日、非原始貼文，且 Reddit 與 StockTwits 比例缺席。
- 價格動能：偏弱。YTD 落後大盤，近期受資料中心 AI 題材與 Texas 電價疑慮拖累。

**Divergence flag：是。** 分析師（偏多）與內部人淨賣（偏空）方向相反。散戶資料亦偏多，但可信度低，不足以確認是否與分析師同向。股價動能偏弱，與分析師偏多亦屬反向，值得在 11/6 財報後重新檢視。

## 資料缺口與限制

- Reddit 與 StockTwits 原始資料缺席，散戶判斷主要依賴聚合器與日期偏舊的快照，信心因此打折。
- Yahoo cookie / crumb 取得失敗（ConnectionError），但 yf 工具仍回傳資料，數字採信，惟未做交叉驗證。
- 分析師家數與評級分布在不同來源間不一致，已於上文註明。
- 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
