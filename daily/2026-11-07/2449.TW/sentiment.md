# Sentiment: 2449.TW 京元電子 (King Yuan Electronics) as of 2026-11-07

## Executive summary

- 分析師評等一面倒偏多: 16 家券商全部為 Buy 或 Strong Buy，無 Hold / Sell。近三個月僅 Strong Buy 由 4 家增至 5 家，未見降評。
- 散戶與社群訊號薄弱，且多為非 2026-11-07 當日的零散資料。能取得的少數討論偏悲觀（股價承壓、籌碼賣壓），但時間點不明，可信度低。
- 內部人交易資料本次無法取得（yfinance insider 回傳空陣列），無法計算近 6 個月淨買賣，不可解讀為「無內部人交易」。
- 機構持股約 35.5%，為單一時點快照，無法判斷持股集中度趨勢。
- 綜合判斷: 分析師偏多、散戶資料不足、內部人資料缺漏，整體情緒評估信心低。

## Data availability

| 資料項目 | 來源 | 狀態 | 備註 |
|---|---|---|---|
| 分析師評等分布 | `pipeline/tools/yf.py 2449.TW rec_summary` | 可用 | 單一時點快照，三個期間（0m / -1m / -2m） |
| 歷史評等變動 | `pipeline/tools/yf.py 2449.TW recommendations` | 部分可用 | 只有相對月份，無具體日期，無法精確對應事件 |
| 內部人交易 | `pipeline/tools/yf.py 2449.TW insider` | 不可用 | 回傳空陣列，原因未知（Yahoo cookie/crumb 取得失敗） |
| 股東結構 | `pipeline/tools/yf.py 2449.TW major_holders` | 可用 | 單一快照，無歷史比較 |
| Reddit (r/wallstreetbets, r/stocks) | WebSearch 替代 | 未取得 | 本次依任務指示以 WebSearch 取代 WebFetch，搜尋未出現相關串文 |
| StockTwits | 未抓取 | 未取得 | 本次未對財經網站發出 WebFetch；StockTwits 對台股覆蓋度有限 |
| X / 新聞與論壇 | WebSearch | 部分可用 | 多為財經資料頁與論壇摘要，日期混雜，部分無法確認日期 |
| 散戶討論量 | 無量化資料 | 無法評估 | 無法取得提及次數，只能定性描述 |

Cookie/crumb 取得失敗，yfinance 相關資料需以「可用但不完整」看待。

## Retail / social sentiment read

**整體傾向: 資料不足，偏中性至偏保守，信心低。**

- 社群彙整 (CMoney 股市社群，日期不明，推測為 2026 年 10 月前後): 摘要指出近期股價承壓、社群情緒偏悲觀、籌碼面賣壓可能放大；同時也有人留意外資買超、有人關注 2027 年 EPS 展望。多空並陳，無一致方向。
- 個人部落格與論壇貼文 (CMoney 單篇，日期不明): 作者認為股價略偏高，但對 2027 年 EPS 預估 15 至 18 元有期待，並提及 255 附近為重要支撐。屬個人意見，樣本數極小。
- 代表性意見（短引述）:
  - 「明年可以400嗎」（CMoney 社群提問，反映長線看多分歧）
  - 「255左右有一個強力支撐」（個人技術面觀點）
- 股價背景 (非社群，但影響情緒): 依 TradingView 頁面，記錄高點為 2026-05-05 的 364.5 TWD；另一頁面顯示 2026-10-22 收盤約 262.5 TWD，單日下跌約 5.6%，前收盤約 278 TWD。兩個時點資料來源日期不同，僅供參考。
- 主題 (Themes):
  1. 股價自高點回落後的承壓與籌碼賣壓
  2. 2027 年 EPS 成長預期與估值是否合理（P/E 約 42 至 48 倍之說法見於不同頁面）
  3. 外資動向與支撐價位
  4. 公司海外布局調整（有一則 Yahoo 財經摘要提及出售中國大陸營運據點，日期不明，未能確認細節）

**Volume vs typical**: 無法量化，定性判斷為「本次搜尋中可見的獨立討論量低」。

## Analyst consensus

**16 buy / 0 hold / 0 sell**（Strong Buy 5、Buy 11）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 0m（當前） | 5 | 11 | 0 | 0 | 0 | 16 |
| -1m | 4 | 11 | 0 | 0 | 0 | 15 |
| -2m | 4 | 11 | 0 | 0 | 0 | 15 |

