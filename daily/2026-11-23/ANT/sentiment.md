# Sentiment — ANT (Anthropic, PBC, Nasdaq NMS) as of 2026-11-23

資料狀態：yf 即時連線失敗，回退至 repo 快取 (prices/yf/ANT.json，refreshed 2026-11-22T14:30 UTC)。Reddit 無法連線 (WebFetch 拒絕)，StockTwits API 網域無法解析 (需於 session 網路設定允許 api.stocktwits.com)。散戶端僅能以 WebSearch 摘要替代，可信度低。

## Analyst consensus
快取 rec_summary：Strong Buy 2 / Buy 5 / Hold 2 / Sell 0 / Strong Sell 0 (共 9 家，recommendationKey = buy)。
目標價 (快取 info，USD)：mean 118.17 / high 155.00 / low 92.00；現價 88.91。
近期升降評等：yf recommendations 只提供彙總，沒有逐筆升降級紀錄，無法列出具體 upgrade/downgrade 日期。
外部摘要 (WebSearch，Benzinga 片段)：「Buy」共 3 家，平均目標價 137 USD；11/19 新覆蓋 Citizens 125 USD、Wolfe Research 135 USD。
**來源衝突**：快取顯示 9 家、平均目標 118.17 USD；Benzinga 片段顯示 3 家、平均 137 USD。兩者日期與計算口徑不同，未能調和，報告以快取數字為主、外部數字僅作參考。

## Retail social
- Reddit (r/wallstreetbets、r/stocks)：無法取得 (WebFetch 拒絕連線)，無貼文樣本與傾向數據。
- StockTwits：API 無法解析，無即時訊息量。WebSearch 摘要指出 11/11 盤前散戶情緒由「bearish」轉為「bullish」，討論量由「low」躍升至「extremely high」。此為單一摘要來源，時點與現況未經確認。
- X / 新聞：WebSearch 摘要提到 IPO 後股價走勢與估值爭議。Gate 報價 11/20 約 95.26 USD (單日 -7.8%)，IPO 定價 83 USD。估值論點：溢價是否能被持續高利潤率支撐；第三季營業損失相對第二季營業利益的轉折被視為風險。Finimize 亦提及可能於 12/11 前後納入 Russell 1000，可能帶來指數型買盤。
- 量能：無法與歷史基準比較，僅能定性判斷為「高於 IPO 前」，但缺乏 Reddit/StockTwits 實際計數。
- 主題：IPO 後估值 (溢價是否合理)、成長與獲利轉折 (Q2 營益 → Q3 營損)、指數納入預期、股價相對 IPO 價位的位置。

## Insider activity
yf insider 回傳空陣列 (快取亦無資料)，無法確認 6 個月內 Form 4 買賣金額。
快取 heldPercentInsiders = 22.2%，顯示內部人持股比例高，但這是持股結構，不是交易流向。
Net 6mo：無資料 (無法判定淨買或淨賣)。Notable：無可驗證的交易紀錄。

## Ownership shifts
yf major_holders：insidersPercentHeld 0.222；institutionsPercentHeld、institutionsCount 皆為 0，inst_holders 為空陣列。判定為資料缺漏 (新上市股票或 Yahoo 欄位不完整)，不能解讀為機構持股為零。機構集中度趨勢無法判斷。

## 市值與單位核對
快取 marketCap = 1,188.4 B USD。以 sharesOutstanding 7.730 B × 現價 88.91 反推約 687.3 B USD，兩者相差約 73%。可能原因：marketCap 採不同股本口徑 (如全稀釋) 或快取價格與市值時點不同。本報告不以市值作判斷依據，下游引用前需先核對。

## Net sentiment score
Composite：**偏多 (bullish)**，信心：**低**。
- 分析師端：9 家中 7 家為 Buy 以上，0 家 Sell，偏多信號較明確。
- 散戶端：僅有單一摘要顯示 11/11 轉多，缺乏 Reddit/StockTwits 實際樣本與近期資料，無法確認目前傾向。
- 內部人與機構端：資料缺漏，無法提供佐證。

Divergence flag：**否**。分析師與散戶 (依摘要) 方向一致偏多，但散戶面數據薄弱，一致性結論可信度有限。若後續補到 Reddit/StockTwits 近期樣本，需重新檢視此旗標。
注意：IPO 後股價 (約 88.9–95.3 USD) 低於分析師平均目標 (118 USD)，同時低於 52 週高點 115.1 USD，市場情緒與評等間存在價格落差，屬待觀察項目。

SENTIMENT REPORT COMPLETE
