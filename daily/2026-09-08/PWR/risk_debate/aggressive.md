# Aggressive risk view — PWR

## Where trader is too cautious

- **AVOID = 主動放棄一個有明確觸發日期的不對稱機會**。Q3 財報定於 2026-10-29，距今約 7 週，催化劑時間表清晰。空等觀望的代價是錯過在隱含波動率尚未因財報接近而大幅上升前建立空方部位的視窗。
- 計畫以「95.28% 機構持倉＝軋空風險」為由迴避空方，邏輯只對**直接融券空股**成立。買入 put options 是定義風險的替代路徑：最大虧損鎖定於 premium，不存在軋空問題。
- CEO Earl Austin 26 次賣出、0 次買入、單月套現 $120.2M，這不是一個可以用「計畫性財務規劃」解釋的數字。連續兩季 GAAP EPS 錯失（Q1 -28.6%、Q2 -10.6%），若 Q3 三度錯失，42.6x Forward P/E 將面臨教科書式倍數壓縮。計畫選擇觀望，但這一結構恰好是空方 options 存在的理由。

## Recommended adjustments

- **Size**：0% NAV → Small（0.5%–1.0% NAV 用於 put premium，固定風險上限）
- **Stop**：Put options 本身即為內建 stop——最大虧損 = 所付 premium，無需另設停損價位
- **Entry**：即時確認報價後立即建立，不等待。財報前 IV 只會上升，越晚進場 premium 越貴
- **Consider**：OTM put spread（例如履約價區間為當前股價 -10% / -25%），到期日選 **2026-11-06**（Q3 財報公告後一週），捕捉財報後即時反應

## Asymmetry argument

PRICE_DATA_UNAVAILABLE，以估值框架推算：

| 情境 | 結果 |
|------|------|
| 最壞情況（Q3 GAAP 超越，put 歸零） | -0.5% to -1.0% NAV（premium 全損） |
| 基本空方情境（Forward P/E 42.6x → 30x） | 股價約 -30%，put spread 獲利 2x–3x premium |
| 完整壓縮情境（Forward P/E 42.6x → 同業 20x） | 股價約 -40%，put spread 獲利 4x–6x premium |

**B/A ratio 約 4:1 至 6:1**，風險完全定義。

## What I'd push for

取得即時報價後，以 **0.5%–1.0% NAV** 買入略微虛值 put（delta 約 -0.30），同步賣出更低履約價 put 降低成本，組成 put spread，到期 **2026-11-06**。催化劑明確（Q3 GAAP EPS 品質）、時間窗口有限（7 週）、最大虧損封頂。這不是賭反轉，而是為一個以「倍數壓縮」為核心、由 CEO 大量拋售背書的概率事件支付合理 insurance premium。AVOID 的判斷在無 options 框架下正確，但若組合允許使用衍生品，此 put spread 結構將不對稱轉化為可執行機會。

AGGRESSIVE VIEW COMPLETE
