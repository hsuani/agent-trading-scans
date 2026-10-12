# Sentiment — VST as of 2026-10-13

資料時點說明: 分析師與內部人資料取自 prices/yf/VST.json 快取 (refreshed 2026-10-12 15:15 UTC, 即時 Yahoo 端點被擋)。散戶與社群資料來自 WebSearch 聚合頁面, 多數無明確日期或停留在 8 月至 10 月初, 僅作方向性參考。Reddit 與 StockTwits 原站不可直接存取, 本報告未取得原始貼文樣本。

## Analyst consensus
21 家券商: 20 buy-side (4 strongBuy + 16 buy) / 0 hold / 1 strongSell (計為 sell, 未標註券商)。
近 3 個月計數: -3m 為 4 strongBuy / 15 buy / 0 hold / 0 sell / 1 strongSell, 即本月多 1 家 buy, 整體評級結構穩定。
近期動向: 快取內僅有聚合計數, 無逐家 upgrade/downgrade 紀錄, 券商個別動作 DATA_UNAVAILABLE。外部報導 (日期不一) 提及:
- BMO 將目標價由 236 上調至 245, 維持 Outperform (報導稱「after Q3 results」, 但 Q3 財報預定 11/6 才公布, 時間點存疑, 可能指 Q2 後)。
- Mizuho 8 月底首次評為 Outperform, 目標價 169。
- 平均目標價來源分歧: 約 210 至 241 (Benzinga 9 月 210, Barchart 8 月 216, Stock Alarm 無日期 241, Street high 293)。
- 外部報導 Q2 營收未達預期, 2027 年營收一致預估自 6/30 起下修約 4%。

## Retail social
- Reddit: r/wallstreetbets 與 r/stocks 以 VST 關鍵字搜尋, WebSearch 未回傳任何直接討論串, 無法取得 thread 樣本與 tilt, 軟失敗 (soft-fail), 以下不做 Reddit 結論。
- StockTwits / X: Tradestie (約 10/5) 報導 StockTwits 最近 126 則中 116 則標示 bullish (約 92%), 綜合分 54/100 (Hold)。該文同時指出社群訊號常落後於價格變動。LunarCrush 頁面顯示 24 小時社群情緒約 95% 正面 (頁面無日期, 價格快照在 135 至 158 間不一致, 多為不同時點擷取)。SentiSense 8/9 SentiSense Score 為 6 (輕度 bullish, 較一個月前降溫)。StockTwits 原站 DATA_UNAVAILABLE。
- 聲量 (buzz volume): 相對量偏高, 絕對量偏低。Tradestie 指 10/5 前後提及量約高於 30 日均值 4.7 個標準差, 但 Reddit 留言僅 7 則 (基準約 2)。整體屬「相對放大、絕對規模小」。
- 價格脈絡: 10/8 股價跌 6.35% 至約 156.14, 結束五日約 20.5% 的反彈 (自 9/30 收盤起算)。社群熱度與反彈同步, 修正後情緒是否延續待確認。
- 主要主題 (跨來源歸納):
  1. 電力需求與 AI 資料中心購電敘事 (仍是多頭主軸)。
  2. PJM 市場價格管制與監管不確定性 (主要空方與回檔理由)。
  3. Q2 GAAP 下的非現金避險損失, 被視為情緒性賣壓的觸發點 (LunarCrush AI 摘要)。
  4. 美國政府可能提供約 40 億美元貸款協助核電機組升級 (Bloomberg 10/2 報導), 屬正面催化。
- Retail tilt: 偏多 (bullish-leaning), 但證據多為聚合頁與舊資料, 信心中等偏低。

