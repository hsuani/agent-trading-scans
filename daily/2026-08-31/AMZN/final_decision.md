# Final decision — AMZN as of 2026-08-31

FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> 部位狀態：AMZN **不在** `held_tickers.txt`，屬新倉，採 A 框架。

---

## 價格資料聲明（必讀）

**PRICE_DATA_UNAVAILABLE。** 所有價格水位均由分析師共識中位數錨點 **$326.84（UNVERIFIED）** 之百分比偏離推導，全部標記 **UNVERIFIED**，不代表即時成交價。

**執行閘門**：下單前必須確認即時成交價落於錨點 -20% 至 -25%（UNVERIFIED ~$245–$261）之內。若實際價格已高於錨點 -18%，本卡片作廢、重新評估；若低於錨點 -30%，先確認是否有基本面/監管事件，未查明前不得承接。

---

## 2. Approved transaction（Final trade card）

| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $245.00 – $261.00（UNVERIFIED，錨點 -25% ~ -20%） |
| Stop | $219.00（UNVERIFIED，錨點 -33%，收盤價確認） |
| Target 1 | $326.84（UNVERIFIED，共識中位數） |
| Target 2 | $359.00（UNVERIFIED，錨點 +10%） |
| Size | Medium — 初始 **3.5% NAV**（首批 1.5–2%），確認後加至 **5–6%**，FTC 庭審前縮至 **2%** |
| Horizon | 3–6 個月（完整驗證至 2027-Q2） |
| Conviction | **6 / 10（M）** |
| R:R to T1 | 2.2 |

**分段執行**
1. **即日**：1.5–2% NAV（執行閘門通過後）。
2. **Q3 財報後（2026-10 月末）**：若 AWS YoY >35% **或** FCF Margin 相對 -25% 底部顯著改善（二擇一），加至 5–6% NAV。上限封在 6%，不採積極方 7–8%。
3. **2027-01 底前**：無條件縮至 2% NAV。此為機械規則，不接受「等信號再減」。

---

## 3. Risk debate resolution

- **Aggressive 最強論點**：AWS +36.7%（18 季新高）與合約負債 $496B 是可查核的財報數字，不是敘事；以 1% NAV 起手等於不認同自己的結論。此點採納 → 首批提高至 1.5–2%。
- **Conservative 最強論點**：FCF Margin 為負、Forward P/E 45–55x 近行業中位兩倍，安全邊際趨近於零；任何盈利下修造成 EPS 與估值雙殺。此點採納 → 總規模封頂 6%，非 8%。
- **Net：我採 neutral 權重最高。** 積極方把 FTC 拆分機率壓到 <8% 並主張庭審前維持 5–6% NAV，錯在假設市場會給予反應時間——裁定夜間的跳空不會。保守方止損收至 -28%（~$235）則與 ATR14 $2–$3.50 的正常波動衝突，是製造 whipsaw。中立方的「維持 -33% 止損 + 庭審前縮至 2%」同時處理了 gap risk 與雜訊，且 6% 上限保留了論點兌現的 alpha。

---

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AWS 成長動能 | YoY >30% 可持續 | Q2 +36.7%，18 季新高 | 成立 |
| 收入能見度 | 合約負債支撐 12–24 個月 | $496B 歷史新高 | 成立 |
| CapEx ROI / FCF 路徑 | ROIC 8–12% → 15%+、FCF 轉正 | FCF Margin -25% ~ 0%，無驗證數據 | 觀察中 |
| 監管尾部可控 | FTC 不觸及結構性拆分 | 庭審日期已定 2027-02-09 | 觀察中 |

---

## 5. Invalidation conditions（論點紀律，與 Stop 分開）

- 若 **AWS 單季 YoY 跌破 25%**（或連兩季低於 30%），成長支柱失效 → **出場**。
- 若 **FTC 出現強制拆分或市集費率上限之初步裁定**，監管支柱失效 → **出場**（不等 Stop）。
- 若 **全年 CapEx 再上調至 $250B+ 且無 ROIC 改善揭露**，ROI 支柱失效 → **減碼至 2%**。
- 若 **廣告業務罰款 >$10B 或廣告毛利率跌破 50%**，第三引擎支柱失效 → **減碼**。
- 若 **合約負債連兩季 QoQ 下滑**，能見度支柱失效 → **減碼**。
- **Stop（價格紀律）**：收盤跌破 $219（UNVERIFIED）無條件出場。

## Monitoring trigger
若 Q3 指引將 AWS 全年增速下修至 30% 以下，或庭審前 60 日內出現任何拆分相關法庭動向，於 Stop 觸發前重新評估。

## 4. Catalysts to monitor
- 2026-10 月末 — Q3 2026 財報（AWS 增速 + FCF Margin，首要確認點）
- 2026-Q4 — 全年 CapEx 執行完成、FCF 實際值
- 2027-01 底 — 強制縮倉至 2% NAV
- 2027-02-09 — FTC 反壟斷庭審開始
- 2027-Q1 — FTC 廣告調查結論（潛在罰款 $5–10B）
- 2027-Q2 — CapEx ROI / ROIC 是否突破 15%

---

## Metrics summary

| Metric | Value |
|---|---|
| Verdict | BUY (MODIFY) |
| Conviction | 6 / 10 |
| Direction | LONG |
| Size (% NAV) | 3.5% 初始（首批 1.5–2%）→ 5–6% 確認後 → 2% FTC 庭審前 |
| Entry | $245.00 – $261.00（UNVERIFIED） |
| Stop | $219.00（UNVERIFIED） |
| T1 | $326.84（UNVERIFIED） |
| T2 | $359.00（UNVERIFIED） |
| R:R T1 | 2.2 |
| R:R T2 | 3.1 |
| Time horizon | 3–6 個月（完整驗證至 2027-Q2） |

FINAL DECISION COMPLETE
