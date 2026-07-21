# Final Decision — 2308.TW (台達電) as of 2026-07-21

FINAL TRANSACTION PROPOSAL: **BUY**

---

## 風險辯論摘要
- **積極派**：月報 +43% YoY 已高度預示 Q2 方向，PEG < 0.7，AI 電源 ASP 結構性提升。主張即刻 0.75% NAV，Q2 後擴至 1.25%。
- **保守派**：Forward P/E 68x 無安全邊際，PRICE_DATA_UNAVAILABLE 使頭寸成為無價格止損的裸倉。主張 0% 等待，確認後才 0.5%，上限 1.0%。
- **中立派**：折衷分階段——即刻 0.5%，Q2（EPS ≥ NT$10、GM ≥ 35%）後擴至 1.0%，事件止損 EPS < NT$8。

三方共識分歧僅在「即時規模」，方向一致 LONG，皆採事件型止損。

## 最終裁決
**MODIFY（下修 Trader 提案）— 採納中立派方案。** Trader 提 0.75% 即刻建倉偏積極：距 Q2 財報僅 9 日、68x P/E 容錯空間極小、且 PRICE_DATA_UNAVAILABLE 使任何即時倉位皆無價格止損。但月報 +43% 與 Q1 EPS +100% 為已實現數字，完全等待（保守派）放棄了驗證前的合理曝險。折衷為最佳風險調整選擇：**即刻 0.5% NAV，7/30 財報二元事件驗證後再定加碼**。這是一筆「先小注、後確認加碼」的事件驅動 LONG，非估值型買進。

## 交易參數
| 參數 | 值 |
|---|---|
| 方向 | LONG |
| 進場規模（即時） | 0.5% NAV |
| 擴倉條件 | Q2 EPS ≥ NT$10 且 GM ≥ 35% → 1.0% NAV；EPS ≥ NT$12 且 GM ≥ 37% → 1.25% NAV |
| 事件止損 | Q2 GM < 33% 或 EPS < NT$8 → 清倉；任一大型 CSP 公開削減 H2 CapEx → 清倉 |
| 目標 T1 / T2 | 無即時價格（PRICE_DATA_UNAVAILABLE）；參考 NT$2,500 / NT$2,857，待價格數據恢復後重設 |

## 關鍵風險
1. **估值容錯極低**：68x Forward P/E 對硬體製造商屬歷史異常，Q2 EPS 稍遜即可觸發 -20%+ 重估。
2. **二元事件集中**：7/30 財報前 9 日，倉位帶賭注性質；故限制即時曝險於 0.5%。
3. **無價格止損**：PRICE_DATA_UNAVAILABLE 下僅能以財報事件觸發止損，跳空風險無技術緩衝。

## Monitoring trigger
若 **2026-07-30 Q2 財報毛利率跌破 33%**（鎵/稀土成本首次侵蝕獲利），立即清倉，不等任何價格訊號。

## Conviction
**MEDIUM** (3/5 signals, P/E 68x 高估值風險)

Score: **58/100**
Score formula: verdict_weight(BUY=1.0) × conviction_pct(0.45) × (1 + min(R:R=1.5,5)/5) × phase_modifier(1.0) ≈ 0.585
（R:R 自 Trader 提案 3.0x 下修至 1.5x，因 PRICE_DATA_UNAVAILABLE 使目標與下行不可驗證，僅認列 LONG 最低門檻）

## Catalyst calendar
- 2026-07-30 — Q2 2026 財報：毛利率、EPS、FY2027 指引（最高優先）
- 2026-08 — 主要 CSP（MSFT/GOOGL/AMZN/META）Q2 CapEx 揭露
- 2026-Q4 — FY2026 全年結算，EPS ≥ NT$39.3 驗證

---

FINAL DECISION COMPLETE
