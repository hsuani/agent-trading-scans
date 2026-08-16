# Sector report — 量子計算 (Quantum) as of 2026-08-11

## Ranking table

| Rank | Ticker | Verdict | Conviction | R:R | Size | Horizon | Trigger |
|------|--------|---------|------------|-----|------|---------|---------|
| 1 | LAES | BUY | M | 1.9 / 4.5 | 0.3% NAV | 1–3m | FIPS 140-3 提交（Sep）；入場 $2.45–$2.60 |
| 2 | IONQ | HOLD（條件式 LONG） | M | 1.5–2.1 | 0.5% NAV | 1–3m | 行情恢復且現價 ≤$60 |
| 3 | ARQQ | HOLD（條件式 Call Spread） | L | 2.3 | ≤0.5% NAV 保費 | 6–12 週 | Options 流動性確認；融資公告前 |
| 4 | QUBT | HOLD（條件式 Call Spread） | L | ~2.5 | 0.125% NAV | 2–3 季 | 行情恢復且確認 $7.80–$10.55 |
| 5 | QBTS | SELL（條件式 Put Spread） | M | 0.3 (T1) / 2.3 (T2) | 0.75% NAV 保費 | 90 天 | 2026-08-15 CHIPS 條款 ≤ 中性落地 |
| 6 | RGTI | AVOID | — | < 2.0（所有結構均不合格） | 0% NAV | — | Q3 收入 < $700 萬，或具體負面催化劑出現 |
| 7 | HON | SKIP | — | N/A | 0% NAV | — | Phase 1 僅 2/5；Quantinuum 為間接曝險 |
| 8 | IBM | SKIP | — | N/A | 0% NAV | — | Phase 1 僅 1/5；量子為純 R&D 支線 |

---

## Consensus top pick

**LAES（SEALSQ）**。

本次掃描唯一獲 BUY 裁定的標的。LAES 本質上是「後量子密碼（PQC）半導體」而非量子硬體押注，直接受惠於 White House EO 規定的 2030–2031 PQC 遷移強制期限。財務面有真實數字支撐：H1 2026 營收 $11.4M（YoY +120%）、商業管道 $225M+ 至 2029 年、流動比率 15.9。近期硬催化劑明確：2026-09 QVault TPM 185 提交 FIPS 140-3、2026-10 QS7001 V2 生產樣品交付。R:R T1 1.9、T2 4.5，0.3% NAV 起步，最大 0.5% NAV，風險可控。主要隱患：母公司 WISeKey $495M 現金不直接屬於 LAES 股東，且毛利率至今未揭露。

---

## Contrarian pick

**ARQQ（Arqit Quantum）**。

主流因 P/S ~580×、H1 FY2027 收入僅 $623K 將其定性為棄守標的；但 ARQQ 是本次掃描中唯一確認即時價格（$22.90）的 PQC 加密網路公司，UK NCSC 試點入選已建立機構可信度，DoD 採購窗口可能在橋接融資公告（預期 2026-09/10）之前提前觸發跳升。等待融資明朗才行動等同放棄最大非線性上行。工具採 $23/$28 Nov-2026 call spread（保費 ≤0.5% NAV），定義風險結構使隔夜融資跳空的尾部損失由 premium 封頂，主流誤把 equity LONG 的止損失效論套用至 options 結構。

---

## Pairs trade idea

**Long LAES / Short QBTS（Put Spread 代替裸空）**。

兩者同屬廣義量子主題但結構截然相反：LAES 擁有真實 PQC 硬體產品線與 FIPS 認證路徑；QBTS Forward P/S 355×，FY2026 年化營收年減約 50%，CEO/CFO 半年淨賣出 $1.74M。此對衝隔離「PQC 認證落地者 vs. 量子計算高估值標的」的相對價值分歧，QBTS 側以 Nov-2026 $20/$10 Put Spread 封頂缺口風險，兩腿合計最大損失皆可預知。

---

## Sector-wide observations

**共同催化劑**
- **2026-08-15 CHIPS Act 量子條款落地**：本週最重要的單一事件，直接決定 QBTS 空頭進場與否，並影響 RGTI 的 gap 風險窗口。
- **White House EO PQC 強制令**：對 LAES 與 ARQQ 持續提供監管尾風。
- **DARPA QBI 商業化時間表 2033**：對所有純量子硬體標的（IONQ、RGTI、QBTS、QUBT）構成長期敘事壓力；估值溢價需依賴「技術躍升」敘事維持，任何延遲消息均可引發急殺。

**共同風險**
- yfinance 403 封鎖七檔標的行情，所有條件式倉位須待行情恢復後才可觸發。
- 量子純玩家估值極端（P/S 100×–580×），敘事破裂尾部損失 -40%–-60%。
- 散戶高度擁擠（RGTI、QBTS、QUBT 均有散戶多頭疊加高賣空比），短壓縮與反向殺盤均可急速發生。

**相關性群集**
- 高度正相關：IONQ / RGTI / QBTS / QUBT（純量子硬體敘事同步，合計視為單一集中風險）。
- 部分相關：LAES / ARQQ（共享 PQC 主題，但商業成熟度與財務結構差距大）。
- 低相關：HON / IBM（大型股，量子 beta 遠低於純玩家；分拆後 HON 仍持 Quantinuum 54%，屬間接曝險）。

**估值區間對比**

| 類型 | 代表標的 | P/S 估算 | 商業化階段 |
|------|---------|---------|---------|
| PQC 半導體 | LAES | 未披露（早期） | 已量產、認證進行中 |
| PQC 加密網路 | ARQQ | ~580× | 試點/早期合約 |
| 量子計算（離子阱） | IONQ | ~100× | 早期商業化 |
| 量子計算（超導） | QBTS | ~355× (Forward) | 訂單轉化待驗 |
| 量子計算（超導） | RGTI | 未計算（不合格） | 早期商業化 |
| 量子計算（光子） | QUBT | 未計算 | 整合磨合期 |

---

## Action sequencing

1. **LAES** — 最優先。唯一 BUY，限價單 $2.45–$2.60，不依賴行情源恢復，今日即可掛單。
2. **QBTS Put Spread** — 靜待 2026-08-15 CHIPS 條款；若落地中性至負面且標的位於 $21–23，立即建倉。
3. **IONQ 條件式 LONG** — 行情恢復後第一時間核查；現價 ≤ $60 則執行 0.5% NAV。
4. **ARQQ Call Spread** — 先確認兩腿 options 流動性合理，再執行；融資公告前窗口有限。
5. **QUBT Call Spread** — 倉位最小（0.125% NAV），最後執行，行情確認後建倉。

---

## Sector risk budget

IONQ / RGTI / QBTS / QUBT 四者高相關，若同時持有多頭側（IONQ）+ 空頭側（QBTS），淨量子硬體曝險相互對沖但個別尾部仍存。若上述全部條件倉位同時觸發，合計約 2.375% NAV（保費計全額）。建議量子板塊總曝險上限 **3.5% NAV**；若 IONQ 與 QUBT 同步觸發，應視為同向量子敘事集中，多頭側合計不超過 1.0% NAV。

---

SECTOR REPORT COMPLETE
