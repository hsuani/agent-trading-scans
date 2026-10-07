# Fundamentals — HPE as of 2026-10-08

## Executive summary
HPE 最新一季（FY26 Q3，截至 2026-07-31）營收 $12.21B、年增 33.7%，GAAP 營業利益率回升至 12.0%，TTM 自由現金流 $4.16B（FCF margin 9.9%），現金流與槓桿指標（淨負債由 $19.08B 降至 $14.03B）明顯改善，但有形淨值為負 −$2.94B、商譽加無形資產佔總資產 35.2%。估值方面，forward P/E 15.0x 低於 DELL（19.7x），但高於其餘同業中位數（估算 10.7x）；trailing P/E 36.3x、EV/EBITDA 15.6x、P/B 3.5x 偏高，股價 $70.48 已接近分析師平均目標價 $72.03（僅 +2.2%）。整體結論：財務健康度持續改善，但 GAAP 盈餘品質與庫存快速膨脹需要追蹤，估值相對 enterprise IT 同業（DELL）偏合理、相對低毛利 ODM 同業偏貴。

資料來源說明：本次 yf 與 ta 工具的即時連線遭 ConnectionError / 403 阻擋，所有數據均取自快取（yf 回傳 `source: "cache"`，cached_at 2026-10-07 13:08–13:13 UTC；ta snapshot as_of 2026-10-06）。財報資料最新至 2026-07-31 季。

## Revenue & profitability

**年度營收趨勢（yf financials，單位 USD）**
- FY22 $28.50B → FY23 $29.14B（+2.2%）→ FY24 $30.13B（+3.4%）→ FY25 $34.30B（+13.8%）
- FY22–FY25 三年 CAGR 約 6.4%；FY21 數據 DATA_UNAVAILABLE，無法計算五年 CAGR
- FY25 營收跳升的背景：yf 資產負債表顯示 FY25 商譽由 $18.09B 增至 $23.77B，季現金流量表 2025-07 季投資活動現金流出 $12.60B，與公開資訊所載的 Juniper 收購時點吻合（此為外部公開資訊，本次工具未直接揭露收購對象）

**季度營收（yf quarterly_fin）**
- Q4 FY25（2025-10）$9.68B → Q1 FY26（2026-01）$9.30B → Q2 FY26（2026-04）$10.68B → Q3 FY26（2026-07）$12.21B
- Q3 年增 +33.7%（對比 Q3 FY25 $9.14B），季增 +14.4%
- TTM 營收 $41.87B；yf 同步 revenueGrowth 0.337，一致
- 年增部分可能含併購貢獻（Juniper 於 2025 年 7 月前後併入），有機成長率 DATA_UNAVAILABLE

**分部組成**
- yf longBusinessSummary 列出五大分部：Server、Hybrid Cloud、Networking、Financial Services、Corporate Investments and Other
- 各分部營收與獲利 DATA_UNAVAILABLE（工具未提供分部財務數據）
- AI 伺服器訂單積壓（backlog）DATA_UNAVAILABLE

**毛利率**
- 年度：FY22 33.4%、FY23 35.1%、FY24 32.8%、FY25 30.3%（逐年下滑，FY25 受 Juniper 併購後組合變化影響）
- TTM 36.7%（yf grossMargins 36.6%，吻合）
- Q3 FY26 40.1%，對比 Q3 FY25 29.2%（+10.9 個百分點）

**營業利益率（GAAP，依 yf 季報自行加總）**
- 年度：FY22 7.8%、FY23 8.4%、FY24 8.3%、FY25 4.8%
- TTM 營業利益 $3.28B，TTM 營業利益率 7.8%
- Q3 FY26 營業利益 $1.46B，營業利益率 12.0%，對比 Q3 FY25 $0.43B（4.7%），年增 +242%
- 口徑差異：yf info 的 operatingMargins 為 12.56%，與 GAAP 加總 7.8% 不一致，推測 yf 採調整後口徑；本報告以 GAAP 加總為準

