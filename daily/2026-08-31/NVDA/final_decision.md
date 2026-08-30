FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — NVDA as of 2026-08-31

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## Final trade card (if not REJECT)
> PRICE_DATA_UNAVAILABLE — 本卡不含任何價格數字。所有進出場一律以事件與條件定義。

| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 事件型三批建倉：(1) 即刻建立目標部位 50%；(2) 2026-09-16/17 ALL IN 大會出現 AI CAPEX 上調或新訂單公告後加 25%；(3) Q3 FY2027 財報毛利率 ≥65% 且營收達指引後補滿 25% |
| Stop | 事件型雙層：硬性—Q3 毛利率 <62%、單季指引下修 >10%、或大客戶公告 ASIC 替代 >20%，全數退出；軟性—累計浮虧達 NAV 0.30% 先縮倉 50% |
| Target 1 | Q3 FY2027 財報維持毛利率 ≥65% 且營收達成 Q3 指引，70% 成長路徑續存 → 持有至 FY2027 Q4 財報 |
| Target 2 | 超大規模客戶集體上調 2027 AI CAPEX、市場給予倍數重估 → 持有期延伸至 FY2028 全年 |
| Size | Medium（1.5% NAV，分三批）+ SMH put 對沖 0.3% NAV |
| Horizon | 1-3 個月為核心期，驗證後延伸至 3m+ |
| Conviction | M（MEDIUM） |
| R:R to T1 | 無價格數據，不給數值。以 Neutral 情境估算約 1.5-2.0，僅供參考 |

## Risk debate adjudication
- Aggressive's strongest point: Forward P/E 24-25x 對應管理層公開指引的 FY2028 +70% 成長，PEG 在半導體板塊中最低；Q2 FY2027 營收 $96.22B（+106%）與 Q3 指引再增 12% 已提供充分基本面確認，「等到十月才進場」等同主動放棄一整段窗口。
- Conservative's strongest point: 三重限制同時存在——95% 分析師 BUY 的共識飽和、內部人六個月淨賣出 $413M+ 且零買入、ATR 與技術停損錨完全不可得。事件型停損是落後指標，觸發時往往已是跳空缺口，這使「規模控制」成為唯一有效的風險工具。
- Net: 我採納 neutral 較多。Aggressive 的 3-4% NAV 在沒有波動度資料、沒有技術停損錨的情況下，是在未知 vol 環境放大暴露；其 OTM call spread 更是在 PRICE_DATA_UNAVAILABLE 下無法設定行權價的空論，直接剔除。Conservative 的 0.75% NAV 則以情緒指標推翻了有數據支撐的基本面論據，過度反應。維持 1.5% NAV，但把風險控制從「規模」轉移到「建倉節奏」與「對沖」：分三批進場，讓每一批都由一個可查證事件買單，並以 SMH put 補上缺失的技術停損。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 定價能力（毛利率） | 維持 ≥65% | Q2 FY2027 守住 65%，Vera Rubin 全球量產 | 成立 |
| 成長動能 | 營收 YoY 高速成長、指引續增 | Q2 +106%、EPS $2.22 +113%、Q3 指引 ~$108B（QoQ +12%） | 成立 |
| CUDA 護城河抵禦 ASIC | 訓練與推論需求續由 GPU 承接 | 訓練端仍穩，推論端 TPU v6 / MTIA v2 / Trainium 2 已實際部署，Broadcom 未交付訂單 $730 億 | 觀察中 |
| 中國市場貢獻 | 曾占營收 13-17%（年化 $17B） | H20 禁令後幾近清零，須由非中國市場全額彌補 | 已失效（已計入，不構成新倉阻卻） |

## 論點失效條件
必須可證偽, 且與 Stop 分開 (Stop 是價格紀律, 這裡是論點紀律)。
- 若 Q3 FY2027 財報毛利率低於 62%，定價能力支柱失效 → 立即減碼 50%，次季未回升則出場
- 若管理層任一季將下一季營收指引下修超過 10%，成長動能支柱失效 → 出場
- 若 Microsoft / Google / Meta 任一家正式公告 ASIC 替代 NVDA 採購比例超過 20%，護城河支柱失效 → 出場
- 若連續兩季資料中心營收 YoY 低於 30%，成長動能支柱失效 → 減碼至 Small
- 若美國出口管制擴及歐洲或日本，市場替代支柱失效 → 縮至 Small 並暫停後續批次

## Monitoring trigger
若 ALL IN 大會（9/16-17）未出現任何 AI CAPEX 上調或新訂單訊號，第二批直接跳過，維持 50% 部位等 Q3 財報；若期間任一超大規模客戶下修 2027 CAPEX 指引，立即在停損觸發前重新評估整體部位。

## Catalyst calendar
- 2026-09-16～17 — ALL IN 大會（第二批建倉判定點）
- 2026-10 月（預估） — Q3 FY2027 財報（第三批 / 論點驗證核心節點）
- 持續監控 — 超大規模客戶季度 CAPEX 指引、Broadcom ASIC 實際出貨、《AI 監察法案》立法進度、出口管制範圍

## Phase score
**6.5 / 10**。基本面支柱（毛利率、成長、財務體質）強度給到 8，但三項扣分：PRICE_DATA_UNAVAILABLE 使停損與 R:R 無法量化、95% 共識飽和壓縮容錯率、內部人零買入。分數支持建立部位但不支持放大部位——這正是 Medium 而非 Large 的依據。

FINAL DECISION COMPLETE
