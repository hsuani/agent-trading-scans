# Sentiment — 6830.TW (汎銓) as of 2026-10-11

資料完整度警示：本次 yfinance 的 cookie/crumb 取得失敗（ConnectionError），Reddit 與 StockTwits 皆無法連線，且 2026年10月的網路資料搜尋不到。以下結論信心偏低，僅供參考。

## Analyst consensus
目前 rec_summary 顯示 1 buy（strongBuy）/ 0 hold / 0 sell，覆蓋家數僅 1 家，樣本不足以代表市場共識。
- 歷史評等變動（recommendations）：DATA_UNAVAILABLE（回傳為空）
- 目標價變動：DATA_UNAVAILABLE
- 搜尋線索：CMoney 投資快訊有一篇「半導體檢測分析業務受惠，研究報告維持增持評等」的文章，但發布日期與券商來源無法確認，不納入計分。
- 2024年7月 CMoney 報告曾維持「增加持股」、目標價220元，屬於兩年前的舊資料，不採用。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（403 / 連線被拒）
- StockTwits：DATA_UNAVAILABLE（DNS 解析失敗，api.stocktwits.com 無法連線）
- X / 新聞與論壇（WebSearch）：
  - CMoney 股市爆料同學會（6830 討論區）意見分歧。多頭留言如「站穩月線再買不錯嗎」；空方留言提到賣壓與約3,000張的大宗成交。另一則留言引用「外資又買了6830 337張」，顯示外資有買超。發文日期皆未標示，無法對應到特定時段。
  - 量能：DATA_UNAVAILABLE（無提及次數統計，無法與歷史基準比較）
- 價格與籌碼背景（非社群，僅作脈絡）：
  - 2026/07/21 約346.5元；2026/08初約380.5元，histock 記載今年以來漲幅約112.6%，自今年高點回落約62%。
  - 2026/09/18 收盤563元，單日上漲約9.96%，成交金額約13.8億元。
  - 2026/07/29 融資使用率約30%，融資餘額連6日增加。
  - 2026年10月的股價與籌碼資料：DATA_UNAVAILABLE

- Themes（從可取得的搜尋摘要歸納）：
  1. 半導體檢測業務受惠題材（研究報告與論壇共同提及）
  2. 月營收創單月歷史新高（2026年8月營收約2.54億元）與 2026Q2 EPS 季減約157%，獲利動能與營收動能呈現落差
  3. 高檔震盪與賣壓 vs. 外資回補的多空拉鋸
  4. 融資餘額增加，短線籌碼偏熱

- Retail tilt：mixed（偏多但分歧，信心低）

## Insider activity
Net 6mo：DATA_UNAVAILABLE（insider 查詢回傳為空清單，且 cookie 失敗期間資料可能不完整，不能視為「無內部人交易」）。
Notable：DATA_UNAVAILABLE

## Ownership shifts
- 內部人持股比例：約 21.3%
- 機構持股比例：約 6.85%（流通股口徑約 8.7%）
- 機構家數：9
- 外資持股趨勢：玩股網記載 2026/06/26 外資持股約 7.63%，高於2026年4月約 5% 左右的水準，呈回升。但此為搜尋摘要，未能以原始資料核實。
- 時間序列集中度變化：DATA_UNAVAILABLE（yfinance 只回傳單一快照）

## Net sentiment score
Composite：**neutral**（信心：**低**）
- 分析師面：樣本僅 1 家且全為買進，偏多，但覆蓋不足，權重低。
- 散戶面：論壇意見分歧，偏多與偏空並存；Reddit / StockTwits 缺資料。
- 籌碼面：外資有回補跡象、內部人持股高（21%），但 insider 交易明細缺失，無法判定近期內部人買賣方向。
- 基本面訊號：營收創高與 EPS 季減並存，正負訊號互相抵消。

Divergence flag：**no（資料不足，無法判定）**
分析師（僅 1 家，偏多）與散戶（分歧，略偏多）方向大致一致，但兩邊樣本都薄弱，不能據此判定背離是否有資訊價值。

## 資料缺口清單
| 項目 | 狀態 |
|---|---|
| 分析師歷史評等 / 目標價變動 | DATA_UNAVAILABLE |
| Reddit（r/wallstreetbets、r/stocks） | DATA_UNAVAILABLE（403 / 連線被拒） |
| StockTwits | DATA_UNAVAILABLE（DNS 失敗） |
| 社群提及量基準 | DATA_UNAVAILABLE |
| Insider 6個月買賣明細 | DATA_UNAVAILABLE |
| 機構持股時間序列 | DATA_UNAVAILABLE |
| 2026年10月股價與籌碼 | DATA_UNAVAILABLE（最新資料為2026/09/18） |

SENTIMENT REPORT COMPLETE
