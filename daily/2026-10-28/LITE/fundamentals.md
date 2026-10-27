# Fundamentals — LITE as of 2026-10-28

## Executive summary
LITE（Lumentum Holdings）FY26（截至 2026 年 6 月季末）營收 USD 3.01B、YoY +83.2%，毛利率由 FY25 的 28.0% 升至 41.7%，營運動能明確；但同年 GAAP 淨損 USD -6.94B（EPS -92.96）主要來自約 USD 7.74B 的特殊費用，性質在工具輸出中無法確認，財務體質的判讀必須依賴 10-K 補件。估值方面，以 forward P/E 22.7x（forwardEps 36.01）計算尚不算極端，但 P/S 24.6x、P/FCF 約 247x 與 EV/EBITDA 約 90x（TTM）顯示市場已將大量高成長預期計入股價，估值吸引力高度依賴後續營收與獲利持續放大。

**資料時點說明**：本報告以 2026-10-28 為 as-of，最新可用行情為 2026-10-26 收盤 USD 818.10（info.regularMarketPrice）；fast_info 顯示 USD 830.70（cnyes 來源、快取時間 2026-10-27 12:00 UTC），兩者不一致，本報告統一採用 818.10。下次財報日為 2026-11-05（尚未發生，非 post-date 資料）。所有金額單位為 USD（美元），以 B（十億）/M（百萬）標示，本報告無 TWD/KRW 金額。

## Revenue & profitability

**營收與成長（USD M）**

| 會計年度 | 營收 | YoY | 毛利 | 毛利率 | 營業利益（as reported）| 營業利益率 | 淨利 | 淨利率 |
|---|---|---|---|---|---|---|---|---|
| FY23 | 1,767.0 | n/a（FY22 為 null）| 569.0 | 32.2% | -115.7 | -6.5% | -131.6 | -7.4% |
| FY24 | 1,359.2 | -23.1% | 251.5 | 18.5% | -434.0 | -31.9% | -546.5 | -40.2% |
| FY25 | 1,645.0 | +21.0% | 459.9 | 28.0% | -180.1 | -10.9% | 25.9 | +1.6% |
| FY26 | 3,014.0 | +83.2% | 1,255.9 | 41.7% | 524.8 | 17.4% | -6,935.1 | -230.1% |

- 3 年 CAGR（FY23→FY26）約 **19.5%**；FY22 資料為 null，無法計算 3–5 年完整 CAGR，此為工具限制。
- 季度趨勢持續加速：FY26 Q1 533.8 → Q2 665.5 → Q3 808.4 → Q4 1,006.3（USD M）；Q4 YoY 為 +109.3%（對 Q4 FY25 的 480.7），與 info.revenueGrowth 1.093 一致。
- 營收結構：info.longBusinessSummary 描述產品分為 component（半導體雷射晶片、雷射次組件、線路子系統、波長管理）與 system（光學模組、光學電路交換器 OCS、工業雷射）三大類，**但工具未提供分部營收數字，segment mix 為 n/a**。最終端市場為 cloud、AI/ML、電信、消費與工業。
- 毛利率改善明顯：FY26 各季毛利率為 Q1 34.0%（181.5 / 533.8）、Q2 36.1%（240.1 / 665.5）、Q3 44.2%（357.0 / 808.4）、Q4 47.4%（477.3 / 1,006.3），逐季上升，為近期最強訊號之一。

**獲利能力與結構**

- 營業費用 FY26：R&D USD 356.5M（11.8% 營收，FY25 為 18.5%）、SG&A USD 363.2M（12.1%），營收放大後費用率大幅下降。
- 正常化（剔除特殊項目）獲利：yfinance Normalized Income FY26 為 USD 558.2M（18.5% 淨利率），Normalized EBITDA 為 USD 857.0M（28.4%）；info.ebitda 為 USD 800.7M（TTM）、ebitdaMargins 26.6%。
- 特殊項目：FY26 Special Income Charges 為 USD -7,740.5M，Other Special Charges 為 USD +7,756.6M（一次性），pretax income 為 USD -7,172.8M，所得稅費用 USD -237.7M（有效稅率計算值 3.2%）。yfinance 將 Total Unusual Items 與「Excluding Goodwill」數字相同，**無法判定是否為商譽減損；工具未揭露性質，需查 10-K / 8-K 確認**。
- 報告期內 Q4 FY26 單季淨利為 USD -7,161.7M，Q4 特殊項目 -7,759.5M；Q3 FY26 淨利 USD +144.2M。
- EPS：FY26 diluted EPS -92.96（GAAP）；以正常化淨利 558.2M / diluted 股數 74.6M 自行推算約 USD 7.48（非官方數字，僅供參考）。Q3 FY26 GAAP diluted EPS 為 1.50；Q4 FY26 為 -84.65（同樣受特殊項目影響）。
- ROE：info.returnOnEquity = -240.0%（受 GAAP 淨損扭曲，無參考價值）；以正常化淨利 558.2M / 平均股東權益 (1,134.7 + 4,643.9)/2 = 2,889.3M 計算，約 **19.3%**（自行推算）。
- ROIC（自行估計）：正常化 EBIT 約 USD 589.5M（EBIT -7,151.0 + 特殊項目 7,740.5）、以 25% 稅率計 NOPAT 約 442M，平均投入資本 (3,707.9 + 6,281.3)/2 = 4,994.6M，ROIC 約 **8.9%**。此為粗估，非工具直接輸出。
- ROA（info）：5.8%。

