# Sentiment — UUP as of 2026-11-21

本標的為 ETF（做多美元對沖工具），依指示略過內部人交易與機構持股區塊。資料可得性整體偏低。

## Analyst consensus
DATA_UNAVAILABLE。`yf UUP rec_summary` 與 `yf UUP recommendations` 皆回傳空陣列，無法得出 buy/hold/sell 分布。ETF 通常不被個股式評級覆蓋。

## Strategist / 機構觀點（替代指標）
- 2026-11 中旬美元指數（DXY）約 103 上下，ING 認為美國成長強勁與通膨黏性（超過 3%）將使聯準會維持緊縮態勢至 2027 年第一季，偏多美元。
- DBS 指出美國殖利率下行削弱美元吸引力，認為美元上行空間受限（風險重定價），偏中性或謹慎。
- 另一則評論認為若就業數據強勁且 12 月升息機率提高，DXY 可能回測 102.00 附近。
- 摩根史丹利的「美元將跌至 94」情境來自 2026 年較早的展望，已不反映當前狀況，不採用。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE，WebFetch 遭封鎖。
- StockTwits：DATA_UNAVAILABLE，api.stocktwits.com 無法解析。
- X / 新聞聲量：WebSearch 未找到 2026-11 針對 UUP 本身的散戶討論，無法估算提及量。
- 主題（僅能由新聞與評論推得，非散戶原始貼文）：利率路徑與聯準會升息預期是主軸；「美國成長 vs 殖利率回落」的拉鋸是主要分歧。

## 基金資金流向（作為情緒代理）
- 資料不一致且日期不明，不可直接採信：某來源顯示 1 年期淨流量約 -1.997 億 USD；Pensions & Investments 顯示 1 個月流量約 42M USD，但快照日期不明。
- 2026-11 的實際淨創設／淨贖回：DATA_UNAVAILABLE。
- 基金規模（AUM）來源衝突：約 445M USD、480M USD、206M USD、1.19B USD 皆有，無法確認。
- 價格快照：2026-11-13 約 29.50 USD；2026-11-06 收盤約 28.93 USD（來源不同，僅供參考）。

## 投機部位（CFTC COT，替代指標）
- 最近可見快照為截至 2026-11-03 當週：USD 淨多頭，EUR、JPY、GBP、AUD、NZD、CAD、CHF 皆為淨空頭。此資料已有數日延遲。
- 另一無日期來源指稱美元多頭曝險連續四週增加，對歐元、英鎊、澳幣的空頭部位創新高，日期無法確認。

## Net sentiment score
**綜合：偏多美元（neutral-to-bullish），信心：低。**
- 支持偏多的依據：投機部位顯示 USD 淨多頭且近期增加；利率與聯準會升息預期支撐美元。
- 抵銷因素：DBS 等看法認為殖利率回落與風險重定價限制上行；資金流向資料矛盾，無法確認籌碼方向。
- 信心低的原因：散戶社群（Reddit、StockTwits）與分析師評級全數缺失，且 COT 與資金流資料時效不足。

**Divergence flag: DATA_UNAVAILABLE。** 因分析師評級與散戶資料皆缺，無法比較兩者是否背離。

SENTIMENT REPORT COMPLETE
