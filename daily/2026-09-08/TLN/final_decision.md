FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — TLN as of 2026-09-08

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

> 新倉判定：TLN 不在 `held_tickers.txt`，走新倉框架。問題是「該不該進」，答案是「可以進，但只進試探性第一批」。
> 價格警示：market.md 為 PRICE_DATA_UNAVAILABLE，以 ~$318.50 為工作價，所有價位為估算，實盤以限價單成交回報為準。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $310.00 – $322.00（限價，拒絕 $322 以上追價） |
| Stop | $270.00（收盤價確認制） |
| Target 1 | $444.00 |
| Target 2 | $500.00 |
| Size | Small（0.5% NAV 第一批；達標後上限 1.5% NAV） |
| Horizon | 3m+，核心窗口 2026 Q4 – 2027 H1 |
| Conviction | M（55%） |
| R:R to T1 | 2.8 |

**信心度：55% conviction。** 合約可查、指引有 Q2 業績背書，但智慧資金訊號與空方基本情境 R:R 1.1:1 壓住了信心上限。

## Risk debate adjudication
- Aggressive's strongest point：Amazon 1.92 GW 是已簽署、$20 億資本已落地的法律合約，屬可查事實而非預測；純以「內部人士賣出」壓縮倉位有過度解讀之嫌。
- Conservative's strongest point：提案引用的 2.8:1 是牛方基本情境算出來的，投資計畫自己揭示空方基本情境下 R:R 僅 1.1:1 — 這是選擇性偏誤，倉位必須據此收縮。
- Net：我採納 **neutral** 為主。Aggressive 的 3% NAV 與 $255 stop 把止損推進到論文早已失效的區域，止損失去結構意義；Conservative 的 $285 stop 在 50–70% 隱含波動率下約 4–5 個正常日波動即被誤觸。$270 是 Q1 急跌低點，是唯一有結構意義的失效邊界。倉位則採 Conservative 的 0.5% 起手，不採其 XLU put spread（0.5% NAV 的股票倉位不值得付對沖成本）。Aggressive 的 call spread 在 ATR 不可知下一律否決。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Amazon 1.92 GW 前電表合約執行 | 2027 H1 達全面商業運營，FCF/share $37 | 框架已重構完成，計費里程碑未驗證 | 觀察中 |
| PJM 容量定價紅利 | $330/MW-day 維持，98% 資產受益 | 定價為已實現事實，政治逆轉風險未解 | 成立 |
| 估值折價（8.6x 2027E P/FCF） | 相對共識 $459.94 折價 44% | 折價仍在，但依賴 FCF 兌現 | 成立 |
| Cornerstone 整合與槓桿 | Net Debt/EBITDA 收斂至 <3.0x | 總負債逾 $7B，利息覆蓋 2.8–3.3x | 觀察中 |

## 論點失效條件
與 Stop 分開；論點先壞就先動作，不等價格。
- 若 Q3 更新顯示 Amazon 前電表計費未啟動，或全面商業運營延遲超過兩季 → 出場（不論價格）
- 若 FERC 對前電表合約模式發布任何新限制令 → 出場
- 若 PJM 下一輪容量拍賣結算價 < $150/MW-day → 出場
- 若季報揭示 Net Debt/EBITDA ≥ 4.0x，或 Q3 調整後 EBITDA < $500M → 減碼至零加碼、砍半
- 若未來 30 日新增內部人士淨賣出 > $50M → 減碼

## 關鍵催化劑
- 2026-09-30 — Q3 營運更新：Amazon 計費進度 + Cornerstone 整合（第一再評估節點）
- 2026-10-15 — PJM 調節市場第二階段上線
- 2026-11 — Q3 正式財報：EBITDA 兌現度、$1.7B 回購執行進度
- 2027 H1 — Amazon 合約全面商業運營（論文核心兌現）
- 2027 mid — 潛在信評升級 BB+ → BBB-

## 風險因子
- $122M 內部人士淨賣出 + 75% 期權大戶看跌，智慧資金與分析師共識背離
- 空方基本情境（15x P/E → $204）下 R:R 僅 1.1:1
- 股票對負面執行訊號極度敏感（Q1 後 5 日 −14%），$270 止損有跳空至 $255 風險
- PJM 容量定價的監管/政治逆轉風險（合計尾部機率約 25%）
- ATR 不可知，所有技術位設定存在執行誤差

## Phase 1 評分表
| Signal | 判定 |
|---|---|
| 催化劑可查性（Amazon 合約 + PJM） | ✅ |
| 估值吸引力（8.6x 2027E P/FCF） | ✅ |
| 業績動能（Q2 EBITDA $374M、指引上調） | ✅ |
| 技術趨勢 / 價格資料品質 | ❌ |
| 智慧資金定位（內部人士 + 期權） | ❌ |
| **合計** | **3 / 5** |

## 執行建議
1. 立即掛 **限價 $322**，於 $310–$322 分次成交 0.5% NAV。不市價單，不追 $322 以上。
2. Stop $270 採收盤確認制，掛好即不動。跌至 $305 以下 **不自動加碼**（避免「越跌越補」）。
3. 加碼三條件必須全達：①Amazon 計費里程碑符合指引 ②Q3 EBITDA ≥ $530M 季均 ③30 日內新增內部人士賣出 < $30M。缺一不加，缺一則維持 0.5% 至下一節點。
4. 全達則加至總計 1.0–1.5% NAV；不加 call spread、不加 XLU 對沖。

## Monitoring trigger
若 2026-09-30 Q3 更新對 Amazon 計費進度僅給出模糊措辭（未給具體 MW 或營收數字），視同「未達標」，於止損被觸及前主動減碼至零。

FINAL TRANSACTION PROPOSAL COMPLETE
