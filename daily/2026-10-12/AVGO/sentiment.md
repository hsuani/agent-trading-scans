# Sentiment — AVGO as of 2026-10-12

資料狀態摘要: 分析師評級與目標價來自 repo 快取 (`prices/yf/AVGO.json`, refreshed 2026-10-12 00:47 UTC)。內部人交易資料最新只到 2026-07-10, 7/10 之後到 10/12 之間的 Form 4 未進入快取。Reddit / StockTwits 無法直接抓取, 且 WebSearch 找不到 2026 年 10 月的散戶討論, 散戶面**無有效當期資料**。

## Analyst consensus

47 位分析師: 7 Strong Buy / 40 Buy / 3 Hold / 0 Sell (rec_summary 當期)。三個月前為 7 / 37 / 4 / 0 (共 44 位), 買進側淨增 3 位, Hold 減 1 位, 無賣出評級。`recommendations` 端點只提供月度彙總, 未提供逐筆升降評等紀錄, 因此無法列出個別 upgrade / downgrade 事件。

目標價 (快取 `info`): 平均 $531.31 / 中位數 $535 / 最高 $715 / 最低 $215.88; 對照當期價 $361.54, 平均目標隱含約 +47% 上行空間。最低目標 $215.88 明顯偏離其他分析師, 解讀時應以中位數為準。

第三方網站 (WebSearch, 9 月初時點, 未經驗證):
- Citigroup 9/4 將目標由 $500 上調至 $515, 維持 Buy。
- DA Davidson 將評等下調為 Neutral, 目標由 $400 降至 $350。
- Goldman Sachs 維持 Buy, 目標 $525; TD Cowen 維持 Buy, 目標 $500。
- 各來源共識目標差異大: Benzinga $505 (30 位), Bullstory $525.97 (46 位), StockTi $428.68 (57 位)。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**: WebSearch 未找到 AVGO 相關 WSB 或 r/stocks 討論串。WebFetch 依指示未嘗試直接抓取 (站點封鎖)。無法判定貼文量與傾向。
- **StockTwits**: 最近可取得的讀數為 2026-06-03 (財報前), 當時 retail sentiment 為 "extremely bullish" 且一週內上升。10 月無資料。
- **X / 其他社群**: 無 2026 年 10 月的可用摘要。LunarCrush 頁面顯示 83% 正面情緒、2K 則貼文, 但該快照無日期, 不列入計分。
- **Investing.com user calls** (7/29 至 8/1): 小樣本、自選樣本, 不代表情緒指數。
- **聲量 (buzz volume)**: 無法量化, 無法與歷史基線比較。

Themes (依可取得的 2026 年上半年至夏季內容):
- 多頭: 客製化 AI 晶片 (custom AI accelerators) 與大型 GPU 叢集高速網路 (networking) 的成長動能; 市值超過 $2T。
- 空頭 / 謹慎: 估值 (trailing P/E 約 46x, forward P/E 約 18.6x, 兩者落差大); 科技巨頭 AI 資本支出回收疑慮; 內部人大額賣出。
- 股價路徑: 快取當期價 $361.54, 較 7/10 Brazeal 賣出價 $401.33 低約 10%; 9/4 收盤約 $357.89 (第三方資料)。

## Insider activity

視窗: 2026-04-12 至 2026-10-12 (快取資料最新 2026-07-10)。

Net 6mo: **$373,570 buys / ~$283.7M sells / 淨賣出約 $283.3M** (僅計公開市場 Sale 與 Purchase, 排除 Stock Gift 與 Stock Award)。

