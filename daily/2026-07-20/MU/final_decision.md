# Final decision — MU as of 2026-07-20

FINAL TRANSACTION PROPOSAL: **BUY**

> **PRICE_DATA_UNAVAILABLE**：Yahoo Finance proxy 403，ATR、支撐阻力、MA 均不可得。所有價格欄位一律標示「無即時價格，暫不給進出場價位」，不捏造任何數字。

## 最終裁決
**MODIFY** — 核准方向為 **BUY（LONG）**，但下修規模並強制條件式建倉。
**Conviction：52%**

## 執行摘要
多頭論點建立在已審計的事實（Q3 FY2026 超預期 +24%、Q4 $50B 長約與 $22 億客戶抵押品）與 Forward P/E ~7.5x 對同業折價逾 66% 的估值保護上，方向可做多。但 PRICE_DATA_UNAVAILABLE 使止損無法錨定、SK Hynix HBM4 量產已於 2026 年 6–7 月啟動、36:1 內部人淨賣出三項風險同時存在，故將 Trader 的 1.5%（可加至 3%）下修至 neutral 的 1.0% NAV 目標並採兩段式建倉。

## 倉位規模
- **初始總目標 1.0% NAV**（不即時建足）。
- 第一批 **0.5% NAV**：於 NVDA 2026-08-26 財報前後建立，取得 SK Hynix 供給衝擊即時程度的觀察窗口。
- 第二批 **0.5% NAV**：於 MU Q4 FY2026 財報正面確認後加碼。
- 升至 Large（>1.5% NAV）須待 FCF/NI 回升至 35%+ 且內部人買賣比明顯改善，否則封頂。
- 進場價位：無即時價格，暫不給進出場價位。

## 風險管控（基本面止損，無價格止損）
- **主觸發**：MU Q4 FY2026 營收 <$48B 或 EPS <$31，或管理層下修 FY2027 指引 → 立即縮倉至 0.3% NAV 以下。
- NVDA 2026-08-26 財報 HBM 下季採購指引明顯低於市場預期（暗示庫存累積）→ 暫停第二批加碼。
- 三星 / SK Hynix 宣布 HBM4 大規模量產出貨進一步提前 → 論文核心假設失效，減倉。
- FCF/NI 全年仍 <25% 且無 Capex 收斂計畫 → 拒絕任何加碼。
- 對沖：可配置 MU put spread 或 SOXX put，規模控制在倉位市值 1–1.5%，對沖情境 B 系統性下行。
- 硬止損：待 PRICE_DATA 恢復後，於進場前確立技術止損，(entry − stop) × shares ≤ 0.3% NAV。

## 風險辯論裁決
- Aggressive 最強點：Q3 +24% 為已驗證事實、7.5x 折價提供絕對損失緩衝。
- Conservative 最強點：無止損錨點下 1.5% 承擔不可度量尾部風險；FCF/NI 19.5%、36:1 內部人賣壓具方向性。
- **Net**：採 **neutral** 為主。Aggressive 自承基礎 R:R 僅 0.6x 卻要求 2.5% 即時建倉，與不可度量的止損缺口不相稱；Conservative 0.75% 硬頂則過度放棄已驗證多頭動能。1.0% 兩段式在兩者間取平衡。

## 催化劑時間表
- 2026-08-26 — NVDA Q2 FY2027 財報：HBM 採購量 + 下季記憶體指引（最高）。
- 2026-08 至 09 月（預期）— MU Q4 FY2026 財報：$50B、EPS $31、HBM4 量產時程（最高，論文最終裁判）。
- 持續監控 — 三星 / SK Hynix HBM4 量產進度、美國對華半導體禁令更新。

## 監控觸發（force re-eval before stop）
若 MU Q4 FY2026 財報營收 <$48B 或管理層下修 FY2027 指引，於止損被觸及前立即重評並縮倉至 0.3% NAV 以下。

| metric | value |
|---|---|
| verdict | MODIFY / BUY |
| conviction_pct | 52 |
| size_nav_pct | 1.0 (0.5% + 0.5% staged) |
| r_r_estimate | PRICE_DATA_UNAVAILABLE (方向性 T1 約 +0.6% NAV / 尾部 −1.0% NAV) |
| phase | Phase 4 — Portfolio Manager Final |

PORTFOLIO-MANAGER COMPLETE
