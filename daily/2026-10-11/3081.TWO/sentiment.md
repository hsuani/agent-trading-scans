# Sentiment — 3081.TWO (聯亞) as of 2026-10-11

資料時效聲明：本次搜尋所得的 TW 社群與法人報導多落在 2026/01 至 2026/08，**未找到 2026/10 的新評等、目標價或社群討論**。以下結論應視為「截至 2026 年中的狀態」，並非當日即時情緒。

## Analyst consensus
yf rec_summary（0m）：1 Strong Buy / 7 Buy / 1 Hold / 1 Sell / 0 Strong Sell（共 10 家，偏多，買方佔 80%）。
- 趨勢：-3m 時為 1 SB / 5 B / 1 H / 1 S，買進家數於近 3 個月增加 2 家，其餘未變。
- 個別券商評等變動（upgrade/downgrade 明細）：DATA_UNAVAILABLE。yf `recommendations` 只回傳彙總分佈，與 rec_summary 相同，未提供逐家事件。
- 目標價變動：yf 未提供 target price 欄位，DATA_UNAVAILABLE。
- 網路補充（均為 2026 上半年）：
  - 3 月：某美系外資目標價由 1,081 元上調至 1,505 元，但評等由「加碼」降為「中立」，理由為評價已反映多數利多。
  - 4 月 23 日：日系外資目標價上調至 2,850 元，維持「中立」。
  - 4 月底：本土投顧維持「買進」，目標價 4,000 元（以 2027E EPS 100 倍計算）；另一家投顧目標價 3,500 元。
  - 1 月法說後：國內法人 EPS 預估 13–17 元不等，目標價最高 1,300 元；美系外資把 2026–2028E EPS 上修至 17.6 / 28.8 / 50.6 元。
- 注意：yf 的 10 家與本土/日系外資報導的覆蓋範圍可能不重疊，兩者目標價差距很大（1,300 至 4,000 元），無法直接合併計算。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：本次未抓取。任務指定 TW 散戶來源以 WebSearch 為主，Reddit 對該檔標的覆蓋度預期極低，標為 DATA_UNAVAILABLE。
- StockTwits：DATA_UNAVAILABLE（未嘗試，TW 上市股覆蓋度低）。
- PTT / Dcard：搜尋未找到可用的近期貼文。PTT 僅有 2021 年疫苗 EUA 事件的舊討論，當時因同名與聯亞藥（6562）混淆。Dcard 無結果。
- CMoney 股市社群（最主要可得來源，為 AI 摘要而非原文）：
  - 短線：近期股價下挫，論壇多聚焦下跌風險與出場壓力；同時有人指出低檔長紅 K 棒，視為反彈訊號；亦有人提醒 MACD 動能收斂。
  - 長線：偏樂觀，認為聯亞在 AI 產業鏈與光通訊、DWDM 長距傳輸需求中有長期利多。
  - 無可量化的提及數量，buzz 量相對一般水準：DATA_UNAVAILABLE。
- X / 新聞鏈：主要為法人報告轉載與財經新聞，未見明顯的散戶情緒性貼文。
- Themes（跨來源重複出現）：
  1. 矽光子（SiPh）、1.6T/3.2T 升級、潛在 CPO 產品
  2. 與 Sumitomo Electric 簽訂五年 InP 供給長約
  3. 月營收爆發（2026/06 4.21 億 年增 128%；2026/07 5.01 億 年增 176.5%，1–7 月累計年增約 121%）
  4. 股價高波動與評價已反映多數利多的疑慮
  5. 外資與投信買賣方向不一（2026/07/27 外資賣超 1,461 張，投信買超 465 張）
- 股價數據矛盾：MONEY LINK 顯示 2026/07/20 收盤約 1,425 元；另一篇 CMoney 快訊提到股價反彈至 387 元（日期不明）。兩者皆為舊資料且互相衝突，本報告不採用具體股價。

## Insider activity
Net 6mo: DATA_UNAVAILABLE。yf `insider` 回傳空陣列，無法判斷是「無交易」或「TW 內部人申報資料未覆蓋」。建議另查公開資訊觀測站之董監事持股異動申報。
- Notable: 無。
- 機構/持股結構（yf major_holders）：內部人持股 13.94%；機構持股 26.26%（佔流通股 30.52%）；機構家數 83。
- 機構集中度趨勢（時間序列）：DATA_UNAVAILABLE，yf 只提供當期快照，無法判斷增減。
- 三大法人：histock 顯示 2026/07/27 外資賣超、投信買超，方向不一致，屬於短期籌碼訊號，非趨勢。

## Net sentiment score
Composite: **偏多（信心：中低）**
- 法人面：偏多（10 家中 8 家買進以上，買方家數近 3 個月增加；但有美系外資「中立」降評、股價已反映利多的論點）。
- 散戶面：中性偏空（短線）、偏多（長線），情緒分歧，無量化數據。
- 籌碼面：外資與投信方向不一，無內部人交易資料，訊號不足。
- 基本面動能（營收）：強，但屬於 2026/07 以前的資料，當日數據未確認。
- 信心偏低的原因：社群來源樣本少且為 AI 摘要；法人目標價跨度過大；內部人資料缺失；資料時效停在約 2–3 個月前。

Divergence flag: **yes（低信心）**。散戶短線情緒偏空（出場壓力、下跌風險討論），與法人偏多方向相反。但因散戶樣本未取得原文、且資料時效偏舊，此訊號僅供參考，不宜據以下結論。

## Data gaps summary
| 項目 | 狀態 |
|---|---|
| rec_summary（當期分佈）| 已取得 |
| 逐家評等變動 / 目標價變動 | DATA_UNAVAILABLE |
| Insider 6 個月淨買賣 | DATA_UNAVAILABLE（yf 回傳空值） |
| 機構持股時間序列 | DATA_UNAVAILABLE（僅快照） |
| Reddit / StockTwits | DATA_UNAVAILABLE |
| PTT / Dcard 近期貼文 | DATA_UNAVAILABLE |
| 2026/10 當月社群與評等 | DATA_UNAVAILABLE |

Sources（WebSearch 結果參考）：
- histock.tw 3081 個股頁
- money.udn.com 外資喊多 聯亞及貿聯直奔漲停
- uanalyze.com.tw 美系外資看好矽光前景調高目標價 聯亞反彈登漲停
- ctee.com.tw 2026/03/26 目標價報導
- wantrich.chinatimes.com 2026/04/28 報導
- cmoney.tw 3081 討論區與快訊
- shop.nstock.tw 聯亞做什麼

SENTIMENT REPORT COMPLETE
