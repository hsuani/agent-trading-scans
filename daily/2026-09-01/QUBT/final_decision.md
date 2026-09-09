FINAL TRANSACTION PROPOSAL: **SELL**

# Final decision — QUBT as of 2026-09-01

## FINAL TRANSACTION PROPOSAL: **SELL**

> **PRICE_DATA_UNAVAILABLE**：本文件所有價格均為估算值，來自分析師共識反推（現價估計 ~$8.40，分析師平均目標 $19.50）。實際下單前必須核實市場報價與選擇權鏈。
> **持倉判定**：QUBT 不在 `held_tickers.txt` 內 → 新倉，走 A 框架。

## Verdict
MODIFY

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | SHORT（僅限 Dec $12/$5 put spread，**嚴禁裸空**） |
| Entry zone | 條件觸發後建倉；全倉須待股價反彈至 $12.00 – $13.00 |
| Stop | $14.00 連續 2 日收盤站穩 → 全數平倉 |
| Target 1 | $7.00 |
| Target 2 | $5.00 |
| Size | Small（總上限 0.25% NAV；條件 1+2 確認先建半倉 0.12% NAV，debit 上限 $1.40；條件 3 觸發補至全倉，總 debit 上限 $2.20） |
| Horizon | 至 Dec 到期（約 3.5 個月），涵蓋 9/30 Planck 窗口與 10 月中 Q3 財報 |
| Conviction | M |
| R:R to T1 | 1.5（以淨 debit $2.00 估；debit ≤$1.40 時約 2.6） |

**條件閘門（今日曝險為 0%，未觸發不得建倉）**：(1) 9/30 前 Planck Dynamics 框架協議未升格為正式 PO；(2) 量子板塊進一步惡化（IONQ/RGTI 破位）；(3) 股價反彈至 $12+。滿足 1+2 建半倉，滿足 3 補全倉。僅滿足 1 項 → 不開倉。

## Risk debate adjudication
- Aggressive's strongest point：spread 寬度改為 $12/$5，以 $0.30–$0.50 的增量 debit 換取 T2（積壓崩解至 $5）的下行空間，邊際 R:R 約 2.5×，這點我採納。
- Conservative's strongest point：MEDIUM 信念 + 28.10% SI + Beta 3.78，軋空機率約 35%，premium 歸零是最可能單一結果；在 $8.40 買深度 OTM 的 $12 put 是在最差 IV 環境付錢。這點我以「條件閘門 + 半倉 + debit 上限」吸收，而非以規模擴張回應。
- Net：我採 **neutral** 較重。積極方把「損失封頂」誤讀成「可以加倍」——封頂改變損失性質，不改變期望值；保守方的 0% 則以尾部情境否定有結構保護的條件性建倉，過嚴。0.25% NAV 上限 + 分段建倉是唯一同時尊重兩邊硬約束的解。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 估值嚴重脫離基本面 | P/S 需回落至行業中位數 | P/S ≈ 83×（年化收入 $22.2M） | 成立 |
| 積壓品質存疑 | $42.5M 積壓多為框架意向書 | Planck 尚未升格為正式 PO | 觀察中 |
| 燒錢速率不可持續 | 淨虧損 / 收入 > 2× | 2.1×，稀釋為常態 | 成立 |
| 競爭資本落差擴大 | 對手融資規模碾壓 | IonQ 單季 $80M、Pasqal 融資 $3.6 億 | 成立 |

## 論點失效條件
與 Stop（$14 連兩收）分開；以下為論點紀律，觸發不必等價格。
- 若 9/30 前公告 Planck Dynamics 正式 PO 且金額 > $8M，「積壓品質存疑」支柱失效 → **不開倉；已建倉則出場**
- 若 Q3（10 月中）季度收入 ≥ $7M 且新增積壓為正，「燒錢不可持續」支柱鬆動 → **減碼至半倉**
- 若 Dirac-3 發佈經同行審查之第三方 benchmark 明確優於 GPU 基準，「競爭落差」支柱失效 → **出場**
- 若獲 CHIPS 法案級聯邦資本承諾，跑道與稀釋壓力解除 → **出場**
- 反向確認：季度收入 < $6M（低於積壓隱含 $7M/季底線）或稀釋 > 10% 流通股 → 空頭論點強化，可持有至 T1

## Monitoring trigger
9/30 收盤後檢查 Planck PO 狀態；無論結果，10 月首個交易日重新核價 Dec $12/$5 spread，debit > $2.20 一律放棄。Q3 財報後不論盈虧強制重評是否續抱至 Dec 到期。

## Catalyst calendar
- 2026-09-09 — 勞工節後量子產業會議季，IONQ/RGTI 更新重新定錨板塊
- 2026-09-30 — Planck Dynamics PO 確認截止觀察窗口（最關鍵）
- 2026-10 中旬 — Q3 2026 財報：季度收入 vs $7M 積壓底線、毛利率、新增積壓
- 不定期 — M&A 收購與稀釋公告、Pasqal 上市後首份業績

FINAL DECISION COMPLETE
