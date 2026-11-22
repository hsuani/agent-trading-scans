# Sentiment — 2408.TW (南亞科) as of 2026-11-22

資料狀態：analyst 分布為 yf cache 快照（Yahoo cookie/crumb 連線失敗，屬預期 fallback）；insider 與 institutional holder 明細回傳空陣列，無法區分「無交易」與「資料缺漏」，標記 DATA_UNAVAILABLE；Reddit / StockTwits / PTT / Dcard 無可用資料。

## Analyst consensus

| 評級 | 目前 (0m) | -1m | -2m | -3m |
|------|-----------|-----|-----|-----|
| Strong Buy | 4 | 4 | 4 | 4 |
| Buy | 8 | 8 | 7 | 7 |
| Hold | 1 | 1 | 0 | 0 |
| Sell | 1 | 1 | 1 | 1 |
| Strong Sell | 0 | 0 | 0 | 0 |
| 合計 | 14 | 14 | 12 | 12 |

目前為 **12 buy / 1 hold / 1 sell**（含 Strong Buy 4 家）。近三個月偏多家數穩定微增（11 → 12），Hold 由 0 增至 1，Sell 維持 1 家。

近期調整與目標價：
- Macquarie 維持 Buy，目標價由 552.00 上調至 681.40（2026-10-08，來源為 Investing.com 彙整頁，屬二手紀錄）。
- 富邦維持買進、目標價 660 元，但認為未來四季營收與 EPS 已無大幅上修空間（新聞彙整）。
- 群益僅給區間操作建議，認為漲幅收斂、成本上升（新聞彙整），屬偏保守立場。
- 聚合平台平均目標價約 655–659 元（高 850 / 低 447），各頁快照日期不一致，僅供參考。
- 無法取得 2026-11 月內具體券商新報告，analyst 目標價數字可信度中等。

## Retail social

- Reddit：WebSearch 未回傳 r/wallstreetbets 或 r/stocks 相關串文，無法判斷 tilt。DATA_UNAVAILABLE。
- StockTwits / X：未取得可用串文。DATA_UNAVAILABLE。
- PTT / Dcard：搜尋未找到討論串。DATA_UNAVAILABLE。
- 媒體與法人觀點（非散戶）：10 月以來股價自高點回落，媒體標題多為「股價欲振乏力」「法人分歧」。一則報導稱股價從 537 元高點跌至約 414 元（波段跌幅約三成），但其他來源的收盤價互相矛盾（343.5、383、414、131.5），未能核對，需以 TWSE 為準。
- 緩和聲量估計：無 Reddit / StockTwits 數據，無法判斷聲量相對平常水準，只能以新聞量定性：財報與營收相關報導密集，屬高關注度。
- 主要題材（來自新聞與法人，非散戶原文）：
  - DRAM 缺貨與價格續漲（TrendForce 預估 4Q26 DRAM ASP 季增約 10%）
  - 陸廠長鑫存儲擴產可能提早結束漲價循環（股價重挫主因之一）
  - AI 產品營收占比超過兩成，目標 2029–2030 年提高至 40%–50%
  - 屏東新廠投資規模（約 100 億美元）與資本支出壓力
  - 2027 年上半年出貨可能持平，ASP 能否支撐獲利為主要疑慮
- 代表性觀點（新聞來源，不逐字引用散戶原文）：偏多方強調「陸廠產能占比有限、DDR4 供需缺口可能持續」；偏空方質疑「獲利高點是否已過」。

## Insider activity

Net 6mo：DATA_UNAVAILABLE（yf insider 回傳空陣列，無法確認是否真的無交易）。

替代訊號（機構層級，非董監個人）：
- 台塑、台化、台塑化（台塑集團關係企業）公告 2026-11-11 起進行第三波處分，合計擬出脫南亞科約 5.69 萬張，完成後合計套現約 96.52 億元。處分期間自 11/12 至 2027-01-30，並已提前完成（新聞來源，公告日期未明確）。
- 三家持股比重據報導由 9.4176% 降至 8.8053%。注意：此數字與 5.69 萬張處分量換算後不完全一致，未能完全核對。
- 上述為大股東處分，屬偏空的籌碼訊號，但與董監個人增減持不同，需分開看待。

## Ownership shifts

- yf major_holders（單一快照）：insiders 持股約 51.66%；institutions 持股約 16.0%（流通股中約 33.1%）；機構家數 241。
- 因 yahoo 將大股東（含台塑集團）計為 insiders，51.66% 的「內部人持股」不代表董監個人持股。
- 機構持股趨勢：DATA_UNAVAILABLE（僅有單一快照，無歷史比較；inst_holders 回傳空陣列）。

## Net sentiment score

- **Analyst 面：偏多（信心：中）。** 12 buy / 1 hold / 1 sell，目標價中位數高於近期成交價區間，但各來源價格與目標價日期不一致。
- **Retail 面：無法判定（信心：低）。** Reddit、StockTwits、PTT、Dcard 皆無可用資料。
- **籌碼 / 內部人面：偏空（信心：中）。** 大股東持續處分，insider 個人交易資料缺漏。
- **新聞基本面：偏多，股價偏弱。** 營收年增約 488%（10 月），但市場因長鑫擴產與高點疑慮分歧。
- **綜合：中性偏多（信心：中低）。** 分析師共識偏多，但股價走弱與大股東處分構成制衡，散戶面缺資料無法驗證。

Divergence flag：**無法判定（部分）**。analyst 偏多，而新聞與股價走勢偏弱；散戶 tilt 無資料，故無法確認是否與 analyst 相反。建議之後補抓 Reddit / StockTwits 或 PTT 資料，再重新評估。

## 資料來源與限制

- yf：`rec_summary` / `recommendations`（成功，cache）、`major_holders`（成功，cache）、`insider` / `inst_holders`（空陣列）
- WebSearch：新聞與法人彙整（TechNews、Statementdog、udn、Investing.com 等），多數為二手資料，價格與日期不一致
- 數字單位：營收與套現金額以 億 計，未混用 B。Q3 稅後淨利 876.3 億與報導的 EPS 25.40 元不一致（以約 24 億股推算 EPS 應約 36 元），此項未採用
- 本報告不構成交易建議

SENTIMENT REPORT COMPLETE
