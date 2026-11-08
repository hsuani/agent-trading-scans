# Sentiment — AMD as of 2026-11-09

資料基準: yf 快取 `prices/yf/AMD.json` (refreshed 2026-11-08 13:14 UTC, source=cache); 社群面以 WebSearch 取得之二手摘要為主 (Reddit / StockTwits 原站無法直接存取)。

## Analyst consensus

最新 rec_summary (0m) 分布: 6 strong buy / 39 buy / 8 hold / 0 sell / 0 strong sell, 合計 53 家 (info 欄位 numberOfAnalystOpinions 為 47, 兩者口徑不同, 以 rec_summary 計數為準)。Buy 類合計 45 家, 約佔 85%, 無賣方評等。

Recommendation mean 1.42 (strong_buy 區間)。

近期變化 (rec_summary 時間序列, 0m 對比 -3m):

| 期間 | strongBuy | buy | hold | sell |
|---|---|---|---|---|
| 0m (本期) | 6 | 39 | 8 | 0 |
| -1m | 5 | 39 | 11 | 0 |
| -2m | 5 | 40 | 11 | 0 |
| -3m | 4 | 40 | 11 | 0 |

過去一個月 hold 由 11 降至 8, strongBuy 由 5 增至 6, 未見新增 sell。這代表評等有小幅向上調整, 而非下調。

目標價 (info): 平均 659.77 USD, 中位數 650 USD, 最高 1250 USD, 最低 540 USD。以現價 449.04 USD 計, 平均目標價相對現價的上行空間約 47%; 最低目標價 540 仍高於現價約 20%。

近期券商調整 (來源為 WebSearch 摘要, 日期與口徑未完全核實, 請視為方向性參考):
- Bank of America: 目標價由 720 下調至 650 USD, 理由為板塊估值倍數收縮。
- Mizuho: 目標價由 705 下調至 610 USD, 維持 Outperform。
- JPMorgan: 目標價由 550 上調至 575 USD, 維持 Neutral。
- Truist: 目標價由 594 上調至 605 USD, 維持 Buy, 理由為資料中心動能較強。
- Morgan Stanley: 目標價由 465 上調至 510 USD, 維持 Equal Weight (此條日期不明)。

整體而言, 大型券商多數維持買進或中性評等, 目標價有分歧: 部分因估值壓縮下修, 部分因財報後上修。

財報背景 (yf earnings_dates): 2026-11-03 公布 Q3, EPS 2.09 vs 預估 1.95 (surprise +7.44%)。營收約 133.8 億 USD, 年增約 45% (WebSearch 摘要)。下一次財報預估 2027-02-02, EPS 預估 2.93。

## Retail social

- Reddit: 本次無法取得 2026 年 11 月 r/wallstreetbets 與 r/stocks 的有效討論串。WebSearch 僅找到一則未註明日期、提及 AMD 與 SOXL 的 WSB 貼文, 無法用於判讀當前情緒。Reddit 部分為 soft-fail, 未納入評分。
- StockTwits: 有一篇約 11 月 4 日的報導指出, 散戶情緒由 "bullish" 升至 "extremely bullish", 訊息量在 24 小時內增加約 200%, 討論熱度升至 "extremely high"。另一篇較早期的 StockTwits 報導則提到情緒由 "bullish" 轉為 "neutral", 日期不明。
- X / 新聞鏈接: CEO Lisa Su 於 11 月 5 日前後在 X 發文, 表示市場對 AI 的看法 "short-sighted" (短視)。
- 代表性標題 (僅引用標題, 不轉載貼文):
  - "AMD Earnings 'Checked Every Box,' But Wall Street Remains Split On The Stock"
  - "AMD Stock Slips Despite Wave Of Price Target Hikes – Retail Traders Say Chip Rally Is 'Starting To Look Exhausted'"
  - "AMD Stock Rises Premarket: Retail Traders Eye $600 Level Despite Limited Analyst Upside"
- 散戶 tilt: 偏多但不穩。多頭論點集中在 AI 資料中心需求、財報超預期、以及向 600 USD 反彈的目標。空頭或保留論點集中在估值偏高、板塊倍數收縮、以及「漲勢疲乏」。
- 聲量: 相對常態偏高 (StockTwits 單日量增約兩倍), Reddit 無法量化。

