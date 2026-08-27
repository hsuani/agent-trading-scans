FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — SPAI as of 2026-08-28

## FINAL TRANSACTION PROPOSAL: **HOLD**
（SPAI 不在 `held_tickers.txt` 內 = 新倉判定。HOLD 在此代表「不動作、不建倉」，非持倉續抱。）

## Verdict
REJECT

決策等價說明：REJECT = AVOID，NAV 配置 **0%**。
多頭論點 conviction：**低（20%）**；AVOID 決策本身 conviction：高（85%）。

## Final trade card
| Field | Value |
|---|---|
| Direction | 無倉位（不做多、不做空） |
| Entry zone | PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位 |
| Stop | PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位 |
| Target 1 | PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位 |
| Target 2 | PRICE_DATA_UNAVAILABLE — 無即時價格，暫不給進出場價位 |
| Size | 0% NAV（例外路徑見下） |
| Horizon | 季度級別（3–6 個月）重評，不適合短線 |
| Conviction | L（多頭論點）|
| R:R to T1 | 無法計算（無 OHLCV） |

**條件性例外路徑（唯一）**：須同時滿足 (1) OHLCV 價格資料恢復可得，(2) 2026-09 月底前至少 1 份**非 SBIR 性質**的政府量產採購合約正式公告落地。兩者同時成立才可建立上限 **0.10% NAV** 觀察倉，並以事件型退出取代價格止損。任一條件未達，維持 0%。

## Dealbreaker（REJECT 的核心理由）
EV/Sales 28.9x 對應年化約 $5.3M 的營收基礎，較同業（AVAV 3–4x、RCAT 4–6x、KTOS 2–3x）溢價 5–10 倍，且無正 EBITDA、無正 FCF、無 P/E 可錨定；同時 OHLCV 缺失使停損與 R:R 框架完全無法建立。估值無安全邊際 + 風控工具失效，兩者疊加即為不可跨越的 dealbreaker。

## Risk debate adjudication
- Aggressive's strongest point：0.25% NAV 的絕對損失已被 sizing 硬封頂，資料抓取失敗屬工具問題而非基本面惡化，不應升格為否決理由。
- Conservative's strongest point：無 OHLCV 即無有效 stop，進場等同裸倉；情境 A（Q3 <$1.2M，機率 35%）下行 -63% 至 -82% 路徑清晰且快速。
- Net：我採納 **neutral** 立場。進取方 sizing 數學成立，但錯在把「名義曝險」當成「實際可退出曝險」——機構持股僅 18.05%、日均量約 36 萬股的微型股，退出滑價可能吞掉整個 0.25% 的假設。其 upside 又錨定在 3 位分析師（100% BUY、零 HOLD/SELL）的 $10.67 目標價，這在微型股是確認偏誤而非共識。保守方診斷正確但把 PRICE_DATA_UNAVAILABLE 重複計為獨立否決略嫌疊加。中立方的「0% 為預設、0.10% 為雙重確認後的窄例外」是唯一在紀律與參與之間留下可執行路徑的方案。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 政府採購牽引力 | 具名合約可驗證、訂單持續擴張 | 陸軍 NODE、空軍 SBIR、國務院 $180K 均為公開具名合約，2026 年 AI 訂單 >$5M | 成立 |
| 增長持續性 | 環比正增長且非基數效應 | Q2 $1.33M 建立在 $92.7K 基數上，環比未披露，單一合約可致 ±50% 波動 | 觀察中 |
| 估值可支撐性 | 高倍數由增長合理化 | EV/Sales 28.9x，同業溢價 5–10 倍，無 EBITDA/FCF 錨點 | 已失效 |
| 現金跑道與稀釋控制 | 融資無壓、稀釋可控 | 燒率推估 $800K–$1.5M/季，跑道 8–15 個月，C 輪須於 2027 年中前完成 | 觀察中 |

## 論點失效條件
（與 Stop 分開；此處無價格 Stop 可設，故論點紀律即為唯一紀律。）
- 若 Q3 2026 季度營收 <$1.2M（環比衰退），增長持續性支柱失效 → 永久移出候選池，不再等待重評。
- 若 C 輪融資以較公告日前收盤折價 >20% 完成，或 10-Q 首次披露現金跑道 <6 個月，現金支柱失效 → 例外路徑作廢。
- 若陸軍 NODE、空軍 SBIR、國務院項目任一公告延遲或中止，政府採購支柱失效 → 例外路徑作廢。
- 若已建立 0.10% NAV 觀察倉，上述任一觸發即**全數平倉**（事件型退出，不等價格）。

## Monitoring trigger
若 2026-09-30 前未出現任何非 SBIR 政府採購合約公告，或 OHLCV 資料仍不可得，維持 0% NAV 並將 SPAI 降級至季度掃描，直到 Q3 財報。反向：若 Q3 營收 ≥$1.8M（環比 +35%+，排除單一一次性合約）+ C 輪 ≥$10M 且不折價 + EV/Sales 修正至 18–22x，方可重新提交完整新倉提案。

## Catalyst calendar
- 2026-09 月底（預估） — Innovation Day 後政府合約公告窗口
- 2026-10 月中（預估） — Q3 2026 財報：營收、毛利率、現金餘額首次可驗證
- 2026-10 至 11 月 — FY2027 NDAA 預算配置確認
- 2026-11 至 12 月（預估） — C 輪或戰略融資公告

FINAL DECISION COMPLETE