## Cashflow & balance sheet

**現金流（USD M）**

| 會計年度 | 營業現金流（推算）| 資本支出 | 自由現金流 FCF | FCF margin | FCF / 淨利 |
|---|---|---|---|---|---|
| FY23 | 179.8 | -128.5 | 51.3 | 2.9% | n/m（淨損）|
| FY24 | 24.7 | -137.0 | -112.3 | -8.3% | n/m（淨損）|
| FY25 | 126.3 | -231.0 | -104.7 | -6.4% | 負值（淨利 25.9）|
| FY26 | 751.4 | -451.3 | 300.1 | 10.0% | n/m；以正常化淨利 558.2 計算為 0.54x |

- 營業現金流（OCF）FY26 為 USD 751.4M（info.operatingCashflow 一致），由 FCF 300.1 加回資本支出 451.3 反推。
- FCF/NI 品質：FY26 GAAP 淨損使比率失去意義；以正常化淨利計 **0.54x，低於 0.9 健康門檻**。季度層面：Q2 FY26 FCF 43.1 / NI 78.2 = 0.55；Q3 FY26 FCF 79.1 / NI 144.2 = 0.55；Q4 FY26 FCF 196.2（NI 受特殊項目影響，比率不適用）。FCF 轉正為 FY26 最大改變，但仍落後獲利。
- 資料不一致：info.freeCashflow 為 USD 224.7M（TTM），與 cashflow 年報推算的 FY26 FCF USD 300.1M 不同，本報告採用年報數字。
- 資本支出：FY26 USD 451.3M，YoY +95.4%，佔營收 15.0%（FY25 為 14.0%、FY24 為 10.1%、FY23 為 7.3%）；資本支出/折舊攤提（Reconciled Depreciation USD 267.0M）= 1.69x，屬擴產期。

**資產負債表（USD M）**

| 項目 | FY25（2025-06）| 2026-03（Q3）| FY26（2026-06）|
|---|---|---|---|
| 總債務 Total Debt | 2,608.2 | 3,313.7 | 1,671.2 |
| 現金（CF 期末現金）| 520.7 | 2,617.8 | 2,043.5 |
| 淨債務（BS Net Debt）| 2,052.5 | 664.0 | n/a（FY26 BS 未提供）|
| 股東權益 | 1,134.7 | 2,973.4 | 4,643.9 |
| 有形帳面價值 TBV | -391.3 | 1,544.2 | 3,247.7 |
| 營運資金 | 1,324.5 | 530.4 | 1,681.4 |

- 淨現金部位（info 口徑）：totalCash USD 2,738.4M - totalDebt USD 1,671.2M = **淨現金 USD 1,067.2M**；若以 CF 期末現金 2,043.5M 計算，淨現金為 USD 372.3M。兩者口徑不同（info 可能包含短期投資），需注意。
- 流動性：current ratio 1.68x、quick ratio 1.32x（info）；營運資金 USD 1,681.4M。
- 槓桿：Debt/Equity 0.36x（info 顯示 35.99%，為百分比口徑）；FY25 為 2.30x（2,608.2 / 1,134.7），槓桿大幅改善主要因股權增加而非盈餘累積。
- 債務結構：FY26 償還債務 USD 1,377.1M、新發 USD 1,302.6M，淨償還 USD 74.5M；利息支出 USD 21.8M，利息收入 USD 60.2M，淨利息收入為正。
- 權益結構劇變：APIC 由 FY25 的 USD 1,986.8M 升至 FY26 的 USD 12,430.1M（+USD 10.4B）；累積虧損（Retained Earnings）由 -861.2M 降至 -7,796.3M。FY26 現金股權募資約 USD 2.0B（CF 欄位以 "Preferred Stock Issuance" 標示，但資產負債表 Preferred Stock 為 0，應為普通股發行，**屬工具標籤錯誤的推論**），APIC 增幅遠大於現金募資，差額約 USD 8.4B 推測為非現金股權發行（如股票收購對價），**尚未經 10-K 證實**。
- 商譽/無形資產（推算）：Stockholders equity 減 TBV，2026-06 約 USD 1,396M，與 2025-12 的約 USD 1,458M、2026-03 的約 USD 1,429M 大致持平，顯示 FY26 上半年以後的股權增加未形成明顯新增商譽帳面，與特殊項目的關聯需另行查證。

