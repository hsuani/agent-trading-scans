# Fundamentals — GEV as of 2026-11-24

資料基準：價格與 info 為 2026-11-23 收盤附近快取（info cached_at 2026-11-23T17:58Z，fast_info cached_at 17:54Z；source=cache 屬正常 fallback）。財報為 2025 年報與 2026 Q1–Q3 季報（最新 Q3 於 2026-10-28 公布）。未發現 2026-11-24 之後的資料；下一次財報 2027-01-27 為預定日期。金額單位：USD B（十億美元），本報告無 TWD / KRW，不涉及億換算。

## Executive summary
GEV 財務體質在 2026 年明顯轉強：Q3'26 營收 USD 12.64B 年增 +26.8%、毛利率升至 24.6%、TTM FCF 約 USD 17.1B，並由 2026 Q1 的 USD 2.6B 債務發行後仍維持 USD 13.97B 淨現金（BS 口徑）。但獲利與現金流品質需打折：Q1'26 GAAP EPS 17.44 含約 USD 4.4B 一次性收益、Q4'25 含 USD 2.57B 稅務利益，TTM 營業 margin 僅 6.4%，而 OCF 有相當部分來自客戶預收款（current deferred revenue 2025 年底 USD 25.77B 到 Q3'26 達 USD 45.67B），屬可逆性較高的營運資金。估值方面，forward P/E 29.1x、EV/EBITDA 34.4x 相對一般工業機械偏高，但股價距 52 週高點 USD 1,195.94 已回落 37%，分析師目標價均值 USD 1,162.40（較現價 +54%），市場對成長性與預收款持續性的分歧是當前核心。

## Revenue & profitability

**營收趨勢（USD B）**
- 年度營收：2022 29.65 → 2023 33.24 → 2024 34.94 → 2025 38.07。
- 3 年 CAGR（2022–2025）約 8.7%；2 年 CAGR（2023–2025）約 7.0%；2025 YoY +9.0%。
- 季度加速明顯：Q3'26 營收 12.64，對比 Q3'25 的 9.97，YoY +26.8%；由季報推算 H1'26 營收 20.44 對比 H1'25 推算值 17.14，約 +19.2%（H1'25 為 2025 年報減 Q3'25、Q4'25 推算，非直接揭露）；9M'26 33.08，約 +22.0%（推算）。
- 分部（Power / Wind / Electrification）營收拆分：yfinance 工具未提供，DATA_UNAVAILABLE。longBusinessSummary 僅描述三大分部內容。

**毛利、營業利益、淨利率趨勢**
| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| 2022 | 11.7% | -9.7% | -9.2% |
| 2023 | 14.5% | -2.8% | -1.3% |
| 2024 | 17.4% | 1.3% | 4.4% |
| 2025 | 19.8% | 3.6% | 12.8%（含稅務與一次性項目） |

- 季度：Q3'26 毛利率 24.6%（Q3'25 為 19.0%）、營業利益率 11.0%（Q3'25 為 3.7%）；Q2'26 營業利益率 5.9%；Q1'26 1.9%。
- TTM（Q4'25–Q3'26）：營收 44.04、毛利 9.57、營業利益 2.83（營業利益率 6.4%）、淨利 10.37（yfinance profitMargins 23.5%，被一次性項目嚴重拉高）。TTM 正常化淨利（normalized income）約 5.91，淨利率約 13.4%。
- ROE（info）93.0%：受股東權益僅 USD 11.18B（2025 年底）與大額 treasury stock 影響，屬失真高值。ROIC 為本報告估算：TTM NOPAT（營業利益 2.83 × (1−25.6% 稅率)）除以 Q3'26 invested capital 14.18，約 14.9%；以 2025 年底 invested capital 11.51 計約 9.0%。
- EBITDA：2025 年報 EBITDA 2.24（normalized EBITDA 2.07）；info 的 TTM ebitda 為 5.05，與季度加總的 4.26 不一致，本報告兩者並列，EV/EBITDA 以 info 值計。

## Cashflow & balance sheet

**現金流（USD B）**
| 期間 | OCF | Capex | FCF | FCF/NI |
|---|---|---|---|---|
| FY2025 | 4.99 | 1.28 | 3.71 | 0.76 |
| TTM（Q4'25–Q3'26） | 19.22 | 2.10 | 17.12 | 1.65（normalized 口徑 2.90） |

- FCF margin：FY2025 9.7%；TTM 38.9%。
- FCF/NI 品質判讀：FY2025 因 OCF 含 Q4'25 大量 deferred tax 與工作資本變化，FCF/NI 0.76 低於 0.9 健康門檻；TTM 高於 1 主要因 NI 含一次性收益，而 TTM OCF 中 change in other working capital 合計約 USD 25.1B（Q4'25–Q3'26 季度加總，當中 current deferred revenue 2025 年底至 Q3'26 增加約 USD 19.9B）。若預收款維持增長，現金流可持續；若交付節奏放緩或預收款回落，FCF 將出現明顯波動。
- 2025 年底至 Q3'26 的預收款增額 USD 19.90 約為同期 9M'26 OCF USD 16.74 的 1.19 倍，屬本報告最需追蹤的品質指標。

