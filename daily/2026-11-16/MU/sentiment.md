# Sentiment — MU as of 2026-11-16

## Analyst consensus
49 家覆蓋（yf rec_summary，0m）：9 Strong Buy / 36 Buy / 4 Hold / 0 Sell / 0 Strong Sell，買方評級佔 92%（45/49）。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell |
|---|---|---|---|---|---|
| 0m（當前） | 9 | 36 | 4 | 0 | 0 |
| -1m | 9 | 36 | 3 | 0 | 1 |
| -2m | 9 | 36 | 3 | 0 | 1 |
| -3m | 9 | 35 | 4 | 0 | 0 |

Recent moves: 近一個月 Strong Sell 由 1 家減為 0，Hold 由 3 家增為 4 家，整體仍偏多。yf 未提供個別券商的升降評等明細，無法指認是哪家機構調整。

目標價：yf 工具未提供目標價資料。WebSearch 找到的目標價數字互相矛盾（平均目標約 642 至 1,562 USD，來源日期不一致，部分頁面標 2026 但內容為 2025 事件），無法確認 2026-11 的共識目標價，本報告不採用。

## Retail social
- Reddit：依任務指示未直接存取 r/wallstreetbets 與 r/stocks（直接社群站點視為封鎖）。間接來源顯示 1 月時 WSB 討論熱烈，主題為選擇權獲利；10 月底專欄指出 Reddit 情緒由多轉空。傾向：偏空（低信心，無 11 月具日期的代表性貼文）。
- StockTwits：未直接呼叫 API（視為 soft-fail）。間接來源：10/1 情緒為「extremely bullish」，10/13 股價 4 個交易日跌超 14% 後轉為 bearish，11/1 報導仍為 bearish。另有一篇標題為「Retail Suggests Buying The Dip」的文章（日期不明），顯示零售端仍有逢低買的聲音。傾向：偏空，但有逢低承接的少數意見。
- X：無直接 X 數據。SentiSense（11/8 聚合頁）顯示 30 日情緒仍偏多但轉弱，今日讀數為中性；該頁未拆分 X 來源。
- LunarCrush：兩個快照分別為正面 93% 與 74%，無日期且價格對不上，已排除。
- 討論量（buzz volume）：無可靠計數，僅能定性判斷。10 月中至 11 月初的話題集中在回檔幅度與 AI 記憶體週期，量能無法量化。
- 主要主題：
  1. 記憶體週期高點與利潤率能否持續（最主要的空方論點）
  2. AI HBM 需求與供給緊缺（多方論點）
  3. 估值便宜（1 月來源引用 forward PEG 0.20 對比板塊中位數 1.66）與循環風險並陳
  4. 與同業（SNDK 等）相對表現比較
  5. 內部人大額賣出的解讀

代表性散戶語句（StockTwits 文章標題，≤15 字）：「Retail Suggests Buying The Dip」。

## Insider activity
窗口：2026-05-16 至 2026-11-16（yf insider 全部 102 筆中，窗口內 13 筆 Sale，0 筆 Purchase）。

| 項目 | USD M |
|---|---|
| 6 個月賣出（13 筆） | 246.3 |
| 6 個月買入（0 筆） | 0.0 |
| 淨額 | -246.3 |

| 內部人 | 職位 | 6mo 賣出 USD M | 備註 |
|---|---|---|---|
| Sanjay Mehrotra | CEO | 160.8（7 筆） | 占賣出總額約 65%，5/29 至 8/21 多次分批出售 |
| April S. Arnzen | Officer | 43.4（7/1） | 單筆最大 |
| Scott J. DeBoer | President | 25.7（10/16） | 最近一筆 |
| Sumit Sadana | Officer | 14.0（8/18） | |
| Lynn A. Dugle | Director | 1.5（6/30） | |
| Scott R. Allen | Officer | 0.9（7/23） | |
| Alexis Bjorlin | Director | <0.1（6/26，間接持有） | |

Notable：CEO 在 6 月至 8 月的售價約 900 至 1,190 USD。窗口內無任何公開市場買入。上一筆買入為 Director Teyin Mark Liu 於 2026-01-14 買進約 7.8 USD M（價約 337 USD），在窗口之外。內部人持股比例僅 0.52%。資料未標示是否為 10b5-1 計畫交易，無法判斷賣出是否為預先安排。

## Ownership
- 機構持股 80.3%（float 80.8%），機構家數 5,164；內部人持股 0.52%。
- 前十大機構（yf inst_holders，股數與比例）：

| 機構 | 持股比例 | 季度變化 | 報告期 |
|---|---|---|---|
| BlackRock | 9.27% | +1.6% | 06-30 |
| Vanguard Capital | 6.51% | +0.7% | 06-30 |
| State Street | 4.52% | +2.1% | 09-30 |
| Invesco | 3.22% | +0.2% | 09-30 |
| FMR | 3.14% | +32.8% | 09-30 |
| Geode | 2.50% | +2.0% | 09-30 |
| Vanguard PM | 2.18% | +7.1% | 06-30 |
| JPMorgan | 1.98% | -13.2% | 09-30 |
| Primecap | 1.65% | -3.1% | 09-30 |
| Morgan Stanley | 1.63% | +9.7% | 06-30 |

- 前十大合計約 36.6%。10 家中 8 家加碼、2 家減碼，FMR 增幅最大。
- 注意：各機構報告期不同（06-30 與 09-30），比較時需留意。

## Net sentiment score
Composite：中性偏空（信心中等偏低）

| 面向 | 傾向 | 信心 | 依據 |
|---|---|---|---|
| 分析師 | 偏多 | 中 | 買方 92%，近期無賣方評等；目標價缺漏 |
| 零售（Reddit / StockTwits / X） | 偏空 | 低 | 10 月後轉空，11 月初仍偏空，皆為間接資料 |
| 內部人 | 偏空 | 中 | 6 個月淨賣 246.3 USD M，無買入；10b5-1 狀態未知 |
| 機構持股 | 中性偏多 | 中 | 前十大 8 增 2 減，FMR 大幅加碼 |

Divergence flag：yes。分析師偏多、零售偏空，內部人淨賣也與分析師方向相反。此類分歧常具參考價值，但本報告不提供交易建議。

資料品質注意：
- yf 的 cookie/crumb 取得失敗，但資料有回傳；rec 與 rec_summary 數值完全相同。
- 內部人資料最新至 2026-10-16，機構持股最新至 2026-09-30（13F），與 as-of 日有時差。
- 股價來源互相矛盾：搜尋頁面提到 11/5 約 656 USD、11/11 約 688 USD，而內部人售價在 6 至 10 月為 900 至 1,190 USD。本報告不以股價推論估值。
- 系統執行日為 2026-11-15，報告 as-of 為 2026-11-16，當日盤中或收盤後資料未納入。

SENTIMENT REPORT COMPLETE
