FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — PWR as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

```
VERDICT: BUY
Direction: LONG
Conviction: 58% (Medium)
Size: 1.0% NAV
Entry: PRICE_DATA_UNAVAILABLE
Stop: PRICE_DATA_UNAVAILABLE (−10% from entry once price available)
T1: PRICE_DATA_UNAVAILABLE
T2: PRICE_DATA_UNAVAILABLE
Catalyst: 2026-Q3 財報 (Nov 2026)
```

PWR 不在 `held_tickers.txt` 內，屬新倉，採 A 框架。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE（取得即時報價後單筆執行） |
| Stop | PRICE_DATA_UNAVAILABLE（進場價 −10% hard stop） |
| Target 1 | PRICE_DATA_UNAVAILABLE（對應分析師均值目標 $783.17，約 +14%） |
| Target 2 | PRICE_DATA_UNAVAILABLE（Q3 驗證後再評價情境，約 +22%） |
| Size | Small–Medium（1.0% NAV，單一批次） |
| Horizon | 1–3 個月，核心驗證點為 Q3 財報 |
| Conviction | M |
| R:R to T1 | 1.4（+14% 上行 ÷ 10% stop） |

**執行前置條件（不可跳過）**：報價恢復前禁止下單。取得即時報價後，先以 market.md 支撐阻力位驗算 stop 與 T1，若 R:R to T1 < 1.2 則放棄本次進場。另配置約倉位名義值 0.5% 的 PWR OTM put 對沖 AECOM 式執行尾部風險。

## 對原提案的修改
1. Size：1.5% NAV → **1.0% NAV**（R:R 僅約 1.4，且報價缺失下不應給滿額 MEDIUM 倉）。
2. 取消以 Fed 9/20 例會語調為觸發的第一批自動進場——宏觀語調不是進場依據。
3. 取消「Q3 後加碼至 1.5%」的預設分批，加碼須另行決策。
4. 加入 0.5% 名義值 OTM put 對沖；否決 aggressive 的 call spread。

## Risk debate adjudication
- Aggressive's strongest point：$53B backlog（+59% YoY）是已簽約合約金額而非敘事，方向性不需要等 Q3 才成立；AECOM 為 EPC wrap 設計建管，與 PWR 工料實報為主的合約結構確有差異，類比不能全盤照搬。
- Conservative's strongest point：41× Forward P/E 的安全邊際接近零，管理層 12 個月淨賣出 $17M、買入 $0、持股僅 0.87%，利益一致性偏弱；這是可查核事實，不是情緒。
- Net：我採 **neutral** 較重。Aggressive 的 PEG 0.58 建立在 +71% EPS 可持續的假設上，但該增速含大型合約集中兌現的時點性成分，不足以支撐 2.5% NAV；Conservative 要求 RSI 形態確認則把不相干的技術過濾器加在基本面論點上。1.0% NAV + 單筆執行 + 尾部對沖是唯一同時尊重兩方可查核事實的方案。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 積壓訂單動能 | backlog YoY 維持高雙位數 | $53B，+59% YoY | 成立 |
| 盈利加速與指引上修 | 指引持續上調 | FY2026 上調至 $39.3–39.7B，EPS +71% | 成立 |
| 大型固定價格合約執行品質 | 毛利率不因 NiSource 等合約惡化 | 未經財報驗證，AECOM $337M 先例在側 | 觀察中 |
| 估值倍數維繫 | 41× P/E 由成長支撐 | 安全邊際薄，內線淨賣出 $17M | 觀察中 |

## 論點失效條件
與 Stop（價格紀律）分離；下列任一成立即依論點紀律動作，不必等價格觸及 stop。
- 若 Q3 2026 電力部門毛利率 YoY 收窄超過 150 bps，執行品質支柱失效 → 出場。
- 若 PWR 公告任一單一合約成本超支或減記金額 ≥ $1 億，執行品質支柱失效 → 出場。
- 若管理層下修 FY2026 EPS 指引中位數（現為 $16.70），盈利動能支柱失效 → 出場。
- 若 Google、Microsoft、Amazon 任一在財報中明確下修年度資料中心資本支出金額，需求支柱失效 → 減碼至 0.5% NAV。
- 若內線 12 個月累計淨賣出擴大至 $30M 以上且仍為 0 買入，估值支柱鬆動 → 減碼一半。

## Monitoring trigger
若取得報價後計得 R:R to T1 < 1.2，或 backlog 季增轉為負值，於 stop 觸發前重新評估。

## Catalyst calendar
- 2026-09-20 前後 — Fed 例會（監控用，非進場觸發）
- 2026-09 月中下旬 — NiSource 合約監管批准進度
- 2026-11 月初 — Q3 2026 財報（核心驗證節點）

FINAL DECISION COMPLETE