**資產負債表（USD B，Q3'26 季報，除非註明）**
- 現金及短期投資：16.76（2025 年底 9.31）。
- 總債務：2.80（2026 Q1 發行 USD 2.57 長期債）；2025 年底 1.17。
- 淨現金（BS 口徑）：約 +13.97。yfinance info 口徑：totalCash 16.36、totalDebt 3.75（含租賃），淨現金約 +12.62。
- 負債/權益（BS 口徑）：2.80 / 11.38 ≈ 0.25x；info debtToEquity 為 29.9（口徑含租賃與少數股權）。
- 流動比率：Q3'26 0.83（2025 年底 0.98）；quick ratio（info）0.57。
- 營運資金：Q3'26 USD −10.79（2025 年底 −0.76），負值主因為 current deferred revenue 45.67 大於多數流動資產項目。
- 商譽與無形資產：Q3'26 13.95（2025 年底 5.17），2026 Q1 收購支出 USD 4.90（yfinance Purchase Of Business 科目；標的與性質未於工具資料揭露，需查 10-Q）。
- 有形淨值（tangible book）：Q3'26 USD −2.57，2025 年底為 +6.01。
- 股東權益：Q3'26 USD 11.38（每股 bookValue 約 43.00）。總資產 86.22，總負債 73.68。

## Capital allocation & insider signal

**資本配置**
- Capex：FY2025 1.28（營收 3.4%）、TTM 2.10（4.8%）、Q3'26 0.65（對比 Q3'25 0.25，YoY +162%）。Capex 進入明顯擴張期。
- 庫藏股：9M'26 回購 USD 5.30（Q1 1.28、Q2 2.39、Q3 1.63）；TTM 回購 USD 6.37；2025 年 USD 3.32。流通股數由 2024 年底 276M 降至 2026 Q3 約 265M（−4.0%）。
- 股息：每季 USD 0.50，年化 USD 2.00，殖利率 0.29%；TTM 股息現金支出約 USD 0.47。FCF 覆蓋約 36 倍，股息為象徵性配置。
- 回購＋股息合計 TTM 約 USD 6.85，相當於 TTM FCF 的約 40%，其餘資金用於收購與淨現金累積。

**內部人交易（6 個月窗口：2026-05-24 至 2026-11-23）**
- 公開市場賣出 2 筆：ABATE VICTOR（Officer）2026-06-01 賣出 4,819 股，約 USD 4.57；POTVIN MATTHEW JOSEPH（Officer）2026-05-14 賣出 2,333 股，約 USD 2.47。合計 USD 7.04，為市值 USD 199.37 的 0.0035%。
- 公開市場買入：無。
- 其他：2026-05-14 八位董事各獲 495–1,350 股之 stock award（授予，非買賣）。
- 窗口外參考：CEO STRAZIK SCOTT 2026-04-27 選擇權行使 44,496 股（yfinance 標示 USD 5.35）；BAERT STEVEN 2026-03-03 賣出 5,300 股（USD 4.51）。
- 內部人持股 heldPercentInsiders 0.14%（約 USD 0.28B），內部人與股東利益綁定程度低。解讀：6 個月內賣出規模小、為個人執行層行為，無集中式減持訊號，亦無增持訊號。

**機構持股（13F，截至 2026-09-30）**
- 機構持股比例 79.8%，機構數 4,224 家。
- 前十大（合計約 36.1%）：BlackRock 7.97%（QoQ −3.1%）、Vanguard Capital 6.59%（−0.7%）、FMR 5.58%（−8.6%）、State Street 4.42%（−0.6%）、Geode 2.43%（+1.3%）、Morgan Stanley 2.07%（−4.0%）、Capital World 1.93%（+2.3%）、Fisher Asset Management 1.86%（+38.3%）、Vanguard PM 1.80%（+1.1%）、JPMorgan 1.42%（−39.8%）。
- 空單：sharesShort 7.48M（占流通 2.83%），shortRatio 2.55 日，較上月 +1.4%，屬低水位。

## Valuation

以現價 USD 753.27（2026-11-23 盤中/收盤附近，市值 USD 199.37，EV USD 173.64）計算：

