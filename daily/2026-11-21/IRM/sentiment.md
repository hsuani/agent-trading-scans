# Sentiment — IRM as of 2026-11-21

資料基準：股價參考為 2026-11-20 收盤 $107.33（取自同日 market.md）。2026-11-21 之後之資料一律視為未知。單位：USD，市值與金額以 B / M 表示。

## Analyst consensus

rec_summary（yf，當期快照）：12 位分析師，4 Strong Buy / 7 Buy / 0 Hold / 1 Sell / 0 Strong Sell，即約 11 買 / 0 持有 / 1 賣。近 3 個月之評級分布由 -3m 之 4 Strong Buy / 6 Buy / 1 Sell 增至當期之 4 Strong Buy / 7 Buy / 1 Sell，即新增 1 檔買進評等，未見降評。yf 的 recommendations 端點回傳與 rec_summary 相同之彙總，未提供逐筆升降評等紀錄，因此下列升降評等資訊來自 WebSearch，未逐筆核對原始券商報告。

近期目標價變動（WebSearch 彙整，來源之間數字不一致）：
| 日期 | 機構 | 動作 | 評等 |
|---|---|---|---|
| 2026-04-21 | Wells Fargo | PT $125 → $135 | 維持正面 |
| 2026-05-01 | JPMorgan | PT $121 → $138 | Overweight |
| 2026-07-01 | Barclays | PT → $143（另一則標題為 $123 → $126，時間不明） | Overweight |
| 2026-07-25 | Wall Street Zen（量化評等，非傳統券商） | buy → hold | 降評 |
| 2026-08-06 | Wells Fargo | PT $135 → $140 | 維持正面 |
| 2026-08-27 | Truist | PT → $155（另一表格顯示為 $140，待核） | 維持正面 |

- 共識目標價各來源差異大：Benzinga 平均 $126；Barchart 平均 $134（Street-high $153）；TipRanks 近 3 個月 9 位分析師平均 $125.57；Google Finance $146.57（資料為 2026-08）；Simply Wall St 公允價值約 $141。
- 以 $126 平均目標價計算，相對 $107.33 約 +17%；以 $134 計算約 +25%。
- 2026 年內未找到 sell-side 之正式降評紀錄，唯一降評為量化服務。
- 11-05 財報後，部分來源指出第四季與全年營收指引低於市場預估，分析師多數維持買進評等，但需留意評等更新可能尚未反映於 rec_summary 快照。

## Retail social

- Reddit：r/wallstreetbets 之 WebFetch 被阻擋（DATA_UNAVAILABLE，無法直接取得 JSON 搜尋結果）。r/stocks 同樣無法取得。以 WebSearch 找到的最具代表性討論為 2024-08-19 之 WSB 空方盡調貼文（約 1.4k upvotes、290 則留言），主張估值過高、P/E 約 140、質疑資料中心策略與負債，但此貼文距今已逾兩年，不代表當前情緒。留言中有反駁，指出 REIT 應以 FFO 衡量。
- 2026 年近期 WSB / r/stocks 之 IRM 討論：DATA_UNAVAILABLE（搜尋未找到）。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗，屬沙箱網路白名單限制），DATA_UNAVAILABLE。
- X / 其他聊天：AltIndex 頁面顯示 X sentiment 86/100 Bullish，但頁面未標示更新日期，僅供參考，未能與 2026-11 之貼文交叉驗證。MarketBeat 之 WSB 熱門股工具未顯示 IRM 近期提及次數。
- 提及量（buzz volume）：DATA_UNAVAILABLE。無法做出與典型水準之定量比較。
- 主要主題（由新聞與搜尋結果歸納，非來自社群原文）：
  1. AI 資料中心需求：Q3 資料中心營收年增 34%（前幾季為 47%、39%），增速放緩仍是多方論點。
  2. 11-05 財報後暴跌：當日跌約 11%（部分來源誤差，早盤報 7%），Q3 AFFO 優於預期但營收指引偏弱。
  3. 估值與槓桿：空方主要論點，包括 P/E 偏高與槓桿、現金流品質質疑。
  4. 空方報告：Gotham City Research 之做空報告，一則來源指 11-19 當日股價下跌 2.9%。報告日期與內容僅一則來源提及，需待核實。
  5. 政策與選址阻力：中期選舉後地方對資料中心選址之限制（德州、俄亥俄、喬治亞），被視為風險。
- 引述（≤15 字，僅示意主題）：來源標題「revenue guidance falls below forecasts despite q3 earnings beat」（finviz 新聞標題）。

## Insider activity

