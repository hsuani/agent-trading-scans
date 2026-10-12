# Fundamentals — VST as of 2026-10-13

## Executive summary
VST 的獲利與自由現金流已自 2025 下半年起回升，TTM 營收 19.21B USD、EBITDA 6.55B USD、FCF 2.26B USD 皆為正，但 2025 全年 FCF 較 2024 下滑約 47%，且季度盈餘波動極大。資產負債表偏緊：net debt/EBITDA 約 2.97x、total debt/total equity 約 3.6x、current ratio 0.97、tangible book value 為負，財務彈性有限。估值方面，trailing P/E 27.1x 偏高、forward P/E 15.4x 明顯較低，EV/EBITDA TTM 約 11.7x、P/FCF TTM 約 23.9x，估值是否合理取決於市場預期的獲利大幅回升能否兌現；近 6 個月內部人為淨賣出約 24.7M USD，占市值約 0.05%，規模不大。

資料說明：本次資料來源為 repo 快取（source: cache），財報最新至 2026-06-30（2026 Q2），股價快取時間為 2026-10-12 15:08 UTC。未發現晚於 2026-10-13 的財務或價格數據；2026-11-06 為排定之下次財報日（未來日期，非資料）。

## Revenue & profitability

**營收與成長**
- 年度營收（Yahoo Total Revenue）：FY2022 13.73B、FY2023 14.78B、FY2024 17.22B、FY2025 17.74B USD。
- YoY：FY2023 +7.7%、FY2024 +16.5%、FY2025 +3.0%。成長動能明顯放緩。
- 3Y CAGR（FY2022–FY2025）：Total Revenue 8.9%；Operating Revenue 口徑 4.3%（FY2022 Operating Revenue 15.63B）。FY2021 為 null，無法計算 5Y CAGR。
- 季度 Total Revenue：2025 Q2 4.25B、Q3 4.97B、Q4 4.58B；2026 Q1 5.64B、Q2 4.02B USD。
- 季度 Operating Revenue：2025 Q2 3.75B、Q3 4.78B、Q4 4.96B；2026 Q1 5.00B、Q2 4.40B USD。兩種口徑在 2026 Q1 與 Q2 差距明顯（例如 Q1 相差約 0.64B），Yahoo Total Revenue 可能包含避險或衍生性損益，本工具無法驗證其組成，請以公司 10-Q 為準。
- 業務結構（來自 info.longBusinessSummary）：五大 segment 為 Retail、Texas、East、West、Asset Closure；服務約 5M 客戶，發電容量約 44,000 MW，組合包含天然氣、核能、煤、太陽能與電池儲能。各 segment 營收與獲利：DATA_UNAVAILABLE。

**獲利能力（以 FY 數字計算）**

| 指標 | FY2022 | FY2023 | FY2024 | FY2025 | TTM（至 2026 Q2） |
|---|---|---|---|---|---|
| Gross margin（Revenue − Reconciled Cost of Revenue） | 12.3% | 37.4% | 43.7% | 32.9% | n/a |
| Operating margin（Total Operating Income As Reported / Total Revenue） | -8.6% | 18.0% | 23.7% | 10.7% | 約 19.6%（EBIT 口徑 3.77B / 19.21B） |
| EBITDA margin（EBITDA / Total Revenue） | 7.6% | 31.0% | 40.4% | 28.5% | 34.1% |
| Normalized EBITDA margin | 5.8% | 30.7% | 39.9% | 29.5% | 34.5% |
| Net margin（Net Income Common Stockholders / Revenue） | -10.0% | 9.1% | 14.3% | 4.2% | 10.6% |

注意：FY2022 gross margin 與 operating margin 為負或偏低，成因在工具資料中未揭露（減損或其他項目：DATA_UNAVAILABLE）；TTM operating margin 以 EBIT 口徑計算，未扣除 Yahoo 歸類的部分 unusual items。

