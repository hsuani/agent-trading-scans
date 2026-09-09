# Neutral risk view — ARM

## Points of agreement（雙方共識）
- 以股票形式在現價 ~$369（UNVERIFIED）新建多頭部位：雙方均拒絕，R:R 不足，無爭議。
- 營業利潤率從 11% 壓縮至 7%：費率倍增紅利尚未有效轉化為盈利，雙方均視為結構性隱憂。
- Qualcomm NUVIA ALA 上訴結果是護城河強弱的最關鍵二元事件，未解決前任何重大建倉均承擔尾部裁決風險。
- Q3 FY2026 財報（2026 年 9-10 月）是近期最高密度驗證窗口，現在距財報僅 4-6 週。

---

## Aggressive overreach
- **Where**：聲稱 IBM Z 系列合作（三天前公告）代表「資訊傳導前沿」，主張立即用 0.25% NAV 進場。
- **Why**：三天公告窗口尚不足以確認機構認知滯後；更關鍵的是，PRICE_DATA_UNAVAILABLE 下期權溢價 $17.5/spread 純屬估算，實際市場溢價可能顯著偏高，致使 R:R 5.7:1 的計算無法驗證。在未確認真實溢價前執行 call spread 等於接受未定義的 R:R，此邏輯矛盾於積極方援引的「數學不對稱」論點本身。此外，將「工具改善數學」與「thesis 改善」混同，忽略了 call spread 在股價維持橫盤或小幅下跌時仍損失 100% 溢價的現實。

## Conservative overreach
- **Where**：要求完全 AVOID 至 $200-$215，並以 GF Value $187.72 作為止損錨點。
- **Why**：GF Value 以歷史盈利作為估值基礎，無法捕捉 ARM v9 費率倍增的結構性轉折，以此作為機械化止損錨點存在方法論瑕疵。更實際的問題是：-46% 跌幅到 $200 只有在系統性崩潰或 Qualcomm 敗訴疊加 AI CapEx 同步反轉的複合尾部情境才會發生。三個尾部情境概率加總 75%（20%+25%+30%）明顯過度悲觀，也與基礎方案承認的「成長引擎屬真實且結構性」相矛盾。SOX ETF put 對沖建議亦欠精準，ARM 核心風險是公司特定事件（授權執行力、EPS 執行）而非廣義 AI 指數系統風險。

---

## Balanced adjustment proposal
- **Size**：0.15% NAV（call spread 形式）；低於積極方的 0.25% NAV，因 PRICE_DATA_UNAVAILABLE 使溢價無法驗證，須在確認真實市場報價後方可執行。
- **Stop**：不適用（call spread 最大損失 = 已付溢價，損失上限內建）。
- **Entry**：以 $370/$470 call spread、到期 2027-01 作為結構框架，但執行前必須先驗證真實期權溢價報價；若溢價超出 $20/spread 使 R:R 降至 4:1 以下，縮減至 0.10% NAV 或放棄。股票直接買入：維持基礎方案 BUY Gate $245-$280（UNVERIFIED），不採納保守方壓低至 $200-$215 的主張。
- **Hedge**：本身的 call spread 結構即為對沖（損失上限已定義），不額外疊加 SOX put，避免對沖成本蠶食極小部位的潛在收益。
- **Time horizon**：至 2027-01 到期（覆蓋 Q3 FY2026 財報 + AGI CPU 量產確認窗口）；若 Q3 財報結果負面，不於到期前追加任何部位。

---

## Net $ risk if stop hits
**$1,500**（= 0.15% NAV，假設 NAV $1,000,000）
全額溢價損失為最壞情境；依 $17.5/spread 估算約 85 組 spread 合約，但此數字須以真實報價重算。

## Net $ upside at T1 / T2
- **T1（股價達 $420，spread 半程獲利）**：約 $2,550（spread 價值約 $30，gain ≈ $12.5/spread × 85 組）
- **T2（股價達 $470+，spread 全額兌現）**：約 $8,500（$100/spread × 85 組 = 0.85% NAV）
- R:R：T1 約 1.7:1；T2 約 5.7:1（前提：溢價驗證為 $17.5）

NEUTRAL VIEW COMPLETE
