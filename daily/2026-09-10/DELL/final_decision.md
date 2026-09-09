# Final decision — DELL as of 2026-09-10

FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> 部位判定：DELL 不在 `held_tickers.txt`，屬**新倉**決策，問題是「該不該進、以什麼形式進」。

## Final trade card

| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無法定價（PRICE_DATA_UNAVAILABLE）— 交易員須自券商取得即時報價後，於財報後盤整區間分批進場 |
| Stop | 無法定價 — 以最近顯著低點下方 1× ATR14 設定；換算約進場價 -12% 至 -13%，硬性 |
| Target 1 | 分析師共識區間（Evercore / Citi / BofA），約進場價 +20% 級距 |
| Target 2 | 多頭極端情境（25× P/E × FY28 EPS），低概率，不作主要持倉依據 |
| Size | Small-to-Medium（**1.25% NAV 上限**；首批 0.75%，FOMC 後補足） |
| Horizon | 1–2 季，至 2026-12 月初 Q3 FY2027 財報 |
| Conviction | M（**55%**） |
| R:R to T1 | 約 1.6（以 -13% Stop、+20% T1 估算）；**實際計算後若 < 1.5 則放棄進場** |

**強制前置條件**：Stop 未以實際報價定義前，不得下單。這是紀律，不是建議。

## Risk debate adjudication
- Aggressive's strongest point: 財報後動能窗口是 alpha 最密集的時段，$95B 積壓訂單、EPS 超預期 44%、指引上修 $25B 三者同步確認的財報品質罕見；以「資料不全」為由縮倉，是用程序問題替換基本面判斷。
- Conservative's strongest point: Stop 未定義即進場等同敞口無底；毛利率 -330 bps 是已確認的財務事實而非預測，內部人淨賣出 $1B+ 且**零買入**是主動決策，不能全數以基金到期解釋。
- Net: 我採納 **neutral** 的權衡。Aggressive 對基本面品質的判斷正確，但 2.5–3% NAV 加 5–7% Call Spread，對「中等信心」而言違反比例原則；在不知進場成本時疊加槓桿是把速度凌駕風控。Conservative 壓到 0.75% 則是對可核實財報的過度折扣。折中為 1.25% NAV、硬性 Stop、分批進場，並以 SMH put spread（≤0.10% NAV）覆蓋 FOMC 鷹派尾部。**否決 Call Spread 疊加。**

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 伺服器積壓訂單能見度 | 積壓訂單持續增長、覆蓋 4–6 季收入 | $95B 積壓，FY2027 指引上修至 $192B | 成立 |
| 全棧整合競爭壁壘 | 單季 AI 伺服器營收顯著領先同業 | $16.1B vs Lenovo 基礎設施 $8.51B | 成立 |
| 毛利率結構可逆 | 組合毛利率隨高階組態回升 | 21.1% → 17.8%（-330 bps），未見企穩 | 觀察中 |
| 估值倍數可持續 | 市場願給硬體商 20×+ P/E | YTD +262% 已定價樂觀情境；內部人淨賣出 $1B+ 且零買入 | 觀察中 |

四根支柱兩成立、兩觀察中、零失效 —— 這正是進場但降檔至 1.25% 的依據。

## 論點失效條件
（與 Stop 分開：Stop 是價格紀律，以下是論點紀律，論點先壞就不等 Stop）
- 若 Q3 FY2027 毛利率低於 17.5%（連續第二季下滑），毛利率可逆支柱失效 → **出場**
- 若 Q3 財報 AI 伺服器積壓訂單未突破 $95B（停滯或下降），能見度支柱失效 → **減碼至半倉**
- 若 AWS、Azure、Google Cloud 任一家公開下修 AI 基礎設施 capex 預算，能見度支柱失效 → **出場**
- 若 HPE Q3 顯示 AI 伺服器市占季對季逼近 DELL，壁壘支柱轉觀察 → **暫停補倉**

## Monitoring trigger
2026-09-16 FOMC 若明確排除降息或升息，於補倉前重評；內部人若出現**首筆買入**（Form 4），估值支柱轉「成立」，方可考慮上調至 1.5% NAV。

## Catalyst calendar
- 2026-09-16 — FOMC 利率決議
- 2026-09 月中至下旬 — HPE Q3 FY2026 財報（AI 伺服器市占）
- 2026-12-01 前後 — DELL Q3 FY2027 財報（毛利率、積壓訂單）
- 持續 — Form 4 內部人申報

FINAL DECISION COMPLETE
