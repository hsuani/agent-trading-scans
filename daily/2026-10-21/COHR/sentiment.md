# Sentiment — COHR as of 2026-10-21

資料時間基準：2026-10-21。股價資料多來自次級來源且彼此衝突，最新可信價位未能完全核實（見文末資料品質）。

## Analyst consensus
rec_summary（0m）：**19 buy**（4 strong buy + 15 buy）/ **5 hold** / **0 sell**，共 24 位分析師。
近四個月趨勢：-1m 19/5/0，-2m 18/5/0，-3m 18/5/0，買方評等僅小幅增加，未見評等轉弱。

目標價（次級來源，時間點不同，僅供參考）：
| 時間點 | 來源 | 平均目標價 | 高 / 低 |
|---|---|---|---|
| 2026-08 中旬 | Barchart | $388.25 | — |
| 2026-10-05 | Google Finance | $404.71 | $500 / $280 |
| 2026-10-15 | 次級文章 | $412.52 | — |

近期評等動作（次級來源，yf recommendations 未回傳逐家券商的升降評明細）：
- Rosenblatt 9/23 維持 $500 目標
- Stifel 9/22 維持 $420 目標
- Citi 9/28 維持 $420 目標
- Bernstein 9/30 首次評等 Outperform，目標 $350（僅一家明確低於平均目標價的新評等）
- 逐家升降評清單：DATA_UNAVAILABLE

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 對 www.reddit.com 被拒，WebSearch 亦未找到近期 COHR 相關討論串，無法取樣貼文與計算傾向。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 無法解析網域（DNS 失敗）。
- X / 其他社群：未找到 2026-10 的可靠即時資料。唯一相關來源為 2026-02 的低權威交易網站，列出混合意見（多方看 AI 雷射與矽光子需求，空方看 RSI 過熱、Put 買盤與關稅風險）。權重低，僅作背景參考。
- 聲量（mention volume）：無量化數據，DATA_UNAVAILABLE。定性上，近期新聞流量偏高（10/1 單日大漲約 11%、10/15 前後一週大跌約 21%），新聞與價格波動明顯高於一般水準。
- 主要話題（依可取得之新聞與評論歸納）：
  1. AI 資料中心光收發模組需求（800G / 1.6T）；Datacom 約佔營收 75%（2026-03 季）
  2. 估值偏高（Google Finance 顯示 P/E 約 80）
  3. 內部人密集出售股票
  4. 供應產能擴張與毛利率擔憂（5/6 財報後股價下跌約 7.4%）
  5. 關稅與中國雲端客戶需求風險
  6. 10/15 大跌被歸因於熱門通膨報告推升 30 年期公債殖利率至 5.63%，屬宏觀因素而非公司基本面

散戶傾向：無法可靠判定（DATA_UNAVAILABLE）。

## Insider activity
過去 6 個月（2026-04-21 至 2026-10-21，依 yf cache）：**買進 0 筆 / $0；賣出 11 筆 / 約 $10.65M**。
股票獎勵（8/28 大量授予）與贈與（9/11 DiRolomo 贈與 1,279 股）不計入買賣金額。

主要賣方：
| 日期 | 姓名 | 職稱 | 股數 | 金額 | 價格區間 |
|---|---|---|---|---|---|
| 2026-09-01 | Julie Sheridan Eng | CTO | 13,077 | 約 $3.58M | $270.69–276.83 |
| 2026-09-11 | Enrico DiRolomo | 董事 | 5,315 | 約 $1.63M | $305.98 |
| 2026-08-31 | Enrico DiRolomo | 董事 | 2,272 | 約 $0.63M | $276.85 |
| 2026-08-31 | Stephen Skaggs | 董事 | 2,272 | 約 $0.63M | $276.88 |
| 2026-09-02 | Lisa Neal-Graves | 董事 | 2,200 | 約 $0.59M | $268.42 |
| 2026-09-09 | Robert Beard | 高階主管 | 500 | 約 $0.15M | $309.32 |
| 2026-08-18 | Sherri Luther | CFO | 3,000 | 約 $0.97M | $324.00 |
| 2026-07-22 | Sherri Luther | CFO | 1,000 | 約 $0.31M | $306.68 |
| 2026-05-12 | Sherri Luther | CFO | 2,000 | 約 $0.75M | $372.96 |
| 2026-05-11 | Howard Xia | 董事 | 2,000 | 約 $0.71M | $344–368 |
| 2026-04-22 | Sherri Luther | CFO | 2,000 | 約 $0.70M | $351.00 |

