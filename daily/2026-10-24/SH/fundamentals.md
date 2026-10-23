# Fundamentals — SH (ProShares Short S&P500) as of 2026-10-24

> 資料說明：本報告為 -1x 反向 S&P 500 ETF，非營運公司，無營收、獲利、資產負債表可分析。以下以基金結構、費用、規模、折溢價、衰減風險取代。數據來源為 pipeline/tools 快取（source: cache），info 快取時間 2026-10-23 11:31 UTC，ta 指標 as_of 2026-10-22，資料日期早於 2026-10-24 分析日，無資料落後於 as-of 之情形。

## Executive summary
SH 為 -1x 每日重設的反向指數 ETF，用於對沖 S&P 500 下跌風險，不適合作為長期持有的估值標的。截至快取價 32.46 USD，價格與 NAV 32.467 USD 幾乎持平（折價約 -0.02%），基金規模約 1.015 B USD，年化費用率 0.88%，3 年期 beta 為 -0.95。估值框架不適用傳統 P/E 或 EV/EBITDA，重點在費用率、每日重設造成的衰減（volatility drag）、以及價格相對 200 日均線仍低 5.0% 的技術位置。

## 基金結構與規模（取代營收與獲利）
- 基金類型：Exchange Traded Fund，發行商 ProShares，類別 Trading--Inverse Equity，掛牌 NYSEArca。
- 投資標的：目標為每日 -1x 報酬，透過衍生性商品（swap、期貨等）及與指數經濟特性相近之工具達成；至少 80% 總資產投資於反向暴露。基金為 non-diversified。
- 持倉集中度：major_holders 與 inst_holders 皆回傳空陣列，**DATA_UNAVAILABLE**。無法以持倉資料判斷交易對手或衍生性商品集中度。
- 規模：totalAssets = 1,015,440,704 USD，即約 1.015 B USD（netAssets 1,015,440,700 USD，與 totalAssets 一致）。
- 規模趨勢：僅有單點快照，無歷史 AUM 序列，**趨勢 DATA_UNAVAILABLE**。
- 基金成立：fundInceptionDate 對應 2006 年；firstTradeDate 對應 2006 年。

## 費用與追蹤表現
- 年化費用率 netExpenseRatio：0.88%。
- 報酬（info 快取）：YTD -7.96%；trailing 3M -0.88%；1Y -11.75%；3Y 平均年化 -0.14%；5Y 平均年化 -0.08%。
- 3 年 beta：-0.95，與 S&P 500 方向相反，符合反向定位。
- 注意：3Y 平均年化報酬接近 0，代表反向 ETF 在長期多頭市場中持續被侵蝕，與費用率與衰減一致。

## 資金流向（creations / redemptions）
- 淨申購 / 贖回數據：**DATA_UNAVAILABLE**（yfinance 無此欄位，快取亦無）。
- 替代觀察：當日成交量 11,825,064 股，約為 3 個月均量 8,260,870 股的 1.43 倍，10 日均量 9,808,970 股。量能放大，但無法區分為申購或次級市場換手。

## 折溢價與 NAV
- 市價 regularMarketPrice：32.46 USD；navPrice：32.467 USD（NAV 之日期欄位缺失，無法確認是否為當日 NAV）。
- 折溢價：(32.46 − 32.467) / 32.467 ≈ **−0.02%**，接近 NAV，無明顯折溢價。
- bid 32.53 / ask 0.0（ask 欄位為 0，屬快取資料缺漏，不採用）。
- 盤中 NAV 序列：DATA_UNAVAILABLE。

## 衰減與複利風險（daily rebalancing）
- 機制：-1x 每日重設，長期持有報酬不等於指數反向報酬的累積值。
- 估算：以 20 日年化已實現波動 9.83%（vol_20d_annualized）粗估，每年 volatility drag 約 σ² ≈ 0.97%，與 0.88% 費用率疊加，約 1.9%/年的額外侵蝕（估算值，非資料欄位）。波動升高時衰減加劇。
- 含義：SH 適合短期對沖，不宜作為方向性長期部位的替代工具。此段僅為風險說明，非交易建議。