**淨利與 EPS**
- 年度淨利（普通股東）：FY22 $868M、FY23 $2.03B、FY24 $2.55B、FY25 −$59M（diluted EPS −$0.04）
- FY25 淨利接近零的主因：yf 單次項目合計 −$1.83B，稅務利益 −$342M 為正面調節
- TTM 淨利（普通股東）$2.68B，淨利率 6.4%；TTM GAAP diluted EPS 約 $1.92（季加總），yf trailingEps 為 $1.94
- Q3 FY26 GAAP diluted EPS $1.06（Q3 FY25 $0.21），但該季 yf 單次項目合計為 **+$373M**（正面），需注意 Q3 盈餘含非經常性利益

**EBITDA**
- yf 正規化 EBITDA：季加總 TTM 約 $6.77B；yf info ebitda $6.89B，EBITDA margin 16.5%
- Q3 FY26 正規化 EBITDA $2.33B（19.1%）

**ROE / ROIC**
- ROE（TTM 淨利 / 期末股東權益）：10.1%（yf returnOnEquity 10.9%）
- ROIC（估算）：TTM 營業利益 $3.28B × (1 − 21%) ÷（總債務 $20.24B + 股東權益 $26.51B − 現金 $6.22B）≈ 6.4%；稅率 21% 取自 yf tax rate for calcs，為近似值

## Cashflow & balance sheet

**現金流（yf cashflow / quarterly_cf）**

| 年度 | OCF | Capex | FCF (OCF−Capex) | FCF margin | FCF / 淨利 |
|---|---|---|---|---|---|
| FY22 | $4.59B | $3.12B | $1.47B | 5.2% | 1.70x |
| FY23 | $4.43B | $2.83B | $1.60B | 5.5% | 0.79x |
| FY24 | $4.34B | $2.37B | $1.97B | 6.6% | 0.77x |
| FY25 | $2.92B | $2.29B | $0.63B | 1.8% | n/m（淨利近零） |
| TTM（至 2026-07） | $6.69B | $2.54B | $4.16B | 9.9% | 1.55x |

- TTM FCF / 淨利 1.55x，高於 0.9 健康門檻；但 TTM OCF 含 D&A $3.49B，且 Q3 FY26 應付帳款增加，現金流品質部分依賴營運資本
- yf info freeCashflow 為 $4.74B，與依季報計算的 $4.16B 不同（差 $0.58B），以計算值為準並標示差異
- 資本支出：FY22 佔營收 11.0% → FY25 6.7%，TTM 6.1%；Q3 FY26 capex $745M 為近四季高點，需追蹤是否進入擴產期

**資產負債表（2026-07-31，yf quarterly_bs）**
- 現金及約當現金：$6.22B（Jul-25 $4.57B，+36%）
- 總債務：$20.24B（流動 $2.90B、長期 $17.34B）；yf totalDebt $20.32B，差異 $0.08B
- 淨負債：$14.03B（Jul-25 $19.08B，年減 $5.05B）
- 總資產 $83.60B、總負債 $57.02B、股東權益 $26.51B
- D/E（總債務 / 股東權益）0.76x（Jul-25 約 0.97x），yf debtToEquity 76.5%，一致
- 流動比 1.11x（流動資產 $33.87B / 流動負債 $30.44B；Jul-25 約 0.95x），yf quickRatio 0.53
- 有形淨值 −$2.94B（股東權益 $26.51B − 商譽及無形資產 $29.45B；Jul-25 約 −$6.00B）
- 商譽及無形資產佔總資產 35.2%
- 利息費用：FY24 $117M；FY25 及季度 DATA_UNAVAILABLE，利息保障倍數 DATA_UNAVAILABLE

**營運資本**
- 存貨 $11.82B，年增 +65.1%（Jul-25 $7.16B），快於 Q3 營收年增 +33.7%
- 應收帳款 $10.03B（Jul-25 $9.43B，+6.3%）
- 應付帳款 $13.73B（Jul-25 $8.92B，+54.0%）
- 存貨增加主要由應付帳款融資，存貨週轉天數 DATA_UNAVAILABLE（需逐季存貨成本資料）

