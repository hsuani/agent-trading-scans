# Final decision — RDDT as of 2026-08-31

FINAL TRANSACTION PROPOSAL: **HOLD**

## FINAL VERDICT

**HOLD / WATCHLIST — 條件式核准，今日不建倉。Conviction 5/10。**

RDDT 不在 `held_tickers.txt` 內，屬新倉評估。結論：核准交易計劃但加上執行閘門與分階段釋放（MODIFY），在條件滿足前部位為 0%。

## Verdict
MODIFY

> **價格錨點警示**：PRICE_DATA_UNAVAILABLE。以下所有價位均由錨點 $153.35 **UNVERIFIED** 以百分比推算，全部標記 **UNVERIFIED**，不得作為獨立下單依據。
> **執行閘門**：下單前必須以交易商即時報價驗證現價；若實際市價偏離錨點 ±5% 以上，本交易卡作廢，需重新計算後方可執行。

## Final trade card

| Field | Value |
|---|---|
| Direction | LONG（條件式，尚未觸發） |
| Entry zone | $145.18 – $153.35（UNVERIFIED） |
| Entry trigger | 三項須同時成立：(1) 執行閘門驗證現價落於進場區間；(2) 財報後低點起**連續 10 個交易日無新低**；(3) 當月無新增執行層 Form 4 單月套現 > $10M |
| Stop | $138.02（UNVERIFIED，錨點 -10%） |
| Target 1 | $176.35（UNVERIFIED） |
| Target 2 | $199.36（UNVERIFIED） |
| Size | Small — 首批 **NAV 1%**；Q3 財報正面確認後上限 NAV 2.5% |
| Horizon | 1–3 個月，核心驗證節點 2026-11-04 |
| Conviction | M（5/10） |
| R:R to T1 | 2.4（T2 為 4.5） |

Call spread 變體不核准：IV 結構未經驗證，在 PRICE_DATA_UNAVAILABLE 下加一層無法定價的風險，不予採用。

## Risk debate adjudication
- Aggressive 最強論點：Stop 已給足空間，NAV 1% 的絕對損失僅 0.075% NAV，倉位小到讓正確判斷失去組合意義。
- Conservative 最強論點：ATR UNAVAILABLE 且已知單日 -12.5% 跳空能力，「-10% 的 Stop」不等於「-10% 的真實保護」，跳空實損可達計劃 1.5–2×。
- Net：**採納 neutral**。激進方把長週期基本面信心（連八季 60%+）直接換算為短週期倉位，時間維度錯置；保守方把合計 ~75% 概率的尾部情境正常化為基準情境，且在已知跳空環境下收窄 Stop 至 -7% 邏輯上劣於 -10%。裁定：維持 **10 個交易日整固門檻 + NAV 1% 首批**，Stop 維持 $138.02 UNVERIFIED。

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營收成長動能 | 連續八季 YoY 60%+，Q3 指引 $860–870M（+47–49%） | Q2 營收超預期 10.3%、EPS 超 31.6% | 成立 |
| 廣告生態擴張 | 廣告主數 YoY >50%、美國 ARPU $11.30（+50%） | 數據仍支撐 | 成立 |
| AI 授權護城河 | $130M/yr 近 100% 毛利 | Google + OpenAI 雙客戶 100% 集中度未解除 | 觀察中 |
| 市場接納度 / 價格行為 | S&P 500 納入帶來持續機構流入 | 財報日 -12.5% + 執行層 $75M+ 套現，distribution 未解除；被動買盤一次性窗口已於 08-18 關閉 | 已失效 |

第四根支柱已失效，正是首批倉位鎖在 NAV 1% 且必須等 10 日整固的直接理由。

## 論點失效條件（與 Stop 分開）
- 若 Google 或 OpenAI 任一方公開縮減／終止授權協議 → **取消進場；已進場則出場**。
- 若 Q3 2026（2026-11-04）營收低於指引下緣 $860M → **出場**。
- 若 Q3 財報日再現單日 -8% 以上跌幅 → distribution 雙重確認，**出場，倉位歸零**。
- 若廣告主數 YoY 增速跌破 50% → **減碼至 0.5% NAV**。
- 若整固期間再現單月執行層套現 > $10M → **延後進場，門檻重新計時**。

## Monitoring trigger
若整固期間出現 AI 授權新增第三家客戶的正式公告，可提前觸發進場，但首批上限仍鎖 NAV 1%；反之若股價跌破錨點 -7%（$142.62 UNVERIFIED）而未觸及 Stop，須在 Stop 被打到前重新評估論文。

## Catalyst calendar
- 2026-08-31 前後 — 執行層 10b5-1 秋季套現節奏監控窗口
- 2026-10（預估）— Meta / Alphabet 業績作為 Q3 廣告市場前瞻指標
- **2026-11-04 — Q3 2026 財報（最關鍵驗證節點）**
- 2026-11-21 — 財報後選擇權到期週，觀察 IV 結構
- 2027 上半年 — AI 授權新客戶擴展與合約續簽週期

## Metrics summary

| Metric | Value | 備註 |
|---|---|---|
| Verdict | HOLD / WATCHLIST | 新倉，MODIFY 核准 |
| Conviction | 5 / 10 | NEUTRAL 偏多 |
| Anchor price | $153.35 | UNVERIFIED |
| Entry zone | $145.18 – $153.35 | UNVERIFIED |
| Entry midpoint | $149.27 | UNVERIFIED |
| Stop | $138.02（-10%） | UNVERIFIED |
| Target 1 | $176.35（+18.1%） | UNVERIFIED |
| Target 2 | $199.36（+33.6%） | UNVERIFIED |
| Risk per share | $11.25 | UNVERIFIED |
| R:R to T1 / T2 | 2.4× / 4.5× | — |
| 首批 Size | NAV 1% | 上限 2.5%（Q3 後） |
| 計劃止損損失 | NAV 0.075% | 跳空情境約 0.125% |
| ATR / 年化波動率 | UNAVAILABLE | 代理封鎖 |
| Horizon | 1–3 個月 | 節點 2026-11-04 |
| Price data status | PRICE_DATA_UNAVAILABLE | 執行閘門強制生效 |

FINAL DECISION COMPLETE
