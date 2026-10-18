# Sentiment — AMD as of 2026-10-19

資料基準: 2026-10-19 (台北時間)。價格與評等快取更新於 2026-10-18 10:52 UTC (`prices/yf/AMD.json`)，即時 Yahoo 連線失敗，改用快取。快取價格 $528.75。2026-10-19 之後的資料一律視為未知。

## Analyst consensus

- 評等分布 (rec_summary, 0m): Strong Buy 5 / Buy 40 / Hold 11 / Sell 0 / Strong Sell 0，合計 56 家。
- **% BUY = 80.4%** ((5+40)/56)，Hold 19.6%，Sell 0%。
- 快取 `info` 另列 numberOfAnalystOpinions = 51，與 rec_summary 合計 56 不一致，原因未明，以 rec_summary 為準並標註。
- recommendationMean = 1.48 (Strong Buy 區間)。
- 目標價: 平均 $627.65 (較 $528.75 上行約 18.7%)；最高 $1,250、最低 $200。最低目標價明顯偏舊，參考價值低。
- 3 個月趨勢: BUY 類 (Strong Buy + Buy) 由 42 (-3m) 升至 45 (0m)，Hold 由 10 升至 11，Sell 始終為 0。評等結構穩定偏多，未見降評潮。

近期評等動態 (WebSearch，部分來源無日期，已依來源日期標註):
- 2026-06-11 BofA (Vivek Arya) 維持 Buy，目標價 $500 上調至 $560。
- 2026-06-12 Citi 由 Neutral 升至 Buy，目標價 $460 上調至 $575。
- 2026-05-04 HSBC 由 Buy 降至 Hold，目標價 $340 (與現價差距大，屬舊評等)。
- 2026-01 KeyBanc 升至 Overweight，目標價 $270 (已被後續價格遠超，屬舊評等)。
- 無法從來源確認 2026-10 的升降評等。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: 無法取得。WebSearch 未回傳該兩個版的 AMD 討論串，依規定未以 WebFetch 直接抓取 (Reddit 主機被封鎖)。本節無可引用樣本，tilt 無法判定。
- **StockTwits**: 單篇無日期的 StockTwits 新聞稿指出散戶情緒由 bullish 轉為 neutral，股價盤前走高時討論焦點為 $600 關卡。來源為聚合站，時效不明。另有 2026-08 的聚合站文章描述 AMD 情緒為「volatile / bearish-neutral」，但來源品質低、內容疑似模板化，權重低。
- **X / 新聞論壇**: 未找到 2026-10 的可靠散戶貼文摘要。Investing.com 使用者多空投票 (2026-08 初) 顯示 $484–$491 附近多空並存。
- **Buzz 量能**: 無可靠數據，無法與歷史基準比較。WebSearch 結果以 2026-08 及更早為主，未見 2026-10 的異常聲量報導，因此僅能定性判定為「無明顯放大訊號 (低信心)」。
- **主要主題 (依來源歸納)**:
  - MI400 / MI450 放量時程與是否延遲 (2026 年初曾有延遲傳聞，股價當日下跌超過 6%，後續有分析師反駁)。
  - 超大規模雲端客戶 (hyperscaler) 供應吃緊，伺服器 CPU 訂單能見度。
  - 毛利率壓力與 ROCm 軟體生態落後於 NVIDIA 的疑慮。
  - 內部人大量賣出的解讀 (多數認為是選擇權行權與預排交易計畫，但仍被散戶拿來當作看空論點)。
- 代表性散戶觀點 (標題式引述，非原文轉貼): "traders eye $600 level despite limited analyst upside"。

## Insider activity

視窗: 2026-04-19 至 2026-10-19 (近 6 個月)，最新一筆為 2026-09-15。

- **Net 6mo: $0 買入 / 約 $261.2M 賣出** (18 筆有金額之 open-market Sale；不含 Stock Gift 與選擇權行權轉換列)。
- 有 19 筆無金額欄位之交易未計入金額，多為行政人員代扣或制度性交易，需以 Form 4 核對。
- 過去 6 個月 **0 筆 open-market Purchase**。前一個 6 個月 (2025-10 至 2026-04) 賣出約 $105.1M，同樣無買入。最後一筆內部人買進為 2025-05-20 (Philip Guido，約 $1.0M)。

按人分類 (6mo 賣出金額):
| 人員 | 職稱 | 金額 (約) | 備註 |
|---|---|---|---|
| Lisa T. Su | CEO | $168.6M | 2026-05-13、06-10、08-18、09-10 等多筆大額賣出 |
| Mark D. Papermaster | CTO | $34.9M | 多筆行權後賣出 (行權價 $84.85) |
| Forrest E. Norrod | Officer | $25.0M | 行權後賣出 |
| Paul D. Grasby | Officer | $18.6M | |
| Jean X. Hu | CFO | $7.1M | 2026-08-25 |
| Nora M. Denzel | Director | $5.5M | 2026-06-02 |
| Ava M. Hahn | General Counsel | $1.5M | 小額 |

值得注意:
- CEO Su 在 2026-09-10 賣出 95,000 股 (約 $48.1M，價格區間 $503.72–$515.55)，同日另有 35,000 股贈與。
- CEO Su 的賣出呈現季度性節奏 (5 月、6 月、8 月、9 月)，可能屬預先排定計畫，需 Form 4 footnote 確認。
- 內部人持股比例僅 0.42%，賣出規模相對持股偏大，但實際佔比需股數基礎核對。

## Ownership shifts (institutional)

- 機構持股 75.3% (5,108 家機構)，內部人 0.42%。
- 前 10 大機構 (2026-06-30 13F，最新可得資料；Q3 13F 尚未揭露): **8 家增持、2 家減持**。
- 主要變動: JPMorgan +66.2%、FMR +67.2%、T. Rowe +24.6%、Invesco +5.4%、BlackRock +3.3%；State Street -0.6%、Geode -0.6%。
- 前 10 大合計淨增約 41.6M 股 (依 pctChange 推算，近似值)。
- 流向判定: **機構淨增持 (偏多)**。

## Net sentiment score

**Composite: 中性偏多 (信心: 中低)**

| 維度 | 判定 | 信心 |
|---|---|---|
| 分析師 | 偏多 (80.4% BUY，Strong Buy 區間，目標價高於現價) | 高 |
| 機構 | 偏多 (前 10 大 8 增 2 減，淨增持) | 中 (資料截至 2026-06-30) |
| 內部人 | 偏空 (6 個月 $261M 賣出、0 買進) | 中高 (但多為行權與計畫性交易，需 Form 4 核對) |
| 散戶 | 中性 (StockTwits 片段顯示 bullish 轉 neutral，Reddit 無資料) | 低 |

整體信心偏低，主因散戶與社群資料缺口大。

**Divergence flag: 弱分歧 (低信心)**
- 分析師與機構偏多，內部人持續賣出，散戶訊號偏中性且不完整。
- 若散戶確實轉為中性，則與分析師偏多形成弱分歧；但目前無法排除散戶數據過期。
- 建議下一輪補抓 Reddit (透過其他合法來源或手動) 與 StockTwits 當日 streams，以確認 tilt。

## Data gaps

- Reddit 完全無資料；StockTwits 僅一篇無日期片段，無法做當日情緒量化。
- 分析師評等的近期動態多數來自 2026-06 以前，2026-10 無新增評等資料。
- 內部人交易最新一筆為 2026-09-15，之後至 2026-10-19 之間的 Form 4 未在快取中。
- 機構持股最新為 2026-06-30，Q3 13F 尚未公布。

SENTIMENT REPORT COMPLETE
