# Final decision — IONQ as of 2026-08-11

FINAL TRANSACTION PROPOSAL: **HOLD**

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY —「條件式掛單框架」，今日不建立任何倉位（0% NAV）。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（條件觸發後生效） |
| Entry zone | $54.00 – $60.00（僅在 PRICE_DATA 恢復且實際成交價落入此區間才執行） |
| Stop | $50.00（硬止損，不可下移） |
| Target 1 | $75.00 |
| Target 2 | $85.00 |
| Size | Small（0.5% NAV，一次建足，不加碼至 Q3 財報後） |
| Horizon | 1–3 個月（決策節點：Q3 2026 財報，預估 10–11 月） |
| Conviction | M |
| R:R to T1 | 1.5（以區間上緣 $60 計；區間下緣 $54 為 2.1） |

執行紀律：價格數據恢復後若股價 > $60，一律不進場，本案作廢並於 Q3 財報後重啟評估。不使用 call spread（現價未知無法設定合理行權價）。不預建 SHIELD 事前倉位。

## Risk debate adjudication
- Aggressive 最強論點：SHIELD 框架首批大單屬離散型 gap-up 事件，等折價的框架在催化劑密集期確有機會成本；且 -10% 止損對日內波動 ±10% 的標的等同保證掃倉。
- Conservative 最強論點：P/S ~100×、adj. EBITDA -$320M、年化 OCF -$604M 再疊加 SkyWater 整合 capex，安全邊際為零；在無法錨定入場估值時，止損只是紙上數字，真正的風險是敘事崩潰後的 -50% 尾部，而非帳面 0.08% NAV。
- Net：我採 neutral 的架構但往 conservative 收緊。積極方的非對稱性試算全部建立在「現價已有折價」這個未經證實的假設上——用未知數論證倉位規模不成立。因此保留 neutral 的條件式建倉邏輯，但把入場門檻由 ≤$65 下修至 ≤$60，理由單一且可驗證：只有 ≤$60 才能讓 T1 的 R:R 真正跨過 1.5× 門檻。$65 入場的 1.1× R:R 不值得為一檔零安全邊際標的動用風險預算。

## Monitoring trigger
若 Q3 2026 財報揭露單季 operating cash flow 惡化至 -$175M 以下（年化超過 -$700M），或公司公告任何形式的股權募資 / ATM 增額，則不待 $50 止損，立即無條件平倉並重評論文。

## Catalyst calendar
- 數小時–數日內 — PRICE_DATA 恢復，第一時間校正 S/R 與 ATR，重算止損
- 2026-10 至 11 月 — Q3 2026 財報（SkyWater 毛利貢獻、OCF 趨勢、量子 organic 增速）
- 持續監控 — SHIELD 框架首批訂單、DARPA Evergreen-05 交付進度
- 2027 Q1（估） — FY2026 全年財報，驗證 $280–290M 指引

FINAL DECISION COMPLETE
