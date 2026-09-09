FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 8996.TW (高力熱處理) as of 2026-09-09

| 項目 | 內容 |
|---|---|
| Ticker | 8996.TW (TWSE) |
| Date | 2026-09-09 |
| 部位狀態 | 新倉（不在 held_tickers.txt） |
| Verdict | BUY_MODIFY（條件式進場） |
| Conviction | MEDIUM，約 60% |
| NAV 上限 | 1.5%（Phase 3 全額），初倉 0.4% |

> **PRICE_DATA_UNAVAILABLE — actual execution requires live-quote verification before entry.**
> yfinance 遭組織代理封鎖，無即時報價。情緒報告引述之 NT$1,240–1,300「現價」與 5 位分析師在
> NT$377.5 目標價下給出 BUY 相互矛盾，判定為錯誤資料，予以剔除。以下所有價位均以
> **分析師共識目標價 NT$377.5 為錨的百分比**表示，取得即時報價前不得下單。

## Verdict
MODIFY

## Summary of thesis
高力是台灣液冷散熱供應鏈中少數同時具備訂單能見度至 2028 年、三年三倍產能擴張與三位數營收成長的標的。8 月單月營收 NT$12.04 億（YoY +112.84%、MoM +30.48%），1–8 月累計 YoY +115.03%，環比仍在加速，顯示需求擴張而非高基期假象。液冷滲透率由 2025 年 33% 躍升至 2026 年 53%，是 NVIDIA Blackwell 單櫃逾 100kW 的物理剛性驅動，非題材炒作。真實風險是 EPS 動能收斂（Q1 +454% → Q2 +61%）、NT$30 億擴產的 FCF 壓力、以及 FOMC/CBC 雙率決議的估值壓縮，這些屬中期波動而非結構性反轉。因此方向做多、信念 MEDIUM、以事件後分階段建倉取代一次性進場。

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 現價須 < NT$377.5；目標買區 NT$320 – NT$360（NT$377.5 之 -15% ~ -5%） |
| Stop | 進場價 -10%（若於 NT$340 進場約 NT$306） |
| Target 1 | NT$377.5（分析師共識中樞） |
| Target 2 | NT$490（NT$377.5 +30%） |
| Size | Small → Medium（Phase 1 0.4% NAV，最終上限 1.5% NAV） |
| Horizon | 事件窗口 1–4 週；核心論點 1–3 季 |
| Conviction | M |
| R:R to T1 | 1.25（+12.5% / -10%）；至 T2 約 3.0；以 Phase 1 風險 0.04% NAV 對 T2 上行 +0.27% NAV 計約 6.75x |

## Entry conditions（全部成立才可執行）
1. 取得即時報價，確認現價 **< NT$377.5**。若現價 > NT$500，本交易全面取消。
2. FOMC 9/17（台灣時間）決議公布後方可下單；維持利率或中性/鴿派方執行，意外升息則暫緩重評。
3. 換算後 R:R to T1 ≥ 1.2，否則縮減或不進場。

## Position sizing by phase
| 階段 | 觸發條件 | 累計 NAV |
|---|---|---|
| Phase 1 | FOMC 後 + 現價 < NT$377.5 | 0.4% |
| Phase 2 | FOMC 中性/鴿派 **且** 9 月月營收 YoY ≥ 100% | 0.9% |
| Phase 3 | Q3 EPS YoY ≥ 50% | 1.5% |

## Stop-loss logic
進場價 -10% 硬停。董監質押比 20.89% 使非線性下跌具強制平倉自我強化風險，故不採 aggressive 的 -12%；台灣中型股日內波動 2–3%，-7% 易遭洗出，故不採 conservative 建議。Phase 1 最大損失 0.04% NAV，Phase 2 全額 0.09% NAV。

## Risk debate adjudication
- Aggressive 最強論點：8 月 MoM +30.48% 是已發生事實，0.25% NAV 等於放棄已確認的基本面 alpha。
- Conservative 最強論點：現價未確認前下單，等同承擔未知 R:R；FOMC 前建倉缺乏等待邏輯。
- Net：採 **neutral**。Conservative 的價格閘門正確但推導出「全面暫停」過度；aggressive 的倉位主張忽略一週即可解除的宏觀不確定性。折衷為「等 FOMC + 驗價 + 0.4% 起步」。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 液冷營收動能 | 月營收 YoY ≥ 100% | 8 月 +112.84%，1–8 月 +115.03% | 成立 |
| 訂單能見度 | 大型雲端合約鎖定至 2028 | 3 月法說會確認，未見撤單 | 成立 |
| EPS 轉換效率 | EPS 隨營收同步高成長 | Q1 +454% → Q2 +61%，動能收斂 | 觀察中 |
| 擴產不損 FCF | NT$30 億以自有現金分期支應 | 融資結構未揭露 | 觀察中 |

## 論點失效條件
- 若連續兩個月月營收 YoY < 60%，「營收動能」支柱失效 → 減碼至 Phase 1 規模。
- 若 Q3 2026 EPS YoY < 20%，「EPS 轉換」支柱失效 → 全數出場。
- 若 Google 或 AWS 正式公告將現有液冷合約移轉予 Envicool 等中國供應商，「訂單能見度」支柱失效 → 全數出場。
- 若公司公告以舉債方式籌措 NT$30 億擴產資金，「FCF」支柱失效 → 減碼一半並凍結 Phase 3。

## Key monitoring triggers
- 取得即時報價後現價 > NT$500：交易取消，不進場。
- 10 月初 9 月月營收若 YoY < 100%：Phase 2 不啟動。
- 收盤跌破 60 日均線且 MACD 翻空：在觸及 -10% 停損前先減半。
- 董監質押比升破 30%：視為槓桿惡化訊號，重評部位。

## Catalyst calendar
- 2026-09-10 — 美國 8 月 PPI
- 2026-09-11 — 美國 8 月 CPI
- 2026-09-15/16 — FOMC 會議（9/17 台灣時間公布）
- 2026-09-17 — CBC 台灣央行利率決議
- 2026-09 中旬 — SEMICON 熱管理技術展示
- 2026-10 初 — 9 月月營收（Phase 2 關鍵觸發）
- 2026-11 — Q3 2026 財報（Phase 3 關鍵觸發）

## FINAL TRANSACTION PROPOSAL

```
TICKER: 8996.TW
ACTION: BUY
VERDICT: BUY_MODIFY
POSITION_STATUS: NEW
DIRECTION: LONG
CONVICTION: MEDIUM (60%)
PRICE_STATUS: PRICE_DATA_UNAVAILABLE
EXECUTION_GATE: live-quote verification required; current price must be < NT$377.5
ENTRY_WINDOW: after FOMC decision 2026-09-17 (Taiwan time)
ENTRY_ZONE: NT$320 - NT$360 (anchored -15% to -5% vs analyst target NT$377.5)
STOP: -10% from fill
TARGET_1: NT$377.5
TARGET_2: NT$490
SIZE_PHASE_1: 0.4% NAV
SIZE_PHASE_2: 0.9% NAV cumulative
SIZE_PHASE_3: 1.5% NAV cumulative
MAX_PHASE_1_LOSS: 0.04% NAV
RR_TO_T1: 1.25
RR_AT_FULL_PHASE_2: 6.75
HORIZON: 1-3 quarters
```

FINAL DECISION COMPLETE
