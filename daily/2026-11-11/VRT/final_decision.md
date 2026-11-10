FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — VRT as of 2026-11-11

倉位判定：VRT 不在 `held_tickers.txt` → 新倉，走 A 框架（問題是「該不該進」）。

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（限價等回檔，現價 $196.45 不進場） |
| Entry zone | $178.25 – $189.01（分批，下緣配較大子倉位） |
| Stop | $170.80（收盤跌破即次日開盤出場，不等二次確認） |
| Target 1 | $210.38 |
| Target 2 | $234.62 |
| Size | Small (0.5% NAV) |
| Horizon | 1–3 個月；掛單有效至 2026-12-11，未成交即撤單重評 |
| Conviction | L |
| R:R to T1 | 2.1（以中位數 $183.63 計；T2 約 4.0） |

相對原提案的修改：
1. Stop 由觸價改為收盤觸發。
2. 加碼拆兩段：收盤站回 $210.38 且 MACD 直方圖翻正 → 加至 1.0%；RSI14 > 50 且量能確認 → 加至 1.5%，Stop 上移 $187.24。
3. VRT 併入 AI capex 主題風險桶。現有持倉 MOD、3017.TW（同屬散熱）、ANET、COHR、MRVL、DLR 已高度重疊，加碼前須先檢查主題總曝險，不得自動升級。
4. 不採用 call spread，維持單一現股交易卡。

## Risk debate adjudication
- Aggressive's strongest point：進場中位到 Stop 僅 0.76×ATR14，在 CPI／NVIDIA 財報窗口容易被雜訊洗出。這點成立，但解法是收盤觸發，不是下移至 $165（會稀釋結構意義）。
- Conservative's strongest point：11/4、11/5 連續兩日 -12.9%／-14.0% 的跳空先例，名目停損不等於實際出場價；且 AI capex 主題集中度未被計入。
- Net: I weight neutral more here because 現價 R:R 僅 0.6–0.9，Aggressive 用 $183.6 的報酬比論證 $196 追價，是兩套假設混用；Conservative 的雙重確認停損在跳空情境反而延後出場。Neutral 的收盤停損加分段加碼，兩邊的有效顧慮都吸收了。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營收與指引上修動能 | 成長延續、指引上調 | Q3 營收 +61.2%，連 15 季優於預估，FY EPS 指引上調至 7.15 | 成立 |
| 利潤率與現金轉換 | 營益率擴張、FCF 走揚 | 營益率 23.0%（+2.5pp），但 Q3 OCF 由 1.10B 降至 0.79B，存貨 YTD +126% | 觀察中 |
| 需求由客戶預付支撐 | 遞延收入增速不低於存貨 | 遞延收入 +127% 至 4.12B，對存貨 +126%；backlog 已停止揭露 | 觀察中 |
| 價格結構止跌 | 守住 $170.80、收復 MA20 | 死叉、空頭排列、lower highs 未破，僅低點墊高 | 觀察中 |

## 論點失效條件
- 若 Q4 FY26（2027-02-10）OCF 低於 Q3 的 0.79B，且遞延收入低於 4.12B 而存貨續增 → 現金轉換與預付支柱同時失效 → 出場。
- 若 Q4 營收 YoY 低於 30%，或 FY27 EPS 指引中位數低於共識 9.84 達 5% 以上 → 成長支柱失效 → 出場。
- 若 NVIDIA 11 月下旬財報的資料中心營收指引季減，或任一主要 hyperscaler 下修 2027 capex 指引 → 需求支柱失效 → 未成交則撤單，已成交則減碼一半。
- 若 ETN 或 Schneider 下一季訂單／backlog 轉為 YoY 負成長 → 產業需求佐證失效 → 減碼。

## Monitoring trigger
If 未成交前收盤站上 $210.38，不追價，撤單並重新評估進場區；If 持倉期間單日收跌超過 10% 但仍在 $170.80 之上，當日即重評，不等 Stop。

## Catalyst calendar
- 2026-11-11 至 11-13 — 美國 10 月 CPI
- 2026-11 下旬 — NVIDIA 財報
- 2026-12-08 至 12-09 — FOMC
- 2027-02-10 — VRT Q4 FY26 財報暨 FY27 指引

FINAL DECISION COMPLETE
