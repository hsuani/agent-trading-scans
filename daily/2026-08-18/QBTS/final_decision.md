# QBTS 最終交易決策 — 2026-08-18

FINAL TRANSACTION PROPOSAL: **SELL/AVOID**（現階段執行為 0% NAV，不建倉）

## 執行摘要

**裁決：MODIFY**（將交易員提案的 0.2% NAV 試探性空倉修正為 0% NAV，並將未來表達工具由裸空改為定義風險的 put spread）。

空方論點在證據品質上明確佔優，且全屬可核實硬數據：Q2 營收 $3.1M、QoQ 零成長；Forward P/S 453x 需 H2 加速 3–4 倍才成立；67% 年度股權稀釋；CEO/CFO 合計 $5.8M 淨拋售（SEC Form 4 可查）。但「論點正確」不等於「現在進場」。四項執行障礙同時存在：PRICE_DATA_UNAVAILABLE（Yahoo Finance HTTP 403）使 entry / stop / ATR / vol-adjusted sizing 全部無法計算；借券利用率約 80%，80 天等待期的 carry cost 侵蝕獲利；Nature 論文（2026-08-17）為敘事動能最強時點；16 位分析師一致 Strong Buy、平均目標 $35.25，構成結構性軋空防線。

無客觀 stop 即無倉位。這是紀律，不是猶豫。

## 風控辯論裁決

- **Aggressive 最強論點：** 0.2% NAV 是「進退失據」的倉位——小到無法貢獻有意義獲利，大到仍完整承擔軋空尾部風險，R:R ≈ 0.5，遠低於 2.0 門檻。真正積極的選擇是保留火力。
- **Conservative 最強論點：** 在無 entry 價的情況下，急漲 40% 的潛在損失完全不可量化，不符合風控紀律。
- **Neutral 的正確裁定：** 否決 Aggressive 的 0.1% NAV 後備選項（不改變 R:R 結構）；同時否決 Conservative 的 QQQ puts / IONQ 配對替代方案（引入 basis risk，稀釋公司級論點的特異性）。

**我採納 neutral 觀點。** 理由：積極與保守兩方在「0% NAV」這個結論上已獨立收斂，分歧只剩未來的表達工具。neutral 在此做出了唯一正確的區分——QBTS 的 bear thesis 是公司級結構性問題，未來若進場，應用 QBTS 自身的 put spread，而非模糊的替代標的。

## 交易參數

| 欄位 | 數值 |
|---|---|
| 當前部位 | **0% NAV — 嚴格 AVOID，不建倉** |
| Direction | SHORT_OR_AVOID（信心 MEDIUM） |
| Entry / Stop / Targets | **待價格恢復後確認**（不臆造數字） |
| 未來工具 | QBTS put spread $20/$13，expiry 2026-12-18；notional ≤ 0.3% NAV |
| 最大損失 | 已付權利金（定義風險）；不用裸空、不用 QQQ puts |
| Horizon | 中期 1–3 個月，第一道閘門為 2026-11-05 |
| 當前 R:R | 不成立（無法計算） |

**進場條件須全部成立：** ① Q3 營收 ≤ $3.2M；② RPO 期末餘額停滯無加速認列；③ 實時價格數據恢復可確認 ATR / RSI；④ 管理層無 SEC Form 4 淨買進。

## 監控觸發點

**若 2026-11-05 Q3 財報營收 > $3.5M 且 QoQ 加速，或 CEO/CFO 出現 SEC Form 4 淨買進，則空方論點失效，永久放棄本次佈局，重啟中性評估。**

次要監控：08-20 至 08-30 分析師是否集體上調至 $40+（軋空燃料強化）；9–10 月 Qubits 2026 大會 17-qubit 客戶交付是否確認（空方論點最大失效風險）。

## Catalyst calendar

- 2026-08-20 至 08-30 — 分析師 Nature 論文評論期
- 2026 年 9–10 月 — Qubits 2026 用戶大會，17-qubit 系統演示
- 2026-11-05 — Q3 2026 財報（核心裁決點）
- 2026-12-18 — 潛在 put spread 到期日

## FINAL TRANSACTION PROPOSAL

**SELL/AVOID** — 方向偏空，但現階段執行為 0% NAV 觀望。空頭論點成立，時機不成立。

PORTFOLIO MANAGER COMPLETE
