FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — AMZN as of 2026-08-19

## FINAL TRANSACTION PROPOSAL: **BUY**（條件式建倉，觸發前不持倉）

## Verdict
**MODIFY** — 方向維持 LONG，但下修 size、下移 stop、加掛尾部對沖，並保留 2026-08-30 觸發條件。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $228 – $240（估算值，見 NOTE） |
| Stop | $208 |
| Target 1 | $280 |
| Target 2 | $326 |
| Size | Small-Medium（1.25% NAV） |
| Horizon | 3–6 個月；Q3 2026 財報為首要評估節點 |
| Conviction | M（60%） |
| R:R to T1 | 1.77 |

補充執行條款：
- **建倉觸發**：2026-08-30 前期業績預告，AWS 指引 ≥35% YoY 且 CapEx 未上調至 $240B+ → 建 1.25% NAV；指引 30–35% → 減至 0.75% NAV；低於 30% 或 CapEx 再上調 → 取消建倉，轉 AVOID。觸發前禁止任何倉位。
- **對沖**：同步買進 PUT 行使價 $200、到期 2027-03，權利金上限 0.10% NAV，覆蓋 FTC 2027-02-09 庭審視窗。
- **Bull call spread 不予批准**：在 PRICE_DATA_UNAVAILABLE 下無法確認真實權利金與價外程度，結構性槓桿缺乏定價依據。

## Risk debate adjudication
- **Aggressive 最強論點**：Conservative 的 stop $220 距入場中點僅 -6%，遠低於 AMZN 年化 25–30% 波動所對應的合理季度緩衝，等同讓噪音替基本面做出場決定。此點成立，故止損採 $208 而非 $220。
- **Conservative 最強論點**：所有價位皆為分析師目標反推，無 ATR、無技術支撐確認；疊加內部人 7–8 月集中賣出 $346.97M、12 個月零買入，且 92% 分析師 BUY 屬擁擠交易。在此執行基礎上放大至 2.5% NAV 不具正當性。
- **Net**：我採 **neutral** 權重最高。基本面錨點（AWS +36.7%、合約負債 $496B）確實硬，但這是論文層優勢，不能補償執行層的價格盲區。Aggressive 主張「等 11 天損失 Alpha」預設預告必為正面，屬結果偏誤；Conservative 則將執行層缺陷誤植為論文層否定。1.25% NAV + stop $208 + PUT 對沖，是唯一同時尊重兩者有效批評的組合。

## Monitoring trigger
**若 2026-08-30 預告揭示 CapEx 全年指引上調至 $240B+，或 AWS 指引低於 30% YoY，立即取消／平倉，不等 $208 止損被觸及。** 此二者直接推翻投資計畫的兩大 crux（FCF 轉換效率、AWS 成長持續力）。

## Catalyst calendar
- 2026-08-30 — 第三季前期業績預告：AWS 指引 + CapEx 執行進度（建倉觸發點）
- 2026-09-XX — Anthropic 融資更新 / AWS AI 基礎設施公告
- 2026-10-XX — Q3 2026 正式財報（首要評估節點；驗證後方可加至 1.5% NAV）
- 2027-02-09 — FTC 反壟斷庭審開庭（中期尾部風險邊界）

```
TICKER:     AMZN
DATE:       2026-08-19
VERDICT:    BUY
CONVICTION: 60%
DIRECTION:  LONG
ENTRY:      $228 – $240（估算區間，非驗證市場報價）
STOP:       $208
TARGET_1:   $280
TARGET_2:   $326
SIZE:       1.25% NAV
HEDGE:      PUT $200 Mar 2027，權利金上限 0.10% NAV
PHASE:      Phase-1-through-4
REASON:     AWS +36.7%（18 季新高）與 $496B 合約負債構成可驗證的硬數據錨點，支撐 LONG 方向；惟 CapEx $220B 的 FCF 短壓、內部人淨賣出與 FTC 尾部風險，要求以縮減 size 及尾部對沖取代滿倉押注。
NOTE:       PRICE_DATA_UNAVAILABLE — Yahoo Finance 代理 403，所有價位均由分析師共識目標 $326.07 與隱含現價 ~$234 反推而得，無 ATR、無技術支撐確認。執行前交易員必須以實際成交價重校 entry/stop；若真實現價偏離 $234 逾 5%，止損須按相同 -11% 比例重設而非沿用絕對值。
```

FINAL DECISION COMPLETE
