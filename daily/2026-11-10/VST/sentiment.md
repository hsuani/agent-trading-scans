# Sentiment — VST as of 2026-11-10

資料截止：2026-11-07（可取得之最新資料）。2026-11-08 至 11-10 無可用資料，未採用。

## Analyst consensus
目前（0m）共 23 位分析師：Strong Buy 4 / Buy 17 / Hold 2 / Sell 0 / Strong Sell 0。
買進側合計 21/23 = 91.3%，持有 2/23 = 8.7%，賣出 0%。

近期變化（對比 -1m 快照：SB 4 / B 18 / H 0 / S 0 / SS 1）：
- 買進評等減 1、持有評等增 2，符合 KeyBanc 於 11-04 下調為 sector weight（即 Hold 等級）的事件。
- 強烈賣出由 1 降為 0，來源未說明是評等上調還是過期移出。

目標價動向（新聞來源，非 yf 原始資料）：
- BMO 將目標價由 245 上調，原為 236 USD，維持 Outperform。
- Wells Fargo、Scotiabank 於 10 月底降目標價，但維持正面評等。
- BofA 維持 Buy，目標價下調。

股價事件：11-04 因 KeyBanc 下調，股價當日跌約 13.9%；11-06 財報後上漲約 10.6%，財報被描述為創紀錄季度並上調全年指引中點。10-08 至 11-06 期間跌約 20.1%。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：本次抓取失敗（WebFetch 無法連線 reddit.com），無法取得討論串樣本、留言數或情緒傾向。標記為資料缺漏。
- StockTwits：api.stocktwits.com 解析失敗（DNS 無法解析，疑為 session 網路白名單未開放），無法取得訊息量與多空標記。標記為資料缺漏。
- X / 新聞輿情：以網路搜尋取得的二手摘要顯示，近期（10 月底至 11 月初）市場情緒偏分歧：先因評等下調與跌勢轉為悲觀，財報後反彈。摘要來源多為 Trefis、MarketBeat、Barchart 等彙整站，非原始社群貼文，可信度中等。
- 過時的舊參考值：Benzinga 顯示 P/C ratio 0.51、short float 3.3%，但頁面日期為 8 月底，僅供參考，不應用於判斷當前情緒。
- 討論量（buzz volume）：無法量化，無法與平時基準比較。
- 主要主題（依新聞摘要推斷，非貼文原文）：財報超預期與 2027 指引、評等下調後的估值爭論、AI/資料中心電力需求題材、內部人賣出。

## Insider activity
統計窗口：2026-05-10 至 2026-11-10，僅計公開市場交易（Sale / Purchase），排除 Stock Award、Gift、Conversion。

- 買入合計：約 1.17M USD（2 筆，皆為 CEO）
- 賣出合計：約 25.9M USD（11 筆，7 位內部人）
- 淨額：約 -24.7M USD（淨賣出）

明細（金額單位 USD M）：

| 日期 | 內部人 | 職稱 | 方向 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-24 | BURKE JAMES A. | CEO | 買入 | 2,000 | 0.27 |
| 2026-09-01 | BURKE JAMES A. | CEO | 買入 | 6,665 | 0.90 |
| 2026-09-08 | HUDSON SCOTT A | Officer | 賣出 | 44,444 | 6.75 |
| 2026-09-08 | MOLDOVAN KRISTOPHER E. | CFO | 賣出 | 20,000 | 3.02 |
| 2026-10-06 | HUDSON SCOTT A | Officer | 賣出 | 22,222 | 3.56 |
| 2026-10-07 | MOLDOVAN KRISTOPHER E. | CFO | 賣出 | 20,000 | 3.30 |
| 2026-06-02 | MONTEMAYOR MARGARET M. | Officer | 賣出 | 4,600 | 0.74 |
| 2026-05-27 | MONTEMAYOR MARGARET M. | Officer | 賣出 | 5,000 | 0.82 |
| 2026-06-15 | BARBAS PAUL M | Director | 賣出 | 488 | 0.07 |
| 2026-06-16 | HELM SCOTT BRADFORD | Director | 賣出 | 25,000 | 4.00 |
| 2026-06-18 | ACOSTA ARCILIA C | Director | 賣出 | 15,000 | 2.51 |
| 2026-06-18 | SULT JOHN R | Director | 賣出 | 6,500 | 1.11 |

要點：
- CEO Burke 在窗口內為唯一買方，兩次小額買入（合計約 1.2M USD），買價約 135 USD，為窗口內最低價位的買入。
- 窗口內最大賣方為 Hudson（約 10.3M USD）與 Moldovan（約 6.3M USD），皆為 Officer / CFO 身分，多數賣價在 150–165 USD。
- 2026-02-24 有大額年度股票授予（Burke 約 54.9M USD 名目），屬 Stock Award，不計入淨買賣。
- 內部人持股比例 0.77%（yf major_holders）。
- 補充：2025 年 9–10 月 CEO 有大量賣出（多為選擇權行使後賣出，窗口外），不計入本期統計。
- 外部新聞（Trefis）稱過去 12 個月內部人賣出約 19.76M USD，與本統計的口徑與期間不同，未做調和。

## Ownership shifts
- 機構持股比例 92.6%，機構數 1,909 家（yf major_holders）。
- 內部人持股 0.77%。
- 缺乏跨期機構持股變化數據，無法判斷集中度趨勢。標記為資料不足。

## Net sentiment score
- 分析師面：偏多（信心：高）。91% 買進側，目標價多數仍在 245 USD 附近或以上，但有下修。
- 內部人面：偏空（信心：中）。窗口內淨賣出約 24.7M USD，但買方為 CEO 且為窗口內最低價位買入，有反向訊號；賣出是否屬預先規劃交易，本資料無法判定。
- 散戶面：無法評估（信心：低）。Reddit 與 StockTwits 皆無資料，僅有二手新聞摘要，無法量化情緒。
- 綜合：中性偏多（信心：中低）。分析師與內部人方向分歧，散戶面缺資料，整體結論僅屬方向性判斷，非交易建議。

Divergence flag：無法判定（散戶面無資料）。
分析師與內部人方向存在分歧（分析師偏多、內部人淨賣出），此項可作為參考但不等於散戶與分析師分歧。
待 StockTwits 網域開放或 Reddit 可連線後，應補抓散戶資料再重新評估此旗標。

## 資料限制與來源說明
- Reddit：WebFetch 無法連線，已跳過。
- StockTwits：DNS 解析失敗，已跳過。需於 session 網路設定中允許 api.stocktwits.com。
- yf insider 與 rec_summary 來源為 Yahoo Finance 介面；本次 cookie/crumb 取得失敗，但資料仍正常回傳。
- 新聞摘要來源日期與數值存在衝突（部分 MarketBeat 與 Benzinga 頁面為舊資料），僅作參考。
- 未拉取 CEG、TLN、GEV、ETN、PWR、NEE、SO 等同業資料，本報告為 VST 單一標的。

SENTIMENT REPORT COMPLETE
