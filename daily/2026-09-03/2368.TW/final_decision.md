FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 2368.TW as of 2026-09-03

> **價格資料聲明**：market.md 標示 PRICE_DATA_UNAVAILABLE。**無即時價格，暫不給進出場價位**。所有 Entry / Stop / Target 一律以條件式觸發表達，本決策不引用亦不推算任何本系統價位。文中出現的價格數字皆為 sentiment.md / news.md 所引外部媒體或 FactSet 之公開數據，僅作為條件描述之錨點。

## Verdict
MODIFY（新倉，未在 held_tickers.txt 內）— **Conviction 62%**

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無即時價格，暫不給進出場價位（見下方進場觸發條件） |
| Stop | 無即時價格，暫不給進出場價位（見下方出場觸發條件） |
| Target 1 | 條件式：FactSet 目標價中位數 1,640 元（外部來源）達成或 Q3 財報超預期後逢強減倉 |
| Target 2 | 條件式：FactSet 最高目標 1,940 元（外部來源），對應 2027 ABF 缺口擴至 21% 情境 |
| Size | Small — **初始 0.5% NAV，硬上限 0.5% 直到 Q3 EPS ≥ 9 元，確認後方可升至 1.0% NAV** |
| Horizon | 1–2 個季度（至 Q3 法說會與 2026 年底業績確認） |
| Conviction | M（62%） |
| R:R to T1 | 無即時進場價，無法計算；定性估計 1.8–2.0 |

## 進場觸發條件（condition-based）
1. 9 月中旬 8 月月營收公布：**YoY ≥ 70% 且 MoM 持平或正成長** → 建倉 0.5% NAV。
2. 採**分兩批**執行：觸發後先建半數，公布後 3–5 個交易日確認未出現放量「sell the news」殺盤，再補足至 0.5%。
3. 若 8 月 YoY < 60% 或 MoM 轉負 → **不建倉**，觀望至 Q3 財報重評。
4. 加碼至 1.0% NAV 唯一條件：**Q3 2026 EPS ≥ 9 元**。楊梅廠稼動率或客戶時程等軟性訊息**不再**單獨作為加碼依據（否決 trade_proposal 的三選一條款）。

## 出場觸發條件（condition-based，雙軌）
- 基本面一：**Q3 2026 EPS < 8 元** → 立即出清，不等技術面。
- 基本面二：全年 EPS 共識下修至 **36 元以下**（H2 貢獻低於 20 元）→ 出清。
- 基本面三：AWS / Google / Meta 任一宣布訂單延後**逾一季**，或 ABF 毛利率壓縮 **> 3 個百分點**且無法轉嫁 → 減碼一半，兩週內未改善即出清。
- 技術面：放量跌破外部媒體所引 900–920 元支撐區且 **3 個交易日未收復** → 出清。

## Risk debate adjudication
- Aggressive 最強論點：7 月 NT$100.15 億元、YoY +77.38%、MoM +21.31% 是已公告硬數字，三重確認同時成立；等 8 月只是延遲兩週的重複確認。
- Conservative 最強論點：營收達標 ≠ 獲利品質達標。170 億 capex > 全年預估淨利、FCF -30 至 -40 億元、折舊浪潮自 Q3-Q4 2026 即開始認列，只有 Q3 財報能驗證轉嫁能力。
- Net：**我採納 conservative 的 sizing 紀律、neutral 的進場時點**。Aggressive 的資產不對稱計算建立在外部媒體引述價格上，在 PRICE_DATA_UNAVAILABLE 下無法驗證，其 R:R 2.7 不具決策效力；在無法量測現價安全邊際時放大到 1.0% NAV 是拿未驗證的數字換真實暴露。同時我否決 conservative 「等到 Q3 才建倉」——8 月營收是低成本的早期確認窗口，全面放棄會犧牲 R:R。折衷：**用 trader 的觸發時點，配 conservative 的倉位上限**。認購權證與 2314 對沖兩項建議均否決（無報價、無流動性驗證）。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 月營收成長動能 | 單月 YoY > 70% | 7 月 +77.38%、1-7 月累計 +70.29% | 成立 |
| H2 獲利交付 | H2 EPS ≥ 22.14 元（月均淨利 > 10 億） | H1 僅 16.14 元，尚未驗證 | 觀察中 |
| ABF 定價權轉嫁 | 毛利率維穩或擴張 | 原料成本 +30%，轉嫁成效未證實 | 觀察中 |
| 財務結構 | FCF 可被現金流消化 | capex 170 億 > 全年淨利，FCF 確定為負 | 已失效（故壓縮至 Small） |

## 論點失效條件（論點紀律，與 Stop 分離）
- 若 **Q3 2026 EPS < 8 元**，H2 獲利交付支柱失效 → 出場。
- 若 **連續兩個月單月營收 YoY < 50%**，成長動能支柱失效 → 減碼至零。
- 若 **Q3 毛利率較 Q2 下滑逾 3 個百分點**，ABF 轉嫁支柱失效 → 減碼一半。
- 若公司宣布**現金增資或可轉債募資逾 50 億元**，財務結構風險由中期轉為立即 → 減碼一半。

## Key risk factors
客戶集中（4 大 Hyperscaler）、FCF 深度為負與折舊提前認列、股價自 8 月低點反彈逾 +72% 的追高風險、台灣 PCB 族群歷史週期跌幅逾 50%、地緣政治流動性折價、以及**即時價格不可得導致無法精算安全邊際**（本身即是壓低倉位的獨立理由）。

## Monitoring trigger
9 月中旬 8 月月營收；未達 YoY 70% 即不建倉。已建倉後，若 9 月營收 MoM 轉負或楊梅廠量產里程碑延後，在技術停損前先減碼一半。

## Catalyst calendar
- 2026-09 中旬 — 8 月月營收（建倉決策點）
- 2026-09 底 — 楊梅廠正式量產里程碑
- 2026-10 上旬 — Q3 2026 財報 EPS（加碼 / 出場決策點）
- 2026-10 中旬 — Q3 法說會全年指引
- 2026-Q4 — Trainium3／Vera Rubin 訂單能見度更新

## Phase
Full Pipeline — Phase 4 complete

FINAL DECISION COMPLETE

PORTFOLIO MANAGER DECISION COMPLETE