- Yahoo info profitMargins（TTM）：11.55%。
- ROE（FY2025，NI to common / 平均 Stockholders Equity，含特別股）：14.1%。若以平均 common equity（扣除特別股約 2.48B）計算：約 26.3%，因普通股權益基數小且受庫藏股影響，此數字放大。
- ROIC（FY2025，EBIT × (1 − 15.9% 稅率) / 平均 Invested Capital）：約 8.3%。

**每股盈餘（EPS）**
- Diluted EPS：FY2022 −3.15、FY2023 3.82、FY2024 7.26、FY2025 2.22 USD。
- 季度 Diluted EPS：2025 Q1 −0.93、Q2 0.83、Q3 1.78、Q4 約 0.55（由年度 2.22 減去前三季推算，季度資料為 null）、2026 Q1 2.90、Q2 0.77 USD。
- TTM Diluted EPS 約 6.00 USD（由季度加總推算）；trailing P/E 以此計算約 26.9x，與 info 的 trailingPE 27.1x 大致一致。
- 財報超預期／不及紀錄（earnings_dates，Yahoo 資料）：2026-08-10 報告 EPS 0.76 vs 預期 1.63（−53.4%）；2026-05-08 報告 2.87 vs 1.87（+53.3%）；2026-02-27 報告 0.54 vs 2.30（−76.5%）；2025-11-07 報告 1.38 vs 1.40（−1.3%）；2025-08-08 報告 0.71 vs 1.05（−32.5%）；2025-05-08 報告 −0.93 vs 0.61（−251.7%）。
- 注意：Yahoo 的 EPS 實際值與一致預期可能不是同一口徑（例如 GAAP 與 adjusted），且 VST 獲利受避險與市價波動影響大。以超預期百分比判讀時須保守，應以公司揭露之 adjusted EBITDA 與 adjusted EPS 交叉確認，本工具無法取得。

## Cashflow & balance sheet

**現金流量**
- 營運現金流（OCF）：FY2022 0.49B、FY2023 5.45B、FY2024 4.56B、FY2025 4.07B USD；TTM 5.12B USD。
- 資本支出（Capex）：FY2022 1.30B、FY2023 1.68B、FY2024 2.08B、FY2025 2.75B USD（FY2025 YoY +32.4%）；TTM 2.87B USD。FY2025 capex / D&A（2.95B）約 0.93x。
- 自由現金流（FCF = OCF − Capex）：FY2022 −0.82B、FY2023 3.78B、FY2024 2.49B、FY2025 1.32B USD（FY2025 YoY −47%）；TTM 2.26B USD。
- FCF margin：FY2025 7.4%、TTM 11.7%。
- FCF / NI：FY2025 為 1.40x（NI 944M，含非控制權益）；以 NI to common（752M）計為 1.75x。TTM FCF / NI from continuing operations（2.22B）為 1.02x，高於 0.9 的健康門檻。
- 季度 FCF 波動大：2025 Q2 −118M、Q3 1,009M、Q4 596M；2026 Q1 316M、Q2 334M USD。

**資產負債表（2026 Q2，除非另註）**
- 現金：435M USD（2025 年底 785M；2024 年底 1,188M）。
- Total Debt：19.90B USD（2025 年底 20.07B；2024 年底 17.05B）。
- Net Debt：19.46B USD（2025 年底 19.28B；2024 年底 15.86B）；FY2025 Net Debt 較 FY2024 增加約 21.6%。
- Net debt / EBITDA：TTM（EBITDA 6.55B）約 2.97x；以 FY2025 EBITDA（5.06B）計約 3.81x。
- 利息保障倍數（TTM EBIT 3.77B / 利息費用 0.97B）：約 3.9x。FY2025 利息費用 982M，較 FY2024（859M）增加 14.3%。
- Current ratio：0.97（2025 年底 0.78；2024 年底 0.96）。Working capital：−281M USD。
- Total debt / Total Stockholders Equity：3.63x（2025 Q2 為 3.74x，改善約 0.11x）。
- Tangible book value：−2.09B USD（負值，表示有形權益為負）。特別股（Preferred Stock Equity）2.48B USD；普通股權益（Common Stock Equity）約 3.01B USD。

