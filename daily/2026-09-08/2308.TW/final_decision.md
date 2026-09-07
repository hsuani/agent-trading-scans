FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — 2308.TW as of 2026-09-08

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## 倉位判定
- **新倉判定**：2308.TW 不在 `held_tickers.txt` 內，屬新倉評估，問題是「該不該進」而非「該不該續抱」。
- **Conviction**：25%（LOW）
- **Position size**：0% NAV（不建倉，現時風險敞口為零）
- **Entry / Stop / Target**：**無即時價格，暫不給進出場價位**（PRICE_DATA_UNAVAILABLE，Yahoo Finance HTTP 403；最近參考價 1,710 TWD 為 2026-08-26 收盤，距基準日 13 天，不可作為執行價）
- **Horizon**：3m+，最早重評時點為 2026 年 10 月 Q3 法說會

## Dealbreaker（為何 REJECT）
兩項硬條件同時不成立，任一項單獨都足以否決建倉：

1. **估值無安全邊際**：Trailing P/E 73.9x、EV/EBITDA 37.0x、P/FCF 86.6x；即使採最樂觀 FY2026E EPS 42 TWD，Forward P/E 仍達 43-48x，相對台積電 25-30x 溢價 50-90%。Phase 1 五訊號中 Valuation 為唯一 FAIL，且正是決定進場點的那一項。
2. **無價格數據 = 無停損錨點**：缺 ATR、缺技術支撐確認，任何倉位（含 0.5% NAV）都無法定義下行止血點。這是操作層面的硬性封鎖，不是註腳。

Fundamentals / News / Sentiment 三項 PASS 說明這是一家好公司，但好公司不等於好價格。

## Risk debate adjudication
- **Aggressive 最強論點**：FCF 壓縮應區分週期性與結構性。70B TWD Capex 是高訂單能見度驅動的前置投資，德州、泰國新廠 2027-2028 投產後 Capex 正常化，FCF 可望回升；以 2026 單一年度 FCF/NI 85% 線性外推為永久損傷確實過度悲觀。AR 78 天對 Hyperscaler 級客戶亦非信用風險。
- **Conservative 最強論點**：估值已隱含未來五年完美執行，毫無安全邊際；且在 PRICE_DATA_UNAVAILABLE 下無法執行任何停損紀律。
- **Net**：我採 **neutral** 的裁定。Aggressive 的基本面反駁部分成立，但其結論（現在建 1.0% NAV，甚至 ATM call）依賴一個不存在的前提——可執行的停損與可驗證的期權定價。無報價環境下談 options premium 是紙上方案。Conservative 對情境 D（AR 壞帳、機率 10%）明顯高估，但核心判斷正確。中性方的三條件框架最貼合現實。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 電源獲利加速 | H2 > H1，EPS 續增 | H1 2026 EPS 17.59 TWD、Q2 +89% YoY | 成立 |
| 毛利率結構性改善 | 維持 ≥ 36% | Q1 2026 達 37% 歷史新高，但 Vertiv/Eaton 800VDC 已上市 | 觀察中 |
| 現金流品質 | FCF/NI ≥ 80% | 128%→107%→85% 三年連跌，2026 Capex 70B 恐壓至 30% 區間 | 已失效 |
| 估值可承受 | Forward P/E ≤ 35x | 實際 43-48x | 已失效 |

## 論點失效條件
與 Stop 分離；此處為論點紀律。
- 若 2026 年 H2 任一單月營收 YoY < 30%，成長敘事支柱失效 → 永久排除，不再列入觀察。
- 若 Q3 2026 法說會揭露毛利率 < 34%，毛利率支柱失效 → 排除。
- 若 Q3 2026 累計 FCF/NI < 80%，現金流支柱維持失效 → 進場門檻由 Forward P/E ≤ 35x 下修至 ≤ 28x。
- 若任一 Hyperscaler 公開下修 2027 Capex 指引，AI 需求支柱失效 → 排除並評估反向。

## 重啟進場條件（三項須同時成立）
① 價格數據源恢復、可算 ATR 與支撐；② 市價對應 Forward P/E ≤ 35x（FY2026E EPS 40 TWD 計，約 ≤ 1,400 TWD）；③ Q3 2026 累計 FCF/NI ≥ 80% 且 EPS > 9.68 TWD。三項齊備方建 Small 0.5% NAV，上限不得越級至 Medium。

## Monitoring trigger
若 9 月或 10 月月營收 YoY 跌破 35%（目前基準 42%），視為情境 A 早期訊號，提前將本標的降級為永久排除，不必等 Q3 法說會。

## Catalyst calendar
- 2026-09 中旬 — 8 月月營收公告，監控 YoY ≥ 42%
- 2026-10 — Q3 2026 法說會：EPS、FCF 指引、Capex 進度（核心重評點）
- 2026-10 起 — 台灣能源署 PUE ≤ 1.3 法規落地進度
- 2026-Q4 — 德州、泰國新廠投產時程更新
- 隨時 — Hyperscaler 2027 Capex 指引修訂；價格數據源恢復

## 相關性提醒
投組已持有 ANET、MOD、COHR、3017.TW 等 AI 基礎設施與散熱標的，2308.TW 的主題曝險已隱性存在。即便未來三條件滿足，建倉前須先扣除此重疊，避免同向集中。

FINAL DECISION COMPLETE
