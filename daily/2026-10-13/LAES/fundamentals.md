# Fundamentals — LAES (SEALSQ Corp) as of 2026-10-13

## Executive summary
SEALSQ 財務體質以現金為主: 2026-06-30 現金及短期投資約 482.2M USD、總負債僅約 7.1M USD，市值約 457.7M USD 低於現金水位（P/B 約 0.85x，股價 2.03 USD 約等於每股現金 2.09 USD）。然而獲利結構極差，FY2025 營業利益率約 -218%、FCF 約 -32.5M USD，前瞻 EPS (-0.27) 比追溯 EPS (-0.20) 更差，且 2025 年股本由 101.5M 股暴增至 193.0M 股，2026 年中已達 224.9M 股，稀釋壓力明顯。估值層面無法以 P/E、EV/EBITDA 衡量（盈餘與 EBITDA 皆為負），僅能以 P/B、現金覆蓋與 P/S (18.6x TTM) 參考，股價相對 52 週高點已下跌約 77%，市場定價已反映大量負面預期。本報告不含交易建議。

## Revenue & profitability

**營收成長 (USD, 年度，來源: yf financials)**
| 年度 | 營收 | YoY |
|---|---|---|
| FY2022 | 23.198M | n/a |
| FY2023 | 30.058M | +29.6% |
| FY2024 | 10.981M | -63.5% |
| FY2025 | 18.252M | +66.2% |

- 3 年 CAGR (FY2022 至 FY2025): 約 -7.7%。2022 至 2025 區間波動大，單年度變化劇烈，CAGR 參考價值有限。
- yfinance info 顯示 TTM 營收 24.578M，revenueGrowth 為 131.1%（資料欄位為 info 所提供，計算基準未說明）。TTM 營收高於 FY2025 營收 18.252M，推論 2026 年上半年營收高於 2025 年上半年，但 yfinance 未提供季度損益表，無法拆分驗證。
- 分部資料: yfinance info 與 longBusinessSummary 未提供營收分部佔比，記為 n/a。業務描述包括 VaultIC 安全元件、量子抗性 RISC-V 安全晶片、安全 ARM 平台、智慧卡讀卡晶片、PKI 與憑證管理 SaaS、ASIC 設計代工及 WISeRobot 人機協作平台。

**獲利能力 (yf financials 計算)**
| 年度 | 毛利率 | 營業利益率 | 淨利率 |
|---|---|---|---|
| FY2022 | 42.2% | 11.1% | 24.9% |
| FY2023 | 46.7% | -13.8% | -10.9% |
| FY2024 | 33.9% | -156.5% | -193.0% |
| FY2025 | 47.3% | -218.0% | -187.3% |

- FY2025 毛利 8.63M，毛利率回升至 47.3%，但營業費用 48.43M（R&D 12.48M、SG&A 38.56M）遠高於毛利，營業虧損 -39.80M。
- FY2025 SG&A 較 FY2024 增加約 137%（16.29M 至 38.56M），R&D 增加約 150%（4.99M 至 12.48M），費用擴張速度遠高於營收。
- 淨利 FY2025 為 -34.19M，EPS -0.24（FY2024 為 -0.60，FY2023 為 -0.21）。TTM EPS -0.20。
- ROE: info 為 -12.3%（TTM）；以 FY2025 年末權益 461.5M 計算淨利 ROE 約 -7.4%。ROIC: 投入資本約 52M（權益 461.5M + 負債 8.0M - 現金 417.7M），NOPAT 為負，ROIC 無實質意義（記為負值，不具比較性）。
- 費用中 SBC 達 11.26M（FY2025），FY2024 僅 0.15M，SBC 占營收約 61.7%，是 FY2025 虧損擴大的主要來源之一。

## Cashflow & balance sheet

**現金流 (yf cashflow，USD)**
| 指標 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| 營運現金流 (OCF) | -2.75M | -10.12M | -31.26M |
| 資本支出 (Capex) | -3.02M | -0.57M | -1.24M |
| 自由現金流 (FCF) | -5.77M | -10.70M | -32.50M |
| FCF 利潤率 | -19.2% | -97.4% | -178.1% |

