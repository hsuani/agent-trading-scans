# Sentiment — SPAI as of 2026-10-22

## Analyst consensus
3 buy / 0 hold / 0 sell（strong_buy 0 家；近 3 個月分布維持不變）。
目標價（yfinance info 快取，2026-10-22 11:41 UTC 更新）：平均 $10.67、最高 $13.00、最低 $9.00。以快取現價 $3.32 計算，平均目標價隱含約 +221% 上漲空間，落差極大，需視為覆蓋樣本過少（僅 3 家）的訊號，而非可直接採信的估值。
近期調整：recommendations 歷史僅回傳彙總計數，未見個別升評或降評事件；無法確認 3 個月內的 target 變動方向。

## Retail social
- Reddit（r/wallstreetbets、r/stocks、r/pennystocks）：DATA_UNAVAILABLE。WebSearch 未找到任何 SPAI 相關的 Reddit 討論串，無法取得樣本或 tilt。
- StockTwits / X：DATA_UNAVAILABLE。StockTwits 符號頁未被索引；WebSearch 只找到 Benzinga 情緒頁與 Investing.com 用戶 call 紀錄（5 月至 9 月，無 10 月資料）。Investing.com 的 call 紀錄條目混合，數個近期 call 顯示大幅虧損，但頁面稀疏且含垃圾留言，僅供參考。
- 聲量（buzz volume）：無法量化，無法與平時比較。
- 間接訊號：Benzinga 情緒頁（最後更新 10/8）標示空頭部位 3.9% of float 且「rising」；快取資料顯示 shortPercentOfFloat 3.63%，兩者日期不同，方向可能一致但數值未對齊。
- 主題（可得來源）：無可靠的散戶主題可歸納。TipRanks 的 "Very Positive" 標籤來自機構/模擬組合，不代表散戶。
- 散戶傾向判定：無法判定（資料不足）。

## Insider activity
Net 6mo（2026-04-22 至 2026-10-22）：約 $4.0M 賣出，$0 買入。
- 主要交易：CEO Daniyel Erdberg 於 2026-09-09 以 $4.00/股賣出 1,000,000 股（約 $4.0M，直接持有 D）。
- 其他 6mo 內交易為獎勵授予（非市場交易）：Brian William Mack（Officer）2026-05-01 授予 300,000 股；Jarret Daniel Mathews（COO）2026-04-01 授予 20,000 股，但 4/1 落在 6mo 視窗外，僅作背景。
- 6mo 外的其他紀錄多為獎勵或贈與（CEO 2025-12-23、2026-03-06 贈與；CFO 2025-08-22 與獨立董事 2025-08-22 獎勵），無公開市場買入。
- 注意：CEO 賣出價 $4.00 高於快取現價 $3.32，賣出後股價有回落。這是單一大額賣出，樣本少，不能推論為全面看空；但 CEO 單次公開市場賣出與分析師全數買進形成對比。
- 持股結構：insidersPercentHeld 45.5%，屬高度內部人持股。

## Ownership shifts
- institutionsPercentHeld 12.1%，institutionsCount 31（截至 2026-06-30，13F 資料）。
- 主要持有人變動（季度）：Vanguard Capital Management 563,837 股（2.77%，+24.5%）；Jane Street 139,551 股（+100%，但基數小）；Tudor Investment 129,459 股（-42.6%）；Geode 147,046 股（-2.0%）；Cresset、Perkins、Thompson Siegel & Walmsley 持平或小幅變動。
- 趨勢判讀：增減互見，淨變動不明顯，缺乏一致的機構加碼或撤退訊號。資料為 6/30 季報，已超過 3 個月。

## Net sentiment score
Composite: **neutral（信心：低）**
- 分析師面：偏多（3/3 buy，目標價遠高於現價）。
- 內部人面：偏空（CEO 單次 $4.0M 公開市場賣出；其餘為獎勵）。
- 機構面：中性（12% 持股，淨變動混合）。
- 散戶面：無資料，無法納入評分。
- 因散戶與社群資料全數缺失，綜合評分只有分析師與內部人兩項訊號，且兩者方向相反，信心偏低。

Divergence flag: **部分分歧（yes，但以可得資料論，屬分析師與內部人之間）**。
- 分析師全數 buy 與 CEO 大額賣出方向相反，此分歧值得在後續決策中留意。
- 散戶 vs 分析師的分歧無法判定（散戶資料缺失）。

## Data gaps and source notes
- yfinance 即時 API 因代理拒絕連線（fc.yahoo.com、query2.finance.yahoo.com、guce.yahoo.com）失敗，本報告使用 repo 快取 prices/yf/SPAI.json（refreshed 2026-10-22T11:41 UTC，misses 為空）。
- 價格來源不一致：快取現價 $3.32；Benzinga 搜尋結果顯示 10/2 報價約 $4.56。兩者日期不同，本報告以快取為準。
- Reddit、StockTwits、X 皆 DATA_UNAVAILABLE；WebSearch 結果以 Benzinga、Investing.com、TipRanks、equibles.com 為主，部分為自動生成或重複鏡像內容，已排除使用。
- 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
