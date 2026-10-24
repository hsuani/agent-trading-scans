# Sentiment — SPAI as of 2026-10-24

## Analyst consensus
3 buy / 0 hold / 0 sell（strongBuy 與 strongSell 皆為 0）。rec_summary 與 recommendations 三個時間點（0m、-1m、-2m）數字完全相同，代表過去三個月沒有評級變動，樣本僅約 3 位分析師。

最近評級動作：工具回傳的是分布快照，沒有逐筆升降評等紀錄，因此無法確認近期 upgrade / downgrade。另據 WebSearch 找到的 Benzinga 頁面，平均目標價為 $10，但該頁最新條目日期偏舊、年份不明，且其所載股價 $4.51（10/8）與目標價相比隱含約 2 倍上行空間。這個目標價數字不能視為 2026-10-24 的最新共識，需以 Benzinga 或券商原始報告再次確認。

## Retail social
- Reddit: 本輪依指示未直接抓取 Reddit JSON（任務指定以 WebSearch 處理社群情緒）。WebSearch 也未找到 r/wallstreetbets 或 r/stocks 上以 SPAI 為主題的討論串，代表 Reddit 聲量低或索引不足。
- StockTwits / X: 本輪未直接呼叫 StockTwits API（同上依指示）。WebSearch 找到的 TradingView 社群留言數量少、看法分歧：有人認為軍方展示可能帶來 2026 年合約，也有人預測至少 $7；另有留言描述賣壓出籠。以上為搜尋摘要改寫，非原文引述，且樣本過小。
- 散戶投資平台（Investing.com scoreboard）：有使用者紀錄，6 月的部分看多 call 到 6 月底虧損約 31–36%，7 月一筆 call 獲利約 65%。屬於個別帳戶的事後結果，不代表整體散戶多空比例。
- Benzinga sentiment 頁面：標示空單部位（short interest）約佔流通股 3.9% 且上升，並將其列為看空訊號；同頁亦顯示近 30 天內部人為淨賣方。該頁日期不明，需謹慎使用。
- 聲量（qualitative）：低。搜尋結果中 SPAI 專屬的社群討論很少，多數是新聞或自動生成的價格異動文章，且部分文章在無關網域重複出現，可信度低。

Themes:
1. 軍方／國防合約預期（多數為推測，尚未見確認公告）
2. 股價低位與價格波動大（2026 年初曾單日跌約 7.7%，股價在 $4 上下區間震盪）
3. 內部人出售與空單增加的警示
4. 小型股流動性與籌碼集中風險

Retail tilt: 混合偏空（低信心）。看多論點集中在合約與題材，看空論點集中在賣壓、空單與內部人出售，兩邊都沒有形成主流共識。

## Insider activity
Net 6mo（2026-04-24 至 2026-10-24）: $0 buys, $4.0M sells（以 USD 計，1M 股 × $4.00 ≈ $4.0M，已用股數乘價驗算）。

Notable:
- Daniyel Erdberg（Chief Executive Officer）：2026-09-09 出售 1,000,000 股，每股 $4.00，合計約 $4.0M，為此期間唯一的公開市場交易。
- 其他為無現金對價的股票獎勵或贈與，不計入淨買賣：Brian William Mack（Officer）2026-05-01 獲贈 300,000 股；Jarret Daniel Mathews（Chief Operating Officer）2026-04-01 獲贈 20,000 股（該筆在 6 個月視窗之外，僅供參考）。
- 較早期 CEO 紀錄多為股票贈與或獎勵（2024-11 至 2026-03），非市場買賣。

## Ownership shifts
- 內部人持股：約 45.5%（異常高，代表流通籌碼相對集中，股價受少數人影響大）
- 機構持股：約 12.1%（佔流通股 22.1%），機構數量 31 家
- 趨勢：工具只提供單一時點快照，無法判斷機構增減的方向。

## Net sentiment score
Composite: 中性（信心：低）

分項判讀：
- 分析師：偏多（3 買、0 賣，但樣本僅 3 位且三個月未變動）
- 散戶：混合偏空（聲量低、樣本少、來源可信度不高）
- 內部人：偏空（6 個月內僅有大額賣出，無公開市場買入）
- 空單：偏空（Benzinga 所載 3.9% 且上升，日期待確認）

Divergence flag: 是（部分）。分析師全數看多，而內部人出售與空單上升方向相反，這個落差值得留意。散戶與分析師方向是否相反，因樣本過少無法明確判定，目前僅能說散戶看法分歧。

Data limits:
- 分析師樣本僅 3 位，且 rec_summary 無逐筆紀錄。
- Reddit、StockTwits 本輪未直接取樣。
- Yahoo cookie / crumb 取得失敗（ConnectionError），但 yf 工具仍回傳資料。
- WebSearch 結果多數日期不明或為舊文，未找到 2026-10 的分析師動作或新聞。

來源（WebSearch 結果參考）:
- https://kr.benzinga.com/quote/SPAI/sentiment
- https://www.investing.com/equities/safe-pro-scoreboard
- https://www.tradingview.com/symbols/NASDAQ-SPAI/minds

SENTIMENT REPORT COMPLETE
