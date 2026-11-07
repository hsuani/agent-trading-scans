# News — ALAB as of 2026-11-08

**資料限制**
- `pipeline/tools/yf ALAB news` 回 403 (proxy 阻擋), 無法取得 yfinance 新聞列表。新聞改以 WebSearch 補充, 覆蓋度低於標準流程。
- `pipeline/tools/yf ALAB info` 可用 (快取時間 2026-11-07 12:53 UTC)。
- 多個來源的 Q3 數字彼此衝突 (見下方), 已分別標註。
- 所有項目日期均在 2026-11-08 以前。

## 價格脈絡 (USD)

| 項目 | 數值 (USD) |
|---|---|
| 2026-11-04 收盤 (TIKR 引述) | 222.76 |
| 2026-11-05 收盤 (由 yf previousClose 推得) | 179.47 |
| 2026-11-06 收盤 (yf) | 190.71 (+6.26%) |
| 52 週高 / 低 | 499.48 / 97.89 |
| 50 日 / 200 日均線 | 300.46 / 256.06 |
| 市值 | 33.3B |
| Beta | 3.86 |
| 分析師平均 / 中位目標價 | 343.17 / 350 (23 家, 最低 190, 最高 500) |

上表中 11-04 至 11-05 的價格落差約 -19%, 目前沒有找到對應的新聞解釋。這是本次最需要核實的數據。

## Top company-specific headlines (last 14d) (金額單位: USD M/B)

- 2026-11-03 — Q3 2026 財報: 營收 584.9M USD, 季增 49%, 高於公司自身指引 (540–560M) 與共識 (約 550.4M); 非 GAAP 毛利率 72.4%; 非 GAAP EPS 1.32, 高於共識 1.19 (Astera Labs press release 經 finviz 轉載; Zacks; 247wallst)。Impact: bullish。基本面全面超標, 且 Scorpio X-Series 已成為營收最大產品線。
- 2026-11-03 — Q4 2026 指引: 營收 730–750M USD (中位數季增約 27%), 非 GAAP EPS 1.62–1.66, GAAP EPS 1.13–1.17 (稀釋股數約 187M); 非 GAAP 營業費用 194–200M USD (Zacks; 247wallst)。Impact: bullish。指引幅度是本季最強的正面訊號。
- 2026-11-04 — 分析師評等分歧: Morgan Stanley 維持 Overweight, 目標價由 382 調至 389 USD; J.P. Morgan 維持 Overweight, 目標價 465 USD; RBC 由 500 下調至 400 USD (TIKR; Stock Track)。Impact: neutral。多數仍給買進評等, 但 RBC 調降顯示估值分歧。
- 2026-11-04 — 財報後股價反應分歧: 盤後下跌約 1.6%; 另有報導稱盤前大漲 5.24% 並歸因於目標價上調 (Stock Track 數據與其他來源不符, 可信度低)。一則報導指出股價在財報公告後數分鐘內即走弱, 並提到自 10 月高點回落約 43% (Stockopedia; TIKR)。Impact: bearish (價格反應)。基本面利多未能支撐股價, 市場可能在交易估值與板塊情緒。
- 2026-11-05 — 股價由 222.76 跌至 179.47 USD (由 yf previousClose 推得, 單日約 -19%)。未找到解釋此跌幅的獨立新聞。Impact: bearish (市場情緒)。此為需核實的數據點。
- 2026-10 (約 OCP 大會期間) — 發布 Orion 機架級參考設計, 基於 320-lane PCIe Gen 6 fabric, 針對 neocloud 與企業市場, 2027 年 Q1 起透過合作夥伴提供; Orion 1.0 僅支援 PCIe Gen 6 與 Open Rack, UALink 延後到未來世代 (Futurum; ConvergeDigest)。Impact: neutral。擴大可觸及市場, 但 UALink 延後可能讓重視 UALink 的投資人下修預期。
- 2026-05 至 2026-06 — 內部人持續減持: MarketBeat 引述過去三個月內部人賣出多於買入; COO 於 2026-05-12 有賣出紀錄 (MarketBeat)。Impact: bearish (弱)。屬例行性質, 權重低。
- 略過的雜訊: 股東大會通過董事與治理提案、各類持股機構的 13F 增減、純價格日報 (MarketBeat 類頁面)。

## Sector macro

- 2026-01-14 (背景, 超過 14 天) — Section 232 對部分進口 AI 晶片課徵 25% 關稅 (例如 H200、MI325X 等級); 白宮表示不適用於供美國資料中心使用的晶片。對 ALAB 直接影響有限, 主要針對經美國轉出口至中國的晶片 (WebSearch: investinglive; ajot)。
- 2026-01-15 (背景) — BIS 規則將 H200 / MI325X 等級晶片出口至中國的審查由推定拒絕改為個案審查 (Morgan Lewis)。Impact: 中性偏多, 對 ALAB 直接影響未知。
- 2025-12 公告、2027 年 6 月生效 (背景) — 中國半導體進口關稅延後執行 (ajot.com)。Impact: 中性, 時間較遠。
- 2026-10-27 至 10-28 — FOMC 會議 (Federal Reserve 官方日曆)。本次決議內容未查到。Impact: 未知。高 beta (3.86) 股票對利率與風險偏好變動敏感。
- 2026-10 OCP Global Summit (機架與 PCIe / UALink 標準相關) — 見 Orion 項目。
- 未查到 2026-11 的產業級關稅、出口管制、中美新規。本節資料為 2026-01 的背景, 屬資料缺口。

