FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — AVGO as of 2026-10-19

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 定位
AVGO 不在 `held_tickers.txt`，屬新倉決策。問題是「該不該進」，答案是：今天不進，但把交易員留白的條件式進場卡鎖定成一張可執行的卡。交易員的 HOLD/AVOID 方向我接受；修改點在於 (1) 試單由 1/3 降為 1/4，(2) 停損與跳空規則明確化，(3) 加入投組相關性限制——本帳戶已持有 MRVL、ANET、COHR、MOD，全是同一條 AI capex 因子，雲端財報前再疊 AVGO 等於在單一事件上加槓桿。

## Final trade card (條件式, 觸發前不執行)
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $335.81 – $340.00（僅限收盤站回 $335.81 且當日量 ≥ 10 日均量後；若觸發日落在 10/27–28 FOMC 前兩個交易日內，延至決議後） |
| Stop | $318.00（進場下方約 1.5x ATR14，位於 $328.58 結構位之下）；隔夜跳空 > 2x ATR（約 $23）則開盤出清 |
| Target 1 | $356.43（7/2 前低 / MA20） |
| Target 2 | $407.52（7/9 local high） |
| Size | Small（1/4 試單，約 1.25% NAV；FQ4 財報驗證後最多升至 2.5% NAV） |
| Horizon | 戰術 4–8 週；基本面驗證點為 12 月初 FQ4 FY26 財報 |
| Conviction | M |
| R:R to T1 | 1.2（T2 為 4.0；T1 偏低正是只給 1/4 倉的原因） |

## Risk debate adjudication
- Aggressive's strongest point：等「站回 $335.81 + higher low」才進，確實會把部分重新評等的漲幅讓出去；已實現基本面（Q3 YoY +85.5%、FCF margin 44.2%、淨負債/EBITDA 0.68x）並未轉壞。
- Conservative's strongest point：FOMC 與雲端財報集中在兩週內，日內 ATR 停損在事件跳空面前形同虛設；且投組已有多個 AI 半導體曝險，單一宏觀事件會同時打擊多個部位。
- Net：我偏向 **neutral**。Aggressive 的 6.9:1 建立在未經 8-K 核實的 forward EPS 與分析師均價上，並要求半倉接刀，與全隊已達成的驗證流程矛盾；call spread 未評估回檔後偏高的隱含波動率成本。Conservative 的 2 日確認會吃掉訊號價值，機率數字缺乏基礎。Neutral 的 1/4 試單 + $318 停損 + 跳空例外規則，是在不否認基本面的前提下，把事件風險用規模與規則處理掉。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 營收動能 | 季營收連續加速，FY26 AI 半導體 ≥ $58B | Q3 FY26 $29.59B（YoY +85.5%）已實現；$58B 指引僅見次級來源 | 成立（實績）/ 觀察中（指引） |
| Forward EPS $19.39 可兌現 | Forward P/E 17x 支撐重新評等 | 口徑疑為 non-GAAP，與 trailing GAAP 43x 差 2.5 倍，未經 8-K 核實 | 觀察中 |
| 雲端 capex 與融資環境 | 超大規模業者 FY27 capex 持續上修 | Hock Tan 10/12 警示資本取得為主要限制；雲端財報尚未公布 | 觀察中 |
| 技術結構止跌 | 守住 $335.81 並形成 higher low | 10/16 放量跌破 $335.81，均線空頭排列，無 higher low | 已失效 |

第四根支柱已失效，這就是今天不建倉的直接理由；前三根仍有一根以實績成立，所以不做空、不放棄觀察。

## 論點失效條件
必須可證偽，且與 Stop 分開（Stop 是價格紀律，這裡是論點紀律）。
- 若 10 月下旬 MSFT / GOOGL / AMZN / META 任兩家下修 FY27 capex 指引，或指引 YoY 成長低於 20% → 「雲端 capex」支柱失效 → 取消觸發；已進場則出場。
- 若 AVGO 8-K 或 FQ4 財報揭露 FY26 AI 半導體營收指引低於 $58B，或 FY27 AI 指引低於 FY26 的 1.7 倍 → 「AI 營收動能」支柱失效 → 出場。
- 若 FQ4 non-GAAP EPS 指引年化低於 $16（forward $19.39 的 8 成），或公司揭露 GAAP 與 non-GAAP 差距主要來自非經常項目 → 「Forward EPS」支柱失效 → 減碼至零。
- 若 Anthropic $42B 融資條款揭露的利率低於 Broadcom 自身借款成本，或轉換條件使 Broadcom 承擔股權下行 → 減碼。
- 若收盤跌破 $328.58 且量 ≥ 1.2x 10 日均量 → 技術支柱持續失效 → 取消觸發，下一參考位 $289.96。

## Monitoring trigger
若觸發進場前，雲端財報已公布且 capex 指引維持或上修，但 AVGO 仍未站回 $335.81 → 這是「需求面被證實、價格面未跟上」的背離，重新評估是否放寬進場位至 $330–$335.81，但規模不變。

## Catalyst calendar
- 2026-10-27 至 10-28 — FOMC 利率決議（高影響，折現率）
- 2026-10 下旬（日期未確認） — 大型雲端業者財報，AI capex 指引
- 2026-11-18（估計） — NVDA FQ3 FY2027 財報，同業需求指標
- 2026-12-02 至 12-10（未確認） — AVGO FQ4 FY26 財報，驗證 forward EPS 與 AI 指引
- 不定期 — Anthropic IPO 進程 / 融資條款揭露；Section 232 第二階段關稅公告

FINAL TRANSACTION PROPOSAL: **HOLD**

FINAL DECISION COMPLETE
