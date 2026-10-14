# Sentiment — 005930.KS (三星電子 Samsung Electronics) as of 2026-10-14

## Analyst consensus
共 36 位分析師覆蓋：35 buy（strongBuy 11 + buy 24）/ 1 hold / 0 sell，買進比例約 97%。
- 近 3 個月分布幾乎不變（-3m 為 36 家中 35 buy / 1 hold；本期 0m 同為 35 buy / 1 hold），僅在 -2m 出現 1 家由 buy 改為 strongBuy 以外的 buy 計數變動，屬小幅波動。
- 近期調整（來源為韓文新聞，非 yf 工具輸出）：2026 年 8 月前後，未來資產證券目標價由 55 萬韓元降至 37 萬，키움 由 39 萬降至 35 萬，신한투자 由 59 萬降至 45 萬，삼성증권 由 50 萬降至 40 萬；KB 證券維持買進與 60 萬目標價。
- 另一篇英文彙整指出 Mirae Asset 於 9 月將目標價上調至 40 萬韓元，Hanwha 維持 Buy、目標 58 萬，IBK 目標 46 萬。Mirae 的方向與韓文來源相反，兩者互相矛盾，需以原始研究報告核對。
- 最新一份研究報告（基準日 2026-10-12，來源為韓文）：投資意見「買進（分批買進，下跌加碼）」，12 個月目標價 54 萬韓元。
- yf 工具未回傳目標價（price target）欄位，無法以工具數據計算目標價中位數。

## Retail social
- Reddit（r/stocks、r/wallstreetbets）：WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com"，本次無法取得貼文樣本，**資料缺口**。
- StockTwits：DNS 解析失敗（api.stocktwits.com ENOTFOUND），**資料缺口**。
- X / 新聞輿情（WebSearch 替代）：找不到可辨識的散戶貼文或社群討論。英文搜尋結果以新聞與分析師觀點為主，未見散戶論壇討論。
- 散戶聲量：無法量化（Reddit 與 StockTwits 皆無資料），僅能定性判斷為「無可見的大量討論訊號」。
- 散戶傾向：無法判定。
- 主要主題（來自新聞，非散戶貼文）：
  1. 第三季獲利預期：彙整共識營業利益約 106.1 兆韓元（約為去年同期 9 倍），IBK 估計 101.7 兆。但另一韓文來源引用 3Q26 營業利益 12.17 兆韓元，數字與英文共識相差近 9 倍，且 12.17 兆與 2025 年同期水準接近，疑為日期或數據混用，本報告不採信該數字。
  2. HBM 定價與市佔：KB 證券預估 2027 年 HBM 價格上升逾 100%；TrendForce 預估 HBM 平均售價年增 121%。一份報告指 HBM 市佔自 2026 Q1 的 21% 升至 Q2 的 33%（單一來源，待核對）。
  3. 股價與資金面：股價自 2026-01-11 高點大幅回落（英文報導稱約 21%），外資 20 日累計淨賣超約 6.49 兆韓元、60 日累計約 6.89 兆韓元（基準 2026-10-12）。
  4. 估值與利多兌現：有觀點認為獲利預期已大幅反映於股價，且 ETF 再平衡可能於財報前後帶來額外賣壓。

## Insider activity
Net 6mo: 無資料。yf `insider` 回傳空陣列 []，無法計算 6 個月淨買賣金額，亦無法確認 CEO / CFO / 其他人員的交易。
- 本次未額外搜尋韓國金融監督院（DART / 전자공시）的高管持股變動申報，屬**資料缺口**，不應推論為「無內部人交易」。
- 注意：三星電子為韓國上市公司，內部人申報以 DART 為準，yf 的覆蓋可能不完整。

## Ownership shifts
- 內部人持股比例：9.69%
- 機構持股比例：46.51%（流通股口徑 51.50%）
- 機構家數：749
- yf 僅提供單一時點快照，無歷史序列，**無法判斷機構集中度趨勢**（增持或減持）。
- 外資淨賣超（見上節）可作為間接代理指標，但它是交易流而非持股變化，不能直接等同於持股集中度下降。

## Net sentiment score
Composite: **neutral（信心：低）**

