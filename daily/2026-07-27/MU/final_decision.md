# Final decision — MU as of 2026-07-27

FINAL TRANSACTION PROPOSAL: **BUY**

**verdict**: BUY
**conviction**: 62%
**phase**: Phase-4-complete

> 無即時價格，使用已知歷史數據($904-$1,092範圍)。所有價位為參考水準，執行前須以即時報價重新驗證。

## Verdict
**MODIFY**（BUY CONDITIONAL）— 採用 Neutral 分層架構，並強制納入 Conservative 的跳空規則與加碼前提。

## Final trade card
| 欄位 | 數值 |
|---|---|
| 方向 | LONG |
| 進場區間 | 三層：0.5% NAV @ $940 附近；0.5% NAV @ $870–$890；0.25% NAV @ $850 以下 |
| 停損 | 成交均價 × 0.83（均價 $940 時約 $780）+ 跳空規則 |
| Target 1 | $1,366 |
| Target 2 | $1,490 |
| 核准倉位 | Medium — **1.25% NAV 上限**（首層 0.5% 立即執行） |
| 對沖 | SOX put，0.1% NAV 權利金預算，持有至 Samsung HBM4 認證結果公布 |
| 持有期 | 2–4 季（核心節點 2026 年 9 月 Q4 FY2026 財報） |
| 信心度 | M |
| R:R to T1 | 2.7x（T2 為 3.4x） |

**跳空規則（強制）**：單日缺口 ≥ -10%，隔日開盤以市價出場，不等 $780 回測。

**最大虧損估算**：正常停損 $2,128（0.21% NAV）；加 SOX put 權利金 0.1% NAV，合計約 **0.31% NAV**。Samsung 認證通過跳空至 $650 之尾部情境約 $3,857（0.39% NAV），部分由 put 抵銷。

## Risk debate adjudication
- **Aggressive 最強論點**：HBM 2026–2027 售罄、Q4 指引 $50B 與 Anthropic 多年合約皆為已落地事實而非預測；死等 $850 是用確定性換取 -9.6% 的機率性折價。
- **Conservative 最強論點**：三個月高管套現 $156.7M、零買入，方向完全一致；記憶體崩跌以跳空啟動，無跳空規則等於無停損。FCF/NI 19.5% 疊加 $250B 剛性建廠承諾，景氣轉弱時沒有軟著陸選項。
- **Net：我採 neutral 為主軸。** 估值訊號自相矛盾（Trailing P/E 51.4x FAIL、分析師均價 $866 低於歷史現價，但 Forward 倍數壓縮），且 market.md 為 PRICE_DATA_UNAVAILABLE——在無 ATR 可做 vol 調整下，Aggressive 的 2.5% NAV 屬主觀定價，不予核准；但 Conservative 的 0.5% 上限使不對稱性在組合層面失去意義。分層建倉把「時機風險」轉為「平均成本問題」，是唯一在資訊缺口下仍成立的解法。

## Monitoring trigger
**若 Samsung 宣布 HBM4 通過 NVIDIA Vera Rubin 平台認證並進入量產，或 MU 任一季度毛利率跌破 40%——立即在停損被觸及前主動減碼至零。** 加碼至 1.25% NAV 需同時滿足：Samsung 認證明確失敗（可溯源）+ Q4 財報毛利率 ≥40%。

## Catalyst calendar
- 2026-09 — Q4 FY2026 財報（毛利率與客戶 HBM 指引）
- 2026-Q4 — HBM4 16-Hi 樣品交付期限 / Samsung 認證結果
- 2026-12 — 回購禁令解除

FINAL DECISION COMPLETE
