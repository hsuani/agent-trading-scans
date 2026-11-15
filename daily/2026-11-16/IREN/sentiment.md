# Sentiment — IREN as of 2026-11-16

> 資料時點注意：本報告依要求標示 as-of 2026-11-16，但執行當下系統日期為 2026-11-15，所有資料皆為可取得的最新快照，未包含 11-16 當日盤中或收盤後資訊。

## Analyst consensus

目前 20 位分析師：15 buy（含 strongBuy 2）/ 5 hold / 0 sell / 0 strongSell。

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 | 買方占比 |
|---|---|---|---|---|---|---|---|
| 當前 (0m) | 2 | 13 | 5 | 0 | 0 | 20 | 75% |
| 前1月 (-1m) | 3 | 13 | 4 | 0 | 0 | 20 | 80% |
| 前2月 (-2m) | 2 | 13 | 5 | 0 | 0 | 20 | 75% |
| 前3月 (-3m) | 1 | 12 | 3 | 0 | 1 | 17 | 76% |

近期變化：過去一個月有一檔 strongBuy 降為 hold（買方家數由 16 降為 15，hold 由 4 升為 5），無 sell 評等出現。三個月內評級結構大致穩定，沒有明顯的集體降評。

目標價變動：yf 工具未提供個別目標價與升降評紀錄，無法確認近期目標價調整。網路搜尋結果提到 Bernstein 下修目標價但仍維持上行空間，以及 MarketBeat 的平均目標價數字，但這些來源日期與數字不一致，未經驗證，不納入結論。

## Retail social

- Reddit (r/wallstreetbets, r/stocks)：無法取得。WebFetch 對 reddit.com 回應無法連線，本次無貼文樣本、無情緒計數。
- StockTwits：無法取得。api.stocktwits.com 無法解析網域，需於 session 網路設定中允許該網域後才能重試。
- X / 新聞輿情（WebSearch）：可得資料有限，且多數結果為 2025 年底至 2026 年初的舊聞。
  - 近期主要敘事偏向融資風險：市場擔心 IREN 於 FY2027 可能需要約 250 億至 300 億美元資本支出，加上 neocloud 同業（如 CoreWeave、Nebius）債務成本上升，壓抑股價。
  - 另有 10 月 MarketBeat 類型的快訊，描述股價大幅波動（單日 ±5% 至 ±9% 皆有出現），以及 AI 基礎設施與 neocloud 類股因 Anthropic IPO 申請而獲得關注。
- 聲量（相對一般水平）：無法量化。缺乏 Reddit 與 StockTwits 計數，只能定性判斷新聞與快訊頻率屬於高波動股的正常水準，未見異常爆量的證據。
- 散戶傾向：無法直接判定；就新聞內容而言為「混合偏空」（融資與債務疑慮）夾雜「仍看多」的分析師與市場觀點。信心：低。

- 主要主題（依網路搜尋歸納）：
  1. 資本支出與融資缺口（FY2027 約 250 億至 300 億美元需求）
  2. Neocloud 同業債務成本與估值壓力
  3. AI 基礎設施需求與題材帶動的反彈
  4. 股價高波動與短期跌幅快訊

- 代表性散戶觀點引述：無（無可用的社群貼文樣本）。

- 不採信項目：網路搜尋提及「過去 7 天下跌超過 21%」與「Wall Street Zen 於 11-15 由 Hold 下調至 Sell」，但第二次搜尋顯示 Wall Street Zen 對 IREN 的調整紀錄為 2025-12-23（Hold 至 Sell）與 2026-02-07（Hold 至 Strong Sell），找不到 11 月的對應紀錄，此說明視為日期誤植，未採用。

## Insider activity

Net 6mo（2026-05-16 至 2026-11-16）：公開市場買入 $0M，賣出 $0M（yf insider 紀錄中，6 個月內僅有 2026-07-01 的股票獎勵授予，無公開市場買賣）。

6 個月內的獎勵授予（價格 $0，屬於薪酬配發，非買入信號）：
- CEO William Gregory Roberts 與 Daniel John Roberts：各 9,651,525 股（間接持有；兩筆紀錄股數相同，疑為同一配發的重複申報，不可直接加總）
- CFO Anthony J. Lewis：26,968 股（直接）
- 董事 Michael Alfred、Sunita Parasuraman、Christopher Guzowski：各 6,657 股；David James Bartholomew：8,369 股

最近一次公開市場賣出（超出 6 個月窗口，僅供參考）：
- 2025-09-11：CEO Roberts（兩筆紀錄各 1,000,000 股，價格 $33.13，每筆約 $33.1M；兩筆疑為同一交易的重複記錄，不可合計為 $66.3M）
- 2025-09-16：董事 Guzowski 11,958 股，價格 $36.32，約 $0.43M

解讀：6 個月內內部人無公開市場買賣，CEO 於 2025 年 9 月的大額賣出超出本窗口，對近期情緒的權重有限。

## Ownership shifts

- 機構持股比例 59.3%（float 口徑 64.0%），機構家數 919；內部人持股 7.4%。
- 前 10 大機構合計約 23.0%（以 pctHeld 加總）。主要持股：
  - Bank of America 3.35%（季度增持 +5.6%）
  - BlackRock 3.14%（+2.0%）
  - Goldman Sachs 2.95%（+1.2%）
  - Citigroup 2.92%（+0.1%，2026-09-30 資料）
  - Situational Awareness LP 2.23%（-0.2%，唯一明顯減持的前十大持有人）
  - Value Aligned Research Advisors 2.00%（+0.8%）
  - Morgan Stanley 1.71%（+0.9%）
  - BIT Capital GmbH 1.66%（+0.1%）
  - State Street 1.60%（+0.1%，2026-09-30 資料）
  - UBS 1.48%（+0.9%，2026-09-30 資料）
- 趨勢：前十大持有人以小幅增持為主（10 家中 9 家為正值），僅 Situational Awareness 一家減持，集中度未見明顯變化，屬溫和的機構累積跡象。資料來自 13F 季報，時效落後約一至數個月。

## Net sentiment score

Composite：**中性偏多（neutral-to-bullish），信心：低至中**

- 分析師面：偏多。15/20 買方評等，0 賣方，評級結構近三個月穩定，但過去一個月出現一檔 strongBuy 下調為 hold。信心：中高。
- 散戶面：無法判定（Reddit 與 StockTwits 皆不可取得）；新聞基調混合偏空（融資與債務疑慮）。信心：低。
- 內部人面：中性。6 個月內無公開市場買賣，僅獎勵授予。
- 機構面：溫和偏多（前十大多數增持）。

Divergence flag：**部分分歧（partial）**。分析師偏多，而網路新聞與融資敘事偏空，但缺乏散戶社群資料，無法確認散戶是否與分析師方向相反。信心低，此旗標不應單獨作為判斷依據。

資料缺口：Reddit、StockTwits 不可取得；目標價升降評紀錄缺失；網路搜尋結果日期混雜，部分來源未經驗證。若需提高信心，建議在 StockTwits 網域開放後重新抓取，並以可靠的新聞來源補充 2026 年 10 月至 11 月的目標價與評等變動。

SENTIMENT REPORT COMPLETE
