# Fundamentals — 3260.TW (威剛 ADATA Technology) as of 2026-11-26

## Executive summary
本次基本面資料嚴重不足：yfinance 的損益表、資產負債表、現金流量表、內部人交易、持股與獲利公告日端點，皆因 Yahoo 連線遭 agent proxy 以 403 拒絕而回傳空值，repo 快取中對應欄位也全部為空，因此無法計算營收成長、獲利率、FCF、淨負債或任何估值倍數。目前僅取得 cnyes 快取的股價資料（最新 244.0 TWD，前收 271.0 TWD，單日跌約 -10.0%）。財務健康度與估值吸引力**無法判定**，本報告不作投資結論，建議待財報資料補齊後再評估。

## Revenue & profitability
- 營收、毛利、營業利益、淨利：financials / quarterly_fin 皆回傳空列表 []，3-5 年 CAGR、YoY、毛利率、營業利益率、淨利率、ROE、ROIC 全部 n/a。
- 業務組成：info 僅回傳 trailingPegRatio（null），longBusinessSummary 與分部資料未取得，無法評估產品組合。
- 新聞線索（非財報數據，取自同日 sentiment.md 新聞彙整，未經財報驗證）：玉山投顧預估毛利率回落至 28.64%、2027 EPS 預估 84.15 元；2026-11-06 法說會表示 Q4 營收將較 Q3 略減（年底客戶庫存結算），但對明年 DRAM 缺貨程度維持正向看法。

## Cashflow & balance sheet
- cashflow、quarterly_cf、balance_sheet、quarterly_bs 皆為空。
- FCF margin、FCF / NI、淨負債、現金部位、流動比率、負債權益比全部 n/a。
- 無法判斷現金流品質是否健康（FCF / NI 是否大於 0.9）。

## Capital allocation & insider signal
- 資本支出、股利、買回：無資料，coverage n/a。
- 內部人交易（insider，近 6 個月）：回傳空列表，無法計算淨買賣金額與占市值比例。空值不代表無交易，僅代表本次無法取得。
- 大股東與機構持股（major_holders、inst_holders）：皆為空，持股集中度 n/a。

## Valuation
- info 未回傳 marketCap、trailingPE、forwardPE、EV/EBITDA；shares 為 null。P/E、P/FCF、P/S、EV/EBITDA 全部 n/a，無法與同業中位數比較。
- 價格面（cnyes 快取，cached_at 2026-11-25T17:04 UTC）：最新 244.0 TWD、前收 271.0 TWD、當日高 254.5、低 244.0。收盤價與前收 ×0.9（約 243.9）幾乎相同，疑似接近台股單日跌停幅度，需以交易所資料確認。
- 50 日、200 日均線與 52 週高低（fifty_day_average、two_hundred_day_average、year_high、year_low）：null 或 NaN，n/a。
- 參考目標價（非本報告估值）：玉山投顧 420 TWD（增持）；國票由強力買進下調為買進，目標價未取得。來源為 sentiment.md 新聞彙整，未經驗證。

## Key catalysts
- 下次財報 / 法說日期：earnings_dates 回傳空列表，n/a。
- 2026-11-06 法說：Q4 營收預期季減，明年 DRAM 缺貨看法維持正向（新聞彙整）。
- 2026-11 國票下調評等，為本季最明確的負向評等動作（新聞彙整）。
- 月營收公告為台股公司慣例，本次無法取得數據，需人工或其他來源補查。

## Metrics table
| 指標 | 最新值 | YoY | 同業中位數（估計） | 判定 |
|---|---|---|---|---|
| 股價 (TWD) | 244.0 | n/a | n/a | 單日約 -10.0%（前收 271.0），來源 cnyes 快取 |
| 50 日均線 (TWD) | n/a | n/a | n/a | 無資料 |
| 200 日均線 (TWD) | n/a | n/a | n/a | 無資料 |
| 營收 (億 TWD) | n/a | n/a | n/a | 無資料 |
| 毛利率 | n/a | n/a | n/a | 無資料；新聞預估 28.64%（未驗證） |
| 營業利益率 | n/a | n/a | n/a | 無資料 |
| 淨利率 | n/a | n/a | n/a | 無資料 |
| ROE | n/a | n/a | n/a | 無資料 |
| ROIC | n/a | n/a | n/a | 無資料 |
| FCF margin | n/a | n/a | n/a | 無資料 |
| FCF / NI | n/a | n/a | >0.9 為健康 | 無資料，無法判定 |
| 淨負債 (億 TWD) | n/a | n/a | n/a | 無資料 |
| 流動比率 | n/a | n/a | n/a | 無資料 |
| 負債權益比 | n/a | n/a | n/a | 無資料 |
| 市值 (億 TWD) | n/a | n/a | n/a | shares 為 null，無法計算 |
| P/E（trailing / forward） | n/a | n/a | n/a | 無資料 |
| EV/EBITDA | n/a | n/a | n/a | 無資料 |
| P/FCF | n/a | n/a | n/a | 無資料 |
| P/S | n/a | n/a | n/a | 無資料 |
| 內部人淨買賣（6 個月） | n/a | n/a | n/a | 無資料，不可解讀為無交易 |

## Red flags
- 財報與估值資料全面缺失（損益、資產負債、現金流、內部人、持股、財報日期）。在補齊前，不可推定財務健康或不健康。
- 資料來源受限：Yahoo 相關主機遭 agent proxy 以 403 拒絕（政策層級拒絕，未重試或繞過，已回報）。repo 快取 prices/yf/3260.TW.json 的財報欄位為空陣列。
- 股價單日約 -10.0%，本次無法從 yfinance 取得原因（無公告或新聞連結），需人工核對。
- 新聞線索多指向基本面轉弱（毛利率回落預估、Q4 營收季減、國票下調），但均未經財報驗證，只能列為待查方向。
- 時間檢查：所有資料 cached_at 為 2026-11-25（UTC 17:04–17:05），早於分析基準日 2026-11-26，未觀察到基準日後的資料。

FUNDAMENTALS REPORT COMPLETE
