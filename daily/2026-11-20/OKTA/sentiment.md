# Sentiment — OKTA as of 2026-11-20

> 資料截至可取得的最新日期（約 2026-11-16 至 11-19）。

## Analyst consensus

44 家券商（最新一期）：34 buy（其中 strongBuy 9、buy 25）/ 10 hold / 0 sell。
- 趨勢（近 3 個月）：buy 由 35 降至 34，hold 由 9 升至 10，sell 維持 0。整體仍偏多，但有小幅往 hold 移動的跡象。
- 近期評等變動：次級新聞來源（AAII 轉載，引用至 2026-11-13）提到過去一個月有 1 家下調、1 家上調。此數字未經券商原始紀錄核對，屬二手資料。
- 目標價變動：工具未提供，本次未取得。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：本次無法取得。Reddit 端點回應 "unable to fetch"，old.reddit 亦被擋。無法估計提及量與多空傾向。
- StockTwits：api.stocktwits.com 無法解析（DNS 失敗）。需在工作階段網路設定放行此網域後才能重試，本次未再重試。
- X / 新聞鏈：僅有一次 WebSearch，結果以財經媒體與評等機構文章為主，並非散戶貼文。
  - 偏空的文章：Weiss Ratings 警示指出，股價跌約 5.9% 主要源於網安族群情緒轉弱而非公司公告，並提到 forward P/E 約 125 倍，假設未來數年利潤率大幅擴張。該文章未註明日期。
  - 偏多的文章：PandaForecast/TradingKey（2026-10-21）提到財報優於預期、財務穩健帶動情緒。同文也點出估值偏高與內部人賣出的疑慮。
  - 其他：Benzinga 快照顯示空單比例約 5.1%（float）、put/call 約 1.77，但日期較早，僅供參考。
- 散戶聲量：無法與基準比較，定性判斷資料不足。
- 主要主題（由新聞標題歸納，非散戶原文）：估值是否過高；網安板塊情緒；今年漲幅大（YTD 約 +107%）後的獲利了結；財報後的股價拉回。

## Insider activity

過去 6 個月（2026-05-20 至 2026-11-19）：公開市場買進 $0；公開市場賣出約 $45.8M（約 9 筆）。
- 主要賣方與金額（USD M）：
  - CEO Todd McKinnon：2026-07-08 約 $10.1M（68,936 股，$145.63–148.16）；2026-09-22 約 $9.4M（48,822 股，$189.04–197.79）。
  - CFO Brett Tighe：2026-06-08 約 $7.6M（65,000 股，$116.67–118.52）；2026-09-02 約 $12.9M（80,000 股，$158.51–167.09）。
  - President Eric Kelleher：2026-06-18 約 $0.5M；2026-09-11 約 $0.4M；2026-09-18 約 $1.2M。
  - Officer Larissa Schwartz：2026-06-02 約 $3.3M；2026-06-22 約 $0.3M。
  - Director Shellye Archambeau：2026-05-18 約 $0.2M（於窗口外），2026-06-17 有期權轉股紀錄約 $0.3M，性質為轉換而非市場賣出，未計入。
- 買進紀錄：唯一一筆公開市場買進為董事 David Schellhase，2026-04-16 約 $0.27M，已在窗口外。
- 排除項目：股票贈與（Stock Gift）與股票獎勵（Stock Award）不計入，因非市場買賣。
- 解讀：金額大且幾乎全為賣出，CEO 與 CFO 均有參與，訊號偏空。部分交易看似與歸屬後出售相符，但工具資料無法確認是否屬 10b5-1 計畫，不應直接推定為看壞。

## Ownership shifts

- 機構持股約 95.9%（float 口徑 96.4%），機構數 1,372 家。
- 內部人持股約 0.53%。
- 單次快照，無歷史序列，無法判斷集中度趨勢。

## Net sentiment score

- 分析師：偏多（77% buy，0% sell）。
- 內部人：偏空（6 個月淨賣約 $45.8M，無公開買進）。
- 散戶：未能評估（Reddit、StockTwits 皆失效；新聞鏈僅有估值與板塊疑慮）。
- 股價脈絡：近期約 $179（2026-11-16，AAII 轉載），YTD 約 +107%，部分賣出價落在 $150–198 區間。
- 綜合：中性（信心：低）。分析師面仍偏多，內部人持續大額賣出是主要的反向訊號，散戶端缺資料無法確認。

Divergence flag: 無法判定（散戶資料缺）。但分析師與內部人方向不一致：分析師多數 buy，內部人淨賣出超過 $45M，這一點值得後續追蹤。

## 資料來源狀態
- 成功：yf recommendations、rec_summary、insider、major_holders；WebSearch（新聞鏈）。
- 失敗：Reddit（www 與 old.reddit 皆被擋）；StockTwits（DNS 無法解析，需放行 api.stocktwits.com）。

SENTIMENT REPORT COMPLETE
