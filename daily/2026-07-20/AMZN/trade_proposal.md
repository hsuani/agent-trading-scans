# Trade proposal — AMZN as of 2026-07-20

FINAL TRANSACTION PROPOSAL: **BUY**

---

## Direction
LONG — conviction MEDIUM

---

## Setup

**無即時價格，暫不給進出場價位。**

market.md 回報 PRICE_DATA_UNAVAILABLE（Yahoo Finance 代理 HTTP 403）。entry zone、stop、target 均無法從即時市場數據計算，依 CRITICAL PRICE INTEGRITY RULE 不填入任何估算數字。

參考資訊（來自 investment_plan.md，非即時報價）：
- 分析師共識目標價 ~$313（距研究計劃撰寫時報價約 +29% 空間）
- TD Cowen 目標價 $340（2026-07-08 設定）
- AWS 增速門檻：Q2 ≥35% 為多頭確認；<30% 為論點失效
- FCF 門檻：季環比回升為最低要求

R:R：因無即時股價，無法計算。待價格資料恢復後重新評估進出場結構。

---

## Sizing

**財報前：Small（0.5% NAV）**
**財報後若達標：加碼至 Medium（1.5% NAV）**

理由：
- Conviction：MEDIUM，不支持建立超重倉位
- 二元事件風險：Q2 財報（2026-07-30）距今 10 天，AWS 增速是否達 35% 為高度不確定的單一事件；若低於 33% 將觸發分析師降評，潛在下行顯著
- ATR 及波動率：無法取得（市場數據不可用），但 AMZN Beta 歷史偏高，大型科技財報前後隱含波動率通常大幅擴張，進一步壓縮財報前持倉合理性
- Anthropic 一次性帳面收益（$16.8B）已導致 EPS 高估逾 40%，盈利品質失真增加估值不確定性
- 投資計劃明確建議「財報前縮減倉位，財報後依結果決定加碼」

---

## Time horizon

**近期觸媒：1-4w**（Q2 財報結果為進一步佈局的決策點）
**中期主線：1-3m**（AWS AI 加速動能、FCF 回升趨勢需 2-3 季驗證）
**長期選擇性持有：3m+**（Trainium 第三方商業化、世芯-KY 量產、Anthropic 生態擴張屬 4-8 季回報週期）

---

## Trigger

**財報前：等待觀察（Wait for earnings）**
建議在 Q2 財報（2026-07-30）公布後，依以下條件決定倉位規模：

| 條件 | 動作 |
|---|---|
| AWS 增速 ≥35% 且 FCF 季環比回升 | 從 Small 加碼至 Medium（1.5% NAV） |
| AWS 增速 35%-30% 之間，FCF 持平 | 維持 Small（0.5%），觀察下季 |
| AWS 增速 <30% 或 FCF 繼續壓縮 | 平倉，降為 NEUTRAL |

若財報前出現明確技術突破確認（需價格資料恢復後評估），可考慮在財報前以 Small 規模建倉，但 10 天內財報帶來的二元風險應審慎評估持倉成本。

---

## Invalidation

以下任一條件成立即終止多頭論點：

1. **Q2 AWS 增速 <30%**：顯示加速動能逆轉，多頭核心數據失效
2. **FCF 繼續壓縮或單季持平**：$200B 資本支出的回本壓力進一步惡化，FCF 回升論點崩塌
3. **FTC 或 CMA 對 Anthropic 投資發出正式禁令或強制分拆要求**：同時失去 $70B 帳面估值、$100B AWS 消費承諾及差異化 AI 合作，潛在單日重估 -15% 至 -20%
4. **管理層下調全年資本支出指引後 AWS 增速仍不達標**：顯示投資縮減且成長未兌現，雙重負面信號

---

## Catalyst calendar

| 日期 | 事件 |
|---|---|
| 2026-07-30 | Q2 2026 財報發布（核心數據：AWS 增速門檻 35%、FCF 季環比方向、管理層全年 CapEx 指引） |
| 財報後持續監控 | Anthropic FTC/CMA 監管調查進展（任何正式行動為重大負面催化劑） |
| 2027H1（預期） | 世芯-KY Trainium 晶片量產交付，驗證自研晶片生態長期競爭力 |
| 持續 | Trainium 直售第三方資料中心談判結果（一旦落定，為 AWS 護城河重要確認） |

---

> **補充說明**：本提案因市場數據不可用，所有具體進出場價格均依 CRITICAL PRICE INTEGRITY RULE 省略。建議在 Yahoo Finance 代理連線恢復後，補充執行技術分析（支撐/阻力位、ATR、RSI14、MACD），以完整計算 R:R 並確認進場區間。在此之前，方向性判斷（LONG MEDIUM conviction）與倉位管理架構（財報前 Small、財報後視結果加碼）已具備可執行性。

---

TRADE PROPOSAL COMPLETE
