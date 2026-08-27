# Final decision — 3163.TWO（波若威）as of 2026-07-21

FINAL TRANSACTION PROPOSAL: **SELL**

> **無即時價格，暫不給進出場價位。** Yahoo Finance 遭封鎖（HTTP 403），全程 PRICE_DATA_UNAVAILABLE。所有進出場條件一律採事件驅動（event-driven），不設任何數值價位或止損。

## Verdict
MODIFY

維持空側方向與 event-driven 架構，但拒絕 Aggressive「今日建倉、上調至 0.5% NAV」，也拒絕 Conservative「完全零倉」。定稿為 **AVOID 新建多倉 ＋ 事件確認後可啟動 ≤0.3% NAV SHORT**。

## Final trade card
| Field | Value |
|---|---|
| Direction | SHORT（tilt，非核心倉） |
| Entry zone | 無即時價格，暫不給進出場價位；僅事件觸發 |
| Stop | 無數值止損；改用消息面即時回補（見下） |
| Target 1 | 事件觸發：估值向保守共識回歸（定性） |
| Target 2 | 事件觸發：CPO 里程碑跳票後估值重置（定性） |
| Size | Small ≤0.3% NAV |
| Horizon | 中期 3～6 個月 |
| Conviction | M |
| R:R to T1 | N/A（無報價，記為 0） |

**建倉觸發**：2026-08-10 前後 7 月月營收公告，確認 YoY 續跌且無 CPO Power-on 正面消息。
**回補觸發（任一）**：月營收 YoY 轉正且 MoM +15% 以上；三大法人單週淨買超逾 200 張；NVIDIA 官方公告 Spectrum-X CPO 具體量產配額且波若威為主要受惠方；CPO Power-on 成功並附具體出貨量。

## Risk debate adjudication
- Aggressive 最強點：空方四訊號（估值溢價 52%、6 月營收 YoY -11.53%、破 MA5/MA20、法人淨賣超 155 張）今日已同向成立，等待有折現流失風險。
- Conservative 最強點：NVIDIA「指名供應商」為官方背書之正面催化劑，在無即時報價、無盤中監控下裸空的尾部軋空不可控。
- Net：本案採 **Neutral** 為主。Aggressive 混淆「基本面確信度」與「執行可見性」，PRICE_DATA_UNAVAILABLE 下擴大倉位只放大尾部曝險、不改善 R:R；Conservative 高估執行盲點（0.3% NAV 即使單日 +50% 亦僅 0.15% NAV 損失，未破風控上限），零倉則放棄真實不對稱 Alpha。0.3% NAV ＋ event-driven ＋ 消息面回補，是唯一同時尊重估值確定性與軋空尾部的解。

## Monitoring trigger
若 2026-08-10 前後，任何 NVIDIA CPO 供應鏈正面媒體報導或 Power-on 提前成功傳聞出現（早於月營收硬數據），立即在無數值止損下市價回補全部空側曝險並重評方向。

## Catalyst calendar
- 2026-08-10 前後 — 7 月月營收公告（第一決定性驗證點）
- 2026-Q3 — CPO「Power-on」小量試產結果
- 2026-Q4 — CPO 月產能「千級」達標驗證
- 2027-Q1 — 月產能「萬級」挑戰

## FINAL SCORE
- verdict_weight：0.65（SELL / short tilt）
- conviction_pct：0.58
- R:R T2：0（PRICE_DATA_UNAVAILABLE）
- phase_modifier：1.0（full pipeline）
- **Score = 0.65 × 0.58 × (1 + 0) × 1.0 × 100 = 37.7**

FINAL DECISION COMPLETE
