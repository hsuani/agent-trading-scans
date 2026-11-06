# Sentiment — 8358.TWO (金居科技 Co-Tech Development) as of 2026-11-06

資料狀態摘要: 分析師評等 (yfinance) 有資料但僅 3 期快照; 內部人交易 DATA_UNAVAILABLE (工具回傳空陣列, 非確認為零交易); Reddit 與 StockTwits 無法取得; 新聞搜尋最新僅到 2026 年 9 月前後, 11 月無可用的輿情資料。

## Analyst consensus

4 buy / 0 hold / 0 sell (當期 0m: strongBuy 2 + buy 2)。分析師家數極少, 樣本代表性有限。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 0m (當期) | 2 | 2 | 0 | 0 | 0 |
| -1m | 2 | 1 | 0 | 0 | 0 |
| -2m | 1 | 1 | 0 | 0 | 0 |

- 評等分布由 3 家增至 4 家, 全數為買進 (含 strongBuy), 無 hold 或 sell。
- 近兩期無評等轉為中性或看空的紀錄。
- 目標價變動: 工具未提供; 新聞提及某外資目標價 730 元 (報導時間約 2026 年 9 月, 非本日資料)。
- 新聞另提及 1 月有四家研究機構同步喊買 (統一投顧、中信投顧等), 但原始評等明細未驗證。

## Retail social

- Reddit (r/stocks, r/wallstreetbets): DATA_UNAVAILABLE。WebFetch 無法連線 www.reddit.com, 無法取樣討論串, 聲量與傾向皆無法判定。
- StockTwits / X: StockTwits DATA_UNAVAILABLE (api.stocktwits.com 無法解析, 需在 session 網路設定中允許該網域)。X 未有可用結果。
- 中文財經媒體 (非社群) 的可見論述: 基本面偏多, 以營收成長與外資評等為主軸; 股價在 9 月中旬起轉弱, 出現 "注意股" 標示與高本益比 (約 68.7 倍) 的分歧討論。
- 聲量 (相對typical): 無法量化。
- 散見價格資訊不一致: 8 月快照約 341 TWD (52 週區間 108 至 758 TWD), 另一來源 615 TWD, 9 月報導提及 491.5 TWD 盤中價。三者時點不同, 不宜直接比較。

### 主要主題 (由新聞推得, 非社群原文)
1. 高階銅箔 HVLP4 供需缺口, 預期延續至 2027 至 2028 年。
2. 訂單能見度延伸至 2027 年底, 8 月單月合併營收年增約 60%。
3. 高本益比與股價波動, 造成短線情緒分歧。

## Insider activity

Net 6mo: DATA_UNAVAILABLE。`yf insider` 回傳空陣列, 無法區分 "無內部人交易" 與 "資料源未涵蓋台股內部人申報"。建議改用 MOPS (公開資訊觀測站) 董監持股申報資料核對。

## Ownership shifts

- 內部人持股比例約 17.9%。
- 法人持股比例約 24.8% (float 口徑約 30.3%), 法人家數 51。
- 僅單一快照, 無法判定 6 個月或季度趨勢; DATA_UNAVAILABLE for trend。

## Net sentiment score

Composite: **neutral (信心: 低)**。
- 分析師面偏多 (4 buy / 0 sell), 但樣本僅 4 家。
- 零售面無法取得社群資料, 僅有新聞側的分歧 (基本面正向、股價與估值面轉弱)。
- 內部人與法人趨勢資料不足, 無法加權。

Divergence flag: **無法判定 (no retail data)**。若以新聞側論述代替零售傾向, 兩者方向大致一致 (偏多), 但這不是零售情緒的直接證據。

Analyst % BUY: 100% (4/4), 當期。
Institutional flow: 無趨勢資料; 法人持股 24.8%, 51 家。
Retail tone: DATA_UNAVAILABLE (Reddit / StockTwits 皆無法取得; 新聞側為分歧)。

SENTIMENT REPORT COMPLETE
