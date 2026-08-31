# Trade proposal — TLN as of 2026-09-01

FINAL TRANSACTION PROPOSAL: **BUY**

---

## Direction
LONG — 信心程度 MEDIUM

---

## Setup

> **PRICE_DATA_UNAVAILABLE**：Yahoo Finance 代理封鎖，無即時價格，暫不給進出場價位。以下所有價格錨點均來自基本面報告引述，屬近似值、未經獨立驗證，僅供參考框架，不可直接作為執行依據。

**Entry zone**：無即時市場數據，無法界定確定性進場區間。
待即時報價恢復後，建議對照 PJM 容量拍賣結果公佈後的技術支撐位，分批建倉。

**Stop**：無即時價格，暫不設定具體止損價。
論文失效邏輯（見「Invalidation」）作為功能性止損條件，優先於價格觸發。

**Target 1**：無即時價格，暫不設定具體目標價。
若 Q3 2026 業績驗證 FCF 軌跡，估值重評至 12-13x Forward P/E；相較當前 10x，隱含上行空間約 20-30%（未驗證近似值）。

**Target 2**：若 Susquehanna AWS 重組完成確認且 H2 FCF 達指引上限，重評至 14x Forward P/E；隱含上行空間約 40%（未驗證近似值）。

**R:R**：因無法取得即時價格與 ATR，R:R 無法量化計算。根據研究主管提供的上下行框架（上行 +40-60% 重估空間 vs 下行風險價格 $126-$150 區間，來源：investment_plan.md，屬未驗證近似值），若進場成本顯著高於此下行錨點，R:R 恐低於 1.5 門檻，需待報價確認後重新評估是否符合 LONG 最低要求。

---

## Sizing
**Medium（1.5%）of portfolio NAV**

理由：信心度 MEDIUM，ATR 無法取得（Price_Data_Unavailable），年化波動率未知。考量以下因素加重限制：
- Debt/Equity 584%、Interest Coverage 0.45x 顯示財務安全邊際薄弱。
- H2 FCF 交付懸崖（H2 須單季貢獻約 H1 六倍以上的 FCF）構成重大二元風險。
- Rubric Capital 持股從 19% 減至 6-7%，機構謹慎信號明確。
- 整合採「半倉至 2/3 倉」建倉策略，預留加碼空間於 Q3 業績後決定。

---

## Time horizon
**1-3 個月**

核心決策窗口：Q3 2026 業績（預計 2026 年 11 月中旬）。若 FCF 軌跡確認，可延伸至 **3-12 個月**，配合 AWS PPA 爬坡期的估值重評週期。

---

## Trigger
**等待條件後分批進場（Wait for condition / Scale in）**

不建議立即全倉進場，理由如下：
1. 即時報價不可用，無法確認當前價格是否已反映 H2 FCF 風險溢價。
2. 需等待 **Susquehanna front-of-meter 傳輸重組公開確認公告**，作為 AWS PPA $18B 合約基礎成立的技術驗證。
3. 若以下任一條件先達成，可考慮初倉（約半倉）：
   - 即時報價恢復後，確認現價相對 investment_plan.md 下行錨點（$126-$150 未驗證近似值）提供足夠 R:R 緩衝。
   - Q3 月度電力出售數據或 PJM 調度紀錄顯示 Susquehanna 容量正在爬坡。

---

## Invalidation
下列任一情況出現即終止論題、啟動出場：

- **H2 FCF 較指引下限短缺 ≥30%**：顯示 GAAP 虧損結構非暫時性，調整後數字失去可信度。
- **信用評級遭降級**：在 Debt/Equity 584% 的槓桿下，融資成本上升可能引發非線性估值崩解。
- **流動比率持續低於 0.78x 且短期債務再融資困難**：流動性危機優先於任何 PPA 合約估值。
- **Amazon 正式宣布調整 AI Capex 節奏或延遲 Susquehanna 合約啟動**：$18B PPA 估值基礎動搖。
- **SG&A 在 Q3 結算後仍高企**（未見自 +283% YoY 常態化回落）：管理費用失控進一步壓縮可信的 FCF 指引。

---

## Catalyst calendar
- **2026-11 月中旬**（預估）— TLN Q3 2026 業績發布：關鍵 FCF 驗證節點，門檻為調整後 FCF 單季 ≥$6 億
- **時間不確定** — Susquehanna AWS front-of-meter 傳輸重組完成公告（截至 2026-09-01 尚未確認）
- **持續監控** — PJM 容量市場後續拍賣結果（確認核能定價溢價是否延續）
- **持續監控** — Rubric Capital 13F 申報（追蹤機構持倉變化趨勢）
- **持續監控** — 季末流動比率是否回升至 1.0x 以上

---

*注意：本提案因 PRICE_DATA_UNAVAILABLE，所有價格水位均無法提供確定性數字。所有引自 investment_plan.md 之價格錨點（如 $126-$150 下行區間、+40-60% 上行空間）均為近似值、未驗證，在即時報價恢復前不得作為實際下單依據。*

TRADE PROPOSAL COMPLETE
