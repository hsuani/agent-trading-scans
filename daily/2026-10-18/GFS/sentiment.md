# Sentiment — GFS as of 2026-10-18

資料基準：yf 快取（prices/yf/GFS.json，refreshed 2026-10-17 10:33 UTC；live Yahoo 無法連線，屬預期 fallback）。股價參考 46.68（快取 info.currentPrice，2026-10-17）。

## Analyst consensus
23 位分析師（rec_summary 0m）：3 strong buy / 10 buy / 9 hold / 0 sell / 1 strong sell。合計 Buy 類 13、Hold 9、Sell 類 1。yf info：recommendationKey = buy，recommendationMean = 2.04（1 至 5 分制，越低越強）。

目標價（yf info，22 位）：平均 74.68、最高 140.00、最低 51.00。相對股價 46.68，平均目標價隱含約 60% 上行空間，此數字僅反映分析師預期分布，不構成任何交易建議。

近三個月評等分布趨勢（rec_summary -3m 至 0m）：Buy 類由 12 增至 13，Hold 由 9 至 9，Sell 類 1 維持不變，變化幅度小。

近期個別評等變動（WebSearch 聚合站摘要，未經原始來源驗證，請以券商報告為準）：
- Arete 升級至 Buy，目標價 95（聚合站標示 2026-10-06）
- Stifel 重申 Buy，目標價 60（聚合站標示 2026-09-09）
- TD Cowen 維持 Buy，目標價由 85 降至 75（2026-08-06，Benzinga 快照）
- UBS 維持 Neutral，目標價由 61 降至 55（2026-08-06，Benzinga 快照）
- Baird Buy，目標價 140（Google Finance 快照，2026-08）
- Cantor Fitzgerald 由 Neutral 升至 Overweight（2026-05）

各來源平均目標價（時點不一，僅供參考）：Bullstory 76.00（2026-09-21）、Google Finance 74.19、Fintel 79.38（2026-08-28）、Investing.com 80.24、MarketBeat 74.63（評等為 Hold，與多數來源的 Buy 不一致）。

個別評等變動的完整歷史：DATA_UNAVAILABLE（yf recommendations 子指令僅回傳彙總計數，不含逐筆升降評）。

財報脈絡：2026-08-05 Q2 EPS 0.46，優於預估 0.43（+6.5%）。下次財報預估 2026-11-04，預估 EPS 0.51。

## Retail social
- Reddit：WebFetch 直連 r/wallstreetbets、r/stocks 於本沙箱遭封鎖；WebSearch 以 GFS / GlobalFoundries 搜尋 r/wallstreetbets、論壇討論，未找到任何 GFS 相關討論串。DATA_UNAVAILABLE（無討論串樣本、無情緒傾向判讀）。
- StockTwits：API 與 WebSearch 皆未取得 GFS 訊息流，無多空訊息比例。DATA_UNAVAILABLE。
- X / 新聞散戶論述：WebSearch 僅找到聚合站與內容農場頁面（部分標示日期為 2026-04 至 2026-05，且內文與標題不一致），無可信的 2026-10 散戶論述樣本。DATA_UNAVAILABLE。
- 討論量（buzz volume）：DATA_UNAVAILABLE。搜尋索引中未見明顯討論熱度，但此為搜尋覆蓋不足的結果，不能推論為「討論冷清」。
- 散戶傾向：DATA_UNAVAILABLE，無法判定 bullish / bearish / mixed。
- 主題（由新聞與聚合站摘要推得，非散戶原文）：
  - 產能擴張能否獲得需求驗證（Barchart 專文）
  - 相對大型晶圓代工的毛利壓力與景氣循環性
  - 股價自高點回落：快取 52 週高點 92.55、低點 32.02，目前 46.68
  - 放空比例：快取 shortPercentOfFloat 13.57%（Benzinga 8 月快照為 15.0%），偏高，可能成為散戶討論的題材之一

## Insider activity
統計區間：2026-04-18 至 2026-10-18（快取 insider 紀錄，最新交易 2026-09-28）。

