# Conservative risk view — WDC

## Where trader is too aggressive

- **即便 0.5% NAV 的 put spread 在當前環境下仍是過激**。PRICE_DATA_UNAVAILABLE 意味著無法確認當前股價，也無法選定合理 strike，更無法計算 delta、gamma 或實際 premium 支出。在無法定義進場成本的條件下開立任何部位，違反基本風控紀律。
- **月跌 -33% 後做空時機風險極高**。空頭最易受傷的時點，往往是一波急跌之後——軋空反彈（short squeeze）或技術性反彈最常發生在恐慌性殺盤甫結束時。此時買 put spread 等同於高隱波（IV 已大幅抬升）下付出高 premium，賠率惡化。
- **Theta 衰減是 put spread 的隱性對手**。若反彈先於進一步下跌，spread 每日吃損 theta；1–3 個月的操作窗口中，若走勢橫盤或小幅反彈 10–15%，spread 可能在等待財報驗證的途中歸零。

## Tail scenarios

- **Scenario A — Citi TMT 反彈（機率約 30%）**：CEO 今日（2026-09-09）出席 Citi TMT 大會，若對 HAMR 進度或 FY2027 Q2 指引發表正面聲明，市場解讀為「壞消息已出清」，股價單日反彈 10–15%，put spread 損失 50–80%；以 0.5% NAV 計算，虧損約 0.25–0.40% NAV。
- **Scenario B — 超大規模業者確認 2027 capex 維持（機率約 25%）**：Microsoft 或 Google 未來數週發表資本支出不縮減聲明，空頭論述最核心的「需求降溫」基礎動搖，股價急彈 20%+ 觸發軋空，put spread 幾乎全損。
- **Scenario C — 價格數據持續不可用（機率偏高）**：若 yfinance 403 問題延續，無法即時監控部位盈虧，無法執行緊急平倉，隱性風險無法量化。

## Recommended adjustments

- **Size：Small（0.5% NAV）→ 零（純觀望）**。理由：無即時價格 = 無法定義成本基礎；月跌 -33% = 反彈風險不對稱；高 IV 環境 = put premium 昂貴。
- **Stop：不適用**（無部位即無止損問題）。
- **Entry：等待 Citi TMT 事件完全消化後（09-10 以後），且價格數據恢復、確認股價位置，再評估是否開立 put spread**。
- **Consider：若一定要表達偏空觀點，改用 SOX ETF puts 對沖半導體整體下行風險，而非 single-name WDC put**。

## Position-level $ risk

目前提案之 put spread 成本約為 NAV 的 0.5%（以 $1M 組合計約 $5,000 premium）。若 Scenario A 或 B 發生，損失接近全額 premium。更關鍵的問題是：**在 PRICE_DATA_UNAVAILABLE 狀態下，連部位成本本身都無法精確確認**，此風險已不在數字可接受性的討論範疇，而是根本的執行可行性問題。**不可接受**。

## What I'd push for

當日行動應為純觀望：不開任何方向的部位。理由是三重疊加的執行障礙——即時價格不可得、當日有 Citi TMT 高管演講造成方向不確定、以及月跌 -33% 後空頭進場時機視窗已過最佳點。最合理的作法是等待：（1）價格數據恢復；（2）Citi 事件後市場方向明確；（3）MA200（$366.99）是否有效跌破並確認成交量配合，再啟動 put spread 部位。空頭論述基本面上正確，但正確的方向不等於正確的時機，在無法管理部位的條件下，不入場本身就是最佳風控決策。

RISK-CONSERVATIVE COMPLETE
