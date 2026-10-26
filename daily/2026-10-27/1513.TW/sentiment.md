# Sentiment — 1513.TW 中興電 as of 2026-10-27

注意事項：
- 資料時效：今日實際日期為 2026-10-26，指定日期 2026-10-27 尚未到來。本報告所有資料皆停在 2026 年中至 9 月初，**無 10 月資料**，不能視為 10/27 當日情緒快照。
- 來源缺口：Reddit（r/wallstreetbets、r/stocks）回傳 "unable to fetch"，StockTwits 因 DNS 解析失敗 (ENOTFOUND) 無法取得。散戶社群面向為空白，只能以新聞與搜尋結果代替。
- yfinance 內部人交易（insider）回傳空陣列，無法計算 6 個月淨買賣。

## Analyst consensus
yfinance rec_summary（0m）：強力買進 1 / 買進 6 / 持有 1 / 賣出 0 / 強力賣出 0，即 **7 buy / 1 hold / 0 sell**（與 Investing.com 之 8 位分析師中 7 買 1 持有一致）。近 3 個月分布未變，僅 -3m 時持有降為 0、買進降為 5，屬樣本波動，非評等下調。

近期動向（來自新聞搜尋，非 yfinance 逐筆紀錄）：
- 2026-01：某投顧 Buy，目標價 219 元。
- 2026-04（法說會後）：元大、富邦、永豐喊買；台新強力買進，目標價 186 元，理由為股價僅約 2027 年 EPS 的 16 倍。元大估 2026/2027 EPS 分別 8.77 / 10.45 元。
- 2026-06：國內外法人同步買進，預估今年 EPS 上看 9.17 元，最新目標價最高 195 元。
- 花旗：Buy，目標價 200 元（資料標示 2025-09 納入，時效偏舊）。
- 負面紀錄：2025-10 有一家投顧由買進降為「增加持股」，目標價由 200 降至 176 元，理由是台電拉貨延後。
- 目標價彙總：Investing.com 12 個月平均 185.5 元。

## Retail social
- Reddit：無法取得（工具封鎖）。
- StockTwits：無法取得（DNS 失敗）。
- X / 新聞討論：中文搜尋僅找到財經媒體與平台頁面，未見散戶貼文。以下為媒體面而非散戶情緒：
  - 9 月初股價約 165 元，近一年均價約 159 元，殖利率約 3.5%（現金股利 6 元）。
  - 報導提醒重電股前波漲幅大，長單題材已部分反映在股價，短線易受題材與籌碼影響。
- buzz 量：無法量化。以媒體出現頻率判斷屬中等，且集中於法說、月營收與股利等事件。
- 散戶傾向：**無法判定**（資料不足）。

Themes（來自媒體，非散戶貼文）：
1. AI 資料中心供電與台電電網升級需求。
2. 在手訂單：2026 Q1 新接訂單 63 億元，在手訂單累計 431 億元（TWD），部分產品能見度延伸至 2031 年。
3. 台積電美國亞利桑那二期供應鏈訂單，預計 2026 Q3 簽約、2027 Q1 出貨（TWD 金額未獲確認）。
4. 月營收：2026 年 8 月 25.02 億元（TWD），年增 8.93%，為十年同期單月新高。
5. 估值與漲幅：前波大漲後的追價風險。

## Insider activity
Net 6mo：**無資料**（yfinance insider 空；台灣董監持股申報無法於搜尋取得，鉅亨網頁面僅有 2023 年資料）。
Notable：無可確認的近期董監買賣紀錄，不得推定為淨買或淨賣。
ownership 參考（yfinance major_holders）：內部人持股 19.9%，機構持股 13.8%（流通股中機構 17.2%），機構數 58 家。機構集中度的時間趨勢無法判定，僅有單一時點。

## Net sentiment score
Composite：**偏多（bullish），信心：低至中**。
- 分析師面：偏多，明確（7 買 / 1 持有 / 0 賣，目標價多落在 186–219 元，高於 9 月初約 165 元股價）。
- 散戶面：無資料。
- 內部人面：無資料。
- 媒體與新聞面：偏多，但集中於 AI 電網與訂單題材，且資料止於 9 月初。
- 信心下調理由：散戶與內部人兩個維度皆缺，且分析師資料最新僅到 2026 年 6 月。

Divergence flag：**無法判定**。散戶傾向缺失，無法與分析師傾向比對。若日後補上散戶資料，需特別留意 ETF／題材追漲式樂觀與分析師目標價之間的落差。

Data gaps to backfill: Reddit/StockTwits 恢復、MOPS 董監持股申報（內部人淨買賣）、2026-10 月營收公告與法說會後最新目標價。

## Sources
- [nownews 中興電相關報導](https://www.nownews.com/news/6762915)
- [nStock 中興電](https://www.nstock.tw/1513?status=6)
- [鉅亨網 董監持股頁](https://www.cnyes.com/twstock/directorholder.aspx?code=1513)
- [wantrich 2026-01 目標價報導](https://wantrich.chinatimes.com/news/20260121900307-420101)
- [wantrich 2026-04 報導](https://wantrich.chinatimes.com/news/20260424900726-420101)
- [今周刊 2026-06 報導（businesstoday tag）](https://www.businesstoday.com.tw/article/category/183008/post/202606220026/)
- [Investing.com 中興電](https://hk.investing.com/equities/chung-hsin)
- [MoneyLink 中興電 SymId=1513](https://ww2.money-link.com.tw/TWStock/StockBasic.aspx?SymId=1513)

SENTIMENT REPORT COMPLETE
