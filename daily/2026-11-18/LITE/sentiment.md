# Sentiment — LITE (Lumentum Holdings) as of 2026-11-18

資料說明: yf 工具的即時抓取於本次執行時全部失敗 (fc.yahoo.com 連線錯誤), 以下數據均來自 `prices/yf/LITE.json` 快取 (快取時間 2026-11-17 UTC)。Reddit 直接抓取依指示略過; StockTwits 未嘗試 (DATA_UNAVAILABLE)。社群聲量與情緒以 WebSearch 聚合站為主, 可信度低。未引用任何過去 daily/ 日期的報告。

## Analyst consensus

25 位分析師: 3 Strong Buy / 16 Buy / 6 Hold / 0 Sell / 0 Strong Sell (即 19 買進系、6 持有、0 賣出)。共識評級 `buy`。

| 期間 | Strong Buy | Buy | Hold | Sell | 買進系合計 | 持有 |
|---|---|---|---|---|---|---|
| 本期 (0m) | 3 | 16 | 6 | 0 | 19 | 6 |
| -1m | 5 | 18 | 5 | 0 | 23 | 5 |
| -2m | 5 | 18 | 4 | 0 | 23 | 4 |
| -3m | 5 | 17 | 4 | 0 | 22 | 4 |

- 目標價 (yf info 快取): 平均 1,069.19 USD / 最高 1,425.00 USD / 最低 685.00 USD。以快取報價約 540 USD 計, 平均目標價隱含上行約 98%。
- 近期動向: 本期買進系評級由 23 降至 19, 持有由 5 升至 6, 賣出仍為 0。依計數推定為數家買進評級下調至持有, 但 yf 未提供逐筆升降評等紀錄 (`recommendations` 僅回傳月度彙總), 個別券商的調評明細為 DATA_UNAVAILABLE。
- 外部聚合站 (WebSearch) 提及 Stifel 將目標價由 1,100 調至 1,232 USD, Zacks 於 10 月由 Strong Buy 改為 Hold, Weiss Ratings 給予 D- 並於 2026-08-18 調降。以上來源單一、未與 yf 交叉驗證, 僅供參考。

## Retail social

- Reddit: 直接抓取受阻 (依指示略過)。WebSearch 未找到 r/wallstreetbets 或 r/stocks 的 LITE 實際討論串。AltIndex 聚合頁顯示 Reddit 提及量近期為 0 則/日 (較近期均值 -100%), 但同一站另一頁給出情緒分數 85/100 (偏多), 兩者互相矛盾, 日期亦不明, 不採信為定論。
- StockTwits / X: StockTwits 未嘗試 (DATA_UNAVAILABLE)。X 相關聚合 (Quiver Quantitative 整理) 描述 LITE 2026 年漲幅約 136%, 為 S&P 500 表現最佳者之一, 多數帖文偏多; 亦有謹慎者指出分析師意見分歧、需持續業績支撐。
- 聲量: 整體屬低到中等, 無法取得可靠的提及數與基準比較 (聲量相對值: DATA_UNAVAILABLE)。
- 主要主題 (依聚合摘要):
  - 高功率雷射與光路交換器訂單能見度 (摘要稱已有排至 2028 年的訂單)。
  - AI 資料中心 / 超大規模雲端客戶擴產帶動。
  - 估值與漲幅過大之疑慮。
  - 可轉換債發行所造成的機械性賣壓 (聚合站提及)。
  - 併購消息: 聚合站 (ibtimes / marketbeat 類) 提及一項以全股票方式進行、每股換 4.5 股 Marvell 的待決交易, 並稱 Marvell 股價於 10 月下跌約 22% 使隱含價值縮水。**此消息僅見於單一 WebSearch 聚合摘要, 未經 yf 或公司公告驗證, 標示為未確認。**
- 價格參考 (聚合站, 互相矛盾): 11 月初股價大幅回落, 不同來源給出 684、638、545 USD 等數字; 本報告以 yf 快取為準 (fast_info 最新價 549.64 USD、info 現價 540.25 USD), 不以聚合站價位作判斷依據。

## Insider activity

