# Fundamentals — SYM (Symbotic Inc.) as of 2026-11-13

資料來源: `source: cache`（`prices/yf/SYM.json`，`_refreshed_at` 2026-11-12T15:07:01Z）。即時 feed 之 Yahoo 連線失敗（CONNECT tunnel 403 / ConnectionError），依規定 fallback 至 cache，屬預期情況，非錯誤。`_misses` 為空，cache 內 info / financials / balance / cashflow / insider / holders / earnings_dates / recommendations 皆可讀取。
單位: 公司以 USD 報價，本報告金額統一以 USD M（百萬）或 USD B（十億）標示，無 TWD/KRW 金額，不混用 億。
財報期間: 財年截止於 9 月 30 日（FY25 = 2025-09-30）。最新已公布季度為 2026-06-30（FY26 Q3）。FY26 Q4（2026-09-30）尚未公布，預定 2026-11-23 發布。

## Executive summary
Symbotic 的營收成長仍強（TTM 營收 USD 2,645.8M，最新季 YoY +21.7%），毛利率與營業利益率在 2025–2026 年連續改善，且 FY25 與 TTM 自由現金流皆為正，帳上淨現金 USD 1,720.6M。然而 GAAP 獲利仍接近零（TTM 歸屬普通股淨利約 USD 12.7M），TTM 營運現金流高度依賴遞延收入（客戶預收款）增加，股本一年內稀釋約 16.9%，且股價較 52 週高點下跌約 60%、放空比率達 float 31.6%。估值上，GAAP trailing P/E 439.8x 與 forward P/E 48.2x 偏高，但以 yfinance 之 adjusted EPS 推算 trailing P/E 約 19.1x、以 TTM FCF 推算 P/FCF 約 6.2x；兩者口徑差異極大，需由下游判斷，本報告不給交易建議。

## Revenue & profitability

**營收與成長**
- 年度營收（USD M）: FY22 593.3 → FY23 1,176.9 → FY24 1,788.2 → FY25 2,246.9。
- FY25 YoY +25.6%；3 年 CAGR（FY22–FY25）約 55.9%；2 年 CAGR（FY23–FY25）約 38.2%。yfinance 僅提供 4 個年度，無法計算 5 年 CAGR。
- 季度營收（USD M）: FY25 Q3 592.1 / Q4 618.5 → FY26 Q1 630.0 / Q2 676.5 / Q3 720.8。最新季 YoY +21.7%（與 info `revenueGrowth` 0.217 一致）。
- TTM 營收 = 720.8 + 676.5 + 630.0 + 618.5 = USD 2,645.8M（與 info `totalRevenue` 2.646B 吻合）。
- 分部營收: yfinance 未提供分部拆分（longBusinessSummary 僅描述 warehouse automation 業務，無分部數字）。segment mix: DATA_UNAVAILABLE。

**獲利能力（口徑: yfinance 財報行項，GAAP）**

| 期間 | 毛利率 | 營業利益率 | 淨利率（歸屬普通股） |
|---|---|---|---|
| FY22 | 16.8% | -23.7% | -1.3%（NI to common -6.9M，含優先股股息調整，口徑特殊） |
| FY23 | 16.1% | -19.0% | -2.0% |
| FY24 | 13.7% | -6.5% | -0.8% |
| FY25 | 18.8% | -4.1% | -0.8% |
| FY26 Q3（6/30） | 22.3% | 4.6% | 1.6% |
| FY25 Q3（6/30 前一年） | 18.9% | -1.6% | -0.7% |
| TTM（4 季合計） | 21.6% | 1.2% | 0.5% |

- 毛利率由 FY24 低點 13.7% 回升至最新季 22.3%；營業利益由 FY25 Q4 的 -15.3M 轉正至 FY26 Q3 的 +32.9M。
- FY26 Q3 的稅前利益 63.5M 中，「其他非營業收入」為 30.6M，超過營業利益 32.9M 的一大部分，且股權法投資損失 -9.6M 亦在其中。本季獲利品質需打折，並非純營業驅動。
- 歸屬普通股淨利與 NI including NCI 差距大: FY26 Q3 NI incl. NCI 為 55.0M，歸屬普通股 11.7M，非控制權益（minority interests）為 -43.3M。425.2M 之 NCI 餘額（Jun-26）顯示合併子公司中有大量外部權益。
- ROE（yfinance `returnOnEquity`）4.39%。ROIC 本報告估算約 4–5%（TTM 營業利益 32.9M 近似 NOPAT，除以 Jun-26 股東權益 708.8M；yfinance 之 invested capital 與股東權益相同，無獨立負債口徑，屬估計值）。
- 營業費用結構改善: R&D 占營收 FY25 9.6%（216.0M）→ FY26 Q3 6.1%（43.8M）；SG&A FY25 13.3%（298.7M）→ FY26 Q3 11.7%（84.2M）。

