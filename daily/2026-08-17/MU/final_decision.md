FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — MU as of 2026-08-17

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
APPROVE（核可交易員的 AVOID／0% 曝險判定，不做任何價位化修改）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（僅方向性偏好，本輪不執行） |
| Entry zone | 無即時價格，暫不給進出場價位 |
| Stop | 無即時價格，暫不給進出場價位 |
| Target 1 | 無即時價格，暫不給進出場價位 |
| Target 2 | 無即時價格，暫不給進出場價位 |
| Size | 0% NAV（本輪不建倉；資料恢復後起手上限 1/4 倉） |
| Horizon | 數週至數季，驗證窗口對齊 8/26 與 9/25 兩場財報 |
| Conviction | M（方向性）／L（可執行性） |
| R:R to T1 | 無即時價格，暫不給進出場價位 |

## 決策理由
market.md 連兩期 `PRICE_DATA_UNAVAILABLE`。sentiment.md 的 "$876"、內部人成交價位、fundamentals.md 的 Forward P/E 10-15x 皆為敘述性數字，非經核實報價。核心矛盾（實際 P/E 是 10-15x 還是 125x+）未解前，任何價位表都是把未驗證數字包裝成風控參數，這比不下單風險更高。結構性多頭論點（跨廠商互相驗證的 HBM 產能鎖定至 2027、FY2025 營收 +61% 與毛利率躍升、41 買進/0 賣出共識）品質確實優於熊方，但足以支撐「方向性偏多」，不足以支撐「在無法量化下檔的狀態下投入資金」。

## Risk debate adjudication
- Aggressive's strongest point：API 故障不等於市場無價；空手等待 8/26、9/25 兩大催化劑確有真實機會成本，且 call spread 以權利金封頂下檔的構想在結構上優於現股試探倉。
- Conservative's strongest point：無法量化 $ 風險時談倉位本身不成立。若 P/E 確為 125-195x，de-rating 幅度 20-40% 屬結構性重估，遠大於錯過數日漲幅的滯後成本；CEO 6-7 月賣股 $37-40M 且無高管買進抵消，與「被低估」敘事方向不一致。
- Net：我採納 neutral 的裁決架構、執行上靠向 conservative。決定性理由是程序性的——trade_proposal.md 已自訂「不得依敘述性數字回推價位」的紅線，Aggressive 的「人工核實現價」無法在報告鏈留下可驗證紀錄，等同繞過自訂風控。連 call spread 也需要行使價，同樣落在紅線內，故本輪一併不執行。Conservative 要求 P/E 必須落在 10-15x 才放行則過度精確，10-15x 本身也是未驗證數字，不採為放行門檻。

## Monitoring trigger
若 market.md 恢復可信即時報價，且以當日股價反算的 Forward P/E 高於 60x（即偏向熊方推算區間而非 fundamentals.md 基準），則 investment_plan.md 的 LONG 論點在建倉前即需重新論證，起手倉位由 1/4 倉再下修。反之若落於 30x 以下，得依 1/4 倉試單執行。另：月度 DRAM/NAND 現貨價格轉跌，或 SK Hynix/Samsung 宣布 HBM4 加速搶佔 MU 客戶份額，任一發生即取消 LONG 偏好。

## Catalyst calendar
- 2026-08-26 — NVDA Q3 FY2027 財報（間接驗證 MU HBM 訂單能見度）
- 2026-09-25（估）— MU Q4 FY2026 財報（HBM 營收占比、毛利率指引、FY2027 展望）
- 2026 Q4（估）— MU HBM4 樣品出貨進度公告
- 持續 — 月度 DRAM/NAND 現貨價格；market.md 行情恢復即優先觸發重評

FINAL DECISION COMPLETE
