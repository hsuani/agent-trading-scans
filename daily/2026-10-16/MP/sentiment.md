# Sentiment — MP as of 2026-10-16

> 資料時點說明：分析師評等為 yfinance 當前快照；新聞與價格資料最新至 2026-10-13。Reddit 與 StockTwits 無法取得（見下方），散戶情緒部分為缺口。

## Analyst consensus
yfinance 目前分布：5 strong buy / 13 buy / 1 hold / 0 sell / 0 strong sell（共 19 家）。近四個月無 sell 評等，hold 由 0 增至 1（約 2026-09 初，與 Freedom Broker 以 hold 首次覆蓋 9/16 時點相符，屬推論）。

- 近期動作（新聞來源，未全數經 yfinance 驗證）：
  - Robert W. Baird 10/1 將目標價由 $80 下調至 $65，維持 outperform。
  - Zacks Research 8/26 由 hold 降至 strong sell（Zacks 通常不計入 yfinance 的券商家數，屬量化評級，需分開看待）。
  - Freedom Broker 9/16 首次覆蓋，hold，目標價 $57。
  - 7 月下旬：JPMorgan 目標價 $75 → $60（overweight）；Needham $81 → $73（buy）；Barclays $69 → $65（overweight）。
  - 一則 TipRanks 標題顯示 Morgan Stanley 由 overweight 降至 equal weight，但搜尋結果未提供日期，無法確認時點，暫不計入。
- 目標價趨勢：平均目標價由 7 月底 $78.35（MarketBeat）、8 月底 $78.28（Fintel）下滑至 10 月約 $75（MarketBeat 自動快訊）。目標價區間 7 月時為 $60–$100。方向為逐步下修，但仍遠高於現價。
- 股價背景：10/12 下跌約 6% 至約 $43，10/13 再跌 1.9% 至約 $42.52，兩者皆低於 50 日與 200 日均線（來源：MarketBeat 快訊搜尋摘要）。

## Retail social
- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 search.json 經 proxy 回傳 403（CONNECT tunnel failed），WebFetch 亦被拒。依規定 soft-fail，未取樣任何貼文，無法給出提及量或多空傾向。
- StockTwits / X：StockTwits API 無法解析網域（ENOTFOUND），無法取得訊息流與 Bullish/Bearish 標籤。X 端僅能從新聞側推估。
- 新聞與論壇側的替代觀察（非散戶直接發言，僅作代理）：WebSearch 未找到任何 Reddit 或 WSB 討論串，故無法判斷散戶熱度相對於基準是高是低，只能定性為「無法量化」。
- 主題（由新聞標題歸納，非散戶原文）：
  - 美國政府持股與國防需求（DoD 2025 年 7 月 $400M 股權投入，政府為最大股東）。
  - 中國稀土出口管制與貿易緊張帶動的政策題材，以及 Defense Production Act 相關資金傳聞。
  - 營收成長與獲利能力：Q 營收 $108.49M，年增 89% 且高於預期，但仍未獲利。
  - 股價自 2025 年 5 月低點漲逾 310% 至 10 月高點後回檔，波動仍大（IV 約 68%，8 月資料）。
- 散戶多空傾向：**無法判定**（資料缺口）。

## Insider activity
yfinance `insider` 回傳空陣列。注意：同時段 Yahoo cookie/crumb 取得失敗，此空值可能是資料缺漏而非實際零交易，**不可直接解讀為無內部人交易**。
- 淨 6 個月：無法計算（$0 買入 / $0 賣出 為未驗證數值，需以 SEC Form 4 核對）。
- 持股結構：內部人持股 19.6%（yfinance major_holders），其中美國政府持股屬非典型內部人，不在一般 Form 4 買賣的解讀框架內，不應與一般高管交易混為一談。

## Ownership shifts
- 機構持股 78.4%（流通股占比 97.6%），機構數 974 家。
- 這僅為單一時點快照，無法判斷機構集中度的趨勢方向，需比較前期 13F 資料後才能得出結論。
- 空頭部位：Fintel 8 月快照 short float 20.24%，屬高空單比例，但資料已逾兩個月，時效性不足。

## Net sentiment score
- 分析師面：**偏多**（信心：中高）。19 家中 18 家為買進或強力買進，0 家賣出，但目標價連續下修，且 Zacks 量化評級為 strong sell，分歧存在。
- 散戶面：**無法判定**（信心：低）。Reddit、StockTwits 皆不可取得，僅有新聞標題作為代理，無法作為情緒量化依據。
- 內部人面：**無法判定**（信心：低）。資料為空，且無法確認是否為真實零交易。
- 綜合：**中性偏多，信心低**。分析師評等仍偏多，但股價在評等與目標價下修的背景下持續走弱，市場情緒未能與分析師共振。這是以新聞代理與分析師面為主的判讀，不是完整的散戶情緒量測。

Divergence flag: **無法判定**。因缺乏可靠的散戶多空資料，無法檢驗散戶與分析師傾向是否相反。若後續取得 Reddit 或 StockTwits 資料，應優先比對這一點。

## 資料缺口與後續建議
1. Reddit（r/wallstreetbets、r/stocks）：403，需從其他網路路徑或授權來源取得。
2. StockTwits：域名無法解析，需確認可用端點。
3. 內部人交易：yfinance 回傳空值，建議以 SEC EDGAR Form 4 直接核對過去 6 個月。
4. 分析師評等：yfinance 與 MarketBeat/Zacks 的家數與分類不同，建議以單一來源為準並註明口徑。
5. 機構持股趨勢：需補抓前兩季 13F 比較。

SENTIMENT REPORT COMPLETE
