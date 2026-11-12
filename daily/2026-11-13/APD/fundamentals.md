# Fundamentals — APD (Air Products and Chemicals, Inc.) as of 2026-11-13

資料說明：本報告所有數字取自 `pipeline/tools/yf` 輸出。Yahoo cookie/crumb 取得失敗後工具已回退至 repo cache（info 與 fast_info 明示 `source: cache`，`cached_at` 2026-11-12）。未發現 2026-11-13 之後的資料。幣別為 USD，大額以 B（十億）/ M（百萬）表示；本報告不使用億。財年截止日為每年 9/30（FY2026 = 2025-10 至 2026-09）。

## Executive summary

APD 以 313.50 USD（info.currentPrice，快取快照）計，市值 69.81B USD，財務體質偏弱：FY2025 營收 12.04B USD 年減 0.5%，正規化營業利益率仍維持約 24%，但 GAAP 淨利 FY2025 為 -0.39B USD，FQ3 FY2026（6/30 季）因 -2.91B USD 特殊損失使單季 Diluted EPS 為 -6.47，自由現金流連續三年為負（FY2025 FCF -3.77B USD），淨負債升至 15.84B USD。估值方面，以 forward EPS 15.54 計 forward P/E 約 20.2x、分析師平均目標價 344.10 USD（較現價 +9.8%），但 trailing P/E 因 GAAP 盈餘為負不具參考性（n/m），EV/EBITDA（info TTM）約 19.2x 偏高；整體結論為「盈餘品質與現金流尚未回到可持續水準，估值建立在 FY2027 正常化獲利回復的假設上」。

## Revenue & profitability

**營收趨勢（annual，USD B）**

| 年度（9/30） | 營收 | YoY |
|---|---|---|
| FY2022 | 12.70B | — |
| FY2023 | 12.60B | -0.8% |
| FY2024 | 12.10B | -4.0% |
| FY2025 | 12.04B | -0.5% |

- 3 年 CAGR（FY2022 → FY2025）：約 -1.8%，營收未成長。
- 季度趨勢：FQ3 FY2026（6/30）營收 3.16B，較 FQ3 FY2025 的 3.02B 年增 +4.6%；FQ1、FQ2 FY2026 營收分別 3.10B、3.17B，尚未看到明顯加速。
- TTM 營收（季報加總）約 12.60B；info.totalRevenue 為 12.99B，兩者差距約 3%，見「Red flags」資料異常。
- 業務結構：longBusinessSummary 只列出產品類別（大宗氣體 atmospheric gases、製程氣體 process gases、特用氣體 specialty gases、設備 equipment）與地區（美洲、亞洲、歐洲、中東、印度），未提供分部營收占比，分部 mix 為 DATA_UNAVAILABLE。

**獲利能力（annual）**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| 毛利率 | 26.5% | 29.9% | 32.5% | 31.4% |
| 營業利益率（Operating Income，不含特殊項） | 19.0% | 21.7% | 24.4% | 24.0% |
| 正規化淨利率（Normalized Income / 營收） | 18.1% | 19.8% | 21.7% | 21.4% |
| GAAP 淨利率 | 17.8% | 18.3% | 31.6%（含一次性利益 1.52B） | -3.3%（含特殊損失，見下） |
| 正規化 EPS（USD，計算） | 10.34 | 11.18 | 11.77 | 11.56 |
| GAAP Diluted EPS（USD） | 10.14 | 10.33 | 17.18 | -1.77 |

- 正規化獲利能力穩定：正規化淨利率自 FY2023 起維持在 21–22%，FY2025 略降至 21.4%。
- GAAP 獲利波動大：FY2024 高估因一次性處分利益 1.52B USD；FY2025 因 Gain On Sale Of Business -3.68B USD 與 Special Income Charges -3.77B USD 轉為虧損。
- FQ3 FY2026（2026-06-30）：營收 3.16B、毛利 1.04B（毛利率 32.8%）、Operating Income 0.81B（營業利益率 25.6%）皆屬正常；但特殊項目 Special Income Charges 為 -2.91B USD，致 Pretax Income -1.94B、淨利 -1.44B、Diluted EPS -6.47（驗算：-6.47 × 222.8M 股 ≈ -1.44B，與 Net Income -1.44B 吻合）。**特殊損失的性質與原因不在本次快取資料中，需另行查核 10-Q / 8-K。**
- FQ1 FY2026 EPS 3.04、FQ2 FY2026 EPS 3.19；Q4 FY2026（2026-09-30 季）Reported EPS 3.61 已於 2026-11-05 公布（見 Key catalysts），但該季損益表明細不在快取中，FY2026 全年營收與毛利為 DATA_UNAVAILABLE。
- ROE：info.returnOnEquity 3.2%（TTM GAAP 口徑，受特殊損失拖累）；以正規化淨利計算 FY2025 ROE 約 16.1%（2.57B ÷ 平均股東權益 16.03B）。
- ROIC（計算）：FY2025 約 7.1%（Operating Income 2.89B × (1 - 有效稅率 21.4%) ÷ 平均 Invested Capital 31.99B），FY2024 約 8.5%。ROIC 連續兩年低於 10%。