- 近期動向: 當前期間相較 -1m 新增一家 Strong Buy，無降評、無 Hold 或 Sell 出現。
- 目標價: 一個估值頁面（ValueInvesting，日期不明）列出平均 12 個月目標價約 342.35 TWD。另一個來源（TradingView）列出目標價區間約 268 至 435 TWD。兩者日期皆不確定，不宜直接換算成最新隱含上行空間。
- 其他: 一則 S&P Global 彙整的資料顯示 15 位分析師給予「Strong Buy」共識、平均目標價約 368.67 (幣別與日期未確認，需核對原始來源)。
- 注意: `recommendations` 的歷史資料僅有相對月份，缺乏具體評等變動日期與目標價調整紀錄，因此「目標價變動」欄位只能以不確定的快照替代。

## Institutional / insider signal

**內部人 (6 個月):** 資料缺漏，無法計算。yfinance insider 回傳空陣列，不應解讀為「無交易」。
- Notable: 無可驗證資料。
- 建議補抓方式: 公開資訊觀測站 (MOPS) 董事、監察人及大股東持股異動申報，或待 Yahoo cookie/crumb 恢復後重新呼叫 `insider`。

**股東結構 (單一快照):**
- 內部人持股比例 (insidersPercentHeld): 約 8.83%
- 機構持股比例 (institutionsPercentHeld): 約 35.52%
- 流通股中機構持股比例 (institutionsFloatPercentHeld): 約 38.96%
- 機構家數 (institutionsCount): 222
- 趨勢: 無歷史比較資料，無法判斷機構集中度是增加或減少。

## Overall sentiment verdict

| 面向 | 判讀 | 信心 |
|---|---|---|
| 分析師共識 | 偏多 (16 Buy / 0 Hold / 0 Sell，近期無降評) | 中 (樣本數 16，但快照單一時點) |
| 散戶 / 社群 | 資料不足，零散內容偏悲觀至中性 | 低 |
| 內部人 | 無法判讀（資料缺漏） | 無 |
| 機構結構 | 持股約 35.5%，無趨勢資料，中性 | 低 |

**綜合情緒: 偏多（以分析師為主），散戶面中性偏保守，信心低。**

**分歧旗標 (Divergence flag): 暫定為「可能分歧」，但證據薄弱。** 分析師一致偏多，而部分社群摘要偏悲觀，兩者方向相反。然而散戶樣本量小、日期不明，不足以作為確定性訊號，不應單獨作為操作依據。

本報告僅為情緒資料彙整，不構成買賣建議。

## Sources

- yfinance 工具輸出: `pipeline/tools/yf.py 2449.TW recommendations`、`rec_summary`、`insider`（回傳空值）、`major_holders`，皆於 2026-11-07 報告日執行
- [CMoney 股市社群 - 小散戶對京元電子的看法](https://www.cmoney.tw/follow/channel/stock-1566chart=d)
- [CMoney 股市社群 - stock 2449](https://www.cmoney.tw/follow/channel/stock-2449)
- [StatementDog - 2449 京元電子](https://statementdog.com/analysis/2449)
- [Nstock - 2449](https://www.nstock.tw/2449?status=2)
- [Yahoo 股市 - 2449.TW 新聞](https://tw.stock.yahoo.com/quote/2449.TW/news)
- [TradingView - TWSE 2449](https://www.tradingview.com/symbols/TWSE-2449/)
- [ValueInvesting.io - 2449.TW 估計](https://www.valueinvesting.io/2449.TW/estimates)
- [Alpha Lenz - King Yuan Electronics 預測與分析](https://alpha-lenz.com/en/companies/king-yuan-electronics-co-ltd)
- [Simply Wall St - King Yuan Electronics](https://simplywall.st/stocks/tw/semiconductors/twse-2449/king-yuan-electronics-shares)
- [Alpha Spread - 2449 分析師預估](https://www.alphaspread.com/security/twse/2449/analyst-estimates)
- [Yahoo Finance AU - 2449.TW 新聞](https://au.finance.yahoo.com/quote/2449.TW/news/)
- [KYEC 2Q26 Investor Update (英文)](https://www.kyec.com.tw/Upfiles/EDUp/files/投資人關係/每季營運報告/KYEC(2449)_2Q26%20Investor%20update_English.pdf)

SENTIMENT REPORT COMPLETE
