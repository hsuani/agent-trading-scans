FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — 2308.TW as of 2026-09-01

## FINAL VERDICT: **HOLD**（不新建倉，條件式 BUY 授權已核可）

## Verdict
MODIFY

## 持倉狀態
2308.TW 不在 `held_tickers.txt` → 新倉框架。今日問題是「該不該進」，答案是「方向對，但今天不進」。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認 |
| Stop | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認（功能性上限 -12%） |
| Target 1 | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認（分析師共識 2,565 TWD，非即時報價） |
| Target 2 | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認（原始目標 2,650 TWD，非即時報價） |
| Size | Small — 起始 0.75% NAV，觸發後上限 1.25% NAV |
| Horizon | 3m+（2–3 季，Q3 法說會後重新評估） |
| Conviction | M — 62% |
| R:R to T1 | 無法計算；驗算後 < 1.5 則不執行 |

## Key rationale
- **AI 電源動能是已公布硬數據，不是敘事**：H1 EPS 17.59 TWD 破全年紀錄、7 月單月營收 NT$67.07B（YoY +47.7%）、AI 電源部門營業利益 YoY +121%。多頭論述的地基是可查證的。
- **但今天執行等於違反自訂紀律**：提案自設「R:R < 1.5 不進場」，而 Entry 與 Stop 皆為 PRICE_DATA_UNAVAILABLE。在無法錨定風險單位時建倉，是以未定義風險換未定義報酬。保守方此點無法反駁。
- **45× P/E 對比歷史 20–30× 沒有容錯空間**：毛利率與 FCF 皆為 DATA_UNAVAILABLE，NT$70B capex 壓縮短期 FCF。故縮小起始倉、保留 9 月 15 日後的加碼彈藥，而非現在押滿。

## Top risk
超大型雲端廠商 capex 延後或削減（機率約 15%）。AI 營收 40% 集中於少數客戶、幾無緩衝，2022 年伺服器庫存去化時本股自高點腰斬有前例。此風險與美國基礎設施關稅（變壓器/開關設備估計稅率達 100%）疊加時，估值收縮與獲利下修會同時發生。

## Entry trigger
1. Yahoo Finance 報價恢復，驗算 R:R ≥ 1.5；且
2. 2026-09-10～09-15 公布之 8 月單月營收 YoY ≥ 45% 且無管理層指引下調。
兩者同時滿足 → 首批 0.75% NAV。Q3 法說會確認「H2 > H1」且毛利率未環比下滑 > 2ppt → 加碼 0.5% NAV 至上限 1.25%。任一條件不成立則維持零倉。

## Stop condition
價格紀律：報價恢復後以技術支撐設量化停損，功能性上限 -12%（滑價後不得超過 -15%）。單筆最大損失控制在 0.15% NAV。

## Risk debate adjudication
- Aggressive's strongest point：-6% 甚至 -10% 停損對一檔曾 5 日 -18.62% 的股票，是在噪訊中被洗出場，不是在論述失效時停損。此點成立，故功能性停損放寬至 -12%。
- Conservative's strongest point：R:R 未驗算前任何規模都是盲目承諾。此點決定了今日不執行。
- Net：I weight **neutral** more here — 積極方「倉位放大同時停損放寬」是雙向擴大暴露，不是鎖定風險；保守方零倉 + -6% 停損則等同否定論述本身。中性方的 0.75%/1.25% 分批 + -12% 停損，是唯一同時尊重資訊缺口與基本面事實的解。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 電源需求動能 | 月營收 YoY ≥ 45% | 7 月 +47.7%、部門營業利益 +121% | 成立 |
| 生態系護城河 | NVIDIA 800VDC 驗證、12–18 月認證週期、訂單能見度至 2027 Q1 | 未見鬆動 | 成立 |
| 毛利率守穩 | 高毛利 AI 組合抵消電費/交期/匯率壓力 | fundamentals DATA_UNAVAILABLE | 觀察中 |
| 估值可承受性 | FCF 支撐 45× P/E | NT$70B capex 壓縮 FCF，FactSet 目標已由 2,650 下調至 2,565 | 觀察中 |

## 論點失效條件
- 若 8 月或 9 月單月營收 YoY < 40%，需求動能支柱失效 → 不進場 / 已進場則出場。
- 若 Q3 毛利率環比下滑 > 2 個百分點，毛利支柱失效 → 減碼至零。
- 若任一超大型雲端廠商公開宣布 capex 延後或削減，客戶集中支柱失效 → 出場。
- 若首家大型券商將評級由 BUY 降為 HOLD，估值支柱轉為失效觀察 → 暫停加碼並減碼一半。

## Monitoring trigger
若 9 月 15 日前報價未恢復，或恢復後驗算 R:R < 1.5，本案自動延後至 Q3 法說會後重評，不得以「怕錯過」為由提前建倉。

## Catalyst calendar
- 2026-09-10 ～ 09-15 — 8 月單月營收（核心觸發點）
- 2026-10 中旬 — 9 月單月營收
- 2026-11 初（預估） — Q3 2026 法說會（H2 首季 EPS 與毛利率驗證）
- 2026 Q4 ～ 2027 Q1 — 美國廠投產與超大型廠商新建置訂單落地

FINAL DECISION COMPLETE
