# Sentiment — 3661.TW (世芯-KY) as of 2026-10-12

## 資料來源狀態
- `pipeline/tools/yf` live feed 失敗（fc.yahoo.com cookie/crumb 連線錯誤），改用 repo cache `prices/yf/3661.TW.json`（_refreshed_at 2026-10-12T00:46 UTC）。
- `recommendations` 指令只回傳彙總家數，沒有個別評等變動歷史，無法列出 upgrade/downgrade 明細。
- `insider` 回傳空陣列；`inst_holders` 也是空的。
- Reddit、StockTwits 依規定未直接抓取；WebSearch 找不到 r/wallstreetbets 或 r/stocks 的相關討論串（無樣本可引用）。
- 2026-10 的 PTT / CMoney 討論也找不到，搜尋到的最新社群內容約為 2026-08。

## Analyst consensus
目前 16 位分析師：**6 strong buy / 9 buy / 1 hold / 0 sell**（recommendationKey: strong_buy，recommendationMean 1.5）。
3 個月前為 6 / 8 / 1 / 0 / 0，買進家數多 1 家，其餘不變。

目標價（cache info）：平均 NT$5,803.25，中位數 NT$5,944，最高 NT$6,800，最低 NT$3,755。
cache 股價：現價 NT$4,345，前收 NT$4,190，52 週高 NT$5,640（2026-05 創高）、低 NT$2,480。

近期動向（WebSearch，日期不一，需留意）：
- 5 月法說後，多家外資調高目標價至 NT$6,000 起跳，最高 NT$6,215，美系外資維持加碼。
- 較早期的下修：里昂因理想汽車專案進度放慢降至 NT$4,500，花旗降至 NT$4,200；大摩重申「優於大盤」，目標價 NT$4,388（8 月資料）。
- 這些下修與 cache 的目標價中位數（約 NT$5,944）有明顯落差，代表 cache 中的目標價可能包含 5 月後的新報告，而下修事件發生時點不同。無法確認哪一組是最新值。

## Retail social
- **Reddit**：無可用樣本，搜尋無結果。
- **StockTwits / X**：StockTwits 依規定未抓取。X 上沒有可靠的近期樣本。
- **PTT / CMoney（WebSearch 間接結果）**：CMoney 股市社群分歧。有人擔心融資壓力拖累股價；也有人認為世芯是長線 AI 晶片供應鏈核心。來源摘要未附引言，無法做 ≤15 字的直接引用。
- **聲量**：無可量化的提及數，無法與常態比較，記為「無法判定」。

主要話題（來自新聞與社群摘要，非直接抓取）：
- 3 奈米 AI 加速器放量，以及 2 奈米專案。
- AWS 以外的 CSP 專案（例如 Meta）是否能取得，被視為催化劑。
- 客戶集中風險與 2026 年產能受限。
- 融資與資金面波動。
- 估值（Simply Wall St DCF 認為低於現價；trailingPE 約 63，forwardPE 約 23）。
- 高波動（beta 約 2.11，週均波動約 9.6–10%）。

## Operating / capital datapoints（影響情緒的客觀事件）
- nStock：2026-08 月營收約 NT$87.76 億，月增 18.07%，年增 273.61%，為歷史單月新高；但 1–6 月累計仍年減 39.74%。
- 2026-08-20 公布的 Q2 EPS 為 18.72，低於預估 19.64（落後 4.7%）。
- 下次財報 2026-11-04，EPS 預估 47.14。
- 2026-06 完成 US$510MM GDS 發行，約 10 倍超額認購；Q2 自由現金流為 -48.6 億元（cache quarterly_cf）。

## Insider activity
Net 6mo：**無資料**（yf insider 回傳空陣列，cache 也為空）。內部人持股 3.14%。無法判定 CEO/CFO 是否買賣。

## Ownership shifts
- 機構持股 39.25%（float 內 40.53%），機構家數 260。
- cache 內沒有時間序列，無法判定集中度趨勢。

## Net sentiment score
- **分析師端：偏多**（信心：中）。16 家中 15 家為買進，目標價中位數高於現價；但評等歷史只到彙總家數，且 WebSearch 顯示部分下修在 8 月前後，時間上不一致。
- **散戶端：無法可靠判定**（信心：低）。Reddit/StockTwits 無資料，PTT/CMoney 只有 8 月前的摘要，且內容分歧。
- **綜合：偏多，信心低。** 主要依據為分析師共識與營運動能；散戶面缺口大。
- **Divergence flag：無法判定**。散戶 tilt 缺乏當期資料，無法比較是否與分析師方向相反。

## 資料缺口與不一致
1. 多個網站的股價快照不一致（WebSearch 範圍約 NT$3,060–4,105），以 cache 的 NT$4,345 為準，但需以即時報價確認。
2. 目標價摘要與 cache 數據時間點不同，無法確定最新版本。
3. 內部人交易、機構持股趨勢、Reddit/StockTwits 樣本全部缺失。
4. 本報告不含交易建議。

## Sources
- [世芯-KY 目標價與股價（udn）](https://money.udn.com/money/amp/story/5607/9396125)
- [鉅亨網 世芯-KY 報導](https://news.cnyes.com/news/id/5545938)
- [China Times 世芯 2026-03](https://wantrich.chinatimes.com/news/20260306900510-420101)
- [China Times 世芯 2026-05](https://wantrich.chinatimes.com/news/20260511900206-420101)
- [nStock 世芯-KY 營收資料](https://www.nstock.tw/世芯-KY做什麼.html)
- [CMoney 3661 社群](https://www.cmoney.tw/follow/channel/stock-3661)
- [自由財經 焦點股 世芯 法說展望](https://ec.ltn.com.tw/article/breakingnews/5432569)
- [MONEY LINK 3661 新聞](https://ww2.money-link.com.tw/TWStock/StockNews.aspx?SymId=3661)
- [Simply Wall St 3661 估值](https://www.simplywall.st//stocks/tw/semiconductors/twse-3661/alchip-technologies-shares/valuation)
- [TradingView TWSE 3661](https://www.tradingview.com/symbols/TWSE-3661/)
- [Investing.com 3661 共識預估](https://il.investing.com/equities/alchip-technologies-ltd-consensus-estimates)
- [GlobeNewswire 美元 GDS 發行公告 (2026-06-26)](https://www.globenewswire.com/de/news-release/2026/06/26/3318020/0/en/Alchip-Successfully-Completes-US-510MM-GDS-Offering.html)

SENTIMENT REPORT COMPLETE
