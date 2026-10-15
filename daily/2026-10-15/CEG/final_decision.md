FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — CEG as of 2026-10-15

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
APPROVE

## Final trade card
CEG 不在 held_tickers.txt，屬新倉判定。核准交易員的「不建倉」提案，**本日不發卡**。不採納激進方的現貨試單或財報前 call spread：財報前隱含波動率偏高、事件後 vol crush 會讓權利金損失與方向對錯脫鉤，且 FOMC 預測市場偏向升息，對淨負債 24.0B 的電力股是逆風而非順風。

下列為觸發成立後的預設參數（非今日指令，僅供觸發後直接套用）：

| Field | Value |
|---|---|
| Direction | LONG（僅於觸發成立後） |
| Entry zone | $287.00 – $292.00（收盤站穩 $287 之上一日即可） |
| Stop | $264.00（1.5×ATR） |
| Target 1 | $305.00 |
| Target 2 | $340.00 |
| Size | Small（0.2× 正常倉位，約 1.5% NAV 風險上限） |
| Horizon | weeks 至 1 季 |
| Conviction | L（觸發後升至 M） |
| R:R to T1 | 0.8（以 $289 入場計；R:R 偏低正是今日不進場的原因，須待 10-Q 把下檔風險砍掉才合理） |

## Risk debate adjudication
- Aggressive's strongest point: 等四重條件全部確認再進場，股價大概率已跳空反應，alpha 被價格吃掉。這點正確，但解法不是提前承擔現貨方向風險，而是把觸發標準簡化為「10-Q 數字 + 收盤收復 $287 一日」，避免連續兩日量能確認錯過跳空。
- Conservative's strongest point: Q2 已出現「調整後 EPS 超預期、GAAP 營業利益 -47M、Normalized Income -224M」的落差模式，若 Q3 重演，頭條 EPS 會誘使提前進場再被 10-Q 打回。觸發必須以 10-Q 為準。另外 2×ATR 停損在 61.3% 年化波動下只擋得住約兩天噪音。
- Net: I weight **neutral** more here because 兩端各有一處過度延伸——激進方把量縮下跌當多頭證據、把分析師共識當「尚未反應」是選擇性引用；保守方用 MA20 當停損距現價僅 2.6%，等於用正常噪音換連續小額止損。中立方的 1.5×ATR 停損、0.2× 起始倉位、10-Q 驗證加單日收復確認，是最可執行的折衷。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 收購資產現金流轉化 | Q3 GAAP 營業利益轉正、季度 FCF 轉正 | 淨負債半年 5.35B→24.0B，TTM FCF 約 309M，股利覆蓋 0.56x，info.freeCashflow 與季度加總口徑矛盾未釐清 | 觀察中 |
| 獲利品質（調整後 vs GAAP） | 落差為一次性併購費用 | Q2 調整後 EPS 2.55 超預期但 Normalized Income -224M，性質未定 | 觀察中 |
| PJM/FERC 容量市場規則 | 2028/29 出清價 $325/MW-day 得以保留，資料中心需求納入預測 | Bowring 建議排除資料中心需求並設價格上限，FERC 共置審查無裁決日期 | 觀察中 |
| 技術結構 | 放量站回 $287 並站穩 MA200 $285.06 | 10-06 突破失敗回測，MACD histogram 收斂、RSI14 51，MA50 < MA200 | 觀察中 |

四根支柱全部「觀察中」、無一「成立」，這就是不建倉的定義。

## 論點失效條件
必須可證偽，且與 Stop 分開。
- 若 Q3 10-Q 顯示季度 FCF 仍為負，或淨負債/EBITDA 高於 3.0x 且較 Q2 上升 → 支柱一失效 → 多頭觸發永久取消，改評估 SHORT。
- 若 Q3 10-Q 的 GAAP 營業利益仍為負，且管理層未在 10-Q 附註中將落差歸類為一次性併購相關項目 → 支柱二失效 → 不進場。
- 若 FERC 或 PJM 正式採納排除資料中心需求預測或設置價格上限 → 支柱三失效 → 即使 10-Q 轉正也不建多倉，長期估值核心假設被重定價。
- 若收盤跌破 MA20 $272.36 後再失守 $256.10 → 支柱四失效 → 轉 SHORT_OR_AVOID 評估。

## Monitoring trigger
- 10-27/28 FOMC 若升息或鷹派指引且 CEG 單日跌逾 1×ATR（$14.20），把觸發後的 Size 再降至 0.1×。
- Q3 財報當日只看 10-Q，不看新聞稿；10-Q 未出前任何「指引上修至 $11.50–12.50」的報導一律視為未驗證。
- 若帳上另有 VST/NRG/TLN 等同主題曝險，觸發建倉前先確認集中度；目前 held_tickers.txt 無此類標的，暫不需板塊避險。

## Catalyst calendar
- 2026-10-27/28 — FOMC 利率決議（預測市場偏向升息，逆風）
- 約 2026-11-05 至 11-09 — CEG Q3 財報與 10-Q（驗證 GAAP 營業利益、季度 FCF、淨負債/EBITDA）
- 待定 — FERC/PJM 對 2028/29 容量拍賣規則（資料中心需求、價格上限、共置交易審查）裁決

FINAL DECISION COMPLETE
