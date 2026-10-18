# Fundamentals — CCXI as of 2026-10-19

> **實體核對警示**: 任務指定 CCXI 為 Chimerix, 但 yfinance 回傳的 CCXI 為 **Churchill Capital Corp XI** (NASDAQ GM, 空白支票公司 / SPAC, 紐約)。Chimerix 的 ticker 為 CMRX (據模型知識, 該公司已於 2025 年被 Jazz 收購, 未經本次工具驗證)。insider 資料亦出現 Chimerix 時代高管名稱 (Schall, Kanaya, Cappel), 疑似資料錯置。本報告以工具回傳的 Churchill Capital Corp XI 為分析對象。
>
> 資料時點: 最新收盤價為 2026-10-16 (regularMarketTime), 快取時間 2026-10-18。未發現 2026-10-19 之後的資料。

## Executive summary
CCXI 為無營收、無營運的 SPAC, 財務健康度應以信託帳戶 (trust) 規模、現金與負債結構、以及併購條件評估, 傳統獲利與現金流指標大多 n/m。2026-06-30 季報顯示 trust 約 420.9M 美元、現金僅 1.25M、流動負債 137.8M 來源不明、單季淨損 -134.7M, 且 insider 資料為過期紀錄, 資料完整性不足。以 41.9M 股推估 trust 每股約 10.05 美元, 最新價 10.66 美元 (溢價約 6%) 估值接近 trust NAV, 吸引力取決於併購結構與股東贖回率。

## Revenue & profitability
- **營收**: 2025Q3 / 2026Q1 / 2026Q2 季度 Total Revenue 皆為 0.0。yfinance annual financials 回傳空陣列, 無法計算 3-5 年 CAGR。
- **毛利 / 營業利益率 / 淨利率**: info 的 grossMargins, operatingMargins, profitMargins 皆為 0.0, 無經濟意義, 標記 n/m。
- **營業費用 (季度)**:
  - 2026Q2 Operating Expense 39.77M, 其中 Other Operating Expenses 39.07M (來源未揭露), G&A 0.69M。
  - 2026Q1 Operating Expense 0.37M。
  - 2025Q3 Operating Expense 0.05M。
- **非營業項目**:
  - 2026Q2 Other Non Operating Income/Expense -98.70M。
  - 2026Q2 利息收入 (trust 投資收益) 3.79M; 2026Q1 為 3.55M。
  - 以 Q2 利息收入 3.79M 年化、除以期間 trust 平均值約 419.5M, 推算 trust 收益率約 3.6% (估算)。
- **淨利潤 (季度)**: 2026Q2 -134.68M; 2026Q1 +3.17M; 2025Q3 -0.05M。2025Q4 資料缺漏, 無法計算完整 TTM。
- **EPS (季度, diluted)**: 2026Q2 -2.42; 2026Q1 +0.06; 2025Q3 -0.001。
- **ROE / ROIC**: n/m。權益由 2025-12-31 的 399.8M 降至 2026-06-30 的 268.3M, 主要受 Q2 淨損影響, 不具業務意義。

## Cashflow & balance sheet
**現金流**
- 2026Q2 Operating CF -0.16M; 2026Q1 -0.33M; 2025Q3 0.00M。FCF 同為負或零, FCF margin n/m。
- FCF / NI: n/m (NI 為負或接近零)。trust 利息收入計入淨利但不屬於營運現金流, 故現金流品質指標不適用。
- info 的 operatingCashflow (TTM) 為 -1.08M。
- annual cashflow 回傳空陣列, 無法與年度 NI 比對。

**資產負債表 (2026-06-30 季報)**
| 項目 | 2026-06-30 | 2026-03-31 | 2025-12-31 (年報) |
|---|---|---|---|
| Cash | 1.25M | 0.41M | 0.74M |
| Trust (Other non-current assets) | 420.88M | 418.09M | 414.55M |
| Total assets | 422.64M | 419.11M | 415.91M |
| Total liabilities | 154.36M | 16.15M | 16.12M |
| Current liabilities | 139.87M | 0.16M | 0.13M |
| 其中 Other current liabilities | 137.77M | n/a | n/a |
| Non-current liabilities (遞延承銷費等) | 14.49M | 15.99M | 15.99M |
| Stockholders' equity | 268.28M | 402.96M | 399.79M |
| Working capital | -138.25M | 0.64M | 0.93M |

