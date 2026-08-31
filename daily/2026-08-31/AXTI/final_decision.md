# Final decision — AXTI as of 2026-08-31

FINAL TRANSACTION PROPOSAL: **SELL**

## Verdict
MODIFY

**FINAL VERDICT：AVOID 現股 / 條件式 SHORT（僅限 defined-risk put spread），Conviction 6/10。**

AXTI 不在 `held_tickers.txt`，屬新倉決策，問題是「該不該進」。答案：不建立現股空倉（保守方在執行面完全正確），但核准以極小額 put spread 承接下行曝險（中立方的關鍵洞見成立）。

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | SHORT（透過 put spread，非現股放空） |
| Entry zone | 標的 $88.00 – $96.00 **UNVERIFIED**；買 $90 Put / 賣 $65 Put **UNVERIFIED**，到期 2026-12 |
| Stop | 無價格停損 — 最大損失＝已付權利金，成交當下鎖定 |
| Target 1 | $87.50 **UNVERIFIED**（估值回歸分析師共識） |
| Target 2 | $52.50 **UNVERIFIED**（出口許可凍結＋估值正常化） |
| Size | Small（權利金支出 ≤ 0.20% NAV，硬上限） |
| Horizon | 約 1 個季度，涵蓋 Q3 2026 財報至 2026-12 到期 |
| Conviction | M（6/10） |
| R:R to T1 | ~1.7（T2 情境 ~6–7） |

**執行閘門（Execution Gate）**：上述所有價格皆為 UNVERIFIED，禁止直接掛單。須先取得券商可驗證即時報價，確認 (1) 標的價仍在 $88–96 區間、(2) 長腳 Delta 約 0.30–0.35、(3) 買賣價差合理。任一項不符即不執行，當日轉為純 AVOID。不追高、不改用現股空單替代。

## Risk debate adjudication
- Aggressive's strongest point：空頭論述今天就成立——EV/Sales 27x 對同業 10x、31 次內部人淨賣出 0 買入、股價已高過分析師目標上限，這些是已發生的事實，不需要等催化劑；等到 $100–105 才進場等於自願遲到。
- Conservative's strongest point：在 PRICE_DATA_UNAVAILABLE 下，現股空單的停損無法提交，等同裸空；ATR 未知則 vol-adjusted sizing 無從計算，R:R to T1 僅 1.3x 也低於空頭門檻。
- Net：我採納 **neutral** 為主。兩方爭的其實不是方向而是工具。Put spread 的最大損失在成交當下即固定，完全繞開「停損無法執行」與 gap risk 這兩個保守方的核心否決理由；同時又保留激進方要的財報前 Gamma 曝險。權利金上限壓到 0.20% NAV（而非激進方的 0.3%），因為信心只有 M。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 估值失錨 | 股價高於分析師目標區間上緣 | ~$93 vs 目標上限 $91（UNVERIFIED） | 成立 |
| 內部人離場 | 淨賣出主導 | 31 次賣出、0 買入，CFO 套現 ~$450 萬 | 成立 |
| 中國出口許可風險 | 許可乾旱可再現 | Q4 2025 先例已記錄，現行指引未量化上限 | 觀察中 |
| 基本面護盾（反向支柱） | Lumentum LTA、InP 雙寡頭 | LTA 有效、Q2 超預期 — 對空頭不利 | 成立（反向） |

## 論點失效條件
與 Stop 分開；此處為論點紀律。
- 若 Q3 2026 財報營收超共識 >30% 且管理層量化出口許可正常化並上調全年指引 → 估值失錨支柱失效 → 出場（權利金認賠平倉）。
- 若 SEC Form 4 出現 CEO 或 CFO 淨買入 → 內部人支柱失效 → 減碼一半。
- 若美國商務部或中國商務部正式放寬 InP 對中出口配額並量化額度 → 政策支柱失效 → 出場。
- 若住友電工退出或大幅削減 InP 產能 → 競爭格局根本改善 → 出場。

## Monitoring trigger
若標的在財報前突破 $100 **UNVERIFIED** 且成交量放大，不加碼、不改現股空單，僅重估權利金剩餘價值；若長腳 Delta 跌破 0.15，直接平倉回收殘值。

## Catalyst calendar
- 2026-10-29 至 11-02 — Q3 2026 財報（核心觸發點）
- 週度 — SEC Form 4 內部人交易申報
- 隨時 — 美中出口管制更新、NVIDIA 採購節奏公告
- 2026-12 — Put spread 到期

## Metrics summary
| 指標 | 數值 | 備註 |
|---|---|---|
| Verdict | MODIFY（AVOID 現股 / 條件式 SHORT） | 新倉框架 |
| Conviction | 6/10 | M |
| EV/Sales | 27x vs 同業 10x | 溢價 +170% |
| P/FCF | 40–60x | 基礎材料廠不適用 |
| 內部人淨交易 | 31 賣 / 0 買 | CFO ~$450 萬 |
| 現股空倉 Size | 0% NAV | 保守方採納 |
| Put spread 權利金 | ≤ 0.20% NAV | 最大損失即此數 |
| Entry zone | $88–96 UNVERIFIED | 需 gate 確認 |
| T1 / T2 | $87.50 / $52.50 UNVERIFIED | — |
| R:R to T1 / T2 | ~1.7 / ~6–7 | — |
| Horizon | 至 2026-12 到期 | 涵蓋 Q3 財報 |
| 價格資料狀態 | PRICE_DATA_UNAVAILABLE | 全部水位 UNVERIFIED |

FINAL DECISION COMPLETE
