# Fundamentals — MRVL as of 2026-11-16

## Executive summary
Marvell (MRVL, NasdaqGS) 的財務體質在 FY26 明顯改善：TTM 營收 9.45B USD（+36.6% YoY，以最新季 2026-07 計），GAAP 營業利益率回升至約 16.8%，TTM FCF 1.72B USD（FCF 利潤率 18.2%），淨負債比 EV 很低（淨負債 1.03B USD，流動比率 3.17）。估值面，以 GAAP trailing P/E 51.6x、EV/EBITDA（去除 2025-10 季一次性利益）約 48.8x、P/FCF 約 80x 來看偏貴；以分析師 non-GAAP forward P/E 21.3x 計則相對便宜，但 trailing 與 forward 口徑不同，需分開看。股價 156.76 USD 較 52 週高點 329.88 USD 回落 52.5%，且低於 50 日均線 (229.2) 與 200 日均線 (187.0)，6 個月內 Insider 僅見公開市場賣出、無買進。

## Revenue & profitability
資料基準：USD，yfinance 年報為 FY（財年截至每年 1 月底），FY26 = 截至 2026-01-31。

**營收趨勢（USD B）**

| 期間 | 營收 | YoY |
|---|---|---|
| FY23 | 5.92 | n/a |
| FY24 | 5.51 | -6.96% |
| FY25 | 5.77 | +4.71% |
| FY26 | 8.19 | +42.09% |

- 3 年 CAGR（FY23→FY26）= 11.4%。yfinance 年報無 FY22 資料，無法計算 4-5 年 CAGR，標示 DATA_UNAVAILABLE。
- 季度 (USD B)：2025-07 季 2.01、2025-10 季 2.07、2026-01 季 2.22、2026-04 季 2.42、2026-07 季 2.74。最新季 YoY +36.6%（對 2025-07 季），QoQ +13.3%。
- TTM 營收 9.45B USD 與 info.totalRevenue 9,450.3M 吻合（四季加總交叉驗證通過）。
- 分部（segment）營收：yfinance 與 longBusinessSummary 只描述產品線（ethernet、custom ASIC、interconnect/光學 DSP、storage 等）並以 data center、communications 為主要市場，未提供分部營收金額，標示 DATA_UNAVAILABLE。

**獲利能力**

| 指標 | FY23 | FY24 | FY25 | FY26 | TTM (至 2026-07) |
|---|---|---|---|---|---|
| 毛利率 | 50.5% | 41.6% | 41.3% | 51.0% | 52.2%（info.grossMargins） |
| 營業利益率 | 6.1% | -7.9% | -6.4% | 16.3% | 16.8% |
| 淨利率 (GAAP) | -2.8% | -16.9% | -15.3% | 32.6% | 27.9%（含一次性利益，見下） |

- 毛利率由 FY25 的 41% 回升到 FY26 的 51%，最新季 (2026-07) 達 53.1%，為連續改善。
- **一次性項目**：2025-10 季 NI 1,901.3M USD、EBIT 2,266.6M USD，但同季營業利益僅 367.4M USD；差額約 1.9B 被 yfinance 歸為 Net Interest Income（1,908.8M 利息收入）。此差額疑為資產出售等非經常性收益，yfinance 的 Total Unusual Items 僅 -9.6M，未正確標示，需以 10-K/10-Q 核對。
- 剔除 2025-10 季後 TTM NI 約 738.6M USD，淨利率約 7.8%。GAAP 淨利率 (ex-gain) 偏低，主因利息支出升高（2026-04 季利息費用 256.1M USD）與 SBC 高（TTM SBC 828.9M USD，佔營收 8.8%）。
- ROE：info.returnOnEquity 16.5%（含一次性利益）；剔除一次性利益後約 4.5%（738.6M / 平均股東權益約 16.4B USD，為估算）。
- ROIC：以 TTM 營業利益 1,588.3M USD × (1 − 15% 假設稅率) / 最新投入資本 23,494.5M USD ≈ 5.7%（估算，稅率為假設）。ROIC 仍低於一般半導體龍頭水準，主因商譽佔總資產 49.6%（11.06B / 22.29B）。
- EPS：FY26 diluted EPS 3.07 USD（與 NI 2,670.1M ÷ diluted shares 869.7M 相符）；TTM GAAP EPS 3.04 USD。最近季 non-GAAP EPS 0.94（2026-08-27 發布，EPS 估計 0.93，超出 0.99%）。