- **淨負債**: total debt 為 0 (2026Q2 Total Debt 為 n/a, 2025Q3 為 0.24M)。以現金扣除負債看, 淨現金 n/m, 因 trust 不可自由動用。
- **流動比率**: info currentRatio 8.13 (依 2026Q2 流動資產 1.61M 與流動負債 139.87M 計算應約 0.01, 兩者不一致, 以季報計算為準, 流動比率約 0.01)。
- **負債 / 權益**: 2026Q2 約 0.58 (154.36 / 268.28); 2026Q1 約 0.04。Q2 跳升主因 137.8M 流動負債來源未揭露。
- **Book value**: info bookValue -2.74 與 priceToBook -3.89 與季報矛盾。以季報權益 268.28M / 55.7M 股計算, 每股淨值約 4.82, P/B 約 2.2x。
- **現金位置**: 現金 1.25M 僅足以支應約 8 個季度的 OCF 支出 (依 Q2 OCF -0.16M 估算), 但 SPAC 的實際營運資金依賴併購前後的股東資金注入與 sponsor 支持, 無法由資料確認。

## Capital allocation & insider signal
**資本配置**
- 無股利 (dividendYield 0.0), 無買回 (資料未見)。
- 股本變化: 2025Q3 46.5M 股 → 2026Q1 55.7M 股 (+9.2M, 約 +19.8%)。性質 (sponsor 股、PIPE 或其他) 未揭露。
- Capex: 無。SPAC 無實體資產。

**Insider (最近 6 個月, 2026-04-18 至 2026-10-18)**
- insider 資料最新一筆為 2022-08-16, **最近 6 個月無任何交易紀錄**, 淨買賣 n/a (無資料)。
- 整份 insider 資料 (約 60 筆) 為 2020–2022 年間的交易, 涉及人員 (Schall, Kanaya, Cappel, Tyree, Parker, Edwards 等) 與 Churchill XI 現任管理層 (info 所列 CEO Michael S. Klein、CFO Lee Jay Taragin) 無重疊, 判定為錯置或過期資料, 不採用。
- info heldPercentInsiders 為 6.33%, 為 SPAC 創辦人 / sponsor 持股比例 (估計), 無法與交易紀錄比對。

**機構持股 (2026-06-30 申報)**
- 機構持股比例 69.0%, 機構數 79 家。
- 前十大持有人合計約 40.0% (Empyrean 7.52%, BlueCrest 5.65%, Fort Baker 4.78%, Polar 4.77%, Magnetar 4.58%, Shaw D.E. 3.10%, Sculptor 2.85%, MMCAP 2.27%, T3 2.26%, Millennium 2.17%)。
- 多家在 2026Q2 為新增或加碼 (pctChange = +1.0), 另有 Fort Baker、Magnetar、Sculptor 減碼。持股結構偏向 event-driven / merger-arb 型基金 (估計)。

## Valuation
**價格與區間 (info, 最新收盤 2026-10-16)**
- 收盤 10.66 USD (前收 11.35, 單日 -6.08%); 成交量 3.51M, 10 日均量 2.98M, 3 個月均量 2.53M。
- 52 週區間 10.07 – 19.69。50 日均線 13.24、200 日均線 11.95, 股價低於兩條均線。
- 52 週漲跌 +3.9%, S&P 500 同期 +13.7%。
- 放空比例: 3.13M 股, 占流通股 (float 35.0M) 約 7.55%, short ratio 1.47。

**市值與 trust NAV**
- marketCap 593.8M (以 55.7M 股計算); nonDilutedMarketCap 709.6M; enterpriseValue 592.5M。
- sharesOutstanding 為 41.9M, 與 55.7M 股的差額推測為非公眾股 (creator / 私募股), 屬估計。
- 以 Q2 trust 420.88M ÷ 41.9M 推估每股 trust 約 10.05 USD (估算)。最新價 10.66 相較溢價約 6%。
- 市值 593.8M 約為 trust 的 1.41 倍 (以 55.7M 股計算, 含非公眾股)。

**傳統倍數**
- trailing / forward P/E: n/m (淨利為負或接近零, 且為 trust 利息收入)。
- EV/EBITDA: n/m (EBITDA 為負)。
- P/FCF: n/m (FCF 為負)。
- P/S: n/a (無營收)。
- P/B: 約 2.2x (以季報權益與 55.7M 股計算); info 的 -3.89 因與季報矛盾, 不採用。

**同業中位數**: n/a。SPAC 屬 "Shell Companies" 產業, 無可比較的獲利或營收中位數。若以 SPAC 慣例, 每股 trust 約 10.00–10.20 USD 為常見參考值 (估算)。

