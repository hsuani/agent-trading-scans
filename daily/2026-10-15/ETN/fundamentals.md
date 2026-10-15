# Fundamentals — ETN as of 2026-10-15

## Executive summary
Eaton (ETN) 的營運面仍然穩健：FY2025 營收 27.45B USD (YoY +10.3%)，營業利益率 18.98%，FCF 3.55B USD，股利 1.63B USD 由 FCF 覆蓋 2.19 倍。然而 Q1 2026 出現明顯的資產負債表轉折，總資產由 41.25B 跳升至 55.09B，長期負債由 8.76B 升至 18.54B，淨負債由 9.27B 增至 20.56B（約 3.3x TTM EBITDA，2025 年底約 1.5x），有形淨值轉為約 -12.9B，符合一筆約 11B USD 投資現金流出的財務痕跡（工具未標示交易標的，此為由報表推論）。估值方面，trailing P/E 43.6x、P/FCF 約 44.7x、P/B 7.84x 偏高，即使以 forward P/E 25.1x 計算，前提是 forward EPS 16.28 的口徑仍待核實（見 Red flags）。

## Revenue & profitability
- **營收趨勢**：FY2022 20.75B → FY2023 23.20B → FY2024 24.88B → FY2025 27.45B。YoY 分別為 +11.8%（2023）、+7.2%（2024）、+10.3%（2025）。2022–2025 三年 CAGR 為 9.8%（FY2021 資料為 null，無法計算四年 CAGR）。
- **季度營收**：Q1'25 6.38B、Q2'25 7.03B、Q3'25 6.99B、Q4'25 7.06B、Q1'26 7.45B（YoY +16.8%）。Q2'26 的營收欄位為 null，因此 DATA_UNAVAILABLE。
- **分部結構**：工具未提供分部營收數字。依 `longBusinessSummary`，業務分為 Electrical Americas、Electrical Global、Aerospace、Vehicle、eMobility 五個分部，但缺乏各分部金額，無法量化結構轉移。
- **毛利率**：2022 33.2% → 2023 36.4% → 2024 38.2% → 2025 37.6%；Q1'26 為 35.6%（Q1'25 為 38.4%），顯示 2026 年初毛利率承壓。
- **營業利益率**：2022 14.4% → 2023 16.8% → 2024 18.6% → 2025 19.0%；Q1'26 降至 15.7%（Q1'25 為 18.8%）。Q1'26 營業費用 1.48B，較 Q4'25 的 1.21B 明顯增加，與收購整合相容，但工具未說明原因。
- **淨利率**：2025 14.9%（2024 為 15.3%）；Q1'26 為 11.6%（Q1'25 為 15.1%）。FY2025 淨利 4.09B，YoY +7.7%；Q1'26 淨利 866M，YoY -10.2%。
- **EBITDA**：FY2025 6.18B（YoY +10.0%），EBITDA margin 22.5%。
- **EPS**：GAAP diluted EPS FY2025 10.45（FY2024 9.50，+10.0%）。yfinance 的 earnings_dates 以 adjusted 口徑列示：FY2025 合計 12.07（FY2024 合計 10.80，+11.8%，由 4 季加總推算）。Q2'26 adjusted EPS 3.15，高於 consensus 3.08（+2.4%）；Q1'26 adjusted EPS 2.81，高於 consensus 2.73（+2.9%）。
- **ROE**：FY2025 以期末股東權益計算為 21.0%（以平均權益計算為 21.6%）。
- **ROIC**：以 EBIT 5.17B × (1 - 稅率 17.1%) ÷ 期末 invested capital 29.32B 估算，FY2025 約 14.6%（FY2024 約 14.1%）。Q1'26 invested capital 升至 40.85B，ROIC 會因分母擴大而被稀釋；Q1'26 尚無完整 TTM 稅前數字可算。

