# Sentiment — ALAB as of 2026-10-25

資料截止：工具可取得的最新資料為 2026-10-24（系統時鐘 2026-10-24 20:11 UTC）。報告日期 2026-10-25 尚無收盤資料，以下結論以 10-24 前可得資訊為準。散戶來源全部失敗，本報告的情緒判斷主要依賴分析師與內部人交易資料。

## Analyst consensus

目前 26 家覆蓋：7 Strong Buy / 11 Buy / 8 Hold / 0 Sell / 0 Strong Sell。買進系 18 家（69%）、持有 8 家（31%）、賣出 0 家。

近 4 期彙總（yf rec_summary）：

| 期間 | Strong Buy | Buy | Hold | Sell | 買進系合計 |
|---|---|---|---|---|---|
| 目前 (0m) | 7 | 11 | 8 | 0 | 18 |
| -1m | 7 | 12 | 7 | 0 | 19 |
| -2m | 7 | 12 | 7 | 0 | 19 |
| -3m | 7 | 11 | 8 | 0 | 18 |

近期變動：過去約一個月，Buy 由 19 降為 18、Hold 由 7 升為 8，等於約一家券商由買進轉為持有（或新增持有評等）。這個變化與前一期的反向變動互相抵銷，三個月淨變動為零。`recommendations` 工具回傳的是彙總期間數據，沒有逐家券商的升降評等明細，因此無法確認是哪一家券商。

已知的個別事件：UBS 於 2026-04 首次覆蓋，評等為 Neutral（來源見下方）。

目標價：Benzinga 彙總的平均目標價為 $291、最高 $500，但該頁標示資料時點為 2026-01，已過期，不能代表 10 月的共識。目前無可靠的 10 月目標價變動資料。

## Retail social

- Reddit：無法取得。WebFetch 被拒絕（"Claude Code is unable to fetch from www.reddit.com"），經 proxy 以 curl 測試 old.reddit.com 亦回 403。r/wallstreetbets 與 r/stocks 均無資料，本節無法列出代表性討論串。
- StockTwits：DNS 解析失敗（api.stocktwits.com ENOTFOUND），無資料。
- X / 新聞聚合：WebSearch 僅回傳股票資訊站與分析彙總頁，沒有 2026-10 的散戶貼文可引用。
- 聲量（buzz volume）：無法量化，無法與平常水準比較。
- 散戶傾向（tilt）：無法判定。
- 主題（themes）：無可引用的散戶主題。
- 其他參考：Benzinga 顯示 put/call ratio 1.12，該站解讀為偏空，但頁面未標示日期，不確定是否為本期數值。Equibles 顯示 90 天內部人淨賣 -$64.0M、空單佔流通股 5.25%（已下降），這個數字與本報告的 6 個月口徑不同，來源時點也不明。另有泰國 BKK 掛牌（ALAB23）的價格資料，與 Nasdaq 美元價格不可比，已排除。

## Insider activity

口徑：2026-04-25 至 2026-10-25（6 個月）。金額單位為 USD M。

- 公開市場買入（open-market buy）：0 筆 / $0.0M
- 賣出（Sale）：24 筆 / 約 $565.7M
- 不計入：Stock Award（董事與主管例行授予）、Stock Gift（贈與）。10-01 授予價為 $311.57，董事 Hurlston 與 Barratt 各 68–72 股，金額很小。
- 注意：2026-08-17（Mohan 與 Gajendra，各 90,630 股、$30.8M）與 2026-05-18（Mohan 與 Gajendra，各 95,444 股、$21.5M）兩組交易的股數與金額完全相同，可能是同一筆交易被重複申報。若去重，賣出總額約 $513.4M。

| 人員 | 職稱 | 筆數 | 賣出金額 (USD M) | 主要日期 |
|---|---|---|---|---|
| Gajendra Sanjay | President | 6 | 292.0 | 05-07 至 08-17 |
| Mohan Jitendra | CEO | 4 | 111.6 | 05-07 至 08-17 |
| Alba Manuel | Director | 4 | 132.5 | 07-01（3 筆）、09-01 |
| Dyckerhoff Stefan A | Director | 5 | 20.0 | 05-07 至 09-02 |
| Mazzara Philip | General Counsel | 3 | 5.8 | 05-18、05-21、08-17 |
| Lazar Jack R | Director | 1 | 3.6 | 06-04 |
| Mayer Bethany J | Director | 1 | 0.3 | 06-24 |
| Tate Michael Truett | CFO（先前） | 0 | 0 | 本期間內無交易 |

Notable：
- President Gajendra 於 2026-05-21 以 $289–293 賣出 400,000 股，約 $116.1M，是期間內最大單筆。
- Alba（Director）於 2026-07-01 以 $430–468 賣出約 $60.5M，並於 09-01 以 $277–289 再賣 $51.3M。
- CEO Mohan 最近一筆為 2026-08-17，以 $334–352 賣出 90,630 股，約 $30.8M。
- 內部人賣出價格區間約 $90 至 $468（2025 至 2026 年），越高價時的賣出規模越大。
- 回溯至 2024-11 的交易資料中，未見任何公開市場買入。
- 主管職稱：Desmond Lynch 於 2026-05-01 的紀錄顯示為 CFO；Tate 最後一筆賣出在 2026-02。

## Ownership

- 內部人持股：10.3%
- 機構持股：75.6%（佔流通股 84.3%），機構家數 1,334
- 趨勢：工具僅提供單一時點快照，無歷史比較，無法判斷機構是增持或減持。

## Net sentiment score

- 分析師：偏多。18/26 買進系，0 家賣出；但近一個月邊際轉弱（一家由 Buy 轉 Hold）。
- 內部人：偏空。6 個月 0 買入、約 $566M 賣出（去重後約 $513M）；CEO 與 President 集中在 5 月與 8 月。工具無法判定這些是否為預先排程交易，因此訊號強度要打折扣。
- 散戶：無資料，無法評估。
- 綜合：中性偏空（neutral-to-bearish），信心低。低信心的原因是散戶資料完全缺失，且分析師目標價資料已過期。
- Divergence flag：無法判定（散戶資料缺失）。但分析師偏多與內部人大量賣出之間存在內部背離，屬於需要在辯論中釐清的重點。

## 資料缺口與限制

1. Reddit：WebFetch 與 proxy curl 均被拒（403），無資料。
2. StockTwits：DNS 失敗，無資料。
3. yf recommendations：只回傳彙總期間，無逐家評等變動明細。
4. 目標價：Benzinga 數字為 2026-01，已過期。
5. 內部人 6 個月口徑與 Equibles 90 天口徑不同，兩者不可直接相加或比較。
6. 報告日期 2026-10-25 晚於系統日期 2026-10-24，所有數據截至 10-24。

## 來源

- [Nasdaq：UBS 首次覆蓋 ALAB，Neutral](https://www.nasdaq.com/articles/ubs-initiates-coverage-astera-labs-alab-neutral-recommendation)
- [Benzinga：ALAB 情緒與分析師評等](https://www.benzinga.com/quote/ALAB/sentiment)
- [Equibles：ALAB 概覽](https://equibles.com/stocks/ALAB)

SENTIMENT REPORT COMPLETE
