FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — VST as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

（持倉判定：VST 不在 `pipeline/tools/held_tickers.txt` 內 → 新倉，適用 A 框架。
Phase indicator：Phase 2-4 full pipeline 完成。）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無即時價格 (PRICE_DATA_UNAVAILABLE) |
| Stop | 無即時價格 (PRICE_DATA_UNAVAILABLE) — 以下方論點失效條件代行紀律 |
| Target 1 | 無即時價格 (PRICE_DATA_UNAVAILABLE) — 對應 Q3 EPS 回歸共識、ERCOT 解凍情境 |
| Target 2 | 無即時價格 (PRICE_DATA_UNAVAILABLE) — 對應 PPA 啟動確認 + FOMC 轉向降息情境 |
| Size | Small-Medium — 首批 0.75% NAV，觸發後追加 0.50%，總上限 **1.25% NAV** |
| Horizon | 中期 12-18 個月 |
| Conviction | M（約 55%） |
| R:R to T1 | 無法量化 (PRICE_DATA_UNAVAILABLE)；定性判斷為中性偏正，T2 情境才具明顯不對稱性 |

**執行紀律**：因無即時報價，首批一律以限價單分筆執行，取得實際報價與 ATR 後
才依波動度回補至 0.75%。不得市價追價。

## Risk debate adjudication
- Aggressive 最強的一點：等待 2026-09-16 FOMC 沒有資訊增量——25 bps 已被期貨
  市場定價，為了「確認一件已知的事」延後兩週建倉，是純粹的負 alpha。這點成立，
  故首批不等 FOMC。
- Conservative 最強的一點：Q2 EPS miss 59% 不能一句「商品噪音」帶過。若全年
  EPS 由 $9.30 下修至 $6-7，則 EV/EBITDA 7.8x 反映的是盈利惡化而非市場錯估——
  多頭的估值支柱可能是幻覺。這點無法反駁，故總倉位不放大。
- Net：**採 neutral 觀點為主**。理由是本案兩邊各對一半——進場時點上 Aggressive
  對，倉位規模上 Conservative 對。Aggressive 的 2.5% 與 EBITDA $14 億止損門檻
  過寬，實質廢掉失效紀律；Conservative 的 0.5% 加上「三取二」加碼門檻，則會讓
  進場永遠落在價格反應之後。故取：立即進場、但總量壓在 1.25% NAV。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 核電護城河與長約鎖定 | Meta/AWS 2,600 MW+ 20 年 PPA、Comanche Peak 許可至 2053 | 合約已簽，非預測；但現金流最快 2027 末啟動 | 成立 |
| 營運現金流強度 | 調整後 EBITDA 維持成長 | Q2 EBITDA $17.7 億 +31% YoY 創高，FCF Margin 20-22% | 成立 |
| 盈利能見度 | 全年 EPS 共識 $9.30 兌現 | Q2 EPS $0.91 vs 共識 $2.21，偏差 59% | 觀察中 |
| ERCOT 需求成長 | 德州 2027 負荷成長 14% | 並聯凍結後腰斬至 6%，審計時程未定 | 觀察中 |

兩根支柱成立、兩根觀察中、零根失效——這正是 1.25% 而非 2.5% 的理由。

## 論點失效條件
（與 Stop 分離；論點先壞就動作，不等價格）
- 若 Q3 2026 財報 EPS miss ≥30% **且** 調整後 EBITDA < $15 億，盈利能見度支柱
  失效 → 減碼至 0.4% NAV 以下
- 若管理層在 Q3 財報下修全年 EBITDA 指引至 $6.8B 以下，同一支柱失效 → 出場
- 若 ERCOT 正式公告並聯凍結延續至 2027 年，需求支柱失效 → 立即全數出場
- 若 IRA 核電 PTC 遭實質削減（法案通過或財政部規則明文縮減），護城河支柱
  失效 → 出場
- 若 Cogentrix 交割延後至 2027 年或出現資產減值，分散化支柱失效 → 減碼一半

## Monitoring trigger
若 10 年期美債殖利率突破 5.0%，或 FOMC 點陣圖顯示 2027 年前無降息路徑，在
任何價格 Stop 觸發前重新評估估值倍數假設與部位規模。

## Catalyst calendar
- 2026-09-16 — FOMC 利率決定與點陣圖（預計 +25 bps 至 3.75-4.00%）
- 2026-09-21 — 現金股利支付日（$0.23/股）
- 2026-10-15 前後 — Q3 2026 財報（最重要驗證點；EPS ≥$2.00 為加碼條件之一）
- 2026-12 — Cogentrix +5.5 GW 交割完成
- 持續 — ERCOT 審計結果與並聯申請恢復時程（另一加碼條件）
- 2027 末 — Comanche Peak 1,200 MW PPA 首批商轉

**附注**：內部人士交易數據在 investment_plan.md（淨賣出 $1.91 億）與
fundamentals.md（淨買進 $20-30M）之間存在直接矛盾。在核實前，此項不列為
任何一方的論據，多空皆不採用。

FINAL DECISION COMPLETE
