# Sentiment — CCXI as of 2026-10-19

> **標的識別警示**：任務指定的 CCXI 原設定為 Chimerix，但經查證 CCXI 目前實為 **Churchill Capital Corp XI**（Nasdaq SPAC，擬與 Agility Robotics 合併）。Chimerix 股票代號為 CMRX，已於 2025 年被 Jazz Pharmaceuticals 收購（每股 $8.55，約 $935M），不應再視為獨立交易標的。本報告所有分析皆以 CCXI（Churchill Capital Corp XI / 擬合併後之 AGLT）為對象。`yf` 工具對 CCXI 回傳的內部人交易與機構資料，明顯來自 Chimerix 歷史（Schall、Kanaya、Cappel 等人 2020–2022 年交易紀錄），與 CCXI 無關，已排除於結論之外。

## Analyst consensus
`yf` 工具對 CCXI 的 `recommendations` 與 `rec_summary` 皆回傳空值；對 CMRX 則因 Yahoo 連線 403 失敗。

WebSearch 結果顯示 CCXI 幾乎無分析師覆蓋：Stockanalysis 顯示 Analysts n/a、Price Target n/a；Intellectia 顯示 0 Buy / 0 Hold / 0 Sell。Quantisnow 一頁列出的目標價 $3100–$3800 明顯為資料錯誤，已排除。

**統計：0 buy / 0 hold / 0 sell（無覆蓋，資料可信度低）**

Recent moves：無分析師評級變動或目標價調整可查證。

## Retail social
- **Reddit（r/wallstreetbets、r/stocks）**：WebSearch 以 CCXI、Churchill Capital XI、Agility Robotics 等關鍵字查詢，未取得任何 CCXI 相關 Reddit 討論串。無法判定 tilt。依任務指示未使用 WebFetch 直接抓取 Reddit JSON。
- **StockTwits / X**：StockTwits 的 CCXI 新聞頁存在，但搜尋結果中未顯示 bullish/bearish 比例或訊息量。CCXIW（認股權證）頁面的 sentiment 欄位為 N/A。X 端未查得可用貼文。
- **聲量（buzz volume）**：無法量化；未見與 Chimerix 時期相比的基準。
- **Retail tilt**：無法判定（資料不足）。

### 媒體與評論面（可作為情緒代理，非散戶貼文）
- **多方論點**：Digit v5 機型有 $300M 以上多年期訂單；Amazon 測試 Digit；Toyota 近期簽署商業合作；Seeking Alpha 評論將 AGLT 列為長期投資的投機性 buy。
- **空方論點**：2025 年營收約 $1.8M、虧損約 $140M（引自 Motley Fool 並經台灣媒體轉述）；高現金消耗與潛在稀釋；2021 年 SPAC 熱潮的失敗前例；商業部署機器人數量不到 100 台。
- **Themes**：估值是否合理（$2.5B pre-money）、人形機器人題材熱度、SPAC 結構風險、Unitree 上市後的估值參照（首日收盤較發行價高 460%）。

### 價格與事件脈絡
- 2026-07-10 收盤約 $15.55；52 週區間 $10.07–$19.69。
- 2026-10-09 約 $10.93。
- 2026-10-13 收盤 $11.16（+3.53%），較 7 月初下跌逾 40%。
- 2026-10-13：S-4 註冊聲明書獲 SEC 宣告生效。
- 2026-11-02：Churchill XI 股東特別大會（EGM）投票，合併後預計於 Nasdaq 以 AGLT 掛牌。
- 交易規模：Agility 估值約 $2.5B（pre-money）。

## Insider activity
Net 6mo：**無資料**。`yf` 的 `insider` 回傳之交易紀錄均為 2020–2022 年、Chimerix 相關人員（CEO Thomas Schall、CFO Susan Kanaya、Officer Markus Cappel、Director James Tyree 等），與 CCXI 無關，已排除。CCXI 為 SPAC，2026 年內部人（sponsor）交易未在可得資料中出現。

## Ownership shifts
`yf major_holders` 回傳 insidersPercentHeld 6.325%、institutionsPercentHeld 69.03%、institutionsCount 79。**此組資料是否屬於 CCXI 未經證實**，且無時間戳，不具趨勢判讀價值。機構持股比例變化：無法判定。

## Net sentiment score
- **Composite：Neutral（信心：低）**
  - 分析師面：無覆蓋，無法給出 tilt。
  - 散戶面：無可查 Reddit / StockTwits 數據，無法判定。
  - 媒體面：多空論點並陳，偏向對估值與現金消耗的擔憂，但有具體客戶訂單與合作案支撐。
  - 價格面：2026-07 以來下跌逾 40%，賣壓或已反映部分擔憂，但樣本僅數週。
- **Divergence flag：無法判定**。缺乏分析師 tilt 可與散戶 tilt 比對。

## 資料限制與後續建議
1. CCXI 的 `yf` 資料源有誤（回傳 Chimerix 歷史），本次 analyst / insider 欄位實質為空。建議修正 ticker 對應後重跑。
2. Reddit 與 StockTwits 在 WebSearch 下無法取得即時貼文，散戶情緒為資料缺口。建議在可直接存取 Reddit JSON 的環境補抓 r/wallstreetbets、r/stocks 中 "CCXI"、"Churchill Capital" 與 "Agility" 的近 30 日貼文。
3. 2026-10-19 之後的資料未納入。S-4 生效與 EGM 日期為 2026-10-13 之前已公告事項。
4. 本報告不含交易建議。

SENTIMENT REPORT COMPLETE
