FINAL TRANSACTION PROPOSAL: **SELL**

# Final decision — IONQ as of 2026-09-01

## Verdict
MODIFY

## 決策定性
IONQ 不在 `held_tickers.txt`，屬**新倉**判斷，問題是「該不該進」而非「該不該續抱」。
方向為 SHORT（看空），但**改以定義最大虧損的 Put Spread 執行，不做裸空**，且未觸發前
基準立場為 AVOID（0% NAV）。

**注意：PRICE_DATA_UNAVAILABLE，暫不給即時進出場價位；以基本面錨定框架執行。**
下表所有價位為論點錨點與條件門檻，不是即時掛單價。

## Final trade card
| Field | Value |
|---|---|
| Direction | SHORT（Dec 2026 $44 / $27 Put Spread，借方價差） |
| Entry zone | 不設即時價位。觸發條件成立後，於標的 $47–50 阻力帶執行 |
| Stop | 標的收盤站上 $55，或 Put Spread 權利金虧損達 50% —— 兩者先到者為準 |
| Target 1 | 標的 $32.00（回補 50% 部位） |
| Target 2 | 標的 $23.50（剩餘部位，接近 spread 最大獲利區） |
| Size | Small — 0.5% NAV（以權利金計，非名目敞口），嚴禁加碼 |
| Horizon | 1–3 個月（Dec 2026 到期） |
| Conviction | M（約 60%） |
| R:R to T1 | 2.5（spread 結構下最壞虧損鎖定於權利金，實質 R:R 更佳） |

## Entry trigger（必須同時滿足兩項）
1. **必要條件**：PRICE_DATA 恢復，且標的確認反彈至 $47–50 阻力帶並量縮（成交量低於 20 日均量 30% 以上）。
2. **加一項基本面確認**：Q3 2026 財報營收環比下滑或毛利率無改善；或 CHIPS Act LOI 未如期轉正；或 Quantinuum IPO 後取得大型企業合約公告。

未同時滿足 → **維持 AVOID，0% NAV**。若股價續留 $39–44，不追空。

## Risk debate adjudication
- Aggressive's strongest point：三重共振證據（財報 beat 後仍分配、高管系統性淨賣出無買進、55x P/S 對年虧損 $310M 公司）確實高於一般 MEDIUM 信念；且 Put Spread 建議是本輪最有價值的結構性貢獻。
- Conservative's strongest point：量子主題盤前跳空 30–60% 可使 $55 停損形同虛設，裸空的名目虧損可超過部位本金；PRICE_DATA_UNAVAILABLE 下預設條件式進場是真實程序風險。
- Net：我採 **neutral** 為主。Aggressive 自相矛盾——既承認跳空風險又要把裸空加倍到 1% NAV；Conservative 的 0.25% 建立在裸空前提上，一旦改用 Put Spread 該理由即失效。Put Spread 把尾部風險歸零，是唯一能同時滿足兩方核心關切的結構。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 估值無法自圓其說 | 55x forward P/S 對應 2026E 虧損 $310–330M | 未見毛利率拐點 | 成立 |
| 財報後分配訊號 | Beat 22.4% 後股價無法守住 $49–50 | 8/24 單日 -7.48% | 成立 |
| 內部人士淨賣出 | CFO/CLO 高位系統性出清，零買進 | 未見反轉申報 | 成立 |
| 政府合約護城河遭稀釋 | Quantinuum 同架構 + Rigetti 亦獲 $1 億 LOI | 待 Quantinuum IPO 後驗證 | 觀察中 |

## 論點失效條件（與 Stop 分開）
- 若 CHIPS Act $1 億 LOI **正式轉為硬合約**，且同季毛利率 >40% → 估值支柱失效 → **立即出場**
- 若公司公告**可驗證的商業量子優勢案例**（非研究論文，須有付費客戶）→ 護城河支柱反轉 → **立即出場**
- 若 SEC Form 4 出現**任一高管公開買進申報** → 內部人士支柱失效 → **減碼至半倉**
- 若 Q3 2026 營收環比續增且毛利率改善 >10pp → 分配訊號支柱失效 → **出場**

## Monitoring trigger
若標的在無基本面消息下衝破 $52，或 Quantinuum IPO 定價引發同業比價炒作，於 Stop 觸及前重新評估部位。

## Catalyst calendar
- 2026-10~11 — Q3 2026 財報（毛利率方向、256-qubit 出貨）
- 2026 H2 — CHIPS Act $100M LOI 正式合約公告或落空
- 2026 Q3–Q4 — NRO Capella SAR 交付里程碑
- 2026 Q4 — Quantinuum IPO 後首季企業合約披露
- 持續 — SEC Form 4 內部人士申報

FINAL DECISION COMPLETE