## Capital allocation & insider signal

**資本配置**

- 股利：無（dividendYield 0.0%、payoutRatio 0.0%）。
- 買回：FY26 買回股票 USD 102.0M（FY25 為 0，FY23 為 USD 175.6M）；同年現金股權募資約 USD 2.0B，**淨資本流向為股權淨增加**，買回不構成股東回報主軸。
- 股本稀釋：年末股數由 FY25 的 69.8M 升至 FY26 的 88.6M（+27%）；2026-03 季末為 71.7M，表示 Q4 FY26 再增約 16.9M 股，需確認是否為收購發行或可轉債轉換。diluted 加權平均股數 FY26 為 74.6M（YoY +7.2%）。
- 資本支出：FY26 USD 451.3M，屬積極擴產；Q4 FY26 單季資本支出 USD 166.8M，為季度高點。
- 利息覆蓋：EBIT（正常化）/ 利息支出 約 27x（自行推算，589.5 / 21.8）。

**內部人交易（近 6 個月，2026-04-28 至 2026-10-28）**

- 期間內共 49 筆交易：Sale 28 筆、Stock Award（grant，價格 0）21 筆；**無公開市場買進紀錄**。
- 賣出合計 USD 101.4M、113,714 股（以 Value 欄位加總），相當於市值 USD 74.1B 的 **約 0.14%**，規模偏小。
- 主要賣出人：Wupen Yuen（President of Global Business Units，10 筆）、Jae Kim（General Counsel，5 筆）、Vincent D. Retort（4 筆）。CEO Michael Hurlston 於 2026-08-27 有賣出 548 股（USD 0.53M）。
- 近 2 年（2024-11 至 2026-09）總賣出 USD 約 167M，其中 Vincent D. Retort 約 USD 75.7M 為最大單一賣家。
- 解讀限制：工具未標示是否為 10b5-1 預定計畫，也無法確認賣出是否與既得股權行權有關；本報告僅陳述資料事實。
- 內部人持股僅 0.31%（heldPercentInsiders），內部人利益與股價綁定度有限。
- 機構持股 94.19%（1,872 家），前十大包括 BlackRock 10.13%（9.18M 股，季度增持 17.1%）、Vanguard 合計約 10.1%、JPMorgan 4.48%（增持 38.0%）、FMR 3.89%（減持 51.0%）、Invesco 3.51%（增持 170%）。
- 空頭：sharesShort 7.45M 股，佔流通股 8.2%，short ratio 1.66 天；較上月 7.12M 增加 4.6%。

## Valuation

**價格基準**：USD 818.10（2026-10-26 收盤）；52 週區間 USD 184.20 – 1,143.00，目前距高點 -28.4%、距低點 +344%；50 日均線 USD 923.08（股價低 11.4%）、200 日均線 USD 790.39（股價高 3.5%）；beta 1.536。

| 估值指標 | 數值 | 說明 |
|---|---|---|
| Trailing P/E | n/m | GAAP EPS -92.96 為負，不適用 |
| Trailing P/E（正常化，自行推算）| 約 109x | 818.1 / 正常化 EPS 約 7.48 |
| Forward P/E（info.forwardPE）| 22.7x | forwardEps 36.01；期間定義未在工具中標註 |
| Current-year P/E（priceEpsCurrentYear）| 37.5x | epsCurrentYear 21.80 |
| PEG（info）| 0.63 | 工具提供值，未驗證成長假設 |
| P/S（TTM）| 24.6x | 市值 USD 74.1B / 營收 USD 3.01B（FY26 自行驗算一致）|
| P/B | 15.6x | info.priceToBook |
| EV/Revenue（TTM）| 24.0x | EV USD 72.3B |
| EV/EBITDA（TTM）| 90.3x | info.enterpriseToEbitda，EBITDA USD 800.7M；以 FY26 正常化 EBITDA 857.0M 計約 84x |
| P/FCF | 約 247x | 市值 74.1B / FCF 300.1M（以 info TTM FCF 224.7M 計約 330x）|

