FINAL TRANSACTION PROPOSAL: **HOLD**

# LAES — 最終決策 2026-09-08

## 決策結果

**HOLD（新倉 verdict：REJECT — 不建立部位，0% NAV）**

LAES 不在 `held_tickers.txt`，屬新倉判定。否決的理由不是「故事不好」，而是三個獨立的否決點同時成立：市場價格全面 PRICE_DATA_UNAVAILABLE（無法定 entry / stop / 部位風險）、fundamentals 全欄位 DATA_UNAVAILABLE（估值只能靠分析師目標反推，屬循環論證）、以及論點的唯一樞軸（QVault FIPS 140-3 / Common Criteria 認證）在 2026-09-21 FIPS 140-2 日落當日尚未到位。沒有價格就沒有風險紀律，沒有紀律就不該下單。

## 信心度

**78% conviction**（對「暫不進場」這個決定的信心；對多頭論點本身的信心為 LOW）

## 進出場價位

| 欄位 | 值 |
|---|---|
| Direction | 無部位（AVOID） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | 0% NAV |
| Horizon | Q4 2026 認證窗口至 2027-01 CNSA 2.0 |
| Conviction | L |
| R:R | 無法計算 |

## 理由摘要

**風險辯論裁決。** Aggressive 最強的一點是事件密度：FIPS 日落、OMB 90 天備忘錄、wolfTPM 整合公告集中在同一個月，且 call spread 以 premium 作天然損失上限，確實繞開了無法設 stop 的技術障礙。Conservative 最強的一點是知情資金：6 個月 33 筆內部人交易全為賣出、0 筆買入，CFO 一人 22 筆共 195,664 股，同期機構空頭增加 16.84% 至流通股 19.86%——這兩股資金的資訊優勢明顯高於僅 2 位分析師的覆蓋共識。

**我採納 neutral 的事實判斷、conservative 的執行結論。** Neutral 點破了 aggressive 的事實性錯誤：9 月 21 日 LAES 手上沒有 FIPS 140-3 資質，聯邦採購只能流向 Thales、NXP、IDEMIA。這個日期是賽道催化劑，不是個股催化劑，方向上甚至對 LAES 不利。而 aggressive 的 call spread 方案同樣不可執行——沒有標的現價就無法判斷行使價的價內外程度、無法評估 premium 是否合理，「premium 即 max loss」只限制了損失金額，不構成正期望值。

**Conservative 的四重門檻我修剪為兩重**：CMVP 資料庫可核實的認證公告 + 至少一份載明金額的聯邦或企業採購合約。要求 CFO 賣出歸零過苛，等同永不進場。

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 監管強制需求 | 行政命令 14412、FIPS 日落、CNSA 2.0 形成硬性期限 | 法規文本確實存在，期限未變 | 成立 |
| QVault 認證按期落地 | 2026 Q4 取得 Common Criteria / FIPS 140-3 | 8 月時程已「微調」，日落日仍無資質 | 觀察中 |
| $225M 管道轉換 | 規模化合約落地 | 僅 Quobly $5M 一筆，有機增長未拆分揭露 | 觀察中 |
| 內部人與估值支撐 | 管理層與股價同向 | 33 筆全賣、空頭 19.86% 且增加 | 已失效 |

## 論點失效條件

與 Stop 分離（本案無 Stop，僅有論點紀律）：

- 若 QVault Common Criteria / FIPS 140-3 認證公告延至 2027-04 之後 → 論點永久失效，移出觀察清單
- 若 Q3 2026 單季營收低於 $7M（FY 指引下限 $27M 的當期斜率）→ 管道支柱失效，不再評估進場
- 若 CFO 累計賣出超出 195,664 股，或空頭佔流通股突破 25% 且續增 → 知情資金支柱確認失效
- 若 Intel / NXP 在 IoT 端點 PQC 取得 FIPS 140-3 資質 → 差異化護城河失效

## 風險因素

主要風險是機會成本而非資本損失：若認證於 Q4 如期落地並疊加 19.86% 空頭回補，初段漲幅將完全錯過。我接受這個代價——在價格與基本面雙盲的狀態下建倉，風險是不可量測的，而不可量測的風險不能靠縮小部位解決。

## Monitoring trigger

CMVP 資料庫出現 QVault TPM 收錄紀錄，或 SEALSQ 公告載明金額的聯邦採購合約時，立即重跑完整分析；同時要求價格數據源恢復（yfinance 403 解除）方可討論部位。

## Catalyst calendar

- 2026-09-21 — FIPS 140-2 日落（受益者為競爭對手，非 LAES）
- 2026-09 月底 — OMB 90 天 PQC 遷移備忘錄
- 2026-10-31 — WISeSat.Space SPAC 合併外部截止日
- 2026-12 — QS7001 Common Criteria / ANSSI 認證目標日（關鍵）
- 2027-01 — CNSA 2.0 生效

FINAL DECISION COMPLETE