## Cashflow & balance sheet
**現金流（USD B）**

| 期間 | OCF | Capex | FCF | FCF 利潤率 | FCF / NI |
|---|---|---|---|---|---|
| FY23 | 1.29 | 0.22 | 1.07 | 18.1% | n/m |
| FY24 | 1.37 | 0.35 | 1.02 | 18.5% | n/m (NI 為負) |
| FY25 | 1.68 | 0.29 | 1.39 | 24.1% | n/m (NI 為負) |
| FY26 | 1.75 | 0.36 | 1.39 | 17.0% | 0.52（NI 含一次性利益，虛高） |
| TTM | 2.20 | 0.48 | 1.72 | 18.2% | 0.65（剔除一次性利益後 FCF/NI ≈ 2.3） |

- FCF 品質：TTM FCF 1.72B 由 OCF 2.20B（與 info.operatingCashflow 2,200.3M 吻合）減 capex 0.48B 計算。info.freeCashflow 為 2.41B，與此不同，本報告以計算值為準，差異需核對。
- FCF/NI > 0.9 的健康門檻：以 GAAP NI 直接比較被一次性利益扭曲；以 FCF 減 SBC 計算，TTM 為 0.89B USD（9.5% 營收），此口徑較保守，屬真實股東經濟利益的參考。
- 季度 capex 上升：2026-07 季 131.2M USD，對比 2025-07 季 48.6M USD，為 AI 基礎建設/產能擴張訊號，需後續確認。

**資產負債表（USD B）**

| 項目 | 2026-01 (FY26 末) | 2026-07 (最新季) |
|---|---|---|
| 現金及約當現金 | 2.64 | 3.93 |
| 總負債（有息） | 4.79 | 5.29 |
| 淨負債 | 1.83 | 1.03 |
| 股東權益 | 14.31 | 18.53 |
| 流動比率 | 2.00（6.46/3.22） | 3.17（info） |
| 速動比率 | n/a | 2.46（info） |
| D/E（有息負債/權益） | 0.33 | 0.29 |
| 淨負債/EBITDA（TTM，clean EBITDA 2.85B） | n/a | 0.36x |

- 利息覆蓋：TTM 營業利益 1,588.3M / TTM 利息費用 439.5M ≈ 3.6x；2026-04 季利息費用 256.1M 為異常高點，需核對是否為一次性（如提前還債成本）。
- 2026-04 季資本結構變化：yfinance 顯示 2.0B USD 股權發行（"Issuance Of Capital Stock"，同時標示為 "Preferred Stock Issuance"）及 0.999B USD 債務發行，但資產負債表 Preferred Stock = 0，標籤不一致，需核對 10-Q。
- 有形帳面價值由 -1.27B（2025-01）轉為 +2.05B（2026-07），改善明顯。

## Capital allocation & insider signal
**資本配置**
- 回購：FY23 0.12B → FY24 0.15B → FY25 0.73B → FY26 2.04B USD（FY26 回購 = FCF 的 1.47 倍，以舉債與 FCF 支應）。2025-10 季單季回購 1.30B USD。
- 股數：2026-01 847.3M → 2026-07 898.6M，半年增加 6.1%。在大量回購後股數反而上升，主要因 2026-04 季約 2.0B USD 股權發行。淨稀釋為重要紅旗。
- 股利：年化 dividendRate 0.24 USD（每季 0.06），殖利率 0.15%；FY26 股利支出 205.1M USD，FCF 覆蓋 6.8x；payoutRatio 7.9%。股利佔比極低，對股東回報影響有限。
- Capex：FY23-FY26 佔營收 3.7% / 6.4% / 5.1% / 4.4%；FY26 Capex 358.6M USD。
- SBC：FY26 590.8M USD（佔營收 7.2%），是 GAAP 獲利與 FCF 之間的主要差距。