## Cashflow & balance sheet

**現金流（annual，USD B）**

| 項目 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| 營業現金流 OCF | 3.23 | 3.21 | 3.65 | 3.26 |
| 資本支出 Capex | 2.93 | 4.63 | 6.80 | 7.02 |
| 自由現金流 FCF | +0.30 | -1.42 | -3.15 | -3.77 |
| FCF / 淨利 | 0.13 | 負值 | 負值 | n/m（淨利為負） |
| FCF margin（FCF / 營收） | 2.4% | -11.3% | -26.0% | -31.3% |
| 股利支出 | 1.38 | 1.50 | 1.57 | 1.58 |

- FCF / 淨利遠低於 0.9 健康門檻，且 FY2023–FY2025 皆為負。
- Capex 占營收由 FY2022 的 23% 攀升至 FY2025 的 58%。FY2025 在建工程（Construction In Progress）為 13.46B USD，佔 Gross PPE 約 31%（FY2024 為 11.19B USD）。在建工程尚未轉為營收，是 FCF 短期無法轉正的主因。
- 季度：FQ1–FQ3 FY2026 OCF 合計約 3.31B USD（0.90 + 1.10 + 1.31B），Capex 合計約 3.36B USD，季度 FCF 合計約 -0.04B USD；FQ3 單季 FCF 為 +0.31B，為近五季首次轉正。
- TTM（Sep25–Jun26 季報加總）：OCF 4.57B、Capex 4.87B、FCF 約 -0.30B USD。info.operatingCashflow 為 4.68B，info.freeCashflow 為 -0.19B，方向一致，數值存在小幅差距。

**資產負債表（USD B）**

| 項目 | FY2024（9/30） | FY2025（9/30） | 2026-06-30（FQ3） |
|---|---|---|---|
| 總資產 | 39.58 | 41.06 | 40.45 |
| 股東權益（歸屬母公司） | 17.04 | 15.03 | 13.88 |
| 少數股東權益 | 1.64 | 2.33 | 2.71 |
| 總債務 Total Debt | 15.01 | 18.41 | 18.16 |
| 現金及約當現金 | 2.98 | 1.86 | 0.98 |
| 淨負債 Net Debt | 11.25 | 15.84 | 16.69 |
| 流動資產 | 6.36 | 5.83 | 4.96 |
| 流動負債 | 4.18 | 4.22 | 4.58 |

- 淨負債：FY2023 為 8.69B，FY2025 為 15.84B（兩年增加 7.15B）；2026-06-30 進一步增至 16.69B USD。
- 淨負債 / EBITDA：以 FY2025 淨負債 ÷ 正規化 EBITDA 5.10B 計約 3.1x；以 info TTM EBITDA 4.68B 計約 3.4x（計算，使用 FY2025 淨負債）。
- 流動比率：2026-06-30 為 1.09（FY2025 為 1.38）；營運資金由 FY2025 的 1.61B 縮減至 2026-06-30 的 0.39B USD。
- 負債權益比（總債務 / 股東權益）：2026-06-30 約 131%（FY2025 約 122%）；info.debtToEquity 為 106.3%（口徑不同，以計算值為準）。
- 現金：2026-06-30 現金 0.98B USD，低於 FY2025 的 1.86B，短期流動性依賴循環信用與再融資。
- 其他：Long Term Equity Investment 為 5.58B USD（2026-06-30），由 Earnings From Equity Interest 約 0.65B USD（FY2025）支撐，屬非現金收益來源。Assets Held For Sale 為 0.43B USD（FY2025）。

## Capital allocation & insider signal