## Cashflow & balance sheet

**現金流量（USD M）**

| 期間 | 營運現金流 CFO | Capex | 自由現金流 FCF | FCF 利潤率 |
|---|---|---|---|---|
| FY22 | -148.2 | -17.9 | -166.2 | n/m |
| FY23 | 230.8 | -21.3 | 209.5 | 17.8% |
| FY24 | -58.1 | -44.4 | -102.5 | -5.7% |
| FY25 | 866.9 | -79.0 | 787.9 | 35.1% |
| FY26 Q1 / Q2 / Q3 | 191.5 / 261.3 / -147.3 | -2.1 / -43.4 / -17.3 | 189.5 / 218.0 / -164.6 | n/m（季度） |
| TTM（FY25 Q4 至 FY26 Q3） | 836.2（季度合計） | -99.0 | 737.2（季度合計） | 27.9% |

- yfinance `info` 的 TTM 欄位為 `operatingCashflow` 894.4M、`freeCashflow` 547.6M（FCF 利潤率 20.7%），與季度合計 836.2M / 737.2M 有差異。本報告兩口徑皆列出，標示為 info 口徑與季度口徑。
- **FCF / NI 比率**: GAAP 淨利接近零或為負（FY25 NI -16.9M，TTM 歸屬普通股 12.7M），比率失真（n/m）。以 TTM NI including NCI 58.7M 計，FCF/NI 約 12.6x，仍無實質參考價值。
- **現金流品質**: FY25 OCF 866.9M 中，「Change in Other Working Capital」為 +583.4M，為主要來源。資產負債表上，遞延收入（current + non-current）由 Jun-25 的 923.1M 增至 Jun-26 的 1,736.5M（+88%，+813.4M），與 TTM OCF 的主要來源高度吻合；這代表客戶預收款而非盈利轉換，屬可持續性待確認項目。
- 最新季 FCF 為負（-164.6M）：CFO -147.3M，主要受應收帳款變動（-155.9M）拖累。

**資產負債表（Jun-26，USD M）**
- 現金及約當現金: 1,746.4（Jun-25: 777.6，YoY +124.6%；Mar-26 高點 2,011.6，本季減少 264.9M）。
- 總負債: debt 25.8（info `totalDebt`，季度 BS 未單列 borrowings，口徑以 yfinance 為準）。淨現金約 USD 1,720.6M。
- 股東權益（歸屬普通股）708.8；非控制權益 425.2；總權益 1,134.0；總資產 3,524.1；總負債 2,390.2。
- 流動比率 1.33（CA 2,857.8 / CL 2,147.1；Jun-25 為 1.08）；quick ratio 1.16（info）。營運資金 710.7。
- 負債權益比: 股東權益口徑 總負債/普通股權益 = 3.37x；有息負債/普通股權益 = 3.6%；yfinance `debtToEquity` 2.278（口徑未明，本報告不採用）。
- 應收帳款 + 其他應收 748.4（Jun-25: 372.7，YoY +100.8%）；存貨 220.8（YoY +59.0%）。營運資產成長快於營收。

## Capital allocation & insider signal

**資本配置（USD M）**
- Capex 占營收: FY22 3.0%、FY23 1.8%、FY24 2.5%、FY25 3.5%；TTM 3.7%。Capex 絕對值 FY25 79.0 為 FY22 的 4.4 倍。
- 併購: FY25 購買事業 -141.8（goodwill 59.9，intangibles 約 79.1）。
- 股權投資: Long-term equity investment 由 Sep-25 123.0 增至 Jun-26 140.5。
- 股權融資: FY22 +384.7、FY24 +258.0、FY25 0；FY26 Dec 季 +424.4（季度現金流量表），APIC 同期由 1,997.6 增至 2,018.0（Mar-26）。
- 股本稀釋: 普通股由 Jun-25 110.3M 增至 Jun-26 128.9M（YoY +16.9%；自 Sep-25 112.6M 起算 +14.5%）。
- SBC（股份基礎報酬）: FY25 183.9M（占營收 8.2%）；TTM 季度合計 207.2M（占營收 7.8%）。
- 股息: 無（`dividendYield` 0.0）。股息覆蓋率: n/a。
- 股票回購: 年報與季報未見明確 buyback 行項。2026 年 3 月季有 -61.0M 之普通股相關現金流出，yfinance 未標示性質（可能為回購或代扣稅，未確認）→ DATA_UNAVAILABLE（性質）。