**Insider 活動（最近 6 個月，2026-05-16 至 2026-11-16）**
- 公開市場賣出（"Sale at price"）合計 83,494 股，揭露金額約 18.88M USD；買進 0 股。
- 佔市值比：18.88M / 市值 137.6B（以最新價計算）= 0.014%，規模極小。
- 賣出價格區間 180.50–299.13 USD，目前股價 156.76 USD 已低於所有賣出價。
- 主要賣出人：CEO Matthew Murphy（多筆 7,500 股，2026-06 至 2026-09）；President Christopher Koopmans（固定 10,000 股，2026-07-01 / 08-03 / 09-01 / 11-02，呈近似每月排程特徵）；Sandeep Bharathi（2026-06-16、07-16）；CFO Daniel Durn（2026-06-23 賣 2,250 股）。
- 另有約 24.5 萬股無金額紀錄（多為 RSU 歸屬、扣繳、贈與或獎勵，yfinance 未標示性質），非公開市場賣出，需以 Form 4 核對。
- Insider 持股比例 1.2%（heldPercentInsiders）。
- 解讀：絕對金額小且有排程特徵，但在股價由 300 附近跌至 157 的期間仍持續賣出，無任何公開市場買進，訊號偏中性至偏負面。

## Valuation
以最新價 156.76 USD、流通股 877.99M 股計算（市值 137.63B USD，EV 138.99B USD）。注意 info.marketCap 141.05B USD 等於以 ask 160.65 USD 計算，為舊價格，本報告以 156.76 為準。

| 倍數 | 數值 | 計算基礎 |
|---|---|---|
| Trailing P/E (GAAP) | 51.6x | 156.76 / TTM EPS 3.04 |
| Forward P/E | 21.3x | 156.76 / forwardEps 7.35（分析師 non-GAAP 一致預期） |
| EV/EBITDA | 約 48.8x | EV 138.99B / clean EBITDA 2.85B（剔除 2025-10 季一次性利益）；yfinance 原始 EBITDA 含一次性利益為 4.76B，倍數約 29x，不具可比性 |
| P/FCF | 約 79.9x | 137.63B / TTM FCF 1.72B；以 info.freeCashflow 2.41B 計約 57x |
| P/S | 約 14.6x | 137.63B / TTM 營收 9.45B |
| P/B | 7.4x | 156.76 / bookValue 21.135 |
| PEG | 0.39 | info.pegRatio |

**與產業比較（估計，非 yfinance 資料）**：半導體產業中位數估計 forward P/E 約 25–35x、EV/EBITDA 約 20–30x、P/S 約 6–10x。MRVL trailing 倍數明顯高於產業估計，forward P/E 接近或略低於產業中位數，顯示市場以 AI 資料中心成長預期定價，對 GAAP 獲利的依賴低。

**分析師共識**：40 位分析師，平均評等 1.40（Strong Buy）；目標價平均 310.32 USD、中位數 300 USD、最高 450 USD、最低 175 USD。目標均價較現價高約 98%，最低目標價也高於現價 11.6%。此為分析師觀點，不代表本報告結論。

**價格位置**：現價位於 52 週區間 70.69–329.88 USD 的 33% 位置；較 52 週高點回落 52.5%；52 週漲幅 +87.8%（S&P 500 同期 +13.3%）；beta 2.33。

