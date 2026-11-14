# Sentiment — POET as of 2026-11-15

資料時點: 以 2026-11-15 為準。2026-11-15 之後的資訊一律視為未知。yf 數據來源為 repo cache (`prices/yf/POET.json`, refreshed 2026-11-14T13:27 UTC), 屬預期行為。

## Analyst consensus
- **BUY% : 無法取得**。cache 內 `rec_summary` 與 `recommendations` 皆為全 0 (strongBuy/buy/hold/sell/strongSell 均為 0), 無法計算 buy/hold/sell 分布, 不應將全 0 解讀為「無覆蓋」。
- 二手彙整來源 (WebSearch, 非 yf, 日期不一, 需自行核對):
  - MarketBeat: 平均評級 "Sell", 平均目標價 $8.00 (引自 2026-03 前後文章)。
  - Benzinga: 共識目標價 $6.25。
  - TipRanks: Smart Score "Underperform"; 評級彙整為 1 買 / 1 賣 (單一來源描述, 樣本極小)。
  - Stockchase: 最新評級 "Don't Buy"; 另稱 Jim Cramer 於 2026-09-30 列為 Mad Money top pick (未經核實)。
  - Northland 維持 $8 目標; Weiss Ratings 為 "sell (d-)"。
- 近期升降評等: 搜尋未找到 2026 年中之後的升降評等紀錄。覆蓋家數少, 單一評等變動即可大幅改變共識。
- 整體分析師傾向: 偏空 (sell-leaning), 信心低 (樣本少、資料日期散落)。

## Retail social
- **Reddit**: 直接 JSON 端點 (r/wallstreetbets, r/stocks) 依規定未重試 (已封鎖)。改以 WebSearch 取得的最新可見資料為 2026-05 中旬前後:
  - 24/7 Wall Street (2026-05-28) 報導 r/wallstreetbets 情緒極度看多, 有貼文預測年底 $40; 情緒指數曾達 94 (5/15)。
  - 同一報導稱股價先由約 $7 衝到 $20 後大幅回吐, 單日跌 45%, 隨後出現集體訴訟。
  - 代表性短句 (WebSearch 摘要, 非原文): "Reddit crowd thinks Cramer is wrong"。
  - 近期 (2026-10 至 11) Reddit 貼文: **無法取得**。
- **StockTwits**: 直接 API 未取得資料 (依規定不重試)。WebSearch 僅見 StockTwits 新聞文章 (日期不明) 描述 "Bulls vs Bears" 與空頭部位上升的討論, 無法確認當前多空比例。
- **X / 新聞**: 2026-11 相關輿情搜尋結果少。allmind.ai 一則評論描述 11 月股價自 9 月 30 日水準回檔, 並稱屬 pre-revenue 公司常態。
- **Retail 聲量**: 無法量化。2026-05 前後為高點 (多篇報導), 2026-11 近期聲量資料不足, 不應推論為「低」或「高」。
- **Retail 傾向**: 無近期可靠讀數。歷史上 (2026 年上半) 偏多且極端, 但隨股價大跌後轉為質疑。
- **主要主題 (歷史可見)**:
  1. AI 光學網路 / 容量目標 (partnership 新聞驅動急漲)。
  2. 低價股高波動、"短擠壓" 與高空單比例 (Stocktwits 文章提及)。
  3. 股票推廣 (stock promotion) 指控: Wolfpack Research 相關報導, 股價當日跌近 10%; 散戶多數駁斥。
  4. 集體訴訟與 Cramer 不看好 vs Reddit 看多的對立敘事。

## Insider activity
資料範圍: cache 最後一筆交易為 2026-08-19; **2026-08-19 至 2026-11-15 之間無資料, 屬覆蓋缺口**。

以 2026-05-15 至 2026-11-15 計算 (cache 可見部分):
- **買入 (open-market buys)**: 0 筆可見。
- **公開市場賣出 (Disposition, 有價格者)**: 合計約 **USD 5.10M** (約 16 筆, 價格約 $5.84–$14.73/股)。
- 行權 (Exercise of options) 另有數筆, 價值約 USD 0.4M 量級, 未計入賣出總額; 無價格或僅 Grant 的紀錄 (如 Venkatesan 369,004 股、170,073 股) 未計入金額。

