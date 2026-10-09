# Fundamentals — UUP (Invesco DB US Dollar Index Bullish Fund) as of 2026-10-10

資料說明：本次 yfinance 即時 API 多數呼叫遭 proxy 403 阻擋（fast_info、財務報表、持股等皆失敗），改用 repo 快取 `prices/yf/UUP.json`（refreshed 2026-10-09T13:07Z）與 `prices/UUP.csv`（最後一筆 2026-10-08）。最新可得收盤為 2026-10-08；2026-10-09 與 2026-10-10 的資料不在快取中。UUP 為 ETF（期貨型工具），因此本報告依 hedge 類工具框架撰寫，不做營收、毛利、ROE 等個股財報分析。

## Executive summary
UUP 為追蹤 ICE 美元指數（DXY）做多方向的期貨型 ETF，費用率 0.75%，快取資料顯示淨資產約 4.31 億美元，最新收盤 28.98 美元（2026-10-08），位於 52 週區間高點 29.08 下方 0.34%，技術面動能偏強（RSI14 68.8、MACD 柱狀體為正、價格高於 20/50/200 日均線）。AUM 歷史、基金申贖流量、展期收益（roll yield）與同類基金中位數在本次資料中均無法取得（DATA_UNAVAILABLE），因此無法對「資金流向」與「展期成本」做出完整判斷；以工具品質而言，本次結論僅能基於價格、波動與費用率。

## Revenue & profitability（工具版：標的與報酬結構）
- **追蹤標的**：ICE 美元指數（DX），對六種主要貨幣（歐元、日圓、英鎊、加幣、瑞典克朗、瑞士法郎）的加權幾何平均，UUP 以持有 DX 期貨多頭（做多美元）方式複製。權重為 ICE 方法論的靜態知識（EUR 約 57.6%、JPY 約 13.6%、GBP 約 11.9%、CAD 約 9.1%、SEK 約 4.2%、CHF 約 3.6%），非本次工具回傳資料，僅供參考。
- **基金規模與成立**：基金家族 Invesco；成立日約 2007-02-20（fundInceptionDate）。
- **報酬（快取價格計算，依 ta 工具與 CSV）**：
  - 1 個月（21 交易日）+3.57%；3 個月 +2.08%；6 個月 +5.46%；12 個月 +4.32%（ta mom_12m）
  - 日曆年：2024 年（自 2024-10-09 起算）+2.08%；2025 年 −8.9%；2026 年 YTD +6.9%（自 2026 首根 K 線 27.11 至 28.98，以 CSV 計算）
  - info 欄位 ytdReturn = 6.28%（基準與 CSV 不同，兩者僅供參考，以 CSV 計算值為準）
  - 3 年平均年報酬 3.93%、5 年平均年報酬 5.90%（threeYearAverageReturn / fiveYearAverageReturn）
- **歷史價格極值（CSV 收盤）**：最高 30.65（2024-12-19）、最低 26.47（2026-01-27）；info 的 allTimeHigh 為 30.76、allTimeLow 為 20.84，與 CSV 不一致，屬於 info 來源的歷史盤中值，已註記。
- **最大回撤（CSV 期間內）**：−13.64%

## Cashflow & balance sheet（工具版：淨值、流動性與費用）
- **淨資產 / 規模**：netAssets / totalAssets = 431,136,608 美元（約 4.31 億美元）。
- **AUM 趨勢**：快取僅有單一時點，無法計算歷史 AUM 變化率 → DATA_UNAVAILABLE。
- **隱含股數（估算）**：netAssets / navPrice ≈ 431.1M / 29.02 ≈ 1,486 萬股（僅為推算，非官方 shares outstanding，後者 DATA_UNAVAILABLE）。
- **NAV 與市價**：navPrice 29.02（時點未明），收盤 28.98，折溢價約 −0.14%。
- **流動性**：3 個月平均日成交量 1,736,918 股，10 日平均 2,031,750 股；以 28.98 計算日均成交金額約 5,030 萬美元（估算）。買賣價差：bid 28.97 / ask 29.05（約 0.28%，以盤中報價計）。
- **費用率**：netExpenseRatio = 0.75%（淨費用率）。
- **展期收益（roll yield）**：DATA_UNAVAILABLE。需要 DX 期貨遠近月價差與展期紀錄，本次資料中無相關欄位。
- **股息 / 收益**：info.yield 與 dividendYield 皆為 3.22%，但 trailingAnnualDividendRate 為 0.0，兩者互相矛盾，已標記為資料不一致，不採用。

## Capital allocation & insider signal（工具版：申贖與持股）
- **基金申贖流量（fund flows）**：DATA_UNAVAILABLE。快取與即時 API 均無申贖資料。
- **持股集中度 / 機構持有人**：major_holders 與 inst_holders 皆回傳空陣列（API 失敗），DATA_UNAVAILABLE。
- **內部人交易**：不適用（ETF 無內部人交易）。
- **資本配置**：UUP 為被動期貨複製，無自身資本配置決策；資本運用集中於 DX 期貨與短期國債擔保品（方法論推定，非工具回傳）。

