# Fundamentals — AMD as of 2026-10-22

## Executive summary
AMD 財務體質良好: 2026-06-30 現金及短期投資 13,111M USD、總債務 4,276M USD，淨現金約 8,835M USD，流動比率 2.61；TTM 營收 41,305M USD、年增率約 50% (Q2'26 YoY +50.1%)，TTM FCF 8,403M USD (FCF margin 20.3%)。估值極度昂貴: 以 TTM GAAP EPS 3.92 計算 trailing P/E 141.0x，forward P/E 35.1x，EV/EBITDA 約 83x–93x，P/FCF 約 107x；分析師共識 Strong Buy (平均目標價 637.61 USD，較現價 552.72 USD 上行約 15%)，但估值已大量反映成長預期，對 beta 2.45 的股票而言回檔風險高。

資料基準: 價格採 pipeline/tools/pricefeed.py quote 與 repo cache prices/yf/AMD.json (cached_at 2026-10-22T11:36–11:39 UTC)，財報採 cache 中 2026-06-30 季報為最新。Q3'26 財報尚未公布 (預定 2026-11-03)，報告無 post-date 資料。注意: 本次即時 yfinance 呼叫 (Yahoo 連線被代理 403 阻擋) 在 info / fast_info 中一度回傳 AVGO 的資料，已全部改採 AMD 專屬 cache 數值並以 pricefeed quote 交叉驗證 (552.72 一致)。

## Revenue & profitability

**營收趨勢 (年度，USD)**
- FY2022 23,601M / FY2023 22,680M / FY2024 25,785M / FY2025 34,639M
- 3 年 CAGR (FY22–FY25): 約 13.6%；2 年 CAGR (FY23–FY25): 約 23.6%
- FY2025 YoY +34.3%，FY2024 YoY +13.7%；成長明顯加速
- 2021 年資料於 cache 中為 n/a，未納入計算

**季度趨勢 (USD)**
- Q3'25 9,246M / Q4'25 10,270M / Q1'26 10,253M / Q2'26 11,536M
- Q2'26 YoY +50.1% (Q2'25 為 7,685M)；TTM 營收 41,305M 與 info.totalRevenue 一致
- Q1'26 較 Q4'25 持平 (-0.2%)，Q2'26 環比 +12.5%，成長動能仍在但季增率需留意

**分部 (segment) 營收**: cache 與 info 僅提供 longBusinessSummary 描述三大分部 (Data Center、Client and Gaming、Embedded)，未提供分部營收拆分。DATA_UNAVAILABLE。

**毛利率 / 營業利益率 / 淨利率**
| 期間 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 44.9% | 5.4% | 5.6% |
| FY2023 | 46.1% | 1.8% | 3.8% |
| FY2024 | 49.4% | 8.1% | 6.4% |
| FY2025 | 49.5% | 10.7% | 12.5% |
| TTM (Q3'25–Q2'26) | 53.2% | 15.7% | 15.6% |
| Q2'26 | 53.8% | 17.3% | 19.9% |

- 毛利率從 FY2022 的 44.9% 擴張到 TTM 53.2%；Q2'25 單季曾跌至 39.8% (該季毛利 3,059M)，之後回升至 51–54% 區間 (Q3'25 51.7%、Q4'25 54.3%、Q1'26 52.8%、Q2'26 53.8%)。
- 營業利益率從 FY2024 的 8.1% 提升到 FY2025 的 10.7%，TTM 達 15.7%，Q2'26 單季 17.3%，經營槓桿明顯。
- 研發費用 FY2025 為 8,091M (占營收 23.4%)；TTM R&D 約 9,394M (占營收 22.7%)，持續高強度投入。
- 淨利率 FY2025 大幅改善至 12.5%，但 FY2025 淨利含 gain on sale of security 366M 等非經常項目 (Total Unusual Items 366M)；TTM 淨利 6,434M 中 Q2'26 單季淨利 2,297M 高於同季營業利益 1,990M，原因於資料中未揭露，需以 Q3 財報確認是否為一次性。
- ROE: info 報告 10.20%；以 TTM 淨利除以平均股東權益 (62,999M 與 67,224M) 計算約 9.9%。ROE 仍偏低，淨利相對於股東權益 (67,224M) 規模有限；商譽 25,126M 與無形資產 16,705M 屬資產端項目，資料未顯示其對 ROE 的具體影響。
- ROIC (估計): TTM 營業利益 6,488M × (1 - 21% 稅率) ÷ 平均投入資本 (66,221M 與 70,450M) 約 7.5%；以期末投入資本計算約 7.3%。ROIC 低於 WACC 估計值 (約 9–10%，屬估計)，表示目前高成長仍在消化大量資本。