- FY2025 FCF/淨利 比率 = -32.50 / -34.19 ≈ 0.95，但兩者皆為負，此比率不具健康度判讀意義；實質上為持續現金流出，且 FCF 年度 burn 由 FY2024 的 -10.7M 擴大至 FY2025 的 -32.5M。
- info TTM: OCF -43.11M、FCF -32.42M、淨利 -41.88M，燒錢速度仍在增加。
- FY2025 營運現金流 -31.26M 中，應收/應付/存貨營運資金變動合計 -8.86M，其餘主要為虧損本身。

**資產負債表 (yf balance_sheet / quarterly_bs，USD)**
| 指標 | FY2024 (12/31) | FY2025 (12/31) | 2026-06-30 |
|---|---|---|---|
| 現金及等價物 | 84.6M | 417.7M | n/a |
| 現金 + 短期投資 | 84.6M | 427.7M | 482.2M |
| 總負債 (Total Debt) | 8.9M | 8.0M | 7.1M |
| 淨現金 (現金+STI - 總債) | 75.7M | 419.7M | 475.1M |
| 流動資產 | 93.1M | 449.6M | 521.8M |
| 流動負債 | 16.9M | 28.2M | 36.2M |
| 流動比率 | 5.5x | 15.9x | 14.4x |
| 權益 | 76.5M | 461.5M | n/a |
| 每股淨值 (bookValue) | n/a | n/a | 2.40 USD (info) |
| 負債/權益 (Debt/Equity) | 11.6% | 1.7% | info 欄位 1.27，單位疑為百分比，與 2025 計算基準不一致 |

- 淨現金約 475M（2026-06-30），現金約佔市值 105%。yfinance info 的 EV 為 19.58M，但以 市值 457.7M + 總債 7.1M - 現金 482.3M 反算，EV 約 -17M。兩者不一致，本報告以 info 的 enterpriseToRevenue 0.797 對應 EV 19.58M 為 yfinance 原值，實際計算結果顯示企業價值接近零或為負。
- 商譽 5.66M（FY2025 新增，對應 FY2025 收購支出 10.55M）。
- 流動比率 14.4x、負債極低，短期償債風險低。
- 以 FY2025 營運現金流 -31.3M 與 TTM OCF -43.1M 粗估，現金水位足以支撐數年營運，但若 burn 持續擴大則緩衝逐年縮短（此為估算，非公司揭露之 runway）。

## Capital allocation & insider signal

**資本配置**
- 股本: 2024 年末 101.5M 股 → 2025 年末 193.0M 股（+90.1%）→ 2026-06-30 224.9M 股（半年 +16.5%）。info sharesOutstanding 223.4M、floatShares 215.9M。
- 2025 年股權募資 (Issuance of Capital Stock) 429.3M，是 FY2025 現金暴增的主要來源；另有 Stock option 行使收入 7.4M。
- 債務: FY2025 償還 5.13M、未新增，債務規模已降至 8M 以下。
- 資本支出極低（FY2025 1.24M，約營收 6.8%），未見回購或股息（dividendYield 0、payoutRatio 0）。股息覆蓋率與回購不適用。
- 資金主要用於營運虧損，尚未形成內生現金流，資本配置效率低；大額募資後的使用效益需等待後續財報驗證。

**內部人交易 (yf insider，列表期間 2026-03-18 至 2026-10-06)**
- 列表中無公開市場買進 (purchase) 紀錄。
- 公開市場賣出 (Sale) 約 36 筆，合計金額約 1.12M USD（依列表 Value 欄位加總，為估算）。
- 主要賣方: Jean-Pierre Enguent (Officer)、John O'Hara (CFO)、Carlos Creus Moreira (CEO)、Franck Buonanno (Officer) 等。
- 近期賣出價格: 2026-10-06 Enguent 以 2.46 賣出 35,000 股（85.9K USD）；2026-09-03 以 2.40 賣出 15,000 股。2026 年 6 月以約 3.5 USD 出售 CEO/CFO 持股。
- 規模: 1.12M USD 約占市值 457.7M 的 0.25%，絕對金額小，但方向一致為淨賣出，且 CEO/CFO 在股價高於現價時持續賣出。
- 另有大量期權/衍生性證券以 0.01 USD 行使 (conversion of derivative security)，多數隨後賣出，屬於行權後變現，非新增持股信號。
- 內部人持股比例 2.69%（heldPercentInsiders）。

