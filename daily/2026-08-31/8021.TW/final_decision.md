> **執行前置條件（必須確認）**：所有價格錨點均基於分析師/計算估算值 ~NT$445（UNVERIFIED）。執行前須確認市場報價接近 NT$445，偏差超過 ±8% 則重新校準所有水位後方可下單。

# Final decision — 8021.TW as of 2026-08-31

## Verdict
MODIFY

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | −1.6% 至 +0.7% 錨定 = NT$438 – NT$448 (UNVERIFIED) |
| Stop | −7.4% 錨定 = NT$412 (UNVERIFIED) |
| Target 1 | +10.1% 錨定 = NT$490 (UNVERIFIED) |
| Target 2 | +25.0% 錨定 = NT$556 (UNVERIFIED) |
| Size | Small — 初始 0.20% NAV，條件式加至最高 0.35% NAV |
| Horizon | 1–3 個月（觀察窗 2026-09 至 2026-11） |
| Conviction | L（4 / 10） |
| R:R to T1 | 1.52（進場中點 NT$443；風險 NT$31 = 7.00%，報酬 NT$47 = 10.61%；T2 R:R 3.65） |

**執行閘門（不可跳過）**：PRICE_DATA_UNAVAILABLE 未解除前禁止下任何單。須先取得 8021.TW 實際市場報價；若實價與 NT$445 偏差 >±8%，本卡片所有水位作廢，須以實價重算 entry / stop / target 後才可執行。

## 對原提案的三項修改
1. **Size 下修**：0.25%（可加至 0.50%）→ 初始 0.20%、上限 0.35% NAV。LOW conviction + 未驗證定價基礎，不容許觸及 0.40% 上限。
2. **Stop 後移至 NT$412（非 NT$408）**：兩造共識是 stop 需 ≥2 ATR（ATR ≈ NT$15）。NT$412 自 NT$443 為 2.07 ATR，已解決 whipsaw 疑慮；再退到 NT$408 只多 0.26 ATR，卻讓 T1 R:R 掉到 1.34、跌破 1.5 門檻。薄浮籌跳空會同時穿透 408 與 412，多付的 NT$4 買不到保護。
3. **Entry 收窄至上半段 NT$438–NT$448**：拒絕 NT$431 低端進場（實質緩衝僅 1 ATR），也拒絕「立即市價全倉」。
4. **刪除 0050 Put 對沖**：0.20% NAV 部位的對沖成本與追蹤誤差不成比例；系統性風險以縮小 size 承擔，不以衍生品層層堆疊。台灣小型股 call spread 建議亦否決（流動性不存在）。

## Risk debate adjudication
- **Aggressive's strongest point**：4–5× 鑽針消耗來自層數 40+、孔壽 3,000→600 孔的工程硬約束，屬規格而非敘事；stop 過窄確實是把籌碼送給做價者。這兩點我採納。
- **Conservative's strongest point**：所有風險參數建構在未驗證錨定價上，thin float 加 FCF 融資依賴使 stop 可能無法以紙面價成交，實際損失高於帳面 60%+。這是本案最真實的風險。
- **Net**：我採 neutral 為主、conservative 為輔。Aggressive 的「立即 0.50% 全倉」在定價盲區中放大暴露，邏輯不成立；Conservative 的「YoY ≥90% 且 CB 條件同時明確」雙門檻等於變相棄權，且 Scenario D（−65%）主觀機率明顯偏高。折衷取 0.20% 起手、上限 0.35%。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI PCB 鑽針結構性消耗 | 每板用量 4–5×，供給緊俏延續至 2026 年底 | 工程規格佐證；但 CoWoS 缺口已由 20% 縮至 10%（Trendforce 2026-06） | 觀察中 |
| 營收與獲利加速度 | 月營收 YoY ≥80% 持續 | 7 月 +102.56%、Q2 EPS YoY +271% | 成立 |
| 產品組合升級／定價力 | 高階鍍膜占比升、GM 擴張 | 48%→56%，GM 36.59%→41.77% | 成立 |
| 資本結構可承受擴產 | capex 由獲利成長覆蓋 | capex/FCF = 13×，NT$1.68B CB 稀釋條件未公布 | 已失效（此支柱不列入多方依據，僅以縮小 size 反映） |

## 論點失效條件
- 若 8 月或 9 月任一月營收 YoY <70%，加速度支柱失效 → 全數出場（不等 stop）。
- 若 CB 轉換條件公布，稀釋 >12% 且轉換價低於市價，資本結構支柱進一步惡化 → 立即減碼至 0.10% 或出場。
- 若 Q3 EPS 低於 NT$8.75 年化基準 15% 以上（即 <NT$7.44），或 Q3 GM 未站上 43%，定價力支柱失效 → 出場。
- 若 hyperscaler 公開下修 2027 AI capex，或 CoWoS 缺口縮至 5% 以下，結構性需求支柱失效 → 出場。
- 若中壢新廠時程延宕逾兩季 → 減碼一半。

## Monitoring trigger
2026-09-10 至 15 月營收：YoY ≥80% 且 CB 無負面公告 → 加至 0.35% NAV；YoY 70–80% → 維持 0.20% 不加；YoY <70% → 出場。另若實價確認後已 >NT$470（+5.6% 錨定），放棄本次進場，不追高。

## Catalyst calendar
- 2026-09-10 至 15 — 8 月月營收（最關鍵加碼／出場觸發）
- 2026-10 月中 — SEMICON Taiwan 2026（高階鍍膜訂單能見度）
- 2026-11 月中 — Q3 財報暨法說會（EPS vs NT$8.75、GM >43%、FCF 轉正指引）
- 2026-11 月底 — 產能 4.5M 支/月達成評估
- 待定 — CB NT$1.68B 轉換條件公告

FINAL TRANSACTION PROPOSAL: BUY (MODIFIED)

FINAL DECISION COMPLETE
