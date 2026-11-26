# Fundamentals — ZS (Zscaler, Inc.) as of 2026-11-27

## Executive summary
Zscaler 維持高成長（FY26 營收 3,352.5M USD，YoY +25.4%），毛利率穩定在 76–77%，FY26 自由現金流 779.1M USD（FCF margin 23.2%），但 GAAP 仍小幅虧損（FY26 淨利 -63.2M USD），且股權激勵（SBC）821.9M USD 已超過 FCF，FCF 扣除 SBC 後為 -42.8M USD。資產負債表仍有淨現金約 1.6B USD（現金加短期投資 3,474.2M 減總債務 1,855.8M），但 FY26 併購支出 918.1M 使股本與商譽明顯膨脹。估值方面，以 cache 價格 230.86 USD 計算，forward P/E 約 41.0x、TTM P/S 10.8x、TTM P/FCF 約 35.1x，屬高估值區間，分析師目標均價 256.8 USD（隱含 +11.3%）。

## 資料說明與 as-of 檢查
- 價格與 info 來源為 pipeline/tools/yf 快取（source: cache，cached_at 2026-11-26 16:51 UTC），股價 230.86 USD 為快取收盤附近價，非 2026-11-27 即時報價。
- 財務報表最新欄位為 FY26（2026-07-31）年度與 2026-07-31 季度；info 的 mostRecentQuarter 為 2026-10-31。Q1 FY27（2026-10-31 季）已於 2026-11-23 公布（earnings_dates 有 EPS 實際值 1.23），但 statement 快取中沒有該季損益表與資產負債表欄位，該季營收與獲利明細標示為 DATA_UNAVAILABLE。
- 第一次批次抓取 info 時曾回傳 SentinelOne（代號 S）的公司資料，重抓後 symbol 與公司名稱皆為 ZS / Zscaler, Inc.，本報告以重抓後的 ZS 資料為準，下游請留意快取一致性。
- 單位：USD 報表以 M（百萬美元）標示，市值與 EV 以 B（十億美元）標示，不使用億。
- 無未來資料（post-date）問題：所有資料時間點不晚於 2026-11-26 快取，Q1 FY27 公布日 2026-11-23 早於 as-of 日期。

## Revenue & profitability

**營收趨勢（USD M）**
- FY23 1,617.0 → FY24 2,167.8（+34.1%）→ FY25 2,673.1（+23.3%）→ FY26 3,352.5（+25.4%）
- FY23–FY26 3 年 CAGR 約 27.5%；增速在 FY25 放緩後 FY26 回升。
- 季度：Q1 FY26 788.1 / Q2 815.8 / Q3 850.5 / Q4 898.2（Q4 YoY +24.9%，對 Q4 FY25 719.2）。Q1–Q3 FY25 對照欄位未在快取中，YoY 無法完整計算。
- 業務組合：info 的 longBusinessSummary 列出 Zero Trust SASE、ZIA、ZPA、Zero Trust Browser、Digital Experience、Security for AI、data security（DSPM、DLP）等產品線，但未提供分部營收，segment mix 為 DATA_UNAVAILABLE。

**獲利能力**
- 毛利率（GAAP）：FY23 77.6% → FY24 78.0% → FY25 76.9% → FY26 76.8%；Q4 FY26 為 76.7%。毛利率持平略降，快取未提供成本拆分，驅動因素無法由資料判定。
- 營業利益（GAAP，yfinance Operating Income 行）：FY23 -234.6M、FY24 -121.5M、FY25 -127.1M、FY26 -121.1M；營業利益率 FY26 -3.6%（FY25 -4.8%、FY24 -5.6%、FY23 -14.5%），改善趨勢明確。
- 季度營業利益：Q1 FY26 -36.4M、Q2 -51.8M、Q3 -29.6M、Q4 -3.4M（Q4 營業利益率約 -0.4%），已接近損益平衡。
- 淨利：FY26 -63.2M（淨利率 -1.9%），FY25 -41.5M（-1.6%），FY24 -57.7M（-2.7%）。Q4 FY26 淨利 -3.4M。
- 稀釋後 EPS（GAAP）：FY26 -0.39、FY25 -0.27、FY24 -0.39、FY23 -1.40。
- 非 GAAP forward EPS（info forwardEps）5.63，與 GAAP 差距大，應以 GAAP 與 forward 分開看待。
- EBITDA：yfinance 正規化 EBITDA FY26 為 190.6M（5.7%），Q4 FY26 為 64.7M（7.2%）；info 的 TTM ebitda 為 63.7M。
- ROE（info TTM）-3.3%；ROA -0.9%。ROIC 以營業利益 / 平均投入資本估算約 -3.1%（FY26 營業利益 -121.1M，平均投入資本 (4,294.6 + 3,500.0) / 2 = 3,897.3M，屬估算值）。

