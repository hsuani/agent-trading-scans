# Sentiment — ZS as of 2026-11-27

> 注意: 系統當前日期為 2026-11-26, 本報告依任務指定之 as-of 2026-11-27 撰寫。最新可得資料點為 2026-11-25 (CFO 賣出成交)。

## Analyst consensus

資料來源: `yf rec_summary` (cache 來源, 目前期 0m)。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 | 買入系 (SB+B) | 持有 |
|---|---|---|---|---|---|---|---|---|
| 0m (當期) | 5 | 17 | 21 | 0 | 0 | 43 | 22 (51%) | 21 (49%) |
| -1m | 7 | 29 | 11 | 0 | 0 | 47 | 36 (77%) | 11 (23%) |
| -2m | 7 | 29 | 10 | 0 | 0 | 46 | 36 (78%) | 10 (22%) |
| -3m | 8 | 29 | 9 | 0 | 0 | 46 | 37 (80%) | 9 (20%) |

賣出評級: 0 家 (各期皆為 0)。

近期評級變化: 當期買入系由 36 家降至 22 家、持有由 11 家升至 21 家, 單月淨降級約 14 家, 為本次最明顯的訊號。但 yf 僅提供彙總計數, 無法辨識是哪幾家券商調整, 也無法確認是否為資料更新造成的計數跳動, 需要交叉驗證。

目標價: 網路來源 (Barchart) 報導平均目標價 $191.71、稱 45 位分析師 "Strong Buy" 共識, 但該文未標日期, 且其所稱 "51% 上漲空間" 隱含股價約 $127, 與同期其他來源的價格不一致, 不可直接採用。Seeking Alpha 的降級文章則認為目標價可能被下修。目標價共識 (日期一致) 為 DATA_UNAVAILABLE。

其他評級機構: Weiss Ratings 給予 D- / Sell (2026-09-23 升等至此評級), 屬獨立評級體系, 不計入上方 sell-side 計數。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): DATA_UNAVAILABLE。以 WebSearch 查詢未取得 ZS 相關 Reddit 討論串 (直接 Reddit JSON 在本沙盒中被封鎖)。唯一 WSB 相關結果是 2025 年 10 月一則提及 ZS 的單篇貼文, 不足以代表情緒。
- StockTwits: 最新可見快照為情緒分數 49 (Neutral), 頁面標示股價 $255.15、財報日 11/24, 但未標示快照時間, 無法確定對應日期, 僅列為低可信參考。2026 年 10 月的報導則指 StockTwits 散戶情緒為 bearish。其他 StockTwits 文章多為 2024–2025 年舊聞, 不列入當期判斷。
- X: 僅有 Quiver Quant 提及 ZS 在 X 上討論熱烈, 無量化資料, 列為 DATA_UNAVAILABLE (量化)。
- AltIndex 彙總 (Reddit + StockTwits 等 NLP): 情緒 85/100 (bullish), 報導稱近期較 30 日均值走弱, 2026 年 8 月曾為 93。日期不明, 且與 StockTwits 中性/看跌讀數方向不同, 可信度低。
- 提及量 (buzz volume): DATA_UNAVAILABLE。無法取得 Reddit/StockTwits 貼文計數, 只能定性判斷: 11 月前後因財報前後與股價大跌, 話題熱度應高於平常, 但無數字佐證。

Top 反覆出現的主題 (來自新聞與彙總文章, 非直接貼文抽樣):
1. AI 衝擊資安/SaaS 的擔憂 ("SaaSpocalypse"), CEO 公開反駁此說法 (StockTwits 報導)。
2. FY2027 營收指引偏保守: 隱含成長約 16.6%–17.5%, 低於 FY2026 的約 25%。
3. 估值面: 多方以 forward EV/Sales 與 PEG 低於同業為論點 (Seeking Alpha 初評買進); 空方則認為 ARR 淨新增成長僅小幅提升。
4. 股價從高點大幅回落, 同業 (CRWD、PANW) 年初至今漲幅遠大於 ZS, 被視為相對弱勢。
5. 散戶歷來在財報後的急跌中逢低買進的模式 (StockTwits 舊聞), 但 2026 年 10 月後轉為偏空。

