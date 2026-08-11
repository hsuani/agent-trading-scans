# Sector report — Cooling & AI Infrastructure as of 2026-08-12

## 資料限制說明（必讀）

**PRICE_DATA_UNAVAILABLE 全面適用**：Yahoo Finance 代理封鎖（HTTP 403）導致全部 9 支標的無即時報價、ATR、RSI、MACD、BB %B。MOD、ANET、COHR 為已持倉標的，完成 Phase 2-4 完整流程；VRT、LITE、FN、AAOI、IPGP、GLW 為 Phase-1-only stubs（news/sentiment 各 1 分，共 2/5，未達正向門檻 3/5），財務與技術面數據全缺。所有進出場價位均為 PRICE_DATA_UNAVAILABLE，執行前須以 Bloomberg 或其他數據源補價並自行驗證 R:R ≥ 1.5 方可下單。

---

## Ranking table

| Rank | Ticker | Verdict | Conviction | R:R | Size | Horizon | Trigger |
|------|--------|---------|------------|-----|------|---------|---------|
| 1 | ANET | BUY | M (60%) | N/A* | 1.0% NAV | 1-3m | NVIDIA 8/26 業績確認 AI capex 動能延續 |
| 2 | MOD | BUY | M (60%) | ~2:1（定性） | 0.5% NAV 首批 | 1-3m | Jackson Hole 8/13-15 無鷹派意外 + 量縮止穩 |
| 3 | COHR | HOLD → 條件式 SHORT | M (55-60%) | 2.5-3.5×（put spread） | 0%今日；0.5% NAV 財報後 | 4-6w | FQ4 財報雙觸發（8/12 盤後） |
| 4 | VRT | HOLD/SKIP | L (30%) | N/A | — | — | 待數據恢復後重評 |
| 4 | LITE | HOLD/SKIP | L (30%) | N/A | — | — | 待數據恢復後重評 |
| 4 | FN | HOLD/SKIP | L (30%) | N/A | — | — | 待數據恢復後重評 |
| 4 | AAOI | HOLD/SKIP | L (30%) | N/A | — | — | 待數據恢復後重評 |
| 4 | IPGP | HOLD/SKIP | L (30%) | N/A | — | — | 待數據恢復後重評 |
| 4 | GLW | HOLD/SKIP | L (30%) | N/A | — | — | 待數據恢復後重評 |

\*ANET R:R 因 PRICE_DATA_UNAVAILABLE 無法計算，數據恢復後以 ATR×2 重算，未驗證前不加倉。

---

## Top 3 BUY picks

本次掃描僅 2 支標的達到 BUY 結論，無第三 BUY 名額。

**#1 — ANET（共識首選）**：Q2 2026 收入 $3.04B（YoY +40%，超預期 7.4%），EPS 超預期 13.3%，FY2026 指引上調至 $12.6B；Oracle 晉升 10%+ 大客戶，分析師 97% 維持買入。1.6 Tbps 液冷交換機平台精準卡位 2026 底至 2027 年換機週期。進場條件：NVIDIA 8/26 業績須同時滿足①AI capex 動能延續、②未揭示 Google/Oracle 大規模替換 ANET 交換機，缺一則取消建倉。核心風險：NVIDIA 已於 IDC Q1 2026 奪得資料中心乙太網交換機收入第一；CEO 44 筆共 $307M 密集出售、全公司 $40 億淨拋售。

**#2 — MOD（逆向機會兼具）**：數據中心收入 YoY +90%，$40 億五年容量協議（$1.65 億預付款已入賬），8 位分析師 100% 買入，共識目標 $310.29（隱含 +58.6%）。財報後已跌 14.43%，部分消化失望情緒，形成相對合理進場視窗。進場條件：Jackson Hole（8/13-15）無鷹派意外 + 一至兩日量縮止穩；首批 0.5% NAV，停損設進場價 -10%（硬性）。核心風險：Q1 FY2027 毛利率惡化 340 bps 至 20.8%；內部人士 12 個月淨賣出 $21M；$40 億協議為容量預訂非不可撤銷訂單，單一客戶集中度高。

---

## SELL/AVOID picks

