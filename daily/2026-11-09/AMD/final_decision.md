FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — AMD as of 2026-11-09

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> 持倉判定：AMD 不在 `pipeline/tools/held_tickers.txt`，屬新倉，問題是「該不該進」。
> 資料註記：價格為 2026-11-06 收盤 $449.04，未含 11-09 行情。

交易員提案為全面 AVOID。我不接受「R:R 無法估算所以不進場」這個結論——風險辯論三方已經收斂出可量化的停損（$402.10 恐慌低點下方）與目標（MA20 / 分析師低限），R:R 是可以算的，算出來約 2.3–2.8x。真正的不確定性（存貨、FCF、forward EPS）要到 2027-02 才能驗證，這是**用倉位大小處理**的問題，不是零倉位的理由。因此改為小倉分批建立，而非空手。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $415 – $455（分兩批：第一批 $440–455 現價區；第二批 $415–422 MA200 回測。若 11-09 開盤已高於 $475，第一批不追價，僅保留第二批） |
| Stop | $395（收盤基準；$402.10 低點下方留緩衝，缺口風險以倉位大小吸收） |
| Target 1 | $527.30（MA20 reclaim） |
| Target 2 | $540（分析師最低目標） |
| Size | Small（約 5% NAV 名目，停損觸發約 -0.5% NAV；若缺口至 $370 約 -0.75% NAV） |
| Horizon | 戰術 1–3 週（跨 NVDA 11-17）；若達 T1 且支柱未鬆動，延長至 2027-02 Q4 財報 |
| Conviction | L |
| R:R to T1 | 2.3（以混合均價 $435 計；若僅第一批成交約 1.5） |

## Risk debate adjudication
- Aggressive's strongest point：11-05 的 -17.3% 由產業與宏觀恐慌驅動（NVDA、INTC、記憶體股同跌），公司端 Q3 數據與 Q4 guidance 反而超預期，MA200 未破。等站回 $488–514 才進場，等於放棄從 $402 起算 21% 的那段。
- Conservative's strongest point：ATR 8.2%、年化波動 102%、Beta 2.54，貼著區間下緣設 5% 停損必被雜訊掃掉；且 11-05 式缺口可能直接穿過停損單，實際虧損會是帳面估算的數倍。
- Net：我偏向 **neutral**。採納 aggressive 的「現在就該有部位」，但拒絕其「標準倉位」——存貨 +45%、FCF/NI 0.23、內部人零買入都是公司層級訊號，不能全歸為宏觀。採納 conservative 的 ATR 停損與缺口意識，但拒絕「兩日確認 + 1/4 倉」——在 NVDA 財報前把進場推遲到趨勢大半確認，等於用尾部情境當基準。Call spread 不採用：IV 偏高且本倉位已是小量，不需疊加槓桿。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 資料中心動能 | Data Center YoY >50%，Q4 guide 高於共識 | Q3 DC 8.55B（+97%），Q4 guide 17B vs 共識 16.2B | 成立 |
| 11-05 重挫屬產業/宏觀面，非公司利空 | MA200 $415.98 守住，板塊同步修復 | 11-06 +11% 反彈，MA200 未破，但 MACD hist 仍負、低於 MA20/MA50 | 觀察中 |
| 存貨與舉債為 Q4 備貨，非需求放緩 | Q4 營收達標且存貨 QoQ 回落、FCF/NI 回升 | 存貨 11.46B（DIO ~199 天）、FCF/NI 0.23、4.73B 發債用途未揭露 | 觀察中 |
| forward EPS 17.64 可兌現，估值有支撐 | 2027 資料中心 capex 不下修 | 尚無客戶下修；州層級 moratorium 僅為選後討論 | 觀察中 |

## 論點失效條件
與 Stop $395 分開；以下任一成立，不等價格打到停損即動作。
- 若 NVDA 11-17 財報的次季營收指引低於市場共識，或其 Data Center 營收 QoQ 成長 <5% → 支柱 2 失效 → 出場。
- 若收盤連續 2 日低於 $402.10 且低於 MA200 → 支柱 2 失效 → 出場（即使尚未觸及 $395）。
- 若 2027-02 Q4 財報：營收 <16.2B、或存貨 QoQ 未下降、或 FCF/NI <0.6 → 支柱 3 失效 → 出場。
- 若任一主要超大規模客戶（MSFT/AMZN/GOOG/META/ORCL）公開下修 2027 capex 指引，或任一州資料中心 moratorium 完成立法 → 支柱 4 失效 → 減碼一半。
- 若 10-Q 揭露 4.73B 發債用途為一般營運周轉而非產能/備貨相關 → 支柱 3 鬆動 → 不加碼第二批。

## Monitoring trigger
- 若在 NVDA 11-17 財報前，價格帶量收復 $488.78 且 MACD histogram 翻正 → 可將第二批改在 $480–490 執行，停損上移至 $440。
- 若 11-09 至 11-17 間單日跌幅 >2× ATR（約 -16%）→ 不等停損，當日重新評估支柱 2。
- 10 月 CPI（11 月中）高於預期 0.2pp 以上 → 第二批暫緩。

## Catalyst calendar
- 2026-11-17 — NVDA 財報（板塊外部驗證點）
- 2026-11 中旬（日期未驗證）— 美國 10 月 CPI
- 2026-11 — AMD Q3 10-Q（發債用途、Other Non-Current Assets 明細）
- 2027-02-02（估計）— AMD Q4 財報（營收 17B 兌現度、存貨去化、FCF/NI）

FINAL DECISION COMPLETE
