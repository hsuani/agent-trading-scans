FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — ZS as of 2026-08-28

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

（ZS 不在 `pipeline/tools/held_tickers.txt` 內 = 新倉決策。REJECT 代表「不建倉」，
非「賣出」。無持倉可賣，故第一行 verdict 為 HOLD = 不動作。）

## Final trade card
不建倉，無交易卡。以下為紀錄用參數，禁止作為執行依據。

| Field | Value |
|---|---|
| Direction | 無部位（NO POSITION） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | 0% NAV（不建倉） |
| Horizon | Days to Weeks（重評節點 2026-09-03 財報後） |
| Conviction | L — 約 35% |
| R:R to T1 | 無法計算（價格資料缺失） |

## Dealbreaker（REJECT 理由）
兩項同時成立，任一即足以否決：

1. **停損無法量化**。ATR14 與即時支撐結構全面缺失，$175 / $172 皆為報告內轉述的
   靜態錨點，非驗證過的即時價位。在一個 6 個交易日後即有跳空催化劑的標的上，
   以未驗證錨點設停損等同無停損 —— 財報跳空會直接穿越停損價，紀律形同虛設。
2. **邊際優勢不存在**。投資計畫自評上下行幅度皆為 15–25%，中性方測算股票
   R:R 僅 1.1x。在 LOW conviction 下押注一個二元事件，期望值近零而變異數極高，
   這是賭博的結構，不是交易的結構。

## Risk debate adjudication
- **Aggressive 最強論點**：10.58% short interest 搭配 3.66 天 DTC，且催化劑日期已知；
  財報後才進場等於為已定價的確定性付溢價。此論點在邏輯上成立。
- **Conservative 最強論點**：CFO Kevin Rubin 與 CLO Robert Schlossman 在股價自 $303
  腰斬後、仍於 $147–150 繼續出售，且從無任何對應買進。這是全案時間標記最清晰、
  品質最高的反向信號，且不依賴任何估值假設。
- **Net**：我採納 **conservative** 較重。激進方的軋空論點犯了機率單向化的錯誤 ——
  中性方指出得對：若基本面惡化，空方不回補反而加碼，同一個 short interest
  數字可以往兩個方向解釋，因此它不是優勢，只是波動放大器。加上激進方的
  call spread 未對財報前 IV 膨脹與事後 IV crush 定價，實際成本高於其靜態試算。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 結構性零信任需求 | EO 14028 / CISA 強制框架撐起多年期政府訂單 | 法規底托仍在，FY2027 預算 9 月簽約 | 成立 |
| ARR / NRR 品質 | NRR 維持 120%+ | 2026 年 5 月已主動下修收入與 FCF 利潤率展望 | 觀察中（偏鬆動） |
| 籌碼結構觸底 | 機構賣壓進入尾聲 | 持股 93.6% → 50.3%，未見止穩證據 | 已失效 |
| 內部人行為對稱 | 賣出為計畫性、集中於高點 | 7 月股價腰斬後 CFO/CLO 仍在 $147–150 賣出 | 已失效 |

## 論點失效條件
與 Stop 分開；此處為論點紀律，價格未動也可觸發動作。
- 若 9/3 財報 NRR 低於 120%，或 ARR YoY 成長低於 18%，多頭估值支柱失效 → **維持不建倉，改列 AVOID 六個月**
- 若管理層第二度下修 FY2027 FCF 利潤率指引，需求疲弱由雜訊轉為趨勢 → **永久剔除觀察名單**
- 若財報後 30 日內 Form 4 仍無任何內部人淨買進，內部人支柱維持失效 → **不得建倉**
- 若 PANW 於財報或法說會公開具名披露自 ZS ZTNA 遷出的企業客戶 → **改判 SHORT 候選**

## 重新評估條件（未來可翻案）
須同時滿足：NRR ≥ 120%、FY2027 指引優於 5 月重置版本、財報後出現內部人淨買進，
且即時價格資料恢復可算出 ATR14 與有效停損。屆時方可以 Small（≤ 1.0% NAV）建倉。

## Monitoring trigger
2026-09-03 財報公布後 24 小時內重新評估，不等待任何價格條件。財報前若價格
資料恢復且股價跌破 $175，直接記錄為下行趨勢確認，建倉門檻進一步提高。

## Catalyst calendar
- 2026-09-03 — ZS Q4 FY2026 財報（ARR 成長率、NRR、FY2027 指引）
- 2026-09 月 — 美國聯邦 FY2027 預算週期集中簽約
- 財報後 30 日 — Form 4 內部人申報窗口，確認是否出現淨買進

FINAL DECISION COMPLETE
