FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — TLN as of 2026-11-10

## Verdict
MODIFY

新倉(不在 held_tickers.txt),走 A 框架。這是條件式買進:觸發前不持有任何部位,現價 $358.16 不進場。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $372.00 – $375.00 |
| Stop | $348.00 |
| Target 1 | $414.79 |
| Target 2 | $449.84 |
| Size | Small (0.5% NAV) |
| Horizon | 1–3 個月 |
| Conviction | L |
| R:R to T1 | 1.6 |

- 觸發:單日收盤站上 $372 且當日量 ≥ 10 日均量 1.26M,次一交易日於區間內進場。高於 $375 不追。
- 觸發有效期至 2026-12-11,未觸發則作廢重評。
- R:R 以進場均值 $373.50 計:(414.79−373.50)/(373.50−348.00) ≈ 1.6。區間上緣 $375 進場時約 1.5。
- 停損觸發的損失約 0.034% NAV;若跳空至 $306.09 約 0.09% NAV。
- 收盤跌破 $306.09 無條件出場。
- 加碼上限 1.0% NAV,須同時滿足:死亡交叉解除、10-Q 原文核實資產負債表與 Adj. FCF 口徑。

## Risk debate adjudication
- Aggressive's strongest point: conviction 低是因為資料髒,不是論點弱;排除失真的 fundamentals.md 後,剩餘可信證據(2027 指引、ASR、VST 上修)方向一致偏多。
- Conservative's strongest point: 原案 R:R 到 T1 僅 1.4,低於自訂 1.5 門檻卻照樣放行;進場區 $372–380 又落在 $373.97 / $375.82 阻力帶內。
- Net: I weight neutral more here because 它同時否決了兩個站不住的停損:$329.13 是 10/22–23 已失守的支撐,$355 距進場不到 1 個 ATR($20.47)。我在其基礎上做兩處修改:
  - 進場上緣由 $380 壓到 $375,讓 R:R 真正過門檻,而不是用小部位掩蓋。
  - 量能門檻維持 100% 均量,不採 neutral 放寬的 80%:11-09 的量只有均量 22%、數據可能不完整,突破進阻力帶更需要足量確認。
- 不採用 call spread 與 VST/PJM 避險:一張交易卡,部位已小到不需要。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 2027 指引成長 | Adj. EBITDA $2.50–2.85B、Adj. FCF $1.50–1.75B,中位數約 +26–27% | 公司已公布,2026 指引收窄未下修;僅有新聞二手來源,尚未以 SEC 原文核對 | 觀察中 |
| 資本回饋 | USD 1.5B ASR(約市值 10%),授權上調至 $3.0B | 已宣布,執行期至 2027-Q1 | 成立 |
| PJM 容量價格環境 | 政策只延後時程,不實質壓價 | FERC 暫停 Reliability Backstop,後續命令未出;選舉後同業曾急跌 | 觀察中 |
| 技術結構翻多 | 放量突破 $365–372 並站穩 MA200 | 死亡交叉未解除,高低點仍下移,尚未突破 | 觀察中 |

## 論點失效條件
- 若公司將 2027 指引下修,使 Adj. EBITDA 中位數低於 $2.50B 或 Adj. FCF 中位數低於 $1.50B,指引支柱失效 → 出場。
- 若 10-Q/8-K 原文的 2027 指引或 ASR 金額與新聞摘要不符(差距 >10%),或 ASR 被縮減、延後至 2027-Q1 之後,→ 出場。
- 若 FERC 或國會發布對既有機組設定容量價格上限、或調降 PJM 拍賣價格上限的正式命令/法案通過,政策支柱失效 → 出場,不等 Stop。
- 若 2027-02-25 財報 EPS 低於共識 20% 以上(連三季大幅不及),→ 減碼一半。共識 $7.22 來源可能受污染,財報前須重新核對。

## Monitoring trigger
If 進場後連兩日收盤回落至 $365 以下且量能放大,或 VST/CEG 單日因政策消息跌逾 8%,re-evaluate before stop is hit。

## Catalyst calendar
- 日期未定 — FERC 對 PJM Reliability Backstop Procurement 後續命令
- 2026-12-11 — 進場觸發有效期截止
- 2027-Q1 — USD 1.5B ASR 預計執行完畢
- 2027-02-25 — 下次財報,驗證 2027 指引

FINAL DECISION COMPLETE