6 個月區間 2026-05-21 至 2026-11-21：
| 人員 | 職務 | 交易性質 | 金額 (USD M) |
|---|---|---|---|
| William L. Meaney | CEO | 賣出（約每月一次，每次約 38,474 股） | 27.02 |
| Greg W. McIntosh | Officer | 賣出 | 3.22 |
| Mark Kidd | Officer | 賣出 | 2.94 |
| Daniel Borges | Officer | 賣出 | 0.90 |
| 合計 | | 買入 $0.00M / 賣出 $34.09M | 淨賣出 ≈ $34.09M |

- 買入：6 個月內無公開市場買入紀錄（DATA_UNAVAILABLE 不適用，為確認無買入）。
- 董事 Walter C. Rakowich 於 2026-11-12 有 5,000 股贈與（Stock Gift，價值 0），非交易性買賣。
- Meaney 之賣出多與 $37.00 之選擇權行權（Conversion of Exercise）配對出現，屬例行性結構。推測為預定交易計畫（10b5-1）之例行執行，但資料本身未標示此計畫，屬推論，需核實。
- 最近一筆大額賣出：Meaney 2026-11-06 賣出 38,474 股，價格 $104.08–106.62，金額 $4.07M。以股數 × 價格驗算：38,474 × ~$105.4 ≈ $4.05M，與工具回傳值一致。
- 內部人持股比例 0.88%（yf major_holders）。

## Ownership shifts

- 機構持股比例：87.88%（institutionsPercentHeld），機構數 1,594 家（yf major_holders）。
- 前十大（2026-09-30 報告期，13F 資料）：
| 機構 | 持股比例 | 持股股數 (M) | 季變化 |
|---|---|---|---|
| BlackRock | 10.91% | 32.49 | -3.2% |
| Vanguard Portfolio Mgmt | 8.59% | 25.58 | +0.05% |
| Vanguard Capital Mgmt | 6.38% | 18.99 | +0.2% |
| State Street | 5.73% | 17.08 | -3.1% |
| Cohen & Steers | 3.81% | 11.35 | -5.5% |
| Geode Capital | 2.98% | 8.88 | +2.7% |
| Wellington Management | 1.85% | 5.52 | 大幅增持（pctChange 9.76，單位待核） |
| FMR | 1.77% | 5.26 | -0.3% |
| Morgan Stanley | 1.66% | 4.94 | +0.1% |
| Dimensional Fund Advisors | 1.57% | 4.67 | +0.01% |

- 市值推算：BlackRock 持股 32.49M 股 / 10.91% ≈ 297.8M 股流通股，× $107.33 ≈ $32.0B。yf 之 Market Cap 27.73B 為早期快照，已過時，不採用。
- 解讀：前十大中多為指數型與被動基金，持股比例大致穩定；Cohen & Steers 等主動型基金有減碼跡象，Wellington 有明顯加碼。整體機構結構未見大規模撤出。

## Net sentiment score

- 分析師面：**偏多**（信心：中高）。11 買 / 1 賣，目標價均高於現價，但 rec_summary 與各來源之目標價差異大，且未見 2026 年 sell-side 降評。
- 散戶面：**無法判定**（信心：低）。Reddit、StockTwits 皆 DATA_UNAVAILABLE；唯一可用之散戶資料為 2024 年之空方貼文與無日期之 X 情緒指標（86 Bullish），兩者互相矛盾且時效不一。
- 內部人面：**偏空 / 中性**（信心：中）。6 個月 $34.09M 純賣出、零買入，且 CEO 為主要賣方。但多數屬例行執行，訊號強度有限。
- 機構面：**中性**（信心：中）。前十大變化小、無大規模撤出。
- 價格與市場情緒面（補充）：股價跌破 MA20 / MA50 / MA200，11-05 財報後大跌，11-19 空方報告後續跌，短期情緒偏弱。

**綜合判定：中性（信心：低至中）**。分析師與機構結構偏穩定正面，但內部人持續淨賣出、財報後市場重新定價與空方報告構成情緒壓力，散戶端資料缺失。

**Divergence flag：是**。分析師評等整體偏多，與內部人淨賣出及股價走勢偏弱方向相反。散戶傾向因資料缺失無法判定，因此無法確認是否也存在相同分歧。此分歧本身可作為後續追蹤重點，但不構成交易建議。

資料缺口與限制：
- Reddit（WebFetch 被阻）、StockTwits（DNS 失敗）、2026 年內社群提及量皆為 DATA_UNAVAILABLE。
- 分析師目標價來源數字不一致，未能確定當前共識目標價之精確值。
- Gotham 空方報告之日期與影響僅一則來源提及。
- yf 工具無 `ratings` 子命令，改用 `rec_summary` 與 `recommendations`，後者未提供逐筆評等變動。

SENTIMENT REPORT COMPLETE
