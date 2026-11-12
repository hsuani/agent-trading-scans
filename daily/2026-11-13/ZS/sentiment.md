# Sentiment — ZS (Zscaler) as of 2026-11-13

資料截止日: 2026-11-13 (不使用此日之後資料)。金額單位: USD。

## Analyst consensus

分布 (yf rec_summary, 0m 快照): **7 Strong Buy / 29 Buy / 11 Hold / 0 Sell / 0 Strong Sell** (合計 47 家)。
Buy 系 (含 Strong Buy) 占 36/47 ≈ 77%；Hold 占 23%；無任何 Sell 評等。
Yahoo info 欄位 numberOfAnalystOpinions 為 45，與 rec_summary 合計 47 有 2 家差異，屬來源口徑不同，未調整。

趨勢 (近 3 個月):

| 期間 | Strong Buy | Buy | Hold | Sell | 合計 |
|---|---|---|---|---|---|
| -3m | 8 | 29 | 9 | 0 | 46 |
| -2m | 7 | 29 | 10 | 0 | 46 |
| -1m | 7 | 29 | 11 | 0 | 47 |
| 0m | 7 | 29 | 11 | 0 | 47 |

近況: 3 個月內淨變化為 Strong Buy -1、Hold +2、Buy 持平、Sell 維持 0。方向是評等往 Hold 微幅移動，尚未出現降評至 Sell 的情況。

目標價 (yf info 快取，45 家): 平均 235.19 / 最高 298.00 / 最低 164.75 (USD)。
對照快取現價 189.09 (USD)，平均目標價隱含上行約 24%。注意: 快取 info 的抓取時間戳未驗證，現價可能與 11-13 實際價格不同，此處僅作量級參考。

個別分析師升降評與目標價變動明細: DATA_UNAVAILABLE (yf recommendations 指令回傳的仍是 rec_summary 格式的趨勢表，沒有逐家機構的升降評紀錄)。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。依規定不直接抓取 Reddit；以 WebSearch 限定 reddit.com 網域時 API 回傳 400 (網域不可存取)，一般搜尋也未找到相關討論串。
- **StockTwits / X / 新聞聚合 (二手來源，WebSearch)**:
  - 2026-10-06 的 StockTwits 文章指出，即使網路安全股整體走強，ZS 在 StockTwits 的散戶情緒仍維持 "bearish"。
  - 另一篇 StockTwits 文章 (日期未明，內容與財報後急跌相符) 描述散戶在盤前大跌後逢低買進，認為被過度拋售。標題原句: "Retail rushes to buy the dip, calls selloff excessive" (約 9 字)。
  - TIKR 於 2026-11-06 與 11-10 的文章指出，ZS 一週內下跌約 14%，並把跌幅歸因於訂閱制資安股的整體拋售。
  - 聲量: 無量化提及數，DATA_UNAVAILABLE。定性判斷為近期媒體與散戶討論集中在 11 月初急跌，聲量中高於平常，但散戶原文不足，無法確認 StockTwits 實際提及數。
- **Retail tilt**: 混合偏空。偏空方以 10 月 StockTwits 情緒為主，逢低買進的聲音則出現在急跌後；兩者都是二手來源，信心低。

主要主題 (recurring themes):
1. FY27 ARR 指引: 年度 ARR 目標 $4.396B–$4.426B，隱含淨新增 ARR 約 $625M–$655M，被視為只略高於去年節奏。
2. AI 顛覆擔憂 ("SaaSpocalypse"): 市場擔心 AI 衝擊 SaaS 估值；公司 CEO 公開反駁，稱此說法被誇大。
3. 板塊連動拋售: 網路安全與訂閱制股票一起被拋售，有媒體舉 Fortinet 大跌為例。
4. 估值爭議: 媒體引用約 40x 前瞻本益比，爭論是否已可逢低買進。
5. 財報催化劑日期不一: Simply Wall St 列 2026-12-02，StockTwits 頁面列 11-27；yf earnings_dates 也列 2026-12-02。以 IR 頁面為準，本報告未能確認。

## Insider activity

期間 2026-05-13 至 2026-11-13 (6 個月)。來源: yf insider。