## Key catalysts
- **下次財報**：2026-12-01（yfinance 收盤後時間，isEarningsDateEstimate = False；在本報告 as-of 日期之後）。下季 non-GAAP EPS 一致預期 1.10 USD（對比最近季實際 0.94，QoQ +17%）。
- 由 yfinance epsCurrentYear 4.22 USD 反推，FY27 (截至 2027-01) Q4 隱含一致預期約 1.38 USD（推算值，非直接資料）。
- **管理層指引**：yfinance 不提供 guidance 文字，標示 DATA_UNAVAILABLE。需參考 2026-08-27 財報稿。
- **除息日**：ex-dividend 2026-10-09 已過，下次股利約 0.06 USD/股，為日後派發資訊。
- **產品/分部轉變**：yfinance 未提供分部營收，無法量化資料中心 vs. 通訊的占比變化；產品線描述包含 co-packaged optics、coherent DSP、Ultra Accelerator Link switch 等 AI 相關產品，屬定性催化劑。
- **股權與負債**：2026-04 季股權與債務發行後，後續 10-Q 對稀釋、利息支出與一次性項目的說明為關注重點。
- **空頭**：short interest 26.09M 股，佔流通股 2.9%，佔浮動股 3.48%，short ratio 1.18 日；較前月 24.05M 股增加。

## Metrics table
單位：營收 / 利潤 / 市值 / FCF 以 USD B 計；比率以 % 或 x 計。Sector median 欄位為估計值，非 yfinance 資料。

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 TTM (USD B) | 9.45 | +36.6% (最新季) | n/a | 高成長，強 |
| 毛利率 (最新季) | 53.1% | +2.7 pts (2025-07 季 50.4%) | 約 55–65% | 略低於產業中位數，但持續改善 |
| 營業利益率 (TTM) | 16.8% | 由 FY25 -6.4% 轉正 | 約 15–25% | 中性 |
| 淨利率 (TTM, ex-Oct25 一次性) | 7.8% | n/a | 約 15–20% | 偏弱 |
| ROE (info, 含一次性) | 16.5% | n/a | 約 15–20% | 數字受一次性扭曲 |
| ROIC (估算) | 5.7% | n/a | 約 10–15% | 偏弱，商譽佔比高 |
| FCF 利潤率 (TTM) | 18.2% | FY26 17.0% | 約 20–30% | 中性 |
| FCF / NI (TTM) | 0.65（ex-gain 約 2.3） | n/a | > 0.9 | 受一次性扭曲，需以 ex-gain 解讀 |
| FCF − SBC 利潤率 (TTM) | 9.5% | n/a | n/a | 偏弱，SBC 偏高 |
| 淨負債 (USD B) | 1.03 | 2026-01 為 1.83 | n/a | 健康 |
| 流動比率 | 3.17 | 2026-01 為 2.00 | 約 2–3 | 健康 |
| D/E | 0.29x | 2026-01 為 0.33x | 約 0.2–0.5x | 健康 |
| 淨負債/EBITDA (clean) | 0.36x | n/a | 約 0.5–1.5x | 健康 |
| 利息覆蓋 (TTM) | 3.6x | n/a | 約 8–15x | 偏弱，2026-04 季利息高 |
| 股數 (M 股) | 898.6 (2026-07) | +6.1% vs 2026-01 | n/a | 稀釋，負面 |
| 回購 FY26 (USD B) | 2.04 | +181% vs FY25 | n/a | 規模大，但超過 FCF |
| 股利殖利率 | 0.15% | n/a | 約 0.5–1% | 極低，非主要回報來源 |
| Capex / 營收 (FY26) | 4.4% | FY25 5.1% | 約 5–10% | 中性 |
| Trailing P/E | 51.6x | n/a | 約 35–45x | 偏貴 |
| Forward P/E | 21.3x | n/a | 約 25–35x | 略便宜 (non-GAAP 口徑) |
| EV/EBITDA (clean) | 約 48.8x | n/a | 約 20–30x | 偏貴 |
| P/FCF | 約 79.9x | n/a | 約 25–40x | 偏貴 |
| P/S | 約 14.6x | n/a | 約 6–10x | 偏貴 |
| Insider 淨買賣 (6mo) | 淨賣出 83,494 股 / 約 18.9M USD | n/a | n/a | 中性偏負 |
| 分析師平均目標價 | 310.32 USD（+98%） | n/a | n/a | 共識極度正向 |
| Beta | 2.33 | n/a | 約 1.2–1.5 | 高波動 |
| 空單佔流通股 | 2.9% (佔浮動股 3.5%) | 較前月增加 | 約 2–4% | 中性 |