- P/E：trailing 19.8x（以 EPS 38.09 計，該 EPS 含 Q1'26 一次性收益，失真偏低）；forward 29.1x（forwardEps 25.90，yfinance 未標註期間定義）；epsCurrentYear 15.68 推算 P/E 48.0x（注意：其值低於 9M'26 已報 GAAP EPS 合計 24.72，口徑不一致，本報告不採用）。
- EV/EBITDA：34.4x（info TTM EBITDA 5.05）；以 2025 年報 EBITDA 2.24 計約 77x。
- P/S：4.53x（TTM 營收 44.04）。
- P/FCF：TTM 11.6x（以計算值 17.12 計）；info freeCashflow 為 22.10，對應 9.0x。兩者差異未能由工具資料解釋，本報告以季度加總值為準。
- P/B：17.5x；PEG（info）1.29。
- 分析師：33 家，recommendationMean 1.46（Strong Buy 區間）；rec_summary 目前 7 Strong Buy／25 Buy／5 Hold／0 Sell，三個月前為 6／24／7／0，評級略升。目標價 high 1,400、mean 1,162.40、median 1,200、low 783.86（全部高於現價）。
- 價格位置：現價較 52 週高 1,195.94 回落 37.0%，較 50 日均線 893.70 低 15.7%，較 200 日均線 951.92 低 20.9%，較 52 週低 553.25 高 36.2%。52 週漲幅 +20.5%，S&P 500 同期 +3.1%。
- 同業比較：本次工具未提供同業財務數據，以下「sector median」為經驗估計，非工具資料，僅供粗略參照。

## Key catalysts

- 下次財報：2027-01-27（yfinance earningsTimestamp，isEarningsDateEstimate=False），Q4'26 EPS 共識 6.95。info 亦含 earningsCallTimestamp 2027-01-21，與財報日不一致，需以公司公告為準。
- 近期財報表現（yfinance 之 GAAP 口徑）：
  - Q3'26（2026-10-28）：EPS 4.81 vs 估計 4.01，+19.9%（營收與毛利率同步改善）。
  - Q2'26（2026-07-22）：EPS 2.47 vs 3.18，−22.4%。
  - Q1'26（2026-04-22）：EPS 17.44 vs 2.00，表面 +771.6%，實為一次性收益 USD 4.4B 所致，不具可比性。
  - Q4'25（2026-01-28）：EPS 13.39 vs 3.22，主因 USD 2.57 稅務利益，同樣失真。
- 股利：除息日 2026-10-27，發放日 2026-11-24（dividendDate）。
- 指引（guidance）與訂單/積壓（backlog）：yfinance 工具未提供，DATA_UNAVAILABLE。
- 新聞與催化事件：news 工具回傳空值，DATA_UNAVAILABLE。2026-11-23 單日 +7.71%（收盤 753.27 vs 前收 699.33）之原因無法由本次資料確認。
- 結構性催化（可由財報觀察）：Power 分部燃氣機組需求與 deferred revenue 能否持續增長、Electrification 與 Q1'26 收購之整合效益、Capex 擴張（Q3 YoY +162%）之報酬，以及 Q4 季度 FCF 是否延續 9M 節奏。

