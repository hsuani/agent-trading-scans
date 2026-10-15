# Fundamentals — LAES as of 2026-10-15

## Executive summary
LAES (SEALSQ Corp, NASDAQ) 的帳上現金約 4.82 億美元 (2026-06-30), 總負債很低 (total debt 約 714 萬美元, 流動比率 14.43x), 短期償債壓力可忽略; 但營運仍深度虧損, FY2025 營業利益率 -218.1%, FCF -3,250 萬美元, 且 2025 年流通股數約增加 90% (101.5M 股增至 193.0M 股), 獲利與稀釋風險是主要財務問題。估值上, EV 為負 (market cap 約 4.14 億美元低於淨現金約 4.75 億美元), P/B 0.77x 看似偏低, 但 P/E、forward P/E、P/FCF、EV/EBITDA 均因分母為負而無法有效比較, 估值吸引力取決於市場是否相信其現金能支撐到營運轉正。內部人 2026-04-15 至 2026-10-15 期間僅有公開市場賣出 (合計約 76.7 萬美元, 約占市值 0.19%), 無買進紀錄, 信號偏負面但規模不大。

資料時效: 本報告以 2026-10-15 為 as-of。價格為 2026-10-14 收盤 1.84 美元 (盤前 2026-10-15 報 1.78 美元, 屬 as-of 當日資料, 未超出 as-of 日期)。財報數據截至 2026-06-30 (季度資產負債表) 與 FY2025 (年報)。季度損益表 quarterly_fin 工具回傳為空, 2026 上半年損益與 2026-09-11 前後財報內容 (若已公布) 均為 DATA_UNAVAILABLE。

## Revenue & profitability

**營收與成長**
- 年度營收 (yfinance financials, 單位 USD): FY2022 2,319.8 萬, FY2023 3,005.8 萬, FY2024 1,098.1 萬, FY2025 1,825.2 萬。
- FY2025 YoY +66.2% (1,825.2 萬 vs 1,098.1 萬); 但 FY2025 仍低於 FY2023 高點 39.3%。
- 3 年 CAGR (FY2022 至 FY2025): -7.7%; FY2023 至 FY2025 2 年 CAGR: -22.1%。5 年 CAGR 因資料不足 (2021 無營收) 為 n/a。
- yfinance info 的 TTM revenue 為 2,457.8 萬美元, revenueGrowth 為 +131.1% (TTM 基準, 與年報 YoY 口徑不同, 僅供參考)。
- 分部營收 (segment mix): DATA_UNAVAILABLE。公司業務描述包含 secure chips (VaultIC、quantum-resistant RISC-V)、PKI / 數位身分服務、SaaS 與 ASIC 設計服務, 但 yfinance 未提供各業務線營收占比。

**毛利、營業利益、淨利率趨勢**

| 年度 | 營收 (百萬 USD) | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|---|
| FY2022 | 23.2 | 42.2% | 11.1% | 24.9% |
| FY2023 | 30.1 | 46.7% | -13.8% | -10.9% |
| FY2024 | 11.0 | 33.9% | -156.6% | -193.1% |
| FY2025 | 18.3 | 47.3% | -218.1% | -187.3% |

- 毛利率於 FY2025 回升至 47.3% (較 FY2024 +13.4 個百分點), 顯示產品組合或成本結構改善, 但規模仍小。
- 營業費用結構嚴重不成比例: FY2025 R&D 1,247.7 萬 (營收 68.4%)、SG&A 3,855.9 萬 (營收 211.2%)。SG&A 中含 SBC (股份基礎薪酬) 1,126.1 萬, 占營收 61.7%。
- 淨利 FY2025 為 -3,419.4 萬美元, 淨利率 -187.3%; 稅率接近 0 (FY2025 tax rate 0.47%), 淨利與營業利益差異主要來自利息收入淨額 (+559.9 萬)。
- ROE (yfinance info, TTM): -12.3%。以 FY2025 淨利 / 年底股東權益計算約 -7.4%, 以平均權益計算約 -12.7%。
- ROIC (估計, EBIT / 期末 invested capital): FY2025 約 -7.3% (EBIT -3,398.5 萬 / invested capital 4.632 億); 這是估計值, 非 yfinance 直接提供。