## Cashflow & balance sheet
- **OCF / FCF**：OCF 2022 2.53B → 2023 3.62B → 2024 4.33B → 2025 4.47B。FCF 2022 1.94B → 2023 2.87B → 2024 3.52B → 2025 3.55B。FCF margin 2025 為 12.9%（2024 為 14.2%）。
- **FCF / NI**：2022 0.79、2023 0.89、2024 0.93、2025 0.87。FY2025 低於 0.9 健康門檻。Q1'26 FCF 314M（Q1'25 為 91M），季度表現改善。
- **資本支出**：capex 2025 919M（2024 808M），佔營收 3.35%（2024 為 3.25%），呈上升趨勢但仍在低水準。
- **淨負債**：2025 年底 net debt 9.27B（total debt 10.53B，現金 622M）；2026 年 3 月底 net debt 20.56B（total debt 21.83B，現金 565M）。以 TTM EBITDA（由四季加總，6.22B）計算，net debt / EBITDA 由 2025 年底約 1.5x 升至 Q1'26 約 3.3x；total debt / EBITDA 約 3.5x。
- **流動性**：2025 年底 current ratio 1.32（流動資產 12.36B / 流動負債 9.37B）；Quick ratio 以 (流動資產 - 存貨) ÷ 流動負債 估算為 0.81（yfinance 的 quickRatio 欄位為 0，視為不可用）。Q1'26 流動負債升至 11.74B，working capital 由 2.99B 降至 2.26B。
- **D/E**：2025 年底 total debt / equity 為 0.54；Q1'26 升至 1.11。
- **利息覆蓋**：Q1'26 EBIT 1.21B / 利息費用 106M，約 11.4x，仍屬充裕。利息費用由 Q1'25 的 33M 增至 Q1'26 的 106M。
- **商譽與有形淨值**：Goodwill 由 2025 年底 15.77B 升至 2026 年 3 月底 21.40B，佔總資產 38.9%；有形淨值 (TBV) 由 -1.40B 惡化至 -12.94B。
- **現金流事件**：Q1'26 investing cash flow -11.38B，同季 debt issuance 9.87B、financing cash flow +10.80B；Q2'25 另有 purchase of business 1.45B。工具未提供交易對象與條款。

## Capital allocation & insider signal
- **資本支出**：2025 capex 919M，佔 OCF 約 21%，屬輕資本結構；成長主要靠收購而非自建產能（由 Q1'26 現金流推論，工具未直接揭露收購細節）。
- **股利**：2025 股利支付 1.63B（2024 為 1.50B，+8.4%）。最近季度 DPS（lastDividendValue）1.10 USD，trailing annual dividend rate 4.28 USD，dividend yield 1.03%（5 年平均 1.39%）。payoutRatio 0.4354。FCF 覆蓋 2.19 倍。
- **買回**：2025 buyback 1.86B（2024 為 2.49B、2023 為 0）；Q1'26 buyback 為 0。2025 股利 + 買回合計 3.49B，約佔 FCF 的 98%，沒有留出 FCF 作為收購的內部資金，因此 Q1'26 收購改以債務支應。
- **股本**：發行股數 2022 年 397.8M → 2025 年底 387.9M（-2.5%）；2026 年 3 月底 388.3M（較年底小幅回升 +0.1%）。
- **內部人交易（2026-04-15 至 2026-10-15，6 個月）**：
  - 公開市場買進：2 筆，共 1,161 股，約 482K USD（Gerald Johnson，董事）。
  - 公開市場賣出：6 筆，共 39,589 股，約 17.11M USD。其中 Heath Monesmith（President & COO, Electrical Sector）兩筆合計 36,403 股、約 15.78M USD，佔賣出金額大宗。
  - 選擇權轉換後賣出（Monesmith 20,041 股、Yelton 658 股）已由其賣出項目涵蓋，未重複計算。
  - 期間內另有董事 / 高階主管的 stock grant 無現金價格（Value null），未納入買賣計算。
  - 淨賣出約 16.6M USD，佔市值 158.76B 的 0.011%；insider 持股比例僅 0.072%，屬小額、以單一主管為主的減持，對整體訊號強度有限。
- **機構持股**：機構持股 87.8%（3,460 家）；前十大包括 BlackRock 7.9%、Vanguard Capital Management 6.5%、State Street 4.5%、JPMorgan 4.3%（季度減持 13.0%）。
- **做空比例**：short interest 7.99M 股，佔流通股 2.06%，short ratio 3.83 天；前期 7.21M 股，月增 10.8%。

