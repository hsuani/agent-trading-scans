# Fundamentals — ARM (Arm Holdings plc, ADR) as of 2026-10-26

> 資料來源：`pipeline/tools/yf.py ARM`（info / financials / quarterly_fin / balance_sheet / quarterly_bs / cashflow / quarterly_cf / earnings_dates / insider / major_holders / inst_holders），yfinance 無法直連時回退至 repo 快取。快取內的股價為 `fulldayPrice` 210.33 USD，未附時間戳記，視為 as-of 近似值。單位：USD，年度以 B（十億）標示，季度以 M（百萬）標示；本報告不使用 億。
> 日期註記：財報日 2026-11-04 為排程日期，晚於 as-of，屬未來事件，未發生。as-of 之後的資料一律視為未知。

## Executive summary
ARM 營收仍維持約 22% 的 YoY 成長（FY26 營收 4.92B USD，+22.8%），毛利率 97.5%、TTM 淨利率 20.2%，資產負債表為淨現金約 3.42B USD，體質健康。FY26 FCF 為 0.95B USD（FCF / NI 1.05x），但 SBC 達 1.05B USD，高於 FCF，且 capex 在 FY26 較前一年增加 141%。估值極度昂貴（trailing P/E 216.8x、forward P/E 68.6x、EV/EBITDA 208.0x、P/S 43.6x），且近六個月內部人僅有公開市場賣出約 58.5M USD、無買入，基本面對未來成長與利潤率兌現高度敏感。

## Revenue & profitability

**營收趨勢（annual，USD B）**

| 年度（FY，3 月結） | 營收 | YoY | 毛利 | 營業利益（EBIT） | 淨利 | 稀釋 EPS |
|---|---|---|---|---|---|---|
| FY23（2023-03-31） | 2.679 | n/a | 2.573 | 0.678 | 0.524 | 0.51 |
| FY24（2024-03-31） | 3.233 | +20.7% | 3.079 | 0.117 | 0.306 | 0.29 |
| FY25（2025-03-31） | 4.007 | +24.0% | 3.886 | 0.831 | 0.792 | 0.61 |
| FY26（2026-03-31） | 4.920 | +22.8% | 4.799 | 0.908 | 0.904 | 0.85 |

- 3 年 CAGR（FY23 → FY26）約 22.4%（以上表計算）。yfinance 的 FY22 欄位為 null，無法計算 4-5 年 CAGR，標示 DATA_UNAVAILABLE。
- 季度趨勢（M USD）：Q2'25 1,053 → Q3'25 1,135 → Q4'25 1,242 → Q1'26 1,490 → Q2'26 1,289。最新季 Q2'26 YoY +22.4%（對照 Q2'25 1,053），QoQ −13.5%（Q1'26 季節性高點回落）。
- TTM 營收 5.156B USD（與 info `totalRevenue` 5,155,999,744 一致，已驗證）。
- 分部營收：DATA_UNAVAILABLE。`longBusinessSummary` 只列產品線（CPU IP、GPU/NPU、systems IP、CSS、軟體工具），未提供各線金額或 royalty / license 拆分。

**獲利能力（margin 趨勢）**

| 指標 | FY23 | FY24 | FY25 | FY26 | TTM（yfinance / 季度加總） |
|---|---|---|---|---|---|
| 毛利率 | 96.0% | 95.2% | 97.0% | 97.5% | 97.5%（季度加總，已驗證） |
| 營業利益率（EBIT / 營收） | 25.3% | 3.6% | 20.7% | 18.5% | info 7.6% ／ 季度加總 17.3%（不一致，見紅旗） |
| 淨利率 | 19.6% | 9.5% | 19.8% | 18.4% | 20.2%（info `profitMargins` 0.2025，與季度加總 1,044M 一致） |
| EBITDA 利潤率 | n/a | n/a | n/a | n/a | 20.6%（info `ebitdaMargins`） |

- EPS 驗證：FY26 稀釋 EPS 0.85 × 股數約 1,068M ≈ 908M，接近 NI 904M，數值一致。
- TTM EPS 0.97 = 季度稀釋 EPS 加總（0.25 + 0.29 + 0.21 + 0.22），一致。
- ROE：info `returnOnEquity` 13.35%；以 TTM NI 1,044M ÷ 2026-06-30 權益 8,630M 計算約 12.1%（自算，為期末權益口徑）。
- ROIC（估計，自算）：FY26 NOPAT ≈ 908M × (1 − 21.9% 稅率) ≈ 709M；投入資本 ≈ 權益 8,286M + 債務 457M − 現金及短期投資 3,601M ≈ 5.14B，ROIC ≈ 13.8%。此為粗估。
- 利潤結構注意：Q2'26 EBIT 僅 98M，但淨利 270M（稅率 40%，非營業項目與稅務影響較大），淨利的營業品質需留意。

