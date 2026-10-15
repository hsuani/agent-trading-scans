# Fundamentals — SPY as of 2026-10-15

資料說明：SPY 為 State Street SPDR S&P 500 ETF Trust (美股 NYSEArca 掛牌，ETF 非公司)，本報告以「指數型基金工具分析」取代營收與獲利分析。資料來源為 pipeline/tools/yf 與 pipeline/tools/ta，回應皆為 `"source": "cache"`（本地快取，屬預期情況）。最新價格資料為 2026-10-14 收盤（regularMarketTime = 2026-10-14 20:00 UTC），未晚於分析基準日 2026-10-15，無 post-date 資料。注意：`prices/SPY.csv` 最後一筆為 2026-10-13，與 info 之 2026-10-14 收盤價存在一日落差，技術指標以 CSV 為準（as of 2026-10-13）。

## Executive summary
SPY 為規模約 8,092 億美元 (totalAssets 809,216,114,688) 的超大型指數 ETF，費用率 netExpenseRatio 0.0945%，流動性極佳（10 日均量 37.6M 股），以基金工具角度看結構健全、無財務槓桿與信用風險。價格 769.60（2026-10-14 收盤，單日 -1.08%）位於 52 週高點 781.62 下方約 1.5%，且站穩 MA50 (768.60) 與 MA200 (723.82)，趨勢仍屬多頭；trailing P/E 24.43、P/B 1.79，估值以歷史水準觀察屬中高位，但工具無法提供同類基金或大盤中位數做直接比較。持倉集中度、資金流與 AUM 時間序列在工具中皆為 DATA_UNAVAILABLE，故「資金面」判讀僅能依賴價格與量能代理指標。

## 基金概況與規模 (取代營收與獲利)
- 基金名稱 / 類別：State Street SPDR S&P 500 ETF Trust；category = Large Blend；fundFamily = State Street Investment Management；quoteType = ETF；成立日 fundInceptionDate 對應 1993 年。
- 策略：依 info.longBusinessSummary，目標為持有 S&P 500 成分股，各股權重大致對應指數權重（完全複製型，非主動管理）。
- 規模 AUM：totalAssets / netAssets = 809.2B 美元（單一快照）。AUM 歷史趨勢：DATA_UNAVAILABLE（工具僅提供單點，無歷史 AUM 序列）。
- 股數與 AUM 交叉檢查：sharesOutstanding = 917,782,016，但 totalAssets / navPrice (777.8567) 反推約 1.040B 股，兩者不一致，判斷 sharesOutstanding 欄位可能過時或來源口徑不同，本報告不採用該股數推算市值。
- 績效（info 欄位）：ytdReturn = 12.68%；fiftyTwoWeekChangePercent = 16.96%；threeYearAverageReturn = 0.232%（年化，欄位定義以來源為準）；fiveYearAverageReturn = 0.138%（同上）。
- 追蹤與淨值：navPrice = 777.8567，收盤價 769.60，市價相對 NAV 折價約 -1.07%（以 navPrice 為基準計算，屬 info 欄位推算，非官方溢折價資料）。

## 費用與追蹤品質
- 費用率 netExpenseRatio = 0.0945%（年化）。
- 追蹤誤差 (tracking error)：DATA_UNAVAILABLE（工具未提供 ETF 淨值與指數報酬序列）。
- 股利：trailingAnnualDividendRate = 5.662 美元；trailingAnnualDividendYield = 0.728%（5.662 / 769.60 計算值 0.736%，接近）；info.yield = 0.99%（與 trailing 計算值有落差，來源口徑未知，以 trailing 為主）。
- 股利 / 配息時間表：yf dividends 回傳空陣列，DATA_UNAVAILABLE。

## 資金流與持倉集中度
- 基金資金流 (fund flows, 申購贖回淨額)：DATA_UNAVAILABLE。
- 前十大持倉權重與集中度：DATA_UNAVAILABLE（major_holders、inst_holders 皆為空陣列；info 無 holdings 欄位）。以 S&P 500 市值加權結構，前幾大權重股合計權重通常較高，但本報告無工具數據可引用，不做數字推論。
- 機構持有人：DATA_UNAVAILABLE。
- 內部人交易：不適用（ETF 無內部人；insider 回傳空陣列）。

## 量能與市場結構 (代理資金面)
- 收盤 769.60（10-14）；當日成交量 55.38M，較 40 日均量 42.94M 高約 29%，較 10 日均量 37.56M 高約 47%；10-13 成交量 25.85M（CSV）。
- 20 日均量 (CSV 至 10-13)：42.52M；60 日均量：42.41M。
- 買賣價差：bid 769.17 / ask 769.28，價差約 0.11 美元（約 1.4 bps），流動性極佳。
- 盤後：postMarketPrice = 767.15（10-14 盤後，-0.32%），屬 10-14 之後盤後資料，尚未超過分析基準日。

## 技術面狀態 (ta snapshot, as of 2026-10-13)
- 收盤 778.01；MA20 769.87；MA50 768.60；MA200 723.82；價格高於 MA20 +1.06%、MA50 +1.22%、MA200 +7.49%。
- MACD 3.61 / signal 2.63 / histogram 0.99（多頭動能維持，柱狀體為正）。
- RSI14 = 59.2（中性偏強，未達超買）。
- Bollinger %B = 0.79（上軌 783.91 / 下軌 755.83）。
- ATR14 = 6.06（約 0.78% 日波動）。
- 報酬動能：1 個月 +2.25%、3 個月 +3.07%、6 個月 +12.03%、12 個月 +19.14%。
- 年化實現波動：20 日 9.5%、60 日 10.8%、252 日 12.7%。
- 距離 2 年內最大回撤：-19.0%（2 年快取區間內最大回撤，為 CSV 收盤價計算值）。

