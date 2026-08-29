FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — EQIX as of 2026-08-29

## FINAL TRANSACTION PROPOSAL: **HOLD**

（HOLD = 不建立新倉、不投入新資金,維持觀察名單。EQIX 不在 `held_tickers.txt`,無既有部位可減。）

> **PRICE_DATA_UNAVAILABLE** — yfinance 代理封鎖(403)。本決策不含 Entry / Stop / Target / R:R 數值。

## Verdict
REJECT

## Final trade card
不適用 — 本次為 REJECT,不建立部位。

| Field | Value |
|---|---|
| Direction | 無部位 |
| Size | 0% NAV |
| Horizon | 觀察至 2026-10 中旬 Q3 財報 |
| Conviction | M(對「不進場」的確信度,非對方向) |

## Dealbreaker(明確講清楚)
**組合層面的重複曝險,而非 EQIX 本身的基本面。** 現有持倉已含 **DLR**(直接同業,共用同一套 8GW+ 供給管線與 2027-2028 供過於求風險)與 **AMT**(同屬長端利率久期敏感的 REIT)。買進 EQIX 等於在同一個因子(長端利率 + 資料中心供給週期)上第三次下注,分散效益接近零,而 Conservative 指出的 -3%/年負 carry 會被複製三份。

第二層 dealbreaker:在 PRICE_DATA_UNAVAILABLE 下無法計算 ATR、無法設定止損。以 55% 確信度的 NEUTRAL 論述,搭配不可量化的下行敞口,新資金沒有理由現在進場。研究經理本人也寫「新資金入場吸引力不足」。

## Risk debate adjudication
- **Aggressive's strongest point**:「等觸發訊號才買 = 在更高價買已知利多」——這個批評對單一標的成立,Q2 硬數字(營收 $2.625B YoY +16.4%、淨互連 9,700 條紀錄、P/AFFO 22-25x 對 +10-12% AFFO 成長)品質確實高於空方的預測型論述。
- **Conservative's strongest point**: 無價格資料即無止損,任何倉位都是裸露曝險;加上 -3% 負 carry,持有六個月光 carry 就吃掉基準情境上行的三分之一。
- **Net: 我採納 conservative 較多**,理由是 Aggressive 的 R:R 翻轉論據(call spread 1.2-2.0:1)建立在未知現價乘以未知權利金之上,Neutral 已正確指出這是「兩個估算值相乘」。但我否決 Neutral 的 0.5% NAV 折衷案——那是為持倉者設計的,對新資金而言,0.5% 的部位在 +15% 基準情境只貢獻 +0.075% NAV,不值得承擔一條無法設停損的曝險與管理成本。**新倉的門檻應該高於續抱。**

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 驅動互連需求 | 淨互連新增維持紀錄水準 | Q2 新增 9,700 條創歷史紀錄,最大客戶合約 60% 涉 AI | 成立 |
| P/AFFO 估值相對成長合理 | P/AFFO ≤25x 搭配 AFFO +10% 以上 | 22-25x vs 成長 +10-12%,與同業 24-27x 持平 | 成立 |
| 利率環境容許 REIT 倍數擴張 | 30Y 美債殖利率回落至 4.5% 以下 | 現為 5.2%,股息殖利率僅 2.0-2.2%,負 carry | 已失效 |
| 管理層行為與指引一致 | 指引上調應伴隨內部人增持 | 六個月 0 買進 / 330 賣出 / 淨 -$16M+ | 觀察中 |

兩根成立的支柱都在「營運」側,兩根鬆動的都在「股價傳導」側。營運好但傳導管道堵住 —— 這正是 REJECT 而非 BUY 的結構性理由。

## 論點失效條件
與 Stop 分開;此處無 Stop(無部位、無價格)。
- 若 Q3 或 Q4 任一季 **淨互連新增條數環比下滑**,「AI 互連需求」支柱失效 → 永久移出觀察名單。
- 若 **AFFO/share 年度指引下調**,或 **Net Debt/EBITDA 升穿 4.0x**,估值支柱失效 → 移出觀察名單。
- 若 **AWS 或 Azure 公開宣佈加速遷出 Equinix 互連層**,護城河支柱失效 → 移出觀察名單。

## 重新評估的正向條件(what would change it)
須 **同時** 滿足兩項才重啟建倉討論,且屆時倉位上限 1.0% NAV:
1. 價格資料恢復,可計算 ATR 與明確止損水位;
2. 30Y 美債殖利率跌破 4.5%(Fed 2026-09-12 後確認),**且** Q3 淨互連新增環比未放緩。

若屆時仍持有 DLR,EQIX 建倉須以減碼 DLR 為前提,資料中心 REIT 合計曝險不超過 2.5% NAV。

## Monitoring trigger
若 Fed 於 2026-09-12 釋出明確降息路徑且 30Y 跌破 4.5%,在 Q3 財報前提前重評;若 30Y 反向突破 5.5%,則連同 DLR / AMT 一併檢視組合利率久期。

## Catalyst calendar
- 2026-09-12 — Fed FOMC 政策決議(利率路徑)
- 2026-10 中旬(待確認) — EQIX Q3 FY2026 財報
- 持續 — SEC Form 4 內部人交易方向、xScale JV 選址公告、借貸成本是否守住 4.2%

FINAL DECISION COMPLETE
