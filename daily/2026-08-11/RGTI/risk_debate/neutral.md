# Neutral risk view — RGTI

## Points of agreement（雙方共識）

- AVOID 為主方向：雙方均不支持建立多頭倉位，熊方基本面論點（P/S ~196×、GAAP 虧損/收入 10×、CTO/CFO 雙線頂部套現）在邏輯層面均獲認可。
- Short squeeze 風險真實存在：88% 分析師買入共識、Wedbush $40 目標價，任何正面政策催化劑均可引發非線性漲勢。
- CHIPS Act gap-up 尾部風險不可忽略：2026-09-01 施工啟動公告若伴隨正面條款，可直接跨越 stop 價位，傳統 stop order 在此場景無保護效力。
- ATR 不可知（PRICE_DATA_UNAVAILABLE）是倉位科學定價的真實缺口，不應以主觀感受替代量化錨點。
- 現價 $17.94 直接入場做空之 R:R = 0.88，明確低於 SHORT 門檻 2.0，不符合執行條件。

---

## Aggressive overreach

- **Where**：立即以 $17.94 入場直接放空（straight short），同時將 stop 設於 $21.00。
- **Why**：此舉自我矛盾——$21.00 正是原交易提案的「條件入場等待區間」上緣；以低於等待區間的價格入場，但把 stop 設在等待區間上方，等於在空頭論點尚未獲技術確認之前就承擔全部方向性風險。再者，1.0–1.5% NAV 在 ATR 完全不可知的條件下缺乏量化依據，屬情緒性放大而非信號強度的合理映射。

---

## Conservative overreach

- **Where**：要求「Q3 收入 <$700 萬且 CHIPS Act 談判破裂」同時成立才考慮入場。
- **Why**：此門檻形同自我取消（self-cancelling）——若兩個催化劑同步負面，屆時市場情緒早已轉空、最佳入場機會已過；且保守方在批評 gap 風險時，完全未回應 aggressive 提出的 put spread 期權結構，而 put spread 的最大損失就是付出的權利金，gap 風險在此結構下已被定義上限，保守方的核心反對理由在 put spread 框架下不成立。

---

## Balanced adjustment proposal

| 項目 | 建議 | 理由 |
|------|------|------|
| **Size** | 0.5% NAV（維持原提案） | ATR 不可知，無量化依據支持 aggressive 的加倉；0.5% 是在信號強度（MEDIUM conviction）下對 squeeze 尾部風險的合理風險預算 |
| **Structure** | Put spread：Buy $17.50P / Sell $10P，到期 2026-11-21 | 採納 aggressive 的期權結構概念：最大損失 = 權利金（≤ 0.5% NAV），完全消除 gap-up 尾部風險，conservative 的核心反對理由隨之失效 |
| **Entry** | 以 0.5% NAV 預算建立 put spread（可於現價附近執行）；直接放空（straight short）仍須等待反彈至 $19.50–$21.00，R:R ≥ 2.0 後方可考慮 | 期權結構不依賴技術入場時機；straight short 則嚴守 R:R 紀律 |
| **Stop** | Put spread：N/A（最大損失 = 權利金，自動定義）；若另加 straight short：$23.00 維持不變 | $23.00 對直接放空仍為有效邏輯止損（突破代表高管套現區間被多方收復） |
| **Hedge** | 不建議用 QTUM put 替代 RGTI put spread——CTO/CFO 個股套現信號無法在 ETF 層面複製，個股 alpha 信號應對應個股工具 | — |
| **Time horizon** | 3 個月（覆蓋 Q3 2026 財報催化劑，2026-11） | Q3 收入軌跡是唯一能在短期內量化驗證熊方論點的節點 |

---

## Net $ risk if stop hits

以 NAV $200,000、0.5% 風險預算計：

**$1,000**（= 0.5% NAV）

Put spread 結構下，最大損失 = 已支付權利金，硬上限即為 $1,000，gap-up 情境不會突破此上限。

---

## Net $ upside at T1 / T2

以入場中位 $20.25、T1 $13.50、T2 $9.00，R:R 2.45 / 4.09（來自原交易提案）：

**T1：$2,450** / **T2：$4,090**

Put spread 結構下，最大獲利為 spread 寬度（$7.50）扣除權利金；若權利金約 $2.50/spread，淨獲利 = $5.00/spread；以 $1,000 預算可購入約 4 份合約（100 股/份），最大獲利 **~$2,000**，略低於 straight short T1 情境，但風險輪廓更乾淨。

---

NEUTRAL VIEW COMPLETE
