# Sentiment — SO as of 2026-11-24

資料基準：yf 工具回傳之最新快照（rec_summary、major_holders、inst_holders 為 2026-09-30 報告期；insider 為 2026-11-06 前最新申報）。Yahoo cookie/crumb 抓取失敗，已使用快取回退（normal fallback）。最近收盤價參考 2026-11-17 約 $93.60。retail 社群原文搜尋未取得 2026-11 之實質內容，相關段落標示 DATA_UNAVAILABLE。

## Analyst consensus

yf 最新 rec_summary（0m，共 23 位分析師）：1 Strong Buy / 7 Buy / 12 Hold / 2 Sell / 1 Strong Sell，即 **8 buy-side / 12 hold / 3 sell-side**。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 買方合計 | 賣方合計 |
|---|---|---|---|---|---|---|---|
| 0m（最新） | 1 | 7 | 12 | 2 | 1 | 8 | 3 |
| -1m | 1 | 7 | 13 | 2 | 1 | 8 | 3 |
| -2m | 1 | 6 | 14 | 2 | 0 | 7 | 2 |
| -3m | 1 | 6 | 13 | 2 | 1 | 7 | 3 |

- 解讀：三個月內持有評等由 13 增至 12 之間，買方合計由 7 微增至 8，屬小幅偏多移動，整體仍以 Hold 為主。
- 注意：`recommendations` 指令回傳的內容與 `rec_summary` 相同（僅彙總趨勢），**未提供逐家券商升降評等明細**。個別動作來自 WebSearch 新聞彙整，見下。
- 近期個別動作（WebSearch，來源為 aggregator 頁面，未逐一核對原始券商報告）：
  - Citigroup 維持 Buy，目標價由 $114 下調至 $104（2026-09-25）。
  - Morgan Stanley 維持 Underweight，目標價由 $89 下調至 $85（2026-09-18）。
  - Evercore ISI 由 In-Line 升至 Outperform（2026-03-05）；KeyBanc 由 Underweight 升至 Sector Weight（2026-03-04）。
  - Jefferies 維持 Neutral；Fintel 平均一年期目標價約 $102.11。
- 與 aggregator 不一致：Benzinga 顯示 28 位分析師、共識 Neutral；StockAnalysis 於 2026-03 顯示 17 位、Hold、平均目標價 $98.78。各來源樣本數不同，本報告以 yf 的 23 位為準。

## Retail social

- Reddit：DATA_UNAVAILABLE。WebSearch 未找到 r/wallstreetbets 或 r/stocks 2026-11 的 SO 相關討論串。依任務指示未使用 WebFetch 抓取 Reddit JSON。
- StockTwits / X：DATA_UNAVAILABLE。未取得 2026-11 的貼文或推文；未進行 StockTwits API 抓取。
- 聚合來源（低可信度，僅供參考）：
  - AltIndex 社群情緒分數 100/100，百分位 93；但其月度歷史只到 2025-12，可能已過時。
  - TipRanks 標示 "Very Positive"，但其數據為持有人組合比例（約 0.3% 散戶持有），未說明是看多或僅持有。
- 聲量（volume）：無可比較之提及次數資料，定性判斷為「低，無法量化」。
- 主要主題（來自新聞與聚合頁，非社群原文）：
  - Q3 財報 EPS 優於預期（報告日 2026-11-05），股價反應有限（約 +0.2%）。
  - 股息穩定（$0.76，除息日 2026-11-16），主打 25 年連續加息的防禦型公用事業敘事。
  - 負債與大型工程執行風險是常被提及的反方論點。
  - 散戶估值分歧大（Simply Wall St 社群合理價區間約 $4 至 $97，樣本少，不具代表性）。

## Insider activity

統計區間：2026-05-24 至 2026-11-23（近 6 個月）。

- 公開市場買入（Purchase）：**0 筆**。
- 公開市場賣出（Sale，有價格）：**11 筆，合計約 $1.19M（USD）**。
- 其他（Award、Gift、無價格紀錄）：不計入買賣金額。

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額（USD） |
|---|---|---|---|---|---|
| 2026-11-06 | SPAINHOUR STERLING A. JR. | Officer | Sale @ $91.81 | 3,333 | 306,003 |
| 2026-11-02 | KIM MATTHEW M. | Officer | Sale @ $93.39 | 100 | 9,339 |
| 2026-10-01 | KIM MATTHEW M. | Officer | Sale @ $82.73 | 100 | 8,273 |
| 2026-09-03 | SENA PETER P III | Officer | Sale @ $88.59 | 4,266 | 377,925 |
| 2026-09-03 | KIM MATTHEW M. | Officer | Sale @ $88.87 | 1,400 | 124,418 |
| 2026-09-01 | KIM MATTHEW M. | Officer | Sale @ $88.45 | 100 | 8,845 |
| 2026-08-06 | SPAINHOUR STERLING A. JR. | Officer | Sale @ $94.02 | 3,333 | 313,369 |
| 2026-08-03 | KIM MATTHEW M. | Officer | Sale @ $94.28 | 100 | 9,428 |
| 2026-07-01 | KIM MATTHEW M. | Officer | Sale @ $95.77 | 100 | 9,577 |
| 2026-06-01 | KIM MATTHEW M. | Officer | Sale @ $91.16 | 100 | 9,116 |
| 2026-05-01 | KIM MATTHEW M. | Officer | Sale @ $96.57 | 100 | 9,657 |

