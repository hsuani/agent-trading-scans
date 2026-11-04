# Sentiment — 2356.TW (英業達) as of 2026-11-05

**注意事項**
- 本次執行環境的今天是 2026-11-04，分析日期 2026-11-05 尚未到。以下資料為工具可取得的最新狀態，不是 11/05 當日資料。
- Reddit（r/wallstreetbets、r/stocks）抓取被擋（"unable to fetch"）。StockTwits 網域無法解析（ENOTFOUND），需在 session 網路設定中允許 `api.stocktwits.com` 後才能重試。散戶社群面因此無法量化。
- 金額單位統一為新台幣億元。

## Analyst consensus

共 10 位分析師：2 Strong Buy / 1 Buy / 7 Hold / 0 Sell / 0 Strong Sell。買進側約 30%（3/10），持有 70%，無賣出評等。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 當期（0m） | 2 | 1 | 7 | 0 | 0 |
| 前 1 個月（-1m） | 2 | 1 | 7 | 0 | 0 |
| 前 2 個月（-2m） | 2 | 1 | 7 | 0 | 0 |

- 近期升降評等：`recommendations` 回傳空陣列，無可見的升降評等紀錄。三個期間的分布完全相同，可能是資料源未更新，不能直接解讀為評等凍結。
- 目標價變動：工具未提供，無法判斷。
- 2026-05 GS 報告（來源：stock-llm-wiki 報告頁）：維持中性（Neutral）評等。認為估值合理，看好 AI 伺服器出貨成長與產能擴充，但指出 PC 出貨可能因記憶體成本上升而持平，客戶提前拉貨可能影響下半年需求。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：抓取失敗，無樣本，無法判斷貼文量與傾向。
- StockTwits / X：StockTwits 無法連線。X 無直接可用資料。WebSearch 找不到 2026-11 的散戶看法報導。
- 搜尋結果中能找到的市場論述偏基本面，不屬於散戶情緒：
  - 本益比約 19.0 倍、股價淨值比約 2.73 倍、殖利率約 3.39%（10/16 收盤 59 元）。
  - 8 月營收 832.68 億元，年增 35.83%，為十年單月同期新高。9 月營收年增約 62.87%（來源為 statementdog 頁面摘要，未逐筆核對）。
  - Q2 毛利率約 4.23%，獲利率偏薄。
- 散戶聲量：無法量化，與歷史基準的比較亦無資料。
- 主要主題（依搜尋結果推估，非散戶原文）：AI 伺服器營收成長、低毛利與 PC 需求承壓、記憶體與 CPU 供應短缺風險、美國/墨西哥/泰國產能擴充（資本支出目標為 2026 年加倍）。

## Insider activity

Net 6mo：無資料（`insider` 回傳空陣列，無法計算淨買賣金額）。這是「查無資料」，不能視為零交易。
- 內部人持股比例約 28.5%，屬於高集中度，但工具未提供持股變動趨勢。
- Notable：無。

## Ownership shifts

- 法人持股約 25.4%（占總股本），占流通股約 35.6%，機構數量約 160 家。
- 無歷史持股比例序列，無法判斷增減趨勢。

## Net sentiment score

- 分析師面：中性偏謹慎（70% Hold、0 Sell，買進側 30%）。
- 散戶面：無法判定（Reddit / StockTwits 皆無資料）。
- 內部人面：無法判定（無交易資料）。
- 綜合：**中性（Neutral），信心低**。主要因為散戶與內部人兩項訊號缺失，且分析師的評等分布在三個期間完全相同，可能是資料延遲。
- 背離旗標：**無法判定**。缺少散戶傾向，無法檢查是否與分析師傾向相反。

## 資料檢核

- 估值一致性：收盤 59 元 ÷ 近四季 EPS 約 3.1 元 ≈ 19.0 倍，與來源列出的本益比 19.02 相符。
- 市值粗估：59 元 × 約 25.9 億股 ≈ 1,528 億元（股數為概估值，未由工具直接驗證）。

## 來源
- [statementdog 英業達 2356 分析頁](https://statementdog.com/analysis/2356)
- [GS 報告 英業達2356 20260519（stock-llm-wiki）](https://stock-llm-wiki.pages.dev/data_base/Raw_data/報告/報告_GS_英業達2356_20260519)
- [Inventec Q4 2025 EPS 報導](https://aeo.washinmura.jp/ai/%E8%8B%B1%E6%A5%AD%E9%81%94%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8/en/news/2025-12-01-inventec-corporation-2356-reports-q4-202)

SENTIMENT REPORT COMPLETE
