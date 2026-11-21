# Sentiment — 3587.TWO 閎康科技 as of 2026-11-22

資料可信度總結: 本次多數來源失效。yf 的分析師評等與內部人交易回傳空值, Reddit 與 StockTwits 無法連線, 只能依 WebSearch 片段與 yf 持股資料整理。整體情緒判定信心低。

## Analyst consensus
yf `recommendations` 與 `rec_summary` 皆回傳空值, 無法取得目前的買進/持有/賣出分布, 也沒有近期評等變動紀錄。

唯一可參考的是 Investing.com 的 WebSearch 片段 (資料截至 2026-07, 已過時, 樣本僅 3 位分析師): 3 買進 / 0 持有 / 0 賣出, 12 個月平均目標價約 365.67 元 (高點 450 元, 低點 300 元)。目前股價約 171–193 元 (見下方說明), 以此推算目標價隱含上漲空間, 但該目標價為 7 月時點數字, 不代表 11 月共識。

近期升評/降評與目標價調整: 無資料。

## Retail social
- Reddit (r/stocks, r/wallstreetbets): 無法存取 (WebFetch 被封鎖), 未取得樣本。
- StockTwits: api.stocktwits.com 無法解析 (DNS 失敗), 需於 session 網路設定中放行, 本次未取得。
- PTT 股板: 搜尋未找到 3587 討論串。
- CMoney 股市爬蟲論壇 (cmoney.tw/forum/stock/3587): 有頁面, 但擷取內容多為其他個股留言與熱門文章, 未見閎康實際討論。
- poorstock.com 3587 討論區: 含 AI 自動生成的籌碼與技術分析, 日期不一致, 技術指標 (RSI 偏低、MACD 死叉) 不可作為情緒依據。
- 聲量 (相對平常): 無法量化。本次未取得 11 月社群提及次數。

- Themes (由 WebSearch 新聞與公司資料歸納, 非社群原文):
  - 日本市場成長: 董事長 2026-03 表示日本與美國為今年成長主力, 日本營收占比有望達 20%。
  - 先進製程檢測題材: 日本客戶 2 奈米試產線, 目標 2027 下半年量產。
  - 矽光子: 董事長表示仍在研發階段, 短期難爆發式成長 (偏保守論述)。
  - 獲利動能: 2026 前三季 EPS 累計 6.68 元, 年增約 57% (WebSearch 報導); 10 月營收 3.38 億元, 年增 10.19%, 月減 1.23%。
  - 風險論述: 董監事持股質押比例 41.6% (Goodinfo)。

- Retail tilt: 無法判定。缺乏可靠社群樣本, 不宜推論散戶偏多或偏空。

## Insider activity
Net 6mo: 無資料。yf `insider` 回傳空值, 無法列出 6 個月內董監與大股東買賣金額。

- 補充 (非交易資料): 董監持股約 20.1%, 其中 41.6% 已質押 (Goodinfo, 資料約至 2026-10)。高質押比例可能是潛在風險, 但不等同於近期賣出。
- Notable: 無法確認 CEO/CFO 或其他人員的近期交易。

## Ownership shifts
yf `major_holders` (時點未標示):
- insidersPercentHeld: 27.2%
- institutionsPercentHeld: 8.5% (占流通股 11.7%)
- 機構家數: 16

注意: 內部人持股比例 yf 為 27.2%, Goodinfo 為 20.1%, 定義或時點不同, 不宜直接比較。另 Goodinfo 顯示超過 1000 張大戶持股比例約 21.8%, 另一來源 (poorstock AI 內容) 為 26.28%, 數字不一致。趨勢方向 (增加或減少) 無法判定, 缺乏多期比較資料。

股價參考 (數據不完全同日): Goodinfo 快照顯示 11 月初約 188–193 元, 11 月 13 日快照為 171 元。此為近似值, 未經統一時點核對。

## Net sentiment score
Composite: **中性 (信心低)**。
- 分析師面: 僅有 7 月的小樣本偏多資料 (3 買進 0 賣出), 已過時, 權重低。
- 散戶面: 無法取得 Reddit、StockTwits 樣本, 無法判定。
- 內部人面: 無交易資料, 質押比例偏高為中性偏謹慎的風險提示。
- 基本面新聞: 10 月營收與前三季獲利年增, 屬正面基本面背景, 但不是社群情緒指標。

Divergence flag: **無法判定** — 缺乏近期散戶樣本與 11 月分析師評等, 無法確認散戶與分析師是否背離。

Data gaps (建議補件):
1. yf `recommendations` 與 `rec_summary` 回傳空值, 需確認 Yahoo 連線 (cookie/crumb 取得失敗) 或改用其他來源。
2. 需放行 www.reddit.com 與 api.stocktwits.com 的網路存取。
3. 需 PTT 股板 (ptt.cc/bbs/Stock) 原始討論或券商研究報告以補充 11 月情緒。
4. yf `insider` 空值需確認是否為該標的資料缺漏。

SENTIMENT REPORT COMPLETE