## Cashflow & balance sheet

**現金流（annual，USD B）**

| 年度 | 營業現金流 OCF | Capex | FCF | FCF 利潤率 | FCF / NI | SBC | FCF − SBC |
|---|---|---|---|---|---|---|---|
| FY23 | 0.739 | 0.093 | 0.646 | 24.1% | 1.23x | 0.079（異常，見紅旗） | n/a |
| FY24 | 1.090 | 0.143 | 0.947 | 29.3% | 3.09x | 1.037 | −0.090 |
| FY25 | 0.397 | 0.239 | 0.158 | 3.9% | 0.20x | 0.820 | −0.662 |
| FY26 | 1.524 | 0.575 | 0.949 | 19.3% | 1.05x | 1.052 | −0.103 |

- FCF / NI FY26 為 1.05x，高於 0.9 健康門檻；但 FY25 僅 0.20x，三年波動極大。
- Capex FY26 0.575B，較 FY25 0.239B 增加 141%，為 D&A 249M 的約 2.3 倍，屬於基礎建設或產品轉型投入上升。
- 季度 FCF（M USD）：Q3'25 427 → Q4'25 181 → Q1'26 170 → Q2'26 694。季度加總 TTM FCF 約 1,472M；info `freeCashflow` 為 1,334M，兩者差約 138M，見紅旗。

**資產負債表（2026-06-30 為最新季，M USD）**

| 項目 | 數值 | 說明 |
|---|---|---|
| 現金及短期投資 | 3,888 | info `totalCash` 3,888M 一致 |
| 總債務 | 464 | 與 FY26 `Capital Lease Obligations` 457M 幾乎相同，債務大多為租賃負債 |
| 淨現金（自算） | 約 3,424 | 3,888 − 464 |
| 股東權益 | 8,630 | FY26 為 8,286M，持續成長 |
| 總資產 | 11,196 | FY26 為 10,703M |
| 流動負債 | 1,207 | FY26 為 1,040M |
| 流動比率 | 5.25x | info `currentRatio` |
| 速動比率 | 5.06x | info `quickRatio` |
| 負債權益比（D/E） | 0.056x（yfinance 欄位 5.62 以百分比呈現） | 自算 464 ÷ 8,630 ≈ 5.4% |
| 商譽（FY26） | 1,623 | 佔 FY26 總資產約 15.2% |
| 有形帳面價值（FY26） | 6,433 | 有形權益高於 FY25 的 5,068M |
| 營運資金（FY26） | 5,196 | FY25 為 3,901M |

- 淨現金由 2025-06-30 約 2,510M（2,906 − 396）增至 2026-06-30 約 3,424M，YoY 約 +36%（自算）。
- 結論：流動性與財務槓桿都極為寬裕，債務風險低。

## Capital allocation & insider signal

**資本配置**
- 股息：無（info `dividendYield` 0.0；年度現金流量表無 dividends 支出）。
- 股票回購：DATA_UNAVAILABLE。本次抽取的年度現金流量表欄位中未見回購金額，不可確認為零或其他值。
- 股份稀釋：流通股數 FY23 1,025.2M → FY24 1,040.3M → FY25 1,056.5M → FY26 1,064.1M，FY26 YoY +0.7%，三年 CAGR 約 1.2%。目前 `sharesOutstanding` 1,068.0M，`impliedSharesOutstanding` 相同。
- 融資現金流：FY26 股票選擇權行權收入 +74M；「Net Other Financing Charges」為 −622M，項目內容 DATA_UNAVAILABLE（可能為員工股權代扣稅款，未經工具確認，不應推論）。
- 資本支出：FY26 Capex 575M（+141%），為當前主要資本配置方向。
- SBC：FY24 1,037M、FY25 820M、FY26 1,052M，約為營收的 20-32%，是 ARM 實質上最大的股東成本之一。

**內部人交易（近六個月：2026-04-26 至 2026-10-26）**

