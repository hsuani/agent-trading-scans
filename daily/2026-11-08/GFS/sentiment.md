# Sentiment — GFS as of 2026-11-08

資料品質提示: 本次 Reddit 與 StockTwits 無法取得可量化的即時貼文樣本 (WebSearch 僅回傳鏡像頁與舊文), 散戶情緒部分信心偏低。分析師與內部人資料來自 pipeline/tools/yf 快取, 實際即時性未驗證。

## Analyst consensus

yf rec_summary (USD 不適用, 此為家數):

| 評級 | 本期 (0m) | -1m | -2m | -3m |
|---|---|---|---|---|
| Strong Buy | 3 | 3 | 4 | 4 |
| Buy | 10 | 10 | 10 | 9 |
| Hold | 9 | 9 | 8 | 8 |
| Sell | 0 | 0 | 0 | 0 |
| Strong Sell | 1 | 1 | 1 | 1 |
| 合計 | 23 | 23 | 23 | 22 |

本期分布: 13 buy (含 Strong Buy 3) / 9 hold / 1 sell (含 Strong Sell 1), 即 13 buy / 9 hold / 1 sell。買進比重約 57%, 較 -3m 的約 59% 微降, 主要是 Strong Buy 由 4 降至 3, Hold 由 8 增至 9。整體仍偏多但動能略減。

近期評級變動 (日期與來源可靠度不一, 僅供參考):
- Cantor Fitzgerald 由 Neutral 升至 Overweight, 日期 2026-05-04 (Fintel 歷史表)。
- Morgan Stanley 目標價由 $60 調降至 $56, 維持 Equal Weight (日期未明, 來自 MarketBeat 摘要)。
- Jefferies 由 Buy 降至 Hold, 目標價 $38 (日期未明, 看似較舊)。
- BofA 降至 Underperform, 目標價 $35 (日期未明)。
- Wedbush 由 Outperform 降至 Neutral, 2025-12-31。

外部彙整網站與 yf 分布不一致: MarketBeat 顯示約 8 buy / 11 hold / 1 sell, Investing.com 顯示約 12 buy / 9 hold / 1 sell。以 yf 為主表, 三者分歧需以即時資料再確認。

財報前瞻: 多個來源指出下一次財報為 2026-11-13 (盤前), 但 Stockevents 另列 2026-11-04, 日期未能交叉驗證。若 11-13 屬實, 距本報告日約 3 個交易日, 屬高事件風險窗口。

## Retail social

- Reddit: 未取得本期 r/wallstreetbets 或 r/stocks 可用貼文。唯一可見的 Reddit 鏡像頁為 2026-02 的舊文, 提到 Wedbush 降評當日股價跌約 4%, 以及空單佔浮動股約 11.7%。樣本過舊, 不計入本期傾向。
- StockTwits / X: StockTwits 即時情緒分數無法取得。舊有 StockTwits 文章顯示 2026-03 財報後情緒為 "extremely bullish" (88/100), 另一篇 2025-01 相關文章為中性 (48/100)。兩者皆非本期, 不作為現況判斷。X 端未找到可辨識的本期貼文。
- 聲量 (定性): 無法量化本期提及次數。搜尋結果中針對 GFS 的新聞與分析師頁面明顯多於散戶社群內容, 推測散戶討論度屬中等至偏低, 但此為間接推論。
- 常見主題 (依新聞與媒體摘要歸納, 非社群原文):
  1. 紐約州 Malta 兩座新晶圓廠: 來源提及最高約 210 億美元投資與 U.S.-Japan 製造倡議, 被視為長線產能與地緣政治受惠題材。
  2. 估值與回檔: 股價自 2026 年中高點明顯回落, 部分文章以 "undervalued" 或 "fair value $76" 論述, 亦有以 "pullback buying opportunity" 框架討論。
  3. 空方論點: 降評理由多為定價壓力 (TSMC、中國), 缺乏催化劑, 以及智慧手機營收占比降至 34% 的歷史低點。
  4. 財報預期: 市場關注下一季營收指引、產能利用率與毛利率走勢。
- 代表性摘要 (非逐字引用, 來源為新聞彙整): 散戶與媒體多數語氣偏向 "長線產能受惠但短線待確認"。

## Insider activity

Net 6mo (2026-05-08 至 2026-11-07, 依 yf insider 資料加總):
- 買進: $0 (期間無公開市場買進紀錄)。
- 賣出: 約 $2.85M (USD), 約 0.0029B。
- 獎勵股與贈與多為 0 價值, 未計入金額。

主要賣出者 (USD):
- VICARI SAMUEL (Officer): 2026-05-11 賣出 8,692 股, 約 $0.66M, 為期內單筆最大。
- RAMAN PRADHEEPA (Officer): 2026-08-18 賣出 6,760 股, 約 $0.35M; 2026-09-28 賣出 2,145 股, 約 $0.10M。
- DORCHAK GLENDA MARY (Director): 2026-07-20 賣出 4,000 股, 約 $0.23M。
- HOGAN MICHAEL JAMES (Officer): 2026-05 至 2026-07 間多筆定期賣出 (每筆約 2,300 至 2,800 股, 合計約 $1.1M), 另有 150 股 / 100 股定期贈與。
- AZAR SAMAK L (Officer): 2026-05 至 2026-09 間約每週或雙週固定賣出 335 至 500 股, 合計約 $0.40M, 呈現規律性交易模式。

解讀: 賣出以 Officer 與 Director 的規律性或分批出售為主, 單筆金額不大, 且期間無任何公開市場買進, 整體偏中性至略偏空。賣出價格區間約 $48 至 $87, 目前股價與此區間的關係在不同來源間分歧 (見下節), 無法判斷是否為高點出清。

機構與持股結構 (yf major_holders, 單一快照, 無時間序列):
- 機構持股約 99.35%, 機構家數約 603, 內部人持股約 0.12%。
- 無法判斷機構集中度趨勢 (需至少兩期快照)。持股已高度集中於機構, 內部人持股比例極低。

## Net sentiment score

Composite: **neutral** (信心: 低)

依據:
- 分析師面: 偏多但動能略減。13 buy / 9 hold / 1 sell, 評級趨勢微幅向 Hold 移動。信心中等。
- 內部人面: 偏空。6 個月約 $2.85M 賣出、零買進。但多為規律性交易, 解讀需保守。信心中等。
- 散戶面: 無法有效量化。本期無可用 Reddit/StockTwits 樣本。信心低。
- 其他: 下一次財報 (2026-11-13 待確認) 為近期主要催化劑, 方向未定。

Divergence flag: **無法判定** — 本期缺乏可靠的散戶傾向資料, 無法確認散戶與分析師是否背離。若日後取得 StockTwits 或 Reddit 即時樣本, 應再檢視此項。

## 資料限制

- yf 資料可能來自快取 (Cookie/crumb 取得失敗), 非即時數值。
- 股價來源衝突極大: MarketBeat 約 $36.33, equibles 約 $47.88, Investing.com 約 $49.99, Earnings Whispers 約 $45.21; 另有 2026-07-14 收盤 $63.81 與 2026-06 內部人賣出價 $80 至 $87 等歷史點位。本報告未以任何單一現價作為判斷基礎。
- 財報 EPS 數字來源亦不一致: 一頁報導 Q1 2026 EPS $0.40 vs 一致預期 $0.3401; 另一頁報導 Q4 2025 EPS $0.55 vs $0.4725, 而 StockTwits 報導 Q4 EPS $0.46 vs $0.45。以上僅作方向參考。

SENTIMENT REPORT COMPLETE