## Cashflow & balance sheet

**現金流量 (USD)**
| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM |
|---|---|---|---|---|---|
| Operating CF | 3,565M | 1,667M | 3,041M | 7,709M | 10,080M |
| Capex | -450M | -546M | -636M | -974M | -1,677M |
| FCF | 3,115M | 1,121M | 2,405M | 6,735M | 8,403M |

- TTM FCF margin: 20.3%；FY2025 FCF margin: 19.4%
- FCF / NI: FY2025 1.55x，TTM 1.31x (>0.9 健康)；info 來源 freeCashflow 8,841M，與報表計算差異約 438M (見 Red flags)
- 注意單季品質: Q2'26 FCF 1,558M，FCF / NI 僅 0.68x (OCF 2,366M，營運資金變動 -730M，capex 808M)，單季現金轉換明顯轉弱
- SBC: TTM 1,895M (占營收 4.6%)；扣除 SBC 後 TTM FCF 約 6,508M (FCF margin 15.8%)

**資產負債表 (2026-06-30, USD)**
- 現金及等價物 5,086M；現金 + 短期投資 13,111M (Q2'25 為 5,867M，年增約 123%)
- 總債務 4,276M (長期債 2,351M、一年內到期 875M、長期租賃負債 1,050M)
- 淨現金 (cash - total debt) 約 8,835M；FY2025 淨現金為 6,692M (10,552M - 3,847M)，持續改善
- 流動資產 31,522M / 流動負債 12,081M，current ratio 2.61，quick ratio (info) 1.69
- Debt / Equity: 6.4% (4,276M / 67,224M)，財務槓桿低
- 股東權益 67,224M；有形帳面價值 26,119M；working capital 19,441M
- 存貨 FY2025 7,920M (年增 38%，略高於營收 +34%)；應收帳款 6,315M (年增 2%)；需監控存貨堆積

**資本支出趨勢**
- Capex FY2022 450M → FY2025 974M → TTM 1,677M，capex / 營收 TTM 4.1%
- Q2'26 單季 capex 808M，較 Q2'25 (282M) 增加約 187%，資本支出明顯加速，與 AI 產能擴張一致
- 固定資產淨值 FY2025 2,312M，折舊攤提 TTM 約 3,027M (FY2025 為 3,004M，FY2022–FY2025 逐年下降)

## Capital allocation & insider signal

**資本配置**
- 股利: 無配息 (dividendRate / trailingAnnualDividendRate 皆為 0)，股利覆蓋率不適用
- 買回: FY2022 4,108M / FY2023 1,412M / FY2024 1,590M / FY2025 1,923M；TTM 約 1,182M，占 TTM FCF 約 14%
- 股數: 流通股本 1,632M (2026-06-30)，FY2025 年底 1,630M；FY2025 稀釋後平均股數 1,636M vs FY2024 1,637M，買回大致抵銷 SBC 稀釋
- 併購: FY2025 購買企業現金支出 1,760M (FY2024 548M)，商譽 25,126M，年內併購活動明顯增加
- 投資: FY2025 購買投資證券 5,972M，用途資料未揭露，現金及短期投資部位大幅擴增

**內部人交易 (過去 6 個月，2026-04-22 至 2026-10-22，依 cache insider 資料)**
- 公開市場賣出 (Sale): 19 筆，578,730 股，合計約 270.6M USD，占市值 (902.3B USD) 約 0.03%
- 公開市場買入: 0 筆 (無 Purchase 紀錄)
- 認股權證行使 (Conversion of Exercise): 7 筆，171,366 股，約 3.8M USD (執行人員包括 Forrest Norrod、Mark Papermaster 等，行權與後續賣出之關聯資料未揭露)
- 贈與 (Stock Gift): 5 筆，122,402 股，無現金價值
- 無價格欄位紀錄 (性質多為 RSU 歸屬 / 稅款代扣): 19 筆，867,766 股，性質待確認
- CEO Lisa Su 於 2026-06-10 賣出 125,000 股 (約 57.6M USD)、2026-08-18 賣出 15,000 股 (約 7.2M USD)、2026-09-10 賣出 95,000 股 (約 48.1M USD)，6 個月合計約 113M USD；另有 2026-06-12 與 2026-09-10 兩次贈與 (共 65,000 股)。是否為 10b5-1 計畫資料未提供，DATA_UNAVAILABLE。
- 解讀: 高管賣出金額 (約 270M USD) 相對市值極小，且近期賣出價位 (449–556 USD) 隨股價上行，資料未揭露賣出計畫性質 (如 10b5-1)，連續性賣出仍需納入信號權重。內部人持股比例僅 0.42%。

**機構持股與空頭**
- 機構持股 75.4% (5,129 家)；前十大包括 BlackRock 9.21%、Vanguard 6.52%、State Street 4.56%、Invesco 3.26%、JPMorgan 2.47% (2026-06-30 季報)
- 放空: 流通股放空 39.28M 股 (占流通股 2.42%)，short ratio 1.83 日，較上月 41.71M 下降約 6%，空頭壓力低

## Valuation

以 2026-10-22 參考價 552.72 USD (pricefeed 與 cache 一致，前一收盤 534.74 USD；盤前 530.40 USD)。

- Trailing P/E (GAAP TTM EPS 3.92): 141.0x；季度 diluted EPS 加總 3.89，約 142x
- 非 GAAP 口徑: earnings_dates 已公布之近四季 EPS 加總 (Q3'25 1.20、Q4'25 1.53、Q1'26 1.37、Q2'26 1.66) 合計 5.76 USD，trailing P/E 約 96x；forward EPS (15.76) 與季報 EPS 共識屬非 GAAP 口徑，比較時需統一口徑
- Forward P/E (forwardEps 15.76): 35.1x；PEG (info): 0.53
- EV / EBITDA: info 來源 93.4x (ebitda 9,562M)；以季度 EBITDA 加總 10,718M 計算約 83.4x
- EV / Revenue (TTM): 21.6x；P/S (TTM): 21.8x
- P/FCF (TTM 8,403M): 約 107x；以 info freeCashflow 8,841M 計算約 102x
- P/B: 13.4x (帳面價值 41.19 USD/股)
- 市值 902.3B USD；企業價值 893.5B USD；beta 2.45

**分析師共識 (cache info, 50 位分析師)**
- recommendationMean 1.49 (Strong Buy)；rec_summary 近 4 個月 strongBuy 5、buy 39–40、hold 10–11、sell 0
- 目標價: 平均 637.61 USD (+15.4%)、中位數 635.50 USD (+15.0%)、最高 1,250 USD、最低 365 USD (-34%)

**與同業中位數比較 (估計)**
- 半導體同業中位數屬分析師估計值，非工具輸出；估計 trailing P/E 約 35x、forward P/E 約 25x、EV/EBITDA 約 25x、P/S 約 8x、P/FCF 約 35x
- AMD 估值相對同業中位數溢價約 3–4 倍 (trailing) 與約 40% (forward)；forward 估值溢價明顯小於 trailing，反映市場對 EPS 成長的預期

**股價位置**: 52 週區間 188.22–658.52 USD，現價距 52 週高點 -16.1%，較 52 週低點 +193.7%；52 週漲幅 +140.1%；50 日均線 541.10 USD (現價 +2.1%)，200 日均線 399.08 USD (現價 +38.5%)。

## Key catalysts

- **下次財報**: 2026-11-03 (earnings_dates 與 info earningsTimestamp 一致，isEarningsDateEstimate = False)；Q3'26 EPS 共識 1.93 USD (此為 earnings_dates 的 EPS Estimate 欄位)
- **歷史 EPS 驚喜**: Q3'25 (2025-11-04) +2.1%、Q4'25 (2026-02-03) +15.5%、Q1'26 (2026-05-05) +5.8%、Q2'26 (2026-08-04) +3.2%；過去四季皆 beat
- **營收動能**: Q2'26 YoY +50.1%；FY2025 Capex 與 Q2'26 capex 明顯上升，對 AI 資料中心需求之後續訂單與毛利率影響需追蹤
- **毛利率**: TTM 53.2%，Q2'26 單季 53.8%；若 Q3 維持此水準，為估值支撐
- **Guidance (下季營收/毛利指引)**: DATA_UNAVAILABLE (工具未提供管理層指引文字)
- **分部營收拆分 (Data Center / Client & Gaming / Embedded)**: DATA_UNAVAILABLE
- **分析師目標價調整**: 目標價區間 365–1,250 USD 差距極大，分歧高，財報前後可能出現修正

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (TTM, USD) | 41,305M | Q2'26 +50.1% (FY25 +34.3%) | 估計 ~ 年增 10–15% | 強 |
| 毛利率 (TTM) | 53.2% | FY25 49.5% (FY24 49.4%) | 估計 ~55% | 中性偏強 |
| 營業利益率 (TTM) | 15.7% | FY25 10.7% (FY24 8.1%) | 估計 ~20% | 改善中 |
| 淨利率 (TTM) | 15.6% | FY25 12.5% (FY24 6.4%) | 估計 ~15% | 中性 |
| ROE (info) | 10.2% | n/a | 估計 ~15–20% | 偏弱 |
| ROIC (估計) | ~7.5% | n/a | 估計 ~12–15% | 偏弱 |
| FCF margin (TTM) | 20.3% | FY25 19.4% (FY24 9.3%) | 估計 ~18% | 強 |
| FCF / NI (TTM) | 1.31x | FY25 1.55x | >0.9 健康 | 健康 (Q2'26 僅 0.68x) |
| SBC / 營收 (TTM) | 4.6% | n/a | 估計 ~5–8% | 可接受 |
| 淨現金 (2026-06-30) | +8,835M USD | 較 FY25 淨現金 6,692M 增加 | 估計 ~ 中性 | 強 |
| Current ratio | 2.61 | FY25 2.85 (26,947/9,455) | 估計 ~2.0 | 強 |
| Debt / Equity | 6.4% | FY25 6.1% (3,847/62,999) | 估計 ~30–40% | 強 |
| Capex / 營收 (TTM) | 4.1% | FY25 2.8% (974/34,639) | 估計 ~5% | 上升中 |
| 股利殖利率 | 0.0% (無配息) | n/a | 估計 ~0.5% | n/a |
| 買回 (TTM, USD) | 1,182M | FY25 1,923M (+21% vs FY24) | n/a | 中性 |
| Trailing P/E (GAAP) | 141.0x (非 GAAP 約 96x) | n/a | 估計 ~35x | 極度昂貴 |
| Forward P/E | 35.1x | n/a | 估計 ~25x | 偏貴 |
| EV / EBITDA (TTM) | 83.4x (info 93.4x) | n/a | 估計 ~25x | 極度昂貴 |
| P / FCF (TTM) | ~107x | n/a | 估計 ~35x | 極度昂貴 |
| P / S (TTM) | 21.8x | n/a | 估計 ~8x | 極度昂貴 |
| 分析師平均目標價 | 637.61 USD (+15.4%) | n/a | n/a | 共識偏多 |
| 內部人 6 個月公開市場賣出 | 約 270.6M USD (19 筆，0 筆買入) | n/a | n/a | 偏空 (金額小) |
| 機構持股比例 | 75.4% | n/a | n/a | 中性 |
| 放空比例 (流通股) | 2.42% (short ratio 1.83) | 較上月下降約 6% | n/a | 低 |
| Beta | 2.45 | n/a | 估計 ~1.2 | 高波動 |

## Red flags
- **估值極端**: trailing P/E 141x、P/FCF 約 107x、EV/EBITDA 約 83–93x，遠高於半導體同業估計中位數；若成長放緩，估值壓縮風險高。
- **Q2'26 現金轉換轉弱**: 單季 FCF 1,558M，較 Q1'26 (2,566M) 下降約 39%，FCF / NI 僅 0.68x；營運資金 -730M 與 capex 808M 同時拉高。
- **存貨與資本支出上升**: FY2025 存貨 7,920M (年增 38%，快於營收 +34%)；Q2'26 capex 年增約 187%，需留意產能過剩或需求不如預期的風險。
- **淨利品質**: FY2025 含 366M 非經常性 gain on sale of security；Q2'26 淨利 2,297M 遠高於營業利益 1,990M，需以 Q3 財報驗證是否重複發生。
- **ROE 與 ROIC 偏低**: ROE 10.2%、ROIC 約 7.5%，高估值下資本效率尚未充分反映。
- **內部人持續賣出**: 6 個月 19 筆公開市場賣出、約 270.6M USD，CEO Lisa Su 合計約 113M USD；雖占市值比例低，但方向一致。
- **Beta 2.45 與股價波動**: 52 週內現價距高點 -16%、距低點 +194%；對事件驅動的波動極為敏感。
- **資料品質**: (1) 本次即時 yfinance info 與 fast_info 呼叫回傳 AVGO 資料 (Yahoo 連線被代理阻擋)，已改用 AMD cache 與 pricefeed quote 交叉驗證；(2) info.totalCash 23,975M 與 2026-06-30 資產負債表現金及短期投資 13,111M 不一致；(3) info.ebitda 9,562M 與季度 EBITDA 加總 10,718M 不一致；(4) info.freeCashflow 8,841M 與 TTM 報表計算 8,403M 不一致；(5) info.grossMargins 55.7% 與季度毛利率加總 53.2% 不一致。本報告以報表資料為主，info 數值僅作參考。
- **資料缺口**: 2021 年財報為 n/a；分部營收、管理層 guidance、10b5-1 計畫資訊均為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
