# Sentiment — SYM as of 2026-10-31

資料限制: Reddit (r/wallstreetbets, r/stocks) 無法抓取 (fetch 失敗); StockTwits 因 DNS 無法解析 (api.stocktwits.com 未在 session 允許網域內) 無法抓取。散戶面向數據缺漏, 下方散戶部分僅能以網路搜尋摘要替代, 信心偏低。要補齊需由使用者於 session 網路設定允許 api.stocktwits.com 與 reddit.com 後重跑。

## Analyst consensus

18 家評等: 10 buy (含 1 strong buy) / 5 hold / 3 sell (含 1 strong sell)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 當期 (0m) | 1 | 9 | 5 | 2 | 1 | 18 |
| -1m | 1 | 8 | 5 | 2 | 1 | 17 |
| -2m | 1 | 9 | 5 | 2 | 1 | 18 |
| -3m | 1 | 9 | 5 | 2 | 1 | 18 |

近三個月評等分布大致持平, 買方約 56%, 無明顯升降評趨勢。工具回傳的 `recommendations` 僅為期間彙總, 未提供個別升降評明細, 因此無法列出具體 upgrade/downgrade 事件與目標價變動。

網路搜尋摘要 (未能於 yf 工具驗證, 日期不明, 僅供參考): 一則 Trefis 條目稱 Weiss Ratings 於 2026-05-11 由 hold 下調至 sell; 另有摘要提及 Goldman Sachs 於 May 財報後下調評等或目標價。Benzinga 快照顯示平均目標價約 $55 (21 位分析師, 區間 $10–$82), 但快照時點不明。

## Retail social

- Reddit: 無法抓取 (r/wallstreetbets、r/stocks 皆失敗), 無樣本貼文, 無法判斷近期提及量與傾向。
- StockTwits / X: StockTwits 無法連線。網路搜尋未找到 2026-10 月份可驗證的散戶意見彙整; 搜尋結果多為過期或重複的低品質頁面。
- 提及量: 無法量化 (資料缺漏)。
- 傾向: 無法判定 (bullish / bearish / mixed 皆無足夠樣本)。
- 主題 (僅依搜尋摘要, 低信心): 空頭比率偏高的說法 (Benzinga 快照 short interest 約 31.7%, 標示為上升); 股價自 2026 年初高點回落的敘事。

## Insider activity

統計窗口: 2026-05-01 至 2026-10-31 (六個月)。

Net 6mo: **買入 $0.0M / 賣出 $291.0M** (以工具 Value 欄位計, 有金額之交易共 28 筆, 皆為 Sale)。
- 其中 SoftBank Group Corp (10% 以上持股者) 於 2026-05-27 賣出 5.59M 股, 金額 $281.8M (約 $50.42/股)。此為大股東減持, 不等同於公司高階主管的看法, 但金額佔總賣出九成以上。
- 排除 SoftBank 後, 董事與高階主管賣出約 $9.2M, 零筆公開市場買入。

主要賣方 (排除 SoftBank, 六個月):

| 姓名 | 職稱 | 賣出金額 (USD M) | 最近一筆 |
|---|---|---|---|
| KRASNOW TODD J | Director | 3.49 | 2026-10-05, 約 $42.67–43.03 |
| KUFFNER JAMES J JR | Chief Technology Officer | 1.88 | 2026-10-27, 約 $38.24–38.34 |
| MARTINS IZILDA P | Chief Financial Officer | 1.40 | 2026-10-28, 約 $38.93 |
| BOYD WILLIAM MADISON III | Officer | 0.97 | 2026-10-27, 約 $38.34–39.14 |
| ALEXANDER BRIAN DANIEL | Officer | 0.72 | 2026-10-27, 約 $38.26–38.28 |
| KANE CHARLES FRANCIS | Director | 0.55 | 2026-10-01, 約 $42.72–43.72 |
| FREVE MARIA G | Officer | 0.18 | 2026-10-27, 約 $38.25–38.34 |

注意:
- CFO MARTINS IZILDA P 與 CTO KUFFNER 於 2026-10 月下旬再次賣出, 且 10/23 另有數筆無金額列 (工具未提供金額, 推測為歸屬或稅務代扣相關, 未計入上述金額)。
- 賣出價格區間: 2026 年 1 月約 $54–60, 5 月約 $50–60, 7–8 月約 $40–46, 10 月下旬約 $38–39。賣出價位隨股價下滑而下移, 但高階主管在低價區仍持續賣出。
- 2025-12-11 CEO COHEN RICHARD B 有 1,000,000 股 Stock Gift (金額 0), 不屬於市場交易。

## Ownership shifts

- 內部人持股 (insidersPercentHeld): 13.66%
- 機構持股 (institutionsPercentHeld): 79.32%; 占浮動股 (float) 91.87%
- 機構數量: 555
- 工具僅提供當前快照, 無歷史季度變化, 無法判斷集中度趨勢。
- SoftBank 於 2026-05 大幅減持 (見上), 若其為重要大股東, 持股結構可能已有變化, 但本次資料無法確認其剩餘持股。

## Net sentiment score

Composite: **偏空 (bearish-leaning) / 中性偏空**, 信心: **低至中**。

- 分析師端: 10/18 buy, 評等近三個月穩定, 偏多但未見上調動能。
- 內部人端: 六個月零買入, 董事與高階主管持續於 $38–60 區間賣出, 近期 (10 月) 賣出密度最高 (10/27 單日多位高階主管同日賣出), 偏空訊號。
- 散戶端: 無資料, 無法評分。
- 價格面 (背景): 近期賣出價位明顯低於年初與春季水準, 與空頭敘事一致。

Divergence flag: **無法判定** — 散戶傾向缺漏, 無法比較與分析師傾向是否相反。若後續補上 Reddit/StockTwits 資料, 再重新評估。

SENTIMENT REPORT COMPLETE
