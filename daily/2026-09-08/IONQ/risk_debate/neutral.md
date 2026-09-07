# Neutral risk view — IONQ

## Points of agreement（雙方共識）
- 認股權證 IONQ WS（2026-09-30 到期）是值得重視的技術性事件，雙方都認同此日前後須調整部位策略。
- 基本面失效標準（Q3 收入 < $65M、現金 < $200M、毛利率 < 30%）合理，應保留於無效化條件。
- Investor Day 反應須納入入場決策，不應忽視市場對催化劑的即時定價。
- EV/Revenue 25-40x 在 PRICE_DATA_UNAVAILABLE 環境下令安全邊際薄，一致支持以小倉位為起點。

---

## Aggressive overreach（激進方過度處）
- **Where**：主張立即將倉位擴至 1.5% NAV，並於 Investor Day 當日收盤前建立 0.75% NAV。
- **Why**：在 PRICE_DATA_UNAVAILABLE 環境下，既無即時 ATR 可計算波動調整倉位，也無法確認 RSI/MACD 多頭排列，倉位計算本身缺乏數據基礎。R:R 1:2.5–1:3.5 的估算建立在假定上行幅度 25-40% 且損失上限已知的前提，兩者在無即時價格時皆屬推算，不足以支撐立即加倍倉位。call spread 建議在 IV 不可查的情況下同樣缺乏執行基礎。

---

## Conservative overreach（保守方過度處）
- **Where**：建議若 ATR 偏高則進一步縮至 0.25% NAV，並考慮 QTUM ETF 反向部位對沖。
- **Why**：0.25% NAV 倉位在任何合理上行情境下對組合的絕對貢獻趨近於零，使持有論題喪失經濟意義。QTUM ETF 反向部位在基礎倉位僅 0.5% NAV 時會製造不對稱的摩擦成本，且在數據不足的環境下難以調校對沖比率。概率估算（情境 A 20%、B 15%、C 10%）同樣缺乏定量支撐，屬反射性悲觀。

---

## Balanced adjustment proposal（均衡調整方案）

- **Size**：初始維持 **0.5% NAV**（保守方正確）。IONQ WS 到期後（2026-10-01 起），若 Investor Day 已確認正向訊號且市場消化稀釋衝擊，加碼至 **1.0% NAV**（折衷，非激進方要求的 1.5%）。
- **Stop**：基本面失效標準保留，同時**必須補設硬性價格止損**（保守方論點成立）：入場後單日跌幅逾 **15%**，無論季報時點立即出場；Investor Day 後連兩交易日收跌逾 8% 同樣觸發。價格數據恢復後依技術支撐校準。
- **Entry**：等待 Investor Day 確認方向正確（原提案）。若當日收盤前無「利多出盡」跡象，可於**當日或次一交易日**建立初始倉位（接受激進方部分邏輯：催化劑窗口不必過度推延）；不等 WS 到期後才全面進場，以免錯過 Investor Day 帶動的初始重新定價。
- **Hedge**：在 PRICE_DATA_UNAVAILABLE 環境下，暫不執行 call spread 或 QTUM 反向部位；若 IV 與流動性資料恢復，可於 Q3 財報前評估輕倉 call spread（cost 上限 0.15% NAV）。
- **Time horizon**：維持 **1-3 個月**，以 Q3 財報（10-11 月）為核心決策節點。

---

## Net $ risk if stop hits
PRICE_DATA_UNAVAILABLE，無法以 (entry − stop) × shares 計算絕對美元損失。
以 NAV 比例估算：
- 初始倉 0.5% NAV × 硬性止損 15% ≈ **~0.075% NAV**
- 加碼後 1.0% NAV × 15% ≈ **~0.15% NAV**（WS 到期後最大敞口）

---

## Net $ upside at T1 / T2
同樣以 NAV 比例框架估算（非絕對美元，待價格數據恢復後重算）：
- **T1**（商業企業收入佔比 > 70%、毛利率 > 50%）：1.0% NAV × ~25% 上行 ≈ **~0.25% NAV**
- **T2**（Investor Day 具體里程碑 + 新企業客戶 + WS 拋壓消散）：1.0% NAV × ~40% 上行 ≈ **~0.40% NAV**

NEUTRAL VIEW COMPLETE