**資本配置**
- 股利：年化股利 7.24 USD（dividendRate；最近一次 1.81 USD，lastDividendDate 2026-10-01），殖利率 2.3%。
- 股利覆蓋：FY2025 股利支出 1.58B USD，OCF 覆蓋 2.06 倍，但 FCF 為 -3.77B，股利完全依賴舉債支應。股利 / 正規化淨利約 61.5%。info.payoutRatio 為 75.7%。
- 舉債：淨發債（Net Issuance Payments of Debt）FY2023 為 3.17B、FY2024 為 3.90B、FY2025 為 3.88B USD，三年合計約 10.95B USD。
- 買回：現金流量表中未見 Repurchase of Capital Stock 項目；流通股數 FY2022 為 222.5M，FY2025 為 222.7M，持平，未見實質買回。
- 股本：2026-06-30 季報 Share Issued 欄位顯示 223M（前期為 249M），與 info.sharesOutstanding 222.69M 一致，但前後欄位口徑不同，見 Red flags。

**內部人交易（6 個月窗口：2026-05-13 至 2026-11-13）**
- 窗口內快取資料無內部人公開市場交易紀錄，窗口內淨買賣為 0 股。快取中最近一筆為 2026-05-01 CFO Melissa N. Schaeffer 賣出 2,714 股（每股 303.76 USD，約 0.82M USD），略早於窗口起點。
- 窗口外但值得關注：2026-02-12 Mantle Ridge, L.P.（持股 >10% 的 beneficial owner）賣出 70,175 股（每股 284.21 USD，約 19.94M USD），另有一筆 1,759 股贈與。
- 規模：即使計入 CFO 的 0.82M USD 賣出，亦佔市值 0.001%，可忽略；Mantle Ridge 的 19.94M USD 佔市值約 0.03%。
- 例行薪酬授予（2024-12 與 2025-12 的 Stock Award，例如 CEO Menezes 17,376 股、CFO Schaeffer 8,357 股）不視為交易訊號。
- 股權結構：insidersPercentHeld 1.89%，institutionsPercentHeld 94.66%（2,256 家機構）。前幾大持股：BlackRock 8.23%（18.32M 股）、Vanguard Capital Management 6.53%、State Farm 5.32%、Capital Research Global Investors 4.76%。Vanguard Portfolio Management 於 2026-06-30 持股較前期增加 54.9%。

## Valuation

**估值指標（以 2026-11-12 快取價格 313.50 USD 計）**

| 指標 | 數值 | 計算 / 來源 |
|---|---|---|
| 市值 | 69.81B USD | info.marketCap；驗算：313.50 × 222.69M 股 ≈ 69.81B |
| 企業價值 EV | 89.99B USD | info.enterpriseValue |
| Trailing P/E（info） | 131.2x | 依 info.trailingEps 2.39，與季報加總 EPS -0.22 不一致，不採用 |
| Trailing P/E（GAAP，季報加總） | n/m | TTM Diluted EPS 約 -0.22 |
| Forward P/E | 20.2x | info.forwardPE（forwardEps 15.54） |
| 當年度 P/E（priceEpsCurrentYear） | 21.8x | info（epsCurrentYear 14.37） |
| EV/EBITDA（TTM，info） | 19.2x | EBITDA TTM 4.68B |
| EV/EBITDA（FY2025 正規化） | 17.6x | 89.99B ÷ 正規化 EBITDA 5.10B |
| P/S（TTM） | 5.37x | info.priceToSalesTrailing12Months |
| P/FCF | n/m | FCF TTM 為負 |
| P/OCF（TTM，計算） | 約 15.3x | 69.81B ÷ OCF 季報加總 4.57B |
| P/B | 4.89x | info.priceToBook |
| PEG | 2.27 | info.pegRatio |
| Beta | 0.669 | info.beta |

- 價格位置：52 週區間 229.11 – 324.00 USD，現價距 52 週高點 -3.2%；50 日均線 295.27、200 日均線 292.07，現價位於兩均線之上。52 週漲幅 +19.8%。
- 分析師：21 位，評級均值 1.92（averageAnalystRating「1.9 - Buy」），目標價均值 344.10、中位數 347.00、高 375.00、低 275.00 USD。
- 空頭部位：Short % of float 2.15%，short ratio 4.77 日（2026-10-30 資料）。
- 同業中位數（sector median）：DATA_UNAVAILABLE。工具未提供同業估值中位數，本報告不以估計值代替。

**估值判讀（定性）**：以 forward EPS 計 P/E 約 20x，估值數字上不算貴；但該 forward EPS 15.54 高於 FY2025 正規化 EPS 11.56 約 34%，代表市場與分析師假設盈餘大幅回升。若 FY2026–FY2027 正規化獲利未能達到此水準，估值將顯得偏貴。trailing P/E 與 P/FCF 皆無法使用，估值支撐完全落在盈餘回復假設上。

