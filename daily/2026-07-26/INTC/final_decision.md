FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — INTC as of 2026-07-26

## Verdict
**MODIFY**（將交易員的「0.5% NAV 試探性倉位」改為事件條件式的零倉位起點）

| 欄位 | 決定 |
|---|---|
| verdict | **HOLD** |
| conviction | **35%** |
| direction | **FLAT**（現階段），條件成立後轉 LONG |
| size_band | **0% NAV（2026-08-04 前）；AMD 財報後條件成立則 0.25–0.5% NAV 上限** |
| Entry | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| T1 | PRICE_DATA_UNAVAILABLE |
| T2 | PRICE_DATA_UNAVAILABLE |
| R:R to T1 | 無法計算（價格數據缺口） |
| Horizon | 2–4 個季度 |

## 最終交易卡
- **現在不進場**。Yahoo Finance 報價來源封鎖（HTTP 403），Entry / Stop / Target 全數為 PRICE_DATA_UNAVAILABLE，無法計算 R:R，本身即構成不得建立方向性倉位的獨立理由。無 R:R 就無倉位，這一條不接受敘事覆蓋。
- **條件式授權**：AMD Q2 財報（2026-08-04）後，若資料中心數據未顯示 INTC 份額進一步結構性流失，且屆時已取得即時報價與 S/R 位階、R:R ≥ 1.5，則授權建立 **0.25–0.5% NAV** 的 call spread（結構參考 $95/$115、expiry 2026-10-16，最大虧損鎖定於 premium）。**不授權現貨多頭**，理由是 stop 位階無法驗證，而已驗證的單日 -10% 波動會使任何未經校準的 stop 被雜訊掃出。
- 上限硬性封頂 0.5% NAV，任何加碼須另行提案。

## Risk debate adjudication
- **Aggressive 最強論點**：18A 良率單季自 65% 升至 85%、Q2 營收 +25% YoY、CEO $21.3M 個人買入——這些是已發生事實而非預期，且 call spread 能把最大虧損錨定於 premium，結構本身正確。
- **Conservative 最強論點**：距 AMD 財報僅 9 天，此期間持倉的正期望報酬近乎為零，承擔的是純單邊事件風險；IFS 外部收入 $174M（佔 3.2%）、單一客戶且用 Intel 4 而非 18A，商業驗證確實落後敘事。
- **Net：我採納 neutral 的裁決。** Aggressive 的結構對、時序錯；Conservative 的時序對、門檻錯（把 $500M/季這個監測指標當成絕對進場條件，會把進場拖到 2027 年，期權性溢價已被定價殆盡）。Neutral 正確拆開了「該不該有敞口」與「何時建立敞口」兩個問題。

## Risk factors（前三）
1. **AMD 資料中心份額續擴**：Q1 2026 已達 $5.8B > INTC $5.1B，Zen 6 只會加劇。
2. **18A 商業量產再延期**：85% 良率距商業門檻 95%+ 仍遠，時程已延一次；若延至 2027 年中後，轉型敘事崩解。
3. **FCF 黑洞**：FY2026 CAPEX $20B+、2027 年再上修，在 EPS 約 $1.52 基礎上 GAAP FCF 幾乎必為負。

## Monitoring trigger
**若 AMD 於 2026-08-04 公布資料中心收入超過 $6.5B 且指引上調，則本條件式授權立即作廢，INTC 轉為 AVOID，不再等待 IFS 客戶消息。** 反向觸發：IFS 宣布第 2 名大型命名外部客戶（AI/伺服器 SoC）——此時重新評估並可提升至上限倉位。

## Catalyst calendar
- 2026-08-04 — AMD Q2 2026 財報（決定條件式授權存廢）
- 2026 Q3 — IFS 第 2 名命名外部客戶公告（若有）
- 2026 Q3–Q4 — 18A 良率 90%+ 與量產 Go/No-Go 決策
- 2026-10 — Intel Q3 2026 財報（IFS 外部收入、毛利率、CAPEX）
- 2026-11-10 — 美國半導體 25% 進口稅暫停期滿

FINAL TRANSACTION PROPOSAL: **HOLD**

FINAL DECISION COMPLETE
