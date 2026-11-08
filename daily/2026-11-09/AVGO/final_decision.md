FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — AVGO as of 2026-11-09

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## 部位性質
AVGO 不在 `pipeline/tools/held_tickers.txt`，屬新倉，採 A 框架（問「該不該進」）。注意帳戶已持有 MRVL（Google TPU 第二供應商，亦是 AVGO 的直接競爭對手）與 ANET，AVGO 進場會提高帳戶層級的 AI 半導體相關性，故不允許在 12-09/10 財報前把部位疊到 Medium 以上。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $291.00 – $296.00（分批，首批不超過總規劃的一半） |
| Stop | $282.00（52 週低點 $289.77 下方約 0.5 倍 ATR14；僅適用非財報交易日） |
| Target 1 | $332.13（MA20） |
| Target 2 | $356.43（2026-07-02 局部低點轉壓力） |
| Size | Small（0.5% NAV）；NVDA 11-17 財報正面可上調至 1%，上調部分優先以 call spread 承接；升至 Medium（1.5%）必須等 AVGO 自家 FQ4 毛利率與 FY27 指引確認 |
| Horizon | 1–3 個月；核心決策點 2026-12-09/10 |
| Conviction | L |
| R:R to T1 | 3.4（以中值 $293.50、停損 $282 計） |

財報跳空處理：12-09/10 財報前一交易日將現股部位減半，剩餘曝險以到期覆蓋財報日的 protective put 或低成本 collar 取代止損單。

## Risk debate adjudication
- Aggressive's strongest point: $284 停損只有 0.4 倍 ATR14 的緩衝，在年化波動 54.7%、兩週內有 NVDA 財報的板塊雜訊下，太容易被洗出去。採納，停損放寬到 $282。但「現在就上 Medium」與低信心評級自相矛盾，三大 crux 一個都沒驗證，拒絕。
- Conservative's strongest point: NVDA 財報只能緩解 Crux 2（CapEx 延續性），無法驗證 Crux 1（AVGO 自身毛利率稀釋）；用別家財報當自己的加碼依據是借用情緒。另外，止損單對財報隔夜跳空沒有保護力。兩點都採納。但以 15–20% 機率的 −35% 尾部情境否定整個進場邏輯，過度。
- Net: I weight **neutral** more here because 雙方其實都不反對 Small 試單，爭點只在加碼節奏與凸性風險處理；neutral 的「NVDA 正面只能小幅上調至 1%、Medium 要等自家財報、財報前減半加 put」正好把 aggressive 的停損空間與 conservative 的雙重確認合在一起，且與 investment_plan 的 LOW conviction 一致。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 半導體營收動能 | FQ4 指引 $34.8B（YoY 約 93%）、FY26 AI 營收約 $58B 可達成 | Q3 營收 +85.5%，指引未下修 | 成立 |
| 現金流品質支撐估值 | TTM FCF $39.4B、FCF/NI 約 1.0、淨負債/EBITDA <1× | 數據可交叉驗證，forward P/E 15.1×、PEG 0.29 | 成立 |
| 毛利率不因客製 XPU 占比上升而明顯稀釋（Crux 1） | FQ4 毛利率與 FY27 EPS 共識守住 forward EPS $19.47 | 待 12-09/10 驗證 | 觀察中 |
| hyperscaler CapEx 延續（Crux 2） | 反資料中心聲浪與 Fed 偏鷹不傳導成訂單下修 | 待 11-17 NVDA 財報 | 觀察中 |
| 技術面止跌 | 放量收復 MA20 $332.13 並站穩 $335.81 | 死亡交叉、MACD hist −3.65 仍擴大、量能未止跌 | 尚未成立（這是進場理由中最弱的一環，也是只給 Small 的原因） |

## 論點失效條件
必須可證偽，且與 Stop 分開（Stop 是價格紀律，這裡是論點紀律）。
- 若 FQ4 財報毛利率較 FQ3 下滑超過 150bp，或財報後兩週內 FY27 EPS 共識下修超過 10%，Crux 1 支柱失效 → 出場，不等價格。
- 若 NVDA 11-17 財報將資料中心下季指引訂在共識以下，或法說會明示 hyperscaler 2027 CapEx 成長轉為個位數，Crux 2 支柱失效 → 減碼至零，轉觀望。
- 若 FQ4 法說會確認 Google 份額流失（如 AI 客戶數目下修、或 Google 合約金額被明示下調），Crux 3 轉為不利 → 減碼一半。
- 若日收盤跌破 $289.77 且三個交易日內無法收復，結構支撐論點失效 → 出清試單（即使尚未觸及 $282）。

## Monitoring trigger
若 11-17 前 AVGO 單日放量跌破 $289.77，或 MRVL 持倉同步出現重挫（顯示板塊性而非個股性賣壓），在止損觸發前先重新評估是否連同 MRVL 一併縮減 AI 半導體總曝險。

## Catalyst calendar
- 2026-11-17 — NVDA FQ3 財報與法說會：Crux 2 第一檢驗點；正面方可上調至 1%
- 2026-12-08（約） — 財報前一交易日：現股減半、建立 protective put 或 collar
- 2026-12-09/10 — AVGO FQ4 FY26 財報（EPS consensus $3.84）：Crux 1 與 Crux 3 核心驗證，決定是否升至 Medium
- 2026-12-09/10（約） — FOMC 12 月決議：偏鷹情境壓縮 forward P/E 空間

FINAL DECISION COMPLETE