## 估值（不適用傳統估值，改以價格位置與區間替代）
- P/E、EV/EBITDA、P/FCF、P/S：不適用（無盈餘、無現金流）。
- 價格位置（ta snapshot，as_of 2026-10-22）：
  - 收盤 32.46 USD；MA20 32.11、MA50 32.31、MA200 34.18。
  - 距 MA20 +1.10%、距 MA50 +0.46%、距 MA200 −5.03%。
  - 52 週區間 31.64 – 39.20 USD；距 52 週高 −17.19%、距 52 週低 +2.59%。
  - 布林 %B 0.874（接近上軌 32.58）。
  - RSI(14) 55.4；MACD −0.027、Signal −0.086、Histogram +0.059。
  - ATR(14) 0.308 USD（約 0.95% 價格）。
  - 動能：1M +1.03%、3M −3.10%、6M −6.99%、12M −11.75%。
- 支撐 / 壓力（ta levels）：壓力 34.42（2026-06-09）、33.96（2026-07-29）、33.27（2026-09-16）；支撐 32.71（2026-06-01）、32.70（2026-07-10）、31.83（2026-08-13）、31.64（2026-10-06）。
- 同業比較（sector median）：不適用，SH 為單一反向工具，無同類營運公司中位數。

## Key catalysts
- 財報：不適用（ETF 無財報）。earnings_dates 工具回傳錯誤，**DATA_UNAVAILABLE**。
- 基金層面：無分派公告、無 corporateActions（快取為空陣列）。
- 總體變數：SH 對 S&P 500 日報酬敏感，主要驅動為大盤指數走勢與波動度變化。具體事件日期（FOMC、CPI、財報季）未由資料來源提供，**DATA_UNAVAILABLE**，不自行推定。
- 殖利率：info 顯示 yield 與 dividendYield 為 3.92%，對一檔反向 ETF 偏高，應視為待核實之快取欄位，不納入判斷。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 收盤價 (USD) | 32.46 | 1Y 報酬 −11.75% | 不適用 | 價格接近 MA20 / MA50，低於 MA200 5.03% |
| NAV (USD) | 32.467 | n/a | 不適用 | 與市價幾乎持平 |
| 折溢價 | −0.02% | n/a | 不適用 | 無明顯折溢價 |
| 基金規模 AUM (USD B) | 1.015 B | n/a (趨勢 DATA_UNAVAILABLE) | 不適用 | 中小型規模，流動性尚可 |
| 年化費用率 | 0.88% | n/a | 不適用 | 偏高，長期持有侵蝕明顯 |
| 3Y beta | −0.95 | n/a | 不適用 | 與大盤反向，對沖功能明確 |
| YTD 報酬 | −7.96% | n/a | 不適用 | 年內走弱 |
| 3Y 平均年化報酬 | −0.14% | n/a | 不適用 | 長期持有效果偏弱 |
| 資金淨申購 / 贖回 | DATA_UNAVAILABLE | n/a | 不適用 | 無法判讀 |
| 持倉集中度 | DATA_UNAVAILABLE | n/a | 不適用 | 無法判讀 |
| 20 日已實現波動 | 9.83% | n/a | 不適用 | 低波動環境，衰減風險相對溫和 |
| RSI(14) | 55.4 | n/a | 不適用 | 中性偏多 |
| 距 200 日均線 | −5.03% | n/a | 不適用 | 長期趨勢仍弱 |
| 當日成交量 vs 3M 均量 | 1.43× | n/a | 不適用 | 量能放大 |

## Red flags
- 費用率 0.88% 加上每日重設衰減，長期持有報酬結構性不利，不適合作為長期部位。
- 持倉、衍生性商品交易對手、資金流向、AUM 趨勢皆為 DATA_UNAVAILABLE，無法驗證基金的交易對手風險與流動性來源。
- info 快取中 ask 為 0.0、yield 3.92%、fulldayChange 與 regularMarketChange 數值不一致，屬快取資料品質問題，需核實後才可引用。
- 快取時間與 ta as_of 不同（info 2026-10-23，ta 2026-10-22），價格指標存在一日時差。
- 波動度上升時衰減與跳空風險放大，SH 在急速上漲的市場中會有明顯的部位損失。

FUNDAMENTALS REPORT COMPLETE
