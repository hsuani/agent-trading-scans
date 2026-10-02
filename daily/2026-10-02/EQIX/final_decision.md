FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — EQIX as of 2026-10-02

## Verdict
MODIFY

verdict_score: 64 / 100（新倉，不在 held_tickers.txt，走 A 框架；研究裁決 NEUTRAL 偏多，trader 原建議 AVOID，本案依 neutral 風險觀點改為小額試單）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $1,012 – $1,020（股票試單）；同時建立 11 月到期 $1,050/$1,150 bull call spread，權利金上限 0.1% NAV |
| Stop | $985（收盤價為準，MA200 $986 / 結構低點 $987.79 正下方） |
| Target 1 | $1,109（08-17 局部高點） |
| Target 2 | $1,200（分析師平均目標價） |
| Size | Small（股票 0.5% NAV + call spread ≤0.1% NAV；Q3 財報確認後上限 Medium 1.5% NAV） |
| Horizon | 4–6 週（涵蓋 11/4 財報）；完整論點驗證 1–2 季 |
| Conviction | M |
| R:R to T1 | 3.0（進場中位 $1,016，風險 $31，獲利 $93） |

## Risk debate adjudication
- **Aggressive 最有力的論點**：現價進場的 R:R（T1 約 3.0、T2 約 6.0）明顯優於等突破 $1,027–1,044 後再進場；等待不是降風險，是降報酬。但 Medium 1.5–2% 在技術面未轉態、MACD 未金叉、二元財報前就重倉，與 NEUTRAL/MEDIUM 的研究裁決不相稱，不採用。
- **Conservative 最有力的論點**：財報跳空會直接穿越任何停損（Scenario A 損失可放大 88%），且淨負債/EBITDA 4.2x、FCF -$400M、流動比率 1.13 是真實的利率尾部風險。但 $1,005 停損僅 0.8 ATR，財報前的正常波動就會洗出，買不到真正的保護；「技術＋財報雙重確認」等於放棄不對稱機會。
- **Net**：採 neutral 架構。跳空風險用「倉位極小」解決（0.5% NAV 跳空至 $950 損失約 0.03% NAV），而非用緊停損解決；財報槓桿上行用定義風險的 call spread 承接。另一項我額外加入的考量：組合已持有 DLR 與 AMT，EQIX 會提高數據中心 REIT 集中度與利率 beta，因此財報前倉位鎖定 0.5%，不開放任何加碼，conservative 建議的數據中心 ETF put 對沖應視為 DLR+EQIX 合併曝險的保護，加碼至 Medium 時同步評估。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 需求動能延續（AI capex 週期） | MRR YoY ≥10%、預訂額 YoY ≥20% | Q2 MRR +11%、預訂額 +23%（歷史第二高）、連接數新增 9,700 創紀錄 | 成立 |
| AFFO 足以覆蓋股息與擴張 | AFFO/股成長、指引維持或上修 | 無 AFFO 數據；GAAP 派息比 137.7%、FCF -$400M、淨負債/EBITDA 4.2x | 觀察中 |
| xScale 合資分攤 CapEx | 第三方資本承擔超大規模擴張 | GIC/CPP $15B+ 合資到位，2027–2029 CapEx $50–70 億/年 | 成立 |
| 技術面中期趨勢未破 | 價格守住 MA200，回到 MA20/50 之上 | $1,012 > MA200 $986，但低於 MA20 $1,027、MA50 $1,044，MACD -1.41 | 觀察中 |

## 論點失效條件
與 Stop 分開：Stop 是價格紀律，以下是論點紀律，觸發即動作，不等價格打到 $985。
- 若 Q3 財報 MRR YoY <8% 或預訂額 YoY <10%，「需求動能」支柱失效 → 出場（股票與 call spread 一併結清）。
- 若 Q3 AFFO/股指引下修，或股息成長暫停，或淨負債/EBITDA 升至 4.5x 以上，「AFFO 覆蓋」支柱失效 → 減碼一半，再出現第二項即出場。
- 若 2027–2029 CapEx 指引再上修，且法說會未揭露對應的超大規模客戶新簽約瓦數，「xScale 分攤」支柱失效 → 取消加碼，維持 0.5% 直到下一季。
- 若聯準會自 3.50%–3.75% 轉向升息，或信評機構將 EQIX 展望調為負向，利率尾部情境成真 → 減碼一半。

## Monitoring trigger
- 財報前若單日放量（>1.5x 五日均量）收盤跌破 $1,000，在 Stop 觸發前重新評估是否提前退出。
- 財報前若放量站回 MA20 $1,027 並突破 $1,044，不加碼（倉位鎖定），僅確認技術支柱轉為「成立」。
- 加碼至 Medium 的充分條件：Q3 MRR YoY ≥10%、預訂額 YoY ≥20%、AFFO/股指引維持或上修，且財報後收盤站回 MA50 之上，四者缺一不加。
- 財報日期存在 10/28（fundamentals）與 11/4（news）兩個版本，call spread 到期日須確保落在實際財報之後，須在建倉前核實。

## Catalyst calendar
- 2026-11-04（盤後，待核實）— Q3 2026 財報與法說會，營收指引 $2.52–2.58B，核心驗證點
- 2026-10-28 — 替代財報日期（fundamentals.md），需於建倉前確認
- 2026-11 月中 — Q3 13F 申報截止，確認機構對內部人連續六個月賣出的承接
- 持續 — FOMC 利率路徑、信評展望、xScale 超大規模客戶簽約進度

FINAL DECISION COMPLETE
