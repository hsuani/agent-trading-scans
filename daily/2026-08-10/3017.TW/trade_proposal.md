# Trade proposal — 3017.TW (奇鋐) as of 2026-08-10

FINAL TRANSACTION PROPOSAL: **HOLD**

---

## Direction

AVOID（財報二元事件前，不建立新倉）

---

## 不進場理由

**核心判斷：48小時後即有 Q2 財報公布（2026-08-12），在 PRICE_DATA_UNAVAILABLE 且高度不對稱二元事件成立的前提下，任何新倉的 R:R 均不符合交易門檻。**

### 1. 價格資料缺失，無法定義交易參數

market.md 回傳 PRICE_DATA_UNAVAILABLE（Yahoo Finance 403 proxy block）。當前股價、ATR14、支撐／阻力位均無法確認，無法計算有效的 Entry / Stop / Target，亦無法評估 R:R。在無法確認 Stop 的情況下，不進場是唯一符合風控規範的決策。

情感面僅提供分析師目標價（[APPROX] NT$3,090–$3,540，來源：sentiment.md 法人調查，非即時市場價格），無法作為交易 Entry 基礎。

### 2. 財報二元事件風險不對稱

- **2026-08-12**：董事會討論 Q2 合併財務報表，為 48 小時內最直接的股價催化劑。
- 多方情境：Q2 EPS ≥ NT$22 元 + 管理層給出正面 Rubin 液冷指引 → 財報後確認支撐再建 LONG。
- 空方情境：Q2 EPS < NT$18 元或管理層對 Rubin 過渡期訂單遞延表示疑慮 → 財報後評估 SHORT 或繼續 AVOID。
- 財報前建倉等同「猜測硬幣正反面」，且 100% BUY 分析師共識意味升評子彈耗盡，任何低於高預期的結果均可能引發非線性賣壓。

### 3. 板塊系統性分配訊號

8 月散熱三雄集體跌幅逾 20%（investment_plan.md），屬系統性資金流出（distribution），並非個股雜訊。在板塊資金流向未明確逆轉前，逆勢建倉需要財報後業績確認作為觸媒支撐。

### 4. 估值溢價確認困難

sentiment.md 顯示 2026 年 EPS 共識中位數 NT$93.75 元，H2 每季需平均 EPS NT$26.7 元以上方可達標，在 Rubin 過渡期不確定性及越南新廠爬坡風險下，估值壓縮風險無法在 PRICE_DATA_UNAVAILABLE 情境下量化。

---

## 財報後行動框架

| 情境 | 條件 | 行動方向 |
|------|------|----------|
| 超預期 | Q2 EPS ≥ NT$22 元，H2 指引正面，Rubin 供應時間確認 | 財報後再評估 LONG，重新建立交易計畫 |
| 符合預期 | Q2 EPS NT$18–22 元，指引中性 | 持續觀察技術面，等待明確方向突破 |
| 低於預期 | Q2 EPS < NT$18 元或管理層對 H2 訂單遞延示警 | 評估 AVOID 或 SHORT；熊市參考目標 [APPROX] NT$1,600（20× EPS NT$80，來源：investment_plan.md 估算，非即時價格） |

---

## Sizing

不適用（AVOID，財報前零新倉）。

conviction: L，ATR: PRICE_DATA_UNAVAILABLE，vol: PRICE_DATA_UNAVAILABLE。

---

## Time horizon

短期 1–4w（財報後 2–4 週內視業績品質與技術面反應重新評估）

---

## Trigger

Wait for 2026-08-12 Q2 財報公布後，依數字品質與管理層 Rubin 液冷指引重新建立交易計畫。

---

## Invalidation

若財報前股價出現明顯技術突破（需待 PRICE_DATA_UNAVAILABLE 解除後確認），且 Q2 提前洩漏超預期業績訊號，可重新評估是否於財報前建立極輕倉試探（不超過正常配置 1/4）。

---

## Catalyst calendar

- **2026-08-12** — 奇鋐董事會討論 Q2 2026 合併財務報表，公布第二季營收與 EPS；管理層 Rubin 液冷供應時間表說明為最關鍵觀察點。
- **2026-08-XX** — 越南廠第 7、8 期廠房投產進度更新（2026 上半年預計投產，爬坡狀況將影響 H2 產能釋放節奏）。

---

TRADE PROPOSAL COMPLETE
