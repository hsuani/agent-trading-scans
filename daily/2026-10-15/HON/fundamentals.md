# Fundamentals — HON as of 2026-10-15

## Executive summary
HON 體質呈現「現金流穩健、槓桿偏高、GAAP 盈餘失真」：FY2025 FCF 為 5.42B（FCF/NI 1.15x），但 2026-06-30 淨負債 25.24B（約 2.7x TTM normalized EBITDA），且 2026Q2 含約 5.9B 稅前一次性處分利益，使 trailing P/E 7.65x、ROE 46.6% 等 GAAP 指標無法直接用於比較。以 normalized 或調整後口徑計，TTM P/E 約 11.7–13.0x、EV/EBITDA 約 10.0x、forward P/E 21.2x，估值相對吸引，分析師平均目標價 255.35（較現價 +23.0%），但 3 年營收 CAGR 僅 1.8% 且股價仍低於 50 日與 200 日均線，成長動能偏弱。Quantinuum 暴露無法由現有工具分離，所有 Quantinuum 專屬數字均標示為 DATA_UNAVAILABLE。

## Revenue & profitability
**營收與成長**
- 年度 Total Revenue（USD）：2022 35,466M → 2023 33,009M → 2024 34,717M → 2025 37,442M。
- 3 年 CAGR（2022→2025）約 1.8%；YoY：2023 -6.9%、2024 +5.2%、2025 +7.8%。4 年 CAGR 為 n/a（2021 欄位 null）。
- TTM 營收：以 quarterly_fin 加總 2025Q3 至 2026Q2 為 36,130M（計算值），與 info.totalRevenue 38,057M 不一致，列為資料衝突，本報告以 quarterly 原始欄位為準。
- 業務組合：longBusinessSummary 列出三大部門 Industrial Automation、Building Automation、Energy and Sustainability Solutions（含 UOP）。各部門營收與獲利為 DATA_UNAVAILABLE。摘要未提及 Aerospace，工具無法確認其目前是否已分拆或列為停業部門。

**獲利率趨勢（年度，由 financials 計算）**

| 指標 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Gross margin | 37.0% | 37.5% | 38.5% | 36.9% |
| Operating margin（Operating Income 欄） | 18.1% | 18.5% | 19.2% | 17.5% |
| Normalized EBITDA margin | 23.8% | 24.1% | 25.3% | 25.8% |
| GAAP net margin | 14.0% | 17.1% | 16.4% | 12.6% |
| Normalized income margin | 15.0% | 14.9% | 15.0% | 14.9% |
| R&D / 營收 | 4.2% | 4.2% | 4.2% | 4.8% |

- 2025 GAAP 獲利承壓主因為特殊項目：Total Unusual Items -1,435M，其中 Impairment 994M、Special Income Charges -1,483M。
- Normalized EBITDA 連續三年提升（23.8% → 25.8%），顯示核心營運利潤率改善；但 GAAP 營業利益率 2025 反而下降 1.7pp。
- ROE：FY2025 以平均權益計算約 29.1%（NI 4,729M / 平均權益 16,262M，計算值）；TTM GAAP ROE 約 44.3%（NI 8,213M / 2026-06-30 權益 18,537M，計算值）。兩者均受權益基數縮小與 Q2 一次性利益影響，不具可比性。TTM normalized ROE 約 27.4%（計算值）。
- ROIC（近似）：FY2025 EBIT 6,820M × (1 − 稅率 18.4%) / 平均 Invested Capital 49,071M ≈ 11.3%（計算值）；FY2024 約 13.6%。ROIC 呈下滑趨勢。

**盈餘品質（earnings_dates）**
- 列表 24 個已公布季度（2020-10 至 2026-07）EPS 全數高於一致預期；近 8 季平均 surprise 約 +6.3%。
- 注意：調整後 EPS 序列出現不連續，2026Q1 Reported EPS 4.90，2026Q2 為 1.95（預估 1.82），而 2026Q2 GAAP diluted EPS 為 17.83（含處分利益）。normalized income 2026Q2 為 1,065M，換算約 3.34/股，與調整後 1.95 亦不一致。三種 EPS 口徑之間的差異工具無法說明，列為資料缺口。

