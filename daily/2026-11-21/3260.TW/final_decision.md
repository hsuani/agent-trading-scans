# Final Decision — 3260.TW (威剛 ADATA Technology) as of 2026-11-21

FINAL TRANSACTION PROPOSAL: **HOLD**

---

## Phase-1-only Stub

**訊號評分：0/5 — 不符合正向選股門檻（≥3/5），不進入 Phase 2-4 完整辯論。**

| 訊號 | 結果 | 說明 |
|---|---|---|
| 基本面 | FAIL | DATA_UNAVAILABLE — yfinance financials/balance_sheet/cashflow/insider/holders 全數回傳空值或連線失敗 (403)，無法評估營收成長與 FCF |
| 市場技術 | FAIL | RSI14=18.88 (OK) 但 MACD hist -5.12 深度負值且擴大、價格 $235.50 遠低於 MA50 $349.94 與 MA200 $379.84，死亡交叉已成立 (11-05) |
| 新聞 | FAIL | Net read: mixed，偏空情緒、偏多基本面敘事；公司面消息 (10 月營收 +282.3% YoY、DRAM 缺貨看法) 正向，但 Q4 季減指引、族群重挫與 NAND 現貨急跌等偏空因子並存，不構成淨正向 |
| 情緒 | FAIL | yfinance rec_summary 回傳空值，分析師共識不可得；僅有 1-2 家零散目標價 (420-556 元)，樣本過小且信心度低，無法確認 ≥60% BUY；機構/內部人資料亦缺失 |
| 估值 | FAIL | 基本面資料不可得，無法計算 forward P/E；EPS 成長催化劑 (2027 EPS 預估 84.15 元) 來自單一二手報導，未經驗證，不視為「已確認」catalyst |

**訊號合計：0/5 PASS**

## 結論

威剛基本面資料因 Yahoo 代理連線失敗全面不可得 (DATA_UNAVAILABLE)，技術面呈現明確空頭排列與深度超賣延伸，新聞面多空訊息並存（公司營收與產業缺貨敘事偏多，但 Q4 指引、族群重挫與 NAND 現貨急跌偏空），情緒面無可靠分析師共識樣本。五項訊號全數未達標準，不符合正向選股門檻。

**建議：不進場。待基本面資料恢復 (yfinance 或 MOPS 公開資訊觀測站) 後重新評估，並觀察股價是否站回 $254 (前收) 以上作為止跌訊號。**

## Conviction
**LOW** (0/5 signals)

Score: **2/100**
Score formula: verdict_weight(HOLD=0.3) × conviction_pct(0.05) × (1 + min(R:R=0,5)/5) × phase_modifier(Phase 1 = 0.35) ≈ 0.0053 → 2 (scaled)

---

FINAL DECISION COMPLETE (Phase-1-only)
