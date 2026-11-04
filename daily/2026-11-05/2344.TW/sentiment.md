# Sentiment — 2344.TW (華邦電 Winbond) as of 2026-11-05

> 資料時效註記: 執行日為 2026-11-04, 報告 as-of 日期為 2026-11-05 (次日)。本次可取得的最新資料約到 2026-10 月初。分析師評等快照多為 2026 年 5 至 7 月, 無 2026-11 當期評等。

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 可取得 (Yahoo cookie/crumb 失敗, 仍回傳資料) |
| yf insider | DATA_UNAVAILABLE (回傳空陣列, 疑為 Yahoo 認證失敗, 非確定無內部人交易) |
| yf major_holders | 可取得 |
| Reddit (r/wallstreetbets, r/stocks) | DATA_UNAVAILABLE (sandbox 封鎖 reddit.com) |
| StockTwits | DATA_UNAVAILABLE (api.stocktwits.com DNS 解析失敗, 需於 session 網路設定放行) |
| X / 新聞 WebSearch | 可取得, 但多為 2026 年 5 至 10 月資料 |

## Analyst consensus

**Yahoo (yf rec_summary, 0m 期間):** 8 buy (strongBuy 4 + buy 4) / 0 hold / 0 sell。
**Investing.com 聚合頁 (WebSearch 摘要):** 約 5 buy / 1 hold / 0 sell (6 家), 與 Yahoo 計數不一致, 原因未明 (可能來源不同或時點不同)。
**個別券商:**
- JPMorgan: Buy, 目標價由 NT$255 調升至 NT$360 (2026-07-15 快照); 較早期為 NT$255 (2026-06) 與 NT$140 (2026-01)。
- Morgan Stanley: Hold, 目標價 NT$140 (2026-03-19 下調評等); 另一則 2026-Q1 財報後報導提及 Hold / NT$100。兩者不一致, 需以原始報告為準。
- 本土投顧 (2026-06): Buy, 目標價 NT$234, 預估 2026 EPS 約 NT$23.42。

**趨勢 (yf 近三期):** 0m 8 buy / -1m 8 buy / -2m 7 buy, 0 hold, 0 sell。評等近三個月持續集中於 Buy, 無下調紀錄。

**目標價變動:** 聚合來源顯示 JPM 目標價在 2026 上半年大幅上修 (NT$140 → NT$255 → NT$360)。各聚合站的目標均價差異大 (NT$133 至 NT$245), 且股價快照分歧 (NT$90 至 NT$172), 目標價數字應視為低信心參考。

## Retail social

- **Reddit:** DATA_UNAVAILABLE (封鎖)。
- **StockTwits:** DATA_UNAVAILABLE (DNS 失敗)。
- **X / 中文社群:** CMoney 個股討論區留言分歧, 有人擔心短線風險, 也有人看好後續營運 (樣本少, 僅定性參考)。WebSearch 未取得可量化的提及次數, 聲量水準 DATA_UNAVAILABLE。
- **Themes (從新聞與討論標題歸納):**
  - 利基型記憶體 (specialty DRAM, SLC NAND, NOR Flash) 供給收縮, 報價上漲
  - 2026 Q3 中小型 DRAM / SLC NAND 價格估計季增 40% 至 50%; Q4 傳統 DRAM 預估續漲 10% 至 15%
  - 產能被長約鎖定 (LTA 延伸至 2030 年的說法)
  - 2026-09 單月營收創新高, 連續第 10 個月創高 (Digitimes 報導)
  - Samsung 傳 2027 年起採購華邦電 DRAM (Digitimes 報導, 未經公司證實)
  - 循環股風險: 獲利高峰時法人可能給較低 P/E, 是常見的反向論點

## Insider activity

Net 6mo: DATA_UNAVAILABLE (yf insider 回傳空陣列, 無法確認是否為真實零交易)。
Notable: DATA_UNAVAILABLE。

## Ownership

- 內部人持股 (insidersPercentHeld): 30.26%
- 機構持股 (institutionsPercentHeld): 27.44%; 流通股中機構持股 (institutionsFloatPercentHeld): 39.34%
- 機構家數 (institutionsCount): 215
- 歷史趨勢: DATA_UNAVAILABLE (單一快照, 無時間序列)。

## Net sentiment score

**Composite: bullish (信心: 中低)**

依據:
- 分析師面: 高度偏多 (Yahoo 8 buy / 0 sell; 近三期無下調)。
- 新聞與營運面: 偏多 (營收連創新高, 價格報導持續上修)。
- 散戶面: 無量化資料, 中文社群分歧, 不計入評分。
- 估值與循環股風險: 法人已提醒循環股獲利高峰時 P/E 會被壓縮, 屬於反向風險。

信心受限於: 散戶與 insider 資料缺失、分析師目標價來源分歧大、無 2026-10 之後的評等與股價快照。

**Divergence flag: no (暫不成立)**
散戶面資料缺失, 無法判斷散戶傾向是否與分析師相反。若日後 StockTwits 或 Reddit 可取得, 需重新檢查。

## 限制與待補項目

1. 放行 api.stocktwits.com 後重跑 StockTwits 段落。
2. Reddit 來源需在可連線環境補抓。
3. yf insider 需於 Yahoo 認證正常時重跑, 確認 6 個月內 CEO / CFO 買賣。
4. 2026-11 當期的券商評等與目標價未取得, 需以 Bloomberg, MarketScreener 或 TWSE 資料核對。

SENTIMENT REPORT COMPLETE
