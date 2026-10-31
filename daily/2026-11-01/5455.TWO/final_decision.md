# Final decision — 5455.TWO as of 2026-11-01

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
**DATA_INTEGRITY_ISSUE — Phase-1-only stub, 未進入 Phase 2-4。本股不計入 tw_photonics 正常排名。**

## 核心問題
universe.py taxonomy 將 5455.TWO 定義為「英特磊」（矽光子磊晶供應鏈上游，tw_photonics 族群成員）。本次 Phase 1 四份報告（fundamentals、market、sentiment、news）皆獨立觀察到 yfinance 針對 5455.TWO 回傳的實際公司身分為 **Sheng Yi Development Co., Ltd（聖億建設，房地產開發商）**，與預期的光通訊業務完全不相關：
- 現價 30.35 TWD（聖億建設口徑）vs 既有歷史筆記記錄「英特磊」價格區間 365–537 TWD。
- 業務描述為住宅/公寓建設與銷售、建材銷售，與矽光子磊晶毫無關聯。
- 財務數字（TTM 營收僅 0.27 億 TWD、連續 4 季虧損）明顯是小型房地產開發商的規模與特徵，不符合英特磊應有的光通訊元件廠規模。

## 為何不進行 positive-pick 評分
由於公司身分本身未經核實，對本股套用 positive-pick 的五項訊號評分（Fundamentals/Market/News/Sentiment/Valuation）在方法論上無意義——無論評分結果為何，都無法確定評分對象究竟是「英特磊」還是「聖億建設」。因此本報告不進行正式評分，直接標記為 HOLD / 不交易，並建議排除於 tw_photonics 族群排名之外。

## 建議後續行動
1. 人工核對 5455.TWO 在 TWSE/TPEx 的正確對應標的（ticker 代碼可能已變更、重複使用或來源對照表有誤）。
2. 若確認「英特磊」的正確 ticker 為其他代號，應將其排入下一輪 tw_photonics 掃描。
3. 本次 serenity/universe.py 的 tw_photonics 清單中 5455.TWO 的對照關係需要排程修正，否則每次掃描都會重複此問題。

## 資料限制聲明
本報告僅使用 2026-11-01 當日工具輸出與同日 WebSearch 結果。所有引用數字均基於 yfinance 實際回傳的 5455.TWO（聖億建設）資料，而非「英特磊」的真實基本面。

FINAL DECISION COMPLETE
