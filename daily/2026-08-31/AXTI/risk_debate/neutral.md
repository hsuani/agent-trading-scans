# Neutral risk view — AXTI

## Points of agreement (both sides)
- PRICE_DATA_UNAVAILABLE 使股票空頭倉位的停損指令無法以正確價格提交給券商；這是操作事實，非立場差異。
- 基本面空頭論述（EV/Sales 27x 對比同業 10x、31 次淨內部人賣出、股價超出所有分析師目標）在邏輯上成立。
- Q3 2026 財報（2026-10-29 至 11-02）是最具確定性的催化劑視窗；現在到財報前存在時間不確定性。
- 任何執行均須先取得可驗證即時報價。

## Aggressive overreach
- **所在**：「等待本身就是最大的風險」、主張立即建立 0.75% NAV 股票空頭。
- **為何過度**：R:R 3.1x 的計算完全建立在 UNVERIFIED 價格上，止損 $106 UNVERIFIED 與其他水位同樣無法執行。聲稱「機會視窗最寬」忽略了一個事實——若 gap risk 發生，無法執行停損的空頭倉位可將損失放大至 2x 帳面計算。論述的邏輯正確，但執行工具不可用時，正確的論述無法保護倉位。

## Conservative overreach
- **所在**：「純 AVOID、零倉位是唯一可辯護立場」，完全拒絕任何曝險。
- **為何過度**：Put spread 結構（如買 $90 Put / 賣 $65 Put，到期 2026-12）的最大損失等於支付的期權金，在下單當下即鎖定，不依賴任何 UNVERIFIED 停損水位的執行——PRICE_DATA_UNAVAILABLE 問題對 defined-risk 選擇權結構並不適用。完全排除此工具屬於過度保守，未能區分「股票空頭的執行風險」與「選擇權的定義風險」。

## Balanced adjustment proposal
- **Size**：股票空頭倉位 = **0%**（保守方正確；無可驗證報價不開股票空倉）。Put spread 期權金支出 ≤ **0.20% NAV**（非 0.3%，進一步壓縮尾部損失）。
- **Stop**：Put spread 結構無需停損；最大損失即期權金，於成交時確定。
- **Entry**：取得可驗證即時報價後，若股價仍在 $88–$96 UNVERIFIED 區間，評估 Put spread 期權金是否合理（Delta ~0.30–0.35）再執行；不追高。
- **Hedge**：以 Put spread 本身作為曝險上限；不另加裸空。
- **Time horizon**：2026-12 到期 Put spread 涵蓋 Q3 財報視窗，符合核心催化劑時間點。

## Net $ risk if stop hits
假設 NAV = $1,000,000，Put spread 期權金 = 0.20% NAV = **$2,000**（期權金全損為最壞情況；無跳空擴大風險）。

## Net $ upside at T1 / T2
- **T1**（股價回至 ~$87.50 UNVERIFIED，Put spread 部分獲利）：**~$3,000–$4,000**（R:R ~1.5–2.0x）
- **T2**（中國出口許可凍結，股價跌至 ~$52.50 UNVERIFIED，Put spread 接近最大獲利）：**~$12,500–$15,000**（= Put spread 最大價差 $25 × 名義張數，R:R ~6–7x）

NEUTRAL RISK ASSESSMENT COMPLETE
