FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — CEG as of 2026-10-28

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 持倉判定
CEG 不在 `pipeline/tools/held_tickers.txt`，屬新倉。問題是「該不該進」，不是「該不該續抱」。結論：財報前不建立方向性部位；只核准一筆 0.5% NAV 的觀察用試單，作為追蹤工具而非多頭表態。第一行寫 HOLD，因為 0.5% 試單不構成方向訊號。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（觀察用試單，非方向性部位） |
| Entry zone | $252.50 – $262.00（不追價至 $265.78 以上） |
| Stop | $247.20 收盤跌破（雙底結構失效），不採 2×ATR $233.40 |
| Target 1 | $281.11（MA200） |
| Target 2 | $305.80（2026-09-08 前高） |
| Size | Small（0.5% NAV）；財報前不加碼 |
| Horizon | 至 2026-11-09 Q3 財報及其後 2 週 |
| Conviction | L（試單）；方向性判斷為 M |
| R:R to T1 | 1.9（以 $258.98 計，風險 $11.78 vs 報酬 $22.13） |

對 neutral 方案的修改：(1) 否決「財報前技術面改善可加至 1% NAV」——RSI 站上 50 不回答 FCF 問題，且 12 天內有 FOMC、VST 財報、CEG 財報三個事件風險疊加 67.1% 年化波動；(2) 財報確認後首次加碼上限為 1/3 倉（採 conservative），且不必等 1–2 週（採 neutral），收盤站回 $273 並放量才補至半倉。否決 aggressive 的 Call Spread 疊加與 1.5–2% NAV 財報前建倉。

## Risk debate adjudication
- Aggressive's strongest point: 要求「收盤站回 $273 且放量」才轉多，若財報報喜直接跳空，規則會變成追高進場。這點成立，所以財報確認後的加碼不再附加 1–2 週等待。
- Conservative's strongest point: 倉位跳升速度不得快於基本面驗證速度。淨負債 +349%、FCF/淨利 0.09x、GAAP 與 adjusted EPS 落差（Q2'26 1.42 vs 2.55）都尚未被 Q3 驗證，單一技術訊號不能授權半倉以上。
- Net: I weight **neutral** more here, 財報前倉位則偏向 conservative。理由：Crux 1（整合後 FCF 與去槓桿）在 11-09 才有答案，財報前沒有資訊優勢；0.5% NAV 以 $247.20 停損的 $ 風險僅約 0.023% NAV，當追蹤工具可接受，當方向性部位則不足以支撐。Aggressive 以分析師目標價 $339 算出 6.9:1 的 R:R，忽略多方自己的 base case（20x × $12.15 ≈ $243）低於現價。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 長約需求能見度 | Google 3.59GW（2028 起）、Meta 1.1GW（2027-06 起）合約有效 | 2026-10-06 公告，Reuters 等多家一致；Meta 合約日期未確認 | 成立 |
| Calpine 整合後現金流修復 | Q3 季度 FCF 轉正、淨負債自 24.00B 下降 | Q4'25–Q2'26 連續三季 FCF 為負（-0.181B、-0.850B、-0.118B），Brazos Valley $860M 尚未入帳 | 觀察中 |
| 盈餘指引 | 全年 adjusted EPS $11.50–12.50 維持或上修 | 8 月上修 $0.50，公司表示 Q3 電話會議重審 | 觀察中 |
| 技術結構 | $247.20 雙底守住，收盤站回 $273 | 雙底守住，10-27 反彈但量縮（3.18M vs 10 日均 3.37M），三均線空頭排列、死亡交叉延續 | 觀察中 |

## 論點失效條件
必須可證偽，且與 Stop 分開（Stop 是價格紀律，這裡是論點紀律）。
- 若 Q3 季度 FCF（OCF − Capex）再度為負（連續第四季），現金流修復支柱失效 → 試單出場，不等價格打到 $247.20
- 若 2026-09-30 淨負債 ≥ 24.00B（含 Brazos Valley 出售款仍未下降），去槓桿支柱失效 → 不加碼，試單減半
- 若全年 adjusted EPS 指引下緣下修至 $11.50 以下，盈餘支柱失效 → 出場
- 若 Google 或 Meta 任一合約公告終止或供電時程延後超過 12 個月，長約支柱失效 → 出場
- 若 VST 11-06 下修 2026 指引且 CEG 當日收盤跌破 $252.48，技術支柱轉為失效邊緣 → 試單減半，財報前不補

## Monitoring trigger
If 2026-10-28 FOMC 偏鷹（點陣圖上修或聲明刪除寬鬆傾向）且 CEG 當日收盤跌破 $252.48，re-evaluate 試單是否在財報前提前出場，不等 $247.20。
If Q3 確認 FCF 轉正 + 淨負債 < 24.00B + 指引維持/上修，且財報當日或次日收盤 > $247.20，於 2 個交易日內加碼至 1/3 倉；收盤 > $273 並伴隨量 > 3.37M，補至半倉。

## Catalyst calendar
- 2026-10-28 14:00 ET — FOMC 利率決議（預期維持 3.75%–4.00%）
- 2026-11-06 — VST Q3 財報（同業領先指標，ERCOT 遠期價已預警走弱）
- 2026-11-09 盤前 — CEG Q3 財報（adjusted EPS 共識 $3.79–3.96；核心檢驗：季度 FCF、淨負債、全年指引）
- 2026-11-09 至 11-23 — 財報後反應窗口，觀察 $247.20 / $273 兩個價位
- 日期未定 — NRC Crane 最終 EA/FONSI；FERC 對 PJM 大型負載規則後續命令

FINAL DECISION COMPLETE
