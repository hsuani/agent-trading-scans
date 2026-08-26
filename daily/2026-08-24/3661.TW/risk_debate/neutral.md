# Neutral risk view — 3661.TW (世芯-KY / Alchip Technologies)

## Points of agreement（雙方共識）
- GM 指引差距（管理層 FY2026 指引 20-25% vs 分析師模型 58-62%）是可驗證的硬事實，非詮釋分歧；熊方基本面論述有效。
- 當前不建立裸 SHORT，兩方均認同 put spreads 是更合適的方向性工具。
- 2026-08-31 月營收及 2026-10 中旬 Q3 財報是雙重關鍵觸發窗口，任何行動須在此日曆框架下評估。

---

## Aggressive overreach（積極方過度主張）
- **主張**：PRICE_DATA_UNAVAILABLE 不影響 put spreads，因最大虧損已定義，無需止損。
- **問題所在**：邏輯在結構上正確，但在執行層面根本不可行。欲建立 put spread，必須知道：(1) 現貨股價（否則 -10%/-35% 行使價無從計算）；(2) 當前 IV 水位（「IV 尚低」的前提本身未獲確認）；(3) 每口合約報價（否則 1-1.5% NAV 等同幾口合約無法換算）。宣稱定義風險即可跳過價格數據，是將「結構性風控」與「執行可行性」混為一談——前者正確，後者不成立。R:R 3:1 至 5:1 的估算亦建立在未知的權利金成本上，屬假設性計算。

---

## Conservative overreach（保守方過度主張）
- **主張**：任何主動倉位均違反風控底線；SHORT 面臨「無上限損失」。
- **問題所在**：用裸 SHORT 的風險框架攻擊 put spreads，是類別錯誤（category error）。Put spreads 最大虧損確實以權利金為上限，不存在無上限損失。Scenario A（GM 回升 >35%，機率 25%）的尾部情境論述有效，但此風險在定義風險結構下已被封頂，不是反對使用期權工具的論據。保守方正確封閉「裸空」選項，但全面否定 put spreads 為工具，論理不夠精準。

---

## Balanced adjustment proposal（平衡調整方案）

| 項目 | 裁定 |
|---|---|
| **Size** | 0% NAV（當前）；價格數據恢復後可評估 ≤0.5% NAV 的探索性 put spread |
| **Stop** | Put spread 結構下不設個別止損；最大損失 = 全部權利金支出 |
| **Entry** | 條件：PRICE_DATA_UNAVAILABLE 解除 **且** 確認 Q3 財報前 IV 仍處低位；否則維持 WATCHLIST |
| **Hedge** | 若組合有 AI 半導體多頭敞口，SOX Index puts 為更穩健替代（保守方建議有效）；不以 3661.TW 個股空倉對沖 |
| **Time horizon** | 以 2026-11 到期的 put spread 涵蓋 Q3 財報（2026-10 中旬）；否則等待 Q3 後數據確認再切入 |

**組合經理應傾向保守**：關鍵理由是目前無法取得執行所需的任何選擇權定價輸入值。積極方的結構邏輯值得備案，但「現在立即進場」的建議在 PRICE_DATA_UNAVAILABLE 狀態下不具操作基礎。正確姿態是：WATCHLIST + 條件觸發（價格數據恢復 + Q3 財報前 IV 確認低位 + 月營收數據未出現 GM 意外改善）三者同時成立，才執行 ≤0.5% NAV 的定義風險 put spread。

---

## Net $ risk if stop hits
**PRICE_DATA_UNAVAILABLE — 當前倉位 0% NAV，風險敞口為 $0。**
若未來執行 0.5% NAV put spread：最大損失 = 0.5% NAV（全部權利金），絕對值取決於 NAV 規模，結構性封頂，無法超出。

---

## Net $ upside at T1 / T2
**PRICE_DATA_UNAVAILABLE — 無法計算具體金額。**
定性估算：若 Q3 GM < 25% 觸發市場重估，0.5% NAV 投入之 put spread 若展現 3:1 R:R，潛在貢獻約 1.5% NAV（T1，Q3 財報後首波急跌）；若共識連鎖下修延續至 Q4，T2 貢獻估 2.5-3.0% NAV。此為條件性估算，需價格數據恢復方可量化。

NEUTRAL VIEW COMPLETE
