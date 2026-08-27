# Final decision — MUB as of 2026-08-08

FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY — 維持現有持倉規模，不加碼、不主動減倉，但把利率停損由 10yr 5.0% 收窄至 **4.90%**，並否決 TLT put 對沖。

## Final trade card

| Field | Value |
|---|---|
| Direction | NEUTRAL（帳上為 LONG duration 的 income 持倉，不新增方向性風險）|
| Entry zone | PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位 |
| Stop | 利率條款式：10yr UST 收盤 **≥ 4.90%**（+27bp）觸發，縮至半倉並轉 1–5 年短 duration 市政債；無即時價格，暫不給進出場價位 |
| Target 1 | 10yr 回落至 **4.30%**（−33bp）→ 倉位報酬約 +2.6% |
| Target 2 | 10yr 回落至 **4.10%**（−53bp，Fed 暫停確認）→ 倉位報酬約 +4.9% |
| Size | Medium — 維持現有約 5% NAV，不增不減 |
| Horizon | 戰術 14 天（至 8/22）；核心 income 邏輯為季度至年度 |
| Conviction | **60%**（MEDIUM）|
| R:R to T1 | 1.5（T2 約 2.8）|

## Sizing rationale
既有持倉的「不動」本身就是最低摩擦選擇。加碼要求承擔 56.7% 升息機率下的額外 duration 暴露，只換取 14 天約 0.22% 的 TEY 複利，報酬風險不成立；縮減 25–30% 則要付出賣出、再進場的雙向摩擦與時機風險，成本可能高過所省下的 duration 損失。停損觸發時組合層級損失僅約 −0.088% NAV，此暴露在現有規模下完全可承受，不需事前削減。

## Risk debate adjudication
- **Aggressive 最強論點**：AMT-Free 指數設計已在成分層面排除 Private Activity Bonds，空方最具結構性的需求侵蝕論點對 MUB 根本不適用——這點我完全採納，因此不以 AMT 為減倉理由。
- **Conservative 最強論點**：5.0% 停損預留 37bp 不利空間，在升息為模態結果（非尾部）的環境下過於被動；早期警報線確有必要。
- **Net**：我採 **neutral** 較重。Aggressive 的 3:1 不對稱前提（升息為少數場景）與 56.7% 升息機率自相矛盾，邏輯有缺口；Conservative 的 4.80% 距現行隱含水位僅 17bp，等同以雜訊執行停損，且 TLT 與 MUB duration 相關性不完美，0.10–0.15% 對沖成本對 income 倉位效益比偏差。4.90% 是唯一能過濾單次數據衝擊、又不放任被動的水位。

## Monitoring trigger
若 **ICI 週度市政債資金流向連續兩週淨流出**（$57B H1 流入動能逆轉），即使 10yr 未達 4.90%，也須在停損前重新評估——資金面反轉會使 NAV 折損非線性放大，是本論文中唯一不由利率直接驅動的失效路徑。

## Catalyst calendar
- 2026-08-15 — 零售銷售與工業生產（偏弱→強化暫停預期）
- 2026-08-22 — Jackson Hole Fed 講話（鴿派 + 10yr < 4.30% 才可加至滿倉）
- 2026-09-19 — FOMC（升息 vs 暫停 + 更新點陣圖）

FINAL DECISION COMPLETE
