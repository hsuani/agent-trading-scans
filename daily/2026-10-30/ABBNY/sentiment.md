# Sentiment — ABBNY (ABB Ltd ADR) as of 2026-10-30

> 資料可信度注意: 本日為 2026-10-30 的 as-of 報告, 但執行當下系統日期為 2026-10-29, 部分價格與評等資料最新僅到 2026-10-16 左右。Reddit 與 StockTwits 無法取得 (見下文), 社群情緒部分為低信心。

## Analyst consensus

| 來源 | Buy | Hold | Sell | 平均目標價 | 備註 |
|---|---|---|---|---|---|
| yf `rec_summary` (0m) | 0 (Strong Buy 0) | 5 | 0 (Strong Sell 1) | 未提供 | 共 6 席, 與網路來源家數不一致 |
| Walnut Invest (2026-10 更新) | 0 | 3 | 2 | 約 USD 93.32 (區間 83–101) | 5 家分析師 |
| StockAnalysis | — | — | — | USD 92.6 | 平均評等 Hold, 5 家 |
| MarketBeat (疑似過時) | 2 | 10 | 1 | USD 58.00 | 資料可能停留在舊期間, 不採信 |

整體結論: 5–6 家分析師以 Hold 為主, 買賣方向幾乎無共識分歧。yf 近 4 個月趨勢顯示 Strong Sell 由 2 家降為 1 家 (期間 -3m 至 0m), Hold 由 3 家增至 5 家, 可解讀為賣方評等減少、中性評等增加, 即整體評等由偏空轉向中性。

近期評等變動 (以瑞士股 CHF 目標價為準, ADR 目標價為 USD 換算, 不可直接比較):
- RBC Capital: 目標價由 CHF 81 調升至 CHF 83, 維持 Sector Perform (中性)。
- Pareto: 由 Hold 升為 Buy, 目標價 CHF 96.40 (分析師 Anders Roslund)。
- Barclays: 重新給予覆蓋, Equal Weight (中性), 目標價 CHF 76。

目標價與股價關係: Walnut 報 ABBNY 最後收盤約 USD 91.05 (2026-10-16), 平均目標價 USD 93.32 略高於股價約 2.5%; StockAnalysis 則顯示平均目標價低於股價約 8%。兩者差異源於收盤時點與樣本家數不同。

## Retail social

- Reddit: **無法取得資料**。r/wallstreetbets 與 r/stocks 的 public JSON 端點回傳 WebFetch 錯誤 ("unable to fetch from www.reddit.com"), 故無貼文樣本與情緒比例。WebSearch 亦未找到 ABBNY 相關 Reddit 討論串。
- StockTwits: **無法取得資料**。api.stocktwits.com DNS 解析失敗 (ENOTFOUND), 疑似不在本 session 允許網域內, 需在 session 網路設定中允許後再重試。
- X / 新聞與部落格聲量:
  - TipRanks 統計 6 則部落格觀點, 66% 看多, 來源皆為 Seeking Alpha。樣本小, 且為專業寫手而非散戶。
  - Nordnet 論壇有散戶留言, 一方認為估值過高, 另一方自稱長期持有者; 留言日期不明, 不宜作為當前情緒依據。
  - 聲量量化: 無可靠 mention 計數。以 ADR 流動性偏低 (yf 顯示機構持股比例資料異常, 見下) 判斷, 散戶討論量屬低檔推估, 信心低。
- 主要主題 (依可取得之新聞與論壇):
  1. 估值: 本益比中段 30 倍以上 (Walnut 指 P/E 介於 30 出頭), 另 Simply Wall St DCF 估計高估約 26.1%, 多頭與空方爭論集中於此。
  2. 訂單與業績: Q2 2026 訂單額創紀錄達 USD 12.04B, 年增約 30%; TipRanks 稱法說語氣正面, 但 EPS USD 0.66 低於其列出之預期值。
  3. 併購: 收購 Rotork 之金額報導不一 (USD 5.5B 與 5.6B 兩種), 市場對併購整合與槓桿的疑慮待確認。
  4. 股價波動: 2026 年 6 月 22 日創 CHF 89.14 歷史高點後, 五週內最多回檔約 15%; 52 週區間 USD 67.56–109.73。
  5. AI 相關股價拋售 (德文新聞標題 "Kurs fällt im KI-Abverkauf"), 顯示股價受 AI 題材情緒影響。

