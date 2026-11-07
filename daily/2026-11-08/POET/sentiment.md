# Sentiment — POET as of 2026-11-08

> 資料限制: yf 即時源被封鎖, 分析師評級與內部人資料皆來自 repo cache, 最新一筆內部人交易為 2026-08-19, 9 月至 11 月無資料。Reddit / StockTwits 直連不可用, 改以 WebSearch 取得的二手摘要為準, 找不到 2026 年 10–11 月的社群原始貼文。以下結論信心皆為低至中。

## Analyst consensus
yf `rec_summary` 與 `recommendations` 回傳全為 0 (無有效計數), 無法給出可信的 N buy / N hold / N sell。

網路二手來源互相矛盾, 且日期不一:
- MarketBeat (較舊): 共識 sell, 平均目標價 $8.00。
- Stockalarm: 2 Buy (100%), 2 位分析師。
- Benzinga: 分析師共識 Buy, 2 位分析師。
- Stockchase: 過去一年 1 buy / 1 sell, 最新評級 "don't buy"。

Recent moves: 找不到 2026 年 9–11 月的評級升降級或目標價變動紀錄。最近可確認的事件為 Q3 2026 財報預定 2026-11-16 (週一) 盤前公布 (公司新聞稿), 預估每股虧損約 -$0.07。

判讀: 分析師端無法形成可靠共識, 只能確認 "覆蓋少、意見分歧、偏保守" 的大方向。

## Retail social
- Reddit: 直連不可用。WebSearch 摘要顯示 2026-05 前後 r/wallstreetbets 有高度看多貼文 (例如 5 月 19 日一則預測年底 $40 的貼文), 但同期亦有 24/7 Wall St 報導指出股價單日暴跌 45% 後社群情緒急轉。2026-11 的 Reddit 討論量與傾向無法確認。
- StockTwits / X: StockTwits 最後可見的情緒讀數為 2026-05-11 的 neutral; 另一篇未標註日期的報導稱散戶情緒已在 bearish 區間持續至少一週。2026-04 曾達 extremely bullish (CFO 訪談後)。X 上無可用的 2026-11 搜尋結果。
- Themes (歷史, 非當前): (1) 光學 / 共封裝光學 (CPO) 與 AI 資料中心題材; (2) 股價波動與軋空 (short interest 偏高); (3) 推廣爭議, Dow Jones 2026-04 報導指公司付費網紅約 $100K 推薦; (4) 2025 年虧損規模 (報導引用約 $63M 淨損、營收約 $1M), 散戶對獲利與現金消耗的質疑。
- 討論量: 無法量化。以 2025-10 與 2026-05 兩波熱度為參照, 目前沒有看到明顯放量的社群報導, 判定為 "低於前高峰" (定性)。
- Retail tilt: 歷史上偏多但極度波動; 最近可見的讀數為 neutral 至 bearish, 信心低。

## Insider activity
Net 6mo (2026-05-08 至 2026-11-08, 但 cache 僅至 2026-08-19): 公開市場賣出約 $5.10M, 公開市場買進 $0。
另有選擇權行權 (Exercise of options) 約 $0.5M 行權成本, 屬行權而非買進, 多數伴隨同日賣出。

| 內部人 (cache 職稱) | 公開市場賣出 (USD M) | 最近一筆 |
|---|---|---|
| Barnes (Kevin), Senior Officer | 1.94 | 2026-08-10, $8.93 |
| James (Lee), Director / Senior Officer | 1.07 | 2026-06-12, $14.68 |
| Jinyu (Mo), Senior Officer | 1.09 | 2026-06-05, $10.82 |
| Mika (Thomas R), Senior Officer | 0.41 | 2026-08-07, $8.93 |
| Kankipati (Venkata Rama Raju), Senior Officer | 0.29 | 2026-08-07, $8.93 |
| Riley (Glen), Director | 0.15 | 2026-08-19, $9.45 |
| Khan (Sohail A), Director | 0.06 | 2026-07-08, $5.84 |
| Ende (Theresa Lan), Director | 0.05 | 2026-06-30, $6.71 |
| Tirva (Robert Linas), Director | 0.04 | 2026-06-30, $6.71 |

Notable: 最大單筆為 Barnes 2026-05-20 以 $14.22–14.69 賣出約 $1.23M 與 Barnes 2026-06-05 以 $11.25 賣出 $0.57M; Jinyu 2026-06-05 以 $10.82 賣出 $0.65M。賣出價從 $14 區間回落至 $6–9 區間, 內部人賣出集中在股價高點之後。
交叉檢核: TipRanks 網頁摘要稱近 3 個月內部人賣出 $0.902M, 與 cache 近 3 個月 (8 月起) 約 $0.9M 大致吻合, 但 cache 完整 6mo 為 $5.1M, 兩者口徑 (期間、是否含行權) 需確認。
Caveat: cache 內職稱僅寫 "Senior Officer" / "Director", 未標示 CEO / CFO, 無法直接判定高階管理層身分。

## Ownership shifts
- insidersPercentHeld: 0.068% (接近零, 與大量賣出並存, 快照時點不明)。
- institutionsPercentHeld: 20.02%, institutionsFloatPercentHeld 20.03%, 機構數 183。
- 趨勢: cache 僅為單一快照, 無歷史比較, 無法判定機構持股是增加或減少。機構持股比例偏低, 代表籌碼集中度低、交易多由散戶與短線資金主導 (定性判讀)。

## Net sentiment score
Composite: **偏空 / 中性偏空 (confidence: 低)**

依據:
- 內部人: 6 個月內 $5.1M 公開市場賣出、零買進, 偏空 (信心中)。
- 分析師: 無可靠計數, 二手來源矛盾, 不納入計分 (信心低)。
- 散戶: 最近可見讀數為 neutral 至 bearish, 歷史多空劇烈擺動, 近期資料缺乏 (信心低)。
- 外部事件: Q3 財報 2026-11-16 為近期最大變數, 目前尚未公布, 情緒可能在財報前後劇烈改變。
- 股價參考: StockChase 報 2026-11-06 收盤約 $5.07; 另一來源 investing.com 顯示約 $7.80, 兩者不一致, 未採用。

Divergence flag: **無法判定 (no)** — 分析師端資料不足以與散戶傾向比較; 內部人 (偏空) 與最近可見的散戶讀數 (neutral 至 bearish) 方向大致一致, 無明顯背離。

資料缺口 (需補):
1. yf rec_summary / recommendations 有效資料 (目前全為 0)。
2. 2026-08-19 之後的內部人 Form 4 交易紀錄。
3. 2026-10 至 11 月的 Reddit / StockTwits 原始貼文量與情緒。
4. 2026-04 "$400M Registered Direct Offering" 的說法僅見單一來源且與 2025-10 "$75M" 融資說法並存, 未交叉驗證, 未納入判讀。

SENTIMENT REPORT COMPLETE
