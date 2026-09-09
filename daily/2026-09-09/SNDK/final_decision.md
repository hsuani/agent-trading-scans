FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — SNDK as of 2026-09-09

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## 部位狀態
SNDK 不在 `held_tickers.txt` 內 → 依新倉框架裁決。REJECT 的意思是**本日不建倉**,
不是賣出(本來就沒有部位)。第一行輸出 HOLD 代表 dashboard 應維持零曝險、繼續觀察。

| Field | Value |
|---|---|
| Direction | 無(不建倉) |
| Conviction | L(多方論點信心約 25%) |
| NAV allocation | 0%(條件解除後上限 0.25–0.5% NAV,僅限 defined-risk call spread) |
| Horizon | 觀察期 1–3 個月(Q4 2026 – Q1 2027 驗證窗口) |
| Dashboard score | 3 / 10 |

## Dealbreaker
**財務數據內部矛盾未解除。** 全年 EPS 估計 $12.01 與 Q3 單季指引 $12–14 相差一個數量級,
「單季淨利 $6.90B > 同期營收 $3.03B」在會計上不可能成立。估值錨(共識目標 $2,125、隱含
P/E 約 41x)完全建立在這組數字上;地基未確認前,任何倉位大小的討論都是在對未驗證的輸入
下注。這不是「保守」的問題,是輸入品質的問題 —— 我不會為了避免錯過而在無法核對的分母上
建倉。疊加 YTD +647%、機構持股 94.4%→87.8%、6 個月淨內部人賣出 $840 萬且無高管買進,
不對稱明顯偏空(上行至 $2,125 vs 空方情境 $270,-87%)。

另加一條執行面理由:PRICE_DATA_UNAVAILABLE。沒有現價就無法定行使價、無法算 R:R、
無法定倉位。Aggressive 自己也承認「不給具體行使價」—— 一筆連參數都填不出來的交易,
不該被批准。

## Risk debate adjudication
- Aggressive's strongest point:等待三重條件(EPS 澄清 + TrendForce 高位 + RSI < 50)同時
  成立的機率極低,實務上等於永久觀望;且 S&P 100 被動買盤是與主動機構減持獨立的機械性支撐。
- Conservative's strongest point:EPS 矛盾是**已知且未解除**的硬性風險,不能用「等財報澄清」
  來合理化現在就承擔曝險;機構出貨通常領先頂部 1–2 季。
- Net: 我採 **neutral 的門檻設計、conservative 的當下結論**。Neutral 正確指出保守方三重
  條件過嚴,我因此把重啟門檻降為兩項可查證條件(見下);但 neutral 自己也承認 EPS 矛盾未
  澄清前不宜建倉 —— 所以今天的答案仍是零倉。Aggressive 的 call spread 結構本身合理,
  問題是現在連行使價都定不出來,不是結構問題而是時點問題。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| NAND 合約價上行週期 | Q2 環比 +70–75%,延續至 2027 | TrendForce 第三方數據支撐,尚未見拐點 | 成立 |
| 技術護城河(BiCS8 / 256TB UltraQLC) | 量產出貨、Kioxia 聯盟產能 | 已量產,對手短期難複製 | 成立 |
| 財務數據可支撐估值框架 | EPS 可作 P/E 錨 | 全年 vs 單季量級矛盾,營收 < 淨利 | 已失效 |
| 風險報酬對稱 | R:R ≥ 1.5 | 上行 vs -87% 下行,定性偏空 | 已失效 |

兩根產業支柱成立,但**兩根與「能不能買」直接相關的支柱已失效** —— 好生意不等於好交易。

## 論點失效條件(論點紀律,與 Stop 分開)
本案無倉位,故列的是「重啟評估」與「永久刪除」門檻:
- 若 Q3 2026 財報公布後全年 EPS 指引仍與單季速率矛盾,或 EPS 低於指引下緣 $12 →
  數據支柱確認失效 → 本標的移出候選池至少兩季。
- 若 TrendForce 月報出現首次 NAND 合約價環比下行 → 週期支柱失效 → 永不追多。
- 若 Samsung / SK Hynix / Micron 任一宣布新晶圓廠量產時程提前 → 供給支柱失效 → 出局。
- 若大型雲端客戶公開削減企業 SSD 採購 → 需求支柱失效 → 出局。

## 重啟建倉的閘門(全部成立才准提案,不再降標)
1. Q3 財報 EPS 數據內部一致,且年化運行速率可核對;**且**
2. TrendForce 當月報告確認 NAND 合約價未轉跌;**且**
3. 取得可用即時價格資料,能定出行使價與 R:R ≥ 1.5。

三項齊備後,授權額度上限 **0.25–0.5% NAV,僅限 Q4/Q1 到期的 OTM call spread**,
禁止直接持有正股(無下行保護),不在財報前夜追入(規避 IV crush)。

## Stop(定性)
無倉位,無價格 Stop。未來建倉後採 defined-risk 結構,最大損失即權利金 = 授權 NAV 額度,
並以上述論點失效條件為功能性停損:任一觸發,於下一個流動性視窗(開盤後 30 分鐘內)
清倉,不得「等等看」。

## Monitoring trigger
若 TrendForce 月報顯示 NAND 合約價漲幅收斂至個位數環比,即使尚未轉跌,亦視為週期見頂
前兆,重新評估並下調本標的優先序。

## Catalyst calendar
- 每月月初 — TrendForce NAND 合約價格月報(首要領先指標)
- 2026-10(預估) — SNDK Q3 2026 財報:EPS 指引澄清(決定性事件)
- 2026 Q4 — Samsung / Kioxia / Micron 新晶圓廠量產進度更新
- 2026 Q4 / 2027 Q1 — 13F:Vanguard / BlackRock 持股變動

FINAL DECISION COMPLETE
