FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — AVGO as of 2026-08-31

## Verdict
MODIFY

（新倉。BUY MODIFIED：方向與論點通過，倉位、止損、目標與對沖結構被我改寫。）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 錨點 −2% 至 +1%（隱含 ~$362–$373） |
| Stop | 錨點 −6.0%（隱含 ~$347，收盤價確認） |
| Target 1 | 錨點 +18%（隱含 ~$435） |
| Target 2 | 錨點 +34%（隱含 ~$495，52週高） |
| Size | 財報前 Small 0.5% NAV → 財報後最高 Medium 2.5% NAV |
| Horizon | 近期 1–4 週（財報窗口）；中期 1–3 個月（TPU v7 量產） |
| Conviction | 6.5 / 10（M） |
| R:R to T1 | 3.0 |

**Hedge（強制，非選配）**：財報前同步買入 OTM Put，行使價約錨點 −8%，到期 2026-09-09，權利金上限 0.02% NAV。跳空尾部總損失因此上限化在約 0.055% NAV。**不執行 Call Spread**——1.0% NAV 權利金押在 48 小時二元事件上是買樂透，不是配置。

## Risk debate adjudication
- Aggressive's strongest point：財報前 48 小時確實是最後的定價窗口，等確認後在 +10~18% 跳空處追進會吃掉大半 entry edge。這點我採納了——所以我不縮到 0.25%，維持 0.5% 立即執行。
- Conservative's strongest point：−5.1% 止損對跳空缺口完全失效，2024-12-13 單日 −26% 是已發生的先例。止損在二元事件前是紀律幻覺，不是保護。這點我採納了——所以強制 Put 對沖。
- Net：我採 **neutral** 較多。Aggressive 自相矛盾——把止損從 −5.1% 放寬到 −7.0% 對跳空一樣無效，卻用它來合理化 4 倍倉位。Conservative 的 0.25% 在 R:R 3x 設定下等同放棄。真正的解法不在倉位大小或止損寬窄，而在改變損失分佈的形狀：小倉 + Put 上限化。
- **我否決了原提案的 R:R 6.7–8.4x**：用 1–4 週的止損搭配 12 個月的分析師共識目標算 R:R 是尺度錯配。T1 下修至 +18%、止損放寬至 −6.0% 後，誠實的 R:R 是 3.0——依然值得做，但不是「罕見設定」。Conviction 也因此從 7 降至 6.5。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI ASIC 積壓訂單能見度 | $73B、Meta 合約至 2029、六大 XPU 客戶 | 來源可查（Bloomberg/CNBC 2026-04-14） | 成立 |
| Q3 AI 半導體收入動能 | AI 收入 ≥ $160 億、YoY +200% | 9/2 才揭曉，指引由 IR 8/22 確認 | 觀察中 |
| 估值折價 | Forward P/E 18–22x vs NVDA 35–40x | 折價仍在 | 成立 |
| 槓桿去化 / 客戶集中度 | Net Debt/EBITDA 降至 3.5x；Google 維持 AVGO 主導 | VMware 軟體僅 +9%、Google 引入 MediaTek | 觀察中 |

## 論點失效條件
- 若 Q3 AI 半導體收入 < $130 億，或 Q4 指引低於 $160 億，動能支柱失效 → **全數出場**（不等 stop）
- 若 Google 或 Meta 公開確認縮減下一財年 XPU 訂單量，集中度支柱失效 → **出場**
- 若軟體業務連續兩季 YoY < 10% 且 Net Debt/EBITDA 未降至 3.5x 以下，槓桿支柱失效 → **減碼至 1% NAV 以下**
- 若 Google 正式宣布 MediaTek 承接下一代 TPU 主要設計 → **出場**

## Key execution gates
1. **價格錨點確認（前置條件）**：下單前必須確認實際市價在 ~$369 ±3% 內。若實際價格偏離錨點超過 3%，全部 % 位階作廢，本決策**不執行**，退回重算。
2. Put 對沖必須與股票部位**同一交易日**成交；Put 未成交則股票部位不建立。
3. 財報前絕對上限 0.5% NAV，無任何例外。
4. 財報後加碼須**同時**滿足：AI 收入 ≥ $160 億 **且** Q4 指引 ≥ $170 億 **且** 等待 1–2 個交易日日間量價結構確認（非盤後情緒）。分兩批加至 2.5% NAV。條件未全滿足則維持 0.5% 或減碼。

## Monitoring trigger
若 9/2 盤後 AI 收入落在 $130–160 億的模糊帶（達標未超標），不觸發加碼也不立即出場：改為 0.5% 維持、觀察 9/3–9/8 是否守住 200日SMA（錨點 −2.2%），跌破即減至零，不等 −6% stop。

## Catalyst calendar
- 2026-09-02（盤後）— Q3 FY2026 財報：AI 收入分項、Q4 指引、2027 展望
- 2026-09-09 — 對沖 Put 到期
- 2026-Q4 — Google TPU v7（Ironwood）N3P 量產出貨
- 2026-Q4 至 2027-Q1 — Net Debt/EBITDA 降至 3.5x，解鎖資本返還
- 持續 — VMware CVE-2026-59310 修補進度；半導體關稅 25% 立法進程

FINAL DECISION COMPLETE