## Valuation
- **價格參考**：info.currentPrice 408.85（cache 時點 2026-10-15T11:16:58 UTC）。同一快取的 fulldayPrice 為 399.81，previousClose 428.31，屬盤中快照差異，本報告以 currentPrice 為準。
- **P/E**：trailing P/E 43.6x（trailingEps 9.38）；forward P/E 25.1x（forwardEps 16.28）。PEG 2.6。
- **EV/EBITDA**：info.enterpriseToEbitda 27.0x（EV 179.47B，info ebitda 6.64B）；若以季度 EBITDA 加總之 TTM 6.22B 計算，約 28.8x。
- **P/FCF**：約 44.7x（市值 158.76B / FY2025 FCF 3.55B）。
- **P/S**：info 為 5.29x（TTM）；以 FY2025 營收計為 5.78x。
- **P/B**：7.84x（bookValue 52.15）。
- **分析師共識**：26 位分析師，recommendationMean 1.57（buy），target mean 484.9、median 496.5、high 534、low 333。以 mean target 計，較現價 +18.6%。
- **技術位置**：現價低於 50 日均線 425.75 約 4.0%，高於 200 日均線 393.41 約 3.9%；52 週區間 311.92–478.00，目前位於區間約 58% 處。beta 1.13。
- **同業中位數**：DATA_UNAVAILABLE（工具未提供產業同業估值資料，無法填入 sector median）。