**內部人交易（trailing 6 個月: 2026-05-13 至 2026-11-13；資料最後一筆 2026-11-02）**

| 類別 | 筆數 | 金額（USD M） | 股數 | 說明 |
|---|---|---|---|---|
| SoftBank Group（10% 以上大股東）賣出 | 1 | 281.8 | 5,590,000 | 2026-05-27，@ 50.42 |
| 董事 / 高管 賣出（ex SoftBank） | 26 | 7.8 | 181,382 | 價格區間約 38–53，多為小額定期性 2,000 股賣出（Krasnow、Kane）；Kuffner、Martins、Boyd、Alexander、Freve 亦有賣出 |
| 其他 / 無文字說明交易 | 14 | 0.0 | 266,410 | yfinance 無價格與性質（可能為股權歸屬或代扣），DATA_UNAVAILABLE |
| 買進 | 0 | — | — | 視窗內無公開市場買進紀錄 |

- 6 個月內賣出總額 USD 289.6M，相對 yfinance `marketCap` 21.3B 僅 1.4%，相對本報告採用的市值 USD 4.57B（129.9M 股 × 35.18）為 6.3%，其中 SoftBank 單筆占 6.2%。
- 排除 SoftBank 後，高管/董事賣出金額極小（USD 7.8M，約占市值 0.2%），但 2026-10-27 高管集中賣出（Kuffner、Alexander、Freve、Boyd，@ 38.2–39.1），且 2026-10-28 CFO Martins 賣出 7,224 股 @ 38.93。
- 解讀界線: 此為事實紀錄；賣出是否屬 10b5-1 計畫、是否為稅務相關，yfinance 未揭露，無法判斷其意圖。

## Valuation

**價格與市值（as-of 2026-11-13，最近報價 2026-11-12 cache）**
- 最新價: 35.18（info `regularMarketPrice`，當日 -5.2%，前收 37.11）。注意: `fast_info.last_price` 為 36.21（cache 15:01 UTC），與 info 不一致，本報告採 info 數值。
- 50 日均線 40.82（現價低於 13.8%）；200 日均線 47.05（現價低於 25.2%）。
- 52 週區間 33.17–87.88；現價高於 52 週低點 6.1%，低於高點 60.0%；52 週報酬 -37.7%；beta 2.06。
- **市值口徑衝突**: yfinance `marketCap` 為 USD 21.30B，但係由 `impliedSharesOutstanding` 605.4M 股推算；`sharesOutstanding` 為 129.87M，`nonDilutedMarketCap` 為 USD 4.89B。Jun-26 資產負債表普通股為 128.9M、BVPS 5.50（與 `priceToBook` 6.40 吻合），皆支持約 129–130M 股口徑。本報告採用 **USD 4.57B（129.87M × 35.18）** 作為主要市值，USD 21.3B 數值列為疑似錯誤，下游請勿直接引用。
- 企業價值 EV: yfinance `enterpriseValue` USD 3.52B；以本報告市值重算（4.57B − 淨現金 1.75B 之現金 + 有息負債 0.03B + NCI 0.43B）約 3.27B。兩者差距來自 NCI 與股數口徑，本報告以 3.3–3.5B 區間表示。

**本益與倍數**

| 指標 | 數值 | 口徑 |
|---|---|---|
| P/E（GAAP trailing） | 439.8x | EPS 0.08（info `trailingEps`）；季度 diluted EPS 合計 0.09 |
| P/E（forward） | 48.2x | `forwardEps` 0.73；`epsCurrentYear` 0.57 與 forward 口徑不一致 |
| P/E（adjusted trailing，推算） | 約 19.1x | earnings_dates 最近 4 季 Reported EPS 合計 0.58 + 0.40 + 0.45 + 0.41 = 1.84（adjusted 口徑，非 GAAP） |
| P/E（adjusted FY26，推算） | 約 24.8x | FY26 已公布 0.40 + 0.45 + 0.41 + 本季估計 0.16 = 1.42 |
| EV/EBITDA | 62.3x（info）；約 47x（推算） | info EBITDA 56.5M；季度 EBITDA 合計 74.3M，以 EV 3.52B 計 |
| P/FCF | 約 6.2x（季度 TTM FCF 737M）；約 8.3x（info FCF 548M） | 市值 4.57B |
| P/S | 約 1.7x（以 4.57B 計）；yfinance 8.05x（以 21.3B 計） | TTM 營收 2,645.8M |
| P/B | 6.4x | BVPS 5.50 |
| EV/Revenue | 1.33x（info） | |
| PEG | 4.58（info） | |

