# Fundamentals — SYM (Symbotic Inc.) as of 2026-10-09

註: 資料截至 2026-10-08 盤後快取報價 (cnyes cache 13:15 UTC) 及最新已揭露季度 2026-06-30 (FY26 Q3)。未發現晚於 DATE 的財報或價格資料。yfinance 將公司歸為 Industrials / Specialty Industrial Machinery (任務描述為 robotics, 以 yfinance 分類與公司簡介為準: 倉儲自動化)。
數據品質警示: yfinance `marketCap` (26.2B) 與 `impliedSharesOutstanding` (605M) 明顯不一致, 實際流通股約 129.9M, 市值以 ~5.6B 計算 (`nonDilutedMarketCap` 5.67B 與 EV 4.33B 相符)。下文 P/S、P/FCF 已以 ~5.6B 重算, 並標註 yfinance 原值。

## Executive summary
SYM 財務健康度的核心在於流動性與負債端無虞 (總負債僅 25.8M, 現金 1,746M, 淨現金約 1.72B), 營收成長快 (FY25 +25.7%, TTM 季度營收 +21.7% YoY) 且毛利率與營業利益由負轉正, 但 GAAP 獲利極薄 (TTM 歸屬普通股淨利約 8–13M), FCF 高度依賴客戶預收款 (Jun-26 季 FCF -164.6M), 且 2026 年內股本增加約 14.5%。估值在任何盈餘口徑下都屬極度昂貴 (trailing P/E 541x, forward P/E 56x, EV/EBITDA 58–77x), 只有以 TTM FCF 計算的 P/FCF ~7.6x 看似便宜, 但該 FCF 的可持續性存疑。

## Revenue & profitability

**營收與成長**
- FY 營收 (9 月結): FY22 593.3M → FY23 1,176.9M (+98.4%) → FY24 1,788.2M (+51.9%) → FY25 2,246.9M (+25.7%)。FY22–FY25 三年 CAGR 約 55.9%, 但成長動能明顯放緩 (+98% → +52% → +26%)。
- 季度營收: 2025-06 592.1M / 2025-09 618.5M / 2025-12 630.0M / 2026-03 676.5M / 2026-06 720.8M。Jun-26 季 YoY +21.7%, 連續五季成長。
- TTM 營收 2,645.8M (與 yfinance `totalRevenue` 一致)。
- 分部營收 (segment mix): yfinance `longBusinessSummary` 未提供分部資料, n/a。客戶集中度 (如 Walmart 關係) 無法從 yfinance 直接確認, 需另查 10-K。

**獲利能力 (margin 趨勢)**
- 毛利率 (年): FY22 16.8% → FY23 16.1% → FY24 13.7% → FY25 18.8%。
- 毛利率 (季): Jun-25 18.9% → Sep-25 20.6% → Dec-25 21.2% → Mar-26 22.2% → Jun-26 22.3%, 呈持續擴張。
- 營業利益率 (年): FY22 -23.7% → FY23 -19.0% → FY24 -6.5% → FY25 -4.1% (EBIT -92.1M)。
- 營業利益率 (季): Jun-25 -1.6% → Sep-25 -2.5% → Dec-25 +1.5% → Mar-26 +0.9% → Jun-26 +4.6% (EBIT 32.9M), 近兩季轉正。
- 淨利率: FY25 歸屬普通股淨利 -16.9M (-0.75%)。TTM 歸屬普通股淨利 8.2M (yfinance `netIncomeToCommon`, 淨利率 0.31%); 以季度加總為 12.6M, 兩者有小差異。
- 非控制權益 (NCI) 影響顯著: FY25 NCI 占用 74.1M, Jun-26 季 NCI 為 -43.3M (即 NCI 分得部分損失/獲利的結構性拉扯)。歸屬母公司的獲利遠低於總體獲利, 需於 10-K 釐清合併結構。
- ROE: TTM 淨利 8.2M / 期末普通股權益 708.8M ≈ 1.2% (自行計算)。FY25 ROE 為負 (-16.9 / 221.3 ≈ -7.6%, 期末權益口徑)。
- ROIC: n/m。淨現金加上龐大 NCI 使投入資本為負, 以 TTM EBIT 33M 計的 NOPAT 相對權益僅約 4–5%, 不具參考價值。
- 研發: FY25 R&D 216.0M (占營收 9.6%); Jun-26 季 R&D 43.8M (占營收 6.1%), 研發費用率下降。

## Cashflow & balance sheet

