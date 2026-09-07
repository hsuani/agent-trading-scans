# Neutral risk view — PWR

## Points of agreement（雙方共識）

- **AVOID 作為核心立場正確**：95.28% 機構持倉下，裸融券空單的軋空風險是真實且量化的，雙方均不反對。
- **PRICE_DATA_UNAVAILABLE 是硬性限制**：任何選擇權執行價、Delta、IV 均無法在當前環境中精確設定，雙方均承認這一約束。
- **Q3 GAAP 財報（2026-10-29）是唯一裁決節點**：雙方均以此為核心觸發事件，約 7 週的時間視窗明確。
- **現有多頭持倉應縮減**：雙方均認為在當前估值（42.6x Forward P/E）與 CEO 內部人信號下，保留完整多頭部位不合理。

---

## Aggressive overreach（激進方過度主張）

- **Where**：聲稱 B/A ratio「4:1 至 6:1」，並建議「立即進場，不等待」。
- **Why**：PRICE_DATA_UNAVAILABLE 下，IV 水準完全未知。若 PWR 財報前隱含波動率已因 AI 概念股熱度被市場定價過高，put spread 的理論獲利倍數將大幅縮水，成本結構無法確認。「越快越好」的邏輯忽略了 IV 過熱的成本風險——不能用估值框架的跌幅直接換算 options 獲利而跳過定價驗證。此外，PWR 在強勁 AI 敘事下仍有短期向上動能，距財報 7 週的期間 put 可能先受 theta 侵蝕再獲益。

---

## Conservative overreach（保守方過度主張）

- **Where**：主張「任何選擇權均不應考慮」，堅持完全零部位是唯一可接受答案。
- **Why**：put spread 的最大虧損在結構上已封頂於 premium，與持有未對沖多頭的無限下行風險在性質上完全不同。保守方自身亦提及「可用 PWR OTM put 作臨時對沖」，但隨後又全盤否定選擇權工具，內部邏輯矛盾。拒絕已定義風險的小倉位 put spread 是反射性厭惡衍生品，而非基於結構性分析。Scenario D (-58%，機率 20%) 的情境設定亦缺乏新的基本面觸發點，屬於尾部疊加非線性放大。

---

## Balanced adjustment proposal（均衡調整方案）

- **Size**：若組合允許使用衍生品，put spread premium 上限 **0.5% NAV**（不採激進方的 1.0% 上限）；**必須等 PRICE_DATA 恢復後**，確認 IV 水準合理再執行，不盲目進場。
- **Stop**：Put spread 結構本身即為內建上限——最大虧損 = 所付 premium，無需額外停損設定。
- **Entry**：**不立即執行**（反對激進方「越快越好」）。優先順序：① 恢復即時報價；② 確認財報前 IV 是否已過度定價；③ 選擇 delta 約 -0.25 至 -0.30 的 OTM long put，配合更低履約價 short put 降低成本，到期日選 2026-11-06（Q3 財報後一週）。
- **Hedge**：現有多頭持倉採保守方立場——**全部清零**，不保留核心倉（理由：PRICE_DATA_UNAVAILABLE 下無法設 ATR Stop，任何多頭保留均為盲目裸曝險）。Put spread 本身為獨立的定義風險空方倉，非多頭對沖。
- **Time horizon**：7 週，以 **2026-10-29 Q3 GAAP EPS** 為裁決節點。

---

## Net $ risk if stop hits

Put spread premium 全損：**$5,000**（= 0.5% NAV，以 NAV $1M 計）

---

## Net $ upside at T1 / T2

| 情境 | 條件 | Put spread 估算獲利 |
|------|------|---------------------|
| T1：Forward P/E 壓縮至 30x | 目標約 $501，跌幅約 -29.5% | 2x–3x premium = **$10,000–$15,000** |
| T2：Forward P/E 壓縮至 20x（同業均值） | 目標約 $334，跌幅約 -53% | 4x–6x premium = **$20,000–$30,000** |

> 注意：上述獲利數字以 PRICE_DATA 恢復後 IV 合理為前提；若 IV 已過度定價，實際 R:R 將低於上表，屆時應重新評估是否執行。

---

NEUTRAL VIEW COMPLETE