## Red flags
- **估值**：GAAP trailing P/E 51.6x、EV/EBITDA（clean）約 48.8x、P/FCF 約 80x，對 GAAP 獲利與現金流的隱含預期極高；forward 倍數依賴 non-GAAP 一致預期。
- **一次性收益扭曲**：2025-10 季約 1.9B USD 收益被 yfinance 歸類為利息收入，使 FY26 淨利與 ROE 嚴重失真；需以 10-K/10-Q 核實性質與金額。
- **股權稀釋**：2026-01 至 2026-07 股數增加 6.1%（847.3M → 898.6M），儘管 FY26 回購 2.04B USD；2026-04 季 2.0B USD 股權發行，標籤與資產負債表不一致。
- **利息支出**：2026-04 季利息費用 256.1M USD，TTM 利息覆蓋 3.6x，低於一般投資級半導體公司水準。
- **SBC 偏高**：TTM SBC 828.9M USD（8.8% 營收），FCF − SBC 利潤率僅 9.5%。
- **股價趨勢**：現價 156.76 較 50 日均線低 31.6%、較 200 日均線低 16.2%，較 52 週高點回落 52.5%；2026-11-13 單日 -4.68%（regularMarketChange），盤後 152.59 USD 再跌 2.66%。
- **Insider 持續賣出**：6 個月內 CEO、President、CFO、多位 officer 皆有公開市場賣出，無買進；Koopmans 固定股數賣出呈排程特徵。
- **治理風險分數偏高**：yfinance overallRisk 9、compensationRisk 10、boardRisk 8（1–10 分，越高越差）。
- **資料品質提醒**（見下方）。

## 資料品質與限制
- **資料時點**：報告 as-of 2026-11-16；yfinance 最新價為 2026-11-13 收盤（regularMarketTime 2026-11-13 21:00 UTC），資料快取時間 2026-11-15 13:50–13:55 UTC。2026-11-16 交易日資料不在本次資料內。下次財報 2026-12-01 在 as-of 之後。
- **身分與單位交叉驗證**：Ticker MRVL、NasdaqGS、Wilmington DE、7,480 名員工，與 longBusinessSummary 一致。yfinance prevName 為 "Marvell Technology Group Ltd."，nameChangeDate 為 2026-11-15，屬欄位異常，未影響本次分析。單位為 USD（financialCurrency USD）；TTM 營收、NI、EPS × 股數（3.07 × 869.7M ≈ 2.67B）交叉驗證通過。
- **yfinance 欄位不一致**：
  - info.marketCap 141.05B USD 對應 ask 160.65，非最新價；本報告以 137.63B USD 為準。
  - fast_info 的 market_cap、shares、ten_day_average_volume 皆為 null；fast_info 價格來自 cnyes 快取，與 info 一致。
  - 單日漲跌欄位不一致：regularMarketChangePercent -4.68% 與 fulldayChangePercent -7.21% 不同，本報告引用前者。
  - info.freeCashflow 2.41B 與 OCF − capex 1.72B 不同。
  - info.ebitda 2.85B 與季度 EBITDA 加總 4.76B 不同（前者剔除一次性利益）。
  - info.priceToSalesTrailing12Months 14.9x 與本報告以最新市值計算的 14.6x 略有差異。
- **DATA_UNAVAILABLE**：分部營收、管理層指引、FY22 以前歷史資料、4–5 年 CAGR、sector median（yfinance 無提供，本表為估計）、10-K/10-Q 原文核對。
- **yfinance 連線**：Cookie/crumb 取得失敗（ConnectionError），但回傳資料通過上述交叉驗證，未觀察到 routing 錯誤。未使用 repo 快取做額外比對（無必要：身分與單位已一致）。

FUNDAMENTALS REPORT COMPLETE
