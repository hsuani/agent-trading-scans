# Sentiment — VRT as of 2026-10-14

## 資料可得性摘要
- yf 結構化資料：rec_summary / recommendations / insider / inst_holders / major_holders 可取得（Yahoo cookie/crumb 失敗，使用快取/備援路徑，屬正常情況）。`ratings` 與 `holders` 不是 yf.py 的有效子命令，已改用 `rec_summary`、`major_holders`、`inst_holders`。
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（WebFetch 無法連線 www.reddit.com；WebSearch 找不到 2026 年相關討論串）。
- StockTwits：DATA_UNAVAILABLE（api.stocktwits.com DNS 解析失敗）。
- X / 新聞社群：WebSearch 僅找到財經新聞與報價頁，無法量化社群聲量。

## Analyst consensus
yf rec_summary（0m）：3 Strong Buy / 23 Buy / 4 Hold / 0 Sell / 0 Strong Sell，共 30 家。近三個月 Buy 家數 21 → 21 → 22 → 23，Hold 穩定在 4 家，無 Sell 評級。

近期評等變動（WebSearch 結果，日期與數字在不同來源間有出入，列為待驗證）：
- 2026-08-07：GLJ Research 由 Hold 升為 Buy，目標價 $381。
- 2026-07-30：KeyCorp 目標價由 $360 降至 $325（維持 Overweight）；Citigroup 目標價由 $414 降至 $358。
- 2026-07-30 前後：RBC Capital 維持 Outperform，目標價由 $435 降至 $418，另一來源顯示降至 $337，兩者衝突。
- 較早事件（不屬近期）：Wolfe Research 曾降為 Peer Perform，理由為估值已反映漲幅。

共識目標價：各來源差異大，MarketBeat 約 $357.83，Benzinga 約 $324，Investing.com 約 $338。2026-09-08 收盤約 $290.83，2026-09-18 約 $248.81（MarketBeat）。以上價格僅供參考，未能確認 2026-10-14 當日收盤價。

本次未找到 2026 年 9 月以後的評等變動。

## Retail social
- Reddit：DATA_UNAVAILABLE（r/wallstreetbets 與 r/stocks 無法抓取，搜尋亦無 2026 年相關討論）。
- StockTwits：DATA_UNAVAILABLE（DNS 失敗）。
- X / 新聞：未能量化聲量，無法與平時基準比較，標記 DATA_UNAVAILABLE。
- 可見的市場敘事（來自新聞而非散戶社群）：AI 資料中心的電力與冷卻需求是主要多頭論述；2026 年 2 月 Q4 財報後股價大漲，財測優於預期。Q4 調整後 EPS $1.36 vs 共識 $1.30，FY26 指引 $5.97–$6.07 vs 共識 $5.33（來源為 CNN 頁面摘要）。
- 下一個催化劑：Yahoo HK 頁面列出 2026-10-21 為財報日，時間來源不確定，需再確認。
- 散戶傾向：DATA_UNAVAILABLE，無法判斷多空，因此無法進行分析師與散戶分歧的比較。

## Insider activity
追溯期間：2026-04-14 至 2026-10-14（近 6 個月）。

- 公開市場買入：0 筆，淨買入 $0。
- 公開市場賣出：1 筆，為董事 Monser, Edward L. 於 2026-09-01 賣出 15,287 股，金額約 $3.88M（價格 $249.43–$256.36），同日以選擇權行使取得等量股份（行使價 $11.50）。
- 其他交易：
  - CEO Albertazzi, Giordano 於 2026-09-08 贈與 118,523 股（$0，非交易）。
  - 2026-10-05 Officer Resha, Michael 獲配股票 3,193 股（約 $0.81M，授予性質）。
  - 2026-06-25 多位高階主管與董事獲配少量 RSU 股份（每人 0–9 股，金額 $0，應屬股息等值或例行授予）。
