# Sentiment — ALAB as of 2026-10-18

資料說明：yf 快取更新時間為 2026-10-17 10:32 UTC，價格與分析師數據以 2026-10-17 為準，非 10-18 收盤。Live Yahoo 無法連線，全部 yf 數據取自快取（`prices/yf/ALAB.json`）。Reddit、StockTwits、X 的 10 月即時討論無法取得，相關欄位標示 DATA_UNAVAILABLE。

## Analyst consensus
rec_summary（0m）：Strong Buy 7 / Buy 11 / Hold 8 / Sell 0 / Strong Sell 0，共 26 家。
- 近三個月趨勢：-1m 為 7/12/7/0/0，-2m 為 7/12/7/0/0，-3m 為 7/11/8/0/0。評等分布穩定，沒有賣出評等，近一個月 Buy 合計由 19 微降為 18，Hold 由 7 升為 8，屬小幅降溫。
- 快取 info：recommendationMean 1.88（接近 Buy），recommendationKey 為 buy，分析師數為 22（與 rec_summary 的 26 家口徑不同，以上面 rec_summary 為準）。
- 目標價（快取 info）：平均 391.77、中位數 425.00、最高 500.00、最低 190.00。目前價 285.82，前收 301.98，較平均目標價低約 27%。
- 近期升降評：DATA_UNAVAILABLE。`recommendations` 欄位與 rec_summary 相同，沒有個別券商的升降評紀錄。Web 搜尋只找到 2026-02 Citigroup 將目標價由 275 降至 250 維持 Buy，以及同期的評等下調新聞，無法確認 10 月是否有變動。另有聚合網站寫 Sept 平均目標價約 348，與快取數字不一致，本報告以快取為準。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebSearch 找不到 2026-10 的相關討論串，直接 WebFetch 也被沙箱擋住，無法取樣熱門串文與語氣。
  - 唯一間接資料：24/7 Wall St 頁面顯示 Reddit 社群情緒中性，53 分，活躍度 21/100（低）。該頁面沒有日期，可信度低。
- StockTwits：DATA_UNAVAILABLE。搜尋無結果，API 無法在此環境取得。
- X：DATA_UNAVAILABLE。搜尋只找到新聞轉貼與自動生成的聚合頁，沒有可辨識的 10 月散戶貼文。
- 聲量（buzz volume）：DATA_UNAVAILABLE，無法與平常水準比較。
- 間接情緒指標（非即時，僅供參考）：
  - AltIndex 綜合情緒分 76/100（偏多），8 月為 88，7 月為 70，但近期較 30 日均值走弱。該分數由論壇與社群文字的 NLP 彙整，最新資料約為 8 月至 9 月中旬。
  - Benzinga 9 月中旬 put/call ratio 約 1.12（偏空），放空比率（short float）約 6.8%，快取為 6.94%，兩者大致一致。7 月 put/call 約 0.37 偏多，顯示選擇權情緒在 7 月至 9 月之間轉向保守。
- 主要主題（來自新聞與聚合網站，非直接的散戶貼文）：
  - 估值：有空方文章指出股價約為前瞻營收 40 倍（2026-06 文章）。
  - 內部人大量賣出：CEO、總裁、董事多次在高價區出脫。
  - 股價由高點 499.48 回落，現價 285.82，跌幅約 43%。
  - 一般看法是 AI 基礎設施連接題材仍被看好，但估值與賣壓是主要爭議。

## Insider activity
統計區間：2026-04-18 至 2026-10-18（6 個月）。
- 公開市場買進（Purchase）：$0。快取中沒有任何 open-market 買進紀錄。
- 公開市場賣出（Sale）：約 $627.96M。另有 Stock Award 與 Stock Gift 等非現金交易，未計入金額。
- 依人員彙總的賣出金額：
  - CEO Jitendra Mohan：約 $169.5M（2026-04-20 約 $57.9M、05-07 約 $28.0M、05-18 約 $21.5M、05-19 約 $31.3M、08-17 約 $30.8M）
  - 總裁 Sanjay Gajendra：約 $292.0M（05-07、05-18、05-19、05-21 合計約 $252M，08-17 約 $30.8M）
  - 董事 Manuel Alba：約 $132.5M（07-01 約 $81.2M，09-01 單筆 183,000 股、約 $51.3M）
  - 董事 Stefan Dyckerhoff：約 $24.4M，多次定期賣出約 12,499 股，屬規律性質
  - 其他（Lazar、Mayer、General Counsel Philip Mazzara 等）：合計約 $9.6M
