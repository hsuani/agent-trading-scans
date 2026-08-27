# Trade proposal — SIVE as of 2026-07-20

FINAL TRANSACTION PROPOSAL: **HOLD**

---

## Direction
AVOID（暫不建倉）

---

## Setup

無即時價格，暫不給進出場價位。

market.md 回傳 PRICE_DATA_UNAVAILABLE（Yahoo Finance proxy 403 錯誤），所有技術面指標（收盤價、ATR、移動平均線、RSI、MACD、支撐壓力區）均不可得，無法計算任何 Entry / Stop / Target 或 R:R。即使方向性判斷已存在，在無真實價格基礎的情況下虛構價位，違反本框架的核心風控原則，故明確拒絕填入數字。

---

## Sizing
倉位：**0%** of portfolio NAV。

理由：
- **主體身份歧義未解除**：代號「SIVE」同時對應 SiTime Corporation（NASDAQ: SITM，美國）及 Sivers Semiconductors（Nasdaq Nordic，瑞典）兩個截然不同的法人實體，兩者基本面、技術面與風險輪廓存在根本差異，無法在同一框架下評估。
- **多頭論述（若 SIVE = SiTime）**：Q1 2026 淨營收 +88.3% YoY、毛利率 64.5%、Renesas 收購帶來 $300M+ 年化增量，具備紮實基本面支撐。
- **空頭論述（若 SIVE = Sivers）**：股價自 ATH 110 SEK 崩至 3.81 SEK（-96.5%），SEK 765M 禁售期已於 2026-07-15 解鎖，Ekobrottsmyndigheten 內部交易調查正式進行中，現金跑道不明，再融資稀釋風險顯著。
- **數據品質**：yfinance 財務數據全部返回 n/a；fundamentals.md 的估值框架（$341-512M 年化營收、65% 良率、ASP $50-75）建立在 Serenity 論文未驗證假設上，非已實現數字。
- conviction：**LOW**；ATR：**不可得**；年化波動率：**不可得**。

---

## Time horizon
暫不適用（倉位為零）。主體身份釐清應在開倉前數小時內完成；若後續確認為 SiTime 多頭論述，核心催化劑窗口為 2026-08-05 Q2 財報，時間框架為 1-3m。

---

## Trigger
**Wait for**：
1. 確認「SIVE」交易所與 ISIN（最高優先，應立即執行）。
2. 若確認為 SiTime (SITM)：等待 2026-08-05 Q2 財報驗證 $140-150M 指引且毛利率 ≥ 64%，再評估 LONG / MEDIUM sizing。
3. 若確認為 Sivers Semiconductors：全面迴避，禁售期後賣壓確認前不考慮任何方向性建倉。

---

## Invalidation
- 若確認為 Sivers Semiconductors，空頭論述自動成立，迴避理由升級為 HIGH conviction AVOID。
- 若確認為 SiTime，但 2026-08-05 財報營收低於 $140M 或毛利率 < 64%，多頭論述立即降級。

---

## Catalyst calendar
- **即時** — 確認「SIVE」對應實體之交易所與 ISIN（Finansinspektionen / SEC EDGAR 查核）
- **2026-07-15（已過）** — Sivers Semiconductors SEK 765M 禁售期解鎖；後續申報異動持續監控
- **2026-08-05** — SiTime (SITM) Q2 2026 財報（若 SIVE = SITM，為首個含 Renesas 完整貢獻季度）

---

TRADE PROPOSAL COMPLETE
