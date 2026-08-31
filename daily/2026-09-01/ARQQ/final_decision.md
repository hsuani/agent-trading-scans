FINAL TRANSACTION PROPOSAL: **SELL**

# Final decision — ARQQ as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **SELL**

## Verdict
MODIFY

> 新倉（ARQQ 不在 held_tickers.txt）。方向性空頭，信心度 **HIGH（85%）**。修改重點：採納 neutral 的雙軌觸發架構，取代 trader 原案的單一 9/30 閘門與單一 strike。

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | SHORT（限風險結構：Dec Put Spread，非裸空） |
| Entry zone | $20.00 – $24.00（雙軌：$22+ 觸發 Dec $20/$10；$18–$21 且 9/30 業績確認觸發 Dec $18/$8） |
| Stop | $28.00 |
| Target 1 | $12.00 |
| Target 2 | $4.80 |
| Size | Small（0.5% NAV，淨權利金上限；軌道 A 首批 0.25%） |
| Horizon | 90 天（Dec 到期，9/30 業績為中繼決策點） |
| Conviction | H（85%） |
| R:R to T1 | 2.2（軌道 A）／軌道 B 為 1.4，僅以 T2 3.0× 為主要目標 |

**執行細則**：軌道 A —— 9/8 AGM 或 9/9–10 Q2B 後股價反彈至 $22 以上，即以 0.25% NAV 買入 Dec $20/$10 Put Spread；9/30 業績確認「現金 < $20M」後補足至 0.5% NAV。軌道 B —— 無反彈者嚴守 9/30 閘門，確認「現金 < $20M 且季度燒錢 > $7M」後，以 Dec $18/$8 Put Spread 一次建滿 0.5% NAV。兩軌不得同時執行，總曝險硬上限 0.5% NAV。價格為 $20.00 估算基準（Yahoo 報價中斷），開盤後須以實際報價校正 strike。

## Risk debate adjudication
- Aggressive's strongest point：SI 6.8% 遠低於 RGTI/QBTS，軋空燃料有限，且 AGM 是被低估的即時壓力點——這正當化了保留反彈前的下行窗口，而非全部押在 9/30。
- Conservative's strongest point：$20 進場的 T1 R:R 僅 1.4×，低於空頭 2× 門檻。有限損失結構是保護機制，不是次優入場點的藉口。這是全場數學支撐最強的論點。
- Net：我採納 **neutral** 較多。Aggressive 要求 1.0% NAV 立即進場，是把一個 R:R 不合格的決定線性放大；Conservative 要求「必須先漲到 $22–$24」則在直接下跌情境完全空手。雙軌機制修正 R:R 缺陷又保留下行窗口。倉位上限採 conservative 的 0.5%。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 現金跑道危機 | $28.9M 現金 ÷ $8.8M/季 = 3.3 季，2027 Q1 見底 | 9 月現金估已降至約 $20M | 成立 |
| 估值無同業支撐 | P/S ~278×，IonQ 收入為其 103 倍卻僅 <35× | 未見收入重估 | 成立 |
| 管理層系統性賣出 | CEO/CFO/CLO 逢反彈套現，六個月零買進 | CLO $25.20 高點賣出未被解釋 | 成立 |
| 技術路線相容性 | NIST FIPS 203/204/205 是否排除對稱金鑰模型 | GSA PQC 高峰會前無定論 | 觀察中 |

## 論點失效條件
- 若 FY2026（9/30）業績顯示**現金餘額 > $25M 且季度燒錢 < $5M**，現金跑道支柱失效 → 放棄進場／已建倉者出場。
- 若公告**非稀釋性策略注資 > $10M**（Intel／BAE／Microsoft 等）或**單筆 > $10M 前期款聯邦框架合約**，生存風險支柱失效 → 出場。
- 若 FY2026 全年收入 **> $3M**（H2 > $2.4M）且合約數 > 20，估值支柱鬆動 → 減碼一半。
- 若出現**內部人淨買進**（任一 C-level 公開市場買入），管理層訊號支柱失效 → 減碼。

## Monitoring trigger
若 9/8 AGM 後 24 小時內管理層明確迴避現金問題且股價跌破 $17，於 $17 附近了結軌道 A 首批一半獲利；反之若股價收盤站上 $25.20（CLO 套現高點）而未觸及 $28 Stop，先行減碼一半，不等 Stop。

## Catalyst calendar
- 2026-09-08 — AGM 年度股東大會（現金與融資問答）
- 2026-09-09/10 — Q2B Copenhagen（ARQQ 是否有重大公告）
- 2026-09（月內）— GSA PQC 高峰會（NIST 標準是否排除對稱金鑰模型）
- 2026-09-30 — FY2026 年度業績（決策閘門：現金餘額、燒錢率）

FINAL DECISION COMPLETE
