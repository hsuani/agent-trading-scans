FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — AMD as of 2026-10-26

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## 部位性質
AMD 不在 `held_tickers.txt` 內，屬**新倉評估**（A 框架）。問題是「該不該進」，答案是：可以進，但只能以分批試單、收盤確認停損、並以選擇權補強的形式進。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $512.00 – $518.00（第一批，計畫倉位之半數） |
| Stop | $498.27（Bollinger 下軌，**日收盤確認**跌破才出場；盤中觸及不動作） |
| Target 1 | $542.28（MA50） |
| Target 2 | $556.79（10-21 盤中高點） |
| Size | Small — 總風險預算 0.5% NAV（1/4 標準部位）；現在動用約 0.25% NAV，餘 0.25% 待財報後加碼 |
| Horizon | 戰術 1–2 週涵蓋 FOMC 與 Q3 財報；upside trigger 成立後轉 1–3 個月趨勢持有 |
| Conviction | M |
| R:R to T1 | 1.6（中點 $515 進場、停損 $498.27）；to T2 為 2.5 |

**附加結構**：小額 Nov-13 $557.5/$600 call spread 承接財報上行 convexity，搭配名目相當的小額 SOXX put 對沖板塊跳空；兩腿權利金大致互抵，不得使總淨風險超過 0.5% NAV。

## Risk debate adjudication
- Aggressive 最強的論點：用 2.8%（< 1 ATR）的緊停損配極小倉，是「兩頭保守」——停損容易被雜訊洗掉，倉位又小到贏了也無感。這點正確，所以停損拉寬到 $498.27 並改收盤確認。
- Conservative 最強的論點：停損防不了跳空。10-22 單日放量跌 8.1% 是近在眼前的先例，8 天內兩個二元事件，現股停損的實際保護力被高估。這點也正確，所以不升級至 1/2 標準部位，並要求 SOXX put。
- Net：我偏向 **neutral**。Aggressive 把「Q2 已實現成長」當成毛利率已兌現，忽略 Q2 毛利率 53.8% 已落空一次，11-03 正是檢驗點；Conservative 的尾部機率屬主觀指派，且「完全空手」與長期結構（股價高於 MA200 28.5%、機構加碼、空單下降）矛盾。分批進場讓第二批在資訊落地後才投入，是對二元事件最誠實的處理。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 成長與現金流已實現 | 營收 YoY >40%、FCF 為正且擴張 | Q2 營收 YoY +50.1%、FCF YoY +180%、淨現金 6.71B USD | 成立 |
| 毛利率拐點 | non-GAAP 毛利率回到約 56% 指引 | Q2 實績 53.8% 低於指引，11-03 待驗證 | 觀察中 |
| AI 需求未受下游融資壓力傳導 | Data Center 指引不降溫、OpenAI 1GW 時程不延 | CoreWeave 殖利率升至 15.06%，但尚無 AMD 砍單證據 | 觀察中 |
| 長期技術結構 | 股價維持 MA200 之上、機構持續加碼 | 高於 MA200 28.5%，JPM/FMR/T. Rowe 加碼，但短線 lower highs/lows、MACD 負值 | 成立（短線弱） |

## 論點失效條件
與 Stop 分開：以下任一成立，不等價格打到 $498.27 即動作。
- 若 Q3 non-GAAP 毛利率 < 56%（連續第二季落空），毛利率支柱失效 → **出場**全部現股，不投入第二批，立場降為 SHORT_OR_AVOID。
- 若 Q4 營收指引 < $13.0B，或 Data Center 營收指引季減 / OpenAI 1GW 首批部署明確延至 2027 之後，需求支柱失效 → **出場**。
- 若財報後 Q4 指引達標但毛利率落在 55–56% 之間（邊緣），視為未確認 → 不加碼第二批，現股**減碼**至 0.15% NAV 以下觀察。
- 若 10-28 FOMC 後收盤跌破 $502.60 但未破 $498.27，屬價格雜訊而非論點失效 → 持有，但第二批延後至財報後。

## Monitoring trigger
- 10-28 FOMC 當日收盤若跌破 $502.60，隔日開盤前重新確認 SOXX put 名目是否足以覆蓋跳空情境。
- 11-03 盤前統一 Q3 EPS 共識口徑（non-GAAP，目前各來源 1.93 / 1.87 / 1.42 USD 不一致），避免用錯基準判讀。
- 加碼第二批條件：毛利率 ≥56%、Q4 指引 > $13.0B，**且**股價放量站回 $542.28；三者缺一不加。

## Catalyst calendar
- 2026-10-28 — FOMC 利率決議（β 2.454、forward P/E 32.8x，對折現率高度敏感）
- 2026-11-03 — AMD Q3 財報（待 IR 確認）：non-GAAP 毛利率 vs 56%、Q4 Data Center 指引、OpenAI 1GW / Anthropic MI450 部署時程
- 2026-11-13 — Nov call spread 到期日；財報後若 upside trigger 未成立，於到期前平倉不展期

FINAL DECISION COMPLETE
