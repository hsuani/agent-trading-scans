FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — TLN as of 2026-11-17

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

TLN 不在 `held_tickers.txt`,屬新倉,走 A 框架。現價 $364.06 尚未進入進場區,這是條件式掛單,不是市價追價。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $349.00 – $357.00(回測才進場;RSI14 需高於 30) |
| Stop | $330.64(收盤確認,非盤中觸價) |
| Target 1 | $390.54 |
| Target 2 | $414.79 |
| Size | Small(市值 0.5% NAV,非風險預算) |
| Horizon | 1–3 個月;2026-12-31 前未回測進場區則掛單作廢 |
| Conviction | L |
| R:R to T1 | 1.7(以中點 $353 計) |

相對原提案的修改:
- **取消突破 $390.54 的第二批加碼。** 在 $390.54 進場、停損 $330.64、目標 $414.79,R:R 僅約 0.4,不符門檻;若突破,另案重新評估。
- 停損改為收盤確認,價位不放寬至 $312.89。
- Size 書面定義為市值上限;停損觸發損失約 0.032% NAV。
- 不加 sector put,不用 call spread。

## Risk debate adjudication
- Aggressive's strongest point: Q3 單季 Adjusted EBITDA 年化約 2.68B,與 2027 指引中值 2.675B 吻合,TTM 失真是可查證的論點,不是信仰題。
- Conservative's strongest point: 「0.5% NAV」必須明定為市值;前三季回購加資本支出 991M 遠高於 TTM FCF 281M,若財報否定 run-rate,跌幅會遠超技術停損距離。
- Net: I weight neutral more here because 論點「可驗證」不等於「已驗證」。Q3 是夏季高峰,單季年化可能高估;GAAP EPS 連兩季未達預期。Aggressive 以現價進場、停損 $312.89 的 R:R 自己算出來只有 0.52,不成立。Conservative 的情境機率沒有推導依據,對 0.5% 倉位再疊避險成本不成比例。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 真實盈餘基期高於 TTM | run-rate Adjusted EBITDA 約 2.5B 以上 | Q3 單季 669M,但含季節性高峰 | 觀察中 |
| 2027 指引兌現 | Adjusted EBITDA 2.50–2.85B、FCF 1.50–1.75B | 指引未下修;GAAP EPS 連兩季低於預期 | 觀察中 |
| PJM 容量價格順風 | 維持 325 USD/MW-day 上限 | 已觸上限;FERC 限制 Susquehanna 共址擴增 | 觀察中 |
| 技術結構轉多 | 價格守在 MA20/MA200 之上 | 站上三條均線;MA50 仍低於 MA200,上攻量 870K 弱於急跌量 2.22M | 成立(未確認突破) |

沒有任何一根支柱達到「已驗證」,這是倉位鎖在 0.5% 的原因。

## 論點失效條件
與 Stop 分開;任一成立即依下列動作,不等價格。
- 若公司將 2027 Adjusted EBITDA 指引下修至低於 2.50B,或 Adjusted FCF 低於 1.50B → 出場
- 若 2027-02-25 財報的 Q4 2026 Adjusted EBITDA 低於 550M → 出場
- 若同份財報的淨負債 / 年化 Adjusted EBITDA 高於 4.0x(未朝 3.5x 收斂)→ 減碼一半
- 若 FERC 或 PJM 正式公告調降容量價格上限至 325 USD/MW-day 以下,或擴大共址限制 → 出場

## Monitoring trigger
If 收盤跌破 $348.85(MA200)且次日無法收回, re-evaluate before stop is hit。另外,若 FOMC 後高收益債利差明顯擴大而倉位尚未建立,暫停掛單。

## Catalyst calendar
- 2026-12-08/09 — FOMC 利率決議
- 2026-12-31 — 進場掛單到期
- 2027-02-25 — Q4 2026 財報(主要驗證點)

FINAL DECISION COMPLETE