- 估值解讀: GAAP 獲利仍近零，GAAP P/E 無參考性；adjusted 口徑與 FCF 口徑顯示估值並不極端，但 adjusted 與 GAAP 之差距本身即為品質警訊。
- 分析師: 15 位（info `numberOfAnalystOpinions`），平均目標價 USD 61.50（+74.8% 相對現價）、中位數 65.0、最高 85.0、最低 38.0（高於現價 8.0%）。`averageAnalystRating` 2.2（Buy）。cache `rec_summary` 當期（0m）為 strongBuy 1 / buy 9 / hold 5 / sell 2 / strongSell 1；1 個月前為 strongBuy 1 / buy 8 / hold 5 / sell 2 / strongSell 1，評級結構大致穩定。
- 同業中位數（估計，非 yfinance 資料）: 工業機械 / 自動化族群之 P/E（forward）約 20–25x、EV/EBITDA 約 12–18x、P/S 約 1.5–3x、P/B 約 2–4x、毛利率約 25–35%、營業利益率約 8–12%，僅供量級比較。

## Key catalysts
- **FY26 Q4 財報**: 2026-11-23（yfinance `earnings_dates` 與 `earningsTimestamp` 一致，為未來排程，非 post-date 資料）。EPS 估計 0.16（adjusted 口徑）。
- **歷史 EPS 驚喜**: 最近 8 季 adjusted EPS 全數高於估計，最近 4 季驚喜幅度 +665%（2025-11）、+364%（2026-02）、+294%（2026-05）、+218%（2026-08）。注意基期極低，驚喜百分比失真，且 adjusted EPS 自 2025-11 的 0.58 高點回落至 0.40–0.45 區間。
- **公司指引（guidance）**: yfinance 未提供，DATA_UNAVAILABLE。
- **股權結構**: SoftBank 持股 30.7%（39.8M 股，2026-06-30）；Walmart 持股 11.6%（15.0M 股，2026-09-30）；Baillie Gifford 9.4%（12.2M 股，季減 0.64%）；機構持股 80.3%（559 家）；內部人持股 13.7%。SoftBank 已於 2026-05 賣出 5.59M 股，後續動向為重要觀察點。
- **放空**: short interest 17.54M 股，佔流通股（float 113.99M）31.6%，short ratio 10.8 日（資料日 2026-10-30，前月 17.69M 股）。
- **股本 / 資金**: 2025-12 季之 +424.4M 股權融資後，現金於 2026-06 仍有 1,746.4M；後續是否再融資，yfinance 未揭露 → DATA_UNAVAILABLE。

## Metrics table

