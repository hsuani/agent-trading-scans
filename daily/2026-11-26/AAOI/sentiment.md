# Sentiment — AAOI as of 2026-11-26

資料來源：yf 工具（analyst、insider、holders）、WebSearch 新聞彙整。Reddit 與 StockTwits 無法取得。

## Analyst consensus

yf 資料（當月，Yahoo 分析師評級計數）：6 家，2 strong buy / 2 buy / 2 hold / 0 sell / 0 strong sell。
- 前一個月（-1m）：2 SB / 1 B / 3 H / 0 S。前兩個月（-2m）：2 SB / 1 B / 3 H / 0 S。
- 最近一個月的變化：1 家由 hold 轉為 buy（hold 3→2，buy 1→2）。
- 買方比例約 67%（4/6），無賣方評級。

網路新聞的計數不一致：Investing.com 摘要寫 5 家、3 buy / 3 hold / 0 sell，日期不明。以 yf 為準，但兩者須併同標註。

近期評級與目標價動向（多為 2026 年中以前資料，需留意日期）：
- B. Riley：2025-11 由 Sell（目標價 $15）下調，2026-02-27 升至 Neutral。
- Rosenblatt：2026-05 股價創高 $185.98（05-01）後，目標價升至 $220。另在更早時點因 $200M 收發器訂單，將目標價升至 $140。
- Raymond James 與 Northland：二者在近期股價大跌後分別提出上行空間看法（TIKR 彙整；日期與目標價未驗證）。
- 目標價共識不可靠：2026-02 快照平均目標 $38.08；後續快照為 $135.58。現價約 $37-50（來源不一），目標與現價落差極大，目前無法確認最新共識目標價。

## Retail social

- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 JSON 端點 WebFetch 皆回報無法連線，未取得樣本貼文，無法量化 mention 數量與 tilt。
- StockTwits：無法取得（api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許此網域後才能重試）。
- X / 新聞輿情（WebSearch，非散戶貼文，僅作參考）：
  - Simply Wall St 描述市場情緒「分歧」：90 日股價跌幅約 67.8%，但一年股東報酬仍約 +132%。
  - 大跌相關標題：「Applied Optoelectronics (AAOI) Dropped, So What Is Behind The Renewed Attention?」（Webull 轉載，內容未能驗證）。
  - 價格資料：2026-11-04 收盤 $59.27（AAII）；財報後一週跌約 20% 至 $50.13（網路報導）。
- Buzz 量：無法定量。無 Reddit / StockTwits 資料，無法與歷史基準比較。
- 主題（由新聞推論，非散戶原文）：
  - 800G / 1.6T 資料中心需求與大額收發器訂單，是多頭主要論點。
  - 股價自高點大幅回落、財報後下跌，是空頭與觀望主因。
  - 一則新聞提到「chipmaker 收購報價溢價」，內容與方向不明，未驗證，不列為依據。
- Retail tilt：無法判定（資料缺口）。

## Insider activity

6 個月（2026-05-26 至 2026-11-26，單位 USD M）：
- 賣出：$62.46M，共 22 筆。
- 買入：$0，0 筆（公開市場）。
- 另有 2 筆贈與（CEO 2026-05-28 贈與 85,790 股；董事 2026-09-15 贈與）與 6 筆 RSU / 獎勵授予，未計入買賣。

6 個月各人賣出金額（USD M）：
| 姓名 | 職位 | 賣出金額 | 備註 |
|---|---|---|---|
| CHANG HUNG-LUN FRED | Officer | 16.89 | 最大賣方，06-17 與 09-08 兩次大額 |
| DELANEY CYNTHIA | Director | 10.71 | 2026-05-26 約 56,575 股，@$189.23 |
| YEH SHU-HUA JOSHUA | Officer | 10.24 | 多次小額賣出，最近 10-05 @$120.03 |
| LIN CHIH-HSIANG THOMPSON | CEO | 9.83 | 2026-05-19 約 58,000 股，@$173.26 |
| MURRY STEFAN J | CFO | 8.28 | 每月約 4,000 股，持續至 11-10 @$48.83 |
| KUO DAVID C. | Officer | 4.87 | 06 月前後大額 |
| CHEN MIN-CHU MIKE | Director | 1.66 | 06-02 @$201 |

Notable：
- CEO Lin Chih-Hsiang Thompson：2026-05-19 賣出約 58,000 股，$10.05M，價位 $173.26。
- CFO Stefan Murry：固定 4,000 股的定期性賣出（如 09-10、10-12、11-10），可能屬預定交易計畫，yf 未標示 10b5-1，此為推論。
- 價位對照：2026-06 高點約 $166–$205 的大量賣出，至 11-10 已降至 $48.83。
- 近 12 個月合計：賣出 $125.8M，買入 $0。最後一次公開市場買入為 2025-08（CEO 與數名董事，約 $21–$23）。

Insider 持股：9.1%（yf major_holders）。

## Ownership shifts

- 機構持股 69.9%（占流通股 76.9%），機構數 635 家。
- yf 只提供快照，無歷史序列，無法判定集中度趨勢，此項標為資料不足。

## Net sentiment score

- 分析師（Analyst）：偏多（中度）。4/6 買方評級，無賣方；但目標價資料過時且互相矛盾，信心中等偏低。
- 內部人（Insider）：偏空。6 個月 $62.5M 賣出、零公開市場買入，且賣出涵蓋 CEO、CFO、董事，時間橫跨股價高點到大跌之後。
- 散戶（Retail）：無法判定。Reddit、StockTwits 均無資料。
- 綜合：中性偏空，信心低。主因是內部人高度淨賣出與散戶資料缺口並存。

Divergence flag：是（部分）。分析師偏多，與內部人淨賣出方向相反，此為值得注意的訊號。散戶 tilt 無資料，無法判定是否與分析師相反。

## 資料缺口與限制

- Reddit（WebFetch 無法連線）與 StockTwits（DNS 失敗）皆未取得。
- 網路新聞的價格與目標價有多筆互相矛盾或過時的數字（如 $31.32 為舊資料，$38 與 $135 目標價平均值差距大）。本報告未採用這些數字作為結論依據。
- 內部人交易為 yf 資料，日期截至 2026-11-10。
- 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
