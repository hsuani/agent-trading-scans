# Sentiment — INTC as of 2026-10-25

## 資料可用性總覽
- Yahoo 分析師 / 內部人 / 持股資料: 可用 (yf 工具)。注意: 本機 Yahoo cookie/crumb 抓取失敗, 但資料仍有回傳。
- Reddit (r/wallstreetbets, r/stocks): 無法取得。WebFetch 被拒, 直接 curl 亦遭 egress proxy 以 403 拒絕連線 (www.reddit.com 不在本 session 允許清單)。以下不含 Reddit 數據。
- StockTwits: 無法取得。api.stocktwits.com DNS 解析失敗 (ENOTFOUND)。
- X / 新聞: 僅有 WebSearch 結果, 來源品質低 (見下方), 不足以作為散戶情緒依據。

## Analyst consensus
49 位分析師 (最新快照 0m): 1 strongBuy / 14 buy / 33 hold / 1 sell / 0 strongSell。
- 買進側 (strongBuy + buy) 15 家, 占 約 31%; 持有 33 家, 占 約 67%; 賣出側 1 家, 占 約 2%。
- 趨勢 (近 3 個月快照): 買進側由 14 家 (-3m: 1+13) 升至 15 家; 賣出側由 3 家 (-3m: 2+1) 降至 1 家; 持有由 31 家升至 33 家。整體為「偏持有、賣方評等小幅改善」。
- 注意: yf recommendations 工具只回傳各期計數快照, 未提供個別評等變動事件, 因此無法列出逐家升降評等紀錄。
- 網路搜尋可見的 2026-10 個別券商動作 (單一來源, 未經交叉驗證, 需在 MarketBeat / TipRanks 核對):
  - JPMorgan (Harlan Sur) 據稱由 Underweight 升至 Neutral, 目標價 $85 (約 2026-10-19)。
  - Northland (Gus Richard) 據稱約六週前升至 Outperform, 目標價 $120。
  - Mizuho Neutral (2026-10-06 重申), TD Cowen Hold (2026-09-24 重申), Tigress Buy (2026-09-15 重申), BofA Buy (2026-07-28), Baird Neutral (2026-07-27)。
- 目標價共識: 未取得可靠的當前平均目標價, 不予估算。

## Retail social
- Reddit: 無資料 (存取遭拒, 見上方)。
- StockTwits: 無資料 (DNS 失敗)。
- X / 網路論壇: 搜尋結果主要來自 historicaloptiondata.com 的自動化選擇權分析頁 (最新至 2026-09-03), 內含 X 貼文摘要 (約 4 多 / 2 空 / 2 中性, 2026-08-25)。該站點的價格數字彼此矛盾, 且「情緒」段落疑為自動產生, 不代表真實散戶討論。此來源僅作參考, 不計入權重。
- 聲量 (buzz volume): 無法量化與常態比較。
- 主要主題 (僅由上述低可信來源推得):
  - 多方: 財報超預期、分析師上調、晶片關稅與先進封裝相關消息、伺服器 CPU 供應緊俏 (Northland 論述)。
  - 空方: 與 AMD、NVIDIA 競爭、估值疑慮、GAAP 每股盈餘為負 (trailing EPS 約 -$2.12, 淨利率約 -19.6%)。
- 潛在催化劑: 上述來源提及 Q3 財報可能於 2026-10-27 公布 (未經官方確認), 位於本報告日之後, 散戶情緒可能在此前後放大。

## Insider activity
Net 6mo (2026-04-25 至 2026-10-25, 以 USD 計, 單位: M USD):

| 類別 | 金額 (M USD) | 筆數 | 說明 |
|---|---|---|---|
| 公開市場買進 (Purchase) | +10.00 | 1 | CEO Lip-Bu Tan, 2026-08-11, 105,263 股 @ $95.00, 間接持有 (I) |
| 公開市場賣出 (Sale) | -6.49 | 2 | CTO Nagasubramanian Chandrasekaran 2026-05-29 賣 21,024 股 @ $118.28 (約 -2.49); Officer April Miller 2026-05-01 賣 40,256 股 @ $99.53 (約 -4.01) |
| 淨額 | **+3.51** | | 買進大於賣出 |

- 換算核對: 105,263 × 95.00 = $9.999985M; 21,024 × 118.28 = $2.487M; 40,256 × 99.53 = $4.007M。
- 其他同期紀錄 (無金額, 多為 RSU 歸屬、年度董事授予或申報性質, 不計入淨額): CTO 2026-07-30 (33,007 股)、CFO David Zinsner 2026-06-01 (37,015 股)、董事 2026-05-07 年度授予 (每人約 12,552 股)、Officer 2026-04-30 (33,008 股)。
- 值得注意:
  - CEO 於 8 月以 $95 公開買進約 $10.0M, 為本期最強的內部人買入訊號, 且為間接持有。
  - 同期的賣出集中在 5 月 (股價約 $99–118 區間), 由 CTO 與 Officer 執行。
  - CFO Zinsner 於 2026-01-26 以 $42.50 買進約 $0.25M (超出 6 個月窗口, 僅供背景參考)。
- 內部人持股占比 13.99%。

## Ownership shifts
- 機構持股占已發行股數 62.94%; 占流通股 (float) 73.18%; 機構家數 4,409。
- 內部人持股 13.99%。
- 僅取得單一時點快照, 無歷史序列, 無法判斷集中度趨勢。

## Net sentiment score
**Composite: neutral (信心: 低至中)**
- 分析師面: 偏中性 (67% 持有, 買方占比略升, 賣方明顯減少), 略偏正面的邊際變化。
- 內部人面: 偏正面。CEO 公開買進 $10.0M 大於同期賣出 $6.5M, 淨額約 +$3.5M。
- 散戶面: 無有效資料 (Reddit / StockTwits 皆不可取得; 唯一來源可信度低)。
- 因散戶面缺失, 綜合評分的信心受限, 主要依賴分析師與內部人兩項。

**Divergence flag: 無法判定 (no)**
- 目前無可靠散戶傾向數據, 無法檢驗散戶與分析師是否相反。
- 若以分析師與內部人對比: 兩者方向大致一致 (中性偏正), 未見明顯背離。
- 待補充: 重新嘗試 Reddit / StockTwits 資料, 或改由其他經允許的來源取得散戶情緒, 再重新評估背離旗標。

SENTIMENT REPORT COMPLETE
