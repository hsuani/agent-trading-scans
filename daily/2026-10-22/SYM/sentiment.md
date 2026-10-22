# Sentiment — SYM (Symbotic Inc) as of 2026-10-22

資料來源狀態: yf 即時 feed 無法連線 (Yahoo cookie/crumb 失敗), 但 `pipeline/tools/yf` 仍回傳資料, 日期標示不明, 視為近期快照。Reddit 與 StockTwits 無法直接抓取, 改以 WebSearch 取得間接資料; 未找到當期 r/wallstreetbets 或 r/stocks 討論串。repo 內 `prices/yf/SYM/` 不存在, 無價格快取可對照。

## Analyst consensus
目前 (0m) 共 17 家: 1 strong buy / 8 buy / 5 hold / 2 sell / 1 strong sell, 即 9 buy / 5 hold / 3 sell。
近 3 個月趨勢: -3m 與 -2m 為 10 buy / 5 hold / 3 sell, -1m 與 0m 降為 9 buy, 呈小幅降溫, 但分布仍偏多。

近期評等與目標價 (WebSearch 聚合, 日期與來源彼此不一致, 需以 MarketBeat / TipRanks 複核):
- Baird: 目標價 $58 下修至 $51, 維持 Neutral (Q3 後模型更新)。
- Oppenheimer: 目標價 $84 上修至 $85, 維持 Outperform。
- Benzinga 彙整 (2026-09): 21 家, Buy, 平均目標價 $55。StockAnalysis 彙整: 18 家 Buy, 平均目標價 $64.32 (未標日期)。
- 偏空端: Barclays Underweight $38 (2025-10 起始); Goldman Sell $47 (2025-12); UBS Sell $35 (2025-09)。
- Craig-Hallum 曾由 Buy 降為 Hold, 目標價 $25 (舊聞, 日期不明); Arete 由 Buy 降為 Neutral, $50 (日期不明)。
- Weiss Ratings 於 2026-05-11 由 hold 降為 sell (WebSearch 來源)。

解讀: 分析師整體仍偏多, 但平均目標價 ($55–64) 與可能的最新收盤價 (約 $37, 見下方) 差距明顯, 顯示市場定價遠低於共識目標。

## Retail social
- Reddit: 未取得當期 r/wallstreetbets / r/stocks 相關討論串 (WebSearch 無結果; 直接抓 Reddit JSON 未於本次執行)。無法判定 tilt, 標示為資料缺口。
- StockTwits / X: AltIndex 第三方彙整, 情緒分數 94/100 (標示 bullish), 平均約 56 則/日, 三個月增加約 24%, 聲量通常在財報、新聞與突破時放大。此為第三方計算值, 非 StockTwits 官方數據, 且未標日期。
- Longbridge 社群 3 個月 Bullish vs Bearish 投票僅 1 票 (bearish), 樣本太小, 不具統計意義。
- TipRanks 顯示 "Very Positive", 但來源為其自有投資組合樣本, 非社群貼文。
- 聲量判定: 相對典型水準為中等 (AltIndex 估計 ~56/日, 無基準可比對, 屬定性判斷)。
- Themes (從新聞與聚合來源歸納, 非貼文原文):
  1. 客戶集中風險: Walmart 為主要客戶, 管理層將 SymMicro 大規模推廣時程由 2026–2027 延至 2028 (來源 sahmcapital 2026-08)。
  2. 獲利轉折: Q3 營收約 US$721M, adjusted EBITDA US$95M, 並達 GAAP 獲利 (同上來源)。
  3. 空方擁擠: Benzinga 列示 short interest 約 31.7% (標示 bearish), 數字高, 需以交易所或 FINRA 資料複核。
  4. 股價走弱: 10 月市場快照顯示收盤約 US$36.94, 年初至今約 -41.6% (來源日期不明)。
- 代表性 crowd 觀點 (WebSearch 聚合摘要, 非原文引用): 「AI warehouse 需求強但部署節奏慢」等論調; 無可靠原文可引用。

## Insider activity
過去 6 個月 (2026-04-22 至 2026-10-22) 無公開市場買入 (open-market purchase) 紀錄。
- 合計申報賣出金額 約 $293.4M, 其中 SoftBank Group (10% 以上大股東) 單筆 $281.8M (2026-05-27, 5.59M 股, 約 $50.42)。
- 排除 SoftBank 後, 董事與管理層賣出約 $11.6M。

Net 6mo: $0 buys, 約 $11.6M sells (不含 SoftBank); 含 SoftBank 為 $293.4M sells。

主要人員 (不含 SoftBank):
- Todd J. Krasnow (Director): 約 $3.49M, 多筆定期小額賣出 (每月 2,000 股上下), 2026-10-05 最近一次 (約 $42.67–43.03)。
- Brian D. Alexander (Officer): 約 $2.64M, 2026-04-24 賣出 37,860 股 (約 $60)。
- James J. Kuffner Jr (CTO): 約 $2.31M, 2026-07-24 賣出 18,987 股 (約 $40.38), 另有 2026-08-24 賣出 3,952 股 (約 $40.59)。
- William M. Boyd III (Officer): 約 $1.15M, 2026-07-27 賣出 9,194 股 (約 $40.8)。
- Izilda P. Martins (CFO): 約 $1.12M, 2026-07-27 賣出 27,463 股 (約 $40.80)。
- Charles F. Kane (Director): 約 $0.55M, 2026-10-01 賣出 2,000 股 (約 $42.7)。
- Maria G. Freve (Officer): 約 $0.36M。

解讀: 大多為規律性小額賣出 (疑似 10b5-1 計畫或稅務相關), 但高階主管在 $40 附近持續出脫, 且 CEO Richard B. Cohen 本期無交易紀錄 (2025-12 有 100 萬股贈與, 非賣出)。無內部人買入, 對情緒為負面訊號, 但強度需依計畫性判讀。

## Ownership shifts
- 機構持股約 79.4%, 機構家數 555, 流通股持有比約 91.9%。內部人持股約 13.6%。
- 前五大持有人 (2026-06-30 申報): SoftBank 30.66% (39.8M 股, 申報期內無變動), Walmart 11.55% (15.0M 股), Baillie Gifford 9.44% (-1.7%), Vanguard PM 3.31% (+13.9%), Morgan Stanley 2.98% (+66%)。
- 集中度高: SoftBank 與 Walmart 合計約 42%, 流動性與股價對少數大股東的動向敏感。SoftBank 本期已有兩次大額出售 (2025-12 與 2026-05)。

## Net sentiment score
Composite: **偏空 (bearish-leaning neutral), 信心度低**

依據權重:
- 分析師 (偏多, 9 buy vs 3 sell, 但目標價漂移與 Baird 下修): 中性偏多
- 內部人 (0 買入, 高階與董事持續賣出, 含 SoftBank 大額減持): 偏空
- 散戶 (資料不足; 第三方 StockTwits 分數偏多, 但 short interest 31.7% 與股價跌幅顯示市場買盤弱): 無法判定

Divergence flag: **資料不足, 無法確認**。若以既有訊號判斷, 分析師偏多與內部人偏空方向相反, 這類背離通常有參考價值, 但散戶端缺乏可靠的當期資料, 不能據此判定散戶與分析師方向是否相反。

信心度: 低。原因: (1) Reddit 無當期資料; (2) 目標價與評等日期互相衝突; (3) 股價快照 (約 $37) 與 10 月內部人成交價 (約 $42–43) 不一致, 價格資料需以即時來源確認。

SENTIMENT REPORT COMPLETE
