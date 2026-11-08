# Sentiment — SKHY (Sky Harbour Group) as of 2026-11-09

> 資料品質警示：Reddit 與 StockTwits 直接 API 皆無法取得（Reddit 拒絕 WebFetch；api.stocktwits.com 無法解析 DNS，需於 session 網路設定中放行）。零售情緒部分僅能依 WebSearch 找到的二手資料，信心偏低。另外，本報告 as-of 日期 2026-11-09 晚於系統當日 2026-11-08，所有引用資料皆取自不晚於 2026-11-09 之來源，但可用的最新資料多為 2026 年中至 10 月。
>
> 注意：本檔案 ticker 為 SKHY，但多數二手來源（MarketBeat、Benzinga 等）之 ticker 為 SKYH（NYSE American）。以下假設兩者指同一公司 Sky Harbour Group，yf 工具亦以 SKHY 回傳資料，但未逐一核對代碼對應。

## Analyst consensus

yf `rec_summary` / `recommendations`（三個期間，單位：家數）：

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買方合計 (SB+B) |
|---|---|---|---|---|---|---|---|
| -2m | 4 | 8 | 1 | 0 | 0 | 13 | 12 |
| -1m | 5 | 8 | 1 | 0 | 0 | 14 | 13 |
| 0m (當期) | 5 | 9 | 1 | 0 | 0 | 15 | 14 |

當期分布：**14 buy / 1 hold / 0 sell**（含 5 Strong Buy）。

趨勢：買方家數連續兩期增加（12 → 13 → 14），Hold 與 Sell 維持不變，未見降評。
近期評等變動：yf 歷史資料僅顯示家數變化，未提供個別券商之升降評明細；WebSearch 亦未找到 2026 年具名的升評或降評事件，因此無法列出具體券商動向。

目標價（二手來源，數值不一致，信心中等偏低）：

| 來源 | 目標價均值 | 區間 | 分析師數 | 日期 |
|---|---|---|---|---|
| MarketBeat（無日期快照） | $13.50 | $13–$14 | 5 | 未知 |
| MarketBeat（2026-07-31） | $13.00 | 未提供 | 6 | 2026-07-31 |
| Google Finance | $13.67 | 最高 $14 | 3 | 近 3 個月 |
| Tickflow（2026-08-02） | $14.50 | 僅依 1 位分析師 (Northland, 2024-09 $16) | 1 | 2024 為主 |
| Trader's Union | $16.20 | $12.50–$25 | 32 | 未知 |
| Investing.com（加拿大頁） | $16.71 | 未提供 | 7 | 未知 |

分析：分析師家數從 3 到 32 不等，目標價均值落在 $13–$17 區間。yf 的 15 家與 MarketBeat 的 6 家差距大，可能源於分析師池定義不同（例如是否計入未公開評等之券商）。以 yf 為準作為家數依據，目標價以 MarketBeat 與 Google Finance 為參考，信心中等。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：WebFetch 之 JSON 端點被拒絕，無法取得最新貼文清單與計數。WebSearch 僅找到一則 2026 年 3 月的第三方鏡像貼文，分數 5、留言 1，內容為看多論述（主張 Q4 營運現金流受一次性 $5.9M 租賃預付款影響，並認為資產面有重估空間）。樣本過少，**不具代表性，信心低**。
- **StockTwits**：無法連線，無資料。
- **X / 新聞聊天**：WebSearch 未找到 2026 年 11 月的社群輿情摘要。2022 年 4 月曾因爆量登上 StockTwits 熱門榜，屬歷史事件，不代表當前。
- **聲量（相對量）**：無法量化。以搜尋結果數量判斷，SKHY 之零售討論度屬低檔，但此為弱訊號。
- **Retail tilt**：無法可靠判斷。現有唯一樣本偏多，但樣本數不足以代表整體。
- **Themes（自二手來源推得，非直接觀察）**：
  - 槓桿與現金流：TipRanks AI 評分指出高槓桿、負利潤率、現金流壓力，是主要疑慮。
  - 資產與營收成長：機場機庫租賃之成長與指引被多數分析師正面看待。
  - 空頭部位：做空比例高（見下），可能是部分零售與機構的主要論點。

