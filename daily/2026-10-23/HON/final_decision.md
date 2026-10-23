FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — HON as of 2026-10-23

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 持倉判定
HON 不在 `pipeline/tools/held_tickers.txt`，屬新倉，問題是「該不該進」。答案：現在不進。交易員 AVOID / 0% 新倉的主結論予以核准；MODIFY 的對象是附帶的「觸發後 LONG 設定」—— 停損從 $204.23 收緊至 $211.26、進場改為分階試單、進場條件由 OR 改為 AND。以下交易卡為**條件式監控設定，目前未啟用，現行曝險 0%**。

## Final trade card (條件式，未啟用)
| Field | Value |
|---|---|
| Direction | LONG（僅於觸發條件全部成立後） |
| Entry zone | $216.13 – $218.10（回測支撐帶企穩、量能萎縮後；不在 BB 延伸段追價） |
| Stop | $211.26（MA20；突破失敗的客觀定義點） |
| Target 1 | $230.67（MA200） |
| Target 2 | $251.64（2026-05-29 區間高點） |
| Size | Small — 首筆 0.25% NAV 試單，pro-forma 數據核實後補至 0.5% NAV 上限 |
| Horizon | 戰術數日至數週（FOMC 10/28、ROK/EMR 11 月初）；論點驗證至 2027-01-28 財報 |
| Conviction | L |
| R:R to T1 | 2.3（以 entry 中位 $217.12、stop $211.26、T1 $230.67 計） |

啟用條件（需同時成立）：(1) 收盤守穩 $216.13 以上並出現回測企穩；(2) 8-K exhibit 99 / 10-Q 原文核實 organic +7% 與分拆後 EV/EBITDA 低於同業中位。若僅技術面成立而數據未核實，最多 0.25% 試單，不得補倉。

## Risk debate adjudication
- Aggressive's strongest point：R:R「約 1:1」是把停損放在遠處的 $204.23 算出來的；改用 $211.26 這個突破失敗點，R:R 到 T1 即達 1.75 以上。這點正確，已採納為停損修正。
- Conservative's strongest point：Scenario B —— 若 pro-forma 揭露 forward P/E 實為 22–26x，那是估值重定價而非技術回檔，收緊的技術停損未必攔得住跳空。這正是研究經理給 LOW conviction 的核心理由。
- Net：我偏向 **neutral**。Aggressive 把「技術確認」當成足以上 Medium 的證據，但本案的多方論點是估值論點，技術面只是進場時機；時機對、論點未核實，不配 1.5–2%。Conservative 要求完全等待文件則會錯過價格發現，且三個尾部情境機率加總 60% 缺乏互斥性檢驗。Neutral 的分階建倉 + 統一停損 $211.26 是兩方真正的共識交集，予以採用。FOMC 距今三個交易日、BB %B 1.09，現在以現股追價沒有理由。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營運動能 | Q3 beat-and-raise 延續，organic 成長 ≥5% | organic +7%、adj. EPS 2.27 超預估 4.88%，全年指引年內第二次上修至 8.40–8.45；惟來源為摘要，10-Q 原文未核實 | 成立 |
| 分拆後估值相對便宜 | EV/EBITDA 顯著低於同業 ~14x | 8.9x 為分拆前口徑；以 2026 指引粗估 EV/EBITDA 落在中高十幾倍、P/E 約 26x，便宜論點很可能不成立 | 觀察中（傾向不成立） |
| 技術面突破有效 | 收復 $216.13/$218.10 後守穩，向 MA200 推進 | 10/22 放量 1.98x 突破、MACD 轉正，但 MA200 之上 -5.4%、死亡交叉未解、BB %B 1.09 過度延伸 | 觀察中 |
| 自動化需求週期 | 同業財報確認需求回升 | ROK/EMR 11/05–11/09 尚未公布 | 觀察中 |

## 論點失效條件
必須可證偽，且與 Stop 分開（Stop 是價格紀律，這裡是論點紀律）。
- 若 8-K exhibit 99 / 10-Q 顯示分拆後 EV/EBITDA ≥ 14x（同業中位）或 FY2026 FCF 指引低於 $1.8B，估值支柱失效 → 撤銷條件式設定，不建倉；已試單者出場。
- 若連續兩個收盤低於 $216.13 且失守 MA20 $211.26，技術支柱失效 → 撤銷設定；已試單者出場（與 Stop 重疊，為同一價位的雙重定義）。
- 若 ROK 或 EMR 任一方將 FY 自動化 organic 成長指引下修至 3% 以下，需求支柱失效 → 不建倉，轉偏空觀察。
- 若 Section 301 關稅正式涵蓋自動化硬體品項，利潤率支柱失效 → 不建倉；已試單者減碼至 0。
- 若 10-Q 原文顯示 organic 成長低於 5%（與摘要 +7% 顯著不符），營運動能支柱失效 → 整個論點重審。

## Monitoring trigger
若 FOMC（10/28）後股價收盤站穩 MA200 $230.67 且 ROK/EMR 釋出正面訊號，在數據核實前即重新評估是否以 0.25% 試單參與；若 10/28 前後收盤跌回 $216.13 之下，提前撤銷設定，不等待 MA20 測試。

## Catalyst calendar
- 2026-10-28 — FOMC 利率決議
- 2026-11-05 至 2026-11-09 — ROK / EMR 財報（自動化需求訊號）
- 待公布 — 8-K exhibit 99 / 10-Q（分拆後 pro-forma EBITDA、淨負債、FCF 核實）
- 2027-01-28 — HON 下一季財報（確認分拆後利潤率是否延續）

FINAL DECISION COMPLETE