## Capital allocation & insider signal

**資本配置**
- 買回股票（Repurchase of Capital Stock）：FY2022 1.95B、FY2023 1.25B、FY2024 1.27B、FY2025 1.03B USD（FY2025 YoY −18.8%）；TTM 約 1.15B USD（2025 Q3 187M、Q4 252M、2026 Q1 372M、Q2 337M）。
- 流通股數（Diluted Average Shares）：FY2022 389.8M → FY2025 338.1M，3 年下降 13.3%；2026 Q2 為 336.0M。Info 中 sharesOutstanding 為 335.6M。庫藏股數量持續上升（2026 Q1 約 217.9M 股）。
- 股息：每股股息率（dividendRate）0.92 USD、殖利率 0.57%、payout ratio（earnings）15.4%。FY2025 普通股股息支付 306M USD、特別股股息 192M USD，合計 498M USD。
- 股息覆蓋：FY2025 FCF 1.32B / 股息合計 0.50B ≈ 2.6x；扣除股息後 FCF 約 820M USD。
- 2025 年投資現金流出 4.40B USD，高於 capex 2.75B，差額約 1.64B USD 屬非資本支出之投資（可能為併購或其他投資），具體內容：DATA_UNAVAILABLE。
- 債務滾動：FY2025 發行債務 6.02B、償還 3.82B USD；2026 Q2 單季發行 4.42B、償還 4.44B USD，顯示以再融資方式滾動債務。

**內部人交易（近 6 個月，2026-04-13 至 2026-10-13，依 insider 資料）**
- 公開市場賣出：10 筆、合計 163,254 股、約 25.88M USD。
- 公開市場買入：2 筆、合計 8,665 股、約 1.17M USD（CEO James A. Burke，2026-08-24 與 2026-09-01，價格約 135–136）。
- 淨賣出約 24.7M USD，占 market cap（53.98B USD）約 0.046%，規模小。
- 主要賣出：
  - CFO Kristopher E. Moldovan：2026-10-07 賣出 20,000 股（約 3.30M USD，165.00）；2026-09-08 賣出 20,000 股（約 3.02M USD，151.03）。
  - President of Retail Scott A. Hudson：2026-10-06 賣出 22,222 股（約 3.56M USD，160.14）；2026-09-08 賣出 44,444 股（約 6.75M USD，約 151–153）。
  - 董事 Scott Bradford Helm：2026-06-16 賣出 25,000 股（約 4.00M USD，160.00）。
  - 董事 Arcilia C. Acosta、John R. Sult、Paul M. Barbas；Margaret M. Montemayor（Officer）亦有小額賣出。
- 工具資料未標示是否為 10b5-1 預設計畫交易，無法確認賣出動機，請交由 trader 判讀。
- 同期 2025 年 10 月前後 CEO Burke 有大量期權行使後賣出（單筆約 400 萬至 1,700 萬 USD），本期 CEO 轉為小額買入，方向上屬於相對正面的信號，但金額小。
- 持股結構：內部人持股 0.77%；機構持股 92.0%（1,880 家）。前五大機構：BlackRock 8.66%、Vanguard Capital Management 6.37%、Vanguard Portfolio Management 5.05%、State Street 5.02%、FMR 4.22%（FMR 季度減持 10.4%）（資料日期 2026-06-30）。

## Valuation

**價格與市值（info 與快取）**
- 最新價（快取，2026-10-12 15:08 UTC）：161.30 USD；前收 161.48 USD。
- 市值（marketCap）：53.98B USD；企業價值（EV）：76.76B USD。
- 52 週區間：132.66–217.10 USD；ATH 219.82 USD。現價較 52 週高點低約 25.7%，較 52 週低點高約 21.6%。
- 50 日均線 143.90 USD（現價高約 12.1%）；200 日均線 154.74 USD（現價高約 4.2%）。
- Beta 1.38。