## Valuation

| 指標 | 數值 | 說明 |
|---|---|---|
| 股價 | 2.03-2.04 USD | fast_info 2.038、info 2.035、ta snapshot 2.0328 |
| 市值 | 457.7M USD | info marketCap；nonDilutedMarketCap 517.3M |
| Trailing P/E | n/a | TTM EPS -0.20，為負 |
| Forward P/E | n/a | info forwardPE -7.54；forwardEPS -0.27，為負 |
| EV/EBITDA | n/a | TTM EBITDA -46.07M，為負 |
| P/FCF | n/a | FCF 為負 |
| P/S (TTM) | 18.6x | info priceToSalesTrailing12Months；以 TTM 營收 24.58M 驗算一致 |
| P/S (FY2025) | 約 25.1x | 457.7M / 18.25M |
| P/B | 0.85x | info priceToBook；bookValue 2.402 |
| 每股現金 | 2.09 USD | info totalCashPerShare；略高於股價 |
| 分析師目標價 | 低 3.75 / 均 5.875 / 高 8.00 USD | 僅 2 位分析師，recommendationKey 為 none |

- 相對 sector median 的比較: 本報告無可靠同業資料。依一般半導體與資安硬體股的經驗區間，P/S 中位數約 5-10x（粗估，非來源數據，僅供參考），LAES 的 P/S 18.6x 屬偏高；但 P/B 0.85x 與淨現金超過市值，屬於深度折價資產定價。兩者相互矛盾，反映市場對 LAES 營收的持續性與獲利前景存在極大疑慮。
- 分析師目標價均值 5.875 USD 相較現價高約 189%，但僅 2 位分析師覆蓋，樣本不足，參考性低。
- 技術位置 (ta snapshot): 股價 2.03 低於 MA20 (2.30)、MA50 (2.44)、MA200 (3.11)；RSI14 為 30.6（接近超賣區）；MACD -0.065 低於訊號線 -0.046，柱狀體為負；布林 %B -0.19（位於下軌之下）；ATR14 0.110 約占股價 5.4%。52 週區間 1.99-8.71，現價距低點 +2.2%、距高點 -76.7%。此為技術面資訊，僅作背景，不構成交易建議。

## Key catalysts
- 下次財報: yfinance earnings_dates 顯示 2027-03-22（EPS estimate 為 null，可能為預估日期占位）。info 的 earningsTimestamp 為 2026-09-11、earnings call 為 2026-09-15，這兩個日期早於 as-of 日期，可能為 2026 年第二季（最近季 2026-06-30）財報的已發生日期，但 yfinance earnings history 未提供該季 EPS 與 surprise，記為 DATA_UNAVAILABLE（盈餘驚喜）。
- 近期指引 (guidance): yfinance 未提供管理層指引；info 的 forwardEps -0.27 與 epsCurrentYear -0.24 為分析師/系統估計值，顯示 2026 年仍預期虧損。
- 業務催化劑（來自 longBusinessSummary，未含量化數據）: 量子抗性 RISC-V 安全晶片、量子安全 PKI/憑證服務、與 L5 Cartronics 合作開發安全 IoT 模組、WISeRobot 人機協作平台。量子安全題材可能帶動估值情緒，但 yfinance 無相應營收貢獻數據。
- 母公司關係: SEALSQ 為 WISeKey International Holding AG 之子公司，關聯交易與母公司持股影響需於 10-K/20-F 驗證（本次工具未提供）。
- 股權結構: 機構持股 6.66%（129 家），空頭部位 9.69M 股（占 float 4.5%，較前月 11.75M 下降），short ratio 1.99 日。

## Metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收 (FY2025) | 18.25M USD | +66.2% | n/a | 波動大，尚未穩定成長 |
| 營收 TTM | 24.58M USD | revenueGrowth 131.1% (info) | n/a | 成長但基數低 |
| 毛利率 (FY2025) | 47.3% | +13.4 pp | 約 50-60% (粗估) | 中性偏弱 |
| 營業利益率 (FY2025) | -218.0% | 由 -156.5% 惡化 | 約 10-20% (粗估) | 差 |
| 淨利率 (FY2025) | -187.3% | 與 FY2024 相近 | 約 5-15% (粗估) | 差 |
| EPS TTM | -0.20 | 由 FY2025 -0.24 改善 | n/a | 虧損 |
| ROE (TTM, info) | -12.3% | n/a | 約 10-15% (粗估) | 差 |
| ROIC | 負值，不具意義 | n/a | 約 10%+ (粗估) | 差 |
| 營運現金流 (FY2025) | -31.26M USD | 由 -10.12M 惡化 | 正值 (粗估) | 差 |
| FCF (FY2025) | -32.50M USD | 由 -10.70M 惡化 | 正值 (粗估) | 差 |
| FCF 利潤率 | -178.1% | 惡化 | 約 10-20% (粗估) | 差 |
| FCF / 淨利 | 0.95 (兩者皆負) | n/a | >0.9 | 不具判讀意義 |
| 現金 + STI (2026-06-30) | 482.2M USD | 2025 年末 427.7M | n/a | 強 |
| 總負債 (2026-06-30) | 7.1M USD | 2025 年末 8.0M | n/a | 強 |
| 淨現金 (2026-06-30) | 475.1M USD | 2025 年末 419.7M | n/a | 強 |
| 流動比率 (2026-06-30) | 14.4x | 2025 年末 15.9x | 約 2x (粗估) | 強 |
| Debt/Equity (2025 年末) | 1.7% | 2024 年末 11.6% | 約 50% (粗估) | 強 |
| Capex 占營收 (FY2025) | 6.8% | 2024 年 5.2% | n/a | 低 |
| 股數 (2026-06-30) | 224.9M | 2025 年末 +16.5% (半年) | n/a | 稀釋中 |
| SBC 占營收 (FY2025) | 61.7% | 2024 年 1.3% | 約 10-15% (粗估) | 差 |
| Trailing P/E | n/a (虧損) | n/a | 約 25-35x (粗估) | 不適用 |
| Forward P/E | n/a (虧損) | n/a | 約 20-30x (粗估) | 不適用 |
| EV/EBITDA | n/a (EBITDA 為負) | n/a | 約 15-25x (粗估) | 不適用 |
| P/S (TTM) | 18.6x | n/a | 約 5-10x (粗估) | 偏高 |
| P/B | 0.85x | n/a | 約 3-5x (粗估) | 折價 |
| 內部人交易 (6 個月) | 淨賣出約 1.12M USD，無買進 | n/a | n/a | 偏負面 |
| 股價 vs 52 週高點 | -76.7% | 52 週 -65.6% | n/a | 弱勢 |
| RSI(14) | 30.6 | n/a | 50 | 接近超賣 |
| 空頭部位占 float | 4.5% | 前月 11.75M 股 → 9.69M 股 | n/a | 中性 |

## Red flags
- 營業利益率 -218%、FCF -32.5M（FY2025），費用擴張速度遠超營收，獲利結構尚未收斂。
- 前瞻 EPS (-0.27) 劣於追溯 EPS (-0.20)，市場分析對 2026 年虧損擴大的預期。
- 股本 2025 年增加 90%、2026 年中再增 16.5%，股東稀釋持續。
- SBC 占營收 61.7%，實際現金成本與 GAAP 虧損的差距需留意。
- 內部人 (CEO、CFO、多位 Officer) 在 2026 年持續賣出，列表期間無公開市場買進。
- 分析師覆蓋僅 2 位，目標價區間 3.75-8.00 USD 參考性低，recommendationKey 為 none。
- yfinance 資料缺口: quarterly_fin 與 quarterly_cf 回傳空陣列，無法驗證季度營收與毛利趨勢；盈餘驚喜歷史為空；營收分部無資料。
- 資料品質: info 的 beta 為 -7.513，數值異常，不可用於風險判斷；info 的 enterpriseValue (19.58M) 與以市值/現金反算結果 (約 -17M) 不一致；debtToEquity 1.27 單位不明。
- 資料來源為 cache（cached_at 2026-10-12 約 15:08-15:13 UTC），Yahoo cookie/crumb 取得失敗，info 中 regularMarketTime 的時間戳與 cached_at 不一致，已以 2.03-2.04 USD 區間交叉驗證，未取得 2026-10-13 收盤後資料。
- 母公司 WISeKey 關聯交易與持股比例，本次工具未提供，需人工查閱公告確認。

FUNDAMENTALS REPORT COMPLETE