- 6 個月窗口外、但與近期判斷相關：2026-03-06 Monser 賣出約 $18.97M，2026-02-27 Fradin 賣出約 $51.4M，2026-02-26 Karlborg、Reinemund、Cote、Van Dokkum 等合計賣出逾 $50M。窗口外交易不計入淨額，但顯示 2026 年上半年內部人持續減持。

結論：近 6 個月淨額為 $0 買入、約 $3.88M 賣出（僅一筆，且與選擇權行使相連，可能為計畫性交易）。未見 CEO 或 CFO 的公開市場買入或賣出。內部人信號偏中性，略偏負面，但信心低。

## Ownership shifts
- 機構持股比例：84.7%（2,714 家機構）；內部人持股 0.24%。
- 前十大機構（2026-06-30 申報）方向：上升 5 家、下降 5 家，淨方向中性。
  - 增持：JPMorgan +65.9%、T. Rowe Price +15.9%、State Street +4.5%、Morgan Stanley +3.6%、Vanguard Capital +0.9%。
  - 減持：Geode -17.0%、Invesco -15.4%、BlackRock -3.5%、Bank of America -1.6%、Vanguard PM -0.1%。
- 注意：百分比變動為單季度數字，未能取得多季趨勢，無法判斷持續性。另外，指數型基金的被動調整可能影響 Geode、BlackRock 等的數字。

## Net sentiment score
- 分析師面：偏多（bullish），評等 26/30 為 Buy 以上（86.7%），無 Sell；信心：中高（家數結構穩定，但目標價來源衝突）。
- 內部人面：中性偏空（neutral-to-bearish），僅一筆公開市場賣出，無買入；信心：低。
- 散戶面：DATA_UNAVAILABLE。
- 機構面：中性，前十大淨方向接近持平。
- 綜合：分析師與機構面偏多或中性，內部人略偏空，散戶缺失。整體判斷為 **neutral-to-bullish（偏多但中性），信心低**，主要受散戶資料缺失限制。

Divergence flag：**DATA_UNAVAILABLE**。無法比較散戶傾向與分析師傾向。分析師面偏多，但內部人在 2026 年持續減持，兩者可能有背離，需待散戶資料補齊後確認。

## 指標表

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師 Buy 以上比例 | 86.7%（26/30） | yf rec_summary，0m |
| 分析師 Hold 比例 | 13.3%（4/30） | yf rec_summary，0m |
| 分析師 Sell 比例 | 0%（0/30） | yf rec_summary，0m |
| Buy 家數三個月變化 | 21 → 23（+2） | yf rec_summary，-3m 至 0m |
| 共識目標價 | $324–$358（來源不一） | MarketBeat / Benzinga / Investing.com，WebSearch |
| 近期評等變動 | GLJ 升 Buy（$381）；KeyCorp、Citi、RBC 降目標價 | WebSearch，日期與價格待驗證 |
| 6 個月內部人淨買入 | $0 | yf insider，窗口 2026-04-14 至 2026-10-14 |
| 6 個月內部人賣出 | $3.88M（1 筆，Monser） | yf insider |
| 內部人 CEO / CFO 公開市場交易 | 無 | yf insider |
| 機構持股比例 | 84.7%（2,714 家） | yf major_holders |
| 內部人持股比例 | 0.24% | yf major_holders |
| 前十大機構淨方向 | 5 增 / 5 減（接近中性） | yf inst_holders，2026-06-30 |
| 機構方向（JPM、T. Rowe 等增持） | 正向少數大型機構加碼 | yf inst_holders |
| Reddit 聲量與傾向 | DATA_UNAVAILABLE | WebFetch 無法連線 |
| StockTwits 多空比 | DATA_UNAVAILABLE | DNS 失敗 |
| X / 社群聲量 | DATA_UNAVAILABLE | 僅找到新聞 |
| 散戶與分析師分歧 | DATA_UNAVAILABLE | 散戶資料缺失 |
| 綜合情緒 | 中性偏多，信心低 | 本報告判斷 |

SENTIMENT REPORT COMPLETE
