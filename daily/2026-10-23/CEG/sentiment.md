# Sentiment — CEG as of 2026-10-23

## Analyst consensus
yf rec_summary（最新期，0m）：21 buy（6 strong buy + 15 buy）/ 4 hold / 0 sell，共 25 家。買進比例約 84%，無 sell 評級。
近 4 個月走勢（buy 合計 / hold）：-3m 20/3，-2m 19/3，-1m 19/3，0m 21/4。最新期淨增 1 家 hold、buy 側增 2 家，但 yf 無法指出是哪家券商改評，**個別升降評等明細 DATA_UNAVAILABLE**（yf recommendations 只回傳月度彙總，無逐筆 upgrade/downgrade）。

網路補充（WebSearch，日期不一，僅供參考）：
- Google Finance（10 月初）：平均目標價約 351.25 USD，區間約 290–441 USD，股價當時約 268 USD。
- Investing.com：平均目標價 352.86 USD，高 441 / 低 296。
- 近期個別券商：BMO Buy $350（10/01）；Evercore ISI Buy $380（10/01）；Morgan Stanley Buy $369（09/21），另有一則未標日期的報導稱其降目標至 $360；Goldman Sachs Hold $305（09/30）；Mizuho 目標價升至 $390（由 $335，評等 Neutral，日期不明，可能早於 2026 Q3）；Citigroup 於 7/1 降目標至 $297（評等未明）。
- 評等來源衝突：Barchart 稱 22 家中 16 Strong Buy / 1 Moderate Buy / 5 Hold；Benzinga 稱 14 Buy / 5 Hold，頁面日期為 7/24。以 yf 為準。
- 股價來源衝突：部分頁面顯示約 268，另一頁顯示約 305。本報告不採用任何股價作為現價，需以即時報價核對。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE。WebFetch 依規定不使用，WebSearch 未索引到近期 r/wallstreetbets 或 r/stocks 的 CEG 討論串，僅有一篇 Yahoo 文章提及 Reddit 點名 CEG 為成長股，未說明來源版塊與立場。無法估算聲量或語氣。
- StockTwits：DATA_UNAVAILABLE（未取得 API 資料，搜尋結果無可用的多空標籤比例）。
- X / 新聞聊天：Nasdaq 的 AI 摘要稱討論集中在 Q1 獲利強勁、能源部（DOE）允許一座 760 MW 設施繼續運轉、以及選擇權異常活動。此為彙整文，非原始貼文，且日期不在 10 月。
- 情緒指標（Benzinga，8 月中）：short float 約 3.3%，put/call ratio 約 0.61。
- 2025 年 Benzinga 選擇權流量報告互相矛盾（一則 41% 看多 / 38% 看空，另一則 17% 看多 / 76% 看空），年份已過時，不具參考性。
- 聲量：DATA_UNAVAILABLE（無法與基準比較）。
- 主要話題（由新聞與分析師文章歸納，非社群原文）：PJM 容量市場與政府干預（1 月的緊急批發電力拍賣、州長與白宮對容量價格上限的協議）、天然氣電廠出售給 LS Power（4.4 GW、50 億 USD，DOJ 要求）、2026 年 EPS 指引 11.00–12.00 USD（Q2 後上修至 11.50–12.50，據 Barchart）、核能與資料中心購電合約。
- 語氣：無可靠社群樣本，無法判定 retail 多空。

## Insider activity
統計區間：2026-04-23 至 2026-10-23。
- 公開市場買進：1 筆，Director ROGER W. CRANDALL 於 2026-08-11 買入 1,500 股，約 278.62 USD/股，合計約 0.42 M USD。
- 公開市場賣出：0 筆。
- 非自願性授予（Stock Award/Grant，不屬情緒訊號）：Crandall 2026-08-04 授予 462 股（約 0.12 M USD）；2026-04-28 獨立董事 10 人各獲 556 股（約 305.71 USD/股，每人約 0.17 M USD，合計約 1.70 M USD）。
- 管理層（CEO DOMINGUEZ、CFO EGGERS 等）：區間內無公開市場交易。2026-02 的一批 Officer 交易不在 6 個月內，且 yf 未提供金額。
- 淨額（6 個月）：買進約 0.42 M USD（僅董事一人）；賣出 0；若計入授予則為淨增持（授予非情緒信號，不計入判斷）。
- 持股：insider 持股比例約 0.34%，屬低比例。

## Ownership shifts
- 機構持股：約 82.9%（institutionsPercentHeld 0.829），機構數 2,466 家。
- 季度趨勢：DATA_UNAVAILABLE（yf major_holders 僅提供單一快照，無歷史變化）。

## Net sentiment score
- Analyst 面：偏多（21 buy / 4 hold / 0 sell，平均目標價約 350 USD，高於 10 月初報價）。信心：中高。
- Insider 面：輕度偏多（一名董事在 8 月以約 278.62 USD 公開買進，區間無賣出）。信心：中（樣本只有一筆）。
- Retail 面：DATA_UNAVAILABLE，無可用社群樣本。
- Web 新聞與 chatter：中性（指標混雜，PJM 政策風險與股價跌幅並存，2026 年迄今約跌 10–25%，數據來源不一致）。
- 綜合：**偏多（bullish），信心中等**。主要依據分析師與董事買進；散戶面缺資料，故無法確認是否一致。

Divergence flag: **DATA_UNAVAILABLE**。無法判定 retail 是否與分析師反向，因此不設背離旗標。

## 資料缺口與可靠度
- Reddit、StockTwits：未取得（WebSearch 未索引，WebFetch 規則不允許）。
- 逐筆評等變動、目標價變動明細：yf 未提供，只能靠網路報導，日期與數字不一致。
- 機構持股趨勢：未提供。
- 股價：來源互相矛盾，未採用。
- 金額單位：insider 金額為 USD，以 M USD 標示；本報告未使用億、TWD、KRW。

本報告不含交易建議。

SENTIMENT REPORT COMPLETE