Themes (重複出現的主題):
1. AI 資料中心需求與 2027 展望 (多頭主軸)。
2. 估值與板塊倍數收縮 (保留與空頭論點)。
3. PC 業務疲弱與 Intel 對 PC 復甦時點的說法 (不確定性來源)。
4. 財報後股價走勢與解讀分歧 (市場定調不一致)。

## Price context (cache)

現價 449.04 USD (cache), 市值約 736.5B USD (= 449.04 × 1.640B 股, 已驗算)。50 日均線 546.8 USD, 200 日均線 416.0 USD, 52 週區間 188.22 至 658.52 USD。現價距 52 週高點約 32%。

注意: StockTwits 相關報導提到 11 月 5 日收盤 404.40 USD, 單日跌約 17%; 與快取現價 449.04 USD 之間存在落差, 推測為之後反彈, 但本次無法完整核實 11 月 5 日至 11 月 8 日的價格序列。財報後股價反應, 不同來源描述不一致, 未能定論。

## Insider activity

Net 6mo (2026-05-09 至 2026-11-09): 公開市場賣出約 2.49 億 USD (約 52 萬股, 17 筆 Sale 紀錄); 公開市場買入 0 筆。另有贈與 (Stock Gift) 與選擇權行權/轉換紀錄, 非市場買賣, 不計入淨買賣。

淨額: 約 -2.49 億 USD (賣方主導)。

Notable:
- CEO Lisa Su: 2026-09-10 賣出 95,000 股 (約 4,815 萬 USD, 價格區間 503.72 至 515.55); 2026-08-18 賣出 15,000 股 (約 721 萬 USD); 2026-06-10 賣出 125,000 股 (約 5,759 萬 USD)。同期另有 35,000 股贈與。
- CFO Jean X. Hu: 2026-08-25 賣出 15,000 股 (約 711 萬 USD)。
- CTO Mark D. Papermaster: 2026-08-20 賣出 28,811 股 (約 1,360 萬 USD); 2026-08-14 賣出 7,369 股; 2026-06 至 07 月多次定期賣出 6,000 股。
- Officer Forrest E. Norrod: 2026-08-24 與 2026-09-15、10-15 各賣出約 1.7 萬股 (每次約 790 萬至 930 萬 USD), 並伴隨 7,261 股選擇權轉換。
- Officer Paul D. Grasby: 2026-08-17 賣出 15,000 股 (約 772 萬 USD)。
- General Counsel Ava M. Hahn: 2026-08-18 賣出 2,993 股 (約 146 萬 USD)。

解讀: 賣出金額集中於 6 月至 10 月, 主要為高階主管, 且股價在 470 至 540 USD 區間成交。此類賣出可能與既定交易計畫或股權激勵變現有關, 但資料無法確認是否為 10b5-1 計畫。無任何高階主管公開買入紀錄。

## Ownership shifts

機構持股比例 75.14%, 機構家數 5,213 家; 內部人持股 0.42%。資料為 2026-06-30 季報揭露, 屬單一時點快照, 無法判定完整趨勢。

前幾大持股 (季度變動):
- BlackRock: 9.16% (1.503 億股), 季增 +3.3%
- Vanguard Capital Management: 6.49%, 季增 +0.5%
- State Street: 4.53%, 季減 -0.6%
- Invesco: 3.24%, 季增 +5.4%
- JPMorgan Chase: 2.46%, 季增 +66.2% (由低基數增加)
- T. Rowe Price: 2.19%, 季增 +24.6%

整體: 前十大機構多數維持或小幅加碼, 無明顯集中撤出跡象。

## Net sentiment score

Composite: **偏多 (bullish)**, 信心度中等偏低。

評分拆解:
- 分析師面: 偏多, 信心度高 (buy 類約 85%, 無賣方評等, 目標價中位數遠高於現價)。
- 散戶面: 偏多但分歧, 信心度低 (StockTwits 有 "extremely bullish" 與 "neutral" 兩種讀數; Reddit 無資料)。
- 內部人面: 偏空 (2.49 億 USD 公開賣出, 0 筆買入), 但解讀受限於可能為計畫性賣出。

Divergence flag: **否** — 散戶與分析師方向大致一致, 均偏多。但 **內部人與分析師方向相反**, 此為值得留意的訊號。

Caveats:
- Reddit 無有效 2026 年資料, 散戶面以單一平台 (StockTwits) 與新聞標題推估。
- 券商目標價與財報後股價反應有來源衝突, 本報告未能完全核實。
- 本報告僅為情緒彙整, 不構成交易建議。

SENTIMENT REPORT COMPLETE
