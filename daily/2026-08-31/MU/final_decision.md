# Final decision — MU as of 2026-08-31

FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> 步驟 0：MU 不在 `held_tickers.txt` 內 → 新倉，走 A 框架。問題是「該不該進」。
> 全篇 PRICE_DATA_UNAVAILABLE（Yahoo Finance 403），所有進出場條件一律以事件與
> 數據門檻表述，不填任何價位。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | 無價位。第一批：業績前 5 個交易日內買入 call spread（買腳貼近市價上方一檔、賣腳設於 CEO 套現價區間或以上，到期 2026-10-17）。第二批：僅在 2026-09-30 業績「三重確認」後才建立股票倉 |
| Stop | 無價位。Options 段無停損（最大損失＝premium，結構性封頂）。股票段：進場後 ATR × 2（待即時報價恢復後計算並回填），且下列任一論點失效條件觸發即無條件出場 |
| Target 1 | 業績確認 EPS ≥ $31 且毛利率 ≥ 85%，call spread 內在價值實現 → 了結 options，保留股票倉 |
| Target 2 | FY2027 HBM 合約量與均價具體指引落地、Forward P/E 重新定價至 15-18x → 股票倉分批減 |
| Size | Small-Medium：業績前 call spread premium 0.75% NAV；業績後股票倉 ≤ 1.25% NAV（分兩批 0.6% + 0.65%）。總敞口上限 2% NAV |
| Horizon | 1-2 季，2026-09-30 為強制重評估點 |
| Conviction | M（MEDIUM） |
| R:R to T1 | 結構性 4-6:1（call spread；實際依成交權利金定價，現無報價無法確認） |

## Risk debate adjudication
- Aggressive's strongest point：業績前 IV 尚未完全墊高，且提出 call spread 這個能把
  binary event 損失封頂的工具——這是全場最有價值的一句話。
- Conservative's strongest point：86% 毛利率指引遠高於 FY2025 的 38-45% 基準，任何邊際
  壓縮都會被市場非線性重新定價；加上 CEO $1,192 套現與機構交易員 72% 看跌的組合。
- Net：我採 **neutral** 較重。保守方正確識別跳空風險，卻用「零部位」這個過度手段解決；
  激進方工具對了但倉位錯了——業績前 2.5-3% NAV 股票倉在 -20% 跳空下，基本面停損
  根本來不及觸發。Neutral 的分層方案（options 承擔事件風險、股票倉只在確認後進場）
  同時解決兩邊的核心顧慮，且總敞口不超過 2% NAV。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| HBM 產能鎖單深度 | 全年產量售罄至 2026 年底、>95% DRAM 產能承諾至 2027 | 多來源確認，但只鎖配額、是否鎖均價未證實 | 觀察中 |
| 近期盈利兌現力 | Q4 指引 EPS $31、毛利率 86% | Q3 EPS $25.11 超預期 24.31%，Q4 尚未公布 | 成立 |
| 供給側競爭壓力 | Samsung 2026 擴產 50%、2027 位元份額 41% | 產能 18-24 個月後到位，與合約到期窗口重疊 | 觀察中 |
| 籌碼與內部人訊號 | 分析師 43/47 Strong Buy | CEO $1,192 套現 $46M；機構交易員 72% 看跌 | 已失效（負向） |

## 論點失效條件
- 若 2026-09-30 EPS < $31 或毛利率 < 85%，「盈利兌現力」失效 → 股票倉不建立、既有 options 到期作廢處理，**出場**。
- 若法說會未給出 FY2027 HBM 具體合約量與均價（僅模糊措辭），「鎖單深度」失效 → **不建股票倉**。
- 若 DDR5 套裝現貨月均價連續兩個月季環比下滑（Sourceability / Counterpoint），週期頂訊號 → **減碼**。
- 若 Samsung 公告 HBM 良率突破並加速 2026 下半年交付，「供給側」失效 → **減碼至零**。

## Monitoring trigger
業績前一週若 implied volatility 飆升使 call spread 淨成本超過 premium 預算 0.75% NAV，放棄
建倉、轉為完全觀望；不追高權利金。另若中美晶片戰觸發第二輪中國銷售限制，立即重評估。

## Phase score
**6.5 / 10**。基本面近期動能真實且可查證（+），但價格數據缺失使 R:R 無法量化（-），
籌碼支柱已負向失效（-），且核心決勝點壓在 30 天後的單一 binary event（-）。
分數支撐的是「小額、封頂、事件驅動」的參與方式，不支撐滿倉。

## Catalyst calendar
- 2026-09-30 — Q4 FY2026 業績（最關鍵 binary event，EPS 指引 $31 / 毛利率 86%）
- 2026-10-17 — call spread 到期日
- 每月 — DDR5 套裝現貨價格追蹤
- 未定 — Samsung HBM 擴產／良率公告；Hyperscaler 新一輪多年 HBM 框架協議

FINAL DECISION COMPLETE
