FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — 2301.TW (光寶科技) as of 2026-09-01

## FINAL VERDICT: **BUY**（條件式分批，非即刻市價追入）

## Verdict
MODIFY

> 部位定位：**新倉**。2301.TW 不在 `pipeline/tools/held_tickers.txt`，本決策回答的是「該不該進」，不是「該不該續抱」。
> 價格狀態：**PRICE_DATA_UNAVAILABLE**（Yahoo Finance HTTP 403）。所有價位欄位一律待報價恢復後確認；文中引述之 250 / 308 / 370 TWD 均為**非即時報價**的分析師與辯論文件參考值。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認 |
| Stop | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認（框架：進場價下方 8–10%，以即時 ATR 校準，取 20 日均線下方者為準） |
| Target 1 | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認（參考分析師高端目標 370 TWD，非即時報價） |
| Target 2 | PRICE_DATA_UNAVAILABLE — 待報價恢復後確認（2027 EPS 上修情境，非即時報價） |
| Size | Small-to-Medium — **首批 1.0% NAV，上限 1.5% NAV** |
| Horizon | 1–3 個月（核心驗證節點 2026-10 月 Q3 財報） |
| Conviction | M — **60%** |
| R:R to T1 | 無法計算（進場與停損皆為 PRICE_DATA_UNAVAILABLE）；執行前須確認 ≥ 2.0 |

## Key rationale
- **財報硬數據支撐**：Q2 EPS 3.14 TWD（YoY +128%、QoQ +89%）、毛利率 27.2%、營益率 15.6% 三項歷史新高，法說會與多家媒體交叉驗證，不是敘事而是已實現數字。
- **供應鏈壁壘可驗證**：110kW Power Shelf 進入 NVIDIA Vera Rubin NVL72 核心電源方案，65 焦耳/GPU 儲能模組認證週期 18–24 個月，短期無替代者。
- **估值安全墊已耗盡**：股價據引述已高於分析師中位數目標約 23%，加上雙廠 capex 壓縮 FCF，方向對但價格貴 —— 故降信念、縮首批、要求觸發條件，而非否決。

## Top risk
AI capex 週期轉折使估值框架由 AI 成長股 P/E 28–35× 回歸 EMS 歷史 P/E 12–18×，下行 40–55%，遠超任何百分比停損的保護範圍。此為跳空型風險，只能靠**小倉位**而非停損管理。

## Entry trigger
硬性前提：**PRICE_DATA 恢復並可計算即時 RSI 與 ATR**（採保守方底線）。前提滿足後，下列任一達成即建首批 1.0%（採激進方「任一即可」而非「全部滿足」）：
1. RSI 14 回落至 60 以下；或
2. 股價於 20 日均線附近整理 ≥ 5 個交易日且量能收縮。
（除息填息僅為次要參考，不單獨構成觸發。）
加碼至 1.5% 的唯一條件：Q3 EPS ≥ 2.5 TWD 且毛利率維持 27%+。**不預設加碼至 2.5%。**

## Stop condition
價格紀律：進場價下方 8–10%，報價恢復後以即時 ATR 校準；若 20 日均線位置更近，以均線下方 1–2% 為準。單筆最大損失控制在 0.10% NAV 以內。

## Risk debate adjudication
- Aggressive 最強論點：等待三個條件全部滿足，在強動能股上等同永不進場，機會成本真實存在。
- Conservative 最強論點：在無法計算 ATR 與實際停損金額時建倉，等同盲目追高；且 Scenario A 的下行遠超停損保護。
- Net：我採 **neutral** 權重最高。激進方的 2.5% 倉位與 12–14% 停損缺乏即時 ATR 依據，是用信心取代數據；保守方的 5–6% 停損在三日 +17.62% 的股票上必被震出。折衷結論：**保守方的「等報價」前提 + 激進方的「任一觸發即進」節奏 + 中性方的倉位與停損區間**。不採納對沖建議 —— 1.0% NAV 的部位用指數 Put 對沖，成本大於效益。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 電源獲利動能 | 毛利率維持 27%+、EPS 季增 | Q2 毛利率 27.2%、EPS QoQ +89% | 成立 |
| NVIDIA NVL72 設計鎖定 | 18–24 個月無替代者 | 認證壁壘尚未被挑戰 | 成立 |
| 估值安全邊際 | 股價低於分析師共識目標 | 高於中位數目標約 23% | 已失效 |
| DenseLight / CPO 長期期權 | 2027H2 外部光源商機 | 21% 少數股權、無控制力、純現金流出 | 觀察中 |

## 論點失效條件
- 若 2026-10 月 Q3 EPS < 2.5 TWD 或毛利率跌破 25%，「獲利動能」支柱失效 → **出場**（不等停損）。
- 若台達電（2308.TW）取得 NVL72 Power Shelf 獨家規格訂單，「設計鎖定」支柱失效 → **出場**。
- 若 Meta / Microsoft / Google 任一家正式下修 2027 年 AI capex 指引，估值框架支柱失效 → **減碼至零**。
- 若連續兩季 FCF 為負且國內＋德州 capex 再度上修，資本紀律支柱失效 → **減碼一半**。

## Monitoring trigger
若 PRICE_DATA 恢復後即時 R:R 至 T1 低於 2.0，或報價顯示股價已再漲逾 10%（安全邊際進一步惡化），取消本次建倉授權，重跑 Phase 2。

## Catalyst calendar
- 2026-09-11 — 除息日，觀察填息動能
- 2026-10 月 — Q3 財報（核心驗證節點：毛利率 27%+、EPS 季比）
- 2026-Q4 — 高雄二期廠、越南廣寧廠啟動，觀察產能利用率
- 2026-H2 — 800V HVDC 出貨量化
- 2027-H2 — DenseLight InP CPO 商機評估節點

FINAL DECISION COMPLETE
