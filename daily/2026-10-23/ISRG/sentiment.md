# Sentiment — ISRG as of 2026-10-23

## Analyst consensus
目前 rec_summary 為 34 家分析師：Strong Buy 8 / Buy 18 / Hold 7 / Sell 1 / Strong Sell 0。
BUY 合計（Strong Buy + Buy）26 家，占 76.5%（以 34 家計）；Hold 占 20.6%；Sell 合計 2.9%。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | BUY 合計 | 合計 |
|---|---|---|---|---|---|---|---|
| 當期 (0m) | 8 | 18 | 7 | 1 | 0 | 26 | 34 |
| -1m | 7 | 17 | 7 | 1 | 0 | 24 | 32 |
| -2m | 7 | 17 | 8 | 1 | 0 | 24 | 33 |
| -3m | 7 | 16 | 9 | 1 | 0 | 23 | 33 |

近四個月趨勢：BUY 家數由 23 增至 26，Hold 由 9 降至 7，評級略為正向移動，但幅度有限。

評等變動紀錄：yf recommendations 工具只回傳彙總分佈，沒有個別券商的升降評與目標價變動明細，因此無法確認近期具體 upgrade / downgrade 或目標價調整。WebSearch 聚合頁提到一家 Oppenheimer 升評與一家 Wall Street Zen 降評，但來源品質低，未經交叉驗證，僅供參考。

## Retail social
- Reddit: r/wallstreetbets 與 r/stocks 搜尋 JSON 端點均回傳存取受限（WebFetch 無法連線 www.reddit.com），本次無法取得直接討論串樣本，此來源缺漏。
- StockTwits: api.stocktwits.com 無法解析主機名稱（ENOTFOUND），此來源缺漏。
- LunarCrush（經 WebSearch 取得之聚合頁）：不同時點快照的正面情緒數字差異極大，一版顯示 81% 正面（24 小時約 423 則貼文、互動量約 37 萬），另一語系版本顯示 45% 正面。兩者時點不同，無法判定穩定方向，此指標不可靠。
- X / 新聞：未找到可直接引用的高品質 X 貼文樣本。聚合頁 AI 摘要提到的主題包括 AI 手術需求支撐上檔、安全召回與網路安全疑慮壓抑漲幅、以及 Q2 基本面優於預期與 FDA 510(k) 申請等，但屬自動生成摘要，僅作方向參考。
- 整體聲量：無法與歷史基準做量化比較，僅能定性為「有討論，但樣本不足」。
- 零售傾向：無法可靠判定，暫列為「混合（資料不足）」。

- Themes（僅來自聚合摘要，未直接驗證）:
  - 多頭：手術機器人需求成長、AI 相關題材、財報優於預期後逢低買進。
  - 空頭：美國手術量成長放緩、競爭加劇、安全召回與網路安全風險。
- 財報時點：來源對 Q3 財報日期說法不一（10/19 盤後 vs 10/20 估計），且未確認實際財報內容。此為重要事件風險缺口，請以公司投資人關係頁面為準。

## Insider activity
Net 6mo（2026-04-23 至 2026-10-23）：$0.00M 買入 / $8.08M 賣出，淨賣出約 $8.08M。
無任何公開市場買進紀錄。

| 姓名 | 職位 | 期間 | 賣出股數 | 賣出金額 (USD M) | 備註 |
|---|---|---|---|---|---|
| GUTHART GARY S | 董事 | 2026-08-11 | 10,000 | 4.00 | 單筆最大，@ $400.00 |
| JEDDI IMAN | 高階主管 (Officer) | 2026-06-01 | 5,625 | 2.37 | 同日另有 derivative 行使（未計入賣出） |
| LADD AMY L | 董事 | 2026-04-29 / 08-11 | 合計約 1,091 | 0.76 | 兩筆 |
| LOEB GARY | 高階主管 (Officer) | 多筆（05-11, 06-10, 08-10） | 合計 1,200 | 0.50 | 每季約 400 股，規律性賣出 |
| BROSIUS MARK PRESTON | 高階主管 (Officer) | 多筆（05 至 09） | 合計約 800+ | 0.33 | 十餘筆小額賣出，頻率高 |
| WIDMAN FREDRIK | 高階主管 (Officer) | 2026-09-15 | 1,089 | 0.41 | 含選擇權行使後賣出 |

- CEO（ROSA DAVID J）在 6 個月窗口內無交易紀錄。
- 2026-10-09 有 LOEB GARY、WADORS PATRICIA L. 兩筆無金額申報，性質不明，未計入。
- 多數為小額、規律性賣出，有可能屬 10b5-1 計畫，但工具資料無法確認。大額賣出為 GUTHART（$4.0M）與 JEDDI（$2.37M）。
- 內部人淨買入為零，與分析師多數 BUY 評等方向相反。

## Ownership shifts
- 機構持股占比約 89.5%（institutionsPercentHeld 0.89483），機構數量約 3,129 家。
- 內部人持股占比約 0.51%。
- 工具僅提供當期快照，沒有季度變化序列，無法計算機構淨流入或流出。
- 一個篩選器聚合頁標示 institutional flow 為「Distributing」，且 6 個月報酬約 -26%、YTD 約 -34%，但來源可靠性低，僅作參考。
- 機構淨流向判定：無可靠資料，暫列為「不確定，偏負向（低可信度）」。

## Price context（僅供對照，非本報告結論）
- 聚合頁顯示價格區間約 $373–$410，與 Yahoo 快照的 52 週區間 $396.68–$603.88 或 $425.00–$603.88 不一致，時點不同。
- 近期內部人成交價格區間約 $344–$474（2026-04 至 09）。
- 股價距 52 週高點明顯回落，與內部人持續賣出、機構流向偏負（低可信度）的訊號一致，但未能確認當前價格。

## Net sentiment score
- 分析師面：偏多（BUY 占 76.5%，近四個月 BUY 家數微增）。
- 內部人面：偏空（6 個月淨賣出約 $8.08M，零買進）。
- 零售面：無法判定（Reddit / StockTwits 缺漏，LunarCrush 數據衝突）。
- 機構面：不確定，偏負向（低可信度）。

**Composite：中性（Neutral），略偏多（分析師）與偏空（內部人）並存。信心度：低至中。** 主要不確定性來自零售資料缺漏、財報結果未確認、以及機構流向資料品質。

Divergence flag: **是（yes）**。分析師多數看多，但內部人淨賣出且無買進，方向相反。零售傾向因資料不足，無法確認是否也與分析師相反，需要後續補充。

## Data gaps
- Reddit（WebFetch 無法連線）、StockTwits（主機名稱解析失敗）皆為缺漏來源。
- 分析師個別評等變動與目標價明細未取得。
- 財報實際結果與日期未確認。
- 機構持股季度變化序列未取得。

## Sources
- yf tool: ISRG recommendations / rec_summary / insider / major_holders（2026-10-23 執行）
- WebSearch 聚合摘要（低可信度，僅輔助）：https://explore.nemo.money/llms.txt/stocks/ISRG 、https://equibles.com/stocks/ISRG 、https://www.tipranks.com/stocks/tse:isrg 、https://lunarcrush.com/en/stock/intuitive-surgical-inc-isrg

SENTIMENT REPORT COMPLETE
