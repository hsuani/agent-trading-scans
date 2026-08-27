FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — PANW as of 2026-08-28

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

（框架判定：PANW 不在 `pipeline/tools/held_tickers.txt` 內 → 新倉決策。REJECT 指「不建立新倉」，非賣出訊號；帳上無部位，故第一行對應 HOLD／站在場外。）

## Final trade card
不適用（REJECT，不建倉）。為下游一致性保留關鍵欄位：

| Field | Value |
|---|---|
| Direction | 無（FLAT） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | None（0% NAV）；業績後若條件達標，授權上限 Small–Medium 1.0% NAV |
| Horizon | 觀望 4 天至 2026-09-01 業績，之後重評 |
| Conviction | L（對「不建倉」這個決定本身：conviction 70%；對做多論述：35%） |
| R:R to T1 | 無法計算（價格資料缺失） |

## Dealbreaker（REJECT 理由）
兩件事同時成立才是關鍵：(1) 四天後是高度二元化的 Q4 FY2026 業績；(2) 股價 ~$398 已高於全部 55 位分析師目標（均值 $333.50），93x Forward P/E 沒有估值緩衝。上行被共識目標壓制、下行開放至 $333–$350 甚至 $280–$300，這是最不對稱的進場時點。

另有一項執行層面的硬性否決：Entry/Stop/Target 全為 PRICE_DATA_UNAVAILABLE。沒有即時報價，我無法核定履約價、部位股數或 Stop 距離。Aggressive 主張的 $400/$445 Call Spread 建立在一個來自研究報告的陳舊價格錨上——用過期價格挑選履約價，會把「已定義風險」變成「已定義的錯誤風險」。故此結構亦不予授權。

## Risk debate adjudication
- Aggressive's strongest point：Call Spread 與股票多頭在風險哲學上確實不同，最大損失可事前鎖定，不應被「業績前零部位」一併否決。這點邏輯正確。
- Conservative's strongest point：業績後追高反而讓 R:R 更差——股價跳漲至 $420–$450 時共識目標仍在 $330–$334，用更高價格建更大部位，與等待不對稱機會的初衷矛盾。同時無 ATR、無 Hard Stop 的倉位建議不構成風控紀律。
- Net：我採納 conservative 較多。Aggressive 的邏輯成立但無法執行——缺乏即時報價使履約價選擇失去基礎，理論上的 6:1 在實務上不可驗證。Neutral 的 0.25% NAV 折衷同樣受制於此。Size 上限採 conservative 的 1.0%，不採 aggressive 的 2.5–3%。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| NGS ARR 平台化動能 | ARR YoY >50% | Q3 FY2026 為 +59–60%，RPO +32–33% | 成立 |
| Prisma AIRS 商業化 | $100M ARR 路線圖 | 300 家客戶，ARR 絕對值未公布 | 觀察中 |
| 估值安全邊際 | 股價低於共識目標 | $398 高於全體分析師目標上限 | 已失效 |
| 管理層內部信心 | 內部人淨買入 | 90 天 47 筆全為賣出、淨賣出 $43M+，CFO 全年零買入 | 已失效 |

四根中兩根已失效，這是 REJECT 而非 MODIFY 的直接依據。

## 論點失效條件
- 若 Q4 營收 < $3.35B 或 FY2027 指引成長率 < 28%，平台化動能支柱失效 → 業績後不建倉，改列觀察名單。
- 若 Prisma AIRS ARR 公布值 < $50M，AI 安全商業化支柱失效 → 取消所有建倉授權，本論述作廢。
- 若 GWAC 合約（2026-09-30）未續約，政府業務支柱失效 → 不建倉。
- 若 CFO Golechha 業績後仍淨賣出，管理層信心支柱維持失效 → 一票否決，無論業績多亮眼。

## Re-visit 條件（何時可重新考慮）
須同時滿足：Q4 營收 > $3.45B、FY2027 指引 ≥ 30%、Prisma AIRS ARR ≥ $80M，且取得即時報價後方可核定倉位。達標則以 1.0% NAV 建倉、Hard Stop $333；業績日不追跳空，等首個交易時段價格穩定後介入。升至 1.5% 保留至 FY2027 Q1 驗證 ARR 環比加速後。

## Monitoring trigger
若業績後股價跌破 $333 且無量能承接，改列 $280–$300 價值區觀察，暫不介入。

## Catalyst calendar
- 2026-09-01 — Q4 FY2026 業績（Prisma AIRS ARR、Q4 營收、FY2027 指引）
- 2026-09-30 — GWAC 政府合約到期／續約
- 2026-10~11 — FY2027 Q1 業績

FINAL DECISION COMPLETE
