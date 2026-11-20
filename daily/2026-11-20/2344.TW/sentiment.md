# Sentiment — 2344.TW (華邦電 Winbond) as of 2026-11-20

> 資料完整度低: Reddit 與 StockTwits 無法取得, 內部交易工具回傳空值, 分析師目標價來源彼此矛盾。以下結論信心偏低, 請勿當作完整情緒判斷。

## Analyst consensus

yf rec_summary (當月快照, 日期未標示):

| 評等 | 當月 (0m) | 前1月 (-1m) | 前2月 (-2m) | 前3月 (-3m) |
|---|---|---|---|---|
| Strong Buy | 3 | 4 | 4 | 4 |
| Buy | 4 | 4 | 4 | 3 |
| Hold | 1 | 0 | 0 | 0 |
| Sell / Strong Sell | 0 | 0 | 0 | 0 |

目前約 **7 buy / 1 hold / 0 sell**。過去三個月皆無賣出評等, 買方家數持平略降, 當月首次出現一家 hold。

- 評等變動: yf recommendations 回傳與 rec_summary 相同的月度彙總, 沒有逐筆升降評紀錄。
- 已知個別券商動態 (來源為聚合網站, 日期可信度不一):
  - JPMorgan: 2026-06-15 目標價由 NT$173 升至 NT$255; 2026-07-15 維持 Buy, 目標價升至 NT$360。這是可查到的最新一筆 JPM 動作。
  - Morgan Stanley: 2026-03-19 由 Overweight 降至 Hold, 目標價由 NT$155 降至 NT$140。另一來源提到大摩重申 Hold、目標價 NT$100, 日期不明。
  - 群益投顧: 維持 Buy, 目標價調至 NT$120.3 (2026-01 報導)。
  - 一則報告 Buy 目標價 NT$218, 對照股價 NT$176.5, 日期不明, 應為較早報告。
- 目標價共識: 各來源平均值從 NT$146 到 NT$245 不等, 高低價區間約 NT$100–360, 完全不一致。FactSet 中位數的說法 (NT$55 升至 NT$62) 來源日期不明, 數字與其他來源不相容, 不採用。
- 股價參照: 2026-11-13 收盤 NT$125 (statementdog)。其他頁面引用的股價從 NT$108 到 NT$176 不等, 無法確認 11-20 當下價位。
- 近期最大的評等面訊號是 "維持買進、目標價大幅上修" 的方向, 但 JPM 目標 NT$360 相對 NT$125 股價仍有很大落差, 需以券商原報告再核對。

## Retail social

- Reddit (r/wallstreetbets, r/stocks): **無法取得** (WebFetch 回報 Claude Code 無法連線 www.reddit.com)。無法評估討論量與多空傾向。
- StockTwits: **無法取得** (api.stocktwits.com DNS 解析失敗, 本次 session 網路白名單可能未允許此網域)。
- X / 新聞 chatter: 一般搜尋找不到 2026-11 的散戶多空文章。Investing.com 的使用者喊單頁面顯示多空兩極, 沒有明確方向, 也沒有可用的時間戳記。
- 技術面聚合頁 (Investing.com) 顯示 Strong Sell、RSI(14) 約 29、7 個賣出訊號、0 個買進訊號, 但頁面日期與價格不明, 只能視為低權重的雜訊, 不能當作散戶情緒。
- 討論量 vs 典型水準: **無法判定**。
- Themes (從新聞面可觀察到的主軸, 非散戶原文):
  - 記憶體景氣與營收爆發: statementdog 引用 2026 Q3 合併營收 NT$823.31 億, 季增 37.6%、年增 278.2% (換算: 823.31 億 × 1 億 = NT$82,331M, 約 NT$82.3B, 與股價與股本量級一致)。
  - 管理層法說預期 2027 年供給比 2026 年更緊。
  - 風險面: 消費性電子需求疲弱、報價高檔反轉疑慮 (statementdog 提及)。
  - 股價波動: Simply Wall St 統計平均週波動約 12.4%, 高於半導體產業平均約 6.9%。
  - 除息: TipRanks 列出 2026-11-18 為除息日, 已過, 對當前股價影響已經反映。

## Insider activity

- yf insider 回傳 **空陣列**, 無法確認 6 個月內的董監、CEO/CFO 買賣。
- 這不等於沒有內部人交易。Taiwan 的董監持股申報 (MOPS) 不在本工具範圍內, 建議另外查核。
- Net 6mo: **資料缺漏** (不能寫成 $0)。

## Ownership shifts

yf major_holders (日期未標示):
- Insider 持股比例 30.26%
- Institutions 持股比例 27.59% (流通股比例 39.57%)
- 機構家數 220
- 趨勢: 只有單一時點快照, 無法判斷近期增減碼方向。

## Net sentiment score

**Composite: bullish (信心: 低)**

- 分析師面: 偏多 (7 buy / 1 hold / 0 sell, 無賣出評等, 目標價持續上修)。
- 散戶面: **無資料**。
- 內部人面: **無資料**。
- 綜合主要依賴分析師面, 且分析師目標價來源矛盾, 評級權重應降低。

**Divergence flag: 無法判定** — 散戶傾向缺漏, 無法檢查是否與分析師傾向相反。

## 資料來源狀態

| 來源 | 狀態 |
|---|---|
| yf rec_summary | 成功 (單一快照) |
| yf recommendations | 成功但與 rec_summary 相同, 無逐筆變動 |
| yf insider | 空陣列 |
| yf major_holders | 成功 (日期不明) |
| Reddit (wallstreetbets / stocks) | 失敗: 無法連線 |
| StockTwits | 失敗: DNS 解析失敗 (需在 session 網路設定中允許 api.stocktwits.com) |
| WebSearch (英文/中文) | 部分成功, 來源矛盾, 日期多數不明 |

SENTIMENT REPORT COMPLETE