## Insider activity
Net 6mo (2026-04-13 至 2026-10-13, 不含 RSU/選擇權授予與 gift): 買入約 $1.17M / 賣出約 $25.88M / 淨額約 -$24.7M。
- 近期賣出集中: 10/6 HUDSON SCOTT A (Officer) 約 22,222 股 @160.14 ($3.56M); 10/7 MOLDOVAN KRISTOPHER E. (Officer, 前為 CFO) 20,000 股 @165.00 ($3.30M); 9/8 HUDSON 44,444 股 @約151 ($6.75M); 9/8 MOLDOVAN 20,000 股 @151.03 ($3.02M)。
- 董事賣出 (6 月): HELM SCOTT BRADFORD $4.00M @160; ACOSTA ARCILIA C $2.51M @165–170; SULT JOHN R $1.11M @170; BARBAS PAUL M $0.07M。
- 其他: MONTEMAYOR MARGARET M. (Officer) 5 月與 6 月合計約 $1.56M。
- 唯一買入來源為 CEO: BURKE JAMES A. 8/24 買入 2,000 股 @135.00 ($0.27M), 9/1 買入約 6,665 股 @135.25–135.99 ($0.90M)。兩筆皆在股價約 135 時進場, 屬本窗口內唯一的公開市場買盤。
- 注意: 2025 年 9 月至 11 月 CEO 大量行權後賣出, 為歷史高額賣出; 本 6 月窗口內的賣出規模仍高於 CEO 買入約 20 倍, 但多數為管理層例行或選擇權相關處分, 不應單看金額解讀為看空訊號。

## Ownership shifts
- 機構持股比例約 92.0% (流通股約 92.7%), 機構數 1,880 家。
- 內部人持股約 0.77%。
- 趨勢: 快取僅提供單一時點快照, 無歷史對比, 機構集中度變化趨勢 DATA_UNAVAILABLE。

## Net sentiment score
Composite: **偏多但分歧 (neutral-to-bullish), 信心中等。**
- 分析師面: 強烈偏多 (20/21 buy-side, 評級穩定)。
- 散戶面: 偏多 (StockTwits 約 92% bull, LunarCrush 高正面), 但多為舊資料, 且 10/8 後熱度與價格同步回落。
- 內部人面: 明顯偏空 (6 個月淨賣 ~$24.7M, 近期高層集中賣出), 唯一買盤為 CEO 於 135 附近的小額買入。
- 扣分因素: PJM 監管不確定性、Q2 營收未達預期、2027 年營收預估下修。

Divergence flag: **yes**。散戶情緒偏多、分析師偏多, 與內部人賣出及 CEO 低檔買入形成內部方向分歧; 散戶與分析師同向, 但內部人反向, 需留意。

## 限制與未取得項目
- Reddit (r/wallstreetbets, r/stocks) 原始貼文: 未取得。
- StockTwits 原站訊息量與 bull/bear 比: 未取得 (僅第三方 10 月初快照)。
- 逐家券商 upgrade/downgrade 與 PT 變動日期: DATA_UNAVAILABLE。
- 機構持股時間序列: DATA_UNAVAILABLE。
- 未做交易建議, 本報告僅彙整情緒。

## Metrics

| 指標 | 數值 | 來源 / 備註 |
|---|---|---|
| 分析師評級 (buy-side / hold / sell-side) | 20 / 0 / 1 | rec_summary 0m, 快取 2026-10-12 |
| 評級 3 個月變化 | +1 buy (4SB/15B → 4SB/16B) | rec_summary -3m 比較 |
| 分析師平均目標價 | 約 210 至 241 (來源分歧) | WebSearch 聚合, 日期不一 |
| 6 個月內部人買入 | 約 $1.17M | yf insider, 2026-04-13 起 |
| 6 個月內部人賣出 | 約 $25.88M | yf insider, 不含授予 |
| 6 個月淨買賣 | 約 -$24.7M | 計算值 |
| 內部人買入者 | CEO BURKE JAMES A. (2 筆, 約 135 元) | yf insider |
| 內部人近 30 天賣出筆數 | 4 筆 (HUDSON, MOLDOVAN 各 2) | yf insider, 9/8 至 10/7 |
| 機構持股比例 | 92.0% | yf major_holders |
| 內部人持股比例 | 0.77% | yf major_holders |
| 機構家數 | 1,880 | yf major_holders |
| StockTwits bull 比例 | 約 92% (116/126) | Tradestie, 約 10/5 (二手) |
| LunarCrush 正面情緒 | 約 95% | 頁面無日期 |
| 提及量相對 30 日均值 | 約 +4.7 SD | Tradestie, 約 10/5 |
| 散戶 tilt | 偏多 (中低信心) | 綜合 |
| 情緒綜合 | 偏多但分歧 (neutral-to-bullish) | 信心中等 |
| Divergence flag | yes | 內部人賣出 vs 分析師與散戶偏多 |

SENTIMENT REPORT COMPLETE