## Key catalysts

- **最近財報**：2026-11-05 公布 FQ4 FY2026，Reported EPS 3.61 vs 預估 3.61（surprise -0.02%，符合預期）。該季損益表細項不在快取中，營收與毛利為 DATA_UNAVAILABLE。
- **下次財報**：2027-01-29（earnings_dates 與 info.earningsTimestampStart，屬預估日期），預估 EPS 3.43 USD（對應 FQ1 FY2027）。
- **股利**：最近一次 1.81 USD（2026-10-01）；info.exDividendDate 為 2027-01-04（資料欄位，未經公司公告確認）。
- **FQ3 FY2026 特殊損失 -2.91B USD**：為 GAAP 獲利轉負的主因，性質與是否可能再現未於快取中說明，是本案最關鍵的未解資訊。
- **在建工程轉產**：Construction In Progress 13.46B USD（FY2025）為大型專案的未來產能來源；產能投產時點與 FCF 轉正時點是中期催化劑。
- **資產處分**：Assets Held For Sale 0.43B USD（FY2025）與 FY2025 的資產處分損失，顯示公司仍在進行資產組合調整。
- **管理層**：CEO Eduardo F. Menezes、CFO Melissa N. Schaeffer（companyOfficers）。管理層異動 DATA_UNAVAILABLE。
- **指引（guidance）**：快取中無公司正式財年指引文字，DATA_UNAVAILABLE。

## Metrics table

單位：營收與現金流以 USD B 表示；市值與淨負債以 USD B 表示；比率以 % 或 x 表示；FY = 9/30 財年。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（USD B，FY2025） | 12.04 | -0.5% | DATA_UNAVAILABLE | 持平偏弱 |
| 營收 TTM 季報加總（USD B） | 12.60 | FQ3 單季 +4.6% | DATA_UNAVAILABLE | 微幅回升 |
| 毛利率（FY2025） | 31.4% | -1.1 pt | DATA_UNAVAILABLE | 尚可 |
| 營業利益率（Operating Income，FY2025） | 24.0% | -0.4 pt | DATA_UNAVAILABLE | 強 |
| 正規化淨利率（FY2025） | 21.4% | -0.3 pt | DATA_UNAVAILABLE | 強 |
| GAAP 淨利率（FY2025） | -3.3% | 由 FY2024 +31.6% 轉負 | DATA_UNAVAILABLE | 弱（一次性項目） |
| GAAP EPS TTM（季報加總，USD） | -0.22 | — | DATA_UNAVAILABLE | 弱 |
| 正規化 EPS（FY2025，USD） | 11.56 | -1.8% | DATA_UNAVAILABLE | 持平 |
| ROE（info TTM，GAAP） | 3.2% | — | DATA_UNAVAILABLE | 弱 |
| ROE（正規化，FY2025，計算） | 16.1% | — | DATA_UNAVAILABLE | 尚可 |
| ROIC（FY2025，計算） | 7.1% | FY2024 8.5% | DATA_UNAVAILABLE | 偏弱 |
| OCF（USD B，FY2025） | 3.26 | -10.7% | DATA_UNAVAILABLE | 下滑 |
| Capex（USD B，FY2025） | 7.02 | +3.3% | DATA_UNAVAILABLE | 高，仍在擴張期 |
| Capex / 營收（FY2025） | 58.3% | +2.1 pt | DATA_UNAVAILABLE | 極高 |
| FCF（USD B，FY2025） | -3.77 | 較 FY2024 -3.15 惡化 | DATA_UNAVAILABLE | 弱 |
| FCF / 淨利 | n/m | — | 0.9（健康門檻） | 弱 |
| FCF margin（FY2025） | -31.3% | — | DATA_UNAVAILABLE | 弱 |
| 淨負債（USD B，FY2025） | 15.84 | +40.8% | DATA_UNAVAILABLE | 弱 |
| 淨負債 / EBITDA（正規化，FY2025） | 3.1x | — | DATA_UNAVAILABLE | 偏高 |
| 流動比率（2026-06-30） | 1.09 | FY2025 1.38 | DATA_UNAVAILABLE | 偏弱 |
| 負債權益比（總債務 / 股東權益，2026-06-30） | 131% | FY2025 122% | DATA_UNAVAILABLE | 偏高 |
| 現金（USD B，2026-06-30） | 0.98 | FY2025 1.86（-47%） | DATA_UNAVAILABLE | 偏低 |
| 股利覆蓋（OCF / 股利，FY2025） | 2.06x | — | DATA_UNAVAILABLE | 尚可（FCF 不覆蓋） |
| 股利 / 正規化淨利（FY2025） | 61.5% | — | DATA_UNAVAILABLE | 中等 |
| 殖利率 | 2.3% | — | DATA_UNAVAILABLE | 中性 |
| 內部人淨買賣（6 個月窗口） | 0 股（窗口內無交易） | 窗口外 Mantle Ridge 賣出 19.94M USD（2026-02） | DATA_UNAVAILABLE | 中性偏警示 |
| Forward P/E | 20.2x | — | DATA_UNAVAILABLE | 中性 |
| Trailing P/E | n/m（GAAP）；info 131.2x 不採用 | — | DATA_UNAVAILABLE | 不適用 |
| EV/EBITDA（TTM，info） | 19.2x | — | DATA_UNAVAILABLE | 偏高 |
| P/S（TTM） | 5.37x | — | DATA_UNAVAILABLE | 偏高 |
| P/FCF | n/m | — | DATA_UNAVAILABLE | 不適用 |
| P/B | 4.89x | — | DATA_UNAVAILABLE | 偏高 |
| PEG | 2.27 | — | DATA_UNAVAILABLE | 偏高 |
| 分析師目標價均值（USD） | 344.10（+9.8%） | — | DATA_UNAVAILABLE | 偏多（21 位，Buy） |
| 52 週位置 | 距高點 -3.2% | 52 週 +19.8% | DATA_UNAVAILABLE | 接近高檔 |