## Cashflow & balance sheet

**現金流（USD M）**
- 營業現金流：FY23 462.3 → FY24 779.8 → FY25 972.5 → FY26 1,129.7（FY26 YoY +16.2%）。
- 資本支出（yfinance Capital Expenditure，含 PPE 與資本化軟體）：FY23 128.7 → FY24 194.9 → FY25 245.8 → FY26 350.5，佔營收 8.0% → 10.5%，上升趨勢。
- 自由現金流（FCF = OCF − Capex）：FY23 333.6 → FY24 585.0 → FY25 726.7 → FY26 779.1（FY26 YoY +7.2%）。
- FCF margin：FY23 20.6% → FY24 27.0% → FY25 27.2% → FY26 23.2%，FY26 因資本支出增加而下滑。TTM（info）FCF 1,080.9M、FCF margin 30.8%，與年度值不同步，TTM 包含 Q1 FY27 的現金流，但該季明細不在快取中。
- FCF / 淨利比：淨利為負，比率無意義（n/m）。FCF / SBC 只有 FY26 0.95x（779.1 / 821.9）；FCF 扣除 SBC 後 FY26 為 -42.8M，FY25 為 +65.3M。
- SBC（股權激勵）：FY26 821.9M，佔營收 24.5%，FY25 為 24.7%，佔比持平但絕對金額持續增加。
- 季度 FCF 極不均：Q1 FY26 413.3M（52.4%，對 788.1M）、Q2 169.1M、Q3 136.0M、Q4 60.8M（6.8%）。Q4 資本支出單季 218.5M，明顯高於 Q1–Q3（35.0 / 34.9 / 62.1），但 yfinance 另一欄位「Capital Expenditure Reported」單季僅 18.7M，兩者口徑不一致，見紅旗。

**資產負債表（2026-07-31，USD M）**
- 現金及約當現金 928.4；現金加短期投資 3,474.2（短期投資 2,545.8）。FY25 為 2,389.0 / 3,572.4。
- 總資產 7,866.7（FY25 6,419.9）；總負債 5,268.5；股東權益 2,598.3（FY25 1,799.3）。
- 總債務 1,855.8（長期債務 1,696.4、長期租賃 94.6、流動債務與租賃 64.9）。FY25 總債務 1,796.6。
- 淨現金（現金加短期投資 − 總債務）約 1,618.4；yfinance 的 Net Debt 欄位為 768.0，無法由資產負債表重現，本報告以自算淨現金為主，yfinance 值標示為不一致。
- 流動比率：FYE26 1.70（5,031.2 / 2,961.3）；info 的 currentRatio 為 1.80（口徑與期間未標明），FY25 為 2.01。
- 負債/權益（D/E）0.71（FY25 為 1.00），主要因股權增加（併購與 SBC 增加權益）。
- 商譽加無形資產 1,432.5（佔股東權益 55%），FY25 為 465.1；有形帳面價值 1,165.8（FY25 1,334.2）。
- 營運資金 2,069.9（FY25 2,464.7）。
- info 的 totalCash 655.2M 與 totalDebt 0 與資產負債表不符，以資產負債表為準，info 欄位標示為不一致。

## Capital allocation & insider signal

**資本配置**
- 併購：FY26 購買業務支出 918.1M（FY25 0.8M、FY24 374.7M、FY23 15.6M）；Q1 FY26 672.8M、Q3 97.3M、Q4 148.0M。商譽由 417.7M 增至 1,218.1M。併購標的與交易細節 DATA_UNAVAILABLE。
- 回購：現金流量表無 repurchase 行，FY23–FY26 皆無回購。
- 股利：無（dividendYield 0.0）。
- 股本稀釋：流通股數（BS Ordinary Shares）FY23 147.2M → FY24 152.5M → FY25 158.3M → FY26 163.1M，年複合增速約 3.5%；FY26 稀釋後加權股數 160.2M。
- 股權激勵行使現金流入：FY26 63.4M。

**內部人交易（最近 6 個月，2026-05-27 至 2026-11-27）**
- 共 29 筆記錄：公開市場賣出 24 筆，合計 80,180 股、15.05M USD；選擇權行使轉換 2 筆（約 5.35M USD）；股票授予 3 筆（非交易）。
- 買入：0 筆。
- 主要賣出者：GELLER ADAM（officer）約 8.57M USD；RUBIN KEVIN E（CFO）約 2.25M USD，為定期每月小額賣出（約 500 股，2026-07-27、08-25、09-25、10-26、11-25）；SCHLOSSMAN ROBERT S 約 1.94M USD；RICH MICHAEL J 約 1.32M USD；CHAUDHRY JAGTAR SINGH 約 0.91M USD。
- 規模：賣出總額 15.05M USD 佔市值 37.9B 的 0.04%，訊號強度低。內部人整體持股 34.5%（major_holders insidersPercentHeld），高持股且無買入，屬中性偏謹慎的信號。
- 機構：機構持股 54.7%（institutionsCount 1,273）；最大持有人 BlackRock 5.36%（持股 8.80M，較前季 -11.0%），AQR 持股 5.04M 股、較前季增加約 270%。

