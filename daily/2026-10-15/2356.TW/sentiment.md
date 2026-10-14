# Sentiment — 2356.TW 英業達 as of 2026-10-15

> 注意事項
> - **日期落差**: 指定的 as-of 日期 2026-10-15 晚於系統今日 2026-10-14。以下資料最新只到 2026-09-17 左右, 無法涵蓋 10/14 之後的任何事件。
> - **Reddit / StockTwits / PTT 均無法取得**: Reddit 抓取被封鎖; StockTwits 網域無法解析 (ENOTFOUND); PTT 股板搜尋沒有找到實際討論串。散戶面相關欄位全部標為 DATA_UNAVAILABLE。

## Analyst consensus
yfinance `rec_summary` 當前為 **3 buy (含 2 strongBuy) / 7 hold / 0 sell**, 共 10 家。兩個月前為 3 buy / 5 hold / 1 sell, 表示一家賣方由 Sell 轉到 Hold, 其他未變。Investing.com 的彙整 (近三個月 9 家) 為 3 buy / 7 hold / 0 sell, 共識 Neutral。

近期動向 (來自新聞搜尋, 未經 yfinance 交叉驗證):
- Macquarie 於 2026-08-13 升評至 Hold。
- JPMorgan 於 2026-08-12 維持 Hold。
- 外資 2025-12 報告維持中立, 目標價由 48.6 上調至 49 元。這是最近一筆可找到的目標價紀錄, 已明顯落後目前股價。

目標價分歧:
- Investing.com 平均 12 個月目標價約 66.5 元。該頁有 JPMorgan 135,000 元目標價的明顯錯誤資料, 不採用。
- valueinvesting.io 平均約 49.5 元 (18 家)。
- Eulerpool 中位數約 48.2 元。

結論: 賣方共識是持有, 0 家賣出, 目標價多數低於現價 (約 60 元), 估值端偏謹慎。

## Retail social
- **Reddit**: DATA_UNAVAILABLE。來源被擋。
- **StockTwits**: DATA_UNAVAILABLE。api.stocktwits.com 無法解析 (ENOTFOUND)。
- **PTT / X / 社群**: DATA_UNAVAILABLE。搜尋結果沒有 PTT Stock 板串文。
- **討論量 (buzz volume)**: DATA_UNAVAILABLE, 無法與基準比較。
- **Retail tilt**: DATA_UNAVAILABLE, 無法判定多空。

替代參考 (主流媒體與法人觀點, 不代表散戶):
- 2026-07-29 udn 報導: 凱基證券看好伺服器占比逐季提高, 股價「位階偏低」, 當日逆勢漲 2.5% 收 60.3 元。
- 2026-05 法說後: 總經理表示伺服器年增率可望超過 30%, 占比有望突破 50%。報導同時指外資在法說前由買轉賣。
- 傳聞: 與兩家美國大客戶洽談 AI 伺服器 L6 業務 (未證實)。
- 2026-08 營收 832.68 億元, 年增 35.83%, 月增 -7.68%, 為十年同期單月新高 (nStock)。

主要主題 (來自媒體, 非散戶): AI 伺服器 ASIC 與 AMD MI450/455 出貨、伺服器占比提升、資本支出倍增至 10 億美元、外資進出與股價位階、筆電受記憶體漲價影響。

## Insider activity
Net 6mo: **DATA_UNAVAILABLE**。`insider` 工具回傳空陣列, 無法計算買賣淨額, 也無法判定 CEO/CFO 或其他人員的交易。

## Ownership shifts
- 內部人持股 (insidersPercentHeld): 29.5%
- 機構持股 (institutionsPercentHeld): 24.9%; 占流通股 (float) 35.4%
- 機構家數: 155
- `inst_holders` 回傳空陣列, 無法計算季度增減趨勢, 因此持股變化方向為 DATA_UNAVAILABLE。
- 新聞提及外資 4 月以來大買後於法說前轉賣, 屬定性描述, 無法量化。

## Net sentiment score
**綜合評分: 中性偏多 (信心: 低)**

- 分析師面: **中性** (共識 Hold, 0 賣出, 目標價多低於現價)。信心中等, 因為樣本 10 家且目標價資料時效不一。
- 基本面與媒體面: **偏多** (營收創十年同期新高, 伺服器占比預期提升)。但這不是散戶情緒。
- 內部人面: DATA_UNAVAILABLE。
- 散戶面: DATA_UNAVAILABLE。

**背離旗標 (Divergence flag): 無法判定**。散戶資料缺失, 無法比較散戶與分析師的傾向。

**價格資料不一致**: 搜尋結果的股價有 42.95、43.20、59.90、85.40 等多個數字, 多為不同日期的舊快照。可確認的最新價位為 2026-09-17 收盤約 61.5 元 (nStock)。目標價比較以此為準。

## 結構化指標表

| 指標 | 數值 | 狀態 / 備註 |
|---|---|---|
| 分析師 Buy (含 Strong Buy) | 3 (2 SB + 1 B) | yfinance rec_summary, 當期 |
| 分析師 Hold | 7 | 兩個月前為 5 |
| 分析師 Sell | 0 | 兩個月前為 1 |
| 近期評等變動 | Macquarie 升 Hold (2026-08-13) | 新聞來源, 未交叉驗證 |
| 平均目標價 (Investing.com) | ~66.5 TWD | 含明顯錯誤資料, 不採用 |
| 平均目標價 (valueinvesting.io) | ~49.5 TWD | 18 家 |
| 中位數目標價 (Eulerpool) | ~48.2 TWD | |
| 最新可靠股價 | ~61.5 TWD (2026-09-17) | 其他快照日期不明 |
| Reddit 討論量 | DATA_UNAVAILABLE | 來源被封鎖 |
| StockTwits 多空 | DATA_UNAVAILABLE | 網域無法解析 |
| PTT 多空 | DATA_UNAVAILABLE | 無實際串文 |
| 散戶 tilt | DATA_UNAVAILABLE | |
| 內部人 6 個月淨買賣 | DATA_UNAVAILABLE | insider 回傳空 |
| 內部人持股 | 29.5% | |
| 機構持股 | 24.9% (float 35.4%) | |
| 機構家數 | 155 | |
| 機構持股趨勢 | DATA_UNAVAILABLE | inst_holders 回傳空 |
| 2026-08 月營收年增 | +35.83% | nStock |
| 綜合情緒 | 中性偏多 | 信心低 |
| 背離旗標 | 無法判定 | 缺散戶資料 |

SENTIMENT REPORT COMPLETE