做空比例（信心低，日期不一）：
- Benzinga：short float 12.2%（日期不明）。
- MarketBeat：2025-10 快照顯示 short interest 約 10.08% of float（資料約一年前，已過時）。

## Insider activity

yf `insider`：回傳空清單（無資料）。

WebSearch 補充（僅供參考，信心低，無法核對 SEC EDGAR 原文）：
- MarketBeat（截至 2026 年 5 月）：2026-04-06 一筆 Boston Omaha 出售 331,500 股，每股 $9.05，約 $3.0M。Boston Omaha 為 10% 持股人，非公司內部人。此筆交易距 2026-11-09 約 7 個月，**位於 6 個月窗口之外**。
- 另一聚合站：近 12 個月有 3 位內部人買進合計約 $185.2K，但未列出姓名與日期。
- 有一份 2026-05-20 之 Form 4 提及 Andrew J. Gessow，交易內容未能取得，無法判定買賣方向與金額。
- 有一份 2026-02-18 之 Form 4 提及 CEO Tal Keinan，內容未揭露，另一來源稱 CEO 近 12 個月未有公開市場賣出紀錄。

6 個月淨額（2026-05-09 至 2026-11-09）：**無法確認**。yf 為空，二手來源互相矛盾，且無 6 個月窗口內的可靠交易明細。
- 若以二手來源的 $185.2K 買進（時間未知）與 $3.0M 賣出（窗口外）為參照，兩者皆不能直接用於判定窗口淨額。
- 具名人物：CEO Tal Keinan 之 6 個月內交易：無法確認。

## Ownership shifts

yf `major_holders`（單一快照，無歷史比較）：
- insidersPercentHeld：0.002%（數值異常低，疑似 yfinance 欄位或單位問題，信心低）
- institutionsPercentHeld：1.02%（同樣異常低，與 441 家機構持有者並存，數字不一致，信心低）
- institutionsCount：441

結論：此組持股數字與機構家數不匹配，無法依此判定集中度變化趨勢。趨勢判斷：**無法確認**。已知的大型持股人為 Boston Omaha（10% 以上持股人，2026 年 4 月有減持記錄）。

## Net sentiment score

| 受眾 | 情緒 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 (bullish) | 中高 | 14 buy / 1 hold / 0 sell；買方家數連續兩期增加；目標價均值 $13–$17，高於 2026 年中股價區間 (~$9.5–$10.2) |
| 零售（Reddit / StockTwits / X） | 無法判定（樣本不足） | 低 | Reddit 與 StockTwits 無資料；僅 1 則第三方貼文偏多；做空比例 10–12% 為弱負向訊號 |
| 內部人 | 中性（無法確認） | 低 | yf 無資料；窗口內無可靠交易；窗口外有 10% 持股人約 $3.0M 減持 |
| 整體綜合 | **偏多 (bullish)，信心中等偏低** | 中低 | 分析師面明確偏多，零售與內部人面資料不足，無法交叉驗證 |

**Divergence flag：無法判定（資料不足）。**
- 分析師偏多，零售傾向未知，因此無法確認是否背離。
- 若以做空比例作為間接代理，存在部分空方部位與分析師偏多的對立，屬弱背離訊號，但此推論未經直接零售資料驗證，不應單獨採信。
- 建議補充：可於 Reddit 與 StockTwits 放行後重新抓取，以確認背離狀態。

資料缺口與待辦：
1. 放行 api.stocktwits.com 網路權限後重抓 StockTwits 訊息流。
2. 直接於 Reddit 搜尋 SKYH / SKHY 取得 wallstreetbets 與 stocks 之近期貼文。
3. 於 SEC EDGAR（CIK 0001823587）核對 2026-05-09 之後的 Form 4，確認 6 個月內內部人淨額。
4. 核對 yf 的 15 位分析師與 MarketBeat 的 6 位之差異，以及 major_holders 異常數值。

SENTIMENT REPORT COMPLETE
