FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — MP as of 2026-08-28

> **持倉標的**：MP 已列於 `pipeline/tools/held_tickers.txt`（5/29 materials picks），本決策採持倉框架，問題是「該不該續抱／加碼」，非「該不該進場」。
> **無即時價格，暫不給進出場價位**（market.md 與 fundamentals.md 均為 PRICE_DATA_UNAVAILABLE，yfinance HTTP 403）。分析師目標 $75.38 與新聞參考價 $58 皆非即時報價，不得作為價位依據。

## Verdict
加碼

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE（非價格 stop：NdPr 現貨連續兩週 <$70/kg，或 CEO 恢復淨賣出 >$10M 且 COO 無對應買進） |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | Medium — 初始 1.0% NAV，確認後加至 1.5% NAV |
| Horizon | 3–6 個月（至 Q4 2026 GM 磁鐵首批出貨） |
| Conviction | M-H（70%） |
| R:R to T1 | PRICE_DATA_UNAVAILABLE |

**加碼執行條件（兩項皆須成立）**：① 即時價格數據恢復；② NdPr 現貨 ≥$70/kg 持續穩定。GM 出貨確認**降格為監控條件**，非阻擋閘門。加至 1.5% NAV 的觸發：Q4 GM 出貨確認，**或** Q3 2026 財報超預期。

## Risk debate adjudication
- Aggressive's strongest point：要求 GM 出貨確認才動作，等同把此交易變成 post-catalyst 交易；公告落地時 30% 重評早已折現，等待本身就是付出 alpha。
- Conservative's strongest point：Molycorp 前例（NdPr 由 ~$300 崩至 ~$40/kg 致破產）證明稀土週期破壞力超出市場預期，且在無 ATR／無年化波動率下無法做 vol-adjusted 定錨，倉位不該給滿。
- Net：我採 **neutral** 綜合。進取方的 R:R 2.2×–3.6× 建立在非即時報價上，數字本身即為估算，不足以支撐即時滿倉；保守方 0.75% 則以情緒性因素懲罰已驗證的硬數據（Q2 營收 $108.5M、+89% YoY、NdPr 銷量 +122%、現金 $1.45B）。1.0% 起步、確認後加至 1.5%，把倉位增量綁在資訊增量上，是唯一與數據狀態相稱的做法。CEO 賣出門檻維持 $10M 而非 $5M——COO 於 $54–$57 自有資金建倉構成部分抵銷，$5M 易生假陽性。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| NdPr 價格受中國出口管制支撐 | 維持高 $90s/kg | 雙波管制（2026-06-22 黑名單、2026-11-10 第二波）結構未鬆動 | 成立 |
| 產銷量爆發性成長 | 營收與銷量雙位數以上成長 | Q2 營收 $108.5M（+89% YoY）、NdPr 銷量 +122%、超共識 13% | 成立 |
| 政策護城河與剛性需求 | 2027-01-01 防務採購禁令排除中俄伊朝稀土 | 立法時程未變，MP 為美國唯一規模化礦採分離一體化供應商 | 成立 |
| GM 磁鐵量產（礦→磁鐵重評） | Q4 2026 首批商業出貨 | Fort Worth 爬坡中，零商業量產記錄，保守方估 25% 延誤機率 | 觀察中 |
| 內部人士信心 | 管理層與股東利益一致 | CEO 淨賣出 $53.2M（零買進）、機構季度淨減 324 萬股，COO 僅買 ~$1.5M 抵銷 | 已鬆動（觀察中） |

三根核心支柱（NdPr 價格、產銷成長、政策護城河）全數成立；鬆動的是內部人士信號與尚未驗證的磁鐵支柱——兩者皆屬「估值重評的上行選擇權」，而非現有現金流的基礎。故續抱並小幅加碼成立，但倉位上限被壓在 1.5% NAV。

## 論點失效條件
- 若 NdPr 現貨**連續兩個交易週**收在 $70/kg 以下 → 支柱一失效 → **出場**。
- 若公司正式公告 GM 磁鐵首批商業出貨**延至 2027 Q1 以後**且無明確新時間表 → 磁鐵支柱失效 → **減碼至 0.5% NAV**。
- 若 CEO Litinsky 新增 Form 4 淨賣出**累計 >$10M** 且 COO 六週內無對應買進 → 內部人士支柱失效 → **減碼一半**。
- 若 Q3 與 Q4 2026 **連續兩季** NdPr 生產量低於 1,000 公噸，或實現價格跌至 $80/kg 以下 → 支柱二失效 → **減碼**。
- 若中美貿易協議明確放寬中國稀土出口管制覆蓋範圍，或 Mountain Pass 環境事故觸發監管停產 → **立即出場**。

## Monitoring trigger
價格數據恢復後 48 小時內重建技術止損與 R:R；在此之前部位維持現狀不加碼。任何 NdPr 現貨單週跌破 $75/kg 即進入每日追蹤，不等兩週確認才開始評估。

## Catalyst calendar
- 2026-09（預計）— Q3 2026 財報：驗證 NdPr 產量 >1,000 公噸、實現價格是否守住高 $90s/kg
- 2026-09 起（持續）— Fort Worth Independence 廠月度產能與良率公告
- 2026-10–11 — Q4 GM 磁鐵首批商業出貨公告（最高權重）
- 2026-11-10 — 中國稀土出口管制第二波生效（五種新增元素）
- 2027-01-01 — 美國防務採購禁令截止日

FINAL DECISION COMPLETE
