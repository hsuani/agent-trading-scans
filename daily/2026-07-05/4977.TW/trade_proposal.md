# Trade proposal — 4977.TW (眾達-KY) as of 2026-07-05

FINAL TRANSACTION PROPOSAL: **HOLD**

---

## Direction
AVOID（不新建方向性倉位）

研究主管裁定 NEUTRAL / conviction MEDIUM。基本情境上行僅 +9%（至 ~225 NTD），下行情境達 -41%（至 ~121 NTD），風險回報結構嚴重不對稱，且 R:R 至 T1 無論多空均未達准入門檻，故拒絕建倉。

---

## Setup（參考水準，現階段均不觸發）

**假設性 LONG 參考（觸發條件未達，不執行）**

| 欄位 | 數值 | 說明 |
|---|---|---|
| Entry | TWD 195 – 210 | 現價附近區間，等待事件驅動後確認 |
| Stop | TWD 179 | 180 NTD 為融資強平關鍵支撐；收盤跌破論文失效 |
| Target 1 | TWD 225 | 基本情境 +9% 上行；investment_plan 明載 |
| Target 2 | TWD 270 | 5 月高點 270.5 NTD；CPO 量產確認後估值重估上限 |
| R:R → T1 | **0.73x** | **(225−206)÷(206−179) = 19÷27)** 低於 LONG 門檻 1.5x → **拒絕** |
| R:R → T2 | 2.37x | (270−206)÷(206−179) = 64÷27，惟 T2 屬樂觀情境，無法作為主建倉依據 |

**假設性 SHORT 參考（NEUTRAL 主管未授權，不執行）**

| 欄位 | 數值 | 說明 |
|---|---|---|
| Entry | TWD 206 | 現價 |
| Stop | TWD 221 | 220 NTD 阻力區上緣破位即論點失效 |
| Target 1 | TWD 180 | 融資強平支撐 |
| Target 2 | TWD 121 | -41% 下行情境 |
| R:R → T1 | **1.73x** | (206−180)÷(221−206) = 26÷15，低於 SHORT 門檻 2.0x → **拒絕** |
| R:R → T2 | 5.67x | (206−121)÷(221−206) = 85÷15，惟需基本面惡化確認 |

*市場原始技術數據（ATR、RSI、MACD）因代理封鎖 fc.yahoo.com 無法取得；支撐阻力水準引自 investment_plan.md 明確數字。*

---

## Sizing
**0% NAV（不建倉）**

理由：conviction MEDIUM、Forward P/E 41x（非多方宣稱 26x）、R:R 至 T1 不論多空均低於各自門檻、估計 ATR ≈ TWD 7（年化波動率約 55–65%）、品固 28 億元聯貸整合效益未經財報驗證。若觸發條件達成後轉 LONG，建議從 Small（0.5% NAV）試探性建倉，最大不超過 Medium（1.5% NAV）。

---

## Time horizon
3m+（等待 Q2 2026 財報後重新評估；核心基本面邏輯以季度為單位判斷）

---

## Trigger
**現況：Wait（等待）**

轉 LONG 觸發（三項須同時滿足）：
1. Q2 2026 財報（MOPS）確認品固整合毛利率 ≥40%、FCF/NI ≥0.75
2. Broadcom 官方公告眾達為 H2 2026 CPO 量產主要 ELS 來源
3. 月營收連續兩個月 MoM >10%

轉 SHORT / AVOID 加深觸發（任一即可）：
1. 股價月收盤跌破 180 NTD（融資強平潮啟動）
2. 毛利率低於 35% 或 FCF/NI 跌破 0.5

---

## Invalidation
- 多頭論文失效：股價收盤跌破 179 NTD；Broadcom 宣布引入第二 ELS 供應商；CPO 量產延至 2027 年。
- 空頭論文失效：Q2 財報毛利率 ≥40% + FCF/NI ≥0.75 同步確認；月營收加速反彈。

---

## Catalyst calendar
- 2026-08 中旬 — Q2 2026 財報（MOPS 公告）：品固整合毛利率、FCF/NI、EPS 驗證
- 2026-07/08/09 每月 10 日前 — 眾達月營收公告：MoM 趨勢監控
- 2026-Q3（滾動） — Broadcom CPO 供應商生態系公告：ELS 獨家地位確認或稀釋
- 2026-Q3/Q4 — 東莞品基合規進展公告：地緣政治去風險評估

---

TRADE PROPOSAL COMPLETE