## Cashflow & balance sheet

**現金流品質**
- 營運現金流 (OCF): FY2023 -274.5 萬, FY2024 -1,012.4 萬, FY2025 -3,125.7 萬 (惡化幅度約 209%)。info TTM OCF 為 -4,310.9 萬, 高於 FY2025 年報的燒錢速度, 顯示近期燒錢幅度仍在擴大。
- 自由現金流 (FCF, OCF 減 capex): FY2023 -576.6 萬, FY2024 -1,069.5 萬, FY2025 -3,250.0 萬。
- FCF margin: FY2025 -178.1%, FY2024 -97.4%。
- FCF / 淨利比 FY2025 為 0.95, 雖高於 0.9 門檻, 但因 FCF 與淨利皆為負值, 此比率無 "健康" 意義, 只表示現金虧損與帳面虧損同步。
- Capex: FY2023 302.1 萬 (營收 10.1%)、FY2024 57.1 萬 (5.2%)、FY2025 124.3 萬 (6.8%)。Capex 規模小, 燒錢主因是營運成本而非資本支出。

**資產負債表 (最新: 2026-06-30)**

| 項目 | 2026-06-30 | 2025-12-31 | 備註 |
|---|---|---|---|
| 現金及短期投資 | 4.822 億 | 4.277 億 | 現金 4.798 億 + 短期投資 |
| 總負債 (total debt) | 714 萬 | 800 萬 | 2025 年底其中長期 99 萬 |
| 淨現金 (cash - total debt) | 約 4.751 億 | 約 4.197 億 | 自行計算 |
| 流動資產 / 流動負債 | 5.218 億 / 3.616 億 | 4.496 億 / 2.825 億 | 流動比率 14.43x / 15.92x |
| 股東權益 | 5.547 億 | 4.615 億 | 2026-06-30 含少數股權 746 萬 |
| 總資產 | 6.146 億 | 5.042 億 | |
| 保留盈餘 | -1.038 億 | -7,610.7 萬 | 持續累積虧損 |
| 商譽 + 無形資產 | 2025 年底 2,661 萬 | n/a | 2025 年收購 (purchase of business 1,055 萬) |

- Debt/Equity: 1.27% (yfinance info, 以百分比表示); 以 2026-06-30 數據估算約 1.29%。
- 2025 年底應付關係人款項 (Due to related parties) 為 566.8 萬, 2024 年為 467.7 萬, 屬於關係人往來 (依公司摘要為 WISeKey 體系), 需留意關聯交易。
- 2025 年底長期投資 (equity method) 1,421.7 萬, 股權型投資風險細節 DATA_UNAVAILABLE。
- 流動性充足; 以 TTM OCF -4,310.9 萬計, 帳上現金可覆蓋約 11 年 (僅為示意性估算, 未計成長投資與稀釋因素)。

## Capital allocation & insider signal

**資本配置**
- 股利: 無 (dividendYield 0.0%, payoutRatio 0.0%)。
- 庫藏股 / 回購: 無紀錄 (treasury shares 2023 為 0, 2024 與 2025 無數據)。
- 股權融資是主要資金來源: 2025 年發行股本 4.293 億美元, 2024 年 6,000 萬美元; 2025 年另有 Proceeds From Stock Option Exercised 740.1 萬。
- 2025 年償還負債 512.7 萬, 2024 年新增負債 2,000 萬、償還 140.7 萬。
- 股本稀釋:
  - 流通股數 (Ordinary Shares): 2023 年底 1,694.7 萬股 → 2024 年底 1.015 億股 → 2025 年底 1.930 億股 (2025 年 +90.1%) → 2026-06-30 2.249 億股 (2026 上半年再 +16.5%)。
  - Diluted 平均股數: FY2024 2,775.0 萬 → FY2025 1.350 億 (+386.6%)。
- 結論: 資本配置以「增資 + 研發與行銷擴張」為主, 尚無股東報酬機制, 股東稀釋是目前最大的資本配置風險。

**內部人交易 (yfinance insider, 2026-04-15 至 2026-10-15, 公開市場 "Sale at price" 列)**

