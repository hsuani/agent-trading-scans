FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 005930.KS as of 2026-09-09

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

（新倉判定：005930.KS 不在 `pipeline/tools/held_tickers.txt` 內，走新倉框架。BUY 為**條件式核准**，觸發條件未達成前不得下單。）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無即時價格，暫不給進出場價位；觸發達成後依當日 KRX 收盤價 ±1.5% 定義區間 |
| Stop | 無即時價格；價格數據恢復前以邏輯止損替代（見「論點失效條件」）。恢復後：SSNLF 收盤跌破 $130 |
| Target 1 | KRW 471,908（分析師共識錨點，非交易指令） |
| Target 2 | KRW 725,000（P/E 修復至歷史中位數 12.74x 之錨點） |
| Size | Small→Medium 分批：第一批 0.4% NAV，第二批補至 0.75% NAV 上限 |
| Horizon | 1–3 個月核心窗口；超級週期確認可延長至 12 個月 |
| Conviction | M（Dashboard score 6/10，conviction 58%） |
| R:R to T1 | 無法計算 — 缺即時進場價與止損價。數據恢復後須驗算 R:R ≥ 1.5 方可執行 |

**執行門檻（兩者皆須成立才可下第一批）**
1. Q3 2026 DRAM 合約定價確認季環比 **+15% 以上**（TrendForce / DRAMeXchange 公告，預計 9 月下旬）。
2. 即時報價恢復且 R:R ≥ 1.5 可驗算。
第二批（+0.35% NAV）：Q3 業績預告（10 月初）優於市場預期後補足。
**不核准**：Aggressive 的立即滿倉 1.5%、call spread（SSNLF OTC 選擇權流動性未經驗證）。
**核准**：0.1% NAV SOX ETF puts（2026-12 到期）作為週期尾部對沖，僅在第二批建立後配置。

## Risk debate adjudication
- Aggressive's strongest point：Forward P/E 4.16x 與 KRW 90–110 兆股東回報是有日期、可偽證的硬性支撐，縮倉到象徵性規模等於放棄真實的非對稱性。
- Conservative's strongest point：無止損即無倉位。R:R 4.3:1 的分母（-7% 至 $130）是在無即時報價下憑空設定的假設值，把估算包裝成驗證過的事實。
- Net：我採納 **neutral** 的權重最高。Aggressive 的 4.3:1 建立在不存在的價格上，這種精確度是虛假的；Conservative 的 0.25% 則在數學上無法對 NAV 產生任何有意義貢獻，是偽裝成風控的拒單。0.4%→0.75% 分批既保留 MEDIUM 評級應得的部位，又把最大不確定性（DRAM 定價、Q3 業績）留在資金投入之前。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 記憶體超級週期延伸 | Q3 DRAM 合約價 QoQ +20%，70% 產能受 LTA 保護 | 尚未公告，9 月下旬揭曉 | 觀察中 |
| HBM4 技術資格與份額回升 | NVIDIA/AMD 雙認證，份額自 <10% 回升至 25–30% | 認證已完成並多源確認 | 成立 |
| 估值深度低估 | Forward P/E 4.16x vs 歷史中位數 12.74x | 估值差距仍在，但 +135% YTD 已消化部分 | 成立（安全邊際縮小） |
| 技術面/籌碼 | 財報後回檔為換手 | Q2 後機構出貨、SSNLF 貼近 52 週高點 $139.76 | 觀察中（偏負面） |

## 論點失效條件
- 若 Q3 DRAM 合約定價 QoQ **低於 +10%**，超級週期支柱失效 → 取消建倉；已建倉則出場。
- 若 Q4 2026 DRAM/NAND 合約價出現**首次季環比轉負**，週期支柱失效 → 出場。
- 若三星 HBM4 份額於 Q4 官方或 TrendForce 數據**跌至 20% 以下**，份額支柱失效 → 減碼至半倉。
- 若 AWS / Azure / GCP 任二家於財報中**公開下修 AI 資本支出指引**，需求支柱失效 → 減碼。
- 若 10 月中前即時報價仍無法恢復，執行前提失效 → 整案擱置，不以盲飛方式建倉。

## Monitoring trigger
若 SSNLF 在 DRAM 定價公告前跌破 $130，或公告當日利多出盡收黑逾 5%，在止損前重新評估整案。

## Catalyst calendar
- 2026-09 下旬 — Q3 DRAM 合約定價確認（主要入場觸發）
- 2026-10 初 — 三星 Q3 業績預告（第二批觸發）
- 2026-10 中下旬 — SK Hynix Q3 法說會，HBM 供需與競爭格局
- 2026-11 — 三星 Q3 完整財報，DX 部門虧損改善程度

FINAL DECISION COMPLETE
