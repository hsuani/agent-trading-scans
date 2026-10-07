# Sentiment — 8046.TW 南亞電路板（南電） as of 2026-10-08

資料狀態說明：本次以 WebSearch 與 yfinance 本地工具取得資料。Reddit、StockTwits 未直接取得（DATA_UNAVAILABLE）。內部人交易 yfinance 回傳空陣列，公開搜尋亦無 2026 年申報紀錄（DATA_UNAVAILABLE）。搜尋摘要中的股價快照日期彼此不一致，下列數字需視為「約略時點」，並非當日收盤。

## Analyst consensus

yfinance `rec_summary`（period 0m）：3 strongBuy / 10 buy / 1 hold / 0 sell / 0 strongSell，共 14 家，即 13 買進、1 持有、0 賣出。近四個月結構穩定，僅 -3m 時 strongBuy 由 2 家變為 3 家，屬小幅變化。

近期券商動向（來源為 Investing.com 搜尋摘要，未能逐一核對原始報告）：
- Goldman Sachs：Buy，目標價 2,310 TWD，2026-07-13 重申評等（先前 2026-04-22 目標 970 TWD）。
- Citi：Buy，目標價 1,550 TWD，2026-07-01 重申。
- CLSA：Buy，目標價 1,300 TWD，2026-06-25 重申。
- UBS：Neutral，目標價 875 TWD，2026-05-22（當時股價約 934 TWD，目標價低於股價）。
- 另一篇摘要提到某外資 2026-07-13 將目標價由 1,444 調升至 2,444 TWD，券商名稱未確認，與 GS 數字不同，無法確定是否為同一家。

平均目標價數字不一致：8 月快照為 1,581.75 TWD，10 月快照為 1,731.54 TWD。valueinvesting.io（865.79 TWD）與 AlphaSpread（約 131 / 435.63 TWD）數字明顯過舊，不採用。

Consensus 方向：偏多。多數目標價高於搜尋摘要中的近期股價，UBS 為唯一中性評等。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。本次未直接抓取，無法給出提及次數或多空比例。
- StockTwits：DATA_UNAVAILABLE。
- PTT 股板：未搜尋到直接討論串。
- CMoney 南電討論區（代理指標）：搜尋摘要顯示討論以 ABF 題材為主軸，氣氛偏觀望。
  - 看多：ABF 缺貨與價格走高被視為本輪行情核心，AI GPU、ASIC、CoWoS 產能布局是主要論點。
  - 謹慎：有人認為 ABF 可能回檔，也有人提醒風控、避免追高，並觀察外資與主動 ETF 買賣。
  - 整體：摘要以「尚未形成一致多空方向」概括。以上為搜尋摘要的歸納，非逐篇原文引用。
- 散戶聲量：無法量化（DATA_UNAVAILABLE）。定性上，搜尋結果中的社群與新聞討論密度屬中等偏高，但缺乏與歷史基準的比較。

Retail 主要主題：
1. ABF 載板供需缺口與價格上漲（AI 伺服器、ASIC、800G 交換器需求）。
2. 母公司南亞的大股東持股動向（2026-06 報導提及南亞處分部分南電股權）。
3. 股價高檔與追高風險，以及外資買賣方向。
4. 獲利是否達到法人預期（2024 年舊文偏保守，較新摘要為正向）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。
- yfinance `insider`：回傳空陣列。
- 公開搜尋：未找到 2026 年董監事持股申報或增減持紀錄。鉅亨網董監持股頁面資料停留在 2023-08。
- 母公司層級：南亞為大股東，2026-06 有減持報導。這屬於大股東股權變動，不應與董監個人交易混為一談。
- 建議查證：公開資訊觀測站（mops.twse.com.tw）之「董監事持股餘額明細資訊」與「內部人持股異動」公告。
- 參考人名（非交易資料）：董事長鄒明仁，總經理呂連瑞。

## Ownership shifts

yfinance `major_holders`（時點未標示）：
- insidersPercentHeld：61.36%（高度集中，符合母公司南亞與台塑集團持股結構）
- institutionsPercentHeld：13.95%
- institutionsFloatPercentHeld：36.11%
- institutionsCount：129

yfinance `inst_holders`：回傳空陣列，因此無機構持股季度變化。機構持股趨勢：DATA_UNAVAILABLE。

注意：insidersPercentHeld 高達 61%，代表自由流通股比例低，股價對籌碼變動可能比一般個股更敏感。

## Net sentiment score

Composite：**偏多（bullish），信心中低（medium-low）**

- 分析師面：偏多，信心高。13/14 買進，目標價普遍高於摘要股價，僅 UBS 為中性。
- 散戶面：中性偏觀望。社群討論不一致，多數人認同 ABF 題材但警示追高風險。信心低，因為 Reddit、StockTwits 無資料，且 CMoney 為代理來源。
- 內部人面：無資料（DATA_UNAVAILABLE），不納入評分。
- 價格資料限制：搜尋摘要股價差異大（408.5、874、1,045、1,150、1,215、1,460 元等），無法確認 2026-10-08 收盤。這使「目標價高於股價」的判斷只能視為方向性參考。

Divergence flag: **yes（溫和分歧）**。分析師傾向偏多，散戶討論偏觀望、警示高檔風險。這是「機構偏多、散戶保守」型分歧，歷史上常見，但本次因社群樣本不足，分歧強度只能列為低到中。

資料缺口清單：
- Reddit / StockTwits：DATA_UNAVAILABLE
- 內部人交易（6 個月）：DATA_UNAVAILABLE
- 機構持股季度變化：DATA_UNAVAILABLE
- 散戶提及量（絕對數）：DATA_UNAVAILABLE
- 2026-10-08 即時股價：未確認（搜尋摘要時點不一致）

SENTIMENT REPORT COMPLETE