**估值倍數**
- Trailing P/E：27.1x（info）；由 TTM EPS 約 6.00 推算約 26.9x。
- Forward P/E：15.4x（info）。Forward 明顯低於 trailing，隱含市場預期獲利大幅回升。
- EV/EBITDA：TTM（EBITDA 6.55B）約 11.7x；TTM normalized EBITDA（6.64B）約 11.6x；FY2025（5.06B）約 15.2x。
- P/FCF：TTM（FCF 2.26B）約 23.9x；FY2025（1.32B）約 41.0x。
- P/S：TTM（Total Revenue 19.21B）約 2.81x。
- Sector median（估計）：以下為分析師一般認知之估計值，非工具資料，需交叉驗證。Utilities – Independent Power Producers 行業 trailing P/E 約 20–25x、EV/EBITDA 約 10–12x、P/S 約 1.5–2.5x、P/FCF 約 20–30x、股息殖利率約 1–3%。依此估計，VST 的 trailing P/E 偏高、EV/EBITDA 處於合理區間、P/S 偏高。

**空頭與流動性**
- 空單股數（sharesShort，資料月）：10.48M 股，占流通股約 3.1%；以 averageVolume 5.28M 計，回補天數約 2.0 日。
- 10 日平均量 9.41M 股，明顯高於 3 個月平均量，近期交易活絡。

## Key catalysts
- 下次財報：2026-11-06（Yahoo 排定，對應 2026 Q3）；EPS 一致預期 2.59 USD。以 2026 Q2 實際 EPS 0.77 USD 相比，預期值需大幅回升，為本季最重要的催化事件。
- 除息日：依 exDividendDate epoch 換算約 2026-09-21（已過），目前股息殖利率 0.57%。
- 近期事件：2026-08-10 季報 EPS 不及預期（−53.4%）；2026 Q2 單季 Total Debt 再融資（發行 4.42B、償還 4.44B USD）；2026 Q2 capex 單季 689M USD（2026 Q1 為 883M）。
- 管理層與治理：CEO James A. Burke（FY2025 薪酬 4.56M USD）、CFO Kristopher E. Moldovan；info overallRisk 為 1（低）、auditRisk 4、shareHolderRightsRisk 5。
- 公司指引（guidance）與新增 segment 營運數據：DATA_UNAVAILABLE（本工具不提供）。
- 分析師一致預期的營收與 EBITDA：n/a（本工具不提供）。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Total Revenue（TTM） | 19.21B USD | FY2025 +3.0% | 約 3–5%（估計成長率） | 中性，成長放緩 |
| Revenue 3Y CAGR（FY22–25，Total Revenue） | 8.9% | n/a | 約 5%（估計） | 中性偏強 |
| Gross margin（FY2025） | 32.9% | 2024 為 43.7%（−10.8pp） | n/a（口徑不可比） | 偏弱 |
| Operating margin（FY2025） | 10.7% | 2024 為 23.7%（−13.0pp） | 約 15%（估計） | 偏弱 |
| EBITDA margin（FY2025） | 28.5% | 2024 為 40.4% | 約 30%（估計） | 中性 |
| Net margin，NI to common（FY2025） | 4.2% | 2024 為 14.3% | 約 10%（估計） | 偏弱 |
| ROE（平均 common equity，FY2025） | 26.3% | ROE（含特別股）14.1% | 約 10–12%（估計） | 強，但權益基數小 |
| ROIC（FY2025） | 8.3% | n/a | 約 7–8%（估計） | 中性 |
| FCF margin（TTM） | 11.7% | FY2025 7.4% | 約 8–10%（估計） | 中性偏強 |
| FCF / NI（TTM，NI from continuing ops） | 1.02x | FY2025 1.40x | 約 1.0x（估計） | 合格（剛過 0.9 門檻） |
| Free Cash Flow（FY2025） | 1.32B USD | −47% | n/a | 偏弱 |
| Capex（FY2025） | 2.75B USD | +32.4% | n/a | 擴張中，偏弱 |
| Net debt / EBITDA（TTM） | 2.97x | FY2025 為 3.81x | 約 3–4x（估計） | 中性，較去年改善 |
| 利息保障倍數（TTM EBIT / Interest） | 3.9x | FY2025 為 2.1x | 約 4x（估計） | 中性 |
| Current ratio（2026 Q2） | 0.97 | 2025 年底 0.78 | 約 1.2x（估計） | 偏弱 |
| Total debt / Total equity（2026 Q2） | 3.63x | 2025 Q2 為 3.74x | 約 1.5–2.5x（估計） | 偏弱，槓桿高 |
| Tangible book value（2026 Q2） | −2.09B USD | — | 正值 | 偏弱 |
| 買回股票（FY2025） | 1.03B USD | −18.8% | n/a | 中性 |
| 股數變化（FY2022→FY2025 Diluted） | −13.3% | — | n/a | 偏強 |
| 股息覆蓋（FY2025 FCF / 股息合計） | 2.6x | — | 約 1.5–2.5x（估計） | 合格 |
| Payout ratio（earnings） | 15.4% | — | 約 40–60%（估計） | 偏保守 |
| 股息殖利率 | 0.57% | — | 約 1–3%（估計） | 偏低 |
| Trailing P/E | 27.1x | — | 約 20–25x（估計） | 偏貴 |
| Forward P/E | 15.4x | — | 約 15–20x（估計） | 合理，取決於獲利回升 |
| EV/EBITDA（TTM） | 11.7x | FY2025 為 15.2x | 約 10–12x（估計） | 合理 |
| P/FCF（TTM） | 23.9x | FY2025 為 41.0x | 約 20–30x（估計） | 中性 |
| P/S（TTM） | 2.81x | — | 約 1.5–2.5x（估計） | 偏高 |
| 內部人淨買賣（6 個月） | 淨賣出約 24.7M USD | — | n/a | 小幅淨賣，占市值 0.05% |
| 空單比例（占流通股） | 3.1% | — | n/a | 低 |
| Beta | 1.38 | — | 約 1.0（估計） | 高於市場 |

