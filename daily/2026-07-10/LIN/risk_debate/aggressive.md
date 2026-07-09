# Aggressive risk view — LIN

## Where trader is too cautious

- **倉位規模近乎放棄阿爾法：** 0.5% NAV 等同宣告放棄本次機會。一個擁有 $100 億 take-or-pay 積壓、EPS +10% YoY、67–69% 分析師買進共識的標的，僅維持象徵性半倉，是對信念的過度折扣。NEUTRAL / MEDIUM conviction 不代表「倉位為零」，而是應對應 1.0–1.5% NAV 的受控部位。
- **等待財報是在讓市場替你定價：** 距 2026-07-31 Q2 財報僅三週，現在是預先佈局 options 的最佳窗口——財報臨近時 implied volatility（IV）將大幅上升，call spread 買入成本將顯著墊高。今日行動的選擇權溢價成本明顯低於兩週後。計畫要求「等確認再進場」，但確認出現時，入場成本已大幅上升，R:R 惡化。
- **空方最強武器已在弱化：** 內部人士賣出均發生於 $440–$508，若當前市價高於此範圍，其心理壓力已大幅消散。做空邏輯最後一根支柱（估值壓縮）在一個 Q2 超預期情境下可在單日內反轉，而短利息僅 1.39%，空方無法維持足夠壓力形成系統性做空。

## Recommended adjustments

- **Size：** 0.5% NAV → 1.5% NAV（以 options call spread 承載，最大虧損鎖定於權利金，無裸部位風險）
- **Stop：** PRICE_DATA_UNAVAILABLE，無法給絕對價位。策略層面：以 options 結構自帶定損，不設傳統股票停損，避免在財報前的正常波動中被洗出。
- **Entry：** 今日或本週進場佈局，而非等待 2026-07-31；現在的 IV 成本低於財報前一週。
- **Consider：** 財報前 call spread（long lower-strike call / short upper-strike call），到期選 2026-08-15 或 2026-09-19（覆蓋財報後市場消化期）。具體 Strike 待價格資料可用時補充（PRICE_DATA_UNAVAILABLE）。

## Asymmetry argument

以 1.5% NAV 的 call spread 為架構：

- **最壞情境最大虧損：** 1.5% NAV（權利金全部歸零）；有定義上限，不存在無限虧損。
- **現實多頭情境潛在獲利：** 若 Q2 EPS 超預期且氫能積壓回升，分析師中位數目標 $525–$546 提供可觀空間；call spread 的 delta + vega 組合在財報後跳空高開情境下潛在報酬可達權利金 2–4 倍。
- **非對稱比：** Realistic upside / Max loss ≈ 2:1 至 4:1。即便只有 50% 的Q2 超預期機率，期望值為正。

> 注意：PRICE_DATA_UNAVAILABLE，以上均為定性框架；絕對獲利金額待報價補齊。

## What I'd push for

現在距 Q2 財報三週，是進場 call spread 的黃金視窗而非等待期。計畫建議的「HOLD 0.5% NAV 等待確認」等同於用最昂貴的時間成本換取確認，在財報跳空後才追入，付出更高的 IV 與更差的 R:R。正確策略是：以 1.5% NAV 買入低成本 call spread（到期 2026-08-15/09-19），最大虧損鎖定於初始權利金，財報若觸發 Upside trigger（EPS 超預期 + 積壓淨增 + Beaumont 更新）則捕獲槓桿收益。若財報觸發 Downside trigger，損失嚴格控制在 1.5% NAV，遠低於等待確認後才建立的股票倉位風險。這是非對稱性最佳的進場時機，放棄即是浪費已識別的催化劑視窗。

AGGRESSIVE VIEW COMPLETE
