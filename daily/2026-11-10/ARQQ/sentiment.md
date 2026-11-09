# Sentiment — ARQQ as of 2026-11-10

資料可用性總覽：analyst 評級（yf recommendations / rec_summary）回傳空值；Reddit（r/wallstreetbets、r/stocks）經 proxy 回 403；StockTwits DNS 無法解析；X/新聞搜尋僅得 2025 至 2026 年初的舊資料。因此本報告的可靠資料只有內部人交易與機構持股快照，其餘部分標註為「無法取得」，不以推測填補。

## Analyst consensus
無法取得。yf `recommendations` 與 `rec_summary` 皆因 Yahoo cookie/crumb 連線失敗而回傳空陣列，重試後結果相同，故無 buy / hold / sell 分布、無近期 upgrade / downgrade、無目標價變動資料。

唯一可見的分析師數字來自 Benzinga 頁面（無日期標記）：單一分析師、平均目標價 $60。來源日期不明，且單一分析師不足以代表共識，本報告不採用。

## Retail social
- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 public JSON 皆被 proxy 擋下（403），無法計算近期提及數、無法判斷 tilt。
- StockTwits / X：StockTwits 主機無法解析，無資料。X 與新聞搜尋未找到 2026-11 的討論；可見文章多為 2025 年或 2026 年 4 月的舊資料，不能代表當前情緒。
  - 2025 年底一篇 Seeking Alpha 文章（標題為 Arqit Hasn't Earned The Benefit Of The Doubt, Yet）立場偏空，認為年初至當時已跌逾 23% 且仍有下行空間。此為舊資料，只反映當時立場。
- 聲量（buzz volume）：無法量化，與典型水準的比較也無從判斷。
- Themes：無可靠主題可列。依搜尋結果，2026 年春季的股價波動多被描述為受量子與資安板塊帶動，而非公司個股事件；此點來自聚合網站，可信度低。

## Insider activity
Window：2026-05-10 至 2026-11-10（6 個月）。以下數字依 yf insider 原始資料，單位 USD M（百萬美元）。

| 類別 | 筆數（約） | 金額 USD M | 說明 |
|---|---|---|---|
| 公開市場買進（有成交價） | 0 | 0 | 無 |
| 公開市場賣出（有成交價，直接持有） | 26 | 約 1.04 | 主要為 CEO、General Counsel、COO、CFO 與多名董事 |
| 賣出（間接持有，董事 Lefebvre D'Ovidio 相關實體，2026-07-01，54,444 股，$30.07–30.24） | 1 | 1.64 | 單筆最大 |
| 衍生性證券轉換（exercise at $2.50） | 3 | 不計入賣出 | 2026-06-03 Calabria 12 萬股、2026-06-05 Ritchie 約 7.4 萬股、2026-09-22 Lefebvre 460 萬股（間接） |
| 無成交價的制度性股份分配 | 多筆 | 不計 | 各董事與高管於 10/01–10/16 等日期有相似股數重複出現，形態較像獎酬或稅務相關分配，資料未標明交易代碼，無法確認 |

合計：6 個月內淨賣出約 USD 2.68 M，無淨買進。扣除單筆 Lefebvre 間接持有賣出後，直接持有人的賣出約 USD 1.04 M。

Notable：
- CEO Andrew Leaver：2026-07-02 以 $25.20 賣出 9,893 股（約 USD 0.25 M）；2026-10-02、10-05、10-06 分別以 $24.47、$23.78、$24.19 賣出，合計約 USD 0.19 M；2026-10-13 以 $16.40 再賣出 2,573 股（約 USD 0.04 M）。
- 10 月 2 日至 6 日，多名高管（General Counsel Willcocks、Officer Feenan、Officer Nilan、COO Wilder、董事 Ritchie）出現幾乎相同的每日賣出節奏，形態與計畫性出售一致，但資料未標示 10b5-1 計畫，此推測無法證實。
- 成交價軌跡：2026-04 約 $13.3；2026-07 約 $25；2026-10-02 至 10-06 約 $24；2026-10-13 約 $16.4。內部人成交價在一週內由約 $24 降至 $16.4，這是 insider 資料本身顯示的價格變化，本報告不以此作為當前股價依據。
- 最後一筆有成交價的交易為 2026-10-13，之後至 11-10 無公開記錄的 insider 交易。

## Ownership shifts
- 機構持股比例 82.2%（institutionsPercentHeld），float 內比例 84.9%，機構數 93 家。
- 內部人持股 3.1%。
- 僅有單一時點快照，無法判斷機構集中度的時間趨勢。

## Net sentiment score
Composite：**bearish 偏弱（low confidence）**

- 依據僅來自內部人交易：6 個月內無公開市場買進，直接持有人與一筆大額間接持有賣出合計約 USD 2.68 M，屬淨賣出。但部分賣出形態可能屬計畫性或稅務相關，故不宜直接解讀為看空訊號。
- 分析師與散戶兩側皆無可靠資料，無法做加權綜合評分。
- 機構持股高（82%）可視為中性偏穩定的背景，但無趨勢資料，不加分或減分。

Divergence flag：**無法判定**。缺乏可靠的 analyst 傾向與散戶傾向，無法判斷兩者是否相反。若日後補齊 analyst 評級與 Reddit / StockTwits 資料，應優先檢查此點。

資料缺口與後續補齊建議：
1. yf 的 Yahoo cookie/crumb 連線恢復後，重新抓取 `recommendations` 與 `rec_summary`。
2. 允許 api.stocktwits.com 與 reddit.com 的存取，或由其他來源取得 r/wallstreetbets 與 r/stocks 的 2026-11 討論。
3. 以 Form 4 原始申報確認 2026-10 的高管賣出是否屬 10b5-1 計畫，以及制度性股份分配的交易代碼。

SENTIMENT REPORT COMPLETE