## Cashflow & balance sheet
**現金流量（cashflow / quarterly_cf）**

| 指標 | 2022 | 2023 | 2024 | 2025 | TTM（2025Q3–2026Q2，計算） |
|---|---|---|---|---|---|
| Operating Cash Flow | 5,274M | 5,340M | 6,097M | 6,408M | 5,118M |
| Capex | -766M | -741M | -871M | -986M | -1,108M |
| FCF（OCF − Capex） | 4,508M | 4,599M | 5,226M | 5,422M | 4,010M |
| FCF margin | 12.7% | 13.9% | 15.1% | 14.5% | 11.1%（÷ 36,130M） |
| FCF / GAAP NI | 0.91x | 0.81x | 0.92x | 1.15x | 0.49x（受處分利益影響） |
| FCF / normalized income | 0.85x | 0.93x | 1.00x | 0.97x | 0.79x |

- 2025 FCF 較 2024 增加 3.8%；但 2026Q1 FCF 為 -873M、Q2 為 961M，季度波動大。
- info.freeCashflow 為 2,610M，與由 quarterly 計算之 TTM FCF 4,010M 不一致，本報告採計算值並列為資料衝突。

**資產負債（quarterly_bs / balance_sheet，2026-06-30 為最新季）**
- Total Debt 33,988M；Cash and Cash Equivalents 8,751M；Net Debt 25,237M（2025-06-30 為 26,163M，YoY -3.5%）。
- Current Debt 7,760M；現金對短期債務覆蓋 1.13x。
- Total Assets 77,344M；Stockholders Equity 18,537M（2025-12-31 為 13,904M）；Tangible Book Value -7,843M（負值，商譽與無形資產 2025-12-31 合計 27,815M）。
- Minority Interest 由 2026-03-31 的 1,077M 降至 2026-06-30 的 320M；Long Term Equity Investment 於 2026Q2 出現 7,459M（前季 1,414M）。兩項變動與 Q2 處分利益的關係，以及是否與 Quantinuum 相關，工具無法確認，列為待核實項目。
- 比率：D/E 約 183%（計算值；info 為 185.4%）；info current ratio 1.21、quick ratio 0.76；Net Debt / TTM normalized EBITDA 約 2.7x（25,237M / 9,180M，計算值）；Total Debt / TTM normalized EBITDA 約 3.7x；利息保障倍數 FY2025 為 5.1x（EBIT 6,820M / 利息費用 1,344M），TTM 約 4.1x（TTM Operating Income 5,990M / 利息 1,447M）。

**債務流動（cashflow）**
- FY2025：Repayment of Debt -25,724M、Issuance of Debt +28,332M，屬大規模再融資。
- 2026Q1：Repayment of Debt -18,623M、Issuance 4,758M，淨償還 LTD 約 -12.6B；同季 Net Other Financing Charges 為 +15,743M。此大額項目性質工具無法說明，列為紅旗之一。

## Capital allocation & insider signal
**資本配置**
- Capex 占營收：2022 2.2%、2023 2.2%、2024 2.5%、2025 2.6%；Capex / D&A（FY2025）約 0.71x（D&A 1,388M，計算值），資本支出低於折舊攤銷。
- 併購：2024 Purchase of Business -8,880M；2025 -2,211M，同年 Sale of Business +1,157M。
- 股利：Cash Dividends Paid 2022 2,719M → 2023 2,855M → 2024 2,902M → 2025 2,976M（年增約 3%）；TTM 3,073M。TTM FCF 對股利覆蓋 1.30x，FY2025 為 1.82x。
- 買回：Repurchase of Capital Stock 2022 4,200M、2023 3,715M、2024 1,655M、2025 3,804M；TTM 1,200M；2026Q2 為 0（前季 2026Q1 為 1,000M）。2025 股利加買回合計 6,780M，約為 FY2025 FCF 的 125%，差額由舉債支應。
- 流通股數：Ordinary Shares 由 2022 年底 333.8M 降至 2026-06-30 的 316.8M，累計減少約 5.1%。
- 股利每股資料衝突：info.trailingAnnualDividendRate 為 9.40、dividendYield 為 1.35%（對應 $0.70 季股利、年化 2.80）、corporateActions 公告 $0.70（除息日 2026-11-13）。以現金流計算之 TTM 股利 3,073M 除以約 317M 股，約為每股 9.7，與 $0.70 不符。每股股利口徑為 DATA_CONFLICT，本報告不採用單一每股值，以 FCF 覆蓋率與 TTM 現金股利總額為準。

