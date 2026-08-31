# Conservative risk view — NBIS

> **價格資料警告**：所有價格水位均以 Goldman Sachs 目標價 $328 [UNVERIFIED] 為唯一錨點推算，執行前須確認實時報價。

---

## Where trader is too aggressive

**倉位規模（3-4% NAV）偏大：**
交易員以「MEDIUM conviction（6/10）」為由建議 3-4% NAV，但此規模未充分反映以下三個結構性風險的疊加效果：

1. **ATR 無法量化**（PRICE_DATA_UNAVAILABLE）。近月單月漲幅 +51%、YTD +203% [UNVERIFIED]，隱含波動率極高；在 ATR 未知的情況下，vol-adjusted 倉位應向下調整，而非以固定 NAV% 推定。標準做法：以目標每日損益不超過 0.1% NAV 反推倉位上限。
2. **Stop 過寬（相對高波動率）**：止損設於 GS anchor × (−20%) ≈ $262 [UNVERIFIED]，距進場中點 ≈ $287 [UNVERIFIED] 約 8.7%。對一支 17.1% 空頭利率、近月 +51% 漲幅的股票，8.7% 可能在數個交易日內因消息面或空頭打壓被輕易觸及，未能提供真正的保護。
3. **CIO 賣出信號被低估**：Korolenko 六個月套現 $115.7M、C-suite 64 筆賣出零買入，屬系統性分散，而非例行高點兌現。交易員雖在文件中點名，但 3-4% NAV 的規模顯示此風險被折現過多。

---

## Tail scenarios

- **Scenario A（概率 ~20%）：Meta 削減外包**
  Meta 公告自建 GPU 集群取代部分 NBIS 合約 → 訂單積壓核心瓦解，市場重定價至熊方 P/S 1.0x × $22B 情境 → 價格相對 GS anchor 下行約 −64% [UNVERIFIED] ≈ $118。以 4% NAV 倉位計，$ 損失約 4% × (265/287) ≈ −3.7% NAV（止損遠在其上，實際虧損取決於止損能否執行）。

- **Scenario B（概率 ~15%）：Q3 CapEx 惡化**
  Q3 財報 CapEx/Revenue 超過 83% 且無收窄跡象，FCF 轉正時程被推遲至 2028 年以後 → EV/EBITDA 重估承壓，價格跌破 GS anchor × (−20%) 觸發止損 → $ 損失 = (287 − 262) × shares，以 4% NAV = $40,000 / $287 ≈ 139 股計，**$ 損失 ≈ $3,475（= 0.35% NAV）**。數字本身尚可接受，但在 Scenario A 發生時止損可能滑點。

- **Scenario C（概率 ~10%）：Fed 意外升息或流動性衝擊**
  高估值、高 beta AI 板塊承受最大衝擊。NBIS TTM P/S 61.42x 在風險偏好急速收縮時首當其衝。同板塊持倉（如 NVDA、SMCI 相關）集中度若存在，會形成隱性相關性損失疊加。

- **Scenario D（概率 ~10%）：做空瀑布**
  17.1% 空頭利率（含 Michael Burry）在任一負面催化劑下可觸發賣空加速；做多方若同時離場，流動性驟縮，實際止損執行價格可能遠差於 $262 [UNVERIFIED]。

---

## Recommended adjustments

- **Size**：3-4% NAV → **最高 2% NAV**（理由：ATR 不可知 + C-suite 系統性賣出 + 高 short interest 三重疊加；2% NAV 於止損觸發時損失僅 ≈ 0.17% NAV，符合不確定期間的風控紀律）
- **Stop**：GS anchor × (−20%) ≈ $262 [UNVERIFIED] → 收緊至 **GS anchor × (−17%) ≈ $272 [UNVERIFIED]**（理由：縮短損失窗口，強制在動能明確轉弱前出場，而非等待整個支撐崩解）
- **Entry**：不建議在現價追入；**等待回調至 GS anchor × (−15%) ≈ $279 [UNVERIFIED] 並出現至少一根收盤確認K線後再建倉 1% NAV**，Q3 財報後若 CapEx/Revenue 季環比收窄才加碼至 2% NAV
- **Consider**：以 OTM put（標的：NBIS 或 AI 基礎設施 ETF）對沖 Scenario A/D 尾部風險；或以 pair trade 方式做多 NBIS / 做空單一客戶集中度更高的同業，降低板塊 beta 暴露

---

## Position-level $ risk

假設標準 NAV = $1,000,000：

| 倉位方案 | NAV% | 倉位市值 | 股數（@ $287 [UNVERIFIED]） | 止損觸發 $ 損失（@ $272） | 占 NAV% |
|---|---|---|---|---|---|
| 交易員提案 | 4% | $40,000 | ≈ 139 股 | ≈ $2,085 | **0.21%** |
| 本文建議 | 2% | $20,000 | ≈ 70 股 | ≈ $1,050 | **0.11%** |

以本文建議而言，止損觸發的 NAV 損失約 0.11%，在任何合理風控框架下均屬可接受。然而，**Scenario A（Meta 削減）若發生在止損前的跳空缺口，滑點損失可能為計算值的 2-3 倍**，因此 2% NAV 上限是保留機動空間、避免單一持倉主導帳戶結果的必要屏障。

---

## What I'd push for

在 Q3 財報（預計 2026 年 9-10 月）公布並確認 EBITDA 邊際率 ≥40%、且 CapEx/Revenue 季環比出現明確收窄訊號之前，NBIS 的核心投資論點尚未獲得足夠的基本面驗證。CIO 六個月套現 $115.7M 遠超任何「例行分散」的基準，Meta 訂單積壓的合約品質不透明，而 17.1% 的空頭利率意味著市場有大量智慧資金做出了與多方相反的押注（含 Michael Burry）。我主張：**立即將建倉上限設為 2% NAV，止損收緊至 GS anchor × (−17%) ≈ $272 [UNVERIFIED]，以 GS anchor × (−15%) ≈ $279 [UNVERIFIED] 為唯一進場門檻，Q3 財報結果公布後再決定是否加碼至 3-4% NAV**。以當前資訊集建立全倉，是在用股東資金替未確認的 CapEx 見頂敘事買保險，風險報酬不合格。

CONSERVATIVE RISK ASSESSMENT COMPLETE