**淨額: $0 買入 / $14.94M 賣出 (Sale 共 23 筆)。** 期間內無公開市場買入 (Purchase) 紀錄。
行權 (Conversion of Exercise) 與股票授予 (Stock Award) 不計入買賣，但行權多與同日賣出配對，屬「行權後賣出」。

| 內部人 | 職位 (yf 欄位) | 賣出筆數 | 賣出金額 (USD M) | 最近一筆賣出 |
|---|---|---|---|---|
| GELLER ADAM | Officer | 6 | 8.57 | 2026-11-02, 1,041 股 @ 238.00 |
| RUBIN KEVIN E | Chief Financial Officer | 7 | 2.13 | 2026-10-26, 514 股 @ 253.26–261.27 |
| SCHLOSSMAN ROBERT S | Officer | 4 | 1.94 | 2026-09-21, 5,394 股 @ 200.00 |
| RICH MICHAEL J | Officer | 2 | 1.32 | 2026-09-16, 4,108 股 @ 192.76 |
| CHAUDHRY JAGTAR SINGH | Chief Executive Officer | 2 | 0.91 | 2026-09-16, 2,852 股 @ 192.76 |
| BEER JAMES ALEXANDER | Director | 2 | 0.06 | 2026-09-17, 177 股 @ 192.01 |
| 合計 | | 23 | 14.94 | |

值得注意的交易:
- **GELLER ADAM, 2026-10-12**: 賣出 25,000 股，約 $5.65M (價格區間 225.00–235.95)，同日行權 25,000 股 (行權價 205.61，約 $5.14M)。為期間內最大單筆。
- **CEO CHAUDHRY, 2026-09-16 與 2026-06-16**: 兩次賣出合計約 $0.91M，均在大批內部人同日出售時段。
- **CFO RUBIN, 2026-09-16**: 賣出 5,957 股，約 $1.15M，為 CFO 期間最大一筆。
- **2025 年大股東 MANGAL AJAY** (Beneficial Owner >10%): 2025 年有大額賣出 (如 2025-06-09 賣 120,000 股)，不在本 6 個月窗口內，僅作背景。

解讀限制: yf 欄位未標示是否為 10b5-1 計畫交易，無法判斷多數賣出是否屬預先排定。6 個月內無任何公開市場買入，此點為偏空訊號，但信心中低。

## Ownership shifts

yf major_holders 目前僅有單一快照:
- 內部人持股 (insidersPercentHeld): 34.68%
- 機構持股 (institutionsPercentHeld): 53.42%
- 機構佔流通股比 (institutionsFloatPercentHeld): 81.78%
- 機構家數 (institutionsCount): 1,231

**機構持股趨勢: DATA_UNAVAILABLE** (無前期快照，無法判斷增減)。
內部人持股 34.68% 偏高，可能包含創辦人與大股東，統計口徑未在工具輸出中說明。

## Net sentiment score

| 面向 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 中高 | 77% Buy、0 Sell、平均目標價隱含約 24% 上行；但近 3 個月 Hold 增加 2 家 |
| 散戶 (二手) | 混合偏空 | 低 | 10 月 StockTwits 偏空；急跌後有逢低買進聲音；Reddit 無資料 |
| 內部人 | 偏空 | 中低 | 6 個月 $14.94M 賣出、0 買入；多為行權後賣出，無法確認是否為計畫交易 |

**綜合: 中性 (信心: 中低)**。分析師面偏多，內部人與散戶面偏空或混合，三者相抵後無明確方向。

**Divergence flag: 是 (弱)**。散戶與內部人傾向偏空，分析師傾向偏多，方向相反。因散戶資料只來自二手來源、且有逢低買進的反向證據，此背離訊號強度低。

資料缺口:
- Reddit 討論串: DATA_UNAVAILABLE
- 個別分析師目標價與升降評明細: DATA_UNAVAILABLE
- 機構持股趨勢: DATA_UNAVAILABLE
- 散戶提及數量化: DATA_UNAVAILABLE
- 快取 info 現價與目標價的抓取時間戳未驗證
- WebSearch 找到的 Barchart 分析師口徑 (34 Strong Buy / 8 Hold / 1 Strong Sell) 來自 2025 年底文章，與 yf 當期數字不一致，未採用

SENTIMENT REPORT COMPLETE
