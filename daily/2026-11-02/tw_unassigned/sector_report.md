# Watchlist digest — tw_unassigned as of 2026-11-02

來源說明: 這兩檔標的來自 tw_unassigned 未分組清單(台股週一排程),目前尚未有 ≥3 檔真實同業可比,僅各自帶 theme tag(8021.TW: pcb_consumables；6438.TW: automation_equipment)。兩者曾共用舊版 v1 的 `tw_pkg` 分組,但該分組已於 1A 拆分、不再重跑同業比較。
本表**不排名**,標的之間不是同業。

| Ticker | 入選原因 / 訊號 | 我方結論 | Conviction | 關鍵催化劑 | 關鍵風險 | 既有 primary group |
|--------|----------------|----------|-----------|-----------|---------|-------------------|
| 8021.TW | 台股未分組排程(pcb_consumables theme) | HOLD（REJECT 新倉，0% NAV） | MEDIUM（偏多觀察） | 11/10 前 10 月營收；11/14 前 Q3 財報（EPS、毛利率、存貨天數） | 停損落點不可執行（$388 小於 1倍ATR、$373.5 偏寬）；48x P/E 下財報前提前押注等於用部位換「不被跳空甩掉」的恐懼 | none（舊 v1 tw_pkg，已拆分不重跑） |
| 6438.TW | 台股未分組排程(automation_equipment theme) | HOLD（Phase-1-only stub，未進完整辯論） | N/A（1/5 訊號，門檻 3/5，未達 positive-pick 標準） | 約 11/10 前 10 月營收；約 11/14 前 Q3 財報；站回 MA50（NT$157.35） | 營收 YoY +11.8% 低於 15% 門檻、FY2025 FCF/NI 為 -1.52、價格 $155.00 低於 MA50 $157.35、分析師與機構覆蓋極低（僅 2 位分析師、機構持股 1.59%） | none（舊 v1 tw_pkg，已拆分不重跑） |

## 逐檔摘要

### 8021.TW（尖點）
- 為何入選: 台股 tw_unassigned 週一排程標的,PCB 鑽針耗材主題,目前無 ≥3 家真實同業可比,僅作 theme tag 追蹤。
- 我方 final_decision 要點: FINAL TRANSACTION PROPOSAL = HOLD,Verdict = REJECT,不建立新部位(0% NAV)。Dealbreaker 三點:(1)價格 $418.50 低於 MA20(-17.2%)與 MA50(-10.1%),MACD 柱狀體 -14.62 仍擴大,RSI 34.9 未超賣,R:R 到 T1 僅約 1.1,不值得在 20 日年化波動率 69% 的個股上承擔；(2)兩個候選停損 $388(小於 1倍 ATR $32.59,雜訊停損)與 $373.5(距現價 10.8%,財報跳空環境滑價更大)都不可執行；(3)11/10 前 10 月營收、11/14 前 Q3 財報將在兩週內自然裁定方向,財報前搶倉等於用部位換「不被跳空甩掉」的恐懼。重訪轉 LONG 條件需 Q3 EPS ≥2.8 TWD 且毛利率 ≥40%、10 月營收 ≥8 億 TWD,且單日站回 MA50(約 $465)並量能放大 1.5 倍以上。
- 已在 primary group: 目前 primary_group() 回傳 none；舊版 v1 的 `tw_pkg`(與 3661.TW、6438.TW 共組)已於 1A 拆分,不再重跑同業比較,此處僅加旗標。

### 6438.TW（迅得）
- 為何入選: 台股 tw_unassigned 週一排程標的,自動化設備主題,目前無 ≥3 家真實同業可比,僅作 theme tag 追蹤。
- 我方 final_decision 要點: FINAL TRANSACTION PROPOSAL = HOLD,Verdict = Phase-1-only stub(非 positive pick,未進入 Phase 2-4 完整辯論)。Phase-1 訊號評分 1/5(門檻 ≥3/5):Fundamentals FAIL(營收 YoY +11.8%,低於 15% 門檻；FY2025 FCF/NI -1.52,低於 -1)、Market FAIL(RSI14=41.28 過關但價格 NT$155.00 低於 MA50 NT$157.35 未過)、News FAIL(方向不明的 mixed)、Sentiment FAIL(僅 2 位分析師覆蓋、機構持股僅 1.59%,樣本不具代表性)、Valuation PASS(Forward P/E 12.7x < 35x,但分析師覆蓋過低,可信度低)。因整體遠低於門檻,未進入 Bull/Bear 辯論、交易員規劃與風險委員會。監控觸發:約 11/10 10 月營收與約 11/14 前 Q3 財報若營收 YoY 回升至 15% 以上且 FCF 轉正,或股價站回並守住 MA50(NT$157.35),或分析師/機構覆蓋擴大,訊號可能轉強。
- 已在 primary group: 目前 primary_group() 回傳 none；舊版 v1 的 `tw_pkg`(與 3661.TW、8021.TW 共組)已於 1A 拆分,不再重跑同業比較,此處僅加旗標。

## 觀察
- 共同曝險: 兩者皆屬台股未分組(theme tag only)、皆面臨 11/10 前 10 月營收與 11/14 前 Q3 財報兩個近期催化時點,但基本面與產業鏈位置完全不同(鑽針耗材 vs. 自動化設備),不構成共同敘事,僅為排程巧合。
- 資料缺口: 6438.TW 因未達 positive-pick 門檻,無 investment_plan.md(Phase 2-4 未執行),本摘要僅能依 final_decision.md 的 Phase-1 評分呈現,無法提供 Bull/Bear 辯論或交易卡細節,需待下次重新評估時人工確認。
- 兩檔皆列於舊版 v1 `tw_pkg` 分組歷史下,但該分組已拆分,目前查無 ≥3 家可比同業,未來若找到足夠 comparables 應個別建立新 primary group,而非沿用舊 `tw_pkg`。

WATCHLIST DIGEST COMPLETE