## Valuation（工具版：工具估值與技術位置）
- **傳統估值（P/E、EV/EBITDA、P/FCF、P/S）**：不適用於 ETF → n/a。
- **價格位置**：收盤 28.98；52 週區間 26.40–29.08；距 52 週高點 −0.34%，距 52 週低點 +9.77%。
- **均線**（ta，as_of 2026-10-08）：MA20 28.63（價格高於 +1.23%）、MA50 28.30（+2.41%）、MA200 27.78（+4.34%）。
- **技術指標**：RSI14 68.76（接近偏強區，未達 70）；MACD 0.2125、訊號線 0.1806、柱狀體 +0.0319；布林 %B 0.80（上軌 29.21、下軌 28.04）；ATR14 0.1216（約 0.42% 價格）。
- **波動度**：20 日年化已實現波動 4.71%；1 年年化波動（CSV 計算）6.69%；全期 7.91%。
- **Beta**：beta3Year = −11.39，數值異常（超出合理範圍），判定為不可靠，不採用。

## Key catalysts（工具版：可觀察事件）
- **財報**：不適用（ETF 無財報）；earnings_dates 無資料。
- **指數與政策面**（方法論層級，非工具回傳）：美元指數走勢主要受美國與主要央行利率預期、歐元區與日本貨幣政策差異、風險情緒驅動；UUP 報酬受 DX 期貨價格直接影響，不受公司事件影響。
- **基金層級事件**：基金分配（distribution）歷史紀錄 DATA_UNAVAILABLE；info 的 3.22% 殖利率若屬實，需於年底分配時驗證。
- **時間注意**：本報告 as-of 為 2026-10-10，但最新可得資料為 2026-10-08 收盤；10-09 與 10-10 資料未取得，屬於 as-of 日期與資料日期之間的缺口，非「資料超過 as-of」。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價（2026-10-08） | 28.98 | 2026 YTD +6.9%（CSV 計算） | DATA_UNAVAILABLE | 處於 52 週高點附近，偏強 |
| 52 週區間 | 26.40–29.08 | — | DATA_UNAVAILABLE | 位於區間上緣（距高點 −0.34%） |
| 淨資產 netAssets | 431.1M 美元 | DATA_UNAVAILABLE（僅單一時點） | DATA_UNAVAILABLE | 規模中等，流動性足夠 |
| AUM 歷史趨勢 | 單點 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判斷資金趨勢 |
| 基金申贖流量 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判斷 |
| 展期收益 roll yield | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法判斷 |
| 淨費用率 netExpenseRatio | 0.75% | DATA_UNAVAILABLE | n/a（未取得同類中位數） | 費用中等偏高（DB 系列典型），需與同類比較 |
| 3 個月平均日成交量 | 1,736,918 股（約 5,030 萬美元） | 10 日均量 2,031,750 股 | DATA_UNAVAILABLE | 流動性足夠 |
| 買賣價差（bid/ask） | 0.28%（盤中） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 尚可 |
| 折溢價（price vs NAV） | −0.14% | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 接近 NAV，無明顯折溢價 |
| 1 個月報酬 | +3.57% | — | DATA_UNAVAILABLE | 短期動能偏多 |
| 12 個月報酬（ta） | +4.32% | — | DATA_UNAVAILABLE | 正報酬 |
| 3 年平均年報酬 | +3.93% | — | DATA_UNAVAILABLE | 中期正報酬 |
| RSI14 | 68.76 | — | DATA_UNAVAILABLE | 偏強，接近超買區 |
| 布林 %B | 0.80 | — | DATA_UNAVAILABLE | 偏上緣 |
| 1 年已實現波動（年化） | 6.69% | 20 日 4.71% | DATA_UNAVAILABLE | 低波動貨幣指數 ETF |
| Beta（beta3Year） | −11.39（異常） | — | DATA_UNAVAILABLE | 不可靠，不採用 |
| 股息殖利率 | 3.22%（與 trailing 股利 0 矛盾） | — | DATA_UNAVAILABLE | 資料不一致，需驗證 |

## Red flags
- 即時 API 大範圍 403 阻擋，本報告主要依賴快取（最新 2026-10-08），未取得 2026-10-09 與 2026-10-10 資料。
- AUM 歷史、申贖流量、展期收益、持股資料全數 DATA_UNAVAILABLE，無法驗證資金面與展期成本對報酬的侵蝕。
- 殖利率與股利欄位矛盾（3.22% vs 0.0），beta3Year = −11.39 異常，兩者均不採用。
- info 的 allTimeHigh（30.76）與 CSV 最高收盤（30.65）不一致，歷史極值以 CSV 為準並註記來源差異。
- RSI14 68.8 接近超買區，布林 %B 0.80，價格貼近 52 週高點，短線追價風險需由交易員評估（本報告不提供交易建議）。
- 費用率 0.75% 屬於期貨型 ETF 的固定成本，長期持有需與 DX 期貨展期成本合併評估，本次無法量化。

FUNDAMENTALS REPORT COMPLETE