- 值得注意的交易：
  - 2026-09-01，董事 Manuel Alba 賣出 183,000 股，價格區間 277.32 至 288.95。聚合網站稱為 10b5-1 計畫，未經原始 Form 4 確認。
  - 2026-08-17，CEO 與總裁各賣出 90,630 股，價格區間 333.60 至 352.11。
  - 2026-05-21，總裁賣出 400,000 股，價格約 289.13 至 293.03。
- 非市場交易：2026-10-01 董事 Barratt 與 Hurlston 各獲 68 與 72 股的 Stock Award（約 $21K 與 $22K，價格 311.57）。這類授予與 CEO 等人的大量賣出不同性質，不應視為看多訊號。
- 判讀：6 個月內內部人淨賣出，且沒有任何公開市場買進。這是本次資料中最明確的偏空訊號。

## Ownership shifts
資料日期為 2026-06-30（Q2 13F），距今約 3.5 個月，屬延遲資料。
- 機構持股：75.69%（快取），institutionsFloatPercentHeld 84.40%，機構數 1,334 家。內部人持股 10.32%。
- 前十大機構（pctChange 為比率）：
  - FMR LLC：14.32%，24.85M 股，季減約 2.7%
  - BlackRock：7.89%，季增約 19.5%
  - Vanguard Portfolio Management：4.55%，季增約 7.9%
  - Vanguard Capital Management：3.88%，季增約 6.1%
  - Invesco：2.83%，季增幅數值為 12.27（比率，約 +1,227%，疑為新建倉或數據異常，需核對 13F 原始資料）
  - State Street：2.12%，季增約 10.3%
  - Geode：1.61%，季增約 11.5%
  - T. Rowe Price：1.39%，季增幅數值 2.90（約 +290%）
  - Van Eck：1.29%，季增約 20.0%
  - Bank of America：1.27%，季增約 22.9%
- 趨勢：最大持股者 FMR 在減碼，被動型與部分主動型基金加碼。整體機構持股集中度高，但不是單一大股東主導。

## Net sentiment score
- 分析師：中性偏多（18 Buy 含 Strong Buy、8 Hold、0 Sell，平均 1.88）。信心：中。
- 內部人：偏空（6 個月淨賣出約 $628M，零公開買進）。信心：高，資料為快取的 Form 4 彙整，與 CEO、總裁的交易紀錄一致。
- 散戶：無法判定（DATA_UNAVAILABLE）。間接指標（AltIndex 76、put/call 1.12）分歧，且多數來自 8 月至 9 月，信心低。
- 綜合：中性（偏保守）。分析師多數仍 Buy，但目標價平均高於現價約 27%，內部人在高價區大量賣出，兩者互相拉扯。信心：中低。

Divergence flag：是。分析師評等偏多，內部人交易偏空，兩者方向相反。散戶與分析師是否相反無法判定，因為缺少 10 月的散戶資料。

## 資料缺口與待確認項目
1. Reddit、StockTwits、X 的 2026-10 即時討論與聲量：DATA_UNAVAILABLE。
2. 個別券商 10 月評等與目標價調整：DATA_UNAVAILABLE。
3. Insider 10b5-1 標記需由 SEC Form 4 確認：未確認。
4. Invesco 13F 增幅數值需核對：未確認。
5. 工具子命令與任務描述不符：yf.py 沒有 `ratings` 與 `holders`，實際使用 `rec_summary`、`recommendations`、`insider`、`major_holders`、`inst_holders`。

SENTIMENT REPORT COMPLETE
