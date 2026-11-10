# Sentiment — 3661.TW（世芯-KY, Alchip Technologies）as of 2026-11-10

資料品質總覽：分析師評等（yf rec_summary）可用但為快取回傳；歷史評等變動資料異常（四個月數字完全相同，視為過期快取）；內部人交易為 DATA_UNAVAILABLE；Reddit、StockTwits、PTT 社群資料全數不可取得，零星來源僅為新聞與法人觀點。

## Analyst consensus

16 位分析師（yf rec_summary，快取）：6 Strong Buy / 9 Buy / 1 Hold / 0 Sell / 0 Strong Sell，即 15 買進（含強力買進）、1 持有、0 賣出。Investing.com 頁面顯示 15 Buy / 1 Hold，與 yf 幾乎一致。

近期評等變動：yf recommendations 回傳的四個期間（0m / -1m / -2m / -3m）數字完全相同，無法辨識實際升降評等事件，判定為 DATA_UNAVAILABLE（僅有快照，無逐家事件）。

目標價（TWD，來源日期不一，以下為搜尋摘要）：

| 機構 | 目標價（TWD） | 評等 | 資料日期（來源標示） |
|---|---|---|---|
| Citi | 6,800 | 未確認 | 2026-08 |
| Macquarie | 6,542 | 未確認 | 2026-08 |
| JPMorgan / CLSA | 6,000 | 未確認 | 2026-11 頁面（日期不確定） |
| 元大投顧 | 4,500 | 買進 | 2026 年 5 月前後 |
| 富邦投顧 | 4,500 → 4,140（下調） | 未確認 | 2026 年內（下調，確切日期不明） |
| 群益投顧 | 3,495 | 區間操作 | 2026 年內（日期不明） |

目標價區間約 3,755 至 6,800 TWD（TradingView 摘要），分歧大。Simply Wall St 社群敘述顯示 11 位分析師小幅下調目標價，日期不明。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。直接 WebFetch 遭拒（"unable to fetch from www.reddit.com"），WebSearch 亦無相關貼文。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 在本環境無法解析（DNS 失敗，需由 session 網路設定放行）。
- PTT / X / 其他論壇：WebSearch 未搜尋到 PTT 網友貼文或 X 討論串，無法判斷散戶語氣。
- 聲量（buzz volume）：無法量化，DATA_UNAVAILABLE。
- 散戶傾向：UNKNOWN（資料不足，不可推論）。
- 可觀察的媒體與法人語氣（非散戶，僅供參考）：
  - 偏多：法人觀點認為 AWS 上修 Trainium 3 伺服器出貨目標，世芯為核心設計夥伴直接受惠（經濟日報引述）；2026 年 5 月外資維持「加碼」，認為最壞情況已過（自由財經）。
  - 偏空或保守：毛利率跌破 20%，公司形容接近業務組合最差情境（uanalyze，2026-11-07）；富邦下調目標價，考量設計服務同業競爭；群益僅給區間操作。
- 主要議題（來源推論，非社群原文）：(1) 毛利率下滑 vs 獲利創高；(2) Trainium 3 出貨與 AWS 客戶集中度；(3) 第 4 季量產營收與新案投片；(4) 估值偏高（Simply Wall St 指 P/E 約 46 倍，高於台灣半導體產業約 33 倍）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。yf insider 回傳空陣列，無法區分「無交易」與「資料缺漏」，不可解讀為零交易。未能確認 CEO / CFO 或其他董監事的買賣方向與金額。

## Ownership shifts

- 內部人持股：3.14%（yf major_holders）
- 機構持股：38.73%；流通股中機構占比 39.99%
- 機構家數：257
- 趨勢：僅單一時點快照，無法判斷集中度變化方向，判定為 DATA_UNAVAILABLE（趨勢部分）。

## Net sentiment score

Composite：**偏多（bullish），信心低（low）**

- 分析師面：強烈偏多（15 買進 / 1 持有 / 0 賣出），但目標價分歧大，且評等資料為快取，時效不確定。
- 內部人面：DATA_UNAVAILABLE，不計入。
- 散戶面：DATA_UNAVAILABLE，無法評估。
- 媒體與法人觀點：多空並陳；業績創高與 AWS 題材偏多，毛利率下滑與估值偏高偏空。
- 價格與時效：來源股價日期互相不一致（約 3,060 至 4,930 TWD），無法確認 2026-11-10 當日收盤；本報告不推論價格走勢。

Divergence flag：**無法判定（DATA_UNAVAILABLE）**。分析師傾向為偏多，但散戶傾向無資料，因此無法確認兩者是否背離。

信心說明：分析師評等單一來源且為快取；其餘 Phase 1 社群與內部人資料缺漏。建議在 session 網路放行 api.stocktwits.com 與 Reddit 存取後重跑，並改用 yf 即時資料重新確認評等與內部人交易。

本報告不含交易建議。

SENTIMENT REPORT COMPLETE