- 代表性敘述 (引述 ≤15 字, 來源為新聞與部落格標題, 非散戶 Reddit 貼文): 「abb heading into fall with momentum」(payoff.ch 標題)。

## Insider activity

Net 6mo: 資料不足, 無法可靠計算淨買賣金額。
- yf `insider` 回傳空陣列, 不能判定為零交易 (可能是資料源缺漏)。
- 網路來源 (insiderscreener, 瑞士 SIX 申報) 顯示:
  - 2026-02-12: 董事長 (Chairman) 賣出 30,000 股, 單價約 CHF 70.25。
  - 2026-05-04 (5/6 申報): 數名董事會成員買進, 包括董事長買進 22,283 股, 其他成員小額買進, 單價約 CHF 78.42。
- 資料品質警告: 同一來源的部分成交價 (CHF 466.22、288.65) 與當時股價 (約 CHF 78–81) 明顯不符, 金額與股數不可信。若以 CHF 78.42 為單價, 董事長 22,283 股約合 CHF 1.75M, 約 USD 2.0M; 但此為推算值, 需對照 SIX 或 6-K 原始申報確認。
- 粗估傾向: 2026 年 6 個月內董事會層級以買進為主 (5 月), 並有一筆董事長賣出 (2 月), 整體內部人情緒為中性偏多, 信心低。
- 最近買賣人: 董事長 (Chairman) 兩筆; 其他董事小額買進。執行長與財務長之交易資料未取得。

## Ownership shifts

- yf `major_holders`: institutionsPercentHeld 0.2% (值明顯異常, 與 ABB 實際機構持股率遠高於此不符, 應視為資料源錯誤), institutionsCount 88 家, insidersPercentHeld 0.0。
- 機構持股趨勢: 無可靠時間序列, 無法判斷集中度變化方向。
- 建議: 以 SEC 13F 或 SIX 股東名冊另行驗證。

## Net sentiment score

**Composite: neutral (信心: 低)**

- 分析師面: 中性 (Hold 為主, 近 3–4 個月 Sell 減少, Buy 1 家 (Pareto) 新增)。
- 部落格面: 偏多 (66% 看多, 樣本僅 6 則)。
- 散戶面: 無法量化 (Reddit、StockTwits 失敗; 論壇留言零碎)。
- 內部人面: 中性偏多 (董事會 5 月買進, 2 月董事長賣出; 金額資料不可信)。
- 價格位置: 股價接近分析師平均目標價 (約 USD 91 vs 目標 USD 92.6–93.3), 上行空間有限, 與估值爭論一致。

**Divergence flag: 無法判定 (no-data)**。散戶端資料缺失, 無法確認散戶傾向是否與分析師 (中性) 反向。若之後取得 Reddit 或 StockTwits 資料, 再重新評估。

## 資料來源與限制

- yf `recommendations` / `rec_summary` / `insider` / `major_holders` 均印出 Yahoo cookie/crumb 連線失敗, 但仍回傳資料; 其中 insider 為空、major_holders 數值異常, 須謹慎使用。
- WebSearch 來源: [MarketBeat ABBNY forecast](https://www.marketbeat.com/stocks/OTCMKTS/ABBNY/forecast/), [Walnut Invest ABBNY forecast](https://walnutinvest.com/stocks/abbny/forecast), [StockAnalysis ABBNY](https://stockanalysis.com/quote/otc/ABBNY/), [TipRanks ABBNY](https://www.tipranks.com/stocks/abbny), [Simply Wall St narrative](https://www.simplywall.st/narratives/fqlz0u7x-global-protectionism-and-rising-cost-burdens-will-erode-margins), [boerse-express ABB](https://www.boerse-express.com/news/articles/abb-aktie-261-ueberbewertung-laut-simply-wall-st-931602), [payoff.ch](https://www.payoff.ch/en/news/abb-heading-into-fall-with-momentum), [insiderscreener ABB](https://www.insiderscreener.com/en/company/abb-ltd)
- 失敗來源: Reddit (www.reddit.com 無法存取)、StockTwits (api.stocktwits.com DNS 失敗)。

SENTIMENT REPORT COMPLETE
