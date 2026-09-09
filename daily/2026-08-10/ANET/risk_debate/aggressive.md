# Aggressive risk view — ANET

> **價格聲明：** PRICE_DATA_UNAVAILABLE — 所有價位均標示 *[APPROXIMATE]*，引自 trade_proposal.md 與 investment_plan.md 之文字記載，非即時行情。風險管理框架以近似區間討論，待即時數據恢復後須重新校準。

---

## Where trader is too cautious

- **倉位雙重打折，過度保守。** 交易員定義 MEDIUM conviction → 1.5% NAV，再以「等待確認」為由切半至 0.75% NAV。兩層折扣疊加，使實際曝險僅為正常規模的一半。然而 ANET 的基本面品質在同儕中屬頂尖：FCF/NI = 1.21、毛利率 64.1%、ROIC 25.8%、淨現金 $12.35B、六季連續平均 EPS 驚喜率 +10.3%——這類「成長品質雙優」組合值得更高的起始倉位，而不是在 MEDIUM conviction 之上再加一刀。

- **「等待回落 $185–195 *[APPROXIMATE]*」策略存在機會成本陷阱。** Q2 財報後股價自 $182.57 *[APPROXIMATE]* 一日跳空 +12.7%，反映三度上調的 $12.6B FY2026 指引、超大規模客戶公開背書（Meta、Microsoft、Oracle）以及 1.6Tbps 7060XE7 風冷版確認出貨。強勁基本面催化的跳空缺口往往不會完全回補；若 Q3 財報前有任何正面新聞流出，$185–195 *[APPROXIMATE]* 的等待區間可能永遠不會到達，交易員將空手錯過整段行情。

- **技術性停損框架混淆「基本面信號」與「價格支撐」。** 以 CEO Ullal $187–189 *[APPROXIMATE]* 賣出區間作為停損參考，是把內部人的估值判斷錯當成技術止損位——這兩者本質上不同。CEO 賣出依 10b5-1 計畫執行，代表他對估值的主觀看法，不代表市場技術性支撐。把停損設得如此貼近，在正常波動下極易被 whipsawed。

---

## Recommended adjustments

- **Size：0.75% NAV → 1.25% NAV（直接建倉，不分兩段等待）**
  理由：FCF/NI 超越 1.2、三連升的年度指引、超大規模客戶實名背書，是同儕中罕見組合，值得突破半倉框架。管理層賣出的信念折扣已在 MEDIUM conviction 中體現，無需再對倉位額外打折。

- **Entry：分兩批進場，而非坐等全額回落 *[APPROXIMATE]***
  - **第一批（即時）0.5% NAV**：以當前近似市價（~$205 *[APPROXIMATE]*）直接建立初始曝險，確保不會空手錯過行情。
  - **第二批 0.75% NAV**：若股價回落至 $190–195 *[APPROXIMATE]* 再加碼，達成目標倉位 1.25% NAV。
  - 若回落不來，Q3 財報前維持 0.5% NAV 單批部位，財報確認後視結果補足。

- **Stop：給予結構性空間，對應前財報基礎 ~$178–180 *[APPROXIMATE]***
  CEO 賣出區間不是技術停損，Q2 跳空前的底部支撐（$182.57 *[APPROXIMATE]* 之下緩衝）才是論題失效的真實技術位。建議以 $178–180 *[APPROXIMATE]* 作為停損參考，給予 ~$15–20 的空間避免日內波動出局。以 1.25% NAV 部位計算，若入場均價約 $200 *[APPROXIMATE]*，此停損幅度約 -9%，對應最大損失 ≈ **0.11% NAV**。

- **Consider：Options call spread — October 到期 $205/$225 *[APPROXIMATE]* call spread**
  Q3 財報預計 10 月初，是天然的 event-driven catalyst 窗口。以 call spread 形式鎖定最大損失於支付 premium，若 ANET 財報後跳空至 $220–225+ *[APPROXIMATE]*，報酬倍率約 1.5–2.5×。此做法可以更小的 NAV 分配（0.25–0.3%）取得相近的 delta 曝險，同時完全定義下行損失上限。

---

## Asymmetry argument

| 情境 | 近似價位 *[APPROXIMATE]* | 損益估算（1.25% NAV，$200 入場均價）|
|---|---|---|
| 最差情境：停損出場 | ~$180 | 損失 -10%，≈ **-0.125% NAV**（絕對損失有限） |
| 基準情境：Target 1（BofA 目標） | ~$200 | 持平至微利 |
| 樂觀情境：Target 2（Citi 目標） | ~$215 | +7.5%，≈ **+0.094% NAV** |
| 強勢情境：Q3 財報 + 1.6Tbps 超預期 | ~$230+ | +15%，≈ **+0.188% NAV** |

R:R（最差 vs 強勢）≈ **1 : 1.5**，若加上 options call spread 槓桿，強勢情境 R:R 可擴大至 **1 : 3–4**。關鍵在於：ANET 的基本面護城河（EOS 軟體生態、64% 毛利率、零負債）為下行提供結構性托底，讓最壞情境的損失可控。

---

## What I'd push for

交易員的核心論題（以太網超越 InfiniBand、FCF 複利護城河、超大規模客戶結構性需求）完全站得住腳，但執行框架過於謹慎，把合理謹慎變成了機會成本。我的建議是：**立即以約 0.5% NAV 建立初始 LONG 部位，鎖住論題參與權；同步下設 GTC 限價單於 $190–195 *[APPROXIMATE]* 區間，等待加碼至 1.25% NAV。停損設於 $178–180 *[APPROXIMATE]*（財報前技術底部）而非 CEO 賣出區間，避免在正常回撤中被震出。** 若看好 October Q3 財報催化劑，額外配置 0.25% NAV 於 October call spread（$205/$225 *[APPROXIMATE]*），以定義風險的方式捕捉事件驅動的非線性報酬。管理層 $2.6B 賣出確實是折扣因子，但不應讓其將倉位壓縮至僅 0.75% NAV——ANET 的基本面品質值得更大的首次曝險。

AGGRESSIVE RISK COMPLETE
