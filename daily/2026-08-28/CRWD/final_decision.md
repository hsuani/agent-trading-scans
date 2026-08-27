FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — CRWD as of 2026-08-28

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

（新倉判定：CRWD 不在 `pipeline/tools/held_tickers.txt` 內，走新倉框架。）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE（觸發後以財報後 1–2 個交易日收盤價分批建倉） |
| Stop | PRICE_DATA_UNAVAILABLE（規則：建倉均價下方 15–18%，價格資料恢復後以 1.5×ATR14 校驗，兩者取較寬者） |
| Target 1 | PRICE_DATA_UNAVAILABLE（對應 +20–25%：NRR 回升獲財報確認） |
| Target 2 | PRICE_DATA_UNAVAILABLE（對應 +35–40%：估值重評 + 訴訟和解落低端） |
| Size | Small–Medium：初始 1.0% NAV，單一觸發後分批加至 1.5% NAV，上限 2.0% NAV |
| Horizon | 1–3 個月（季度級別，涵蓋 FY2026 Q3 財報） |
| Conviction | M（55%） |
| R:R to T1 | 約 1.5（依 neutral 的 15% stop / 20–25% 上行推估，價格恢復後須重驗，低於 1.5 則不建倉） |

補充條件：同步買入 HACK ETF 少量 OTM put（0.10–0.15% NAV）對沖板塊系統性下跌。不採用 aggressive 提議的 call spread 疊加——在 stop 距離不可計算時再加一層槓桿，屬於重複下注同一個二元事件。

## Risk debate adjudication
- Aggressive's strongest point：保守派的複合觸發（NRR ≥ 115% 且和解 ≤ $150M 同時成立）機率過低，實質等於放棄建倉；99%+ 留存率是危機後實測值而非預測，不應被當作待驗證假設打折。
- Conservative's strongest point：在 entry/stop 全數 PRICE_DATA_UNAVAILABLE 下，(entry − stop) × shares 無法核實，任何以 % NAV 表述的倉位都缺乏風險基準；訴訟 $500M 上限理論上超過年度 FCF，屬真實尾部。
- Net：我採 **neutral** 權重較高。保守派存在自我矛盾——其自訂 stop（25–27%）比激進派（15–18%）更寬，卻據此要求壓倉至 0.75%，計算上其自身情境的單次損失 0.40% NAV 本就在可接受範圍。激進派則在指標全空的情況下要求 2.5% NAV 加期權，屬於在資訊真空中放大部位。折衷取 1.0% NAV 起手、單一觸發、財報後確認收盤再進，並保留 hedge。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 客戶留存韌性 | 危機後留存率 > 95% | 實測 99%+，機構持股 87–90% 未見出清 | 成立 |
| Falcon 平台黏性／ARPU | 每客戶 5+ 模組採用、替換周期 12–18 個月 | 未有最新財報模組數據佐證 | 觀察中 |
| 訴訟負債可吸收 | 和解落於 $100–150M，現金池 $800M–$1B 可吸收 | 金額未公告，區間仍寬至 $500M | 觀察中 |
| 估值安全邊際 | P/S 向行業 12x 收斂 | P/S 15–20x、EV/EBITDA 50–70x，較行業溢價 50–100%；EBITDA margin 由 15–20% 壓至 5–10% | 觀察中（偏弱） |

四根支柱中僅一根明確成立，其餘皆待驗——這正是倉位壓在 1.0% NAV 而非 1.5–2.5% 的核心理由。

## 論點失效條件
（與 Stop 分離：論點壞了就動作，不等價格。）
- 若 FY2026 Q3 財報 NRR ≤ 100%，「留存韌性」支柱失效 → 出場（全數）。
- 若 NRR 落於 100–110% 區間且管理層下修 FY2026 FCF 指引，該支柱轉為鬆動 → 減碼至 0.5% NAV，凍結加碼。
- 若訴訟和解金額公告 ≥ $400M，或公司為此發行新股補充流動性，「訴訟可吸收」支柱失效 → 出場。
- 若揭露每客戶平均模組採用數低於 4.0，或 Fortune 500 續約中多供應商採購比例明顯上升，「平台黏性」支柱失效 → 減碼一半。
- 若發生第二次重大軟體宕機事件 → 立即出場，不論價格。

## Monitoring trigger
建倉觸發（任一即可，不需同時）：(1) FY2026 Q3 財報確認 NRR ≥ 115% 且 FCF 指引未下修；(2) 訴訟和解公告 ≤ $150M。由財報觸發者，須等財報後 1–2 個交易日收盤站穩再進，規避 ±12–18% 當日滑點。觸發前一律觀望，不追價。另：若價格資料恢復後 R:R to T1 < 1.5，取消建倉。

## Catalyst calendar
- 2026-11（預計）— FY2026 Q3 財報：NRR、每客戶模組數、FCF margin
- 時間未定 — 訴訟和解金額公告
- 2026 Q3–Q4 — AI 安全模組新品發布
- 持續 — EU NIS2 合規期限推動的新簽約

FINAL DECISION COMPLETE
