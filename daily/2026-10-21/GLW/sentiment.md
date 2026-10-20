# Sentiment — GLW as of 2026-10-21

資料來源狀態: yf 工具 (rec_summary / insider / major_holders / inst_holders / recommendations) 皆取得 (`"source": "cache"`, 屬正常)。Reddit (r/wallstreetbets, r/stocks) 與 StockTwits 無法存取 (proxy 403 / DNS 解析失敗), 視為 DATA_UNAVAILABLE。WebSearch 結果多為 2026 年 3 月至 9 月的新聞與分析, 未找到 2026 年 10 月的散戶討論。

## Analyst consensus

目前 (rec_summary, period 0m): **13 buy / 5 hold / 0 sell** (strongBuy 0, strongSell 0), 合計 18 家。
過去四個月趨勢: buy 11 → 12 → 13 → 13; hold 5 → 4 → 5 → 5; sell 恆為 0。評等分布穩定偏多, 未見評等集中下調。

近期評等與目標價變動 (來自 WebSearch, 日期與數字未完全交叉驗證):
- JPMorgan 於 4 月下調至 Neutral。
- Truist 於 7 月回檔後由 Hold 升至 Buy, 目標價由 205 下調至 175 (理由為較高折現率與較弱的產業估值)。
- JPMorgan 與 Barclays 於 8 月前後下調目標價; MarketBeat 報告 8 月中共識目標價約 174.08 美元。
- 其他快照 (StreetInsider) 顯示平均目標價約 191 美元, 區間 12 至 270 美元, 最低值明顯為離群值。
- 來源間不一致: Barchart 8 月報告為 14 家 (9 Strong Buy / 5 Hold), 與 yf 的 0 Strong Buy 分類不同, 以 yf 數字為準。

財報前瞻: 下一次財報預估為 2026-10-27 (來源為估計, 非公司正式公告)。

## Retail social

- Reddit: DATA_UNAVAILABLE (r/wallstreetbets 與 r/stocks 搜尋端點無法存取)。
- StockTwits: DATA_UNAVAILABLE (api.stocktwits.com DNS 解析失敗)。
- X / 新聞討論: WebSearch 未找到可引用的 X 貼文或散戶留言。可用的間接指標:
  - 新聞摘要指出, 近一個月散戶推升的 GLW 空單部位增加超過 8% (來源品質中等, 未能獨立驗證)。
  - 9 月 14 日盤中下跌約 13%, 主因為公司公告一項最高 20 億美元的 at-the-market 股權銷售計畫, 疊加 AI 硬體族群賣壓。
- 聲量 (buzz volume) 相對一般水準: DATA_UNAVAILABLE。無法量化提及次數。
- 散戶偏向 (tilt): DATA_UNAVAILABLE。若以新聞標題語氣作代理, 2026 年 3 月至 9 月多為「估值重設」與「回檔買點」兩種論述並存, 無明確單邊傾向。

主要敘事 (來自新聞與分析文章, 非散戶原文):
- AI 資料中心光纖需求: 股價主要驅動因子, 3 月因 Broadcom CEO 淡化短期光纖需求而下跌約 7%。
- 估值與指數效應: 6 月曾因 FTSE Russell 納入成長指數而飆升, 之後回檔; 有分析指出本益比仍約 95 倍 (trailing) 且自由現金流波動大。
- 財報指引: 7 月 Q2 財報後 Q3 營收指引低於預期, 有報導指出單日下跌超過 20% (日期與幅度來源不一致, 僅供參考)。
- 融資與股權稀釋: 9 月的 ATM 股權銷售計畫成為短期賣壓來源。

## Insider activity

統計區間: 2026-04-21 至 2026-10-21 (6 個月)。統計口徑: 僅計 Value 有值的公開市場賣出 (Sale); 排除 Stock Gift、Stock Award、衍生性證券轉換 (Conversion of Exercise) 與無金額之 RSU 歸屬類紀錄。

Net 6mo: **$0 買入 / 約 $57.5M 賣出** (共 14 筆公開市場賣出, 無任何 P 類型公開市場買入)。

