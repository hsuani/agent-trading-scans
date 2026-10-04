# Watchlist digest — tw_unassigned as of 2026-10-05

來源說明: 這兩檔標的目前無 ≥3 家可比同業,僅掛 theme tag 走 `tw_unassigned` 排程桶,今天一起出現純粹是排程巧合,彼此之間**不是同業**。8021.TW 完整跑完 Phase 2-4;6438.TW 在 Phase 1 positive-pick 篩選即未達門檻,停在 Phase-1 stub。

本表**不排名**,標的之間不是同業。

| Ticker | 入選原因 / 訊號 | 我方結論 | Conviction | 關鍵催化劑 | 關鍵風險 | 既有 primary group |
|--------|----------------|----------|-----------|-----------|---------|-------------------|
| 8021.TW | theme: pcb_consumables；positive-pick 通過進入 Phase 2-4 | HOLD (Verdict: REJECT,新倉不進場) | N/A (REJECT,未給倉位) | 9 月營收 YoY (10月中)、Q3 法說會 (11月中下旬) | Forward EPS 18.65 元未經驗證、RSI14 73.93 超買、應收/存貨/負債增速遠超營收 | none / unassigned |
| 6438.TW | theme: automation_equipment；positive-pick 2/5 訊號,未達 ≥3 門檻,停在 Phase-1 | 無評等 (未進入 Phase 2-4,無進出場建議) | N/A | 待 Q3/Q4 營運現金流轉正或毛利率回升至 25% 以上 | FCF/NI ≈ -1.51 (現金流品質惡化)、RSI14 72.09 超買、無分析師覆蓋、機構持股僅 1.775% | none / unassigned |

## 逐檔摘要

### 8021.TW (尖點)
- 為何入選: theme tag `pcb_consumables`,positive-pick 評分通過,進入完整 Phase 2-4 風控辯論流程。
- 我方 final_decision 要點: FINAL TRANSACTION PROPOSAL = HOLD,Verdict = REJECT。現價 $553 不進場,R:R 僅約 0.8 (到 T1 $623 為 +12.7%,收斂停損 $465 為 -15.9%),低於進場門檻。Dealbreaker 包括:Forward EPS 18.65 元 (對應 Forward P/E 29.65x) 與 H1 實際 EPS 3.25 元、Q2 年化約 8.3 元差距逾一倍,尚無 Q3 數據驗證;應收 +34%、存貨 +59%、總負債 +74% QoQ 均遠超營收 +80%;技術面 RSI14 73.93、BB %B 1.21、高於 MA200 55.2%。重訪條件(任一達成可轉 LONG MEDIUM):數據路徑為 9 月營收 YoY≥80% 且 Q3 單季 EPS≥2.8 元、毛利率≥40%、應收周轉天數下降、營運現金流轉正(可在 $465–520 以 ≤1/3 標準部位試單,停損 $465);價格路徑為股價回落 $410–465 支撐區且月營收 YoY 未跌破 50%、毛利率未破 37%(可用 ≤1/4 標準部位,停損 $400)。數字均照抄 final_decision.md,未重算。
- primary group: 目前為 none / unassigned (universe.py --group 8021.TW → unassigned)。歷史上 v1 分類 `tw_pkg` 曾將其與 3661.TW、6438.TW 併列,但該分組已凍結僅供舊 outcome cohort 回溯,非現行 primary group,此處僅加旗標,不重跑同業比較。

### 6438.TW (迅得)
- 為何入選: theme tag `automation_equipment`,但 positive-pick 5 項訊號僅通過 2 項 (News 情緒正向、TTM P/E 29.2x<35x),未達 ≥3 門檻,故停在 Phase-1,未進入 Phase 2-4 完整分析。
- 我方 final_decision 要點: 無即時進出場建議,暫不給進出場價位。未過原因:Fundamentals 項 FCF/NI ≈ -1.51 (2025 營收 +26.3% YoY 但淨利 -26.0%,FCF 轉負 -646.4M,低於 -1 門檻);Market 項 RSI14 72.09 超買 (略超 72 門檻),雖 MACD 正值、價格站上 MA50;Sentiment 項無分析師覆蓋 (DATA_UNAVAILABLE)、機構持股僅 1.775%。毛利率三年連跌至 23.46%,存貨激增 35.1% 與營收成長不匹配,暗示去化壓力。維持 Phase-1 觀察名單,待 Q3/Q4 營運現金流轉正或毛利率回升至 25% 以上後重新評估。數字均照抄 final_decision.md,未重算。
- primary group: 目前為 none / unassigned (universe.py --group 6438.TW → unassigned)。同上,v1 `tw_pkg` 分組已凍結非現行分類,此處僅加旗標,不重跑同業比較。

## 觀察
- 兩檔同屬 PCB/面板製程上游供應鏈(鑽針耗材 vs. 自動化設備),對台灣 PCB 產業景氣(含 AI PCB 擴產周期)有共同曝險,但缺乏直接可比的財務結構,不構成同業比較基礎。
- 兩檔技術面同步出現超買訊號 (8021.TW RSI14 73.93、6438.TW RSI14 72.09),屬巧合疊加而非共同基本面訊號,仍需留意短期均值回歸風險各自獨立評估。
- 資料缺口待人工確認:8021.TW 的 Q3 應收/存貨/現金流數據尚未揭露;6438.TW 無分析師覆蓋,Forward EPS 12.94 元可信度未經交叉驗證,僅憑公司單方預估。

WATCHLIST DIGEST COMPLETE
