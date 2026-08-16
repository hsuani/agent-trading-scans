FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — GLD as of 2026-08-15

## Verdict
**MODIFY**（方向採納，規模與執行方式下修）

**無即時價格，暫不給進出場價位。** 本決議所有風險控制一律以百分比表述，禁止在 PRICE_DATA_UNAVAILABLE 狀態下杜撰 Entry / Stop / Target 數字。

## Final trade card

| 欄位 | 數值 |
|---|---|
| 方向 | LONG |
| 信心（Conviction） | 60%（MEDIUM） |
| 黃金配置額度（sleeve 上限） | NAV 5% |
| 初始倉位 | sleeve 的 35% ≈ **NAV 1.75%**（立即建立） |
| 第二批 | 8/26 PCE 年率 ≤ 2.5% → +20% sleeve（累計 55% ≈ NAV 2.75%） |
| 第三批 | 9/11 CPI 核心 ≤ 2.3% → +15% sleeve（累計 70% ≈ NAV 3.5%，硬上限） |
| Entry | PRICE_DATA_UNAVAILABLE（以當日收盤附近市價分批執行） |
| Stop | PRICE_DATA_UNAVAILABLE（改採時間／事件止損，見下） |
| T1 | PRICE_DATA_UNAVAILABLE（對應 GLD +8–10%，NAV +4.4–5.5%） |
| T2 | PRICE_DATA_UNAVAILABLE（對應 GLD +15–20%，NAV +10.5–14.0%） |
| 時間框架 | 1–3 個月，涵蓋 PCE→CPI→FOMC 完整催化劑週期 |
| 風險預算 | 單筆最大 NAV 損失上限 **3.0%**，逾此無條件縮至 sleeve 20% |
| R:R（定性） | 約 1:4 |

**取代條款**：不採納 aggressive 的 Oct/Nov call spread。無即時報價即無法評估權利金與隱含波動率，買選擇權等同盲下注，明令禁止。

## Risk debate adjudication
- Aggressive 最強論點：Q1 2026 的 244 噸實際央行購金 vs. IMF 記錄 16 噸，是已發生事實而非預測；等三個催化劑全數確認才進場，等於在不確定性最低時付最高價。
- Conservative 最強論點：ATR 與即時價格皆不可得時，任何精確止損都是猜測；50–60% 起跳倉位在 40% 升息機率下的尾部損失（NAV −6% 以上）超出 MEDIUM 信心該承受的三倍。
- 淨判：**採 neutral 為主軸，執行紀律偏 conservative**。理由：方向論據（央行買盤、DXY 走弱、7 月 ETF 淨流入 $3B、回調 21.7%）足以支持立即建立方向性頭寸，但無法量化止損時，唯一負責任的風控工具是「小起始 + 事件止損 + 硬性 NAV 損失上限」。Conservative 的完全凍結被否決——GLD 流動性極佳，時間／事件止損可有效替代價格止損；Aggressive 的 75–80% 即刻重倉同樣被否決——在無法計算暴露的環境下重倉屬程序性錯誤。

## Monitoring trigger（單一可證偽）
若 **北美黃金 ETF 出現單週淨流出 ≥ $2B**，則「7 月資金逆轉」多頭支柱直接失效，須在任何價格止損觸發前立即將倉位縮至 sleeve 20%（≈ NAV 1%）並重新評估。
次級硬條件（任一觸發即同步縮倉至 20%）：9/15-16 FOMC 升息或聲明明確鷹派；8 月 CPI 核心反彈破 3.0%；COT 淨多頭跌破 90k。無論損益，9/16 FOMC 未確認鴿派路徑一律降至 20%。

## Catalyst calendar
- 2026-08-26 — PCE 物價指數（7 月），2.5% 為分水嶺
- 2026-09-11 — 8 月 CPI（08:30 ET），核心 ≤ 2.3% 為加碼門檻
- 2026-09-15/16 — FOMC 利率決議，決定是否延伸為戰略配置

## 執行前置條件
恢復即時報價後 24 小時內補齊 Entry / Stop / ATR，並將事件止損疊加 −10% 硬價格止損。稅務：優先於 IRA / 401k 帳戶持有（28% 收藏品稅率）。

---

## FINAL TRANSACTION RECORD

- **Verdict**: BUY (MODIFY of proposal)
- **Conviction**: 60%
- **Direction**: LONG
- **Size**: Start NAV 1.75% (35% of a 5% NAV gold sleeve); scale to NAV 2.75% on PCE, NAV 3.5% hard cap on CPI
- **Entry**: PRICE_DATA_UNAVAILABLE
- **Stop**: PRICE_DATA_UNAVAILABLE — time/event stop in force; max single-trade loss 3.0% of NAV
- **T1**: PRICE_DATA_UNAVAILABLE (GLD +8–10%)
- **T2**: PRICE_DATA_UNAVAILABLE (GLD +15–20%)
- **Timeframe**: 1–3 months
- **Key catalysts**: 2026-08-26 PCE / 2026-09-11 CPI / 2026-09-15-16 FOMC
- **Kill switch**: North American gold ETF weekly outflow ≥ $2B, or FOMC hike, or core CPI > 3.0%, or COT net long < 90k → cut to 20% of sleeve
- **Prohibited**: options overlay while PRICE_DATA_UNAVAILABLE

FINAL DECISION COMPLETE