**資料分類不一致警示**
- 年度 BS（2025-10-31）與季度 BS（2026-07-31）的資產分類差異極大：Other Non-Current Assets 由 $1.54B 變為 $14.63B，Other Non-Current Liabilities 由 $0.79B 變為 $9.24B，Net PPE 由 $7.54B 變為 $5.65B。此為 yf 分類口徑變動的可能性，本報告不以此推論結論，需人工核對 10-Q

## Capital allocation & insider signal

**股利**
- 季股息 $0.143，年化 $0.57，殖利率 0.81%（yf dividendYield；5 年平均殖利率 2.48%）
- 股利支付率（以 GAAP EPS 計）28.7%（yf payoutRatio）
- 普通股股利 TTM $739M（季度加總），TTM FCF 覆蓋 5.6x；yf 股利現金流出 TTM 含非普通股部分為 $855M，分項 DATA_UNAVAILABLE

**買回與稀釋**
- 買回金額：FY22 $512M、FY23 $421M、FY24 $150M、FY25 $202M；TTM $547M
- TTM SBC $795M，買回僅覆蓋約 69%
- 流通股數由 1,318.8M（Jul-25）增至 1,328.1M（Jul-26），年增 +0.71%，存在輕微淨稀釋

**債務去槓桿**
- 2025-07 季發行債務 $5.08B（Q3 FY25，與併購資金時點吻合），2025-10 季償還 $5.17B
- FY26 前三季（2026-01、2026-04、2026-07）償還債務合計 $4.69B、發行債務合計 $2.55B，淨償還約 $2.14B
- 上述數字為季度現金流加總計算，與 yf 年度口徑未逐項核對

**內部人交易（yf insider，近 6 個月 2026-04-08 至 2026-10-08，共 20 筆）**
- 公開市場賣出（Sale）：11 筆，合計 655,233 股，約 $29.42M
- 前六個月同口徑賣出約 $24.59M（2025-10 至 2026-04），本期賣出金額增加約 20%
- CEO Antonio Neri：2026-04-17 賣出 150,000 股（$26.50，$3.97M）；2026-09-11 賣出 250,000 股（$60.44，$15.11M）；合計 $19.08M
- CFO Marie Myers：2026-05-05 賣出 93,583 股（$30.01，$2.81M）
- Networking 負責人 Rami Rahim：2026-09-29 賣出 34,456 股（$61.42，$2.12M）；另有 2026-07 選擇權行使 1,122,365 股（$41.23，行使價值 $46.28M）與 655,427 股贈與
- 董事 Gary Reiner：2026-06-03 賣出 20,000 股（$54.77）、2026-09-14 賣出 17,000 股（$56.91）
- 選擇權行使（Conversion of Exercise）3 筆，1.19M 股，行使價值 $49.13M；贈與（Stock Gift）3 筆 2.34M 股（其中 CEO 2026-05-01 贈與 1.68M 股）；授予（Stock Award）3 筆，合計 $0.08M
- 無公開市場買入紀錄
- 規模判斷：6 個月公開市場賣出 $29.42M 僅佔市值 $93.56B 的 0.03%，內部人合計持股僅 0.37%。賣出金額絕對值小，但方向為淨賣出，且 9 月 CEO 大額賣出價位（$60.44）接近目前股價區間。10b5-1 交易計畫標記 DATA_UNAVAILABLE

**機構持股（yf inst_holders，截至 2026-06-30）**
- 機構持股比例 91.2%（1,948 家機構）
- 前十大：BlackRock 10.1%（季減 6.8%）、Vanguard Capital Management 6.5%（季增 0.4%）、Vanguard Portfolio Management 5.5%（季減 1.5%）、State Street 5.1%、Capital World Investors 4.5%（季增 1.6%）、JPMorgan 3.0%（季減 26.6%）、Bank of America 3.0%（季減 46.7%）、Geode 2.8%、Elliott Investment Management 2.4%（季增 17.7%）、Goldman Sachs 1.85%（季增 44.1%）
- Elliott 為知名積極型股東，其持股增加需留意是否伴隨治理訴求；工具未提供其意圖資料，標記 DATA_UNAVAILABLE

