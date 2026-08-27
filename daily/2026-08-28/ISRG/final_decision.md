FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — ISRG as of 2026-08-28

## Verdict
MODIFY

## 新倉判定
ISRG 不在 `held_tickers.txt` 內 → 新倉，適用 A 框架。問題是「該不該進」，答案是「該進，但要縮小、要附條件」。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位。掛單前需確認 ISRG 實際成交於 $360–$390 區間（與 sentiment.md 報價一致），否則整份決策重跑 |
| Stop | PRICE_DATA_UNAVAILABLE — 技術止損無法計算。價格數據恢復後以當日 ATR 設定，暫以「論點失效條件」代行紀律 |
| Target 1 | ~$573（24 位分析師中位目標） |
| Target 2 | ~$599（分析師共識均值） |
| Size | Small — 首批 0.5% NAV，Q3 確認後加至 1.0% NAV（硬上限 1.25%） |
| Horizon | 3–18 個月 |
| Conviction | M |
| R:R to T1 | PRICE_DATA_UNAVAILABLE（情境估算約 4.0，未經技術止損驗證，不作為決策依據） |

## Risk debate adjudication
- **Aggressive 最強論點**：P/FCF 16–17x 對比同行 18–25x，市場正以現金流標準折價交易 ISRG；且「催化劑後才加碼」確實是在更高價填倉，機會成本真實存在。
- **Conservative 最強論點**：PRICE_DATA_UNAVAILABLE 是結構性障礙而非技術瑕疵。sentiment.md（$370.42）與 fundamentals.md（$415–425）之間有 $45–55 落差，估價基礎本身存疑時，任何 R:R、任何 $ risk 計算都是虛構。
- **Net**：我採 **neutral** 為主軸。Aggressive 用未確認的 $370 反推 R:R 4.0:1 再據此要求 1.25% NAV，是循環論證；$400/$550 call spread 在報價落差 $45–55 下 delta 完全失義，**否決 options 部位**。但 Conservative 要求全面延後至 10 月，同樣用未確認報價推導 $340 止損，邏輯自我矛盾；且 Q2 已公佈的 EPS 超預期 11.83%、指導上調至 13.5–15.5%、Ion +36% 是既成事實，不是臆測。折衷：接受 Conservative 的**閘門**（價格數據必須先恢復），但拒絕其**延期**（不設 Q3 財報為強制等待）。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 現金流品質與資產負債表 | FCF/NI >90%、零負債 | FCF/NI 96.2%、淨現金 $7.13B、毛利率 71.2% | 成立 |
| 外科醫生鎖定護城河 | 競品滲透需 3–5 年 | 逾 15,000 名醫生已完訓 da Vinci 5；Ottava 尚無帳戶數據 | 觀察中 |
| Ion 第二成長引擎 | 程序量 YoY >30% | Q2 +36%，裝機基數 1,096 台 | 成立 |
| 中國市場重啟 | 積壓需求釋放 | Q1 全中國僅裝機 4 台，報銷政策 2027 才明朗 | 已失效（但未計入本次論點，故不影響入場） |

## 論點失效條件
與 Stop 分離；論點先壞就先動作，不等價格。
- 任一季度 da Vinci 程序量 YoY < 12%（指導下緣以下）→ **出場**
- 連續兩季毛利率壓縮 >150bp（跌破 ~69.7%）→ **出場**
- Ottava + Hugo 兩季合計取得 >3% 市佔，或前二十大醫學中心公開宣佈換供應商 → **減碼一半**
- Q3 Ion 程序量 YoY < 20% → **減碼一半**（第二引擎熄火）

## Monitoring trigger
即時價格恢復後，若 ISRG 實際成交價落在 $360–$390 區間外（尤其高於 $415），首批倉位取消並整份重估——估值前提已變。Q3 財報前若出現 Ottava 重量級帳戶新聞，暫停第二批加碼。

## Catalyst calendar
- 2026-10 中旬 — Q3 2026 財報（第二批加碼至 1.0% NAV 的唯一觸發點）
- 2026 年底–2027 初 — Ion 胃腸道適應症 FDA 提交
- 2027-01 — Q4 2026 財報：Ottava/Hugo 侵蝕首次量化
- 2027（待定）— 中國達文西收費代碼與報銷政策

## Metrics summary
| 指標 | 數值 |
|---|---|
| FCF/NI | 96.2% |
| 淨現金 | $7.13B（零負債） |
| 毛利率 | 71.2% |
| Q2 EPS 超預期 | +11.83% |
| Q2 營收 YoY | +18.6% |
| Forward P/E | 64–67x |
| P/FCF | 16–17x |
| YTD | -30% |
| 初始 NAV | 0.5%（上限 1.25%） |

FINAL DECISION COMPLETE
