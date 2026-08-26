# Neutral risk view — TLT

## Points of agreement (both sides)

- PRICE_DATA_UNAVAILABLE 是真實的執行障礙，任何止損設定均需以確認後的即時報價為錨。
- ADX > 40 確認當前趨勢方向向下，逆勢多頭必須對抗技術動能，不可視而不見。
- 關鍵催化劑窗口集中於 9/4 NFP → 9/11 CPI → 9/18 FOMC，方向尚未確認之前，倉位不宜過重。
- 18.3% short interest 若正向催化劑到位確實能放大上行動能，但前提是催化劑必須先兌現。

## Aggressive overreach

- **Where**：主張立即以 2.5% NAV 建倉、call spread 額外佔用 0.35% NAV，同時將止損寬放至 $79.00。
- **Why**：在 PRICE_DATA_UNAVAILABLE 旗標下，無法確認進場價是否已低於 $81.66 支撐或已進一步惡化。機構流入 $12.3B 與單日淨流出 $477M 的時段口徑矛盾未解，用「先行入場」合理化跳過數據確認步驟，是以不確定性掩護倉位偏見。Stop $79.00 雖給予緩衝，但實際上也放大了因錯誤方向或流動性惡化帶來的損失絕對值。call spread 增加期權定價複雜度，在基礎持倉方向尚無法精確錨定的前提下屬疊加風險，不是風險管理。

## Conservative overreach

- **Where**：以 PRICE_DATA_UNAVAILABLE 為由主張 0% 倉位、等待 9/18 FOMC 後才行動。
- **Why**：PRICE_DATA_UNAVAILABLE 是系統性數據缺口，不代表市場沒有可操作的參考錨點（news.md 已確認 8/20 低點 $81.66，技術支撐 $80–$81 同步確認）。等到 FOMC 決議後再建倉，屆時資訊已全面公開，先行不對稱消失。Sahm Rule 0.38、NFP 連兩月 < 60K、機構流入轉正，均是有時效性的宏觀信號，全部忽略是把不確定性放大為零倉位的藉口，超出謹慎範疇。

## Balanced adjustment proposal

- **Size**：維持 Small（0.5% NAV）。不接受激進派 2.5% NAV，因數據缺口使 R:R 無法精確評估；不接受保守派 0%，因宏觀方向性信號具備初步可信度。
- **Stop**：以即時確認價格為錨，設於 $80.00（較 news.md 低點 $81.66 約下方 2%，給予高波動緩衝，同時明顯寬於過緊之 $80.50 建議，但嚴於激進派 $79.00）。**價格確認前不開倉**。
- **Entry**：待 PRICE_DATA_UNAVAILABLE 解除，確認現價在 $81.00 以上後方建立試探性倉位；若現價已跌穿 $81.00，延至 9/4 NFP 數據後再評估。
- **Hedge**：本階段不採用 call spread，等 9/4 NFP 確認方向後再考慮選擇性加倉或引入期權。
- **Time horizon**：觀察期 2–4 週（至 9/11 CPI）；若 NFP + CPI 雙重觸發確認，升至 Small-Medium（1.0–1.5% NAV）並調整止損。

## Net $ risk if stop hits

假設 NAV = $500,000，倉位 0.5% NAV = $2,500；入場約 $81.66，止損 $80.00，跌幅 ~2.0%：

**最大止損損失 ≈ $50（= 0.01% NAV）**

此數字雖小，但 PRICE_DATA_UNAVAILABLE 解除前不開倉的紀律，是防止損失因不良執行擴大的首要控制。

## Net $ upside at T1 / T2

- **T1**（9/18 FOMC 確認降息 25bp，TLT +5%）：$2,500 × 5% ≈ **$125（= 0.025% NAV）**；R:R ≈ 2.5×
- **T2**（降息 50bp + 短暫軋空，TLT +12%）：$2,500 × 12% ≈ **$300（= 0.06% NAV）**；R:R ≈ 6×

NEUTRAL RISK COMPLETE
