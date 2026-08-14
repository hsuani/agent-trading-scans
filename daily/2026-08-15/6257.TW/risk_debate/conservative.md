# Conservative risk view — 6257.TW (矽格股份)

## Where trader is too aggressive

**0.5% NAV 觀察倉本身仍過於寬鬆**，理由有三：

1. **PRICE_DATA_UNAVAILABLE → 無法進行 vol-adjusted sizing**。ATR 未知、stop 距離未知、entry 未知，所有 % NAV 計算均屬臆測。在無法算出 (entry − stop) × shares 的前提下，任何非零倉位都是脫離框架的隨意賭注，正確答案是 0%。

2. **管理層資本摧毀事件尚未消化**。以均價 NT$214.64 回購，現價約 NT$117，帳面損失 ~45%，回購總金額 NT$643.9M 約等於公司數季淨利。這不是「內部人逢低加碼」，而是管理層估值模型與市場嚴重脫節的直接證據。資本配置能力存疑，應對管理層決策品質打折扣，而非溢價。

3. **R:R 嚴重對多方不利，比率約 0.14**：多方上行 +6.7%（NT$125 保守目標），空方下行 -48%（NT$60）至 -69%（NT$36）。最低門檻 R:R ≥ 1.5 未達，且差距懸殊；在此條件下，維持任何方向性觀察倉均隱含方向性偏誤。

---

## Tail scenarios

- **Scenario A（概率 ~25%）：HBM 需求拐點提前**
  SK Hynix / 三星宣布 HBM4 測試大幅內製化 → DRAM+HBM 委外滲透率下滑 → 矽格 45-50% 收入基礎受結構性侵蝕 → EPS 共識從 NT$7.8 下修至 NT$5.0 以下 + P/E 多重壓縮 → 股價至 NT$60，損失 **-48%（NAV 損失約 0.24%）**。

- **Scenario B（概率 ~15%）：景氣雙殺**
  Fed 意外升息或雲端業者（AWS / Azure / Google）CapEx 指引下修 → AI 資料中心投資縮手 → HBM 訂單延後 → 矽格 NT$59.3B CapEx（佔營收 32-37%）固定成本槓桿反噬 → FCF 轉負 → 股價至 NT$36，損失 **-69%（NAV 損失約 0.35%）**。

- **Scenario C（概率 ~20%）：Q2 EPS 缺口觸發共識下修**
  矽格 Q2 EPS < NT$1.8 → FY2026 共識 NT$7.8 須大幅下修 → 現 P/E ~15x 實為虛胖 → 無外資評等背書、無技術面支撐，股價加速尋底。

---

## Recommended adjustments

- **Size**：0.5% NAV → **0%（完全避免）**
  理由：PRICE_DATA_UNAVAILABLE 使 vol-adjusted sizing 無從計算；管理層 NT$643.9M 庫藏股損失重創資本配置信譽；R:R ≈ 0.14，遠低於 1.5 門檻。

- **Stop**：無法設定（PRICE_DATA_UNAVAILABLE）。缺乏有效 stop，等同於裸持風險敞口。

- **Entry**：等待明確觸發訊號再評估——NVIDIA Q2 財報（2026-08-26）確認 HBM4 外包需求，且矽格 Q2 EPS ≥ NT$2.3；兩者缺一不可。

- **Consider**：若投資組合已持有其他台灣半導體（TSMC / ASE / 京元電子），加入矽格即使 0.5% 也形成隱性集中度，整體台灣半導體測試封裝曝險合計可能遠超 5% NAV，需拆算合併曝險。

---

## Position-level $ risk

因 PRICE_DATA_UNAVAILABLE，無法計算 (entry − stop) × shares 的絕對美元損失。

**概念試算（以情境 A 為基準）**：
假設 NAV = USD 1,000,000，0.5% NAV = USD 5,000 買入倉位。若股價從 NT$117 跌至 NT$60（-48.7%），倉位損失 ≈ USD 2,435（= 0.24% NAV）。
表面上看似微小，但問題在於：**這是在 stop 寬到無法量化的情況下被動承受的損失**，並非按 ATR 精算後主動接受的風險。兩者在策略紀律上有本質差異。

---

## What I'd push for

在 PRICE_DATA_UNAVAILABLE 尚未解除前，正確持倉為 **0% NAV**，不設觀察倉。理由：任何非零倉位都無法追溯至 vol-adjusted 計算，等同於繞過風險管理框架；管理層 NT$214.64 回購後 ~45% 帳面損失已證明內部估值模型失效，不值得給予內部人信號溢價；R:R 約 0.14 且空方情境最大跌幅 -69%，在方向未確認前持倉只是提供下行承接而不享受上行。待 2026-08-26 NVIDIA Q2 財報與 2026-09 矽格 Q2 財報同時落地，且兩項均指向 HBM 委外需求加速，再以有即時報價的條件重新計算 ATR、確認有效 stop，才考慮以 **0.5-1% NAV 最大限度**的試探性建倉。現在的正確行動是：**完全場外觀察，不動用任何 NAV**。

---

RISK-CONSERVATIVE COMPLETE
