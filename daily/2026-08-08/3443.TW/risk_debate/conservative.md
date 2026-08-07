# Conservative risk view — 3443.TW (創意電子 / GUC)

## Where trader is too aggressive

- **雙重資料黑洞使 Stop 根本無法設定**：market.md（PRICE_DATA_UNAVAILABLE）與 fundamentals.md（全面 DATA_UNAVAILABLE）同時失效。ATR14、支撐位、RSI 均不存在，倉位規模 0.5% NAV 是按信念強度而非 vol-adjusted sizing 決定，等同跳過波動調整步驟。沒有 Stop 的「Small」部位，最大損失就是全倉——美元風險完全未定義。

- **P/E 84x 不對稱極端**：分析師共識目標 NT$4,812 距現價 NT$4,070 僅 +18%；熊市目標 NT$2,000 距現價 -51%。上下行比例約 1:2.8，即使成長故事成立，當前估值的 R:R 本身已不支持立即建倉。

- **機構出走速度被嚴重低估**：機構家數單季從 77 降至 44（-43%），持股量 -19.22%。此幅度與速度屬極端事件，不能以「獲利了結」輕易解釋——代表聰明錢正在主動規避 84x 定價，而非正常輪動。

- **加密礦機集中度是非線性尾部風險**：收入占比逾 30%，但毛利率受壓且管理層未給出回升時間表。若幣價單季崩跌，此板塊訂單可快速歸零，EPS 與估值倍數雙殺。

## Tail scenarios

- **Scenario A（概率 20%）：BTC/ETH 崩跌 ≥30%，礦機客戶取消訂單**
  加密收入歸零 → EPS 重估，P/E 壓縮至 50x。
  估算價：50 × NT$48.54 ≈ NT$2,427，跌幅 **-40%**，損失 ≈ NAV × 0.5% × 40% = **NAV 的 0.20%**。

- **Scenario B（概率 15%）：Alchip 贏得 GUC 現有雲端客戶下一代標案，疊加毛利下修**
  市場重新定價，熊市目標 NT$2,000 成短期共識。
  跌幅 **-51%**，損失 ≈ **NAV 的 0.255%**。

- **Scenario C（概率 10%）：Fed 鷹派衝擊 + 台股流動性緊縮**
  高 P/E 成長股估值首當其衝，P/E 壓縮至 60x。
  估算價：60 × NT$48.54 ≈ NT$2,912，跌幅 **-28%**，損失 ≈ **NAV 的 0.14%**。

## Recommended adjustments

- **Size**：0.5% NAV 為絕對天花板，非目標值。**現階段建議 AVOID（0% NAV）**；待價格資料恢復且催化劑觸發後，上限才回到 0.5%。
- **Stop**：無法設定（PRICE_DATA_UNAVAILABLE）。沒有 Stop 的倉位不是 Small，是無保護敞口。禁止在技術資料恢復前入場。
- **Entry**：嚴格執行 2026-09-10 月營收觸發條件——YoY ≥100% 且 Turnkey 占比未萎縮，未見觸發前 AVOID。
- **Consider**：若情境允許，以 SOXX Put 或 Alchip（3661.TW）相對空頭對沖半導體板塊系統性下行。

## Position-level $ risk

Stop 未定義，最壞情況損失 = 全倉 0.5% NAV。以熊市跌幅 -51% 計：
**損失 = NAV × 0.5% × 51% ≈ NAV 的 0.255%**。
絕對金額看似可控，但此數字建立在「無 Stop、依賴催化劑如期兌現」的前提，而非主動風險管理。**不可接受**——因為失去 Stop 保護，風險框架已破壞，資料不透明本身即為溢價理由。

## What I'd push for

在 PRICE_DATA_UNAVAILABLE 問題解決並恢復即時報價之前，本倉位應維持 AVOID，不以任何規模入場。0.5% NAV 是正確的倉位天花板，但前提是擁有有效的 Stop 價格。基本面財務全面 DATA_UNAVAILABLE 疊加技術面 PRICE_DATA_UNAVAILABLE，屬雙盲交易，不符合任何紀律性風險管理標準。若資料在 2026-09-10 前恢復，且確認 RSI < 70、未跌破月均線，可於月營收 YoY ≥100% 確認後以最多 0.3% NAV 試探性建倉，保留 0.2% NAV 留至 Q3 法說會（2026-10）確認 N2 design win 後加碼，Stop 設於技術結構低點（待 market.md 恢復後計算）。當前最正確的操作是：等待，而非提前佈局。

CONSERVATIVE VIEW COMPLETE