重點觀察：
- CFO Sherri Luther 在窗口期內四次出售，合計約 $2.73M，為持續性賣出。
- CEO James Robert Anderson 窗口期內僅有 8/28 股票授予（30,564 股），無公開市場賣出紀錄。
- 多數賣出集中於 8 月底至 9 月，股價在 $268–325 區間。
- 10b5-1 交易計畫與否：DATA_UNAVAILABLE。
- 資料落差：cache 中最後一筆交易日為 2026-09-11，9/12 至 10/21 之申報可能未納入，需以 SEC Form 4 核對。
- 次級來源（Quiver Quantitative）稱 6 個月內 15 筆賣出、0 筆買進，與本工具計算的 11 筆不一致，可能因統計口徑或窗口不同。

## Ownership shifts
（as-of 2026-06-30 13F 申報資料）
- 機構持股：88.01%；機構數 1,774 家
- 內部人持股：4.41%
- 前十大機構：
  | 機構 | 持股比例 | 股數 | 季度變化 |
  |---|---|---|---|
  | BlackRock | 8.43% | 16.6M | +11.1% |
  | Vanguard Capital Management | 6.48% | 12.8M | +4.8% |
  | FMR (Fidelity) | 5.59% | 11.0M | **-51.4%** |
  | Vanguard Portfolio Management | 5.09% | 10.0M | +5.9% |
  | State Street | 4.36% | 8.6M | +10.9% |
  | NVIDIA | 3.95% | 7.8M | 0.0% |
  | Invesco | 3.77% | 7.4M | +10.7% |
  | Geode Capital | 2.68% | 5.3M | +0.6% |
  | Capital International Investors | 1.83% | 3.6M | +100% |
  | Morgan Stanley | 1.67% | 3.3M | +19.1% |
- 趨勢：前十大中九家增持，FMR 大幅減持（-51%）為主要例外。FMR 減持幅度異常大，建議與 13F 原始申報核對（可能包含基金間轉移或申報口徑調整）。
- 季度資料為 2026-06-30，不反映 Q3 後的變動。

## Net sentiment score
**綜合：中性偏多（信心：低）**

依來源分項：
- 分析師：偏多（19 buy / 5 hold / 0 sell，平均目標價約 $405–413，相對近期價位仍有上行空間），信心中高。
- 內部人：偏空（0 買 / 11 賣，約 $10.65M，CFO 與多位董事持續減持），信心中。注意內部人賣出不一定代表看空，可能與股權激勵到期或計畫性出售有關。
- 機構持股：中性偏多（多數增持，FMR 為例外），信心中。
- 散戶 / 社群：無法判定（Reddit、StockTwits 無資料，X 無可靠 2026-10 資料），信心低。
- 價格動能：近一週大跌（約 -21%），短線情緒受宏觀利率衝擊，但此為價格資料，不屬於情緒來源。

**背離旗標：無法判定（散戶資料缺失）**。
- 分析師與內部人方向不一致：分析師偏多而內部人持續賣出，此為可觀察的分歧，值得留意。
- 分析師與散戶方向：DATA_UNAVAILABLE。

## 資料品質與限制
- `yf.py COHR ratings` 指令不存在（可用子命令不含 ratings）。已改用 rec_summary、recommendations、insider、major_holders、inst_holders。recommendations 回傳內容與 rec_summary 重複，無逐家升降評明細。
- Yahoo 的 cookie / crumb 取得失敗，但 yf 仍回傳資料（cache）。
- Reddit、StockTwits 無法存取，已軟失敗並記為 DATA_UNAVAILABLE。
- 價格衝突：Google Finance 10/5 收盤 $333.64；次級文章 10/15 稱約 $263（週跌 21.3%，單日 -9.2%）。原始來源 247wallst.com 無法在本次驗證，10/20–10/21 的正式收盤價 DATA_UNAVAILABLE，需以即時報價確認。
- 目標價與評等數字來自多個次級來源，時間點不同，未逐一核對至原始券商報告。
- 本報告為情緒彙整，不含交易建議。

SENTIMENT REPORT COMPLETE
