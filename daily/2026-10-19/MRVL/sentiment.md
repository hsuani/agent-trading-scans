# Sentiment — MRVL as of 2026-10-19 (Taipei)

資料基準: yf cache 更新於 2026-10-18 10:54 UTC; 股價 currentPrice 227.83, previousClose 241.24。Reddit / StockTwits 直接端點為 blocked, 改以 WebSearch 取得間接資料。資料日期皆不晚於 2026-10-19。

## Analyst consensus

- 評級分布 (rec_summary 0m): 9 strongBuy / 33 buy / 4 hold / 0 sell / 0 strongSell, 共 46 家。
- **%BUY = 91.3%** (42 / 46), %HOLD = 8.7%, %SELL = 0%。
- 趨勢: %BUY 依序為 88.4% (-3m) → 88.6% (-2m) → 87.0% (-1m) → 91.3% (本月)。近一個月 BUY 數由 40 升至 42, HOLD 由 6 降至 4, 偏多方向小幅增強。
- recommendationMean 1.37 (strong buy 區間)。
- 目標價 (yf info): 均值 339.36, 中位數 350, 最高 450, 最低 210。以 227.83 計, 均值隱含上漲約 49%, 中位數隱含約 54%。
- 近期調整 (網路報導, 日期以 Investor Day 10/6 之後為準): TD Cowen 由 Hold 升為 Buy, 目標價 245 → 350; Jefferies 目標價 325 → 450; Evercore ISI 目標價 275 → 433。Stifel 目標價 230 → 321 與 Morningstar 130 → 235 出現於較早的 6 月報導。yf `actions` 本次回傳為空, 上述調整無法與 yf 交叉驗證。
- 公司 Investor Day 將 FY2028 營收目標由 $18B 上調至 $20B, FY2031 目標 $70–90B。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 直接 JSON 端點 blocked, 本次未取得。WebSearch 未檢索到 MRVL 相關 WSB 或 r/stocks 討論串。無法判斷 Reddit 語氣, 不做 Reddit 結論。
- **StockTwits (間接, WebSearch 報導)**:
  - 2026-05 財報後: 股價盤前下跌但 retail 情緒由 "bullish" 轉為 "extremely bullish", 24 小時訊息量較前期增加約 575%。
  - 2026-06 Computex 期間 (Jensen Huang 稱 "trillion-dollar company" 後): 股價創高後回落 3%, 散戶情緒仍 "extremely bullish"。
  - 這些資料皆為 5–6 月, 無 10 月 StockTwits 資料可用。
- **X / 新聞聊天**: 無可用的 10 月 X 貼文摘要。較早 (日期不明) 的 AI 摘要提及對 Microsoft 客製晶片可能轉向 Broadcom 的擔憂。
- **聚合平台交叉檢查 (日期不明)**: Naga 新聞情緒約 95% bullish, 但 crowd sentiment 分數為 NEGATIVE。Google Finance 早期 10 月 outlook 約 54.7% bullish / 1.6% bearish。
- **聲量 (buzz volume)**: 以定性判斷。10 月目前無可檢索到的散戶熱潮報導, 聲量相較 5 月財報後與 6 月 Computex 高峰應屬較低。無法量化與歷史常態比較。
- **主要話題 (themes)**:
  - 多方: AI 資料中心與客製矽 (custom silicon) 成長; Investor Day 上調營收目標; Jensen Huang 背書; 分析師大幅上調目標價。
  - 空方: 光學業務市佔流失疑慮 (Barclays 稱為 "battleground stock"); 負債與指引 (guidance) 不確定性; 客戶轉單風險 (Microsoft / Broadcom); 估值 (trailing P/E 約 75, forward P/E 約 31, 依 yf info)。
- **Retail 語氣判定**: 最後一次可確認的散戶語氣為偏多 (5–6 月)。10 月散戶語氣 **無足夠資料判定**。

## Insider activity

統計區間: 2026-04-19 至 2026-10-18 (6 個月)。依 yf insider 交易文字 (Sale / Purchase) 統計。

