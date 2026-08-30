# Neutral risk view — AVGO

## Points of agreement (兩方共識)

- 2026-09-02 Q3 FY2026 財報為高度二元事件，財報前不應建立完整倉位。
- PRICE_DATA_UNAVAILABLE 排除以 ATR 為基礎的名義停損，雙方均認同應改採**事件觸發型 Invalidation Stop**（AI XPU < $14B 或 XPV 事件化 → 出場）。
- AI XPU $16B 指引為管理層公開承諾，是最重要的近期驗證點。
- XPV $370B 為或有負債、尚未事件化；雙方均未主張其為基本情境，但對折扣程度看法分歧。

---

## Aggressive overreach（進取方過度主張）

- **Where**：建議財報前持倉提升至 55%，強調「等財報後是追漲」。
- **Why**：在 PRICE_DATA_UNAVAILABLE 且距離二元事件僅 2 個交易日的條件下，55% 倉位缺乏有效損控錨定。進取方的 R:R 2.2:1 建立在「現實下行」假設上，但尾部情境（XPV 爆雷 + Google 削減採購同步發生）的 13-16% NAV 虧損並非可以忽略的低概率事件。完全淡化 Henry Samueli $999M 售股訊號也屬便利性選擇——10b5-1 計畫確實常見，但規模與時機值得納入風險折扣，不宜歸零。

---

## Conservative overreach（保守方過度主張）

- **Where**：將倉位上限嚴格鎖定 30%，並宣稱「超過 30% 等同違反風控紀律」；主張加 SOX index puts 對沖。
- **Why**：PRICE_DATA_UNAVAILABLE 不代表基本面能見度為零——$16B 官方指引、FCF 40%、蘋果合約延至 2031 皆是可驗證的基本面錨點，可支撐略高於 30% 的倉位。將 XPV $370B 視為近似確定性尾部風險屬誇大，BofA 估算非官方認定損失。SOX puts 在 PRICE_DATA_UNAVAILABLE 環境下 strike 與 premium 皆無法驗算，建議卻缺乏落地可行性，屬形式性對沖主張。

---

## Balanced adjustment proposal

- **Size**：財報前建立 **38% 目標倉位**。高於保守方 30% 上限（基本面錨點仍存），低於進取方 55%（二元事件 + 無價格停損不支撐更高敞口）。財報後若兩項入場條件（總收入 ≥ $14B；AI XPU 達成 $16B 並維持展望）同時達成，次一至兩個交易日分批擴充至中倉（1.5% NAV）。
- **Stop**：採事件觸發型，禁止設名義價格停損（PRICE_DATA_UNAVAILABLE）。觸發條件：① Q3 AI XPU 收入低於 $14B；② 法說會確認 XPV 信用事件 → 次日開盤分批清倉。
- **Entry**：2026-08-31 收盤前以 38% 倉位分批進場，不在財報前追加。
- **Hedge**：不採 SOX puts（PRICE_DATA_UNAVAILABLE 使 strike 無法驗算）。對沖以**倉位規模本身**實現——38% 限倉即是主要風控手段。若進取方偏好選擇權，call spread 結構（Buy ATM / Sell OTM，到期 2026-10-17）可作為股票倉位的部分替代，**但須待財報後方可於報價時確認 strike 與 premium**，財報前不得盲目建立衍生品。
- **Time horizon**：主視窗 1-3 個月，財報後驗證論點可延伸至 3 個月以上。

---

## Net $ risk if stop hits

PRICE_DATA_UNAVAILABLE，無法計算公式 `(entry − stop) × shares`。

以概率情境估算：若財報失敗觸發 20-25% 修正，38% 目標倉位（假設目標倉位 = 1.5% NAV）敞口為約 **0.57% NAV**；最大損失情境約為 **0.11–0.14% NAV**。

若尾部情境（XPV + Google 雙重衝擊，-30%）：損失約 **0.17% NAV**——可接受，不至於對組合造成結構性傷害。

---

## Net $ upside at T1 / T2

同樣以 0.57% NAV 敞口估算：

- **T1**（財報超預期 +15%，估值重估至前瞻 P/E 26-28x）：**+0.086% NAV**
- **T2**（財報後論點全面驗證，1-3 個月持有，+25%）：**+0.14% NAV**

財報後若加碼至 1.5% NAV（達成兩項入場條件），T2 回報升至約 **+0.375% NAV**，R:R 進一步改善。

---

NEUTRAL RISK COMPLETE