## Red flags

- **自由現金流連續 3 年為負**（FY2023 -1.42B、FY2024 -3.15B、FY2025 -3.77B USD），FCF margin 惡化至 -31.3%；FQ3 FY2026 雖單季轉正，TTM 仍為負。
- **GAAP 獲利受大額特殊損失影響**：FY2025 淨利 -0.39B USD；FQ3 FY2026 特殊損失 -2.91B USD，單季淨利 -1.44B USD。性質與是否可能再現未於快取中說明。
- **股利由舉債支應**：FY2025 股利 1.58B USD，FCF 為 -3.77B；FY2023–FY2025 淨發債合計約 10.95B USD，財務彈性收斂。
- **淨負債持續擴張**：淨負債 FY2023 8.69B → FY2025 15.84B → 2026-06-30 16.69B USD；股東權益由 FY2024 的 17.04B 降至 2026-06-30 的 13.88B，槓桿提高且股東權益縮減。
- **營收未成長，資本支出倍增**：FY2022–FY2025 營收 CAGR 約 -1.8%，同期 Capex 由 2.93B 增至 7.02B USD，Capex / 營收達 58%；投資回收尚未在財報上顯現。
- **流動性收緊**：現金由 FY2024 的 2.98B 降至 2026-06-30 的 0.98B USD，流動比率 1.09。
- **估值對盈餘回復高度敏感**：trailing P/E 與 P/FCF 皆不可用，forward P/E 依賴 forward EPS 15.54（較 FY2025 正規化 EPS 高約 34%）。
- **內部人與大股東出脫**：Mantle Ridge（>10% 股東）2026-02 賣出 19.94M USD；窗口內內部人無買入，無內部人加碼訊號。
- **資料異常（需下游注意）**：
  1. info.trailingEps 2.39 與 info.netIncomeToCommon 0.53B USD，與季報加總（EPS -0.22、淨利約 -0.05B USD）嚴重不一致；本報告 GAAP 獲利判斷以季報為準，info 的 trailing P/E 不採用。
  2. info.totalRevenue TTM 12.99B 與季報加總 12.60B 差約 3%。
  3. 季報 Share Issued 欄位由 249M 變為 223M（2026-06-30），口徑不一致，流通股數以 info 222.69M 為準。
  4. 2026-09-30 季（FQ4 FY2026）損益表與現金流明細缺漏，僅有 earnings_dates 的 EPS 3.61，FY2026 全年財務為 DATA_UNAVAILABLE。
  5. 價格快照：info.currentPrice 313.50 與 fast_info.last_price 315.555（cnyes cache，2026-11-12 15:01 UTC）不同，本報告市值與估值以 info 為準，差距約 0.65%。
  6. 分部營收、同業估值中位數、正式財年指引與 2026-11-13 當日收盤價皆為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
