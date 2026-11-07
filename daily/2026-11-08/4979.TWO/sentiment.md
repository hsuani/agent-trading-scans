# Sentiment — 4979.TWO (華星光) as of 2026-11-08

資料完整度: 低。Reddit、StockTwits 無法取得，分析師資料為快取且樣本極少，內部人交易資料為空。下列結論信心偏低，應視為參考。

## Analyst consensus
2 buy / 0 hold / 0 sell (含 1 筆 strongBuy)。樣本只有 2 家券商，覆蓋度薄，不足以代表市場共識。

Recent moves: yf 的 recommendations 只回傳 0m 與 -1m 兩期，且兩期內容相同（1 strongBuy + 1 buy），未顯示任何評等調整、目標價變動的歷史紀錄。現有資料無法確認 2026 年內是否有升降評。

媒體引述的券商觀點（非 yf 來源，時間不一、需留意）:
- 2024 年 9 月一家券商將評等調為「降低持股」，目標價 98 元。此為舊資料，與目前股價差距極大，參考價值低。
- 2024 年一份研究報告評等「增加持股」，目標價 210 元，同樣已過時。
- 2026 年 9 月優分析報導引述法人預估 2026 年營收年增約 38%、2027 年年增約 98%。這是媒體轉述的預估，未確認為正式目標價更新。

## Retail social
- Reddit: 無法取得。r/stocks 查詢回傳 "unable to fetch"，r/wallstreetbets 未嘗試（同一主機限制）。無法判斷散戶 tilt。
- StockTwits / X: StockTwits 主機 api.stocktwits.com 無法解析（DNS 失敗），需在 session 網路設定中允許該網域後才能重試。X 端以 WebSearch 查詢，未找到 2026 年 11 月的散戶貼文。
- PTT / Dcard: WebSearch 未找到相關股版討論串，只回傳新聞與研究報告。
- Buzz volume: 無法量化。以搜尋結果看，媒體報導頻率在 2026 年 8 至 9 月明顯高於 2026 年 7 月，但這不等於散戶討論量。
- Tilt: 無法判定（無散戶樣本）。

Themes (取自媒體與法人報導，不是散戶原文):
1. 800G 進入量產與放量: 2026 年 8 月法說會表示 800G 今年起批量出貨，1.6T 小量出貨、目標 2027 年下半年量產。
2. 800G ZR 長距離模組: 2026 年 9 月報導稱第三季量產放量，單價為 400G 的數倍。
3. CW Laser / CPO: 媒體稱 CW Laser 出貨成長快，CPO 被視為下一階段題材。
4. 上游磷化銦（InP）基板短缺: 有投顧認為缺口可能延續到 2028 年。
5. Google TPU 供應鏈傳聞: 部落格與文章提及，未經公司證實，應視為傳聞。
6. 毛利率波動: 2026 年第二季毛利率因財稅認列時間差與庫存跌價損失季減，市場預估 7 月已回升至約 34%。
7. 估值與殖利率: 近五年平均現金殖利率約 0.55%，偏低，股價在媒體資料中區間大幅波動。

Sample (媒體標題，非散戶): 「光通訊持續蓬勃發展」（CMoney 投資快訊，日期不明）。

## Insider activity
Net 6mo: 無資料。yf insider 回傳空陣列，無法確認是「無交易」或「資料未取得」。台股董監持股變動應以公開資訊觀測站（MOPS）為準，本次未存取。

Notable: 無可引用的 CEO / CFO / 其他董監交易紀錄。

## Ownership shifts
- 內部人持股比例: 約 12.0%（yf insidersPercentHeld）
- 法人持股比例: 約 24.1%（yf institutionsPercentHeld），流通股中法人占比約 27.3%
- 法人家數: 35 家（yf institutionsCount）
- 趨勢: 無歷史序列，無法判斷增減。

## Price and fundamentals reference (for context, 非 sentiment 核心)
資料來源不一致，價格序列未能對齊，以下僅供參考:
- 2026 年 2 月收盤約 338.5 元（stockfeel）
- 2026 年 7 月 21 日約 345.5 元（MoneyLink）
- 2026 年 9 月參考價約 611 元，近一周均價約 554 元，近一年均價約 404 元（網路整理資料）
- 11 月份股價: 未取得

營收（億 TWD）:
| 期間 | 合併營收（億 TWD） | 備註 |
|---|---|---|
| 2025 全年 | 43.85 | 年增約 27%（stockfeel 彙整） |
| 2026 Q2 | 12.89 | 季增 8.0%、年增 18.5% |

EPS 驗算: 2026 Q2 稅後純益 1.84 億 TWD ÷ EPS 1.29 元 ≈ 1.43 億股。以此推估，參考價 345 元對應市值約 49 億 TWD，611 元約 87 億 TWD。股數為由 EPS 反推，未以公司正式股本核對。

## Net sentiment score
Composite: 偏多（bullish lean），信心 低。

依據:
- 分析師: 2 buy / 0 sell，偏多，但樣本只有 2 家且無近期變動紀錄，權重低。
- 散戶: 無資料，無法計入。
- 媒體與法人敘事: 偏樂觀（800G 放量、法說會正面），但多為公司自述或推廣性質，未扣除。
- 內部人: 無資料，不計入。

Divergence flag: 無法判定。散戶 tilt 缺失，因此無法確認是否與分析師方向相反。

後續補強建議:
1. 允許 api.stocktwits.com 網域後重試 StockTwits。
2. 以 MOPS 查詢董監事持股申報，補足 Insider 欄位。
3. 取得 2026 年 11 月實際股價與近期券商評等，修正價格與目標價序列。
4. 重試 Reddit 或改用可存取的股版來源（PTT Stock），補足散戶 tilt。

SENTIMENT REPORT COMPLETE
