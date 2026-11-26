# Sentiment — MP (MP Materials) as of 2026-11-27

註：環境日期為 2026-11-26，web 資料最新僅到 2026-11 中旬（約 11/12–11/17），11/17 之後的資料缺失。

## Analyst consensus
目前 rec_summary（yf，cache）：18 buy（強力買進 5 + 買進 13）/ 0 hold / 0 sell。
近四個月趨勢：-3m 0 hold；-2m 1 hold；-1m 1 hold；0m 0 hold。買方家數穩定在 18，hold 由 1 降為 0，代表近期有一家由 Hold 升為 Buy。

近期變動（web 來源）：
- Freedom Broker：11/12 由 Hold 升為 Buy，目標價由 $57 降為 $51，理由是營運費用下降。$51 約有 40% 上行空間，對應股價約 $36–37。
- AAII（11/16）記載過去一個月有 1 家分析師降評、0 家升評。這與上述 Freedom 升評及 yf 的 0 sell 有矛盾，無法在本次資料中解決，需標註。
- 目標價參考（皆為舊資料）：Morgan Stanley 2026-05 目標 $70（由 $62 調升，維持 Overweight）；Fintel 平均 12 個月目標 $81.21（2026-05-14）。
- 當前 consensus 平均目標價：DATA_UNAVAILABLE。yf 僅回傳評級分布，無目標價欄位。
- 個別券商 2026-11 的新評級，除 Freedom 外：DATA_UNAVAILABLE。yf 的 recommendations 只提供期間彙總，沒有逐筆評等變動日期。

## Retail social
- Reddit：r/wallstreetbets 與 r/stocks 直連被沙箱封鎖，改以 WebSearch 查詢。搜尋結果只找到 2025 年的 WSB 多頭論文，沒有 2026-11 的貼文量與 tilt 數據。Reddit 近期 tilt：DATA_UNAVAILABLE。
- StockTwits：最新一筆（日期不明）顯示情緒由 bearish 轉為 bullish，三個月前為 bearish；訊息量週增約 140%，追蹤人數一年增約 76%。另一篇 Freedom 升評新聞提到情緒由 "extremely bullish" 降至 "bullish"。直接 API 未取得，DATA_UNAVAILABLE（原始貼文）。
- X / 其他：LunarCrush 快照互相矛盾（一筆顯示社群正向情緒 86%，另一筆顯示重度賣壓）。TipRanks 部落客 bullish 76.9%（21 則意見，日期不明）。
- 聲量相對典型值：DATA_UNAVAILABLE（缺乏 2026-11 的提及數基準）。
- 主要主題：
  1. 美國國防與供應鏈（Army 供應鏈壓力測試、國防需求）
  2. 中國稀土出口管制，MP 作為非中國垂直整合龍頭的稀缺性
  3. 永磁體產能擴張（Needham 認為未來三年成為美國主要供應商）
  4. 價格保障（price floor）可能取消的風險
  5. 估值與成本控制（Freedom 升評理由）
  6. 股價波動大，2026-09 相對 sector 下跌約 21%
- 代表性散戶觀點（短引）："MP Materials CEO Says It's Moving At 'Warp Speed'"（StockTwits 標題，2025 年舊文）。

## Insider activity
yf insider 回傳空陣列，視為 DATA_UNAVAILABLE；以下資料來自 WebSearch 的 Form 4 彙整，僅部分可信。

過去 6 個月（約 2026-05-27 起）可確認的交易：
- CEO James Litinsky：2026-05-27 至 05-29 賣出 400,000 股，均價約 $64.56，約 $25.8M。
- CEO（經信託）：2026-06-03 賣出 185,167 股，價約 $68.65，約 $12.7M。未見 10b5-1 計畫敘述。
- CFO：2026-05 賣出 20,000 股（價格與金額 DATA_UNAVAILABLE）。
- 2026-11-10 至 11-17：多名高管與董事合計買進約 98,600 股，金額 > $3.5M（約 $35–36/股）。個別姓名 DATA_UNAVAILABLE。
- 6 個月淨額（部分）：買入 ≥ $3.5M；賣出 ≥ $38.5M（不含 CFO）。6 月中至 11 月的交易資料缺失，故 6 個月淨額為估計，淨賣出可能偏大。

較早期（12 個月彙總，約到 2026-10-26）：3 名內部人共賣出 $146.8M（14 筆）；一名 COO 買入 $1.5M（時間不明）。Litinsky 的 1 月與 4 月賣出（300,000 股；259,179 股，約 $16.6M）標示為 10b5-1 計畫。

## Ownership
（yf major_holders，cache 快照，無趨勢資料）
- 內部人持股：19.67%
- 機構持股：79.35%（占流通股 98.77%）
- 機構家數：966
- 機構集中度趨勢：DATA_UNAVAILABLE（只有單一快照）

## Net sentiment score
- 分析師：偏多（18 buy、0 sell，樣本小，且含 Freedom 降價目標）。
- 散戶：中性偏多但證據薄弱。StockTwits 最後一次為 bullish，但日期不明，且 11/17 後無資料。
- 內部人：偏空混合。H1 以 CEO 大額賣出為主（多為 10b5-1），11 月出現高管與董事集中買進，訊號較正面。

綜合：中性偏多，信心低–中。主要依據是分析師一致買進與 11 月內部人買進，但散戶端 2026-11 資料缺失，且市場價格自 2026 年中高點 $64–68 下跌至約 $37，波動與情緒可能快速變化。

Divergence flag：部分是。內部人在 H1 大量賣出，而分析師為一致買進，兩者方向不同。散戶與分析師方向是否相反無法判定（散戶 2026-11 資料 DATA_UNAVAILABLE）。

未解決的資料缺口：
1. 分析師 consensus 平均目標價與 2026-11 逐筆評等變動
2. Reddit 與 StockTwits 2026-11 的貼文量與 tilt
3. 6 月中至 11 月的 Form 4 完整清單與內部人姓名
4. 機構持股趨勢
5. AAII 所稱 11 月降評與 Freedom 升評的矛盾
