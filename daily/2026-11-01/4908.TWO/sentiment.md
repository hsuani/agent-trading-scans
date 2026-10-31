# Sentiment — 4908.TWO 前鼎光電 as of 2026-11-01

資料完整度：低。本次可取得的即時來源只有 yf major_holders。analyst、insider、Reddit、StockTwits、X/新聞搜尋都沒有取得 2026-10 之後的可用資料。下列結論多數依賴 2026-06-24 與 2026-07-21 的既有報告，已標註日期。

## 資料取得狀況

| 來源 | 狀態 | 說明 |
|------|------|------|
| yf recommendations / rec_summary | 失敗（回傳空陣列） | Yahoo cookie/crumb 取得失敗 |
| yf insider | 失敗（回傳空陣列） | 同上 |
| yf major_holders | 成功 | 見下方「Ownership」 |
| Reddit r/wallstreetbets、r/stocks | 失敗 | WebFetch 無法連線 www.reddit.com |
| StockTwits | 失敗 | api.stocktwits.com DNS 無法解析 |
| WebSearch（英文、中文） | 無相關結果 | 未找到 4908 於 2026-10 的評論、評等或目標價 |

## Analyst consensus

本次無法取得 buy/hold/sell 分布，也無近期升降評與目標價變動。既有報告一致指出：Yahoo Finance 及主流國際券商無專業分析師覆蓋；台灣本地平台也無官方目標價或評等統計。

## Retail social

- Reddit：本次無法取得。2026-06-24 報告指出 wallstreetbets 與 stocks 幾乎沒有 4908 討論。
- StockTwits / X：本次無法取得。
- 既有論調（2026-07-21）：長期樂觀、短期分歧。看好者聚焦 CPO、800G/1.6T 光模組與 AI 光通訊需求；警戒者質疑本益比與股價漲幅是否已反映基本面。
- 主要主題（沿用舊資料，未經本次驗證）：CPO 切入進度（ELS 2026 小量出貨、2027 預計放量）、800G/1.6T 量產、本益比泡沫風險。

## Insider activity

本次 yf insider 失敗，無 6 個月內的買賣明細，無法計算淨買賣金額。

既有資料（需注意日期）：
- 2026-06-24：董監持股約 13.14%，無質押紀錄。
- 2026-07-21：未見董監或內部人明顯的大額買進或賣出；董事長為葉政彥、總經理為李昌祐；2026 年 5 月決議 2025 年度現金股利每股 1.00 元。

Net 6mo: 無法計算（本次無資料）。

## Ownership

yf major_holders（本次可取得）：
- insidersPercentHeld：44.18%
- institutionsPercentHeld：0.90%（float 口徑 1.62%）
- institutionsCount：5

解讀與限制：Yahoo 的 insider 比例 44.18% 明顯高於既有報告的董監 13.26%，兩者定義不同，可能把大股東合併計入，本數據不宜直接採用。既有報告顯示個人與國內法人持股合計超過九成，外資持股約 3% 至 6%。本次無法判定機構集中度趨勢。

## Net sentiment score

綜合：資料不足，無法給出可信的 bullish / neutral / bearish 結論。沿用 2026-07-21 的判定為中立偏空（Neutral-to-Bearish，風險高），但該判定基於 7 月資料，本次無法更新。

信心：低。

Divergence flag: 無法判定（缺少 analyst 與 retail 本期資料）。

## 建議後續補充
1. 在 session 網路設定中允許 api.stocktwits.com，並確認 Yahoo 是否可用。
2. 改用台灣來源補 analyst 與 insider：鉅亨網研究評等、MoneyDJ、Goodinfo 的董監持股與大股東異動、公開資訊觀測站的內部人申報。
3. 補抓 TDCC 股權分散表，核對 major_holders 的衝突數據。
