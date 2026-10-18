FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — MU as of 2026-10-19

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 判定框架
MU 不在 `held_tickers.txt`，屬新倉，問題是「該不該進」。答案：現在不進。交易員「不新開倉」的立場正確，但其升級條件僅以 $737.88 作失效參考、「半倉分批」語意鬆散，故 MODIFY：鎖定一張**待觸發**的條件卡，觸發前不持有任何現股或選擇權部位。

## Final trade card (待觸發，非即時生效)
| Field | Value |
|---|---|
| Direction | LONG（條件式） |
| Entry zone | $905 – $930，須同時滿足：(a) SK Hynix 或 Samsung 財報確認 2027 DRAM／HBM 續漲；(b) 收盤站回 $902.60；(c) MACD histogram 連續 2 日收斂 |
| Stop | $845（10-15 盤中低點 $858 下方，約 1.7× ATR14） |
| Target 1 | $1,036.13（8-17 前高） |
| Target 2 | $1,108.72（9-25 高點） |
| Size | Small（1.5% NAV，Beta 2.2 已折算；確認後最多加至 3%） |
| Horizon | 觸發窗口 10-27 至 11-07；論點驗證至 12-23 FQ1 2027 財報 |
| Conviction | M |
| R:R to T1 | 1.65（以 $917 中價計） |

## Risk debate adjudication
- Aggressive's strongest point：等確認再進場常錯過反彈段，分析師共識與技術回檔的落差確實是潛在不對稱機會。但其 B/A 4.85 建立在未驗證的 $1,560 均值目標上，以近端壓力計算只剩 1.1，且把內部人賣出推定為 10b5-1 無資料佐證。
- Conservative's strongest point：$737.88 停損距現價 -16%、逾 3× ATR，等於用寬停損掩蓋趨勢轉弱；FOMC 與同業財報同週，高 Beta 股的放大效應不可輕忽。但 $830 停損僅 1× ATR，在 48% 年化波動下會被雜訊洗出。
- Net：我偏向 **neutral**。RSI/BB 只說明位置極端，MACD 死亡交叉擴大加放量破位才是趨勢確認；兩者衝突時以後者為準。現在追多 R:R 不足門檻，但長期結構（MA200 上揚、+22%）未破，不該轉空。因此以「價格重返結構之上 + 同業確認」為觸發，停損設在 2× ATR 附近，是雙方皆能接受的折衷。不採用 call spread：10-27 至 10-29 事件前隱含波動偏貴，權利金 R:R 不優於等待現股確認。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 記憶體漲價週期延續至 2027 | DRAM 合約價 QoQ 漲幅維持 ≥ +10%，同業指引 2027 持續短缺 | TrendForce Q4 +10–15%（Q3 +13–18%），斜率放緩；SK Hynix／Samsung 尚未發言 | 觀察中 |
| 盈餘與指引兌現 | 連續優於預估，指引高於共識 | 連四季 beat，FQ1 2027 指引營收 61.5B、EPS 38.15 皆高於共識 | 成立 |
| 技術結構支撐多方 | 守住 $902.60，MACD 不翻空 | 10-16 放量跌破 $902.60，MACD 死亡交叉且 histogram -23.68 擴大；MA200 仍上揚 | 已失效（短期）／中期未破 |
| 現金轉換品質 | FCF/NI 回升至 ≥ 0.5 | TTM 0.34x，隱含 FQ4 capex 約 40.9B 待 10-K 驗證；AR 單季 +75% | 觀察中 |

續抱／進場論證：唯一完全成立的支柱是盈餘兌現，但單憑它無法克服短期結構失效，故不進場；條件卡要求支柱 1 與支柱 3 同時轉為成立才啟動。

## 論點失效條件
必須可證偽，與 Stop 分開。
- 若 SK Hynix 或 Samsung 指引 2027 年 DRAM 合約價持平或下跌，或宣布 2027 capex YoY 上修 ≥ 30%，支柱 1 失效 → 條件卡作廢，轉 AVOID。
- 若 TrendForce 對 2027 Q1 DRAM 合約價預估 ≤ +5% QoQ（連續兩季斜率低於 +10%），支柱 1 失效 → 作廢或已進場者出場。
- 若 MU 10-K 顯示 FQ4 2026 capex ≥ $30B，或 FY2027 capex 指引使 FCF/NI 低於 0.3x，支柱 4 失效 → 已進場者減碼至 1% NAV 以下。
- 若 12-23 FQ1 2027 EPS 低於指引中值 $38.15，或 FQ2 指引 EPS < $38，支柱 2 失效 → 出場。
- 若收盤跌破 $737.88，中期結構失效 → 條件卡作廢，重新評估是否轉空。

## Monitoring trigger
若 10-27 前股價在無催化劑下站回 $902.60，不追價，仍等同業財報；若 10-28 FOMC 後單日收盤跌破 $830，條件卡暫停，待 MA200 $717.84 附近重新評估。

## Catalyst calendar
- 2026-10-27／28 — SK Hynix Q3 財報（2027 價格、capex、HBM4 出貨）
- 2026-10-28 — FOMC 利率決議
- 2026-10-29 — Samsung Q3 完整財報與記憶體事業部拆分
- 2026-10 下旬 — TrendForce 月度 DRAM／NAND 合約價
- 2026-11-10 — 美國 10 月 CPI
- 2026-12-23（估）— MU FQ1 2027 財報

FINAL TRANSACTION PROPOSAL: **HOLD**

FINAL DECISION COMPLETE
