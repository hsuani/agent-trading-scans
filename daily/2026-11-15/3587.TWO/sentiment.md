# Sentiment — 3587.TWO (閎康) as of 2026-11-15

注意：本次所有來源的可取得資料多半停在 2026 年 7 月，2026 年 11 月的實際討論與評等皆未能確認，信心偏低。

## 資料可得性總覽

| 來源 | 狀態 |
|---|---|
| pipeline/tools/yf recommendations / rec_summary | 回傳空值（Yahoo cookie/crumb 取得失敗） |
| pipeline/tools/yf insider | 回傳空值 |
| pipeline/tools/yf major_holders | 有資料（見下方持股段） |
| Reddit r/stocks 搜尋 | 被拒絕存取（WebFetch 無法連線 reddit.com），略過 |
| Reddit r/wallstreetbets 搜尋 | 未嘗試（同一網域已被拒絕） |
| StockTwits | DNS 解析失敗（api.stocktwits.com 不在允許網域內），略過 |
| WebSearch 新聞/論壇 | 有部分資料，多為 2025 至 2026 年中 |
| PTT / CMoney 股市討論 | 搜尋快照未見 2026 年 11 月的討論內容 |

若要完整零售情緒，需於工作階段網路設定允許 reddit.com 與 api.stocktwits.com。

## Analyst consensus

- 數量：Investing.com 彙整為 3 buy / 0 hold / 0 sell，平均目標價 365.67 TWD（最高 450、最低 300）。快照時間不明，推估為 2026 年中，與 2026-11-15 有明顯落差。
- FactSet 調查（鉅亨速報，時間不明）：6 位分析師，積極 5 位、中立 1 位。中位目標價由 264 下修至 250 TWD（約 -5.3%），最高 320、最低 210 TWD。
- 歷史：CMoney 2025-03-04 報導，因擴廠折舊下修 2024 與 2025 年 EPS，目標價調整至 290 至 340 TWD；CMoney 2024-06-28 有券商買進、目標價 310 TWD。
- 評述：多數券商維持買進，但 Investing 平均目標價（約 366）與 FactSet 中位數（250）差距大，顯示樣本、日期與口徑不一致，不宜直接相加平均。

## Retail social

- Reddit：無法取得（見上表）。
- StockTwits / X：StockTwits 無法連線。X 未具體檢索到 2026 年 11 月的貼文。
- 論壇：CMoney 股市討論頁搜尋快照未見實質留言；PTT 未取得。
- 聲量：無法量化，無法與平時基準比較。
- 主題（僅能從新聞與基本面資料推論，非零售原文）：
  - 營收動能：2026 年 6 月單月營收 5.58 億 TWD，年增 11.01%，為歷史單月新高；成長來自先進製程的材料分析（MA）與故障分析（FA）需求。
  - 獲利效率：2026Q1 EPS 2.24 TWD，年增 194.74%；但 ROE 僅 3%。
  - 估值：本益比約 38.5 倍，股價淨值比 3.06，低於產業平均 8.39（同一來源口徑，需留意）。
  - 日本布局：熊本、名古屋、北海道等實驗室，為常見正面敘事。
  - 折舊壓力：擴廠折舊拖累 EPS，為分析師下修的主因之一。
- 零售傾向：無法判定（樣本缺失）。

## Insider activity

- 6 個月淨買賣：無法取得（yf insider 空值，且未找到 2026 年個別董監申報明細）。
- 董監持股比例：2026 年 5 月下旬 20.21%，7 月 3 日 20.08%，變動約 -0.13 個百分點，幅度小。
- 治理事件：董事改選日為 2026-06-18，董事長為謝詠芬。
- 公告：Goodinfo 列出出售上海子公司 80% 股權與轉投資架構調整，未見董監持股異動的說明。
- 結論：無足夠資料判斷內部人情緒，僅能描述為持股穩定。

## Ownership shifts

- yfinance major_holders：insidersPercentHeld 27.2%、institutionsPercentHeld 8.5%、institutionsFloatPercentHeld 11.7%、機構數 16（口徑與台灣來源不同，且日期不明）。
- 台灣來源：外資持股約 11.56%（2026/07/09）；投信持股僅 0.06%。
- 趨勢：無時間序列，無法判斷集中度是升或降。

## Price reference（僅供背景，非當日確認）

- 2026/06/23 收盤 306.00 TWD；2026/07/09 約 276.5 TWD；2026/07/24 收盤 258.00 TWD。
- 2026 年 11 月價格未確認。

## Net sentiment score

- 分析師面：偏多但分歧（多數買進，目標價中位數近期下修）。
- 零售面：無法判定。
- 內部人面：中性（持股小幅下降，無買賣明細）。
- 綜合：中性，信心低。原因是零售與內部人資料大量缺失，且分析師資料日期落後。
- 背離旗標：無法判定。零售面資料缺，不能確認零售是否與分析師反向。

## 數據缺口與建議

1. 允許 reddit.com、api.stocktwits.com 網域，或改由其他工具取得 PTT / Dcard 股版。
2. 修復 yf 的 Yahoo cookie/crumb，以取得 recommendations 與 insider 原始資料。
3. 補抓 2026 年 10 月至 11 月的券商評等變動與價格，以驗證目標價是否仍有效。

來源（節錄）：
- https://tw.stock.yahoo.com/news/%E9%89%85%E4%BA%A8%E9%80%9F%E5%A0%B1-factset-%E6%9C%80%E6%96%B0%E8%AA%BF%E6%9F%A5-%E9%96%8E%E5%BA%B7-3587-041017576.html
- https://hk.investing.com/equities/materials-analysis-technology-consensus-estimates
- https://www.nstock.tw/author/article?id=910
- https://www.cmoney.tw/forum/stock/3587
- https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID=3587
- https://histock.tw/stock/large.aspx?no=3587

SENTIMENT REPORT COMPLETE