- 市值：USD 74.1B（marketCap 74,105.8M）；流通股 89.1M（floatShares）；sharesOutstanding 90.6M。
- 分析師共識（28 位）：recommendationMean 1.56（"Buy"）；目標價平均 USD 1,166.28、中位數 USD 1,200、最高 USD 1,500、最低 USD 750。平均目標價較現價約高 42.6%，最低目標價低於現價。此為外部共識，非本報告判斷。
- 同業中位數（**估計，非工具輸出，僅供粗略定位，需人工以同業資料核實**）：光通訊/通訊設備同業 forward P/E 約 25–35x、EV/EBITDA 約 25–35x、P/S 約 5–8x。LITE 在 P/E 上接近或略低於估計區間，但在 P/S、EV/EBITDA、P/FCF 上明顯溢價，反映成長與 AI 光通訊題材的定價。

**估值結論（事實描述）**：估值對「FY27 EPS 能達到 forwardEps 36.01 以上」高度敏感。若以 epsCurrentYear 21.80 計算，P/E 升至 37.5x。EPS 預期的期間與口徑需與 10-K / 財報電話會議確認。

## Key catalysts

- **下次財報**：2026-11-05（yfinance earnings_dates，isEarningsDateEstimate = false；時間戳 2026-11-05 20:00 UTC，電話會議時間戳 22:00 UTC）。FQ1（2026 年 9 月季）EPS 預估 USD 4.22（EPS Estimate）。
- **歷史財報表現**（earnings_dates 的 EPS 為 consensus 比對口徑，與上方 GAAP EPS 不同）：FY26 Q4（2026-08-11 公布）3.23 vs 預估 2.97（+8.8%）；FY26 Q3（2026-05-05）2.37 vs 2.27（+4.6%）；FY26 Q2（2026-02-03）1.67 vs 1.41（+18.6%）；FY26 Q1（2025-11-04）1.10 vs 1.03（+7.0%）。2023 年以來僅 2023-05 一季為負 surprise（-3.9%）。
- **營收動能**：Q4 FY26 YoY +109.3%，為下一季的比較基礎已大幅墊高，需關注 FQ1 營收是否仍維持高成長。
- **毛利率**：Q4 FY26 單季毛利率 47.4%，為季度新高。
- **特殊項目與股權**：USD 7.74B 一次性費用的性質、非現金股權發行的規模、以及 Q4 股數由 71.7M 增至 88.6M，是下一次財報最需釐清的項目。
- **資本支出**：FY26 資本支出 USD 451.3M，擴產能否轉化為營收，需於財報管理層指引（guidance）中確認；工具未提供 guidance 文字。
- **管理層**：CEO Michael Hurlston（pay USD 3.10M）、CFO Wajid Ali（USD 1.60M）；近期賣股主要來自 Wupen Yuen 與 Jae Kim。

## Metrics table

