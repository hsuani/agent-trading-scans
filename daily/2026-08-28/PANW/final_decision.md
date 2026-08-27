FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — PANW as of 2026-08-28

## FINAL TRANSACTION PROPOSAL: **HOLD**

> 持倉判定：PANW **不在** `pipeline/tools/held_tickers.txt` → 走 **A. 新倉框架**。
> 問題是「該不該進」，答案是不進。第一行的 HOLD 代表「不建倉、不動作」，等同 AVOID。

## Verdict
REJECT

## Conviction
**35%**（對「現在做多」的信心。對「財報前不進場」這個決策本身的信心為 80%。）

## Position size recommendation
**0% NAV**（財報前不建立任何現股或選擇權部位）
財報後若下方觸發條件成立，首批建倉上限 **0.5% NAV**，2–4 週動能確認後可加至 **1.0% NAV**；本標的硬上限 1.0% NAV。

## Final trade card
| Field | Value |
|---|---|
| Direction | 無方向部位（財報前空手） |
| Entry zone | 無即時價格，暫不給進出場價位 |
| Stop | 無即時價格，暫不給進出場價位 |
| Target 1 | 無即時價格，暫不給進出場價位 |
| Target 2 | 無即時價格，暫不給進出場價位 |
| Size | 0% NAV（財報後條件式 0.5% → 1.0%） |
| Horizon | 3–6 個月，首次評估節點為 2026-09-01 財報後 2–4 週 |
| Conviction | L（35%） |
| R:R to T1 | 無法計算（PRICE_DATA_UNAVAILABLE） |

## Risk debate adjudication
- Aggressive's strongest point：Q3 NGS ARR +60%、Prisma AIRS 客戶 100→300+ 是可核實的超越指引，不是邊際改善；若 Q4 再超預期，財報夜跳空會讓事後建倉成本高出 10–20%。
- Conservative's strongest point：在 PRICE_DATA_UNAVAILABLE 下無法設定有效 Stop，等於沒有風控邊界；同時股價已高於 55 家分析師共識均值 $333–338，Forward P/E >50x，指引只需「略低預期」就會觸發非線性多重壓縮。
- Net：我採 **conservative** 為主、neutral 為輔。決定性理由是**無法定義 Stop**。Aggressive 的 R:R 3.3–5.5x 完全建立在「30% 止損可執行」的假設上，但沒有價格資料就沒有止損，這個 R:R 是紙上數字。新倉不同於持倉——放棄一個跳空機會的成本是有限的，承擔一個無邊界的事件風險則不是。Aggressive 的 call spread 方向正確，但財報前 4 日 IV 處於結構高點，無報價即無法驗證保費是否合理，同樣不執行。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| NGS ARR 加速真實 | YoY ≥40% | Q3 為 60%，遠超自身 30–35% 指引 | 成立 |
| 平台黏性與收入能見度 | NRR ≥110%、訂閱占比高 | NRR 110–115%、RPO $65–70B、訂閱 83%+ | 成立 |
| 估值提供安全邊際 | 股價低於分析師共識目標 | $359.76 已高於共識均值 $333–338，上行僅靠 Wells Fargo $475 | 已失效 |
| 管理層以資本背書 | 內部人淨買入或中性 | 12 個月淨賣出 $325.4M，近 3 個月 0 筆買入 | 已失效 |
| CyberArk $25B 整合 | 協同 2–3 季兌現、槓桿可控 | 尚未驗證，Net Debt/EBITDA 為關鍵 | 觀察中 |

四根支柱中兩根已失效（估值安全邊際、內部人背書），這正是新倉不成立的核心。基本面兩根仍站得住，所以是 REJECT 而非 SHORT。

## 論點失效條件
與 Stop 分開；Stop 是價格紀律，以下為論點紀律。
- 若 2026-09-01 Q4 NGS ARR 增速 <40%，加速論點失效 → 永久移出候選名單，不再評估多方。
- 若 FY2027 全年指引的 NGS ARR 增速目標 <30%，平台化盈利轉化論點失效 → 出場（本已 0%，即不建倉）。
- 若 CyberArk 宣布商譽減損，或 Net Debt/EBITDA >3.0x 且協同收入確認延後，整合論點失效 → 轉入 SHORT 評估。
- 若財報後 GAAP 運營利潤率仍 <8%，銷售效率收斂論點失效 → 建倉上限降至 0.25% NAV。

## 建倉觸發條件（須同時滿足兩項）
1. Q4 NGS ARR 增速 ≥60%，且 FY2027 指引 NGS ARR 增速 ≥40%。
2. GAAP 運營利潤率突破 10%，或 RPO/ARR ≥1.1x。
滿足後方可建首批 0.5% NAV，並以財報後確立之技術支撐位設 Stop（偏離不超過進場 -6%）。

## Monitoring trigger
若 2026-09-01 財報後股價站上 Wells Fargo $475 區間並伴隨量能顯著擴大（共識重新定錨於高目標位），須立即重評——此時觀望的機會成本已超過事件風險，即使兩項觸發條件僅滿足其一，亦應以 0.25% NAV 追蹤性建倉。

## Catalyst calendar
- 2026-09-01 — PANW Q4 FY2026 財報（決定性）：NGS ARR 增速、Prisma AIRS 客戶數、FY2027 指引、GAAP 運營利潤率
- 2026-08-31 至 09-03 — CrowdStrike Fal.Con Conference：競爭訊號
- 2026-Q4 待定 — 可能的補充性併購（$5–10B），若推升 Net Debt/EBITDA >3.0x 視為負面
- 2026-Q4 持續 — CCPA / Delete Act / CMMC 合規期限，結構性需求支撐

## Dealbreaker（REJECT 理由）
股價已高於 55 家分析師共識均值，安全邊際歸零；同時內部人 12 個月淨賣出 $325.4M 且近 3 個月零買入。在管理層自己不以資本背書、且缺乏價格資料無法設定 Stop 的情況下，於財報前 4 個交易日建立新倉不具正當性。**未來重訪條件**：上述兩項建倉觸發條件同時成立，且取得可用即時價格以設定明確 Stop。

## Phase
Phase 1-4 complete

FINAL DECISION COMPLETE