**COHR — 今日 HOLD，財報後條件式做空**：空方硬數據佔優——26 次內部人賣出、零買入，CFO Sherri Luther 於 $306-$354 大量出貨；七日急漲 70%（$222→$325）已提前定價最佳情境，上行空間僅 +18%，但估值還原下行達 -42% 至 -57%；GF Value 溢價 338%；Citi 目標 $136、Barclays 目標 $170 遠低現價。今日 FQ4 財報（盤後 4:30 ET）若出現以下任兩項負面觸發：①營收 < $1.98B、②Non-GAAP 毛利率 < 39%、③FY2027Q1 指引未加速，則次一至兩個交易日建立 long put spread（0.5% NAV 上限，4-6 週，R:R 2.5-3.5×）。

---

## 逆向操作（Contrarian pick）

**MOD**：主流市場因毛利率惡化（340 bps）與內部人賣出而保守觀望，但液冷數據中心全棧整合架構（AbsolutAire、L.B. White、Climate by Design International 三次收購）與五年協議的真實收入能見度為同業所無，且 8 位分析師共識在財報後並未根本性轉向。財報後 -14.43% 跌幅已提供修正後的進場點，若 Jackson Hole 無鷹派意外，這是搶在 Q2 FY2027 毛利率驗證前低成本試入的非對稱機會。

---

## Pairs trade

**Long ANET / Short COHR（via put spread）**

兩者均深度曝險於 AI 資料中心網路與光學基礎設施，但相對價值分歧鮮明：ANET 基本面持續加速（首個 $3B 單季、指引上修）；COHR 估值過度擴張（GF Value 溢價 338%）、內部人賣壓沉重。此配對可隔離整體 AI capex 宏觀波動，聚焦於估值合理性與管理層行為的相對差距。執行序：先等 COHR 財報確認雙觸發後啟動空側，再於 NVIDIA 8/26 業績後建立 ANET 多側。

---

## 全板塊觀察

- **共同催化劑**：NVIDIA Q2 FY2027（8/26）為跨冷卻、交換機、光學三子板塊最大共同讀數指標；COHR FQ4（今日盤後）為光學先行指標；Jackson Hole（8/13-15）影響利率敏感估值框架
- **共同風險**：Big-5 廠商資本強度已達營收 48-57%（歷史頂部位區），AI capex 週期轉折疑慮升溫；電力基礎設施瓶頸估計延遲 30-50% 的 2026 年數據中心容量至 2028 年；FCC 中國光學收發器禁令草案若延遲或縮水，COHR、LITE、AAOI、FN 估值整體重新定價
- **擁擠警示（Crowding）**：VRT、ANET、COHR、LITE、AAOI 高度集中於「AI 資料中心基礎設施」主題，ANET 機構持股 82.47%；主題去評等時同步下行風險顯著
- **相關性群組**：①光學/收發器（COHR、LITE、AAOI、FN）— 共同受 FCC 禁令草案與 1.6T 換機週期驅動，避免同時集中曝險；②冷卻/熱管理（MOD、VRT）— 超大規模 CapEx 直接受益，兩者高度同向；③交換機（ANET）— NVIDIA 競爭為主要區分因子，與光學群相關但非完全同步；④材料/光纖（IPGP、GLW）— 相對獨立驅動，Phase-1 數據不足，暫無法評估

---

## 行動優先序

1. **COHR 財報監測（今日最優先）**：雙觸發成立 → 次日建 long put spread 0.5% NAV；超預期強勁 + 管理層量化 FCC 替代訂單 → 取消空方計畫，轉為觀察多方機會
2. **MOD（8/13-15 Jackson Hole 後）**：無鷹派意外 + 量縮止穩 → 首批 0.5% NAV 建倉；8/26 前未達成則遞延至 9 月底重評
3. **ANET（8/26 NVIDIA 業績後首個交易日）**：雙條件均滿足 → 1.0% NAV 建倉；任一條件缺失則取消
4. **VRT、LITE、FN、AAOI、IPGP、GLW**：待 Yahoo Finance 數據恢復後重跑 Phase 2-4，今日零倉位，暫不行動

---

## 板塊風險預算

MOD（最高 1.0% NAV）+ ANET（1.0% NAV）+ COHR put spread（0.5% NAV，期權限損為最大損失）= **潛在最大板塊曝險 2.5% NAV**。三者均深度相關於 AI capex 週期，建議**板塊總上限維持 2.5% NAV**。若 Big-5 任一業績後指引下修，或 NVIDIA 超越 ANET 市佔的明確訊號浮現，應將 ANET + MOD 合計壓縮至 1.0% NAV 以下。Phase-1 標的（VRT、LITE、FN、AAOI、IPGP、GLW）數據未恢復前，不計入板塊額度。

---

SECTOR REPORT COMPLETE
