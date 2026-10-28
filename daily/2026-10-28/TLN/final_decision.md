FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — TLN as of 2026-10-28

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## Final trade card
不適用 — 不建立任何部位。現股 0% NAV；選擇權亦為 0% NAV。理由：檔案中沒有任何真實選擇權鏈報價，aggressive 的 $355/$390 call spread 與 neutral 的 1–2% NAV 權利金皆為示意數字，無法核算 IV、max loss 與 IV crush 後的實際盈虧。neutral 自己設下的前提是「查不到真實報價即歸零」，此前提目前不成立，因此歸零。

## Risk debate adjudication
- Aggressive's strongest point: 研究經理已承認條件式偏多略優（PJM 容量價格貼近上限、Amazon 1,920 MW PPA 皆為已確認事實），而財報跳空的首日漲幅確實無法在「放量站穩 $350」之後才去捕捉；用 defined-risk 工具參與二元事件，在邏輯上是正確的工具選擇。
- Conservative's strongest point: 利息覆蓋 0.75x、現金 0.231B、流動比率 0.78、Q2 OCF -0.434B、股數 +4.8% 全部直接取自財報，是全案最硬的數據。公司指引在 fundamentals.md 為 DATA_UNAVAILABLE，舉證責任在多方；ATR 5.3% 加財報缺口使 $315.50 停損在財報夜毫無保護力。
- Net: I weight neutral more here because 兩端的實質差距只是「要不要用 1–5% NAV 的選擇權小倉參與」。neutral 正確指出 aggressive 的 3–5x 報酬忽略了財報前 IV 已高估與 IV crush，也正確指出 conservative 的 35–40% / 20–25% 機率沒有可驗證基礎。我再加一條：對一家近四季兩次 EPS miss（-10.3%、-30.0%）的公司，在財報前付高 IV 買 call，不是不對稱，是付費賭博。

## Dealbreaker
整個估值框架取決於單一未驗證變數：adjusted EBITDA 2.025–2.225B / adjusted FCF 1.200–1.350B 指引能否與 GAAP 勾稽。若真，EV/EBITDA 約 12x、淨負債/EBITDA 約 4.4x；若假，則是 23–45x 與 0.75x 利息覆蓋。這個答案 4 個交易日後（2026-11-03）免費揭曉。能免費等到驗證，卻要先付 68.7% 年化波動的事件風險，沒有理由。

## 論點支柱
以下為「財報後條件式偏多」候選論點的支柱現況，作為重新評估的基準：

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| PJM 容量順風 | 容量價格貼近 FERC 上限（約 325–333 USD/MW-day） | 多來源交叉確認；DOE 支持 150 億 USD 容量拍賣提案 | 成立 |
| 長約資產 | Amazon 1,920 MW 核能 PPA 至 2042 | 已確認，無變動 | 成立 |
| 指引可兌現 | adjusted EBITDA ≥2.025B、FCF ≥1.200B，且可與 GAAP 調節 | 僅二手摘要；Q2 OCF -0.434B、Q2 EPS miss -30% | 觀察中 |
| 償債能力 | 利息覆蓋 >1.5x、現金重建、無稀釋增資 | 0.75x、現金 0.231B、流動比率 0.78、股數 +4.8% | 已失效（目前） |
| 新資料中心合約 | 1 GW 合約簽約 | 自 2026-02 停滯；CEG 10-06 拿下 Google 3.59 GW | 觀察中 |

「償債能力」支柱目前已失效，這是現股 0% 的直接依據；前兩根成立的支柱只足以讓 TLN 留在候選名單，不足以支撐建倉。

## 論點失效條件
此處針對「觀望」立場本身，與價格停損無關（目前無部位、無 Stop）：

- 若 Q3 財報（11-03）同時滿足：提供 adjusted EBITDA 對 GAAP 的調節表、維持或上修指引、Q3 OCF 轉正、期末現金 >0.5B、揭露 12 個月內到期債務可由現金加循環額度覆蓋 → 「觀望」立場失效，轉為 LONG 候選；進場條件為收盤放量（>1.2x 10 日均量）站上 $350。
- 若 Q3 指引下修、或宣布股權增資、或 OCF 連續第二季為負 → 「償債能力」支柱確認結構性失效，TLN 自候選名單剔除至少一季，不考慮任何方向性部位（高空方比例下亦不追空）。
- 若 Q3 EPS 較一致預期 7.06 USD miss >10% → 「指引可兌現」支柱失效，同上處理。
- 若 11-06 VST 財報顯示 PJM 容量收益不及預期或下修 → 「PJM 容量順風」支柱降為觀察中，LONG 候選延後。

## Monitoring trigger
財報前（10-29 至 11-02）：若收盤跌破 $315.50 或放量突破 $350，不改變本決定（財報前一律不進場），僅記錄以校正財報後的進場基準。財報後：以 11-03 當日收盤量價、11-06 VST 財報的 PJM 訊號為依據，於 11-09 前重新出具 trade_proposal。若交易台能在 11-03 前取得真實選擇權鏈報價，可另行提交 ≤1% NAV 的 defined-risk 提案，但那是新提案，不在本決定核准範圍內。

## Catalyst calendar
- 2026-11-03（二）08:00 ET — Talen Energy Q3 2026 財報與電話會議；關注 adjusted 對 GAAP 調節表、OCF、期末現金、債務到期表、1 GW 合約進度
- 2026-11-06（五）盤前 — Vistra（VST）Q3 財報，PJM 容量與板塊情緒交叉驗證
- 2026-11-18（三）14:00 ET — FOMC 10 月會議紀要與 Beige Book
- 待定 — FERC 對 PJM large-load / co-location 框架後續裁定
- 待定 — CEG Q3 財報日（news.md 標記 DATA_UNAVAILABLE）

FINAL DECISION COMPLETE
