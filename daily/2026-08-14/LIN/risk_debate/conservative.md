# Conservative risk view — LIN

## Where trader is too aggressive

- **定價數據全面缺失，倉位卻仍設 1.5% NAV**：所有技術欄位（Entry、Stop、Target、R:R、ATR）標記為 PRICE_DATA_UNAVAILABLE。沒有即時報價就無法計算 vol-adjusted stop，等同在黑箱中開倉。在數據恢復前，任何大於 0.5% NAV 的部位都屬不負責任的倉位管理。
- **Stop 寬度隱性過大**：交易計劃以 $389 作為熊方目標（22x P/E 情境），對估計入場約 $430–440 而言代表約 **-10 至 -12% 下行幅度**。若以年化波動率 ~20% 換算，2x ATR 止損約 $9–10，即正確 vol-adjusted stop 比敘事性止損**窄 5 倍以上**。以更寬的 $51 止損進場，需大幅縮小倉位才符合風險紀律。
- **五大投行同步下調目標價**（UBS、Citi、Goldman、RBC、BMO），顯示賣方對 Q2 EPS 僅差 $0.03 便引發 -5-6% 股價反應高度敏感——市場已對 26–28x P/E 失去容錯彈性，多重壓縮風險被低估。
- **Lead Independent Director 淨賣出 $5.7M（減持自身持股 36%）**，12 個月無任何對沖買入。內部人士信號被歸為「謹慎」，但對高估值股票而言，這類信號應觸發倉位縮減而非維持。

## Tail scenarios

- **Scenario A（機率約 15%）：Fed 意外升息 50 bps（通膨復燃）**→ 成長股估值壓縮，LIN 從 27x 跌至 22x P/E → 股價約 $389，對 $435 入場損失約 $46/股 → 1.5% NAV 倉位損失 ≈ **0.16% NAV**（可承受，但在 PRICE_DATA_UNAVAILABLE 環境下無法動態控損）
- **Scenario B（機率約 20%）：Lincare 剝離延誤至 2027 年或以低價強迫出售**→ Americas margin 拖累延伸、市場重新定價，股價跌至 $400–410 區間，短期損失 $25–35/股
- **Scenario C（機率約 12%）：Q3 2026 EPS 跌破 $4.45 + capex 再次上修超過 $6.0B**→ 管理層公信力下滑，機構進一步降評，股價測試 $390 甚至更低
- **Scenario D（機率約 10%）：宏觀工業需求驟降（有機成長跌至 <5%）**→ 高 capex 背景下 FCF/NI 跌破 0.80，成長故事全面動搖，目標倍數壓縮至 20x，股價約 $354–360

## Recommended adjustments

- **Size**：1.5% NAV → **0.5–0.75% NAV**（理由：PRICE_DATA_UNAVAILABLE 使 ATR 無從計算；Lead Independent Director 大幅減持；Q2 miss 後市場對估值敏感度已升高；0.5% 上限在 Scenario A/C 下損失控制於 0.05–0.06% NAV）
- **Stop**：待價格恢復後，以 **2x ATR（估計 $9–11）** 設定機械止損，而非以 $389 熊方情境作為隱性止損——當前設定等同接受 11% 回撤才出場
- **Entry**：縮至 **0.5% NAV 先行建倉**，確認 Lincare 剝離 8-K 申報或 Q3 Americas margin ≥30% 後，方可加碼至 0.75%；不建議在未取得即時報價前觸及第二批
- **Consider**：以 **XLB 或 Air Liquide（LQADF）sector put** 作為部分對沖，或買入距到期約 3 個月的 LIN OTM put（Delta -0.20 至 -0.25），覆蓋 Scenario B/C 尾部風險

## Position-level $ risk

假設 NAV = $1,000,000；估計入場 $435；估計 ATR stop $10（2x ATR）：
- **0.5% NAV 倉位**：$5,000 ÷ $435 ≈ **11 股**；若 stop 命中，損失 = 11 × $10 = **$110 = 0.011% NAV** → 可接受
- **1.5% NAV 倉位（原案）**：$15,000 ÷ $435 ≈ 34 股；若以 $389 熊方止損，損失 = 34 × $46 = **$1,564 = 0.156% NAV** → 表面可接受，但在無即時報價環境下，止損觸發時機完全取決於主觀判斷，紀律風險極高

**結論：0.156% NAV 的絕對損失雖不大，但在 PRICE_DATA_UNAVAILABLE 條件下，缺乏動態控損機制使實際損失路徑無法監控——這才是核心風險。**

## What I'd push for

立即將第一批倉位上限硬設為 **0.5% NAV**，明確要求 Yahoo Finance 即時報價恢復後才能計算 ATR 並設定機械止損。Lincare 剝離正式完成（8-K 公告）及 Q3 Americas margin 回升 ≥30% **兩項條件同時達成**後，方可考慮加碼至 0.75%；1.5% NAV 的滿倉目標在 Lead Independent Director 減持信號未消化、capex 軌跡未確認之前暫不列入計劃。若 Q3 EPS 跌破 $4.45，立即全部撤倉，無需等待進一步確認。

CONSERVATIVE VIEW COMPLETE
