# Neutral risk view — PWR

## Points of agreement (both sides)

- Stop 缺失是原始 trade_proposal 最大的結構性缺陷，雙方均明確指出。
- ERCOT 審計（9 月末）是最關鍵的短期催化劑，方向未明前均不宜全倉建立。
- CEO 26 筆、$120M 系統性套現構成有效警示，不可輕易略過。
- PRICE_DATA_UNAVAILABLE 尚未解除前，任何訂單均不應提交。

## Aggressive overreach

- **Where**：主張立即以 1.5% NAV 建倉，且以未驗證的 $687 作為可執行 entry 錨點。
- **Why**：PRICE_DATA_UNAVAILABLE 是實際執行障礙，非可忽略的細節。在沒有可驗證即時報價的情況下計算 R:R 並下單，是用「論點正確」替代「交易紀律」。此外，Stop $618 距 entry 逾 10%，遠超合理 ATR 緩衝，一旦觸發，單倉損失將超過 conservative 全部方案的承擔上限。空頭覆蓋訊號（short interest 降至 2.6%）是支持論點的補充數據，但不足以抵消價格盲區與監管不確定性的雙重暴露。

## Conservative overreach

- **Where**：主張「PRICE_DATA_UNAVAILABLE 解除前拒絕超過 0.25% NAV 的任何倉位」，並要求 ERCOT 審計完全結案後才考慮升倉。
- **Why**：0.25% NAV 已低於 trade_proposal 自訂的最小倉（0.5% NAV），屬於過度縮減。等待所有不確定性消除才進場，本質上是讓正面催化劑先計價後才進入，系統性削弱 R:R。Stop $640–$655 雖比 aggressive 更合理，但以此作為「等待」的替代品而非立即採用，是合理建議被包裝在過度保守的外殼下。

## Balanced adjustment proposal

- **Size**：0.75% NAV。優先於 trade_proposal 的 0.5%（與 MEDIUM 信心度相符），但不接受 aggressive 在價格盲區直接跳至 1.5%。ERCOT 審計通過後，視 backlog 確認情況升至 1.25% NAV。
- **Stop**：PRICE_DATA_UNAVAILABLE 解除後，技術止損設於 $645（距參考錨點 $687 約 -6.1%）。此位置位於 conservative 建議支撐帶上緣，保留合理震盪空間但不給過寬緩衝。
- **Entry**：僅在取得可驗證即時報價後方可提交。初始建倉 0.5% NAV；ERCOT 無重大懲罰結果後加至 0.75% NAV；Q3 財報確認 backlog > $53B 後評估升至 1.25% NAV。
- **Hedge**：ERCOT 審計結果公告前，買入 PWR 輕微價外 put（1 個月期），成本控制在 0.05% NAV 以內。審計正面通過後可替換為 $700/$820 call spread（到期 2026-12-19）以參與上行空間。
- **Time horizon**：3m+（催化劑依序：ERCOT 9 月末、Q3 財報 10 月中）。

## Net $ risk if stop hits

以 NAV $1,000,000 為基礎：0.75% NAV = $7,500 部位 @ $687 ≈ 10.9 股；止損 $645 → 損失 $42 × 10.9 ≈ **$458（≈ NAV 0.046%）**；加 put hedge 成本 $500 → 最大已知損失 ≈ **$958（≈ NAV 0.10%）**。

## Net $ upside at T1 / T2

- **T1 $836**：$149 × 10.9 ≈ **$1,624（≈ NAV 0.16%）**
- **T2（Q3 後升倉至 1.25% NAV + backlog 確認）**：估算潛在獲利 ≈ **$2,700+（≈ NAV 0.27%+）**
- **R:R（初始）≈ 1.7 : 1**；升倉後接近 **2.5 : 1**，與 MEDIUM 信心度相符。

NEUTRAL VIEW COMPLETE
