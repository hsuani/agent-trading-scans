FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — MU as of 2026-08-31

> **執行警示**：PRICE_DATA_UNAVAILABLE。以下所有絕對價位均以錨點 ~$930 推算，標示 [UNVERIFIED]，以百分比偏移為準。

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $910 – $955 [UNVERIFIED]（錨點 −2% ～ +3%） |
| Stop | $790 [UNVERIFIED]（entry 中點 −15%） |
| Target 1 | $1,200 [UNVERIFIED]（+29%） |
| Target 2 | $1,515 [UNVERIFIED]（+63%） |
| Size | Small（0.5% NAV 起倉，add gate 後上限 1.0%） |
| Horizon | 4–8 週，硬性重評節點 2026-09-30 Q4 財報 |
| Conviction | M（6 / 10） |
| R:R to T1 | 1.9 |

**修改重點（相對原提案）**：加碼上限由 1.5% NAV 降至 1.0% NAV；否決 Call spread $950/$1,150；新增執行閘門與 fundamentals 資料品質保留。

## Risk debate adjudication
- **Aggressive 最強論點**：-10% Stop 在記憶體股財報前後 15–25% 慣性波幅下不具保護意義，只會被雜訊掃出場。此點正確，Stop 維持 -15%。Put/Call 1.25 屬中度對沖非恐慌，也成立。
- **Conservative 最強論點**：在 PRICE_DATA_UNAVAILABLE 下，實際成交若偏離中點 ±3%，R:R 立即惡化；且 fundamentals.md 明顯是舊資料（假設股價 $80–100、P/E 25–36x），與 investment plan 的 P/E 7.6x 完全衝突——這代表估值支柱目前是**未經獨立驗證的**。此點決定了我不給 1.5% NAV。
- **Net**：本案我採 **neutral** 權重最高。理由是雙方各對一半——Conservative 對「規模」對、對「Stop」錯；Aggressive 對「Stop」對、對「規模與期權」錯。0.5% 起倉 + -15% Stop + 財報後條件式加碼至 1.0%，是唯一同時吸收兩者正確部分的組合。否決 Call spread：財報前 30 天 IV 已含不確定性溢價，0.3% NAV premium 在 0.5% 現貨部位上是不成比例的複雜度。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| HBM 供給緊俏定價權 | 三廠 2026 全年產能售罄，ASP 維持 | 三廠均已確認售罄；Samsung 已與 NVIDIA 建立 GB300 HBM3E 供應關係 | 觀察中 |
| 毛利率結構性維持 | FY2026 Q3 GM 84.9%、Q4 指引 86% | 已公布數字為實，但 FY2027 指引未知 | 觀察中 |
| 估值折讓（隱含 P/E 7.6x） | AI 半導體中罕見低估 | fundamentals.md 為過期資料，無法交叉驗證 | 觀察中 |
| 分析師共識與催化劑時程 | 93% Buy、目標 $1,515、財報 30 天內 | 成立；Mizuho 8/25 下調目標為唯一雜音 | 成立 |

## 論點失效條件
- 若 2026-09-30 Q4 財報之 **FY2027 Q1 毛利率指引 < 75%**，毛利率支柱失效 → **出場**（不等 Stop）。
- 若指引落在 **75%–80%**，支柱轉弱 → **減碼至 0.25% NAV**，取消加碼閘門。
- 若 Samsung 公開宣佈 **HBM3E 良率驗證完成並啟動大規模擴產**，供給支柱失效 → **出場**。
- 若出現 **客戶取消或重談 SCA 長約** 的公開消息（任一份），需求可見度支柱失效 → **減碼一半**。
- 若高管出現 **10b5-1 計畫外的額外大額賣出**（Form 4 揭露），→ **減碼一半**。

## Execution gate（強制）
1. 下單前必須以實時報價確認現價；若現價偏離錨點 $930 逾 ±5%，**本決策作廢**，須重跑定價。
2. 若現價 > $955 [UNVERIFIED] 且無新催化劑，不追高，等回測。
3. 分批建倉，不得一次市價全額打入。

## Add gate
2026-09-30 財報後（當日或次日），同時滿足：(a) FY2027 Q1 GM 指引 ≥ 80%，(b) 無 Samsung 擴產宣告——方可加碼至 **1.0% NAV**，Stop 上移至加碼後成本 −12%。不滿足則維持或依上述失效條件減碼。

## Monitoring trigger
若股價在財報前跌破 **$860 [UNVERIFIED]**（−8%）且無明確消息面歸因，視為機構提前定價壞指引，先減半再等財報。

## Catalyst calendar
- 2026-09-30 — MU Q4 FY2026 財報（FY2027 Q1 毛利率指引為最關鍵單一數字）
- 持續 — Samsung HBM3E 良率驗證與 NVIDIA GB300 供應進度
- 持續 — SCA 合約條款任何公開揭露
- 持續 — 高管 Form 4 申報

FINAL TRANSACTION PROPOSAL: BUY MU 0.5% NAV

FINAL DECISION COMPLETE
