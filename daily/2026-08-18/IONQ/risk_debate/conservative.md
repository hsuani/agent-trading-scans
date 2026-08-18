# Conservative risk view — IONQ

## 交易員過於激進之處

- **倉位上限設定偏高（0.3–0.5% NAV）：** 在 PRICE_DATA_UNAVAILABLE 狀態下，ATR 與波動率均無法計算，等同於在不知道 vol-adjusted 風險的情況下建倉。P/S 約 60 倍、EBITDA 虧損超過全年營收，此類股票年化波動率通常落在 80–120%；以 1% vol-adjusted 標準部位計算，建議上限應壓縮至 0.2% NAV，而非 0.5%。

- **允許試探性半倉（0.15–0.25% NAV）在 Investor Day 前進場：** 在無價格資料、無有效止損位的條件下預先佈局，等同於以「催化劑期望」代替「風險管理」。9 月 8 日 Investor Day 是唯一能解析 SkyWater 毛利率與 EBITDA 轉正路徑的資訊節點，在此之前入場屬資訊不足的賭注。

- **Stop 仍待確認（PRICE_DATA_UNAVAILABLE）：** 沒有明確止損位即沒有最大虧損上界，這使倉位規模設定在邏輯上失去錨點。財務面來看，若市場重新以 15× P/S 定價（仍屬高估），下行幅度達 75%；0.5% NAV × 75% = 0.375% NAV 的潛在組合衝擊，在 LOW conviction 下難以接受。

- **隱性集中風險：** IONQ 與廣義科技/AI 主題高度相關（beta 通常 > 1.5）。若投組已持有 NVDA、PLTR 或其他高 beta 科技股，此部位實際上加重了同一因子的曝險，而非獨立的量子運算 alpha。

---

## Tail 情境

- **Scenario A（機率 25%）：Investor Day 令市場失望** — 管理層未能提供 SkyWater 毛利率改善路徑或 EBITDA 轉正時間表，甚至下調全年指引。歷史上同類型催化劑落空（如 2022 年 IonQ Q4 miss），股價單日可跌 20–35%。以入場倉位 0.5% NAV、跌幅 30% 計，組合衝擊 = **0.15% NAV**；若為 0.2% NAV 倉位，衝擊壓縮至 **0.06% NAV**。

- **Scenario B（機率 15%）：SkyWater 整合後毛利率低於 30%** — 代工業務毛利率 20–35% 的低端實現，Q3 法說會披露混合毛利率顯著低於 40%，市場重新定價結構性 FCF 永久為負。P/S 壓縮至 30×，股價自 52 週高點 $84.64 的 45% 跌幅可再擴大至 65–70%，累計跌幅逼近 75%。倉位 0.5% NAV 下，潛在損失 = **0.375% NAV**。

- **Scenario C（機率 10%）：總體環境惡化（Fed 鷹派衝擊 / 科技股 sector rotation）** — 無獲利科技股在高利率再定價下首當其衝，歷史上 IONQ 在 2022 年升息週期跌幅超過 70%。此類 regime change 無催化劑可對沖，持有任何倉位均承受系統性損失。

- **Scenario D（機率 10%）：256-qubit 調試延遲超過一季** — 移除最重要的中期 Bull 論點，GPU 替代競爭論據因此增強，機構投資者可能重新評估持倉，觸發持倉結構性賣壓。

---

## 建議調整

- **Size：** 0.3–0.5% NAV → **最大 0.2% NAV**（理由：PRICE_DATA_UNAVAILABLE 使 vol-adjusted 風險無法計算；EBITDA 虧損超越全年營收的結構性隱患使下行不對稱性顯著偏向空方；LOW conviction 倉位應低於標準半倉）

- **Stop：** 待價格恢復後設定 → **強制要求：在未確認止損位前，禁止開立任何倉位**（no stop = no entry，此為原則性要求）

- **Entry：** 放棄 Investor Day 前的試探性半倉 → **等待 9 月 8 日 Investor Day 揭露後確認進場**，確認條件：混合毛利率指引 > 40% 且管理層提供 EBITDA 轉正時間表（即便模糊如「2027 年底前」亦可）

- **Consider：** 若進場後持有，考慮以 XLK puts 或 ARKQ（量子/科技 ETF）puts 作為部分對沖，對沖比例建議 30–50% 倉位名目值，以控制 Scenario C 的系統性風險

---

## Position-level $ 風險

由於 PRICE_DATA_UNAVAILABLE，以比例方式說明：

若倉位為 **0.2% NAV**，Investor Day 失望情境（跌幅 30%）：
損失 = 0.2% × 30% = **0.06% NAV** — 在 LOW conviction 下可接受。

若倉位維持 **0.5% NAV**，同情境損失 = **0.15% NAV**；若 Scenario B 成真（跌幅 75%），損失達 **0.375% NAV** — 對 LOW conviction 投機部位而言不可接受，尤其在 stop 位置尚未確認的前提下。

---

## 我的主張

**核心立場：** 在 PRICE_DATA_UNAVAILABLE 且 EBITDA 虧損超越全年營收的雙重條件下，任何 Investor Day 前的建倉行為都是在無風險量化基礎上進行的投機，而非紀律性交易。我推薦將最大倉位從 0.5% NAV 壓縮至 **0.2% NAV**，並要求：（1）價格資料恢復後先確認止損位，（2）9 月 8 日 Investor Day 必須釋出 SkyWater 混合毛利率 > 40% 且有明確 EBITDA 轉正時間表，方可啟動建倉。任何一個條件未滿足，立場應降為 AVOID。以 LOW conviction 之名持有 0.5% NAV 的部位而無止損，是名稱與行動不一致的風險管理，必須糾正。

---

CONSERVATIVE VIEW COMPLETE
