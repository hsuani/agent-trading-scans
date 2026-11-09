# Sentiment — IBM as of 2026-11-10

資料限制：Reddit（r/wallstreetbets、r/stocks）與 StockTwits 直接抓取皆失敗（Reddit 無法連線；api.stocktwits.com 無法解析，需於 session 網路設定放行）。本報告的散戶面資料改以網路搜尋彙整的二手來源補充，時間多落在 2026 年 5–6 月，**非 11 月即時資料**。Yahoo 端點 cookie/crumb 取得失敗，但 recommendations / insider / holders 數據仍有回傳。

## Analyst consensus

單位：分析師家數（yf rec_summary，合計 25 家）

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 買方合計 | 持有 | 賣方合計 |
|---|---|---|---|---|---|---|---|---|
| 當期 (0m) | 3 | 9 | 11 | 1 | 1 | 12 | 11 | 2 |
| -1m | 3 | 9 | 11 | 1 | 1 | 12 | 11 | 2 |
| -2m | 3 | 9 | 10 | 1 | 1 | 12 | 10 | 2 |
| -3m | 3 | 10 | 10 | 1 | 1 | 13 | 10 | 2 |

目前分布：**12 買 / 11 持有 / 2 賣**（共 25 家）。

近期變化：過去約 3 個月買方評級由 13 降至 12，持有由 10 升至 11；變化集中在 -3m 至 -2m 之間，近一個月無變動。yf recommendations 端點回傳的是月度彙總，並未提供個別券商的升降評等明細，因此無法列出具體 upgrade / downgrade 事件。

目標價：網路搜尋提到 JPMorgan 在 Confluent 收購案後將目標價調降至 283 美元（Neutral），BMO 亦下修目標價；另有 Citi 於 2025 年量子題材推升時將目標價上調至 375 美元。以上皆為 2026 年上半年的二手報導，日期無法確認為 11 月，請勿當作當前目標價使用。

## Retail social

- Reddit（r/wallstreetbets / r/stocks）：直接抓取失敗，無法取得本日貼文樣本與分數。
- StockTwits：api.stocktwits.com 無法解析，無法取得訊息量與多空標籤。
- X / 新聞鏈：搜尋結果顯示 2026 年 6 月 IBM 曾出現明顯的散戶追捧，Axios 報導 Reddit WSB 提及量與買入 call 量同步上升，兩日漲幅被形容為近數十年最大之一。ChartExchange 的 Reddit 提及追蹤顯示討論者視 IBM 為較低風險的量子曝險（相對 IONQ、RGTI 等純量子股）。另有 Yahoo 報導指 2 月 AI 顛覆疑慮拋售期間，Reddit 情緒在 48 小時內由極度看多轉為看空。
- 討論量：WSB 提及量 2026 年 6 月出現明顯上升；StockTwits 2025 年 10 月訊息量曾於一週內增加約 715%。本日（11/10）的提及量無法量化，僅能定性判斷為「無法確認」。
- 代表性觀點（二手描述，非原文引述）：Reddit 討論者多將 IBM 視為較低風險的量子曝險，因其已有企業客戶基礎，相較之下小型量子新創較難取得開發資金。
- 主要主題：
  1. 量子運算題材（$10B 量子投資計畫、Quantum Foundry、政府補助）
  2. Confluent 收購與 AI 資料串流定位
  3. AI 顛覆疑慮（2 月拋售）與估值爭議
  4. 與純量子股（IONQ、RGTI、QBTS、QUBT）的相對風險比較

散戶傾向（保守判讀）：歷史上偏多，題材導向；但缺乏 11 月的直接樣本，**無法確認當前傾向**。

## Insider activity

查詢區間：2026-05-10 至 2026-11-10（6 個月）。

單位：USD M（百萬美元）

| 日期 | 內部人 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-08-26 | THOMAS ROBERT DAVID | Officer | 賣出 @230.32 | 25,000 | 5.76 |
| 2026-07-01 | ROBINSON ANNE | Officer | 無金額欄位（性質未明） | 7,295 | 空值 |
| 2026-06-04 | FEHRING NICOLAS A. | Officer | 贈與 | 400 | 0 |

Net 6mo：**買入 0 USD M ／ 賣出 5.76 USD M**（僅計公開市場明確標示的賣出；空值項目未計入）。

Notable：
- THOMAS ROBERT DAVID（Officer）於 8/26 以約 230 美元賣出 25,000 股，為本區間唯一有金額之公開市場交易，淨賣出約 5.76 USD M。
- 本區間內無 CEO（KRISHNA ARVIND）或 CFO（KAVANAUGH JAMES J.）之公開市場買賣紀錄。
- 背景對照（6 個月前）：2026 年 2 月董事 MIEBACH MICHAEL 買入 434 股（約 0.10 USD M）、HOWARD MICHELLE J. 買入 50 股（約 0.01 USD M）；1 月底董事 FARR DAVID N 買入 1,000 股於 304 美元（約 0.30 USD M）。2026 年 2 月後股價明顯低於 1 月買價。
- 2026 年 1 月底與 2 月的大量紀錄多為 RSU / 績效股授予（Stock Award，價格 0），屬薪酬機制，不代表市場買進。

解讀注意：內部人買入以董事為主且金額小；唯一的大額賣出來自非 CEO / CFO 的 Officer，樣本少，信號偏弱。

## Ownership shifts

- 機構持股比例：66.18%（institutionsPercentHeld），機構家數 4,340。
- 內部人持股比例：0.105%。
- 歷史趨勢：yf major_holders 僅回傳單一時點快照，無法判斷機構集中度的季度變化方向。機構持股比例屬高位且穩定，但趨勢需另行確認。

## Net sentiment score

- **分析師面：中性偏多**（12 買 / 11 持有 / 2 賣；近 3 個月買方略降，持有略升；無近一月變化）。
- **內部人面：中性偏空（信號弱）**（6 個月僅一筆 5.76 USD M 公開市場賣出，無 CEO / CFO 交易，董事 2 月小額買入為舊資料）。
- **散戶面：無法可靠判定**（Reddit / StockTwits 皆無法取得；二手資料顯示 2026 年 6 月前後偏多且高波動，缺乏 11 月樣本）。
- **機構面：持股比例高，趨勢不明**。

綜合評分：**中性（Neutral）**，信心：**低**（主因是散戶面資料缺失，且內部人與分析師面訊號不一致）。

Divergence flag：**無法判定（資料不足）**。若以可得資料粗估，分析師傾向為中性偏多，內部人為偏空（但樣本少），兩者方向不完全相反；散戶面因缺乏當期樣本，無法與分析師傾向比較。待 Reddit / StockTwits 放行或取得 11 月資料後再重新評估。

資料來源（僅作為記錄）：
- yf recommendations / rec_summary / insider / major_holders（pipeline/tools/yf）
- Reddit 與 StockTwits 直接抓取失敗（Reddit 連線失敗；api.stocktwits.com DNS 無法解析）
- 網路搜尋（二手，日期多為 2026 年上半年至 6 月）

SENTIMENT REPORT COMPLETE