## Key catalysts
- **併購進度 (主要催化劑)**: repo 內 serenity 筆記 (2026-10-16 等) 記載 CCXI 透過 SPAC 與 Agility Robotics 合併, S-4 已生效, 預計 11 月完成合併並以 AGLT 掛牌 (為未經本次工具驗證之次級資料)。
- **股東贖回 (redemption)**: 併購表決時的贖回比例將決定最終可用現金, 直接影響 trust 價值與股價折溢價。目前資料無贖回率資訊。
- **流動負債 137.8M 之性質**: 若為贖回應付款、併購相關負債或衍生性負債, 將對 trust 與權益產生直接影響, 需以 10-Q 確認。
- **下次財報**: earnings_dates 工具回傳 403, 無法取得。SPAC 季報通常於季後數週內提交 (估計), 下一份為 2026Q3 報告。
- **最近價格變動**: 2026-10-16 單日 -6.08%, 量能高於 10 日均量, 原因未在工具資料中揭露。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 實體類型 | Churchill Capital Corp XI (SPAC) | n/a | n/a | 與任務指定 Chimerix 不符, 需確認 |
| 營收 (2026Q2) | 0.00M | n/a | n/a | 無營運 |
| 毛利率 / 營業利益率 / 淨利率 | 0.0 / n/m / n/m | n/a | n/a | n/m |
| 淨利 (2026Q2 季度) | -134.68M | n/a | n/a | 警示 (非營業項目 -98.70M 來源未揭露) |
| EPS diluted (2026Q2 季度) | -2.42 | n/a | n/a | 警示 |
| ROE / ROIC | n/m | n/a | n/a | n/m |
| Operating CF (2026Q2 季度) | -0.16M | n/a | n/a | 中性 (規模小) |
| FCF margin / FCF/NI | n/m | n/a | n/a | n/m |
| 現金 (2026-06-30) | 1.25M | n/a | n/a | 偏弱 (依賴 trust) |
| Trust 資產 (2026-06-30) | 420.88M | n/a (2025-06 總資產僅 0.06M, 不可比) | n/a | 核心資產 |
| 流動比率 (季報計算) | 約 0.01 | n/a | n/a | 警示 (info 的 8.13 與季報矛盾) |
| 負債 / 權益 | 0.58 | n/a | n/a | 警示 (Q2 負債跳升) |
| 股本 (BS) | 55.7M | +19.8% vs 2025Q3 (46.5M) | n/a | 稀釋警示 |
| 市值 | 593.8M | n/a | n/a | 約 trust 1.41 倍 (含非公眾股) |
| 每股 trust (估算, 41.9M 股) | 約 10.05 | n/a | 約 10.00–10.20 | 中性 |
| 最新價 vs trust/股 | 10.66 (溢價約 6%) | n/a | n/a | 中性偏貴 |
| P/E / EV/EBITDA / P/FCF / P/S | n/m / n/m / n/m / n/a | n/a | n/a | 不適用 |
| P/B (季報計算) | 約 2.2x | n/a | n/a | 中性 (info -3.89 不採用) |
| 價格 vs 50DMA / 200DMA | 10.66 vs 13.24 / 11.95 | n/a | n/a | 弱勢 |
| 52 週漲跌 | +3.9% (S&P +13.7%) | n/a | n/a | 落後大盤 |
| 放空 (占 float) | 7.55% (short ratio 1.47) | n/a | n/a | 中性 |
| 機構持股 | 69.0% (79 家) | n/a | n/a | 中性 |
| Insider 交易 (近 6 月) | 無資料 (最新 2022-08-16) | n/a | n/a | 無法判讀 |
| 下次財報 | n/a (工具 403) | n/a | n/a | 資料缺漏 |

## Red flags
- **實體不符**: 任務指定 Chimerix, 工具資料為 Churchill Capital Corp XI (SPAC), 需確認 ticker 與分析對象是否正確。
- **無營運, 傳統基本面指標大多 n/m**: 營收為 0, 獲利與現金流指標不適用, 估值只能以 trust NAV 與併購條件為依據。
- **2026Q2 單季淨損 -134.68M**: 其中 Other Operating Expenses 39.07M 與 Other Non Operating -98.70M 均未揭露性質。
- **流動負債 137.77M 來源不明**: 造成 working capital -138.25M, 負債 / 權益由約 0.04 升至 0.58。
- **股本 46.5M → 55.7M (+19.8%)**: 稀釋來源未揭露; 41.9M (sharesOutstanding) 與 55.7M (BS 與市值計算基準) 並存, 股數口徑不一。
- **info 與季報矛盾**: currentRatio 8.13 vs 季報約 0.01; bookValue -2.74 vs 季報每股約 4.82。
- **IPO 日期與資料矛盾**: info firstTradeDate 為 2026-02-09, 但 2025-12-31 年報已有約 415.9M 總資產, 時間線不一致。
- **Insider 資料失效**: 6 個月內無交易紀錄, 且內容為 2020–2022 的 Chimerix 時代資料, 不採用。
- **年報與部分季報缺漏**: annual financials / annual cashflow 回傳空陣列, 2025Q4 季報缺漏, earnings_dates 回傳 403。
- **股價弱勢**: 低於 50DMA 與 200DMA, 單日 -6.08%, 52 週落後 S&P 500 約 10 個百分點。
- **併購與贖回風險 (未經工具驗證)**: 併購完成與否與贖回率將決定最終現金, 目前無法評估。

FUNDAMENTALS REPORT COMPLETE
