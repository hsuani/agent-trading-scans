# Sentiment — 6669.TW (緯穎 Wiwynn) as of 2026-10-08

> 資料限制: 本次任務指定 as-of 2026-10-08，但執行環境日期為 2026-10-07。可取得的最新分析師動態停在 2026-08 初，最新券商明確評等動作為 2026-07-24。散戶社群來源 (Reddit / StockTwits) 皆無法存取，屬 DATA_UNAVAILABLE。

## Analyst consensus

yfinance `rec_summary` (period 0m): **5 strongBuy / 14 buy / 0 hold / 0 sell / 0 strongSell**，共 19 家。
3 個月前 (-3m) 為 5 strongBuy / 13 buy，評等結構基本未變，僅多 1 家 buy。

網路來源的分歧:
- Investing.com 共識: Strong Buy，17–18 家，0 hold / 0 sell。
- Valueinvesting.io: 9 strong buy / 16 buy / 2 hold / 0 sell，仍為 BUY。
- 差異多半來自統計日期與計算口徑，方向一致: 幾乎全數買進，無賣出評等。

**目標價 (TWD)**
- Investing.com 平均 12 個月目標價約 7,569 (高 10,000 / 低 5,400)。
- Valueinvesting.io 平均約 6,685 (區間 4,732–8,925)。
- AlphaSpread 平均約 2,795，但頁面未標日期且引用股價明顯過時，視為不可用。

**近期評等動作 (依時間排序)**
| 日期 | 券商 | 評等 | 目標價 (TWD) | 備註 |
|---|---|---|---|---|
| 2026-05-08 | JPMorgan | Buy | 6,500 | 維持 |
| 2026-05-12 | Nomura / Instinet | Buy | 8,500 | 維持 |
| 2026-06 (月中) | 兆豐證券 | 買進 | 7,945 | 上調；看好 Trainium 3 平台 2027 年放量 |
| 2026-06-02 | Goldman Sachs | Buy (升評) | 7,147 | 升評 |
| 2026-07-09 | CLSA | Buy | 8,000 | 維持 |
| 2026-07-24 | Macquarie | Buy | 9,000 | 上調 (前值 6,500, 2026-05) |
| 2026-08 (初) | 美系外資 (來源未列明機構名) | 買進 | 10,000 | 上調 (前值 7,147)；2026–2028 EPS 上修，目標 P/E 由 15.8x 調至 20x；預估 2026–2028 營收 CAGR 32% |

- 2026-08 之後未找到新的升降評等紀錄 (DATA_UNAVAILABLE，需以券商研究報告或 MOPS 公告確認)。
- FactSet 調查 (日期不明) 的 21 家 2026 EPS 中位數為 348.72 元，對應目標價約 6,600 元，引用時需注意日期。
- 歷史上 2025-09 美系外資曾降評為「中立」，當日股價重挫，顯示評等變動對股價的敏感度高；此為舊事件，不計入當前評等結構。
- yfinance `recommendations` 回傳的仍是彙總統計，未提供逐家券商的升降評明細，因此逐筆 upgrade/downgrade 以網路來源為準。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: DATA_UNAVAILABLE。WebFetch 回報無法存取 www.reddit.com。WebSearch 未找到與 6669 相關的 Reddit 討論串，亦無法判定 tilt。
- **StockTwits / X**: StockTwits DATA_UNAVAILABLE (api.stocktwits.com 被 egress proxy 阻擋)。X 端無可用的 6669 近期貼文摘要。
- **PTT / 社群補充**: 未找到 2026-09 的 PTT 股板討論。CMoney 股市社群頁面 (股票 6669) 無日期標示，摘要顯示留言多數偏樂觀，同時有人提醒高檔回檔風險。此屬弱證據，無法確認時間與樣本量。
- **聲量 (buzz volume)**: DATA_UNAVAILABLE。無量化提及數；搜尋索引中未見 2026-09 至 10 月的明顯討論熱潮，此點僅為定性判斷。
- **Retail tilt**: 無法可靠判定，僅能依 CMoney 留言摘要判斷為偏多但分歧，信心低。

**Themes (依可得來源整理)**
- AI 伺服器 / ASIC 專案放量 (AWS ASIC、Trainium 3、GPU 機架)。
- 估值擴張: 外資把目標 P/E 由 15.8x 提高到 20x，市場關注是否已反映。
- 營收結構變化: 2026-04 起部分客戶改採「代採購模式」，記憶體不計入營收，2026-Q2 起營收規模預期收斂。Q1 2026 合併營收 2,765.08 億元 (年增 62%)，6 月單月 1,113.71 億元 (年增 29.8%)。
- 高檔回檔風險與股價波動: 近幾個月價格區間寬，單一快照之間差異大 (約 5,300–6,100 TWD)。

## Insider activity

- yfinance `insider`: 回傳空陣列 → **DATA_UNAVAILABLE** (Yahoo cookie/crumb 取得失敗，可能影響資料)。
- 網路來源: 玩股網 大股東頁面 2026-07-03 顯示「董監持股」36.77%，之後 2026-07-09 與 07-17 顯示 0.00%。此跳變與實際全數賣出不符，較可能是資料源口徑或欄位調整，無法確認，不採信。
- 公開資訊觀測站 (MOPS) 董監持股增減申報未取得，無法計算 6 個月淨買賣金額。

Net 6mo: DATA_UNAVAILABLE。Notable: DATA_UNAVAILABLE。

## Ownership shifts

yfinance `major_holders` (cached):
- insidersPercentHeld: 44.03%
- institutionsPercentHeld: 38.14%
- institutionsFloatPercentHeld: 68.15%
- institutionsCount: 342

yfinance `inst_holders`: 空陣列 → DATA_UNAVAILABLE，無法判定機構持股的季度趨勢。
玩股網持股分布快照 (2026-07-17): 欄位未標明，不做解讀。

## Net sentiment score

**Composite: bullish (信心: 低至中)**

- 分析師面: bullish，信心高。評等幾乎全為買進、無賣出，目標價多數高於近期成交價區間。但資料最新停在 2026-08，且評等與目標價來源彼此有差異。
- 散戶面: 無法判定 (DATA_UNAVAILABLE)。僅有弱證據偏多但分歧。
- 內部人面: 無法判定 (DATA_UNAVAILABLE)。
- 整體分數以分析師面為主，因此信心僅為低至中；缺少 Reddit、StockTwits、內部人與機構趨勢資料，無法作為完整的多源綜合結論。

**Divergence flag: 無法判定 (DATA_UNAVAILABLE)**
散戶 tilt 無可靠數據，無法檢驗是否與分析師方向相反。若日後取得 CMoney、PTT 或 MOPS 申報資料，應重新評估。

此報告為情緒彙整，不構成買賣建議。

SENTIMENT REPORT COMPLETE
