# Sentiment — BE (Bloom Energy) as of 2026-11-23

**狀態摘要**：分析師與內部人資料已取得（資料來自 repo cache，`_refreshed_at` 為 2026-11-22 14:30 UTC，因 Yahoo live 連線失敗）。Reddit 與 StockTwits 無法取得，散戶面只能靠 WebSearch 間接推論，散戶傾向屬於資料缺口。

## Analyst consensus

目前 29 位分析師：6 strong buy / 11 buy / 11 hold / 1 sell / 0 strong sell。買方合計 17 位（約 59%），持有 11 位（約 38%），賣方 1 位（約 3%）。

近三個月的變化：
- -3m、-2m、-1m 的分布皆為 5 / 10 / 12 / 1 / 1（共 29 位）。
- 0m（本月）相較 -1m，strong buy +1、buy +1、hold -1、strong sell -1，屬於小幅偏多調整。
- 工具只回傳家數，沒有具名評等變動與目標價變動。

網路新聞可見的個別動作（日期多不明確，需以券商原文確認）：
- BMO 由偏空轉為升評（報導時點與 Anthropic IPO 同日）。
- Jefferies 將目標價下調至 $242，維持 Hold。
- Morningstar 維持 "Extreme Uncertainty" 評等，目標價 $102，理由是股價過度反映樂觀預期。
- BofA 維持 Underperform、目標價上調至 $39，但該筆紀錄為 2025-11-25，已過時，不應採信為現行評等。
- Benzinga 共識列為 Hold，Webull 列為 Moderate Buy、平均目標價約 $267.46（發布時點不明）。

結論：分析師整體偏多，但共識分歧大，部分機構持續強調估值風險。

## Retail social

- **Reddit (r/wallstreetbets, r/stocks)**：無法取得。WebFetch 回傳無法連到 reddit.com，判定為 soft-fail，未納入評分。
- **StockTwits**：無法取得。api.stocktwits.com 解析失敗（需在 session 網路設定中允許該網域）。網路上 StockTwits 相關報導提到散戶情緒「在極度看空與極度看多之間擺盪」，但時間點不明，不足以量化。
- **X / 新聞聲量**：以 WebSearch 代替。有 Q3 財報超預期、Nebius 與 CoreWeave 大型專案、約 $5.8B 供應承諾至 2029 年等正面報導；也有現金流為負、AI 資本支出疑慮、股價大跌等負面報導。
- **聲量與傾向**：無法量化提及次數，相對於常態的聲量判斷為未知。傾向上無法確認，不宜以新聞代替散戶傾向。
- **主要題材**（依新聞出現頻率排序）：
  1. 現金流與估值（負自由現金流、Morningstar 估值警告）。
  2. AI 資料中心需求（CoreWeave、Nebius、Anthropic 相關題材）。
  3. 股價回檔與波動（AI 基建擔憂、政治面消息造成賣壓）。
  4. 執行力改善（財報超預期、供應承諾大增）。

## Insider activity

以 2026-05-23 至 2026-11-23 為 6 個月窗口，**公開市場買進 0 筆、$0**；**公開市場賣出 17 筆、約 $42.7M**（約 166,114 股）。

| 內部人 | 職稱 | 賣出筆數 | 金額 (USD M) | 備註 |
|---|---|---|---|---|
| CHAMBERS JOHN T | Director（間接持有） | 4 | 25.0 | 最大賣方，含 5/28 約 $16.4M（55,000 股） |
| IMMELT JEFFREY R | Director | 1 | 7.2 | 8/17，30,000 股，約 $238.91 |
| JOSHI AMAN | Officer | 4 | 5.6 | 最近一筆 11/16 約 $178.53 |
| SODERBERG SHAWN MARIE | Officer | 3 | 2.0 | 11/16 有賣出 |
| CHITOORI SATISH PRABHU | COO | 3 | 1.7 | 11/16 有賣出 |
| KURZYMSKI MACIEJ | Officer（2026-03 前為 CFO） | 1 | 0.7 | 6/16 |
| BURGER BARBARA J | Director | 1 | 0.5 | 11/03 |

Notable：
- **CEO SRIDHAR K. R.**：窗口內無公開市場賣出。8/31 有 300,000 股贈與（gift，非市場交易），9/1 有 9,688 股選擇權行使（conversion）。2026-02-24 曾賣出 200,000 股、均價 $170（約 $34M），但不在本窗口內。
- **CFO EDWARDS SIMON STEPHEN**：8/27 有 15,000 股獎勵股（award），非市場買進。
- 董事獎勵（award）如 9/30、6/30、5/21 多筆為例行發放，不計入買賣淨額。
- 價格參考：11/16 賣出價約 $178–179，8/17 約 $239，7/1 約 $300，因此近期股價較夏季高點明顯下跌。
- 機構持股中內部人占比約 5.5%。

淨額：約 **-$42.7M（淨賣出）**，無公開市場買進。賣出集中於 8 月與 5 月，11 月仍有賣出。

## Ownership shifts

- 機構持股占比約 81.7%（流通股占比約 86.4%），機構數 1,865 家。
- 2026-09-30 季報前十大機構中，**9 家季增加碼、1 家減碼**：
  - 增加：FMR +103%、State Street +96%、Geode +86%、Vanguard Capital +55%、BlackRock +33%。
  - 減碼：JPMorgan -34%。
- 前三大：BlackRock 約 8.3%、Vanguard Capital 約 6.4%、Ameriprise 約 6.2%。
- 整體呈現機構集中度上升，但多數增持來自被動與指數型資金，主動基金的訊號有限。

## Net sentiment score

**綜合：中性（信心度：低）**，偏多的分析師共識與偏空的內部人賣出相互抵消，散戶面無資料。

- 分析師面：偏多（17 買 / 11 持有 / 1 賣，近期小幅升級）。
- 內部人面：偏空（6 個月淨賣出約 $42.7M，零公開市場買進）。
- 散戶面：無法判定（Reddit / StockTwits 皆失敗）。
- 機構面：偏多（前十大多數季增）。

**分歧旗標：是**。分析師整體偏多，但內部人持續賣出，且 Morningstar 等估值派明確偏空，分歧方向相反。散戶傾向因資料不足，無法判定是否與分析師相反，需補抓後再確認。

資料限制：
- 分析師與內部人資料來自 repo cache（2026-11-22 更新），非即時資料。
- 新聞來源的日期多不明確，不作為量化依據。
- 散戶面未取得，綜合評分的信心度因此下修。

SENTIMENT REPORT COMPLETE
