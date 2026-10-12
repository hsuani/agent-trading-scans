# Sentiment — ARQQ (Arqit Quantum) as of 2026-10-13

> 資料時效聲明: 系統當前日期為 2026-10-12, 本報告以 2026-10-13 為標示日期。內部交易資料最新一筆為 2026-10-06, 其後無可用資料。不採用 2026-10-13 之後的任何資料。

## Analyst consensus
DATA_UNAVAILABLE. `pipeline/tools/yf ARQQ rec_summary` 與 `recommendations` 均回傳空陣列。Proxy 紀錄顯示 query2.finance.yahoo.com 與 guce.yahoo.com 的 CONNECT 請求被 gateway 以 403 拒絕 (政策阻擋), 因此無法取得 buy/hold/sell 分布、評級變動或目標價。此為存取限制, 並非該股無覆蓋。

## Retail social
- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE. 公開 JSON 端點無法存取 (WebFetch 回報 "unable to fetch from www.reddit.com")。
- StockTwits: DATA_UNAVAILABLE. 主機名稱無法解析 (getaddrinfo ENOTFOUND api.stocktwits.com), 依規定軟失敗。
- X / 新聞搜尋: WebSearch 未找到 2026-10 的 ARQQ 相關評論或意見文章。最新結果為 2026-04 與 2026-05 的自動生成站點, 內容含無關填充文字, 不納入判斷。引用: 2026-04-01 一則頁面提及股價約 $13.59, 支撐 $12.91、壓力 $14.27; 2026-05-20 一則頁面提及 ARQQW (權證, 非普通股) 約 $0.08。兩者皆屬低品質來源, 僅供背景參考。
- 聲量 (buzz volume): DATA_UNAVAILABLE, 無法與歷史基準比較。
- 情緒傾向: DATA_UNAVAILABLE。
- 主要主題: DATA_UNAVAILABLE。

## Insider activity
資料來源: `pipeline/tools/yf ARQQ insider`, 區間 2026-04-13 至 2026-10-06 (6 個月)。

Net 6mo: 公開市場買入 $0 (無 open-market buy); 公開市場賣出約 $2.65M (2,648,688 美元, 依 Value 欄位加總)。

另有行權轉換 (Exercise of derivative security at $2.50, 非市場買入), 合計約 $11.98M 名義價值: Lefebvre D'Ovidio (間接持有, 2026-09-22, 4.6M 股, $11.5M); Calabria (2026-06-03, 120,000 股, $0.30M); Ritchie (2026-06-05, 73,562 股, $0.18M)。

賣出明細 (依日期):

| 日期 | 人員 | 職位 | 股數 | 約略金額 (USD) | 成交價 |
|---|---|---|---|---|---|
| 2026-10-06 | Andrew Leaver | CEO | 2,398 | 58,011 | 24.19 |
| 2026-10-05 | Andrew Leaver | CEO | 2,535 | 60,294 | 23.78 |
| 2026-10-02 | Andrew Leaver | CEO | 2,818 | 68,969 | 24.47 |
| 2026-10-02 至 10-06 | Willcocks / Feenan / Nilan / Wilder / Ritchie | GC / Officer / Officer / COO / Director | 多筆 | 合計約 $0.3M | 23.78–24.47 |
| 2026-07-02 | Andrew Leaver | CEO | 9,893 | 249,329 | 25.20 |
| 2026-07-01 | Lefebvre D'Ovidio (間接) | Director | 54,444 | 1,642,643 | 30.07–30.24 |
| 2026-06-30 | Patrick Willcocks | General Counsel | 4,000 | 117,920 | 29.48 |
| 2026-06-22 | Jennifer Bers | Officer | 8,288 | 177,529 | 21.42 |
| 2026-04-20 | Nicholas Pointon | CFO | 435 | 6,903 | 15.87 |

Notable:
- CEO Andrew Leaver 在 2026-07-02 與 2026-10-02/05/06 合計賣出逾 2 萬股 (約 $0.5M), 為高頻率賣出。
- 最大單筆為 Director Manfredi Lefebvre D'Ovidio 間接持有之 54,444 股 (約 $1.64M, 2026-07-01)。
- 2026-10 初的多筆賣出價落在 $23.78–24.47, 相較 2026-07 的 $25.20–30.24 與 2026-04 的 $13.25–15.87 形成價格區間線索 (取自成交價, 非市場報價)。
- 資料中另有多筆 Value 為空白的 Ownership=D 記錄 (如 2026-10-01 至 10-06 期間 CEO 每日約 5,200 股量級), 性質未標示 (可能為 RSU 歸屬、稅務代扣或其他非市場交易), 無法確認為賣出, 未計入上述金額。

## Ownership shifts
- 內部人持股 (insidersPercentHeld): 2.63%
- 機構持股 (institutionsPercentHeld): 82.43%; 流通股機構持股 (float): 84.65%
- 機構數量 (institutionsCount): 95
- 趨勢: 工具僅回傳單一時點快照, 無歷史序列, 無法判斷近期增減持趨勢。

## Net sentiment score
Composite: **bearish (低信心)**

判斷依據僅來自內部交易。分析師與散戶兩側皆為 DATA_UNAVAILABLE, 無法交叉驗證。內部人 6 個月內無公開市場買入、賣出合計約 $2.65M, 且 2026-10 初集中出現多名高階主管與董事賣出, 偏向負面訊號。但行權轉換與 RSU 類記錄可能扣除部分賣壓的解讀空間, 且內部人賣出亦可能為個人稅務或多元化安排, 單看金額不足以定論。

Divergence flag: **無法判定** — 缺少分析師評級與散戶情緒資料, 無法比較兩者傾向是否相反。

資料缺口與後續建議: 待 Yahoo Finance 端點恢復後重抓 rec_summary 與 recommendations; 若 Reddit / StockTwits 可存取, 補充散戶聲量與主題。

SENTIMENT REPORT COMPLETE

## Metrics

| 指標 | 數值 | 備註 |
|---|---|---|
| 分析師 buy / hold / sell | DATA_UNAVAILABLE | yf 回傳空陣列, Yahoo 端點 403 |
| 近期評級變動 | DATA_UNAVAILABLE | 同上 |
| 目標價變動 | DATA_UNAVAILABLE | 同上 |
| Reddit 樣本數 | DATA_UNAVAILABLE | 公開 JSON 無法存取 |
| StockTwits 訊息數 | DATA_UNAVAILABLE | 主機無法解析 |
| 散戶聲量 vs 基準 | DATA_UNAVAILABLE | 無資料 |
| 6 個月公開市場買入 | $0 | 無 open-market buy |
| 6 個月公開市場賣出 | ~$2.65M (2,648,688) | 依 Value 加總 |
| 6 個月行權轉換名義價值 | ~$11.98M | 非市場買入 |
| 最大單筆賣出 | ~$1.64M | Lefebvre D'Ovidio (間接), 2026-07-01 |
| CEO 近期賣出 (2026-07 起) | 約 $0.5M | Leaver, 高頻 |
| 內部人持股 | 2.63% | yf major_holders |
| 機構持股 | 82.43% | yf major_holders |
| 機構家數 | 95 | yf major_holders |
| 機構持股趨勢 | 無法判定 | 僅單一時點 |
| 綜合情緒 | 偏空 (低信心) | 僅內部交易單一來源 |
| 背離旗標 | 無法判定 | 缺分析師與散戶資料 |
