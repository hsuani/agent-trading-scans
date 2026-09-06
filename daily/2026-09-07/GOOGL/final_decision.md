# Final decision — GOOGL as of 2026-09-07

FINAL TRANSACTION PROPOSAL: **BUY**

## FINAL TRANSACTION PROPOSAL: **BUY**

Phase: Full Pipeline (Phase 1-4)

> 本文件所有價位均為**研究參考值**，來源為分析師報告與 SEC 10-Q，非即時報價（Yahoo Finance 403 無法存取）。實際下單須以即時市場數據複核。

## Verdict
MODIFY

（部位狀態確認：GOOGL 不在 `held_tickers.txt` 內，屬**新倉**，採 A 框架。）

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $338.00 – $345.00（研究參考值） |
| Stop | $322.00（研究參考值，收盤價確認） |
| Target 1 | $400.00（研究參考值） |
| Target 2 | $426.00（研究參考值） |
| Size | Small-Medium（**1.0% NAV** 初始，Q3 財報達標後可增至 1.5% NAV） |
| Horizon | 1–3 個月（季度級別），錨定 Q3 財報 |
| Conviction | M |
| R:R to T1 | 3.0（入場中點 $341.50；最差入場 $345 仍有 2.4，全區間過門檻） |

**執行計畫**：於 $338–$345 分兩批建立 1.0% NAV。**$345 為硬性上緣，不追高**——原提案的 $350 上緣在 T1 $400 下 R:R 僅 1.19，不通過 1.5 門檻，予以剔除。若 DOJ 消息面（非基本面）急跌至 $325–$332，可在既有 1.0% NAV 額度內完成剩餘建倉，但**不擴大額度**。加碼至 1.5% NAV 的唯一條件為 Q3 財報 GCP 成長 ≥75% 且 FCF 轉正，兩者須同時達標。得以 0.2–0.3% NAV 配置一個月期 QQQ put（Delta ~0.2）對沖 Magnificent Seven 系統性相關，屬選擇性覆蓋，不影響上述現股額度。

## Risk debate adjudication
- **Aggressive's strongest point**：GCP +82% YoY 與作業利潤 $2.8 億 → $8.8 億 出自 SEC 10-Q，是已發生的事實而非預測；以「等待 Q3 確認」為由壓低倉位，確實有把確定性溢價付給市場的成本。此論點支撐了我拒絕保守方將上限永久鎖死在 0.75% NAV。
- **Conservative's strongest point**：$350 入場時 R:R = 1.19 低於自設門檻，這是原提案的**可量化瑕疵**，無從辯駁；且 Stop $308 等同 5–6× ATR，該區間的止損被觸發時多半反映大盤 beta 而非 GOOGL 論點破損，止損失去診斷功能。
- **Net**：我採納 **neutral** 的裁定。理由是兩側各有一項無法反駁的硬論證，但方向不同——激進方贏在「論點品質」，保守方贏在「執行參數」。正確解不是折衷情緒，而是**接受牛方論點、同時修正保守方指出的參數錯誤**：維持進場（採納激進方），收緊 Stop 至 $322、砍掉 $350 上緣（採納保守方），倉位取 1.0% NAV 並保留條件式加碼路徑。激進方的 2.0% NAV 與 call spread 均遭否決：MEDIUM conviction 不支撐槓桿放大。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| GCP 營收動能 | YoY ≥75% | Q1 +63% → Q2 +82%（SEC 10-Q） | 成立 |
| GCP 規模效益兌現 | 作業利潤隨規模擴張 | $2.8 億 → $8.8 億 YoY | 成立 |
| 搜尋廣告未受 AI Overviews 結構侵蝕 | YoY 維持雙位數 | Q2 +17%，尚無量化惡化 | 觀察中 |
| CapEx 回報 / FCF 回正 | FCF 於 2 個季度內轉正 | 上市以來首見負 FCF 季度，P/FCF 模型暫時失效 | 觀察中 |

## 論點失效條件
（與 Stop 分開：Stop 是價格紀律，以下是論點紀律；論點先壞不必等價格。）
- 若 **Q3 2026 搜尋廣告 YoY 成長率跌破 10%**，第三根支柱失效 → **出場**（全數）。
- 若 **FCF 連續兩季為負，且同期 GCP 成長率跌至 60% 以下**，第一與第四根支柱同時失效 → **出場**。
- 若 **Q3 GCP 成長率落在 60–75% 區間但 FCF 仍為負**，動能支柱轉「觀察中」而非失效 → **減碼至 0.5% NAV**，取消加碼路徑。
- 若 **D.C. 巡迴法院裁定強制剝離 Chrome 或搜尋業務**（結構性補救而非行為補救），法律尾風實現 → **出場**，不等 Stop。

## Monitoring trigger
若 GOOGL 收盤跌破 **$330**（研究參考值，Stop 上方一檔）**且**同期無 QQQ 同幅回撤（即為個股獨立弱勢而非大盤 beta），在觸及 $322 前重新評估論點完整性。另：若 Ruth Porat 或 John Hennessy 出現實際申報賣出（非僅終止 10b5-1 計畫），立即重審倉位。

## Catalyst calendar
- 2026-10-27 至 10-30（預期） — Alphabet Q3 2026 財報：GCP 營收 YoY、FCF 絕對值、搜尋廣告 YoY 三項關鍵數字，同為加碼與失效判定的共同節點
- 2026 年內不定期 — DOJ 搜尋案 D.C. 巡迴法院上訴裁定（12–18 個月長尾，時點不可預期）
- 2026 Q4 — YouTube 面臨 FIFA 世界盃一次性高基期，成長率下滑須與結構性侵蝕區分

FINAL DECISION COMPLETE