| 日期 | 內部人 | 職位 | 股數 | 金額（M USD） | 類型 |
|---|---|---|---|---|---|
| 2026-09-21 | Jason E. Child | CFO | 10,400 | 3.12 | 公開市場賣出 @300.00 |
| 2026-08-27 | Jason E. Child | CFO | 10,400 | 2.66 | 公開市場賣出 @255.33 |
| 2026-06-02 | Laura K. Bartels | Officer | 11,306 | 4.44 | 公開市場賣出 @392.70 |
| 2026-06-01 | William Abbey | Officer | 6,566 | 2.64 | 公開市場賣出 @383.73–415.52 |
| 2026-05-28 | William Abbey | Officer | 4,200 | 1.44 | 公開市場賣出 @343.81 |
| 2026-05-22 | William Abbey | Officer | 2,300 | 0.70 | 公開市場賣出 @305.82 |
| 2026-05-21 | William Abbey | Officer | 4,655 | 1.34 | 公開市場賣出 @287.03 |
| 2026-05-21 | Charlotte Eaton | Officer | 7,100 + 7,805 | 1.91 + 2.26 | 公開市場賣出 |
| 2026-05-20 | Jason E. Child | CFO | 31,920 | 7.23 | 公開市場賣出 @226.54 |
| 2026-05-20 | William Abbey | Officer | 15,956 | 3.74 | 公開市場賣出 @224.14–257.18 |
| 2026-05-19 | Spencer Collins | Officer | 40,941 | 8.80 | 公開市場賣出 @215.00 |
| 2026-05-18 | Richard Grisenthwaite | Officer | 24,339 | 5.09 | 公開市場賣出 @209.15 |
| 2026-05-15 | William Abbey | Officer | 10,154 | 2.15 | 公開市場賣出 @199.00–221.99 |
| 2026-05-11 | Spencer Collins | Officer | 51,961 | 11.00 | 公開市場賣出 @207.77–214.41 |

- 近六個月合計：公開市場賣出 15 筆，約 58.5M USD，涉及 6 位內部人（CFO、CEO 以外之 Officer 與 CFO）；公開市場買入 0 筆。
- 另有 2026-05-15 的 `Stock Award (Grant)` 與 2026-08-31 CEO Haas 的 64 股授予，屬薪酬授予，不計為買入。
- 2026-08-07 Director Sine 贈與 9,572 股（價格 0），不計入交易金額。
- 規模比較：58.5M ÷ 市值 224.6B ≈ 0.026%，絕對金額不大；但方向一致（全為賣出）。
- 價格比較：CFO 於 2026-09-21 以 300.00 USD 賣出，現價 210.33 USD 低於該成交價約 30%。
- 賣出多集中於 2026 年 5 月財報後窗口期（財報日 2026-05-06）。
- 解讀：內部人淨賣出屬偏謹慎訊號，但金額相對市值極小，不宜單獨作為方向判斷。

**機構持股（major_holders / inst_holders，持股日期 2026-06-30）**
- 機構持股比例：96.2%（以流通股計 96.3%）；機構數 1,304 家；內部人持股比例 0.07%。
- 流通股數（floatShares）142.6M 股，約佔流通股本 1,068.0M 的 13.4%。其餘約 86.6% 未在 yfinance 持股清單中列名。`longBusinessSummary` 明載 ARM 為 SoftBank Group Corp. 之子公司，推論此為母公司持股，但工具未直接列出 SoftBank 名稱，標示為推論。
- 前十大機構（股數 / 占已發行股本 / 季度變化）：

| 機構 | 股數（M） | 占已發行股本 | 季度變化 |
|---|---|---|---|
| Invesco Ltd. | 12.82 | 1.20% | +1.18% |
| DZ Bank AG | 6.50 | 0.61% | −0.31% |
| Capital World Investors | 4.33 | 0.41% | +1.0% |
| Arrowstreet Capital | 4.09 | 0.38% | +3.33% |
| FMR, LLC | 4.06 | 0.38% | +0.66% |
| Goldman Sachs Group | 2.92 | 0.27% | +0.79% |
| Van Eck Associates | 2.60 | 0.24% | +0.18% |
| Capital Research Global Investors | 2.40 | 0.22% | −0.43% |
| Morgan Stanley | 2.16 | 0.20% | −0.52% |
| Capital International Investors | 2.05 | 0.19% | +0.76% |