- **Open-market 買入**: 0 筆, $0。
- **Open-market 賣出**: 13 筆, 約 **$20.67M**。
- 依人員:
  - CEO Matthew Murphy: 約 $8.59M, 約每月一次 7,500 股 (2026-05-13, 06-15, 07-15, 08-17, 09-15), 節奏規律; 可能為 10b5-1 計畫, 但 feed 未確認。
  - President Christopher Koopmans: 約 $8.28M, 每月約 10,000 股 (05-01, 07-01, 08-03, 09-01), 亦呈規律節奏。
  - Officer Sandeep Bharathi: 約 $2.46M (06-16, 07-16)。
  - CFO Willem Meintjes: 約 $0.70M (05-15)。
  - CFO Daniel Durn: 約 $0.63M (06-23)。
- 其他: 2026-04 至 09 期間另有大量 "無交易文字" 的資料列 (17 筆), 多為歸屬、扣繳或授予類, 未計入上述金額。
- 職稱異動: feed 中 CFO 於 2026-05 為 Meintjes, 2026-06 起為 Durn, 需於 SEC 文件確認。
- 區間賣出價: 約 $162–$299; 9 月賣價為 $203–$224。
- **淨方向: 淨賣出 (net selling), 無內部人買入。** 高階主管賣出為規律性質, 單看數字偏空, 但缺乏 open-market 買入使 insider 信號為中性偏空。

## Ownership shifts (institutional)

資料為 2026-06-30 季末 13F (yf major_holders / inst_holders)。

- 機構持股: 81.7% (2,952 家), 內部人持股 0.50%。
- 前幾大持股 (季度變化):
  - BlackRock: 85.6M 股 (9.77%), +34.1%
  - Vanguard Capital Management: 57.9M 股 (6.60%), +48.1%
  - FMR (Fidelity): 56.9M 股 (6.49%), **-56.6%**
  - State Street: 41.8M 股 (4.77%), +79.3%
  - Invesco: 30.3M 股 (3.45%), +5.1%
  - Geode: 21.1M 股 (2.41%), +67.9%
  - Vanguard Portfolio Management: 21.0M 股 (2.40%), -36.7%
  - Goldman Sachs: 14.7M 股 (1.68%), +30.7%
- **流向判定**: 被動與指數型機構 (BlackRock, Vanguard, State Street, Geode) 多數增持; 主動型 FMR 大幅減持。整體機構流向偏淨增持, 但主動基金有撤出訊號, 需與下一季 13F 比對確認。

## Net sentiment score

- **Composite: 偏多 (bullish), 信心中等偏低。**
  - 分析師 (權重最高): 偏多, 強。%BUY 91.3%, 平均目標價隱含約 49% 上漲空間, 近期上調幅度大。
  - 機構: 偏多 (被動增持為主), 主動基金撤出為反向訊號。
  - 內部人: 偏空 (淨賣出 $20.67M, 無買入), 但多數為規律性計畫賣出。
  - 散戶: 無法判定 (最後可確認為 5–6 月偏多, 10 月資料缺口)。
- **信心降低的原因**: 散戶 10 月資料缺口; 內部人淨賣出規模大; 股價由 Investor Day 後報導的 287.01 (日期未明) 回落至 227.83, 與分析師上調目標價形成反向, 此價格序列需以行情來源進一步確認。

**Divergence flag: 無法判定 (insufficient data)**。目前分析師與機構為偏多, 內部人為偏空。散戶 10 月語氣缺失, 無法確認散戶是否與分析師方向相反。若 10 月散戶轉為偏空, 可能形成 "分析師多 / 散戶空" 的背離, 屆時需再次檢查。

## 資料限制

- Reddit 與 StockTwits 直接端點 blocked; 散戶資料皆來自 WebSearch 間接報導, 日期多為 5–6 月, 非即時。
- yf `actions` 為空, 評級調整僅能依賴網路報導。
- 股價序列 (287 → 228) 與 cache 數據需交叉驗證。
- 下次財報日期: 2026-12-01 (EPS 預估 1.10), 位於本報告基準日之後。

SENTIMENT REPORT COMPLETE
