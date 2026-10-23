# Sentiment — SNDK as of 2026-10-23

資料品質註記: 分析師評等計數來自 yf rec_summary (當期快照)。評等變動歷史與 StockTwits 無法取得。Reddit 與 X/新聞搜尋結果多為 2026 年早期或夏季的快照，無法確認與 2026-10-23 同期。內部人交易以 yf insider 為準 (最新一筆 2026-09-17)。

## Analyst consensus

| 評等 | 當期 (0m) | 3 個月前 (-3m) | 變化 |
|---|---|---|---|
| Strong Buy | 4 | 3 | +1 |
| Buy | 17 | 15 | +2 |
| Hold | 3 | 4 | -1 |
| Sell | 0 | 0 | 0 |
| Strong Sell | 1 | 1 | 0 |
| 合計 | 25 | 23 | +2 |

當期: **21 buy (含 strong buy 4) / 3 hold / 1 sell (strong sell 1)**，共 25 家。買方占比約 84%。

Recent moves:
- yf recommendations 只回傳與 rec_summary 相同的計數彙總，**評等升降級明細 (個別券商、日期、前後評等) 為 DATA_UNAVAILABLE**。
- 目標價: 搜尋結果顯示 Susquehanna 目標價 1,000 → 2,000 USD (維持 Positive)；Citi 目標價 1,300 → 2,025 USD (維持 Buy)；Rosenblatt 2,400 USD (新覆蓋，約 9 月 22 日)；Bernstein SocGen 3,000 USD (約 8 月 17 日)；Investing.com 平均 12 個月目標價約 2,137 USD (頁面可能停在 8 月)。
- 目標價離散度很大 (約 1,000 至 3,000 USD)。搜尋中出現的 Arete $63 目標價與 Mizuho $215 目標價屬過時資料，已排除。
- 近期股價在 6 月高點後明顯回檔 (一篇報導指四個交易日跌約 25%，日期不明)。
- 下一次財報: Investing.com 列出 **2026-10-29**，在 10-23 之後一週內。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: WebFetch JSON 端點依指示不使用。以 WebSearch 取得的資料只有 2026 年初的快照: 一篇報導指 r/wallstreetbets 情緒分數在 1 月底達 88–89 (極度看多)；另一則指同期 Reddit 活動量低、散戶相對沉寂。**找不到 2026-10 的 thread 樣本，當期 Reddit tilt 為 DATA_UNAVAILABLE。**
- **StockTwits**: 依 soft-fail 規則未取得 (未以 WebFetch 呼叫)，**DATA_UNAVAILABLE**。
- **X / 新聞聲量**: WebSearch 找到的新聞以分析師目標價上調為主，語氣偏多；未找到可比對的 X 貼文量資料。
- **聲量 (定性)**: 無可靠數字。搜尋結果顯示 SNDK 在 2026 年是高關注的 AI 記憶體題材，但無法量化與平均值的比較。
- **主要題材 (依新聞與分析師敘述)**:
  - AI 資料中心需求帶動 NAND / flash 需求與長期供應協議 (Citi 報告提及 Kioxia 財報與 SNDK 長期協議)。
  - 財報 beat 但股價盤後下跌 (FQ4 2026, 8 月 5 日)，市場對估值與高獲利可持續性有疑慮。
  - 估值爭議: 有評論認為目前估值假設極端利潤率可以長期維持。
  - 指引: 管理層預估 FQ1 2027 營收 10.3B–10.8B USD。

Sample (representative bullish take, ≤15 words): 來自分析師報導，非散戶貼文；散戶原文樣本 DATA_UNAVAILABLE。

## Insider activity

以 yf insider 計算近 6 個月 (2026-04-23 至 2026-10-23)，金額單位為 **USD M**:

- **買入 (open-market buy)**: 0 筆，**約 0 M USD**。
- **賣出 (Sale)**: 共 13 筆，合計約 **130.3 M USD**。
- 非現金交易 (Stock Gift、Stock Award 無金額) 不列入金額計算。ILKBAHAR ALPER 於 2026-08-20 另有一筆 276 股交易，金額欄位為空，未計入。
- **淨額: 約 -130.3 M USD (淨賣出)**。

Notable:
- **GOECKELER DAVID V (CEO)**: 2026-09-14 賣出約 33,838 股 (約 51.7 M USD，價約 1,522–1,542)；2026-09-17 賣出約 33,841 股 (約 53.3 M USD，價約 1,567–1,587)。兩筆合計約 105 M USD，占期間賣出總額約 81%。兩筆規模接近，可能為事先排程 (10b5-1) 交易，但資料未標示計畫，**此推論未經證實**。
- **SHEK BERNARD (Officer)**: 6 月至 9 月多次小額賣出，合計約 8.5 M USD。
- **ILKBAHAR ALPER (CTO)**: 6 月至 9 月賣出，合計約 12.0 M USD (含 6/01 約 3.5 M USD、9/03 約 7.9 M USD)。
- **POKORNY MICHAEL (Officer)**: 5 月 12 日賣出約 3.5 M USD。
- **VISOSO LOMELIN LUIS FELIPE (CFO)**: 9 月 15 日賣出 1,000 股，約 1.6 M USD。
- **董事**: SAYINER NECIP 5 月賣出約 0.9 M USD；其餘董事於此期間主要為股票贈與或獎勵，無重大買進。
- 此期間所有高階人員與董事均無公開市場買進紀錄。

## Ownership shifts

- 機構持股比例: 82.9% (institutionsPercentHeld)；機構家數: 2,351。
- 內部人持股: 1.09%。
- 最大單一持股: Western Digital Corporation 為 10% 以上持有人，持股 29,863,251 股，申報日 2025-02-13 (資料為舊申報，非當期)。
- **機構持股趨勢 (季度變化): DATA_UNAVAILABLE**。目前只有單一時點快照，無法判定集中度是上升或下降。

## Net sentiment score

**Composite: 偏多 (信心: 低至中)**

依構成項目的判斷:
- 分析師面: **偏多** (信心: 中高)。21/25 買進，目標價上調居多，近三個月淨升評。但目標價離散度大，評等計數不含升降級明細。
- 內部人面: **偏空** (信心: 高)。6 個月內約 130 M USD 淨賣出，以 CEO 兩筆大額賣出為主，且無任何公開市場買進。
- 散戶面: **無法可靠判定** (信心: 低)。Reddit、StockTwits、X 的 2026-10 資料皆為 DATA_UNAVAILABLE。
- 綜合: 分析師偏多，內部人偏空，散戶不明。整體標為偏多，但信心僅低至中，並以內部人賣出作為風險註記。

**Divergence flag: 是 (有限度)** — 分析師偏多與內部人淨賣出方向相反。散戶 tilt 無法確認，因此無法判定散戶與分析師是否背離。內部人賣出常見於例行或排程交易，不必然代表看空，但這個背離值得在後續步驟追蹤，特別是 2026-10-29 財報前後。

## 資料缺口摘要

- 評等升降級明細: DATA_UNAVAILABLE
- StockTwits: DATA_UNAVAILABLE
- Reddit 2026-10 thread 樣本與 tilt: DATA_UNAVAILABLE
- 機構持股趨勢: DATA_UNAVAILABLE
- 10b5-1 計畫標記: 未提供

SENTIMENT REPORT COMPLETE