分項判斷：
- 分析師面：偏多（bullish），買進比例約 97%，但近期目標價下修與分歧並存。
- 散戶面：無法判定（Reddit / StockTwits 皆不可用）。
- 資金面（外資）：偏空（bearish），20 日與 60 日均為大額淨賣超。
- 基本面新聞：分歧，獲利與 HBM 定價正面，但獲利預期可能已反映於股價，且總經與地緣風險未消。
- 內部人面：無資料。

信心偏低的原因：散戶來源全部失效、內部人資料為空、新聞來源品質不一且多項數字互相矛盾（Q3 營業利益、Mirae 目標價方向、股價基準）。綜合判斷建立在分析師評等與外資資金流上，不應視為完整輿情評估。

Divergence flag: **yes（以代理指標判斷，信心低）**。sell-side 分析師高度偏多（買進約 97%），但外資持續大額淨賣超，兩者方向相反。散戶面無資料，無法確認散戶是否與分析師相反。此分歧可能有資訊價值，但也可能反映外資偏好與國內法人偏好不同，需結合價格與基本面進一步檢驗。

## 資料品質與缺口
- Reddit：403 / 無法存取，已略過。
- StockTwits：DNS 失敗，已略過。
- yf：Cookie / crumb 取得失敗（ConnectionError），仍回傳數據；insider 為空、無目標價欄位。
- 新聞來源：部分為 AI 生成摘要或低品質彙整站，部分報導日期與內容不一致（例如以 7 月報導描述 10 月初的連續下跌）。
- 股價基準互相矛盾：韓文研究報告引用 26.2 萬韓元（2026-10-12），TradingView 頁面顯示 18.12 萬韓元（無時間戳，未驗證）。本報告不以任何單一股價作為結論依據。

## 來源
- [Bloomberg 相關報導（經 WebSearch 彙整）](https://www.thewealthadvisor.com/article/samsung-has-lost-fifth-value-and-no-one-has-sell-rating)
- [Edaily 2026-08 報導](https://en.edaily.co.kr/news/eda202607035057)
- [TradersUnion 預測頁](https://tradersunion.com/currencies/forecast/005930-krw/)
- [sammyfans 2026-10-06 Q3 獲利預期](https://www.sammyfans.com/2026/10/06/samsung-q3-2026-profit-expected-to-hit-massive-usd-75-billion/amp/)
- [sammyfans 2026-10-01 HBM 價格](https://www.sammyfans.com/2026/10/01/samsung-hbm-prices-could-rise-over-100-next-year/amp/)
- [StockHub 新聞](https://stockhub.kr/en/news/news_540599d345fe)
- [Edaily 2026-09 Issues & Trends](https://en.edaily.co.kr/news/eda202609075210)
- [MTN 外資 VS 연기금 報導](https://news.mtn.co.kr/news-detail/2026081415453781393)
- [JKN 新聞](https://news.jkn.co.kr/post/963992)

## 指標表

| 指標 | 數值 | 備註 |
|---|---|---|
| 覆蓋分析師數 | 36 | yf rec_summary（0m） |
| Strong Buy / Buy | 11 / 24 | 買進合計 35 |
| Hold | 1 | |
| Sell / Strong Sell | 0 / 0 | |
| 買進比例 | 約 97% | 35 / 36 |
| 近 3 個月買進家數變化 | 35 → 35（持平） | yf recommendations |
| 目標價中位數 | 無資料 | yf 未回傳 |
| 6 個月內部人淨買賣 | 無資料 | yf insider 為空 |
| 內部人持股 | 9.69% | yf major_holders |
| 機構持股 | 46.51% | yf major_holders |
| 流通股機構持股 | 51.50% | yf major_holders |
| 機構家數 | 749 | yf major_holders |
| 機構持股趨勢 | 無資料 | 僅單一快照 |
| 外資 20 日淨買賣 | 約 -6.49 兆韓元（淨賣超） | 韓文來源，基準 2026-10-12 |
| 外資 60 日淨買賣 | 約 -6.89 兆韓元（淨賣超） | 同上 |
| Reddit 貼文樣本數 | 0（不可用） | WebFetch 無法存取 |
| StockTwits 訊息數 | 0（不可用） | DNS 失敗 |
| 散戶聲量 | 無法量化 | |
| 散戶傾向 | 無法判定 | |
| 綜合情緒 | 中性 | 信心：低 |
| 分歧旗標 | 是（代理指標） | sell-side 偏多 vs 外資淨賣 |

SENTIMENT REPORT COMPLETE