## Key catalysts
- **下次財報**：2026-11-03（yfinance 日期，EPS consensus 3.54；實際日期以公司公告為準）。
- **前次財報（2026-07-31，Q2'26）**：adjusted EPS 3.15，高於 consensus 3.08，YoY +6.8%（Q2'25 為 2.95）。
- **Q1'26 財報（2026-05-05）**：adjusted EPS 2.81，高於 consensus 2.73，YoY +3.3%；但 GAAP 淨利 YoY -10.2%，毛利率與營業利益率同步下滑。
- **債務與收購整合**：Q1'26 長期負債增加約 9.8B，後續需觀察利息費用、再融資與去槓桿節奏。
- **Guidance**：工具未提供公司 guidance 數字，DATA_UNAVAILABLE。
- **分部轉移**：工具未提供分部收入資料，DATA_UNAVAILABLE。
- **內部人**：最近一筆 2026-10-02 Adam Wadecki 997 股，無金額，性質待確認（可能為 stock grant）。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 Revenue (FY2025) | 27.45B USD | +10.3% | DATA_UNAVAILABLE | 成長穩定，三年 CAGR 9.8% |
| 營收 Q1'26 | 7.45B USD | +16.8% | DATA_UNAVAILABLE | 成長加速 |
| 毛利率 Gross margin (FY2025) | 37.6% | -0.6pt (vs 38.2%) | DATA_UNAVAILABLE | 高位持平，Q1'26 降至 35.6% 需留意 |
| 營業利益率 Operating margin (FY2025) | 19.0% | +0.4pt | DATA_UNAVAILABLE | 持續改善，Q1'26 回落至 15.7% |
| 淨利率 Net margin (FY2025) | 14.9% | -0.4pt | DATA_UNAVAILABLE | 良好，Q1'26 為 11.6% |
| ROE (FY2025, 期末權益) | 21.0% | 與 2024 約 20.5% 相近 | DATA_UNAVAILABLE | 優良 |
| ROIC (FY2025 估算) | 14.6% | +0.5pt | DATA_UNAVAILABLE | 尚可，收購後會稀釋 |
| FCF margin (FY2025) | 12.9% | -1.2pt | DATA_UNAVAILABLE | 良好但略降 |
| FCF / NI (FY2025) | 0.87 | -0.06 | DATA_UNAVAILABLE | 略低於 0.9 門檻 |
| Net debt / EBITDA (Q1'26, TTM) | 3.3x | 2025 年底約 1.5x | DATA_UNAVAILABLE | 明顯升高，需追蹤 |
| Total debt / equity (Q1'26) | 1.11 | 2025 年底 0.54 | DATA_UNAVAILABLE | 槓桿顯著上升 |
| Current ratio (FY2025) | 1.32 | 2024 約 1.50 | DATA_UNAVAILABLE | 流動性足夠 |
| Tangible book value (Q1'26) | -12.94B USD | 2025 年底 -1.40B | DATA_UNAVAILABLE | 有形淨值轉負，商譽佔總資產 38.9% |
| 股利覆蓋 Dividend coverage (FCF/股利, FY2025) | 2.19x | 2024 約 2.35x | DATA_UNAVAILABLE | 充足 |
| 股利支付 Dividends paid (FY2025) | 1.63B USD | +8.4% | DATA_UNAVAILABLE | 穩定增加 |
| 買回 Buybacks (FY2025) | 1.86B USD | -25.3% | DATA_UNAVAILABLE | 2026 Q1 暫停 |
| 內部人淨買賣 (6 個月) | 淨賣出約 16.6M USD | n/a | DATA_UNAVAILABLE | 小幅、單一主管為主，訊號偏弱 |
| trailing P/E | 43.6x | n/a | DATA_UNAVAILABLE | 偏高 |
| forward P/E | 25.1x | n/a | DATA_UNAVAILABLE | 偏高，forward EPS 待核實 |
| EV/EBITDA | 27.0x (info) / 約 28.8x (TTM 計算) | n/a | DATA_UNAVAILABLE | 偏高 |
| P/FCF | 約 44.7x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/S (TTM) | 5.29x | n/a | DATA_UNAVAILABLE | 偏高 |
| P/B | 7.84x | n/a | DATA_UNAVAILABLE | 偏高（有形淨值為負，此倍數參考性低） |
| 分析師目標價 mean | 484.9 USD（+18.6%） | n/a | DATA_UNAVAILABLE | 共識偏多（mean 1.57） |

## Red flags
- **槓桿快速上升**：Q1'26 net debt 由 9.27B 增至 20.56B，net debt / TTM EBITDA 由約 1.5x 升至約 3.3x，total debt / equity 升至 1.11，有形淨值轉為約 -12.9B。
- **收購融資與股東回饋衝突**：2025 年股東回饋（股利 + 買回）已接近 FCF 的 98%，2026 Q1 收購改由債務支應，後續若要去槓桿，可能壓抑買回。
- **獲利能力季度回落**：Q1'26 毛利率 35.6%（Q1'25 為 38.4%），營業利益率 15.7%（18.8%），淨利 YoY -10.2%，與營收 +16.8% 的成長形成背離。
- **FCF / NI 未達 0.9**：FY2025 為 0.87，雖然 Q1'26 FCF 改善，但全年轉換率仍偏低。
- **估值偏高**：trailing P/E 43.6x、P/FCF 約 44.7x、P/B 7.84x，市場對成長與收購綜效已有相當定價。
- **Forward EPS 數字不一致（數據品質風險）**：info 的 forwardEps 16.28 隱含 H2'26 EPS 約 10.32（16.28 - Q1 2.81 - Q2 3.15），即每季約 5.2，遠高於 Q3'26 consensus 3.54 與近期季度水準（約 3.1–3.3）。forward P/E 25.1x 因此可能低估實際倍數。須以 consensus 來源核實。
- **GAAP 與 adjusted EPS 口徑混合**：trailingEps 9.38 與 GAAP 季度 diluted EPS 加總 9.83（2.59 + 2.91 + 2.22 + 2.11）不符；info 的 TTM P/S 5.29 隱含 TTM 營收約 30.0B，而季度營收加總為 28.52B；info ebitda 6.64B 與季度加總 6.22B 也不符。上述數字應以原始來源核實，本報告並列標示。
- **Q2'26 季度財務不完整**：quarterly_fin 與 quarterly_cf 的 2026-06-30 欄位大多為 null（僅 EPS 有值），無法完整計算 Q2'26 營收與現金流。
- **價格快照不一致**：info currentPrice 408.85 與 fulldayPrice 399.81 並存，盤中資料源為 cache，建議交易前以即時報價確認。
- **做空比例上升**：short interest 月增 10.8%，佔流通股 2.06%，絕對水準不高，但方向值得追蹤。
- **資料缺口**：同業中位數、分部營收、公司 guidance、收購細節均為 DATA_UNAVAILABLE。

FUNDAMENTALS REPORT COMPLETE
