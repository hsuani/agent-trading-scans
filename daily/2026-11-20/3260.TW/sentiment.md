# Sentiment — 3260.TW（威剛）as of 2026-11-20

資料來源大多缺失，置信度低。

## 資料可用性總覽

| 來源 | 狀態 |
|---|---|
| yf recommendations / rec_summary | 失敗（Yahoo cookie/crumb 連線失敗，回傳空陣列） |
| yf insider | 失敗（同上，無資料） |
| yf major_holders | 失敗（同上，無資料） |
| Reddit r/wallstreetbets, r/stocks | 失敗（www.reddit.com 無法存取） |
| StockTwits | 失敗（api.stocktwits.com DNS 無法解析，需於 session 網路設定放行） |
| 新聞 / 研報 WebSearch | 可用，但多為中文新聞轉述，部分數字需交叉核對 |

## Analyst consensus

rec_summary 無資料，無法給出標準 N buy / N hold / N sell 分布。以新聞可查到的評等如下：

| 日期 | 機構 | 類型 | 評等 | 目標價（NT$） | 備註 |
|---|---|---|---|---|---|
| 2026-11 初 | 玉山投顧 | 本土投顧 | 增持 | 420 | Q3 毛利率低於預期後仍維持，已於新聞中確認 |
| 2026-05 | 官股金控旗下投顧 | 本土投顧 | 買進 | 556 | 早期資料，已過時 |
| 2025-11 | 某法人 | 法人 | 由 BUY 下調 Trading BUY | 297.5 降至 200 | 一年前資料，已過時 |
| — | Nasdaq/Fintel 彙整 | 共識 | — | 255 | 引用 2025-11 估值與收盤 87.60，明顯過時，不採用 |

- 目前可確認的 2026-11 評等僅一筆（玉山 增持，TP 420）。未找到 2026-11 外資評等或目標價。
- 近期基本面動向：11/6 法說表示 Q4 營收因年底客戶庫存結算將較 Q3 略降；但管理層看好 DRAM 2026 年缺貨延續，且認為 2027 年缺貨將更嚴重。
- 分析師整體傾向：偏多（以本土投顧為主），但樣本極少，且 Q3 毛利率不如預期是主要負面點。

## Retail social

- **Reddit**：無法取得（403 / 無法存取）。
- **StockTwits / X**：StockTwits 無法存取。WebSearch 未找到可量化的 X 討論量。
- **Retail 聲量**：無法量化相對於平常的提及次數，缺口需註明。
- **Retail 傾向**：無資料，無法判定 bullish / bearish / mixed。
- **Themes（僅依新聞推論，非社群原文）**：
  - 記憶體（DRAM / NAND）漲價與缺貨週期延續
  - Q3 毛利率低於預期、成本上升壓縮獲利
  - Q4 營收季減的指引
  - 公司買回庫藏股（轉讓員工）的支撐效果

## Insider activity

無資料（yf insider 失敗）。無法計算 6 個月淨買賣金額，也無法辨識 CEO/CFO 等人的交易。
- 公司公告 2026-11-09 董事會通過買回最多 600 萬股，用於轉讓員工，期間 2026-11-10 至 2027-01-08，價格區間 NT$213.50–532.20。此為公司行為，非內部人交易，不列入淨買賣計算。

## Ownership shifts

無資料（yf major_holders 失敗）。無法判斷機構持股集中度趨勢。

## 營收與獲利（供交叉核對，單位 億 TWD）

| 期間 | 營收（億 TWD） | 年增率 | 來源 |
|---|---|---|---|
| 2026-10 單月 | 170.63 | +282.3%（technews 年增標示） | technews |
| 2026-01 至 10 月累計 | 1,343.69 | +222.7% | technews |
| 2026-01 至 09 月累計 | 1,173.06 | +215.6% | technews |

- 新聞彙總稿中寫成「NT$17.06 billion」與「NT$134.37 billion」，為 10 倍單位錯誤。以原始報導 170.63 億、1,343.69 億為準。
- 交叉驗算：9 個月累計 EPS 約 101.47 元 × 股本約 6.49 億股 ≈ 約 65.8 億元淨利，淨利率約 5.6%，與營收規模合理。
- 另有 2025-11 的「11 月營收 55.98 億」報導屬於 2025 年，非本期資料。

## Net sentiment score

- **Composite：中性偏多（neutral-to-bullish），置信度低。**
- 偏多依據：記憶體供需偏緊的產業敘事、10 月營收大幅年增、玉山 增持 TP 420、公司買回庫藏股。
- 偏空依據：Q3 毛利率不及預期、Q4 營收季減指引、2025 年之後的評等下調紀錄。
- 置信度低的原因：只有一筆當期分析師評等；零社群資料；無內部人與持股資料。

**Divergence flag：無法判定。** 因無 retail 資料，無法比較 retail 與分析師的傾向是否相反。目前只能說分析師側偏多。

## Sources

- [威剛 10 月營收 170.63 億（technews）](https://finance.technews.tw/2026/11/06/adata-3260-202610-financial-report/)
- [威剛 9 月營收 157.30 億（technews）](https://finance.technews.tw/2026/10/06/adata-3260-202609-financial-report/)
- [威剛估 Q4 營收略降（uanalyze）](https://uanalyze.com.tw/articles/3527858570)
- [威剛法說與 Q3 毛利率討論（chinatimes）](https://wantrich.chinatimes.com/news/20261102900001-420101)
- [威剛買回庫藏股公告（cnyes）](https://news.cnyes.com/news/id/6653403)
- [玉山投顧維持增持、TP 420（chinatimes）](https://wantrich.chinatimes.com/news/20261106900281-420101)
- [威剛 2025-11 評等下調（chinatimes）](https://wantrich.chinatimes.com/news/20251118900294-420101)
- [威剛 2026-05 買進評等（chinatimes）](https://wantrich.chinatimes.com/news/20260508900003-420101)
- [威剛 Nasdaq/Fintel 目標價 255（過時，僅供排除）](https://www.nasdaq.com/articles/adata-technology-co-tpex-3260-price-target-increased-9380-25500)

## 待補項目

1. 放行 api.stocktwits.com 與 Reddit，或改用其他社群來源，補上 retail 聲量與傾向。
2. 修復 yf 的 Yahoo cookie/crumb 連線，才能取得 rec_summary、insider、major_holders。
3. 目前股價未確認，NT$213.50–532.20 買回區間很寬，建議以行情資料核對。

SENTIMENT REPORT COMPLETE
