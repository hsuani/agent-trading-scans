# Sentiment — 3008.TW (大立光 Largan Precision) as of 2026-10-25

資料說明: yf 價格快照為 6,175 TWD (前收 6,170 TWD)，快照日期未能確認，預期為 2026-10-24 收盤附近。Yahoo cookie/crumb 取得失敗，insider 查詢回傳空陣列，無法視為「無內部人交易」。Reddit 與 StockTwits 無法連線，散戶社群段落為缺口。

## Analyst consensus

單位: 家數; 目標價 TWD

| 項目 | 數值 |
|---|---|
| Strong Buy / Buy | 6 / 9 |
| Hold | 2 |
| Sell / Strong Sell | 3 / 0 |
| 合計 (有效家數) | 20 |
| Mean recommendation (1=Strong Buy, 5=Sell) | 2.1 (對應 buy) |
| 目標價 mean / high / low (TWD) | 7,294 / 11,830 / 3,250 |
| 目標價 mean 相對現價 6,175 TWD | 約 +18% |

Recent moves: 近一個月 (-1m → 0m) 買方家數由 13 增至 15，Hold 由 4 降至 2，Sell 維持 3，屬於少數持有評等上調。3 個月視窗內 Sell 由 2 增至 3。評等歷史 endpoint 回傳與快照相同，無法取得逐筆升降評明細。

從 aggregator 搜尋摘要看到 7 月的個別券商動作 (JPMorgan 升 Buy，目標價 5,000 TWD; Goldman Sachs 維持 Buy，目標價 6,231 TWD; Macquarie Sell，目標價 3,261 TWD)。這些數字來自未驗證的搜尋摘要，日期為 7 月，已可能過時，僅作參考。另一則摘要寫「average price target $4,734」，單位應為 TWD 而非 USD，未採用。

## Retail social

- Reddit: 無法取得。r/wallstreetbets 與 r/stocks 的 search.json 均無法由 WebFetch 連線，無法判斷討論串與情緒。
- StockTwits: 無法取得 (DNS 解析失敗 api.stocktwits.com)。台股在 StockTwits 覆蓋度本來就低，預期影響不大。
- 中文論壇 (非 PTT 直接資料): 搜尋結果中僅找到 CMoney 股市論壇的摘要，語氣偏向短線樂觀、長線看好 EPS 成長，但多數人認為需時間驗證。此為第三方摘要，非原文抽樣，且日期不明。
- X / 新聞鏈: 未找到 2026 年 10 月的散戶或投顧公開意見。可查到的新聞多為 4 月至 8 月，時效不足。
- 聲量 (buzz volume): 無法量化，定性判定為「資料不足」，無法與常態比較。
- Themes (由新聞與論壇摘要歸納):
  - CPO (co-packaged optics) 題材: 4 月股價因 CPO 題材連漲，法說後管理層表示量產需一到兩年，股價隨即回檔。此為市場反覆評估的核心敘事。
  - 獲利動能: 上半年稅後淨利約 NT$107.9 億 (年增約 44%)，第二季營收約 NT$136.7 億 (年增約 17%)。
  - 庫藏股: 2025-12 至 2026-02 執行買回 2,670 張，屬於公司端的正向訊號。
  - 獲利能見度: 投顧與論壇普遍認為估值已反映部分成長，需要後續營收數字驗證。

Quote sample: 無可直接引用的近期原文，本次不引述。

## Insider activity

Net 6mo: 無法確認 (資料缺口)。

- yf insider endpoint 回傳空陣列，但因 Yahoo crumb 取得失敗，此結果不可作為「無交易」的證據。
- 公開資訊觀測站董監申報轉讓的 2026 年資料未能由搜尋取得。
- 搜尋結果中提到林家成員個人持股大幅降低 (創辦人林耀英、董事長林恩舟、執行長林恩平個人持股降至個位數張數或歸零)，但該報導無日期，且林家可能為前幾年的舊聞，不能當作 2026 年趨勢使用。
- Notable (公司層級，非內部人): 2025-12 至 2026-02 公司庫藏股買回 2,670 張，這不是董監交易，需與 insider 資料分開看待。

建議: 補抓 MOPS 董監事持股異動 (近 6 個月) 再判定。

## Ownership shifts

- Insiders held: 28.97%
- Institutions held (占總股本): 28.69%
- Institutions (占流通股): 40.38%
- 機構家數: 227
- 時間序列 (季度變化): yf 僅提供當下快照，無法判斷機構集中度趨勢。不作趨勢結論。

## Net sentiment score

Composite: **bullish (信心: 低)**

- 分析師面 (bullish, 信心中): 20 家中 15 家買方評等 (75%)，平均目標價高於現價約 18%，且近一個月持有評等減少。這是本次唯一可量化的訊號。
- 內部人面 (unknown): 資料缺口，不納入評分。
- 散戶面 (unknown): Reddit 與 StockTwits 不可達，僅有少量第三方摘要，不足以判定。
- 信心偏低的原因: 社群與內部人兩大資料來源缺失，分析師目標價範圍很寬 (3,250 至 11,830 TWD)，且部分券商動作資料來自未驗證的 7 月摘要。

Divergence flag: 無法判定 (no) — 散戶傾向資料不足，無法確認與分析師傾向是否相反。若補到 PTT 或 StockTwits 資料，需要重新評估此欄。

Data gaps to fill next run: Reddit/StockTwits 連線恢復後重抓; MOPS 董監申報轉讓 (近 6 個月); Yahoo crumb 恢復後重跑 insider 與 recommendations 歷史; 2026-10-08 法說 (或最近一次財報) 後的投顧更新。

SENTIMENT REPORT COMPLETE
