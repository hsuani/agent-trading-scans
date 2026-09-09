# Conservative risk view — 000660.KS (SK Hynix)

## Where trader is too aggressive

提案建議 HOLD、倉位 0.5% NAV 或以下，立場看似保守，實則在以下三個維度仍顯過激：

- **定倉無錨**：ATR 與即時股價均為 PRICE_DATA_UNAVAILABLE，無法進行 vol-adjusted sizing。在連波動率都無法量化的情況下，0.5% NAV 是毫無根據的數字，而非風控計算的結果。
- **Stop 缺失**：提案明確標示無法給出進出場價位。沒有 Stop 意味著下行損失在制度上是無上限的，這本身即構成風控失格。
- **共識擁擠被輕描淡寫**：37/38 分析師給 BUY、目標價均值 KRW 3.21M，歷史上此類極端共識往往是調降週期的前兆。Morgan Stanley 將目標壓在 KRW 120,000（與共識均值差距 26 倍），在 PRICE_DATA_UNAVAILABLE 的情況下無法排除此機構已掌握市場尚未定價的不利資訊。

---

## Tail scenarios

- **Scenario A（機率 ~25%）：三星 NVIDIA HBM4 全認證通過並大量出貨** → HBM ASP 開始下行，SK Hynix HBM 市佔繼續從 50% 向 40% 滑落。OPM 由 76% 壓縮至 55–60%，觸發 Q3/Q4 盈利下修潮。歷史類比（2018 記憶體週期逆轉）顯示股價可於 12–18 個月內下修 50–70%。對 0.5% NAV 多頭部位，尾部損失可達 0.25–0.35% NAV。
- **Scenario B（機率 ~20%）：Q3 OPM 低於 65%** → 確認 ASP 開始下行，週期峰值信號成立。KRW 40T capex 既已鎖定，FCF 急轉直下，資產負債表壓力升高，機構被迫止損。
- **Scenario C（機率 ~15%）：Fed 超預期緊縮或全球需求急速萎縮** → AI 資本支出預算削減，HBM 需求假設崩塌，整體半導體板塊同步下修，個股無法倖免。
- **Scenario D（機率 ~10%）：Morgan Stanley KRW 120,000 目標價的資訊缺口被解釋，且指向已發生的股價大幅上漲** → 當前進場等同在已翻倍或翻多倍的高位追入，隱含估值風險遠超共識所呈現。

---

## Recommended adjustments

- **Size**：0.5% NAV → **<0.25% NAV，新倉建議歸零**（理由：無 ATR 錨、無 Stop、Morgan Stanley 分歧未解、HBM 市佔侵蝕趨勢明確）
- **Stop**：PRICE_DATA_UNAVAILABLE 情況下不得開新倉；既有倉位應以 Q3 OPM < 65% 或三星 HBM4 認證通過為硬性止損觸發條件，提前設定退出計畫
- **Entry**：等待 Q3 財報（2026-10-27）確認 HBM4 blended ASP 環比上升、OPM ≥ 70%，方可考慮重建多頭
- **Hedge**：考慮以 SOX ETF put 或三星電子（005930.KS）相對空頭作為配對保護，降低 HBM 板塊集中風險

---

## Position-level $ risk

無即時股價，精確 $ loss 無法計算。以尾部情境估算：若持有 0.5% NAV 多頭部位，Scenario A/B 下歷史週期跌幅 50–70% 意味著部位損失達 **0.25–0.35% NAV**。此損失乘以整體組合規模後，在無 Stop 的條件下不可接受——尤其當前進場訊號不明、估值錨點缺失。**結論：可接受上限為 <0.25% NAV，且必須預設 Q3 財報前的硬性退出條件。**

---

## What I'd push for

在 Q3 財報（2026-10-27）公布前，新倉應歸零；既有倉位壓縮至 **<0.25% NAV**。理由是五重不確定性同時存在：PRICE_DATA_UNAVAILABLE 使 vol-adjusted sizing 無法執行、Morgan Stanley 26 倍目標價分歧尚未解析、HBM 市佔率一年流失 14 個百分點的結構惡化趨勢仍在延續、KRW 40T capex 已鎖定財務退路、76% OPM 在記憶體週期史上從未作為底線持續。Q3 財報若確認 HBM4 毛利率提升且 OPM ≥ 70%，屆時重新評估加碼；任何一項觸發條件失守，立即轉為 AVOID。在資訊嚴重不完整的環境下，等待是最划算的選擇。

---

CONSERVATIVE VIEW COMPLETE

RISK-CONSERVATIVE COMPLETE