6 個月窗口 (2026-05-18 至 2026-11-18, 來源 yf insider 快取, 最新一筆交易日 2026-09-29):
- 淨買入: 0 USD (期間內無任何公開市場買入)。
- 賣出: 合計約 81.5M USD (依逐筆 Value 加總)。
- 配予 (Stock Award / Grant) 不計入買賣金額。

主要賣出者 (約略數字):

| 姓名 | 職稱 | 期間內賣出金額 (約) | 備註 |
|---|---|---|---|
| Vincent D. Retort | Officer | 約 41M | 2026-08-25 單筆 38,663 股, 約 33.0M USD |
| Wupen Yuen | Officer / President of Global Business Units | 約 13.8M | 2026-05-18 起多次分批出售, 9 月持續 |
| Jae Kim | General Counsel | 約 14.4M | 2026-08-25 單筆 12,000 股, 約 10.2M USD |
| Wajid Ali | CFO | 約 2.4M | 2026-05-18 出售 2,487 股 |
| Michael E. Hurlston | CEO | 約 0.5M | 2026-08-27 出售 548 股 (@958.66) |
| Isaac Harris | Director | 約 4.9M | 2026-05-29 與 06-02 出售 |
| Ian Seymour Small | Director | 約 4.3M | 2026-05-21 出售 |

- 重點觀察: CEO 本期賣出金額極小 (約 0.5M USD), 但 CFO 與多位高階主管 (Retort、Kim、Yuen) 在 8 月前後大量出售, 其中 8/25 一日就有約 43M USD 的賣出。
- 價格脈絡: 2026 年內賣出價格約 530–1,000 USD, 2025 年同類交易多在 75–270 USD, 高階主管於股價高位變現。是否屬 10b5-1 計畫: DATA_UNAVAILABLE (yf 未提供)。
- 資料缺口: 最新一筆交易日為 2026-09-29, 10 月至 11 月中無任何申報紀錄, 可能為資料延遲或確實無交易, 無法區分。

## Ownership shifts

- 機構持股: 94.5% (流通股 94.8%), 機構數 1,964 家。內部人持股 0.33%。
- 最新申報日 (2026-09-30) 主要機構變化:
  - BlackRock 持股 10.74%, 季增 +6.1%。
  - Vanguard Capital Management 持股 6.43%, 季增 +14.8%。
  - Vanguard Portfolio Management 持股 5.15%, 季增 +14.1%。
  - State Street 持股 4.28%, 季增 +12.4%。
  - FMR 持股 3.10%, 季減 -20.1%。
  - JPMorgan 持股 2.81%, 季減 -37.3%。
- 2026-06-30 申報的 Jupiter Topco LLC 持股 2.08%, 季增 +100%, 性質與背景 (是否與併購或其他交易相關) DATA_UNAVAILABLE。
- 解讀: 被動型基金 (Vanguard、BlackRock、State Street) 持股擴大, 較具主動性的 FMR 與 JPMorgan 減持, 機構結構趨向指數化持有。

## Net sentiment score

**Composite: 中性偏多 (neutral-to-bullish), 信心: 中低 (low-to-moderate)。**

- 分析師面 (偏多, 信心中): 19/25 買進系、0 賣出、平均目標價約為現價兩倍。但買進系數量自 -1m 的 23 降至 19, 共識已見鬆動。
- 內部人面 (偏空, 信心中高): 6 個月 0 買入、約 81.5M 賣出, 且多數為 8 月後的大額出售。內部人賣出未必代表基本面轉差 (可能為分散持股或既有計畫), 但屬明確負面訊號。
- 散戶面 (混合, 信心低): 聲量資料不足且來源矛盾, 社群偏多敘事 (AI 訂單、漲幅) 與估值、併購、賣壓疑慮並存。
- 機構面 (中性偏多): 被動基金加碼, 部分主動基金減碼。

**Divergence flag: 是** — 分析師整體偏多與內部人大額賣出方向相反, 且散戶敘事與機構持股變化亦呈分歧。此類分歧通常值得留意, 但本報告不作交易建議。

資料可信度提示: 散戶面資料多為聚合站摘要, Reddit / StockTwits 缺失, 聚合站股價與併購條款未經驗證, 個別評級機構事件僅來自單一來源。

SENTIMENT REPORT COMPLETE