單位: 金額 USD M / USD B；比率為 %、x。
「Sector median」為本報告估計值，非 yfinance 資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM（USD M） | 2,645.8 | +21.7%（FY26 Q3） | 約 5–10% 成長（估計） | 成長快於同業（估計） |
| 毛利率 TTM | 21.3%（info）/ 21.6%（季度合計） | Q3 22.3% vs 18.9%（+3.4pp） | 約 25–35% | 偏低，改善中 |
| 營業利益率 TTM | 1.2% | Q3 4.6% vs -1.6% | 約 8–12% | 偏低，轉正中 |
| 淨利率 TTM（歸屬普通股） | 0.5%（季度）/ 0.3%（info） | Q3 1.6% vs -0.7% | 約 8% | 偏低 |
| ROE | 4.4%（info） | n/a | 約 12–15% | 偏低 |
| ROIC（估算） | 約 4–5% | n/a | 約 10% | 偏低 |
| FCF 利潤率 TTM | 27.9%（季度）/ 20.7%（info） | FY25 35.1% vs FY24 -5.7% | 約 5–10% | 高，但依賴遞延收入 |
| FCF / NI | n/m | n/m | 約 1.0x | 失真，不採用 |
| 現金（USD M） | 1,746.4 | +124.6% | n/a | 充裕 |
| 淨現金（USD M） | 約 1,720.6 | n/a | n/a | 健康 |
| 流動比率 | 1.33 | 1.08 → 1.33（+0.25） | 約 1.5–2.0 | 中性 |
| 有息負債 / 普通股權益 | 3.6% | n/a | 約 30–50% | 極低，槓桿不構成風險 |
| 總負債 / 普通股權益 | 3.37x | n/a | 約 1.0–1.5x | 偏高（含遞延收入） |
| Capex / 營收 TTM | 3.7% | FY25 3.5% vs FY24 2.5% | 約 3–5% | 中性 |
| SBC / 營收 TTM | 7.8% | FY25 8.2% vs FY24 6.3% | 約 3–5% | 偏高 |
| 普通股股數（M） | 128.9 | +16.9% | n/a | 稀釋 |
| 應收 + 其他應收（USD M） | 748.4 | +100.8% | n/a | 偏高，需追蹤 |
| 遞延收入（current + non-current，USD M） | 1,736.5 | +88.1% | n/a | 正向（預收款）但集中 |
| P/E GAAP trailing | 439.8x | n/a | 約 20–30x | 無參考性 |
| P/E forward（yf） | 48.2x | n/a | 約 20–25x | 偏高 |
| P/E adjusted trailing（推算） | 約 19.1x | n/a | 約 20–25x | 接近同業 |
| EV/EBITDA | 62.3x（info）/ 約 47x（推算） | n/a | 約 12–18x | 偏高 |
| P/FCF（推算） | 約 6.2x | n/a | 約 20x | 偏低（口徑敏感） |
| P/S（推算） | 約 1.7x | n/a | 約 1.5–3x | 中性 |
| P/B | 6.4x | n/a | 約 2–4x | 偏高 |
| PEG | 4.58 | n/a | 約 1.5–2.0 | 偏高 |
| 內部人 6 個月賣出（USD M） | 289.6（含 SoftBank 281.8） | n/a | n/a | 淨賣出，大股東為主 |
| 放空 / float | 31.6%（short ratio 10.8 日） | 前月 17.69M → 17.54M 股 | 約 3–5% | 極高 |
| 分析師平均目標價（USD） | 61.50（+74.8%） | n/a | n/a | 分析師偏多 |
| Beta | 2.06 | n/a | 約 1.0–1.2 | 波動高 |
| 52 週股價變動 | -37.7% | n/a | 同期 S&P 500 +13.1%（info `SandP52WeekChange`） | 顯著落後大盤 |

## Red flags
- **GAAP 獲利接近零且 NCI 佔比大**: TTM 歸屬普通股淨利約 USD 12.7M，NCI 於 FY26 Q3 吸收 43.3M；歸屬母公司之獲利品質低。
- **營運現金流依賴遞延收入**: 遞延收入 +813.4M（YoY）幾乎等於 TTM OCF；最新季 CFO 轉負（-147.3M），應收帳款翻倍（+100.8%）。
- **FCF 口徑衝突**: 季度合計 TTM FCF 737M 與 yfinance info 548M 不一致（OCF 836M vs 894M），需以 10-Q/10-K 核對。
- **股本持續稀釋**: 股數 YoY +16.9%，SBC 占營收 7.8%；2025-12 季有 USD 424.4M 股權融資。
- **市值與股數資料異常**: yfinance `marketCap` USD 21.3B 依賴 605.4M 隱含股數，與 129.9M 基本股數相差 4.7 倍。若誤用，所有市值相關估值（P/S、EV 等）將失真。
- **EPS 口徑混用**: earnings_dates 的 Reported EPS（adjusted，最近季 0.41）與 income statement 的 diluted EPS（GAAP，最近季 0.09）差距大；`epsCurrentYear` 0.57 與已公布 adjusted EPS 合計不一致。
- **非營業收入撐高 Q3 獲利**: 其他非營業收入 30.6M 與股權法損失 -9.6M 合計約 21M，占 Q3 稅前利益 63.5M 之三分之一。
- **大股東與內部人賣出**: SoftBank 於 2026-05 單筆賣出 USD 281.8M（5.59M 股）；高管於 2026-10-27 集中以 USD 38–39 賣出。
- **放空比率極高**: float 31.6%、short ratio 10.8 日，且股價低於 50 與 200 日均線。
- **股價趨勢弱**: 52 週跌幅 -37.7%，現價僅高於 52 週低點 6.1%，beta 2.06。
- **資料缺口**: 分部營收、公司指引、回購細節、債務明細、2026-06 季 debt 行項、內部人無文字交易之性質，yfinance 皆未提供（DATA_UNAVAILABLE）。
- **資料時點**: 最新財報為 2026-06-30 季；FY26 Q4 尚未公布。cache 報價時點為 2026-11-12，早於 as-of 日期 2026-11-13，無 post-date 資料使用。

FUNDAMENTALS REPORT COMPLETE