| 內部人 | 職位 | 期間賣出股數 (約) | 期間賣出金額 (約, USD) | 備註 |
|---|---|---|---|---|
| O'Hara John Charles | CFO | 約 9.6 萬 (04-17 至 06-05 共 6 筆) | 約 29.6 萬 | 多次分批賣出, 價格區間 2.69 至 3.69 |
| Moreira Carlos Creus | CEO / Chairman | 約 3.1 萬 (05-29、06-03、06-05) | 約 11.2 萬 | 價格 3.50 至 3.69 |
| Enguent Jean-Pierre | Officer (R&D 系統與方案副總) | 約 11.0 萬 (05-06 至 10-06 共 6 筆, 含 10-06 35,000 股) | 約 30.1 萬 | 約每月一次, 多筆在行使期權 (0.01 美元行使價) 後賣出, 規律性高 |
| Buonanno Franck Jean | Officer (全球銷售副總) | 約 2.0 萬 (05-14) | 約 5.8 萬 | 2.90 美元賣出 |

- 合計公開市場賣出 (上述列表加總): 約 25.7 萬股、約 76.7 萬美元 (依 yfinance Value 欄位加總), 占 market cap 約 0.19%。
- 期間內無公開市場買進紀錄 (Purchase 列)。
- 另有多筆期權行使列示 (Conversion of Exercise of derivative security, 行使價 0.01 美元), 行使股數未逐筆加總 (視為 DATA_UNAVAILABLE)。Peter Ward (Director) 於 2026-06-16 行使 366,746 股, 未見同日賣出紀錄。
- 解讀: 內部人 6 月賣價約 3.5 美元, 目前股價 1.84 美元; 規律性賣出 (Enguent) 可能屬於既定交易計畫, 但 yfinance 未提供 10b5-1 標記, 無法確認。
- 機構持股: 6.65% (institutionsCount 127); 內部人持股 2.69%; 最大機構 UBS 持 0.71%, 持股集中度低。
- 大股東 (WISeKey 體系) 的持股比例: DATA_UNAVAILABLE (yfinance major_holders 未提供)。
- 融券: 9.70M 股 (2026-09-30), 占 float 約 4.49%, short ratio 1.99 日, 月比前期 11.75M 股下降約 17.5%。

## Valuation

| 指標 | 數值 | 說明 |
|---|---|---|
| Price | 1.84 USD | 2026-10-14 收盤 |
| Market cap | 4.139 億 USD | yfinance info |
| Trailing P/E | n/m | TTM EPS -0.20 |
| Forward P/E | n/m | forward EPS -0.27 (yfinance forwardPE -6.81) |
| P/S (TTM) | 16.84x | 市值 / TTM 營收 2,457.8 萬 |
| P/B | 0.77x | BVPS 2.402 USD |
| EV | -4,277 萬 USD | yfinance enterpriseValue |
| EV/EBITDA | n/m | EV 與 TTM EBITDA (-4,607.4 萬) 皆為負; yfinance 顯示的 0.928x 為負除以負, 無經濟意義 |
| EV/Revenue | -1.74x | EV 為負, 無經濟意義 |
| P/FCF | n/m | TTM FCF 為負 |
| 分析師目標價 | 平均 5.875 / 最低 3.75 / 最高 8.00 USD | 僅 2 位分析師覆蓋, recommendationKey 為 none |
| 股價表現 | 52 週 -69.7%; 較 52 週低點 1.83 僅高 0.5%; 較 200DMA 3.09 低 40.5% | 同期 S&P 500 52 週 +15.7% (yfinance) |
| 產業中位數 (Semiconductors / Technology) | DATA_UNAVAILABLE | 工具未提供產業中位數, 不予估計 |

- 估值判斷: 以 P/B 0.77x 與負 EV 衡量, 市場給予的價值低於帳面淨資產與現金, 但這反映的是營運燒錢與持續增資稀釋的預期, 而非估值便宜的直接證據。P/S 16.84x 在營收大幅波動 (FY2023 至 FY2025 下降 39%) 且毛利率不穩的情況下偏高。
- 技術面參考 (ta.py snapshot, 非基本面但影響估值解讀): RSI(14) 24.3 接近超賣, 股價低於 MA20 (2.26) 18.6%、MA50 (2.41) 23.8%、MA200 (3.09) 40.5%; MACD 柱狀體為負 (-0.045); ATR(14) 0.114 (約 6.2% 股價)。

