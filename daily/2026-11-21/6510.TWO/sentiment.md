# Sentiment — 6510.TWO (中華精測) as of 2026-11-21

資料說明：本報告以 2026-11-21 為基準日。Reddit 與 StockTwits 無法取得（見下方），PTT / Dcard 無有效結果。凡標示 DATA_UNAVAILABLE 者皆為查無資料，未以推論補足。

## Analyst consensus

截至 yf rec_summary（期間 0m）：10 家券商，其中 strongBuy 4 / buy 6 / hold 0 / sell 0 / strongSell 0，即 10 buy / 0 hold / 0 sell。

近期變化：
- 0m 與 -1m 皆為 10 家（4 strongBuy + 6 buy）。
- -2m 與 -3m 為 9 家（4 strongBuy + 5 buy）。
- 過去約兩個月多出 1 家買進評等。因 hold 與 sell 在所有期間皆為 0，這一筆更像是新增覆蓋或新增買進評等，而非由 hold 升級，此為推論。
- yf recommendations 回傳內容與 rec_summary 完全相同，只有彙總數字，沒有個別券商的升降評等紀錄。因此無法確認具體 upgrade / downgrade 事件。
- 目標價與目標價變動：DATA_UNAVAILABLE（工具輸出未提供）。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 回報無法連線 www.reddit.com，無法取得貼文樣本或情緒傾向。
- StockTwits：DATA_UNAVAILABLE。api.stocktwits.com 無法解析（DNS 失敗），疑為本次工作階段的網路白名單未開放。在使用者確認允許此網域之前，不重試。
- PTT / Dcard / X：WebSearch 未找到 2026-11 月的股板或社群討論串，搜尋結果幾乎全為新聞與公司公告。因此無法判定散戶論壇的多空傾向，也無法引用網友原文。
- 聲量（buzz volume）：DATA_UNAVAILABLE 為量化數字。定性來看，媒體報導量在 2026 年 Q3 財報、擴產與股東會前後明顯偏多，但這是新聞流量，不等於散戶聲量。
- 主要題材（取自新聞，非社群）：
  - 2026 年 Q3 營收 19.1 億元，年增 53.4%，每股純益 16.75 元，創歷史新高（來源：優分析報導，2026-10-28）。
  - 產能超載，首階段擴產接近完成，預計 8 月底產能較 2025 年底倍增；第三座新廠於 2026 年上半年動土，預計 2028 年完工。
  - 2026 年資本支出由 3.5 億元上修至 5 億元。
  - 新產品老化測試板初期毛利率偏低，財務長表示下半年毛利率可回到 50～55% 長期目標區間。
  - 2025 年股利 15.3 元，配發率 50%。
- 股價參考（新聞引述，非即時報價）：nStock 資料顯示股價約 3,320 元，近一年均價約 2,918.5 元；4 月曾觸及 4,475 元新高後回檔，近期在 3,060～3,575 元區間盤整。這些數字來自不同時點的報導，未能確認與 2026-11-21 收盤一致，只作背景參考。
- 引述：本次無可引用的散戶原文。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。yf insider 回傳空陣列。空陣列不代表沒有內部人交易，可能是資料來源缺漏，因此不能當成零交易。
- 台灣董監事持股異動需以 MOPS（公開資訊觀測站）申報為準，本次未查詢。
- Notable：DATA_UNAVAILABLE。

## Ownership shifts

yf major_holders（當期快照）：
- 內部人持股 36.82%
- 機構持股 27.69%（占流通股約 43.83%）
- 機構家數 74

yf inst_holders 回傳空陣列，無法看到前後期機構持股變化，因此「集中度趨勢」只能判定為 DATA_UNAVAILABLE。內部人持股比例高，流通股相對有限，這一點在解讀股價波動時值得留意，但本次沒有時序資料可判斷是增持還是減持。

## Net sentiment score

Composite：**偏多（bullish），信心度中低**。
- 分析師面：偏多且一致。10 家全數買進，0 家持有或賣出，近兩個月略增。權重高。
- 散戶面：無資料，無法納入評分。
- 內部人面：無資料，無法納入評分。
- 新聞基本面：Q3 創高、擴產與股利延續，語氣偏正面，但這屬於基本面資訊，不等於情緒指標。
- 信心度受限於社群與內部人資料全部缺漏，只能以分析師一致性與新聞語氣作判斷。

Divergence flag：**無法判定**。散戶傾向資料不足，無法確認是否與分析師傾向相反。

SENTIMENT REPORT COMPLETE
