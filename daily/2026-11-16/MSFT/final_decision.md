## FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — MSFT as of 2026-11-16

框架：A 新倉（MSFT 不在 `held_tickers.txt`）。價格資料為 2026-11-13 收盤 $523.88。

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $513.73 – $519.00（限回測守穩後進場，現價不追） |
| Stop | $509.00（收盤確認；11/19 除息日缺口不計） |
| Target 1 | $549.46 |
| Target 2 | $559.15 |
| Size | Medium（1.5% NAV；首批 0.75%，第二批 0.75% 須待 12/9 FOMC 之後） |
| Horizon | 1–3 個月（第一驗證點為估計 2027-01-27 財報） |
| Conviction | M |
| R:R to T1 | 4.5（以中點 $516.37 計，名目值） |

相對原提案的修改：
1. 取消「放量站回 MA20 $529.39」的替代進場路徑。該路徑停損距離 $20.39（約 1.3 倍 ATR），R:R 降到 1.6–2.1，等於另一筆交易；若發生，重新評估，不自動進場。
2. 第二批延到 FOMC 之後，且首批須未跌破 $513.73 收盤。
3. 原提案「收盤跌破 $513.73」與 Stop $509 互相矛盾，統一為：$513.73 失守 = 停止加碼，$509 失守 = 全數出場。
4. 不採用 call spread 衛星倉位，也不升至 Large。

提醒：停損距建倉中點僅 $7.37，約 0.48 倍 ATR（提案寫 0.9 倍，那是從現價算）。R:R 4.5 來自窄停損，不代表勝率高；被洗出場的機率不低，跳空時實際虧損會大於帳面。這是維持 Medium、不加碼的主因。

## Risk debate adjudication
- Aggressive's strongest point: 可驗證的基本面確實紮實（17 季 EPS beat、OCF 136.16B → 195.88B USD、D/E 0.12x），停損觸發時損失僅約 0.02% NAV。
- Conservative's strongest point: 替代路徑風險放大近 3 倍卻未重新定 sizing；FOMC 在持倉期內，同業 11/1 起跌 12%–18%，財報跳空時 $509 擋不住。
- Net: I weight neutral more here because 高 R:R 不等於高勝率，短線三項動能訊號（MACD 柱 -1.83、跌破 MA20、量能 0.87 倍）皆偏空，沒有理由追價或放大倉位；而 conservative 的組合 put 對沖建立在沒有證據的持倉假設上（實際持倉清單中 AI 相關僅 MRVL、ANET、COHR 等，重疊有限），不列為硬性條件。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營運現金與獲利品質 | OCF 持續成長、EPS 持續 beat | TTM OCF 195.88B USD；Q1 FY27 EPS +3.6% | 成立 |
| Azure 加速、CapEx 轉化為營收 | Azure ≥45% | 據報 48%，單一來源、未經官方新聞稿複核 | 觀察中 |
| FCF 於 CapEx 高峰後修復 | 單季 FCF 回升至 20B USD 以上 | 單季 18.63B；FCF/淨利 0.42；CapEx/營收 42.7% | 觀察中 |
| 資產負債表緩衝 | 維持淨現金 | 淨現金 7.09B USD（FY25 為 33.97B） | 觀察中 |

四根中只有一根確定成立，其餘皆待 1 月財報驗證，這是 Conviction 停在 M 的原因。

## 論點失效條件
- 若官方數據顯示 Azure 成長率低於 40% → 出場；介於 40%–45% → 減碼一半。
- 若季報淨現金轉負，或公司宣布舉債支應 CapEx → 減碼一半。
- 若下季單季 CapEx/營收高於 45% 且單季 FCF 低於 15B USD → 減碼一半。
- 若連續兩季 EPS 未優於預期 → 出場。

## Monitoring trigger
If 收盤跌破 $513.73，或 FOMC 當日 MSFT 單日跌幅超過 1 倍 ATR（約 $15），re-evaluate before stop is hit；第二批取消。另外，若 2026-12-05 前未回測進場區，本交易卡失效，須重新出卡。

## Catalyst calendar
- 2026-11-19 — 除息 $0.98/股
- 2026-11-26 — 感恩節休市
- 2026-12-08/09 — FOMC（日期依行事曆推算，未確認）
- 2027-01-27（估計）— FY27 Q2 財報：Azure、CapEx/營收、單季 FCF

FINAL DECISION COMPLETE
