# Final decision — 3231.TW (緯創資通/Wistron) as of 2026-07-23

FINAL TRANSACTION PROPOSAL: **BUY**

> ⚠️ PRICE_DATA_UNAVAILABLE：yfinance proxy 403 封鎖即時行情。價格錨點以 sentiment.md 確認之 NT$164（7 月下旬）為基準；止損以百分比表示，禁用絕對 NT$ 數字。

## Verdict
APPROVE（採 neutral risk 折衷方案為最終定案）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 市價 ~NT$164 參考（分批） |
| Stop | Entry 下方 12% |
| Target 1 | NT$206（+26%，分析師共識中位） |
| Target 2 | NT$225（+37%，UBS 目標） |
| Size | Medium — 總 1.25% NAV（分兩批） |
| Horizon | 1–2 季（核心窗口 2026 Q3–Q4） |
| Conviction | M（70–75%） |
| R:R to T1 | 2.17x |
| Risk score | 3 / 5 |

### 分批執行
- 批次一 **0.75% NAV — 即刻市價執行**：Fort Worth D1 廠 48 小時前開幕，催化劑尚未定價；FactSet EPS NT$13.72 對應 P/E ~12x，相對 +94.1% H1 YoY 成長仍顯著低估，無須等待。
- 批次二 **0.50% NAV — 觸發加碼**：8/10 TWSE 月營收 YoY ≥ 40%。

## Risk debate adjudication
- Aggressive 最強論點：高波動率（9 日 +14.3%）本身是「更寬止損 + 較大規模」的理由，8% 止損必被雜訊洗出——此點成立，故採 12% 止損而非保守方 8%。
- Conservative 最強論點：PRICE_DATA_UNAVAILABLE 使 vol-adjusted sizing 全盲，EPS 若貼近 FactSet NT$13.72 則 P/E 已 12x 非 9.6x，安全邊際縮窄——此點成立，故拒絕 aggressive 的 2.5–3% NAV 與 call spread。
- Net：weight **neutral** 較重。理由：方向無分歧，真正爭點在規模與時點。aggressive 的三倍擴倉在技術面全盲下屬情緒性偏誤；conservative 取消即刻進場等於讓渡 Fort Worth Alpha。1.25% NAV + 12% 止損 + 即刻建基礎倉是唯一與 70–75% 信念、資訊品質同時相稱的解。EPS 基準採 FactSet NT$13.72（非 UBS NT$17），UBS 為上行情境。

## Monitoring trigger
若 **8/10 TWSE 7 月月營收 YoY < 40%**，趨勢斷裂，在止損觸發前即縮倉至計畫 30–40% 並重評方向；此為批次二之反向失效節點。

## Exit conditions
1. 8/10 月營收 YoY < 40% → 縮倉、重評。
2. Q2 法說會 GM guidance < 5.5% → 退出剩餘倉位（「以量換質」坐實）。
3. Vera Rubin 德州第二產線未能於 2026-09 如期點火 → T2 廢止、下修。
4. 機械式止損：跌破 Entry 下方 12%，無論基本面出場（滿倉最大損失 1.25% × 12% = 0.15% NAV）。

## Catalyst calendar
- 2026-08-10 — TWSE 7 月月營收公告（批次二觸發）
- 2026-08 中 — Q2 法說會：GM guidance + H2 展望（極高）
- 2026-09 初 — Fort Worth D1 Vera Rubin 第二產線量產點火
- 2026-10-10 — TWSE 9 月月營收（驗證出貨動能）
- 2026-11 中 — Q3 法說會：GM 與 FY2027 EPS 指引

FINAL DECISION COMPLETE
