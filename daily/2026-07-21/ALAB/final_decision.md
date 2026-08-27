FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — ALAB as of 2026-07-21

## Verdict
MODIFY —即時動作為 HOLD（不建新倉），核准一個「事件觸發後」的條件式 LONG 框架。研究側與風險側均無異議：財報前進場缺乏依據，Q2（2026-08-04）為唯一解析點。

## Final trade card (conditional — event-gated)
| Field | Value |
|---|---|
| Direction | LONG（條件式，現持倉 0%） |
| Entry conditions | 事件型（PRICE_DATA_UNAVAILABLE，不設價位）：①FOMC 7/29 未確認激進三次升息路徑、市場消化完畢 → ②Q2 8/4 財報營收 ≥$365M + 非 GAAP 毛利率 ≥73% + Q3 指引優於共識。兩閘門依序達成後，次日開盤穩定（無跳空拉高）分批建倉，不追盤後跳空 |
| Exit conditions | 事件型停損（任一觸發即清倉）：Q2 營收 <$355M、或毛利率 <70%、或管理層下調全年指引、或 MCHP/MRVL 取得超大型雲端業者 PCIe 6 正式設計勝利 |
| Size | Small — **0.20% NAV 上限**（Q3 連續驗證後方可擴至 0.35%） |
| Horizon | 1–3 個月，以 Q2、Q3 財報為里程碑 |
| Conviction | M（偏低） |
| R:R to T1 | 3.0（post-earnings 保守估計；T1 UBS $400、T2 Stifel $460） |

## Risk debate adjudication
- Aggressive 最強點：-27.3% 回檔 + 事件型停損使最差絕對損失極小（~0.02% NAV），非對稱有利。但其「財報前預建倉」在共識均值 $272.47 低於現價 ~$304、無安全邊際下不成立。
- Conservative 最強點：Trailing P/E >300×、內部人士六個月淨賣出 $14M、董事長出售 $60.5M，估值與訊號雙重警示，倉位須硬性壓縮。但其「第三閘門等分析師均值 >$350」具反射性滯後，等同放棄整段財報後上行。
- Net：我採 **Neutral** 為主。0.20% NAV、雙閘門（FOMC 序列前置 + Q2 三指標），既否決 aggressive 的裸露預建倉，也剔除 conservative 過度滯後的第三閘門。核心理由：PRICE_DATA_UNAVAILABLE 使 R:R 無法定量驗證，加上共識無上行安全邊際，任何進場都必須先由財報消除二元不確定性。

## Monitoring trigger
若 FOMC 7/29 確認三次各 +25bps 升息路徑並引發高成長科技股系統性倍數壓縮，即便 Q2 超預期亦全面暫緩；此為進場資格的一票否決條件，須在建倉前重評。

## Conviction score
- 公式：verdict_weight(HOLD=0.3) × conviction_pct(0.55) × (1 + min(R:R,5)/5)（=1.60）× phase_modifier(1.0)
- 計算：0.3 × 0.55 × 1.60 × 1.0 = **0.264 → 26/100**

## Catalyst calendar
- 2026-07-29 — FOMC 會議：升息路徑，宏觀前置閘門
- 2026-08-04 — Q2 2026 財報（盤後）：核心解析點，決定進場資格
- 持續 — 台灣 Cloud-Scale Interop Lab 設計勝利、超大型雲端業者 $450B AI 資本支出確認

FINAL DECISION COMPLETE
