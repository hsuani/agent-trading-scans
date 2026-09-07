FINAL TRANSACTION PROPOSAL: **HOLD**

# QUBT — 最終決策 2026-09-08

## 決策結果

**HOLD（不建倉 / 觀望）** — QUBT 不在 `held_tickers.txt` 內，屬新倉判定，Verdict 為 **REJECT**（本次不進場）。第一行以 HOLD 輸出，代表「不採取買賣動作」，非既有部位之續抱。

Dealbreaker 有二：其一，`market.md` 為 PRICE_DATA_UNAVAILABLE，無現價、無 ATR14、無支撐位，因此停損距離、部位美元風險與 R:R 全數無法計算——在無法量化最壞損失的前提下建倉，是承擔未定義的尾部風險，而非風控下的持倉。其二，`trade_proposal.md` 自訂的進場觸發（Q3 毛利轉正 / 積壓訂單轉化率 >50% / H.R. 10163 全院通過並明列 QUBT）**一項都尚未成立**。提案自己說「等」，卻同時輸出 BUY，這是內部矛盾，由我在此裁定為不執行。

## 信心度

**35% conviction**（對「本次不進場」這個決策本身的信心為高；對多頭論述的信心僅 35%）

## 進出場價位

| 欄位 | 數值 |
|---|---|
| Direction | 不建倉（若未來啟動則為 LONG） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | 0% NAV（未來啟動上限 0.5%） |
| Horizon | 重評節點 2026-10 Q3 財報 |
| R:R | PRICE_DATA_UNAVAILABLE |

## 理由摘要

**風險辯論裁決。** Aggressive 最強的一點：H.R. 10163 已於 2026-09-05 過委員會，是時間敏感催化劑，等財報確實會付出 alpha 成本。Conservative 最強的一點：算不出 (entry − stop) × shares，就沒有部位規模這回事，0.5% NAV 只是一個沒有錨的數字。**我採納 Conservative。** 理由是 Aggressive 的 B/A ≥4:1 建立在未知入場價與分析師目標價之上，屬循環論證；而政策催化劑的不對稱性不足以補償「連 1R 都無法定義」的結構缺陷。Neutral 的 0.5–0.75% 折衷同樣繼承了這個缺陷。

**證據品質問題（本次決策的隱藏關鍵）。** `fundamentals.md` 通篇為「基於典型早期量子計算公司特徵」的推估模板，其年度營收 $1–3M 與新聞面已入帳的單季 $5.6M 直接衝突，且列出 Gross Margin 為 n/a——這份基本面報告未提供任何可用的公司實際數據。加上 `sentiment.md` 所載「現金部位 $13 億」與燒錢率、市值規模明顯不相稱。**價格面與基本面兩條腿同時失效**，僅靠新聞與情緒建倉不可接受。

多頭論述並非無效：Q2 營收 $5.6M、$42.5M 積壓訂單、NASA / NIST 認可皆為可查事實。但負毛利意味規模化即加速燒錢，CFO 以市價出脫約 $614K、機構空倉 29.9%、缺席商務部 $2B 名單三者，證據品質高於多頭的情境推估。

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 商業化拐點 | 營收自零起飛 | Q2 $5.6M vs 去年 $61K | 成立 |
| 訂單能見度 | 積壓訂單支撐至 2027Q3 | $42.5M，轉化率未驗證 | 觀察中 |
| 單位經濟 | 毛利轉正可期 | Gross Margin 仍為負 | 已失效 |
| 政策受益者 | 聯邦資金 / 法案受惠 | 缺席商務部 $2B 名單 | 觀察中 |
| 內部人信心 | 管理層與股東同向 | CFO / COO 市價減持 | 已失效 |

## 風險因素（論點失效條件，與 Stop 分離）

- 若 Q3 2026 財報 Gross Margin 仍為負且未見收斂 → 單位經濟支柱確認失效，無限期排除。
- 若積壓訂單餘額較 $42.5M 縮水 >20% → 能見度支柱失效。
- 若 Form 4 出現 CFO 或 CEO 第二筆大額市價賣出 → 內部人支柱確認失效。
- 若公司宣布新一輪股權融資（down round 或 >10% 稀釋）→ 直接排除。
- 若 H.R. 10163 本會期未過眾議院全院，或通過但未明列 QUBT → 政策支柱失效。

## Monitoring trigger

市場數據恢復後，重取現價 / ATR14 / 支撐位；**同時**滿足「毛利轉正或明顯收斂」與「R:R ≥ 1.5」兩項，方可以 ≤0.5% NAV、停損 ≤1.5× ATR14 分批建倉。任一未達成即維持零部位。

## Catalyst calendar

- 2026-09 至 10 — H.R. 10163 眾議院全院投票
- 2026-10 — Q3 2026 財報（Gross Margin、積壓訂單、NASA 合約）
- 持續 — SEC Form 4；NHanced TFLN 垂直整合進度

FINAL DECISION COMPLETE