## Metrics table
單位：營收、利潤、現金流、市值、EV、負債、現金為 USD B；比率為 %；倍數為 x。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 Revenue（FY2025，USD B） | 38.07 | +9.0% | n/a | 穩健成長 |
| 營收 Q3'26（USD B） | 12.64 | +26.8% | n/a | 加速 |
| 3Y 營收 CAGR（2022–25） | 8.7% | n/a | n/a | 中等 |
| 毛利率 Gross margin（FY2025） | 19.8% | +2.4pt（對 2024 17.4%） | 約 25–30%（估計） | 低於同業估計，持續改善 |
| 毛利率 Gross margin（Q3'26） | 24.6% | +5.5pt（對 Q3'25 19.0%） | 約 25–30%（估計） | 接近同業 |
| 營業利益率 Operating margin（TTM） | 6.4% | n/a | 約 10–12%（估計） | 偏低 |
| 淨利率 Net margin（TTM，含一次性） | 23.5% | n/a | 約 8–10%（估計） | 失真，參考 normalized 13.4% |
| ROE（info） | 93.0% | n/a | 約 15%（估計） | 因權益基數小而失真 |
| ROIC（本報告估算，TTM） | 14.9% | n/a | 約 10%（估計） | 改善中 |
| OCF（TTM，USD B） | 19.22 | n/a | n/a | 強，但依賴預收款 |
| FCF（TTM，USD B） | 17.12 | n/a | n/a | 強 |
| FCF margin（TTM） | 38.9% | n/a | 約 10%（估計） | 極高，可逆性需追蹤 |
| FCF / NI（FY2025） | 0.76 | n/a | >0.9 為健康門檻 | 偏弱 |
| Capex / 營收（TTM） | 4.8% | 2025 為 3.4% | 約 3–5%（估計） | 擴張中 |
| 現金 Cash（Q3'26，USD B） | 16.76 | 2025 年底 9.31 | n/a | 充裕 |
| 總債務 Total debt（Q3'26，USD B） | 2.80 | 2025 年底 1.17 | n/a | 2026 上升，仍低 |
| 淨現金 Net cash（BS 口徑，USD B） | +13.97 | 2025 年底約 +8.1 | 約 0（估計） | 強 |
| 負債/權益 Debt/Equity（BS） | 0.25x | n/a | 約 0.5x（估計） | 低 |
| 流動比率 Current ratio（Q3'26） | 0.83x | 2025 年底 0.98x | 約 1.5x（估計） | 偏低，因預收款結構 |
| 有形淨值 Tangible book（USD B） | −2.57 | 2025 年底 +6.01 | n/a | 警訊 |
| 股東權益 Equity（Q3'26，USD B） | 11.38 | 2025 年底 11.18 | n/a | 小幅增加 |
| 股份數 Shares outstanding（M） | 265 | 2024 年底 276（−4.0%） | n/a | 回購縮股 |
| 回購 Buyback（TTM，USD B） | 6.37 | 2025 年 3.32 | n/a | 增加 |
| 股息 Dividend yield | 0.29% | n/a | 約 1–2%（估計） | 象徵性 |
| 內部人 6M 淨交易（USD B） | 買入 0 / 賣出 −0.007 | n/a | n/a | 中性 |
| 機構持股 Institutional ownership | 79.8% | n/a | 約 80–90%（估計） | 正常 |
| 空單 Short % float | 2.83% | 較上月 +1.4% | 約 3–5%（估計） | 低 |
| 市值 Market cap（USD B） | 199.37 | n/a | n/a | — |
| EV（USD B） | 173.64 | n/a | n/a | — |
| P/E trailing | 19.8x | n/a | 約 25x（估計） | 因一次性收益失真 |
| P/E forward | 29.1x | n/a | 約 25x（估計） | 偏高 |
| EV/EBITDA（TTM，info） | 34.4x | n/a | 約 18x（估計） | 明顯偏高 |
| P/S（TTM） | 4.53x | n/a | 約 2.0x（估計） | 偏高 |
| P/FCF（TTM，計算） | 11.6x | n/a | 約 25x（估計） | 低，但預收款可逆 |
| P/B | 17.5x | n/a | 約 4x（估計） | 因權益基數小而偏高 |
| 分析師目標價均值 vs 現價 | +54.3%（mean 1,162.40） | n/a | n/a | 共識樂觀 |
| 股價 vs 52 週高 | −37.0% | n/a | n/a | 修正明顯 |

## Red flags
- OCF 與 FCF 品質：TTM OCF 中大量來自 current deferred revenue 增加（2025 年底至 Q3'26 增加 USD 19.9B，約為 9M'26 OCF 的 1.2 倍）。若預收款回落，FCF 會明顯下降。
- GAAP 獲利失真：Q1'26 含約 USD 4.4B 一次性收益（yfinance 列為 Special Income Charges 負值），Q4'25 含 USD 2.57B 稅務利益。TTM EPS 38.09、ROE 93%、淨利率 23.5% 均不應直接用於估值。
- 有形淨值為負（USD −2.57），商譽與無形資產升至 USD 13.95，2026 Q1 收購支出 USD 4.90 之標的與價格未於工具資料揭露。
- 營運資金為負（USD −10.79）、流動比率 0.83x，短期償債依賴客戶預付款與持續營運現金流。
- 營業利益率 TTM 僅 6.4%，相對 forward P/E 29x 與 EV/EBITDA 34x 隱含的獲利改善需求高。
- Q2'26 EPS 未達預期 −22.4%，為 2026 年唯一明顯不及的一季（Q1、Q4 均因一次性項目而不可比）。
- Capex 快速擴張：Q3'26 USD 0.65，YoY +162%，TTM 占營收 4.8%；資本報酬需後續驗證。
- 估值與股價位置：股價距 ATH 回落 37%，但仍高於 52 週低點 36%；估值倍數偏高，若獲利未如預期成長，回檔風險高。
- 資料一致性問題（已如實呈現，不自行修正）：info freeCashflow 22.10 vs 季度加總 17.12；info ebitda 5.05 vs 季度加總 4.26；epsCurrentYear 15.68 低於 9M'26 已報 GAAP EPS 24.72；earningsCallTimestamp（2027-01-21）與 earningsTimestamp（2027-01-27）不一致；forwardEps 期間未標註。
- 缺口：分部營收、指引、訂單/積壓、新聞均為 DATA_UNAVAILABLE；同業中位數為經驗估計，未經工具驗證。
- 單日 +7.71%（2026-11-23）原因未確認，短期波動可能來自無法於本次資料確認的事件。

FUNDAMENTALS REPORT COMPLETE