Notable:
- **Wendell P. Weeks (CEO)**, 2026-06-09: 行使 100,000 股選擇權 (履約價 27.03 美元) 後以 186.46 美元賣出, 金額約 18.6M 美元。
- **Steverson, Lewis A. (Officer)**, 2026-05-08 賣出約 5.44M 美元; 2026-08-28 再賣出約 1.98M 美元 (151.29 美元)。
- **Becker, Stefan (Officer)**, 2026-05-08 賣出約 3.95M 美元。
- **Schlesinger, Edward A. (CFO)**, 2026-05-07 賣出約 4.20M 美元。
- **Amin, Jaymin (CTO)**, 2026-05-22 賣出約 5.26M 美元。
- **Seetharam, Soumya (CTO)**, 2026-05-11 賣出約 4.12M 美元。
- **Nelson, Avery H. III (COO)**, 2026-05-15 賣出約 3.92M 美元。
- **Gullo, Michelle L. (Officer)**, 2026-09-04 賣出約 1.50M 美元 (152.29 美元), 為區間內最近一筆。
- 其他 5 月賣出者: Verkleeren (Officer, 2.08M 美元)、Zhang (Officer, 1.98M 與 2.77M 美元)、Tillman (General Counsel, 0.67M 美元)。

觀察:
- 賣出高度集中於 2026 年 5 月 (股價約 184 至 207 美元), 呈現多位高階主管同週期賣出的群聚特徵。
- 8 月至 9 月的賣出規模明顯較小, 價位約 151 至 152 美元。9 月 4 日後無新增紀錄。
- 2026 年 4 月 15 日、2 月 9 日等多筆無金額紀錄 (推測為 RSU 歸屬或稅務扣繳), 性質未確認, 未計入統計。
- 前一年 (2025 年) 同樣為淨賣出為主, 6 個月與 12 個月口徑一致偏空。
- 本段為事實整理, 不代表內部人士對股價的判斷。

## Ownership shifts

- 機構持股比例 (institutionsPercentHeld): 74.80%; 機構持股占流通股比例 81.36%; 機構家數 3,193。
- 內部人持股比例 (insidersPercentHeld): 8.07%。
- 前十大機構 (2026-06-30 季報):
  - BlackRock 7.63% (季變動 -1.42%)
  - Vanguard Capital Management 5.90% (+0.74%)
  - State Street 4.77% (+13.36%)
  - JPMorgan 4.18% (+203%, 基數低, 以 36.0M 股計)
  - Capital Research Global Investors 2.87% (+13.05%)
  - FMR 2.79% (-3.54%)
  - Vanguard Portfolio Management 2.20% (-33.08%)
  - Bank of America 2.17% (+29.18%)
  - Geode 2.13% (-12.41%)
  - Morgan Stanley 1.76% (-3.40%)
- 趨勢判讀: 僅單一季度快照, 無法確認連續趨勢。前十大中增持與減持家數接近, 整體集中度未見明顯跳升或下降。WebSearch 摘要提及近期機構資金流入明顯大於流出, 但未能用 yf 資料驗證。

## Net sentiment score

Composite: **中性偏空 (neutral-to-bearish)**, 信心度 **低至中**。

分項判讀:
- 分析師: 偏多 (13 buy / 5 hold / 0 sell), 但目標價在 7 至 8 月間下修, 且來源間目標價分歧大。
- 內部人: 偏空 (6 個月淨賣出約 57.5M 美元, 0 筆公開市場買入)。
- 散戶: DATA_UNAVAILABLE (Reddit 與 StockTwits 不可用)。新聞代理指標顯示波動大且有空單增加的訊號, 但不足以定調。
- 機構: 中性 (持股高度集中於指數型與主動型大型機構, 季變動方向分歧)。

權重說明: 因散戶端完全缺資料, 綜合分數主要依賴分析師與內部人兩項, 信心度因此受限。

Divergence flag: **是 (分析師與內部人方向相反)**。分析師評等維持偏多, 內部人在 2026 年 5 月與 6 月大量公開市場賣出 (包含 CEO 與多位 C 級主管), 並無買入紀錄。此背離值得留意, 但通常內部人賣出含有多種非投資判斷因素 (如選擇權到期、分散投資、稅務安排), 不宜單獨解讀為看空訊號。

散戶 vs 分析師的背離判斷: DATA_UNAVAILABLE, 無法判定。

## 資料缺口與限制

- Reddit / StockTwits: 無法存取, 散戶情緒與聲量完全缺失。
- X: WebSearch 未回傳可用貼文。
- 股價: 本報告未取得 2026-10-21 當日報價, 內部人交易價格與目標價僅作為歷史參考。
- 來源不一致: 分析師家數 (yf 18 家 vs Barchart 14 家)、目標價平均 (174 vs 191)、Q3 指引相關數字與單日跌幅幅度, 各來源說法不同, 以 yf 數字為準, 其餘僅列為參考。
- 財報日期 2026-10-27 為估計值。

SENTIMENT REPORT COMPLETE
