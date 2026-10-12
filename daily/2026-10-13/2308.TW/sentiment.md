# Sentiment — 2308.TW（台達電 Delta Electronics）as of 2026-10-13

資料時點說明：yfinance 分析師彙總未附日期，且 2026-10-13 當日的 Reddit、StockTwits、社群資料皆無法取得。以下結論以可取得的最近資料為準，不代表 10-13 當日的即時狀態。

## Analyst consensus
yf rec_summary（4 個期間回傳完全相同，疑似快取或未更新）：6 strongBuy / 15 buy / 1 hold / 0 sell / 0 strongSell，即 21 買進（含強買）、1 持有、0 賣出。
網路彙整來源（valueinvesting.io，日期不明）則列 27 家分析師、26 家買進或強買、1 家持有，兩者家數不一致，需以更新來源校正。

近期評等與目標價變動（依 WebSearch 摘要，日期以原報導為準）：
- 民營金控旗下投顧：目標價由 2300 元下修至 2200 元，維持「買進」（近期報告，9 月前後）。
- 日系外資：維持「買進」，目標價 2922 元（7 月報告，股價已自高點回檔約 39%）。
- 美系外資：4 月目標價上調至 2110 元，理由為 AI 電源 12kW 產品需求與 HVDC 出貨時程可能提前至 2027 上半年。
- 法人下修 2026、2027 年 EPS 預估，主要因 8 月營收月減 3.7%、18.3kW 電力機架產品問題與電源 IC 短缺造成出貨遞延。預期 Q4 營收季增約 15%，受惠 Vera Rubin 機架量產與首批 HVDC 出貨。
- 聚合目標價均值約 2751 元（valueinvesting.io，日期不明），目標區間約 2444 至 3181 元。

價格基準不一致：同一輪搜尋中，各來源股價從約 1550 元到 2455 元不等。9 月中旬報導提及收盤 1685 元（跌 1.46%）。無法確認 10-13 價位，目標價與現價的距離無法精確計算。

## Retail social
- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 WebFetch 皆被擋（無法連線），不計入判斷。
- StockTwits / X：StockTwits API 無法解析（DNS 失敗），本次無資料。X 無可用的 2308.TW 貼文摘要。
- PTT / Dcard：WebSearch 未回傳任何散戶論壇討論，無法評估。
- 中文財經媒體的討論量與語氣未能量化，僅見新聞報導，不足以代表散戶情緒。
- 討論量（相對常態）：無法判定。
- Themes（僅依媒體與分析師報導歸納，非散戶原文）：
  - AI 資料中心與液冷、HVDC 架構出貨時程
  - 短期供應瓶頸（電源 IC 短缺）與毛利率壓力
  - 估值偏高（trailing P/E 約 69.6、forward P/E 約 29.5，來源日期不一）
  - 下一次法說／財報預計 2026-10-29，屬於近期催化劑

## Insider activity
yf insider 回傳空清單。這可能代表過去 6 個月無內部人申報，也可能是台股資料覆蓋不足，本次無法區分。
Net 6mo：資料不足（DATA_UNAVAILABLE），不估算淨買賣金額。
Notable：無。

## Ownership shifts
yf major_holders：內部人持股約 25.9%，機構持股約 38.5%（占流通股約 52.0%），機構家數 551。
趨勢資料（時間序列）未取得，無法判斷集中度是增加或減少。

## Net sentiment score
Composite：偏多（信心：低）。
- 分析師面：偏多。21 買進、1 持有、0 賣出，多數外資維持買進，但有下修目標價與 EPS 的紀錄。
- 散戶面：無資料，無法評分。
- 內部人面：無資料。
- 整體依可取得的分析師資料推論為偏多，但因散戶與內部人資料皆缺，信心偏低。

Divergence flag：無法判定（散戶資料缺失，無法比較兩方是否反向）。
若日後取得散戶資料，需特別注意：分析師偏多、散戶偏空的組合通常值得進一步查證。

## 資料缺口與建議補強
1. yf recommendations 四期數值完全相同，需以其他來源確認是否為最新數字。
2. Reddit、StockTwits 在本環境無法連線，需改用代理或其他來源。
3. 台股內部人申報（公開資訊觀測站）未接入，建議補充。
4. 機構持股時間序列（如 wantgoo 大戶集中度）未取得。
5. 10-13 當日股價未取得，需先確認價格基準。

Metrics

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師買進（strongBuy + buy） | 21 | yf rec_summary，4 期相同，疑似快取 |
| 分析師持有（hold） | 1 | yf rec_summary |
| 分析師賣出（sell + strongSell） | 0 | yf rec_summary |
| 聚合分析師家數（網路來源） | 27（26 買進 / 1 持有） | valueinvesting.io，日期不明，與 yf 不一致 |
| 聚合目標價均值 | 約 2751 TWD | valueinvesting.io，日期不明 |
| 目標價區間 | 2444 至 3181 TWD | valueinvesting.io，日期不明 |
| 近期目標價調整 | 2300 → 2200 TWD（民營金控投顧，維持買進） | 媒體報導，約 9 月 |
| 內部人 6 個月淨買賣 | DATA_UNAVAILABLE | yf insider 回傳空清單 |
| 內部人持股比例 | 25.93% | yf major_holders |
| 機構持股比例 | 38.52%（流通股占比 52.00%） | yf major_holders |
| 機構家數 | 551 | yf major_holders |
| 機構持股趨勢 | DATA_UNAVAILABLE | 無時間序列 |
| Reddit 提及量 | DATA_UNAVAILABLE | WebFetch 被擋 |
| StockTwits 訊息數 | DATA_UNAVAILABLE | DNS 失敗 |
| 散戶多空傾向 | DATA_UNAVAILABLE | 無可用來源 |
| trailing P/E | 約 69.6 | Snowball Analytics，日期不明 |
| forward P/E | 約 29.5 | Snowball Analytics，日期不明 |
| 下次財報日 | 2026-10-29 | Simply Wall St，依來源 |
| 綜合情緒 | 偏多（信心低） | 僅依分析師資料推論 |
| 背離旗標 | 無法判定 | 散戶資料缺失 |

SENTIMENT REPORT COMPLETE
