# Final decision — IONQ as of 2026-06-30

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY（核准進場，但調整止損與進場觸發條件，並要求 tail hedge）

採用 neutral 平衡方案為基準：維持 0.5% NAV 不擴倉（FCF 疑義未解），亦不縮至 0.25%（探針倉在 T2 失去實質意義）；止損放寬至 $48.50 修正原案邏輯矛盾；進場觸發精簡為兩項。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $52.00 – $55.50（首批 60%，餘 40% 留 $52 以下承接） |
| Stop | $48.50（約 1.5x ATR，仍在 MA200 $44.12 之上） |
| Target 1 | $65.00 |
| Target 2 | $75.00 |
| Size | Small（0.5% NAV）；Q2 財報驗證 FCF -$130M 後可加碼至 1.0% |
| Horizon | 中期 1–3 個月，核心窗口 8 月 Q2 財報 |
| Conviction | M（約 55%） |
| R:R to T1 | 2.1（含 hedge 成本；以中位進場 $53.75、止損 $48.50 計） |

附加：配置約 0.05% NAV 於 IONQ Sep-2026 $45 Put 作 FCF 尾部對沖。CALL SPREAD 為可選增益，非必要。

## 進場觸發（精簡為兩項）
1. 收盤進入 $52–$55.50 且站穩 MA50 $51.35 連續 2 日
2. MACD 柱狀圖連續 2 根收窄
30 個日曆日（2026-07-30）內未觸發則暫停重評。移除量能條件（易滯後）。

## Risk debate adjudication
- Aggressive 最強點：止損 $50.50 僅 0.57 個 ATR，在 ATR $5.67 環境必被雜訊洗出——此邏輯正確，故採其 $48.50。
- Conservative 最強點：FCF -$130M vs -$914M 八倍歧義在 Q2 財報前無法核實，論文整個架構建於浮動假設上——故拒絕擴倉至 1.0%+，並要求 Put 對沖。
- Net：我較重 **neutral**。Aggressive 在 FCF 未解前擴倉 1.25% 是替不確定性付保費；Conservative 縮至 0.25% 又使 T2 $75 失去意義且確認門檻過高導致追高至 $57–59、R:R 跌破門檻。0.5% + 寬止損 + tail hedge 是唯一同時尊重非對稱性與資訊缺口的配置。

## Monitoring trigger
若 IONQ 收盤跌破 MA50 $51.35 後，Quantinuum 公告搶下任一 DoD 或主要雲端合約（直接侵蝕 $470M backlog），立即在 $48.50 止損觸發前重新評估——此為基本面論文破裂信號，技術止損反應過慢。

## Catalyst calendar
- 2026-07（未定）— SkyWater 合併完成公告
- 2026-08 — Q2 2026 季報：單季 OCF、期末現金、Q3 指引（FCF 疑義決勝點）
- 2026-08 — OMB 120 天後量子密碼遷移期限 — Clavis QKD 需求催化
- 2026-09 前後 — Q3 指引：確認成長加速或正常化
- 持續監測 — DoD/DARPA HAQ 合約進展

FINAL TRANSACTION PROPOSAL: **BUY**

FINAL DECISION COMPLETE
