# Sentiment — QUBT as of 2026-11-10

> 資料限制：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 本次皆無法取得（Reddit 抓取被拒、StockTwits 網域無法解析），散戶情緒部分缺資料，僅能以 X/新聞搜尋的零星結果補充。資料截止於工具可取得的最新日期（約 2026-11-09）。

## Analyst consensus
目前 4 buy / 2 hold / 0 sell（strongBuy 與 strongSell 皆為 0）。近 4 個月（0m 至 -3m）分佈完全相同，代表工具回傳的可能是停滯的彙總值，而非逐月變動。
- 近期升降評等：工具未提供個別 upgrade/downgrade 紀錄，無法確認近期評等變動。
- 目標價變動：工具未提供目標價資料，無法評估。
- 網路搜尋的聚合站另報「67% 買進、3 位分析師」，與 yf 的 4 買 / 2 持有 樣本數不一致，以 yf 數字為準，兩者不可混用。

## Retail social
- Reddit：本次無法取得 r/wallstreetbets 與 r/stocks 的 QUBT 討論串，無法計算提及量或多空比例。
- StockTwits / X：StockTwits 無法連線（網域未開放）。X/新聞搜尋結果多為 2025 年 11 月的舊聞（當月跌約 30%，歸因於 AI 泡沫疑慮）與 2026 年 8 月的零散報導，沒有可靠的 2026 年 11 月散戶情緒紀錄。
- 聲量：無法量化，以定性判斷屬「資料不足」，不能推論為低聲量。
- 散戶傾向：無法判定（不偽造多空比例）。
- 主要主題（僅依新聞標題歸納，非散戶原文）：量子運算概念股的題材炒作與高波動、營收規模極小（季營收低於 100 萬美元）使股價易受大盤 AI 與高風險科技情緒牽動。
- 財報事件：一則財報行事曆來源列出下一次財報為 2026-11-09 盤後，但未能驗證實際結果，本報告不含該次財報的市場反應。

## Insider activity
統計區間：2026-05-10 至 2026-11-10（近 6 個月）。金額單位：USD M。

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-20 | HUANG YUPING | CEO | 股票獎勵 / 衍生性證券轉換 | 584,897 (多筆) | 約 4.8–5.2（各筆列示金額不一致，疑為重複或不同價格的獎勵紀錄） |
| 2026-05-28 | HUANG YUPING、DIANAT POUYA、BEGLIARBEKOV MILAN | CEO / Officer / COO | 股票獎勵（價格 0） | 58,558 / 24,774 / 24,774 | 0 |

- 公開市場買入（open market buy）：0 筆，USD 0 M。
- 公開市場賣出（open market sale）：0 筆，USD 0 M。
- 淨額：約 USD 0 M（獎勵與轉換不計入買賣）。
- 注意：區間外（2026-03-10 至 2026-03-11）法務長 ROBERTS CHRISTOPHER BRUCE（General Counsel）曾轉換 40 萬股並賣出 78,262 股（約 USD 0.61 M）；2025 年 9 月 CEO 與董事曾有大額賣出，屬較早期資料。
- 解讀：6 個月內無公開市場買賣，內部人士傾向「不動」，屬中性訊號；沒有內部人士加碼買入的正向證據。

## Ownership
- 內部人持股：12.16%
- 機構持股：48.64%（占流通股 55.37%）
- 機構家數：425
- 工具只提供單一時點快照，無法判斷機構集中度的趨勢（增持或減持）。

## Net sentiment score
- 分析師：偏多（4 買 / 2 持有 / 0 賣，無賣方評等）。
- 內部人：中性（6 個月無公開市場交易，僅有獎勵性質的股權發放）。
- 散戶：無法判定（Reddit 與 StockTwits 皆無資料）。
- 綜合：**中性偏多，信心低**。主要依據為分析師評等結構，但評等在多個月份完全不變，且缺乏目標價與評等變動資料，加上散戶端完全缺席，綜合分數的可靠度有限。

Divergence flag: **無法判定**。因散戶情緒資料缺失，無法檢驗散戶與分析師是否背離。若日後補足 Reddit 或 StockTwits 資料，應再評估此項。

## 資料來源與缺口
- yf recommendations / rec_summary / insider / major_holders：成功（yf 的 cookie/crumb 取得失敗，但資料有回傳）。
- Reddit（r/wallstreetbets、r/stocks）：抓取被拒，未取得。
- StockTwits：網域無法解析，未取得（需於工作階段網路設定中開放 api.stocktwits.com 才能重試）。
- X / 新聞搜尋：部分成功，多為舊聞，時效性不足。

SENTIMENT REPORT COMPLETE