- 前十大合計約 43.9M 股，約 4.1% 已發行股本；多數為增持，但規模有限。
- 空方：sharesShort 16.19M 股，佔流通股 11.15%，short ratio 2.93 日（short interest 報告日約 2026-09-29，較前月 16.74M 微減）。

## Valuation

**估值倍數（以 fulldayPrice 210.33 USD，市值 224.6B USD，EV 221.2B USD 計算）**

| 倍數 | 數值 | 計算依據 |
|---|---|---|
| Trailing P/E | 216.8x | 價格 ÷ TTM EPS 0.97 |
| Forward P/E | 68.6x | 價格 ÷ forward EPS 3.07 |
| PEG | 1.73 | info `pegRatio` |
| EV/EBITDA（TTM） | 208.0x | EV 221.2B ÷ TTM EBITDA 1.064B（info `enterpriseToEbitda` 207.98） |
| EV/Revenue（TTM） | 42.9x | info `enterpriseToRevenue` |
| P/S（TTM） | 43.6x | info `priceToSalesTrailing12Months` |
| P/B | 26.0x | 價格 ÷ BVPS 8.08 |
| P/FCF（TTM） | 約 168x | 市值 224.6B ÷ info FCF 1.334B；若用季度加總 1.472B 則約 153x |

- 市值驗證：210.33 × 1,068.0M 股 ≈ 224.6B，與 info `marketCap` 224,632M 一致。
- 股價位置：現價 210.33 較 52 週高點 452.7 低約 53.5%，但高於 52 週低點 100.02；低於 50 日 MA 262.40 與 200 日 MA 226.07。beta 3.79，波動性極高。
- 分析師共識（yfinance，40 位，非本報告建議）：`recommendationKey` buy，目標均價 290.7 USD（較現價 +38%），高 500.0、低 125.0。
- 成長與估值的關係：forward EPS 3.07 對比 TTM EPS 0.97，市場預期 EPS 需數倍成長；PEG 1.73 顯示以預期成長計價仍不便宜。

## Key catalysts
- **下一次財報**：2026-11-04（yfinance `earnings_dates`，排程，尚未發生）；EPS 估計 0.48 USD。
- **上一次財報**：2026-07-29，稀釋 EPS 實際 0.45 USD，優於估計 0.40（+11.44%）。近 11 季中 10 季 EPS 優於估計，1 季（2025-07）為 −0.31% 的微幅不及。
- 近兩年 EPS surprise 歷史：2024-02 +16.35%、2024-05 +17.73%、2024-07 +15.43%、2024-11 +17.12%、2025-02 +14.0%、2025-05 +5.04%、2025-07 −0.31%、2025-11 +17.7%、2026-02 +5.09%、2026-05 +3.57%、2026-07 +11.44%。
- **管理層指引**：DATA_UNAVAILABLE（yfinance 未提供指引數字）。
- **分部與產品線轉換**：DATA_UNAVAILABLE（無分部金額）。定性上，業務重心包含 CSS、NPU、雲端資料中心與汽車，但不可量化。
- **Capex 週期**：FY26 Capex 0.575B（+141%），後續 FCF 能否隨收入成長擴大，是重要觀察點。
- **SBC 與股權稀釋**：SBC 規模持續約 1B USD，若無法隨營收成長稀釋，會壓縮 FCF 品質。
- **股東結構**：流通股僅 13.4%，母公司 SoftBank 相關持股變動（DATA_UNAVAILABLE 於本工具）可能影響流動性與股價。

## Metrics table