## Peer signals

- NVDA — 2026 年 FQ3 財報日未確認, 來源給出 11/17、11/18 或 11/25 三種說法 (Earnings Whispers、therighttrader 等)。若在 11/17–18, 將落在 14 天視窗內, 是 AI 資本支出情緒的重要催化劑。未找到 11 月的 NVDA 新聞。
- CRDO — 未找到 2026-11 新聞。背景: 宣布以約 7.5 億美元收購 DustPhotonics 以強化光學網路 (webull.ca; 日期未明); Zacks 評等 Strong Buy (nasdaq.com)。被視為直接競爭者 (主動電纜 AEC 與 ALAB 的 retimer 與連接產品重疊)。
- AVGO — 背景: FQ1 2026 AI 網路營收年增 60%, 占 AI 營收約三分之一, 管理層預期 FQ2 占比升至約 40%; Tomahawk 6 與 Jericho 4 為主要驅動 (nasdaq.com)。AVGO 的 Tomahawk 與 Scorpio 之間為直接競爭關係; AI 網路需求的正面訊號對 ALAB 有間接利多。
- MRVL — 背景: 定製 AI 晶片業務預期年增至少一倍, 並透過 Celestial AI、Polariton 收購擴充 scale-up 網路與光學 (Motley Fool 2026-05 引述; webull.ca)。Zacks 評等 Hold。
- 所有同業的 2026-11 股價或財報動態都未找到, 無法判斷 ALAB 的股價下跌是否為板塊性 (屬資料缺口)。

## Forward calendar (next 14d, 2026-11-08 至 2026-11-22)

- 2026-11-10 (週二) 08:30 ET — 美國 10 月 CPI (Thrive in Markets 與 financecalendar 日期一致)。Expected impact: 高 beta 成長股對通膨與利率路徑的反應較大。
- 2026-11-17 或 11-18 (未確認) — NVDA FQ3 財報 (日期來源衝突, 亦有 11-25 說法)。Expected impact: AI 基礎設施資本支出訊號, 對 ALAB 的情緒影響可能大於基本面影響。
- 2026-11-20 (週五) — 11 月月度選擇權到期日 (計算日期, 非新聞)。Expected impact: 波動率與 gamma 相關的短期影響, 對高空頭比例與高波動的股票較為顯著。
- 無已知 ALAB 個股事件 (財報下次在 2027 年初, 不在視窗內; 無已宣布的股東會、解鎖或產品發表日期)。
- 未驗證: MarketBeat 頁面提及 ALAB 為 S&P 500 候選 (來源日期不明, 日期推測為 2026-06)。若屬實, 季度調整公告可能落在 12 月初 (視窗外), 僅列為待查項目。

## Net read

ALAB 近期的基本面新聞整體偏多: Q3 營收 584.9M USD 與非 GAAP EPS 1.32 同時超越自身指引與共識, Q4 指引 730–750M USD 中位數季增約 27%, 而且 Scorpio X-Series 已成為最大營收產品線, Orion 也擴大了 neocloud 的可觸及市場。分析師多數仍維持買進 (平均評等 1.8, 平均目標價約 343 USD), 只有 RBC 明顯下調。然而市場對這些利多的反應明顯偏弱: 盤後與盤前反應不一, 11-04 至 11-05 的股價落差 (約 -19%, 未找到獨立新聞解釋) 與 52 週高點相比仍跌約 62%, 而且 Beta 高達 3.86, 表示價格受板塊與市場情緒影響較大。綜合判斷: 新聞面淨傾向偏多 (基本面強, 幅度大), 但價格相關訊號呈分歧 (市場反應偏負面, 幅度大), 整體屬於 mixed。必須先核實 11-05 的跌幅與 Q3 的 EPS 數字, 才能確定是基本面弱於市場預期, 還是只是情緒與估值問題。

## 資料品質與待核實項目

- Q3 數字衝突: Zacks、247wallst、finviz 稿件標題給出營收 584.9M USD 與非 GAAP EPS 1.32; Stockopedia 的簡訊則寫 adjusted EPS 0.23 (對共識 0.17); Stock Track 另稱 Q3 營收 230.58M。以 584.9M 與 1.32 為主要採用值, 但建議以 SEC 8-K 或 IR 新聞稿核實。
- YoY 數據不一致: 來源提到 Q3 營收年增 154%、Q1 2026 營收年增 93%, 但與 2025 年實際營收基期不符。本報告不採用 YoY 數字, 僅採用季增與指引。
- 股價路徑: 11-04 222.76 (TIKR)、11-05 179.47 (yf 前收推得)、11-06 190.71 (yf) 三者需由行情源核實。
- 52 週高點 499.48 USD 與 "自 10 月高點回落約 43%" 的敘述不一致; 若 10 月高點約 333 USD 則兩者可以相容, 但仍需確認。
- 其他 WebSearch 結果中的 "346.33"、"417.07" (2026-06-18) 等快照價格與 11-06 的 190.71 並不衔接, 不用於本報告的價格判斷。

NEWS REPORT COMPLETE
