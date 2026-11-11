# Sentiment — 5475.TWO (德宏) as of 2026-11-12

資料完整度說明: 本次 yf 工具的 recommendations / rec_summary / insider 回傳空陣列 (Yahoo cookie/crumb 取得失敗, 工具降級後無資料)。Reddit 與 StockTwits 在本沙箱無法連線 (StockTwits 為 DNS 無法解析, 需於 session 網路設定允許 api.stocktwits.com)。本報告的分析師與內部人部分因此無法量化, 僅能以網路搜尋摘要與持股結構資料作為替代, 信心度偏低。

## Analyst consensus
資料不足: rec_summary 回傳空值, 無法取得目前 buy / hold / sell 家數。recommendations 歷史評等變動亦為空。以台股 OTC 小型股的覆蓋程度推估, 證券商覆蓋可能很有限, 但這屬於推論, 未經資料驗證。目標價變動: 無資料。

## Retail social
- Reddit: 無法取得 (r/wallstreetbets、r/stocks 搜尋端點在本沙箱被阻擋, 未重試)。
- StockTwits / X: StockTwits 無法連線 (DNS 失敗)。X 未直接搜尋; 一般新聞搜尋未找到 2026 年 11 月的散戶討論貼文。
- 網路搜尋摘要 (非散戶社群原文, 來源多為財經媒體與資料站, 日期混雜, 部分彼此不一致):
  - 玩股網 (statementdog) 的估值數字顯示股價淨值比在 2026 年 5 月至 8 月間由約 41.65 倍降至約 18.73 倍, 本益比由約 1,378 倍降至約 123 倍。這反映獲利快速回升前的低基期, 單看倍數意義有限。
  - nStock 頁面提到 2026 年 7 月營收為八年來單月新高, 2026 年第二季 EPS 約 0.95 元。
  - 相關報導將題材連結至石英纖維布與 AI 需求 (NVIDIA Rubin 平台對 M9 等級材料與 Q 布的需求)。工商時報引述董事長看法, 認為 AI 相關應用需求增加。
  - Goodinfo 顯示該股曾因玻纖布題材被列為處置股, 處置期限至 2026-11-03, 即本報告日前約一週已到期。
- Retail tilt: 偏多 (以媒體與題材敘事為主, 而非社群原文量化)。信心: 低。

- Buzz volume: 無法量化 (社群來源全數不可用)。
- Themes: (1) AI 供應鏈題材 (石英纖維布、Q 布、高階基板材料); (2) 營收與獲利由虧轉盈的轉折敘事; (3) 處置股解除後的籌碼與波動議題; (4) 估值倍數高企, 獲利基期低。

注意: 上述媒體與資料站的日期有前後不一的情況 (例如一篇 2026-01 的工商時報報導與 2026 年 7 月以後的數據並列), 數字未逐一核對原始財報, 僅作敘事參考。

## Insider activity
資料不足: insider 工具回傳空陣列, 無法計算 6 個月內董監與大股東的淨買賣金額, 亦無法辨識 CEO / CFO 等身分的交易。此項不得視為「無內部人交易」。

## Ownership shifts
- insidersPercentHeld: 約 27.9% (內部人持股比例偏高, 與小型公司控股結構一致)。
- institutionsPercentHeld: 約 2.7%; institutionsFloatPercentHeld: 約 3.8%; 機構家數 7 家。
- 機構持股比例極低, 籌碼以內部與大戶為主。
- 網路搜尋摘要提到 400 張以上大戶持股比例在 2026 年 7 月約 41%, 外資持股約 12.7% (來源為玩股網, 日期為 2026 年 7 月, 與 yf 的機構比例口徑不同, 不可直接相加比較)。
- 趨勢: 無法判斷, 因為缺少多期比較資料。

## Net sentiment score
Composite: 偏多 / 信心低 (neutral-to-bullish, low confidence)。
理由: 唯一可用的正向訊號是媒體敘事 (AI 題材、營收轉折), 但缺少分析師、內部人與社群原始資料, 無法與其他訊號交叉驗證。機構持股極低也意味著專業資金參與度有限, 價格易受題材與散戶情緒影響。

Divergence flag: 無法判定 (分析師與內部人資料缺失, 無法比較零售與分析師方向)。

## 資料來源與限制摘要
- yf: recommendations / rec_summary / insider 為空; major_holders 有部分資料。
- Reddit: 不可用 (沙箱阻擋)。
- StockTwits: 不可用 (DNS 解析失敗, 需允許 api.stocktwits.com)。
- WebSearch: 有數則媒體與資料站結果, 日期與數字未逐一核對, 僅作參考。

本報告不構成交易建議。

SENTIMENT REPORT COMPLETE
