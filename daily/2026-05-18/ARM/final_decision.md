# Final decision — ARM as of 2026-05-18

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
APPROVE（採納 trader 條件式 HOLD，疊加 neutral 之 Put 對沖）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（僅在觸發後建倉；當下不進場） |
| Entry zone | $195.00 – $205.00（FTC 公告後當日收盤確認，不追跳空） |
| Stop | $166.69（結構性局部高點，跌破即中期上升結構受損） |
| Target 1 | $239.50（52 週高點阻力） |
| Target 2 | $280.00（牛方研究區間下緣） |
| Size | Small（0.5% NAV，觸發後分批建立） |
| Horizon | 1–3 個月（FTC 裁定 + 2026-07-29 財報雙窗口） |
| Conviction | M |
| R:R to T1 | 1.36（以 Entry $197.50 計）；R:R to T2 ≈ 2.4，合格 |
| 對沖 | ARM 2026-09 $170 Put，成本約 0.05–0.07% NAV |

## Risk debate adjudication
- Aggressive 最強論點：FTC 二元事件「等到確定時股價已不在」，call spread 捕捉非線性跳升。
- Conservative 最強論點：FTC 拆分裁定具跳空繞 Stop 性質，倉位必須小到 Stop 失效仍不傷帳戶。
- Net：採納 **neutral** 立場。Aggressive 1.5% NAV + 立即進場在二元事件未解前過度承擔尾部風險；Conservative 將 Stop 收緊至 $182 在 ATR $14.61 環境下會被正常震盪洗出。0.5% NAV + 結構性 Stop $166.69 + Put 對沖 = 風險可控且保留事件後加碼彈性。

## Monitoring trigger
**FTC 裁定性質**：行為修正令落地 → 觸發 $195–$205 分批建倉並考慮加至 1.0–1.5%；若公告為結構性拆分授權業務或強制重構 AGI CPU 計畫 → 立即放棄論題、Put 對沖兌現。在此裁定前其他指標均為次要雜訊。

## Catalyst calendar
- 2026-07-29 — Q1 FY2027 財報（A/R 回落、FCF/NI ≥50%、Armv9 滲透率 >30%）
- 2026 Q3（預估） — FTC 調查初步方向或中期裁定
- 每週追蹤 — Qualcomm 反訴 ARM 訴訟進展

FINAL DECISION COMPLETE