## Valuation

**價格與市值（yf fast_info / info，快取）**
- 股價 $70.48（前收 $68.36，日漲 +3.1%）；52 週區間 $19.84–$71.22，股價位於 52 週高點下方 1.0%
- 市值 $93.56B；企業價值 EV $107.73B；流通股數 1,327.5M
- 股價相對 200 日均線 37.36（+88.7%）、50 日均線 56.59（+24.6%）、20 日均線 61.92（+13.8%）

**估值倍數（以目前股價計）**

| 倍數 | HPE | 口徑說明 |
|---|---|---|
| Trailing P/E | 36.3x | GAAP TTM EPS $1.94 |
| Forward P/E | 15.0x | yf forwardEps $4.71，為分析師一致預估口徑，與 GAAP 不同 |
| PEG | 0.56x | yf pegRatio |
| EV / Revenue（TTM） | 2.57x | EV $107.73B / 營收 $41.87B |
| P/S（TTM） | 2.23x | |
| EV / EBITDA | 15.6x | yf enterpriseToEbitda，EBITDA $6.89B |
| EV / EBIT（TTM，GAAP 加總） | 32.8x | EBIT $3.28B |
| P/FCF | 19.7x | yf FCF $4.74B；依季報計算 22.5x（FCF $4.16B） |
| P/B | 3.53x | 每股帳面價值 $19.96 |

**同業比較（估算中位數，樣本為 DELL、SMCI、2317.TW、2382.TW 共 4 檔）**

| 指標 | HPE | DELL | SMCI | 2317.TW | 2382.TW | 同業中位數（估算） |
|---|---|---|---|---|---|---|
| Trailing P/E | 36.3x | 33.4x | 13.3x | 16.7x | 15.2x | 16.0x |
| Forward P/E | 15.0x | 19.7x | 8.2x | 10.9x | 10.5x | 10.7x |
| EV / EBITDA | 15.6x | 21.9x | 12.2x | 8.6x | 12.6x | 12.4x |
| P/S | 2.23x | 2.41x | 0.73x | 0.38x | 0.46x | 0.60x |
| 毛利率 | 36.6% | 19.9% | 10.8% | 6.1% | 5.5% | 8.5% |
| 營業利益率 | 12.6%（yf）/ 7.8%（GAAP 加總） | 12.0% | 13.4% | 3.8% | 3.3% | 7.9% |
| 營收成長（yf） | 33.7% | 57.7% | 93.2% | 40.8% | 105.6% | 75.5% |

- 估值解讀：HPE 的 forward P/E 高於低毛利 ODM 同業中位數約 40%，但低於 DELL；EV/EBITDA 低於 DELL 但高於其餘三檔中位數。DELL 為企業 IT 與伺服器結構最接近的可比對象，相對 DELL 估值較低
- P/S 不宜直接比較：HPE 毛利率 36.6%，遠高於 ODM 同業（5–11%），P/S 溢價主要反映毛利結構差異
- 同業數據品質提醒：2317.TW 的 freeCashflow 為 −TWD 182B、2382.TW 營收成長 105.6% 與負債權益比 168%、SMCI FCF −$8.25B，皆屬大幅異常值，同業中位數僅供粗略參考；倍數屬貨幣中性，TWD 與 USD 倍數可直接比較

**分析師一致預期（yf info）**
- 覆蓋分析師 21 位；平均評等 1.96（介於 Buy 區間）
- 平均目標價 $72.03（較現價 +2.2%）；最高 $92.00（+30.5%）；最低 $52.59（−25.4%）
- 目標價上行空間有限，市場價格已反映大部分一致預期