**內部人交易（insider，時間窗 2026-04-15 至 2026-10-15）**
- 公開市場賣出（Text 標示 "Sale at price"）：
  - Kenneth J. West（Officer）2026-07-27 賣出 17,032 股，約 $4.15M（均價約 243.77）；同日另有 17,032 股衍生性證券轉換（exercise），即行權後全數賣出，實際持股淨變動接近 0。
  - Kenneth J. West 2026-08-03 賣出 316 股，約 $77.6K（均價約 245.47）。
- 公開市場買入：窗口期內無任何買入紀錄。
- 未標示交易類型（Value 與 Text 皆空白）的紀錄數量多，涵蓋 CFO、General Counsel、CEO、Masso 等，時間集中於 2026-07 月中及月底，推測為 RSU 歸屬或稅款扣繳，但工具無法區分，故未計入淨買賣判斷。
- 董事 2026-04-15 有多筆相同股數（約 625 股）紀錄，推測為年度股權授予，同樣不計入買賣。
- 淨額：窗口期公開市場淨賣出約 $4.23M，占市值 65.80B 約 0.006%，強度極低；無叢集賣出，亦無買入訊號。insider 持股比例 0.081%。
- 對照（窗口期外）：2025-02 Anne T. Madden 賣出約 $6.0M、2025-08 Lucian Boldea 賣出約 $9.34M，均屬較早期事件。

**機構與空頭**
- 機構持股 84.5%，共 2,789 家。前十大合計約 39.7%：BlackRock 7.19%（QoQ -6.7%）、Vanguard Capital 6.53%、State Street 5.91%（QoQ +18.1%）、Newport Trust 4.06%（QoQ +100%）、Invesco 3.55%、Morgan Stanley 3.04%、Geode 2.59%、Vanguard Portfolio Mgmt 2.48%、Goldman Sachs 2.30%（QoQ +102%）、Franklin 2.05%（QoQ -3.9%）。
- Short interest：7,856,282 股，佔流通股 2.48%，較前月 6,445,823 股增加 21.9%；short ratio（days to cover）2.54 日。

## Valuation
**現價與規模**：現價 207.61（cache 2026-10-15 11:16 UTC）；市值 65.80B；企業價值 EV 91.88B（info）。

**估值倍數**

| 倍數 | 數值 | 計算基礎 |
|---|---|---|
| P/E trailing（GAAP） | 7.65x | info.trailingPE；含 2026Q2 處分利益，失真 |
| P/E TTM（調整後 EPS 17.67） | 約 11.7x | earnings_dates 最近四季 Reported EPS 加總，計算值 |
| P/E TTM（normalized income 5,074M / 318.6M 股） | 約 13.0x | 計算值 |
| P/E forward | 21.15x | info.forwardPE，forwardEps 9.82 |
| P/E 當年度（epsCurrentYear 8.30） | 約 25.0x | info.priceEpsCurrentYear |
| EV / EBITDA | 10.8x（info）／約 10.0x（TTM normalized EBITDA 9,180M，計算值） | |
| P/FCF | 約 16.4x（TTM FCF 4,010M，計算值）；約 25.2x（info FCF 2,610M） | 兩者差異來自 FCF 資料衝突 |
| P/S | 1.73x（info）／約 1.82x（TTM 營收 36,130M，計算值） | |
| P/B | 3.55x | bookValue 58.49/股 |
| PEG | 3.39x | 不具參考意義 |

