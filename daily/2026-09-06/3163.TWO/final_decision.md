FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — 3163.TWO as of 2026-09-06

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

> **價格資料警示**：市場狀態為 PRICE_DATA_UNAVAILABLE（TPEx 連線受阻、Yahoo Finance HTTP 403）。本文所有價位、P/E、ATR 均為**推算值（DERIVED，非直接觀測）**。執行前必須以實際報價重新校準；若無法取得報價，一律不下單。

**倉位判定**：3163.TWO 不在 `held_tickers.txt` → 新倉框架。目前部位 0% NAV，今日**不建倉**，故第一行為 HOLD（無動作），並非續抱。

## Final trade card (if not REJECT)
本卡為**條件式**，僅在下方 Monitoring trigger 的觸發條件 ① 成立後生效；未觸發前部位為 0% NAV。

| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $740 – $780（DERIVED，GTC 確認後次一交易日市價）|
| Stop | $680（DERIVED）|
| Target 1 | $900（DERIVED；$826 分析師牛市目標處先減 1/3）|
| Target 2 | $1,000（DERIVED，需 Q4 月千套量產兌現）|
| Size | Small（0.2% NAV）|
| Horizon | 6–8 週（至 2026-10 Q3 財報）|
| Conviction | L |
| R:R to T1 | 1.75 |

## Risk debate adjudication
- Aggressive's strongest point：NVDA GTC（9/16）是時限明確的二元催化劑，資訊優勢窗口當日關閉；若現場確認波若威 CPO 量產里程碑，NT$620 回落窗口將永久關閉，屆時被迫以更差 R:R 追高。催化劑缺席成本是真實成本。
- Conservative's strongest point：在全部財務數據 DATA_UNAVAILABLE、股價為推算值的前提下，財報跳空可讓實際損失達計畫 Stop 的 2 倍以上，Stop 形同虛設。P/E 75.6x（回落至 NT$620 仍 61.7x）對被動光纖元件供應商毫無安全邊際。
- Net：我採用 **neutral** 的分支架構。理由是兩方論點並不互斥而是分屬不同時序——GTC 前期權價值未定價（Aggressive 對），GTC 沉默後高 P/E 風險重新主導（Conservative 對）。但我對 Conservative 的「NT$400 以下才進場」不採納：該價位隱含 NVIDIA 認證關係完全崩解，屆時論點本身已不存在。以 0.2% NAV 而非 0.5% 控制尾端，是對跳空風險的實質讓步。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| CPO 產業週期與 NVIDIA 認證壁壘 | 認證週期 12-18 個月構成先行者護城河 | TSMC COUPE 2026H2 量產、NVIDIA 竹北驗證實驗室，事件有具體來源 | 成立 |
| H2 EPS 後端加載 | H2 需貢獻 EPS ≈ NT$6.50 支撐 P/E 75.6x | Q2 EPS NT$0.47（QoQ -84.5%），H1 僅 NT$3.50 | 觀察中（偏弱）|
| 營收動能加速 | 量產爬坡應推升月營收 YoY | YTD 年增率由 +24.4%(1-5月) 降至 +19.0%(1-7月)；7 月單月 +28.65% 為唯一反證 | 觀察中 |
| 定價權／毛利率天花板 | CPO 供應鏈溢價 | FAU、光纖套件屬被動端，毛利率估 35-45%，遠低於光聖 ~60% | 已失效（結構性上限，非可改善項）|

## 論點失效條件
- 若 Q3 2026 單季 EPS < NT$3.0，「H2 後端加載」支柱失效 → 取消進場計畫；若已持試探倉，**出場**。
- 若 8 月與 9 月月營收 YoY 連續兩個月 < 20%，「營收動能」支柱失效 → 全面取消計畫（含加碼路徑）。
- 若公司或供應鏈確認 CPO 量產驗證延至 2027Q1 以後，「產業週期時序」支柱失效 → **出場**。
- 若股價在無 EPS 兌現下續漲至 P/E ≥ 85x，安全邊際歸零 → 不追、已有部位減碼。

## Monitoring trigger
① **NVDA GTC 2026（9/16）現場確認波若威 CPO 量產里程碑** → 次一交易日以市價建 0.2% NAV 試探倉，Stop NT$680。
② **GTC 未提及波若威／CPO 進度** → 維持 0% NAV，改等推算 NT$620 回落**且** Q3 EPS ≥ NT$3.0 雙重條件，屆時另立新卡。
③ 任一分支下，若 TPEx 實際報價恢復後與推算價偏離 >10%，本卡作廢重算。

## Catalyst calendar
- 2026-09-16 — NVDA GTC 2026（CPO 進度，主要觸發點）
- 2026-09 底前 — 8 月及 9 月月營收公告
- 2026-10 中旬 — Q3 2026 財報（關鍵 EPS 驗證窗口）
- 2026-11 — NVDA Computex（Spectrum-X 下一代路線圖）

FINAL DECISION COMPLETE