**技術面脈絡（ta snapshot，快取，as_of 2026-10-06）**
- RSI14 69.6（接近超買區間）；BB %B 1.00（股價位於布林上軌）；MACD 3.55、Signal 2.83、Hist 0.71
- ATR14 $3.61；20 日年化波動 78.5%
- 6 個月動能 +186%、12 個月動能 +188%
- 技術指標僅作脈絡參考，不構成交易建議

## Key catalysts
- **下次財報**：2026-12-03（yf earnings_dates，FY26 Q4），一致預估 EPS $1.27（口徑為分析師預估，與 GAAP 不同）
- **上一次財報**：2026-09-02（依 yf info earningsTimestamp）。FY26 Q3 季報數字已入 yf 財報（2026-07-31 季），但 yf earnings_dates 表仍顯示 2026-09-02 的 Reported EPS 為空白；Q3 調整後 EPS 實際值 DATA_UNAVAILABLE
- **歷史 EPS 驚喜**：近 8 季中 7 季為正向驚喜，最近一季（2026-06-01 報告的 FY26 Q2）調整後 EPS $0.79 對比預估 $0.53，驚喜 +48.0%（口徑為 yf adjusted EPS，GAAP Q2 為 $0.44）
- **公司指引（guidance）**：DATA_UNAVAILABLE（工具未提供最新 FY26 營收與獲利指引）
- **股利**：yf 時間戳換算，前次除息約 2026-09-18，下次付息日約 2026-10-17（依 yf dividendDate 時間戳換算，需以公司公告核對）
- **分部轉變**：Networking 與 AI 伺服器（Server）的營收佔比變化 DATA_UNAVAILABLE；Juniper 相關整合綜效 DATA_UNAVAILABLE
- **AI 伺服器需求與訂單**：DATA_UNAVAILABLE（工具未提供 backlog 或客戶集中度資料）

## Red flags
- **有形淨值為負**：有形淨值 −$2.94B，商譽與無形資產 $29.45B 佔總資產 35.2%。若 Networking 或 Server 業務景氣反轉，有減損風險，且限制 ROE 的參考價值
- **庫存快速膨脹**：存貨年增 +65.1% 至 $11.82B，快於 Q3 營收年增 +33.7%；應付帳款年增 +54.0%。需確認是否為 AI 伺服器備貨，以及下一季存貨是否去化
- **GAAP 盈餘含一次性項目**：Q3 FY26 yf 單次項目合計 +$373M（正面），FY25 合計 −$1.83B。GAAP 獲利波動大，單季 EPS 不宜直接外推
- **估值偏高（相對 GAAP 基礎）**：trailing P/E 36.3x、P/B 3.5x、EV/EBITDA 15.6x；股價距 52 週高點僅 1.0%，52 週漲幅 +170%
- **分析師目標價上行空間有限**：平均目標價僅較現價 +2.2%，最低目標價 $52.59 低於現價 25.4%
- **內部人淨賣出**：6 個月公開市場賣出 $29.42M，較前 6 個月增加約 20%；CEO 於 2026-09-11 以 $60.44 賣出 250,000 股。金額佔市值比例小，但方向一致
- **股本輕微稀釋**：流通股年增 +0.71%，TTM SBC $795M，買回 $547M 僅覆蓋約 69%
- **利息與償債資料不足**：FY25 及季度利息費用 DATA_UNAVAILABLE，無法計算利息保障倍數
- **資料口徑不一致（需人工核對）**：
  - yf operatingMargins 12.6% 與 GAAP 加總 7.8% 不符
  - yf freeCashflow $4.74B 與季報計算 $4.16B 不符
  - 年度與季度資產負債表分類變動極大（Other Non-Current Assets、Other Non-Current Liabilities、Net PPE），本報告未用於結論
  - yf earnings_dates 未更新 2026-09-02 的 Q3 實際值
  - yf info 之 regularMarketTime（Unix 時間戳換算晚於 cached_at 2026-10-07 13:12 UTC），股價時點不確定，視為 2026-10-06 至 2026-10-07 的近期快取值