**分析師共識**：23 位分析師，平均目標價 255.35、中位數 262、最高 303、最低 186；推薦均值 2.0（buy）。相對現價，平均目標價隱含 +23.0%，最低目標價隱含 -10.4%。

**技術位置（僅作背景）**：50 日均線 215.86（現價低 3.8%）；200 日均線 230.52（現價低 9.9%）；52 週區間 195.87–260.28（現價距低點 +6.0%、距高點 -20.2%）；52 週漲幅 +3.4%，同期 S&P 500 為 +15.7%；beta 0.888。

**相對同業估計**：Sector median 為模型依 US Industrials／Conglomerates 常見區間所作估計，非工具數據，僅供量級參考。以 normalized 或調整後口徑比較，HON 的 EV/EBITDA 與 P/FCF 低於估計中位數，forward P/E 接近估計中位數，顯示估值相對便宜，但需以 2026Q2 後的組合重組結果修正盈餘基礎。

## Key catalysts
- **下一次財報**：2026-10-22（earnings_dates 與 info 之 earningsTimestamp 一致），Q3 2026 EPS 一致預期 2.16。過去 24 季皆 beat。
- **除息**：每股 $0.70，除息日 2026-11-13，發放日約 2026 年 12 月初（dividendDate）。
- **近期指引（guidance）**：DATA_UNAVAILABLE，工具未提供管理層指引原文。
- **組合重組**：2025-12-31 Assets Held for Sale 2,492M；2026Q2 Gain On Sale of Business 約 5.9B（稅前）；Tax Effect of Unusual Items 約 1.22B；營收與 EPS 序列出現斷點。需以 10-Q 與 8-K 核實分拆、處分與停業部門的範圍。
- **Quantinuum 代理暴露**：
  - Quantinuum 營收、虧損、估值、NCI 歸屬與股權比例之獨立數字：DATA_UNAVAILABLE。
  - 間接線索（僅為觀察，未證實與 Quantinuum 相關）：2026Q2 NCI 由 1,077M 降至 320M；Long Term Equity Investment 由 1,414M 升至 7,459M；同季有 5.9B 處分利益。
  - 建議下游研究員以 Honeywell 10-Q 附註（Noncontrolling interests、Investments、Discontinued operations）核實。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue FY2025 | 37.44B | +7.8% | 3–5%（YoY 估計） | 中性 |