## 估值
- Trailing P/E = 24.43（price 769.60 / EPS TTM 31.497，計算值吻合）。
- Forward P/E：DATA_UNAVAILABLE。
- P/B = 1.79（bookValue 429.22）。
- P/S、EV/EBITDA、P/FCF：不適用於 ETF（無公司財報）。
- 同類 / 大盤中位數：DATA_UNAVAILABLE（快取中無 VOO、IVV、QQQ、VTI、RSP 等同類 ETF 資料，無法做 sector median 比較）。
- 估值定性：trailing P/E 24.4 對指數 ETF 屬中高位，但本報告不以外部歷史經驗數字替代工具數據，僅做此定性提示。

## 催化劑
- 基金本身無財報，earnings_dates 回傳 None，DATA_UNAVAILABLE。
- 成分股財報季節：10 月為美股三季財報密集期，SPY 之 EPS / 指引變化將透過成分股權重間接傳導，但工具未提供具體日期與成分股權重，本報告不列具體日期。
- 總體事件（FOMC、CPI 等）：工具無行事曆資料，DATA_UNAVAILABLE。
- 價格結構性事件：距 52 週高點 781.62（intraday）僅約 1.5%，若突破前高將為技術面關鍵點；收盤高點 779.09（2026-10-06）為 CSV 收盤基準。

## 指標表
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 價格 (regularMarketPrice, 2026-10-14 收盤) | 769.60 | 1Y +19.14% (CSV 12M 報酬) | n/a | 高位整理，趨勢維持 |
| 52 週區間 (info, intraday) | 629.28 – 781.62 | 距高點 -1.54%，距低點 +22.3% | n/a | 接近高點 |
| 52 週區間 (CSV 收盤) | 631.97 – 779.09 | 距收盤高點 -1.2% (以 769.6 計) | n/a | 同上 |
| AUM (totalAssets) | 809.2B USD | 歷史趨勢 DATA_UNAVAILABLE | n/a | 規模極大，流動性足 |
| 費用率 netExpenseRatio | 0.0945% | n/a | n/a（同類 ETF 中位數 DATA_UNAVAILABLE） | 費用率低，但非市場最低 (定性) |
| 基金資金流 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判讀 |
| 前十大持倉權重 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | 無法判讀 |
| Trailing P/E | 24.43 | n/a | n/a | 中高位 |
| Forward P/E | DATA_UNAVAILABLE | n/a | n/a | 無法判讀 |
| P/B | 1.79 | n/a | n/a | 中性 |
| Trailing 股息殖利率 | 0.73% (計算) / 0.99% (info.yield) | n/a | n/a | 口徑有落差 |
| YTD 報酬 | 12.68% (info) / +14.09% (CSV 2025-12-31 至 10-13) | 以 CSV 計 | n/a | 強勢，口徑有落差 |
| Beta (3Y) | 1.00 | n/a | 1.00 (定義上 S&P 500 基準) | 與大盤同步 |
| 20 日實現波動 (年化) | 9.5% | 60 日 10.8%、252 日 12.7% | n/a | 波動低於年度均值 |
| RSI14 | 59.2 (10-13) | n/a | n/a | 中性偏強 |
| MACD histogram | +0.99 (10-13) | n/a | n/a | 多頭動能 |
| 價格 vs MA200 | +6.3% (以 769.6 計) / +7.5% (以 778.01 計) | n/a | n/a | 長期趨勢向上 |
| 日均量 (10 日) | 37.56M | 40 日均量 42.94M | n/a | 流動性極佳 |
| 買賣價差 | 0.11 美元 (~1.4 bps) | n/a | n/a | 極佳 |
| 近 2 年最大回撤 | -19.0% | n/a | n/a | 歷史回撤可接受 |

## Red flags
- 資料缺口：持倉集中度、資金流、AUM 歷史、追蹤誤差、forward P/E、同類基金中位數皆為 DATA_UNAVAILABLE，本報告無法完整檢驗基金面。
- 股數與 AUM 不一致：sharesOutstanding (917.8M) 與 totalAssets / navPrice 反推股數 (約 1.040B) 差距約 13%，屬來源欄位異常，使用時需注意。
- 股息殖利率口徑不一：info.yield 0.99% 與 trailing 計算值 0.73% 不一致。
- YTD 報酬口徑不一：info.ytdReturn 12.68% 與 CSV 計算 14.09% 有落差。
- 快取時間差：技術指標 (ta) 截至 2026-10-13，價格與 info 截至 2026-10-14，兩者差一日。
- 估值偏高風險：trailing P/E 24.4，若大型權值股盈餘不如預期，指數層級回檔風險存在（定性提示）。
- 價格接近 52 週高點 (-1.5%)，短線延續性需觀察能否突破 781.62。
- 單日跌幅 -1.08%（10-14）伴隨成交量放大至約 1.3 倍 40 日均量，屬需留意的短線賣壓訊號（定性）。

FUNDAMENTALS REPORT COMPLETE
