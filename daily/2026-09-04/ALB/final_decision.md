FINAL TRANSACTION PROPOSAL: **SELL**

# Final decision — ALB as of 2026-09-04

## FINAL TRANSACTION PROPOSAL: **SELL**

## Verdict
減碼

> **PRICE_DATA_UNAVAILABLE**（Yahoo Finance 403）— 本決策不提供任何進場價、停損價或目標價。減碼以「論點紀律」執行,不以價格觸發。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（既有部位,執行部分了結） |
| Entry zone | N/A — 不加碼,PRICE_DATA_UNAVAILABLE |
| Stop | N/A — 無報價,改以下方論點失效條件為紀律 |
| Target 1 | N/A |
| Target 2 | N/A |
| Size | 減碼至原部位 40% 以下（殘餘 ≤ 1.0% NAV,即「半倉以下」） |
| Horizon | 4–8 週,至 Q3 2026 財報（2026-10 初） |
| Conviction | M（conviction_pct = 68） |
| R:R to T1 | N/A（本次為減碼,非開倉） |

**Score calculation**
`Score = verdict_weight × conviction_pct/100 × (1 + min(R:R_T2, 5)/5) × phase_modifier`
- verdict_weight = 0.65（SELL）
- conviction_pct = 68
- R:R_T2 = N/A（減碼動作,無新開倉報酬結構）→ 該項以 0 計,括號項 = 1.0
- phase_modifier = 1.0（完整 Phase 2–4 pipeline）
- **Score = 0.65 × 0.68 × 1.0 × 1.0 = 0.442**

## Risk debate adjudication
- **Aggressive's strongest point**：18.51% SI 是多方的不對稱槓桿而非單純的「不做空理由」;OTM Call Spread（$140/$170,2026-11-21）能把最大損失鎖在權利金內,R:R 2.3x–6.2x 的結構本身無可挑剔。
- **Conservative's strongest point**：P/S 0.5–0.8x 在淨債務/EBITDA 12–20x、FCF 年燒 $2–3B、流動比率 0.7–0.9x 的資本結構下是「槓桿風險溢價」而非安全邊際;加上機構持股 92.87% 的集中度,一旦贖回啟動,下行速度會超出常規波動模型。
- **Net**：我採納 **conservative** 為主、neutral 為輔。理由是本案是持倉決策,不是新倉決策。Aggressive 的不對稱論證只在「零敞口、以有限權利金買樂透」時成立;我們已經有股票敞口,曝險早已建立,再疊加投機多頭等於用一個新賭注去合理化一個支柱已鬆動的舊部位。Aggressive 提議的 0.25% NAV Call Spread **不予採納**。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營運動能（Revenue / EBITDA margin） | Revenue YoY 雙位數成長、margin 維持高檔 | Q2 2026 Revenue +31% YoY（$1.74B）、EBITDA margin 49%、Energy Storage EBITDA +229%,為已實現硬事實 | 成立 |
| 鋰價周期回升 | 鋰碳酸鹽現貨向 CRU Q3 均價 $33,900/MT 收斂 | 現貨僅 $24,086/MT,達標需再漲 +41%;Goldman 預警全球供應過剩 20–22% | 已失效 |
| 賣方與內部人共識支撐 | 目標價維持、管理層與股東利益一致 | 7 家主要銀行掌握完整 Q2 數據後仍集中下調（JPM $160→$140、MS $189→$161、Mizuho $185→$160）;內部人 12 個月淨賣出 $1.4M、90 天零買入 | 已失效 |
| 業務多元化緩衝 | Ketjen 催化劑業務提供非鋰現金流對沖 | 2026 年初剝離後 ALB 已成純鋰周期股,恰逢供應過剩預警,失去對沖 | 已失效 |
| 資產負債表韌性 | 撐過周期低點的財務空間 | 淨債務/EBITDA 12–20x、FCF 年燒 $2–3B、流動比率 0.7–0.9x 低於 1.0x 警戒線 | 觀察中（偏惡化） |

四根支柱中三根已失效,僅營運動能一根成立,且該根屬回顧性數據(Q2 49% margin 更符合「周期頂點確認」而非「起漲訊號」)。依持倉紀律,單靠一根回顧性支柱不足以支撐完整部位——但也不足以構成全數出場,因 18.51% SI 使清倉本身暴露於逼空反向風險。故裁定為**減碼而非出場**,保留殘餘部位跨越 Q3 這一決定性節點。

## 論點失效條件
（與 Stop 分離;Stop 是價格紀律,以下是論點紀律,論點先壞不必等價格）
- 若 **Q3 2026 EBITDA margin < 40% 且管理層下調全年指引** → 營運動能支柱失效 → **殘餘部位全數出場**
- 若 **鋰碳酸鹽現貨連續 4 週低於 $22,000/MT**,確認 Goldman 供應過剩 20–22% 論題 → 鋰價支柱徹底失效 → **出場**
- 若 **流動比率跌破 0.7x**,或公司公告股權融資 / 資產出售 / covenant 豁免申請 → 資產負債表支柱失效 → **立即出場**
- 若 **S&P 或 Moody's 調降至 CCC 區間** → 再融資風險實現 → **立即出場**
- 反向:若 **Q3 EBITDA margin ≥ 45% 且管理層上調指引,且現貨持穩 $30,000/MT 以上（兩條件須同時成立）** → 鋰價支柱恢復,方可評估把減碼掉的部位買回

## Monitoring trigger
若中國鋰碳酸鹽現貨在 Q3 財報前突破並持穩 $28,000/MT,或空頭比例自 18.51% 降至 12% 以下,均需在 Q3 財報前提早重新評估殘餘部位。

## Catalyst calendar
- 2026-09-11 — ALB 股息除權日（$0.41/股）
- 2026-09 每週 — 中國鋰碳酸鹽現貨報價更新（對比 CRU $33,900/MT 目標）
- 2026-10 初（預估）— **Q3 2026 財報暨管理層指引電話會議 — 決定性節點**
- 2026-11-21 — 11 月選擇權到期日（Aggressive 提案之工具期限,本次不採用）
- 持續 — SQM 季度實際出貨量 vs. 240,000 噸年度目標

FINAL DECISION COMPLETE — ALB
