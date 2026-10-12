FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — MU as of 2026-10-12

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

## 倉位性質
MU 不在 `held_tickers.txt`,屬新倉。本決策回答的是「該不該進」,而非「該不該續抱」。

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $1,017.00 – $1,026.00(上限收緊,原案 $1,036 上緣取消) |
| Stop | $976.19(MA50,收盤跌破觸發,不加盤中條件) |
| Target 1 | $1,098.90 |
| Target 2 | $1,150.66 |
| Size | Small(0.5% NAV);upside trigger 成立後最多加至 1.0% NAV |
| Horizon | 1–3 個月,以 10 月下旬同業財報與 2026-12-23 FQ1'27 財報為檢驗點 |
| Conviction | L |
| R:R to T1 | 2.0(於 $1,017 進場);1.5(於 $1,026 進場) |

修改內容:
1. 進場上限由 $1,036 收緊至 $1,026。原案自己算出上緣成交 R:R 僅 1.0,卻沒有機制阻止,這是執行漏洞,直接用價格上限堵掉。
2. 維持 Small 0.5% NAV 起始。Aggressive 主張升至 1.0–1.5% 的前提是 R:R 2.0–3.3,但那只在區間下緣成立;投資計畫明文「低信心、不超過標準部位」,部位不應跑在信心前面。
3. 加碼條件明確化:SK hynix / Samsung 財報確認 HBM 價格續漲 **且** 收盤帶量站回 $1,099,兩者同時成立才加至 1.0% NAV。單一條件不加碼。
4. 不採用 call spread。低信心戰術倉不需要再疊加到期與隱含波動率風險。
5. 不採用盤中 ATR 輔助停損。Beta 2.23、年化波動 48%,盤中條件只會提高被噪音洗出的機率,與 Conservative 自己列的 Scenario C 矛盾。

## Risk debate adjudication
- Aggressive 最強的一點:停損距離約 4%、約等於 1 ATR14,風險定義清楚,本身不需要放寬。這點我接受,所以 stop 維持不動。
- Conservative 最強的一點:進場區間 1.9% 跨度內 R:R 從 2.0 掉到 1.0,但 Trigger 條款沒有硬性阻止上緣成交。這是整份提案最實質的缺陷,我直接採納修正。
- Net:我較偏向 **neutral**。Aggressive 把只在下緣驗證過的不對稱性外推到整個倉位,Conservative 則在罷工與同業財報上疊加雙重凍結。Neutral 的「收緊進場、維持 Small、觸發後才加碼至 Medium 下緣」最貼近投資計畫原意,且每一項都有數字依據。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 盈餘修正方向向上 | FQ1'27 指引高於共識 | 指引 $61.5B vs 共識約 $57.9B;FQ4'26 $54.23B 超過自身指引上緣 | 成立 |
| HBM/DRAM 供給緊缺延續至 2027 | 合約價持續上漲,同業展望上修 | 尚待 10 月下旬 SK hynix / Samsung 財報與 TrendForce Q4 預估 | 觀察中 |
| 中期技術結構未破 | 價格高於 MA50/MA200,低點抬高 | 仍高於 MA50 $976;但 MACD 死叉、RSI14 50.2、10-01 後形成 lower high | 觀察中 |
| 供給事件不衝擊 FQ1'27 指引 | 桃園廠罷工不實際發生或影響有限 | 10-07 授權 99% 通過,日期未定 | 觀察中 |

四根支柱中僅一根確定成立,其餘三根都要靠未來數據驗證,這正是信心只能給 L、部位只能給 Small 的原因。

## 論點失效條件
與 Stop $976.19 分開。以下任一項成立,不必等價格觸及 stop 即動作。
- 若 SK hynix 或 Samsung Q3 財報顯示 HBM 平均售價 QoQ 轉跌,或 2027 HBM 出貨展望下修,支柱二失效 → 出場。
- 若 TrendForce Q4'26 DRAM 合約價預估 QoQ 漲幅低於 5%(接近持平),支柱二失效 → 減碼至少一半。
- 若桃園廠實際罷工持續超過 3 個交易日,支柱四失效 → 減碼一半;若超過 5 個交易日或公司公告出貨受影響 → 出場。
- 若 FQ1'27(估 2026-12-23)實際營收低於 $61.5B 指引,或 FQ2'27 指引 QoQ 成長低於 +5%,支柱一失效 → 出場,立場轉 NEUTRAL。
- 若上述任兩項同時成立 → 出場並轉 SHORT_OR_AVOID 評估。

## Monitoring trigger
若收盤跌破 $1,017 且 MACD histogram 連續三日負值擴大,停止所有未完成的分批進場,在觸及 $976 前重新評估支柱三。若 SK hynix / Samsung 財報公布前股價已站回 $1,099,不追價,等財報確認後再決定是否加碼。

## Catalyst calendar
- 2026-10-14 — Ex-dividend(季股息 $0.15)
- 2026 年 10 月下旬 — SK hynix / Samsung Q3 財報(支柱二驗證點,加碼前提之一)
- 2026 年 10 月下旬 — TrendForce Q4'26 DRAM/HBM 合約價預估
- 待定 — 桃園廠罷工日期公布(支柱四驗證點)
- 2026-12-23(估)— MU FQ1'27 財報(支柱一驗證點,本論點的最終檢驗)

FINAL DECISION COMPLETE