**現金流品質**
- FY 營運現金流: FY22 -148.2M / FY23 230.8M / FY24 -58.1M / FY25 866.9M。FY25 FCF 787.9M (FCF margin 35.1%), 但 FY22/FY24 為負, 波動極大。
- FY25 FCF 的主要來源是 Change in Working Capital +714.0M, 即預收款 (current deferred revenue 1,242M) 增加。
- TTM (2025-09 至 2026-06 四季加總): OCF 836.2M, Capex -99.0M, FCF 737.3M, FCF margin 27.9%。
- Jun-26 季: OCF -147.3M, WC 變動 -252.6M, FCF -164.6M。當季現金流顯著反轉。
- FCF / NI 比率: FY25 因 NI 為負 n/m; TTM FCF/NI ≈ 58x (以 12.6M 計), 遠超過 0.9 的健康門檻, 但這反映的是 NI 過低而非 FCF 品質高。
- SBC 占比高: FY25 SBC 183.9M (占營收 8.2%); TTM SBC 207.2M (占 7.8%)。扣除 SBC 後 TTM FCF 約 530M。
- 結論: FCF 品質為中低, 高度依賴客戶預收款與 WC 時序, 不應外推為穩定自由現金流。

**資產負債表 (2026-06-30)**
- 現金及約當現金 1,746.4M (較 2025-09-30 的 1,245.0M 增加 40%; 較 2025-06-30 的 777.6M 增加 125%)。
- 總負債 (有息) 約 25.8M (yfinance `totalDebt`)。淨現金 ≈ 1,720.6M, 約占市值 31%。
- 總負債 2,390.2M, 其中遞延收入 (current 1,553.7M + non-current 182.8M) 約 1,736.5M, 占總負債約 73%。負債主要為經營性預收款, 非金融負債。
- 流動比率 1.331 (流動資產 2,857.8M / 流動負債 2,147.1M); 速動比率 1.162 (yfinance)。
- 營運資金 710.7M (2025-09 為 160.9M)。
- 應收帳款 (應收 accounts receivable) 288.5M (Jun-26), 較 Mar-26 132.6M 大增, 需留意收款與帳期。存貨 220.8M (Jun-26), 較 2025-06 138.9M 上升 59%。
- debt/equity: yfinance `debtToEquity` 2.278 (應為百分比口徑, 即 2.28%, = 25.8M / 總權益含 NCI 1,134.0M), 財務槓桿極低。
- 每股帳面價值 5.40; P/B ~8.0x。
- 商譽 59.9M (2025-06 起), 2025 年有收購 (FY25 Purchase of Business -141.8M; Jun-26 季 -20.2M)。

## Capital allocation & insider signal

**資本配置**
- 資本支出: FY22 17.9M / FY23 21.3M / FY24 44.4M / FY25 79.0M (占營收 3.5%, 為 FY25 D&A 44.1M 的 1.8 倍); TTM 99.0M (占 3.7%)。擴產投資加速。
- 股利: 無 (dividendYield 0)。回購: 無 (現金流量表無 repurchase 科目)。
- 股本稀釋: 普通股 2025-09-30 112.6M → 2026-06-30 128.9M (+14.5%, 9 個月)。Dec-25 季股票發行 424.4M, APIC 由 1,564.8M 增至 2,029.0M。Jun-26 季稀釋後加權股數 133.3M (YoY +22%)。
- 資本配置邏輯: 以股權融資 + 客戶預收款支撐成長, 而非內生 FCF。FY25 同時支付 141.8M 收購與 129.9M 投資 (淨購入)。
- 股息覆蓋率: n/a (無股息)。

**內部人與大股東 (過去 6 個月 2026-04-09 至 2026-10-08)**
- 共 28 筆公開市場賣出, 合計 5.82M 股、約 293.4M USD。其中:
  - SoftBank Group (Beneficial Owner) 2026-05-27 賣出 5.59M 股, 約 281.8M USD (均價 50.42)。占總賣出金額 96%。
  - 扣除 SoftBank 後, 內部人賣出約 11.6M USD (230.8K 股), 占市值 (~5.67B) 約 0.20%。主要賣方: 董事 Todd Krasnow 約 3.49M USD, CTO Kuffner 約 2.31M USD, 高階主管 Brian Alexander 約 2.64M USD, Boyd 約 1.15M USD, CFO Izilda Martins 約 1.12M USD (2026-07-27, 27,463 股, 均價 40.80)。
