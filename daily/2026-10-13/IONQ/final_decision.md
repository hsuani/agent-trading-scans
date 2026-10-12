FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — IONQ as of 2026-10-13

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
APPROVE

## 步驟 0 — 倉位判定
IONQ 不在 `pipeline/tools/held_tickers.txt`，屬新倉，走 A 框架。問題是「該不該進」，答案是：不進。核准交易員的 AVOID / Sizing = 0 提案，並否決 Aggressive 與 Neutral 提出的小型 call spread 試單。

## Final trade card
| Field | Value |
|---|---|
| Direction | 無（不建倉） |
| Entry zone | 無 — 觀察位：收復 $41.30–$41.50 可重評多方；收盤跌破 $35.00 可重評空方 |
| Stop | 無 |
| Target 1 | 無 |
| Target 2 | 無 |
| Size | 0% NAV |
| Horizon | 觀察至 2026-11-04 Q3 財報後重新評估 |
| Conviction | L（對「迴避」的信心為 M，對任一方向的信心為 L） |
| R:R to T1 | 無 |

## Risk debate adjudication
- Aggressive's strongest point：RSI 34、BB %B 0.01、量縮下殺、空單比例 10%、beta 3.36，確實是軋空反彈的常見組合，等 $41.5 確認再進場會錯過大半反彈。
- Conservative's strongest point：FOMC 與財報都可能跳空，收盤價觸發的風控在跳空情境下失效；加上本股 ATR 約 7.4%，Aggressive 的 $34.50 停損（距離 4.1%）等於用雜訊決定輸贏。
- Net：我偏向 conservative，並採納 neutral 對雙方的修正。否決 call spread 的理由：研究結論是 SHORT_OR_AVOID，三根空方支柱（毛利、稀釋、商譽）都還成立，call spread 是逆研究方向、逆趨勢賭一個「空單必回補」的技術假設；權利金雖小，但這是方向性下注，不是風控結構。超賣本身不是進場理由，要等價格證明趨勢反轉。Conservative 建議疊加 QQQ/ARKQ 對沖則不採納——沒有部位就沒有需要對沖的風險。

## 論點支柱（支撐「迴避」的支柱）
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營收品質未驗證 | 下半年約 $310M 增量多來自 SkyWater，量子本業成長無法拆分 | 需 11-04 Q3 分部數據 | 觀察中 |
| 毛利率結構惡化 | 季度毛利率 59.9% → 24.9%，連五季下滑，原因不明 | Q3 併入低毛利代工後可能再降 | 成立 |
| 稀釋與商譽風險 | 股數 381.0M → 約 405.1M；商譽加無形資產佔權益 89% | SkyWater 現金對價尚未反映在 06-30 現金 $2,119M | 成立 |
| 技術面下行趨勢 | 價格在三條均線下、death cross、lower highs、MACD 柱體負值擴大 | $35.98 收盤守住 $35.00，但趨勢未反轉 | 成立 |

## 論點失效條件
與 Stop 分開；這裡是論點紀律，任一條成立即在財報前後重新評估，不等價格。
- 若 Q3 財報揭露量子本業（扣除 SkyWater）營收 YoY 仍高於 50%，且本業毛利率止跌回升至 30% 以上，並重申或上修 FY2026 $450–460M 指引 → 「營收品質」與「毛利率」兩根支柱失效 → 轉為可評估低信心 LONG。
- 若股價收盤收復 $41.50（MA20/MA50）且 MACD 上穿 signal → 「技術面下行」支柱失效 → 重評多方，不必等財報。
- 若財報前公司宣布新一輪股權募資、提前揭露商譽減損，或 Q3 毛利率跌破 20% → 迴避立場的方向性假設（「不值得放空」）失效 → 轉為可評估有限風險空方結構（put spread，不裸空）。
- 若收盤跌破 $35.00 → 下一支撐 $31.81，以 $35.00 上方為停損重新試算空方 R:R。

## Monitoring trigger
財報前任何一日收盤站上 $41.50 或跌破 $35.00，皆在次一交易日前重新跑一次評估；11-04 財報後，無論結果如何都重做完整分析，重點看分部營收、本業毛利率、併購後現金餘額與流通股數。

## Catalyst calendar
- 2026-10-27/28 — FOMC 利率決議（高 beta 成長股估值敏感）
- 2026-11-04 — IONQ Q3 財報與 10-Q（主要驗證點）

FINAL DECISION COMPLETE