| Revenue CAGR 2022–2025 | 1.8% | — | 3–4%（估計） | 偏弱 |
| Gross margin FY2025 | 36.9% | -1.6pp | 30–35%（估計） | 中性偏佳 |
| Operating margin FY2025（Operating Income） | 17.5% | -1.7pp | 15–18%（估計） | 中性 |
| Normalized EBITDA margin FY2025 | 25.8% | +0.5pp | 20–25%（估計） | 健康 |
| GAAP net margin FY2025 | 12.6% | -3.8pp | 10–12%（估計） | 中性（含減損） |
| ROE FY2025（平均權益） | 29.1% | — | 15–20%（估計） | 偏高（權益基數小，非典型） |
| ROIC FY2025（近似） | 11.3% | 2024 約 13.6% | 10–12%（估計） | 中性偏弱 |
| FCF FY2025 | 5.42B | +3.8% | — | 健康 |
| FCF margin FY2025 | 14.5% | -0.6pp | 10–15%（估計） | 中性偏佳 |
| FCF / GAAP NI FY2025 | 1.15x | — | >0.9（判準） | 健康 |
| FCF TTM（計算） | 4.01B | — | — | 波動（2026Q1 為負） |
| Net Debt（2026-06-30） | 25.24B | -3.5%（vs 2025-06-30） | — | 偏高 |
| Net Debt / TTM normalized EBITDA | 2.7x | — | 2.0–2.5x（估計） | 偏高 |
| Debt / Equity | 183% | — | 80–100%（估計） | 偏高 |
| Current ratio（info） | 1.21 | — | 1.2–1.5（估計） | 中性 |
| Quick ratio（info） | 0.76 | — | 0.8–1.0（估計） | 中性偏弱 |
| Interest coverage FY2025（EBIT/利息） | 5.1x | — | 8–10x（估計） | 偏弱 |
| Tangible Book Value（2026-06-30） | -7.84B | 2025-12-31 為 -13.91B | — | 紅旗（負值） |
| Dividends paid TTM | 3.07B | — | — | FCF 覆蓋 1.30x，中性 |
| Share repurchase FY2025 | 3.80B | +130%（vs 2024） | — | 2026Q2 為 0，動能減緩 |
| Ordinary shares outstanding | 316.8M（2026-06-30） | -5.1%（vs 2022） | — | 正向 |
| P/E trailing GAAP | 7.65x | — | — | 失真，不採用 |
| P/E TTM adjusted（計算） | 約 11.7x | — | 約 18–22x（估計） | 偏便宜 |
| P/E forward | 21.15x | — | 19–21x（估計） | 中性 |
| EV/EBITDA（TTM normalized，計算） | 約 10.0x（info 10.8x） | — | 14–16x（估計） | 偏便宜 |
| P/FCF TTM（計算） | 約 16.4x | — | 22–25x（估計） | 偏便宜 |
| P/S TTM | 1.73x | — | 2.0–2.5x（估計） | 偏便宜 |
| P/B | 3.55x | — | 3–4x（估計） | 中性 |
| 分析師平均目標價隱含漲幅 | +23.0%（目標 255.35） | — | — | 正向 |
| 內部人公開市場淨額（6 個月） | 約 -$4.23M（賣出） | — | — | 低強度，無買入 |
| 機構持股比例 | 84.5% | — | — | 中性 |
| Short % float | 2.48% | short 股數 +21.9%（MoM） | — | 低，但月增 |
| 財報 EPS beat 紀錄 | 24/24 季 | — | — | 健康 |
| 股價相對 200 日均線 | -9.9% | — | — | 偏弱 |
| 52 週股價漲幅 vs S&P 500 | +3.4% vs +15.7% | — | — | 落後大盤 |
| Quantinuum 獨立營收／估值 | DATA_UNAVAILABLE | — | — | 無法評估 |

## Red flags
- GAAP 盈餘失真：2026Q2 含約 5.9B 稅前處分利益，trailing P/E 7.65x、TTM ROE 44%、earnings growth 2.6x 均不可用於比較。
- 資料一致性問題：TTM 營收（36.1B 計算 vs info 38.1B）、TTM FCF（4.0B 計算 vs info 2.6B）、股利每股（9.40 vs 2.80）、EPS 三種口徑、季度序列 2025Q1 為 null 等，多項衝突，需以 10-Q 核實後才能定論。
- 槓桿偏高：淨負債 25.2B、D/E 183%、Total Debt / TTM normalized EBITDA 約 3.7x；利息保障 FY2025 僅 5.1x。
- 有形權益為負（-7.84B），商譽與無形資產佔總資產比重高。
- 2026Q1 大額債務淨償還（約 -12.6B）與同季 Net Other Financing Charges +15.7B 性質不明。
- 股東報酬動能減弱：2026Q2 買回為 0；2025 股利加買回超過 FCF 的 125%，缺口靠舉債。
- ROIC 由 2024 約 13.6% 降至 2025 約 11.3%；2025 年減損 994M、特殊項目 -1.48B。
- 成長偏弱：3 年營收 CAGR 1.8%，股價 52 週落後 S&P 500 約 12 個百分點，且低於 50 日與 200 日均線。
- 空頭持倉 7.86M 股，月增 21.9%，但佔流通股僅 2.48%，訊號強度有限。
- 資料來源為 cache（Yahoo cookie/crumb 取得失敗），最新季為 2026-06-30；data after 2026-10-15 僅有排定中的 2026-10-22 財報，未納入實際結果。

FUNDAMENTALS REPORT COMPLETE
