FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — NVDA as of 2026-10-26

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> 步驟 0: NVDA 不在 `pipeline/tools/held_tickers.txt`, 屬新倉評估, 問題是「該不該進」。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 第一筆 0.25% NAV: $207.25 – $209.00 (支撐測試且未收盤跌破); 第二筆補至 0.50% NAV: 收盤站回 $213.85 |
| Stop | $203.67 (MA200, 收盤基礎, 掛硬性停損單; 明確註記: 不保護跳空) |
| Target 1 | $218.88 |
| Target 2 | $225.54 |
| Size | Small (0.5% NAV 上限, 分兩筆); 升級 Medium (1.5%) 需 FOMC 不轉鷹 **且** 11-17 財報驗證 OCF/AR, 兩者缺一不可 |
| Horizon | 戰術 1–4 週 (10-28 FOMC 至 11-17 財報); 驗證後可延長至 1–3 個月 |
| Conviction | L |
| R:R to T1 | 2.5 (代表進場 $208.00); to T2 ≈ 4.0 |

尾部避險: 以極小名目買入短天期 (到期覆蓋 10-28 至 11-17) 約 $195 strike 的 OTM put, 僅對沖跳空缺口, 名目不超過股票部位的對等股數。**不做** call spread。

## Risk debate adjudication
- Aggressive's strongest point: 等收盤站回 $213.85 才進場會放棄支撐區最佳 R:R (到 T2 約 4.0x); 支撐測試分批條款應保留。
- Conservative's strongest point: $203.67 的停損在 FOMC 鷹派或 CoreWeave 信用事件下是失真的保護 —— 跳空時無法在該價成交, 不能把「停損距離 $4.33」誤讀為「風險已鎖定」。
- Net: 我偏向 **neutral**。Aggressive 把 $ 絕對虧損小當成放大倉位的理由, 只是線性放大兩端, 沒有改善 R:R, 也直接無視投資計畫 LOW 信心的紀律; Conservative 的 0.25% 砍半是對同一組已知風險 (26B 負債、OCF) 重複計提, 且取消支撐分批等於用 R:R 換確認感。Neutral 的兩段式進場保留了支撐區 R:R, 同時用 put 而非倉位縮減來處理跳空這個真正未被定價的風險, 是最自洽的結構。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 已實現成長 + 第三方需求驗證 | 季營收 YoY >50%, 毛利率 ≥70%, 供應鏈 (TSMC/Meta CapEx) 同步上修 | 季營收 $96.22B (YoY +105.9%), 毛利率 75.0%, TSMC 上調全年成長至約 44%, Meta 上調 2026 CapEx 下限 | 成立 |
| 估值安全邊際 | forward P/E 低於 20x, 即使 EPS 下修 20% 仍合理 | forward P/E 13.3x, 下修 20% 後約 16.6x | 成立 |
| 現金轉換品質 (OCF / AR / DSO) | OCF 回升至 ≥ $40B, DSO 回落至 ≤ 55 天 | 上季 OCF 季減 52%, AR 季增 55%, DSO 54→60 天, 待 11-17 驗證 | 觀察中 |
| 26B 帶息負債性質 + neocloud 傳導 | 屬一般融資, 非 vendor financing; CoreWeave/Nebius 無違約砍單 | 10-Q 尚未揭露; CoreWeave 2031 債殖利率 >16% | 觀察中 |
| MA200 中期多頭結構 | 價格守住 $203.67 並修復至 MA20 上方 | 現價 $210.96, 跌破 MA20/MA50, MACD hist -2.15 | 觀察中 |

## 論點失效條件
必須可證偽, 且與 Stop 分開 (Stop 是價格紀律, 這裡是論點紀律)。
- 若 11-17 財報 OCF < $40B **或** DSO 未回落至 ≤ 58 天 (連兩季惡化), 現金轉換支柱失效 → 不論價位, 出場。
- 若 10-Q 揭露 26B 帶息負債中任何部分與客戶融資 / neocloud 回購承諾掛鉤, 負債支柱失效 → 出場。
- 若 CoreWeave 或 Nebius 公告違約、重組債務, 或 NVDA 公告砍單 / 回購承諾被觸發, 傳導支柱失效 → 出場, 不等 Stop。
- 若 10-28 FOMC 升息或聲明明確轉鷹 (點陣圖上移), 估值支柱動搖 → 不補第二筆, 第一筆 0.25% 保留但 put 持有至財報。
- 若 11-17 財報營收 < $105B (低於約 $109B 預期 4% 以上) 且指引未上修, 成長支柱轉為觀察中 → 減碼至 0.25%。

## Monitoring trigger
- 若 CoreWeave 2031 債殖利率升破 20% 或 10 月以來跌幅擴大超過 45%, 在 Stop 被打到之前重新評估傳導風險。
- 若收盤站回 $225.54 (MA20) 且 FOMC 不轉鷹, 重新評估是否提前至財報前升級至 Medium (預設仍是否, 需另行論證)。
- 若第一筆建立後連續 3 個交易日收盤低於 $207.25 但未破 $203.67, 視為支撐失效的前兆, 暫停第二筆。

## Catalyst calendar
- 2026-10-28 — FOMC 利率決議與聲明; 決定第二筆是否可以補到 0.5%
- 2026-11-17 — NVDA 財報 + 10-Q; 驗證 OCF/AR/DSO 與 26B 負債性質, 決定升級 Medium 或出場
- 2026-11-20 — put 到期窗口前後; 財報後若支柱全數成立則讓 put 到期, 不續

FINAL DECISION COMPLETE
