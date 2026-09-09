FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — RGTI as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

> 新倉判定（RGTI 不在 held_tickers.txt）。核准一個**有條件的空方 Put Spread**，但今日入場閘門
> 尚未成立（現價估算 ~$15.64，仍高於 $15.00，三項條件無一書面確認），故今日**不建倉**，
> 第一行為 HOLD。閘門滿足 2 項後，此卡片即為授權執行的唯一版本，無須再回報。

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | SHORT（Buy $14 Put / Sell $7 Put，Nov 2026 到期） |
| Entry zone | $14.50 – $15.00（underlying），且須 2-of-3 條件同時成立 |
| Stop | $18.50（論點失效線 / 認賠全額淨權利金）；$17.50 收盤啟動評估，$19.00 強制平倉 |
| Target 1 | $7.07 |
| Target 2 | $3.84 |
| Size | Small（0.5% NAV，即全額淨權利金上限） |
| Horizon | 1–3m，不延續持有超過一季 |
| Conviction | M（60%） |
| R:R to T1 | 2.3（underlying 等效）／1.8（Put Spread 結構內） |

**入場閘門（三選二，須同時成立）**：① 連續兩日收盤 < $15.00 且單日量 ≥ 20 日均量 1.5×
② CHIPS Act LOI 出現書面負面或延期公告（非傳聞）③ ATM 融資 SEC 8-K 正式申報。

**相對交易員提案的修改**：入場由「任一條件」收緊為「2-of-3」；新增 $17.50 評估線與
$19.00 強制平倉，解決深度 OTM 流動性滑點；駁回 aggressive 的 1.0–1.5% NAV 與 $15/$5 結構；
駁回 conservative 的 0.25% 與純 AVOID；取消 $20 Call 保險（成本侵蝕本已僅 1.8× 的結構內 R:R）。

## Risk debate adjudication
- Aggressive's strongest point：Put Spread 已把軋空的無限尾部風險鎖成淨權利金，因此
  17.71% Short Interest 不該重複用來當縮倉理由——這個結構論證是對的。
- Conservative's strongest point：年化 vol 120–150% 下，買方腳付的是已充分定價的下行溢價，
  而九月是催化劑最密集的月份；「任一條件即入場」的門檻低到無法區分噪音與趨勢。
- Net：我採 **neutral** 較重。方向感有五項時間戳記事實支撐（值得留曝險，故不採純 AVOID），
  但信念僅 MEDIUM 60%，不足以跨越規模級距；在買方付高 vol 溢價的窗口，紀律該花在
  **入場時點**而非規模上——這正是 2-of-3 閘門的用意。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 商業化缺口 | 虧損倍率結構性難解 | Q2 淨損 $52.6M / 營收 $5.1M = 10.3× | 成立 |
| CHIPS Act $100M 未落地 | 仍為 LOI，非入帳資本 | 至今無正式合約 | 成立 |
| 超導技術排他性受壓 | 護城河敘事被侵蝕 | IonQ 2026-08-27 實時 QEC 已成事實 | 成立 |
| 內部人信心缺位 | 高管無買入背書 | CEO 1 月行使 100 萬股全數套現，6 個月零買入 | 成立 |

## 論點失效條件
可證偽，且與 Stop 分開（Stop 是價格紀律，以下是論點紀律）。
- 若 CHIPS Act $100M LOI 轉為正式聯邦合約（DOC 公告或 SEC 8-K 書面確認），支柱 2 失效 → 出場
- 若 Q3 2026 營收 > $8.0M 且毛利率 ≥ 40%，支柱 1 失效 → 出場
- 若 Cepheus-1 達 99.5% 雙比特保真度**且**同步公告企業級採購合約，支柱 3 失效 → 減碼一半
- 若任一 C-level 於公開市場買入 ≥ $500K（Form 4），支柱 4 失效 → 減碼一半

## Monitoring trigger
若收盤突破 $17.50，或 Short Interest 由 17.71% 降至 12% 以下（軋空動能耗盡反轉為承接），
在 $18.50 論點失效線被觸及前先行重評並考慮減碼。

## Catalyst calendar
- 2026-09 內 — CHIPS Act LOI 正式合約或延期公告（核心裁定）
- 2026-09 內 — ATM 融資 SEC 8-K 申報
- 2026-09 內 — IonQ / IBM 企業級部署合約公告
- 2026-09-01 起 — TangleLab 動工後客戶與媒體反應
- ~2026-11 — Q3 2026 財報（論點存廢事件，與 Nov 到期日對齊）

FINAL DECISION COMPLETE