- 買入: 6 個月內 0 筆公開市場買入。
- 無償/ 稅務扣繳/ 授予類 (no-price 或 Award/Gift) 13 筆, 不計入上述賣出。
- 賣出價格走勢: 2026-04/05 多在 52–60 美元; 2026-07 至 10 月多在 39–45 美元, 內部人在股價下跌後仍持續賣出。
- 10b5-1 計畫與否: yfinance 資料未提供, n/a。
- 持股結構: 內部人 13.6%, 機構 79.4% (551 家), SoftBank 30.7% (39.8M 股, 2026-06-30), Walmart 11.6% (15.0M 股), Baillie Gifford 9.4%。
- SoftBank 仍持有 30.7%, 即使已大量出售, 其後續減持仍為籌碼壓力來源。
- 做空: shares short 17.6M (前月 15.8M, +11.7%), 占流通股 (float 114.0M) 31.7%, short ratio 11.2 天。高空單比例放大波動。

## Valuation

| 指標 | yfinance 原值 | 自行重算 (市值 ~5.6B) | 說明 |
|---|---|---|---|
| Trailing P/E | 541.4x | 541x | 價格 43.31 / TTM EPS 0.08 (GAAP) |
| Forward P/E | 56.1x | 56x | 價格 / forward EPS 0.7716 (調整後口徑) |
| PEG | 5.45 | — | 高估的成長溢價 |
| P/S (TTM) | 9.9x | ~2.1x | yfinance 使用 26.2B 錯誤市值 |
| P/B | 8.0x | ~8.0x | 股價 / 每股帳面價值 5.40 |
| EV/Revenue | 1.64x | ~1.6x | EV 4,329M / TTM 營收 2,646M |
| EV/EBITDA | 76.6x | 58x (季度加總 EBITDA 74.2M) | yfinance TTM EBITDA 56.5M 與季度加總 74.2M 不一致 |
| P/FCF (TTM) | n/a | ~7.6x | 市值 5.6B / TTM FCF 737M; FCF 收益率 ~13% |

- 估值判讀: 盈餘口徑 (P/E, EV/EBITDA) 極度昂貴; 現金流口徑 (P/FCF) 看似便宜, 但 FCF 含大量 WC 預收款與 SBC 之前的現金, 扣除 SBC 後約 530M 對應 P/FCF ~10.6x。
- 分析師目標價: 14 位, 平均 62.86, 中位數 67.5, 最高 85.0, 最低 38.0。平均目標較現價 +45%。recommendationKey = "none"。
- 股價位置: 現價 43.31 (2026-10-08 收盤附近, 日內 -1.36%), 52 週區間 37.68–87.88 (較高點 -51%), 52 週漲跌 -35.5%, 50 日均 42.23, 200 日均 50.21 (現價位於 200 日均線下方)。beta 1.97。
- 與 sector median 比較 (估計, 非 yfinance 資料): Industrials / 機械類 trailing P/E ~25–30x, forward P/E ~20x, EV/EBITDA ~14–18x, P/S ~2–3x, P/FCF ~20x。

## Key catalysts
- 下次財報: 2026-11-16 (yfinance; 日期可能為估計), 預估 EPS 0.16 (調整後口徑)。依 fiscal year 結束於 2026-09 底 (nextFiscalYearEnd epoch 1790467200) 推測為 FY26 Q4 與全年財報。
- 上次財報: 2026-08-05 (FY26 Q3), 調整後 EPS 0.41 vs 預估 0.13 (surprise +218.5%)。GAAP 稀釋 EPS 為 0.09, 兩者口徑不同 (yfinance `Reported EPS` 為調整後, 需以 earnings release 核對)。
- 過去 8 季 EPS surprise 全部為正 (範圍 +7.7% 至 +901%), 歷史超預期慣性強, 但多為低基數效應。
- 指引 (guidance): yfinance 未提供, n/a。需查 2026-08-05 earnings release 與 8-K。
- 分部與訂單 (segment shifts / backlog): n/a。
- 潛在壓力事件: SoftBank 持股 30.7% 的後續減持; 做空比例 31.7%; 股本稀釋 (2025-12 季發行 424M)。
- 財報 2026-11-16 前的 FY26 年底現金流與 WC 變化是關鍵觀察點 (Jun-26 季 WC 逆轉)。