- 無價格紀錄之項目：2026-06-26 SENA PETER P III（712 股）、2026-05-22 WOMACK CHRISTOPHER C.（CEO，7,662 股）。交易代碼在資料中為空，無法判定是否為稅務扣繳或其他非市場交易，標示為待確認。
- 重點觀察：
  - CEO WOMACK 在區間內無公開市場賣出紀錄（僅 2026-05-22 一筆無價格項）。
  - 賣出主要集中於 KIM MATTHEW M.（約每月 100 股之小額、規律性賣出，符合預先安排交易型態的常見特徵，但資料無法證實）與 SPAINHOUR（兩次約 3,333 股）。
  - 2026-02 之大量 Stock Award 屬薪酬授予，不計入買賣判斷。
- 內部人持股比例約 0.095%（insidersPercentHeld），金額相對市值（約 109 B USD）極小。
- 換算檢核：BlackRock 持股 97.37M 股 / 8.36% ≈ 1.165 B 股；乘以 $93.60 ≈ 109 B USD，與 BlackRock 申報市值 9.05 B USD / 97.37M 股 ≈ $92.96/股 相符。

## Ownership shifts

- 機構持股比例：73.58%（institutionsPercentHeld），機構家數 2,790。
- 前十大持有人（2026-09-30 報告期）合計約 40.4%，以指數型與被動資金為主：

| 持有人 | 持股比例 | 股數（M） | 季度變動 |
|---|---|---|---|
| BlackRock Inc. | 8.36% | 97.37 | +4.71% |
| Vanguard Capital Management | 6.40% | 74.54 | +1.19% |
| State Street Corp | 5.88% | 68.44 | +5.60% |
| Capital World Investors | 5.27% | 61.33 | -1.90% |
| T. Rowe Price Associates | 3.30% | 38.37 | -17.33% |
| JPMorgan Chase & Co | 2.84% | 33.02 | +0.74% |
| Geode Capital Management | 2.61% | 30.42 | +3.75% |
| Vanguard Portfolio Management | 2.35% | 27.42 | +1.45% |
| FMR LLC | 1.91% | 22.24 | -1.31% |
| Franklin Templeton | 1.48% | 17.18 | +3.73% |

- 趨勢：十大中 7 家增持、3 家減持（Capital World、T. Rowe、FMR）。T. Rowe 減持幅度最大（-17.33%），屬主動型基金的明顯降倉；被動機構（BlackRock、State Street、Geode）則持續加碼，多屬指數與資金流入驅動。
- 結論：機構持股集中度穩定，無明顯撤出跡象；主動型資金出現分化。

## Net sentiment score

- 分析師面（權重高）：中性偏多。8 買 / 12 持有 / 3 賣，三個月買方家數微增，但 Citigroup 與 Morgan Stanley 近期目標價下調，且平均目標價約 $102 高於近期股價約 $93.60。
- 內部人面：中性偏空（輕微）。6 個月約 $1.19M 公開賣出、0 買入，但金額小、規律性強，且 CEO 無公開市場賣出。
- 機構面：中性偏多。持股穩定，被動資金持續增持，主動型有分化。
- 散戶面：DATA_UNAVAILABLE。聚合來源偏正面，但樣本與時效不足，不納入加權。
- **綜合判定：中性（neutral），信心：中低（low-to-medium）**。主要理由：分析師與機構結構均偏中性，內部人賣出幅度小，散戶面無可用的 2026-11 實證。

**Divergence flag：無法判定（no usable retail data）**。分析師傾向為中性偏多，但缺乏逐期散戶貼文，無法確認兩者是否反向。若日後取得 Reddit 或 StockTwits 資料，應重新評估。

## Data gaps and caveats

- `recommendations` 無逐家券商明細，個別評等變動依賴 WebSearch 聚合頁，未核對原始報告。
- 分析師家數在 aggregator 間不一致（yf 23、Benzinga 28、StockAnalysis 17）。
- Q3 EPS 預期值來源不一（$1.71 與 $1.76），實際值為 $1.94，兩者皆顯示為超預期。
- 資料日期為 2026-11-24，但執行環境日期為 2026-11-23；最新價格與持股資料分別停在 2026-11-17 與 2026-09-30。
- Yahoo cookie/crumb 抓取失敗，已使用快取回退。

## Summary table

| 面向 | 結論 | 信心 | 關鍵數據 |
|---|---|---|---|
| 分析師共識 | 中性偏多 | 中 | 8 買 / 12 持有 / 3 賣（yf 23 家）；三個月買方 7 到 8 |
| 目標價動向 | 近期下調 | 中 | Citi $114 到 $104；MS $89 到 $85；平均約 $102 |
| 內部人交易 | 中性偏空（輕微） | 中 | 6 個月 0 買 / 約 $1.19M 賣（USD）；CEO 無公開市場賣出 |
| 機構持股 | 中性偏多 | 中高 | 73.6% 機構持股；十大 7 增 3 減；T. Rowe -17.3% |
| 散戶社群 | DATA_UNAVAILABLE | 低 | Reddit、StockTwits、X 2026-11 無實質內容；聚合來源偏正面但過時 |
| 綜合情緒 | 中性 | 中低 | 散戶面缺失，分歧旗標無法判定 |

SENTIMENT REPORT COMPLETE
