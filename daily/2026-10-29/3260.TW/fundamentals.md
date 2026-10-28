# Fundamentals — 3260.TW as of 2026-10-29

**狀態：基本面資料無法取得，本報告無法判定財務健康度或估值吸引力。** 原因是 yfinance 所有財務報表、資產負債表、現金流、內部人交易、法人持股與財報日期端點，都被 egress 代理以政策拒絕（CONNECT 403，目標為 query2.finance.yahoo.com 與 guce.yahoo.com）。依 /root/.ccr/README.md 規定，403 屬政策拒絕，不重試、不繞過，僅回報。

## Executive summary
目前僅取得價格資料：2026-10-28 收盤 363.5 TWD（前收 330.5，單日 +9.98%，資料來源 cnyes 快取）。財務報表、現金流、資產負債、內部人交易與估值倍數全部為 n/a，因此無法評估財務健康度與估值是否合理。建議下游研究者以 market / technical 報告為主要參考，並待 yfinance 權限恢復後補跑本報告。

## Data availability
| 端點 | 狀態 |
|---|---|
| info | 僅回傳快取中的 trailingPegRatio: null，其餘欄位缺失 |
| fast_info | 成功（cnyes 來源，快取時間 2026-10-28T12:37 UTC）；市值、股數、50/200 日均線、52 週高低皆為 null / NaN |
| financials / quarterly_fin | 空陣列 [] |
| balance_sheet / quarterly_bs | 空陣列 [] |
| cashflow / quarterly_cf | 空陣列 [] |
| earnings_dates | 連線被 403 拒絕 |
| insider | 空陣列 [] |
| major_holders / inst_holders | 空陣列 [] |

資料時點註記：價格 363.5 對應 2026-10-28 收盤（與 ta 工具最新一根 K 線一致），沒有 2026-10-29 的資料。

公司身分：依分析師既有知識，3260 為威剛科技（ADATA Technology），但本次工具未回傳 longName 或 sector，此身分未經工具驗證。

## Revenue & profitability
n/a。營收、毛利、營業利益、淨利、ROE、ROIC 均無資料，無法計算 3-5 年 CAGR、YoY 或利潤率趨勢。Segment mix 亦因 info.longBusinessSummary 未回傳而無法確認。

## Cashflow & balance sheet
n/a。FCF、FCF/NI、淨負債、流動比率、負債權益比、現金部位均無資料。

## Capital allocation & insider signal
n/a。資本支出、買回、股利與股利覆蓋率無資料。內部人交易（近 6 個月）回傳空陣列，但這是端點失敗後的空回傳，不能解讀為「無內部人交易」。

## Valuation
n/a。trailing / forward P/E、EV/EBITDA、P/FCF、P/S 均無資料，無法與產業中位數比較。

已知價格面數據（非估值指標）：收盤 363.5 TWD，前收 330.5，當日高 363.5、低 336.5。市值與股數為 null，因此無法驗證 TWD 億元單位換算。

## Key catalysts
- 下次財報日期：n/a（earnings_dates 被 403 拒絕）。
- 近期財測或法說會指引：無資料。
- 產品或業務組合轉變：無法從 info 取得。
- 價格面事件：2026-10-28 單日 +9.98%，屬技術面與市場報告範疇，本報告不做解讀。

## Metrics table
單位：金額欄位無資料，未做 億 / B 換算；價格單位為 TWD。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價 (TWD) | 363.5 (2026-10-28) | n/a | n/a | 資料可用 |
| 前收盤 (TWD) | 330.5 | n/a | n/a | 資料可用 |
| 營收 | n/a | n/a | n/a | 無法判定 |
| 毛利率 / 營益率 / 淨利率 | n/a | n/a | n/a | 無法判定 |
| ROE / ROIC | n/a | n/a | n/a | 無法判定 |
| FCF / FCF 利潤率 / FCF÷NI | n/a | n/a | n/a | 無法判定 |
| 淨負債 / 流動比率 / D/E | n/a | n/a | n/a | 無法判定 |
| 資本支出 / 股利 / 買回 | n/a | n/a | n/a | 無法判定 |
| 內部人淨買賣 (6 個月) | n/a（空回傳不代表無交易） | n/a | n/a | 無法判定 |
| Trailing / Forward P/E | n/a | n/a | n/a | 無法判定 |
| EV/EBITDA / P/FCF / P/S | n/a | n/a | n/a | 無法判定 |
| 市值 | n/a | n/a | n/a | 無法判定 |

## Red flags
- 資料缺口：財務、現金流、資產負債、內部人、法人持股與財報日期全部缺失，屬於本報告的主要風險。
- 代理政策拒絕：yahoo finance 相關網域 403，屬基礎設施限制，需由 orchestrator 或維運確認權限，不建議自行繞過。
- 內部人與法人空回傳不可當作正面或負面訊號。
- 2026-10-28 單日 +9.98% 的基本面成因無法從財務資料確認。

FUNDAMENTALS REPORT COMPLETE