所有金額為 USD；M = 百萬、B = 十億。「Sector median (estimate)」為估計值，非工具輸出。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（FY26，USD M）| 3,014.0 | +83.2% | 無可靠估計 | 高度成長，明顯優於同業（估計）|
| 季度營收 Q4 FY26（USD M）| 1,006.3 | +109.3% | n/a | 加速中 |
| 3 年營收 CAGR（FY23–26）| 19.5% | n/a | n/a | 受 FY24 衰退扭曲，僅供參考 |
| 毛利率（FY26）| 41.7% | +13.7 pp | 約 35–40%（估計）| 改善，優於估計中位數 |
| 毛利率（Q4 FY26）| 47.4% | 季度逐升 | n/a | 強 |
| 營業利益率（FY26，as reported）| 17.4% | +28.3 pp | 約 10–15%（估計）| 由虧轉盈，含一次性項目 |
| 正常化淨利率（FY26）| 18.5% | n/a | 約 10–15%（估計）| 良好 |
| GAAP 淨利率（FY26）| -230.1% | 惡化（FY25 為 +1.6%）| 約 5–10%（估計）| 不佳，受 USD 7.74B 特殊費用影響 |
| ROE（正常化，自行推算）| 19.3% | n/a | 約 10–15%（估計）| 合格 |
| ROIC（粗估，自行推算）| 約 8.9% | n/a | 約 10–12%（估計）| 偏低，資本投入大 |
| FCF margin（FY26）| 10.0% | +16.4 pp（由 -6.4%）| 約 8–12%（估計）| 轉正，與估計中位數接近 |
| FCF / 正常化淨利（FY26）| 0.54x | n/a | >0.9 為健康門檻 | 不足 |
| 資本支出 / 營收（FY26）| 15.0% | +1.0 pp | 約 5–8%（估計）| 偏高，擴產期 |
| 淨現金（info 口徑）| USD 1,067.2M | 由淨債 USD 2,052.5M（FY25）轉為淨現金 | n/a | 強（口徑需核實）|
| 流動比率 current ratio | 1.68x | n/a | 約 2.0x（估計）| 尚可 |
| Debt / Equity | 0.36x | 由 2.30x 降低 | 約 0.3–0.5x（估計）| 健康，但係由股權增加推動 |
| 股數（年末）| 88.6M | +27%（FY25 為 69.8M）| n/a | 顯著稀釋 |
| 股利殖利率 | 0.0% | n/a | 約 0.5–1.0%（估計）| 不發息 |
| 6 個月內部人淨交易（賣出 USD）| USD 101.4M（約 0.14% 市值）| 無買進 | n/a | 偏中性偏空，規模不大 |
| Trailing P/E | n/m | n/a | 約 25–30x（估計）| 不適用 |
| Forward P/E | 22.7x | n/a | 約 25–35x（估計）| 略低於估計區間 |
| EV/EBITDA（TTM）| 90.3x | n/a | 約 25–35x（估計）| 明顯溢價 |
| P/S（TTM）| 24.6x | n/a | 約 5–8x（估計）| 明顯溢價 |
| P/FCF | 約 247x | n/a | 約 30–50x（估計）| 明顯溢價 |
| 空頭佔流通股 | 8.2% | 月增 4.6% | 約 3–5%（估計）| 偏高 |
| 分析師平均目標價 vs 現價 | USD 1,166.28 vs 818.10（+42.6%）| n/a | n/a | 共識偏多 |

## Red flags

- **GAAP 大額虧損**：FY26 淨損 USD -6.94B（EPS -92.96），主要由約 USD 7.74B 特殊費用推動，性質未在工具中揭露，需向 10-K 查證是否含商譽或資產減損。
- **股權大幅稀釋**：年末股數 +27%，APIC 增加約 USD 10.4B，其中現金募資約 USD 2.0B，差額約 USD 8.4B 推測為非現金股權發行，屬高度不確定項目。
- **FCF 品質不足**：FY26 FCF 轉正但正常化 FCF/NI 僅 0.54x；資本支出 USD 451.3M 為折舊的 1.69 倍，後續 FCF 將依賴營收持續放大。
- **估值溢價**：P/S 24.6x、EV/EBITDA 約 90x（TTM）、P/FCF 約 247x，估值高度依賴高成長假設。
- **股價波動**：beta 1.536；52 週區間 USD 184.20 – 1,143.00；現價低於 50 日均線 11.4%，顯示近期高檔回落後的波動。
- **資料一致性問題**（工具層面）：
  - info.freeCashflow（USD 224.7M）與 cashflow 年報 FCF（USD 300.1M）不一致；
  - info.totalCash（USD 2,738.4M）與 CF 期末現金（USD 2,043.5M）口徑不同；
  - CF 欄位 "Preferred Stock Issuance" 標示與資產負債表 Preferred Stock 為 0 矛盾，以普通股發行推斷；
  - 2026-03 季 diluted 加權股數 96.2M 高於 basic 71.5M，與 Q3 單季 GAAP 獲利（正值）的稀釋邏輯不一致，股數數據需核實；
  - fast_info last_price USD 830.70 與 info 現價 USD 818.10 不一致；
  - info.grossProfits（USD 1,333.5M，TTM）與 FY26 gross profit（USD 1,255.9M）不同，本報告採用年報數字。
- **資料缺口**：FY22 為 null，無法計算 3–5 年 CAGR；segment 營收無數字；FY26 BS 的 Net Debt 為 null；無 guidance 文字；同業中位數無工具來源，均為估計值。
- **內部人持股低**：內部人僅持有 0.31%，且 6 個月內有 28 筆賣出交易、0 筆買進。
- **空頭部位上升**：short interest 8.2% 且月增 4.6%。

FUNDAMENTALS REPORT COMPLETE
