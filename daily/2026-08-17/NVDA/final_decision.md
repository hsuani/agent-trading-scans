FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — NVDA as of 2026-08-17

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

修改的是**倉位授權的模糊空間**，不是方向。方向維持交易員原案（既有部位續抱、新資金不進場），但我把 investment_plan 留下的「若選擇財報前建倉，可用 quarter size 以下」這道後門**關閉**：本輪新資金授權為零，含選擇權變體。

## Final trade card
| Field | Value |
|---|---|
| Direction | 既有部位 LONG 續抱；新資金無方向性授權 |
| Entry zone | 無即時價格，暫不給進出場價位 |
| Stop | 無即時價格，暫不給進出場價位 |
| Target 1 | 無即時價格，暫不給進出場價位 |
| Target 2 | 無即時價格，暫不給進出場價位 |
| Size | 新資金 0% NAV；既有部位不加不減 |
| Horizon | 1-2 週，以 2026-08-26 財報為重評錨點 |
| Conviction | M（長線基本面）/ L（短線方向） |
| R:R to T1 | 無法計算（無真實價格基準） |

market.md 為 PRICE_DATA_UNAVAILABLE。無 ATR、無支撐阻力、無即時股價，任何價位數字都是虛構，一律不填。

## Risk debate adjudication
- Aggressive 最強的一點：技術面缺失是**資料源故障**，不是空頭訊號；把資料真空直接等同於零曝險，確實有把資訊風險誤譯為方向風險之嫌，而 CoreWeave backlog $104.2B、SMCI 上修、BofA $107-108B vs 共識 $91-95B 的落差是真實且有時效的。
- Conservative 最強的一點：無止損依據即無風控框架；縮小倉位只降低曝險金額，**未提供出場觸發機制**，財報後跳空重挫時 quarter size 一樣吃全額跳空。
- Net：我採 conservative，並駁回 neutral 的選擇權折衷。理由是 neutral 自己戳破了 aggressive 的「規模代替止損」，但接著提出的 call spread 同樣落在禁令內——**沒有即時股價就無法選履約價，也無法判斷權利金是貴是便宜**。「最大損失鎖定在權利金」只保證損失有上限，不保證這筆交易有正期望值；在資料真空下建立定義風險部位，等於用已知上限的價格買一個未知賠率。距離二元事件僅約一週，不進場的機會成本是有限的，錯誤定價的成本不是。

## Monitoring trigger
若 **8/26 財報前技術面資料源仍未恢復（即連續兩個掃描週期 market.md 維持 PRICE_DATA_UNAVAILABLE）**，則不等財報、不等止損，主動將既有 NVDA 部位降至核心規模，理由是連續無法重建風控框架本身即為出場理由。此條與財報結果同等優先，非附屬條款。

## Catalyst calendar
- 2026-08-19 — 加拿大關稅生效（宏觀情緒，非半導體直接衝擊）
- 2026-08-26 — NVIDIA Q3 FY2027 財報：Q4 指引是否破 $100B、毛利率是否守 75%、Blackwell/Rubin 交付進度
- 2026-09 — 聯準會政策會議（融資成本影響非超級廠商資本支出意願）
- 2026-09/10 — Rubin 架構上市時程

FINAL DECISION COMPLETE
