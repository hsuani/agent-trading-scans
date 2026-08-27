# Conservative risk view — VRT

## Where trader is too aggressive

1. **倉位口徑不一，存在隱性擴倉路徑**：trade_proposal 設定 Small 0.5% NAV，但 investment_plan 另以「三成→六成倉」框架重新描述，隱含最終部位可達 ~1.5% NAV。兩份文件語義不一致，為倉位悄然放大埋下伏筆。

2. **無 Stop 等於無風險上限**：以 PRICE_DATA_UNAVAILABLE 為由刻意不設止損，在 Trailing P/E 76.86 + 二元財報事件前，等同持有開放式下行部位——缺口跌（gap-down）無法控制。

3. **CSO 大額減持信號被輕輕帶過**：Roger Fradin 出售直接持股 57%（約 $5,140 萬美元），機構上季淨賣 177.6M 股，兩者同向、量大，報告僅以「不可忽視」帶過，力道遠不足以反映其嚴重性。

4. **競爭侵蝕速度低估**：EV/EBITDA 49.25 對 Eaton（Boyd Thermal 整合）+ Modine（資料中心銷售 +78%）壓縮毛利率的情境完全未定價。每 200 bps 毛利率下滑即蒸發 FY2026 EPS 約 $0.40-0.50，直接觸發盈利與倍數雙殺。

## Tail scenarios

- **Scenario A（概率 25-30%）**：Q2 EPS < $1.43 且毛利率跌破 36%，管理層下調 H2 指引 → 股價單日 -15 至 -25%（以 $304.50 參考價估算，跌至 $228-259 區間）。若倉位已按 investment_plan 擴至 1.5% NAV，損失達 0.225-0.375% NAV。
- **Scenario B（概率 15%）**：Fed 重啟緊縮或「Higher for Longer」政策延長 → 高 P/E 組合性殺估值，VRT 與 NVDA、SMCI、DELL 高度相關（AI 基建主題），同步跌 20-30%，持倉無法有效分散。
- **Scenario C（概率 10%）**：Meta/Google/Microsoft 任一方公開宣布削減 AI CapEx ≥ 10% → $15B backlog 轉化率疑慮驟升，股價可能跌破 $250，IV 飆升同步加劇持倉成本。
- **Scenario D（概率 10-15%）**：Eaton 液冷業務主動降價奪單 → 毛利率 36% 防線失守且量無法補價，多頭論點核心崩潰，無觸底信號。

## Recommended adjustments

- **Size**：Small 0.5% NAV → **0.25% NAV**（財報前），明文鎖死上限，禁止依 investment_plan「六成倉」語義在財報前擴倉。
- **Stop**：取得即時報價後立即設 **2× ATR(14)** 硬止損，不以「財報後再說」為由無限期推延。若財報前仍無法設止損，倉位應再減半至 0.125% NAV。
- **Entry**：嚴格等待 Q2 財報後——EPS ≥ $1.60 且 H2 指引上調**兩個條件同時成立**，方才建倉至 Small 0.5%；單一條件達標僅維持 0.25%。
- **Hedge**：以 VRT 倉位等值 5% 資金買進 Q2 財報期間 put spread（若期權流動性允許），或以 XLI puts 對沖工業股系統性拋售風險。

## Position-level $ risk

以 $304.50 參考價計算（PRICE_DATA_UNAVAILABLE，僅供示意）：

| 倉位 | NAV $1M 倉位金額 | Scenario A 跌 20% 損失 | 占 NAV |
|------|----------------|----------------------|--------|
| 提案 Small 0.5% | $5,000 | $1,000 | 0.10% |
| 建議壓縮至 0.25% | $2,500 | $500 | 0.05% |
| 若擴至 Medium 1.5% | $15,000 | $3,000 | 0.30% |

0.5% 倉位的 0.10% NAV 損失尚屬可接受。**但 investment_plan「六成倉」語義若實現為 1.5% NAV 且無止損，同樣跌幅下損失升至 0.30% NAV，且無封頂——風險不對稱性不可接受。**

## What I'd push for

財報前將倉位嚴格壓在 **0.25% NAV**，明文禁止任何形式的財報前加碼。若 2026-07-29 當日無法於盤中取得即時報價並設定 2× ATR 止損，則全數退出至現金、財報後重新評估。核心理由：Trailing P/E 76.86 + CSO 大額減持 57% + 機構淨賣 177.6M 股 + 無即時止損，四重疊加意味財報前任何持倉都是在支付「不確定性溢價」而非獲得風險補償。財報後若 EPS ≥ $1.60 且 H2 指引上調，以 2× ATR 止損後建倉 Small 0.5%；Q3 執行確認後再討論 Medium。現在的邊際多頭論點不值得在二元事件前承擔開放式下行。

CONSERVATIVE RISK POSITION COMPLETE
