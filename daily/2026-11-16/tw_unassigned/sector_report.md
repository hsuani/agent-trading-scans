# Watchlist digest — tw_unassigned as of 2026-11-16

來源說明: 此 2 檔並非 Serenity 訊號,而是 `tw_unassigned` 排程 bucket 今日依週排程（isoweekday 1）出現的標的 —— 兩者皆因尚無 ≥3 家真實同業可比,僅被標記 theme tag（8021.TW: pcb_consumables；6438.TW: automation_equipment）,未進入任何 primary peer group。
本表**不排名**,標的之間不是同業,也不互為可比較對象。

| Ticker | 入選原因 / 訊號 | 我方結論 | Conviction | 關鍵催化劑 | 關鍵風險 | 既有 primary group |
|--------|----------------|----------|-----------|-----------|---------|-------------------|
| 8021.TW | tw_unassigned 排程, theme=pcb_consumables；Phase-1 positive-pick 篩選僅 2/5 訊號過關(門檻≥3),未進入完整辯論 | HOLD（Phase-1-only stub,非 positive pick） | N/A（未產出,未達門檻即終止分析） | 自由現金流轉正、資本支出增速趨緩、股價站回 MA50 (~$457) 並帶量、yfinance 分析師/法人資料恢復可用且偏多 | TTM FCF/NI 約 -1.63；有息負債 9 個月內 +168%；價格 $385 < MA50 $457.03；分析師與法人資金流數據因 yfinance 取數失敗無法驗證 | none（theme tag: pcb_consumables） |
| 6438.TW | tw_unassigned 排程, theme=automation_equipment；完整走過 Phase 1-4,風險委員會裁決 REJECT | HOLD / REJECT（0% NAV,不建新倉） | LOW（NEUTRAL） | Q3'26 財報入庫（毛利率、EPS、OCF、有息負債,法定應已公告但未入快取）；2026-12-10 11 月營收公告(基期 5.70 億 TWD)；2026-12-10 除息 3.00 TWD；5 億 TWD 可轉債募集結果與轉換價 | TTM FCF 約 -5.29 億 TWD；過去四季 EPS 全數未達共識；價格位於 MA20(152.43)/MA50(156.15)/MA200(157.22) 之下,空頭排列、死亡交叉；ATR14 達 5.6%,日均成交額僅約 1.3 億 TWD,流動性薄;可轉債潛在稀釋 ~4.3% | none（theme tag: automation_equipment） |

## 逐檔摘要

### 8021.TW（尖點）
- 為何入選: tw_unassigned 排程標的,theme tag 為 pcb_consumables（PCB 鑽針耗材）,今日非 Serenity 訊號。
- 我方 final_decision 要點: Phase-1 positive-pick 訊號評分僅 2/5 過關（Fundamentals FAIL、Market FAIL、News PASS、Sentiment FAIL、Valuation PASS）,未達≥3 門檻,因此**未進入** Phase 2-4 的 Bull/Bear 辯論、交易員規劃與風險委員會,無交易計畫、無進場/失效條件可抄錄。監控觸發：若 FCF 轉正或資本支出增速趨緩,且 yfinance 分析師/法人資料恢復並確認偏多,或股價站回 MA50 (~$457) 並帶量,可重新評估。
- 若已在 primary group: 目前不在任何 PEER_GROUPS,`universe.py --group 8021.TW` 回報 unassigned；注意舊版(v1) taxonomy 曾將其與 3661.TW、6438.TW 同列 `tw_pkg`,但該分類已於 v2 拆分且為歷史凍結,不代表現行同業關係,此處僅加 theme flag,不重跑同業比較。

### 6438.TW（迅得機械）
- 為何入選: tw_unassigned 排程標的,theme tag 為 automation_equipment（自動化設備）,今日非 Serenity 訊號。
- 我方 final_decision 要點: 最終提案 HOLD／裁決 REJECT,0% NAV,不建新倉（新倉適用 A 框架,非既有持股續抱）。Dealbreaker 為 Q3'26 財報法定應已公告但未入工具快取,investment_plan 三個 crux 全繫於此；風險委員會採信 conservative/neutral 一方：aggressive 提出以 143 進場、137 停損、對 167 名目 R:R 約 4.0,但因 ATR14 5.6%、日均成交額僅約 1.3 億 TWD,實際停損恐無法保證成交,實質風險應以 126（約 -11.9%）計算,故不採用。四根做多論點支柱中僅「營收動能」成立,獲利品質、現金流轉折、技術結構皆仍「觀察中」,不足以支撐新倉。失效條件與重啟條件均已於 final_decision.md 列出數字(毛利率 ≥26%／EPS ≥2.3 TWD／OCF 轉正／站回 152 等),未重算。
- 若已在 primary group: 目前不在任何 PEER_GROUPS,`universe.py --group 6438.TW` 回報 unassigned；同上,v1 `tw_pkg` 分類已廢止,此處僅加 theme flag,不重跑同業比較。

## 觀察
- 兩檔無共同宏觀敘事曝險：8021.TW 的獲利動能與 6438.TW 的自動化設備需求來自不同終端應用,僅因同屬 tw_unassigned 排程 bucket 而同日出現,不構成同業或主題關聯。
- 共同資料缺口：8021.TW 的 yfinance 分析師/法人資金流資料持續取數失敗；6438.TW 的 Q3'26 財報雖法定應已公告但尚未入庫,兩者皆需人工確認資料來源是否恢復/補齊,才能重新評估。

WATCHLIST DIGEST COMPLETE
