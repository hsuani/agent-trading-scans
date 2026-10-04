FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — IREN as of 2026-10-04

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 定性
新倉(IREN 不在 held_tickers.txt)。現價 $41.76 不建立現股方向性部位,維持 trader 的條件式雙劇本架構,但依 risk-neutral 調整:(1) 允許 Anthropic 分配公告當日以 Jan 2027 價平 call 小額卡位,不必等 11/05 財報;(2) 劇本 B 改用 put spread 取代裸空;(3) 10/27-28 FOMC 列為獨立檢查點,決議前不擴大任一方向總曝險。

**未解決事項(明確記錄)**:fundamentals.md 存在內部矛盾 —— 在建工程 376.4 億美元大於總資產 157.9 億美元(疑為單位錯誤,應約 37.6 億);營運 CF/營收寫成 29.7%,實為約 297%。這兩項在 11/05 財報釐清前,所有 sizing 上限鎖在 Medium,不得升 Large。

## Final trade card — 劇本 A(LONG,條件觸發)
| Field | Value |
|---|---|
| Direction | LONG |
| 觸發條件 | 正式公告 IREN 取得 Anthropic 容量 ≥500MW,且收盤站上 $49.19、重回 MA200($45.57)之上 |
| 前哨部位 | 分配公告當日即可買 Jan 2027 價平 call(約 $45-50 履約),0.3-0.5% NAV,最大虧損=權利金 |
| Entry zone | $49.20 – $51.50(現股主倉) |
| Stop | $45.30(收盤) |
| Target 1 | $65.61 |
| Target 2 | $70.71 |
| Size | Medium(1.5% NAV)起手;11/05 財報驗證營運 CF 為經常性且數據錯誤已更正後,可升至 Large(2-2.5% NAV) |
| Horizon | 1-3 個月 |
| Conviction | M(觸發後) |
| R:R to T1 | 3.0(以 $50.35 中值計) |

## Final trade card — 劇本 B(SHORT,條件觸發)
| Field | Value |
|---|---|
| Direction | SHORT(以 put spread 執行,不裸空) |
| 觸發條件 | Anthropic 未選入或分配量明顯縮水、收盤跌破 $34.81,或 11/05 財報營收再度環比下滑並宣布大額增資 |
| Entry zone | $34.00 – $34.80 |
| Stop | $37.00(收盤;put spread 最大損失=淨權利金) |
| Target 1 | $28.93 |
| Target 2 | 約 $25 |
| Size | Small(0.5% NAV) |
| Horizon | 1-4 週 |
| Conviction | L |
| R:R to T1 | 2.1 |

## Risk debate adjudication
- Aggressive 最強論點:催化劑為二元事件,公告當日極可能跳空,三重確認會讓第一段軋空漲幅(21.1% 空頭比例)完全錯過。這點成立,故採納「公告即以權利金定義風險的 call 卡位」。但 Large(2.5-3%)建立在未經核實的財報數字上,不採。
- Conservative 最強論點:fundamentals.md 數據自相矛盾,財報前任何 Large sizing 等於對錯誤數字下重注;FOMC 對 187% 債務/股本結構是獨立風險。前者採納為 Large 的前置門檻,後者採納為檢查點。但要求財報作「第二重確認」等同放棄 10 月底決標的整個時間窗,0.25% NAV 近乎無意義,不採。
- Net:採 **neutral**。方向判斷三方皆未質疑(NEUTRAL/LOW),分歧只在 sizing 與時機;neutral 方案在「不錯過軋空段」與「不對可疑數字重倉」間取得平衡,且用選擇權結構讓兩劇本的跳空尾部損失都有上限。

## 論點支柱(對應劇本 A 多方論點)
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Anthropic 澳洲容量分配 | IREN 取得 ≥500MW | 決策延至 10 月底/11 月初,未定案 | 觀察中 |
| 營運 CF 可持續性 | 21 億美元為經常性營運所得 | 約為營收 297%,疑為預付款/營運資金變動;數據錯誤未更正 | 觀察中 |
| 已簽約 ARR 放量 | AI ARR 4.0 億美元(Cohere、Perplexity、Figure AI、Nvidia)如期上線 | 合約具名可查;但最新季營收 1.372 億環比下滑 | 成立(需 11/05 確認季增幅) |
| 技術結構翻多 | 收盤重回 MA200 $45.57 之上 | 低於 MA200 達 8.4%,MACD 直方圖 -0.59 | 尚未成立 |

## 論點失效條件
與 Stop 分開 —— 論點先壞就先動作,不等價格。
- 若 Anthropic 公告 IREN 分配量 <500MW 或未入選 → 支柱一失效 → 劇本 A 前哨 call 全數平倉,不建主倉;評估劇本 B 觸發。
- 若 11/05 財報顯示營運 CF 中遞延收入/客戶預付款占比過半,或在建工程、現金流量表數字未更正 → 支柱二失效 → 劇本 A 主倉禁止升 Large,已有部位減半。
- 若 11/05 財報營收連續第二季環比下滑(低於 1.372 億美元)且宣布新一輪大額股權增資 → 支柱三失效 → 劇本 A 全部出場。
- 若 Anthropic 決標延後至 11/05 之後或分配量未明確披露 → 兩劇本皆不成立,維持 AVOID,前哨 call 不建。

## Monitoring trigger
- 10/27-28 FOMC 決議偏鷹(升息或點陣圖上修):決議後 24 小時內不新增任一方向曝險,重新評估劇本 B 提前觸發機率。
- 現價若在無公告下先跌破 $37.00(前整理區),劇本 A 前哨 call 不建。

## Catalyst calendar
- 2026-10 下旬 — Anthropic 澳洲 2.16GW 容量決標(前哨 call 觸發點)
- 2026-10-27/28 — FOMC 利率決議(獨立檢查點)
- 2026-11-05 — IREN 財報:營運 CF 組成、AI ARR 季增、FY2027 CapEx 與融資指引(Large 升級門檻)

FINAL DECISION COMPLETE