## Key catalysts
- 最近一次財報: yfinance earnings timestamp 為 2026-09-11 12:30 UTC, 電話會議 2026-09-15 13:00 UTC, 皆早於 as-of 日期。但季度損益表 (quarterly_fin) 回傳為空, 2026 Q2 (或 H1) 的營收、EPS 與 surprise 數據為 DATA_UNAVAILABLE。
- 下次財報: yfinance earnings_dates 列出 2027-03-22 (EPS estimate 為 n/a)。
- 公司指引 (guidance): DATA_UNAVAILABLE。僅有 consensus-type 欄位: 本年度 EPS -0.24 (epsCurrentYear), forward EPS -0.27。
- 股本: 2025 年大規模增資後, 2026 上半年股數再增 16.5%, 後續是否再增資為主要催化劑 (正負皆可能, 視融資條件)。
- 收購與投資: 2025 年收購 (purchase of business 1,054.9 萬, 商譽 565.6 萬, 無形資產 2,095.3 萬), 以及 1,421.7 萬美元權益法投資, 對營收與獲利的貢獻 DATA_UNAVAILABLE。
- 內部人持續出售 (Enguent 規律月賣, 最近 2026-10-06 賣出 35,000 股 @2.46) 為短期負面訊號。
- 融券比率與空單: 占 float 4.49%, 非極端水準。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY, USD) | 1,825.2 萬 (FY2025) | +66.2% | DATA_UNAVAILABLE | 反彈但仍低於 FY2023 高點 39.3% |
| 營收 3 年 CAGR (FY22-25) | -7.7% | n/a | DATA_UNAVAILABLE | 弱 |
| 毛利率 | 47.3% (FY2025) | +13.4 pts | DATA_UNAVAILABLE | 改善, TTM 52.6% (info) 需季度資料驗證 |
| 營業利益率 | -218.1% (FY2025) | -61.5 pts (惡化) | DATA_UNAVAILABLE | 嚴重虧損 |
| 淨利率 | -187.3% (FY2025) | +5.8 pts | DATA_UNAVAILABLE | 嚴重虧損 |
| ROE | -12.3% (TTM, info) | n/a | DATA_UNAVAILABLE | 弱 |
| ROIC (估計) | -7.3% (FY2025) | n/a | DATA_UNAVAILABLE | 弱 |
| OCF (FY, USD) | -3,125.7 萬 | 惡化約 209% | DATA_UNAVAILABLE | 弱 |
| FCF (FY, USD) | -3,250.0 萬 | 惡化約 204% | DATA_UNAVAILABLE | 弱 |
| FCF margin | -178.1% | -80.7 pts (惡化) | DATA_UNAVAILABLE | 弱 |
| FCF / NI | 0.95 (兩者皆負) | n/a | 約 0.9 以上為健康 | 不適用, 非健康訊號 |
| Capex (FY, USD) | 124.3 萬 | +117.7% | DATA_UNAVAILABLE | 規模小 |
| SBC / 營收 | 61.7% (FY2025) | 由 1.3% (FY2024) 升至 61.7% | DATA_UNAVAILABLE | 極高, 稀釋與獲利品質風險 |
| 現金及短期投資 (2026-06-30) | 4.822 億 USD | +12.8% (vs 2025-12-31) | DATA_UNAVAILABLE | 強 |
| 總負債 (2026-06-30) | 714 萬 USD | -10.7% | DATA_UNAVAILABLE | 極低 |
| 淨現金 (2026-06-30) | 4.751 億 USD | +13.2% | DATA_UNAVAILABLE | 強 |
| 流動比率 | 14.43x | 由 15.92x 降至 14.43x | DATA_UNAVAILABLE | 極強 |
| Debt / Equity | 1.27% (info) | 由 1.73% (2025 年底) 降至 1.27% | DATA_UNAVAILABLE | 極低 |
| 流通股數 (2026-06-30) | 2.249 億股 | +90.1% (2025 年); +16.5% (2026 H1) | DATA_UNAVAILABLE | 高度稀釋 |
| 股利殖利率 / 回購 | 0% / 無 | n/a | DATA_UNAVAILABLE | 不適用 |
| 內部人淨買賣 (2026-04-15 至 10-15) | 淨賣出約 76.7 萬 USD, 無買進 | n/a | DATA_UNAVAILABLE | 偏負面 (規模小) |
| 機構持股 | 6.65% (127 家) | n/a | DATA_UNAVAILABLE | 偏低 |
| 融券占 float | 4.49% (2026-09-30) | 月減 17.5% | DATA_UNAVAILABLE | 中性 |
| Trailing P/E | n/m (EPS -0.20) | n/a | DATA_UNAVAILABLE | 不適用 |
| Forward P/E | n/m (forward EPS -0.27) | n/a | DATA_UNAVAILABLE | 不適用 |
| P/S (TTM) | 16.84x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/B | 0.77x | n/a | DATA_UNAVAILABLE | 低於帳面, 反映燒錢預期 |
| EV/EBITDA | n/m (EV、EBITDA 皆負) | n/a | DATA_UNAVAILABLE | 不適用 |
| P/FCF | n/m (FCF 為負) | n/a | DATA_UNAVAILABLE | 不適用 |
| 股價 vs 52 週高點 (info 7.749) | -76.3% | 52 週股價 -69.7% | DATA_UNAVAILABLE | 大幅弱勢 |
| 分析師目標價均值 | 5.875 USD (2 位) | n/a | DATA_UNAVAILABLE | 覆蓋不足, 參考價值低 |
| 下次財報日 | 2027-03-22 (yfinance) | n/a | DATA_UNAVAILABLE | 資訊 |

