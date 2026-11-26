# Sentiment — COHR as of 2026-11-26

注意: Reddit、StockTwits 無法取得，Yahoo 端點部分被 proxy 拒絕（yf 工具仍回傳分析師與內部人資料）。

## Analyst consensus

資料來源: `yf COHR rec_summary` / `recommendations`（分析師評等分布，共 27 家）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 本月 (0m) | 4 | 18 | 5 | 0 | 0 |
| -1m | 4 | 16 | 6 | 0 | 0 |
| -2m | 4 | 15 | 5 | 0 | 0 |
| -3m | 4 | 14 | 5 | 0 | 0 |

目前分布: 22 buy-side / 5 hold / 0 sell，無任何賣出評等。近三個月買進類由 18 增至 22，hold 由 6 降為 5，評等趨勢偏向上調。工具未回傳逐筆 upgrade/downgrade 明細，因此無法列出個別評等變動。

目標價變動（二手來源，日期部分不明，需以原始券商報告確認）:
- Citi: 目標價由 $420 上調至 $440，當日股價上漲約 13%。
- BofA: 財報後由 $400 下調至 $240（目標價下修）。
- Bernstein: 維持 Outperform，目標價 $350（2026-11-18 前後）。
- Benzinga 共識評等為 Buy。

## Retail social

- Reddit: 無法取得（r/wallstreetbets 與 r/stocks 搜尋皆被擋，工具回報 unable to fetch）。無貼文樣本可引用。
- StockTwits: 無法取得（api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許該網域）。一則二手摘要稱 2026-11 初 StockTwits 散戶情緒偏空，但未能驗證原始資料。
- X / 新聞: 本日 WebSearch 結果以新聞為主。一則 StockTwits 新聞標題為「COHR Stock Draws Upgrade As Marvell's $115B Lumentum Deal Highlights 'Value Of Scarce AI Optics'」，顯示市場敘事偏向 AI 光學稀缺性，但日期不明。
- 聲量: 無可靠計數，無法與平常水準比較（定性: 無法判斷）。
- 主要議題（來自新聞與摘要，非散戶貼文直接樣本）:
  - AI 光學 "from copper to optical" 的成長敘事
  - 估值: 二手文章稱 forward P/E 約 18x，低於五年均值 24x，且遠低於 6 月高點 57x
  - 現金流: 支出速度快於現金流入，市場關注下一季（預計 2 月初）營運現金流能否回正
  - 股價: 自 6 月高點回落逾 50%

## Insider activity

資料區間: 2026-05-26 至 2026-11-26（6 個月）。排除 Stock Award、Stock Gift、衍生性證券轉換（Conversion）等非市場交易。

- 買進合計: 約 $16.44M
  - 2026-11-20 Stephen G. Pagliuca（董事）: 82,000 股，約 $15.22M，價位 $183.70–190.05
  - 2026-11-09 James Robert Anderson（CEO）: 5,000 股，$997,400，價位 $199.48
  - 2026-11-10 Enrico DiGirolamo（董事）: 1,000 股，$222,885，價位 $222.88
- 賣出合計: 約 $8.49M
  - 2026-09-01 Julie Sheridan Eng（CTO）: 13,077 股，約 $3.58M，價位 $270.69–276.83
  - 2026-09-11 Enrico DiGirolamo（董事）: 5,315 股，約 $1.63M，價位 $305.98
  - 2026-08-18 Sherri R. Luther（CFO）: 3,000 股，$972,000，價位 $324.00
  - 2026-09-02 Lisa Neal-Graves（董事）: 2,200 股，約 $591K
  - 2026-08-31 Stephen A. Skaggs（董事）: 2,272 股，約 $629K
  - 2026-08-31 Enrico DiGirolamo（董事）: 2,272 股，約 $629K
  - 2026-07-22 Sherri R. Luther（CFO）: 1,000 股，約 $307K
  - 2026-09-09 Robert P. Beard（Officer）: 500 股，約 $155K
- 淨額: 約 +$7.95M（含 Pagliuca）；若排除 Pagliuca 則約 -$7.27M。

解讀: 11 月的買進集中在股價由高點大幅回落之後，且包括 CEO 與董事會成員，是本期最強的內部人正向訊號。買進金額主要來自單一董事 Pagliuca。6–9 月的賣出多在 $270–325 區間，屬較高價位了結，與 11 月的低點買進形成對比。

另一筆重要的持股變動: Bain Capital（10% 以上持有人）於 2025-11-07 賣出 7.5M 股，約 $1.08B，價位 $143.37（超出本期 6 個月區間，但屬大型籌碼出清）。

## Ownership shifts

- 內部人持股: 4.43%
- 機構持股: 88.16%（流通股比率 92.2%）
- 機構家數: 1,774
- 趨勢: 工具只回傳單一時點快照，無法判斷季度變化。Bain Capital 於 2025-11 大幅減持，屬已知的大股東結構變化。

## Net sentiment score

綜合: **偏多（bullish-leaning），信心中等**

- 分析師: 偏多，信心高。22 家買進類、0 家賣出，近三月上調趨勢，但 BofA 大幅下調目標價是重要反向訊號。
- 內部人: 偏多，信心中高。11 月 CEO 與董事大額買進；但 6–9 月高價區有明顯賣出。
- 散戶: 偏空（二手來源），信心低。無法直接取得 Reddit 與 StockTwits 資料，無法驗證。
- 主要風險: 估值與現金流、股價自高點回落超過 50%、大股東 Bain 過去的大量出清。

Divergence flag: **是（低信心）**。分析師與內部人偏多，若二手摘要正確，散戶偏空，兩者方向相反。散戶部分的證據不足，需在 StockTwits 或 Reddit 可用後重新確認。

## 資料限制與來源注意

- Reddit、StockTwits 無法取得；Yahoo 端點部分被 proxy 拒絕，但 yf 工具仍回傳資料。
- 新聞與目標價資料來自 WebSearch 摘要，部分日期不明或與其他來源不一致（例如 BofA 與 Citi 的日期），應以原始報告為準。
- Stockchase 報告 2026-11-23 收盤價 $215.65，但 Nasdaq/Fintel 的 $403.71 來源無日期，不反映目前價格。
- 近期 Motley Fool 與 StockAnalysis 評等頁面的條目為 2025 年，權重較低。

## 來源

- [Benzinga COHR sentiment](https://kr.benzinga.com/quote/COHR/sentiment)
- [Stockchase COHR](https://stockchase.com/COHR-Q)
- [TIKR: Bernstein holds $350 target](https://www.tikr.com/blog/bernstein-is-holding-its-350-coherent-target-with-the-stock-52-off-its-high)
- [TIKR: Citi lifts target to $440](https://www.tikr.com/blog/coherent-soars-13-as-citi-lifts-target-to-440-lumentum-up-3-in-ai-optics-rebound)
- [StockTwits: COHR upgrade headline](https://stocktwits.com/news-articles/markets/equity/cohr-stock-draws-upgrade-as-marvell-s-115-b-lumentum-deal-highlights-value-of-scarce-ai-optics/cNGaRcAR9Pg)

SENTIMENT REPORT COMPLETE