## Metrics table
| Metric | Latest | YoY | Sector median (估計) | Verdict |
|---|---|---|---|---|
| 營收 (TTM) | 2,645.8M (Jun-26 季 720.8M) | Jun-26 季 +21.7%; FY25 +25.7% | 成長 ~5–10% | 成長強, 但減速 |
| 毛利率 (Jun-26 季) | 22.3% | +3.4pp (18.9%) | 25–30% | 偏低但持續改善 |
| 營業利益率 (Jun-26 季) | 4.6% | 由 -1.6% 轉正 | ~8–10% | 轉正初期, 低於同業 |
| 淨利率 (TTM, 歸屬普通股) | 0.3% | n/m | ~6–8% | 偏弱 |
| ROE (TTM) | ~1.2% | FY25 為負 | ~10–12% | 弱 |
| ROIC | n/m | n/m | ~8–10% | 無法有意義評估 |
| OCF (TTM) | 836.2M | FY25 866.9M (vs FY24 -58.1M) | — | 高但波動大 |
| FCF (TTM) | 737.3M | FY25 787.9M | — | 高, 依賴 WC |
| FCF margin (TTM) | 27.9% | FY25 35.1% | ~5–10% | 數字亮眼, 品質存疑 |
| FCF / NI | n/m (NI 過小) | — | >0.9 健康 | 無法判讀 |
| SBC / 營收 (TTM) | 7.8% | FY25 8.2% | ~2–3% | 偏高, 稀釋 |
| 淨現金 | 約 1,720.6M | 現金 YoY +125% (Jun-25 777.6M) | — | 強 |
| 流動比率 | 1.33 | — | ~1.5–2.0 | 尚可 |
| 負債權益比 (有息負債/總權益) | ~2.3% (yfinance 2.278 為百分比口徑) | — | ~30–60% | 極低 |
| 普通股股數 | 128.9M | +16.9% YoY (110.3M) | — | 稀釋明顯 |
| Capex / 營收 (FY25) | 3.5% | FY25 Capex +78% | 3–5% | 正常, 擴產中 |
| 內部人賣出 (6 個月, 扣除 SoftBank) | ~11.6M USD (0.20% 市值) | — | — | 規模小 |
| SoftBank 賣出 (6 個月) | 281.8M USD (5.59M 股) | 2025-12 另售 3.5M 股 | — | 大股東減持壓力 |
| Trailing P/E | 541x | — | ~25–30x | 極度昂貴 |
| Forward P/E | 56x | — | ~20x | 昂貴 |
| EV/EBITDA | 58–77x | — | ~14–18x | 昂貴 |
| P/S (TTM) | ~2.1x (yfinance 9.9x 錯誤) | — | ~2–3x | 略低於估計中位 |
| P/FCF (TTM) | ~7.6x | — | ~20x | 表面便宜, 需扣 WC/SBC |
| Short interest / float | 31.7% | 空單 +11.7% MoM | <5% | 極高 |
| Beta | 1.97 | — | ~1.0 | 高波動 |

## Red flags
- 估值極端: trailing P/E 541x, forward P/E 56x, PEG 5.45。若成長放緩, 估值壓縮風險大。
- GAAP 獲利薄弱: TTM 歸屬普通股淨利僅 8–13M, 且 NCI 大幅吸收合併損益, 母公司獲利能力遠低於總體。
- FCF 品質低: 2026-06 季 FCF -164.6M、WC 變動 -252.6M; 全年 FCF 高度依賴客戶預收款 (遞延收入 1,736M)。
- 股本稀釋: 2025-09 至 2026-06 普通股 +14.5%, Dec-25 季發行 424M; 稀釋後加權股數 YoY +22%。
- 大股東減持: SoftBank 2026-05 單筆賣出 281.8M USD, 仍持 30.7%。
- 內部人持續賣出: 6 個月內 28 筆賣出, 股價跌至 40 美元區間仍在賣出, 無公開市場買入。
- 高空單: 空單占流通股 31.7%, short ratio 11.2 天, 股價波動與擠壓風險並存。
- 技術面: 現價低於 200 日均 (50.21); 52 週跌幅 -35.5%; beta 1.97。
- 數據品質: yfinance 市值 (26.2B) 與股數 (605M implied) 錯誤; TTM EBITDA (56.5M) 與季度加總 (74.2M) 不一致; EPS 調整後與 GAAP 口徑混用; fast_info 因 Yahoo 403 改由 cnyes 快取取得, 部分欄位 (50/200 日均、市值) 為 null, 本報告 MA 改採 info 欄位。
- 資訊缺口: 指引 (guidance)、分部資料、客戶集中度、合約積壓 (backlog)、10b5-1 計畫、NCI 結構說明 均為 n/a, 需補查 10-K / 10-Q / earnings release。

FUNDAMENTALS REPORT COMPLETE