## Insider activity

資料來源: `yf insider` (cache), 期間 2026-05-27 至 2026-11-25, 依 "Sale at price" 與 "Conversion" / "Grant" 區分。

| 項目 | 金額 (USD M) | 筆數 |
|---|---|---|
| 買入 (open-market purchase) | 0.00 | 0 |
| 賣出 (Sale) | 15.05 | 24 |
| 淨額 | -15.05 | — |

各人賣出金額 (USD M):

| 內部人 | 職稱 | 賣出金額 (USD M) | 備註 |
|---|---|---|---|
| GELLER ADAM | Officer | 8.57 | 最大賣方, 2026-10-12 單筆 25,000 股約 $5.65M (行權後賣出) |
| RUBIN KEVIN E | CFO | 2.25 | 持續小額定期賣出, 最近一筆 2026-11-25 (514 股, $114.5K) |
| SCHLOSSMAN ROBERT S | Officer | 1.94 | 2026-09-21 單筆 5,394 股 @ $200 |
| RICH MICHAEL J | Officer | 1.32 | 2026-09-16 與 06-16 賣出 |
| CHAUDHRY JAGTAR SINGH | CEO | 0.91 | 2026-06-16 與 09-16 各一筆 |
| BEER JAMES ALEXANDER | Director | 0.06 | 小額 |

重點觀察:
- 6 個月內無任何公開市場買入, 全數為賣出。CEO 於 2026-06-16 與 09-16 各賣出一次 (合計約 $0.91M), 金額相對其持股與 CEO 薪酬屬小額。
- 賣出多集中於股價 $190–260 區間。部分交易可能屬 10b5-1 預先排程, 報告無法確認, 標記為 DATA_UNAVAILABLE。
- 交叉驗證: Quiver Quant 報導 6 個月內 insider 0 買 / 18 賣, 與本次 24 筆賣出 (含同一日多列) 的計算口徑不同, 但方向一致。
- 驗算: CHAUDHRY 2,878 股 × $126.43 ≈ $363.9K, 與資料欄位 $363,864 吻合。

## Ownership shifts

來源: `yf major_holders` (cache)。
- 內部人持股: 34.5%
- 機構持股: 54.7% (佔流通股約 83.6%)
- 機構數量: 1,273 家
- 趨勢: 僅單一快照, 無法判斷集中度是增加或減少, 歷史趨勢為 DATA_UNAVAILABLE。

## Net sentiment score

綜合判斷: **中性 (neutral), 信心低**。

- 分析師面: 當期仍有 51% 買入系評級、0 家賣出, 但相較前三期買入系比例顯著下降 (由約 77–80% 降至 51%), 偏中性略偏多, 方向為轉弱。
- 散戶面: 最新 StockTwits 快照中性 (49), 10 月為看跌, AltIndex 彙總為偏多但日期不明。無可靠的 Reddit 數據。整體偏中性, 且數據時效性不足。
- 內部人面: 6 個月 $15.05M 純賣出、零買入, 偏空訊號, 但受 10b5-1 排程影響, 強度需保留。

**Divergence flag: 部分分歧 (未完全確認)**。分析師當期仍多數買入, 而可得的散戶讀數偏中性至偏空, 兩者方向有分歧; 但因散戶資料時效不足, 且分析師當期計數有資料一致性疑慮, 無法可靠認定為確定的反向訊號。

資料缺口摘要 (DATA_UNAVAILABLE):
- Reddit 貼文與情緒 (WebFetch 於沙盒中被封鎖, WebSearch 未返回 ZS 相關討論串)
- 散戶提及量 (定量)
- X 情緒量化
- 逐家券商評級變化與目標價共識 (日期一致版本)
- 機構持股歷史趨勢
- 內部人交易是否為 10b5-1 排程

SENTIMENT REPORT COMPLETE
