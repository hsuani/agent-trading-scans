# Sentiment — 5475.TWO (德宏實業) as of 2026-11-06

**資料狀態：部分可用 (PARTIAL)。分析師共識與內部人交易為 DATA_UNAVAILABLE；散戶情緒僅有 2026 年 7 至 8 月的間接資料。**

## Analyst consensus（分析師共識）
DATA_UNAVAILABLE。
- `yf 5475.TWO recommendations` 與 `rec_summary` 皆回傳空陣列（重試兩次結果相同）。Yahoo cookie/crumb 取得失敗，可能是資料源覆蓋不足，也可能是此櫃買股票本來就沒有券商評等。
- 搜尋券商目標價與評等，沒有找到任何 buy/hold/sell 分布或目標價調整。僅找到 wantgoo 的券商分點買賣統計（星展、瑞銀、摩根士丹利，2026 年 7 月），只有買賣金額，沒有評等。
- 結論：分析師 % BUY 無法計算，目前不能判斷 analyst tilt。

## Retail social（散戶社群）
- **Reddit**：r/stocks 搜尋被拒（無法連線 www.reddit.com），無資料。r/wallstreetbets 未嘗試（同一網域，預期相同結果）。
- **StockTwits**：api.stocktwits.com 無法解析（DNS 失敗），無資料。
- **X / 新聞 / 論壇（WebSearch）**：來源主要是 CMoney 股市論壇與投資快訊，搜尋結果未出現 2026 年 11 月的內容，最新資料停在 2026 年 7 月底至 8 月。
  - 論壇 AI 彙整摘要顯示多數留言偏悲觀，擔心股價再跌，也有人建議短線觀望。摘要本身不是留言原文，可靠度有限。
  - 同一批摘要提到 2026 年 7 月 24 日外資大幅買超，且有留言指出主力賣壓與意見分歧。
  - 有留言質疑 Q1 2026 EPS 0.65 元（另一處引用為 0.43 元，兩者不一致）的成長動能是否撐得住股價，並提到 EVT 量產最快要到 2027 年。
  - 有一則快訊提到股價單月漲幅很大（標題寫 566.82%，日期與來源不明），此數字未經驗證，不能採信。
- **Retail buzz 量**：無法與平常基準比較，只能判定為低到中等（可見來源僅有少數 CMoney 文章與彙整頁）。
- **Retail tilt**：資料過時，且來源為 AI 彙整，只能判斷為偏保守 / 分歧 (mixed-to-cautious)，信心低。
- **主要主題**（依搜尋摘要）：7 月營收創高的成長故事（nStock：7 月營收 2.29 億元，年增 264%，為八年來單月新高；1 至 7 月累計 10.64 億元）、股價波動與主力賣壓、EPS 與估值是否合理、EVT 量產時程。
- **處置股紀錄**：搜尋結果提到該股曾被列為處置股（5 分盤交易），但年份在不同來源中不一致（2025 年 5 月 vs. 2026 年 5 月 29 日至 6 月 12 日），需再核對。

## Insider activity（內部人交易）
DATA_UNAVAILABLE。`yf insider` 回傳空陣列，無法計算 6 個月淨買賣金額，也無法辨識 CEO/CFO 等人的交易。

## Ownership shifts（股權結構）
Yahoo `major_holders`（可能不完整，台股資料）：
- 內部人持股 27.9%
- 機構持股 2.7%（占流通股 3.8%），機構數量 7 家
- 機構集中度低，無歷史趨勢資料，無法判斷變化方向。

## Net sentiment score（綜合情緒分數）
**Composite：neutral（信心低）**
- 分析師面：無資料。
- 散戶面：保守偏分歧，但資料停在 2026 年 7 至 8 月，不能代表 11 月現況。
- 籌碼面：內部人持股高，機構持股低；7 月外資有買超紀錄，但時點已舊。
- **Divergence flag：無法判定**（缺少分析師資料）。

## Summary line
analyst % BUY：N/A（DATA_UNAVAILABLE）；機構流向：7 月外資買超（資料過時，11 月無資料）；散戶語氣：保守偏分歧（信心低，資料截至 2026 年 8 月）。

## Sources
- CMoney 5475 論壇
- CMoney 5475 追蹤頁
- nStock 德宏資料
- wantgoo 5475 分點買賣

SENTIMENT REPORT COMPLETE