## Valuation

**估值指標（價格 230.86 USD，市值 37.89B USD，EV 35.62B USD）**
- Trailing P/E：n/m（info 的 trailingEps -0.39 與 FY26 GAAP EPS 一致，為負值，P/E 無意義）。
- Forward P/E：40.99x（forwardEps 5.63）。
- EV/Revenue（TTM，3,513.7M）10.1x；P/S（TTM）10.8x。
- EV/EBITDA：info TTM EBITDA 63.7M 對應 558.8x（n/m）；以 FY26 正規化 EBITDA 190.6M 估算約 186.8x。EBITDA 尚未充分反映經營槓桿，此指標不具參考價值。
- P/FCF：TTM 35.1x（FCF 1,080.9M）；FY26 FCF 基礎為 48.6x。
- P/B：14.5x（bookValue 15.94）。
- 價格位置：52 週區間 114.62–267.87 USD，目前位於高點下 13.8%；高於 50 日均線 7.5%（214.71）與 200 日均線 37.7%（167.63）。Beta 0.84。
- 分析師：40 家，recommendationMean 2.03（buy）；目標價均值 256.83、高 340.00、低 170.00 USD（ZS info 未提供中位數目標價）；均值隱含 +11.3%。
- 空頭部位：sharesShort 5.19M，佔流通 4.8%（shortPercentOfFloat 0.0482），屬低水位。

**與同業估計中位數比較（以下為估計值，非工具資料）**
- 資安軟體（software-infrastructure，大型成長股）forward P/E 約 35–45x；ZS 41.0x 位於區間內偏上段。
- EV/Revenue 約 8–10x；ZS 10.1x 偏高。
- P/FCF 約 30–40x；ZS 35.1x 接近區間中段。

## Key catalysts
- 已公布：Q1 FY27 於 2026-11-23 公布，EPS 實際 1.23 vs 估計 1.16，超出 5.94%。營收、毛利、指引與分部數據 DATA_UNAVAILABLE（快取無該季明細）。
- 下次財報：2027-02-25（EPS 估計 1.20）。
- 歷史 EPS 驗證：近 8 季 EPS 皆超出估計，超出幅度介於 +5.9% 至 +12.7%（2026-09-03 +9.18%、2026-05-26 +7.11%、2026-02-26 +12.56%、2025-11-25 +11.42%）。
- 併購整合：FY26 併購支出 918.1M，短期內需觀察商譽減損與整合費用（標的 DATA_UNAVAILABLE）。
- 產品方向：Security for AI、AI 資料安全（DSPM / DLP）、Zero Trust Branch 與 Zero Trust Cloud 為 longBusinessSummary 列出之增長方向，但無量化數據。
- 內部人與分析師：CFO 定期賣出為例行操作；分析師目標價區間 170–340 USD。

## Metrics table

以下欄位單位：營收、FCF、資產負債表以 USD M 標示；市值與 EV 以 USD B 標示。YoY 指 FY26 相對 FY25（若另註明除外）。Sector median 為估計值。