主要交易者:
| 日期 | 內部人 | 職稱 (yf 欄位) | 交易 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-05-20 | Barnes (Kevin) | Senior Officer | 賣出 @ $14.22–14.69 | 85,625 | 約 1.23 |
| 2026-06-05 | Jinyu (Mo) | Senior Officer | 行權後賣出 @ $10.82 | 60,000 | 約 0.70 |
| 2026-06-05 | Barnes (Kevin) | Senior Officer | 行權後賣出 @ $11.25 | 50,750 | 約 0.57 |
| 2026-06-03 | James (Lee) | Director/Senior Officer | 賣出 @ $14.39–14.57 | 34,375 | 約 0.50 |
| 2026-06-03 | Jinyu (Mo) | Senior Officer | 賣出 @ $14.65 | 30,000 | 約 0.44 |
| 2026-08-07 | Mika (Thomas R) | Senior Officer | 賣出 @ $8.93 | 45,799 | 約 0.41 |

解讀: 賣出集中於 2026-05 至 06 股價 $10–15 區間, 8 月 $8.9–9.5 亦有賣出。無內部人買進紀錄。

## Ownership shifts
- 機構持股 (`major_holders`): 機構持股比例約 **18.4%**, 內部人持股約 **0.11%**, 機構家數 191。
- 機構流向 (`inst_holders`, 前 10 大, 最新申報期 2026-09-30 或 2026-06-30):
  - 增持 6 家 / 減持 4 家 (依 pctChange 符號)。
  - 增持顯著者: Arrowstreet Capital (+84%, 1.10%→ 持股約 1.68M 股), Goldman Sachs (+25%, 2.31M 股), Jane Street (+6%, 5.94M 股, 持股 3.87%, 為最大持有人)。
  - 減持輕微: IMC-Chicago (-0.3%), Renaissance Technologies (-0.6%), Citadel Advisors (-0.6%)。
  - **機構流向: 前 10 大整體淨增持, 但幅度多數為小幅, 以量化/做市型帳戶為主, 非長線基金大幅建倉**。申報期不同步 (9 月與 6 月混合), 解讀需保守。

## Net sentiment score
- **Composite: 偏空 (bearish-leaning), 信心低 (low)**
  - 分析師: 偏空 (Sell/Underperform, 目標價約 $6–8, 樣本少)。
  - 內部人: 淨賣出約 USD 5.1M, 無買入, 屬偏空訊號。
  - 機構: 前 10 大小幅淨增持, 中性偏多。
  - 散戶: 無近期可靠讀數; 歷史為極端多頭後轉為質疑, 方向不明。
- **Divergence flag: 無法判定 (資料不足)**。若以歷史 (2026-05) 為準, 散戶偏多與分析師偏空分歧, 屬 divergence; 但目前缺乏 11 月散戶讀數, 無法確認是否仍分歧。

## 資料缺口與衝突
1. **股價衝突**: Stockchase 記 2026-11-06 收盤 $5.07; RTTNews 同日報導飆漲 28% 至 $18.46。兩者不可同時成立, 需以行情來源核對。機構持股每股市值約 $5.1 (2026-09-30 申報), 與 $5 區間較一致。
2. **財報日期衝突**: cache `earnings_dates` 為 2026-11-16 (13:00 UTC, 盤前), EPS 預估 -0.05; Earnings Whispers 曾列 11-12。以 11-16 為準 (多來源一致), 但該日期在 as-of 日之後, 結果視為未知。
3. Reddit / StockTwits 直接端點依規定未重試 (封鎖); 社群部分以 WebSearch 摘要替代, 日期多為 2026-05 或更早。
4. yf 分析師評等 cache 為全 0, 不應當作實際數據。

SENTIMENT REPORT COMPLETE
