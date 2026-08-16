FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — QUBT as of 2026-08-11

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY — 今日不發送任何委託單；但將交易員的無條件 HOLD 修改為「附硬性價格閘門的預授權 call spread」。閘門未通過即維持零倉位。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（defined-risk call spread，非股票） |
| Instrument | QUBT $10 / $18 call spread，expiry 2027 Q1 |
| Entry zone | 僅在確認即時成交價（非快取）落於 $7.80 – $10.55 時執行；價格 > $11.00 一律不進場；premium 上限 $1.50/spread |
| Stop | 標的跌破 $6.00（現金底線 $6.25 下方）即平倉；結構性 max loss = 已付 premium |
| Target 1 | 標的 $14.00（spread 部分了結 50%） |
| Target 2 | 標的 $18.00（spread 到期滿值 $8.00） |
| Size | Small — 0.125% NAV（eighth-size，以 premium 計） |
| Horizon | 2 – 3 季（2026 Q3 – 2027 Q1） |
| Conviction | L |
| R:R to T1 | 約 2.5（premium $1.20 假設下） |

執行紀律：價格閘門為一次性、非自行裁量。若行情源恢復後現價超出區間，本授權作廢，須重新提案。

## Risk debate adjudication
- Aggressive's strongest point：$130M 現金構築的 $6.25 底線是真實結構性下檔，且改用 call spread 後 max loss 固定為 premium，把「ATR 不可得無法 sizing」這個反對意見直接解構掉。此點在邏輯上成立。
- Conservative's strongest point：收入 QoQ +51%、淨虧損 QoQ +191%、opex 達收入 3.9 倍，加上六個月三宗併購尚未交出整合答卷——虧損加速是結構性而非過渡性。這是關於標的本身的事實，不會因為換成期權結構而消失，只會使 $18 履約價的達成機率被系統性高估。
- Net：我採納 neutral 較多。真正的約束既不是估值也不是波動率，而是無法定價的輸入變數：沒有確認的 spot 與 IV，就無法計算 premium，R:R 5:1 只是假設價 $9.18 成立下的推導，不是可執行數字。Aggressive 用未確認價格推出的 3.1:1 屬地基不穩；Conservative 的「完全 AVOID」則放棄了一個 max loss 已定義、成本僅 0.125% NAV 的二元事件曝險。折衷解是預授權加硬閘門。

## Monitoring trigger
若 Q3 2026 財報（預估 2026 年 11 月）季度淨虧損超過 $15M，或期間公告任何稀釋性股權融資，立即撤銷本授權並平倉，不等 $6.00 標的止損線。

## Catalyst calendar
- 2026-11（預估）— Q3 2026 財報：毛利率是否首次轉正、Fab 1 毛利轉正時間表
- 持續 — Planck Dynamics 5 套 NeuraWave 交付與客戶驗收確認
- 2026 Q4 – 2027 Q1 — 100 套 NeuraWave 框架協議批量觸發進度
- 持續 — 美國國防量子預算 $5.67 億撥付與 QUBT 新合約

FINAL DECISION COMPLETE
