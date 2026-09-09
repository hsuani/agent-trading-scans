# Final decision — FCX as of 2026-09-04

FINAL TRANSACTION PROPOSAL: **BUY**

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> **持倉判定**：FCX 不在 `pipeline/tools/held_tickers.txt` → 新倉，走 A 框架，問題是「該不該進」。
> **資料警示**：PRICE_DATA_UNAVAILABLE（Yahoo Finance HTTP 403）。以下價位均為研究文件之結構性估計與分析師共識推導，**非即時報價**；報價來源恢復前不得下單。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $68.00 – $72.00（須待報價恢復確認） |
| Stop | $65.50 |
| Target 1 | $77.00 |
| Target 2 | $92.00 |
| Size | Small（0.4% NAV：首批 0.15%，次批 0.25%） |
| Horizon | 2–3 個月（2026Q3–Q4 催化劑窗口） |
| Conviction | L-M（conviction_pct = 52） |
| R:R to T1 | 1.6 |
| R:R to T2 | 4.9 |
| phase_modifier | 1.0（完整 Phase 2-4 pipeline） |

**Score 計算**
`Score = verdict_weight × conviction_pct/100 × (1 + min(R:R_T2, 5)/5) × phase_modifier`
`= 1.0（BUY） × 0.52 × (1 + 4.9/5) × 1.0 = 0.52 × 1.98 = **1.03**`

**執行條件（缺一不可）**：① 報價來源恢復並確認股價位於 $66 上方；② 銅現貨維持 $6.40+/lb。滿足後投 0.15% NAV。次批 0.25% 僅在 Section 232 精銅關稅力度 ≥15% 確認後投入。至 2026-10-10 條件仍未對齊 → 放棄本次進場，不追高。

## Risk debate adjudication
- **Aggressive 最強論點**：$4.8B capex 為已公開指引，EV/EBITDA 3.8–5.5x 對比行業 5–7x 的折價本身就說明市場已定價此壓縮；且模糊止損比寬止損更危險，必須量化。這兩點我採納——止損明確設 $65.50。
- **Conservative 最強論點**：基礎情境 T1 R:R 僅 1.3–1.6，而尾端下行達 -35% 至 -60%，這是靠 Section 232 二元事件撐起來的不對稱賭注；在 PRICE_DATA_UNAVAILABLE 下先入場後補止損等同盲押。此點我採納——因此壓縮至 0.4% 並設報價恢復為前置條件。
- **Net**：我更偏向 **neutral**。Aggressive 的 1.5% NAV 建立在「B/A = 3.1x」上，但該算式把 T2 當成可達情境處理，而 T2 需要 Section 232 達 25–30% **且** Fed 轉鴿雙重共振，機率遠低於隱含假設；Conservative 的 0.25%／完全等待則放棄了唯一的高賠率窗口。0.4% 分批、明確止損、以催化劑而非價格作為加碼閘門，是唯一同時尊重兩邊的結構。選擇權 call spread 與銅期貨對沖在 0.4% 名目下維護成本不划算，不採用。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 成本護城河 | 現金成本 $1.90/lb，全球前三 | Q2 2026 EPS $0.74 超預期 35%（已審計） | 成立 |
| Grasberg 復產 | H2 2026 達 65% 產能 | 6 月日產 69,000 噸，管理層確認 | 成立 |
| Section 232 政策溢價 | 9 月中旬落地，力度 ≥15% | 未公告，時間與力度均未定 | 觀察中 |
| 銅市結構性赤字 | JPM 33 萬噸缺口支撐 $6.0+/lb | Goldman 反向預測盈餘，未解析 | 觀察中 |
| 2027 FCF 完整性 | FCF 維持高檔 | 指引 capex $4.8B，FCF 由 $8.3B 壓至 ~$3.5B | 已失效（已納入縮倉） |

第五根支柱已失效，這正是倉位由 trader 的 0.5% 降至 0.4%、且拒絕 aggressive 1.5% 的直接理由。前兩根成立的支柱為進場依據。

## 論點失效條件
（與 Stop $65.50 分開；論點先壞就不等價格）
- 若 LME/COMEX 銅庫存**連續兩週**淨增加 → 赤字支柱失效 → **出場**
- 若 Section 232 精銅關稅公告**延後至 2027 年**或力度 <15% → 政策支柱失效 → **出場（未建倉則放棄）**
- 若 Q3 財報 2027 capex 指引上修**超過 $5B** → FCF 支柱進一步惡化 → **減碼至 0.15%**
- 若 Grasberg 日產**連續一季低於 60,000 噸/日** → 復產支柱失效 → **減碼一半**
- 若 C-Suite 再出現任一新增賣出（現況 4 賣 0 買） → 資訊不對稱信號強化 → **不執行次批加碼**

## Monitoring trigger
若 2026-09-18 Fed 傳遞鷹派升息暗示、且銅現貨同步跌破 $6.00/lb，在 Stop $65.50 觸及前即減碼一半。反向：若 Section 232 力度 ≥20% 且 LME 庫存連降三週，可將上限上調至 0.7% NAV。

## Catalyst calendar
- 2026-09 中旬 — Section 232 精銅關稅決議公告（核心二元催化劑）
- 2026-09-18 — Fed FOMC 利率決議
- 2026-10（預計）— FCX Q3 2026 財報：Grasberg 日產、2027 capex 更新
- 每週 — LME/COMEX 銅庫存週報

FINAL DECISION COMPLETE — FCX
