# Trade proposal — 2376.TW 截至 2026-08-20

FINAL TRANSACTION PROPOSAL: **BUY**

---

## Direction
LONG — Conviction: **MEDIUM**

論述核心：H1 EPS NT$17.73（+92.6% YoY）財報數據可查，前瞻 P/E 約 10x，相對獲利成長速度存在顯著折價。唯 Q2 毛利率 9.6%（歷史低位，環比 -2.4pp）為決定性不確定因子，主論點需等 2026-08-31 Q3 首月月營收數據驗證。

---

## Setup

無即時價格，暫不給進出場價位。

| 欄位 | 數值 | 說明 |
|---|---|---|
| **Entry** | PRICE_DATA_UNAVAILABLE | Yahoo Finance HTTP 403；market.md 全數缺失，無 S/R 技術水位可參照 |
| **Stop** | PRICE_DATA_UNAVAILABLE | 無技術圖可定義多方論點失效水位 |
| **Target 1 (T1)** | PRICE_DATA_UNAVAILABLE | 研究端 base case NT$456，待市場數據恢復後換算 R:R |
| **Target 2 (T2)** | PRICE_DATA_UNAVAILABLE | 研究端 bull case NT$588，條件為毛利率回升確認 + 估值重估 |
| **R:R** | N/A | 無法計算；市場數據恢復後須確認 R:R ≥ 1.5 方可執行 |

> **注意**：sentiment.md 所載快照價格 NT$393.50 僅供情境參考，不用於設定技術進出場位，不代表交易時點即時價格。

---

## Sizing

**Medium（1.5% NAV）— 起始建倉**；待 Q3 毛利率確認後評估加碼至 Large（3% NAV）。

| 因子 | 評估 |
|---|---|
| Conviction | MEDIUM（獲利數據扎實，但毛利率結構風險未解）|
| ATR | PRICE_DATA_UNAVAILABLE |
| 年化波動率 | PRICE_DATA_UNAVAILABLE |
| 外資動態 | 持股比 17.97% → 13.36%（-4.6pp），顯示派發（distribution）壓力，限制初始規模上限 |
| 投資計畫建議 | 半倉至六成倉起始，與 Medium（1.5% NAV）對應 |

不建議一次性建立 Large 倉位，原因：① 毛利率仍在歷史谷底；② 外資持續結構性減碼；③ ATR 與技術水位因數據缺失無法支撐精準停損設定。

---

## Time horizon

**季度級別（Quarters）**：主要驗證窗口為 2026-08-31 至 2026-10-31（Q3 毛利率數據逐月揭露）。若毛利率回升至 11% 以上確認，持倉可延伸至 FY2026 全年結算（2027 Q1）。不建議以週為單位短線操作，估值重估需時間醞釀。

---

## Trigger

**等待條件（Wait for）**：

主觸發條件（任一）：
1. **2026-08-31 Q3 首月月營收**：毛利率跡象從 9.6% 改善，優先確認方向後入場；或確認惡化則延後或取消。
2. **市場數據恢復**：Yahoo Finance 重新可用後，立即補算 ATR、S/R、R:R，確認 R:R ≥ 1.5 再執行實際建倉。

若以上兩條件均未滿足，**維持觀察，不主動追高**。

---

## Invalidation

以下任一事件發生，立即重新評估並考慮清倉或停損：

- Q3 毛利率持續低於 **9%**，顯示利潤率惡化為結構性而非週期性
- 外資持股比進一步降至 **11% 以下**，反映機構加速派發
- NVIDIA GB300 出貨時程延遲超過一季，影響 H2 出貨量能見度
- AMD Helios 次世代平台核心合作名單確認不納入技嘉，多元化路徑受阻程度超預期
- Q3 EPS 低於 **NT$8**（低於多方預估下緣）

---

## Catalyst calendar

| 日期 | 事件 | 重要性 |
|---|---|---|
| **2026-08-31** | Q3 首月月營收公告（毛利率趨勢關鍵驗證窗口） | ★★★ 最高 |
| **2026 年 9–10 月** | NVIDIA GTC 秋季：Rubin Ultra 次世代 GPU 計畫披露 | ★★★ 高 |
| **2026-10-31 前後** | Q3 完整季報：毛利率、EPS 全面驗證 | ★★★ 高 |
| **2026 年 Q4** | 技嘉 AI Day：新客戶案例、新產品線披露 | ★★ 中 |
| **2027 年 Q1** | FY2026 年度財報：全年 EPS 是否落在 NT$35–42 區間 | ★★ 中 |

---

TRADE PROPOSAL COMPLETE
