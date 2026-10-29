# Sentiment — MP (MP Materials) as of 2026-10-30

> 注意: 今日系統日期為 2026-10-29, 指定的 as-of 日期 2026-10-30 尚未到來。本報告以目前可取得的最新資料為準 (多為 2026-10-14 前後的新聞), 沒有 10-30 當日資料。

## Analyst consensus

yf `rec_summary` (本期): **5 Strong Buy / 13 Buy / 1 Hold / 0 Sell / 0 Strong Sell**, 共 19 家。
- 近 4 個月分布幾乎不變: 前 1 個月為 5 SB / 13 B / 1 H, 前 2–3 個月為 5 SB / 13 B / 0 H。最近一期多出 1 家 Hold, 屬小幅轉弱, 幅度有限。
- 近期目標價調整 (來源為 MarketBeat 與 Benzinga 等彙整新聞, 未經原始報告核對):
  - Morgan Stanley 目標價由 $73 降至 $66, 維持 Overweight。
  - Robert W. Baird 目標價由 $80 降至 $65, 維持 Outperform (10-01 報告)。
  - MarketBeat 共識評等為 "Moderate Buy", 平均目標價約 $75 (另一頁面為 $76.58, 日期不同)。
- **資料衝突**: MarketBeat 文字提到 2 家 Sell 評等, 但 yf 顯示 0 Sell。以 yf 為準記為 0, 需再核對。

## Retail social

- **Reddit**: 本次無法取得。`r/wallstreetbets` 與 `r/stocks` 的 JSON 端點被封鎖 (WebFetch 回報無法存取 www.reddit.com)。以 WebSearch 查 Reddit 相關討論也沒有找到任何 MP 串文。Reddit 情緒為**未知**, 不作推論。
- **StockTwits / X**: StockTwits API 無法解析 (api.stocktwits.com 在本次 session 網路白名單外, 需於 session 網路設定中允許)。X 與新聞型搜尋結果有少量 StockTwits 與 Yahoo 討論板連結, 但沒有可計數的貼文樣本, 無法判斷 bullish / bearish 比例。
- **Buzz 量級**: 無法量化。以新聞密度推估, 10 月中旬有數則股價大幅波動報導 (MarketBeat 10-12「下跌 6.2%」、10-14「下跌 6.1%」), 屬中等偏高的關注度, 但不能當作社群聲量的代理。
- **主要議題 (由新聞與報導歸納, 非社群原文)**:
  1. 中國稀土出口管制: 中國限制稀土及磁鐵出口, 是股價主要驅動因子。
  2. 美國政策支持與國防供應鏈定位: 政府支持國內稀土項目的消息曾多次引發大漲。
  3. 估值偏高與執行風險: Zacks 等文章指出股價有溢價, 同時推進多個資本密集項目。
  4. 近期技術面轉弱: 10 月週線下跌約 6.2%, Fintel 動能分數 31.7 偏低。
- **Retail 偏向**: 無直接社群資料。以新聞與價格走勢看, 偏中性, 信心低。
- **代表性引述**: 本次無可用的社群原文, 不引述。

## Insider activity

yf `insider` 回傳空陣列 (Yahoo cookie/crumb 取得失敗), 此結果**不可視為無交易**, 資料可能不完整。以下為第三方彙整 (非 SEC 原始檔), 需以 EDGAR Form 4 核對:
- 4 月: 董事長兼 CEO James Litinsky 大量賣出 (一則彙整顯示約 25.9 萬股, 約 $16.6M, 4/20); 另一則標題指 4/21 公告的內部人賣出金額約 $19.2M。
- 5 月: CEO 再次賣出 (標題金額約 $0.52M, 屬另一筆較小交易, 日期與對象不完全一致)。CFO Ryan Corbett 於 5/8 賣出 20,000 股; 總法律顧問 Elliot Hoops 於 5/8 賣出約 7,000 股。
- 5 月 20 日: COO Michael Rosenthal 買進 17,000 股, 約 $0.96M, 是區間內少數的買入。
- 90 日淨額: 一則彙整估計約 **-$57.2M** (淨賣出)。
- 6 月資料 (6/3 賣出、6/9 買進) 來源內部數字矛盾 ($543K 與 $2.58M 並列), 未能確認, 不納入計算。

**6 個月淨額 (估計)**: 買入約 $1M (已確認), 賣出 **數十 M USD 級** (第三方彙整, 未經 Form 4 核對)。方向為**淨賣出**, 以 CEO 為主要賣方, COO 為唯一已確認的買方。

## Ownership shifts

yf `major_holders`:
- 內部人持股: 19.6%
- 機構持股: 78.3% (流通股中機構占 97.5%)
- 機構家數: 966
- 歷史季度變化: 本次未取得, 無法判斷集中度趨勢。

## Net sentiment score

**Composite: 分析師 bullish (高信心) / 內部人 bearish 偏向 (中等信心, 資料不完整) / 散戶 neutral (低信心, 無直接資料)**
- 綜合判斷: **neutral 偏 bullish** (低到中等信心)。分析師評等結構強勢 (0 Sell, 18/19 為 Buy 或以上), 但目標價連續下修, 內部人以賣出為主, 散戶面無法確認。
- Divergence flag: **無法判定**。散戶資料缺失, 無法確認與分析師是否反向。若日後取得 Reddit 或 StockTwits 資料再重算。

## 資料限制摘要
- 2026-10-30 為未來日期, 本報告依最新可得資料撰寫。
- Reddit 與 StockTwits 均不可用 (封鎖 / 網路白名單外)。
- yf insider 與部分 Yahoo 資料因 cookie/crumb 失敗而可能不完整。
- 第三方內部人與分析師數字有矛盾, 需以 SEC EDGAR 與原始分析報告核對。
- 不含交易建議。

SENTIMENT REPORT COMPLETE