## Red flags
- 持續且擴大的營運虧損: FY2025 營業利益 -3,979.9 萬美元, 營業利益率 -218.1%, 未見轉正跡象。
- 燒錢加速: OCF 由 FY2024 -1,012.4 萬擴大到 FY2025 -3,125.7 萬; TTM OCF -4,310.9 萬。
- 股本大幅稀釋: 2025 年流通股數 +90.1%, 2026 上半年再 +16.5%; diluted 平均股數 FY2025 較 FY2024 增 386.6%。
- SBC 占營收 61.7% (FY2025 由 1.3% 跳升), 股東獲利品質與實際現金成本差距大。
- 營收不穩: FY2022 至 FY2025 3 年 CAGR -7.7%, FY2024 大幅萎縮後僅部分反彈; TTM 與年報口徑差異大, 季度資料缺失。
- 累積虧損擴大: 保留盈餘由 2025 年底 -7,610.7 萬 降至 2026-06-30 -1.038 億 (半年虧損約 2,771 萬, 以 BS 差額估算)。
- 內部人持續公開市場賣出, 無買進: 含 CEO、CFO 於 2026 年 6 月以 3.50 至 3.69 美元出售, 目前股價 1.84 美元 (約 -48%)。
- 關係人往來: 應付關係人款項 2025 年底 566.8 萬; 公司為 WISeKey 體系子公司 (依 info 摘要), 關聯交易與控制權影響需另行查核 (大股東持股 DATA_UNAVAILABLE)。
- 分析師覆蓋極少 (2 位), 目標價離散度高 (3.75 至 8.00 美元), 不足以作為估值錨點。
- 估值指標失真: beta -7.513 (yfinance) 與 EV/EBITDA 0.928x 為負負相除產生, 不應用於決策; 52 週高點在 yfinance info (7.749) 與 ta.py 快照 (8.71) 不一致, 需以原始價格資料再核對。
- 資料缺口: quarterly_fin 為空, 無 2026 Q1 / Q2 損益、無分部營收、無 guidance、無大股東 (WISeKey) 持股比例、無產業中位數。info 中 TTM FCF (-3,242 萬) 與 TTM OCF (-4,310.9 萬) 口徑不一致, 以年報數字為準。
- 股價與技術面: 股價低於 MA20 / MA50 / MA200 (-18.6%、-23.8%、-40.5%), RSI(14) 24.3, MACD 負向。
- 數據來源: 全部資料來自 yfinance (cache 來源, cached_at 2026-10-15 11:20 UTC), 非即時 feed; 此為工具預期行為, 不影響結論, 但價格應於交易前再確認。

FUNDAMENTALS REPORT COMPLETE
