# ABBNY (ABB Ltd ADR) — 最終決策 2026-09-04

**分析層級**: Phase 1 Only（未達正面選股門檻）  
**決策人**: orchestrator  
**pipeline 狀態**: Phase 1 完成，Phase 2-4 跳過（quota 保留）

---

## Phase 1 訊號評分

| 訊號 | 結果 | 說明 |
|------|------|------|
| 基本面（營收成長 >15% YoY） | ❌ FAIL | 數據不可用（yfinance 403），新聞推估 Q2 營收成長 10-13%，低於 15% 門檻 |
| 市場技術（RSI/MACD/MA） | ❌ FAIL | PRICE_DATA_UNAVAILABLE（Yahoo Finance 403） |
| 新聞（30 天內正面催化劑） | ✅ PASS | 創紀錄訂單 $120 億、EBITA 20.2%、電氣化/AI 資料中心三位數成長 |
| 情緒（分析師 ≥60% BUY） | ❌ FAIL | 僅 14.3% 分析師 BUY（2/14），Banco BTG 和美銀近期降級 |
| 估值（Forward P/E < 35x） | ❌ FAIL | 數據不可用；但機器人部門已出售給 SoftBank（$5.375B EV），組合已改變 |

**總計：1/5 訊號** — 未達正面選股門檻（需 ≥3/5）

---

## 決策結論

**裁決：HOLD / 觀察名單**  
**倉位建議：0% NAV（不部署新資金）**  
**信心度：20%**  
**phase_modifier: 0.35**（Phase 1-only stub）

### 拒絕理由

1. **分析師共識偏弱**：僅 14.3% BUY，遠低於 60% 門檻；多家大行近期降級
2. **機器人業務已出售**：ABB 已將機器人部門（YuMi/GoFa）出售給 SoftBank $53.75 億，在 robotics 族群中的主題契合度大幅降低
3. **基本面數據缺口**：yfinance 403 + 訓練截止（2025-02），無法確認 Q2 2026 實際財務數據
4. **成長主要來自電氣化**：Rotork 收購 $55 億，業務組合正轉型中，機器人曝險已出清

### 保留看多因子

- 電氣化部門 AI 資料中心訂單三位數成長
- Q2 2026 創紀錄訂單 $120 億
- 股票回購（8 月末）
- 全球工廠自動化市場長期成長（~$175B at 2031）

---

## 評分（dashboard 用）

- verdict: HOLD
- conviction_pct: 20
- phase_modifier: 0.35
- score = 0.3 × 0.20 × 1.0 × 0.35 = **0.021**（極低）
- R:R: N/A（Phase 1 only）

---

**FINAL DECISION COMPLETE — ABBNY Phase 1-only stub**
