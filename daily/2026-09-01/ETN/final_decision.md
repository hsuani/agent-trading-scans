# Final decision — ETN as of 2026-09-01

FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## 部位狀態判定
ETN **不在** `pipeline/tools/held_tickers.txt` 內 → 屬**新倉決策**，問題是「該不該進」，
而非「該不該續抱」。裁定為 REJECT（不建立新倉），非賣出訊號。第一行 HOLD = 不動作、
維持零部位。

## Conditional watch card（非可執行單，僅為條件觸發後之預備參數）
**PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位。** 以下數字全部來自
investment_plan 內部推算與風險辯論，未經即時 S/R 驗證，**不得直接掛單**。

| Field | Value |
|---|---|
| Direction | LONG（條件成立後） |
| Entry zone (conditional) | $360 – $375（對應調整後 P/E 18–20x） |
| Stop | $355（PRICE_DATA_UNAVAILABLE，須以實際 ATR 重驗） |
| Target 1 | $393（DCF 公允值中值上緣） |
| Target 2 | $460（關稅輕 + Q3 財報強之牛市情境） |
| Size | Small — 首筆 0.25% NAV，Q3 確認後方可升至 0.5% NAV |
| Horizon | 3–6 個月（覆蓋關稅 + Q3 財報） |
| Conviction | L — 約 30%（不進場的信心度約 70%） |
| R:R to T1 | 2.2（$375 進場、$355 停損、$393 目標；僅為條件情境試算） |

## Risk debate adjudication
- **Aggressive 最強論點**：內部人淨賣出 $2,200 萬僅佔市值約 0.04%，被過度放大為關鍵
  阻礙，比例感失衡；且「三條件同時成立」在時序上不可能（關稅 09-08、財報 10 月、
  技術確認），等於策略癱瘓而非紀律。這兩點我接受。
- **Conservative 最強論點**：$375–$390 的所謂「安全邊際」對應調整後 P/E 仍有 27–28x，
  而熊方 DCF 中值上緣僅 $393 — 在該區間進場等於在公允價值上緣買入，緩衝是負的。
  在 PRICE_DATA_UNAVAILABLE 下用內部推算值錨定進場點，更是雙重不可信。
- **Net**：我採 **neutral** 權重最高。基本面硬數據（積壓訂單 +43%、book-to-bill 1.3、
  Electrical Americas 毛利率 27.5%）確實成立，所以不做空；但估值已把故事完全定價，
  上行 +13% vs 下行 -36%，在沒有任何即時報價可驗證的情況下，任何新倉都是在對
  不可信的數字下注。Aggressive 的 Call Spread 提案結構合理，但**在無即時報價與無
  IV 數據時無法定價權利金**，同樣不可執行 — 這是本次 REJECT 的技術性理由之一。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 資料中心訂單動能 | 積壓訂單 YoY >40%、book-to-bill >1.2 | 積壓 +43%、Americas 1.3 | 成立 |
| 定價能力 / 毛利率擴張 | Electrical Americas 毛利率創高並維持 | Q2 27.5% 歷史新高，但 09-08 關稅未計入 | 觀察中 |
| 估值安全邊際 | 進場價 ≤ DCF 中值 | 現價 ~$413 vs DCF $321–$393，安全邊際為負 | 已失效 |
| Boyd 整合 / FCF 品質 | $200–300M 協同、FCF 跟上 EPS | FCF +8–12% 落後 EPS +12%，CapEx 3.4%→4–5% | 觀察中 |

**唯一已失效的是估值支柱 — 這正是拒絕新倉的核心原因，而非基本面轉弱。**

## 論點失效條件
（與 Stop 分離：Stop 是價格紀律，以下是論點紀律，論點先壞即動作，不等價格）
- 若 Meta 或 Google 公告 2027 年 capex 指引年增 <10% → 訂單動能支柱失效 → **永久出場觀察名單，不再考慮建倉**
- 若 Q3 2026 財報 Electrical Americas 毛利率 <26.5% → 毛利率支柱失效 → 條件觸發全部作廢
- 若 Boyd 首次整合季報年化協同 <$140M（折扣 >30%）→ 整合支柱失效 → 不建倉
- 若上述皆未發生但股價未回落至 $375 以下 → 估值支柱維持失效 → **維持零部位**

## Monitoring trigger
09-08 關稅生效後 48 小時內，若實際執行範圍未涵蓋 Eaton 主力電力元件進口，**且**
即時報價恢復並確認股價進入 $360–$375 並守穩，才升級為 Small (0.25% NAV) 試探倉。
兩者缺一即維持 REJECT。

## Dealbreaker（明說）
估值支柱已失效：現價高於任一 DCF 情境中值，R:R 不足 1.5x LONG 門檻；且在
PRICE_DATA_UNAVAILABLE 下無法驗證任何進場、停損或選擇權定價。**未來重啟的唯一條件**
是即時報價恢復 + 股價實際進入 $360–$375 + 09-08 關稅衝擊低於預期，三者同時成立。

## Catalyst calendar
- 2026-09-08 — 美加關稅（鋼鋁 25%/10%）正式生效，近期最關鍵風險事件
- 2026-10（預期） — ETN Q3 2026 財報：Electrical Americas 毛利率、積壓訂單成長、Boyd 初期數據
- 持續監控 — Meta / Google / Microsoft 2027 資料中心 capex 前瞻指引

FINAL DECISION COMPLETE