- 公開市場買入（Purchase）：0 筆、$0
- 公開市場賣出（Sale）：約 $3.38M，共 47 筆紀錄中的 Sale 部分（已排除 Stock Award 5 筆與 Stock Gift 7 筆，這些非市場交易）
- 依人員分列賣出金額：
  - Michael James Hogan（Officer）：約 $1.31M，9 筆，含 2026-07-09 價位 65.90 至 70.90 區間賣出
  - Samuel Vicari（Officer）：約 $0.66M，1 筆，2026-05-11，價位 75.62
  - Samak L. Azar（Officer）：約 $0.50M，21 筆，多為每次 335 股的規律小額賣出，模式與預定計畫（如 10b5-1）相容，但快取資料無法確認，需以 SEC Form 4 核對
  - Glenda Mary Dorchak（Director）：約 $0.47M，2 筆，價位約 58 左右
  - Pradheepa Raman（Officer）：約 $0.45M，2 筆，2026-08-18 價位 51.12 等
- 董事授予股票（Stock Award）：2026-07-28，多位董事（Rao、Halawa、Obeid、Languille、Antaki），屬例行薪酬，非買入信號。

解讀：6 個月內無內部人公開市場買入，賣出集中在股價 60 至 87 區間的 2026-05 至 2026-07；目前股價已明顯低於這些賣出價位。賣出總額相對公司規模不大，但方向一致偏空。

## Ownership shifts（yf major_holders / inst_holders，13F 報告日 2026-06-30）
- 內部人持股：0.106%
- 機構持股：快取顯示 100.4%（超過 100%，為資料異常，不可直接採用）；機構數 591
- 前十大機構：
  - Mubadala Investment Co：72.82%，持股減少 5.55%（大股東小幅減碼）
  - FMR LLC：12.73%，增加 9.04%
  - JPMorgan Chase：1.23%，增加 33.3%
  - Marshall Wace：0.84%，減少 9.3%
  - T. Rowe Price：0.73%，增加 61.4%
  - Two Sigma：0.62%，增加 0.28%
  - BlackRock：0.58%，增加 2.8%
  - Victory Capital：0.56%，增加 100%
  - Morgan Stanley：0.56%，減少 33.4%
  - Bessemer Group：0.51%，增加 0.22%
- 趨勢：前十大中 7 家增持、3 家減持。持股高度集中於 Mubadala，散戶與中小機構的增減對股價的影響力有限。Mubadala 本季減持幅度雖小，但為最大持股人，值得持續追蹤。

## Net sentiment score
- 分析師面：偏多（13 Buy 類 vs 1 Sell 類，mean 2.04，目標價中位數高於現價）。信心：中。
- 內部人面：偏空（6 個月零買入，約 $3.4M 公開賣出，方向一致）。信心：中。由於 Azar 規律小額賣出可能屬預定計畫，部分偏空訊號的強度應打折。
- 機構面：中性偏多（前十大 7 增 3 減，但最大持股人小幅減碼）。信心：低。
- 散戶面：DATA_UNAVAILABLE。

綜合：**中性**（分析師偏多與內部人偏空相互抵銷，散戶面缺失）。信心：低。

Divergence flag：**無法判定**。散戶 tilt 為 DATA_UNAVAILABLE，無法與分析師偏多做比較。若日後取得可靠的散戶資料，應特別留意「分析師偏多、內部人偏空、散戶若同時偏空」的組合。

## 資料缺口與注意事項
- yf 子指令名稱為 `rec_summary`、`recommendations`、`inst_holders`、`major_holders`，原任務中的 `ratings`、`holders` 不存在，已改用對應指令。
- yf 快取的 major_holders 機構持股比例超過 100%，判定為資料異常，未採用該比例，僅引用個別機構數字。
- Reddit、StockTwits、X 皆無可用的 2026-10 原始樣本，本報告未引用任何散戶原文。
- WebSearch 結果中有多個內容農場鏡像頁面（標題重複、日期錯置），已降低權重，僅採用與 yf 快取或可辨識來源一致的數字。
- 分析師目標價與評等來自多個聚合站，時點與樣本數不同，不應視為單一權威數字。

SENTIMENT REPORT COMPLETE
