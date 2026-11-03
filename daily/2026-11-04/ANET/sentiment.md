# Sentiment — ANET as of 2026-11-04

> 資料限制: 今日實際日期為 2026-11-03, 本報告以 2026-11-04 為 as-of 標示。Reddit 與 StockTwits 無法取得, 散戶情緒部分資訊不足。Yahoo cookie/crumb 取得失敗, yf 輸出可能來自快取, 分析師評等快照日期未確認。

## Analyst consensus

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 (家) | 買進比 (SB+B) |
|---|---|---|---|---|---|---|---|
| 目前 (0m) | 7 | 24 | 1 | 0 | 0 | 32 | 96.9% |
| 3 個月前 (-3m) | 8 | 23 | 0 | 0 | 0 | 31 | 100% |

共 32 家覆蓋, 32 家中 31 家為買進評等 (96.9%), 1 家 Hold, 0 家 Sell。相較 3 個月前, 新增 1 家覆蓋且為 Hold, Strong Buy 減 1 家。買進比小幅下降但仍屬高度一致的多方共識。

近期評等變動: yf 的 `recommendations` 只回傳彙總計數, 無個別券商升降評等明細, 無法列出具體 upgrade/downgrade 與目標價變動。外部搜尋結果 (來源不一, 日期多為 2026 年 7 月以前) 提到 TD Cowen 於 2026-07-13 給予 $210 目標價, 共識目標價約 $185–188, 但這些數字已早於 as-of 日期, 僅供參考, 不納入評分。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): 取得失敗。WebFetch 回傳無法連線, 直接以 curl 測試亦被 proxy 以 403 拒絕。本段無資料。
- StockTwits: 無法解析網域 (api.stocktwits.com), 需於 session 網路設定中允許該網域後再試。本段無資料。
- X / 新聞搜尋: WebSearch 未找到 2026 年 10 月底至 11 月初的相關討論, 結果多為聚合網站的舊頁面 (分析師彙整與 2026 年中股價), 無法代表當前散戶語氣。
- 聲量 (buzz volume): 無法量化, 無法與常態比較。
- 語氣 (tilt): 無法判定。缺乏近期散戶原始資料, 不做方向性推論。
- 主題 (themes): 無可靠樣本, 無法列出重複出現的主題。
- 引述: 無可引用的近期貼文。

## Insider activity

Net 6mo (2026-05-04 至 2026-11-03): 公開市場買入 $0M / 公開市場賣出 $1,162.6M (36 筆, 約 610 萬股)。另有選擇權/衍生性證券行使 6 筆 ($6.3M 行使價值, 非公開市場買入)。無 P (open-market purchase) 紀錄。

| 內部人 | 職位 | 6mo 賣出筆數 | 賣出金額 (USD M) | 備註 |
|---|---|---|---|---|
| Jayshree Ullal | CEO | 11 | 580.2 | 最後一筆 2026-10-09, 約 $217 |
| Andreas Bechtolsheim | 10%+ 大股東 (非高管) | 11 | 544.6 | 最後一筆 2026-09-17, 約 $194–204 |
| Kenneth Duda | President | 4 | 32.1 | 另有衍生性證券行使; 最後一筆 2026-10-20 |
| Charles Giancarlo | Director | 2 | 2.7 | 定期小額賣出 |
| Mark Templeton | Director | 2 | 2.0 | 最後一筆 2026-10-01 |
| Chantelle Breithaupt | CFO | 3 | 0.8 | 小額 |
| Kelly Battles | Director | 2 | 0.1 | 小額 |
| Yvonne Wassenaar | Director | 1 | 0.1 | 小額 |

觀察:
- 賣出金額高度集中於 CEO 與 10% 大股東, 兩者合計約 $1.12B, 佔總賣出金額約 96%。
- Ullal 與 Bechtolsheim 的交易呈分批、多期出售型態 (多日、每日數十萬股), 2026 年 5 月至 10 月持續進行, 價格區間約 $140 至 $217。本報告無法確認是否為 10b5-1 計畫。
- 未見任何內部人公開市場買入。
- 另有 19 筆無金額欄位的紀錄 (多為年度董事/高管授予或申報型紀錄), 未計入上述統計。

## Ownership shifts

- 內部人持股: 17.2%
- 機構持股: 73.4% (占流通股 88.7%)
- 機構家數: 3,211
- 趨勢: 工具僅提供單一時點快照, 無法判斷近期增減。

## Net sentiment score

- 分析師: 偏多, 信心高 (96.9% 買進, 無 Sell)。
- 內部人流向: 偏空 (金額大, 集中於 CEO 與大股東, 無公開買入), 但多為持續性獲利了結型態, 解讀信心中等。
- 散戶: 無資料, 信心低。
- 綜合: 中性 (信心: 低到中)。分析師偏多與內部人淨賣出並存, 整體不構成明確單向訊號。

Divergence flag: 無法判定 (散戶資料缺失)。若以分析師與內部人對比, 呈現「分析師偏多、內部人大額賣出」的分歧, 此分歧值得後續追蹤, 但不應直接解讀為散戶與分析師背離。

## 後續補強建議
- Reddit / StockTwits 網域放行後重跑散戶段落。
- 確認 yf 快照日期 (rec_summary 與 insider), 必要時以 `refresh-cache` 或 Yahoo 可連線時重取。
- 取得 13F 季度機構持股變化, 補上持股趨勢。

SENTIMENT REPORT COMPLETE
