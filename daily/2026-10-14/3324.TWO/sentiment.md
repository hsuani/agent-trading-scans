# Sentiment — 3324.TWO (雙鴻 Auras Technology) as of 2026-10-14

資料可信度提醒: Reddit 與 StockTwits 本次皆無法取得 (見下方),社群情緒部分為空白。分析師評等來自 yf rec_summary (當期快照),券商個別評等與目標價來自 WebSearch 聚合頁,日期與數字彼此不一致,僅供參考。

## Analyst consensus
17 家: 4 strongBuy / 9 buy / 4 hold / 0 sell / 0 strongSell,即 13 buy 系 / 4 hold / 0 sell。

近四個月趨勢 (yf rec_summary):
| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 當期 (0m) | 4 | 9 | 4 | 0 | 0 |
| -1m | 4 | 9 | 4 | 0 | 0 |
| -2m | 3 | 9 | 4 | 0 | 0 |
| -3m | 3 | 8 | 4 | 0 | 0 |

- 趨勢: 買進系評等由 -3m 的 11 家增至當期 13 家,hold 維持 4 家,賣出評等始終為 0。評等結構持續偏多且小幅升級。
- yf recommendations 回傳的仍是上述彙總趨勢,未提供個別券商的升降評等明細,因此無法確認具體 upgrade/downgrade 事件。
- 目標價 (WebSearch 彙整,日期不一致):
  - 日系外資 (2026-07): 買進, 目標價 NT$1,640,據稱預估 2026 年營收年增 60%–70%,並提到部分產品重回 NVIDIA Vera Rubin 合格供應商。
  - Nomura/Instinet (2026-05): 買進, 目標價 NT$1,740。
  - JPMorgan (2026-05): 持有 (Hold)。
  - Investing.com 平均 12 個月目標價約 NT$1,406 (頁面日期不明)。
  - 較舊資料: 美系外資 2025-09 買進 NT$1,118;2025-11 改為觀望。已過時,不納入當期判斷。

## Retail social
- Reddit: 無法取得。r/stocks 與 r/wallstreetbets 的搜尋端點回傳 "unable to fetch from www.reddit.com",本次無樣本,無法判定討論量與情緒傾向。
- StockTwits / X: StockTwits 端點 DNS 解析失敗 (api.stocktwits.com 無法連線),本次無樣本。X 無獨立可用來源。
- 其他情緒指標: Investing.com 會員情緒小工具偏空 (bearish),但樣本來源與時間不明,權重低。
- 討論量: 無法量化,以定性記錄為 "無資料"。
- Themes (來自 WebSearch 摘要,非社群原文): 液冷散熱 (AI 伺服器與 ASIC 客戶導入)、記憶體相關需求、NVIDIA Vera Rubin 供應鏈認證、營收高成長。
- 價格與估值 (聚合頁,日期不一致): 2026-09 初收盤約 NT$1,340,本益比約 30.9x;其他頁面顯示股價 NT$820–1,155 與 P/E 27–29x。一年漲幅約 68%–87%。
- 財報訊號衝突: TradingView 稱最近一季 EPS NT$10.66 優於預估 NT$8.55;Investing.com 稱 2026-08-07 公布 EPS 10.41 低於預估 13.16。兩者不能同時成立,需以公司公告核對。

## Insider activity
Net 6mo: 無資料。pipeline/tools/yf.py 3324.TWO insider 回傳空陣列 `[]`,未提供任何內部人交易紀錄。此項既無法確認淨買或淨賣,也無法區分 CEO/CFO 與其他人員。注意: 台股內部人申報 (董監持股異動) 通常不會以 yfinance 格式完整呈現,空結果不代表無交易。

## Ownership shifts
- 內部人持股比例 (insidersPercentHeld): 28.9%
- 機構持股比例 (institutionsPercentHeld): 12.5%;占浮動股比例 (float) 17.5%
- 機構數量 (institutionsCount): 55
- 歷史趨勢: 本次工具僅提供單一時點快照,無法判定機構集中度的變化方向。
- 解讀: 內部人持股比例高 (近 29%),機構持股偏低,股權集中於創辦人與關係人,散戶與機構的籌碼結構需留意。

## Net sentiment score
- 分析師: 偏多 (bullish),13 家買進系、0 家賣出、評等持續小幅上修。信心: 中高。
- 散戶 (社群): 無資料。Investing.com 會員情緒偏空,但權重低、來源不明。
- 內部人: 無資料。
- **綜合: 偏多 (bullish),信心低。** 理由: 分析師面為唯一有實質樣本的訊號,其他三項 (社群、內部人、可靠的財報共識) 在本次皆無法確認,不足以支撐高信心結論。

Divergence flag: 無法判定 (no) — 分析師偏多,但散戶面無樣本可比。Investing.com 會員情緒偏空 (與分析師偏多方向相反) 可視為弱分歧訊號,但不足以正式標記,待 Reddit/StockTwits 恢復後重新評估。

## 待補項目
1. Reddit 與 StockTwits 恢復後重跑社群面板,補充討論量與多空比例。
2. 核對 2026-08 季報 EPS 實際值 (TradingView 與 Investing.com 數字衝突)。
3. 以台灣證交所或公開資訊觀測站核對董監事持股異動,補足內部人淨買賣。
4. 取得 2026-10 當月的券商研究報告,更新目標價與評等。

## 指標摘要

| 指標 | 數值 | 日期 / 來源 | 備註 |
|---|---|---|---|
| 買進系評等 (strongBuy + buy) | 13 | 當期, yf rec_summary | -3m 為 11 家 |
| 持有 (hold) | 4 | 當期, yf rec_summary | 持平 |
| 賣出 (sell + strongSell) | 0 | 當期, yf rec_summary | 持續為 0 |
| 最新目標價 (日系外資) | NT$1,640 | 2026-07, WebSearch | 買進 |
| Nomura/Instinet 目標價 | NT$1,740 | 2026-05, WebSearch | 買進 |
| 平均目標價 | 約 NT$1,406 | 頁面日期不明, WebSearch | 僅參考 |
| 內部人淨交易 (6mo) | 無資料 | yf insider 回傳空陣列 | 無法判定 |
| 內部人持股比例 | 28.9% | yf major_holders | 單一時點 |
| 機構持股比例 | 12.5% (float 17.5%) | yf major_holders | 單一時點 |
| 機構數量 | 55 | yf major_holders | 單一時點 |
| Reddit 討論量 / 情緒 | 無資料 | 無法存取 | 403 類阻擋 |
| StockTwits 情緒 | 無資料 | DNS 失敗 | 無法連線 |
| Investing.com 會員情緒 | 偏空 | WebSearch 聚合頁 | 來源與日期不明,低權重 |
| 本益比 (P/E) | 約 27–31x | WebSearch 聚合頁 | 數字不一致 |
| 綜合情緒 | 偏多 (bullish) | 本報告 | 信心低 |
| 分歧旗標 (Divergence) | 無法判定 | 本報告 | 社群面無資料 |

資料來源 (WebSearch 聚合頁):
- https://www.ctee.com.tw/news/20251107700804-430201
- https://wantrich.chinatimes.com/news/20260715900267-420101
- https://statementdog.com/analysis/3324/pe
- https://in.tradingview.com/symbols/TPEX-3324
- https://ca.investing.com/equities/auras-technology-co-ltd-consensus-estimates
- https://simplywall.st/stocks/tw/tech/tpex-3324/auras-technology-shares

SENTIMENT REPORT COMPLETE
