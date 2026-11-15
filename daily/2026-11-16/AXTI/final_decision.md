## FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — AXTI as of 2026-11-16

框架：新倉（AXTI 不在 held_tickers.txt）。

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $38.90 – $41.84 |
| Stop | $36.56（收盤基準，不攤平）；$37.75 為內部警示線，收盤跌破先減半 |
| Target 1 | $49.04 |
| Target 2 | $62.52（延伸情境，不作為定部位依據） |
| Size | Small（上限 0.75% NAV）；首批 0.30% NAV，第二批 0.45% NAV |
| Horizon | 1–3 個月 |
| Conviction | L |
| R:R to T1 | 2.3（均價 $40.37，風險 $3.81，報酬 $8.67） |

執行規則：
- 首批在區間內進場，不追高於 $41.84。
- 第二批只在以下任一條件成立時進場：(a) 11-17 NVIDIA 財報消化後，回測 $38.90–$39.50 且量縮守穩；(b) 收盤站上 $49.04 並收復 MA20 $50.44；(c) 10-Q 證實現金流來自預收款。
- 不使用 call spread，也不買族群 put，部位規模不值得增加複雜度。
- 觸及停損的 NAV 損失約 0.07%，跳空情境約 0.10%。

## Risk debate adjudication
- Aggressive 的最強論點：基本面數據（Q3 營收 +162% YoY、backlog 超過 500 USD M、Lumentum 協議至 2031-12-31）已公布且可查證，0.5% NAV 的風險金額小到無法有效參與。
- Conservative 的最強論點：停損距離僅 0.56×ATR14，beta 2.01 加上空單 21.35%，11-17 NVIDIA 財報後容易跳空穿越停損；Q3'26 現金流品質尚未證實。
- Net：我較偏重 neutral。接受上限提高到 0.75% NAV，但駁回 Aggressive 同時放寬停損到 $34.31 又放大部位的主張，那是放大美元風險而非管理風險。首批壓在 0.30% NAV 是我額外加的限制，理由是組合已持有 COHR 與 MRVL：前者是 InP 同業，後者正在收購 AXTI 的核心客戶 Lumentum，三者對 AI 光通訊族群是同向曝險，風險辯論三方都沒有計入這一點。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營收與毛利轉折 | 營收 YoY 超過 100%，毛利率 45% 以上 | Q3'26 營收 73.4 USD M（+162%），non-GAAP 毛利率 56.1%，Q4 指引約 90 USD M | 成立 |
| 需求能見度 | backlog 與長約支撐 2027 營收 | backlog 超過 500 USD M；Lumentum 預付 87 USD M；但 Lumentum 將被 Marvell 收購 | 觀察中 |
| 現金流品質 | 經常性營業現金流轉正 | 倒推 Q3 營業現金流約 102 USD M 高於營收，TTM FCF/NI 0.59 | 觀察中 |
| 價格結構止跌 | 守住 11-05 低點並收復 MA20 | 死亡交叉，價格低於三條均線，僅守住 $36.56 | 觀察中 |

## 論點失效條件
與 Stop 分開，論點先壞就先動作。
- 若 Q3'26 10-Q 顯示合約負債（客戶預收款）單季增加低於 43.5 USD M，即異常現金流無法由 Lumentum 預付款解釋，現金流支柱失效 → 不建第二批，首批減碼。
- 若 Q4'26 營收低於 85 USD M 或 non-GAAP 毛利率低於 45%，轉折支柱失效 → 出場。
- 若公司或 Marvell/Lumentum 公開揭露供應協議重新議價、縮量或終止，需求支柱失效 → 出場。
- 若公司揭露 InP 出口許可遭拒或出貨中斷，→ 出場。
- 若 Tongmei 贖回金額超過 49 USD M，或母公司再度宣布股權募資，→ 減碼。

## Monitoring trigger
- 進場前必查兩件事。第一，Q3'26 10-Q 的法定申報期限落在 11 月中旬，trade_proposal 把它排到 2027-02 是錯的；若已申報，先讀營業現金流拆解與合約負債再下單。第二，sentiment 報告提到的 11-10 中國出口管制暫停期限結果未確認，需先查明。
- 若 11-17 NVIDIA 財報後 AXTI 跳空開在 $37.75 以下，當日不等收盤即重新評估。
- 近期董事 11-05 出售 100,000 股的報導尚未對照 Form 4，若屬實且非 10b5-1 計畫，不建第二批。

## Catalyst calendar
- 2026-11 中旬 — Q3'26 10-Q 申報（期限前後，日期待查 EDGAR）
- 2026-11-17 — NVIDIA FQ3 財報電話會議
- 2026-11（日期未定） — Tongmei 私募基金贖回窗口（約 49 USD M）
- 2026-12-09 — FOMC 利率決議
- 2027-02-18（預估） — AXTI Q4'26 財報

FINAL DECISION COMPLETE
