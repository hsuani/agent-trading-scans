# Sentiment — SH (ProShares Short S&P 500) as of 2026-11-21

## Analyst consensus
DATA_UNAVAILABLE。SH 為 ETF，`pipeline/tools/yf SH rec_summary` 與 `recommendations` 皆回傳空陣列，無買進/持有/賣出分布，也無評等升降級或目標價變動紀錄。

## Retail social
- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（WebFetch 遭拒）。
- StockTwits / X：DATA_UNAVAILABLE（api.stocktwits.com 無法解析；WebSearch 未找到 2026-11 針對 SH 的散戶討論）。

## Retail hedging sentiment（以 ETF 基本資料與策略師評論代替）
- 產品定位：SH 目標為標普 500 單日報酬的 -1 倍，ProShares 同時將其行銷給看空與避險用途，結構上以 T-bills 搭配 swap 達成。
- 策略師評論（皆非 2026-11 確認資料，需謹慎）：
  - Goldman Sachs 衍生品策略師 Brian Garrett 據報導指出，因 Nvidia 財報前，標普指數保護相對便宜（來源為轉載文章，數字彼此不一致，僅可作為弱參考）。
  - SSGA 2026-10-19 的分析認為沒有萬用避險工具，長天期公債在成長型衝擊中較有效，黃金則是兩類衝擊中最穩定的分散工具；文章同時指出標普 500 已連續三年兩位數上漲，歷史上罕見。這是避險框架，不是明確看空。
  - Morgan Stanley 與 BNP Paribas 的 SPY 看跌選擇權避險建議見於報導，但未標示日期，無法確認為當前觀點。
- 整體：策略師圈內有避險需求的討論，但未找到 2026-11 的明確看空或看多 call。

## Fund flow sentiment（流量代理指標）
- Trackinsight 頁面顯示 YTD flows 為 -6.87%，定義不明，不可直接解讀為美元淨流出。
- 同一頁面列出 2026-11-10 的 AUM 為 €818M，價格 $32.67，52 週區間 $31.64 至 $39.20。
- 另一頁（無日期）列出 AUM 為 874.40M USD，且 1 年淨流入 186.36M USD。兩者日期皆不明，無法確認是否為 11 月數據。
- 未找到 2026-11 的單日或月度創建/贖回數據，故無法判定近期淨流入或淨流出。
- 結論：流量訊號 DATA_UNAVAILABLE（僅有不可靠的舊資料）。

## Insider activity / Ownership shifts
不適用（ETF，依任務指示略過）。

## Net sentiment score
Composite: neutral（信心：低）。
理由：分析師評等無資料；散戶社群（Reddit、StockTwits）全部無資料；流量資料日期不明、定義不清；策略師評論只有避險框架與舊的看跌建議，沒有 2026-11 的明確多空立場。

Divergence flag: no。因缺乏可比較的分析師與散戶雙方資料，無法判定 retail 與 analyst 傾向是否相反。

SENTIMENT REPORT COMPLETE
