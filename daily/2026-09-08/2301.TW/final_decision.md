FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 2301.TW as of 2026-09-08

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無即時價格，暫不給進出場價位（PRICE_DATA_UNAVAILABLE，分兩批建倉：即刻 0.25%，Q3 法說會後 0.25%） |
| Stop | 無即時價格，暫不給進出場價位 — 改用 fundamental stop：Q3 2026 EPS < 2.5 TWD（10/28 公布），法說會後一個交易日出清 |
| Target 1 | 338 TWD（Nomura 目標，Q2 後更新之共識） |
| Target 2 | 400 TWD（FY2027 EPS 16 TWD × P/E 25x） |
| Size | Small — 0.5% NAV（首批 0.25%，上限 1.5% 待驗證後放行） |
| Horizon | 1–3 個月（決策節點 2026-10-28），論點成立則延長至 12–18 個月 |
| Conviction | L（35%） |
| R:R to T1 | 無法計算（缺乏即時價格與技術止損位） |

未持有標的（不在 held_tickers.txt），走新倉框架。核准建倉，但對交易員原案做兩點修改：
(1) 0.5% 分兩批投入，法說會前僅動用 0.25%；(2) 以 fundamental stop 明確取代懸空的技術止損。

## Risk debate adjudication
- Aggressive's strongest point: 281 TWD 平均目標建立於 Q2 EPS 3.13 TWD（超預期 +47.71%）之前，Yuanta 370、Nomura 338 才是吸收新資訊後的參考。「現價高於共識」是用滯後數據反對，這個反駁成立。
- Conservative's strongest point: 止損位懸空。在 PRICE_DATA_UNAVAILABLE 下，倉位的最大損失無法量化；同時 CapEx 18B vs 2025 OCF 14.53B、股利 10.3B > FCF 7.59B，2026 FCF 趨零是可查證的實質壓力，非情緒。
- Net: 我採 neutral 為主。Aggressive 對「共識滯後」的判斷正確，但要求 1.5% NAV 外加認購權證，在沒有即時價格與隱含波動率報價的環境下是不可執行的建議。Conservative 的 250 TWD 硬性止損同樣以滯後數據管理當下風險，易誤觸。折衷：小倉位進場保留資訊價值，用論點紀律補上價格紀律的缺口。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 電源出貨落地 | Vera Rubin Power Shelf 進入量產 | 2026-08-24 微軟 Azure NVL72 110kW 量產部署，可查證 | 成立 |
| 獲利加速 | Q2 EPS 超越共識 | Q2 EPS 3.13 vs 估 2.12（+47.71%），毛利率 27.2% | 成立 |
| 現金流可支撐擴張 | OCF 隨獲利同步躍升，FCF 不轉負 | CapEx 18B vs 2025 OCF 14.53B，FCF/NI 僅 0.502，2026 FCF 可能趨零 | 觀察中 |
| 估值仍有空間 | 現價低於分析師目標 | 現價 308 高於舊均值 281，僅低於 Yuanta 370 / Nomura 338 | 觀察中 |

四根支柱中兩根成立、兩根觀察中、零根失效 → 允許建倉，但只給最小倉位。

## 論點失效條件
- 若 Q3 2026 EPS < 2.5 TWD（共識 2.97），獲利加速支柱失效 → 出場（法說會後一個交易日）
- 若 2026 全年 OCF 指引 < 20B TWD 且 CapEx 維持 18B 以上，現金流支柱失效 → 減碼至 0.25%
- 若月營收 YoY 增速連續兩個月低於 +20%（現為 +37.61%），出貨支柱失效 → 減碼至 0.25%
- 若任一主要 CSP 客戶公告 Vera Rubin 部署延後至 2027 Q1，出貨支柱失效 → 出場
- 若股利因 FCF 不足被縮減或暫停，現金流支柱失效 → 出場

## Upgrade conditions（加碼至 1.5% NAV，需同時滿足兩項）
1. Q3 EPS ≥ 3.0 TWD；2. 2026 OCF 指引 ≥ 25B TWD 或管理層給出 FY2027 EPS 指引 ≥ 14 TWD。

## Monitoring trigger
若 9 月與 10 月月營收（每月 10 日前公告）任一個月 YoY 跌破 +25%，不等 10/28 法說會，先減碼至 0.25%。另：取得即時價格後，立刻補設技術止損並重算 R:R；若 R:R to T1 < 1.5，退回 0.25%。

## Catalyst calendar
- 2026-09 中 — 高雄二期廠投產，AI 電源產能 +20–30%
- 2026-10-08 前後 — 9 月營收公告
- 2026-10-28 — Q3 2026 法說會（核心決策窗口：EPS、OCF、CapEx、Vera Rubin 出貨進度）
- 2026-Q4 — 越南廣寧廠投產、Vera Rubin 出貨高峰
- 2027-H1 — DenseLight CPO 初始營收

FINAL DECISION COMPLETE