| Metric | Latest（FY26 / TTM / 價格 230.86）| YoY | Sector median（估計）| Verdict |
|---|---|---|---|---|
| 營收（USD M） | 3,352.5 | +25.4% | 約 +15%（估計）| 高成長 |
| 毛利率（GAAP） | 76.8% | -0.1pp | 約 75%（估計）| 優於中位數 |
| 營業利益率（GAAP） | -3.6% | +1.2pp（FY25 -4.8%）| 約 0%（估計）| 仍略虧，改善中 |
| 淨利率（GAAP） | -1.9% | -0.3pp（FY25 -1.6%）| 約 0%（估計）| 接近損益平衡 |
| 稀釋後 EPS（GAAP） | -0.39 | 惡化（FY25 -0.27）| n/a | 尚未獲利 |
| Forward EPS（info） | 5.63 | n/a | n/a | 估值基礎 |
| Q4 FY26 營收（USD M） | 898.2 | +24.9% | n/a | 穩定 |
| ROE（TTM，info） | -3.3% | n/a | 約 10%（估計）| 弱 |
| ROIC（營業利益 / 平均投入資本，估算） | -3.1% | n/a | 約 8–10%（估計）| 弱 |
| 營業現金流（USD M） | 1,129.7 | +16.2% | n/a | 強 |
| 自由現金流（USD M） | 779.1 | +7.2% | n/a | 正向 |
| FCF margin | 23.2% | -4.0pp（FY25 27.2%）| 約 20%（估計）| 中等 |
| FCF / 淨利 | n/m（淨利為負）| n/a | n/a | 無法評估 |
| FCF − SBC（USD M） | -42.8 | 由 +65.3 轉負 | n/a | 紅旗 |
| SBC / 營收 | 24.5% | -0.2pp | 約 15–20%（估計）| 偏高 |
| 資本支出 / 營收 | 10.5% | +1.3pp | 約 3–5%（估計）| 偏高，上升中 |
| 現金加短期投資（USD M） | 3,474.2 | -2.7%（FY25 3,572.4）| n/a | 充裕 |
| 總債務（USD M） | 1,855.8 | +3.3%（FY25 1,796.6）| n/a | 中等 |
| 淨現金（自算，USD M） | 1,618.4 | n/a | n/a | 正向 |
| 流動比率 | 1.70 | 由 2.01 下降 | 約 1.5–2.0（估計）| 健康 |
| D/E | 0.71 | 由 1.00 下降 | 約 0.3–0.6（估計）| 槓桿中等 |
| 併購支出（USD M） | 918.1 | 大幅增加（FY25 0.8）| n/a | 需觀察整合 |
| 流通股數（M） | 163.1 | +3.0%（FY25 158.3）| n/a | 稀釋中 |
| 回購 / 股利 | 無 / 無 | n/a | n/a | 無資本返還 |
| 內部人近 6 月淨交易（USD M） | 賣出 15.05、買入 0 | n/a | n/a | 中性偏謹慎，規模 0.04% 市值 |
| 內部人持股 | 34.5% | n/a | n/a | 高 |
| Forward P/E | 41.0x | n/a | 約 35–45x（估計）| 偏高 |
| Trailing P/E | n/m | n/a | n/a | 無意義 |
| EV/Revenue（TTM） | 10.1x | n/a | 約 8–10x（估計）| 偏高 |
| EV/EBITDA（FY26 正規化，估算） | 約 186.8x | n/a | n/a | n/m |
| P/FCF（TTM） | 35.1x | n/a | 約 30–40x（估計）| 中段偏高 |
| P/S（TTM） | 10.8x | n/a | 約 8–10x（估計）| 偏高 |
| P/B | 14.5x | n/a | n/a | 偏高 |
| 分析師目標價均值（USD） | 256.8（隱含 +11.3%）| n/a | n/a | 正向共識 |
| 短期空單 / 流通股 | 4.8% | n/a | n/a | 低 |
| 市值（USD B） | 37.89 | n/a | n/a | 大型 |
| 企業價值 EV（USD B） | 35.62 | n/a | n/a | n/a |

## Red flags
- SBC 821.9M 超過 FY26 FCF 779.1M，FCF 扣除 SBC 轉負（-42.8M）；股本年增約 3.0–3.5%，股東實質稀釋明顯。
- Q4 FY26 FCF 僅 60.8M（6.8%），單季資本支出 218.5M 遠高於前三季；yfinance 內 Capital Expenditure（218.5）與 Capital Expenditure Reported（18.7）口徑不一致，需向原始 10-K/10-Q 核對。
- 資產負債表與 info 欄位不一致：info totalDebt 0 與 totalCash 655.2M vs 資產負債表 總債務 1,855.8M、現金加短期投資 3,474.2M；yfinance netDebt 768.0M 無法重現。本報告以資產負債表為準。
- 商譽與無形資產大增（商譽 417.7M → 1,218.1M），FY26 併購 918.1M，整合與減損風險上升；有形帳面價值縮減至 1,165.8M。
- 仍為 GAAP 淨虧損，FY26 淨利 -63.2M，EPS 由 FY25 -0.27 惡化至 -0.39。
- 估值偏高：forward P/E 41.0x、P/S 10.8x、EV/Revenue 10.1x，相對成長率（營收 YoY 25.4%）的成長溢價有限，對業績不及預期的敏感度高。
- 內部人 GELLER ADAM 六個月內賣出約 8.57M USD，為最大賣家；無任何內部人買入。
- 資料缺口：Q1 FY27 營收與獲利明細、指引、分部營收、併購標的細節均為 DATA_UNAVAILABLE；快取曾於單次抓取時回傳 SentinelOne（S）資料，需留意快取正確性。

FUNDAMENTALS REPORT COMPLETE
