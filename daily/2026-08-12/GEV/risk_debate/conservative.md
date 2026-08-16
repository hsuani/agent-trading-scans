# Conservative risk view — GEV (GE Vernova)

> 參考底價：fundamentals.md 引用 2026-08-11 收盤約 $990.85。market.md 全面 PRICE_DATA_UNAVAILABLE，以下 $ 計算以 $990 為敘述性錨點，非即時報價，不代表可交易價位。

---

## Where trader is too aggressive

**① Trailing P/E ~100x 建立在尚未兌現的利潤跳躍上**
Q2 adj. EPS $2.47，年化 $9.88/股；@ $990 → trailing P/E ≈ 100x（可追溯：$990 ÷ $9.88）。
Forward P/E 20-25x 成立的前提是 2027 EPS 達 $40-50/股，即盈利須在 18 個月內擴大 **4-5 倍**。
Operating margin 從 5-8% 升至 12-15% 的路徑完全未經 Q3 確認，任何季度滑點均觸發估值崩塌。

**② FCF 品質：預付訂金膨脹現金流**
2024 FCF 估計 $1.8-3.6B，但 Q2 2026 全年 FCF 指引跳升至 $11.5-12.5B，成長幅度遠超 operating margin 改善幅度。
$176B backlog 伴隨大量客戶 advance deposits 流入，FCF/NI 仍只有 0.6-0.8x（健康標準 0.9-1.0x）。
此組合高度暗示 FCF 增量由工作資本預付款驅動，而非真實盈利能力提升——交貨後預付款反轉，FCF 將承壓。

**③ Q2 EPS miss 18.75% 尚未消化**
$2.47 vs 預期 $3.04（來源：news.md），在訂單同比 +88% 的強勁背景下仍大幅 miss，說明**成本端 / 交付端**執行存在落差，非純訂單問題。

**④ Wind CEO 內部人拋售 $4.57M**
Victor Abate（Wind 業務 CEO）2026-06-03 售出 4,819 股（來源：sentiment.md）。
Wind 是 GEV 核心增長引擎，其部門負責人在 Q2 財報前後大額減持，與 bull 論點形成直接矛盾。

**⑤ PRICE_DATA_UNAVAILABLE = 止損位形同虛設**
無 ATR14、支撐位、RSI 等技術資料，無法設定 evidence-based stop。
R:R ≥ 1.5 門檻無法驗證；以「資料恢復後確認」作為觸發條件，等同在無安全網的情況下規劃入場。

---

## Tail scenarios

| # | 事件 | 概率 | 價格估計 | 損失（0.75% NAV / $7,500） | 損失（1.5% NAV / $15,000） |
|---|------|------|---------|--------------------------|--------------------------|
| A | Q3 EPS 再次 miss + FCF/NI ≤ 0.65x → 2027 EPS 下修至 $25，市場給 20x → $500 | 20% | ~$500（-49%） | ~$3,675（NAV 0.37%） | ~$7,350（NAV 0.74%） |
| B | Fed 重啟升息 → 公用事業 CapEx 延遲 → 季度新訂單跌破 $15B → backlog 品質惡化 → 市場給 15x on $25 EPS → $375 | 15% | ~$375（-62%） | ~$4,650（NAV 0.47%） | ~$9,300（NAV 0.93%） |
| C | AI CapEx 週期反轉 → $176B backlog 大額訂單取消 → 成長敘事瓦解 → 股價跌回工業股 P/S 1.5x 水位 | 10% | ~$250（-75%） | ~$5,625（NAV 0.56%） | ~$11,250（NAV 1.13%） |

*Scenario A/B/C 均以 $990 基準計算，損失百分比可追溯。*

---

## Recommended adjustments

- **Size**：候補 Medium（1.5% NAV）→ 硬上限 Small（**0.5% NAV**），Q3 雙確認前不允許建任何倉位
- **Stop**：PRICE_DATA_UNAVAILABLE → 進場前必須恢復即時報價，止損需設於 **2× ATR14 below confirmed support**，否則禁止入場
- **Entry**：Q3 財報（adj. EPS ≥ $5/季 **且** FCF/NI ≥ 0.80x）必須作為**進場前提條件**，而非第二批加倉後置條件；技術資料恢復不能單獨觸發建倉
- **Hedge**：若投組已持有 ETN / FSLR / VST 等能源 / 電力基礎設施部位，需確認與 GEV 的隱性集中度；考慮以 XLI 相對強弱監控板塊輪動訊號

---

## Position-level $ risk

設 NAV = $1,000,000：

| 倉位規模 | 持倉 $ | Scenario A（-49%）損失 | Scenario B（-62%）損失 | 可接受性 |
|---------|-------|----------------------|----------------------|---------|
| 0.5% NAV（保守建議） | $5,000 | $2,450（NAV 0.25%） | $3,100（NAV 0.31%） | 可接受 |
| 0.75% NAV（提案首批） | $7,500 | $3,675（NAV 0.37%） | $4,650（NAV 0.47%） | 邊界可接受 |
| 1.5% NAV（提案滿倉） | $15,000 | $7,350（NAV 0.74%） | $9,300（NAV 0.93%） | **需 Q3 確認才可考慮** |

**核心問題**：絕對損失金額尚在容忍範圍，但 **PRICE_DATA_UNAVAILABLE 意味著沒有定義「認錯點」**——進場即無可執行止損，屬風控缺口，不論倉位大小。

---

## What I'd push for

Trade proposal「暫不進場、等待雙重確認」的方向正確，但進場門檻仍不夠嚴格。我的立場：在 Q3 2026 財報（10-11 月）同時確認 adj. EPS ≥ $5/季 **且** FCF/NI ≥ 0.80x 之前，GEV 分配上限為 **0% NAV**；任何理由的提前建倉均不被支持，包括技術資料恢復或德州清潔能源峰會消息面。Trailing P/E ~100x、Q2 EPS miss 18.75%、Wind CEO 拋售 $4.57M 三重信號同時出現，說明「MEDIUM conviction」定性過於樂觀，應降至「LOW-MEDIUM」，對應 Small 倉（0.5% NAV）最終硬上限，且只在 Q3 雙確認後才允許一次性建倉至上限，不設二次加碼至 Medium 的路徑。

---

CONSERVATIVE RISK ADVOCATE COMPLETE
