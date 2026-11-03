FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — IPGP as of 2026-11-04

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 判定說明
新倉 (不在 held_tickers.txt)。核准交易員「法說會前不建方向性部位」的主軸, 但修改條件性 LONG 的參數: 停損由 $69.41 收緊至進場價下方約 1.2×ATR, 進場區上緣由 $81.82 降至 $78.50 (不追價), 倉位由「半倉以下」改為 Small 分批。法說會前不建任何部位, 含選擇權 —— 財報前一日 IV 已反映事件, call spread 的「不對稱」多半被權利金吃掉, 而且 Crux 2 (FCF 低於 SBC) 尚未驗證, 現在押多等於只用損益表數據押注現金流也會跟上。

## Final trade card (條件性, 僅在 11-04 後觸發條件成立才生效)
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $76.38 – $78.50 (需放量收盤站上 MA50 後, 分 3 批, 首批 ≤1/3) |
| Stop | $73.40 (收盤確認; 約進場中值 −1.2×ATR) |
| Target 1 | $86.42 |
| Target 2 | $94.66 |
| Size | Small (風險上限 0.5% NAV; 建滿後部位約 3–4% NAV) |
| Horizon | 2–6 週, 事件驅動 |
| Conviction | L |
| R:R to T1 | 2.2 (以 $77.50 進場計) |

未觸發前: 空手。

## Risk debate adjudication
- Aggressive's strongest point: Q3 營收與營業利益已由 8-K 證實優於財測, 股價卻仍貼近 52 週低點, 加上 24.9% short float, 若 guidance 正面, 第一天的軋空漲幅確實會被「等 2–3 天確認」讓掉。這是真實成本, 我承認。
- Conservative's strongest point: 法說會跳空會讓 $68.00 的現股停損無法以掛單價成交, 「0.05% NAV 最大虧損」是紙上數字; 且原案停損距離達 2.2–3.8×ATR, 以 0.5% NAV 風險反推根本建不出有意義的倉位。
- Net: I weight **conservative** more here because 讓掉第一天漲幅的代價是可量化、可承受的 (進場價差幾塊錢), 而押錯方向的代價是跳空穿越停損, 不可控。Q3 beat 是已知資訊, 市場已有 8-K 可讀, 股價仍在低檔本身就說明市場在等 guidance 與現金流, 不是在等我。Neutral 的 call spread 方案邏輯合理, 但在財報前一天進場, 權利金定價已含事件 IV, 我不認為 0.1–0.2% NAV 的賭注值得多一個部位去管。

## 論點支柱 (條件性 LONG 的假設)
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Q4 guidance 與毛利率 | 中位數優於共識, 調整後毛利率 ≥40% | 11-04 揭露, 尚無資料 | 觀察中 |
| 獲利轉現金 | Q3 營運現金流為正, 存貨增速不高於營收增速 | TTM FCF $20.8M < SBC $41.4M, 存貨天數 184 天 | 觀察中 |
| 淨現金底板 | 總負債 $16.3M, 流動比率 6.18, Lumibird 交割後淨現金仍 ≥$11/股 | 8-K 已證實, 交割待法國 FDI | 成立 |
| 技術面轉強 | 放量收復 MA50 $76.38 | MA20<MA50<MA200, 死亡交叉 | 尚未成立 (進場前提) |

## 論點失效條件
與 Stop 分開: Stop 是價格紀律, 以下是論點紀律, 論點先壞就先動作。
- 若 Q4 guidance 營收中位數低於共識, 或毛利率指引 <40%, 支柱一失效 → 條件性 LONG 作廢; 已進場則出場。
- 若 Q3 營運現金流為負, 或存貨 YoY 增速高於營收增速 5 個百分點以上且連續兩季 (Q3、Q4), 支柱二失效 → 已進場則減碼至 1/3, Q4 再確認即出場。
- 若 Lumibird 交割因 FDI 審查破局、延後超過一季, 或交易條件實質改變 (現金對價上調), 支柱三失效 → 出場。
- 若法說會後 3 個交易日內未能收盤站上 MA50 $76.38, 進場前提不成立 → 條件性 LONG 作廢, 下次掃描重評。

## Monitoring trigger
If 11-04 法說會後首日股價跳空幅度超過 ±2×ATR (約 ±$6.50), 重評進場區與停損距離, 不得沿用本卡的數字直接進場。
If 收盤跌破 $69.41 並跌破 52 週低點 $68.27, 轉為 SHORT_OR_AVOID 評估, 但因 short ratio 9.4 日, 做空門檻 R:R ≥2 且倉位減半。

## Catalyst calendar
- 2026-11-04 — IPGP 法說會: Q3 調整後 EPS/EBITDA、營運現金流、存貨、Q4 guidance
- 2026-11-05 ~ 11-07 — 法說會後 2–3 個交易日價能確認 (MA50 $76.38 收復與否)
- 後續追蹤 — Lumibird 交割與法國 FDI 審查進度 (影響淨現金底板)
- 2027-02 (預估) — Q4 財報, 驗證支柱二 (FCF 轉正) 第二季資料

FINAL DECISION COMPLETE