## Red flags
- 槓桿與流動性偏緊：net debt 19.46B USD、total debt/equity 3.63x、current ratio 0.97、tangible book value −2.09B USD；利息費用 2025 年增 14.3%，且 2026 Q2 單季即有 4.4B USD 規模的再融資。
- FCF 2025 年減少 47%，capex 2025 年增 32.4% 且 TTM capex 仍達 2.87B USD；TTM FCF 的改善部分來自 2025 Q3 單季 1.0B USD，單季波動大，不宜外推。
- 盈餘品質與可預測性低：2026 Q2 EPS 0.77 vs 預期 1.63（−53.4%）；2025 Q1 EPS −0.93；Yahoo EPS 與一致預期口徑可能不一致，需以 adjusted 數字交叉確認。
- Total Revenue 與 Operating Revenue 口徑差異大（2026 Q1 相差約 0.64B USD），收入品質需以公司揭露為準。
- 估值依賴獲利回升：trailing P/E 27.1x 對比 forward P/E 15.4x，隱含市場預期 2026 Q3 起 EPS 大幅回升（一致預期 2.59 USD vs 2026 Q2 實際 0.77 USD）。
- 內部人淨賣出（CFO 與 Retail President 於 2026 年 9–10 月的賣出合計約 16.6M USD），雖占市值比例小，但需確認是否為 10b5-1 計畫。
- 2025 年非資本支出投資約 1.64B USD（investing cash flow 扣除 capex 之差額），用途未揭露於工具資料，DATA_UNAVAILABLE。
- 股價較 200 日均線高約 4.2%、較 52 週高點低約 25.7%，短期波動與 Beta 1.38 相對較高。

FUNDAMENTALS REPORT COMPLETE
