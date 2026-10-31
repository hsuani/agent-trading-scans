# Sentiment — 3289.TWO (宜特 Integrated Service Technology) as of 2026-11-01（資料截至 2026-10-31）

注意：本次資料嚴重不足，多數來源失敗。綜合評級只能視為「資料不足、信心低」，不可當作市場情緒判斷的依據。

## 來源狀態

| 來源 | 狀態 | 說明 |
|---|---|---|
| yf recommendations | 失敗 (空值) | Yahoo cookie/crumb 取得失敗，無歷史評等變動 |
| yf rec_summary | 失敗 (空值) | 同上，無 current buy/hold/sell 分布 |
| yf insider | 失敗 (空值) | 無內部人交易資料 |
| yf major_holders | 部分成功 | 見下方股權結構 |
| Reddit r/wallstreetbets / r/stocks | 失敗 | 抓取被拒 |
| StockTwits | 失敗 | api.stocktwits.com DNS 無法解析 |
| WebSearch 英文 | 無有效資料 | 無 2026-10 的意見或情緒資料；公司名稱來源不一致 |
| WebSearch 中文 | 部分有效 | 找到 2026 年股價與營運零散資訊，但無最新券商評等 |

## 公司辨識

3289 為宜特科技 (Integrated Service Technology)。英文搜尋結果中有一處標為 Waffer Technology Corp.，與其他來源衝突，本報告以宜特為準，但建議人工確認代號對應。

## Analyst consensus

0 buy / 0 hold / 0 sell（資料缺失，無法取得）。2026 年最新券商目標價與評等：未找到。中文搜尋找到的舊資料（2024/2025 年目標價）僅供參考，不代表現行評等。

## Retail social

- Reddit (wallstreetbets / stocks)：無法取得。
- StockTwits / X：StockTwits 無法連線；X 無有效搜尋結果。
- 中文投資社群：找到 CMoney 投資快訊類文章標題，多為正面描述（「穩健成長與未來展望」、「營運展望正向」、「股價上揚」），但這些是單篇摘要，無法做量化統計，不能視為散戶情緒樣本。
- 主要主題（僅從標題推測，信心低）：營運展望、毛利率改善預期、股利填息、財務體質優化。

## Insider activity

Net 6mo：無資料（yf insider 回傳空值）。

## Ownership shifts

yf major_holders：
- 內部人持股比例約 17.55%
- 機構持股比例約 2.77%（佔流通股約 3.36%）
- 機構家數約 7 家

解讀：流通股中機構持股比例偏低，但這是單一快照，無歷史趨勢可比較。

## 公司基本面背景（來自中文搜尋，非情緒資料）

- 2026 年 6 月自結合併營收約 4.26 億 TWD；2026 年上半年合併營收年減約 2.93%。
- 轉投資宜錦自 2026 年 3 月中旬起改採權益法認列，營收不再併入合併營收。
- 2026 年 3 月自結稅後淨利約 1.95 億 TWD，EPS 約 2.27 元；公司預期第二季起毛利率有顯著成長動能。
- 2025 年全年自結稅後淨利約 3.66 億 TWD，年減 23.82%，EPS 4.81 元。
- 股價：2026 年 3 月 19 日一度漲停至 149.5 元，為約 15 個月高點；2026 年 8 月除息後很快填息，股價在 150 元附近，當週三大法人偏多買超。

## Net sentiment score

綜合判斷：中性 (neutral)，信心低。
理由：無分析師評等資料、無散戶社群量化資料、無內部人交易資料。唯一可用的正面訊號是中文財經摘要的正向標題與 8 月後三大法人偏多買超的報導，但樣本少、時點舊，且營收與本業獲利在 2026 年仍呈年減。

Divergence flag：無法判定（缺少分析師與散戶雙方資料）。

## 建議後續補足
1. 在 session 網路設定允許 api.stocktwits.com 與 reddit.com 後重試。
2. 以 Yahoo 股市或 MoneyDJ「法人評等」頁面人工確認 2026 年最新目標價與評等。
3. 以 TWSE/TPEX 公開資訊觀測站確認近 6 個月內部人申報。