金額單位：USD（B = 十億，M = 百萬）。Sector median 為粗估值，非工具資料，僅供參考。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 FY26（USD B） | 4.92 | +22.8% | 約 10%（成長率） | 強 |
| 營收 TTM（USD B） | 5.16 | Q2'26 +22.4% | n/a | 強 |
| 毛利率 TTM | 97.5% | FY25 97.0%（+0.5pp） | 約 55% | 極強（IP 授權特性） |
| 營業利益率 FY26（EBIT 口徑） | 18.5% | FY25 20.7%（−2.2pp） | 約 20% | 中性 |
| 淨利率 TTM | 20.2% | FY25 19.8% | 約 15% | 偏強（含非營業項目） |
| ROE（info，TTM） | 13.4% | n/a | 約 15% | 中性 |
| ROIC（自算，粗估） | 約 13.8% | n/a | 約 12% | 中性 |
| FCF FY26（USD B） | 0.95 | FY25 0.16（+501%） | n/a | 改善，但波動大 |
| FCF 利潤率 FY26 | 19.3% | FY25 3.9% | 約 15% | 中性偏強 |
| FCF / NI FY26 | 1.05x | FY25 0.20x | >0.9 為健康 | 健康（單年） |
| SBC / 營收 FY26 | 21.4% | FY25 20.5% | 約 5-8% | 紅旗 |
| FCF − SBC FY26（USD B） | −0.10 | FY25 −0.66 | n/a | 紅旗 |
| Capex FY26（USD B） | 0.575 | +141% | n/a | 投入增加，需留意 |
| 淨現金 2026-06-30（USD B） | 3.42 | 約 +36%（自算） | n/a | 強 |
| 流動比率 | 5.25x | DATA_UNAVAILABLE（年度對比） | 約 2.0x | 強 |
| D/E（總債務 ÷ 權益） | 0.056x | n/a | 約 0.3x | 強 |
| 流通股數（FY26，B 股） | 1.064 | +0.7% | 約 1-2% 年增 | 可接受 |
| 股息 | 0 | n/a | 約 1% | 無 |
| 股票回購 | DATA_UNAVAILABLE | n/a | n/a | DATA_UNAVAILABLE |
| 內部人 6 個月淨買賣（M USD） | 賣出 58.5，買入 0 | n/a | n/a | 偏空（金額小） |
| Trailing P/E | 216.8x | n/a | 約 30x | 極貴 |
| Forward P/E | 68.6x | n/a | 約 30x | 極貴 |
| EV/EBITDA（TTM） | 208.0x | n/a | 約 25x | 極貴 |
| P/S（TTM） | 43.6x | n/a | 約 8x | 極貴 |
| P/FCF（TTM） | 約 168x | n/a | 約 30x | 極貴 |
| 股價距 52 週高點 | −53.5% | n/a | n/a | 大幅回檔 |
| 分析師目標均價 | 290.7 USD（+38%） | n/a | n/a | 共識偏多（非本報告建議） |

## Red flags
- **SBC 高於 FCF**：FY26 SBC 1.05B USD 高於 FCF 0.95B USD，FCF − SBC 為 −0.10B USD；每年約 20% 營收以股權支付，獲利品質需打折。
- **估值極度昂貴**：forward P/E 68.6x、EV/EBITDA 208x、P/S 43.6x，任何成長不及預期都可能造成大幅重估；beta 3.79。
- **內部人持續賣出**：近六個月 15 筆、約 58.5M USD 公開市場賣出，0 筆買入；CFO 於 2026-09-21 以 300 USD 賣出，之後股價低於該價約 30%。
- **資料不一致（需人工核對）**：
  - 營業利益率：info `operatingMargins` 7.6%，但季度 EBIT 加總約 892M / 營收 5,156M ≈ 17.3%。
  - TTM FCF：info `freeCashflow` 1.334B，季度 FCF 加總 1.472B。
  - TTM EBITDA：info 1.064B，季度 EBITDA 加總約 1.156B。
  - 以上不一致會影響 EV/EBITDA、P/FCF 等倍數，使用前應以原始申報數字核對。
- **淨利與營業利益落差**：Q2'26 EBIT 僅 98M，淨利 270M，非營業收益與稅率（40%）對獲利影響大，營業品質需追蹤。
- **資本支出倍增**：FY26 Capex +141%，為 D&A 的 2.3 倍，FCF 轉換能力尚未穩定（FY25 FCF/NI 僅 0.20x）。
- **季度營收環比回落**：Q2'26 營收 1,289M，較 Q1'26 1,490M 回落 13.5%，需確認是否為季節性。
- **FY23 SBC 數值異常**：79M，與 FY24 1,037M 差距過大，不宜用於 SBC 趨勢比較。
- **融資現金流項目不透明**：FY26 Net Other Financing Charges −622M，內容 DATA_UNAVAILABLE。
- **流通性結構**：流通股僅 142.6M（約 13.4%），空方持股 11.15% of float，short ratio 2.93 日。
- **資料時效**：股價為快取快照，無時間戳記；財報日 2026-11-04 為 as-of 之後的排程事件。compensation 相關欄位指向 2027 年初之未來日期，僅為欄位標記，未用於分析。
- **缺漏**：分部營收、管理層指引、股票回購、SoftBank 等母公司持股明細均為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
