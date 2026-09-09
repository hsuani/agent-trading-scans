FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — VST as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG（條件式核准，條件未滿足前不下單） |
| Entry zone | 無即時價格，暫不給進出場價位 |
| Stop | 無即時價格，暫不給進出場價位 |
| Target 1 | 無即時價格，暫不給進出場價位 |
| Target 2 | 無即時價格，暫不給進出場價位 |
| Size | Small（0.5% NAV 初倉，滿倉上限 1.2% NAV） |
| Horizon | 3m 初驗（Q3 財報）→ 12-18m 完整論題 |
| Conviction | M |
| R:R to T1 | 無法計算（PRICE_DATA_UNAVAILABLE） |

**未經驗證之新聞錨點（僅供事後校準，非交易指令）**：Q2 低谷約 $138.79、合理估值區間約 $140-$165。這些數字不得作為下單依據。

## 執行前置條件（兩者皆須滿足，缺一不下單）
1. 即時價格數據恢復，可計算 ATR 並設定硬性價格止損，且 R:R to T1 ≥ 1.5x。
2. trade_proposal 三項觸發**任一**達成（Q3 EPS 正常化 / Cogentrix 整合完成公告 / PJM 上限確認）。

## Risk debate adjudication
- Aggressive's strongest point：Cogentrix 已於 2026-08-05 取得 FERC 批准、Q2 EPS miss 已釐清為 $4.88 億非現金套保損失，等「官方公告」確實會在市場消化後才進場，時間成本真實存在。
- Conservative's strongest point：ATR 為零時，任何 sizing 都是憑感覺；提案自己承認 R:R 無法計算，卻仍給出方向性建倉指令，這是把基本面邏輯當成價格紀律的替代品。
- Net：我採 conservative 偏 neutral。理由很簡單——這是**新倉**，不是已承擔的曝險。新倉唯一的優勢就是可以不進場；在沒有 stop、沒有 R:R 驗證、且知情人士 12 個月淨拋售 $2.11 億的組合下，放棄幾天的時間優勢是極便宜的保費。Aggressive 主張的 Call Spread 一律否決：PRICE_DATA_UNAVAILABLE 下無法驗證 Premium 定價，等於盲下注。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| PJM 容量收入鎖定 | 10,924 MW @ $325/MW-day，2026 套保 100%、2027 94% | 尚無削減公告，年化毛容量收入近 $13 億 | 成立 |
| EBITDA 動能與估值折價 | EBITDA +31% YoY、EV/EBITDA 7.8-8.5x 低於板塊 | 全年指引 $68-76 億維持，但 Q2 營收 YoY -5.5%、EPS miss 53% | 觀察中 |
| AI 電力需求與 Comanche Peak PPA | 1,200 MW PPA、資料中心用電 +26-27% | Helix 聯盟推進中，惟現金流 2027 年末才啟動 | 觀察中 |
| 內部人士信心 | 與分析師共識同向 | 12 個月淨拋售 $2.11 億，CFO 及董事 90 天賣出逾 41,588 股 | 已失效 |

四根支柱中已有一根失效、兩根觀察中，這正是不給滿倉、且要求前置條件的直接理由。

## 論點失效條件
- 若 PJM 監管機構公告容量上限削減 ≥ 15%（年損約 $2.6 億），支柱一失效 → 取消建倉；已建倉則出場。
- 若 Q3 2026 財報 EPS 再次 miss 且管理層說明主因為現金流衝擊（非套保會計），或全年 EBITDA 指引下修至 $68 億以下，支柱二失效 → 出場。
- 若 Meta 或 AWS 公告延遲、縮減或重談 Comanche Peak PPA 條款，支柱三失效 → 出場。
- 若內部人士 12 個月累積淨拋售突破 $3 億，支柱四進一步惡化 → 初倉上限降至 0.3% NAV 並停止加碼。
- 若 Henry Hub 收於 $4.50/MMBtu 以上連續 10 個交易日且 2028 年套保覆蓋率維持 72%，→ 減碼一半。

## Monitoring trigger
價格數據一旦恢復，48 小時內重算 ATR、R:R 與 vol-adjusted size；若 R:R to T1 < 1.5x，本案自動降級為 REJECT，不再等待觸發條件。

## Catalyst calendar
- 2026-09（月內）— Cogentrix 5,496 MW 併購完成
- 2026-09-10 — FERC 傳輸規劃規則合規文件截止
- 2026-10/11 — Q3 2026 財報（EPS 正常化關鍵驗證點）
- 2026-Q4 — ERCOT / PJM 2027 容量拍賣結果
- 2027-末 — Comanche Peak 1,200 MW PPA 商轉

FINAL DECISION COMPLETE
