FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — QUBT as of 2026-09-08

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## 部位狀態
QUBT 不在 `pipeline/tools/held_tickers.txt`，屬**新倉判定**（框架 A）。問題是「該不該進」，答案是不進。
第一行 HOLD = 維持零部位、不建倉，非「續抱」。

- Conviction: **75%**（對「現在不該建倉」這個結論的信心，非對方向的信心）
- NAV allocation: **0.0%**（現階段不預留任何多頭或空頭配額）

## Dealbreaker（駁回理由，直白說）
價格數據不可得（PRICE_DATA_UNAVAILABLE）+ Beta 3.88 + 負 Gross Margin + P/S 50x+，四項同時成立。
沒有即時報價就無法錨定 ATR、無法設可執行止損、也無法計算期權權利金與 Spread Width。
Aggressive 主張的 Call Spread「最大損失已鎖定」是循環論證：鎖定多少，本身就需要報價才知道。
在一檔日內 2-sigma 波動可達 ±12–15% 的標的上，用無法量化的風險去換主觀估計的 25% 機率轉折，
不是非對稱機會，是無法定價的賭注。**沒有可量化的下檔，就沒有部位。**

## Risk debate adjudication
- Aggressive's strongest point: Q3 財報（10 月）確實是明確、時間有界的催化劑窗口，等到訊號完全明朗通常等於已定價；限定風險結構在原則上是對的工具選擇。
- Conservative's strongest point: $42.5M 積壓被當成「硬底板」是倖存者偏誤——政府合約可因預算年度更替或優先序調整取消；且 0.5% NAV 在 Beta 3.88 下實際日波動貢獻遠超帳面數字。
- Net: 我採 **conservative** 為主、neutral 的觸發條件框架為輔。理由是 Neutral 已精準拆穿 Aggressive 的執行前提缺口（期權定價本身依賴報價與 IV，小型量子股期權 Bid-Ask 過寬會吃掉理論 R:R）。但我不接受 Conservative「把條件式選項從選單刪除」——選單保留，配額歸零，兩者不衝突。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 商業模式驗證（Gross Margin） | 規模化後毛利率轉正 | 仍為負毛利率，每元收入成本 > 一元 | 已失效 |
| 收入動能可持續 | 積壓 $42.5M 穩定兌現 | Q1 $3.7M → Q2 $5.6M 環比上升，方向對但絕對規模微小 | 觀察中 |
| 估值有安全邊際 | 成長支撐倍數 | P/S 50x+ 對 H1 $9.3M 收入，安全邊際近零 | 已失效 |
| 資產負債表韌性 | 現金消除生存風險 | $850M 現金，跑道 5 年以上，無強迫稀釋 | 成立 |

四根支柱中兩根已失效，其中一根（負毛利率）是商業模型本身尚未成立的根本性信號。新倉在此結構下不予放行。

## 論點失效條件（論點紀律，與價格 Stop 分開）
- 若 Q3 2026 與 Q4 2026 **連續兩季 Gross Margin 仍為負**，商業化論點正式失效 → 移出觀察名單 12 個月
- 若 $42.5M 積壓中**單一合約取消或延遲金額超過 $10M**，能見度支柱失效 → 永久剔除多頭選項
- 若 Q3 收入**環比低於 $5.6M**（即 Q2 為高點、動能反轉），收入動能支柱失效 → 不再重評
- 若 NHanced 良率問題導致**績效付款觸發條件被公開下修或減記**，製造轉型支柱失效 → 出場級別訊號

## 重新評估的進場觸發（全部須同時成立）
1. PRICE_DATA_UNAVAILABLE 解除，可計算 ATR 與期權鏈流動性（Bid-Ask ≤ 10% of mid）
2. Q3 2026 財報出現**首個正 Gross Margin 季度**
3. 估值收縮至 **P/S ≤ 25x**
4. R:R ≥ 2.5

上述四項全數成立，方可以 **0.3% NAV 上限**試多（非 0.5%，非 1%）。
空頭選項保留於選單但配額為零：Beta 3.88 下軋空單日可吞掉 1–1.5% NAV，止損無從錨定時不執行。

## Exit conditions（若未來建倉）
- 論點失效條件任一觸發 → 立即全數出場，不等 Stop
- Stop 錨定 Beta 調整後 ATR × 1.5（須待報價恢復後量化）
- 到期日上限 2026-11-21（跨越財報與參議院投票窗口）

## Monitoring trigger
若量子板塊在 9 月跌破 8 月低點，或 Form 4 再現 CFO / COO 級別拋售，直接下修至「12 個月不重評」。
若《American Quantum Competitiveness Act》提前通過參議院且報價已恢復，提早啟動重評（但正毛利率仍為必要條件，不可豁免）。

## Key monitoring metrics
- 季度 Gross Margin（負轉正 = 必要條件）
- 積壓轉化率 = 當季確認收入 / 期初積壓餘額
- 季度營運燒錢率（目前年化 > $80M）與 NHanced 資本支出
- 內部人 Form 4 申報

## Catalyst calendar
- 2026-10（預計） — Q3 2026 財報：Gross Margin 與積壓轉化率
- 2026-Q4 — 《American Quantum Competitiveness Act》參議院投票
- 持續 — 內部人 Form 4；量子板塊 Beta 聯動

FINAL DECISION COMPLETE
