# Sentiment — 8021.TW (尖點) as of 2026-11-02

> 資料完整度低:Yahoo 端點(cookie/crumb)連線失敗,Reddit 與 StockTwits 無法取得(StockTwits 因網域無法解析)。本報告主要依據 WebSearch 結果,最新可確認的價格與新聞約落在 2026 年 8 月,與 DATE 相隔約三個月。

## Analyst consensus
yfinance `rec_summary` 回傳 0 buy / 0 hold / 0 sell,`recommendations` 為空。這是資料缺口,不代表無券商覆蓋,不能解讀為中性。

可確認的單一券商評等:工商時報(ctee.com.tw,2026-07-26)報導,一家法人在 6 月自結財報後維持「買進」,認為近期股價偏弱來自鎢粉等原物料回落,中長期成長趨勢不變。未找到目標價數字,也沒有近期調評紀錄。

## Retail social
- Reddit(wallstreetbets / stocks):工具呼叫遭拒,無資料。
- StockTwits:DNS 解析失敗,無資料(需在 session 網路設定中允許 api.stocktwits.com)。
- X / 新聞與論壇:搜尋未取得 PTT 內容。CMoney 股市社群的個別網友留言大致分為兩派,無法量化,僅供參考:
  - 多頭:看好上半年 EPS 優於前一季,以及 ABF 與高階面板需求帶動的成長。
  - 謹慎:提到融資散戶比重偏高、外資與主力可能賣出,並有人質疑主力是否仍在出貨。
- 聲量:無可靠的提及次數資料,無法判斷相對於平常的高低。
- 散戶傾向:混合偏多。依據僅為少量論壇與搜尋摘要,信心低。

Themes:
1. 鎢粉與原物料成本:現貨價自 2026 年 Q1 高點回落約 50%,市場擔心鑽針漲價動能放緩。
2. AI 伺服器帶動 PCB 製程升級,高階鑽針供需仍緊。
3. 營收動能:7 月營收 7.30 億 TWD,年增約 102.6%,連續五個月單月新高。
4. 估值與籌碼:本益比與股價淨值比偏高,融資與主力動向有爭議。

## Insider activity
yfinance `insider` 回傳空陣列,無法判斷 6 個月內的內部人買賣。台灣公司的董監持股變動通常需另行查詢公開資訊觀測站,本次未取得。

Net 6mo: 資料不足(無法計算 $X buys / $Y sells)。Notable: 無。

## Ownership shifts
yfinance `major_holders`(時點未標示):
- 內部人持股約 10.1%
- 機構持股約 20.7%(浮動股比例約 23.1%)
- 機構家數 29

僅有單一時點,無法判斷趨勢。另一來源的法人持股表停在 2025-09-23,已過時。

## Price context (for interpretation only)
- 2026-02 前後交易區間約 190–230 TWD。
- 2026-07-24 收 370.00 TWD(單日跌約 9%)。
- 2026-08-04 收 390.50 TWD(單日漲約 10%)。
- 11 月資料未找到,無法確認最新股價。

## Net sentiment score
Composite: **neutral**(信心:低)

依據:
- 分析師面:僅見一家買進評等,無法形成統計共識,不予計分。
- 散戶面:混合偏多,樣本少,無量化數據。
- 內部人與機構面:資料不足,無法判斷方向。

Divergence flag: **無法判定**。分析師端資料缺口,無法與散戶傾向比較。若日後取得完整 rec_summary,可再評估是否背離。

Data gaps to close before next run:
1. Yahoo cookie/crumb 連線恢復後重抓 rec_summary 與 insider。
2. 允許 api.stocktwits.com 與 reddit.com 的網路存取。
3. 補查台灣公開資訊觀測站的董監持股申報。
4. 補查 2026 年 9 月至 11 月的股價與券商目標價。

SENTIMENT REPORT COMPLETE