- 買進: Harry You (Director), 2026-06-11, 1,000 股 @ $373.57, 約 $0.37M。是視窗內唯一的公開市場買進。
- 賣出 (Samueli, Henry, Director, 間接持有): 2026-06-24, 654,241 股 @ $377.61–388.17, 約 $250.0M。為視窗內單筆最大賣出, 另有同日 336,893 股 gift。
- 賣出 (Brazeal, Mark David, Officer): 2026-06-17 / 06-25 / 07-08 / 07-10, 合計約 $32.4M, 為視窗內最頻繁的賣方。
- 賣出 (Delly, Gayla J, Director): 2026-07-08, 1,890 股, 約 $0.73M。
- 賣出 (Page, Justine F., Director): 2026-06-29, 1,602 股, 約 $0.60M。
- CEO Hock Tan: 視窗內無公開市場交易 (最後一次賣出為 2025-12-23)。
- CFO: 視窗內無賣出; 2026-06-15 有 Amie Thuener O'Toole 名義之 50,000 股 Stock Award (授予, 非買入)。Kirsten Spears 最後一次賣出為 2025-12-31。

解讀: 視窗內賣出集中於 2026 年 6 月至 7 月, 且以董事 (Samueli) 與 Officer (Brazeal) 為主。CEO 與 CFO 在 6 個月內未見公開市場賣出, 此點需與賣出者之 10b5-1 計畫 (本快取未提供) 合併判讀。資料截至 7/10, 7/10 至今之交易未知。

## Ownership shifts

- 內部人持股約 1.92%; 機構持股約 79.85% (機構數 6,265, 快取 major_holders 資料)。
- 前十大機構 (2026-06-30 資料): 7 家增持、3 家減持。
  - 增持: FMR +16.3%, Capital World Investors +4.9%, BlackRock +3.2%, JPMorgan +3.5%, State Street +2.9%, Geode +1.9%, Vanguard Capital Management +0.4%。
  - 減持: Vanguard Portfolio Management -1.1%, Capital Research Global Investors -2.5%, T. Rowe Price -1.9%。
- 解讀: 機構持倉在 2026 年 Q2 呈淨增持, 與內部人淨賣出形成對照。未包含 Q3 13F 資料。

## Net sentiment score

- **分析師面**: 偏多 (信心: 中高)。評級以 Buy 為主, 無 Sell, 近三月小幅上修, 目標中位數高於現價約 48%。扣除資料時間差 (第三方目標為 9 月初時點) 後, 結論不變。
- **內部人交易面**: 偏空 (信心: 中)。6 個月淨賣出約 $283M, 以董事與 Officer 為主, CEO 與 CFO 無公開市場賣出。資料截至 7/10, 需以最新 Form 4 補強。
- **散戶面**: 無法判定 (信心: 低)。Reddit 與 X 無當期資料, StockTwits 最後讀數為 6 月偏多, 不足以代表 10 月狀態。
- **機構持倉面**: 偏多 (信心: 中)。Q2 前十大機構多數增持。
- **綜合**: **中性** (偏多分析師與機構、偏空內部人交易; 散戶面缺資料)。信心: 低至中。

**Divergence flag: 無法判定 (no)**。當期散戶傾向缺資料, 無法確認是否與分析師傾向相反。若未來補入 Reddit / StockTwits 資料, 應重新評估。

## 資料缺口與注意事項

1. 財報日期: 快取 `earnings_dates` 顯示 2026-09-02 (EPS 預估 $3.24) 未填入實際 EPS; 下次財報 2026-12-09 (預估 $3.83)。第三方文章另有 9/30 之說法, 互相衝突。尚未找到 Q3 財報實際結果與財報後目標價調整的資料, 分析師目標可能已改變。
2. 內部人交易截至 2026-07-10, 之後無資料。
3. Reddit、StockTwits、X 當期資料皆無法取得; 未進行 semi 同業 sector scan (本任務範圍為 AVGO 單一標的)。
4. WebSearch 結果多為聚合網站與舊文, 僅作參考, 未逐筆驗證。

## 來源

- 快取資料: `prices/yf/AVGO.json` (yf recommendations / rec_summary / insider / major_holders / info / earnings_dates / inst_holders)。
- WebSearch 第三方摘要 (未直接驗證): Benzinga, Bullstory, StockTi 之 AVGO 分析師頁面; StockTwits 6/3 文章 (stocktwits.com/news-articles); LunarCrush AVGO 頁面; Investing.com 散戶 call 頁面。

SENTIMENT REPORT COMPLETE
