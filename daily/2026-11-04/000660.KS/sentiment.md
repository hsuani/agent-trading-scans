# Sentiment — 000660.KS (SK Hynix) as of 2026-11-04

> 資料注意: 系統今日為 2026-11-03，本報告 as-of 日 2026-11-04 尚未到達，所有資料為 2026-11-03 前可取得之最新值。

## Analyst consensus

來源: `pipeline/tools/yf 000660.KS rec_summary` (與 `recommendations` 數值一致)

| 期間 | strongBuy | buy | hold | sell | strongSell | 合計 | 偏多家數 (SB+B) |
|---|---|---|---|---|---|---|---|
| 0m (當前) | 12 | 28 | 1 | 0 | 0 | 41 | 40 |
| -1m | 12 | 28 | 1 | 0 | 0 | 41 | 40 |
| -2m | 11 | 28 | 1 | 0 | 0 | 40 | 39 |
| -3m | 11 | 27 | 1 | 0 | 0 | 39 | 38 |

當前分布: 40 buy (含 12 strongBuy) / 1 hold / 0 sell，偏多家數 3 個月內增加 2 家，無任何 sell。

近期調整: yf 無逐筆升降評等紀錄，僅見上表彙總的小幅上修。WebSearch 找到的目標價為美股 ADR SKHY 口徑 (非 000660.KS 韓股本身): MarketBeat 2026-10-20 共識目標價 $253.22 (前一筆 2026-09 為 $247.67)；RBC 於 2026-08 首次覆蓋給予 Outperform、目標價 $200。兩者口徑與日期不同，僅供方向參考。

## Retail social

- **Reddit (r/wallstreetbets、r/stocks):** 無法取得。WebFetch 被拒絕，直接 curl 亦連線失敗 (HTTP 000)，依規則 soft-fail。提及次數與散戶傾向: 未知。
- **StockTwits:** 無法取得。`api.stocktwits.com` DNS 解析失敗，該域名不在本 session 允許網路清單內。需由使用者於 session 網路設定放行後才能重試。
- **X / 新聞與論壇類聊天 (WebSearch 替代):** 找到的內容多為財經媒體與分析師觀點，缺乏真正的散戶貼文。最新可見日期為 2026-10-20 附近，未找到 2026-11 的相關討論。
- **散戶傾向 (由替代來源推估，信心低):** 偏中性偏多。分析師面偏多，但媒體常見「漲幅過大、可能過熱、獲利了結」的提醒，且股價隨記憶體族群拋售而承壓。
- **Buzz 量 (定性):** 無法量化與平常基準比較。

**主要主題 (來自替代來源):**
1. HBM 市佔與 AI 需求: 分析師認為 HBM 市佔約 55% 可維持至 2027 年 (Barchart 2026-08 報導)，是多方論點核心。
2. 族群拋售與高估風險: 記憶體族群 (含 SanDisk 等) 拋售時，SK Hynix 跟跌；先前漲幅大後出現獲利了結與高波動提醒。
3. 記憶體景氣循環: 「memory winter」類擔憂在歷史新聞中反覆出現，屬常見反方敘事。

## Insider activity

- yf `insider` 回傳空陣列。無法確定是該來源對韓股無資料，或確實無交易紀錄，因此 6 個月淨買賣金額 **無法量化**。
- 非官方來源 (MarketBeat 摘要，日期不明，未經 SEC/DART 核對) 提到 SK 集團會長 Chey Tae-won 首次買入 SK Hynix 股票，市場解讀為信心訊號。此為單一未驗證來源，不計入量化分數。
- 建議後續以韓國 DART 大股東申報或 yf 其他欄位補查。

## Ownership shifts

來源: `pipeline/tools/yf 000660.KS major_holders` (單一時點快照，無歷史趨勢)

| 指標 | 數值 |
|---|---|
| 內部人持股 (insidersPercentHeld) | 20.17% |
| 機構持股 (占流通股外) | 38.94% |
| 機構持股 (占浮動股數) | 48.78% |
| 機構家數 (institutionsCount) | 732 |

機構集中度屬中高，但無前期數據，無法判斷增減趨勢。

## Net sentiment score

- **分析師面:** 偏多 (強)。40/41 偏多、0 賣出，3 個月內略升。
- **散戶面:** 無法直接量測。替代來源顯示中性偏多，但含過熱與族群拋售的警示。
- **內部人面:** 無法量化。僅有未驗證的會長買入傳聞。

**綜合: 偏多 (bullish)，信心: 低至中。**
理由: 分析師共識明確偏多，覆蓋廣且 sell 為零；但散戶與內部人兩個維度資料缺失，且主要敘事集中在族群波動與高估風險。

**Divergence flag: 無法判定 (資料不足)。**
目前無可靠的散戶傾向數據可與分析師傾向比較。若日後 StockTwits 或 Reddit 放行，應重新評估是否出現「散戶偏空、分析師偏多」的背離。

## 資料來源與限制

- yf: `recommendations`、`rec_summary`、`major_holders` 成功；`insider` 空陣列；yf 的 cookie/crumb 取得失敗 (ConnectionError)，仍回傳資料，但需留意可能不完整。
- Reddit: 不可達 (WebFetch 拒絕；curl 連線失敗)。
- StockTwits: DNS 解析失敗，域名未放行。
- WebSearch 來源 (替代): Barchart (analysts bullish on SK Hynix)、MarketBeat SKHY 2026-10-20 price alert、MarketBeat SKHY 2026-09-14、StockAnalysis 000660 forecast。
- 上述 WebSearch 多數指 NASDAQ ADR (SKHY) 而非韓股 000660，價格與目標價為 USD 口徑，未做換算。

SENTIMENT REPORT COMPLETE
