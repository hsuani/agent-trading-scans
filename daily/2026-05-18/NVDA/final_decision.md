# Final decision — NVDA as of 2026-05-18

FINAL TRANSACTION PROPOSAL: **BUY**

## FINAL TRANSACTION RECORD

## Verdict
**MODIFY**（採納 Neutral 折衷方案，調整原 trade proposal 的 sizing 與進場結構）

---

## Final trade card

| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone（財報前）| Call Spread：Long Call $225 / Short Call $255，到期 2026-07-18 |
| Entry zone（財報後股票）| $222 – $228（需財報後首日收盤 > $222 且成交量 > 150M 確認）|
| Stop（股票倉）| $204.00（MA20 $210.30 下方約 2 ATR）|
| Stop overlay | 財報後 gap down 跌破 $200 直接市價出場，不依賴止損單 |
| Target 1 | $236.54（52週高點，財報後 1–3 週）|
| Target 2 | $260.00（突破延伸，3–6 個月）|
| Size（財報前 Call Spread）| Small：淨保費合計 ≤ NAV 0.30%（約 2–3 口）|
| Size（財報後股票）| Small 0.5% NAV，動能持續 3 日後可加至 1.0% NAV |
| Horizon | 1–3 個月為主，T2 延展至 6 個月 |
| Conviction | M（MEDIUM）|
| R:R to T1 | 約 1.5（股票進場 $225、止損 $204、T1 $236.54）|
| R:R to T2 | 約 1.7（股票），Call Spread 結構槓桿 R:R 達 3.0+ |

---

## 執行計劃（時序）

1. **今日 – 2026-05-19 收盤前**：建立 Call Spread Long $225 / Short $255，到期 2026-07-18，2–3 口，淨保費控管於 NAV 0.30% 以內。**禁止**在財報前建立純股票多倉。
2. **2026-05-20 財報日**：純觀察，不交易。
3. **2026-05-21（財報後首日）**：檢視三項條件——EPS 超預期、Q2 指引 ≥ $83B、毛利率 ≥ 70%，至少 2 項成立 + 收盤 > $222 + 成交量 > 150M，方可進入步驟 4。任一條件不成立則 Call Spread 持有至 6 月評估時間價值，不開股票倉。
4. **2026-05-22 – 05-26**：分批建立股票倉 Small 0.5% NAV，進場區間 $222–$228，止損 $204。
5. **後續 3 日動能確認**：若連續 3 日收盤 > $225、量能維持，加碼至 Medium 1.0% NAV；視波動率買入 1 個月 Put（Strike $210）作尾部保護。
6. **抵達 T1 $236.54**：股票倉減半（落袋 50%），剩餘倉位移動止損至成本價，朝 T2 延展。

---

## 主要風險（投資組合層面尾部風險）

- **二元事件 gap down**：歷史 NVDA 財報日 ±8–12%，止損單在跳空下無效。已透過「財報前僅 Call Spread、財報後才進股票」隔離。
- **P/FCF 56.5x 估值脆弱性**：若 Fed 通膨數據意外導致科技股 multiple 壓縮，NVDA 高倍數成長股跌幅恐領先大盤 1.5–2x。組合應確保 NVDA + 其他 AI/半導體部位合計不超過 NAV 5%。
- **政策尾部**：美中重新封閉 H200 出口管制，瞬間移除未定價的中國增量催化劑，跌幅 -15% 至 -20% 不等。Call Spread 已封頂下行。
- **客戶集中**：超大型雲端廠商自研 ASIC 加速為慢性結構風險，非短期止損事件，列為持有期間的 thesis-drift 監控項。

---

## Risk debate adjudication

- **Aggressive 最強之處**：指出財報前等回測 $213 的概率接近零、$206.50 止損在 1.27 ATR 內極易被洗出。Stop 設定在 $204 採納此邏輯。
- **Conservative 最強之處**：強調 gap down 下止損 slippage 風險真實存在，且 P/FCF 56.5x 在 multiple 壓縮場景下的尾部風險被原提案輕描淡寫。財報前以 Call Spread 取代裸多倉採納此邏輯。
- **Net**：本案 **weight neutral more**——理由：財報距今 < 48 小時，二元事件結構決定「先用封頂損失工具佈局、財報後再以股票倉位接續」是唯一同時尊重「上行動能不該錯過」與「下行 gap 不可承擔」兩條約束的方案。Aggressive 的 2% 裸股 + $202 止損在 gap down 至 $198 場景下實際損失達 NAV 0.40%，與其自稱「最差 0.20%」不符；Conservative 的 0.25% + $210 又過度保守且止損噪音過大。Neutral 折衷在尾部封頂與上行槓桿之間取得最佳平衡。

---

## 監控觸發點（Monitoring trigger）

**若 2026-05-21 財報後首日 NVDA 跌破 $210（MA20）且 Q2 指引營收低於 $80B 或毛利率指引 < 69%**，立即出清所有股票倉（不等 $204 止損觸發），Call Spread 視 IV crush 後殘值決定平倉或持有至 6 月。

次要觸發：**任一超大型雲端客戶（AMZN/MSFT/GOOGL）在 H2 2026 公告中明示將 ≥ $5B 季度 AI 工作負載轉移至自研 ASIC**，立即重新評估 thesis。

---

## Catalyst calendar

- **2026-05-20** — NVDA Q1 FY2027 財報（EPS、毛利率、Q2 指引）—— 全案核心觸發
- **2026-05-20 法說會** — 中國 H200 出貨進度、Blackwell Ultra 路線圖更新
- **2026-06** — Amazon / Microsoft H2 2026 capex 公告
- **2026-06 至 2026-07** — AMD MI350 出貨量與客戶採用進度
- **2026-07-18** — Call Spread 到期日，最遲評估出場
- **持續** — 美中出口管制（H200）政策動態

---

整體評級：**BUY**

FINAL DECISION COMPLETE
