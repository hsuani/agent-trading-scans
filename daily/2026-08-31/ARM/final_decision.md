FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — ARM as of 2026-08-31

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

> 新倉框架 (ARM 不在 held_tickers.txt)。股票部位 **0% NAV — 不建倉**；僅核准一筆
> 條件式期權偵察倉。Conviction 4/10 (L)。

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG (call spread, 非股票) |
| Entry zone | $370/$470 call spread, 到期 2027-01；淨權利金 ≤ $18.00/spread (超過即棄) |
| Stop | 不適用 — 最大損失 = 已付權利金 (內建上限) |
| Target 1 | 標的 $420 (spread 市值約 $30) |
| Target 2 | 標的 $470+ (spread 全額 $100) |
| Size | Small — 0.15% NAV (股票部位 0% NAV) |
| Horizon | 至 2027-01 到期 (覆蓋 Q3 FY2026 財報 + AGI CPU 量產) |
| Conviction | L (4/10) |
| R:R to T1 | 1.7 (T2 約 5.7，前提為權利金 ≤$18 經真實報價驗證) |

**執行前提 (硬性)**：PRICE_DATA_UNAVAILABLE，錨點 ~$369 為 UNVERIFIED。未取得
真實 bid/ask 報價前不得下單。若實際淨權利金 >$18 或 IV 84 使 T2 R:R 低於 4:1，
整筆放棄，退回 0% NAV 純觀察。此筆為選配 (optional)，不執行不算失誤。

## Stock BUY Gate (股票部位重評條件, 須同時滿足)
1. 價格回落至 **$245–$280** (UNVERIFIED)；不採納保守方壓低至 $200–$215
2. Q3 FY2026 non-GAAP 營業利潤率回升至 **10%+** (vs 現 7%)
3. Qualcomm NUVIA ALA 上訴裁決結果明朗且未實質削弱授權執行力
4. 機構持股升至 **3%+** (vs 現 0.47%)

觸發後起始 Small 0.5% NAV，AGI CPU 首筆代理稅收認列後才評估加至 1.5% NAV。

## Risk debate adjudication
- Aggressive's strongest point: R:R 1:1.4 是工具選擇問題而非 thesis 問題；
  call spread 可在絕對損失封頂下取得不對稱性，且距 Q3 財報僅 4–6 週，全空手
  等待 -24% 至 -34% 回調的機會成本真實存在。
- Conservative's strongest point: Qualcomm 上訴與 AI CapEx 週期是兩個未解的
  二元事件；244x trailing P/E 加上 Q1 已發生 -38% EPS 錯失，容錯空間為零，
  機構持股 0.47% 是專業資金對此價位的結構性棄票，不是尚未發現的機會。
- Net: 我採 **neutral** 權重最高。積極方的數學我接受，但它建立在未驗證的
  $17.5 權利金上——在 PRICE_DATA_UNAVAILABLE 下宣稱 5.7:1 是循環論證。保守方
  的 75% 尾部概率加總與其自己承認的「成長引擎真實」自相矛盾，GF Value $187.72
  以歷史盈利錨定 v9 費率拐點亦有方法論瑕疵。故：股票 0%，期權減至 0.15% 並
  加掛權利金驗證閘門。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 代理稅收動能 | YoY >25% | Q2 FY2026 $737M, +27% YoY | 成立 |
| 資料中心市佔 | ARM server >40% 營收佔比 | 45–50%，AGI CPU 已簽 Oracle/ByteDance/Meta | 成立 |
| 費率紅利轉化為盈利 | 營業利潤率維持 11%+ | 壓縮至 7%，研發吞噬紅利 | 已失效 |
| 授權執行力 (護城河) | ALA 條款可強制執行 | 2025-09 一審不利，上訴未決 | 觀察中 |
| 估值/籌碼結構 | 專業資金認同 | 現價高於街道中位 25–35%；機構 0.47%、90 天 20 筆 insider sell 零買進 | 已失效 |

兩根支柱已失效 → 這正是股票部位維持 0% NAV 的直接依據；剩餘成立的兩根僅足以
支撐一筆權利金封頂的偵察倉，不足以支撐方向性股票部位。

## 論點失效條件
與 Stop 分開；以下為論點紀律，觸發即動作，不等價格。
- 若 Q3 FY2026 代理稅收 YoY **低於 20%**，成長支柱失效 → 取消 BUY Gate，
  期權倉不加碼且不展延，觀察降級為 AVOID
- 若 Qualcomm NUVIA ALA 上訴 **確定敗訴**，護城河支柱失效 → 立即出清期權倉，
  BUY Gate 全面撤回
- 若 Q3 FY2026 non-GAAP 營業利潤率 **連續兩季低於 8%**，盈利轉化支柱確認失效
  → 永久移除 BUY Gate 條件 2 之外的建倉可能
- 若 Amazon/Google/Microsoft 任兩家於 Q3 財報 **下修 2027 AI CapEx 指引**，
  週期支柱失效 → 期權倉即刻減半
- 若 RISC-V 於資料中心/伺服器新設計案佔比 **升破 15%** (現邊緣 10–15%、
  整體 25%)，長期護城河支柱失效 → 出場

## Monitoring trigger
若股價在無新催化劑下反彈至 **$400+** (估值泡沫警戒)，或 Q3 財報前 IV 由 84
升破 100，在 stop 前重評：前者代表 BUY Gate 永不觸發、應正式放棄追蹤；
後者代表權利金已被吃掉 R:R，偵察倉不得執行。

## Catalyst calendar
- 2026-09 至 2026-10 — Q3 FY2026 財報 (代理稅收 YoY、營業利潤率、AGI CPU 進度)
- 2026 下半年 — Qualcomm NUVIA ALA 上訴裁決 (日期待確認)
- 2026-10 前後 — Amazon / Google / Microsoft Q3 財報之 2027 AI CapEx 指引
- 2026 年底 — AGI CPU 量產首批出貨與首筆代理稅收認列
- 2027-01 — call spread 到期

FINAL TRANSACTION PROPOSAL: HOLD ARM 0% NAV (股票)；選配期權偵察倉上限 0.15% NAV，
須先驗證真實權利金報價。

FINAL DECISION COMPLETE
