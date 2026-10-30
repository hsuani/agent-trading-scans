# 情緒分析 — 6257.TW 矽格 (Sigurd Microelectronics) 截至 2026-10-31

## Executive summary

矽格目前可取得的情緒訊號很薄弱。分析師面只有一位覆蓋者 (rec_summary 顯示 1 strongBuy, 0 buy / 0 hold / 0 sell)，屬於單一券商意見，代表性不足。散戶面 (Reddit、StockTwits) 在本次執行中全部無法取得，搜尋引擎也找不到 2026 年 10 月的網友討論。內部人交易資料為空。唯一較具參考性的間接訊號是夏季股價大幅回檔 (HiStock 資料顯示 7 月約下跌 24%)，以及 2026 年 Q2 營運與獲利創歷史新高的新聞。綜合判斷為 **中性偏觀望，信心低**。這份報告不構成任何交易建議。

## Analyst consensus

資料來源: `pipeline/tools/yf 6257.TW rec_summary` 與 `recommendations`

- 最新 (0m): 1 strongBuy / 0 buy / 0 hold / 0 sell / 0 strongSell
- -1m、-2m 的計數與 0m 完全相同，代表評等在這段期間沒有變動，也可能只是資料快照未更新。
- 歷史評等變動 (recommendations) 沒有可辨識的升降評紀錄，只有同一位覆蓋者維持 strongBuy。
- 目標價: yf 工具未提供。Investing.com 搜尋摘要內的目標價數字彼此不一致 (一處為 TWD 328，另一處為 TWD 106)，無法確認，因此不採用。

結論: 分析師一致性為「單一覆蓋者偏多」。樣本數為 1，統計上不具備一致性意義。

## Retail social

- **Reddit (r/wallstreetbets、r/stocks):** DATA_UNAVAILABLE。WebFetch 回傳 "Claude Code is unable to fetch from www.reddit.com"，本次無法讀取貼文、分數與留言數。
- **StockTwits:** DATA_UNAVAILABLE。`api.stocktwits.com` 無法解析 (getaddrinfo ENOTFOUND)，該網域需在 session 網路設定中放行後才能重試。
- **X / 論壇 (WebSearch):** 中文與英文搜尋均未找到 2026 年 10 月的網友看法。搜尋結果主要是新聞與行情頁面，不是社群發文，因此不計入散戶情緒。
- **討論量 (buzz volume):** DATA_UNAVAILABLE，無法與平常水準比較。
- **主要主題 (可由間接來源推論):**
  - 基本面面向: 先進測試需求、AI 相關封測成長、湖口二廠產能被大客戶預訂、中興三廠提前至 2026 Q4 完工 (來源: 新聞摘要)。
  - 價格面面向: 夏季回檔與股價波動被關注 (HiStock 7 月資料)。
- **無法計算任何散戶多空百分比。** 本次沒有足以計算比例的貼文樣本。

## Insider activity

- `pipeline/tools/yf 6257.TW insider` 回傳空陣列 `[]`。DATA_UNAVAILABLE。
- 台股董監事與大股東持股變動主要透過公開資訊觀測站 (MOPS) 申報，Yahoo 來源對台股覆蓋不完整，因此空資料不代表沒有交易。
- 6 個月內 net 買賣金額: DATA_UNAVAILABLE。
- 資料點: yf major_holders 顯示內部人持股比例約 7.87%。這是持股水準，不是交易方向，不能用來推斷買賣傾向。

## Institutional and ownership

- 機構持股比例 (institutionsPercentHeld): 約 18.13%
- 機構持股占流通股比例 (institutionsFloatPercentHeld): 約 19.68%
- 機構數量 (institutionsCount): 78
- 趨勢: yf 只給單一時點快照，無法判斷集中度是增加還是減少。
- 間接訊號: HiStock 7 月資料提到外資持股略減 (單一來源，未經其他資料交叉驗證)。

## Price and fundamental context (供判讀情緒用，非本報告主要結論)

- 2026-09-17 快照股價 TWD 222.50，52 週區間 TWD 87.50 至 TWD 279.50 (來源: 搜尋摘要)。
- 10 月的股價與新聞: 未找到，無法判斷 10 月市場情緒。
- Q2 2026 單季營收約 59 億元 (搜尋摘要原文為 NT$5.9 十億，換算即 59 億)，來源為摘要，未經財報核對，摘要稱為單季新高。
- 單季 EPS 2.55 元，上半年累計 EPS 4.65 元，同樣為歷年同期新高 (來源: 8 月新聞摘要)。
- 2026 年資本支出追加至約 88 億元，用於先進測試產能。
- 以上財務數字均為搜尋摘要轉述，未經原始財報驗證。Q3 財報預計 2026 年 11 月初公布。

## Net sentiment score

- **綜合判斷:** 中性偏觀望 (neutral, leaning cautious)
- **信心:** 低。原因: 分析師樣本只有 1 位；散戶來源全數缺失；內部人資料缺失；10 月市況未取得。
- **基本面與情緒的關係:** 營運與獲利面的新聞偏正向，但夏季股價回檔與外資持股略減顯示市場資金的態度較為謹慎。兩者之間存在落差，無法確認是否為短期修正或長期轉向。
- **背離旗標 (divergence flag):** 無法判定。分析師面偏多，但散戶面資料缺失，無法比較兩者方向是否相反。

## Data gaps and follow-up

1. Reddit 與 StockTwits 需放行網路或改用其他可用來源後重試。
2. 目標價數據需從付費或可用的券商彙總來源取得，且要核對 Investing.com 摘要中的矛盾數字。
3. 台股內部人申報應以 MOPS 公開資料補抓。
4. 10 月股價與 Q3 財報公布後，應重跑本報告。

SENTIMENT REPORT COMPLETE
