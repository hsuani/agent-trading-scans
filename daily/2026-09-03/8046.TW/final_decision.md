# Final decision — 8046.TW 南亞電路板 as of 2026-09-03

FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY — 條件式核准，今日不投入任何資金（觀察名單）。Conviction **60%**（LONG 方向偏多，但進場時機未到）。

新倉判定（8046.TW 不在 held_tickers.txt）。方向認可，時點與規模下修。

## Final trade card
| 欄位 | 內容 |
|---|---|
| Direction | LONG（條件式，尚未建倉） |
| Entry zone | 無即時價格，暫不給進出場價位 |
| Stop | 無即時價格，暫不給進出場價位；改以「成交價 -20%」為硬性價格底板，於實際成交當日以真實成交價換算後鎖定 |
| Target 1 | 無即時價格；外部參考為分析師均值目標（基準情境） |
| Target 2 | 無即時價格；外部參考為 Goldman Sachs 目標（高峰情境，選擇權性質） |
| Size | Small — 觸發後初始 **0.5% NAV**，硬上限 **0.75% NAV** |
| Horizon | 2-4 季 |
| Conviction | M |
| R:R to T1 | 無價格數據，不計算 |

## Entry trigger（條件式，四項須全數成立）
1. **價格數據恢復**：market.md 不再是 PRICE_DATA_UNAVAILABLE。無法設定停損就不得動用資金——這是不可豁免的前置條件。
2. **財報驗證**（2026-11-10 Q3）：EPS ≥ NT$3.0 **且** 合併毛利率高於 Q2 水準（口徑須為公司財報揭露之合併毛利率；Q1「12.1%」為營益率，兩者不可混用——原提案的「毛利率 ≥ 48%」門檻定義不一致，不予採用）。
3. **產業信號**：2026-10～11 月 DigiTimes ABF 報價指數未出現連續兩個月下跌。
4. **需求端**：Microsoft／Google／Meta Q3 法說會 AI 資本支出年增 ≥ +30%。

1+2+3 成立 → 建 0.5% NAV；四項全數成立 → 加至 0.75% NAV 上限。任一未達標，不進場。

## Exit trigger
- 成交價 -20% 硬底板跌破 → 無條件全出，不等財報。
- Q3 或 Q4 毛利率環比下滑且 EPS < NT$3.0 → 全出。
- Unimicron 或 Kinsus 正式公告 ABF 新產能提前至 2027 上半年量產 → 減碼 50%。
- DigiTimes ABF 報價指數連兩月下跌且累計跌幅 >10% → 減碼 50%。
- Hyperscaler 資本支出指引年增 <+15% → 全出。

## 論點支柱
| 支柱 | 當初預期 | 現況 | 判定 |
|---|---|---|---|
| ABF 供給短缺與定價權 | 產能售罄、交期拉長 | DigiTimes 及同業多源確認，交期 20-30 週 | 成立 |
| Ajinomoto 成本轉嫁 | 漲價可全額轉嫁客戶 | +30% 成本 Q3 才生效，無任何財報驗證 | 觀察中（核心未決） |
| 盈利動能 | EPS 加速 | Q1 EPS +534% YoY 已實現 | 成立 |
| 估值紀律 | 週期性股高 P/E 可承受 | P/E >30x，降溫情境下行風險大 | 觀察中（偏負面） |

## 論點失效條件（論點紀律，與 Stop 分開）
- 若 Q3 2026 合併毛利率環比下滑 → 支柱二失效 → 取消進場（已建倉則出場）。
- 若欣興／Kinsus 公告 ABF 產能提前量產 → 支柱一失效 → 減碼。
- 若連兩季 ABF 報價指數累計跌逾 10% → 支柱一失效 → 減碼。

## Key risk factors
Ajinomoto 95% 市占、議價權為零；Q1 營益率僅 12.1%，緩衝極薄；週期頂部估值雙殺；投信近 20 日賣超 6,078 張與外資背離；FCF／負債結構 DATA_UNAVAILABLE。

## 三方風險觀點裁決
- Aggressive 最強論點：68 天等待期確有機會成本，正面事實已多源確認。
- Conservative 最強論點：以論點條件完全取代價格止損，在空窗期形成無底板下行；12.1% 營益率承受不起 +30% 成本失誤。
- Net：本次採 **conservative 為主、neutral 為輔**。理由是本案根本缺陷在「無價格數據」，連停損都無法定義；Aggressive 主張立即滿倉、call spread，是在無風控工具的狀態下加大曝險，方向對但程序不成立。故保留 LONG 方向與 neutral 的條件式進場邏輯，採納 conservative 的 0.75% 上限與硬性百分比底板；不採 SOXX put 對沖——0.5% NAV 部位的對沖成本高於尾部效益。

## Monitoring trigger
若 2026-10-15 前 hyperscaler 出現資本支出負面預警，或 ABF 報價指數轉跌，整份論點降級重審，不等 11-10 財報。

## Catalyst calendar
- 2026-10～11 月 — DigiTimes ABF 報價指數月度更新
- 2026-11-10 — Q3 2026 財報（論點主要裁決點）
- 2026-11 月 — Microsoft／Google／Meta Q3 法說會
- 2027-Q1 — ABF 供需缺口 21% 驗證點

## Phase
Full Pipeline (Phase 4 complete)

FINAL DECISION COMPLETE

PORTFOLIO MANAGER DECISION COMPLETE
