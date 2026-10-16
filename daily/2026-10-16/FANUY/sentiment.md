# Sentiment — FANUY as of 2026-10-16

## 資料來源狀態
- pipeline/tools/yf 可用指令為 recommendations / rec_summary / insider / major_holders / inst_holders。原任務指定的 `ratings` 與 `holders` 不是有效指令，已改用上述指令。
- Yahoo cookie/crumb 取得失敗，全部回退至 repo cache（符合預期）。
- Reddit（r/wallstreetbets、r/stocks）與 StockTwits 依指示視為封鎖，未取得資料。Retail social 部分為 DATA_UNAVAILABLE。
- insider 指令回傳空陣列 []。這代表「無資料」，不能推論為「過去 6 個月無內部人交易」，因此內部人部分視為 DATA_UNAVAILABLE。

## Analyst consensus
rec_summary 與 recommendations（cache）一致：目前 2 位分析師，0 strongBuy / 0 buy / 2 hold / 0 sell / 0 strongSell。
- **BUY 比例：0%（0 / 2）**。覆蓋樣本極小，統計意義有限。
- 近期升降評：cache 中未見新的 upgrade 或 downgrade，上月與本月分布相同（皆為 2 hold）。目標價變動：DATA_UNAVAILABLE。
- 外部次要來源（WebSearch，Pluang 轉述）提到 2026-10-08 有一則 Seeking Alpha「Buy」評等，理由為 Factory Automation 成長與北美 Robot 業務年增 21%。此說法與 Yahoo 類 cache 的 0 buy 相衝突，且無法從一手來源驗證，因此未納入計算，僅作為待確認事項。
- Investing.com 技術面訊號為「Strong Sell」，但其資料時點為 2026-08-21，已過時，僅供參考。

## Retail social
- Reddit：DATA_UNAVAILABLE（沙箱封鎖）。
- StockTwits：DATA_UNAVAILABLE（沙箱封鎖）。
- X / 新聞輿情（WebSearch，僅 standard 搜尋）：未找到 FANUY 專屬的 Reddit 或 StockTwits 討論。一篇 2026-02 Seeking Alpha 標題認為機器人訂單改善與美國回流需求推動 ADR 上漲（偏多）。另一篇較早的 Seeking Alpha 文章認為此股波動過大、不適合個人投資（偏空）。兩者皆非近期 retail 情緒的直接證據。
- 量能：無法量化相對於基準的提及次數。定性判斷為低知名度標的（OTC ADR，FANUY 非散戶熱門股）。
- 主題（僅依新聞推測，非 retail 直接證據）：工業自動化訂單回升、美國 reshoring 題材、日本工具機訂單、ADR 波動性。

## Insider activity
Net 6mo：DATA_UNAVAILABLE（insider 回傳空陣列，無法判定買賣方向與金額）。
- 未能辨識 CEO / CFO 或其他內部人是否有交易。

## Ownership shifts（inst_holders / major_holders）
- major_holders：insidersPercentHeld = 0.0；institutionsPercentHeld = 0.00229（即約 0.23%）；institutionsCount = 27。0.23% 的機構持股比例對 Fanuc 偏低，疑為 ADR 資料結構或單位問題，請勿直接採用。
- inst_holders（最新季 2026-06-30，另 1 筆為 2026-09-30）前幾大持有人：
  - Aristotle Capital Management：3,559,342 股，QoQ -5.83%（為主要持有人，佔列表股數大部分）
  - Sterling Capital：13,380 股，-69.7%
  - Rhumbline Advisers：47,612 股，+10.6%
  - Hantz Financial：82,507 股，-9.6%
  - Front Row Advisors：6,985 股，+18.4%
  - Sankala Group：37,850 股，+100%（可能由極小基數變動，需確認）
  - Gamma Investing（2026-09-30）：10,734 股，+12.3%
- 依上列粗估，合計約淨減 0.23M 股，主要來自 Aristotle 減持。機構流向：**整體偏淨減碼（mixed，偏空）**，但樣本僅列出前幾大持有人，且日期不一致（06-30 與 09-30），信心低。

## 淨情緒評分
- 綜合：**中性（neutral），信心低**。
  - 分析師面：偏弱（0% BUY，2 位皆 hold，無升評）。
  - 機構流向：偏淨減碼（Aristotle 主導）。
  - 內部人：無資料。
  - Retail 面：無資料。
- 分歧旗標（divergence flag）：**無法判定**。因 retail 資料缺失，無法比較 retail 與分析師方向是否相反。若採用外部 Seeking Alpha Buy 說法，會出現分析師內部分歧，但未經驗證。

## 待確認 / 資料品質
1. Seeking Alpha 2026-10-08 Buy 評等與 Yahoo 類 cache 的 0 BUY 相衝突，需一手來源確認。
2. insidersPercentHeld = 0 與 institutionsPercentHeld = 0.23% 疑為資料結構問題。
3. 2026-10-22 Q 業績為未來事件（晚於 DATE），僅列為即將到來的催化劑，不納入當下判斷。
4. 價格相關資料（如 2026-08-21 的 19.02 USD，或 MarketBeat 9/4 的 FANUF 報價）皆過時，未作為當下情緒依據。

## 摘要
- **Analyst consensus % BUY：0%**（0 buy / 2 hold / 0 sell，樣本 2 人）。
- **機構流向方向：淨減碼（偏空，信心低）**，主要由 Aristotle Capital 減持 -5.8% 主導。

SENTIMENT REPORT COMPLETE
