# Trade proposal — ZS as of 2026-08-28

FINAL TRANSACTION PROPOSAL: **HOLD**

## Direction
AVOID（未持倉者暫不建倉）/ HOLD 象徵性倉位（已持倉者縮倉至 quarter size 以下）

無即時價格，暫不給進出場價位。所有技術支撐／阻力位均標記為 PRICE_DATA_UNAVAILABLE，待 yfinance 或即時資料恢復後補充。

---

## Setup

Entry:   PRICE_DATA_UNAVAILABLE
Stop:    PRICE_DATA_UNAVAILABLE（理由：無法取得 ATR14 與支撐結構，停損位無法量化）
Target 1: PRICE_DATA_UNAVAILABLE
Target 2: PRICE_DATA_UNAVAILABLE
R:R: 無法計算（價格資料全面缺失）

**參考錨點（來自 investment_plan.md，非即時報價）：**
- 內部人近期賣出區間：$147–150（CFO Kevin Rubin、CLO Robert Schlossman，7 月）
- 投資計畫提及股價錨點：約 $186（夾於 $175 技術支撐與分析師均值目標 $193.79 之間）
- 分析師共識目標：均值 $193.79，高端 $250；上行保護空間僅約 3.7%
- 估值參考：9.6x P/S（相較歷史 15–25x 有折價）

以上數字取自研究報告，**不代表當前市場成交價**，不得作為實際進出場依據。

---

## Sizing
AVOID — 不建倉。

理由：確信度 **L（低）**，ATR 不可得，年化波動率不可得。Investment plan 指出財報前上行（軋空）或下行（估值殺傷）幅度均可達 15–25%，風險不對稱性尚未確立，不宜以任何規模建立方向性部位。若已持倉，縮至象徵性規模（< 0.5% NAV）以控制尾部風險。

---

## Time horizon
Days to Weeks（以 2026-09-03 財報為核心催化劑節點）

---

## Trigger

**等待條件，不立即進場。**

觸發上行重新評估（改判 LONG）：
1. Q4 FY2026 ARR 成長超預期，且 NRR ≥ 120%
2. FY2027 指引強於 5 月重置後版本
3. 財報後出現任何內部人淨買進紀錄

觸發下行重新評估（改判 SHORT / AVOID 並清倉）：
1. ARR 成長或 FCF 利潤率再次下修
2. 任何主要政府合約遺失
3. PANW 客戶轉換案例公開披露

---

## Invalidation

以下任一情況出現，NEUTRAL 立場即失效，需重新定向：

- **財報 ARR 數字與 NRR 雙雙不及預期**：論點轉向 SHORT_OR_AVOID，機構持股從 93.6% 崩至 50.3% 的趨勢若未止穩，下行空間未封。
- **財報後 CFO / CLO 繼續賣出**：7 月已在股價較 52 週高點 $303 腰斬後賣出，若財報後仍無買進對應，是最高品質看空信號，全面撤出。
- **PANW 競爭加劇實證**：若 Palo Alto Networks 公開披露自 ZS 遷出的重要企業客戶，ARR 品質立即受質疑，毛利率壓力擴大。

---

## Catalyst calendar

- **2026-09-03** — ZS Q4 FY2026 財報（最核心試金石：ARR 成長率、NRR、FY2027 指引）
- **2026-09 月**  — 美國聯邦 FY2027 預算週期集中簽約（EO 14028 / CISA 零信任框架政府採購）
- **財報後隨時** — 觀察管理層 Form 4 申報，確認是否出現任何淨買進

---

**核心論述摘要**

投資計畫判定 NEUTRAL 的理由充分：多空雙方均有可驗證論據，但熊方佔有時間標記優勢——5 月指引主動重置、7 月 CFO 在股價已腰斬後仍出售、機構持股折半，均為近期高品質反向信號。多頭的結構性零信任需求故事長期成立，但在 9 月 3 日財報明朗化前，正反論點的邊際優勢均不足以建立全倉方向性部位。交易人的職責是等待確定性提升再執行，而非在不確定節點強行押注。

TRADE PROPOSAL COMPLETE
