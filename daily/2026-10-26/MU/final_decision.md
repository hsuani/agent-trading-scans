FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — MU as of 2026-10-26

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

（步驟 0：MU 不在 `pipeline/tools/held_tickers.txt` 清單內，依新倉 A 框架審核。問題是「該不該進」，不是「該不該續抱」。）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $849.25 – $877.55（第一批試探倉，現價 $877.55） |
| Stop | $849.25（收盤跌破須**連續 2 日收盤確認**；寬停損 $737.88 僅限獨立 ≤0.2% NAV 衛星倉，禁止與主倉疊加） |
| Target 1 | $931.65 |
| Target 2 | $982.73 – $986.70（MA50/MA20 動態壓力區） |
| Size | Small 0.5% NAV 起步；加碼觸發後累計上限 1.5% NAV；12/23 財報前不得升至 Large |
| Horizon | 1–4 週技術確認（10/27–10/29），延伸至 12/23 財報後重估；不視為多季長抱 |
| Conviction | L |
| R:R to T1 | 1.9（風險 $28.30 / 報酬 $54.10） |

加碼觸發（簡化為二擇一）：收盤站回 $931.65 **且**（收復 MA20/MA50 $983–987 **或** MACD histogram 翻正）其一成立，加碼當日成交量須 ≥1x 10 日均量。
事件對沖：僅針對 12/23 財報窗口，以小額 MU put 或 $900/$1000 2027/1 call spread 二擇一；FOMC/SK hynix 窗口不另行對沖。

## Risk debate adjudication
- Aggressive's strongest point：原三條件「同時成立」的加碼門檻，實際上要等到 $983–987 站上才啟動，距 T2 已近在咫尺，alpha 大半被等掉；且緊停損 $28.30 窄於 1 個 ATR（$47.85），被噪音洗出的機率確實偏高。
- Conservative's strongest point：10/23 反彈量僅 0.78x 均量，第一批等於在雜訊帶買進；三條件可能被 10/29 單日跳空一次滿足，讓加碼時點恰好落在財測環比降至 +13% 的基本面轉弱窗口。寬停損 $737.88 若誤套在 1.5% NAV 倉位上，R:R 跌至 0.4，必須嚴格隔離。
- Net：我採 **neutral** 的折衷。Aggressive 要求第一批直接 1.5–2% NAV 並同時下移停損，是在 LOW 信心下雙重放大 $ 風險，與投資計畫定調矛盾；Conservative 對 0.016% NAV 的試探倉再要求 2 日確認進場加 put 對沖，防禦成本已超過部位本身的風險。採「2 日收盤確認」解決 aggressive 的洗出顧慮、以 0.5% 起步解決 conservative 的量能顧慮，加碼門檻改二擇一但加上量能條件，兼顧兩邊。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 近期財報與財測硬數據 | 營收與財測持續優於共識 | FQ4 營收 54.23B vs 共識 51.5B；FQ1 FY27 財測 61.5B vs 57.9B（+6%）；淨現金 33.2B、D/E 3.7% | 成立 |
| 毛利率守在週期高位 | 毛利率不自 86.8% 明顯回落、forward EPS 206.89 站得住 | 尚無新數據，12/23 財報為驗證點；財測隱含環比僅 +13%，增速已拐 | 觀察中 |
| HBM/DRAM 定價維持 | HBM 長約、Samsung Q4 漲價 7–10% 落實、合約價不轉跌 | 10/29 SK hynix 財報與 10–11 月 TrendForce 合約價待驗；CXMT 份額 3%→8%、Apple 測試 LPDDR5X 為反向壓力 | 觀察中 |
| 長期技術結構未破 | 價格守 MA200 之上、$849.25 不破 | 高於 MA200 +19.9%、MA50 > MA200、MACD histogram 自 -23.68 收斂至 -17.07；但 lower highs/lows、自高點 -30.1% | 觀察中 |

## 論點失效條件
必須可證偽，且與 Stop 分開（Stop 是價格紀律，這裡是論點紀律）。
- 若 12/23（估）FQ1 FY27 毛利率明顯低於 FQ4 的 86.8%，**或** FQ2 營收財測環比轉平/轉負 → 毛利率支柱失效 → **出場**，不等價格打到 Stop。
- 若 10/29 SK hynix 財報顯示 HBM 價量轉弱，**或** TrendForce 10–11 月 DRAM 合約價報導轉跌，**或** Samsung Q4 漲價 7–10% 未落實 → 定價支柱失效 → 凍結加碼，**減碼**至 ≤0.3% NAV。
- 若 CXMT LPDDR5X 通過 Apple 認證且見量產出貨報導 → 競爭侵蝕由「非核心」升級為「核心」 → **減碼**。
- 若收盤跌破 MA200（$732.10） → 技術結構支柱失效 → 轉 SHORT_OR_AVOID，全部出清（含衛星倉）。

## Monitoring trigger
If 收盤跌破 $849.25（即使僅單日），或 10/27–10/29 FOMC 鷹派意外導致高 Beta 板塊去槓桿，在 2 日確認未完成前先重新評估是否提前離場；若同時持有 MRVL 等半導體曝險，應合併計算板塊集中度。

## Catalyst calendar
- 2026-10-27 至 10-29 — FOMC 會議
- 2026-10-29 — SK hynix 財報（驗證 HBM 價量）
- 近期 — Samsung Q4 DRAM 漲價 7–10% 是否落實
- 2026-10 至 11 月 — TrendForce DRAM 合約價更新
- 待確認 — CXMT LPDDR5X 於 Apple 的認證結果
- 2026-12-23（估）— MU FQ1 FY27 財報（毛利率、FQ2 財測，二元事件）

FINAL DECISION COMPLETE
