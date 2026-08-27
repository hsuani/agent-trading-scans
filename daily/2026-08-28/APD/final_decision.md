FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — APD as of 2026-08-28

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

（APD 不在 held_tickers.txt，屬新倉判定；本次不建立部位，維持 0% NAV。REJECT 對應第一行 HOLD＝不採取任何交易動作。）

## Final trade card
不建倉，故無交易卡。**無即時價格，暫不給進出場價位**（yfinance HTTP 403，Entry / Stop / Target / R:R 全部 PRICE_DATA_UNAVAILABLE）。

| Field | Value |
|---|---|
| Direction | 無（不建倉） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | 0% NAV |
| Horizon | 季度級別（2026-11-05 → 2027 Q1） |
| Conviction | L |
| R:R to T1 | 無法計算 |

## Dealbreaker（本次否決的核心理由）
在無法取得任何價格與技術面資料（5 項評估信號僅 3/5 通過，基本面與市場技術雙 FAIL）的狀態下，對一檔 Forward P/E ~22×、FCF 深度負值、且有 LCEC 成本超支 100% 前例的資本密集型標的建倉，等同盲態下押注管理層執行力。這不是價格問題，是資訊完整度問題——**無價格即無風控，無風控即不建倉**。

## Risk debate adjudication
- Aggressive 最強論點：新聞缺口風險真實存在，Q4 若超預期並上調 FY2027 指引，股價可能跳空重估；0.5% NAV 的絕對損失上限僅 0.125% NAV。此點成立，我承認等待有隱性成本。
- Conservative 最強論點：LCEC 從 $4.5B 燒到 $9B 才認賠 $2.9B，這是「已實現」的執行力證據，而 NEOM 的成本紀律仍是「聲稱」；已投入逾 $5B 且未完工，賠率不對稱（上行 +13% / 下行 −25%）。
- Net：我採納 **neutral** 的框架。Aggressive 的缺口論在數學上自我否定——0.5% NAV 在牛市情境只賺 0.10% NAV，換取的「先機」價值低於盲態建倉的資訊成本；其 Call Spread 建議在 PRICE_DATA_UNAVAILABLE 下根本無法定價，屬空洞主張。Conservative 對 CFO 出脫 $824K 的定性過重（相對 89.51% 機構持股僅屬注意訊號），且低估了 Yara 佣金制協議相對 LCEC「先建後賣」的結構性改善。Neutral 的「零倉位現在、0.25% NAV 有條件試倉」是唯一同時尊重上行期權與執行風險的路徑。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 核心工業氣體定價力 | 利潤率持續擴張、EPS 超預期 | Q3 FY2026 EPS $3.47（+3.3% 超預期），利潤率 +100 bps 至 25.6%，全年指引上調至 $13.39–$13.49 | 成立 |
| NEOM 第二曲線兌現 | 2027 年商業啟動、Yara 承接銷售 | 完工 90%+、Yara 協議已簽，但商業啟動日期未經 Q4 財報重申 | 觀察中 |
| Capex 頂點與 FCF 轉折 | FY2026 為 capex 高點，FCF 朝正值改善 | FY2026 capex $3.5B，FCF 深度負值，尚無轉折證據 | 觀察中 |
| 管理層資本配置紀律 | 大型項目成本可控 | LCEC 超支 100%（$4.5B → $9B）後才停損，$2.9B 減值 | 已失效 |

## 論點失效條件
可證偽，與 Stop 分離（此處為論點紀律，非價格紀律）：
- 若 2026-11-05 Q4 FY2026 調整後 EPS < $3.45，或 FY2027 指引低於 $14.00 → 「定價力」支柱失效 → 整個觀察名單移除，不再追蹤進場條件。
- 若管理層在 Q4 財報未明確重申 NEOM 2027 Q1 商業啟動、或將時間表推遲至 2028 年以後 → 「第二曲線」支柱失效 → 永久放棄進場，板塊需求改配 LIN。
- 若 FY2027 capex 指引再度上修（高於 $3.5B），或出現第二筆 ≥$1B 氫能項目減值 → 「capex 頂點」支柱失效 → 放棄進場。
- 若 IRA Section 45V 稅額抵免遭立法削減至 $0.60/kg 以下 → 美國氫業務回報基礎失效 → 放棄進場。

## 有條件的進場路徑（0.25% NAV 試倉）
以下條件須**同時**滿足，方可於 2026-11-05 後建立 0.25% NAV 試探性多頭倉：
1. Q4 FY2026 調整後 EPS 落於 $3.55–$3.65 或以上；
2. 管理層明確重申 NEOM 2027 Q1 商業啟動時間表；
3. FY2027 capex 指引顯示 NEOM 後正常化軌跡（不再上修），GAAP 與調整後 EPS 差距收窄；
4. 價格資料恢復（yfinance 代理封鎖解除），可計算 ATR 與可執行的 Stop。
任一條未達，維持 0% NAV。建倉後升至正常倉位須待 2027 Q1 首批氨量產公告。

## Monitoring trigger
若 2026-10-22 Linde Q3 財報顯示工業氣體板塊定價力普遍鬆動（利潤率 YoY 收縮），提前下修 APD 定價力支柱評等，無須等到 11 月財報。

## Catalyst calendar
- 2026-10-22 — Linde Q3 2026 財報（板塊定價力對照組）
- 2026-11-05 — APD Q4 FY2026 財報（EPS、FCF 軌跡、FY2027 capex 指引）
- 2027 Q1 — NEOM 綠氫商業生產啟動公告

---

## FINAL TRANSACTION PROPOSAL

- **VERDICT: HOLD** (zero position, no new capital deployed)
- **CONVICTION: 25%** (LOW)
- **NAV ALLOCATION: 0.0% NAV**
- **CONDITIONAL PATH: 0.25% NAV trial long**, contingent on simultaneous satisfaction of: (1) Q4 FY2026 adjusted EPS $3.55–$3.65 or above on 2026-11-05; (2) management reaffirmation of NEOM 2027 Q1 commercial startup; (3) FY2027 capex guidance showing post-NEOM normalization with no further upward revision; (4) restoration of price data (yfinance 403 lifted) enabling an executable Stop.
- **ENTRY / STOP / TARGETS: PRICE_DATA_UNAVAILABLE** — 無即時價格，暫不給進出場價位。

## Metrics

| Metric | Value |
|---|---|
| Ticker | APD |
| Decision date | 2026-08-28 |
| Verdict | HOLD (REJECT new entry) |
| Position status | 未持有（不在 held_tickers.txt） |
| NAV allocation | 0.0% |
| Conditional NAV | 0.25%（條件達成後） |
| Conviction | 25% (L) |
| Horizon | 季度級別（3m+） |
| Entry / Stop / T1 / T2 | PRICE_DATA_UNAVAILABLE |
| R:R to T1 | 無法計算 |
| Signals passed | 3/5（基本面 FAIL、市場技術 FAIL） |
| Pillars 成立 / 觀察中 / 已失效 | 1 / 2 / 1 |
| Dominant risk view | Neutral |
| Next review | 2026-11-05（Q4 FY2026 財報） |

FINAL DECISION COMPLETE