- **數據時效**：財報最新至 2026-07-31；股價與 info 為快取（非即時）；ta 指標 as_of 2026-10-06；未發現晚於 2026-10-08 的資料

## Metrics table

| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| 營收（TTM） | $41.87B | Q3 +33.7% | 75.5%（同業營收成長中位數） | 成長穩健，低於 AI 伺服器同業 |
| 毛利率（TTM） | 36.7% | Q3 40.1%，前年同期 29.2% | 8.5% | 明顯優於同業（組合偏企業網路與服務） |
| 營業利益率（TTM，GAAP 加總） | 7.8% | Q3 12.0%，前年同期 4.7% | 7.9% | 持平，Q3 改善明顯，但含 +$373M 單次項目 |
| 淨利率（TTM，普通股東） | 6.4% | FY25 −0.2% | 4.4% | 優於同業 |
| ROE（TTM） | 10.1% | DATA_UNAVAILABLE | 21.5%（3 檔可用） | 偏低 |
| ROIC（估算） | 6.4% | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 偏低，近似值 |
| 自由現金流（TTM） | $4.16B | FY25 $0.63B | DATA_UNAVAILABLE | 明顯改善 |
| FCF margin（TTM） | 9.9% | FY25 1.8% | DATA_UNAVAILABLE（2 檔同業 FCF 為負） | 改善 |
| FCF / 淨利（TTM） | 1.55x | FY25 n/m | DATA_UNAVAILABLE | 健康（高於 0.9） |
| 資本支出 / 營收（TTM） | 6.1% | FY25 6.7% | DATA_UNAVAILABLE | 合理，Q3 capex 升至近四季高點 |
| 現金及約當現金 | $6.22B | +36%（Jul-25 $4.57B） | DATA_UNAVAILABLE | 改善 |
| 淨負債 | $14.03B | −26.5%（Jul-25 $19.08B） | DATA_UNAVAILABLE | 改善 |
| D/E（總債務 / 股東權益） | 0.76x | Jul-25 約 0.97x | 0.64x（3 檔可用） | 略高於同業，但持續下降 |
| 流動比 | 1.11x | Jul-25 約 0.95x | 1.28x | 偏低，但改善 |
| 有形淨值 | −$2.94B | Jul-25 約 −$6.00B | DATA_UNAVAILABLE | 風險：商譽佔資產 35.2% |
| 存貨 | $11.82B | +65.1% | DATA_UNAVAILABLE | 警示：快於營收成長 |
| 利息保障倍數 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 無法評估 |
| 股利殖利率 | 0.81% | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 中性，5 年平均 2.48% |
| 股利 FCF 覆蓋（TTM） | 5.6x | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 健康 |
| 流通股數變化 | +0.71% | +0.71%（Jul-25 至 Jul-26） | DATA_UNAVAILABLE | 輕微稀釋 |
| 內部人 6 個月公開市場賣出 | $29.42M（0.03% 市值） | 前 6 個月 $24.59M，+20% | DATA_UNAVAILABLE | 淨賣出，金額小 |
| 機構持股比例 | 91.2% | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 高，集中於指數與大型基金 |
| Trailing P/E | 36.3x | DATA_UNAVAILABLE | 16.0x | 偏高 |
| Forward P/E | 15.0x | DATA_UNAVAILABLE | 10.7x | 相對同業偏高，低於 DELL |
| EV / EBITDA | 15.6x | DATA_UNAVAILABLE | 12.4x | 偏高，低於 DELL |
| P/FCF（yf） | 19.7x | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 中性偏高 |
| P/S（TTM） | 2.23x | DATA_UNAVAILABLE | 0.60x | 不宜直接比較（毛利結構差異） |
| P/B | 3.53x | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 偏高 |
| 分析師平均目標價上行空間 | +2.2%（目標 $72.03） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 上行空間有限 |
| 下次財報 | 2026-12-03（EPS 預估 $1.27） | DATA_UNAVAILABLE | DATA_UNAVAILABLE | 中性 |

FUNDAMENTALS REPORT COMPLETE
